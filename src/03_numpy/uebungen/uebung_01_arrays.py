#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Übung 1: NumPy Array-Grundlagen

Diese Übung behandelt die Grundlagen von NumPy-Arrays:
- Array-Erstellung mit verschiedenen Methoden
- Array-Eigenschaften und Datentypen
- Grundlegende Array-Operationen
- Indexing und Slicing
"""

import numpy as np


def uebung_1_1() -> None:
    """Übung 1.1: Arrays erstellen"""
    print("=" * 60)
    print("ÜBUNG 1.1: Arrays erstellen")
    print("=" * 60)

    # TODO: Erstellen Sie verschiedene Arrays

    # a) Erstellen Sie ein Array aus der Liste [10, 20, 30, 40, 50]
    print("a) Array aus Liste erstellen:")
    # LÖSUNG:
    array_aus_liste = np.array([10, 20, 30, 40, 50])
    print(f"   Array: {array_aus_liste}")
    print(f"   Typ: {type(array_aus_liste)}")

    # b) Erstellen Sie ein Array mit 10 Nullen
    print("\nb) Array mit 10 Nullen:")
    # TODO: Ihr Code hier
    nullen_array = np.zeros(10)
    print(f"   Array: {nullen_array}")

    # c) Erstellen Sie ein Array mit 8 Einsen
    print("\nc) Array mit 8 Einsen:")
    # TODO: Ihr Code hier
    einsen_array = np.ones(8)
    print(f"   Array: {einsen_array}")

    # d) Erstellen Sie ein Array mit Zahlen von 0 bis 20 (Schrittweite 2)
    print("\nd) Array 0 bis 20 mit Schrittweite 2:")
    # TODO: Ihr Code hier
    bereich_array = np.arange(0, 21, 2)
    print(f"   Array: {bereich_array}")

    # e) Erstellen Sie 5 gleichmäßig verteilte Werte zwischen 1 und 10
    print("\ne) 5 gleichmäßig verteilte Werte zwischen 1 und 10:")
    # TODO: Ihr Code hier
    linspace_array = np.linspace(1, 10, 5)
    print(f"   Array: {linspace_array}")

    # f) Erstellen Sie ein 3x3 Array mit Zufallszahlen zwischen 0 und 1
    print("\nf) 3x3 Zufallsarray:")
    # TODO: Ihr Code hier
    np.random.seed(42)  # Für reproduzierbare Ergebnisse
    zufall_array = np.random.random((3, 3))
    print(f"   Array:\n{zufall_array}")


def uebung_1_2() -> None:
    """Übung 1.2: Array-Eigenschaften untersuchen"""
    print("\n" + "=" * 60)
    print("ÜBUNG 1.2: Array-Eigenschaften")
    print("=" * 60)

    # Gegeben: Produktionsdaten einer Woche (7 Tage, 3 Schichten, 4 Maschinen)
    np.random.seed(123)
    produktionsdaten = np.random.randint(800, 1200, size=(7, 3, 4))

    print("Produktionsdaten erstellt (7 Tage, 3 Schichten, 4 Maschinen)")

    # TODO: Untersuchen Sie die Array-Eigenschaften

    # a) Welche Form (Shape) hat das Array?
    print(f"\na) Shape des Arrays: {produktionsdaten.shape}")

    # b) Wie viele Dimensionen hat es?
    print(f"b) Anzahl Dimensionen: {produktionsdaten.ndim}")

    # c) Wie viele Elemente insgesamt?
    print(f"c) Gesamtanzahl Elemente: {produktionsdaten.size}")

    # d) Welchen Datentyp haben die Elemente?
    print(f"d) Datentyp: {produktionsdaten.dtype}")

    # e) Wie viel Speicher verbraucht das Array?
    print(f"e) Speicherverbrauch: {produktionsdaten.nbytes} Bytes")

    # f) Zeigen Sie die ersten 2 Tage an
    print(f"\nf) Erste 2 Tage:\n{produktionsdaten[:2]}")


def uebung_1_3() -> None:
    """Übung 1.3: Indexing und Slicing"""
    print("\n" + "=" * 60)
    print("ÜBUNG 1.3: Indexing und Slicing")
    print("=" * 60)

    # Maschinendaten: 6 Maschinen, 5 Kennwerte pro Maschine
    maschinendaten = np.array(
        [
            [8.5, 0.92, 45.2, 24, 1],  # Laufzeit, Effizienz, Energie, Teile/h, Ausfälle
            [7.2, 0.88, 38.7, 20, 2],
            [9.1, 0.95, 52.3, 28, 0],
            [6.8, 0.85, 35.1, 18, 3],
            [8.3, 0.90, 47.8, 25, 1],
            [7.9, 0.93, 44.1, 26, 0],
        ]
    )

    print("Maschinendaten (6 Maschinen x 5 Kennwerte):")
    print("Spalten: Laufzeit, Effizienz, Energie, Teile/h, Ausfälle")
    print(maschinendaten)

    # TODO: Verwenden Sie Indexing und Slicing

    # a) Holen Sie die Daten der 3. Maschine (Index 2)
    print(f"\na) Daten der 3. Maschine: {maschinendaten[2]}")

    # b) Holen Sie alle Laufzeiten (erste Spalte)
    print(f"b) Alle Laufzeiten: {maschinendaten[:, 0]}")

    # c) Holen Sie die Effizienzen der ersten 3 Maschinen
    print(f"c) Effizienzen 1-3: {maschinendaten[:3, 1]}")

    # d) Holen Sie die letzten 2 Kennwerte aller Maschinen
    print(f"d) Letzte 2 Kennwerte:\n{maschinendaten[:, -2:]}")

    # e) Holen Sie jede zweite Maschine (Index 0, 2, 4)
    print(f"e) Jede zweite Maschine:\n{maschinendaten[::2]}")

    # f) Ändern Sie die Effizienz der ersten Maschine auf 0.95
    maschinendaten[0, 1] = 0.95
    print(f"f) Erste Maschine nach Änderung: {maschinendaten[0]}")


def uebung_1_4() -> None:
    """Übung 1.4: Array-Operationen"""
    print("\n" + "=" * 60)
    print("ÜBUNG 1.4: Array-Operationen")
    print("=" * 60)

    # Qualitätsmessdaten
    messwerte = np.array([2.05, 1.98, 2.02, 2.07, 1.95, 2.01, 2.04, 1.99, 2.03, 1.97])
    sollwert = 2.0
    toleranz = 0.05

    print(f"Messwerte: {messwerte}")
    print(f"Sollwert: {sollwert} ± {toleranz}")

    # TODO: Führen Sie verschiedene Operationen durch

    # a) Berechnen Sie die Abweichung vom Sollwert
    abweichungen = messwerte - sollwert
    print(f"\na) Abweichungen: {abweichungen}")

    # b) Berechnen Sie die absoluten Abweichungen
    abs_abweichungen = np.abs(abweichungen)
    print(f"b) Absolute Abweichungen: {abs_abweichungen}")

    # c) Finden Sie alle Werte außerhalb der Toleranz
    ausserhalb_toleranz = abs_abweichungen > toleranz
    print(f"c) Außerhalb Toleranz (Boolean): {ausserhalb_toleranz}")
    print(f"   Anzahl: {np.sum(ausserhalb_toleranz)}")

    # d) Holen Sie die Werte, die außerhalb der Toleranz liegen
    fehlerhafte_werte = messwerte[ausserhalb_toleranz]
    print(f"d) Fehlerhafte Werte: {fehlerhafte_werte}")

    # e) Berechnen Sie den Prozentsatz der guten Teile
    gute_teile_prozent = (1 - np.sum(ausserhalb_toleranz) / len(messwerte)) * 100
    print(f"e) Gute Teile: {gute_teile_prozent:.1f}%")

    # f) Setzen Sie alle fehlerhaften Werte auf den Sollwert
    korrigierte_werte = messwerte.copy()
    korrigierte_werte[ausserhalb_toleranz] = sollwert
    print(f"f) Korrigierte Werte: {korrigierte_werte}")


def uebung_1_5() -> None:
    """Übung 1.5: Mehrdimensionale Arrays"""
    print("\n" + "=" * 60)
    print("ÜBUNG 1.5: Mehrdimensionale Arrays")
    print("=" * 60)

    # TODO: Arbeiten Sie mit 2D-Arrays

    # a) Erstellen Sie eine 4x5 Matrix mit Zahlen von 1 bis 20
    matrix = np.arange(1, 21).reshape(4, 5)
    print("a) 4x5 Matrix:")
    print(matrix)

    # b) Berechnen Sie die Summe jeder Zeile
    zeilen_summen = np.sum(matrix, axis=1)
    print(f"\nb) Zeilen-Summen: {zeilen_summen}")

    # c) Berechnen Sie die Summe jeder Spalte
    spalten_summen = np.sum(matrix, axis=0)
    print(f"c) Spalten-Summen: {spalten_summen}")

    # d) Finden Sie das Maximum in jeder Zeile
    zeilen_maxima = np.max(matrix, axis=1)
    print(f"d) Zeilen-Maxima: {zeilen_maxima}")

    # e) Transponieren Sie die Matrix
    transponiert = matrix.T
    print(f"e) Transponierte Matrix:\n{transponiert}")

    # f) Erstellen Sie eine Boolean-Maske für Werte > 10
    groesser_10 = matrix > 10
    print(f"f) Werte > 10:\n{groesser_10}")
    print(f"   Anzahl Werte > 10: {np.sum(groesser_10)}")


def uebung_1_6() -> None:
    """Übung 1.6: Praktisches Beispiel - Koordinaten"""
    print("\n" + "=" * 60)
    print("ÜBUNG 1.6: Praktisches Beispiel - Koordinaten")
    print("=" * 60)

    # CNC-Koordinaten für ein rechteckiges Teil
    punkte = np.array(
        [
            [0, 0],  # Startpunkt
            [50, 0],  # Rechts
            [50, 30],  # Hoch
            [0, 30],  # Links
            [0, 0],  # Zurück zum Start
        ]
    )

    print("CNC-Koordinaten:")
    for i, punkt in enumerate(punkte):
        print(f"  P{i}: ({punkt[0]:2.0f}, {punkt[1]:2.0f})")

    # TODO: Berechnen Sie verschiedene Werte

    # a) Berechnen Sie die Entfernungen zwischen aufeinanderfolgenden Punkten
    # Tipp: np.diff() für Differenzen, np.sqrt() und np.sum() für Entfernungen
    differenzen = np.diff(punkte, axis=0)
    entfernungen = np.sqrt(np.sum(differenzen**2, axis=1))
    print(f"\na) Entfernungen zwischen Punkten: {entfernungen}")

    # b) Berechnen Sie die Gesamtlänge des Pfads
    gesamtlaenge = np.sum(entfernungen)
    print(f"b) Gesamtlänge: {gesamtlaenge:.1f} mm")

    # c) Finden Sie den Mittelpunkt des Rechtecks
    # Tipp: Verwenden Sie die ersten 4 Punkte (ohne den Endpunkt)
    mittelpunkt = np.mean(punkte[:-1], axis=0)
    print(f"c) Mittelpunkt: ({mittelpunkt[0]:.1f}, {mittelpunkt[1]:.1f})")

    # d) Berechnen Sie die Entfernung jedes Punkts vom Mittelpunkt
    entf_vom_mittelpunkt = np.sqrt(np.sum((punkte[:-1] - mittelpunkt) ** 2, axis=1))
    print(f"d) Entfernungen vom Mittelpunkt: {entf_vom_mittelpunkt}")

    # e) Verschieben Sie alle Punkte um (10, 15)
    verschiebung = np.array([10, 15])
    verschobene_punkte = punkte + verschiebung
    print(f"e) Verschobene Punkte:\n{verschobene_punkte}")


def hauptprogramm() -> None:
    """Hauptprogramm - alle Übungen ausführen"""
    print("🔢 NUMPY ARRAY-GRUNDLAGEN - ÜBUNGEN")

    try:
        uebung_1_1()
        uebung_1_2()
        uebung_1_3()
        uebung_1_4()
        uebung_1_5()
        uebung_1_6()

        print("\n" + "=" * 60)
        print("✅ ALLE ÜBUNGEN ERFOLGREICH ABGESCHLOSSEN!")
        print("=" * 60)
        print("\n📝 Was Sie gelernt haben:")
        print("• Array-Erstellung mit verschiedenen Methoden")
        print("• Array-Eigenschaften (Shape, Dtype, etc.)")
        print("• Indexing und Slicing von Arrays")
        print("• Boolean Indexing für Filteroperationen")
        print("• Grundlegende Array-Operationen")
        print("• Arbeit mit mehrdimensionalen Arrays")
        print("• Praktische Anwendung: Koordinatenberechnungen")

        print("\n🎯 Nächste Schritte:")
        print("• Übung 2: Mathematische Operationen")
        print("• Vertiefung: Broadcasting und erweiterte Operationen")

    except Exception as e:
        print(f"\n❌ Fehler in den Übungen: {e}")
        print("Überprüfen Sie Ihren Code und versuchen Sie es erneut.")


if __name__ == "__main__":
    hauptprogramm()
