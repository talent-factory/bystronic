#!/usr/bin/env python3
"""
NumPy Advanced: Enterprise Data Pipeline und Real-time Processing
================================================================

Übung 3: Hochskalierbare Datenpipelines und Echtzeit-Verarbeitung
für industrielle Anwendungen mit NumPy.

Lernziele:
- Enterprise-grade Datenpipelines entwickeln
- Stream Processing für Live-Sensordaten
- Batch Processing für historische Analysen
- Data Quality Management und Validation
- ETL-Pipelines mit NumPy optimieren
- Event-driven Architecture implementieren
- Performance Monitoring und Alerting

Schwierigkeitsgrad: ★★★★★ (Advanced)
Geschätzte Bearbeitungszeit: 120-150 Minuten
"""

import asyncio
import json
import logging
import multiprocessing as mp
import pickle
import queue
import sqlite3
import threading
import time
import warnings
from collections import deque
from collections.abc import Callable
from concurrent.futures import ProcessPoolExecutor
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any

import h5py
import numpy as np

# Unterdrücke Warnungen für bessere Lesbarkeit
warnings.filterwarnings("ignore")

# Logging Setup
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class DataQuality(Enum):
    """Data Quality Levels"""

    EXCELLENT = "excellent"
    GOOD = "good"
    ACCEPTABLE = "acceptable"
    POOR = "poor"
    INVALID = "invalid"


@dataclass
class DataPoint:
    """Einzelner Datenpunkt mit Metadaten"""

    timestamp: datetime
    value: np.ndarray
    sensor_id: str
    quality: DataQuality = DataQuality.GOOD
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp.isoformat(),
            "value": (
                self.value.tolist()
                if isinstance(self.value, np.ndarray)
                else self.value
            ),
            "sensor_id": self.sensor_id,
            "quality": self.quality.value,
            "metadata": self.metadata,
        }


@dataclass
class PipelineMetrics:
    """Pipeline Performance Metriken"""

    processed_records: int = 0
    failed_records: int = 0
    processing_time: float = 0.0
    throughput: float = 0.0
    memory_usage: float = 0.0
    error_rate: float = 0.0

    def update(self, processed: int, failed: int, duration: float):
        self.processed_records += processed
        self.failed_records += failed
        self.processing_time += duration
        total_records = self.processed_records + self.failed_records
        self.throughput = (
            self.processed_records / self.processing_time
            if self.processing_time > 0
            else 0
        )
        self.error_rate = (
            self.failed_records / total_records if total_records > 0 else 0
        )


class DataValidator:
    """Umfassende Datenvalidierung und Quality Assessment"""

    @staticmethod
    def validate_sensor_data(
        data: np.ndarray, bounds: tuple | None = None, max_outliers_pct: float = 0.05
    ) -> dict[str, Any]:
        """
        Validiert Sensordaten auf verschiedene Qualitätskriterien
        """
        validation_result = {
            "is_valid": True,
            "quality_score": 1.0,
            "issues": [],
            "statistics": {},
        }

        # Basis-Statistiken
        if data.size > 0:
            stats = {
                "mean": np.mean(data),
                "std": np.std(data),
                "min": np.min(data),
                "max": np.max(data),
                "count": len(data),
                "null_count": np.sum(np.isnan(data)),
                "null_percentage": np.sum(np.isnan(data)) / len(data) * 100,
            }
            validation_result["statistics"] = stats

            # Check für NaN/Inf Werte
            if np.any(np.isnan(data)) or np.any(np.isinf(data)):
                validation_result["issues"].append("Enthält NaN oder Inf Werte")
                validation_result["quality_score"] *= 0.7

            # Bounds-Check
            if bounds:
                min_bound, max_bound = bounds
                out_of_bounds = np.sum((data < min_bound) | (data > max_bound))
                if out_of_bounds > 0:
                    validation_result["issues"].append(
                        f"{out_of_bounds} Werte außerhalb der Grenzen"
                    )
                    validation_result["quality_score"] *= 1 - out_of_bounds / len(data)

            # Outlier Detection (Z-Score)
            if len(data) > 3:
                z_scores = np.abs((data - np.mean(data)) / np.std(data))
                outliers = np.sum(z_scores > 3)
                outlier_pct = outliers / len(data)

                if outlier_pct > max_outliers_pct:
                    validation_result["issues"].append(
                        f"Zu viele Ausreißer: {outlier_pct:.2%}"
                    )
                    validation_result["quality_score"] *= 0.8

            # Constant Values Check
            if np.std(data) < 1e-10:
                validation_result["issues"].append("Daten sind konstant")
                validation_result["quality_score"] *= 0.5

        else:
            validation_result["issues"].append("Keine Daten vorhanden")
            validation_result["is_valid"] = False
            validation_result["quality_score"] = 0.0

        # Finale Bewertung
        if validation_result["quality_score"] < 0.5:
            validation_result["is_valid"] = False

        return validation_result

    @staticmethod
    def assess_data_quality(validation_result: dict) -> DataQuality:
        """Konvertiert Quality Score zu DataQuality Enum"""
        score = validation_result["quality_score"]

        if score >= 0.95:
            return DataQuality.EXCELLENT
        elif score >= 0.85:
            return DataQuality.GOOD
        elif score >= 0.70:
            return DataQuality.ACCEPTABLE
        elif score >= 0.50:
            return DataQuality.POOR
        else:
            return DataQuality.INVALID


class StreamProcessor:
    """High-Performance Stream Processing für Live-Daten"""

    def __init__(self, buffer_size: int = 10000, processing_interval: float = 0.1):
        self.buffer_size = buffer_size
        self.processing_interval = processing_interval
        self.data_buffer = deque(maxlen=buffer_size)
        self.is_running = False
        self.processors: list[Callable] = []
        self.metrics = PipelineMetrics()
        self._lock = threading.Lock()

    def add_processor(self, processor: Callable[[np.ndarray], np.ndarray]):
        """Fügt einen Verarbeitungsschritt hinzu"""
        self.processors.append(processor)

    def ingest_data(self, data_point: DataPoint):
        """Fügt Datenpunkt zum Stream hinzu"""
        with self._lock:
            self.data_buffer.append(data_point)

    def _process_batch(self, batch: list[DataPoint]) -> list[DataPoint]:
        """Verarbeitet einen Batch von Datenpunkten"""
        if not batch:
            return []

        processed_batch = []
        start_time = time.time()
        failed_count = 0

        for data_point in batch:
            try:
                # Validierung
                validation = DataValidator.validate_sensor_data(data_point.value)
                data_point.quality = DataValidator.assess_data_quality(validation)

                # Verarbeitung durch alle Processor
                processed_value = data_point.value
                for processor in self.processors:
                    processed_value = processor(processed_value)

                # Neuer DataPoint mit verarbeiteten Daten
                processed_point = DataPoint(
                    timestamp=data_point.timestamp,
                    value=processed_value,
                    sensor_id=data_point.sensor_id,
                    quality=data_point.quality,
                    metadata={**data_point.metadata, "processed": True},
                )
                processed_batch.append(processed_point)

            except Exception as e:
                logger.error(f"Fehler bei Verarbeitung: {e}")
                failed_count += 1

        # Metriken aktualisieren
        duration = time.time() - start_time
        self.metrics.update(len(processed_batch), failed_count, duration)

        return processed_batch

    async def start_stream_processing(self, output_queue: queue.Queue | None = None):
        """Startet kontinuierliche Stream-Verarbeitung"""
        self.is_running = True
        logger.info("Stream Processing gestartet")

        while self.is_running:
            # Batch aus Buffer extrahieren
            with self._lock:
                batch_size = min(100, len(self.data_buffer))
                batch = [self.data_buffer.popleft() for _ in range(batch_size)]

            if batch:
                processed_batch = self._process_batch(batch)

                # Output an Queue senden
                if output_queue and processed_batch:
                    for item in processed_batch:
                        output_queue.put(item)

                logger.info(
                    f"Verarbeitet: {len(processed_batch)} items, "
                    f"Throughput: {self.metrics.throughput:.1f} items/sec"
                )

            await asyncio.sleep(self.processing_interval)

    def stop(self):
        """Stoppt Stream Processing"""
        self.is_running = False
        logger.info("Stream Processing gestoppt")


class BatchProcessor:
    """Hochperformante Batch-Verarbeitung für historische Daten"""

    def __init__(self, chunk_size: int = 50000, n_workers: int = None):
        self.chunk_size = chunk_size
        self.n_workers = n_workers or mp.cpu_count()
        self.metrics = PipelineMetrics()

    @staticmethod
    def process_chunk(
        chunk_data: np.ndarray, operations: list[str]
    ) -> dict[str, np.ndarray]:
        """Verarbeitet einen Datenblock mit spezifizierten Operationen"""
        results = {"original": chunk_data}

        for operation in operations:
            if operation == "normalize":
                results["normalized"] = (chunk_data - np.mean(chunk_data)) / np.std(
                    chunk_data
                )
            elif operation == "smooth":
                # Gleitender Durchschnitt
                window_size = min(5, len(chunk_data) // 10)
                if window_size > 0:
                    smoothed = np.convolve(
                        chunk_data, np.ones(window_size) / window_size, mode="same"
                    )
                    results["smoothed"] = smoothed
            elif operation == "detrend":
                # Linearen Trend entfernen
                x = np.arange(len(chunk_data))
                coeffs = np.polyfit(x, chunk_data, 1)
                trend = np.polyval(coeffs, x)
                results["detrended"] = chunk_data - trend
            elif operation == "fft":
                # FFT Analyse
                fft_result = np.fft.fft(chunk_data)
                results["fft_magnitude"] = np.abs(fft_result)
                results["fft_phase"] = np.angle(fft_result)

        return results

    def process_large_dataset(
        self, data: np.ndarray, operations: list[str]
    ) -> dict[str, np.ndarray]:
        """Verarbeitet große Datasets parallel"""
        start_time = time.time()

        # Daten in Chunks aufteilen
        chunks = [
            data[i : i + self.chunk_size] for i in range(0, len(data), self.chunk_size)
        ]

        logger.info(f"Verarbeite {len(chunks)} Chunks mit {self.n_workers} Workern")

        # Parallel processing
        with ProcessPoolExecutor(max_workers=self.n_workers) as executor:
            # Jeder Worker verarbeitet mehrere Chunks
            chunk_operations = [(chunk, operations) for chunk in chunks]
            results = list(executor.map(self._process_chunk_wrapper, chunk_operations))

        # Ergebnisse zusammenführen
        combined_results = {}
        for operation in operations + ["original"]:
            combined_data = []
            for chunk_result in results:
                if operation in chunk_result:
                    combined_data.append(chunk_result[operation])

            if combined_data:
                combined_results[operation] = np.concatenate(combined_data)

        # Metriken aktualisieren
        duration = time.time() - start_time
        self.metrics.update(len(data), 0, duration)

        logger.info(f"Batch-Verarbeitung abgeschlossen in {duration:.2f}s")

        return combined_results

    @staticmethod
    def _process_chunk_wrapper(args):
        """Wrapper für multiprocessing"""
        chunk, operations = args
        return BatchProcessor.process_chunk(chunk, operations)


class DataPipeline:
    """Enterprise Data Pipeline mit ETL-Funktionalität"""

    def __init__(self, pipeline_id: str):
        self.pipeline_id = pipeline_id
        self.stages: list[dict[str, Any]] = []
        self.metrics = PipelineMetrics()
        self.error_handlers: dict[str, Callable] = {}

    def add_stage(
        self,
        stage_name: str,
        processor: Callable,
        error_handler: Callable | None = None,
    ):
        """Fügt eine Pipeline-Stage hinzu"""
        self.stages.append(
            {"name": stage_name, "processor": processor, "error_handler": error_handler}
        )

    def execute(self, input_data: list[DataPoint]) -> list[DataPoint]:
        """Führt die komplette Pipeline aus"""
        current_data = input_data
        stage_metrics = {}

        logger.info(
            f"Pipeline {self.pipeline_id} startet mit {len(input_data)} Datenpunkten"
        )

        for i, stage in enumerate(self.stages):
            stage_start = time.time()
            stage_name = stage["name"]

            try:
                logger.info(f"Verarbeite Stage: {stage_name}")

                # Stage ausführen
                current_data = stage["processor"](current_data)

                stage_duration = time.time() - stage_start
                stage_metrics[stage_name] = {
                    "duration": stage_duration,
                    "input_count": len(input_data) if i == 0 else len(current_data),
                    "output_count": len(current_data),
                    "success": True,
                }

                logger.info(
                    f"Stage {stage_name} abgeschlossen: "
                    f"{len(current_data)} Datenpunkte in {stage_duration:.2f}s"
                )

            except Exception as e:
                logger.error(f"Fehler in Stage {stage_name}: {e}")

                # Error Handler ausführen
                if stage["error_handler"]:
                    current_data = stage["error_handler"](current_data, e)
                else:
                    # Default: Stage überspringen
                    pass

                stage_metrics[stage_name] = {
                    "duration": time.time() - stage_start,
                    "error": str(e),
                    "success": False,
                }

        # Pipeline-Metriken aktualisieren
        total_duration = sum(m.get("duration", 0) for m in stage_metrics.values())
        self.metrics.update(
            len(current_data), len(input_data) - len(current_data), total_duration
        )

        return current_data


class DataStorage:
    """Hochperformante Datenspeicherung mit verschiedenen Backends"""

    def __init__(self, storage_type: str = "hdf5", base_path: str = "./data"):
        self.storage_type = storage_type
        self.base_path = Path(base_path)
        self.base_path.mkdir(exist_ok=True)

    @contextmanager
    def get_connection(self, filename: str):
        """Context Manager für Datenbank-Verbindungen"""
        if self.storage_type == "hdf5":
            filepath = self.base_path / f"{filename}.h5"
            conn = h5py.File(filepath, "a")
        elif self.storage_type == "sqlite":
            filepath = self.base_path / f"{filename}.db"
            conn = sqlite3.connect(filepath)
        else:
            raise ValueError(f"Unbekannter Storage-Typ: {self.storage_type}")

        try:
            yield conn
        finally:
            conn.close()

    def store_batch(self, data_points: list[DataPoint], dataset_name: str):
        """Speichert Batch von DataPoints effizient"""
        if not data_points:
            return

        if self.storage_type == "hdf5":
            self._store_hdf5(data_points, dataset_name)
        elif self.storage_type == "sqlite":
            self._store_sqlite(data_points, dataset_name)

    def _store_hdf5(self, data_points: list[DataPoint], dataset_name: str):
        """HDF5 Storage Implementation"""
        with self.get_connection(dataset_name) as h5file:
            # Timestamps als Unix-Timestamp
            timestamps = [dp.timestamp.timestamp() for dp in data_points]

            # Values als 2D Array (falls verschiedene Größen)
            max_size = max(
                len(dp.value) if hasattr(dp.value, "__len__") else 1
                for dp in data_points
            )

            values = np.zeros((len(data_points), max_size))
            sensor_ids = []
            qualities = []

            for i, dp in enumerate(data_points):
                if hasattr(dp.value, "__len__"):
                    values[i, : len(dp.value)] = dp.value
                else:
                    values[i, 0] = dp.value

                sensor_ids.append(dp.sensor_id.encode("utf-8"))
                qualities.append(dp.quality.value.encode("utf-8"))

            # Datasets erstellen/erweitern
            if "timestamps" in h5file:
                # Erweitern existierender Datasets
                old_size = h5file["timestamps"].shape[0]
                h5file["timestamps"].resize((old_size + len(timestamps),))
                h5file["timestamps"][old_size:] = timestamps

                h5file["values"].resize((old_size + len(values), max_size))
                h5file["values"][old_size:] = values

                h5file["sensor_ids"].resize((old_size + len(sensor_ids),))
                h5file["sensor_ids"][old_size:] = sensor_ids

                h5file["qualities"].resize((old_size + len(qualities),))
                h5file["qualities"][old_size:] = qualities
            else:
                # Neue Datasets erstellen
                h5file.create_dataset(
                    "timestamps", data=timestamps, maxshape=(None,), compression="gzip"
                )
                h5file.create_dataset(
                    "values", data=values, maxshape=(None, max_size), compression="gzip"
                )
                h5file.create_dataset(
                    "sensor_ids", data=sensor_ids, maxshape=(None,), compression="gzip"
                )
                h5file.create_dataset(
                    "qualities", data=qualities, maxshape=(None,), compression="gzip"
                )

    def _store_sqlite(self, data_points: list[DataPoint], dataset_name: str):
        """SQLite Storage Implementation"""
        with self.get_connection(dataset_name) as conn:
            cursor = conn.cursor()

            # Tabelle erstellen falls nicht existiert
            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS {dataset_name} (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    value BLOB,
                    sensor_id TEXT,
                    quality TEXT,
                    metadata TEXT
                )
            """
            )

            # Daten einfügen
            for dp in data_points:
                cursor.execute(
                    f"""
                    INSERT INTO {dataset_name}
                    (timestamp, value, sensor_id, quality, metadata)
                    VALUES (?, ?, ?, ?, ?)
                """,
                    (
                        dp.timestamp.timestamp(),
                        pickle.dumps(dp.value),
                        dp.sensor_id,
                        dp.quality.value,
                        json.dumps(dp.metadata),
                    ),
                )

            conn.commit()

    def load_data(
        self,
        dataset_name: str,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
    ) -> list[DataPoint]:
        """Lädt Daten aus Storage"""
        if self.storage_type == "hdf5":
            return self._load_hdf5(dataset_name, start_time, end_time)
        elif self.storage_type == "sqlite":
            return self._load_sqlite(dataset_name, start_time, end_time)

    def _load_hdf5(
        self, dataset_name: str, start_time: datetime = None, end_time: datetime = None
    ) -> list[DataPoint]:
        """HDF5 Load Implementation"""
        try:
            with self.get_connection(dataset_name) as h5file:
                timestamps = h5file["timestamps"][:]
                values = h5file["values"][:]
                sensor_ids = h5file["sensor_ids"][:]
                qualities = h5file["qualities"][:]

                data_points = []
                for i in range(len(timestamps)):
                    timestamp = datetime.fromtimestamp(timestamps[i])

                    # Zeitfilter anwenden
                    if start_time and timestamp < start_time:
                        continue
                    if end_time and timestamp > end_time:
                        continue

                    dp = DataPoint(
                        timestamp=timestamp,
                        value=values[i],
                        sensor_id=sensor_ids[i].decode("utf-8"),
                        quality=DataQuality(qualities[i].decode("utf-8")),
                    )
                    data_points.append(dp)

                return data_points
        except Exception as e:
            logger.error(f"Fehler beim Laden von HDF5: {e}")
            return []


class RealTimeAnalyzer:
    """Real-time Analytics Engine für Live-Dashboards"""

    def __init__(self, window_size: int = 1000):
        self.window_size = window_size
        self.data_windows: dict[str, deque] = {}
        self.analytics_results: dict[str, dict] = {}
        self.alert_thresholds: dict[str, dict] = {}

    def add_sensor(self, sensor_id: str, alert_thresholds: dict[str, float] = None):
        """Fügt Sensor für Real-time Monitoring hinzu"""
        self.data_windows[sensor_id] = deque(maxlen=self.window_size)
        if alert_thresholds:
            self.alert_thresholds[sensor_id] = alert_thresholds

    def update_sensor_data(self, sensor_id: str, value: float):
        """Aktualisiert Sensor-Daten und berechnet Analytics"""
        if sensor_id not in self.data_windows:
            self.add_sensor(sensor_id)

        self.data_windows[sensor_id].append(value)
        self._compute_analytics(sensor_id)
        self._check_alerts(sensor_id)

    def _compute_analytics(self, sensor_id: str):
        """Berechnet Real-time Analytics für Sensor"""
        data = np.array(self.data_windows[sensor_id])

        if len(data) < 10:  # Mindestens 10 Datenpunkte
            return

        analytics = {
            "current": data[-1],
            "mean": np.mean(data),
            "std": np.std(data),
            "min": np.min(data),
            "max": np.max(data),
            "trend": self._calculate_trend(data),
            "anomaly_score": self._calculate_anomaly_score(data),
            "timestamp": datetime.now(),
        }

        self.analytics_results[sensor_id] = analytics

    def _calculate_trend(self, data: np.ndarray) -> float:
        """Berechnet Trend (Steigung der linearen Regression)"""
        if len(data) < 2:
            return 0.0

        x = np.arange(len(data))
        coeffs = np.polyfit(x, data, 1)
        return coeffs[0]  # Steigung

    def _calculate_anomaly_score(self, data: np.ndarray) -> float:
        """Berechnet Anomaly Score für aktuellen Wert"""
        if len(data) < 10:
            return 0.0

        # Z-Score des letzten Wertes
        current = data[-1]
        history = data[:-1]
        z_score = abs((current - np.mean(history)) / np.std(history))

        # Normalisierter Anomaly Score (0-1)
        return min(z_score / 3.0, 1.0)

    def _check_alerts(self, sensor_id: str):
        """Prüft Alert-Bedingungen"""
        if sensor_id not in self.alert_thresholds:
            return

        analytics = self.analytics_results.get(sensor_id, {})
        thresholds = self.alert_thresholds[sensor_id]

        alerts = []

        # Threshold-Checks
        current_value = analytics.get("current", 0)
        if "max_value" in thresholds and current_value > thresholds["max_value"]:
            alerts.append(
                f"Wert {current_value} überschreitet Maximum {thresholds['max_value']}"
            )

        if "min_value" in thresholds and current_value < thresholds["min_value"]:
            alerts.append(
                f"Wert {current_value} unterschreitet Minimum {thresholds['min_value']}"
            )

        # Anomaly-Check
        anomaly_score = analytics.get("anomaly_score", 0)
        if (
            "anomaly_threshold" in thresholds
            and anomaly_score > thresholds["anomaly_threshold"]
        ):
            alerts.append(f"Anomalie erkannt: Score {anomaly_score:.2f}")

        # Trend-Check
        trend = analytics.get("trend", 0)
        if "max_trend" in thresholds and abs(trend) > thresholds["max_trend"]:
            alerts.append(f"Starker Trend erkannt: {trend:.4f}")

        # Alerts loggen
        for alert in alerts:
            logger.warning(f"ALERT [{sensor_id}]: {alert}")


# ================================
# AUFGABEN UND ÜBUNGEN
# ================================


def aufgabe_1_stream_processing():
    """
    Aufgabe 1: Real-time Stream Processing System

    Implementiere ein hochperformantes Stream Processing System für Live-Sensordaten.
    """
    print("=== Aufgabe 1: Stream Processing System ===")

    # TODO: Erstelle einen StreamProcessor mit mehreren Verarbeitungsschritten:
    # 1. Datenvalidierung und Quality Assessment
    # 2. Glättung mit gleitendem Durchschnitt
    # 3. Ausreißererkennung und -korrektur
    # 4. Einheitenkonvertierung

    # TODO: Simuliere Live-Sensordaten:
    # - Mehrere Sensoren gleichzeitig
    # - Verschiedene Samplingraten
    # - Realistische Rauschen und Trends
    # - Gelegentliche Ausreißer und Ausfälle

    # TODO: Implementiere Performance-Monitoring:
    # - Throughput messen (Datenpunkte/Sekunde)
    # - Latenz überwachen
    # - Memory Usage tracking
    # - Error Rate berechnen

    # TODO: Erstelle ein Alert-System:
    # - Konfigurierbare Schwellwerte
    # - Anomalie-basierte Alerts
    # - Trend-basierte Warnungen

    # BONUS: Implementiere Load Balancing für mehrere Worker

    pass


def aufgabe_2_batch_processing():
    """
    Aufgabe 2: Hochskalierbare Batch-Verarbeitung

    Entwickle ein System zur effizienten Verarbeitung großer historischer Datasets.
    """
    print("=== Aufgabe 2: Batch Processing System ===")

    # TODO: Generiere großes Test-Dataset (>1 Million Datenpunkte):
    # - Mehrere Jahre Sensordaten
    # - Verschiedene Qualitätslevel
    # - Realistische zeitliche Muster

    # TODO: Implementiere verschiedene Batch-Operationen:
    # - Statistical Analysis (Min, Max, Mean, Std, Percentiles)
    # - Frequency Domain Analysis (FFT, PSD)
    # - Trend Analysis und Saisonalität
    # - Quality Metrics und Reporting

    # TODO: Optimiere für Performance:
    # - Chunk-basierte Verarbeitung
    # - Parallelisierung mit multiprocessing
    # - Memory-mapped Files für sehr große Daten
    # - Progress Monitoring

    # TODO: Erstelle Performance-Vergleich:
    # - Single-threaded vs Multi-threaded
    # - In-Memory vs Memory-mapped
    # - Verschiedene Chunk-Größen

    # BONUS: Implementiere incremental processing (nur neue Daten)

    pass


def aufgabe_3_etl_pipeline():
    """
    Aufgabe 3: Enterprise ETL-Pipeline

    Baue eine vollständige ETL-Pipeline für Produktionsdaten.
    """
    print("=== Aufgabe 3: ETL-Pipeline ===")

    # TODO: Extract Phase:
    # - Daten aus verschiedenen Quellen (CSV, JSON, Database)
    # - Data Discovery und Schema-Erkennung
    # - Incremental Data Loading
    # - Error Handling für fehlerhafte Quellen

    # TODO: Transform Phase:
    # - Data Cleaning und Validation
    # - Format-Konvertierungen
    # - Aggregationen und Berechnungen
    # - Data Enrichment mit Metadaten

    # TODO: Load Phase:
    # - Optimierte Speicherung in verschiedenen Formaten
    # - Partitionierung für bessere Performance
    # - Indexierung für schnelle Queries
    # - Data Versioning und Lineage

    # TODO: Pipeline-Orchestrierung:
    # - Dependency Management zwischen Stages
    # - Retry-Mechanismen für fehlgeschlagene Jobs
    # - Monitoring und Alerting
    # - Configuration Management

    # BONUS: Implementiere Data Lineage Tracking

    pass


def aufgabe_4_realtime_analytics():
    """
    Aufgabe 4: Real-time Analytics Dashboard

    Entwickle ein System für Live-Analytics und Dashboard-Updates.
    """
    print("=== Aufgabe 4: Real-time Analytics ===")

    # TODO: Real-time Metrics Engine:
    # - Sliding Window Analytics
    # - Complex Event Processing
    # - Multi-sensor Korrelationsanalyse
    # - Adaptive Threshold Learning

    # TODO: Dashboard Data Pipeline:
    # - WebSocket-basierte Updates
    # - Data Aggregation für verschiedene Zeitfenster
    # - KPI-Berechnung in Echtzeit
    # - Historical Context für aktuelle Werte

    # TODO: Advanced Analytics:
    # - Predictive Alerts basierend auf Trends
    # - Multivariate Anomalieerkennung
    # - Pattern Recognition in Zeitreihen
    # - Root Cause Analysis für Anomalien

    # TODO: Performance Optimierung:
    # - Caching-Strategien für häufige Queries
    # - Lazy Evaluation für teure Berechnungen
    # - Compression für historische Daten
    # - Auto-scaling basierend auf Load

    # BONUS: Machine Learning Integration für Predictive Analytics

    pass


def vollstaendige_pipeline_demo():
    """
    Demonstration einer vollständigen Data Pipeline
    """
    print("🏭 Enterprise Data Pipeline Demo")
    print("=" * 50)

    # 1. Datengeneration simulieren
    print("\n1. Generiere Simulationsdaten...")

    # Simuliere Sensordaten über 24 Stunden
    timestamps = [
        datetime.now() - timedelta(hours=24) + timedelta(minutes=i)
        for i in range(0, 24 * 60, 5)
    ]  # Alle 5 Minuten

    sensor_data = []
    for i, ts in enumerate(timestamps):
        # Simuliere Temperatur mit täglichem Zyklus + Rauschen
        base_temp = 20 + 5 * np.sin(2 * np.pi * i / 288)  # 288 = 24h in 5min Schritten
        noise = np.random.normal(0, 0.5)

        # Gelegentliche Ausreißer
        if np.random.random() < 0.02:  # 2% Ausreißer
            noise += np.random.normal(0, 5)

        value = base_temp + noise

        dp = DataPoint(
            timestamp=ts,
            value=np.array([value]),
            sensor_id="TEMP_001",
            metadata={"location": "production_line_1", "unit": "celsius"},
        )
        sensor_data.append(dp)

    print(f"Generiert: {len(sensor_data)} Datenpunkte")

    # 2. Stream Processing Demo
    print("\n2. Stream Processing...")

    stream_processor = StreamProcessor()

    # Glättungsfilter hinzufügen
    def smoothing_filter(data: np.ndarray) -> np.ndarray:
        if len(data) == 1:
            return data
        # Exponentieller gleitender Durchschnitt
        alpha = 0.3
        return np.array([data[0] * alpha + data[0] * (1 - alpha)])

    stream_processor.add_processor(smoothing_filter)

    # Einige Datenpunkte durch Stream Processing
    for dp in sensor_data[:100]:
        stream_processor.ingest_data(dp)

    print(f"Stream Buffer: {len(stream_processor.data_buffer)} Datenpunkte")

    # 3. Batch Processing Demo
    print("\n3. Batch Processing...")

    batch_processor = BatchProcessor(chunk_size=100)

    # Extrahiere Werte für Batch Processing
    values = np.array([dp.value[0] for dp in sensor_data])

    operations = ["normalize", "smooth", "detrend", "fft"]
    batch_results = batch_processor.process_large_dataset(values, operations)

    print("Batch Processing Ergebnisse:")
    for operation, result in batch_results.items():
        if len(result) > 0:
            print(
                f"  {operation}: {len(result)} Werte, "
                f"Range: [{np.min(result):.2f}, {np.max(result):.2f}]"
            )

    # 4. ETL Pipeline Demo
    print("\n4. ETL Pipeline...")

    pipeline = DataPipeline("temperature_processing")

    def validation_stage(data_points: list[DataPoint]) -> list[DataPoint]:
        """Validierungs-Stage"""
        validated = []
        for dp in data_points:
            validation = DataValidator.validate_sensor_data(
                dp.value,
                bounds=(0, 50),  # Realistische Temperaturgrenzen
            )
            dp.quality = DataValidator.assess_data_quality(validation)

            if dp.quality != DataQuality.INVALID:
                validated.append(dp)

        return validated

    def aggregation_stage(data_points: list[DataPoint]) -> list[DataPoint]:
        """Aggregierungs-Stage - Stündliche Mittelwerte"""
        if not data_points:
            return []

        hourly_aggregates = {}

        for dp in data_points:
            hour_key = dp.timestamp.replace(minute=0, second=0, microsecond=0)

            if hour_key not in hourly_aggregates:
                hourly_aggregates[hour_key] = []
            hourly_aggregates[hour_key].append(dp.value[0])

        aggregated = []
        for hour, values in hourly_aggregates.items():
            agg_dp = DataPoint(
                timestamp=hour,
                value=np.array([np.mean(values)]),
                sensor_id="TEMP_001_HOURLY",
                quality=DataQuality.GOOD,
                metadata={"aggregation": "hourly_mean", "count": len(values)},
            )
            aggregated.append(agg_dp)

        return aggregated

    pipeline.add_stage("validation", validation_stage)
    pipeline.add_stage("aggregation", aggregation_stage)

    processed_data = pipeline.execute(sensor_data)
    print(f"Pipeline Output: {len(processed_data)} aggregierte Datenpunkte")

    # 5. Real-time Analytics Demo
    print("\n5. Real-time Analytics...")

    analyzer = RealTimeAnalyzer(window_size=50)
    analyzer.add_sensor(
        "TEMP_001",
        {
            "max_value": 30.0,
            "min_value": 10.0,
            "anomaly_threshold": 0.7,
            "max_trend": 0.1,
        },
    )

    # Simuliere Live-Updates
    for dp in sensor_data[-20:]:  # Letzte 20 Datenpunkte
        analyzer.update_sensor_data("TEMP_001", dp.value[0])

    # Analytics-Ergebnisse anzeigen
    if "TEMP_001" in analyzer.analytics_results:
        analytics = analyzer.analytics_results["TEMP_001"]
        print("Current Analytics:")
        print(f"  Aktueller Wert: {analytics['current']:.2f}°C")
        print(f"  Mittelwert: {analytics['mean']:.2f}°C")
        print(f"  Trend: {analytics['trend']:.4f}°C/min")
        print(f"  Anomaly Score: {analytics['anomaly_score']:.2f}")

    # 6. Data Storage Demo
    print("\n6. Data Storage...")

    storage = DataStorage("hdf5", "./pipeline_demo_data")
    storage.store_batch(processed_data, "temperature_hourly")

    # Daten wieder laden
    loaded_data = storage.load_data("temperature_hourly")
    print(f"Gespeichert und geladen: {len(loaded_data)} Datenpunkte")

    print("\n✅ Vollständige Pipeline Demo abgeschlossen!")


def performance_benchmark_pipelines():
    """
    Performance Benchmark verschiedener Pipeline-Konfigurationen
    """
    print("\n🚀 Pipeline Performance Benchmark")
    print("=" * 45)

    # Test-Daten generieren
    data_sizes = [1000, 5000, 10000, 50000]
    results = {}

    for size in data_sizes:
        print(f"\nBenchmark für {size} Datenpunkte:")

        # Generiere Testdaten
        test_data = []
        for i in range(size):
            dp = DataPoint(
                timestamp=datetime.now() + timedelta(seconds=i),
                value=np.random.normal(20, 2, 1),
                sensor_id="BENCH_SENSOR",
            )
            test_data.append(dp)

        # 1. Stream Processing Benchmark
        start_time = time.time()
        stream_proc = StreamProcessor()
        for dp in test_data:
            stream_proc.ingest_data(dp)
        stream_time = time.time() - start_time

        # 2. Batch Processing Benchmark
        values = np.array([dp.value[0] for dp in test_data])
        batch_proc = BatchProcessor()

        start_time = time.time()
        batch_proc.process_large_dataset(values, ["normalize", "smooth"])
        batch_time = time.time() - start_time

        # 3. ETL Pipeline Benchmark
        pipeline = DataPipeline(f"benchmark_{size}")

        def dummy_stage(data: list[DataPoint]) -> list[DataPoint]:
            # Einfache Verarbeitung für Benchmark
            return [dp for dp in data if dp.value[0] > 15]

        pipeline.add_stage("filter", dummy_stage)

        start_time = time.time()
        pipeline.execute(test_data)
        etl_time = time.time() - start_time

        results[size] = {
            "stream_processing": stream_time,
            "batch_processing": batch_time,
            "etl_pipeline": etl_time,
        }

        print(f"  Stream Processing: {stream_time:.4f}s")
        print(f"  Batch Processing: {batch_time:.4f}s")
        print(f"  ETL Pipeline: {etl_time:.4f}s")

    # Performance Summary
    print("\n📊 Performance Summary:")
    for method in ["stream_processing", "batch_processing", "etl_pipeline"]:
        avg_time = np.mean([results[size][method] for size in data_sizes])
        print(f"{method.replace('_', ' ').title()}: {avg_time:.4f}s durchschnittlich")


if __name__ == "__main__":
    print("🏭 NumPy Advanced: Enterprise Data Pipeline")
    print("=" * 60)
    print("Dieses Modul demonstriert Enterprise-grade Datenpipelines:")
    print("• Stream Processing für Live-Daten")
    print("• Hochskalierbare Batch-Verarbeitung")
    print("• ETL-Pipelines mit Error Handling")
    print("• Real-time Analytics und Monitoring")
    print("• Performance-optimierte Datenspeicherung")
    print("\n" + "=" * 60)

    # Hauptdemo ausführen
    vollstaendige_pipeline_demo()

    # Performance Benchmark
    performance_benchmark_pipelines()

    print("\n✅ Enterprise Data Pipeline Demo abgeschlossen!")
    print("Bearbeite nun die Aufgaben 1-4 für vertieftes Verständnis.")
