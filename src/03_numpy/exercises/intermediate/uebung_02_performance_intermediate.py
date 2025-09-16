#!/usr/bin/env python3
"""
NumPy Übung 2: Performance-Optimierung und Profiling (Intermediate)
Bystronic Python Grundkurs - Kapitel 3

Diese Übung fokussiert auf Performance-kritische NumPy-Techniken für
produktive Anwendungen mit großen Datenmengen.

Lernziele:
- NumPy Performance-Bottlenecks identifizieren und beheben
- Memory-effiziente Programmierung mit NumPy
- Profiling-Tools für NumPy-Code verwenden
- Vectorization vs. Loops optimieren
- Production-Ready Code für Bystronic-Anwendungen

Schwierigkeitsgrad: 🟡 Intermediate
Geschätzte Bearbeitungszeit: 40-45 Minuten
"""

import gc
import sys
import time
import warnings
from collections.abc import Callable

import numpy as np

warnings.filterwarnings("ignore")


def main():
    """Hauptfunktion für alle Performance-Optimierungs-Übungen"""
    print("🎯 NUMPY INTERMEDIATE ÜBUNG 2: PERFORMANCE-OPTIMIERUNG")
    print("=" * 70)
    print("Diese Übung behandelt Performance-kritische Techniken für")
    print("produktive NumPy-Anwendungen mit großen Datenmengen.")
    print()

    try:
        # Aufgabe 1: Memory-Management und Datentypen
        aufgabe_1_memory_optimization()

        # Aufgabe 2: Vectorization vs. Loops
        aufgabe_2_vectorization_optimization()

        # Aufgabe 3: Broadcasting Performance
        aufgabe_3_broadcasting_performance()

        # Aufgabe 4: Numerical Stability
        aufgabe_4_numerical_stability()

        # Aufgabe 5: Production-Ready Performance
        aufgabe_5_production_performance()

        print("\n" + "🎉" * 60)
        print("🎉 ALLE PERFORMANCE-OPTIMIERUNGS-AUFGABEN ABGESCHLOSSEN! 🎉")
        print("🎉" * 60)
        print("\n📋 GELERNTE KONZEPTE:")
        print("✅ Memory-effiziente Datentypen und Layouts")
        print("✅ Vectorization-Techniken für komplexe Operationen")
        print("✅ Broadcasting-Performance-Optimierung")
        print("✅ Numerische Stabilität und Genauigkeit")
        print("✅ Profiling und Performance-Monitoring")
        print("✅ Production-Ready Code-Patterns")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler in der Übung: {e}")
        print("💡 Tipp: Prüfen Sie Memory-Verfügbarkeit und Array-Größen!")


def get_memory_usage() -> float:
    """Hilfsfunktion: Aktuelle Memory-Nutzung in MB"""
    return sys.getsizeof(gc.get_objects()) / (1024 * 1024)


def profile_function(func: Callable, *args, **kwargs) -> tuple[any, float, float]:
    """Hilfsfunktion: Profiling einer Funktion"""
    # Memory vor Ausführung
    gc.collect()
    memory_before = get_memory_usage()

    # Zeit-Messung
    start_time = time.perf_counter()
    result = func(*args, **kwargs)
    end_time = time.perf_counter()

    # Memory nach Ausführung
    memory_after = get_memory_usage()

    execution_time = end_time - start_time
    memory_delta = memory_after - memory_before

    return result, execution_time, memory_delta


def aufgabe_1_memory_optimization():
    """Aufgabe 1: Memory-Management und Datentypen-Optimierung"""
    print("🎯 AUFGABE 1: MEMORY-MANAGEMENT UND DATENTYPEN")
    print("-" * 50)
    print("Ziel: Optimiere Memory-Verbrauch durch intelligente Datentyp-Wahl")
    print("und Layout-Optimierungen für große Produktionsdaten")
    print()

    start_time = time.time()

    # 1.1 Datentyp-Vergleich
    print("📊 1.1 Datentyp-Optimierung:")

    # Simuliere Produktionsdaten verschiedener Größenordnungen
    n_parts = 1000000  # 1 Million Teile

    # Test verschiedene Datentypen für gleiche Daten
    data_types = {
        "float64": np.float64,
        "float32": np.float32,
        "int64": np.int64,
        "int32": np.int32,
        "int16": np.int16,
        "int8": np.int8,
    }

    print(f"  Datensatz: {n_parts:,} Elemente")
    print()

    memory_usage = {}
    for name, dtype in data_types.items():
        if "float" in name:
            # Simuliere Messwerte (0-100 mit Dezimalstellen)
            test_data = np.random.uniform(0, 100, n_parts).astype(dtype)
        else:
            # Simuliere Zählwerte (0-1000)
            test_data = np.random.randint(0, 1000, n_parts, dtype=dtype)

        memory_mb = test_data.nbytes / (1024 * 1024)
        memory_usage[name] = memory_mb

        print(f"  {name:8s}: {memory_mb:8.2f} MB ({test_data.itemsize} bytes/element)")

    # Vergleiche zu float64 baseline
    baseline_memory = memory_usage["float64"]
    print("\n  Memory-Einsparungen vs. float64:")
    for name, memory in memory_usage.items():
        if name != "float64":
            savings = (1 - memory / baseline_memory) * 100
            print(f"  {name:8s}: {savings:5.1f}% weniger Memory")

    # 1.2 Memory Layout Optimierung
    print("\n📊 1.2 Memory Layout Optimierung:")

    # C-style vs. Fortran-style Layout
    n_rows, n_cols = 10000, 100

    # C-style (row-major) - Standard
    array_c = np.random.randn(n_rows, n_cols)

    # Fortran-style (column-major)
    array_f = np.asfortranarray(array_c)

    print(f"  Array-Dimensionen: {n_rows:,} × {n_cols}")
    print(f"  C-style flags: {array_c.flags}")
    print(f"  Fortran-style flags: {array_f.flags}")

    # Performance-Test: Row-wise vs. Column-wise Access
    print("\n  Access-Pattern Performance:")

    # Row-wise sum (sollte bei C-style schneller sein)
    start = time.perf_counter()
    row_sum_c = np.sum(array_c, axis=1)
    time_row_c = time.perf_counter() - start

    start = time.perf_counter()
    row_sum_f = np.sum(array_f, axis=1)
    time_row_f = time.perf_counter() - start

    # Column-wise sum (sollte bei Fortran-style schneller sein)
    start = time.perf_counter()
    col_sum_c = np.sum(array_c, axis=0)
    time_col_c = time.perf_counter() - start

    start = time.perf_counter()
    col_sum_f = np.sum(array_f, axis=0)
    time_col_f = time.perf_counter() - start

    print(f"    Row-wise sum - C-style:      {time_row_c:.6f}s")
    print(f"    Row-wise sum - Fortran-style: {time_row_f:.6f}s")
    print(f"    Col-wise sum - C-style:      {time_col_c:.6f}s")
    print(f"    Col-wise sum - Fortran-style: {time_col_f:.6f}s")

    # 1.3 Memory-Pool und Preallocated Arrays
    print("\n📊 1.3 Memory-Pool Strategien:")

    # Schlecht: Viele kleine Allokationen
    def many_small_allocations(n_iterations):
        results = []
        for i in range(n_iterations):
            temp_array = np.random.randn(1000)
            result = np.sum(temp_array**2)
            results.append(result)
        return np.array(results)

    # Besser: Preallocated Arrays wiederverwenden
    def preallocated_strategy(n_iterations):
        temp_array = np.empty(1000)  # Preallocate
        results = np.empty(n_iterations)  # Preallocate results

        for i in range(n_iterations):
            temp_array[:] = np.random.randn(1000)  # Reuse memory
            results[i] = np.sum(temp_array**2)

        return results

    n_iterations = 5000
    print(f"  Test: {n_iterations:,} Iterationen")

    # Benchmark beide Strategien
    result1, time1, memory1 = profile_function(many_small_allocations, n_iterations)
    result2, time2, memory2 = profile_function(preallocated_strategy, n_iterations)

    print(f"    Viele Allokationen: {time1:.4f}s, Memory: {memory1:+.1f} MB")
    print(f"    Preallocated:      {time2:.4f}s, Memory: {memory2:+.1f} MB")
    print(f"    Speedup: {time1 / time2:.1f}x")

    # 1.4 View vs. Copy Performance
    print("\n📊 1.4 View vs. Copy Performance:")

    large_array = np.random.randn(10000, 1000)
    print(f"  Basis-Array: {large_array.shape}, {large_array.nbytes / 1024**2:.1f} MB")

    # View (kein Memory-Copy)
    start = time.perf_counter()
    view_result = large_array[::2, ::2]  # Every 2nd row and column
    time_view = time.perf_counter() - start

    # Copy (Memory-Duplikation)
    start = time.perf_counter()
    copy_result = large_array[::2, ::2].copy()
    time_copy = time.perf_counter() - start

    print(f"    View-Operation:  {time_view:.6f}s")
    print(
        f"    Copy-Operation:  {time_copy:.6f}s ({time_copy / time_view:.0f}x langsamer)"
    )
    print(f"    View shares memory: {np.shares_memory(large_array, view_result)}")
    print(f"    Copy shares memory: {np.shares_memory(large_array, copy_result)}")

    duration = time.time() - start_time
    print(f"\n⚡ Memory-Optimierung in {duration:.3f} Sekunden")
    print("💡 Richtige Datentypen können 50-75% Memory sparen!")
    print()


def aufgabe_2_vectorization_optimization():
    """Aufgabe 2: Vectorization vs. Loops Optimierung"""
    print("🎯 AUFGABE 2: VECTORIZATION VS. LOOPS OPTIMIERUNG")
    print("-" * 50)
    print("Ziel: Transformiere komplexe Loop-basierte Algorithmen in")
    print("vectorisierte NumPy-Operationen für maximale Performance")
    print()

    start_time = time.time()

    # 2.1 Komplexe Berechnungs-Vectorization
    print("📊 2.1 Komplexe Berechnungs-Vectorization:")

    # Simuliere SPC (Statistical Process Control) Berechnungen
    n_measurements = 500000
    np.random.seed(42)

    # Messdaten mit systematischen Trends
    timestamps = np.arange(n_measurements)
    base_values = 25.0 + 0.001 * timestamps  # Leichter Trend
    noise = np.random.normal(0, 0.5, n_measurements)
    measurements = base_values + noise

    print(f"  Datensatz: {n_measurements:,} Messungen")

    # Loop-basierte SPC-Berechnung (langsam)
    def spc_calculation_loops(data, window_size=100):
        n = len(data)
        cp_values = []
        cpk_values = []

        for i in range(window_size, n):
            window = data[i - window_size : i]
            mean_val = np.mean(window)
            std_val = np.std(window, ddof=1)

            # Cp und Cpk für Fenster
            tolerance = 1.0  # ±0.5 um Sollwert
            cp = tolerance / (6 * std_val) if std_val > 0 else 0

            target = 25.0
            cpk_upper = (
                (target + tolerance / 2 - mean_val) / (3 * std_val)
                if std_val > 0
                else 0
            )
            cpk_lower = (
                (mean_val - (target - tolerance / 2)) / (3 * std_val)
                if std_val > 0
                else 0
            )
            cpk = min(cpk_upper, cpk_lower)

            cp_values.append(cp)
            cpk_values.append(cpk)

        return np.array(cp_values), np.array(cpk_values)

    # Vectorisierte SPC-Berechnung (schnell)
    def spc_calculation_vectorized(data, window_size=100):
        n = len(data)

        # Sliding window mit Broadcasting
        indices = (
            np.arange(window_size)[None, :] + np.arange(n - window_size + 1)[:, None]
        )
        windowed_data = data[indices]  # Shape: (n_windows, window_size)

        # Alle Statistiken mit Vectorization
        means = np.mean(windowed_data, axis=1)
        stds = np.std(windowed_data, axis=1, ddof=1)

        # Cp und Cpk vectorisiert
        tolerance = 1.0
        target = 25.0

        # Verhindere Division durch 0
        safe_stds = np.where(stds > 0, stds, np.inf)

        cp_values = tolerance / (6 * safe_stds)

        cpk_upper = (target + tolerance / 2 - means) / (3 * safe_stds)
        cpk_lower = (means - (target - tolerance / 2)) / (3 * safe_stds)
        cpk_values = np.minimum(cpk_upper, cpk_lower)

        return cp_values, cpk_values

    # Performance-Vergleich
    window_size = 100

    print(f"  Gleitendes Fenster: {window_size} Messungen")

    start = time.perf_counter()
    cp_loop, cpk_loop = spc_calculation_loops(measurements, window_size)
    time_loop = time.perf_counter() - start

    start = time.perf_counter()
    cp_vec, cpk_vec = spc_calculation_vectorized(measurements, window_size)
    time_vec = time.perf_counter() - start

    print(f"    Loop-basiert:   {time_loop:.4f}s")
    print(f"    Vectorisiert:   {time_vec:.4f}s")
    print(f"    Speedup:        {time_loop / time_vec:.1f}x")

    # Validierung der Ergebnisse
    max_diff_cp = np.max(np.abs(cp_loop - cp_vec))
    max_diff_cpk = np.max(np.abs(cpk_loop - cpk_vec))
    print(f"    Max Unterschied Cp:  {max_diff_cp:.2e}")
    print(f"    Max Unterschied Cpk: {max_diff_cpk:.2e}")

    # 2.2 Conditional Logic Vectorization
    print("\n📊 2.2 Conditional Logic Vectorization:")

    # Komplexe Qualitätsbewertung mit vielen Bedingungen
    n_parts = 1000000
    np.random.seed(123)

    # Mehrere Qualitätsmerkmale
    dimensions = np.random.normal(25.0, 0.1, (n_parts, 3))  # Länge, Breite, Höhe
    surface_quality = np.random.uniform(0, 10, n_parts)
    hardness = np.random.normal(45, 2, n_parts)

    print(f"  Qualitätsdaten: {n_parts:,} Teile × 5 Merkmale")

    # Loop-basierte Klassifikation
    def classify_parts_loops(dims, surface, hardness):
        classifications = []

        for i in range(len(dims)):
            # Komplexe Bewertungslogik
            dim_ok = np.all(np.abs(dims[i] - 25.0) <= 0.2)
            surface_grade = "A" if surface[i] >= 8 else "B" if surface[i] >= 6 else "C"
            hardness_ok = 43 <= hardness[i] <= 47

            if dim_ok and surface_grade == "A" and hardness_ok:
                classification = "Premium"
            elif dim_ok and surface_grade in ["A", "B"] and hardness_ok:
                classification = "Standard"
            elif dim_ok or (surface_grade != "C" and hardness_ok):
                classification = "Acceptable"
            else:
                classification = "Reject"

            classifications.append(classification)

        return classifications

    # Vectorisierte Klassifikation
    def classify_parts_vectorized(dims, surface, hardness):
        n = len(dims)

        # Alle Bedingungen vectorisiert prüfen
        dim_deviations = np.abs(dims - 25.0)
        dim_ok = np.all(dim_deviations <= 0.2, axis=1)

        surface_a = surface >= 8
        surface_b = surface >= 6
        surface_c = surface < 6

        hardness_ok = (43 <= hardness) & (hardness <= 47)

        # Klassifikation mit np.where
        classifications = np.full(n, "Reject", dtype="U10")

        # Von schlechteste zu beste Kategorie (überschreibt vorherige)
        acceptable_mask = dim_ok | ((~surface_c) & hardness_ok)
        classifications = np.where(acceptable_mask, "Acceptable", classifications)

        standard_mask = dim_ok & (surface_a | surface_b) & hardness_ok
        classifications = np.where(standard_mask, "Standard", classifications)

        premium_mask = dim_ok & surface_a & hardness_ok
        classifications = np.where(premium_mask, "Premium", classifications)

        return classifications

    # Performance-Test
    start = time.perf_counter()
    class_loop = classify_parts_loops(dimensions, surface_quality, hardness)
    time_loop = time.perf_counter() - start

    start = time.perf_counter()
    class_vec = classify_parts_vectorized(dimensions, surface_quality, hardness)
    time_vec = time.perf_counter() - start

    print(f"    Loop-basiert:   {time_loop:.4f}s")
    print(f"    Vectorisiert:   {time_vec:.4f}s")
    print(f"    Speedup:        {time_loop / time_vec:.1f}x")

    # Ergebnis-Validierung
    loop_counts = {cls: class_loop.count(cls) for cls in set(class_loop)}
    vec_counts = {cls: np.sum(class_vec == cls) for cls in np.unique(class_vec)}

    print("    Klassifikations-Verteilung (Loops vs. Vectorized):")
    for cls in ["Premium", "Standard", "Acceptable", "Reject"]:
        loop_count = loop_counts.get(cls, 0)
        vec_count = vec_counts.get(cls, 0)
        print(f"      {cls:10s}: {loop_count:6d} vs {vec_count:6d}")

    # 2.3 ufuncs für Custom Operations
    print("\n📊 2.3 Universal Functions (ufuncs):")

    # Custom Berechnung: Komplexe Toleranzprüfung
    def complex_tolerance_check_python(measurement, target, lower_tol, upper_tol):
        """Python-Funktion für einzelne Werte"""
        if measurement < target - lower_tol:
            return -1  # Untermaß
        elif measurement > target + upper_tol:
            return 1  # Übermaß
        else:
            return 0  # OK

    # Erstelle ufunc
    tolerance_check_ufunc = np.frompyfunc(complex_tolerance_check_python, 4, 1)

    # Test-Daten
    measurements = np.random.normal(25.0, 0.3, 100000)
    targets = np.full_like(measurements, 25.0)
    lower_tolerances = np.full_like(measurements, 0.2)
    upper_tolerances = np.full_like(measurements, 0.15)  # Asymmetrische Toleranz

    print(f"  Test: {len(measurements):,} asymmetrische Toleranzprüfungen")

    # Loop vs. ufunc
    start = time.perf_counter()
    results_loop = [
        complex_tolerance_check_python(m, t, lt, ut)
        for m, t, lt, ut in zip(
            measurements, targets, lower_tolerances, upper_tolerances, strict=False
        )
    ]
    time_loop = time.perf_counter() - start

    start = time.perf_counter()
    results_ufunc = tolerance_check_ufunc(
        measurements, targets, lower_tolerances, upper_tolerances
    )
    time_ufunc = time.perf_counter() - start

    print(f"    Python Loops:   {time_loop:.4f}s")
    print(f"    ufunc:          {time_ufunc:.4f}s")
    print(f"    Speedup:        {time_loop / time_ufunc:.1f}x")

    # Ergebnis-Counts
    unique_loop, counts_loop = np.unique(results_loop, return_counts=True)
    unique_ufunc, counts_ufunc = np.unique(
        results_ufunc.astype(int), return_counts=True
    )

    print("    Ergebnis-Verteilung:")
    status_names = {-1: "Untermaß", 0: "OK", 1: "Übermaß"}
    for status, name in status_names.items():
        loop_count = (
            counts_loop[unique_loop == status][0] if status in unique_loop else 0
        )
        ufunc_count = (
            counts_ufunc[unique_ufunc == status][0] if status in unique_ufunc else 0
        )
        print(f"      {name:8s}: {loop_count:5d} vs {ufunc_count:5d}")

    duration = time.time() - start_time
    print(f"\n⚡ Vectorization-Optimierung in {duration:.3f} Sekunden")
    print("🚀 Vectorization kann 10-100x Speedup bringen!")
    print()


def aufgabe_3_broadcasting_performance():
    """Aufgabe 3: Broadcasting Performance-Optimierung"""
    print("🎯 AUFGABE 3: BROADCASTING PERFORMANCE-OPTIMIERUNG")
    print("-" * 50)
    print("Ziel: Optimiere Broadcasting-Operationen für verschiedene")
    print("Array-Größen und identifiziere Performance-Bottlenecks")
    print()

    start_time = time.time()

    # 3.1 Broadcasting Shape-Optimierung
    print("📊 3.1 Broadcasting Shape-Optimierung:")

    # Verschiedene Broadcasting-Szenarien testen
    scenarios = [
        ("Small-Small", (1000, 100), (100,)),
        ("Medium-Medium", (5000, 200), (200,)),
        ("Large-Small", (10000, 50), (50,)),
        ("Large-Large", (10000, 500), (500,)),
        ("Huge-Tiny", (50000, 10), (10,)),
    ]

    print("  Broadcasting Performance für verschiedene Shapes:")
    print("  Scenario        Array1 Shape    Array2 Shape    Time      Memory")
    print("  " + "-" * 65)

    for name, shape1, shape2 in scenarios:
        # Erstelle Test-Arrays
        array1 = np.random.randn(*shape1).astype(np.float32)
        array2 = np.random.randn(*shape2).astype(np.float32)

        # Memory vor Operation
        memory_before = array1.nbytes + array2.nbytes

        # Broadcasting-Operation
        start = time.perf_counter()
        result = array1 + array2  # Broadcasting
        time_broadcast = time.perf_counter() - start

        # Memory nach Operation
        memory_after = memory_before + result.nbytes

        print(
            f"  {name:14s}  {str(shape1):14s}  {str(shape2):12s}  "
            f"{time_broadcast:.5f}s  {memory_after / 1024**2:.1f} MB"
        )

    # 3.2 Memory-Layout Auswirkungen auf Broadcasting
    print("\n📊 3.2 Memory-Layout Auswirkungen:")

    # Große Arrays für signifikante Unterschiede
    large_shape = (5000, 2000)
    broadcast_shape = (2000,)

    # C-order (row-major)
    array_c = np.random.randn(*large_shape)
    broadcast_array = np.random.randn(*broadcast_shape)

    # Fortran-order (column-major)
    array_f = np.asfortranarray(array_c)

    print(f"  Array Shape: {large_shape}, Broadcast Shape: {broadcast_shape}")

    # Broadcasting mit C-order
    start = time.perf_counter()
    result_c = array_c + broadcast_array
    time_c = time.perf_counter() - start

    # Broadcasting mit Fortran-order
    start = time.perf_counter()
    result_f = array_f + broadcast_array
    time_f = time.perf_counter() - start

    print(f"    C-order (row-major):      {time_c:.5f}s")
    print(f"    Fortran-order (col-major): {time_f:.5f}s")
    print(f"    Performance-Ratio:        {time_f / time_c:.2f}x")

    # 3.3 Broadcasting vs. Alternative Strategien
    print("\n📊 3.3 Broadcasting vs. Alternative Strategien:")

    # Test-Szenario: Matrix + Vektor über verschiedene Achsen
    matrix_shape = (8000, 1000)
    vector_shapes = [(8000,), (1000,)]

    matrix = np.random.randn(*matrix_shape).astype(np.float32)

    for i, vec_shape in enumerate(vector_shapes):
        vector = np.random.randn(*vec_shape).astype(np.float32)
        axis = i  # 0 für rows, 1 für columns

        print(f"\n  Szenario {i + 1}: Matrix {matrix_shape} + Vektor {vec_shape}")

        # Methode 1: Broadcasting
        start = time.perf_counter()
        if axis == 0:
            result_broadcast = matrix + vector[:, np.newaxis]
        else:
            result_broadcast = matrix + vector
        time_broadcast = time.perf_counter() - start

        # Methode 2: Tile/Repeat
        start = time.perf_counter()
        if axis == 0:
            tiled_vector = np.tile(vector[:, np.newaxis], (1, matrix_shape[1]))
        else:
            tiled_vector = np.tile(vector, (matrix_shape[0], 1))
        result_tile = matrix + tiled_vector
        time_tile = time.perf_counter() - start

        # Methode 3: Loop-basiert (nur für kleine Samples)
        sample_size = 100
        matrix_sample = matrix[:sample_size, :sample_size]
        vector_sample = vector[:sample_size]

        start = time.perf_counter()
        result_loop = np.zeros_like(matrix_sample)
        if axis == 0:
            for j in range(matrix_sample.shape[1]):
                result_loop[:, j] = matrix_sample[:, j] + vector_sample
        else:
            for j in range(matrix_sample.shape[0]):
                result_loop[j, :] = matrix_sample[j, :] + vector_sample
        time_loop = time.perf_counter() - start
        # Skaliere auf volle Größe
        time_loop_scaled = time_loop * (matrix.size / matrix_sample.size)

        print(f"    Broadcasting: {time_broadcast:.5f}s")
        print(f"    Tile/Repeat:  {time_tile:.5f}s ({time_tile / time_broadcast:.1f}x)")
        print(
            f"    Loops (est.): {time_loop_scaled:.5f}s ({time_loop_scaled / time_broadcast:.1f}x)"
        )

        # Memory-Verbrauch
        memory_broadcast = result_broadcast.nbytes
        memory_tile = result_tile.nbytes + tiled_vector.nbytes
        print(f"    Memory Broadcasting: {memory_broadcast / 1024**2:.1f} MB")
        print(
            f"    Memory Tile:         {memory_tile / 1024**2:.1f} MB ({memory_tile / memory_broadcast:.1f}x)"
        )

    # 3.4 In-Place Broadcasting
    print("\n📊 3.4 In-Place Broadcasting Performance:")

    # Test In-Place vs. neue Array-Erstellung
    test_sizes = [1000, 5000, 10000]

    for size in test_sizes:
        matrix = np.random.randn(size, size).astype(np.float32)
        vector = np.random.randn(size).astype(np.float32)

        print(f"\n  Array-Größe: {size} × {size}")

        # Standard Broadcasting (neue Matrix)
        matrix_copy = matrix.copy()
        start = time.perf_counter()
        result_new = matrix_copy + vector
        time_new = time.perf_counter() - start

        # In-Place Broadcasting
        matrix_copy = matrix.copy()
        start = time.perf_counter()
        matrix_copy += vector  # In-place
        time_inplace = time.perf_counter() - start

        # Memory-Verbrauch
        memory_new = matrix.nbytes + result_new.nbytes
        memory_inplace = matrix.nbytes

        print(f"    Standard:  {time_new:.5f}s, {memory_new / 1024**2:.1f} MB")
        print(f"    In-Place:  {time_inplace:.5f}s, {memory_inplace / 1024**2:.1f} MB")
        print(f"    Speedup:   {time_new / time_inplace:.2f}x")
        print(f"    Memory Savings: {(1 - memory_inplace / memory_new) * 100:.1f}%")

    duration = time.time() - start_time
    print(f"\n⚡ Broadcasting-Performance in {duration:.3f} Sekunden")
    print("💡 Broadcasting ist fast immer optimal - aber Layout matters!")
    print()


def aufgabe_4_numerical_stability():
    """Aufgabe 4: Numerische Stabilität und Genauigkeit"""
    print("🎯 AUFGABE 4: NUMERISCHE STABILITÄT UND GENAUIGKEIT")
    print("-" * 50)
    print("Ziel: Identifiziere und behebe numerische Probleme in")
    print("produktions-kritischen Berechnungen")
    print()

    start_time = time.time()

    # 4.1 Floating-Point Präzisionsprobleme
    print("📊 4.1 Floating-Point Präzisionsprobleme:")

    # Problematische Berechnungen identifizieren
    print("  Klassische Präzisionsprobleme:")

    # Problem 1: Subtraktion ähnlicher Zahlen
    a = np.array([1.0000001, 1.0000002, 1.0000003])
    b = np.array([1.0000000, 1.0000000, 1.0000000])

    diff_float32 = a.astype(np.float32) - b.astype(np.float32)
    diff_float64 = a.astype(np.float64) - b.astype(np.float64)

    print("    Subtraktion ähnlicher Zahlen:")
    print(f"      float32: {diff_float32}")
    print(f"      float64: {diff_float64}")
    print(
        f"      Relative Fehler: {np.abs(diff_float32 - diff_float64) / diff_float64}"
    )

    # Problem 2: Summation vieler kleiner Zahlen
    n = 1000000
    small_values = np.full(n, 1e-7, dtype=np.float32)

    # Naive Summation
    sum_naive = np.sum(small_values)

    # Kahan-Summation (kompensierte Summation)
    def kahan_sum(arr):
        sum_val = 0.0
        compensation = 0.0

        for x in arr:
            y = x - compensation
            temp = sum_val + y
            compensation = (temp - sum_val) - y
            sum_val = temp

        return sum_val

    sum_kahan = kahan_sum(small_values)
    expected = n * 1e-7

    print(f"\n    Summation von {n:,} kleinen Zahlen:")
    print(f"      Erwartet:       {expected:.10f}")
    print(f"      Naive Summe:    {sum_naive:.10f}")
    print(f"      Kahan-Summe:    {sum_kahan:.10f}")
    print(f"      Relativer Fehler (naive): {abs(sum_naive - expected) / expected:.2e}")
    print(f"      Relativer Fehler (Kahan): {abs(sum_kahan - expected) / expected:.2e}")

    # 4.2 Numerisch stabile Algorithmen
    print("\n📊 4.2 Numerisch stabile Algorithmen:")

    # Beispiel: Standardabweichung
    # Instabile "naive" Formel vs. stabile "two-pass" Formel

    # Test-Daten mit großen Werten aber kleiner Varianz
    large_base = 1e8
    n_samples = 10000
    np.random.seed(42)
    data = large_base + np.random.normal(0, 1, n_samples)

    print("  Standardabweichung-Berechnung:")
    print(f"    Daten: {n_samples:,} Werte um {large_base:.0e} ± 1")

    # Naive Formel: sqrt(E[X²] - E[X]²)
    def std_naive(arr):
        mean_x = np.mean(arr)
        mean_x2 = np.mean(arr**2)
        variance = mean_x2 - mean_x**2
        return np.sqrt(variance) if variance > 0 else 0

    # Two-pass Formel: sqrt(E[(X - μ)²])
    def std_stable(arr):
        mean_x = np.mean(arr)
        variance = np.mean((arr - mean_x) ** 2)
        return np.sqrt(variance)

    std_naive_result = std_naive(data.astype(np.float32))
    std_stable_result = std_stable(data.astype(np.float32))
    std_numpy = np.std(data.astype(np.float32), ddof=0)
    std_reference = np.std(
        data.astype(np.float64), ddof=0
    )  # Double precision reference

    print(f"    Naive Formel:     {std_naive_result:.6f}")
    print(f"    Stabile Formel:   {std_stable_result:.6f}")
    print(f"    NumPy (float32):  {std_numpy:.6f}")
    print(f"    Referenz (float64): {std_reference:.6f}")

    # 4.3 Condition Numbers und Ill-conditioned Problems
    print("\n📊 4.3 Konditionszahlen und schlecht konditionierte Probleme:")

    # Erstelle Matrizen mit verschiedenen Konditionszahlen
    condition_numbers = [1e2, 1e6, 1e10, 1e14]

    for cond_target in condition_numbers:
        # Erstelle Matrix mit gewünschter Konditionszahl
        n = 100
        # Start mit zufälliger Matrix
        A = np.random.randn(n, n)
        U, S, Vt = np.linalg.svd(A)

        # Setze Singulärwerte für gewünschte Konditionszahl
        S_new = np.linspace(1, 1 / cond_target, n)
        A_conditioned = U @ np.diag(S_new) @ Vt

        # Berechne tatsächliche Konditionszahl
        actual_cond = np.linalg.cond(A_conditioned)

        # Löse lineares System
        x_true = np.random.randn(n)
        b = A_conditioned @ x_true

        # Füge kleines Rauschen zu b hinzu
        noise_level = 1e-10
        b_noisy = b + noise_level * np.random.randn(n)

        # Löse mit und ohne Rauschen
        x_clean = np.linalg.solve(A_conditioned, b)
        x_noisy = np.linalg.solve(A_conditioned, b_noisy)

        # Analysiere Fehler-Verstärkung
        input_error = np.linalg.norm(b_noisy - b) / np.linalg.norm(b)
        output_error = np.linalg.norm(x_noisy - x_clean) / np.linalg.norm(x_clean)
        amplification = output_error / input_error

        print(f"    Konditionszahl {actual_cond:.1e}:")
        print(f"      Input-Fehler:  {input_error:.2e}")
        print(f"      Output-Fehler: {output_error:.2e}")
        print(f"      Verstärkung:   {amplification:.1e} (Theorie: {actual_cond:.1e})")

    # 4.4 Overflow/Underflow Behandlung
    print("\n📊 4.4 Overflow/Underflow Behandlung:")

    # Beispiel: Log-Sum-Exp für numerische Stabilität
    def log_sum_exp_naive(x):
        return np.log(np.sum(np.exp(x)))

    def log_sum_exp_stable(x):
        x_max = np.max(x)
        return x_max + np.log(np.sum(np.exp(x - x_max)))

    # Test mit großen Werten (würde overflow verursachen)
    large_values = np.array([700, 800, 900, 1000])  # exp(1000) würde overflow

    print(f"  Log-Sum-Exp für große Werte: {large_values}")

    try:
        result_naive = log_sum_exp_naive(large_values)
        print(f"    Naive Methode:  {result_naive}")
    except:
        print("    Naive Methode:  OVERFLOW!")

    result_stable = log_sum_exp_stable(large_values)
    print(f"    Stabile Methode: {result_stable:.6f}")

    # Test mit kleinen Werten (würde underflow verursachen)
    small_values = np.array([-700, -800, -900, -1000])  # exp(-1000) ≈ 0

    print(f"\n  Log-Sum-Exp für kleine Werte: {small_values}")

    result_naive_small = log_sum_exp_naive(small_values)
    result_stable_small = log_sum_exp_stable(small_values)

    print(f"    Naive Methode:   {result_naive_small:.6f}")
    print(f"    Stabile Methode: {result_stable_small:.6f}")

    duration = time.time() - start_time
    print(f"\n⚡ Numerische Stabilität in {duration:.3f} Sekunden")
    print("⚠️ Numerische Probleme können produktions-kritische Fehler verursachen!")
    print()


def aufgabe_5_production_performance():
    """Aufgabe 5: Production-Ready Performance-Patterns"""
    print("🎯 AUFGABE 5: PRODUCTION-READY PERFORMANCE-PATTERNS")
    print("-" * 50)
    print("Ziel: Implementiere produktions-taugliche Performance-Patterns")
    print("für Bystronic-Anwendungen mit großen Datenmengen")
    print()

    start_time = time.time()

    # 5.1 Memory-Pooling für kontinuierliche Verarbeitung
    print("📊 5.1 Memory-Pooling für kontinuierliche Verarbeitung:")

    class MemoryPool:
        """Einfacher Memory-Pool für NumPy Arrays"""

        def __init__(self):
            self.pools = {}

        def get_array(self, shape, dtype=np.float64):
            key = (shape, dtype)
            if key not in self.pools:
                self.pools[key] = []

            if self.pools[key]:
                return self.pools[key].pop()
            else:
                return np.empty(shape, dtype=dtype)

        def return_array(self, arr):
            key = (arr.shape, arr.dtype)
            if key not in self.pools:
                self.pools[key] = []
            self.pools[key].append(arr)

        def get_stats(self):
            total_arrays = sum(len(pool) for pool in self.pools.values())
            total_memory = sum(
                sum(arr.nbytes for arr in pool) for pool in self.pools.values()
            )
            return total_arrays, total_memory

    # Simuliere kontinuierliche Datenverarbeitung
    def process_batches_no_pool(n_batches, batch_size):
        """Ohne Memory-Pool (viele Allokationen)"""
        results = []
        for i in range(n_batches):
            # Simuliere eingehende Daten
            data = np.random.randn(batch_size, 100)

            # Verarbeitung
            processed = np.mean(data**2, axis=1)
            results.append(np.sum(processed))

        return results

    def process_batches_with_pool(n_batches, batch_size, pool):
        """Mit Memory-Pool (Array-Wiederverwendung)"""
        results = []

        for i in range(n_batches):
            # Hole Array aus Pool
            data = pool.get_array((batch_size, 100))
            data[:] = np.random.randn(batch_size, 100)  # Füllen

            # Verarbeitung
            temp_result = pool.get_array((batch_size,))
            temp_result[:] = np.mean(data**2, axis=1)

            result = np.sum(temp_result)
            results.append(result)

            # Arrays zurück in Pool
            pool.return_array(data)
            pool.return_array(temp_result)

        return results

    n_batches = 1000
    batch_size = 500
    pool = MemoryPool()

    print(f"  Simulation: {n_batches} Batches à {batch_size} Samples")

    # Benchmark ohne Pool
    start = time.perf_counter()
    results_no_pool = process_batches_no_pool(n_batches, batch_size)
    time_no_pool = time.perf_counter() - start

    # Benchmark mit Pool
    start = time.perf_counter()
    results_with_pool = process_batches_with_pool(n_batches, batch_size, pool)
    time_with_pool = time.perf_counter() - start

    pool_arrays, pool_memory = pool.get_stats()

    print(f"    Ohne Pool:  {time_no_pool:.4f}s")
    print(
        f"    Mit Pool:   {time_with_pool:.4f}s ({time_no_pool / time_with_pool:.1f}x speedup)"
    )
    print(
        f"    Pool Stats: {pool_arrays} Arrays, {pool_memory / 1024**2:.1f} MB cached"
    )

    # 5.2 Streaming/Chunked Processing
    print("\n📊 5.2 Streaming/Chunked Processing:")

    def process_large_dataset_memory_efficient(total_size, chunk_size):
        """Verarbeite große Datasets chunk-weise"""

        results = []
        n_chunks = (total_size + chunk_size - 1) // chunk_size  # Ceiling division

        # Statistiken über alle Chunks
        running_mean = 0
        running_var = 0
        total_count = 0

        for chunk_idx in range(n_chunks):
            start_idx = chunk_idx * chunk_size
            end_idx = min(start_idx + chunk_size, total_size)
            current_chunk_size = end_idx - start_idx

            # Simuliere Chunk-Laden (würde normalerweise von Disk/DB kommen)
            chunk_data = np.random.normal(25.0, 1.0, (current_chunk_size, 10))

            # Chunk-Statistiken
            chunk_mean = np.mean(chunk_data, axis=0)
            chunk_var = np.var(chunk_data, axis=0, ddof=1)

            # Update running statistics (Welford's algorithm)
            old_count = total_count
            total_count += current_chunk_size

            if old_count == 0:
                running_mean = chunk_mean
                running_var = chunk_var * (current_chunk_size - 1) / total_count
            else:
                # Update mean
                delta = chunk_mean - running_mean
                running_mean += delta * current_chunk_size / total_count

                # Update variance (vereinfacht für Demo)
                running_var = (
                    old_count * running_var + (current_chunk_size - 1) * chunk_var
                ) / (total_count - 1)

            # Chunk-spezifische Verarbeitung
            chunk_result = {
                "chunk_idx": chunk_idx,
                "size": current_chunk_size,
                "mean": np.copy(chunk_mean),
                "std": np.sqrt(chunk_var),
                "outliers": np.sum(
                    np.abs(chunk_data - chunk_mean) > 3 * np.sqrt(chunk_var), axis=0
                ),
            }

            results.append(chunk_result)

        return results, running_mean, np.sqrt(running_var)

    # Test verschiedene Chunk-Größen
    total_size = 1000000
    chunk_sizes = [10000, 50000, 100000]

    print(f"  Dataset: {total_size:,} Samples")

    for chunk_size in chunk_sizes:
        start = time.perf_counter()
        chunk_results, final_mean, final_std = process_large_dataset_memory_efficient(
            total_size, chunk_size
        )
        processing_time = time.perf_counter() - start

        n_chunks = len(chunk_results)
        print(
            f"    Chunk-Größe {chunk_size:,}: {n_chunks:3d} Chunks, {processing_time:.3f}s"
        )
        print(f"      Final Stats: μ={final_mean[0]:.3f}, σ={final_std[0]:.3f}")

    # 5.3 Parallel Processing Vorbereitung
    print("\n📊 5.3 Parallel Processing Vorbereitung:")

    # Zeige wie NumPy-Code für Parallelisierung vorbereitet wird
    def parallelizable_quality_analysis(data_chunk):
        """Qualitätsanalyse die parallel verarbeitet werden kann"""

        # Statistische Kennwerte
        means = np.mean(data_chunk, axis=0)
        stds = np.std(data_chunk, axis=0, ddof=1)

        # Ausreißer-Detektion
        z_scores = np.abs((data_chunk - means) / stds)
        outliers = np.sum(z_scores > 3, axis=0)

        # Prozessfähigkeiten (Cp)
        tolerances = np.array([0.2, 0.1, 0.05, 0.1, 0.15])  # Beispiel-Toleranzen
        cp_values = tolerances / (6 * stds)

        return {
            "means": means,
            "stds": stds,
            "outliers": outliers,
            "cp_values": cp_values,
            "sample_count": len(data_chunk),
        }

    # Simuliere Daten für mehrere "Worker"
    n_workers = 4
    total_samples = 100000
    samples_per_worker = total_samples // n_workers

    print(
        f"  Parallelisierung Setup: {n_workers} Worker à {samples_per_worker:,} Samples"
    )

    # Sequential Processing (Baseline)
    start = time.perf_counter()
    all_data = np.random.normal(
        [25, 15, 8, 12, 20], [1, 0.5, 0.2, 0.8, 1.2], (total_samples, 5)
    )
    sequential_result = parallelizable_quality_analysis(all_data)
    time_sequential = time.perf_counter() - start

    # Simulated Parallel Processing (wie es mit multiprocessing aussehen würde)
    start = time.perf_counter()
    worker_results = []
    for worker_id in range(n_workers):
        start_idx = worker_id * samples_per_worker
        end_idx = (worker_id + 1) * samples_per_worker
        worker_data = all_data[start_idx:end_idx]

        worker_result = parallelizable_quality_analysis(worker_data)
        worker_results.append(worker_result)

    # Combine worker results
    combined_means = np.mean([r["means"] for r in worker_results], axis=0)
    combined_stds = np.sqrt(np.mean([r["stds"] ** 2 for r in worker_results], axis=0))
    combined_outliers = np.sum([r["outliers"] for r in worker_results], axis=0)

    time_parallel_sim = time.perf_counter() - start

    print(f"    Sequential:  {time_sequential:.4f}s")
    print(f"    Parallel Sim: {time_parallel_sim:.4f}s")
    print(
        f"    Theoretical Speedup: {time_sequential / (time_parallel_sim / n_workers):.1f}x"
    )

    # Vergleiche Ergebnisse
    mean_diff = np.max(np.abs(sequential_result["means"] - combined_means))
    print(f"    Result Accuracy: Max difference in means = {mean_diff:.6f}")

    # 5.4 Performance Monitoring
    print("\n📊 5.4 Performance Monitoring:")

    class PerformanceMonitor:
        """Einfacher Performance-Monitor für NumPy-Operationen"""

        def __init__(self):
            self.metrics = {}

        def measure(self, operation_name):
            """Context manager für Zeitmessung"""
            return self._MeasureContext(self, operation_name)

        class _MeasureContext:
            def __init__(self, monitor, name):
                self.monitor = monitor
                self.name = name
                self.start_time = None

            def __enter__(self):
                gc.collect()  # Clean garbage before measurement
                self.start_time = time.perf_counter()
                return self

            def __exit__(self, exc_type, exc_val, exc_tb):
                duration = time.perf_counter() - self.start_time

                if self.name not in self.monitor.metrics:
                    self.monitor.metrics[self.name] = []

                self.monitor.metrics[self.name].append(duration)

        def get_stats(self):
            stats = {}
            for name, times in self.metrics.items():
                times_array = np.array(times)
                stats[name] = {
                    "count": len(times),
                    "mean": np.mean(times_array),
                    "std": np.std(times_array),
                    "min": np.min(times_array),
                    "max": np.max(times_array),
                    "total": np.sum(times_array),
                }
            return stats

    # Demonstriere Performance-Monitoring
    monitor = PerformanceMonitor()

    # Simuliere verschiedene Operationen
    n_iterations = 100
    array_size = 10000

    for i in range(n_iterations):
        # Matrix-Multiplikation
        with monitor.measure("matrix_multiply"):
            a = np.random.randn(array_size // 100, array_size // 100)
            b = np.random.randn(array_size // 100, array_size // 100)
            result = a @ b

        # FFT
        with monitor.measure("fft"):
            signal = np.random.randn(array_size)
            fft_result = np.fft.fft(signal)

        # Statistical Operations
        with monitor.measure("statistics"):
            data = np.random.randn(array_size)
            mean_val = np.mean(data)
            std_val = np.std(data)
            percentiles = np.percentile(data, [25, 50, 75])

    # Performance-Statistiken ausgeben
    stats = monitor.get_stats()
    print(f"  Performance-Statistiken ({n_iterations} Iterationen):")

    for operation, stat in stats.items():
        print(
            f"    {operation:15s}: μ={stat['mean']:.5f}s, σ={stat['std']:.5f}s, "
            f"range=[{stat['min']:.5f}, {stat['max']:.5f}]s"
        )

    duration = time.time() - start_time
    print(f"\n⚡ Production-Performance in {duration:.3f} Sekunden")
    print("🚀 Production-Ready Code erfordert systematische Performance-Überwachung!")
    print()


if __name__ == "__main__":
    main()
