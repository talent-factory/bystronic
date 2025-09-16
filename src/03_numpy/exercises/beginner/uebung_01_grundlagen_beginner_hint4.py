#!/usr/bin/env python3
"""
Hilfe Stufe 4: Fast vollständige Lösung für NumPy Grundlagen
===========================================================

💡 HINT 4 - Nahezu vollständige Implementierung

Dies ist eine fast vollständige Lösung. Du musst nur noch die TODO-Bereiche
vervollständigen und eventuell Anpassungen vornehmen.
"""

import numpy as np


def aufgabe_1_array_erstellung():
    """
    Fast vollständige Lösung für Aufgabe 1: Array-Erstellung
    """
    print("=== Aufgabe 1: Array-Erstellung ===")

    # 1. Erstelle 1D Array aus Liste
    temperaturen = [20.5, 21.2, 19.8, 22.1, 20.9]
    temp_array = np.array(temperaturen)
    print(f"Temperaturen: {temp_array}")

    # 2. Erstelle 2D Array (Matrix) für Sensordaten
    sensordaten = [[1.2, 1.5, 1.8], [2.1, 2.3, 2.0], [1.9, 1.7, 2.2]]
    sensor_matrix = np.array(sensordaten)
    print(f"Sensordaten:\n{sensor_matrix}")

    # 3. Spezielle Arrays erstellen
    nullvektor = np.zeros(10)
    einheitsmatrix = np.ones((3, 3))
    zeitreihe = np.arange(0, 100, 5)  # 0, 5, 10, ..., 95

    print(f"Nullvektor: {nullvektor}")
    print(f"Einheitsmatrix:\n{einheitsmatrix}")
    print(f"Zeitreihe: {zeitreihe}")

    # TODO: Erstelle zusätzlich:
    # - Ein Array mit Zufallszahlen (np.random.random)
    # - Ein lineares Array mit np.linspace
    # - Ein Array mit wiederholenden Werten (np.repeat)

    return temp_array, sensor_matrix


def aufgabe_2_array_eigenschaften():
    """
    Fast vollständige Lösung für Aufgabe 2: Array-Eigenschaften
    """
    print("\n=== Aufgabe 2: Array-Eigenschaften ===")

    # Beispiel-Array erstellen
    produktionsdaten = np.array(
        [[100, 105, 98, 103], [95, 102, 99, 104], [101, 97, 106, 100]]
    )

    print(f"Produktionsdaten:\n{produktionsdaten}")

    # Eigenschaften analysieren
    print(f"Shape: {produktionsdaten.shape}")  # (3, 4)
    print(f"Dimensionen: {produktionsdaten.ndim}")  # 2
    print(f"Gesamtelemente: {produktionsdaten.size}")  # 12
    print(f"Datentyp: {produktionsdaten.dtype}")
    print(f"Speicherverbrauch: {produktionsdaten.nbytes} Bytes")

    # TODO: Ergänze:
    # - Prüfung auf verschiedene Datentypen (int32, float64, etc.)
    # - Memory Layout Information
    # - Stride Information

    return produktionsdaten


def aufgabe_3_grundoperationen():
    """
    Fast vollständige Lösung für Aufgabe 3: Grundoperationen
    """
    print("\n=== Aufgabe 3: Grundoperationen ===")

    # Maschinendaten simulieren
    maschine_a = np.array([80, 85, 90, 88, 92])
    maschine_b = np.array([75, 88, 85, 90, 87])

    print(f"Maschine A Leistung: {maschine_a}")
    print(f"Maschine B Leistung: {maschine_b}")

    # Elementweise Operationen
    gesamtleistung = maschine_a + maschine_b
    leistungsdifferenz = maschine_a - maschine_b
    effizienz_ratio = maschine_a / maschine_b

    print(f"Gesamtleistung: {gesamtleistung}")
    print(f"Leistungsdifferenz: {leistungsdifferenz}")
    print(f"Effizienz-Ratio: {effizienz_ratio}")

    # Broadcasting-Operationen
    toleranz = 5  # ±5% Toleranz
    obergrenze = maschine_a + toleranz
    untergrenze = maschine_a - toleranz

    print(f"Obergrenze (+{toleranz}): {obergrenze}")
    print(f"Untergrenze (-{toleranz}): {untergrenze}")

    # TODO: Ergänze:
    # - Mathematische Funktionen (np.sqrt, np.sin, np.exp)
    # - Vergleichsoperationen (>, <, ==)
    # - Logische Operationen (np.logical_and, np.logical_or)

    return gesamtleistung, leistungsdifferenz


def aufgabe_4_aggregationen():
    """
    Fast vollständige Lösung für Aufgabe 4: Aggregationsfunktionen
    """
    print("\n=== Aufgabe 4: Aggregationsfunktionen ===")

    # Qualitätsdaten über mehrere Tage
    qualitaetsdaten = np.array(
        [
            [98.5, 99.1, 97.8, 98.9],  # Tag 1
            [99.2, 98.7, 99.5, 98.3],  # Tag 2
            [97.9, 98.8, 99.3, 99.0],  # Tag 3
            [98.6, 99.4, 98.1, 99.2],  # Tag 4
        ]
    )

    print(f"Qualitätsdaten (4 Tage × 4 Messungen):\n{qualitaetsdaten}")

    # Gesamtstatistiken
    print("\nGesamtstatistiken:")
    print(f"Durchschnitt: {np.mean(qualitaetsdaten):.2f}%")
    print(f"Minimum: {np.min(qualitaetsdaten):.2f}%")
    print(f"Maximum: {np.max(qualitaetsdaten):.2f}%")
    print(f"Standardabweichung: {np.std(qualitaetsdaten):.2f}%")
    print(f"Median: {np.median(qualitaetsdaten):.2f}%")

    # Tagesweise Statistiken (pro Zeile)
    print("\nTagesweise Durchschnitte:")
    tagesdurchschnitte = np.mean(qualitaetsdaten, axis=1)
    for tag, durchschnitt in enumerate(tagesdurchschnitte, 1):
        print(f"Tag {tag}: {durchschnitt:.2f}%")

    # Messungsweise Statistiken (pro Spalte)
    print("\nMessungsweise Durchschnitte:")
    messungsdurchschnitte = np.mean(qualitaetsdaten, axis=0)
    for messung, durchschnitt in enumerate(messungsdurchschnitte, 1):
        print(f"Messung {messung}: {durchschnitt:.2f}%")

    # TODO: Ergänze:
    # - Percentile (np.percentile)
    # - Varianz (np.var)
    # - Cumulative Summen (np.cumsum)
    # - Korrelation zwischen Tagen

    return qualitaetsdaten, tagesdurchschnitte


def bonus_aufgaben():
    """
    Bonus-Aufgaben für fortgeschrittene Anwendung
    """
    print("\n=== Bonus-Aufgaben ===")

    # 1. Qualitätskontrolle mit booleschen Arrays
    messwerte = np.array([98.5, 97.2, 99.8, 96.5, 101.2, 98.9, 97.8])
    sollwert = 98.0
    toleranz = 2.0

    # Prüfe welche Werte innerhalb der Toleranz liegen
    in_toleranz = np.abs(messwerte - sollwert) <= toleranz
    ausreisser = ~in_toleranz  # Negation

    print(f"Messwerte: {messwerte}")
    print(f"Sollwert ± Toleranz: {sollwert} ± {toleranz}")
    print(f"In Toleranz: {in_toleranz}")
    print(f"Ausreißer bei Indizes: {np.where(ausreisser)[0]}")

    # 2. Produktionseffizienz-Index
    geplante_stueckzahl = np.array([100, 120, 110, 105, 115])
    tatsaechliche_stueckzahl = np.array([95, 118, 112, 103, 120])

    effizienz = (tatsaechliche_stueckzahl / geplante_stueckzahl) * 100
    print(f"\nEffizienz pro Tag: {effizienz.round(1)}%")
    print(f"Durchschnittliche Effizienz: {np.mean(effizienz):.1f}%")

    # TODO: Erweitere um:
    # - Trend-Analyse
    # - Vorhersage nächster Werte
    # - Optimale Produktionsplanung


def vollstaendige_demo():
    """
    Führe alle Aufgaben in der richtigen Reihenfolge aus
    """
    print("🔧 NumPy Grundlagen - Fast vollständige Lösung")
    print("=" * 60)

    # Alle Aufgaben durchführen
    temp_array, sensor_matrix = aufgabe_1_array_erstellung()
    produktionsdaten = aufgabe_2_array_eigenschaften()
    gesamtleistung, differenz = aufgabe_3_grundoperationen()
    qualitaetsdaten, tage = aufgabe_4_aggregationen()

    # Bonus-Material
    bonus_aufgaben()

    print("\n✅ Alle Grundlagen-Aufgaben demonstriert!")
    print("💡 Vervollständige die TODO-Bereiche für deine eigene Lösung.")


if __name__ == "__main__":
    vollstaendige_demo()

"""
📝 ANLEITUNG ZUR VERVOLLSTÄNDIGUNG:

1. Führe dieses Skript aus um die Grundfunktionalität zu sehen
2. Gehe durch jeden TODO-Bereich und implementiere die Ergänzungen
3. Experimentiere mit eigenen Daten und Anwendungsfällen
4. Teste Edge-Cases (leere Arrays, verschiedene Datentypen, etc.)
5. Erweitere um industrielle Anwendungsfälle aus deiner Erfahrung

🎯 LERNZIELE ERREICHT?
☐ Array-Erstellung aus verschiedenen Quellen
☐ Array-Eigenschaften verstehen und abfragen
☐ Elementweise Operationen und Broadcasting
☐ Aggregationsfunktionen achsenweise anwenden
☐ Praktische Anwendung in industriellen Szenarien
"""
