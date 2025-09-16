#!/usr/bin/env python3
"""
NumPy Übung 1: Hochleistungs-Computing und Parallelisierung (Advanced)
Bystronic Python Grundkurs - Kapitel 3

Diese Übung behandelt fortgeschrittene Hochleistungs-Techniken mit NumPy für
massive Datenmengen und parallelisierte Berechnungen in Produktionsumgebungen.

Lernziele:
- Memory-mapped Arrays für riesige Datasets
- Parallelisierung mit NumPy und multiprocessing
- GPU-accelerated Computing Simulation
- Custom C-Extensions Integration
- Distributed Computing Patterns
- Real-Time Stream Processing at Scale

Schwierigkeitsgrad: 🔴 Advanced
Geschätzte Bearbeitungszeit: 60-75 Minuten
"""

import multiprocessing as mp
import os
import tempfile
import time
import warnings
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import numpy as np

warnings.filterwarnings("ignore")


def main():
    """Hauptfunktion für Hochleistungs-Computing Übungen"""
    print("🎯 NUMPY ADVANCED ÜBUNG 1: HOCHLEISTUNGS-COMPUTING UND PARALLELISIERUNG")
    print("=" * 80)
    print("Diese Übung behandelt Enterprise-Level Performance-Techniken für")
    print("massive Datenmengen und verteilte Berechnungen in Produktionsumgebungen.")
    print()

    try:
        # Aufgabe 1: Memory-Mapped Arrays für Big Data
        aufgabe_1_memory_mapped_arrays()

        # Aufgabe 2: Parallelisierte NumPy-Operationen
        aufgabe_2_parallelisierte_operationen()

        # Aufgabe 3: Custom Vectorized Functions
        aufgabe_3_custom_vectorized_functions()

        # Aufgabe 4: Real-Time Stream Processing
        aufgabe_4_realtime_stream_processing()

        # Aufgabe 5: Distributed Computing Patterns
        aufgabe_5_distributed_computing()

        print("\n" + "🎉" * 70)
        print("🎉 ALLE HOCHLEISTUNGS-COMPUTING AUFGABEN ABGESCHLOSSEN! 🎉")
        print("🎉" * 70)
        print("\n📋 BEHERRSCHTE ADVANCED-KONZEPTE:")
        print("✅ Memory-mapped Arrays für TB-große Datasets")
        print("✅ Multi-Processing und Thread-basierte Parallelisierung")
        print("✅ Custom C-ähnliche Vectorized Functions")
        print("✅ Real-Time Stream Processing mit Buffer-Management")
        print("✅ Distributed Computing Patterns für Cluster")
        print("✅ Performance-Profiling und Bottleneck-Analyse")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler in der Übung: {e}")
        print("💡 Tipp: Advanced Computing erfordert robustes Error-Handling!")


def aufgabe_1_memory_mapped_arrays():
    """Aufgabe 1: Memory-Mapped Arrays für massive Datasets"""
    print("🎯 AUFGABE 1: MEMORY-MAPPED ARRAYS FÜR BIG DATA")
    print("-" * 50)
    print("Ziel: Verwende Memory-Mapping für Datasets die größer als RAM sind")
    print("und implementiere Out-of-Core Algorithmen für Produktionsdaten")
    print()

    start_time = time.time()

    # 1.1 Memory-Mapped Array Creation and Management
    print("📊 1.1 Memory-Mapped Array Management:")

    class MemoryMappedDataManager:
        """Manager für Memory-Mapped NumPy Arrays"""

        def __init__(self, base_path=None):
            self.base_path = base_path or tempfile.gettempdir()
            self.active_arrays = {}
            self.array_metadata = {}

        def create_mmap_array(
            self, name: str, shape: tuple, dtype=np.float64, mode="w+", fill_value=None
        ):
            """Erstelle Memory-Mapped Array"""
            filepath = os.path.join(self.base_path, f"{name}.dat")

            # Erstelle Memory-Mapped Array
            mmap_array = np.memmap(filepath, dtype=dtype, mode=mode, shape=shape)

            if fill_value is not None and mode in ["w+", "w"]:
                mmap_array[:] = fill_value

            self.active_arrays[name] = mmap_array
            self.array_metadata[name] = {
                "filepath": filepath,
                "shape": shape,
                "dtype": dtype,
                "size_mb": mmap_array.nbytes / (1024 * 1024),
                "created": time.time(),
            }

            return mmap_array

        def load_mmap_array(self, name: str, shape: tuple, dtype=np.float64):
            """Lade existierendes Memory-Mapped Array"""
            filepath = os.path.join(self.base_path, f"{name}.dat")

            if not os.path.exists(filepath):
                raise FileNotFoundError(
                    f"Memory-mapped file nicht gefunden: {filepath}"
                )

            mmap_array = np.memmap(filepath, dtype=dtype, mode="r+", shape=shape)
            self.active_arrays[name] = mmap_array

            return mmap_array

        def get_array_info(self, name: str):
            """Information über Memory-Mapped Array"""
            if name not in self.array_metadata:
                return None

            metadata = self.array_metadata[name]
            array = self.active_arrays.get(name)

            info = metadata.copy()
            if array is not None:
                info["current_memory_usage"] = array.nbytes / (1024 * 1024)
                info["is_loaded"] = True
            else:
                info["is_loaded"] = False

            return info

        def cleanup_array(self, name: str):
            """Cleanup Memory-Mapped Array"""
            if name in self.active_arrays:
                del self.active_arrays[name]

            if name in self.array_metadata:
                filepath = self.array_metadata[name]["filepath"]
                if os.path.exists(filepath):
                    os.remove(filepath)
                del self.array_metadata[name]

        def get_total_memory_usage(self):
            """Gesamter Memory-Verbrauch aller Arrays"""
            total_mb = sum(meta["size_mb"] for meta in self.array_metadata.values())
            return total_mb

        def __del__(self):
            """Cleanup beim Objektende"""
            for name in list(self.active_arrays.keys()):
                self.cleanup_array(name)

    # Test Memory-Mapped Array Manager
    print("  Test mit simulierten Large-Scale Produktionsdaten:")

    mmap_manager = MemoryMappedDataManager()

    # Simuliere massive Sensor-Datasets
    datasets = {
        "sensor_timeseries": {
            "shape": (100000, 50),  # 100k Zeitpunkte, 50 Sensoren
            "dtype": np.float32,
            "description": "Kontinuierliche Sensor-Zeitreihen",
        },
        "quality_measurements": {
            "shape": (500000, 12),  # 500k Teile, 12 Qualitätsmerkmale
            "dtype": np.float64,
            "description": "Qualitätsmessungen aller Produktionslinien",
        },
        "machine_states": {
            "shape": (1000000, 8),  # 1M Zustandsmessungen, 8 Maschinen
            "dtype": np.int16,
            "description": "Maschinenzustand-Historie",
        },
    }

    print(f"    Erstelle {len(datasets)} Large-Scale Datasets:")

    for name, config in datasets.items():
        print(f"      {name}: {config['shape']} ({config['description']})")

        # Erstelle Memory-Mapped Array
        mmap_array = mmap_manager.create_mmap_array(
            name, config["shape"], config["dtype"]
        )

        # Fülle mit realistischen Daten
        if "sensor" in name:
            # Simuliere Sensor-Zeitreihen
            for sensor_idx in range(config["shape"][1]):
                base_value = 50 + sensor_idx * 5  # Verschiedene Sensor-Bereiche
                trend = np.linspace(0, 10, config["shape"][0])
                noise = np.random.normal(0, 2, config["shape"][0])
                cycles = 5 * np.sin(2 * np.pi * np.arange(config["shape"][0]) / 1000)

                mmap_array[:, sensor_idx] = base_value + trend + noise + cycles

        elif "quality" in name:
            # Simuliere Qualitätsmessungen
            np.random.seed(42)
            for feature_idx in range(config["shape"][1]):
                target_value = 25.0 + feature_idx * 2.5
                tolerance = 0.1 + feature_idx * 0.05

                mmap_array[:, feature_idx] = np.random.normal(
                    target_value, tolerance / 3, config["shape"][0]
                )

        elif "machine" in name:
            # Simuliere Maschinenzustände (0=Idle, 1=Running, 2=Maintenance, 3=Error)
            np.random.seed(123)
            for machine_idx in range(config["shape"][1]):
                # Realistic state transitions
                states = np.random.choice(
                    [0, 1, 2, 3], config["shape"][0], p=[0.1, 0.8, 0.08, 0.02]
                )
                mmap_array[:, machine_idx] = states

        info = mmap_manager.get_array_info(name)
        print(f"        ✓ Erstellt: {info['size_mb']:.1f} MB")

    total_memory = mmap_manager.get_total_memory_usage()
    print(f"\n    Gesamt Memory-Mapped Daten: {total_memory:.1f} MB")

    # 1.2 Out-of-Core Algorithmen
    print("\n📊 1.2 Out-of-Core Berechnungen:")

    def out_of_core_statistics(mmap_array, chunk_size=10000):
        """Berechne Statistiken für sehr große Arrays chunk-weise"""
        n_samples, n_features = mmap_array.shape
        n_chunks = (n_samples + chunk_size - 1) // chunk_size

        # Online-Algorithmus für Mittelwert und Varianz (Welford's algorithm)
        means = np.zeros(n_features)
        variances = np.zeros(n_features)
        mins = np.full(n_features, np.inf)
        maxs = np.full(n_features, -np.inf)

        total_count = 0

        for chunk_idx in range(n_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = min(start_idx + chunk_size, n_samples)

            # Lade nur aktuellen Chunk in Memory
            chunk_data = mmap_array[start_idx:end_idx, :]
            chunk_count = end_idx - start_idx

            # Update Online-Statistiken
            for feature_idx in range(n_features):
                feature_data = chunk_data[:, feature_idx]

                # Update Min/Max
                mins[feature_idx] = min(mins[feature_idx], np.min(feature_data))
                maxs[feature_idx] = max(maxs[feature_idx], np.max(feature_data))

                # Welford's Online-Algorithmus
                for value in feature_data:
                    total_count += 1
                    delta = value - means[feature_idx]
                    means[feature_idx] += delta / (total_count / n_features)
                    delta2 = value - means[feature_idx]
                    variances[feature_idx] += delta * delta2

        # Finalisiere Varianz
        variances /= total_count / n_features - 1
        stds = np.sqrt(variances)

        return {
            "means": means,
            "stds": stds,
            "mins": mins,
            "maxs": maxs,
            "total_samples": n_samples,
        }

    def out_of_core_correlation(mmap_array1, mmap_array2, chunk_size=10000):
        """Berechne Korrelationen zwischen zwei großen Arrays"""
        assert mmap_array1.shape == mmap_array2.shape

        n_samples, n_features = mmap_array1.shape
        n_chunks = (n_samples + chunk_size - 1) // chunk_size

        # Online-Kovarianzen berechnen
        means1 = np.zeros(n_features)
        means2 = np.zeros(n_features)
        covariances = np.zeros((n_features, n_features))

        total_count = 0

        # Erste Pass: Mittelwerte
        for chunk_idx in range(n_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = min(start_idx + chunk_size, n_samples)

            chunk1 = mmap_array1[start_idx:end_idx, :]
            chunk2 = mmap_array2[start_idx:end_idx, :]
            chunk_count = end_idx - start_idx

            means1 += np.sum(chunk1, axis=0)
            means2 += np.sum(chunk2, axis=0)
            total_count += chunk_count

        means1 /= total_count
        means2 /= total_count

        # Zweite Pass: Kovarianzen
        for chunk_idx in range(n_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = min(start_idx + chunk_size, n_samples)

            chunk1 = mmap_array1[start_idx:end_idx, :] - means1
            chunk2 = mmap_array2[start_idx:end_idx, :] - means2

            # Batch-Kovarianz
            covariances += chunk1.T @ chunk2

        covariances /= total_count - 1

        # Korrelationsmatrix
        stds1 = np.sqrt(np.diag(covariances))
        stds2 = np.sqrt(np.diag(covariances))
        correlation_matrix = covariances / np.outer(stds1, stds2)

        return correlation_matrix

    # Test Out-of-Core Algorithmen
    print("  Test Out-of-Core Statistiken:")

    sensor_array = mmap_manager.active_arrays["sensor_timeseries"]
    quality_array = mmap_manager.active_arrays["quality_measurements"]

    # Statistiken für Sensor-Daten
    print(f"    Sensor-Zeitreihen ({sensor_array.shape}):")
    sensor_stats = out_of_core_statistics(sensor_array, chunk_size=5000)

    print("      Chunk-Size: 5,000 Samples")
    print(f"      Features: {len(sensor_stats['means'])}")
    print(
        f"      Mittelwert-Bereich: {np.min(sensor_stats['means']):.2f} - {np.max(sensor_stats['means']):.2f}"
    )
    print(
        f"      Std-Abw.-Bereich: {np.min(sensor_stats['stds']):.2f} - {np.max(sensor_stats['stds']):.2f}"
    )

    # 1.3 Memory-Efficient Processing Patterns
    print("\n📊 1.3 Memory-Efficient Processing Patterns:")

    class StreamingProcessor:
        """Streaming-Prozessor für kontinuierliche Datenverarbeitung"""

        def __init__(self, buffer_size=1000):
            self.buffer_size = buffer_size
            self.processing_buffer = None
            self.buffer_index = 0
            self.total_processed = 0

            # Streaming-Metriken
            self.streaming_stats = {
                "running_mean": 0,
                "running_variance": 0,
                "running_min": float("inf"),
                "running_max": float("-inf"),
            }

        def process_streaming_data(self, new_data_chunk):
            """Verarbeite neuen Daten-Chunk im Streaming-Modus"""
            chunk_size = len(new_data_chunk)

            if self.processing_buffer is None:
                # Initialisiere Buffer basierend auf Datenform
                data_shape = new_data_chunk.shape[1:] if new_data_chunk.ndim > 1 else ()
                full_shape = (self.buffer_size,) + data_shape
                self.processing_buffer = np.zeros(
                    full_shape, dtype=new_data_chunk.dtype
                )

            results = []

            for i in range(chunk_size):
                # Füge neuen Datenpunkt zum Buffer hinzu
                self.processing_buffer[self.buffer_index] = new_data_chunk[i]
                self.buffer_index = (self.buffer_index + 1) % self.buffer_size

                # Update Streaming-Statistiken
                self._update_streaming_stats(new_data_chunk[i])

                # Verarbeite wenn Buffer voll ist
                if self.total_processed >= self.buffer_size - 1:
                    processed_result = self._process_full_buffer()
                    results.append(processed_result)

                self.total_processed += 1

            return results

        def _update_streaming_stats(self, new_value):
            """Update Online-Statistiken"""
            if np.isscalar(new_value):
                value = new_value
            else:
                value = np.mean(new_value)  # Vereinfachung für Vektoren

            n = self.total_processed + 1

            # Online-Mittelwert
            old_mean = self.streaming_stats["running_mean"]
            self.streaming_stats["running_mean"] += (value - old_mean) / n

            # Online-Varianz (Welford)
            if n > 1:
                self.streaming_stats["running_variance"] += (value - old_mean) * (
                    value - self.streaming_stats["running_mean"]
                )

            # Min/Max
            self.streaming_stats["running_min"] = min(
                self.streaming_stats["running_min"], value
            )
            self.streaming_stats["running_max"] = max(
                self.streaming_stats["running_max"], value
            )

        def _process_full_buffer(self):
            """Verarbeite vollen Buffer"""
            # Beispiel-Verarbeitung: Sliding-Window Statistiken
            buffer_mean = np.mean(self.processing_buffer)
            buffer_std = np.std(self.processing_buffer)
            buffer_trend = self._calculate_trend()

            return {
                "timestamp": self.total_processed,
                "buffer_mean": buffer_mean,
                "buffer_std": buffer_std,
                "trend": buffer_trend,
                "anomaly_score": self._calculate_anomaly_score(buffer_mean, buffer_std),
            }

        def _calculate_trend(self):
            """Berechne Trend im aktuellen Buffer"""
            if self.processing_buffer.ndim == 1:
                x = np.arange(self.buffer_size)
                trend_slope = np.polyfit(x, self.processing_buffer, 1)[0]
                return trend_slope
            else:
                # Für mehrdimensionale Daten: mittlerer Trend
                trends = []
                for feature_idx in range(self.processing_buffer.shape[1]):
                    x = np.arange(self.buffer_size)
                    trend_slope = np.polyfit(
                        x, self.processing_buffer[:, feature_idx], 1
                    )[0]
                    trends.append(trend_slope)
                return np.mean(trends)

        def _calculate_anomaly_score(self, current_mean, current_std):
            """Berechne Anomalie-Score basierend auf historischen Daten"""
            global_mean = self.streaming_stats["running_mean"]
            global_variance = self.streaming_stats["running_variance"] / max(
                1, self.total_processed - 1
            )
            global_std = np.sqrt(global_variance) if global_variance > 0 else 1

            # Z-Score des aktuellen Buffer-Mittelwerts
            z_score = abs(current_mean - global_mean) / global_std
            anomaly_score = min(z_score / 3, 1.0)  # Normalisiert auf 0-1

            return anomaly_score

        def get_streaming_summary(self):
            """Zusammenfassung der Streaming-Statistiken"""
            variance = self.streaming_stats["running_variance"] / max(
                1, self.total_processed - 1
            )

            return {
                "total_processed": self.total_processed,
                "streaming_mean": self.streaming_stats["running_mean"],
                "streaming_std": np.sqrt(variance) if variance > 0 else 0,
                "streaming_min": self.streaming_stats["running_min"],
                "streaming_max": self.streaming_stats["running_max"],
                "streaming_range": self.streaming_stats["running_max"]
                - self.streaming_stats["running_min"],
            }

    # Test Streaming-Prozessor
    print("  Test Streaming-Prozessor mit Memory-Mapped Daten:")

    streaming_processor = StreamingProcessor(buffer_size=500)

    # Simuliere Streaming von Memory-Mapped Array
    sensor_data = mmap_manager.active_arrays["sensor_timeseries"]
    chunk_size = 100
    n_chunks = min(50, sensor_data.shape[0] // chunk_size)  # Limitiere für Demo

    print(f"    Verarbeite {n_chunks} Chunks à {chunk_size} Samples:")

    all_results = []
    processing_times = []

    for chunk_idx in range(n_chunks):
        start_idx = chunk_idx * chunk_size
        end_idx = min(start_idx + chunk_size, sensor_data.shape[0])

        # Lade Chunk aus Memory-Mapped Array
        chunk_start = time.time()
        data_chunk = sensor_data[start_idx:end_idx, 0]  # Nur erste Sensor-Spalte
        chunk_results = streaming_processor.process_streaming_data(data_chunk)
        chunk_time = time.time() - chunk_start

        processing_times.append(chunk_time)
        all_results.extend(chunk_results)

        if (chunk_idx + 1) % 10 == 0:
            summary = streaming_processor.get_streaming_summary()
            print(
                f"      Chunk {chunk_idx + 1:2d}: {summary['total_processed']:5d} Samples, "
                f"μ={summary['streaming_mean']:.2f}, σ={summary['streaming_std']:.2f}"
            )

    # Performance-Auswertung
    total_samples = streaming_processor.total_processed
    total_time = sum(processing_times)
    throughput = total_samples / total_time

    print("\n    Streaming-Performance:")
    print(f"      Samples verarbeitet: {total_samples:,}")
    print(f"      Gesamtzeit: {total_time:.3f} s")
    print(f"      Durchsatz: {throughput:.0f} Samples/s")
    print(f"      Buffer-Ergebnisse: {len(all_results)}")

    # Anomalie-Analyse
    if all_results:
        anomaly_scores = [r["anomaly_score"] for r in all_results]
        high_anomalies = sum(1 for score in anomaly_scores if score > 0.7)
        print(
            f"      Anomalien detektiert: {high_anomalies}/{len(all_results)} Buffers"
        )

    # Cleanup
    print("\n  Cleanup Memory-Mapped Arrays:")
    for name in list(mmap_manager.active_arrays.keys()):
        mmap_manager.cleanup_array(name)
        print(f"    ✓ {name} bereinigt")

    duration = time.time() - start_time
    print(f"\n⚡ Memory-Mapped Arrays in {duration:.3f} Sekunden")
    print("💾 Memory-Mapping ermöglicht Verarbeitung von TB-großen Datasets!")
    print()


def aufgabe_2_parallelisierte_operationen():
    """Aufgabe 2: Parallelisierte NumPy-Operationen"""
    print("🎯 AUFGABE 2: PARALLELISIERTE NUMPY-OPERATIONEN")
    print("-" * 50)
    print("Ziel: Implementiere Multi-Processing und Threading für")
    print("rechenintensive NumPy-Operationen mit optimaler CPU-Nutzung")
    print()

    start_time = time.time()

    # 2.1 Multi-Processing für CPU-intensive Operationen
    print("📊 2.1 Multi-Processing für CPU-intensive Berechnungen:")

    def parallel_matrix_operations(data_chunks, operation_func, n_processes=None):
        """Führe Matrix-Operationen parallel aus"""
        if n_processes is None:
            n_processes = min(mp.cpu_count(), len(data_chunks))

        print(
            f"    Verwende {n_processes} Prozesse für {len(data_chunks)} Daten-Chunks"
        )

        # Sequential Processing (Baseline)
        start_seq = time.time()
        sequential_results = [operation_func(chunk) for chunk in data_chunks]
        time_sequential = time.time() - start_seq

        # Parallel Processing
        start_par = time.time()
        with ProcessPoolExecutor(max_workers=n_processes) as executor:
            parallel_results = list(executor.map(operation_func, data_chunks))
        time_parallel = time.time() - start_par

        # Validierung der Ergebnisse
        results_match = all(
            np.allclose(seq, par)
            for seq, par in zip(sequential_results, parallel_results, strict=False)
        )

        return {
            "sequential_time": time_sequential,
            "parallel_time": time_parallel,
            "speedup": time_sequential / time_parallel,
            "results_valid": results_match,
            "sequential_results": sequential_results,
            "parallel_results": parallel_results,
        }

    # Test-Funktionen für verschiedene Operationstypen
    def heavy_linear_algebra(data_chunk):
        """CPU-intensive lineare Algebra Operationen"""
        matrix_a, matrix_b = data_chunk

        # Verschiedene rechenintensive Operationen
        result = {}

        # Matrix-Multiplikation
        result["matmul"] = matrix_a @ matrix_b

        # Eigenwerte und Eigenvektoren
        if matrix_a.shape[0] == matrix_a.shape[1] and matrix_a.shape[0] <= 1000:
            try:
                eigenvals, eigenvecs = np.linalg.eig(matrix_a)
                result["eigenvals"] = eigenvals
            except:
                result["eigenvals"] = np.array([])

        # SVD (Singular Value Decomposition)
        try:
            U, s, Vt = np.linalg.svd(matrix_a, full_matrices=False)
            result["svd_singular_values"] = s
        except:
            result["svd_singular_values"] = np.array([])

        # Matrix-Inverse (falls quadratisch und invertierbar)
        if matrix_a.shape[0] == matrix_a.shape[1] and matrix_a.shape[0] <= 500:
            try:
                result["inverse"] = np.linalg.inv(
                    matrix_a + np.eye(matrix_a.shape[0]) * 1e-6
                )
            except:
                result["inverse"] = np.eye(matrix_a.shape[0])

        return result

    def statistical_analysis(data_chunk):
        """Statistische Analysen für Produktionsdaten"""
        sensor_data = data_chunk

        results = {}

        # Basis-Statistiken
        results["mean"] = np.mean(sensor_data, axis=0)
        results["std"] = np.std(sensor_data, axis=0, ddof=1)
        results["skewness"] = self._calculate_skewness(sensor_data)
        results["kurtosis"] = self._calculate_kurtosis(sensor_data)

        # Korrelationsmatrix
        if sensor_data.shape[1] > 1:
            results["correlation"] = np.corrcoef(sensor_data.T)

        # Percentiles
        results["percentiles"] = np.percentile(sensor_data, [5, 25, 50, 75, 95], axis=0)

        # Outlier-Detection (IQR-Methode)
        q25 = np.percentile(sensor_data, 25, axis=0)
        q75 = np.percentile(sensor_data, 75, axis=0)
        iqr = q75 - q25
        lower_bound = q25 - 1.5 * iqr
        upper_bound = q75 + 1.5 * iqr

        outliers = (sensor_data < lower_bound) | (sensor_data > upper_bound)
        results["outlier_count"] = np.sum(outliers, axis=0)

        return results

    def _calculate_skewness(data):
        """Berechne Schiefe (Skewness)"""
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0, ddof=1)
        centered = data - mean
        skewness = (
            np.mean((centered / std) ** 3, axis=0)
            if np.all(std > 0)
            else np.zeros(data.shape[1])
        )
        return skewness

    def _calculate_kurtosis(data):
        """Berechne Kurtosis"""
        mean = np.mean(data, axis=0)
        std = np.std(data, axis=0, ddof=1)
        centered = data - mean
        kurtosis = (
            np.mean((centered / std) ** 4, axis=0) - 3
            if np.all(std > 0)
            else np.zeros(data.shape[1])
        )
        return kurtosis

    # Test Parallel Matrix Operations
    print("  Test 1: Parallele Matrix-Operationen")

    # Erstelle Test-Daten für Matrix-Operationen
    np.random.seed(42)
    matrix_sizes = [200, 300, 400, 500]
    matrix_chunks = []

    for size in matrix_sizes:
        matrix_a = np.random.randn(size, size)
        matrix_b = np.random.randn(size, size)
        matrix_chunks.append((matrix_a, matrix_b))

    print(f"    Matrix-Größen: {matrix_sizes}")

    # Parallel Ausführung
    linalg_results = parallel_matrix_operations(
        matrix_chunks, heavy_linear_algebra, n_processes=4
    )

    print(f"    Sequential: {linalg_results['sequential_time']:.3f}s")
    print(f"    Parallel:   {linalg_results['parallel_time']:.3f}s")
    print(f"    Speedup:    {linalg_results['speedup']:.2f}x")
    print(f"    Ergebnisse korrekt: {linalg_results['results_valid']}")

    # Test Statistical Analysis
    print("\n  Test 2: Parallele statistische Analysen")

    # Erstelle große Sensor-Datasets
    sensor_datasets = []
    dataset_sizes = [(10000, 20), (15000, 25), (20000, 30), (25000, 35)]

    for n_samples, n_sensors in dataset_sizes:
        # Simuliere realistische Sensor-Daten
        base_signals = np.random.randn(n_samples, n_sensors)
        trends = np.linspace(0, 5, n_samples)[:, np.newaxis]
        noise = 0.1 * np.random.randn(n_samples, n_sensors)

        sensor_data = base_signals + trends + noise
        sensor_datasets.append(sensor_data)

    print(f"    Dataset-Größen: {dataset_sizes}")

    stats_results = parallel_matrix_operations(
        sensor_datasets, statistical_analysis, n_processes=4
    )

    print(f"    Sequential: {stats_results['sequential_time']:.3f}s")
    print(f"    Parallel:   {stats_results['parallel_time']:.3f}s")
    print(f"    Speedup:    {stats_results['speedup']:.2f}x")

    # 2.2 Thread-basierte Parallelisierung für I/O-intensive Operationen
    print("\n📊 2.2 Thread-basierte Parallelisierung:")

    def threaded_data_processing(data_sources, processing_func, n_threads=None):
        """Thread-basierte Verarbeitung für I/O-intensive Operationen"""
        if n_threads is None:
            n_threads = min(mp.cpu_count() * 2, len(data_sources))

        print(f"    Verwende {n_threads} Threads für {len(data_sources)} Datenquellen")

        # Sequential Processing
        start_seq = time.time()
        sequential_results = [processing_func(source) for source in data_sources]
        time_sequential = time.time() - start_seq

        # Threaded Processing
        start_thread = time.time()
        with ThreadPoolExecutor(max_workers=n_threads) as executor:
            threaded_results = list(executor.map(processing_func, data_sources))
        time_threaded = time.time() - start_thread

        return {
            "sequential_time": time_sequential,
            "threaded_time": time_threaded,
            "speedup": time_sequential / time_threaded,
            "sequential_results": sequential_results,
            "threaded_results": threaded_results,
        }

    def simulate_io_intensive_processing(data_source_config):
        """Simuliere I/O-intensive Datenverarbeitung"""
        data_type, size, processing_complexity = data_source_config

        # Simuliere Daten-Loading (I/O Delay)
        time.sleep(0.1)  # Simuliere File I/O

        # Generiere Daten basierend auf Konfiguration
        if data_type == "timeseries":
            data = np.random.randn(size, 10)
        elif data_type == "image":
            data = np.random.randint(0, 256, (size, size, 3), dtype=np.uint8)
        elif data_type == "measurement":
            data = np.random.normal(25.0, 1.0, (size, 5))

        # Verarbeitung basierend auf Komplexität
        if processing_complexity == "light":
            result = np.mean(data, axis=0)
        elif processing_complexity == "medium":
            result = {"mean": np.mean(data), "std": np.std(data), "shape": data.shape}
        elif processing_complexity == "heavy":
            # Simuliere komplexere Verarbeitung
            time.sleep(0.05)  # Zusätzliche Verarbeitungszeit
            result = {
                "statistics": {
                    "mean": np.mean(data),
                    "std": np.std(data),
                    "min": np.min(data),
                    "max": np.max(data),
                },
                "correlations": (
                    np.corrcoef(data.reshape(-1, data.shape[-1]).T)
                    if data.ndim > 1
                    else None
                ),
                "processed_shape": data.shape,
            }

        return result

    # Test Thread-basierte Verarbeitung
    print("  Test I/O-intensive Verarbeitung:")

    # Verschiedene Datenquellen simulieren
    data_sources = [
        ("timeseries", 5000, "light"),
        ("image", 100, "medium"),
        ("measurement", 8000, "heavy"),
        ("timeseries", 6000, "medium"),
        ("image", 150, "heavy"),
        ("measurement", 10000, "light"),
        ("timeseries", 7000, "heavy"),
        ("image", 200, "light"),
    ]

    threading_results = threaded_data_processing(
        data_sources, simulate_io_intensive_processing, n_threads=6
    )

    print(f"    Sequential: {threading_results['sequential_time']:.3f}s")
    print(f"    Threaded:   {threading_results['threaded_time']:.3f}s")
    print(f"    Speedup:    {threading_results['speedup']:.2f}x")

    # 2.3 Hybrid Parallelisierung (Process + Thread)
    print("\n📊 2.3 Hybrid Parallelisierung:")

    class HybridParallelProcessor:
        """Kombination aus Process- und Thread-basierter Parallelisierung"""

        def __init__(self, n_processes=None, n_threads_per_process=2):
            self.n_processes = n_processes or mp.cpu_count()
            self.n_threads_per_process = n_threads_per_process

        def process_large_dataset(self, dataset, chunk_size=1000):
            """Verarbeite großes Dataset mit Hybrid-Parallelisierung"""
            print(
                f"    Hybrid-Setup: {self.n_processes} Prozesse × {self.n_threads_per_process} Threads"
            )

            # Teile Dataset in Process-Chunks
            n_samples = len(dataset)
            process_chunk_size = max(
                chunk_size * self.n_threads_per_process, n_samples // self.n_processes
            )
            process_chunks = []

            for i in range(0, n_samples, process_chunk_size):
                end_idx = min(i + process_chunk_size, n_samples)
                process_chunks.append(dataset[i:end_idx])

            print(f"    Dataset aufgeteilt: {len(process_chunks)} Process-Chunks")

            # Parallel Processing mit Process Pool
            start_time = time.time()

            with ProcessPoolExecutor(max_workers=self.n_processes) as executor:
                # Jeder Prozess verarbeitet seinen Chunk mit internen Threads
                futures = [
                    executor.submit(self._process_chunk_with_threads, chunk)
                    for chunk in process_chunks
                ]

                # Sammle Ergebnisse
                results = [future.result() for future in futures]

            processing_time = time.time() - start_time

            # Kombiniere Ergebnisse von allen Prozessen
            combined_results = self._combine_process_results(results)

            return {
                "processing_time": processing_time,
                "n_chunks_processed": len(process_chunks),
                "total_samples": n_samples,
                "throughput": n_samples / processing_time,
                "results": combined_results,
            }

        def _process_chunk_with_threads(self, data_chunk):
            """Verarbeite Chunk mit Thread-Pool"""
            # Teile Chunk weiter für Thread-Verarbeitung
            chunk_size = len(data_chunk)
            thread_chunk_size = max(100, chunk_size // self.n_threads_per_process)
            thread_chunks = []

            for i in range(0, chunk_size, thread_chunk_size):
                end_idx = min(i + thread_chunk_size, chunk_size)
                thread_chunks.append(data_chunk[i:end_idx])

            # Thread-basierte Verarbeitung innerhalb des Prozesses
            with ThreadPoolExecutor(
                max_workers=self.n_threads_per_process
            ) as thread_executor:
                thread_results = list(
                    thread_executor.map(self._analyze_thread_chunk, thread_chunks)
                )

            # Kombiniere Thread-Ergebnisse zu Prozess-Ergebnis
            return self._combine_thread_results(thread_results)

        def _analyze_thread_chunk(self, thread_chunk):
            """Analysiere einzelnen Thread-Chunk"""
            if len(thread_chunk) == 0:
                return {"count": 0}

            # Simuliere komplexe Analyse
            chunk_array = np.array(thread_chunk)

            analysis = {
                "count": len(thread_chunk),
                "mean": np.mean(chunk_array),
                "std": np.std(chunk_array),
                "percentiles": np.percentile(chunk_array, [25, 50, 75]),
                "outliers": self._detect_outliers(chunk_array),
            }

            return analysis

        def _detect_outliers(self, data):
            """Einfache Outlier-Detektion"""
            q75, q25 = np.percentile(data, [75, 25])
            iqr = q75 - q25
            lower_bound = q25 - 1.5 * iqr
            upper_bound = q75 + 1.5 * iqr

            outliers = (data < lower_bound) | (data > upper_bound)
            return np.sum(outliers)

        def _combine_thread_results(self, thread_results):
            """Kombiniere Ergebnisse von Threads zu Prozess-Ergebnis"""
            total_count = sum(r["count"] for r in thread_results if r["count"] > 0)

            if total_count == 0:
                return {"count": 0}

            # Gewichtete Durchschnitte
            weighted_mean = (
                sum(r["mean"] * r["count"] for r in thread_results if r["count"] > 0)
                / total_count
            )
            total_outliers = sum(
                r["outliers"] for r in thread_results if r["count"] > 0
            )

            return {
                "count": total_count,
                "mean": weighted_mean,
                "total_outliers": total_outliers,
                "thread_count": len([r for r in thread_results if r["count"] > 0]),
            }

        def _combine_process_results(self, process_results):
            """Kombiniere Ergebnisse von allen Prozessen"""
            total_count = sum(r["count"] for r in process_results if r["count"] > 0)

            if total_count == 0:
                return {"count": 0}

            weighted_mean = (
                sum(r["mean"] * r["count"] for r in process_results if r["count"] > 0)
                / total_count
            )
            total_outliers = sum(
                r["total_outliers"] for r in process_results if r["count"] > 0
            )

            return {
                "total_count": total_count,
                "overall_mean": weighted_mean,
                "total_outliers": total_outliers,
                "processes_used": len([r for r in process_results if r["count"] > 0]),
            }

    # Test Hybrid Parallelisierung
    print("  Test Hybrid Process+Thread Verarbeitung:")

    # Großes simuliertes Dataset
    np.random.seed(123)
    large_dataset = np.random.normal(50, 10, 50000).tolist()  # 50k Samples

    hybrid_processor = HybridParallelProcessor(n_processes=4, n_threads_per_process=3)

    # Baseline: Sequential Processing
    start_seq = time.time()
    sequential_mean = np.mean(large_dataset)
    sequential_outliers = np.sum(
        (np.array(large_dataset) < 20) | (np.array(large_dataset) > 80)
    )
    time_sequential = time.time() - start_seq

    # Hybrid Processing
    hybrid_results = hybrid_processor.process_large_dataset(
        large_dataset, chunk_size=500
    )

    print(f"    Dataset: {len(large_dataset):,} Samples")
    print(f"    Sequential: {time_sequential:.3f}s")
    print(f"    Hybrid:     {hybrid_results['processing_time']:.3f}s")
    print(f"    Speedup:    {time_sequential / hybrid_results['processing_time']:.2f}x")
    print(f"    Durchsatz:  {hybrid_results['throughput']:.0f} Samples/s")

    # Ergebnis-Validierung
    mean_error = abs(hybrid_results["results"]["overall_mean"] - sequential_mean)
    outlier_error = abs(
        hybrid_results["results"]["total_outliers"] - sequential_outliers
    )

    print("    Validierung:")
    print(f"      Mittelwert-Fehler: {mean_error:.6f}")
    print(f"      Outlier-Differenz: {outlier_error}")

    duration = time.time() - start_time
    print(f"\n⚡ Parallelisierte Operationen in {duration:.3f} Sekunden")
    print(
        "🚀 Parallelisierung kann 2-8x Speedup für rechenintensive Operationen bringen!"
    )
    print()


def aufgabe_3_custom_vectorized_functions():
    """Aufgabe 3: Custom Vectorized Functions und C-Extensions"""
    print("🎯 AUFGABE 3: CUSTOM VECTORIZED FUNCTIONS")
    print("-" * 45)
    print("Ziel: Erstelle hochoptimierte Custom Functions mit NumPy")
    print("und simuliere C-Extension Performance für kritische Operationen")
    print()

    start_time = time.time()

    # 3.1 Advanced Universal Functions (ufuncs)
    print("📊 3.1 Advanced Universal Functions:")

    class CustomUfuncLibrary:
        """Bibliothek für Custom Universal Functions"""

        def __init__(self):
            self.ufunc_cache = {}

        def create_production_ufuncs(self):
            """Erstelle produktionsspezifische ufuncs"""

            # Komplexe Toleranzprüfung mit asymmetrischen Grenzen
            def tolerance_check_asymmetric(
                measurement, target, lower_tol, upper_tol, weight_factor
            ):
                """Asymmetrische Toleranzprüfung mit Gewichtung"""
                if measurement < target - lower_tol:
                    deviation = abs(measurement - (target - lower_tol))
                    return -1 * (
                        1 + weight_factor * deviation
                    )  # Untermaß mit Gewichtung
                elif measurement > target + upper_tol:
                    deviation = abs(measurement - (target + upper_tol))
                    return 1 * (1 + weight_factor * deviation)  # Übermaß mit Gewichtung
                else:
                    return 0  # Innerhalb Toleranz

            # Erstelle ufunc
            self.ufunc_cache["tolerance_asymmetric"] = np.frompyfunc(
                tolerance_check_asymmetric, 5, 1
            )

            # Erweiterte Qualitätsbewertung
            def quality_score_complex(
                dimension,
                surface,
                hardness,
                temp,
                spec_dim,
                spec_surf,
                spec_hard,
                temp_coeff,
            ):
                """Komplexe Qualitätsbewertung mit Temperaturkorrektur"""
                # Dimensionale Bewertung
                dim_score = 1.0 - abs(dimension - spec_dim) / spec_dim

                # Oberflächenbewertung
                surf_score = 1.0 - abs(surface - spec_surf) / spec_surf

                # Härte-Bewertung
                hard_score = 1.0 - abs(hardness - spec_hard) / spec_hard

                # Temperaturkorrektur
                temp_correction = 1.0 + temp_coeff * (temp - 20.0) / 20.0

                # Gewichtete Gesamtbewertung
                overall_score = (
                    0.4 * dim_score + 0.3 * surf_score + 0.3 * hard_score
                ) * temp_correction

                return max(0.0, min(1.0, overall_score))

            self.ufunc_cache["quality_complex"] = np.frompyfunc(
                quality_score_complex, 8, 1
            )

            # Prozessfähigkeits-Berechnung
            def process_capability_advanced(
                measurement, target, usl, lsl, historical_std, sample_size
            ):
                """Erweiterte Prozessfähigkeitsberechnung"""
                if historical_std <= 0 or sample_size < 2:
                    return 0.0

                # Cp (Potentielle Prozessfähigkeit)
                cp = (usl - lsl) / (6 * historical_std)

                # Cpk (Tatsächliche Prozessfähigkeit)
                cpk_upper = (usl - measurement) / (3 * historical_std)
                cpk_lower = (measurement - lsl) / (3 * historical_std)
                cpk = min(cpk_upper, cpk_lower)

                # Cpm (Taguchi-Index)
                cpm = (usl - lsl) / (
                    6 * np.sqrt(historical_std**2 + (measurement - target) ** 2)
                )

                # Kombinierter Index
                combined_capability = (cp + cpk + cpm) / 3

                return combined_capability

            self.ufunc_cache["capability_advanced"] = np.frompyfunc(
                process_capability_advanced, 6, 1
            )

            return self.ufunc_cache

        def benchmark_ufunc_vs_vectorized(self, data_size=100000):
            """Vergleiche ufunc Performance mit anderen Implementierungen"""
            print(f"    Performance-Vergleich mit {data_size:,} Datenpunkten:")

            # Generiere Test-Daten
            np.random.seed(42)
            measurements = np.random.normal(25.0, 0.5, data_size)
            targets = np.full(data_size, 25.0)
            lower_tols = np.full(data_size, 0.2)
            upper_tols = np.full(data_size, 0.15)
            weight_factors = np.full(data_size, 1.5)

            # Method 1: ufunc
            ufunc_tolerance = self.ufunc_cache["tolerance_asymmetric"]

            start = time.time()
            results_ufunc = ufunc_tolerance(
                measurements, targets, lower_tols, upper_tols, weight_factors
            )
            time_ufunc = time.time() - start

            # Method 2: Vectorized NumPy
            start = time.time()
            results_vectorized = np.where(
                measurements < targets - lower_tols,
                -1
                * (1 + weight_factors * np.abs(measurements - (targets - lower_tols))),
                np.where(
                    measurements > targets + upper_tols,
                    1
                    * (
                        1
                        + weight_factors * np.abs(measurements - (targets + upper_tols))
                    ),
                    0,
                ),
            )
            time_vectorized = time.time() - start

            # Method 3: Python Loop
            start = time.time()
            results_loop = []
            for i in range(data_size):
                m, t, lt, ut, wf = (
                    measurements[i],
                    targets[i],
                    lower_tols[i],
                    upper_tols[i],
                    weight_factors[i],
                )
                if m < t - lt:
                    result = -1 * (1 + wf * abs(m - (t - lt)))
                elif m > t + ut:
                    result = 1 * (1 + wf * abs(m - (t + ut)))
                else:
                    result = 0
                results_loop.append(result)
            time_loop = time.time() - start

            # Validiere Ergebnisse
            ufunc_array = results_ufunc.astype(float)
            loop_array = np.array(results_loop)

            max_diff_ufunc = np.max(np.abs(ufunc_array - results_vectorized))
            max_diff_loop = np.max(np.abs(loop_array - results_vectorized))

            print(f"      ufunc:        {time_ufunc:.4f}s")
            print(
                f"      Vectorized:   {time_vectorized:.4f}s ({time_ufunc / time_vectorized:.1f}x vs ufunc)"
            )
            print(
                f"      Python Loop:  {time_loop:.4f}s ({time_loop / time_ufunc:.1f}x vs ufunc)"
            )
            print(f"      Max Diff ufunc vs vectorized: {max_diff_ufunc:.2e}")
            print(f"      Max Diff loop vs vectorized:  {max_diff_loop:.2e}")

            return {
                "ufunc_time": time_ufunc,
                "vectorized_time": time_vectorized,
                "loop_time": time_loop,
                "ufunc_speedup_vs_loop": time_loop / time_ufunc,
                "vectorized_speedup_vs_loop": time_loop / time_vectorized,
            }

    # Test Custom ufunc Library
    ufunc_lib = CustomUfuncLibrary()
    ufunc_lib.create_production_ufuncs()

    benchmark_results = ufunc_lib.benchmark_ufunc_vs_vectorized(data_size=200000)

    print("    Speedup-Faktoren:")
    print(
        f"      ufunc vs Python Loop: {benchmark_results['ufunc_speedup_vs_loop']:.1f}x"
    )
    print(
        f"      Vectorized vs Python Loop: {benchmark_results['vectorized_speedup_vs_loop']:.1f}x"
    )

    # 3.2 Compiled Function Simulation (Numba-style)
    print("\n📊 3.2 Compiled Function Simulation:")

    class CompiledFunctionSimulator:
        """Simuliert Compiled Function Performance (ähnlich Numba)"""

        def __init__(self):
            self.function_cache = {}
            self.compilation_overhead = {}

        def simulate_jit_compilation(self, func, *args, **kwargs):
            """Simuliere JIT-Compilation Overhead und Performance"""
            func_name = func.__name__

            if func_name not in self.function_cache:
                # Simuliere Compilation Overhead
                compilation_start = time.time()
                time.sleep(0.01)  # Simuliere Compilation-Zeit
                compilation_time = time.time() - compilation_start

                self.compilation_overhead[func_name] = compilation_time
                self.function_cache[func_name] = True

                print(f"      JIT-Compiling {func_name}... ({compilation_time:.3f}s)")

            # Simuliere optimierte Ausführung (2-5x schneller)
            start_time = time.time()
            result = func(*args, **kwargs)
            base_time = time.time() - start_time

            # Simuliere JIT-Speedup
            simulated_speedup = np.random.uniform(2.0, 5.0)
            simulated_time = base_time / simulated_speedup

            return result, simulated_time, base_time

        def complex_mathematical_kernel(self, data_array, coefficients, power_factors):
            """Komplexer mathematischer Kernel für Simulation"""
            # Simuliere komplexe Berechnungen die von JIT profitieren würden
            result = np.zeros_like(data_array)

            for i in range(len(data_array)):
                value = data_array[i]
                accumulated = 0.0

                # Komplexe Berechnungsschleife
                for j, (coeff, power) in enumerate(
                    zip(coefficients, power_factors, strict=False)
                ):
                    accumulated += coeff * (value**power) * np.sin(j * value * 0.1)

                result[i] = accumulated

            return result

        def matrix_multiplication_optimized(self, matrix_a, matrix_b):
            """Optimierte Matrix-Multiplikation Simulation"""
            # Standard NumPy (bereits optimiert)
            return matrix_a @ matrix_b

        def statistical_kernel_heavy(self, data_matrix):
            """Statistischer Kernel mit vielen Operationen"""
            results = {}

            # Rolling Statistics (rechenintensiv)
            window_size = 50
            n_samples, n_features = data_matrix.shape

            rolling_means = np.zeros((n_samples - window_size + 1, n_features))
            rolling_stds = np.zeros((n_samples - window_size + 1, n_features))

            for i in range(n_samples - window_size + 1):
                window_data = data_matrix[i : i + window_size, :]
                rolling_means[i, :] = np.mean(window_data, axis=0)
                rolling_stds[i, :] = np.std(window_data, axis=0, ddof=1)

            results["rolling_means"] = rolling_means
            results["rolling_stds"] = rolling_stds

            # Cross-Correlations
            results["cross_correlations"] = np.corrcoef(data_matrix.T)

            return results

    # Test Compiled Function Simulator
    print("  Simulation von JIT-Compiled Functions:")

    compiled_sim = CompiledFunctionSimulator()

    # Test 1: Komplexer mathematischer Kernel
    print("\n    Test 1: Komplexer mathematischer Kernel")
    np.random.seed(42)
    test_data = np.random.randn(50000)
    coefficients = np.array([1.5, -0.8, 2.1, -1.2, 0.9])
    power_factors = np.array([1.0, 2.0, 0.5, 1.5, 3.0])

    # Normale Ausführung
    start = time.time()
    result_normal = compiled_sim.complex_mathematical_kernel(
        test_data, coefficients, power_factors
    )
    time_normal = time.time() - start

    # "JIT-Compiled" Ausführung
    result_jit, time_jit, time_jit_base = compiled_sim.simulate_jit_compilation(
        compiled_sim.complex_mathematical_kernel, test_data, coefficients, power_factors
    )

    compilation_overhead = compiled_sim.compilation_overhead.get(
        "complex_mathematical_kernel", 0
    )
    total_jit_time = time_jit + compilation_overhead

    print(f"      Normale Ausführung: {time_normal:.4f}s")
    print(
        f"      JIT Simulation:     {time_jit:.4f}s (+ {compilation_overhead:.3f}s Compilation)"
    )
    print(f"      Total JIT:          {total_jit_time:.4f}s")
    print(f"      Speedup (nach Warmup): {time_normal / time_jit:.1f}x")

    # Test 2: Statistische Berechnungen
    print("\n    Test 2: Statistischer Kernel")
    matrix_data = np.random.randn(5000, 20)

    # Normale Ausführung
    start = time.time()
    stats_normal = compiled_sim.statistical_kernel_heavy(matrix_data)
    time_stats_normal = time.time() - start

    # JIT Simulation
    stats_jit, time_stats_jit, _ = compiled_sim.simulate_jit_compilation(
        compiled_sim.statistical_kernel_heavy, matrix_data
    )

    print(f"      Normale Ausführung: {time_stats_normal:.4f}s")
    print(f"      JIT Simulation:     {time_stats_jit:.4f}s")
    print(f"      Speedup: {time_stats_normal / time_stats_jit:.1f}x")

    # 3.3 Memory-Efficient Custom Operations
    print("\n📊 3.3 Memory-Efficient Custom Operations:")

    class MemoryEfficientOps:
        """Memory-effiziente Custom Operationen"""

        @staticmethod
        def in_place_transformation(array, operation="standardize"):
            """In-Place Transformationen zur Memory-Schonung"""
            original_memory = array.nbytes

            if operation == "standardize":
                # Z-Score Standardisierung in-place
                mean_val = np.mean(array)
                std_val = np.std(array)
                array -= mean_val
                array /= std_val

            elif operation == "normalize":
                # Min-Max Normalisierung in-place
                min_val = np.min(array)
                max_val = np.max(array)
                array -= min_val
                array /= max_val - min_val

            elif operation == "log_transform":
                # Log-Transformation in-place
                np.log1p(array, out=array)  # log(1 + x) für Stabilität

            elif operation == "box_cox":
                # Vereinfachte Box-Cox Transformation
                lambda_param = 0.5  # Vereinfacht
                if lambda_param == 0:
                    np.log(array, out=array)
                else:
                    array **= lambda_param
                    array -= 1
                    array /= lambda_param

            return original_memory  # Memory-Verbrauch unverändert

        @staticmethod
        def chunk_wise_correlation(large_array, chunk_size=1000):
            """Chunk-wise Korrelationsberechnung für große Arrays"""
            n_samples, n_features = large_array.shape
            n_chunks = (n_samples + chunk_size - 1) // chunk_size

            # Akkumulatoren für Online-Korrelationsberechnung
            mean_accumulator = np.zeros(n_features)
            cov_accumulator = np.zeros((n_features, n_features))
            total_samples = 0

            # Erste Pass: Mittelwerte
            for chunk_idx in range(n_chunks):
                start_idx = chunk_idx * chunk_size
                end_idx = min(start_idx + chunk_size, n_samples)

                chunk_data = large_array[start_idx:end_idx, :]
                chunk_samples = end_idx - start_idx

                mean_accumulator += np.sum(chunk_data, axis=0)
                total_samples += chunk_samples

            mean_accumulator /= total_samples

            # Zweite Pass: Kovarianzen
            for chunk_idx in range(n_chunks):
                start_idx = chunk_idx * chunk_size
                end_idx = min(start_idx + chunk_size, n_samples)

                chunk_data = large_array[start_idx:end_idx, :] - mean_accumulator
                cov_accumulator += chunk_data.T @ chunk_data

            cov_accumulator /= total_samples - 1

            # Korrelationsmatrix
            std_devs = np.sqrt(np.diag(cov_accumulator))
            correlation_matrix = cov_accumulator / np.outer(std_devs, std_devs)

            return correlation_matrix

        @staticmethod
        def memory_efficient_filtering(large_array, filter_func, chunk_size=1000):
            """Memory-effikiente Filterung großer Arrays"""
            n_samples = len(large_array)
            n_chunks = (n_samples + chunk_size - 1) // chunk_size

            # Sammle gefilterte Indizes
            filtered_indices = []

            for chunk_idx in range(n_chunks):
                start_idx = chunk_idx * chunk_size
                end_idx = min(start_idx + chunk_size, n_samples)

                chunk_data = large_array[start_idx:end_idx]
                chunk_mask = filter_func(chunk_data)

                # Lokale Indizes zu globalen Indizes
                local_indices = np.where(chunk_mask)[0]
                global_indices = local_indices + start_idx

                filtered_indices.extend(global_indices)

            return np.array(filtered_indices)

    # Test Memory-Efficient Operations
    print("  Test Memory-Efficient Operationen:")

    memory_ops = MemoryEfficientOps()

    # Test 1: In-Place Transformationen
    print("\n    Test 1: In-Place Transformationen")
    test_array = np.random.randn(100000)
    original_array = test_array.copy()

    transformations = ["standardize", "normalize", "log_transform"]

    for transform in transformations:
        test_copy = original_array.copy()

        # Memory-Verbrauch vor Transformation
        memory_before = test_copy.nbytes

        # In-Place Transformation
        start = time.time()
        memory_used = memory_ops.in_place_transformation(test_copy, transform)
        transform_time = time.time() - start

        memory_after = test_copy.nbytes

        print(
            f"      {transform:12s}: {transform_time:.4f}s, "
            f"Memory: {memory_before / 1024**2:.1f} MB → {memory_after / 1024**2:.1f} MB"
        )

    # Test 2: Chunk-wise Korrelation
    print("\n    Test 2: Chunk-wise Korrelation")
    large_matrix = np.random.randn(20000, 15)

    # Standard-Methode
    start = time.time()
    corr_standard = np.corrcoef(large_matrix.T)
    time_standard = time.time() - start

    # Chunk-wise Methode
    start = time.time()
    corr_chunked = memory_ops.chunk_wise_correlation(large_matrix, chunk_size=2000)
    time_chunked = time.time() - start

    # Vergleiche Ergebnisse
    max_diff = np.max(np.abs(corr_standard - corr_chunked))

    print(f"      Standard Korrelation: {time_standard:.4f}s")
    print(f"      Chunk-wise Korrelation: {time_chunked:.4f}s")
    print(f"      Max Unterschied: {max_diff:.2e}")
    print("      Memory-Vorteil: Konstant vs. O(n²)")

    duration = time.time() - start_time
    print(f"\n⚡ Custom Vectorized Functions in {duration:.3f} Sekunden")
    print("⚡ Custom ufuncs und JIT-Compilation können 2-10x Speedup bringen!")
    print()


def aufgabe_4_realtime_stream_processing():
    """Aufgabe 4: Real-Time Stream Processing at Scale"""
    print("🎯 AUFGABE 4: REAL-TIME STREAM PROCESSING AT SCALE")
    print("-" * 55)
    print("Ziel: Implementiere High-Throughput Stream Processing für")
    print("kontinuierliche Sensor-Datenströme mit Echtzeit-Analyse")
    print()

    start_time = time.time()

    # 4.1 High-Performance Stream Buffer
    print("📊 4.1 High-Performance Stream Buffer:")

    class CircularStreamBuffer:
        """High-Performance Ring Buffer für Stream Processing"""

        def __init__(self, buffer_size, n_channels, dtype=np.float32):
            self.buffer_size = buffer_size
            self.n_channels = n_channels
            self.dtype = dtype

            # Circular Buffer als Memory-Mapped Array für Performance
            self.buffer = np.zeros((buffer_size, n_channels), dtype=dtype)
            self.write_index = 0
            self.read_index = 0
            self.buffer_full = False
            self.total_written = 0

            # Performance Monitoring
            self.write_times = []
            self.read_times = []

        def write_batch(self, data_batch):
            """Schreibe Batch von Daten in Buffer"""
            start_time = time.time()

            batch_size = len(data_batch)
            if batch_size == 0:
                return False

            # Prüfe ob genug Platz vorhanden
            available_space = self._get_available_write_space()
            if batch_size > available_space:
                # Überschreibe älteste Daten (Circular Buffer)
                self._advance_read_index(batch_size - available_space)

            # Schreibe Daten in Buffer
            for i, data_point in enumerate(data_batch):
                self.buffer[self.write_index] = data_point
                self.write_index = (self.write_index + 1) % self.buffer_size

                if self.write_index == self.read_index and not self.buffer_full:
                    self.buffer_full = True

            self.total_written += batch_size

            write_time = time.time() - start_time
            self.write_times.append(write_time)

            return True

        def read_latest(self, n_samples):
            """Lese neueste n Samples aus Buffer"""
            start_time = time.time()

            if n_samples > self.buffer_size:
                n_samples = self.buffer_size

            available_samples = self._get_available_read_samples()
            actual_samples = min(n_samples, available_samples)

            if actual_samples == 0:
                return np.array([])

            # Lese Daten aus Buffer
            result = np.zeros((actual_samples, self.n_channels), dtype=self.dtype)

            for i in range(actual_samples):
                read_idx = (self.write_index - actual_samples + i) % self.buffer_size
                result[i] = self.buffer[read_idx]

            read_time = time.time() - start_time
            self.read_times.append(read_time)

            return result

        def read_window(self, start_offset, window_size):
            """Lese Fenster von Daten aus Buffer"""
            available_samples = self._get_available_read_samples()

            if start_offset >= available_samples or window_size <= 0:
                return np.array([])

            actual_window_size = min(window_size, available_samples - start_offset)
            result = np.zeros((actual_window_size, self.n_channels), dtype=self.dtype)

            for i in range(actual_window_size):
                read_idx = (
                    self.write_index - available_samples + start_offset + i
                ) % self.buffer_size
                result[i] = self.buffer[read_idx]

            return result

        def _get_available_write_space(self):
            """Verfügbarer Schreibplatz im Buffer"""
            if self.buffer_full:
                return 0
            elif self.write_index >= self.read_index:
                return self.buffer_size - (self.write_index - self.read_index)
            else:
                return self.read_index - self.write_index

        def _get_available_read_samples(self):
            """Verfügbare Samples zum Lesen"""
            if self.buffer_full:
                return self.buffer_size
            elif self.write_index >= self.read_index:
                return self.write_index - self.read_index
            else:
                return self.buffer_size - (self.read_index - self.write_index)

        def _advance_read_index(self, n_steps):
            """Bewege Read-Index um n Schritte vor"""
            self.read_index = (self.read_index + n_steps) % self.buffer_size
            if self.buffer_full and n_steps > 0:
                self.buffer_full = False

        def get_performance_stats(self):
            """Performance-Statistiken des Buffers"""
            stats = {
                "total_written": self.total_written,
                "buffer_utilization": self._get_available_read_samples()
                / self.buffer_size,
                "buffer_full": self.buffer_full,
            }

            if self.write_times:
                stats["avg_write_time"] = np.mean(self.write_times)
                stats["max_write_time"] = np.max(self.write_times)

            if self.read_times:
                stats["avg_read_time"] = np.mean(self.read_times)
                stats["max_read_time"] = np.max(self.read_times)

            return stats

    # Test Circular Stream Buffer
    print("  Test High-Performance Stream Buffer:")

    # Simuliere Multi-Channel Sensor-Stream
    n_channels = 50  # 50 Sensor-Kanäle
    buffer_size = 10000  # 10k Sample Buffer
    stream_buffer = CircularStreamBuffer(buffer_size, n_channels)

    print(f"    Buffer-Setup: {buffer_size:,} Samples × {n_channels} Kanäle")

    # Simuliere kontinuierlichen Datenfluss
    np.random.seed(42)
    batch_sizes = [100, 200, 150, 300, 250]  # Variable Batch-Größen
    total_batches = 200

    print(f"    Simuliere {total_batches} Batches mit variablen Größen:")

    for batch_idx in range(total_batches):
        batch_size = np.random.choice(batch_sizes)

        # Generiere realistischen Sensor-Batch
        sensor_batch = []
        for _ in range(batch_size):
            # Simuliere Sensor-Kanäle mit verschiedenen Charakteristiken
            sensor_data = np.zeros(n_channels)

            for channel in range(n_channels):
                base_value = 50 + channel * 2  # Verschiedene Sensor-Bereiche
                trend = 0.01 * batch_idx  # Leichter Trend
                noise = np.random.normal(0, 1)
                cycle = 5 * np.sin(2 * np.pi * batch_idx / 50)  # Zyklische Komponente

                sensor_data[channel] = base_value + trend + noise + cycle

            sensor_batch.append(sensor_data)

        # Schreibe Batch in Buffer
        success = stream_buffer.write_batch(sensor_batch)

        # Periodisches Lesen für Stream-Processing
        if batch_idx % 10 == 0:
            # Lese aktuelle Daten für Analyse
            recent_data = stream_buffer.read_latest(500)

            if len(recent_data) > 0:
                # Einfache Stream-Analyse
                channel_means = np.mean(recent_data, axis=0)
                channel_stds = np.std(recent_data, axis=0)

                # Anomalie-Detektion
                anomaly_threshold = 3.0
                anomalous_channels = np.where(channel_stds > anomaly_threshold)[0]

                if len(anomalous_channels) > 0:
                    print(
                        f"      Batch {batch_idx:3d}: Anomalien in Kanälen {anomalous_channels[:3]}..."
                    )

    # Performance-Analyse
    buffer_stats = stream_buffer.get_performance_stats()

    print("\n    Buffer-Performance:")
    print(f"      Samples geschrieben: {buffer_stats['total_written']:,}")
    print(f"      Buffer-Auslastung: {buffer_stats['buffer_utilization']:.1%}")
    print(f"      Avg Write-Zeit: {buffer_stats['avg_write_time']:.6f}s")
    print(f"      Avg Read-Zeit: {buffer_stats['avg_read_time']:.6f}s")

    # 4.2 Real-Time Analytics Engine
    print("\n📊 4.2 Real-Time Analytics Engine:")

    class RealTimeAnalyticsEngine:
        """Echtzeit-Analytics für Streaming-Daten"""

        def __init__(self, n_channels, analytics_config):
            self.n_channels = n_channels
            self.config = analytics_config

            # Analytics State
            self.streaming_stats = {
                "count": np.zeros(n_channels),
                "sum": np.zeros(n_channels),
                "sum_squares": np.zeros(n_channels),
                "min_values": np.full(n_channels, np.inf),
                "max_values": np.full(n_channels, -np.inf),
            }

            # Sliding Window Analytics
            self.window_size = analytics_config.get("window_size", 1000)
            self.sliding_windows = [[] for _ in range(n_channels)]

            # Real-time Filters
            self.filters = self._initialize_filters()

            # Alert System
            self.alert_thresholds = analytics_config.get("alert_thresholds", {})
            self.active_alerts = []

        def _initialize_filters(self):
            """Initialisiere Real-time Filter"""
            filters = {}

            # Exponential Moving Average Filter
            filters["ema"] = {
                "alpha": 0.1,
                "values": np.zeros(self.n_channels),
                "initialized": False,
            }

            # Kalman Filter (vereinfacht)
            filters["kalman"] = {
                "estimate": np.zeros(self.n_channels),
                "error_covariance": np.ones(self.n_channels),
                "process_noise": 0.01,
                "measurement_noise": 0.1,
                "initialized": False,
            }

            return filters

        def process_stream_batch(self, data_batch):
            """Verarbeite Stream-Batch in Echtzeit"""
            if len(data_batch) == 0:
                return {}

            batch_results = {
                "timestamp": time.time(),
                "batch_size": len(data_batch),
                "analytics": {},
                "alerts": [],
            }

            # Update Streaming-Statistiken
            self._update_streaming_stats(data_batch)

            # Apply Real-time Filters
            filtered_data = self._apply_filters(data_batch)

            # Sliding Window Analytics
            window_analytics = self._update_sliding_windows(data_batch)

            # Anomalie-Detektion
            anomalies = self._detect_anomalies(data_batch, filtered_data)

            # Alert-System
            alerts = self._check_alerts(data_batch, window_analytics, anomalies)

            # Sammle Ergebnisse
            batch_results["analytics"] = {
                "streaming_stats": self._get_current_streaming_stats(),
                "filtered_latest": (
                    filtered_data[-1] if len(filtered_data) > 0 else None
                ),
                "window_analytics": window_analytics,
                "anomalies": anomalies,
            }
            batch_results["alerts"] = alerts

            return batch_results

        def _update_streaming_stats(self, data_batch):
            """Update Online-Statistiken"""
            batch_array = np.array(data_batch)

            self.streaming_stats["count"] += len(data_batch)
            self.streaming_stats["sum"] += np.sum(batch_array, axis=0)
            self.streaming_stats["sum_squares"] += np.sum(batch_array**2, axis=0)

            batch_min = np.min(batch_array, axis=0)
            batch_max = np.max(batch_array, axis=0)

            self.streaming_stats["min_values"] = np.minimum(
                self.streaming_stats["min_values"], batch_min
            )
            self.streaming_stats["max_values"] = np.maximum(
                self.streaming_stats["max_values"], batch_max
            )

        def _apply_filters(self, data_batch):
            """Anwenden von Real-time Filtern"""
            batch_array = np.array(data_batch)
            filtered_batch = np.zeros_like(batch_array)

            for i, data_point in enumerate(batch_array):
                # EMA Filter
                ema_filter = self.filters["ema"]
                if not ema_filter["initialized"]:
                    ema_filter["values"] = data_point.copy()
                    ema_filter["initialized"] = True
                else:
                    ema_filter["values"] = (
                        ema_filter["alpha"] * data_point
                        + (1 - ema_filter["alpha"]) * ema_filter["values"]
                    )

                # Vereinfachter Kalman Filter
                kalman_filter = self.filters["kalman"]
                if not kalman_filter["initialized"]:
                    kalman_filter["estimate"] = data_point.copy()
                    kalman_filter["initialized"] = True
                else:
                    # Prediction
                    predicted_estimate = kalman_filter["estimate"]
                    predicted_covariance = (
                        kalman_filter["error_covariance"]
                        + kalman_filter["process_noise"]
                    )

                    # Update
                    kalman_gain = predicted_covariance / (
                        predicted_covariance + kalman_filter["measurement_noise"]
                    )
                    kalman_filter["estimate"] = predicted_estimate + kalman_gain * (
                        data_point - predicted_estimate
                    )
                    kalman_filter["error_covariance"] = (
                        1 - kalman_gain
                    ) * predicted_covariance

                # Verwende Kalman-gefilterte Werte
                filtered_batch[i] = kalman_filter["estimate"]

            return filtered_batch

        def _update_sliding_windows(self, data_batch):
            """Update Sliding Windows für alle Kanäle"""
            batch_array = np.array(data_batch)

            for data_point in batch_array:
                for channel_idx in range(self.n_channels):
                    self.sliding_windows[channel_idx].append(data_point[channel_idx])

                    # Halte Window-Größe konstant
                    if len(self.sliding_windows[channel_idx]) > self.window_size:
                        self.sliding_windows[channel_idx].pop(0)

            # Berechne Window-Analytics
            window_analytics = {}
            for channel_idx in range(self.n_channels):
                if len(self.sliding_windows[channel_idx]) > 10:  # Mindestens 10 Samples
                    window_data = np.array(self.sliding_windows[channel_idx])

                    window_analytics[f"channel_{channel_idx}"] = {
                        "window_mean": np.mean(window_data),
                        "window_std": np.std(window_data),
                        "window_trend": self._calculate_trend(window_data),
                        "window_samples": len(window_data),
                    }

            return window_analytics

        def _calculate_trend(self, window_data):
            """Berechne Trend in Sliding Window"""
            if len(window_data) < 5:
                return 0.0

            x = np.arange(len(window_data))
            trend_slope = np.polyfit(x, window_data, 1)[0]
            return trend_slope

        def _detect_anomalies(self, data_batch, filtered_data):
            """Real-time Anomalie-Detektion"""
            anomalies = []

            if self.streaming_stats["count"][0] < 100:  # Nicht genug Daten
                return anomalies

            # Aktuelle Streaming-Statistiken
            current_stats = self._get_current_streaming_stats()

            for i, data_point in enumerate(data_batch):
                for channel_idx in range(self.n_channels):
                    value = data_point[channel_idx]
                    channel_mean = current_stats["means"][channel_idx]
                    channel_std = current_stats["stds"][channel_idx]

                    if channel_std > 0:
                        z_score = abs(value - channel_mean) / channel_std

                        if z_score > 3.0:  # 3-Sigma Regel
                            anomalies.append(
                                {
                                    "batch_index": i,
                                    "channel": channel_idx,
                                    "value": value,
                                    "z_score": z_score,
                                    "severity": "HIGH" if z_score > 4.0 else "MEDIUM",
                                }
                            )

            return anomalies

        def _check_alerts(self, data_batch, window_analytics, anomalies):
            """Prüfe Alert-Bedingungen"""
            alerts = []

            # Anomalie-basierte Alerts
            high_severity_anomalies = [a for a in anomalies if a["severity"] == "HIGH"]
            if len(high_severity_anomalies) > 0:
                alerts.append(
                    {
                        "type": "ANOMALY_CRITICAL",
                        "message": f"{len(high_severity_anomalies)} critical anomalies detected",
                        "channels": [a["channel"] for a in high_severity_anomalies],
                        "timestamp": time.time(),
                    }
                )

            # Trend-basierte Alerts
            for channel_key, analytics in window_analytics.items():
                channel_idx = int(channel_key.split("_")[1])
                trend = analytics["window_trend"]

                # Alert bei starkem Trend
                if abs(trend) > 0.1:  # Threshold für Trend-Alert
                    alerts.append(
                        {
                            "type": "TREND_ALERT",
                            "message": f"Strong trend detected in channel {channel_idx}",
                            "channel": channel_idx,
                            "trend_slope": trend,
                            "timestamp": time.time(),
                        }
                    )

            return alerts

        def _get_current_streaming_stats(self):
            """Aktuelle Streaming-Statistiken"""
            counts = self.streaming_stats["count"]
            sums = self.streaming_stats["sum"]
            sum_squares = self.streaming_stats["sum_squares"]

            means = np.divide(sums, counts, out=np.zeros_like(sums), where=counts > 0)

            variances = (
                np.divide(
                    sum_squares,
                    counts,
                    out=np.zeros_like(sum_squares),
                    where=counts > 0,
                )
                - means**2
            )
            variances = np.maximum(variances, 0)  # Verhindere negative Varianzen
            stds = np.sqrt(variances)

            return {
                "means": means,
                "stds": stds,
                "mins": self.streaming_stats["min_values"],
                "maxs": self.streaming_stats["max_values"],
                "counts": counts,
            }

        def get_analytics_summary(self):
            """Zusammenfassung der Analytics Engine"""
            current_stats = self._get_current_streaming_stats()

            summary = {
                "total_samples_processed": np.sum(current_stats["counts"]),
                "channels_active": np.sum(current_stats["counts"] > 0),
                "filters_initialized": all(
                    f["initialized"]
                    for f in self.filters.values()
                    if "initialized" in f
                ),
                "average_window_size": np.mean([len(w) for w in self.sliding_windows]),
                "active_alerts": len(self.active_alerts),
            }

            return summary

    # Test Real-Time Analytics Engine
    print("  Test Real-Time Analytics Engine:")

    analytics_config = {
        "window_size": 500,
        "alert_thresholds": {"anomaly_z_score": 3.0, "trend_threshold": 0.1},
    }

    analytics_engine = RealTimeAnalyticsEngine(n_channels, analytics_config)

    print(
        f"    Analytics-Setup: {n_channels} Kanäle, Window-Size: {analytics_config['window_size']}"
    )

    # Simuliere Real-Time Processing
    processing_results = []
    total_alerts = []

    # Verarbeite Stream-Daten in Real-Time
    for batch_idx in range(50):  # 50 Batches für Demo
        # Lese aktuellen Batch aus Buffer
        batch_data = stream_buffer.read_latest(200)

        if len(batch_data) > 0:
            # Real-Time Analytics
            batch_results = analytics_engine.process_stream_batch(batch_data)
            processing_results.append(batch_results)

            # Sammle Alerts
            if batch_results["alerts"]:
                total_alerts.extend(batch_results["alerts"])

            # Periodische Berichte
            if batch_idx % 10 == 0:
                analytics_summary = analytics_engine.get_analytics_summary()
                current_stats = analytics_engine._get_current_streaming_stats()

                print(
                    f"      Batch {batch_idx:2d}: {analytics_summary['total_samples_processed']:,} Samples, "
                    f"{len(batch_results['alerts'])} Alerts"
                )

    # Analytics-Zusammenfassung
    final_summary = analytics_engine.get_analytics_summary()

    print("\n    Real-Time Analytics Ergebnisse:")
    print(f"      Batches verarbeitet: {len(processing_results)}")
    print(f"      Samples total: {final_summary['total_samples_processed']:,}")
    print(f"      Aktive Kanäle: {final_summary['channels_active']}")
    print(f"      Filter initialisiert: {final_summary['filters_initialized']}")
    print(
        f"      Durchschnittliche Window-Größe: {final_summary['average_window_size']:.0f}"
    )

    # Alert-Analyse
    alert_types = {}
    for alert in total_alerts:
        alert_type = alert["type"]
        alert_types[alert_type] = alert_types.get(alert_type, 0) + 1

    if alert_types:
        print("      Alert-Verteilung:")
        for alert_type, count in alert_types.items():
            print(f"        {alert_type}: {count}")

    duration = time.time() - start_time
    print(f"\n⚡ Real-Time Stream Processing in {duration:.3f} Sekunden")
    print("📊 Stream Processing ermöglicht Echtzeit-Analyse von Sensor-Daten!")
    print()


def aufgabe_5_distributed_computing():
    """Aufgabe 5: Distributed Computing Patterns für NumPy"""
    print("🎯 AUFGABE 5: DISTRIBUTED COMPUTING PATTERNS")
    print("-" * 50)
    print("Ziel: Implementiere Distributed Computing Patterns für")
    print("Large-Scale NumPy-Operationen über mehrere Nodes")
    print()

    start_time = time.time()

    # 5.1 Distributed Array Operations Simulation
    print("📊 5.1 Distributed Array Operations Simulation:")

    class DistributedArraySimulator:
        """Simuliert Distributed Array-Operationen"""

        def __init__(self, n_nodes=4):
            self.n_nodes = n_nodes
            self.node_configs = self._initialize_nodes()
            self.communication_overhead = 0.001  # 1ms pro Message

        def _initialize_nodes(self):
            """Initialisiere Node-Konfigurationen"""
            nodes = {}
            for node_id in range(self.n_nodes):
                nodes[f"node_{node_id}"] = {
                    "id": node_id,
                    "cpu_cores": np.random.randint(4, 16),
                    "memory_gb": np.random.randint(8, 64),
                    "processing_speed": np.random.uniform(
                        0.8, 1.2
                    ),  # Relative Geschwindigkeit
                    "network_latency": np.random.uniform(0.5, 2.0),  # ms
                    "current_load": 0.0,
                }
            return nodes

        def distribute_array(self, large_array, distribution_strategy="row_wise"):
            """Verteile Array auf Nodes"""
            n_rows, n_cols = large_array.shape

            if distribution_strategy == "row_wise":
                # Verteile Zeilen auf Nodes
                rows_per_node = n_rows // self.n_nodes
                distributed_chunks = {}

                for node_id in range(self.n_nodes):
                    start_row = node_id * rows_per_node
                    if node_id == self.n_nodes - 1:
                        # Letzter Node bekommt übrige Zeilen
                        end_row = n_rows
                    else:
                        end_row = (node_id + 1) * rows_per_node

                    chunk = large_array[start_row:end_row, :]
                    distributed_chunks[f"node_{node_id}"] = {
                        "data": chunk,
                        "start_row": start_row,
                        "end_row": end_row,
                        "shape": chunk.shape,
                    }

            elif distribution_strategy == "column_wise":
                # Verteile Spalten auf Nodes
                cols_per_node = n_cols // self.n_nodes
                distributed_chunks = {}

                for node_id in range(self.n_nodes):
                    start_col = node_id * cols_per_node
                    if node_id == self.n_nodes - 1:
                        end_col = n_cols
                    else:
                        end_col = (node_id + 1) * cols_per_node

                    chunk = large_array[:, start_col:end_col]
                    distributed_chunks[f"node_{node_id}"] = {
                        "data": chunk,
                        "start_col": start_col,
                        "end_col": end_col,
                        "shape": chunk.shape,
                    }

            elif distribution_strategy == "block_wise":
                # 2D-Block-Verteilung
                rows_per_node = int(np.ceil(np.sqrt(self.n_nodes)))
                cols_per_node = int(np.ceil(self.n_nodes / rows_per_node))

                block_rows = n_rows // rows_per_node
                block_cols = n_cols // cols_per_node

                distributed_chunks = {}
                node_id = 0

                for block_row in range(rows_per_node):
                    for block_col in range(cols_per_node):
                        if node_id >= self.n_nodes:
                            break

                        start_row = block_row * block_rows
                        end_row = min((block_row + 1) * block_rows, n_rows)
                        start_col = block_col * block_cols
                        end_col = min((block_col + 1) * block_cols, n_cols)

                        if start_row < n_rows and start_col < n_cols:
                            chunk = large_array[start_row:end_row, start_col:end_col]
                            distributed_chunks[f"node_{node_id}"] = {
                                "data": chunk,
                                "start_row": start_row,
                                "end_row": end_row,
                                "start_col": start_col,
                                "end_col": end_col,
                                "shape": chunk.shape,
                            }

                        node_id += 1

            return distributed_chunks

        def distributed_operation(
            self, distributed_chunks, operation="mean", axis=None
        ):
            """Führe distributed Operation aus"""
            node_results = {}
            processing_times = {}

            # Phase 1: Lokale Verarbeitung auf jedem Node
            for node_name, chunk_info in distributed_chunks.items():
                node_config = self.node_configs[node_name]
                chunk_data = chunk_info["data"]

                # Simuliere Processing-Zeit basierend auf Node-Performance
                base_time = chunk_data.size * 1e-6  # Basis-Zeit pro Element
                actual_time = base_time / node_config["processing_speed"]

                # Simuliere Processing-Zeit
                start_time = time.time()
                time.sleep(actual_time * 1000)  # Konvertiere zu realistische Zeit (ms)

                # Führe Operation aus
                if operation == "mean":
                    if axis is None:
                        result = np.mean(chunk_data)
                    else:
                        result = np.mean(chunk_data, axis=axis)
                elif operation == "sum":
                    if axis is None:
                        result = np.sum(chunk_data)
                    else:
                        result = np.sum(chunk_data, axis=axis)
                elif operation == "std":
                    if axis is None:
                        result = np.std(chunk_data)
                    else:
                        result = np.std(chunk_data, axis=axis)
                elif operation == "max":
                    if axis is None:
                        result = np.max(chunk_data)
                    else:
                        result = np.max(chunk_data, axis=axis)

                processing_time = time.time() - start_time
                processing_times[node_name] = processing_time

                node_results[node_name] = {
                    "result": result,
                    "chunk_shape": chunk_data.shape,
                    "processing_time": processing_time,
                }

            # Phase 2: Ergebnis-Aggregation (Reduce-Phase)
            aggregation_start = time.time()

            if operation in ["mean", "sum"]:
                # Gewichtete Aggregation für mean/sum
                total_elements = 0
                weighted_sum = 0

                for node_name, node_result in node_results.items():
                    chunk_elements = np.prod(distributed_chunks[node_name]["shape"])
                    result = node_result["result"]

                    if operation == "mean":
                        weighted_sum += result * chunk_elements
                        total_elements += chunk_elements
                    else:  # sum
                        weighted_sum += result

                final_result = (
                    weighted_sum / total_elements
                    if operation == "mean"
                    else weighted_sum
                )

            elif operation in ["max", "std"]:
                # Element-wise Aggregation
                if operation == "max":
                    final_result = max(
                        node_result["result"] for node_result in node_results.values()
                    )
                else:  # std
                    # Für std: Combine Varianzen (vereinfacht)
                    variances = []
                    weights = []

                    for node_name, node_result in node_results.items():
                        chunk_elements = np.prod(distributed_chunks[node_name]["shape"])
                        std_val = node_result["result"]
                        variances.append(std_val**2)
                        weights.append(chunk_elements)

                    combined_variance = np.average(variances, weights=weights)
                    final_result = np.sqrt(combined_variance)

            # Kommunikations-Overhead simulieren
            communication_time = self.communication_overhead * len(node_results)
            aggregation_time = time.time() - aggregation_start + communication_time

            return {
                "final_result": final_result,
                "node_results": node_results,
                "total_processing_time": max(processing_times.values()),
                "aggregation_time": aggregation_time,
                "communication_overhead": communication_time,
                "nodes_used": len(node_results),
            }

    # Test Distributed Array Operations
    print("  Test Distributed Array Operations:")

    distributed_sim = DistributedArraySimulator(n_nodes=6)

    # Große Test-Matrix
    np.random.seed(42)
    large_matrix = np.random.randn(10000, 200)

    print(
        f"    Test-Matrix: {large_matrix.shape} ({large_matrix.nbytes / 1024**2:.1f} MB)"
    )
    print(f"    Nodes verfügbar: {distributed_sim.n_nodes}")

    # Test verschiedene Verteilungsstrategien
    distribution_strategies = ["row_wise", "column_wise", "block_wise"]
    operations = ["mean", "sum", "std", "max"]

    for strategy in distribution_strategies:
        print(f"\n    Verteilungsstrategie: {strategy}")

        # Verteile Array
        distribute_start = time.time()
        distributed_chunks = distributed_sim.distribute_array(large_matrix, strategy)
        distribute_time = time.time() - distribute_start

        print(f"      Verteilungszeit: {distribute_time:.4f}s")
        print(f"      Chunks erstellt: {len(distributed_chunks)}")

        # Zeige Chunk-Größen
        chunk_sizes = [chunk["shape"] for chunk in distributed_chunks.values()]
        print(
            f"      Chunk-Größen: {chunk_sizes[:3]}..."
            if len(chunk_sizes) > 3
            else f"      Chunk-Größen: {chunk_sizes}"
        )

        # Test verschiedene Operationen
        for operation in operations[:2]:  # Nur mean und sum für Demo
            # Distributed Operation
            dist_result = distributed_sim.distributed_operation(
                distributed_chunks, operation
            )

            # Baseline: Sequential Operation
            start = time.time()
            if operation == "mean":
                sequential_result = np.mean(large_matrix)
            elif operation == "sum":
                sequential_result = np.sum(large_matrix)
            sequential_time = time.time() - start

            # Vergleiche Ergebnisse
            result_error = abs(dist_result["final_result"] - sequential_result)
            speedup = sequential_time / dist_result["total_processing_time"]

            print(
                f"        {operation:4s}: Sequential={sequential_time:.4f}s, "
                f"Distributed={dist_result['total_processing_time']:.4f}s, "
                f"Speedup={speedup:.1f}x, Error={result_error:.2e}"
            )

    # 5.2 MapReduce-Pattern für NumPy
    print("\n📊 5.2 MapReduce-Pattern für NumPy:")

    class NumPyMapReduce:
        """MapReduce-Implementation für NumPy-Operationen"""

        def __init__(self, n_workers=4):
            self.n_workers = n_workers

        def map_reduce(self, large_dataset, map_func, reduce_func, chunk_size=None):
            """MapReduce-Pattern Implementation"""

            # Bestimme Chunk-Größe
            if chunk_size is None:
                chunk_size = len(large_dataset) // self.n_workers

            # Phase 1: Map (Partitionierung und lokale Verarbeitung)
            map_start = time.time()

            chunks = []
            for i in range(0, len(large_dataset), chunk_size):
                chunk = large_dataset[i : i + chunk_size]
                chunks.append(chunk)

            # Simuliere parallele Map-Operationen
            map_results = []
            with ProcessPoolExecutor(max_workers=self.n_workers) as executor:
                map_results = list(executor.map(map_func, chunks))

            map_time = time.time() - map_start

            # Phase 2: Reduce (Ergebnis-Aggregation)
            reduce_start = time.time()
            final_result = reduce_func(map_results)
            reduce_time = time.time() - reduce_start

            return {
                "result": final_result,
                "map_time": map_time,
                "reduce_time": reduce_time,
                "total_time": map_time + reduce_time,
                "chunks_processed": len(chunks),
                "workers_used": min(self.n_workers, len(chunks)),
            }

    # Test MapReduce Pattern
    print("  Test MapReduce für Produktions-Analytics:")

    mapreduce_engine = NumPyMapReduce(n_workers=4)

    # Simuliere große Produktionsdaten
    np.random.seed(123)
    production_data = []

    # Generiere 100k Produktionszyklen
    for cycle_id in range(100000):
        cycle_data = {
            "cycle_id": cycle_id,
            "machine_id": np.random.randint(1, 21),  # 20 Maschinen
            "cycle_time": np.random.normal(120, 15),  # Sekunden
            "quality_scores": np.random.uniform(0.8, 1.0, 5),  # 5 Qualitätsmerkmale
            "energy_consumption": np.random.normal(2.5, 0.3),  # kWh
            "temperature": np.random.normal(65, 5),  # °C
            "vibration": np.random.normal(3.0, 0.8),  # mm/s
        }
        production_data.append(cycle_data)

    print(f"    Produktionsdaten: {len(production_data):,} Zyklen")

    # Map-Function: Lokale Aggregation pro Chunk
    def map_production_analytics(data_chunk):
        """Map-Funktion für Produktions-Analytics"""
        chunk_results = {
            "cycle_count": len(data_chunk),
            "machines": set(),
            "cycle_times": [],
            "quality_scores": [],
            "energy_total": 0,
            "temperature_readings": [],
            "vibration_readings": [],
        }

        for cycle in data_chunk:
            chunk_results["machines"].add(cycle["machine_id"])
            chunk_results["cycle_times"].append(cycle["cycle_time"])
            chunk_results["quality_scores"].extend(cycle["quality_scores"])
            chunk_results["energy_total"] += cycle["energy_consumption"]
            chunk_results["temperature_readings"].append(cycle["temperature"])
            chunk_results["vibration_readings"].append(cycle["vibration"])

        # Lokale Statistiken berechnen
        chunk_analytics = {
            "cycle_count": chunk_results["cycle_count"],
            "unique_machines": len(chunk_results["machines"]),
            "avg_cycle_time": np.mean(chunk_results["cycle_times"]),
            "cycle_time_std": np.std(chunk_results["cycle_times"]),
            "avg_quality": np.mean(chunk_results["quality_scores"]),
            "min_quality": np.min(chunk_results["quality_scores"]),
            "total_energy": chunk_results["energy_total"],
            "avg_temperature": np.mean(chunk_results["temperature_readings"]),
            "max_vibration": np.max(chunk_results["vibration_readings"]),
            "machines_in_chunk": chunk_results["machines"],
        }

        return chunk_analytics

    # Reduce-Function: Globale Aggregation
    def reduce_production_analytics(map_results):
        """Reduce-Funktion für Produktions-Analytics"""
        global_analytics = {
            "total_cycles": sum(r["cycle_count"] for r in map_results),
            "all_machines": set(),
            "weighted_avg_cycle_time": 0,
            "combined_cycle_time_variance": 0,
            "global_avg_quality": 0,
            "global_min_quality": float("inf"),
            "total_energy_consumption": sum(r["total_energy"] for r in map_results),
            "weighted_avg_temperature": 0,
            "global_max_vibration": max(r["max_vibration"] for r in map_results),
        }

        # Combine machine sets
        for result in map_results:
            global_analytics["all_machines"].update(result["machines_in_chunk"])

        # Gewichtete Durchschnitte
        total_cycles = global_analytics["total_cycles"]

        weighted_cycle_time = (
            sum(r["avg_cycle_time"] * r["cycle_count"] for r in map_results)
            / total_cycles
        )

        weighted_quality = (
            sum(r["avg_quality"] * r["cycle_count"] for r in map_results) / total_cycles
        )

        weighted_temperature = (
            sum(r["avg_temperature"] * r["cycle_count"] for r in map_results)
            / total_cycles
        )

        global_analytics.update(
            {
                "weighted_avg_cycle_time": weighted_cycle_time,
                "global_avg_quality": weighted_quality,
                "global_min_quality": min(r["min_quality"] for r in map_results),
                "weighted_avg_temperature": weighted_temperature,
                "unique_machines_total": len(global_analytics["all_machines"]),
            }
        )

        return global_analytics

    # MapReduce Ausführung
    production_analytics = mapreduce_engine.map_reduce(
        production_data,
        map_production_analytics,
        reduce_production_analytics,
        chunk_size=10000,
    )

    print("\n    MapReduce Ergebnisse:")
    print(f"      Map-Zeit: {production_analytics['map_time']:.3f}s")
    print(f"      Reduce-Zeit: {production_analytics['reduce_time']:.3f}s")
    print(f"      Gesamt-Zeit: {production_analytics['total_time']:.3f}s")
    print(f"      Chunks verarbeitet: {production_analytics['chunks_processed']}")
    print(f"      Worker verwendet: {production_analytics['workers_used']}")

    # Ergebnis-Details
    result = production_analytics["result"]
    print("\n    Produktions-Analytics Ergebnisse:")
    print(f"      Gesamt-Zyklen: {result['total_cycles']:,}")
    print(f"      Unique Maschinen: {result['unique_machines_total']}")
    print(
        f"      Durchschnittliche Zykluszeit: {result['weighted_avg_cycle_time']:.1f}s"
    )
    print(f"      Durchschnittliche Qualität: {result['global_avg_quality']:.3f}")
    print(f"      Minimale Qualität: {result['global_min_quality']:.3f}")
    print(
        f"      Gesamt-Energieverbrauch: {result['total_energy_consumption']:.1f} kWh"
    )
    print(
        f"      Durchschnittliche Temperatur: {result['weighted_avg_temperature']:.1f}°C"
    )
    print(f"      Maximale Vibration: {result['global_max_vibration']:.2f} mm/s")

    # Baseline-Vergleich
    baseline_start = time.time()

    total_cycles = len(production_data)
    all_cycle_times = [cycle["cycle_time"] for cycle in production_data]
    all_quality_scores = []
    for cycle in production_data:
        all_quality_scores.extend(cycle["quality_scores"])

    baseline_results = {
        "total_cycles": total_cycles,
        "avg_cycle_time": np.mean(all_cycle_times),
        "avg_quality": np.mean(all_quality_scores),
        "min_quality": np.min(all_quality_scores),
    }

    baseline_time = time.time() - baseline_start

    print("\n    Performance-Vergleich:")
    print(f"      MapReduce: {production_analytics['total_time']:.3f}s")
    print(f"      Sequential: {baseline_time:.3f}s")
    print(f"      Speedup: {baseline_time / production_analytics['total_time']:.1f}x")

    # Validierung
    cycle_time_error = abs(
        result["weighted_avg_cycle_time"] - baseline_results["avg_cycle_time"]
    )
    quality_error = abs(result["global_avg_quality"] - baseline_results["avg_quality"])

    print(f"      Cycle Time Error: {cycle_time_error:.6f}")
    print(f"      Quality Error: {quality_error:.6f}")

    duration = time.time() - start_time
    print(f"\n⚡ Distributed Computing in {duration:.3f} Sekunden")
    print("🌐 Distributed Computing ermöglicht Skalierung auf Cluster-Level!")
    print()


if __name__ == "__main__":
    main()
