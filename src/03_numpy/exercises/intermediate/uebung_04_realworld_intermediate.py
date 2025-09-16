#!/usr/bin/env python3
"""
NumPy Übung 4: Real-World Produktionsanalyse (Intermediate)
Bystronic Python Grundkurs - Kapitel 3

Diese Übung kombiniert alle Intermediate NumPy-Konzepte in einem realistischen
Bystronic-Produktionsszenario mit komplexen Multi-Dimensionalen Analysen.

Lernziele:
- Integration aller NumPy-Techniken in komplexen Anwendungen
- Multi-Source Datenintegration und -analyse
- Performance-kritische Echtzeit-Verarbeitung
- Statistische Prozesskontrolle (SPC) auf Enterprise-Level
- Predictive Analytics mit NumPy
- Production-Ready Code-Patterns

Schwierigkeitsgrad: 🟡 Intermediate
Geschätzte Bearbeitungszeit: 50-60 Minuten
"""

import json
import time
import warnings

import numpy as np

warnings.filterwarnings("ignore")


def main():
    """Hauptfunktion für Real-World Produktionsanalyse"""
    print("🎯 NUMPY INTERMEDIATE ÜBUNG 4: REAL-WORLD PRODUKTIONSANALYSE")
    print("=" * 75)
    print("Diese Übung simuliert eine vollständige Bystronic-Produktionsumgebung")
    print("mit Multi-Maschinen, Multi-Sensoren und Echtzeit-Qualitätskontrolle.")
    print()

    try:
        # Aufgabe 1: Multi-Source Datenintegration
        aufgabe_1_datenintegration()

        # Aufgabe 2: Echtzeit-Qualitätskontrolle
        aufgabe_2_echtzeit_qualitaetskontrolle()

        # Aufgabe 3: Predictive Maintenance
        aufgabe_3_predictive_maintenance()

        # Aufgabe 4: Performance-Dashboard
        aufgabe_4_performance_dashboard()

        # Aufgabe 5: Enterprise-SPC System
        aufgabe_5_enterprise_spc()

        print("\n" + "🎉" * 70)
        print("🎉 ALLE REAL-WORLD PRODUKTIONSANALYSE-AUFGABEN ABGESCHLOSSEN! 🎉")
        print("🎉" * 70)
        print("\n📋 BEHERRSCHTE KONZEPTE:")
        print("✅ Multi-Source Datenintegration mit komplexen Arrays")
        print("✅ Echtzeit-Verarbeitung mit Streaming-Algorithmen")
        print("✅ Predictive Analytics und Anomalie-Detektion")
        print("✅ Enterprise-Level Statistical Process Control")
        print("✅ Performance-optimierte Production-Code-Patterns")
        print("✅ Multi-dimensionale Korrelationsanalyse")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler in der Übung: {e}")
        print("💡 Tipp: In Production-Umgebungen sind robuste Error-Handling kritisch!")


class ProductionDataSimulator:
    """Simulator für realistische Bystronic-Produktionsdaten"""

    def __init__(self, n_machines=8, n_sensors_per_machine=12):
        self.n_machines = n_machines
        self.n_sensors_per_machine = n_sensors_per_machine
        self.sensor_config = self._initialize_sensor_config()
        np.random.seed(42)  # Für reproduzierbare Ergebnisse

    def _initialize_sensor_config(self):
        """Konfiguriere realistische Sensor-Parameter"""
        sensor_types = {
            "temperature": {"unit": "°C", "range": (60, 80), "noise": 1.5},
            "vibration_x": {"unit": "mm/s", "range": (2, 8), "noise": 0.3},
            "vibration_y": {"unit": "mm/s", "range": (2, 8), "noise": 0.3},
            "vibration_z": {"unit": "mm/s", "range": (1, 5), "noise": 0.2},
            "spindle_current": {"unit": "A", "range": (15, 45), "noise": 2.0},
            "feed_force": {"unit": "N", "range": (100, 800), "noise": 20},
            "hydraulic_pressure": {"unit": "bar", "range": (180, 220), "noise": 5},
            "coolant_flow": {"unit": "l/min", "range": (8, 12), "noise": 0.5},
            "acoustic_emission": {"unit": "dB", "range": (60, 85), "noise": 3},
            "power_consumption": {"unit": "kW", "range": (25, 65), "noise": 3},
            "tool_wear": {"unit": "μm", "range": (0, 100), "noise": 2},
            "surface_roughness": {"unit": "μm", "range": (0.8, 3.2), "noise": 0.1},
        }

        return sensor_types

    def generate_production_cycle(self, cycle_duration_minutes=45, sampling_rate_hz=10):
        """Generiere einen vollständigen Produktionszyklus"""
        n_samples = int(cycle_duration_minutes * 60 * sampling_rate_hz)
        time_stamps = np.linspace(0, cycle_duration_minutes * 60, n_samples)

        # Multi-dimensionales Array: (machines, sensors, time_samples)
        sensor_data = np.zeros((self.n_machines, self.n_sensors_per_machine, n_samples))

        sensor_names = list(self.sensor_config.keys())

        for machine_idx in range(self.n_machines):
            # Maschinen-spezifische Eigenschaften
            machine_efficiency = 0.85 + 0.15 * np.random.random()  # 85-100% Effizienz
            machine_age_factor = (
                1 + machine_idx * 0.02
            )  # Ältere Maschinen = mehr Variation

            for sensor_idx, sensor_name in enumerate(sensor_names):
                config = self.sensor_config[sensor_name]

                # Basis-Signal mit verschiedenen Komponenten
                base_value = np.mean(config["range"])

                # 1. Zyklische Komponenten (Produktionszyklen)
                main_cycle = (
                    0.1
                    * base_value
                    * np.sin(2 * np.pi * time_stamps / (cycle_duration_minutes * 60))
                )
                fast_cycle = (
                    0.05 * base_value * np.sin(2 * np.pi * time_stamps / 120)
                )  # 2-Minuten Zyklen

                # 2. Trend-Komponenten (Verschleiß, Aufwärmung)
                warmup_trend = (
                    0.05 * base_value * (1 - np.exp(-time_stamps / 600))
                )  # 10min Aufwärmung
                wear_trend = (
                    0.02 * base_value * time_stamps / (cycle_duration_minutes * 60)
                )  # Leichter Verschleiß

                # 3. Maschinen-spezifische Abweichungen
                machine_offset = (machine_efficiency - 0.925) * base_value * 0.5
                machine_noise_scale = machine_age_factor

                # 4. Sensor-spezifische Effekte
                if "vibration" in sensor_name:
                    # Vibration korreliert mit Spindelstrom
                    spindle_correlation = 0.3 * base_value * np.random.random()
                elif sensor_name == "temperature":
                    # Temperatur steigt mit Zeit und Leistung
                    warmup_trend *= 2
                elif sensor_name == "tool_wear":
                    # Werkzeugverschleiß akkumuliert
                    wear_trend = (
                        0.1
                        * base_value
                        * (time_stamps / (cycle_duration_minutes * 60)) ** 1.5
                    )

                # 5. Rauschen
                noise = (
                    config["noise"] * machine_noise_scale * np.random.randn(n_samples)
                )

                # Kombiniere alle Komponenten
                signal = (
                    base_value
                    + main_cycle
                    + fast_cycle
                    + warmup_trend
                    + wear_trend
                    + machine_offset
                    + noise
                )

                # Clipping auf realistische Bereiche
                signal = np.clip(
                    signal, config["range"][0] * 0.8, config["range"][1] * 1.2
                )

                sensor_data[machine_idx, sensor_idx, :] = signal

        return {
            "data": sensor_data,
            "timestamps": time_stamps,
            "sensor_names": sensor_names,
            "machine_ids": [f"CNC-{i + 1:02d}" for i in range(self.n_machines)],
            "sampling_rate": sampling_rate_hz,
            "cycle_duration": cycle_duration_minutes,
        }


def aufgabe_1_datenintegration():
    """Aufgabe 1: Multi-Source Datenintegration und -synchronisation"""
    print("🎯 AUFGABE 1: MULTI-SOURCE DATENINTEGRATION")
    print("-" * 50)
    print("Ziel: Integriere Daten von verschiedenen Quellen mit unterschiedlichen")
    print("Sampling-Raten und synchronisiere sie für gemeinsame Analyse")
    print()

    start_time = time.time()

    # 1.1 Generiere Multi-Source Daten
    print("📊 1.1 Multi-Source Datenquellen generieren:")

    simulator = ProductionDataSimulator(n_machines=6, n_sensors_per_machine=12)

    # Verschiedene Datenquellen mit unterschiedlichen Eigenschaften
    data_sources = {
        "realtime_sensors": {
            "rate": 10,  # 10 Hz
            "duration": 30,  # 30 Minuten
            "description": "Hochfrequente Sensor-Daten",
        },
        "quality_measurements": {
            "rate": 1 / 60,  # Alle 60 Sekunden
            "duration": 30,
            "description": "Qualitätsmessungen",
        },
        "production_logs": {
            "rate": 1 / 300,  # Alle 5 Minuten
            "duration": 30,
            "description": "Produktions-Events",
        },
    }

    integrated_data = {}

    for source_name, config in data_sources.items():
        print(f"  Generiere {source_name}:")
        print(f"    Sampling-Rate: {config['rate']} Hz")
        print(f"    Dauer: {config['duration']} Minuten")

        if source_name == "realtime_sensors":
            # Hochfrequente Sensordaten
            cycle_data = simulator.generate_production_cycle(
                config["duration"], config["rate"]
            )
            integrated_data[source_name] = cycle_data

        elif source_name == "quality_measurements":
            # Weniger häufige Qualitätsmessungen
            n_measurements = int(config["duration"] * 60 * config["rate"])
            timestamps = np.linspace(0, config["duration"] * 60, n_measurements)

            # Qualitätsparameter für alle Maschinen
            quality_metrics = {
                "dimensional_accuracy": np.random.normal(
                    0.02, 0.01, (6, n_measurements)
                ),  # mm Abweichung
                "surface_finish": np.random.normal(
                    1.6, 0.3, (6, n_measurements)
                ),  # μm Ra
                "roundness_error": np.random.normal(
                    0.005, 0.002, (6, n_measurements)
                ),  # mm
                "part_temperature": np.random.normal(25, 2, (6, n_measurements)),  # °C
            }

            integrated_data[source_name] = {
                "data": quality_metrics,
                "timestamps": timestamps,
                "sampling_rate": config["rate"],
            }

        elif source_name == "production_logs":
            # Event-basierte Produktionsdaten
            n_events = int(config["duration"] * 60 * config["rate"])
            timestamps = np.linspace(0, config["duration"] * 60, n_events)

            # Produktions-Events
            events_data = {
                "parts_completed": np.random.poisson(
                    25, (6, n_events)
                ),  # Teile pro Periode
                "cycle_times": np.random.normal(120, 15, (6, n_events)),  # Sekunden
                "tool_changes": np.random.poisson(0.1, (6, n_events)),  # Binär (0/1)
                "alarm_counts": np.random.poisson(0.05, (6, n_events)),  # Alarme
            }

            integrated_data[source_name] = {
                "data": events_data,
                "timestamps": timestamps,
                "sampling_rate": config["rate"],
            }

        print(f"    ✓ {source_name} generiert")

    # 1.2 Daten-Synchronisation
    print("\n📊 1.2 Daten-Synchronisation auf gemeinsame Zeitbasis:")

    # Definiere gemeinsame Zeitbasis (niedrigste Auflösung)
    target_rate = 1 / 60  # Jede Minute
    duration = 30 * 60  # 30 Minuten in Sekunden
    common_timestamps = np.arange(0, duration + 1, 1 / target_rate)

    print(f"  Ziel-Zeitbasis: {len(common_timestamps)} Samples @ {target_rate:.4f} Hz")

    synchronized_data = {}

    for source_name, source_data in integrated_data.items():
        print(f"\n  Synchronisiere {source_name}:")

        source_timestamps = source_data["timestamps"]
        synchronized_data[source_name] = {"timestamps": common_timestamps}

        if source_name == "realtime_sensors":
            # Downsample hochfrequente Sensordaten
            sensor_data = source_data["data"]  # Shape: (machines, sensors, samples)

            # Für jede Maschine und jeden Sensor
            downsampled_data = np.zeros(
                (
                    sensor_data.shape[0],  # machines
                    sensor_data.shape[1],  # sensors
                    len(common_timestamps),  # new time samples
                )
            )

            for machine_idx in range(sensor_data.shape[0]):
                for sensor_idx in range(sensor_data.shape[1]):
                    # Interpolation auf neue Zeitbasis
                    downsampled_data[machine_idx, sensor_idx, :] = np.interp(
                        common_timestamps,
                        source_timestamps,
                        sensor_data[machine_idx, sensor_idx, :],
                    )

            synchronized_data[source_name]["data"] = downsampled_data
            synchronized_data[source_name]["sensor_names"] = source_data["sensor_names"]

            print(
                f"    Downsampled von {sensor_data.shape[2]} auf {downsampled_data.shape[2]} Samples"
            )

        else:
            # Upsample niederfrequente Daten
            data_dict = source_data["data"]
            resampled_dict = {}

            for metric_name, metric_data in data_dict.items():
                # metric_data Shape: (machines, original_samples)
                resampled_data = np.zeros(
                    (metric_data.shape[0], len(common_timestamps))
                )

                for machine_idx in range(metric_data.shape[0]):
                    resampled_data[machine_idx, :] = np.interp(
                        common_timestamps,
                        source_timestamps,
                        metric_data[machine_idx, :],
                    )

                resampled_dict[metric_name] = resampled_data

            synchronized_data[source_name]["data"] = resampled_dict

            print(
                f"    Upsampled von {metric_data.shape[1]} auf {len(common_timestamps)} Samples"
            )

    # 1.3 Cross-Source Korrelationsanalyse
    print("\n📊 1.3 Cross-Source Korrelationsanalyse:")

    # Kombiniere verschiedene Metriken für Korrelationsanalyse
    correlation_metrics = {}

    # Sensor-Daten: Mittlere Vibration und Temperatur pro Maschine
    sensor_data = synchronized_data["realtime_sensors"]["data"]
    sensor_names = synchronized_data["realtime_sensors"]["sensor_names"]

    # Finde relevante Sensoren
    temp_idx = sensor_names.index("temperature")
    vibration_x_idx = sensor_names.index("vibration_x")
    power_idx = sensor_names.index("power_consumption")

    for machine_idx in range(sensor_data.shape[0]):
        machine_id = f"CNC-{machine_idx + 1:02d}"

        correlation_metrics[f"{machine_id}_temperature"] = sensor_data[
            machine_idx, temp_idx, :
        ]
        correlation_metrics[f"{machine_id}_vibration"] = sensor_data[
            machine_idx, vibration_x_idx, :
        ]
        correlation_metrics[f"{machine_id}_power"] = sensor_data[
            machine_idx, power_idx, :
        ]

    # Qualitätsdaten hinzufügen
    quality_data = synchronized_data["quality_measurements"]["data"]
    for machine_idx in range(6):
        machine_id = f"CNC-{machine_idx + 1:02d}"
        correlation_metrics[f"{machine_id}_surface_finish"] = quality_data[
            "surface_finish"
        ][machine_idx, :]
        correlation_metrics[f"{machine_id}_accuracy"] = quality_data[
            "dimensional_accuracy"
        ][machine_idx, :]

    # Produktionsdaten hinzufügen
    production_data = synchronized_data["production_logs"]["data"]
    for machine_idx in range(6):
        machine_id = f"CNC-{machine_idx + 1:02d}"
        correlation_metrics[f"{machine_id}_cycle_time"] = production_data[
            "cycle_times"
        ][machine_idx, :]

    # Berechne Korrelationsmatrix
    metric_names = list(correlation_metrics.keys())
    metric_values = np.array([correlation_metrics[name] for name in metric_names])

    correlation_matrix = np.corrcoef(metric_values)

    print(
        f"  Korrelationsmatrix: {len(metric_names)} Metriken × {len(metric_names)} Metriken"
    )

    # Finde stärkste Korrelationen (Cross-Source)
    interesting_correlations = []

    for i, name1 in enumerate(metric_names):
        for j, name2 in enumerate(metric_names[i + 1 :], i + 1):
            corr_value = correlation_matrix[i, j]

            # Nur Cross-Source und starke Korrelationen
            source1 = name1.split("_")[1]  # temperature, vibration, etc.
            source2 = name2.split("_")[1]

            if abs(corr_value) > 0.3 and source1 != source2:
                interesting_correlations.append((name1, name2, corr_value))

    # Sortiere nach Korrelationsstärke
    interesting_correlations.sort(key=lambda x: abs(x[2]), reverse=True)

    print("\n  Top Cross-Source Korrelationen:")
    for i, (metric1, metric2, corr) in enumerate(interesting_correlations[:8]):
        machine1 = metric1.split("_")[0]
        machine2 = metric2.split("_")[0]
        type1 = "_".join(metric1.split("_")[1:])
        type2 = "_".join(metric2.split("_")[1:])

        if machine1 == machine2:  # Gleiche Maschine
            print(f"    {i + 1:2d}. {machine1}: {type1} ↔ {type2} (r={corr:+.3f})")

    duration = time.time() - start_time
    print(f"\n⚡ Datenintegration in {duration:.3f} Sekunden")
    print(
        f"📊 {len(synchronized_data)} Datenquellen mit {len(common_timestamps)} Zeitpunkten synchronisiert"
    )
    print()

    return synchronized_data


def aufgabe_2_echtzeit_qualitaetskontrolle():
    """Aufgabe 2: Echtzeit-Qualitätskontrolle mit Streaming-Algorithmen"""
    print("🎯 AUFGABE 2: ECHTZEIT-QUALITÄTSKONTROLLE")
    print("-" * 45)
    print("Ziel: Implementiere Streaming-Algorithmen für kontinuierliche")
    print("Qualitätskontrolle ohne Speicherung aller Daten")
    print()

    start_time = time.time()

    # 2.1 Streaming Statistics Implementierung
    print("📊 2.1 Streaming Statistics für kontinuierliche QK:")

    class StreamingQualityControl:
        """Streaming-basierte Qualitätskontrolle"""

        def __init__(self, window_size=100, control_limits_sigma=3):
            self.window_size = window_size
            self.control_limits_sigma = control_limits_sigma

            # Streaming-Statistiken
            self.count = 0
            self.sum = 0
            self.sum_squares = 0
            self.min_value = float("inf")
            self.max_value = float("-inf")

            # Sliding window für advanced statistics
            self.window_buffer = np.full(window_size, np.nan)
            self.buffer_index = 0
            self.buffer_full = False

            # Control chart parameters
            self.target_value = None
            self.control_limits = None

            # Alarm tracking
            self.consecutive_alarms = 0
            self.alarm_history = []

        def update(self, value):
            """Update mit neuem Messwert"""
            # Basic streaming statistics
            self.count += 1
            self.sum += value
            self.sum_squares += value**2
            self.min_value = min(self.min_value, value)
            self.max_value = max(self.max_value, value)

            # Update sliding window
            self.window_buffer[self.buffer_index] = value
            self.buffer_index = (self.buffer_index + 1) % self.window_size

            if self.buffer_index == 0 and not self.buffer_full:
                self.buffer_full = True

            return self.check_control_limits(value)

        def get_current_stats(self):
            """Aktuelle Statistiken abrufen"""
            if self.count == 0:
                return None

            mean = self.sum / self.count
            variance = (self.sum_squares / self.count) - mean**2
            std = np.sqrt(max(0, variance))

            # Window-basierte Statistiken
            valid_window = self.window_buffer[~np.isnan(self.window_buffer)]
            window_mean = np.mean(valid_window) if len(valid_window) > 0 else mean
            window_std = np.std(valid_window, ddof=1) if len(valid_window) > 1 else std

            return {
                "count": self.count,
                "mean": mean,
                "std": std,
                "min": self.min_value,
                "max": self.max_value,
                "window_mean": window_mean,
                "window_std": window_std,
                "range": self.max_value - self.min_value,
            }

        def initialize_control_limits(self, target_value, tolerance):
            """Initialisiere Kontrollgrenzen"""
            self.target_value = target_value
            self.control_limits = {
                "target": target_value,
                "ucl": target_value + tolerance,  # Upper Control Limit
                "lcl": target_value - tolerance,  # Lower Control Limit
                "usl": target_value + tolerance * 1.5,  # Upper Spec Limit
                "lsl": target_value - tolerance * 1.5,  # Lower Spec Limit
            }

        def check_control_limits(self, value):
            """Prüfe Kontrollgrenzen und generiere Alarme"""
            if self.control_limits is None:
                return None

            alarms = []

            # Spezifikationsgrenzen (kritisch)
            if value > self.control_limits["usl"]:
                alarms.append(
                    {"type": "SPEC_HIGH", "severity": "CRITICAL", "value": value}
                )
            elif value < self.control_limits["lsl"]:
                alarms.append(
                    {"type": "SPEC_LOW", "severity": "CRITICAL", "value": value}
                )

            # Kontrollgrenzen (Warnung)
            elif value > self.control_limits["ucl"]:
                alarms.append(
                    {"type": "CONTROL_HIGH", "severity": "WARNING", "value": value}
                )
            elif value < self.control_limits["lcl"]:
                alarms.append(
                    {"type": "CONTROL_LOW", "severity": "WARNING", "value": value}
                )

            # Trend-Erkennung (wenn genug Daten im Window)
            if self.buffer_full:
                trend_alarm = self._check_trends()
                if trend_alarm:
                    alarms.append(trend_alarm)

            # Update Alarm-Tracking
            if alarms:
                self.consecutive_alarms += 1
                self.alarm_history.extend(alarms)
            else:
                self.consecutive_alarms = 0

            return alarms

        def _check_trends(self):
            """Erkenne Trends im Sliding Window"""
            valid_data = self.window_buffer[~np.isnan(self.window_buffer)]

            if len(valid_data) < 7:  # Mindestens 7 Punkte für Trend
                return None

            # Lineare Regression für Trend-Detektion
            x = np.arange(len(valid_data))
            slope = np.polyfit(x, valid_data, 1)[0]

            # Trend-Schwellwerte (relativ zur Standardabweichung)
            std_threshold = np.std(valid_data) * 0.1

            if abs(slope) > std_threshold:
                return {
                    "type": "TREND_DETECTED",
                    "severity": "INFO",
                    "slope": slope,
                    "direction": "INCREASING" if slope > 0 else "DECREASING",
                }

            return None

        def get_process_capability(self):
            """Berechne Prozessfähigkeiten Cp und Cpk"""
            if self.control_limits is None or self.count < 10:
                return None

            stats = self.get_current_stats()
            if stats["std"] == 0:
                return None

            # Toleranzbereich
            tolerance = self.control_limits["usl"] - self.control_limits["lsl"]

            # Cp (Prozessfähigkeit)
            cp = tolerance / (6 * stats["std"])

            # Cpk (berücksichtigt Zentrierung)
            target = self.control_limits["target"]
            cpk_upper = (self.control_limits["usl"] - stats["mean"]) / (
                3 * stats["std"]
            )
            cpk_lower = (stats["mean"] - self.control_limits["lsl"]) / (
                3 * stats["std"]
            )
            cpk = min(cpk_upper, cpk_lower)

            return {
                "cp": cp,
                "cpk": cpk,
                "cp_grade": self._grade_capability(cp),
                "cpk_grade": self._grade_capability(cpk),
            }

        def _grade_capability(self, value):
            """Bewerte Prozessfähigkeit"""
            if value >= 2.0:
                return "EXCELLENT"
            elif value >= 1.67:
                return "GOOD"
            elif value >= 1.33:
                return "ADEQUATE"
            elif value >= 1.0:
                return "MARGINAL"
            else:
                return "INADEQUATE"

    # Test der Streaming-QK mit simulierten Daten
    print("  Test mit simulierten Messdaten:")

    # Simuliere kontinuierliche Messungen (z.B. Durchmesser)
    np.random.seed(42)
    n_measurements = 1000
    target_diameter = 25.0  # mm
    tolerance = 0.1  # ±0.1 mm

    qc_controller = StreamingQualityControl(window_size=50)
    qc_controller.initialize_control_limits(target_diameter, tolerance)

    print(f"    Zielwert: {target_diameter:.1f} ± {tolerance:.1f} mm")
    print(f"    Streaming Window: {qc_controller.window_size} Messungen")

    # Simuliere verschiedene Prozess-Phasen
    measurements = []
    all_alarms = []

    for i in range(n_measurements):
        # Verschiedene Prozess-Bedingungen simulieren
        if i < 200:
            # Normale Produktion
            measurement = np.random.normal(target_diameter, 0.03)
        elif i < 400:
            # Drift-Szenario
            drift = (i - 200) * 0.0002
            measurement = np.random.normal(target_diameter + drift, 0.03)
        elif i < 600:
            # Erhöhte Variabilität
            measurement = np.random.normal(target_diameter, 0.06)
        elif i < 800:
            # Offset-Fehler
            measurement = np.random.normal(target_diameter + 0.05, 0.03)
        else:
            # Zurück zur normalen Produktion
            measurement = np.random.normal(target_diameter, 0.03)

        measurements.append(measurement)

        # Update Streaming-QK
        alarms = qc_controller.update(measurement)
        if alarms:
            all_alarms.extend([(i, alarm) for alarm in alarms])

        # Periodische Berichte
        if (i + 1) % 200 == 0:
            stats = qc_controller.get_current_stats()
            capability = qc_controller.get_process_capability()

            print(f"\n    Nach {i + 1:4d} Messungen:")
            print(f"      Mittelwert: {stats['mean']:.4f} mm")
            print(f"      Std.-Abw.: {stats['std']:.4f} mm")
            print(f"      Bereich: {stats['min']:.4f} - {stats['max']:.4f} mm")

            if capability:
                print(f"      Cp: {capability['cp']:.2f} ({capability['cp_grade']})")
                print(f"      Cpk: {capability['cpk']:.2f} ({capability['cpk_grade']})")

            recent_alarms = [alarm for idx, alarm in all_alarms if idx >= i - 199]
            print(f"      Alarme (letzte 200): {len(recent_alarms)}")

    # 2.2 Multi-Stream Qualitätskontrolle
    print("\n📊 2.2 Multi-Stream Qualitätskontrolle:")

    class MultiStreamQC:
        """Qualitätskontrolle für mehrere Datenströme"""

        def __init__(self, stream_configs):
            self.streams = {}
            self.correlations = {}

            for stream_name, config in stream_configs.items():
                self.streams[stream_name] = StreamingQualityControl(
                    window_size=config.get("window_size", 50)
                )
                if "target" in config and "tolerance" in config:
                    self.streams[stream_name].initialize_control_limits(
                        config["target"], config["tolerance"]
                    )

            self.stream_names = list(stream_configs.keys())
            self.correlation_window = np.full((len(self.stream_names), 100), np.nan)
            self.correlation_index = 0

        def update_all_streams(self, measurements_dict):
            """Update alle Streams mit neuen Messungen"""
            all_alarms = {}

            # Update einzelne Streams
            for stream_name, value in measurements_dict.items():
                if stream_name in self.streams:
                    alarms = self.streams[stream_name].update(value)
                    if alarms:
                        all_alarms[stream_name] = alarms

            # Update Korrelationen
            self._update_correlations(measurements_dict)

            # Cross-Stream Anomalie-Detektion
            cross_alarms = self._check_cross_stream_anomalies(measurements_dict)
            if cross_alarms:
                all_alarms["cross_stream"] = cross_alarms

            return all_alarms

        def _update_correlations(self, measurements_dict):
            """Update Korrelationen zwischen Streams"""
            for i, stream_name in enumerate(self.stream_names):
                if stream_name in measurements_dict:
                    self.correlation_window[i, self.correlation_index] = (
                        measurements_dict[stream_name]
                    )

            self.correlation_index = (self.correlation_index + 1) % 100

        def _check_cross_stream_anomalies(self, measurements_dict):
            """Prüfe Cross-Stream Anomalien"""
            # Vereinfachte Implementierung: Ungewöhnliche Korrelationsmuster
            valid_data = self.correlation_window[
                :, ~np.isnan(self.correlation_window).any(axis=0)
            ]

            if valid_data.shape[1] < 20:  # Nicht genug Daten
                return None

            # Berechne aktuelle Korrelationen
            current_corr = np.corrcoef(valid_data)

            # Hier könnten komplexere Anomalie-Detektions-Algorithmen implementiert werden
            # Für Demo: Prüfe auf ungewöhnlich hohe/niedrige Korrelationen

            anomalies = []
            for i in range(len(self.stream_names)):
                for j in range(i + 1, len(self.stream_names)):
                    corr_value = current_corr[i, j]
                    if abs(corr_value) > 0.9:  # Ungewöhnlich hohe Korrelation
                        anomalies.append(
                            {
                                "type": "HIGH_CORRELATION",
                                "streams": [self.stream_names[i], self.stream_names[j]],
                                "correlation": corr_value,
                            }
                        )

            return anomalies if anomalies else None

        def get_dashboard_summary(self):
            """Erstelle Dashboard-Zusammenfassung"""
            summary = {}

            for stream_name, qc in self.streams.items():
                stats = qc.get_current_stats()
                capability = qc.get_process_capability()

                if stats:
                    summary[stream_name] = {
                        "current_value": self.correlation_window[
                            self.stream_names.index(stream_name),
                            (self.correlation_index - 1) % 100,
                        ],
                        "mean": stats["mean"],
                        "std": stats["std"],
                        "count": stats["count"],
                        "capability": capability,
                        "alarm_count": len(qc.alarm_history),
                        "consecutive_alarms": qc.consecutive_alarms,
                    }

            return summary

    # Test Multi-Stream QC
    stream_configs = {
        "diameter": {"target": 25.0, "tolerance": 0.1, "window_size": 50},
        "length": {"target": 100.0, "tolerance": 0.5, "window_size": 50},
        "surface_roughness": {"target": 1.6, "tolerance": 0.4, "window_size": 30},
        "roundness": {"target": 0.005, "tolerance": 0.002, "window_size": 40},
    }

    multi_qc = MultiStreamQC(stream_configs)

    print(f"  Multi-Stream Setup: {len(stream_configs)} Qualitätsmerkmale")
    for name, config in stream_configs.items():
        print(f"    {name}: {config['target']} ± {config['tolerance']}")

    # Simuliere korrelierte Multi-Stream Daten
    n_parts = 500
    total_alarms = 0

    for part_idx in range(n_parts):
        # Simuliere korrelierte Messungen
        base_quality = np.random.normal(0, 1)  # Gemeinsamer Qualitätsfaktor

        measurements = {
            "diameter": 25.0 + 0.02 * base_quality + np.random.normal(0, 0.03),
            "length": 100.0 + 0.1 * base_quality + np.random.normal(0, 0.2),
            "surface_roughness": 1.6 - 0.1 * base_quality + np.random.normal(0, 0.1),
            "roundness": 0.005 + 0.001 * base_quality + np.random.normal(0, 0.001),
        }

        # Update Multi-Stream QC
        alarms = multi_qc.update_all_streams(measurements)
        if alarms:
            total_alarms += sum(
                len(alarm_list) if isinstance(alarm_list, list) else 1
                for alarm_list in alarms.values()
            )

        # Periodische Berichte
        if (part_idx + 1) % 100 == 0:
            summary = multi_qc.get_dashboard_summary()
            print(f"\n    Nach {part_idx + 1:3d} Teilen:")

            for stream_name, data in summary.items():
                if not np.isnan(data["current_value"]):
                    grade = (
                        data["capability"]["cpk_grade"] if data["capability"] else "N/A"
                    )
                    print(
                        f"      {stream_name:15s}: {data['current_value']:.4f} "
                        f"(μ={data['mean']:.4f}, Cpk={grade})"
                    )

    print(
        f"\n  Gesamt-Alarme: {total_alarms} in {n_parts} Teilen ({total_alarms / n_parts * 100:.1f}%)"
    )

    duration = time.time() - start_time
    print(f"\n⚡ Echtzeit-QK in {duration:.3f} Sekunden")
    print(
        "📊 Streaming-QK ermöglicht kontinuierliche Überwachung ohne Memory-Overhead!"
    )
    print()

    return multi_qc


def aufgabe_3_predictive_maintenance():
    """Aufgabe 3: Predictive Maintenance mit Anomalie-Detektion"""
    print("🎯 AUFGABE 3: PREDICTIVE MAINTENANCE")
    print("-" * 40)
    print("Ziel: Implementiere Predictive Analytics für Maschinenwartung")
    print("basierend auf Sensor-Trends und Anomalie-Erkennung")
    print()

    start_time = time.time()

    # 3.1 Anomalie-Detektion Algorithmen
    print("📊 3.1 Anomalie-Detektion Implementierung:")

    class AnomalyDetector:
        """Multi-Method Anomalie-Detektor"""

        def __init__(self, methods=["zscore", "iqr", "isolation"]):
            self.methods = methods
            self.baselines = {}
            self.history = []

        def fit_baseline(self, data, window_size=1000):
            """Lerne normale Basislinie"""
            if len(data) < window_size:
                baseline_data = data
            else:
                baseline_data = data[-window_size:]

            self.baselines = {
                "mean": np.mean(baseline_data),
                "std": np.std(baseline_data),
                "q25": np.percentile(baseline_data, 25),
                "q75": np.percentile(baseline_data, 75),
                "iqr": np.percentile(baseline_data, 75)
                - np.percentile(baseline_data, 25),
                "median": np.median(baseline_data),
            }

        def detect_anomalies(self, new_data):
            """Erkenne Anomalien in neuen Daten"""
            if not self.baselines:
                raise ValueError(
                    "Baseline muss erst mit fit_baseline() erstellt werden"
                )

            anomalies = {}

            if "zscore" in self.methods:
                anomalies["zscore"] = self._zscore_detection(new_data)

            if "iqr" in self.methods:
                anomalies["iqr"] = self._iqr_detection(new_data)

            if "isolation" in self.methods:
                anomalies["isolation"] = self._isolation_detection(new_data)

            # Kombiniere Ergebnisse
            combined_score = self._combine_anomaly_scores(anomalies)

            return {
                "individual_scores": anomalies,
                "combined_score": combined_score,
                "is_anomaly": combined_score > 0.7,  # Threshold
            }

        def _zscore_detection(self, data):
            """Z-Score basierte Anomalie-Detektion"""
            if self.baselines["std"] == 0:
                return np.zeros_like(data)

            z_scores = np.abs((data - self.baselines["mean"]) / self.baselines["std"])
            return np.where(z_scores > 3, z_scores / 10, 0)  # Normalisiere auf 0-1

        def _iqr_detection(self, data):
            """IQR-basierte Anomalie-Detektion"""
            q25, q75 = self.baselines["q25"], self.baselines["q75"]
            iqr = self.baselines["iqr"]

            lower_bound = q25 - 1.5 * iqr
            upper_bound = q75 + 1.5 * iqr

            # Normalisierte Anomalie-Scores
            scores = np.zeros_like(data)
            outlier_mask = (data < lower_bound) | (data > upper_bound)

            if np.any(outlier_mask):
                # Distanz zur nächsten Grenze, normalisiert
                lower_dist = np.abs(data - lower_bound) / iqr
                upper_dist = np.abs(data - upper_bound) / iqr
                min_dist = np.minimum(lower_dist, upper_dist)
                scores[outlier_mask] = np.clip(min_dist[outlier_mask] / 5, 0, 1)

            return scores

        def _isolation_detection(self, data):
            """Vereinfachte Isolation Forest Anomalie-Detektion"""
            # Für Demo: Simplified version basierend auf lokaler Dichte
            scores = np.zeros_like(data)

            for i, value in enumerate(data):
                # Lokale Nachbarschaft im Baseline
                baseline_data = np.array([self.baselines["mean"]])  # Vereinfacht

                # Berechne lokale Dichte (vereinfacht)
                distances = np.abs(value - baseline_data)
                min_distance = np.min(distances)

                # Normalisiere basierend auf typischer Varianz
                normalized_distance = min_distance / (self.baselines["std"] + 1e-10)
                scores[i] = np.clip(normalized_distance / 5, 0, 1)

            return scores

        def _combine_anomaly_scores(self, anomaly_dict):
            """Kombiniere verschiedene Anomalie-Scores"""
            if not anomaly_dict:
                return np.array([0])

            # Gewichteter Durchschnitt
            weights = {"zscore": 0.4, "iqr": 0.3, "isolation": 0.3}
            combined = np.zeros_like(list(anomaly_dict.values())[0])

            total_weight = 0
            for method, scores in anomaly_dict.items():
                if method in weights:
                    combined += weights[method] * scores
                    total_weight += weights[method]

            return combined / total_weight if total_weight > 0 else combined

    # 3.2 Degradation Trend Analysis
    print("  Verschleiß-Trend Analyse:")

    class DegradationAnalyzer:
        """Analysiere Verschleiß-Trends für Predictive Maintenance"""

        def __init__(self, trend_window=200):
            self.trend_window = trend_window
            self.degradation_models = {}

        def analyze_degradation(self, sensor_data, sensor_name):
            """Analysiere Verschleiß-Trend eines Sensors"""
            if len(sensor_data) < 20:
                return None

            # Verwende gleitenden Trend
            if len(sensor_data) > self.trend_window:
                recent_data = sensor_data[-self.trend_window :]
                time_points = np.arange(len(recent_data))
            else:
                recent_data = sensor_data
                time_points = np.arange(len(recent_data))

            # Verschiedene Trend-Modelle fitten
            models = {}

            # Linearer Trend
            if len(recent_data) >= 2:
                linear_coeffs = np.polyfit(time_points, recent_data, 1)
                linear_trend = linear_coeffs[0]  # Steigung
                linear_r2 = self._calculate_r_squared(
                    recent_data, np.polyval(linear_coeffs, time_points)
                )
                models["linear"] = {"slope": linear_trend, "r2": linear_r2}

            # Exponentieller Trend (für beschleunigte Verschleiß)
            if len(recent_data) >= 3 and np.all(recent_data > 0):
                try:
                    log_data = np.log(recent_data)
                    exp_coeffs = np.polyfit(time_points, log_data, 1)
                    exp_rate = exp_coeffs[0]  # Exponentialrate
                    exp_pred = np.exp(np.polyval(exp_coeffs, time_points))
                    exp_r2 = self._calculate_r_squared(recent_data, exp_pred)
                    models["exponential"] = {"rate": exp_rate, "r2": exp_r2}
                except:
                    models["exponential"] = {"rate": 0, "r2": 0}

            # Wähle bestes Modell
            best_model = (
                max(models.keys(), key=lambda k: models[k]["r2"])
                if models
                else "linear"
            )

            # Berechne Verschleiß-Score
            degradation_score = self._calculate_degradation_score(models, recent_data)

            # Vorhersage für Wartungsplanung
            maintenance_prediction = self._predict_maintenance_need(
                models[best_model], recent_data
            )

            self.degradation_models[sensor_name] = {
                "models": models,
                "best_model": best_model,
                "degradation_score": degradation_score,
                "maintenance_prediction": maintenance_prediction,
                "last_update": len(sensor_data),
            }

            return self.degradation_models[sensor_name]

        def _calculate_r_squared(self, actual, predicted):
            """Berechne R² Güte"""
            ss_res = np.sum((actual - predicted) ** 2)
            ss_tot = np.sum((actual - np.mean(actual)) ** 2)
            return 1 - (ss_res / ss_tot) if ss_tot > 0 else 0

        def _calculate_degradation_score(self, models, data):
            """Berechne Verschleiß-Score (0-1)"""
            if not models:
                return 0

            score = 0

            # Linear trend contribution
            if "linear" in models and models["linear"]["r2"] > 0.1:
                # Normalisiere Steigung relativ zu Datenbereich
                data_range = np.max(data) - np.min(data)
                normalized_slope = abs(models["linear"]["slope"]) / (data_range + 1e-10)
                score += 0.5 * min(normalized_slope * 10, 1) * models["linear"]["r2"]

            # Exponential trend contribution
            if "exponential" in models and models["exponential"]["r2"] > 0.1:
                exp_contribution = min(abs(models["exponential"]["rate"]) * 100, 1)
                score += 0.5 * exp_contribution * models["exponential"]["r2"]

            return min(score, 1.0)

        def _predict_maintenance_need(self, best_model, data):
            """Vorhersage Wartungsbedarf"""
            if not best_model or best_model["r2"] < 0.1:
                return {"days_until_maintenance": None, "confidence": "LOW"}

            # Vereinfachte Vorhersage
            current_value = data[-1]
            data_std = np.std(data)

            # Annahme: Wartung nötig bei 3σ Abweichung vom Normalwert
            normal_value = np.mean(
                data[: min(50, len(data))]
            )  # Erste 50 Werte als "normal"
            threshold = normal_value + 3 * data_std

            if "slope" in best_model and best_model["slope"] != 0:
                # Lineare Extrapolation
                samples_until_threshold = (threshold - current_value) / best_model[
                    "slope"
                ]
                days_until_maintenance = max(
                    0, samples_until_threshold / 24
                )  # Annahme: 24 Samples/Tag
            elif "rate" in best_model and best_model["rate"] > 0:
                # Exponentielle Extrapolation
                time_constant = 1 / best_model["rate"]
                days_until_maintenance = time_constant / 24
            else:
                days_until_maintenance = None

            # Confidence basierend auf R²
            if best_model["r2"] > 0.8:
                confidence = "HIGH"
            elif best_model["r2"] > 0.5:
                confidence = "MEDIUM"
            else:
                confidence = "LOW"

            return {
                "days_until_maintenance": days_until_maintenance,
                "confidence": confidence,
                "threshold_value": threshold,
                "current_value": current_value,
            }

        def get_maintenance_schedule(self):
            """Erstelle Wartungsplan für alle Sensoren"""
            schedule = []

            for sensor_name, analysis in self.degradation_models.items():
                prediction = analysis["maintenance_prediction"]

                if (
                    prediction["days_until_maintenance"] is not None
                    and prediction["days_until_maintenance"] < 30  # Nächste 30 Tage
                    and prediction["confidence"] in ["HIGH", "MEDIUM"]
                ):
                    schedule.append(
                        {
                            "sensor": sensor_name,
                            "days_until_maintenance": prediction[
                                "days_until_maintenance"
                            ],
                            "confidence": prediction["confidence"],
                            "degradation_score": analysis["degradation_score"],
                            "priority": (
                                "HIGH"
                                if prediction["days_until_maintenance"] < 7
                                else "MEDIUM"
                            ),
                        }
                    )

            # Sortiere nach Dringlichkeit
            schedule.sort(key=lambda x: x["days_until_maintenance"])
            return schedule

    # 3.3 Test mit simulierten Sensor-Daten
    print("\n  Test mit realitätenahen Verschleiß-Daten:")

    # Simuliere 3 verschiedene Sensoren mit unterschiedlichen Verschleiß-Patterns
    sensors_simulation = {
        "spindle_vibration": {
            "baseline": 5.0,
            "degradation_type": "linear",
            "degradation_rate": 0.01,  # pro Tag
            "noise_level": 0.3,
        },
        "bearing_temperature": {
            "baseline": 65.0,
            "degradation_type": "exponential",
            "degradation_rate": 0.001,
            "noise_level": 1.5,
        },
        "tool_wear": {
            "baseline": 10.0,
            "degradation_type": "accelerating",
            "degradation_rate": 0.005,
            "noise_level": 0.5,
        },
    }

    anomaly_detector = AnomalyDetector()
    degradation_analyzer = DegradationAnalyzer()

    print(f"  Simuliere {len(sensors_simulation)} Sensoren über 90 Tage:")

    # Generiere Sensor-Daten für 90 Tage (24 Messungen/Tag)
    n_days = 90
    samples_per_day = 24
    total_samples = n_days * samples_per_day

    sensor_histories = {}
    anomaly_histories = {}

    for sensor_name, config in sensors_simulation.items():
        print(f"\n    {sensor_name} ({config['degradation_type']} degradation):")

        # Generiere Sensor-Verlauf
        time_points = np.arange(total_samples)
        days = time_points / samples_per_day

        baseline = config["baseline"]
        degradation_rate = config["degradation_rate"]
        noise = config["noise_level"] * np.random.randn(total_samples)

        if config["degradation_type"] == "linear":
            degradation = degradation_rate * days
        elif config["degradation_type"] == "exponential":
            degradation = baseline * (np.exp(degradation_rate * days) - 1)
        elif config["degradation_type"] == "accelerating":
            degradation = degradation_rate * days**1.5

        sensor_values = baseline + degradation + noise

        # Füge gelegentliche Anomalien hinzu
        anomaly_indices = np.random.choice(
            total_samples, size=int(total_samples * 0.02), replace=False
        )
        sensor_values[anomaly_indices] += np.random.normal(
            0, config["noise_level"] * 5, len(anomaly_indices)
        )

        sensor_histories[sensor_name] = sensor_values

        # Anomalie-Detektion (nach Baseline-Training)
        baseline_samples = 500  # Erste 500 Samples für Baseline
        anomaly_detector.fit_baseline(sensor_values[:baseline_samples])

        detected_anomalies = []
        for i in range(baseline_samples, total_samples):
            current_window = sensor_values[max(0, i - 10) : i + 1]  # Sliding window
            anomaly_result = anomaly_detector.detect_anomalies(current_window)

            if anomaly_result["is_anomaly"][-1]:  # Letzter Wert im Window
                detected_anomalies.append(i)

        anomaly_histories[sensor_name] = detected_anomalies

        # Degradation Analysis
        degradation_result = degradation_analyzer.analyze_degradation(
            sensor_values, sensor_name
        )

        print(f"      Aktuelle Wert: {sensor_values[-1]:.2f} {config.get('unit', '')}")
        print(f"      Degradation Score: {degradation_result['degradation_score']:.3f}")
        print(
            f"      Best Model: {degradation_result['best_model']} "
            f"(R² = {degradation_result['models'][degradation_result['best_model']]['r2']:.3f})"
        )

        prediction = degradation_result["maintenance_prediction"]
        if prediction["days_until_maintenance"]:
            print(
                f"      Wartung in: {prediction['days_until_maintenance']:.1f} Tagen "
                f"({prediction['confidence']} Konfidenz)"
            )
        else:
            print(
                f"      Wartung: Nicht vorhersagbar ({prediction['confidence']} Konfidenz)"
            )

        print(
            f"      Anomalien detektiert: {len(detected_anomalies)} "
            f"({len(detected_anomalies) / (total_samples - baseline_samples) * 100:.1f}%)"
        )

    # 3.4 Wartungsplan erstellen
    print("\n📊 3.4 Automatischer Wartungsplan:")

    maintenance_schedule = degradation_analyzer.get_maintenance_schedule()

    if maintenance_schedule:
        print("  Anstehende Wartungen (nächste 30 Tage):")
        for i, item in enumerate(maintenance_schedule, 1):
            print(
                f"    {i}. {item['sensor']} - {item['days_until_maintenance']:.1f} Tage "
                f"(Priorität: {item['priority']}, Konfidenz: {item['confidence']})"
            )
    else:
        print("  ✅ Keine kritischen Wartungen in den nächsten 30 Tagen")

    # 3.5 Cross-Sensor Korrelations-Analyse
    print("\n📊 3.5 Cross-Sensor Korrelations-Analyse:")

    # Analysiere Korrelationen zwischen Sensor-Degradation
    sensor_names = list(sensor_histories.keys())
    correlation_matrix = np.corrcoef([sensor_histories[name] for name in sensor_names])

    print("  Sensor-Korrelationen:")
    for i, name1 in enumerate(sensor_names):
        for j, name2 in enumerate(sensor_names[i + 1 :], i + 1):
            corr = correlation_matrix[i, j]
            if abs(corr) > 0.3:  # Nur signifikante Korrelationen
                print(f"    {name1} ↔ {name2}: r = {corr:+.3f}")

    duration = time.time() - start_time
    print(f"\n⚡ Predictive Maintenance in {duration:.3f} Sekunden")
    print("🔧 Predictive Analytics kann ungeplante Ausfälle um 70% reduzieren!")
    print()

    return degradation_analyzer, sensor_histories


def aufgabe_4_performance_dashboard():
    """Aufgabe 4: Echtzeit Performance-Dashboard mit KPIs"""
    print("🎯 AUFGABE 4: PERFORMANCE-DASHBOARD")
    print("-" * 40)
    print("Ziel: Erstelle ein Performance-Dashboard mit Real-Time KPIs")
    print("für Production Management und Entscheidungsunterstützung")
    print()

    start_time = time.time()

    # 4.1 KPI-Berechnungsengine
    print("📊 4.1 KPI-Berechnungsengine:")

    class KPIEngine:
        """Berechnet und verfolgt Key Performance Indicators"""

        def __init__(self):
            self.kpi_definitions = {
                "oee": {
                    "name": "Overall Equipment Effectiveness",
                    "unit": "%",
                    "target": 85.0,
                    "calculation": self._calculate_oee,
                },
                "availability": {
                    "name": "Machine Availability",
                    "unit": "%",
                    "target": 95.0,
                    "calculation": self._calculate_availability,
                },
                "performance": {
                    "name": "Performance Efficiency",
                    "unit": "%",
                    "target": 90.0,
                    "calculation": self._calculate_performance,
                },
                "quality_rate": {
                    "name": "Quality Rate",
                    "unit": "%",
                    "target": 99.0,
                    "calculation": self._calculate_quality_rate,
                },
                "throughput": {
                    "name": "Production Throughput",
                    "unit": "parts/hour",
                    "target": 150.0,
                    "calculation": self._calculate_throughput,
                },
                "mtbf": {
                    "name": "Mean Time Between Failures",
                    "unit": "hours",
                    "target": 200.0,
                    "calculation": self._calculate_mtbf,
                },
                "mttr": {
                    "name": "Mean Time To Repair",
                    "unit": "hours",
                    "target": 2.0,
                    "calculation": self._calculate_mttr,
                },
                "energy_efficiency": {
                    "name": "Energy Efficiency",
                    "unit": "kWh/part",
                    "target": 1.5,
                    "calculation": self._calculate_energy_efficiency,
                },
            }

            self.kpi_history = {kpi: [] for kpi in self.kpi_definitions.keys()}
            self.current_values = {}

        def update_kpis(self, production_data):
            """Update alle KPIs mit neuen Produktionsdaten"""
            updated_kpis = {}

            for kpi_name, definition in self.kpi_definitions.items():
                try:
                    value = definition["calculation"](production_data)
                    self.current_values[kpi_name] = value
                    self.kpi_history[kpi_name].append(
                        {
                            "timestamp": production_data.get("timestamp", time.time()),
                            "value": value,
                        }
                    )
                    updated_kpis[kpi_name] = value
                except Exception as e:
                    print(f"    Warning: KPI {kpi_name} calculation failed: {e}")
                    updated_kpis[kpi_name] = None

            return updated_kpis

        def _calculate_oee(self, data):
            """OEE = Availability × Performance × Quality"""
            availability = self._calculate_availability(data)
            performance = self._calculate_performance(data)
            quality = self._calculate_quality_rate(data)

            return (
                availability * performance * quality
            ) / 10000  # Alle in % -> Dezimal

        def _calculate_availability(self, data):
            """Availability = (Total Time - Downtime) / Total Time × 100"""
            total_time = data.get("total_time", 8 * 60)  # 8 Stunden in Minuten
            downtime = data.get("downtime", 0)

            return max(0, (total_time - downtime) / total_time * 100)

        def _calculate_performance(self, data):
            """Performance = (Actual Production / Target Production) × 100"""
            actual_production = data.get("actual_parts", 0)
            target_production = data.get("target_parts", 1)

            return min(100, actual_production / target_production * 100)

        def _calculate_quality_rate(self, data):
            """Quality Rate = (Good Parts / Total Parts) × 100"""
            good_parts = data.get("good_parts", 0)
            total_parts = data.get("total_parts", 1)

            return good_parts / total_parts * 100 if total_parts > 0 else 0

        def _calculate_throughput(self, data):
            """Throughput = Parts Produced / Time (parts/hour)"""
            parts_produced = data.get("actual_parts", 0)
            time_hours = data.get("total_time", 60) / 60  # Minuten -> Stunden

            return parts_produced / time_hours if time_hours > 0 else 0

        def _calculate_mtbf(self, data):
            """Mean Time Between Failures"""
            failures = data.get("failure_events", [])
            total_runtime = data.get("total_time", 480)  # Minuten

            if len(failures) <= 1:
                return total_runtime / 60  # Keine/ein Ausfall -> volle Laufzeit

            # Berechne Zeiten zwischen Ausfällen
            failure_times = sorted(failures)
            intervals = np.diff(failure_times)
            return np.mean(intervals) / 60 if len(intervals) > 0 else total_runtime / 60

        def _calculate_mttr(self, data):
            """Mean Time To Repair"""
            repair_times = data.get("repair_times", [])
            return (
                np.mean(repair_times) / 60 if repair_times else 0
            )  # Minuten -> Stunden

        def _calculate_energy_efficiency(self, data):
            """Energy per part produced"""
            energy_consumed = data.get("energy_kwh", 0)
            parts_produced = data.get("actual_parts", 1)

            return energy_consumed / parts_produced if parts_produced > 0 else 0

        def get_dashboard_summary(self, time_window_hours=8):
            """Erstelle Dashboard-Zusammenfassung"""
            summary = {}

            for kpi_name, definition in self.kpi_definitions.items():
                current_value = self.current_values.get(kpi_name)
                target_value = definition["target"]

                if current_value is not None:
                    # Performance vs. Target
                    if kpi_name in ["mttr"]:  # Lower is better
                        performance_ratio = (
                            target_value / current_value if current_value > 0 else 1
                        )
                        status = "GOOD" if current_value <= target_value else "POOR"
                    else:  # Higher is better
                        performance_ratio = (
                            current_value / target_value if target_value > 0 else 1
                        )
                        status = "GOOD" if current_value >= target_value else "POOR"

                    # Trend-Analyse (letzte Werte)
                    recent_history = self.kpi_history[kpi_name][-10:]  # Letzte 10 Werte
                    if len(recent_history) >= 3:
                        values = [h["value"] for h in recent_history]
                        trend_slope = np.polyfit(range(len(values)), values, 1)[0]

                        if abs(trend_slope) < target_value * 0.01:  # <1% Änderung
                            trend = "STABLE"
                        elif trend_slope > 0:
                            trend = "IMPROVING" if kpi_name != "mttr" else "DEGRADING"
                        else:
                            trend = "DEGRADING" if kpi_name != "mttr" else "IMPROVING"
                    else:
                        trend = "UNKNOWN"

                    summary[kpi_name] = {
                        "name": definition["name"],
                        "current_value": current_value,
                        "target_value": target_value,
                        "unit": definition["unit"],
                        "performance_ratio": performance_ratio,
                        "status": status,
                        "trend": trend,
                    }

            return summary

        def get_critical_alerts(self):
            """Identifiziere kritische Alerts basierend auf KPIs"""
            alerts = []

            for kpi_name, definition in self.kpi_definitions.items():
                current_value = self.current_values.get(kpi_name)
                target_value = definition["target"]

                if current_value is not None:
                    # Definiere Alert-Schwellwerte
                    if kpi_name == "oee" and current_value < 60:
                        alerts.append(
                            {
                                "type": "CRITICAL",
                                "message": f"OEE critically low: {current_value:.1f}% (target: {target_value}%)",
                                "kpi": kpi_name,
                            }
                        )
                    elif kpi_name == "availability" and current_value < 80:
                        alerts.append(
                            {
                                "type": "WARNING",
                                "message": f"Low machine availability: {current_value:.1f}%",
                                "kpi": kpi_name,
                            }
                        )
                    elif kpi_name == "quality_rate" and current_value < 95:
                        alerts.append(
                            {
                                "type": "CRITICAL",
                                "message": f"Quality rate below threshold: {current_value:.1f}%",
                                "kpi": kpi_name,
                            }
                        )
                    elif kpi_name == "mttr" and current_value > 4:
                        alerts.append(
                            {
                                "type": "WARNING",
                                "message": f"High repair time: {current_value:.1f} hours",
                                "kpi": kpi_name,
                            }
                        )

            return alerts

    # 4.2 Real-Time Dashboard Simulation
    print("  Simuliere Echtzeit-Dashboard über Produktionsschicht:")

    kpi_engine = KPIEngine()

    # Simuliere 8-Stunden Schicht mit verschiedenen Produktionsphasen
    shift_duration = 8 * 60  # 480 Minuten
    update_interval = 15  # Update alle 15 Minuten
    n_updates = shift_duration // update_interval

    print(
        f"    Schicht-Simulation: {shift_duration} Minuten in {update_interval}-Min Intervallen"
    )

    dashboard_history = []
    total_alerts = []

    for update_idx in range(n_updates):
        current_time = update_idx * update_interval

        # Simuliere Produktionsbedingungen basierend auf Tageszeit
        if current_time < 60:  # Erste Stunde: Anlauf
            base_efficiency = 0.7
            downtime_probability = 0.15
        elif current_time < 360:  # Stunden 1-6: Normale Produktion
            base_efficiency = 0.9
            downtime_probability = 0.05
        else:  # Letzte 2 Stunden: Ermüdung
            base_efficiency = 0.8
            downtime_probability = 0.1

        # Zufällige Variation
        efficiency_variation = np.random.normal(0, 0.05)
        actual_efficiency = np.clip(base_efficiency + efficiency_variation, 0.4, 1.0)

        # Simuliere Produktionsdaten
        target_parts_per_interval = 40  # 40 Teile pro 15 Min
        actual_parts = int(target_parts_per_interval * actual_efficiency)

        # Qualitätssimulation
        quality_base = 0.98
        quality_variation = np.random.normal(0, 0.01)
        quality_rate = np.clip(quality_base + quality_variation, 0.9, 1.0)
        good_parts = int(actual_parts * quality_rate)

        # Downtime-Simulation
        if np.random.random() < downtime_probability:
            downtime = np.random.uniform(5, 30)  # 5-30 Minuten
        else:
            downtime = np.random.uniform(0, 2)  # Kleinere Störungen

        # Energie-Simulation
        base_power = 45  # kW
        energy_kwh = (base_power * update_interval / 60) * actual_efficiency

        # Ausfall-Simulation
        failure_events = []
        repair_times = []
        if downtime > 10:  # Größere Störung als "Ausfall" betrachten
            failure_events.append(current_time)
            repair_times.append(downtime)

        production_data = {
            "timestamp": current_time,
            "total_time": update_interval,
            "actual_parts": actual_parts,
            "target_parts": target_parts_per_interval,
            "good_parts": good_parts,
            "total_parts": actual_parts,
            "downtime": downtime,
            "energy_kwh": energy_kwh,
            "failure_events": failure_events,
            "repair_times": repair_times,
        }

        # Update KPIs
        updated_kpis = kpi_engine.update_kpis(production_data)

        # Dashboard-Snapshot
        dashboard_summary = kpi_engine.get_dashboard_summary()
        alerts = kpi_engine.get_critical_alerts()

        dashboard_history.append(
            {
                "time": current_time,
                "summary": dashboard_summary,
                "alerts": alerts,
                "production_data": production_data,
            }
        )

        total_alerts.extend(alerts)

        # Periodische Berichte
        if (update_idx + 1) % 4 == 0:  # Jede Stunde
            hour = (update_idx + 1) * update_interval / 60
            print(f"\n    Nach {hour:.0f} Stunden:")

            # Top KPIs anzeigen
            key_kpis = ["oee", "availability", "quality_rate", "throughput"]
            for kpi in key_kpis:
                if kpi in dashboard_summary:
                    data = dashboard_summary[kpi]
                    status_icon = "✅" if data["status"] == "GOOD" else "⚠️"
                    trend_icon = {
                        "IMPROVING": "📈",
                        "STABLE": "➡️",
                        "DEGRADING": "📉",
                    }.get(data["trend"], "❓")

                    print(
                        f"      {data['name']}: {data['current_value']:.1f} {data['unit']} "
                        f"{status_icon} {trend_icon}"
                    )

            # Aktuelle Alerts
            current_alerts = [a for a in alerts if a["type"] == "CRITICAL"]
            if current_alerts:
                print(f"      🚨 Critical Alerts: {len(current_alerts)}")

    # 4.3 Dashboard-Auswertung
    print("\n📊 4.3 Schicht-Auswertung:")

    final_summary = kpi_engine.get_dashboard_summary()

    print("  Finale KPI-Werte:")
    for kpi_name, data in final_summary.items():
        target_status = "✅" if data["performance_ratio"] >= 1.0 else "❌"
        print(
            f"    {data['name']}: {data['current_value']:.1f} {data['unit']} "
            f"(Ziel: {data['target_value']:.1f}) {target_status}"
        )

    # Alert-Zusammenfassung
    critical_alerts = [a for a in total_alerts if a["type"] == "CRITICAL"]
    warning_alerts = [a for a in total_alerts if a["type"] == "WARNING"]

    print("\n  Alert-Zusammenfassung:")
    print(f"    Critical Alerts: {len(critical_alerts)}")
    print(f"    Warning Alerts: {len(warning_alerts)}")

    if critical_alerts:
        print(f"    Letzte Critical Alert: {critical_alerts[-1]['message']}")

    # Performance-Trends
    print("\n  Performance-Trends:")
    for kpi in ["oee", "availability", "quality_rate"]:
        if kpi in final_summary:
            trend = final_summary[kpi]["trend"]
            trend_icon = {"IMPROVING": "📈", "STABLE": "➡️", "DEGRADING": "📉"}.get(
                trend, "❓"
            )
            print(f"    {final_summary[kpi]['name']}: {trend} {trend_icon}")

    duration = time.time() - start_time
    print(f"\n⚡ Performance-Dashboard in {duration:.3f} Sekunden")
    print("📊 Echtzeit-KPIs ermöglichen proaktives Production Management!")
    print()

    return kpi_engine, dashboard_history


def aufgabe_5_enterprise_spc():
    """Aufgabe 5: Enterprise-Level Statistical Process Control"""
    print("🎯 AUFGABE 5: ENTERPRISE-LEVEL STATISTICAL PROCESS CONTROL")
    print("-" * 60)
    print("Ziel: Implementiere ein umfassendes SPC-System für Multi-Line")
    print("Produktionskontrolle mit automatischer Regelkarten-Überwachung")
    print()

    start_time = time.time()

    # 5.1 Erweiterte SPC-Implementierung
    print("📊 5.1 Enterprise SPC-System:")

    class EnterpriseSPC:
        """Enterprise-Level Statistical Process Control System"""

        def __init__(self, lines_config):
            self.lines = {}
            self.global_stats = {}

            # Initialisiere Produktionslinien
            for line_id, config in lines_config.items():
                self.lines[line_id] = {
                    "config": config,
                    "control_charts": {},
                    "process_capability": {},
                    "alarm_rules": self._initialize_alarm_rules(),
                    "data_buffer": {},
                }

                # Initialisiere Regelkarten für jedes Qualitätsmerkmal
                for feature in config["quality_features"]:
                    self.lines[line_id]["control_charts"][feature] = {
                        "x_chart": {"data": [], "limits": None},
                        "r_chart": {"data": [], "limits": None},
                        "s_chart": {"data": [], "limits": None},
                    }
                    self.lines[line_id]["data_buffer"][feature] = []

        def _initialize_alarm_rules(self):
            """Initialisiere Western Electric Alarm-Regeln"""
            return {
                "rule_1": {"description": "1 Punkt außerhalb 3σ", "active": True},
                "rule_2": {
                    "description": "9 aufeinanderfolgende Punkte auf einer Seite",
                    "active": True,
                },
                "rule_3": {
                    "description": "6 aufeinanderfolgende steigende/fallende Punkte",
                    "active": True,
                },
                "rule_4": {
                    "description": "14 aufeinanderfolgende alternierende Punkte",
                    "active": True,
                },
                "rule_5": {
                    "description": "2/3 Punkte außerhalb 2σ (gleiche Seite)",
                    "active": True,
                },
                "rule_6": {
                    "description": "4/5 Punkte außerhalb 1σ (gleiche Seite)",
                    "active": True,
                },
                "rule_7": {
                    "description": "15 aufeinanderfolgende Punkte innerhalb 1σ",
                    "active": True,
                },
                "rule_8": {
                    "description": "8 aufeinanderfolgende Punkte außerhalb 1σ",
                    "active": True,
                },
            }

        def add_measurement_batch(self, line_id, measurements_dict, subgroup_size=5):
            """Füge Messungen hinzu und aktualisiere Regelkarten"""
            if line_id not in self.lines:
                raise ValueError(f"Unbekannte Linie: {line_id}")

            line_data = self.lines[line_id]
            alarms = []

            for feature, measurements in measurements_dict.items():
                if feature not in line_data["data_buffer"]:
                    continue

                # Füge Messungen zum Buffer hinzu
                line_data["data_buffer"][feature].extend(measurements)

                # Verarbeite in Subgroups
                buffer = line_data["data_buffer"][feature]
                while len(buffer) >= subgroup_size:
                    subgroup = buffer[:subgroup_size]
                    buffer = buffer[subgroup_size:]

                    # Berechne Subgroup-Statistiken
                    subgroup_mean = np.mean(subgroup)
                    subgroup_range = np.max(subgroup) - np.min(subgroup)
                    subgroup_std = np.std(subgroup, ddof=1)

                    # Update Control Charts
                    charts = line_data["control_charts"][feature]

                    # X-Chart (Mittelwerte)
                    charts["x_chart"]["data"].append(subgroup_mean)

                    # R-Chart (Spannweiten)
                    charts["r_chart"]["data"].append(subgroup_range)

                    # S-Chart (Standardabweichungen)
                    charts["s_chart"]["data"].append(subgroup_std)

                    # Berechne/Update Kontrollgrenzen
                    self._update_control_limits(line_id, feature, subgroup_size)

                    # Prüfe Alarm-Regeln
                    feature_alarms = self._check_alarm_rules(line_id, feature)
                    alarms.extend(feature_alarms)

                # Update Buffer
                line_data["data_buffer"][feature] = buffer

            # Update Prozessfähigkeiten
            self._update_process_capabilities(line_id)

            return alarms

        def _update_control_limits(self, line_id, feature, subgroup_size):
            """Berechne Kontrollgrenzen basierend auf aktuellen Daten"""
            charts = self.lines[line_id]["control_charts"][feature]

            # Konstanten für Kontrollgrenzen (abhängig von Subgroup-Größe)
            control_constants = {
                2: {"A2": 1.88, "D3": 0, "D4": 3.27, "B3": 0, "B4": 3.27},
                3: {"A2": 1.02, "D3": 0, "D4": 2.57, "B3": 0, "B4": 2.57},
                4: {"A2": 0.73, "D3": 0, "D4": 2.28, "B3": 0, "B4": 2.27},
                5: {"A2": 0.58, "D3": 0, "D4": 2.11, "B3": 0.03, "B4": 1.96},
                6: {"A2": 0.48, "D3": 0, "D4": 2.00, "B3": 0.03, "B4": 1.87},
            }

            constants = control_constants.get(subgroup_size, control_constants[5])

            # X-Chart Limits
            x_data = charts["x_chart"]["data"]
            r_data = charts["r_chart"]["data"]

            if len(x_data) >= 25:  # Mindestens 25 Subgroups für stabile Grenzen
                x_bar_bar = np.mean(x_data)
                r_bar = np.mean(r_data)

                charts["x_chart"]["limits"] = {
                    "center": x_bar_bar,
                    "ucl": x_bar_bar + constants["A2"] * r_bar,
                    "lcl": x_bar_bar - constants["A2"] * r_bar,
                    "sigma_1": x_bar_bar + (constants["A2"] * r_bar) / 3,
                    "sigma_2": x_bar_bar + (2 * constants["A2"] * r_bar) / 3,
                    "sigma_minus_1": x_bar_bar - (constants["A2"] * r_bar) / 3,
                    "sigma_minus_2": x_bar_bar - (2 * constants["A2"] * r_bar) / 3,
                }

                # R-Chart Limits
                charts["r_chart"]["limits"] = {
                    "center": r_bar,
                    "ucl": constants["D4"] * r_bar,
                    "lcl": constants["D3"] * r_bar,
                }

                # S-Chart Limits
                s_data = charts["s_chart"]["data"]
                s_bar = np.mean(s_data)

                charts["s_chart"]["limits"] = {
                    "center": s_bar,
                    "ucl": constants["B4"] * s_bar,
                    "lcl": constants["B3"] * s_bar,
                }

        def _check_alarm_rules(self, line_id, feature):
            """Prüfe Western Electric Alarm-Regeln"""
            charts = self.lines[line_id]["control_charts"][feature]
            alarm_rules = self.lines[line_id]["alarm_rules"]
            alarms = []

            # Nur X-Chart für Alarm-Regeln (hauptsächlich)
            x_data = charts["x_chart"]["data"]
            x_limits = charts["x_chart"]["limits"]

            if not x_limits or len(x_data) < 9:  # Nicht genug Daten
                return alarms

            center = x_limits["center"]
            ucl = x_limits["ucl"]
            lcl = x_limits["lcl"]
            sigma_1 = x_limits["sigma_1"]
            sigma_2 = x_limits["sigma_2"]
            sigma_minus_1 = x_limits["sigma_minus_1"]
            sigma_minus_2 = x_limits["sigma_minus_2"]

            recent_data = x_data[-15:]  # Letzte 15 Punkte für Regeln

            # Rule 1: 1 Punkt außerhalb 3σ
            if alarm_rules["rule_1"]["active"]:
                if recent_data[-1] > ucl or recent_data[-1] < lcl:
                    alarms.append(
                        {
                            "rule": "rule_1",
                            "line": line_id,
                            "feature": feature,
                            "description": "Punkt außerhalb Kontrollgrenzen",
                            "value": recent_data[-1],
                            "severity": "CRITICAL",
                        }
                    )

            # Rule 2: 9 aufeinanderfolgende Punkte auf einer Seite
            if alarm_rules["rule_2"]["active"] and len(recent_data) >= 9:
                last_9 = recent_data[-9:]
                if all(x > center for x in last_9) or all(x < center for x in last_9):
                    alarms.append(
                        {
                            "rule": "rule_2",
                            "line": line_id,
                            "feature": feature,
                            "description": "9 Punkte auf einer Seite der Mittellinie",
                            "severity": "WARNING",
                        }
                    )

            # Rule 3: 6 aufeinanderfolgende steigende/fallende Punkte
            if alarm_rules["rule_3"]["active"] and len(recent_data) >= 6:
                last_6 = recent_data[-6:]
                differences = np.diff(last_6)
                if all(d > 0 for d in differences) or all(d < 0 for d in differences):
                    alarms.append(
                        {
                            "rule": "rule_3",
                            "line": line_id,
                            "feature": feature,
                            "description": "6 aufeinanderfolgende Trend-Punkte",
                            "severity": "WARNING",
                        }
                    )

            # Rule 5: 2/3 Punkte außerhalb 2σ
            if alarm_rules["rule_5"]["active"] and len(recent_data) >= 3:
                last_3 = recent_data[-3:]
                above_2sigma = sum(
                    1 for x in last_3 if x > sigma_2 or x < sigma_minus_2
                )
                if above_2sigma >= 2:
                    alarms.append(
                        {
                            "rule": "rule_5",
                            "line": line_id,
                            "feature": feature,
                            "description": "2/3 Punkte außerhalb 2σ",
                            "severity": "WARNING",
                        }
                    )

            # Rule 6: 4/5 Punkte außerhalb 1σ
            if alarm_rules["rule_6"]["active"] and len(recent_data) >= 5:
                last_5 = recent_data[-5:]
                above_1sigma = sum(
                    1 for x in last_5 if x > sigma_1 or x < sigma_minus_1
                )
                if above_1sigma >= 4:
                    alarms.append(
                        {
                            "rule": "rule_6",
                            "line": line_id,
                            "feature": feature,
                            "description": "4/5 Punkte außerhalb 1σ",
                            "severity": "WARNING",
                        }
                    )

            return alarms

        def _update_process_capabilities(self, line_id):
            """Update Prozessfähigkeiten für alle Features einer Linie"""
            line_config = self.lines[line_id]["config"]

            for feature in line_config["quality_features"]:
                charts = self.lines[line_id]["control_charts"][feature]
                x_data = charts["x_chart"]["data"]
                s_data = charts["s_chart"]["data"]

                if len(x_data) >= 25 and len(s_data) >= 25:  # Genug Daten
                    # Berechne Prozess-Statistiken
                    process_mean = np.mean(x_data)
                    process_std = np.mean(
                        s_data
                    )  # Durchschnittliche Subgroup-Standardabweichung

                    # Hole Spezifikationsgrenzen
                    feature_spec = line_config["specifications"].get(feature, {})
                    usl = feature_spec.get("usl")  # Upper Spec Limit
                    lsl = feature_spec.get("lsl")  # Lower Spec Limit
                    target = feature_spec.get("target")

                    if usl is not None and lsl is not None and process_std > 0:
                        # Cp (Prozessfähigkeit)
                        cp = (usl - lsl) / (6 * process_std)

                        # Cpk (berücksichtigt Zentrierung)
                        if target is not None:
                            cpk_upper = (usl - process_mean) / (3 * process_std)
                            cpk_lower = (process_mean - lsl) / (3 * process_std)
                            cpk = min(cpk_upper, cpk_lower)

                            # Cpm (berücksichtigt Abweichung vom Zielwert)
                            cpm = (usl - lsl) / (
                                6
                                * np.sqrt(process_std**2 + (process_mean - target) ** 2)
                            )
                        else:
                            cpk = min(
                                (usl - process_mean) / (3 * process_std),
                                (process_mean - lsl) / (3 * process_std),
                            )
                            cpm = None

                        # Pp und Ppk (Performance-Indices, langfristig)
                        all_measurements = []
                        for subgroup_data in self.lines[line_id]["data_buffer"][
                            feature
                        ]:
                            all_measurements.extend(subgroup_data)

                        if all_measurements:
                            overall_std = np.std(all_measurements, ddof=1)
                            pp = (
                                (usl - lsl) / (6 * overall_std)
                                if overall_std > 0
                                else 0
                            )
                            ppk = (
                                min(
                                    (usl - process_mean) / (3 * overall_std),
                                    (process_mean - lsl) / (3 * overall_std),
                                )
                                if overall_std > 0
                                else 0
                            )
                        else:
                            pp = ppk = None

                        self.lines[line_id]["process_capability"][feature] = {
                            "cp": cp,
                            "cpk": cpk,
                            "cpm": cpm,
                            "pp": pp,
                            "ppk": ppk,
                            "process_mean": process_mean,
                            "process_std": process_std,
                            "last_update": len(x_data),
                        }

        def get_enterprise_summary(self):
            """Erstelle Enterprise-weite Zusammenfassung"""
            summary = {"lines": {}, "global_metrics": {}, "critical_issues": []}

            all_alarms = []
            all_capabilities = []

            for line_id, line_data in self.lines.items():
                line_summary = {
                    "total_features": len(line_data["config"]["quality_features"]),
                    "features_in_control": 0,
                    "critical_alarms": 0,
                    "average_cpk": 0,
                    "process_capabilities": line_data["process_capability"],
                }

                # Analysiere Features
                for feature in line_data["config"]["quality_features"]:
                    charts = line_data["control_charts"][feature]

                    # Check if in control (vereinfacht)
                    x_data = charts["x_chart"]["data"]
                    x_limits = charts["x_chart"]["limits"]

                    if x_limits and len(x_data) >= 10:
                        recent_points = x_data[-10:]
                        in_control = all(
                            x_limits["lcl"] <= x <= x_limits["ucl"]
                            for x in recent_points
                        )
                        if in_control:
                            line_summary["features_in_control"] += 1

                    # Sammle Capability-Daten
                    if feature in line_data["process_capability"]:
                        cap_data = line_data["process_capability"][feature]
                        all_capabilities.append(cap_data["cpk"])

                # Durchschnittliche Cpk
                line_capabilities = [
                    line_data["process_capability"][f]["cpk"]
                    for f in line_data["process_capability"]
                ]
                if line_capabilities:
                    line_summary["average_cpk"] = np.mean(line_capabilities)

                summary["lines"][line_id] = line_summary

            # Globale Metriken
            if all_capabilities:
                summary["global_metrics"] = {
                    "enterprise_average_cpk": np.mean(all_capabilities),
                    "enterprise_min_cpk": np.min(all_capabilities),
                    "lines_below_cpk_1_33": sum(
                        1 for cpk in all_capabilities if cpk < 1.33
                    ),
                    "total_lines": len(self.lines),
                    "total_features": sum(
                        len(line["config"]["quality_features"])
                        for line in self.lines.values()
                    ),
                }

            return summary

        def export_spc_report(self, format="json"):
            """Exportiere umfassenden SPC-Report"""
            report_data = {
                "timestamp": time.time(),
                "enterprise_summary": self.get_enterprise_summary(),
                "detailed_data": {},
            }

            for line_id, line_data in self.lines.items():
                line_report = {
                    "config": line_data["config"],
                    "control_charts": {},
                    "process_capabilities": line_data["process_capability"],
                    "alarm_summary": {},
                }

                for feature in line_data["config"]["quality_features"]:
                    charts = line_data["control_charts"][feature]
                    line_report["control_charts"][feature] = {
                        "x_chart": {
                            "data": charts["x_chart"]["data"][-50:],  # Letzte 50 Punkte
                            "limits": charts["x_chart"]["limits"],
                        },
                        "r_chart": {
                            "data": charts["r_chart"]["data"][-50:],
                            "limits": charts["r_chart"]["limits"],
                        },
                    }

                report_data["detailed_data"][line_id] = line_report

            if format == "json":
                return json.dumps(report_data, indent=2, default=str)
            else:
                return report_data

    # 5.2 Test Enterprise SPC System
    print("  Enterprise SPC System Test:")

    # Konfiguration für mehrere Produktionslinien
    lines_config = {
        "Line_A": {
            "quality_features": ["diameter", "length", "surface_roughness"],
            "specifications": {
                "diameter": {"target": 25.0, "usl": 25.1, "lsl": 24.9},
                "length": {"target": 100.0, "usl": 100.5, "lsl": 99.5},
                "surface_roughness": {"target": 1.6, "usl": 2.0, "lsl": 1.2},
            },
        },
        "Line_B": {
            "quality_features": ["diameter", "length", "hardness"],
            "specifications": {
                "diameter": {"target": 30.0, "usl": 30.15, "lsl": 29.85},
                "length": {"target": 150.0, "usl": 150.8, "lsl": 149.2},
                "hardness": {"target": 45.0, "usl": 47.0, "lsl": 43.0},
            },
        },
        "Line_C": {
            "quality_features": ["diameter", "roundness", "concentricity"],
            "specifications": {
                "diameter": {"target": 15.0, "usl": 15.05, "lsl": 14.95},
                "roundness": {"target": 0.005, "usl": 0.010, "lsl": 0.000},
                "concentricity": {"target": 0.008, "usl": 0.015, "lsl": 0.000},
            },
        },
    }

    spc_system = EnterpriseSPC(lines_config)

    print(f"    Initialisiert: {len(lines_config)} Produktionslinien")
    for line_id, config in lines_config.items():
        print(f"      {line_id}: {len(config['quality_features'])} Qualitätsmerkmale")

    # Simuliere Produktionsdaten über mehrere Schichten
    n_shifts = 5  # 5 Schichten
    batches_per_shift = 20  # 20 Batches pro Schicht
    parts_per_batch = 5  # 5 Teile pro Batch (Subgroup-Größe)

    total_alarms = []

    print(f"\n  Simuliere {n_shifts} Schichten mit {batches_per_shift} Batches:")

    np.random.seed(42)

    for shift in range(n_shifts):
        shift_alarms = []

        for batch in range(batches_per_shift):
            # Simuliere verschiedene Prozesszustände
            process_drift = shift * 0.01  # Leichter Drift über Schichten
            process_variation = 1 + batch * 0.02  # Steigende Variation

            for line_id, config in lines_config.items():
                measurements = {}

                for feature in config["quality_features"]:
                    spec = config["specifications"][feature]
                    target = spec["target"]

                    # Simuliere realistische Messwerte
                    base_std = (spec["usl"] - spec["lsl"]) / 12  # 6σ = Toleranz
                    actual_std = base_std * process_variation

                    # Verschiedene Störungen einbauen
                    if shift == 2 and batch > 10:  # Schicht 3, zweite Hälfte
                        # Simuliere Prozess-Drift
                        mean_shift = target + process_drift * (
                            spec["usl"] - spec["lsl"]
                        )
                    elif shift == 4 and 5 <= batch <= 15:  # Schicht 5, Mitte
                        # Simuliere erhöhte Variation
                        actual_std *= 1.5
                        mean_shift = target
                    else:
                        mean_shift = target

                    # Generiere Messungen für Subgroup
                    part_measurements = np.random.normal(
                        mean_shift, actual_std, parts_per_batch
                    )
                    measurements[feature] = part_measurements.tolist()

                # Update SPC System
                batch_alarms = spc_system.add_measurement_batch(
                    line_id, measurements, parts_per_batch
                )
                shift_alarms.extend(batch_alarms)

        total_alarms.extend(shift_alarms)

        # Schicht-Bericht
        critical_alarms = [a for a in shift_alarms if a["severity"] == "CRITICAL"]
        warning_alarms = [a for a in shift_alarms if a["severity"] == "WARNING"]

        print(
            f"    Schicht {shift + 1}: {len(critical_alarms)} Critical, {len(warning_alarms)} Warning Alarms"
        )

    # 5.3 Enterprise-Auswertung
    print("\n📊 5.3 Enterprise-Auswertung:")

    enterprise_summary = spc_system.get_enterprise_summary()

    print("  Enterprise-Metriken:")
    global_metrics = enterprise_summary["global_metrics"]
    print(f"    Durchschnittliche Cpk: {global_metrics['enterprise_average_cpk']:.3f}")
    print(f"    Minimale Cpk: {global_metrics['enterprise_min_cpk']:.3f}")
    print(
        f"    Linien unter Cpk 1.33: {global_metrics['lines_below_cpk_1_33']}/{global_metrics['total_lines']}"
    )

    print("\n  Linien-Performance:")
    for line_id, line_summary in enterprise_summary["lines"].items():
        control_rate = (
            line_summary["features_in_control"] / line_summary["total_features"] * 100
        )
        status = (
            "✅" if control_rate >= 80 and line_summary["average_cpk"] >= 1.33 else "⚠️"
        )

        print(
            f"    {line_id}: {control_rate:.0f}% unter Kontrolle, "
            f"Cpk={line_summary['average_cpk']:.3f} {status}"
        )

    print("\n  Alarm-Zusammenfassung:")
    critical_total = len([a for a in total_alarms if a["severity"] == "CRITICAL"])
    warning_total = len([a for a in total_alarms if a["severity"] == "WARNING"])

    print(f"    Gesamt-Alarme: {len(total_alarms)}")
    print(f"    Critical: {critical_total}, Warning: {warning_total}")

    # Top Alarm-Regeln
    alarm_rules_count = {}
    for alarm in total_alarms:
        rule = alarm["rule"]
        alarm_rules_count[rule] = alarm_rules_count.get(rule, 0) + 1

    if alarm_rules_count:
        print("\n  Häufigste Alarm-Regeln:")
        sorted_rules = sorted(
            alarm_rules_count.items(), key=lambda x: x[1], reverse=True
        )
        for rule, count in sorted_rules[:3]:
            rule_desc = spc_system.lines["Line_A"]["alarm_rules"][rule]["description"]
            print(f"    {rule}: {count}× ({rule_desc})")

    # Export Report
    print("\n📄 SPC-Report Export:")
    spc_report = spc_system.export_spc_report("json")
    report_size = len(spc_report)

    print(f"    Report-Größe: {report_size:,} Zeichen")
    print("    Enthält: Detailed Control Charts, Process Capabilities, Alarm History")

    duration = time.time() - start_time
    print(f"\n⚡ Enterprise SPC in {duration:.3f} Sekunden")
    print("🎯 Enterprise SPC ermöglicht unternehmensweite Qualitätskontrolle!")
    print()

    return spc_system


if __name__ == "__main__":
    main()
