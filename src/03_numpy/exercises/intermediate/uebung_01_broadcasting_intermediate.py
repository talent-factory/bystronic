#!/usr/bin/env python3
"""
NumPy Übung 1: Erweiterte Broadcasting-Techniken (Intermediate)
SmartFactory Python Grundkurs - Kapitel 3

Diese Übung fokussiert auf fortgeschrittene Broadcasting-Konzepte mit
mehrdimensionalen Arrays und komplexen Produktionsszenarien.

Lernziele:
- Mehrdimensionales Broadcasting verstehen und anwenden
- Komplexe Array-Formen effizient manipulieren
- Performance-kritische Operationen optimieren
- Speicher-effiziente Berechnungen durchführen
- Real-World Produktionsdaten verarbeiten

Schwierigkeitsgrad: 🟡 Intermediate
Geschätzte Bearbeitungszeit: 35-40 Minuten
"""

import time

import numpy as np


def main():
    """Hauptfunktion für alle Broadcasting-Übungen"""
    print("🎯 NUMPY INTERMEDIATE ÜBUNG 1: ERWEITERTE BROADCASTING-TECHNIKEN")
    print("=" * 75)
    print("Diese Übung behandelt komplexe Broadcasting-Szenarien mit")
    print("mehrdimensionalen Produktionsdaten und Performance-Optimierung.")
    print()

    try:
        # Aufgabe 1: Multi-Machine Broadcasting
        aufgabe_1_multi_machine_broadcasting()

        # Aufgabe 2: Zeitreihen-Broadcasting
        aufgabe_2_zeitreihen_broadcasting()

        # Aufgabe 3: 3D-Qualitätsdaten Broadcasting
        aufgabe_3_3d_qualitaetsdaten_broadcasting()

        # Aufgabe 4: Performance-optimiertes Broadcasting
        aufgabe_4_performance_broadcasting()

        # Aufgabe 5: Komplexe Produktionsanalyse
        aufgabe_5_komplexe_produktionsanalyse()

        print("\n" + "🎉" * 60)
        print("🎉 ALLE INTERMEDIATE BROADCASTING-AUFGABEN ABGESCHLOSSEN! 🎉")
        print("🎉" * 60)
        print("\n📋 GELERNTE KONZEPTE:")
        print("✅ Mehrdimensionales Broadcasting (3D+)")
        print("✅ Memory-effiziente Operationen")
        print("✅ Komplexe Array-Shape-Manipulationen")
        print("✅ Performance-kritische Berechnungen")
        print("✅ Broadcasting-Regeln in der Praxis")
        print("✅ Zeitreihen- und Sensor-Datenverarbeitung")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler in der Übung: {e}")
        print("💡 Tipp: Prüfen Sie Array-Shapes mit .shape vor Broadcasting!")


def aufgabe_1_multi_machine_broadcasting():
    """Aufgabe 1: Broadcasting mit Multi-Machine Produktionsdaten"""
    print("🎯 AUFGABE 1: MULTI-MACHINE BROADCASTING")
    print("-" * 50)
    print("Ziel: Verarbeite Produktionsdaten von 10 Maschinen über 30 Tage")
    print("mit unterschiedlichen Schichtmodellen pro Maschine")
    print()

    start_time = time.time()

    # 1.1 Erstelle Multi-Machine Datenstruktur
    print("📊 1.1 Multi-Machine Datenstruktur erstellen:")

    np.random.seed(42)
    n_machines = 10
    n_days = 30
    shifts_per_day = 3  # Früh, Spät, Nacht

    # Basis-Produktivität pro Maschine (unterschiedliche Kapazitäten)
    machine_base_productivity = np.array(
        [180, 165, 190, 175, 200, 155, 185, 170, 195, 160]
    )  # Teile pro Schicht

    # Schichtfaktoren (Früh=1.0, Spät=0.9, Nacht=0.8)
    shift_factors = np.array([1.0, 0.9, 0.8])

    # Tagesfaktoren (Wochenende niedrigere Produktion)
    day_factors = np.array(
        [
            0.95 if day % 7 in [5, 6] else 1.0  # Wochenende = Tag 6,7 (Sa,So)
            for day in range(n_days)
        ]
    )

    print(f"  • {n_machines} Maschinen")
    print(f"  • {n_days} Tage")
    print(f"  • {shifts_per_day} Schichten pro Tag")
    print(
        f"  • Base Produktivität: {machine_base_productivity.min()}-{machine_base_productivity.max()} Teile/Schicht"
    )

    # 1.2 Broadcasting-Operation durchführen
    print("\n📊 1.2 Broadcasting-Berechnung:")
    print("  Array-Shapes:")
    print(f"    machine_base_productivity: {machine_base_productivity.shape}")
    print(f"    shift_factors: {shift_factors.shape}")
    print(f"    day_factors: {day_factors.shape}")

    # Reshape für Broadcasting: (machines, days, shifts)
    machines_reshaped = machine_base_productivity[
        :, np.newaxis, np.newaxis
    ]  # (10, 1, 1)
    days_reshaped = day_factors[np.newaxis, :, np.newaxis]  # (1, 30, 1)
    shifts_reshaped = shift_factors[np.newaxis, np.newaxis, :]  # (1, 1, 3)

    print("    Nach Reshape:")
    print(f"      machines_reshaped: {machines_reshaped.shape}")
    print(f"      days_reshaped: {days_reshaped.shape}")
    print(f"      shifts_reshaped: {shifts_reshaped.shape}")

    # Broadcasting-Multiplikation
    production_matrix = machines_reshaped * days_reshaped * shifts_reshaped

    # Zufällige Variation hinzufügen (±10%)
    noise = np.random.normal(1.0, 0.1, production_matrix.shape)
    production_matrix = production_matrix * noise
    production_matrix = np.maximum(production_matrix, 0)  # Keine negativen Werte

    print(f"    Finales Array: {production_matrix.shape} (machines, days, shifts)")

    # 1.3 Analyse der Broadcasting-Ergebnisse
    print("\n📊 1.3 Ergebnisanalyse:")

    # Gesamtproduktion pro Maschine
    total_per_machine = np.sum(production_matrix, axis=(1, 2))
    print("  Gesamtproduktion pro Maschine:")
    for i, total in enumerate(total_per_machine):
        print(f"    Maschine {i + 1:2d}: {total:6.0f} Teile")

    # Durchschnitt pro Schicht-Typ
    avg_per_shift_type = np.mean(production_matrix, axis=(0, 1))
    shift_names = ["Frühschicht", "Spätschicht", "Nachtschicht"]
    print("\n  Durchschnitt pro Schichttyp:")
    for shift_name, avg in zip(shift_names, avg_per_shift_type, strict=False):
        print(f"    {shift_name}: {avg:.1f} Teile/Schicht")

    # Wochenend-Effekt analysieren
    weekday_production = production_matrix[
        :, [d for d in range(n_days) if d % 7 not in [5, 6]], :
    ]
    weekend_production = production_matrix[
        :, [d for d in range(n_days) if d % 7 in [5, 6]], :
    ]

    weekday_avg = np.mean(weekday_production)
    weekend_avg = np.mean(weekend_production)

    print("\n  Wochenend-Effekt:")
    print(f"    Werktag-Durchschnitt: {weekday_avg:.1f} Teile/Schicht")
    print(f"    Wochenend-Durchschnitt: {weekend_avg:.1f} Teile/Schicht")
    print(f"    Wochenend-Faktor: {weekend_avg / weekday_avg:.3f}")

    duration = time.time() - start_time
    print(f"\n⚡ Multi-Machine Broadcasting in {duration:.3f} Sekunden")
    print(f"📊 {production_matrix.size:,} Datenpunkte mit Broadcasting berechnet!")
    print()


def aufgabe_2_zeitreihen_broadcasting():
    """Aufgabe 2: Zeitreihen-Broadcasting für Sensor-Daten"""
    print("🎯 AUFGABE 2: ZEITREIHEN-BROADCASTING")
    print("-" * 50)
    print("Ziel: Verarbeite Sensor-Zeitreihen von Produktionsmaschinen")
    print("mit verschiedenen Sampling-Raten und Zeitfenstern")
    print()

    start_time = time.time()

    # 2.1 Simuliere Sensor-Zeitreihen
    print("📊 2.1 Sensor-Zeitreihen generieren:")

    np.random.seed(123)

    # Verschiedene Sensoren mit unterschiedlichen Sampling-Raten
    sensors = {
        "temperature": {"rate": 60, "unit": "°C", "baseline": 65.0, "noise": 2.0},
        "vibration": {"rate": 10, "unit": "mm/s", "baseline": 5.0, "noise": 0.8},
        "pressure": {"rate": 30, "unit": "bar", "baseline": 8.5, "noise": 0.3},
        "power": {"rate": 5, "unit": "kW", "baseline": 45.0, "noise": 3.0},
    }

    duration_hours = 8  # 8-Stunden Schicht

    # Generiere Zeitreihen für jeden Sensor
    sensor_data = {}
    for sensor_name, config in sensors.items():
        n_samples = duration_hours * 3600 // config["rate"]  # Samples pro Schicht

        # Basis-Zeitreihe mit Trend und Zyklen
        time_points = np.linspace(0, duration_hours, n_samples)

        # Tageszyklen (Aufwärmphase, Betrieb, Abkühlung)
        daily_cycle = 0.1 * np.sin(2 * np.pi * time_points / duration_hours)

        # Betriebszyklen (höhere Frequenz)
        operation_cycle = 0.05 * np.sin(2 * np.pi * time_points * 6)

        # Rauschen
        noise = np.random.normal(0, config["noise"], n_samples)

        # Kombiniere alle Komponenten
        values = config["baseline"] + daily_cycle + operation_cycle + noise

        sensor_data[sensor_name] = {
            "values": values,
            "timestamps": time_points,
            "config": config,
        }

        print(
            f"  • {sensor_name}: {len(values):,} Samples ({config['rate']}s Intervall)"
        )

    # 2.2 Broadcasting für Zeitfenster-Analyse
    print("\n📊 2.2 Zeitfenster-Analyse mit Broadcasting:")

    window_sizes = [60, 300, 900]  # 1min, 5min, 15min Fenster

    for sensor_name, data in sensor_data.items():
        values = data["values"]
        timestamps = data["timestamps"]
        rate = data["config"]["rate"]

        print(f"\n  {sensor_name.upper()} ({data['config']['unit']}):")

        for window_size in window_sizes:
            window_samples = window_size // rate

            if window_samples < len(values):
                # Broadcasting für gleitende Fenster
                n_windows = len(values) - window_samples + 1

                # Erstelle Index-Array für Broadcasting
                indices = (
                    np.arange(window_samples)[np.newaxis, :]
                    + np.arange(n_windows)[:, np.newaxis]
                )

                # Broadcasting-Operation: Extrahiere alle Fenster auf einmal
                windowed_data = values[indices]  # Shape: (n_windows, window_samples)

                # Statistiken für alle Fenster berechnen
                window_means = np.mean(windowed_data, axis=1)
                window_stds = np.std(windowed_data, axis=1)
                window_mins = np.min(windowed_data, axis=1)
                window_maxs = np.max(windowed_data, axis=1)

                # Anomalie-Detektion (3-Sigma-Regel)
                overall_mean = np.mean(values)
                overall_std = np.std(values)
                anomalies = np.abs(window_means - overall_mean) > 3 * overall_std

                print(
                    f"    {window_size // 60:2d}min Fenster: {len(window_means):4d} Fenster, "
                    f"μ={np.mean(window_means):.1f}, σ={np.mean(window_stds):.2f}, "
                    f"{np.sum(anomalies)} Anomalien"
                )

    # 2.3 Cross-Sensor Korrelations-Broadcasting
    print("\n📊 2.3 Cross-Sensor Korrelationsanalyse:")

    # Resample alle Sensoren auf gemeinsame Zeitbasis (niedrigste Rate)
    min_rate = min(config["rate"] for config in sensors.values())
    common_samples = duration_hours * 3600 // min_rate
    common_timestamps = np.linspace(0, duration_hours, common_samples)

    # Interpoliere alle Sensoren auf gemeinsame Zeitbasis
    resampled_data = {}
    for sensor_name, data in sensor_data.items():
        resampled_values = np.interp(
            common_timestamps, data["timestamps"], data["values"]
        )
        resampled_data[sensor_name] = resampled_values

    # Erstelle Matrix für Broadcasting-Korrelation
    sensor_names = list(resampled_data.keys())
    sensor_matrix = np.array([resampled_data[name] for name in sensor_names])

    print(f"  Sensor-Matrix Shape: {sensor_matrix.shape} (sensors, timestamps)")

    # Broadcasting-Korrelation zwischen allen Sensor-Paaren
    # Standardisiere Daten
    sensor_matrix_std = (
        sensor_matrix - np.mean(sensor_matrix, axis=1, keepdims=True)
    ) / np.std(sensor_matrix, axis=1, keepdims=True)

    # Korrelationsmatrix mit Broadcasting
    correlation_matrix = np.dot(sensor_matrix_std, sensor_matrix_std.T) / (
        common_samples - 1
    )

    print("\n  Korrelationsmatrix:")
    print("    " + "".join(f"{name:>12s}" for name in sensor_names))
    for i, row_name in enumerate(sensor_names):
        correlations = "".join(
            f"{correlation_matrix[i, j]:>12.3f}" for j in range(len(sensor_names))
        )
        print(f"    {row_name:<12s}{correlations}")

    duration = time.time() - start_time
    print(f"\n⚡ Zeitreihen-Broadcasting in {duration:.3f} Sekunden")
    print(
        f"📊 {sum(len(data['values']) for data in sensor_data.values()):,} Sensor-Datenpunkte verarbeitet!"
    )
    print()


def aufgabe_3_3d_qualitaetsdaten_broadcasting():
    """Aufgabe 3: 3D-Broadcasting für komplexe Qualitätsdaten"""
    print("🎯 AUFGABE 3: 3D-QUALITÄTSDATEN BROADCASTING")
    print("-" * 50)
    print("Ziel: Verarbeite 3D-Qualitätsdaten (Teile × Messungen × Merkmale)")
    print("mit Broadcasting für statistische Analysen")
    print()

    start_time = time.time()

    # 3.1 Erstelle 3D-Qualitätsdatenstruktur
    print("📊 3.1 3D-Qualitätsdatenstruktur erstellen:")

    np.random.seed(456)

    # Dimensionen
    n_parts = 2000  # Anzahl produzierte Teile
    n_measurements = 5  # Messungen pro Teil
    n_features = 8  # Qualitätsmerkmale pro Messung

    # Qualitätsmerkmale definieren
    feature_names = [
        "Länge_mm",
        "Breite_mm",
        "Höhe_mm",
        "Gewicht_g",
        "Rauheit_μm",
        "Härte_HRC",
        "Rundheit_μm",
        "Parallelität_μm",
    ]

    # Sollwerte und Toleranzen pro Merkmal
    target_values = np.array([25.0, 15.0, 8.0, 120.0, 1.6, 45.0, 5.0, 10.0])
    tolerances = np.array([0.1, 0.05, 0.02, 2.0, 0.2, 2.0, 2.0, 5.0])

    print(f"  • Teile: {n_parts:,}")
    print(f"  • Messungen pro Teil: {n_measurements}")
    print(f"  • Qualitätsmerkmale: {n_features}")
    print(f"  • Gesamt-Datenpunkte: {n_parts * n_measurements * n_features:,}")

    # 3.2 Generiere realistische 3D-Qualitätsdaten
    print("\n📊 3.2 3D-Daten mit Broadcasting generieren:")

    # Base-Matrix erstellen
    quality_data_3d = np.zeros((n_parts, n_measurements, n_features))

    # Broadcasting für Sollwerte: (1, 1, features) → (parts, measurements, features)
    targets_broadcasted = target_values[np.newaxis, np.newaxis, :]

    # Verschiedene Variationsquellen
    # 1. Teil-zu-Teil Variation (zwischen verschiedenen Teilen)
    part_variation = np.random.normal(0, tolerances / 6, (n_parts, 1, n_features))

    # 2. Messungs-Variation (Messgenauigkeit)
    measurement_variation = np.random.normal(
        0, tolerances / 10, (n_parts, n_measurements, n_features)
    )

    # 3. Systematische Trends (Werkzeugverschleiß)
    part_numbers = np.arange(n_parts)[:, np.newaxis, np.newaxis]  # (parts, 1, 1)
    wear_trend = part_numbers * tolerances[np.newaxis, np.newaxis, :] / (10 * n_parts)

    # Broadcasting-Kombination aller Effekte
    quality_data_3d = (
        targets_broadcasted + part_variation + measurement_variation + wear_trend
    )

    print(f"  Array-Shape: {quality_data_3d.shape}")
    print("  Shapes für Broadcasting:")
    print(f"    targets_broadcasted: {targets_broadcasted.shape}")
    print(f"    part_variation: {part_variation.shape}")
    print(f"    measurement_variation: {measurement_variation.shape}")
    print(f"    wear_trend: {wear_trend.shape}")

    # 3.3 Statistische Analyse mit Broadcasting
    print("\n📊 3.3 Statistische Analyse mit Broadcasting:")

    # Mittelwerte pro Feature über alle Teile und Messungen
    feature_means = np.mean(quality_data_3d, axis=(0, 1))  # Shape: (features,)

    # Standardabweichungen pro Feature
    feature_stds = np.std(quality_data_3d, axis=(0, 1), ddof=1)

    # Mittelwerte pro Teil (über alle Messungen)
    part_means = np.mean(quality_data_3d, axis=1)  # Shape: (parts, features)

    # Mittelwerte pro Messung (über alle Teile)
    measurement_means = np.mean(
        quality_data_3d, axis=0
    )  # Shape: (measurements, features)

    print("  Feature-Statistiken:")
    for i, (name, mean, std, target, tol) in enumerate(
        zip(
            feature_names,
            feature_means,
            feature_stds,
            target_values,
            tolerances,
            strict=False,
        )
    ):
        deviation = abs(mean - target)
        status = (
            "🟢" if deviation <= tol / 4 else "🟡" if deviation <= tol / 2 else "🔴"
        )
        print(
            f"    {name:15s}: μ={mean:7.3f}, σ={std:6.4f}, "
            f"Ziel={target:6.1f} ±{tol:5.3f} {status}"
        )

    # 3.4 Toleranzprüfung mit Broadcasting
    print("\n📊 3.4 Toleranzprüfung mit Broadcasting:")

    # Broadcasting für Toleranzprüfung: (parts, measurements, features)
    deviations = np.abs(quality_data_3d - target_values[np.newaxis, np.newaxis, :])
    in_tolerance = deviations <= tolerances[np.newaxis, np.newaxis, :]

    # Ausschussraten pro Feature
    reject_rates_per_feature = (1 - np.mean(in_tolerance, axis=(0, 1))) * 100

    # Ausschussraten pro Teil (wenn ein Feature outside tolerance)
    parts_all_ok = np.all(in_tolerance, axis=(1, 2))  # Alle Messungen und Features OK
    overall_reject_rate = (1 - np.mean(parts_all_ok)) * 100

    print("  Ausschussraten pro Feature:")
    for name, rate in zip(feature_names, reject_rates_per_feature, strict=False):
        status = "🟢" if rate < 1.0 else "🟡" if rate < 5.0 else "🔴"
        print(f"    {name:15s}: {rate:5.2f}% {status}")

    print(f"\n  Gesamt-Ausschussrate: {overall_reject_rate:.2f}%")
    print(f"  OK-Teile: {np.sum(parts_all_ok):,} von {n_parts:,}")

    # 3.5 Prozessfähigkeitsanalyse mit Broadcasting
    print("\n📊 3.5 Prozessfähigkeitsanalyse:")

    # Cp und Cpk für alle Features mit Broadcasting
    cp_values = tolerances / (6 * feature_stds)

    # Cpk berücksichtigt Zentrierung
    upper_spec_limits = target_values + tolerances / 2
    lower_spec_limits = target_values - tolerances / 2

    cpk_upper = (upper_spec_limits - feature_means) / (3 * feature_stds)
    cpk_lower = (feature_means - lower_spec_limits) / (3 * feature_stds)
    cpk_values = np.minimum(cpk_upper, cpk_lower)

    print("  Prozessfähigkeiten:")
    for name, cp, cpk in zip(feature_names, cp_values, cpk_values, strict=False):
        cp_status = "🟢" if cp >= 1.33 else "🟡" if cp >= 1.0 else "🔴"
        cpk_status = "🟢" if cpk >= 1.33 else "🟡" if cpk >= 1.0 else "🔴"
        print(f"    {name:15s}: Cp={cp:5.2f} {cp_status}, Cpk={cpk:5.2f} {cpk_status}")

    duration = time.time() - start_time
    print(f"\n⚡ 3D-Broadcasting in {duration:.3f} Sekunden")
    print(f"📊 {quality_data_3d.size:,} Datenpunkte in 3D-Array verarbeitet!")
    print()


def aufgabe_4_performance_broadcasting():
    """Aufgabe 4: Performance-optimiertes Broadcasting"""
    print("🎯 AUFGABE 4: PERFORMANCE-OPTIMIERTES BROADCASTING")
    print("-" * 50)
    print("Ziel: Vergleiche Broadcasting-Performance mit alternativen Ansätzen")
    print("und optimiere für große Datenmengen")
    print()

    start_time = time.time()

    # 4.1 Performance-Vergleich Setup
    print("📊 4.1 Performance-Vergleich Setup:")

    # Verschiedene Datengrößen testen
    test_sizes = [1000, 5000, 10000, 50000]
    n_features = 10

    print(f"  • Test-Größen: {test_sizes}")
    print(f"  • Features pro Datensatz: {n_features}")
    print()

    for size in test_sizes:
        print(
            f"📈 Datengröße: {size:,} × {n_features} = {size * n_features:,} Elemente"
        )
        print("-" * 40)

        # Testdaten erstellen
        np.random.seed(42)
        data_matrix = np.random.randn(size, n_features)
        operation_vector = np.random.randn(n_features)

        # Method 1: Broadcasting (NumPy-optimiert)
        start = time.time()
        result_broadcasting = data_matrix + operation_vector  # Broadcasting
        time_broadcasting = time.time() - start

        # Method 2: Explicit Loop (Python)
        start = time.time()
        result_loop = np.zeros_like(data_matrix)
        for i in range(size):
            result_loop[i] = data_matrix[i] + operation_vector
        time_loop = time.time() - start

        # Method 3: List Comprehension
        start = time.time()
        result_listcomp = np.array([row + operation_vector for row in data_matrix])
        time_listcomp = time.time() - start

        # Method 4: Vectorized with tile
        start = time.time()
        tiled_vector = np.tile(operation_vector, (size, 1))
        result_tile = data_matrix + tiled_vector
        time_tile = time.time() - start

        # Ergebnisse vergleichen
        print(f"  Broadcasting:     {time_broadcasting:.6f}s")
        print(
            f"  Explicit Loop:    {time_loop:.6f}s ({time_loop / time_broadcasting:6.1f}x langsamer)"
        )
        print(
            f"  List Comprehension: {time_listcomp:.6f}s ({time_listcomp / time_broadcasting:6.1f}x langsamer)"
        )
        print(
            f"  Tiled Operation:  {time_tile:.6f}s ({time_tile / time_broadcasting:6.1f}x langsamer)"
        )

        # Speicherverbrauch vergleichen
        memory_broadcasting = result_broadcasting.nbytes
        memory_tile = result_tile.nbytes + tiled_vector.nbytes

        print(f"  Memory Broadcasting: {memory_broadcasting / 1024**2:.2f} MB")
        print(
            f"  Memory Tiled:       {memory_tile / 1024**2:.2f} MB ({memory_tile / memory_broadcasting:.1f}x mehr)"
        )
        print()

    # 4.2 Memory-effiziente Broadcasting-Strategien
    print("📊 4.2 Memory-effiziente Broadcasting-Strategien:")

    # Große Matrix simulieren
    large_size = 100000
    n_features = 50

    print(
        f"  Große Matrix: {large_size:,} × {n_features} = {large_size * n_features:,} Elemente"
    )

    # In-Place Operationen
    np.random.seed(123)
    large_matrix = np.random.randn(large_size, n_features).astype(
        np.float32
    )  # Float32 für Speicher
    operation_vector = np.random.randn(n_features).astype(np.float32)

    initial_memory = large_matrix.nbytes / 1024**2
    print(f"  Initial Memory: {initial_memory:.1f} MB")

    # Method 1: Standard Broadcasting (neue Matrix)
    start = time.time()
    result_new = large_matrix + operation_vector
    time_new = time.time() - start
    memory_new = (large_matrix.nbytes + result_new.nbytes) / 1024**2

    # Method 2: In-Place Broadcasting
    start = time.time()
    large_matrix += operation_vector  # In-place
    time_inplace = time.time() - start
    memory_inplace = large_matrix.nbytes / 1024**2

    print(f"  Standard Broadcasting: {time_new:.4f}s, {memory_new:.1f} MB")
    print(f"  In-Place Broadcasting: {time_inplace:.4f}s, {memory_inplace:.1f} MB")
    print(f"  Memory Savings: {(memory_new - memory_inplace) / memory_new * 100:.1f}%")

    # 4.3 Chunk-basiertes Broadcasting für sehr große Daten
    print("\n📊 4.3 Chunk-basiertes Broadcasting:")

    # Simuliere sehr große Daten die nicht in Memory passen
    very_large_size = 1000000
    chunk_size = 10000
    n_chunks = very_large_size // chunk_size

    print(f"  Sehr große Daten: {very_large_size:,} Zeilen")
    print(f"  Chunk-Größe: {chunk_size:,} Zeilen")
    print(f"  Anzahl Chunks: {n_chunks}")

    # Simuliere Chunk-Processing
    start = time.time()
    processed_chunks = 0

    for chunk_idx in range(n_chunks):
        # Simuliere Chunk-Laden (würde normalerweise von Disk/DB kommen)
        chunk_data = np.random.randn(chunk_size, n_features).astype(np.float32)

        # Broadcasting auf Chunk anwenden
        processed_chunk = chunk_data + operation_vector

        # Simuliere Chunk-Speichern
        processed_chunks += 1

    chunk_time = time.time() - start

    print(f"  Verarbeitungszeit: {chunk_time:.3f}s")
    print(f"  Chunks verarbeitet: {processed_chunks}")
    print(f"  Rate: {very_large_size / chunk_time:.0f} Zeilen/Sekunde")

    duration = time.time() - start_time
    print(f"\n⚡ Performance-Analyse in {duration:.3f} Sekunden")
    print("💡 Broadcasting ist fast immer die beste Wahl für Performance!")
    print()


def aufgabe_5_komplexe_produktionsanalyse():
    """Aufgabe 5: Komplexe Produktionsanalyse mit Multi-Level Broadcasting"""
    print("🎯 AUFGABE 5: KOMPLEXE PRODUKTIONSANALYSE")
    print("-" * 50)
    print("Ziel: Kombiniere alle Broadcasting-Techniken für eine")
    print("umfassende Multi-Level Produktionsanalyse")
    print()

    start_time = time.time()

    # 5.1 Multi-Level Datenstruktur erstellen
    print("📊 5.1 Multi-Level Produktionsdatenstruktur:")

    np.random.seed(789)

    # Hierarchische Struktur: Fabriken → Linien → Maschinen → Schichten → Teile
    n_factories = 3
    n_lines_per_factory = 4
    n_machines_per_line = 5
    n_shifts = 21  # 3 Wochen
    avg_parts_per_shift = 200

    total_elements = n_factories * n_lines_per_factory * n_machines_per_line * n_shifts

    print(f"  • Fabriken: {n_factories}")
    print(f"  • Linien pro Fabrik: {n_lines_per_factory}")
    print(f"  • Maschinen pro Linie: {n_machines_per_line}")
    print(f"  • Schichten: {n_shifts}")
    print(f"  • Gesamt-Kombinationen: {total_elements:,}")

    # 5.2 Multi-Dimensional Broadcasting Setup
    print("\n📊 5.2 Multi-Dimensional Broadcasting Setup:")

    # Verschiedene Einflussfaktoren mit unterschiedlichen Dimensionen

    # Fabrik-spezifische Faktoren (pro Fabrik)
    factory_efficiency = np.array([1.05, 1.00, 0.95])  # Fabrik A,B,C

    # Linien-spezifische Faktoren (pro Linie, gleich für alle Fabriken)
    line_capacity = np.array([1.1, 1.0, 0.9, 1.05])  # Linie 1,2,3,4

    # Maschinen-spezifische Faktore (pro Maschine, gleich für alle Linien)
    machine_reliability = np.array([0.98, 1.02, 0.95, 1.01, 0.99])  # Maschine 1-5

    # Zeit-spezifische Faktoren (pro Schicht)
    # Wochentag-Effekt und Lernkurve
    shift_factors = np.array(
        [
            0.95 if i % 21 < 5 else 0.85 if i % 21 < 10 else 1.0  # Woche 1,2,3
            for i in range(n_shifts)
        ]
    )
    shift_factors *= 1 + np.arange(n_shifts) * 0.001  # Leichte Lernkurve

    print("  Shapes vor Broadcasting:")
    print(f"    factory_efficiency: {factory_efficiency.shape}")
    print(f"    line_capacity: {line_capacity.shape}")
    print(f"    machine_reliability: {machine_reliability.shape}")
    print(f"    shift_factors: {shift_factors.shape}")

    # 5.3 Reshape für Multi-Level Broadcasting
    print("\n📊 5.3 Multi-Level Broadcasting durchführen:")

    # Reshape alle Faktoren für Broadcasting
    # Ziel-Shape: (factories, lines, machines, shifts)
    factories_reshaped = factory_efficiency[:, np.newaxis, np.newaxis, np.newaxis]
    lines_reshaped = line_capacity[np.newaxis, :, np.newaxis, np.newaxis]
    machines_reshaped = machine_reliability[np.newaxis, np.newaxis, :, np.newaxis]
    shifts_reshaped = shift_factors[np.newaxis, np.newaxis, np.newaxis, :]

    print("  Shapes nach Reshape:")
    print(f"    factories_reshaped: {factories_reshaped.shape}")
    print(f"    lines_reshaped: {lines_reshaped.shape}")
    print(f"    machines_reshaped: {machines_reshaped.shape}")
    print(f"    shifts_reshaped: {shifts_reshaped.shape}")

    # Base-Produktion (gleich für alle)
    base_production = avg_parts_per_shift

    # Multi-Level Broadcasting
    production_4d = (
        base_production
        * factories_reshaped
        * lines_reshaped
        * machines_reshaped
        * shifts_reshaped
    )

    # Zufällige Variation hinzufügen
    random_variation = np.random.normal(1.0, 0.05, production_4d.shape)
    production_4d *= random_variation
    production_4d = np.maximum(production_4d, 0)  # Keine negativen Werte

    print(f"  Finale 4D-Matrix: {production_4d.shape}")
    print(f"  Gesamt-Datenpunkte: {production_4d.size:,}")

    # 5.4 Multi-Level Analysen mit Broadcasting
    print("\n📊 5.4 Multi-Level Analysen:")

    # Aggregationen auf verschiedenen Ebenen

    # Level 1: Gesamt pro Fabrik (über alle Linien, Maschinen, Schichten)
    factory_totals = np.sum(production_4d, axis=(1, 2, 3))
    print("  Fabrik-Totals:")
    for i, total in enumerate(factory_totals):
        print(f"    Fabrik {chr(65 + i)}: {total:,.0f} Teile")

    # Level 2: Durchschnitt pro Linie (über alle Fabriken, Maschinen, Schichten)
    line_averages = np.mean(production_4d, axis=(0, 2, 3))
    print("\n  Linien-Durchschnitte:")
    for i, avg in enumerate(line_averages):
        print(f"    Linie {i + 1}: {avg:.1f} Teile/Schicht")

    # Level 3: Top-Maschinen (über alle Fabriken, Linien, Schichten)
    machine_totals = np.sum(production_4d, axis=(0, 1, 3))
    best_machine_idx = np.argmax(machine_totals)
    print(
        f"\n  Beste Maschine: #{best_machine_idx + 1} mit {machine_totals[best_machine_idx]:,.0f} Teilen"
    )

    # Level 4: Zeittrend (über alle Fabriken, Linien, Maschinen)
    time_trend = np.mean(production_4d, axis=(0, 1, 2))

    # Lineare Regression für Trend
    shift_numbers = np.arange(n_shifts)
    trend_slope = np.polyfit(shift_numbers, time_trend, 1)[0]

    print("\n  Zeittrend:")
    print(f"    Erste Schicht: {time_trend[0]:.1f} Teile")
    print(f"    Letzte Schicht: {time_trend[-1]:.1f} Teile")
    print(f"    Trend-Steigung: {trend_slope:+.2f} Teile/Schicht")

    # 5.5 Performance-KPIs mit Broadcasting
    print("\n📊 5.5 Performance-KPIs berechnen:")

    # Overall Equipment Effectiveness (OEE) Simulation
    # Availability * Performance * Quality (vereinfacht)

    # Simuliere Verfügbarkeit (zufällige Ausfälle)
    availability = np.random.uniform(0.85, 0.98, production_4d.shape)

    # Performance-Ratio (Ist vs. Soll)
    target_production = base_production
    performance_ratio = np.minimum(
        production_4d / target_production, 1.5
    )  # Cap bei 150%

    # Qualitätsrate (zufällig, aber korreliert mit Produktion)
    quality_rate = np.random.uniform(0.92, 0.99, production_4d.shape)
    quality_rate = np.where(
        production_4d > target_production * 1.2, quality_rate * 0.95, quality_rate
    )  # Qualität sinkt bei Überproduktion

    # OEE-Berechnung mit Broadcasting
    oee_4d = availability * performance_ratio * quality_rate

    # Aggregierte OEE-Werte
    factory_oee = np.mean(oee_4d, axis=(1, 2, 3))
    line_oee = np.mean(oee_4d, axis=(0, 2, 3))
    machine_oee = np.mean(oee_4d, axis=(0, 1, 3))

    print("  OEE-Werte:")
    print(f"    Fabrik-OEE: {[f'{oee:.1%}' for oee in factory_oee]}")
    print(f"    Beste Linie: #{np.argmax(line_oee) + 1} mit {np.max(line_oee):.1%} OEE")
    print(
        f"    Beste Maschine: #{np.argmax(machine_oee) + 1} mit {np.max(machine_oee):.1%} OEE"
    )

    # 5.6 Anomalie-Detektion mit Broadcasting
    print("\n📊 5.6 Anomalie-Detektion:")

    # Z-Score basierte Anomalie-Detektion
    overall_mean = np.mean(production_4d)
    overall_std = np.std(production_4d)

    z_scores = (production_4d - overall_mean) / overall_std
    anomalies = np.abs(z_scores) > 3  # 3-Sigma-Regel

    anomaly_count = np.sum(anomalies)
    anomaly_rate = anomaly_count / production_4d.size * 100

    print(
        f"  Anomalien: {anomaly_count:,} von {production_4d.size:,} ({anomaly_rate:.2f}%)"
    )

    # Finde kritischste Anomalien
    if anomaly_count > 0:
        max_anomaly_idx = np.unravel_index(np.argmax(np.abs(z_scores)), z_scores.shape)
        max_z_score = z_scores[max_anomaly_idx]
        max_production = production_4d[max_anomaly_idx]

        print("  Extremste Anomalie:")
        print(
            f"    Fabrik {chr(65 + max_anomaly_idx[0])}, Linie {max_anomaly_idx[1] + 1}, "
            f"Maschine {max_anomaly_idx[2] + 1}, Schicht {max_anomaly_idx[3] + 1}"
        )
        print(
            f"    Produktion: {max_production:.0f} Teile (Z-Score: {max_z_score:+.2f})"
        )

    duration = time.time() - start_time
    print(f"\n⚡ Komplexe Multi-Level Analyse in {duration:.3f} Sekunden")
    print(f"🚀 {production_4d.size:,} Datenpunkte in 4D-Array analysiert!")
    print(f"📊 Broadcasting ermöglichte {total_elements:,} Berechnungen parallel!")
    print()


if __name__ == "__main__":
    main()
