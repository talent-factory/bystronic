#!/usr/bin/env python3
"""
Hilfe Stufe 3: Code-Snippets für NumPy Grundlagen
================================================

💡 HINT 3 - Konkrete Code-Beispiele

Hier sind die wichtigsten Code-Bausteine für die Aufgaben:
"""

import numpy as np


def aufgabe_1_array_erstellung_hilfe():
    """Code-Snippet für Aufgabe 1"""
    print("=== Aufgabe 1: Array-Erstellung ===")

    # TODO: Vervollständige diese Beispiele

    # 1D Array aus Liste
    liste = [10, 20, 30, 40, 50]
    arr_1d = np.array(liste)
    print(f"1D Array: {arr_1d}")

    # 2D Array (Matrix)
    matrix_liste = [[1, 2, 3], [4, 5, 6]]
    arr_2d = np.array(matrix_liste)
    print(f"2D Array:\n{arr_2d}")

    # Spezielle Arrays
    nullen = np.zeros(5)  # [0. 0. 0. 0. 0.]
    einsen = np.ones((2, 3))  # 2x3 Matrix mit Einsen
    sequenz = np.arange(1, 11)  # [1 2 3 4 5 6 7 8 9 10]

    print(f"Nullen: {nullen}")
    print(f"Einsen:\n{einsen}")
    print(f"Sequenz: {sequenz}")


def aufgabe_2_eigenschaften_hilfe():
    """Code-Snippet für Aufgabe 2"""
    print("\n=== Aufgabe 2: Array-Eigenschaften ===")

    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    # TODO: Analysiere diese Eigenschaften
    print(f"Array:\n{arr}")
    print(f"Shape (Dimensionen): {arr.shape}")  # (2, 4)
    print(f"Ndim (Anzahl Dimensionen): {arr.ndim}")  # 2
    print(f"Size (Gesamtzahl Elemente): {arr.size}")  # 8
    print(f"Dtype (Datentyp): {arr.dtype}")  # int64

    # Memory-Info
    print(f"Itemsize (Bytes pro Element): {arr.itemsize}")
    print(f"Nbytes (Gesamter Speicher): {arr.nbytes}")


def aufgabe_3_operationen_hilfe():
    """Code-Snippet für Aufgabe 3"""
    print("\n=== Aufgabe 3: Grundoperationen ===")

    a = np.array([1, 2, 3, 4])
    b = np.array([10, 20, 30, 40])

    # TODO: Führe diese Operationen aus
    print(f"Array a: {a}")
    print(f"Array b: {b}")

    # Elementweise Operationen
    print(f"a + b = {a + b}")  # [11 22 33 44]
    print(f"a * b = {a * b}")  # [10 40 90 160]
    print(f"b / a = {b / a}")  # [10. 10. 10. 10.]
    print(f"a ** 2 = {a**2}")  # [1 4 9 16]

    # Broadcasting-Beispiel
    print(f"a + 10 = {a + 10}")  # [11 12 13 14]
    print(f"a * 3 = {a * 3}")  # [3 6 9 12]


def aufgabe_4_aggregationen_hilfe():
    """Code-Snippet für Aufgabe 4"""
    print("\n=== Aufgabe 4: Aggregationsfunktionen ===")

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    # TODO: Berechne verschiedene Statistiken
    print(f"Matrix:\n{matrix}")

    # Gesamt-Statistiken
    print(f"Summe: {np.sum(matrix)}")
    print(f"Mittelwert: {np.mean(matrix)}")
    print(f"Minimum: {np.min(matrix)}")
    print(f"Maximum: {np.max(matrix)}")
    print(f"Standardabweichung: {np.std(matrix)}")

    # Achsen-spezifische Operationen
    print(f"Summe pro Spalte (axis=0): {np.sum(matrix, axis=0)}")
    print(f"Summe pro Zeile (axis=1): {np.sum(matrix, axis=1)}")
    print(f"Mittelwert pro Spalte: {np.mean(matrix, axis=0)}")


if __name__ == "__main__":
    # Führe alle Hilfe-Beispiele aus
    aufgabe_1_array_erstellung_hilfe()
    aufgabe_2_eigenschaften_hilfe()
    aufgabe_3_operationen_hilfe()
    aufgabe_4_aggregationen_hilfe()

    print("\n💡 Nutze diese Code-Snippets als Vorlage für deine Lösung!")
    print("   Erweitere sie um die spezifischen Anforderungen der Aufgaben.")
