#!/usr/bin/env python3
"""
🟢 BEGINNER - NumPy Array-Manipulation - HINT 3 (Code-Snippets)
Übung 3: Array-Manipulation für SmartFactory Produktionsdaten

🎯 DETAILLIERTE CODE-BEISPIELE:
"""

import numpy as np


def beispiel_reshape_und_transpose():
    """📋 Beispiel für Aufgabe 1: Reshape und Transpose"""
    print("=" * 60)
    print("🟢 HINT 3: Code-Beispiele für Reshape")
    print("=" * 60)

    # Beispiel-Daten
    daten = np.arange(1, 25)  # 24 Elemente
    print(f"Original: {daten}")
    print(f"Shape: {daten.shape}")
    print()

    # Reshape Beispiele
    print("🔄 RESHAPE-BEISPIELE:")

    # Zu 4×6 Matrix
    matrix_4x6 = daten.reshape(4, 6)
    print(f"4×6 Matrix:\n{matrix_4x6}")
    print(f"Shape: {matrix_4x6.shape}")
    print()

    # Zu 6×4 Matrix
    matrix_6x4 = daten.reshape(6, 4)
    print(f"6×4 Matrix:\n{matrix_6x4}")
    print()

    # Transpose
    print("🔄 TRANSPOSE-BEISPIELE:")
    transposed = matrix_4x6.T
    print(f"Transponiert (6×4):\n{transposed}")
    print(f"Shape nach Transpose: {transposed.shape}")
    print()

    # Alternative Transpose-Syntax
    transposed_alt = matrix_4x6.transpose()
    print("Alternative: .transpose() statt .T")


def beispiel_concatenate():
    """📋 Beispiel für Aufgabe 2: Arrays kombinieren"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Code-Beispiele für Concatenate")
    print("=" * 60)

    # Beispiel-Arrays
    tag1 = np.array([[10, 15, 20], [25, 30, 35]])  # 2×3
    tag2 = np.array([[40, 45, 50], [55, 60, 65]])  # 2×3

    print("Tag 1 Daten:")
    print(tag1)
    print("Tag 2 Daten:")
    print(tag2)
    print()

    # Horizontal kombinieren (axis=1)
    print("🔗 HORIZONTAL KOMBINIEREN (axis=1):")
    horizontal = np.concatenate([tag1, tag2], axis=1)
    print(f"Horizontal:\n{horizontal}")
    print(f"Shape: {horizontal.shape}")
    print()

    # Vertikal kombinieren (axis=0)
    print("🔗 VERTIKAL KOMBINIEREN (axis=0):")
    vertikal = np.concatenate([tag1, tag2], axis=0)
    print(f"Vertikal:\n{vertikal}")
    print(f"Shape: {vertikal.shape}")
    print()

    # Alternative Methoden
    print("🔗 ALTERNATIVE METHODEN:")
    h_alt = np.hstack([tag1, tag2])  # Horizontal stack
    v_alt = np.vstack([tag1, tag2])  # Vertical stack
    print(f"hstack: {h_alt.shape}, vstack: {v_alt.shape}")


def beispiel_boolean_indexing():
    """📋 Beispiel für Aufgabe 3: Boolean Indexing"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Code-Beispiele für Boolean Indexing")
    print("=" * 60)

    # Beispiel-Produktionsdaten
    produktion = np.array([45, 52, 38, 65, 71, 29, 58, 63, 41, 67])
    print(f"Produktionsdaten: {produktion}")
    print()

    # Einfache Bedingung
    print("🎯 EINFACHE BEDINGUNGEN:")
    schwellwert = 50
    hohe_produktion = produktion > schwellwert
    print(f"Produktion > {schwellwert}: {hohe_produktion}")
    print(f"Gefilterte Werte: {produktion[hohe_produktion]}")
    print()

    # Mehrere Bedingungen
    print("🎯 MEHRERE BEDINGUNGEN:")
    min_wert, max_wert = 40, 60
    mittlere_produktion = (produktion >= min_wert) & (produktion <= max_wert)
    print(f"Produktion zwischen {min_wert} und {max_wert}:")
    print(f"Boolean Mask: {mittlere_produktion}")
    print(f"Gefilterte Werte: {produktion[mittlere_produktion]}")
    print()

    # Indices finden
    print("🎯 INDICES FINDEN:")
    indices_hoch = np.where(produktion > schwellwert)[0]
    print(f"Indices mit hoher Produktion: {indices_hoch}")

    # Kombinierte Operationen
    print("🎯 KOMBINIERTE OPERATIONEN:")
    print(f"Anzahl hohe Produktion: {np.sum(hohe_produktion)}")
    print(f"Anteil hohe Produktion: {np.mean(hohe_produktion):.2%}")


def beispiel_erweiterte_manipulation():
    """📋 Beispiel für Aufgabe 4: Erweiterte Manipulation"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Code-Beispiele für erweiterte Manipulation")
    print("=" * 60)

    # Beispiel-Daten
    daten = np.array([23, 45, 12, 67, 34, 89, 56, 78, 23, 45])
    print(f"Original-Daten: {daten}")
    print()

    # Aufteilen
    print("✂️ ARRAYS AUFTEILEN:")
    try:
        teile = np.split(daten, 5)  # In 5 Teile
        print(f"Aufgeteilt in {len(teile)} Teile:")
        for i, teil in enumerate(teile):
            print(f"  Teil {i + 1}: {teil}")
    except ValueError as e:
        print(f"Fehler beim Aufteilen: {e}")
        # Alternative: array_split für ungleiche Teile
        teile = np.array_split(daten, 3)
        print("Mit array_split in 3 Teile:")
        for i, teil in enumerate(teile):
            print(f"  Teil {i + 1}: {teil}")
    print()

    # Sortieren
    print("📈 SORTIEREN:")
    sortiert = np.sort(daten)
    print(f"Sortiert: {sortiert}")

    # Sortier-Indices
    sort_indices = np.argsort(daten)
    print(f"Sortier-Indices: {sort_indices}")
    print()

    # Eindeutige Werte
    print("🔍 EINDEUTIGE WERTE:")
    eindeutig, counts = np.unique(daten, return_counts=True)
    print(f"Eindeutige Werte: {eindeutig}")
    print(f"Häufigkeiten: {counts}")
    print()

    # Statistiken
    print("📊 STATISTIKEN:")
    print(f"Mittelwert: {np.mean(daten):.2f}")
    print(f"Median: {np.median(daten):.2f}")
    print(f"Standardabweichung: {np.std(daten):.2f}")
    print(f"Min/Max: {np.min(daten)} / {np.max(daten)}")


def hilfreiche_funktionen():
    """Zusätzliche hilfreiche Funktionen"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Hilfreiche Zusatzfunktionen")
    print("=" * 60)

    print("🛠️ NÜTZLICHE FUNKTIONEN:")
    print("• np.reshape(array, new_shape) - Array umformen")
    print("• array.T oder array.transpose() - Transponieren")
    print("• np.concatenate([a1, a2], axis=0/1) - Arrays verbinden")
    print("• np.hstack(), np.vstack() - Horizontal/Vertikal stapeln")
    print("• np.split(), np.array_split() - Arrays aufteilen")
    print("• np.where(condition) - Indices finden")
    print("• np.unique() - Eindeutige Werte")
    print("• np.sort(), np.argsort() - Sortieren")
    print()

    print("🔍 DEBUG-TIPPS:")
    print("• Verwende .shape um Dimensionen zu prüfen")
    print("• Teste mit kleinen Arrays zuerst")
    print("• print() zwischen Operationen für Zwischenergebnisse")
    print("• Verwende aussagekräftige Variablennamen")


if __name__ == "__main__":
    beispiel_reshape_und_transpose()
    beispiel_concatenate()
    beispiel_boolean_indexing()
    beispiel_erweiterte_manipulation()
    hilfreiche_funktionen()
