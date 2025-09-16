#!/usr/bin/env python3
"""
🟢 BEGINNER - Bystronic Python Grundkurs - Kapitel 3
Übung 1: NumPy Array-Grundlagen (Einsteigerfreundlich)

🎯 LERNZIELE (20-25 Minuten):
- NumPy-Arrays erstellen und verstehen
- Grundlegende Array-Eigenschaften erkunden
- Erste vektorisierte Operationen durchführen
- Array-Indexing und einfaches Slicing anwenden
- Performance-Vorteile gegenüber Python-Listen erkennen

📚 HILFSMITTEL:
- Hints: solutions/beginner/uebung_01_hints.md
- Skeleton: solutions/beginner/uebung_01_skeleton.py
- Partial: solutions/beginner/uebung_01_partial.py
- Complete: solutions/beginner/uebung_01_complete.py

🏭 BYSTRONIC-KONTEXT:
Lernen Sie NumPy-Arrays mit realen Produktionsdaten kennen:
Maschinenlaufzeiten, Stückzahlen, Qualitätsmessungen.
"""

import time

import numpy as np


def aufgabe_1_arrays_erstellen():
    """🎯 Aufgabe 1: NumPy-Arrays erstellen und erkunden"""
    print("=" * 60)
    print("🟢 AUFGABE 1: NumPy-Arrays erstellen")
    print("=" * 60)

    # TODO 1: Erstellen Sie verschiedene Arrays für Produktionsdaten
    print("📊 Produktionsdaten als NumPy-Arrays:")
    print()

    # a) Tägliche Stückzahlen für eine Woche (als Liste gegeben)
    stueckzahlen_liste = [1250, 1180, 1320, 1290, 1400, 980, 1150]
    print("a) Stückzahlen der Woche (7 Tage):")
    print(f"   Python-Liste: {stueckzahlen_liste}")

    # TODO: Konvertieren Sie die Liste zu einem NumPy-Array
    stueckzahlen_array = np.array(stueckzahlen_liste)
    print(f"   NumPy-Array:  {stueckzahlen_array}")
    print(f"   Typ:          {type(stueckzahlen_array)}")
    print()

    # b) Maschinenlaufzeiten mit np.zeros()
    print("b) Maschinenlaufzeiten initialisieren (5 Maschinen):")
    # TODO: Erstellen Sie ein Array mit 5 Nullen für Laufzeiten
    laufzeiten = np.zeros(5)
    print(f"   Initiale Laufzeiten: {laufzeiten}")
    print(f"   Shape: {laufzeiten.shape}")
    print(f"   Datentyp: {laufzeiten.dtype}")
    print()

    # c) Effizienz-Sollwerte mit np.ones()
    print("c) Effizienz-Sollwerte (alle Maschinen 85%):")
    # TODO: Erstellen Sie ein Array mit 5 Einsen und multiplizieren mit 0.85
    effizienz_soll = np.ones(5) * 0.85
    print(f"   Sollwerte: {effizienz_soll}")
    print()

    # d) Temperaturbereich mit np.linspace()
    print("d) Temperaturbereich für Laser (20°C bis 80°C, 7 Werte):")
    # TODO: Erstellen Sie 7 gleichmäßig verteilte Werte zwischen 20 und 80
    temperaturen = np.linspace(20, 80, 7)
    print(f"   Temperaturen: {temperaturen}")
    print(f"   Gerundet: {np.round(temperaturen, 1)}")
    print()

    # e) Sequenz von Stunden mit np.arange()
    print("e) Arbeitszeiten (8 bis 17 Uhr):")
    # TODO: Erstellen Sie eine Sequenz von 8 bis 17 (exclusive)
    arbeitszeiten = np.arange(8, 18)
    print(f"   Stunden: {arbeitszeiten}")
    print()

    print("✅ Aufgabe 1 abgeschlossen!")
    return stueckzahlen_array, laufzeiten, effizienz_soll


def aufgabe_2_array_eigenschaften():
    """🎯 Aufgabe 2: Array-Eigenschaften verstehen"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 2: Array-Eigenschaften erkunden")
    print("=" * 60)

    # Erstelle ein 2D-Array für Maschinendaten
    # 3 Maschinen × 4 Kennwerte (Laufzeit, Effizienz, Energie, Stückzahl)
    maschinendaten = np.array(
        [
            [8.5, 0.92, 45.2, 1200],  # Maschine 1
            [7.8, 0.89, 42.1, 1150],  # Maschine 2
            [9.2, 0.95, 48.7, 1380],  # Maschine 3
        ]
    )

    print("📊 Maschinendaten-Matrix:")
    print(f"   {maschinendaten}")
    print()

    # TODO 1: Erkunden Sie die Array-Eigenschaften
    print("🔍 Array-Eigenschaften:")
    print(f"   Shape (Form): {maschinendaten.shape}")
    print(f"   Dimensionen: {maschinendaten.ndim}")
    print(f"   Größe (Elemente): {maschinendaten.size}")
    print(f"   Datentyp: {maschinendaten.dtype}")
    print(f"   Memory (Bytes): {maschinendaten.nbytes}")
    print()

    # TODO 2: Vergleichen Sie mit Python-Liste
    python_liste = maschinendaten.tolist()

    import sys

    array_memory = maschinendaten.nbytes
    liste_memory = sys.getsizeof(python_liste)

    print("📏 Memory-Vergleich:")
    print(f"   NumPy-Array: {array_memory} Bytes")
    print(f"   Python-Liste: {liste_memory} Bytes")
    print(f"   Faktor: {liste_memory / array_memory:.1f}x mehr für Liste")
    print()

    # TODO 3: Grundlegende Statistiken
    print("📈 Statistiken (alle Werte):")
    print(f"   Minimum: {np.min(maschinendaten):.2f}")
    print(f"   Maximum: {np.max(maschinendaten):.2f}")
    print(f"   Mittelwert: {np.mean(maschinendaten):.2f}")
    print(f"   Summe: {np.sum(maschinendaten):.2f}")
    print()

    print("✅ Aufgabe 2 abgeschlossen!")
    return maschinendaten


def aufgabe_3_indexing_slicing():
    """🎯 Aufgabe 3: Array-Indexing und Slicing"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 3: Indexing und Slicing")
    print("=" * 60)

    # Verwende Maschinendaten aus vorheriger Aufgabe
    maschinendaten = np.array(
        [
            [
                8.5,
                0.92,
                45.2,
                1200,
            ],  # Maschine 1: [Laufzeit, Effizienz, Energie, Stückzahl]
            [7.8, 0.89, 42.1, 1150],  # Maschine 2
            [9.2, 0.95, 48.7, 1380],  # Maschine 3
        ]
    )

    print("📊 Maschinendaten (3 × 4 Matrix):")
    print("   Spalten: [Laufzeit(h), Effizienz(%), Energie(kW), Stückzahl]")
    print(f"   {maschinendaten}")
    print()

    # TODO 1: Einzelne Elemente extrahieren
    print("🎯 Einzelne Werte:")
    # Erste Maschine, Laufzeit (Zeile 0, Spalte 0)
    laufzeit_m1 = maschinendaten[0, 0]
    print(f"   Laufzeit Maschine 1: {laufzeit_m1} Stunden")

    # TODO: Stückzahl der dritten Maschine (Zeile 2, Spalte 3)
    stueckzahl_m3 = maschinendaten[2, 3]
    print(f"   Stückzahl Maschine 3: {stueckzahl_m3}")
    print()

    # TODO 2: Ganze Zeilen (Maschinen)
    print("🏭 Komplette Maschinendaten:")
    erste_maschine = maschinendaten[0]  # oder maschinendaten[0, :]
    print(f"   Maschine 1: {erste_maschine}")

    # TODO: Daten der letzten Maschine
    letzte_maschine = maschinendaten[-1]  # oder maschinendaten[2]
    print(f"   Letzte Maschine: {letzte_maschine}")
    print()

    # TODO 3: Ganze Spalten (Kennwerte)
    print("📊 Kennwerte aller Maschinen:")
    alle_laufzeiten = maschinendaten[:, 0]  # Alle Zeilen, Spalte 0
    print(f"   Alle Laufzeiten: {alle_laufzeiten}")

    # TODO: Alle Effizienzen (Spalte 1)
    alle_effizienzen = maschinendaten[:, 1]
    print(f"   Alle Effizienzen: {alle_effizienzen}")

    # TODO: Alle Stückzahlen (letzte Spalte)
    alle_stueckzahlen = maschinendaten[:, -1]  # oder [:, 3]
    print(f"   Alle Stückzahlen: {alle_stueckzahlen}")
    print()

    # TODO 4: Slicing - Teilbereiche
    print("✂️ Slicing-Operationen:")
    # Erste zwei Maschinen, erste zwei Kennwerte
    teilbereich = maschinendaten[:2, :2]
    print("   Erste 2 Maschinen, erste 2 Kennwerte:")
    print(f"   {teilbereich}")

    # TODO: Letzte zwei Kennwerte aller Maschinen
    energie_und_stueck = maschinendaten[:, 2:]
    print("   Energie und Stückzahl aller Maschinen:")
    print(f"   {energie_und_stueck}")
    print()

    print("✅ Aufgabe 3 abgeschlossen!")
    return alle_laufzeiten, alle_effizienzen, alle_stueckzahlen


def aufgabe_4_erste_operationen():
    """🎯 Aufgabe 4: Erste vektorisierte Operationen"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 4: Vektorisierte Operationen")
    print("=" * 60)

    # Produktionsdaten für eine Woche
    stueckzahlen = np.array([1250, 1180, 1320, 1290, 1400, 980, 1150])
    wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    print("📊 Wöchentliche Stückzahlen:")
    for tag, anzahl in zip(wochentage, stueckzahlen, strict=False):
        print(f"   {tag}: {anzahl:,} Stück")
    print()

    # TODO 1: Grundlegende Statistiken
    print("📈 Wochenstatistiken:")
    print(f"   Gesamt produziert: {np.sum(stueckzahlen):,} Stück")
    print(f"   Durchschnitt/Tag: {np.mean(stueckzahlen):.0f} Stück")
    print(
        f"   Minimum: {np.min(stueckzahlen):,} Stück ({wochentage[np.argmin(stueckzahlen)]})"
    )
    print(
        f"   Maximum: {np.max(stueckzahlen):,} Stück ({wochentage[np.argmax(stueckzahlen)]})"
    )
    print(f"   Standardabweichung: {np.std(stueckzahlen):.0f} Stück")
    print()

    # TODO 2: Vektorisierte Berechnungen
    print("🎯 Zielvergleich (Soll: 1200 Stück/Tag):")
    sollwert = 1200

    # Abweichungen berechnen (vektorisiert!)
    abweichungen = stueckzahlen - sollwert
    print(f"   Abweichungen: {abweichungen}")

    # Prozentuale Abweichungen
    prozent_abweichung = (abweichungen / sollwert) * 100
    print(f"   Prozentual: {np.round(prozent_abweichung, 1)}%")

    # TODO: Wie viele Tage über/unter Soll?
    tage_ueber_soll = np.sum(stueckzahlen > sollwert)
    tage_unter_soll = np.sum(stueckzahlen < sollwert)
    print(f"   Tage über Soll: {tage_ueber_soll}")
    print(f"   Tage unter Soll: {tage_unter_soll}")
    print()

    # TODO 3: Effizienz-Berechnung
    print("⚡ Effizienz-Berechnungen:")
    arbeitsstunden = np.array([8, 8, 8, 8, 8, 6, 4])  # Wochenende kürzer

    # Stück pro Stunde (vektorisiert)
    stueck_pro_stunde = stueckzahlen / arbeitsstunden
    print(f"   Stück/Stunde: {np.round(stueck_pro_stunde, 1)}")

    # Effizienz relativ zum Sollwert
    effizienz_prozent = (stueckzahlen / sollwert) * 100
    print(f"   Effizienz: {np.round(effizienz_prozent, 1)}%")
    print()

    # TODO 4: Kumulative Summe (Wochenverlauf)
    print("📈 Kumulativer Produktionsverlauf:")
    kumulative_produktion = np.cumsum(stueckzahlen)
    for tag, kumulativ in zip(wochentage, kumulative_produktion, strict=False):
        print(f"   Nach {tag}: {kumulativ:,} Stück")
    print()

    print("✅ Aufgabe 4 abgeschlossen!")
    return stueckzahlen, effizienz_prozent


def aufgabe_5_performance_demo():
    """🎯 Aufgabe 5: Performance-Vergleich NumPy vs Python"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 5: Performance-Demo")
    print("=" * 60)

    # Große Datenmengen simulieren (ein Monat Sensordaten)
    n_messungen = 100000  # 100k Messungen
    print(f"🔬 Simuliere {n_messungen:,} Sensormessungen")

    # Generiere Testdaten
    np.random.seed(42)  # Für reproduzierbare Ergebnisse
    messungen_liste = [20 + 10 * np.random.random() for _ in range(n_messungen)]
    messungen_array = 20 + 10 * np.random.random(n_messungen)

    print(f"   Datenbereich: {messungen_array.min():.1f} - {messungen_array.max():.1f}")
    print()

    # TODO 1: Summe berechnen
    print("🧮 Test 1: Summe aller Messungen")

    # Python-Version
    start_time = time.time()
    python_summe = sum(messungen_liste)
    python_zeit = time.time() - start_time

    # NumPy-Version
    start_time = time.time()
    numpy_summe = np.sum(messungen_array)
    numpy_zeit = time.time() - start_time

    print(f"   Python-Liste: {python_zeit:.4f}s (Summe: {python_summe:,.0f})")
    print(f"   NumPy-Array:  {numpy_zeit:.4f}s (Summe: {numpy_summe:,.0f})")
    print(f"   Speedup: {python_zeit / numpy_zeit:.1f}x schneller mit NumPy!")
    print()

    # TODO 2: Komplexere Berechnung (Quadrat + 1)
    print("🧮 Test 2: Quadrat + 1 für alle Werte")

    # Python List Comprehension
    start_time = time.time()
    python_result = [x**2 + 1 for x in messungen_liste]
    python_zeit = time.time() - start_time

    # NumPy vektorisiert
    start_time = time.time()
    numpy_result = messungen_array**2 + 1
    numpy_zeit = time.time() - start_time

    print(f"   Python-Liste: {python_zeit:.4f}s")
    print(f"   NumPy-Array:  {numpy_zeit:.4f}s")
    print(f"   Speedup: {python_zeit / numpy_zeit:.1f}x schneller mit NumPy!")
    print()

    # TODO 3: Memory-Verbrauch
    import sys

    python_memory = sys.getsizeof(messungen_liste) / (1024 * 1024)
    numpy_memory = messungen_array.nbytes / (1024 * 1024)

    print("💾 Memory-Verbrauch:")
    print(f"   Python-Liste: {python_memory:.2f} MB")
    print(f"   NumPy-Array:  {numpy_memory:.2f} MB")
    print(f"   Faktor: {python_memory / numpy_memory:.1f}x weniger Memory mit NumPy!")
    print()

    # TODO 4: Praktische Anwendung - Toleranzprüfung
    print("🎯 Praxis-Test: Qualitätskontrolle (Toleranzprüfung)")
    sollwert = 25.0
    toleranz = 2.0

    # Python-Version
    start_time = time.time()
    python_ok_count = sum(1 for x in messungen_liste if abs(x - sollwert) <= toleranz)
    python_zeit = time.time() - start_time

    # NumPy-Version
    start_time = time.time()
    numpy_ok_count = np.sum(np.abs(messungen_array - sollwert) <= toleranz)
    numpy_zeit = time.time() - start_time

    print(f"   Python: {python_zeit:.4f}s ({python_ok_count:,} OK)")
    print(f"   NumPy:  {numpy_zeit:.4f}s ({numpy_ok_count:,} OK)")
    print(f"   Speedup: {python_zeit / numpy_zeit:.1f}x schneller!")

    ausschuss_rate = (1 - numpy_ok_count / n_messungen) * 100
    print(f"   Ausschussrate: {ausschuss_rate:.2f}%")
    print()

    print("✅ Aufgabe 5 abgeschlossen!")


def main():
    """🚀 Hauptprogramm - Alle Aufgaben ausführen"""
    print("🟢 BEGINNER: NumPy Array-Grundlagen für Bystronic")
    print("=" * 70)
    print("📚 Lernen Sie NumPy-Arrays mit praktischen Produktionsbeispielen!")
    print("🎯 Ziel: NumPy verstehen und Performance-Vorteile erleben")
    print()

    try:
        # Aufgabe 1: Arrays erstellen
        stueckzahlen, laufzeiten, effizienz = aufgabe_1_arrays_erstellen()

        # Aufgabe 2: Array-Eigenschaften
        maschinendaten = aufgabe_2_array_eigenschaften()

        # Aufgabe 3: Indexing und Slicing
        alle_laufzeiten, alle_effizienzen, alle_stueckzahlen = (
            aufgabe_3_indexing_slicing()
        )

        # Aufgabe 4: Erste Operationen
        woche_stueckzahlen, effizienz_prozent = aufgabe_4_erste_operationen()

        # Aufgabe 5: Performance-Demo
        aufgabe_5_performance_demo()

        # Erfolgreicher Abschluss
        print("\n" + "🎉" * 30)
        print("🎉 HERZLICHEN GLÜCKWUNSCH! 🎉")
        print("🎉" * 30)
        print("✅ Sie haben alle Beginner-Aufgaben zu NumPy-Arrays gemeistert!")
        print()
        print("🎓 Sie können jetzt:")
        print("   • NumPy-Arrays erstellen und verstehen")
        print("   • Array-Eigenschaften erkunden")
        print("   • Indexing und Slicing anwenden")
        print("   • Vektorisierte Operationen durchführen")
        print("   • Performance-Vorteile von NumPy nutzen")
        print()
        print("➡️ NÄCHSTE SCHRITTE:")
        print("📚 Übung 2: Mathematische Operationen")
        print("🚀 uv run python exercises/beginner/uebung_02_mathematik_beginner.py")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
        print("💡 Sie können jederzeit weitermachen!")

    except Exception as e:
        print(f"\n❌ Fehler aufgetreten: {e}")
        print(
            "💡 Tipp: Überprüfen Sie die Hints in solutions/beginner/uebung_01_hints.md"
        )


if __name__ == "__main__":
    main()
