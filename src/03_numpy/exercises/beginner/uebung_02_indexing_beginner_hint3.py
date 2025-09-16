#!/usr/bin/env python3
"""
Hilfe Stufe 3: Code-Snippets für NumPy Indexing & Slicing
========================================================

💡 HINT 3 - Konkrete Code-Beispiele

Hier sind die wichtigsten Code-Bausteine für die Aufgaben:
"""

import numpy as np


def aufgabe_1_einfaches_indexing_hilfe():
    """Code-Snippet für Aufgabe 1: Einfaches Indexing"""
    print("=== Aufgabe 1: Einfaches Indexing ===")

    # Sensordaten von 24 Stunden (stündliche Messwerte)
    temperaturen = np.array(
        [
            18.5,
            19.2,
            19.8,
            20.1,
            20.5,
            21.2,
            22.1,
            23.5,
            24.8,
            25.3,
            26.1,
            26.8,
            27.2,
            26.9,
            26.5,
            25.8,
            24.9,
            23.7,
            22.8,
            21.9,
            21.1,
            20.3,
            19.7,
            19.1,
        ]
    )

    # TODO: Vervollständige diese Zugriffe
    print(f"Alle Temperaturen: {temperaturen}")

    # Einzelne Werte
    erste_messung = temperaturen[0]  # Stunde 0
    letzte_messung = temperaturen[-1]  # Stunde 23
    mittag_temp = temperaturen[12]  # Stunde 12

    print(f"Erste Messung (0h): {erste_messung}°C")
    print(f"Mittag (12h): {mittag_temp}°C")
    print(f"Letzte Messung (23h): {letzte_messung}°C")

    # Negative Indexierung
    vorletzter_wert = temperaturen[-2]
    drittletzter_wert = temperaturen[-3]

    print(f"Vorletzter Wert: {vorletzter_wert}°C")
    print(f"Drittletzter Wert: {drittletzter_wert}°C")


def aufgabe_2_slicing_hilfe():
    """Code-Snippet für Aufgabe 2: Array Slicing"""
    print("\n=== Aufgabe 2: Array Slicing ===")

    # Produktionsdaten für eine Woche (7 Tage)
    stueckzahlen = np.array([120, 135, 128, 142, 118, 105, 95])

    # TODO: Implementiere verschiedene Slicing-Operationen
    print(f"Wochendaten: {stueckzahlen}")

    # Bereiche extrahieren
    erste_drei_tage = stueckzahlen[:3]  # [120, 135, 128]
    letzte_drei_tage = stueckzahlen[-3:]  # [118, 105, 95]
    arbeitswoche = stueckzahlen[:5]  # Montag bis Freitag
    wochenende = stueckzahlen[5:]  # Samstag, Sonntag

    print(f"Erste 3 Tage: {erste_drei_tage}")
    print(f"Letzte 3 Tage: {letzte_drei_tage}")
    print(f"Arbeitswoche: {arbeitswoche}")
    print(f"Wochenende: {wochenende}")

    # Step-Parameter verwenden
    jeden_zweiten_tag = stueckzahlen[::2]  # [120, 128, 118, 95]
    rueckwaerts = stueckzahlen[::-1]  # Umgekehrte Reihenfolge

    print(f"Jeden 2. Tag: {jeden_zweiten_tag}")
    print(f"Rückwärts: {rueckwaerts}")


def aufgabe_3_2d_indexing_hilfe():
    """Code-Snippet für Aufgabe 3: 2D Array Indexing"""
    print("\n=== Aufgabe 3: 2D Array Indexing ===")

    # Qualitätsdaten: 4 Schichten × 6 Stunden pro Schicht
    qualitaetsdaten = np.array(
        [
            [98.5, 99.1, 97.8, 98.9, 99.2, 98.7],  # Frühschicht
            [97.9, 98.8, 99.3, 99.0, 98.6, 99.4],  # Spätschicht
            [98.1, 99.2, 97.5, 98.3, 99.1, 98.8],  # Nachtschicht
            [99.0, 98.7, 99.5, 98.9, 99.3, 99.1],  # Wochenendschicht
        ]
    )

    # TODO: Implementiere 2D-Zugriffe
    print(f"Qualitätsdaten (4×6):\n{qualitaetsdaten}")

    # Einzelne Elemente [zeile, spalte]
    fruehschicht_stunde_2 = qualitaetsdaten[0, 2]  # 97.8
    nachtschicht_letzte = qualitaetsdaten[2, -1]  # 98.8

    print(f"Frühschicht Stunde 2: {fruehschicht_stunde_2}%")
    print(f"Nachtschicht letzte Stunde: {nachtschicht_letzte}%")

    # Ganze Zeilen und Spalten
    erste_schicht = qualitaetsdaten[0, :]  # Ganze erste Zeile
    dritte_stunde = qualitaetsdaten[:, 2]  # Ganze dritte Spalte

    print(f"Erste Schicht (alle Stunden): {erste_schicht}")
    print(f"Dritte Stunde (alle Schichten): {dritte_stunde}")

    # Submatrizen extrahieren
    erste_zwei_schichten = qualitaetsdaten[:2, :]  # Erste 2 Zeilen
    letzte_drei_stunden = qualitaetsdaten[:, -3:]  # Letzte 3 Spalten
    mittlerer_bereich = qualitaetsdaten[1:3, 2:5]  # 2×3 Submatrix

    print(f"Erste 2 Schichten:\n{erste_zwei_schichten}")
    print(f"Letzte 3 Stunden:\n{letzte_drei_stunden}")
    print(f"Mittlerer Bereich:\n{mittlerer_bereich}")


def aufgabe_4_boolean_indexing_hilfe():
    """Code-Snippet für Aufgabe 4: Boolean Indexing"""
    print("\n=== Aufgabe 4: Boolean Indexing ===")

    # Maschinendaten mit einigen problematischen Werten
    maschinendaten = np.array([85, 92, 78, 95, 103, 88, 91, 76, 89, 97])

    # TODO: Implementiere Boolean Filtering
    print(f"Maschinendaten: {maschinendaten}")

    # Einfache Bedingungen
    hohe_werte = maschinendaten > 90
    niedrige_werte = maschinendaten < 80

    print(f"Werte > 90: {hohe_werte}")
    print(f"Hohe Werte gefiltert: {maschinendaten[hohe_werte]}")
    print(f"Niedrige Werte gefiltert: {maschinendaten[niedrige_werte]}")

    # Kombinierte Bedingungen
    normale_werte = (maschinendaten >= 80) & (maschinendaten <= 95)
    extreme_werte = (maschinendaten < 80) | (maschinendaten > 95)

    print(f"Normale Werte (80-95): {maschinendaten[normale_werte]}")
    print(f"Extreme Werte (<80 oder >95): {maschinendaten[extreme_werte]}")

    # Indizes der gefilterten Werte finden
    problematische_indizes = np.where(extreme_werte)[0]
    print(f"Indizes problematischer Werte: {problematische_indizes}")


def aufgabe_5_fancy_indexing_hilfe():
    """Code-Snippet für Aufgabe 5: Fancy Indexing"""
    print("\n=== Aufgabe 5: Fancy Indexing ===")

    # Sensordaten von 10 Sensoren
    sensordaten = np.array([23.1, 24.5, 22.8, 25.2, 23.9, 24.1, 22.5, 23.7, 24.8, 23.3])

    # TODO: Implementiere Fancy Indexing
    print(f"Alle Sensordaten: {sensordaten}")

    # Spezifische Sensoren auswählen
    wichtige_sensoren = [0, 3, 7, 9]  # Sensor 1, 4, 8, 10
    wichtige_werte = sensordaten[wichtige_sensoren]

    print(f"Wichtige Sensoren (Indizes {wichtige_sensoren}): {wichtige_werte}")

    # Dynamische Index-Arrays
    # Finde Indizes der 3 höchsten Werte
    sortierte_indizes = np.argsort(sensordaten)  # Sortiert aufsteigend
    top_3_indizes = sortierte_indizes[-3:]  # Letzte 3 = höchste
    top_3_werte = sensordaten[top_3_indizes]

    print(f"Top 3 Indizes: {top_3_indizes}")
    print(f"Top 3 Werte: {top_3_werte}")

    # Array-Indizes für 2D Arrays
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    zeilen_indizes = [0, 2, 1]
    spalten_indizes = [1, 0, 2]

    # Wähle Elemente [0,1], [2,0], [1,2]
    ausgewaehlte_elemente = matrix[zeilen_indizes, spalten_indizes]
    print(f"Matrix:\n{matrix}")
    print(f"Ausgewählte Elemente: {ausgewaehlte_elemente}")  # [2, 7, 6]


if __name__ == "__main__":
    # Führe alle Hilfe-Beispiele aus
    aufgabe_1_einfaches_indexing_hilfe()
    aufgabe_2_slicing_hilfe()
    aufgabe_3_2d_indexing_hilfe()
    aufgabe_4_boolean_indexing_hilfe()
    aufgabe_5_fancy_indexing_hilfe()

    print("\n💡 Nutze diese Code-Snippets als Vorlage für deine Lösung!")
    print("   Erweitere sie um die spezifischen Anforderungen der Aufgaben.")
