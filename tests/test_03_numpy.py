#!/usr/bin/env python3
"""
Tests für 03_numpy/beispiele

Diese Tests validieren die Funktionalität der NumPy-Beispiele
und demonstrieren Test-Patterns für numerische Berechnungen.
"""

import sys
import warnings
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

# Pfad zu den Beispielen hinzufügen
beispiele_path = Path(__file__).parent.parent / "src" / "03_numpy" / "beispiele"
sys.path.insert(0, str(beispiele_path))

# Module importieren
try:
    import array_manipulation
    import arrays_demo
    import linear_algebra
    import mathematical_operations
    import vba_vs_numpy
except ImportError as e:
    pytest.skip(
        f"NumPy Beispiele können nicht importiert werden: {e}", allow_module_level=True
    )


class TestArraysDemo:
    """Tests für arrays_demo.py Beispiel"""

    def test_module_imports_successfully(self) -> None:
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert arrays_demo is not None

    def test_main_function_exists(self) -> None:
        """Testet, ob die main() Funktion existiert"""
        assert hasattr(arrays_demo, "main")
        assert callable(arrays_demo.main)

    @patch("builtins.print")
    def test_main_runs_without_error(self, mock_print: MagicMock) -> None:
        """Testet, ob main() ohne Fehler läuft"""
        arrays_demo.main()
        assert mock_print.called

    def test_array_creation_methods(self) -> None:
        """Testet verschiedene Array-Erstellungsmethoden"""
        # Array aus Liste
        messwerte = np.array([2.05, 1.98, 2.02, 2.07, 1.95])
        assert messwerte.dtype == np.float64
        assert messwerte.shape == (5,)
        assert np.allclose(messwerte.mean(), 2.014)

        # Nullen-Array
        nullen = np.zeros(10)
        assert nullen.shape == (10,)
        assert np.all(nullen == 0)

        # Einsen-Array
        einsen = np.ones(5)
        assert einsen.shape == (5,)
        assert np.all(einsen == 1)

        # Bereich
        bereich = np.arange(0, 10, 2)
        expected = np.array([0, 2, 4, 6, 8])
        assert np.array_equal(bereich, expected)

        # Linspace
        linear = np.linspace(0, 1, 5)
        expected = np.array([0, 0.25, 0.5, 0.75, 1])
        assert np.allclose(linear, expected)

    def test_2d_array_operations(self) -> None:
        """Testet 2D-Array-Operationen"""
        # 2D-Array erstellen
        matrix = np.array([[8.5, 0.92, 45.2], [7.2, 0.88, 38.7], [9.1, 0.95, 52.3]])

        assert matrix.shape == (3, 3)
        assert matrix.ndim == 2
        assert matrix.size == 9

        # Spalten extrahieren
        laufzeiten = matrix[:, 0]
        assert laufzeiten.shape == (3,)
        assert np.allclose(laufzeiten, [8.5, 7.2, 9.1])

        # Boolean Indexing
        hohe_effizienz = matrix[:, 1] > 0.90
        assert np.sum(hohe_effizienz) == 2  # 0.92 und 0.95

    def test_coordinate_calculations(self) -> None:
        """Testet Koordinatenberechnungen"""
        punkte = np.array([[0, 0], [10, 0], [10, 5], [0, 5], [0, 0]])

        # Entfernungen zwischen Punkten
        differenzen = np.diff(punkte, axis=0)
        entfernungen = np.sqrt(np.sum(differenzen**2, axis=1))

        # Erwartete Entfernungen: 10, 5, 10, 5
        expected = np.array([10, 5, 10, 5])
        assert np.allclose(entfernungen, expected)

        # Gesamtlänge
        gesamtlaenge = np.sum(entfernungen)
        assert gesamtlaenge == 30.0


class TestMathematicalOperations:
    """Tests für mathematical_operations.py Beispiel"""

    def test_module_imports_successfully(self) -> None:
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert mathematical_operations is not None

    @patch("builtins.print")
    def test_main_runs_without_error(self, mock_print: MagicMock) -> None:
        """Testet, ob main() ohne Fehler läuft"""
        mathematical_operations.main()
        assert mock_print.called

    def test_vectorized_operations(self) -> None:
        """Testet vektorisierte Operationen"""
        a = np.array([1, 2, 3, 4, 5])
        b = np.array([2, 3, 4, 5, 6])

        # Grundrechenarten
        assert np.array_equal(a + b, [3, 5, 7, 9, 11])
        assert np.array_equal(a * b, [2, 6, 12, 20, 30])
        assert np.allclose(a / b, [0.5, 0.667, 0.75, 0.8, 0.833], atol=0.001)

    def test_trigonometric_functions(self) -> None:
        """Testet trigonometrische Funktionen"""
        winkel_grad = np.array([0, 30, 45, 60, 90])
        winkel_rad = np.radians(winkel_grad)

        sinus = np.sin(winkel_rad)
        cosinus = np.cos(winkel_rad)

        # Bekannte Werte testen
        assert abs(sinus[0] - 0.0) < 1e-10  # sin(0°) = 0
        assert abs(sinus[-1] - 1.0) < 1e-10  # sin(90°) = 1
        assert abs(cosinus[0] - 1.0) < 1e-10  # cos(0°) = 1
        assert abs(cosinus[-1]) < 1e-10  # cos(90°) = 0

        # Trigonometrische Identität: sin²(x) + cos²(x) = 1
        identitaet = sinus**2 + cosinus**2
        assert np.allclose(identitaet, 1.0)

    def test_statistical_functions(self) -> None:
        """Testet statistische Funktionen"""
        np.random.seed(42)
        data = np.random.normal(50, 10, 100)

        # Grundlegende Statistiken
        mean = np.mean(data)
        std = np.std(data, ddof=1)
        median = np.median(data)

        # Plausibilitätschecks
        assert 45 < mean < 55  # Sollte um 50 liegen
        assert 8 < std < 12  # Sollte um 10 liegen
        assert 45 < median < 55  # Sollte ähnlich wie mean sein

        # Min/Max
        assert np.min(data) < mean < np.max(data)

        # Percentile
        q25 = np.percentile(data, 25)
        q75 = np.percentile(data, 75)
        assert q25 < median < q75

    def test_process_capability_calculation(self) -> None:
        """Testet Prozessfähigkeitsberechnung"""
        # Simulierte Messdaten
        messwerte = np.array([49.8, 50.1, 49.9, 50.2, 49.7, 50.0, 50.1, 49.9])
        sollwert = 50.0
        toleranz = 1.0  # ±0.5

        mittel = np.mean(messwerte)
        std = np.std(messwerte, ddof=1)

        # Cp-Wert
        cp = toleranz / (6 * std)
        assert cp > 0

        # Cpk-Wert
        cpk_ober = (sollwert + toleranz / 2 - mittel) / (3 * std)
        cpk_unter = (mittel - (sollwert - toleranz / 2)) / (3 * std)
        cpk = min(cpk_ober, cpk_unter)
        assert cpk > 0

    def test_exponential_functions(self) -> None:
        """Testet Exponential- und Logarithmusfunktionen"""
        # Exponentialfunktion
        x = np.array([0, 1, 2])
        exp_x = np.exp(x)
        expected = np.array([1, np.e, np.e**2])
        assert np.allclose(exp_x, expected)

        # Logarithmus
        y = np.array([1, 10, 100])
        log_y = np.log10(y)
        expected = np.array([0, 1, 2])
        assert np.allclose(log_y, expected)

        # Natürlicher Logarithmus
        ln_e = np.log(np.e)
        assert abs(ln_e - 1.0) < 1e-10


class TestArrayManipulation:
    """Tests für array_manipulation.py Beispiel"""

    def test_module_imports_successfully(self) -> None:
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert array_manipulation is not None

    @patch("builtins.print")
    def test_main_runs_without_error(self, mock_print: MagicMock) -> None:
        """Testet, ob main() ohne Fehler läuft"""
        array_manipulation.main()
        assert mock_print.called

    def test_reshaping(self) -> None:
        """Testet Array-Reshaping"""
        linear = np.arange(1, 13)  # 1-12
        assert linear.shape == (12,)

        # 3x4 Matrix
        matrix_3x4 = linear.reshape(3, 4)
        assert matrix_3x4.shape == (3, 4)
        assert matrix_3x4[0, 0] == 1
        assert matrix_3x4[2, 3] == 12

        # 2x6 Matrix
        matrix_2x6 = linear.reshape(2, 6)
        assert matrix_2x6.shape == (2, 6)

        # Automatische Dimension
        matrix_auto = linear.reshape(-1, 4)
        assert matrix_auto.shape == (3, 4)

    def test_transposition(self) -> None:
        """Testet Transponierung"""
        matrix = np.array([[1, 2, 3], [4, 5, 6]])

        transposed = matrix.T
        assert transposed.shape == (3, 2)
        assert transposed[0, 0] == 1
        assert transposed[2, 1] == 6

        # Doppelte Transposition = Original
        double_transposed = transposed.T
        assert np.array_equal(matrix, double_transposed)

    def test_concatenation(self) -> None:
        """Testet Array-Zusammenfügung"""
        a = np.array([[1, 2], [3, 4]])
        b = np.array([[5, 6], [7, 8]])

        # Horizontal (axis=1)
        h_concat = np.concatenate([a, b], axis=1)
        expected_h = np.array([[1, 2, 5, 6], [3, 4, 7, 8]])
        assert np.array_equal(h_concat, expected_h)

        # Vertikal (axis=0)
        v_concat = np.concatenate([a, b], axis=0)
        expected_v = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
        assert np.array_equal(v_concat, expected_v)

        # hstack und vstack
        assert np.array_equal(np.hstack([a, b]), h_concat)
        assert np.array_equal(np.vstack([a, b]), v_concat)

    def test_splitting(self) -> None:
        """Testet Array-Aufspaltung"""
        matrix = np.arange(1, 13).reshape(3, 4)

        # Horizontal split
        links, rechts = np.hsplit(matrix, 2)
        assert links.shape == (3, 2)
        assert rechts.shape == (3, 2)

        # Vertikal split
        oben, unten = np.vsplit(matrix, [1])  # Bei Index 1 teilen
        assert oben.shape == (1, 4)
        assert unten.shape == (2, 4)

    def test_broadcasting(self) -> None:
        """Testet Broadcasting-Regeln"""
        # Skalar mit Array
        array = np.array([1, 2, 3])
        result = array * 2
        expected = np.array([2, 4, 6])
        assert np.array_equal(result, expected)

        # 2D mit 1D
        matrix = np.array([[1, 2, 3], [4, 5, 6]])  # (2, 3)
        vector = np.array([10, 20, 30])  # (3,)
        result = matrix + vector  # Broadcasting zu (2, 3)
        expected = np.array([[11, 22, 33], [14, 25, 36]])
        assert np.array_equal(result, expected)

    def test_boolean_indexing(self) -> None:
        """Testet Boolean-Indexierung"""
        data = np.array([1, 5, 3, 8, 2, 7])

        # Elemente > 4
        mask = data > 4
        filtered = data[mask]
        expected = np.array([5, 8, 7])
        assert np.array_equal(filtered, expected)

        # Mehrere Bedingungen
        mask_complex = (data > 2) & (data < 7)
        filtered_complex = data[mask_complex]
        expected_complex = np.array([5, 3])
        assert np.array_equal(filtered_complex, expected_complex)

    def test_advanced_indexing(self) -> None:
        """Testet erweiterte Indexierung"""
        matrix = np.arange(1, 13).reshape(3, 4)

        # Fancy indexing
        rows = [0, 2]
        cols = [1, 3]
        submatrix = matrix[np.ix_(rows, cols)]
        expected = np.array([[2, 4], [10, 12]])
        assert np.array_equal(submatrix, expected)

        # Argmax/Argmin
        flat = matrix.flatten()
        max_idx = np.argmax(flat)
        min_idx = np.argmin(flat)
        assert flat[max_idx] == 12
        assert flat[min_idx] == 1


class TestLinearAlgebra:
    """Tests für linear_algebra.py Beispiel"""

    def test_module_imports_successfully(self) -> None:
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert linear_algebra is not None

    @patch("builtins.print")
    def test_main_runs_without_error(self, mock_print: MagicMock) -> None:
        """Testet, ob main() ohne Fehler läuft"""
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")  # Ignoriere LinAlg warnings
            linear_algebra.main()
        assert mock_print.called

    def test_matrix_operations(self) -> None:
        """Testet Matrix-Grundoperationen"""
        A = np.array([[1, 2], [3, 4]])
        B = np.array([[2, 1], [1, 3]])

        # Matrix-Multiplikation
        C = A @ B
        expected = np.array([[4, 7], [10, 15]])
        assert np.array_equal(C, expected)

        # Element-weise Multiplikation
        D = A * B
        expected_elem = np.array([[2, 2], [3, 12]])
        assert np.array_equal(D, expected_elem)

        # Transposition
        A_T = A.T
        expected_T = np.array([[1, 3], [2, 4]])
        assert np.array_equal(A_T, expected_T)

    def test_matrix_properties(self) -> None:
        """Testet Matrix-Eigenschaften"""
        A = np.array([[2, 1], [1, 2]])

        # Determinante
        det_A = np.linalg.det(A)
        assert abs(det_A - 3.0) < 1e-10

        # Spur
        trace_A = np.trace(A)
        assert trace_A == 4

        # Rang
        rank_A = np.linalg.matrix_rank(A)
        assert rank_A == 2

    def test_linear_system_solving(self) -> None:
        """Testet Lösung linearer Gleichungssysteme"""
        # System: 2x + y = 5, x + 2y = 4
        A = np.array([[2, 1], [1, 2]])
        b = np.array([5, 4])

        # Lösung berechnen
        x = np.linalg.solve(A, b)
        expected = np.array([2, 1])
        assert np.allclose(x, expected)

        # Verifikation: A @ x = b
        verification = A @ x
        assert np.allclose(verification, b)

    def test_matrix_inversion(self) -> None:
        """Testet Matrix-Inversion"""
        A = np.array([[2, 1], [1, 2]])

        # Inverse berechnen
        A_inv = np.linalg.inv(A)

        # Verifikation: A @ A_inv = I
        identity = A @ A_inv
        expected_identity = np.eye(2)
        assert np.allclose(identity, expected_identity)

    def test_eigenvalues_eigenvectors(self) -> None:
        """Testet Eigenwerte und Eigenvektoren"""
        # Symmetrische Matrix für reelle Eigenwerte
        A = np.array([[3, 1], [1, 3]])

        eigenvalues, eigenvectors = np.linalg.eig(A)

        # Eigenwerte sollten real sein
        assert np.all(np.isreal(eigenvalues))

        # Verifikation: A @ v = λ @ v für ersten Eigenvektor
        v1 = eigenvectors[:, 0]
        lambda1 = eigenvalues[0]

        left_side = A @ v1
        right_side = lambda1 * v1

        assert np.allclose(left_side, right_side)

    def test_geometric_transformations(self) -> None:
        """Testet geometrische Transformationen"""
        # Rotation um 90 Grad
        angle = np.pi / 2
        rotation_matrix = np.array(
            [[np.cos(angle), -np.sin(angle)], [np.sin(angle), np.cos(angle)]]
        )

        # Punkt (1, 0) sollte zu (0, 1) werden
        point = np.array([1, 0])
        rotated = rotation_matrix @ point
        expected = np.array([0, 1])
        assert np.allclose(rotated, expected, atol=1e-10)

        # Translation
        translation = np.array([5, 3])
        translated = rotated + translation
        expected_translated = np.array([5, 4])
        assert np.allclose(translated, expected_translated)

    def test_qr_decomposition(self) -> None:
        """Testet QR-Zerlegung"""
        A = np.array([[1, 2], [2, 1], [3, 1]], dtype=float)  # 3x2 Matrix

        Q, R = np.linalg.qr(A)

        # Q sollte orthogonal sein (Q.T @ Q = I)
        QTQ = Q.T @ Q
        assert np.allclose(QTQ, np.eye(Q.shape[1]))

        # R sollte obere Dreiecksmatrix sein
        assert np.allclose(R, np.triu(R))

        # Rekonstruktion: Q @ R = A
        reconstructed = Q @ R
        assert np.allclose(reconstructed, A)

    def test_svd(self) -> None:
        """Testet Singulärwertzerlegung"""
        A = np.array([[1, 2], [3, 4], [5, 6]], dtype=float)  # 3x2 Matrix

        U, s, Vt = np.linalg.svd(A, full_matrices=False)

        # Rekonstruktion
        S = np.diag(s)
        reconstructed = U @ S @ Vt
        assert np.allclose(reconstructed, A)

        # Singulärwerte sollten absteigend sortiert sein
        assert np.all(s[:-1] >= s[1:])


class TestVBAvsNumPy:
    """Tests für vba_vs_numpy.py Beispiel"""

    def test_module_imports_successfully(self) -> None:
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert vba_vs_numpy is not None

    @patch("builtins.print")
    def test_main_runs_without_error(self, mock_print: MagicMock) -> None:
        """Testet, ob main() ohne Fehler läuft"""
        vba_vs_numpy.main()
        assert mock_print.called

    def test_performance_comparison_concepts(self) -> None:
        """Testet Performance-Vergleichskonzepte"""
        # Kleine Daten für Test
        data = np.array([1, 2, 3, 4, 5])

        # NumPy vektorisiert
        numpy_result = data * 2
        expected = np.array([2, 4, 6, 8, 10])
        assert np.array_equal(numpy_result, expected)

        # Python äquivalent (simuliert VBA-Schleife)
        python_result = []
        for x in data:
            python_result.append(x * 2)

        assert python_result == expected.tolist()

    def test_matrix_operations_comparison(self) -> None:
        """Testet Matrix-Operationen Vergleich"""
        # Einfache 2x2 Matrizen
        matrix1 = np.array([[1, 2], [3, 4]])
        matrix2 = np.array([[2, 1], [1, 2]])

        # NumPy: Eine Zeile
        numpy_result = matrix1 @ matrix2

        # "VBA-Stil": Manuelle Berechnung
        manual_result = np.zeros((2, 2))
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    manual_result[i, j] += matrix1[i, k] * matrix2[k, j]

        # Beide sollten gleich sein
        assert np.allclose(numpy_result, manual_result)

    def test_statistical_operations_comparison(self) -> None:
        """Testet statistische Operationen"""
        data = np.array([10, 20, 30, 40, 50])

        # NumPy
        numpy_sum = np.sum(data)
        numpy_mean = np.mean(data)
        numpy_std = np.std(data, ddof=1)

        # Manual (VBA-Stil)
        manual_sum = 0
        for x in data:
            manual_sum += x
        manual_mean = manual_sum / len(data)

        manual_var = 0.0
        for x in data:
            manual_var += (x - manual_mean) ** 2
        manual_var = manual_var / (len(data) - 1)
        manual_std = np.sqrt(manual_var)

        # Vergleiche
        assert numpy_sum == manual_sum
        assert abs(numpy_mean - manual_mean) < 1e-10
        assert abs(numpy_std - manual_std) < 1e-10


class TestNumpyPerformanceAndAccuracy:
    """Zusätzliche Tests für NumPy-spezifische Eigenschaften"""

    def test_array_memory_layout(self) -> None:
        """Testet Array-Speicherlayout"""
        # C-contiguous array
        c_array = np.array([[1, 2, 3], [4, 5, 6]], order="C")
        assert c_array.flags["C_CONTIGUOUS"]

        # Fortran-contiguous array
        f_array = np.array([[1, 2, 3], [4, 5, 6]], order="F")
        assert f_array.flags["F_CONTIGUOUS"]

    def test_dtype_precision(self) -> None:
        """Testet Datentyp-Präzision"""
        # Float32 vs Float64
        data32 = np.array([1.0, 2.0, 3.0], dtype=np.float32)
        data64 = np.array([1.0, 2.0, 3.0], dtype=np.float64)

        assert data32.dtype == np.float32
        assert data64.dtype == np.float64
        assert data32.nbytes < data64.nbytes

    def test_numerical_stability(self) -> None:
        """Testet numerische Stabilität"""
        # Große und kleine Zahlen
        large = 1e10
        small = 1e-10

        # NumPy sollte dies korrekt handhaben
        result = np.array([large, small])
        assert result[0] == large
        assert result[1] == small

        # Summe sollte korrekt sein
        total = np.sum(result)
        expected = large + small
        assert abs(total - expected) / expected < 1e-15

    def test_nan_and_inf_handling(self) -> None:
        """Testet Umgang mit NaN und Inf"""
        data = np.array([1.0, np.nan, np.inf, -np.inf, 2.0])

        # NaN und Inf erkennen
        assert np.isnan(data[1])
        assert np.isinf(data[2])
        assert np.isinf(data[3])

        # Finite Werte
        finite_mask = np.isfinite(data)
        finite_values = data[finite_mask]
        expected_finite = np.array([1.0, 2.0])
        assert np.array_equal(finite_values, expected_finite)

    def test_random_reproducibility(self) -> None:
        """Testet Reproduzierbarkeit von Zufallszahlen"""
        # Seed setzen
        np.random.seed(42)
        random1 = np.random.random(5)

        # Seed erneut setzen
        np.random.seed(42)
        random2 = np.random.random(5)

        # Sollten identisch sein
        assert np.array_equal(random1, random2)

    def test_edge_cases(self) -> None:
        """Testet Edge Cases"""
        # Leere Arrays
        empty = np.array([])
        assert empty.size == 0
        assert empty.shape == (0,)

        # Einzel-Element Arrays
        single = np.array([42])
        assert single.size == 1
        assert single.shape == (1,)
        assert single[0] == 42

        # Sehr große Arrays (nur Shape testen, nicht erstellen)
        # shape = (1000000,)  # 1 Million Elemente wäre noch ok für Test

        # Division durch Null
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            result = np.array([1, 2, 3]) / 0
            assert np.all(np.isinf(result))


if __name__ == "__main__":
    # Führe Tests aus wenn Skript direkt ausgeführt wird
    pytest.main([__file__, "-v"])
