#!/usr/bin/env python3
"""
NumPy Performance-Vergleich
Bystronic Python Grundkurs - Kapitel 3

Dieses Beispiel demonstriert die Performance-Vorteile von NumPy
gegenüber Pure Python mit praxisrelevanten Berechnungen.

Themen:
- Performance-Benchmarks verschiedener Operationen
- Memory-Verbrauch und Effizienz
- Skalierbarkeit mit Datengröße
- Praktische Anwendungen für Bystronic
"""

import sys
import time

import numpy as np


def memory_usage_mb(obj) -> float:
    """Berechnet den Memory-Verbrauch eines Objekts in MB"""
    return sys.getsizeof(obj) / (1024 * 1024)


def benchmark_basic_operations():
    """Vergleicht grundlegende mathematische Operationen"""
    print("🔥 PERFORMANCE-VERGLEICH: Grundlegende Operationen")
    print("=" * 60)

    sizes = [1000, 10000, 100000, 1000000]

    for size in sizes:
        print(f"\n📊 Datengröße: {size:,} Elemente")
        print("-" * 40)

        # Daten vorbereiten
        python_list = list(range(size))
        numpy_array = np.arange(size, dtype=np.int64)

        # Memory-Verbrauch
        list_memory = memory_usage_mb(python_list)
        array_memory = memory_usage_mb(numpy_array)

        print(f"Memory - Python Liste: {list_memory:.2f} MB")
        print(f"Memory - NumPy Array:  {array_memory:.2f} MB")
        print(
            f"Memory Ratio:          {list_memory / array_memory:.1f}x mehr für Liste"
        )
        print()

        # Test 1: Summe berechnen
        print("Test 1: Summe berechnen")

        # Python List Comprehension
        start = time.time()
        python_sum = sum(python_list)
        python_time = time.time() - start

        # NumPy
        start = time.time()
        numpy_sum = np.sum(numpy_array)
        numpy_time = time.time() - start

        print(f"  Python: {python_time:.4f}s (Ergebnis: {python_sum:,})")
        print(f"  NumPy:  {numpy_time:.4f}s (Ergebnis: {numpy_sum:,})")
        print(f"  Speedup: {python_time / numpy_time:.1f}x schneller")
        print()

        # Test 2: Quadrat und Addition
        print("Test 2: Quadrat + 1 für alle Elemente")

        # Python List Comprehension
        start = time.time()
        python_result = [x**2 + 1 for x in python_list]
        python_time = time.time() - start

        # NumPy vektorisiert
        start = time.time()
        numpy_result = numpy_array**2 + 1
        numpy_time = time.time() - start

        print(f"  Python: {python_time:.4f}s")
        print(f"  NumPy:  {numpy_time:.4f}s")
        print(f"  Speedup: {python_time / numpy_time:.1f}x schneller")

        # Memory für Ergebnisse
        result_list_memory = memory_usage_mb(python_result)
        result_array_memory = memory_usage_mb(numpy_result)
        print(f"  Result Memory - Python: {result_list_memory:.2f} MB")
        print(f"  Result Memory - NumPy:  {result_array_memory:.2f} MB")


def benchmark_production_calculations():
    """Benchmarks für typische Produktionsberechnungen"""
    print("\n\n🏭 PRODUKTIONS-BENCHMARK: Bystronic-relevante Berechnungen")
    print("=" * 60)

    # Simuliere Produktionsdaten für eine Woche
    n_measurements = 50000  # 50k Messungen
    print(f"📈 Datensatz: {n_measurements:,} Qualitätsmessungen")
    print()

    # Generiere realistische Messdaten
    np.random.seed(42)
    measurements_list = [np.random.normal(25.0, 0.5) for _ in range(n_measurements)]
    measurements_array = np.random.normal(25.0, 0.5, n_measurements)

    target_value = 25.0
    tolerance = 1.0

    print("🎯 Test 1: Qualitätskontrolle - Toleranzprüfung")
    print("-" * 45)

    # Python Version
    start = time.time()
    python_in_tolerance = sum(
        1 for x in measurements_list if abs(x - target_value) <= tolerance
    )
    python_time = time.time() - start

    # NumPy Version
    start = time.time()
    numpy_in_tolerance = np.sum(np.abs(measurements_array - target_value) <= tolerance)
    numpy_time = time.time() - start

    print(f"Python: {python_time:.4f}s ({python_in_tolerance:,} in Toleranz)")
    print(f"NumPy:  {numpy_time:.4f}s ({numpy_in_tolerance:,} in Toleranz)")
    print(f"Speedup: {python_time / numpy_time:.1f}x")
    print()

    print("🎯 Test 2: Statistische Prozesskontrolle (SPC)")
    print("-" * 45)

    # Python Version - Cp-Wert berechnen
    start = time.time()
    python_mean = sum(measurements_list) / len(measurements_list)
    python_variance = sum((x - python_mean) ** 2 for x in measurements_list) / (
        len(measurements_list) - 1
    )
    python_std = python_variance**0.5
    python_cp = (2 * tolerance) / (6 * python_std)
    python_time = time.time() - start

    # NumPy Version
    start = time.time()
    numpy_mean = np.mean(measurements_array)
    numpy_std = np.std(measurements_array, ddof=1)
    numpy_cp = (2 * tolerance) / (6 * numpy_std)
    numpy_time = time.time() - start

    print(f"Python: {python_time:.4f}s (Cp = {python_cp:.3f})")
    print(f"NumPy:  {numpy_time:.4f}s (Cp = {numpy_cp:.3f})")
    print(f"Speedup: {python_time / numpy_time:.1f}x")
    print()

    print("🎯 Test 3: Trend-Analyse - Gleitender Durchschnitt")
    print("-" * 45)

    window_size = 100

    # Python Version
    start = time.time()
    python_moving_avg = []
    for i in range(len(measurements_list) - window_size + 1):
        window = measurements_list[i : i + window_size]
        avg = sum(window) / len(window)
        python_moving_avg.append(avg)
    python_time = time.time() - start

    # NumPy Version mit Convolution
    start = time.time()
    numpy_moving_avg = np.convolve(
        measurements_array, np.ones(window_size) / window_size, mode="valid"
    )
    numpy_time = time.time() - start

    print(f"Python: {python_time:.4f}s ({len(python_moving_avg):,} Werte)")
    print(f"NumPy:  {numpy_time:.4f}s ({len(numpy_moving_avg):,} Werte)")
    print(f"Speedup: {python_time / numpy_time:.1f}x")


def benchmark_matrix_operations():
    """Benchmarks für Matrix-Operationen (relevant für CNC/Koordinatentransformation)"""
    print("\n\n🔧 MATRIX-BENCHMARK: CNC-Koordinatentransformationen")
    print("=" * 60)

    # Simuliere CNC-Koordinaten
    n_points = 10000
    print(f"📐 Datensatz: {n_points:,} CNC-Koordinatenpunkte")
    print()

    # 2D-Koordinaten
    points_list = [[i * 0.1, i * 0.05] for i in range(n_points)]
    points_array = np.array(points_list)

    # Rotationsmatrix für 45°
    angle = np.pi / 4  # 45 Grad
    rotation_matrix = np.array(
        [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
    )

    print("🎯 Test: Rotation aller Koordinaten um 45°")
    print("-" * 40)

    # Python Version - Manuelle Matrix-Multiplikation
    start = time.time()
    rotated_python = []
    for point in points_list:
        x, y = point
        new_x = rotation_matrix[0, 0] * x + rotation_matrix[0, 1] * y
        new_y = rotation_matrix[1, 0] * x + rotation_matrix[1, 1] * y
        rotated_python.append([new_x, new_y])
    python_time = time.time() - start

    # NumPy Version - Vektorisierte Matrix-Multiplikation
    start = time.time()
    rotated_numpy = points_array @ rotation_matrix.T
    numpy_time = time.time() - start

    print(f"Python: {python_time:.4f}s")
    print(f"NumPy:  {numpy_time:.4f}s")
    print(f"Speedup: {python_time / numpy_time:.1f}x")

    # Verifikation der Ergebnisse
    max_diff = np.max(np.abs(np.array(rotated_python) - rotated_numpy))
    print(f"Max. Abweichung: {max_diff:.2e} (sollte ~0 sein)")


def benchmark_scalability():
    """Zeigt Skalierbarkeit mit verschiedenen Datengrößen"""
    print("\n\n📈 SKALIERBARKEITS-ANALYSE")
    print("=" * 60)

    sizes = [1000, 5000, 10000, 50000, 100000]
    python_times = []
    numpy_times = []
    speedups = []

    print("Datengröße    Python    NumPy     Speedup")
    print("-" * 45)

    for size in sizes:
        # Erstelle Testdaten
        data_list = list(range(size))
        data_array = np.arange(size)

        # Python: Quadrat aller Elemente
        start = time.time()
        python_result = [x**2 for x in data_list]
        python_time = time.time() - start

        # NumPy: Vektorisierte Operation
        start = time.time()
        numpy_result = data_array**2
        numpy_time = time.time() - start

        speedup = python_time / numpy_time

        python_times.append(python_time)
        numpy_times.append(numpy_time)
        speedups.append(speedup)

        print(
            f"{size:>8,}    {python_time:>6.4f}s   {numpy_time:>6.4f}s   {speedup:>6.1f}x"
        )

    print()
    print("📊 ERKENNTNISSE:")
    print(f"• Durchschnittlicher Speedup: {np.mean(speedups):.1f}x")
    print(f"• Maximaler Speedup: {np.max(speedups):.1f}x")
    print("• NumPy-Vorteil steigt mit Datengröße!")


def benchmark_real_world_scenario():
    """Realistisches Szenario: Tagesauswertung Bystronic-Produktion"""
    print("\n\n🏭 REAL-WORLD SZENARIO: Tagesauswertung Produktion")
    print("=" * 60)

    # Simuliere einen Produktionstag
    n_parts = 5000  # 5000 Teile an einem Tag
    n_measurements_per_part = 3  # 3 Messungen pro Teil
    total_measurements = n_parts * n_measurements_per_part

    print(f"📋 Szenario: {n_parts:,} Teile mit je {n_measurements_per_part} Messungen")
    print(f"📊 Gesamt: {total_measurements:,} Messwerte")
    print()

    # Generiere realistische Produktionsdaten
    np.random.seed(123)

    # Verschiedene Toleranzbereiche für verschiedene Maße
    target_values = [25.0, 15.5, 8.2]  # mm
    tolerances = [0.1, 0.05, 0.02]  # mm
    measurement_names = ["Länge", "Breite", "Dicke"]

    measurements = {}
    for i, (target, tol, name) in enumerate(
        zip(target_values, tolerances, measurement_names, strict=False)
    ):
        measurements[name] = np.random.normal(target, tol / 3, n_parts)

    print("🎯 AUFGABE: Vollständige Qualitätsauswertung")
    print("-" * 45)

    start_total = time.time()

    # 1. Toleranzprüfung für alle Maße
    for name, values in measurements.items():
        target = target_values[measurement_names.index(name)]
        tolerance = tolerances[measurement_names.index(name)]

        in_tolerance = np.abs(values - target) <= tolerance
        reject_rate = (1 - np.mean(in_tolerance)) * 100

        print(
            f"  {name}: {np.sum(in_tolerance):,}/{len(values):,} OK ({reject_rate:.2f}% Ausschuss)"
        )

    # 2. Statistische Auswertung
    print("\n📊 Statistische Kennwerte:")
    for name, values in measurements.items():
        mean_val = np.mean(values)
        std_val = np.std(values, ddof=1)
        target = target_values[measurement_names.index(name)]
        tolerance = tolerances[measurement_names.index(name)]

        # Prozessfähigkeit
        cp = tolerance / (3 * std_val)
        cpk = min(
            (target + tolerance / 2 - mean_val) / (3 * std_val),
            (mean_val - (target - tolerance / 2)) / (3 * std_val),
        )

        print(
            f"  {name}: μ={mean_val:.3f}, σ={std_val:.4f}, Cp={cp:.2f}, Cpk={cpk:.2f}"
        )

    # 3. Korrelationsanalyse
    print("\n🔗 Korrelationsanalyse:")
    all_measurements = np.column_stack(
        [measurements[name] for name in measurement_names]
    )
    correlation_matrix = np.corrcoef(all_measurements.T)

    for i in range(len(measurement_names)):
        for j in range(i + 1, len(measurement_names)):
            corr = correlation_matrix[i, j]
            print(f"  {measurement_names[i]} ↔ {measurement_names[j]}: r={corr:.3f}")

    # 4. Trend-Erkennung (gleitender Durchschnitt)
    print("\n📈 Trend-Analyse (letzte 500 Teile):")
    window = 100
    for name, values in measurements.items():
        recent_values = values[-500:]
        trend = np.convolve(recent_values, np.ones(window) / window, mode="valid")
        slope = np.polyfit(range(len(trend)), trend, 1)[0]

        trend_direction = (
            "↗️ steigend"
            if slope > 0.001
            else "↘️ fallend" if slope < -0.001 else "→ stabil"
        )
        print(f"  {name}: {trend_direction} (Steigung: {slope:.6f})")

    total_time = time.time() - start_total

    print(f"\n⚡ GESAMTZEIT: {total_time:.3f} Sekunden")
    print(f"🚀 Das entspricht {total_measurements / total_time:.0f} Messungen/Sekunde")
    print()
    print("💡 MIT PYTHON-LISTEN HÄTTE DAS DEUTLICH LÄNGER GEDAUERT!")
    print("   (Schätzung: 10-50x länger je nach Komplexität)")


def main():
    """Hauptfunktion für alle Performance-Benchmarks"""
    print("🎯 NUMPY PERFORMANCE-DEMONSTRATION")
    print("=" * 60)
    print("Dieses Beispiel zeigt die Performance-Vorteile von NumPy")
    print("gegenüber Pure Python mit praxisrelevanten Berechnungen.")
    print()

    try:
        # Grundlegende Operationen
        benchmark_basic_operations()

        # Produktionsberechnungen
        benchmark_production_calculations()

        # Matrix-Operationen
        benchmark_matrix_operations()

        # Skalierbarkeit
        benchmark_scalability()

        # Real-World Szenario
        benchmark_real_world_scenario()

        print("\n" + "🎉" * 30)
        print("🎉 PERFORMANCE-DEMO ABGESCHLOSSEN 🎉")
        print("🎉" * 30)
        print()
        print("📋 ZUSAMMENFASSUNG:")
        print("• NumPy ist 10-100x schneller als Pure Python")
        print("• Memory-Verbrauch ist deutlich geringer")
        print("• Skaliert besser mit Datengröße")
        print("• Ermöglicht komplexe Berechnungen in Echtzeit")
        print("• Ideal für Bystronic-Produktionsanalysen")
        print()
        print("➡️ NÄCHSTE SCHRITTE:")
        print("1. Probieren Sie die NumPy-Übungen aus")
        print("2. Integrieren Sie NumPy in Ihre eigenen Projekte")
        print("3. Messen Sie die Performance-Verbesserungen!")

    except KeyboardInterrupt:
        print("\n\n⚠️ Benchmark abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler beim Benchmark: {e}")


if __name__ == "__main__":
    main()
