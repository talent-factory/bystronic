#!/usr/bin/env python3
"""
NumPy Advanced: Algorithmische Optimierung und Mathematische Verfahren
=================================================================

Übung 2: Fortgeschrittene algorithmische Techniken und mathematische Verfahren
mit NumPy für industrielle Anwendungen.

Lernziele:
- Implementierung numerischer Algorithmen mit NumPy
- Optimierung mathematischer Berechnungen
- Sparse Matrix Operationen
- Signal Processing und Fourier Transforms
- Monte Carlo Methoden
- Gradient-basierte Optimierung
- Custom Algorithmen für Produktionsdaten

Schwierigkeitsgrad: ★★★★☆ (Advanced)
Geschätzte Bearbeitungszeit: 90-120 Minuten
"""

import time
import warnings
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from typing import Any

import numpy as np
import numpy.fft as fft
import numpy.linalg as linalg
import scipy.sparse as sparse

# Unterdrücke Warnungen für bessere Lesbarkeit
warnings.filterwarnings("ignore")


@dataclass
class OptimizationResult:
    """Datenklasse für Optimierungsergebnisse"""

    solution: np.ndarray
    cost: float
    iterations: int
    convergence_history: list[float]
    computation_time: float


class AdvancedNumericalSolver:
    """
    Erweiterte numerische Löser für industrielle Anwendungen
    """

    def __init__(self, tolerance: float = 1e-8, max_iterations: int = 1000):
        self.tolerance = tolerance
        self.max_iterations = max_iterations
        self.convergence_history = []

    def conjugate_gradient(
        self, A: np.ndarray, b: np.ndarray, x0: np.ndarray | None = None
    ) -> tuple[np.ndarray, int]:
        """
        Conjugate Gradient Verfahren für große lineare Gleichungssysteme
        Ideal für FEM-Berechnungen in der Fertigung
        """
        n = len(b)
        x = x0 if x0 is not None else np.zeros(n)

        r = b - A @ x
        p = r.copy()
        rsold = r @ r

        for iteration in range(self.max_iterations):
            Ap = A @ p
            alpha = rsold / (p @ Ap)
            x = x + alpha * p
            r = r - alpha * Ap
            rsnew = r @ r

            if np.sqrt(rsnew) < self.tolerance:
                return x, iteration + 1

            beta = rsnew / rsold
            p = r + beta * p
            rsold = rsnew

        return x, self.max_iterations

    def gauss_seidel_parallel(
        self,
        A: np.ndarray,
        b: np.ndarray,
        x0: np.ndarray | None = None,
        num_threads: int = 4,
    ) -> tuple[np.ndarray, int]:
        """
        Parallelisiertes Gauss-Seidel Verfahren
        Nutzt Red-Black Ordering für Parallelisierung
        """
        n = len(b)
        x = x0 if x0 is not None else np.zeros(n)

        # Red-Black Indexierung für Parallelisierung
        red_indices = np.arange(0, n, 2)
        black_indices = np.arange(1, n, 2)

        def update_subset(indices, x_current):
            x_new = x_current.copy()
            for i in indices:
                if A[i, i] != 0:
                    x_new[i] = (
                        b[i] - A[i, :i] @ x_new[:i] - A[i, i + 1 :] @ x_current[i + 1 :]
                    ) / A[i, i]
            return x_new

        for iteration in range(self.max_iterations):
            x_old = x.copy()

            # Parallel update red and black points
            with ThreadPoolExecutor(max_workers=num_threads) as executor:
                # Update red points
                x = update_subset(red_indices, x)
                # Update black points
                x = update_subset(black_indices, x)

            # Konvergenzcheck
            if np.linalg.norm(x - x_old) < self.tolerance:
                return x, iteration + 1

        return x, self.max_iterations


class SparseMatrixProcessor:
    """
    Hochperformante Verarbeitung von Sparse Matrizen
    Für FEM-Modelle und große Netzwerke
    """

    @staticmethod
    def create_fem_stiffness_matrix(
        n_nodes: int, connectivity: np.ndarray
    ) -> sparse.csr_matrix:
        """
        Erstellt Steifigkeitsmatrix für FEM-Berechnungen
        """
        n_elements = len(connectivity)
        row_ind = []
        col_ind = []
        data = []

        # Lokale Steifigkeitsmatrix (vereinfacht für 1D Elemente)
        k_local = np.array([[1, -1], [-1, 1]])

        for elem_idx, nodes in enumerate(connectivity):
            for i in range(2):
                for j in range(2):
                    row_ind.append(nodes[i])
                    col_ind.append(nodes[j])
                    data.append(k_local[i, j])

        K = sparse.coo_matrix((data, (row_ind, col_ind)), shape=(n_nodes, n_nodes))
        return K.tocsr()

    @staticmethod
    def analyze_matrix_properties(matrix: sparse.spmatrix) -> dict[str, Any]:
        """
        Analysiert Eigenschaften von Sparse Matrizen
        """
        density = matrix.nnz / (matrix.shape[0] * matrix.shape[1])

        # Konditionszahl schätzen (nur für kleinere Matrizen)
        if matrix.shape[0] < 1000:
            eigenvals = sparse.linalg.eigsh(
                matrix, k=min(6, matrix.shape[0] - 2), return_eigenvectors=False
            )
            condition_number = np.max(eigenvals) / np.max([np.min(eigenvals), 1e-12])
        else:
            condition_number = "N/A (Matrix zu groß)"

        return {
            "shape": matrix.shape,
            "nnz": matrix.nnz,
            "density": density,
            "format": matrix.format,
            "condition_number": condition_number,
            "memory_usage_mb": matrix.data.nbytes / 1024**2,
        }


class SignalProcessor:
    """
    Erweiterte Signalverarbeitung für Sensordaten
    """

    @staticmethod
    def advanced_fft_analysis(
        signal: np.ndarray, sampling_rate: float
    ) -> dict[str, np.ndarray]:
        """
        Erweiterte FFT-Analyse mit Spektrogramm und Phasenanalyse
        """
        # Standard FFT
        fft_result = fft.fft(signal)
        frequencies = fft.fftfreq(len(signal), 1 / sampling_rate)

        # Power Spectral Density
        psd = np.abs(fft_result) ** 2 / len(signal)

        # Phase spectrum
        phase = np.angle(fft_result)

        # Spektrogramm mit überlappenden Fenstern
        window_size = min(256, len(signal) // 4)
        overlap = window_size // 2

        spectrograms = []
        time_segments = []

        for start in range(0, len(signal) - window_size, overlap):
            segment = signal[start : start + window_size]
            windowed = segment * np.hanning(window_size)
            segment_fft = fft.fft(windowed)
            spectrograms.append(np.abs(segment_fft) ** 2)
            time_segments.append(start / sampling_rate)

        spectrogram = np.array(spectrograms).T

        return {
            "frequencies": frequencies[: len(frequencies) // 2],
            "magnitude": np.abs(fft_result)[: len(fft_result) // 2],
            "phase": phase[: len(phase) // 2],
            "psd": psd[: len(psd) // 2],
            "spectrogram": spectrogram[: window_size // 2, :],
            "time_segments": np.array(time_segments),
        }

    @staticmethod
    def detect_anomalies_in_signal(
        signal: np.ndarray, method: str = "statistical"
    ) -> dict[str, np.ndarray]:
        """
        Erweiterte Anomalieerkennung in Signalen
        """
        if method == "statistical":
            # Z-Score basierte Erkennung
            z_scores = np.abs((signal - np.mean(signal)) / np.std(signal))
            anomalies = z_scores > 3

        elif method == "spectral":
            # Spektrale Residuen Methode
            fft_signal = fft.fft(signal)
            # Entferne Hauptfrequenzen
            threshold = np.percentile(np.abs(fft_signal), 95)
            fft_filtered = fft_signal.copy()
            fft_filtered[np.abs(fft_signal) > threshold] = 0

            reconstructed = np.real(fft.ifft(fft_filtered))
            residuals = signal - reconstructed
            anomalies = np.abs(residuals) > 2 * np.std(residuals)

        elif method == "morphological":
            # Morphologische Filterung
            from scipy import ndimage

            # Strukturelement für Erosion/Dilatation
            struct_elem = np.ones(5)
            eroded = ndimage.grey_erosion(signal, structure=struct_elem)
            dilated = ndimage.grey_dilation(signal, structure=struct_elem)

            # Anomalien als Abweichungen vom morphologischen Profil
            morphological_gradient = dilated - eroded
            anomalies = morphological_gradient > np.percentile(
                morphological_gradient, 95
            )

        else:
            raise ValueError(f"Unbekannte Methode: {method}")

        return {
            "anomalies": anomalies,
            "anomaly_indices": np.where(anomalies)[0],
            "anomaly_scores": (
                z_scores
                if method == "statistical"
                else residuals if method == "spectral" else morphological_gradient
            ),
        }


class MonteCarloSimulator:
    """
    Monte Carlo Simulationen für Risiko- und Toleranzanalysen
    """

    @staticmethod
    def simulate_tolerance_analysis(
        nominal_values: np.ndarray,
        tolerances: np.ndarray,
        n_simulations: int = 10000,
        correlation_matrix: np.ndarray | None = None,
    ) -> dict[str, Any]:
        """
        Monte Carlo Toleranzanalyse für Fertigungsprozesse
        """
        n_variables = len(nominal_values)

        # Generiere korrelierte Zufallsvariablen
        if correlation_matrix is not None:
            # Cholesky Dekomposition für korrelierte Samples
            L = linalg.cholesky(correlation_matrix)
            samples = np.random.normal(0, 1, (n_simulations, n_variables))
            corr_samples = samples @ L.T
        else:
            corr_samples = np.random.normal(0, 1, (n_simulations, n_variables))

        # Skaliere mit Toleranzen und addiere Nominalwerte
        simulated_values = nominal_values + corr_samples * tolerances

        # Berechne statistische Kennwerte
        result_mean = np.mean(simulated_values, axis=0)
        result_std = np.std(simulated_values, axis=0)
        result_range = np.ptp(simulated_values, axis=0)

        # Prozessfähigkeitsindizes (vereinfacht)
        cp_indices = tolerances / (3 * result_std)

        return {
            "simulated_values": simulated_values,
            "mean": result_mean,
            "std": result_std,
            "range": result_range,
            "cp_indices": cp_indices,
            "confidence_intervals": {
                "95%": np.percentile(simulated_values, [2.5, 97.5], axis=0),
                "99%": np.percentile(simulated_values, [0.5, 99.5], axis=0),
            },
        }

    @staticmethod
    def estimate_pi_advanced(n_samples: int = 1000000) -> dict[str, float]:
        """
        Erweiterte Pi-Schätzung mit Varianzreduktion
        """
        # Standard Monte Carlo
        start_time = time.time()
        points = np.random.uniform(-1, 1, (n_samples, 2))
        distances = np.sum(points**2, axis=1)
        pi_estimate_standard = 4 * np.mean(distances <= 1)
        standard_time = time.time() - start_time

        # Antithetic Variates (Varianzreduktion)
        start_time = time.time()
        n_half = n_samples // 2
        points1 = np.random.uniform(-1, 1, (n_half, 2))
        points2 = -points1  # Antithetic pairs

        distances1 = np.sum(points1**2, axis=1)
        distances2 = np.sum(points2**2, axis=1)

        pi_estimate_antithetic = 4 * np.mean((distances1 <= 1) + (distances2 <= 1)) / 2
        antithetic_time = time.time() - start_time

        # Stratified Sampling
        start_time = time.time()
        strata_per_dim = int(np.sqrt(n_samples / 4))
        stratum_size = 2 / strata_per_dim

        pi_estimates = []
        for i in range(strata_per_dim):
            for j in range(strata_per_dim):
                # Stratifizierte Samples in jedem Quadrat
                samples_per_stratum = n_samples // (strata_per_dim**2)
                x_base = -1 + i * stratum_size
                y_base = -1 + j * stratum_size

                x_samples = x_base + np.random.uniform(
                    0, stratum_size, samples_per_stratum
                )
                y_samples = y_base + np.random.uniform(
                    0, stratum_size, samples_per_stratum
                )

                distances = x_samples**2 + y_samples**2
                pi_estimates.append(4 * np.mean(distances <= 1))

        pi_estimate_stratified = np.mean(pi_estimates)
        stratified_time = time.time() - start_time

        return {
            "standard": {
                "estimate": pi_estimate_standard,
                "error": abs(pi_estimate_standard - np.pi),
                "time": standard_time,
            },
            "antithetic": {
                "estimate": pi_estimate_antithetic,
                "error": abs(pi_estimate_antithetic - np.pi),
                "time": antithetic_time,
            },
            "stratified": {
                "estimate": pi_estimate_stratified,
                "error": abs(pi_estimate_stratified - np.pi),
                "time": stratified_time,
            },
        }


class GradientOptimizer:
    """
    Gradient-basierte Optimierungsverfahren für industrielle Anwendungen
    """

    def __init__(self, learning_rate: float = 0.01, momentum: float = 0.9):
        self.learning_rate = learning_rate
        self.momentum = momentum
        self.velocity = None

    def adam_optimizer(
        self,
        objective_func: Callable,
        gradient_func: Callable,
        x0: np.ndarray,
        max_iterations: int = 1000,
        beta1: float = 0.9,
        beta2: float = 0.999,
        epsilon: float = 1e-8,
    ) -> OptimizationResult:
        """
        Adam Optimizer Implementation für Produktionsoptimierung
        """
        x = x0.copy()
        m = np.zeros_like(x)  # First moment estimate
        v = np.zeros_like(x)  # Second moment estimate

        convergence_history = []
        start_time = time.time()

        for t in range(1, max_iterations + 1):
            # Berechne Gradient
            grad = gradient_func(x)

            # Update biased first moment estimate
            m = beta1 * m + (1 - beta1) * grad

            # Update biased second raw moment estimate
            v = beta2 * v + (1 - beta2) * grad**2

            # Compute bias-corrected first moment estimate
            m_hat = m / (1 - beta1**t)

            # Compute bias-corrected second raw moment estimate
            v_hat = v / (1 - beta2**t)

            # Update parameters
            x = x - self.learning_rate * m_hat / (np.sqrt(v_hat) + epsilon)

            # Speichere Konvergenzhistorie
            cost = objective_func(x)
            convergence_history.append(cost)

            # Konvergenzcheck
            if len(convergence_history) > 1:
                if abs(convergence_history[-1] - convergence_history[-2]) < 1e-8:
                    break

        computation_time = time.time() - start_time

        return OptimizationResult(
            solution=x,
            cost=objective_func(x),
            iterations=t,
            convergence_history=convergence_history,
            computation_time=computation_time,
        )

    def optimize_production_schedule(
        self,
        processing_times: np.ndarray,
        setup_times: np.ndarray,
        due_dates: np.ndarray,
    ) -> dict[str, Any]:
        """
        Optimiere Produktionsreihenfolge mit Genetischem Algorithmus
        """
        n_jobs = len(processing_times)
        population_size = 50
        generations = 100
        mutation_rate = 0.1

        def fitness(schedule):
            """Bewertungsfunktion: Minimiere Verspätung und Setup-Zeit"""
            total_time = 0
            total_tardiness = 0
            total_setup = 0

            for i, job in enumerate(schedule):
                if i > 0:
                    total_setup += setup_times[int(schedule[i - 1]), int(job)]
                total_time += processing_times[int(job)]
                tardiness = max(0, total_time - due_dates[int(job)])
                total_tardiness += tardiness

            return -(total_tardiness + 0.1 * total_setup)  # Negativ für Maximierung

        # Initialisiere Population
        population = [np.random.permutation(n_jobs) for _ in range(population_size)]

        best_fitness_history = []

        for generation in range(generations):
            # Bewerte Population
            fitness_scores = [fitness(schedule) for schedule in population]

            # Speichere beste Lösung
            best_idx = np.argmax(fitness_scores)
            best_fitness_history.append(fitness_scores[best_idx])

            # Selektion (Tournament Selection)
            new_population = []
            for _ in range(population_size):
                tournament_size = 3
                tournament_indices = np.random.choice(population_size, tournament_size)
                tournament_fitness = [fitness_scores[i] for i in tournament_indices]
                winner_idx = tournament_indices[np.argmax(tournament_fitness)]
                new_population.append(population[winner_idx].copy())

            # Crossover (Order Crossover)
            for i in range(0, population_size - 1, 2):
                if np.random.random() < 0.8:  # Crossover probability
                    parent1, parent2 = new_population[i], new_population[i + 1]

                    # Order Crossover
                    start, end = sorted(np.random.choice(n_jobs, 2, replace=False))
                    child1 = np.full(n_jobs, -1)
                    child2 = np.full(n_jobs, -1)

                    child1[start:end] = parent1[start:end]
                    child2[start:end] = parent2[start:end]

                    # Fülle restliche Positionen
                    remaining1 = [x for x in parent2 if x not in child1]
                    remaining2 = [x for x in parent1 if x not in child2]

                    fill_idx1 = [i for i, x in enumerate(child1) if x == -1]
                    fill_idx2 = [i for i, x in enumerate(child2) if x == -1]

                    for idx, pos in enumerate(fill_idx1):
                        child1[pos] = remaining1[idx]
                    for idx, pos in enumerate(fill_idx2):
                        child2[pos] = remaining2[idx]

                    new_population[i] = child1
                    new_population[i + 1] = child2

            # Mutation (Swap Mutation)
            for individual in new_population:
                if np.random.random() < mutation_rate:
                    idx1, idx2 = np.random.choice(n_jobs, 2, replace=False)
                    individual[idx1], individual[idx2] = (
                        individual[idx2],
                        individual[idx1],
                    )

            population = new_population

        # Finale Bewertung
        final_fitness = [fitness(schedule) for schedule in population]
        best_schedule = population[np.argmax(final_fitness)]

        return {
            "best_schedule": best_schedule,
            "best_fitness": max(final_fitness),
            "fitness_history": best_fitness_history,
            "final_population": population,
        }


# ================================
# AUFGABEN UND ÜBUNGEN
# ================================


def aufgabe_1_numerische_solver():
    """
    Aufgabe 1: Implementierung und Vergleich numerischer Löser

    Implementiere verschiedene Verfahren zur Lösung linearer Gleichungssysteme
    und vergleiche deren Performance.
    """
    print("=== Aufgabe 1: Numerische Löser ===")

    # TODO: Erstelle eine große, sparse Koeffizientenmatrix (1000x1000)
    # Tipp: Verwende eine Tridiagonalmatrix oder FEM-ähnliche Struktur

    # TODO: Implementiere und vergleiche:
    # 1. Conjugate Gradient Verfahren
    # 2. Parallelisiertes Gauss-Seidel
    # 3. NumPy's direkter Löser (np.linalg.solve)
    # 4. Sparse Löser (scipy.sparse.linalg.spsolve)

    # TODO: Messe und vergleiche:
    # - Rechenzeit
    # - Speicherverbrauch
    # - Genauigkeit der Lösung
    # - Anzahl Iterationen bis Konvergenz

    # BONUS: Visualisiere die Konvergenzgeschwindigkeit

    pass


def aufgabe_2_sparse_matrix_operationen():
    """
    Aufgabe 2: Erweiterte Sparse Matrix Operationen

    Arbeite mit großen, sparse Matrizen wie sie in FEM-Simulationen auftreten.
    """
    print("=== Aufgabe 2: Sparse Matrix Operationen ===")

    # TODO: Erstelle eine FEM-Steifigkeitsmatrix für ein 2D-Gitter
    # Tipp: Verwende die create_fem_stiffness_matrix Funktion als Basis

    # TODO: Analysiere die Matrix-Eigenschaften:
    # - Sparsity pattern visualisieren
    # - Konditionszahl berechnen
    # - Eigenwerte analysieren

    # TODO: Implementiere Matrix-Operationen:
    # - Matrix-Vektor Multiplikation optimieren
    # - Block-Matrix Operationen
    # - Matrix Assembling simulieren

    # TODO: Performance-Vergleich verschiedener Sparse-Formate:
    # - CSR vs CSC vs COO
    # - Memory usage
    # - Operation speed

    # BONUS: Implementiere einen iterativen Matrix-Assembler

    pass


def aufgabe_3_signalverarbeitung():
    """
    Aufgabe 3: Erweiterte Signalverarbeitung

    Implementiere fortgeschrittene Techniken zur Analyse von Sensorsignalen.
    """
    print("=== Aufgabe 3: Erweiterte Signalverarbeitung ===")

    # TODO: Generiere ein komplexes Testsignal mit:
    # - Mehreren Frequenzkomponenten
    # - Rauschen
    # - Trends
    # - Ausreißern/Anomalien

    # TODO: Implementiere und vergleiche Anomalieerkennung:
    # - Statistische Methoden (Z-Score, IQR)
    # - Spektrale Methoden (FFT-basiert)
    # - Morphologische Filterung

    # TODO: Erweiterte FFT-Analyse:
    # - Short-Time Fourier Transform (STFT)
    # - Spektrogramm erstellen
    # - Phase-Amplitude Beziehungen

    # TODO: Filter-Design und -Anwendung:
    # - Butterworth Filter
    # - Kalman Filter (vereinfacht)
    # - Adaptive Filter

    # BONUS: Real-time Signal Processing Simulation

    pass


def aufgabe_4_monte_carlo_optimierung():
    """
    Aufgabe 4: Monte Carlo Methoden und Optimierung

    Nutze Monte Carlo Simulation für Toleranzanalyse und Optimierung.
    """
    print("=== Aufgabe 4: Monte Carlo und Optimierung ===")

    # TODO: Toleranzanalyse für Fertigungsprozess:
    # - Definiere ein Produktionsmodell mit mehreren Variablen
    # - Implementiere korrelierte Toleranzen
    # - Berechne Prozessfähigkeitsindizes

    # TODO: Verschiedene Sampling-Strategien vergleichen:
    # - Standard Random Sampling
    # - Latin Hypercube Sampling
    # - Stratified Sampling
    # - Importance Sampling

    # TODO: Produktionsoptimierung:
    # - Genetischer Algorithmus für Reihenfolgeplanung
    # - Adam Optimizer für kontinuierliche Parameter
    # - Multi-objective Optimization

    # TODO: Sensitivity Analysis:
    # - Sobol Indices berechnen
    # - Morris Method implementieren
    # - Tornado Plots erstellen

    # BONUS: Robust Design Optimization

    pass


def fortgeschrittene_demo():
    """
    Demonstration aller erweiterten Algorithmen
    """
    print("🔬 NumPy Advanced Algorithmic Techniques Demo")
    print("=" * 60)

    # 1. Numerische Löser Demo
    print("\n1. Numerische Löser Vergleich")
    solver = AdvancedNumericalSolver()

    # Erstelle Testsystem
    n = 500
    A = np.random.rand(n, n)
    A = A @ A.T + np.eye(n)  # Positive definit machen
    b = np.random.rand(n)

    # Conjugate Gradient
    start_time = time.time()
    x_cg, iter_cg = solver.conjugate_gradient(A, b)
    time_cg = time.time() - start_time

    # NumPy direkter Löser
    start_time = time.time()
    x_direct = np.linalg.solve(A, b)
    time_direct = time.time() - start_time

    print(f"Conjugate Gradient: {iter_cg} Iterationen, {time_cg:.4f}s")
    print(f"Direkter Löser: {time_direct:.4f}s")
    print(f"Fehler CG vs Direct: {np.linalg.norm(x_cg - x_direct):.2e}")

    # 2. Sparse Matrix Demo
    print("\n2. Sparse Matrix Analyse")
    processor = SparseMatrixProcessor()

    # FEM Matrix erstellen
    n_nodes = 100
    connectivity = np.array([[i, i + 1] for i in range(n_nodes - 1)])
    K = processor.create_fem_stiffness_matrix(n_nodes, connectivity)

    props = processor.analyze_matrix_properties(K)
    print(f"Matrix Shape: {props['shape']}")
    print(f"Sparsity: {props['density']:.4f}")
    print(f"Memory Usage: {props['memory_usage_mb']:.2f} MB")

    # 3. Signalverarbeitung Demo
    print("\n3. Erweiterte Signalanalyse")

    # Komplexes Testsignal
    t = np.linspace(0, 1, 1000)
    signal = (
        np.sin(2 * np.pi * 10 * t)
        + 0.5 * np.sin(2 * np.pi * 25 * t)
        + 0.2 * np.random.randn(len(t))
        + 0.1 * t
    )  # Trend

    # Anomalien hinzufügen
    anomaly_indices = np.random.choice(len(signal), 20, replace=False)
    signal[anomaly_indices] += np.random.randn(20) * 2

    # FFT Analyse
    fft_results = SignalProcessor.advanced_fft_analysis(signal, 1000)
    print(
        f"Dominante Frequenz: {fft_results['frequencies'][np.argmax(fft_results['magnitude'])]:.1f} Hz"
    )

    # Anomalieerkennung
    anomalies = SignalProcessor.detect_anomalies_in_signal(signal, "statistical")
    print(f"Erkannte Anomalien: {len(anomalies['anomaly_indices'])}")

    # 4. Monte Carlo Demo
    print("\n4. Monte Carlo Simulation")

    # Pi Schätzung mit verschiedenen Methoden
    pi_results = MonteCarloSimulator.estimate_pi_advanced(100000)

    for method, result in pi_results.items():
        print(
            f"{method.capitalize()}: π ≈ {result['estimate']:.6f}, "
            f"Fehler: {result['error']:.6f}, Zeit: {result['time']:.4f}s"
        )

    # 5. Optimierung Demo
    print("\n5. Optimierungsverfahren")

    # Quadratische Testfunktion
    def objective(x):
        return np.sum((x - np.array([1, 2])) ** 2)

    def gradient(x):
        return 2 * (x - np.array([1, 2]))

    optimizer = GradientOptimizer()
    result = optimizer.adam_optimizer(
        objective, gradient, np.array([10, 10]), max_iterations=100
    )

    print(f"Optimum gefunden: {result.solution}")
    print(f"Finale Kosten: {result.cost:.6f}")
    print(f"Iterationen: {result.iterations}")
    print(f"Zeit: {result.computation_time:.4f}s")


def performance_benchmark():
    """
    Performance Benchmark verschiedener algorithmischer Ansätze
    """
    print("\n🚀 Performance Benchmark")
    print("=" * 40)

    sizes = [100, 500, 1000, 2000]
    methods = ["NumPy Direct", "Conjugate Gradient", "Sparse Solver"]

    results = {method: [] for method in methods}

    for n in sizes:
        print(f"\nTeste Systemgröße: {n}x{n}")

        # Erstelle Testsystem
        A_dense = np.random.rand(n, n)
        A_dense = A_dense @ A_dense.T + np.eye(n)
        b = np.random.rand(n)

        # Sparse Version
        A_sparse = sparse.csr_matrix(A_dense)

        # NumPy Direct
        start = time.time()
        x1 = np.linalg.solve(A_dense, b)
        time_direct = time.time() - start
        results["NumPy Direct"].append(time_direct)

        # Conjugate Gradient
        solver = AdvancedNumericalSolver()
        start = time.time()
        x2, _ = solver.conjugate_gradient(A_dense, b)
        time_cg = time.time() - start
        results["Conjugate Gradient"].append(time_cg)

        # Sparse Solver
        start = time.time()
        x3 = sparse.linalg.spsolve(A_sparse, b)
        time_sparse = time.time() - start
        results["Sparse Solver"].append(time_sparse)

        print(f"  Direct: {time_direct:.4f}s")
        print(f"  CG: {time_cg:.4f}s")
        print(f"  Sparse: {time_sparse:.4f}s")

    # Performance Summary
    print("\n📊 Performance Summary:")
    for method in methods:
        avg_time = np.mean(results[method])
        print(f"{method}: {avg_time:.4f}s durchschnittlich")


if __name__ == "__main__":
    print("🧮 NumPy Advanced: Algorithmische Optimierung")
    print("=" * 60)
    print("Dieses Modul demonstriert erweiterte algorithmische Techniken:")
    print("• Numerische Löser und Optimierung")
    print("• Sparse Matrix Operationen")
    print("• Erweiterte Signalverarbeitung")
    print("• Monte Carlo Methoden")
    print("• Performance-optimierte Algorithmen")
    print("\n" + "=" * 60)

    # Hauptdemo ausführen
    fortgeschrittene_demo()

    # Performance Benchmark
    performance_benchmark()

    print("\n✅ Advanced Algorithmic Demo abgeschlossen!")
    print("Bearbeite nun die Aufgaben 1-4 für vertieftes Verständnis.")
