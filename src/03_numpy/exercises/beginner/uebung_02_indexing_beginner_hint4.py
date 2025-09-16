#!/usr/bin/env python3
"""
Hilfe Stufe 4: Fast vollständige Lösung für NumPy Indexing & Slicing
===================================================================

💡 HINT 4 - Nahezu vollständige Implementierung

Dies ist eine fast vollständige Lösung. Du musst nur noch die TODO-Bereiche
vervollständigen und eventuell Anpassungen vornehmen.
"""

import numpy as np


def aufgabe_1_einfaches_indexing():
    """
    Fast vollständige Lösung für Aufgabe 1: Einfaches Indexing
    """
    print("=== Aufgabe 1: Einfaches Indexing ===")

    # Temperaturmessungen über 24 Stunden (stündlich)
    temperaturen = np.array(
        [
            18.5,
            19.2,
            19.8,
            20.1,
            20.5,
            21.2,
            22.1,
            23.5,  # 0-7 Uhr
            24.8,
            25.3,
            26.1,
            26.8,
            27.2,
            26.9,
            26.5,
            25.8,  # 8-15 Uhr
            24.9,
            23.7,
            22.8,
            21.9,
            21.1,
            20.3,
            19.7,
            19.1,  # 16-23 Uhr
        ]
    )

    print(f"24h Temperaturdaten: {temperaturen}")
    print(f"Array-Shape: {temperaturen.shape}")

    # Einzelne kritische Zeitpunkte
    mitternacht = temperaturen[0]
    morgendaemmerung = temperaturen[6]
    mittag = temperaturen[12]
    abend = temperaturen[18]
    spaet_abends = temperaturen[-1]

    print("\nKritische Zeitpunkte:")
    print(f"Mitternacht (0h): {mitternacht}°C")
    print(f"Morgendämmerung (6h): {morgendaemmerung}°C")
    print(f"Mittag (12h): {mittag}°C")
    print(f"Abend (18h): {abend}°C")
    print(f"Spät abends (23h): {spaet_abends}°C")

    # Negative Indexierung für letzte Werte
    letzte_3_messungen = [temperaturen[-3], temperaturen[-2], temperaturen[-1]]
    print(f"Letzte 3 Messungen: {letzte_3_messungen}")

    # TODO: Ergänze:
    # - Finde Min/Max Temperaturen und ihre Zeitpunkte
    # - Bestimme Temperaturen zu Arbeitszeiten (8-17 Uhr)
    # - Identifiziere Nachttemperaturen (22-6 Uhr)

    return temperaturen


def aufgabe_2_array_slicing():
    """
    Fast vollständige Lösung für Aufgabe 2: Array Slicing
    """
    print("\n=== Aufgabe 2: Array Slicing ===")

    # Produktionsdaten für 2 Wochen (14 Tage)
    produktionsdaten = np.array(
        [
            120,
            135,
            128,
            142,
            118,
            105,
            95,  # Woche 1
            130,
            125,
            140,
            145,
            122,
            110,
            100,  # Woche 2
        ]
    )

    print(f"Produktionsdaten (14 Tage): {produktionsdaten}")

    # Wochenweise Aufteilen
    woche_1 = produktionsdaten[:7]
    woche_2 = produktionsdaten[7:]
    # Alternativ: woche_2 = produktionsdaten[7:14]

    print(f"Woche 1: {woche_1}")
    print(f"Woche 2: {woche_2}")

    # Arbeitstage vs. Wochenende (Mo-Fr vs. Sa-So)
    arbeitstage_w1 = produktionsdaten[:5]  # Tag 0-4
    wochenende_w1 = produktionsdaten[5:7]  # Tag 5-6
    arbeitstage_w2 = produktionsdaten[7:12]  # Tag 7-11
    wochenende_w2 = produktionsdaten[12:14]  # Tag 12-13

    print(f"\nArbeitstage Woche 1: {arbeitstage_w1}")
    print(f"Wochenende Woche 1: {wochenende_w1}")
    print(f"Arbeitstage Woche 2: {arbeitstage_w2}")
    print(f"Wochenende Woche 2: {wochenende_w2}")

    # Alle Arbeitstage kombinieren
    alle_arbeitstage = np.concatenate([arbeitstage_w1, arbeitstage_w2])
    alle_wochenenden = np.concatenate([wochenende_w1, wochenende_w2])

    print(f"Alle Arbeitstage: {alle_arbeitstage}")
    print(f"Alle Wochenenden: {alle_wochenenden}")

    # Step-Parameter nutzen
    jeden_zweiten_tag = produktionsdaten[::2]  # Tag 0, 2, 4, 6, 8, 10, 12
    jeden_dritten_tag = produktionsdaten[::3]  # Tag 0, 3, 6, 9, 12
    rueckwaerts = produktionsdaten[::-1]  # Komplett umgekehrt

    print(f"\nJeden 2. Tag: {jeden_zweiten_tag}")
    print(f"Jeden 3. Tag: {jeden_dritten_tag}")
    print(f"Rückwärts: {rueckwaerts}")

    # Mittlerer Bereich extrahieren
    mittlere_woche = produktionsdaten[3:11]  # Tag 3-10 (Donnerstag bis Donnerstag)
    print(f"Mittlere Woche: {mittlere_woche}")

    # TODO: Ergänze:
    # - Erste und letzte 3 Tage kombinieren
    # - Nur ungerade Tage (1, 3, 5, ...)
    # - Komplexere Slicing-Muster

    return produktionsdaten, woche_1, woche_2


def aufgabe_3_2d_indexing():
    """
    Fast vollständige Lösung für Aufgabe 3: 2D Array Indexing
    """
    print("\n=== Aufgabe 3: 2D Array Indexing ===")

    # Qualitätsmessungen: 5 Maschinen × 8 Stunden pro Tag
    qualitaetsdaten = np.array(
        [
            [98.5, 99.1, 97.8, 98.9, 99.2, 98.7, 99.0, 98.4],  # Maschine 1
            [97.9, 98.8, 99.3, 99.0, 98.6, 99.4, 98.1, 99.2],  # Maschine 2
            [98.1, 99.2, 97.5, 98.3, 99.1, 98.8, 99.5, 98.7],  # Maschine 3
            [99.0, 98.7, 99.5, 98.9, 99.3, 99.1, 98.2, 99.4],  # Maschine 4
            [98.3, 99.0, 98.6, 99.1, 98.8, 99.2, 98.9, 99.3],  # Maschine 5
        ]
    )

    print(f"Qualitätsdaten (5 Maschinen × 8 Stunden):\n{qualitaetsdaten}")
    print(f"Shape: {qualitaetsdaten.shape}")

    # Einzelne Elemente zugreifen [zeile, spalte]
    maschine_1_stunde_3 = qualitaetsdaten[0, 3]  # 98.9
    maschine_3_letzte_stunde = qualitaetsdaten[2, -1]  # 98.7
    mittlere_maschine_mittag = qualitaetsdaten[2, 4]  # 99.1

    print("\nEinzelzugriffe:")
    print(f"Maschine 1, Stunde 3: {maschine_1_stunde_3}%")
    print(f"Maschine 3, letzte Stunde: {maschine_3_letzte_stunde}%")
    print(f"Mittlere Maschine, Mittag: {mittlere_maschine_mittag}%")

    # Ganze Zeilen (Maschinen)
    maschine_1_komplett = qualitaetsdaten[0, :]  # Ganze erste Zeile
    maschine_3_komplett = qualitaetsdaten[2]  # Vereinfachte Syntax
    letzte_maschine = qualitaetsdaten[-1, :]  # Letzte Zeile

    print(f"\nMaschine 1 (ganzer Tag): {maschine_1_komplett}")
    print(f"Maschine 3 (ganzer Tag): {maschine_3_komplett}")
    print(f"Letzte Maschine: {letzte_maschine}")

    # Ganze Spalten (Stunden)
    erste_stunde = qualitaetsdaten[:, 0]  # Alle Maschinen, erste Stunde
    mittags_stunde = qualitaetsdaten[:, 4]  # Alle Maschinen, Stunde 4
    letzte_stunde = qualitaetsdaten[:, -1]  # Alle Maschinen, letzte Stunde

    print(f"\nErste Stunde (alle Maschinen): {erste_stunde}")
    print(f"Mittags-Stunde (alle Maschinen): {mittags_stunde}")
    print(f"Letzte Stunde (alle Maschinen): {letzte_stunde}")

    # Submatrizen extrahieren
    erste_drei_maschinen = qualitaetsdaten[:3, :]  # Erste 3 Zeilen, alle Spalten
    letzte_vier_stunden = qualitaetsdaten[:, -4:]  # Alle Zeilen, letzte 4 Spalten
    mittlerer_block = qualitaetsdaten[1:4, 2:6]  # 3×4 Block in der Mitte

    print(f"\nErste 3 Maschinen:\n{erste_drei_maschinen}")
    print(f"Letzte 4 Stunden:\n{letzte_vier_stunden}")
    print(f"Mittlerer Block (3×4):\n{mittlerer_block}")

    # TODO: Ergänze:
    # - Schichtweise Auswertung (Früh/Spät/Nacht)
    # - Diagonal-Elemente extrahieren
    # - Ecken der Matrix

    return qualitaetsdaten


def aufgabe_4_boolean_indexing():
    """
    Fast vollständige Lösung für Aufgabe 4: Boolean Indexing
    """
    print("\n=== Aufgabe 4: Boolean Indexing ===")

    # Maschinendaten mit realistischen Schwankungen
    maschinendaten = np.array(
        [
            85.2,
            92.1,
            78.5,
            95.3,
            103.7,
            88.9,
            91.4,
            76.2,
            89.1,
            97.8,
            82.3,
            94.5,
            87.6,
            99.2,
            81.7,
            96.1,
        ]
    )

    print(f"Maschinendaten: {maschinendaten}")
    print(f"Anzahl Messwerte: {len(maschinendaten)}")

    # Sollbereich definieren (80-95)
    untere_grenze = 80
    obere_grenze = 95

    # Einfache Boolean-Bedingungen
    zu_niedrig = maschinendaten < untere_grenze
    zu_hoch = maschinendaten > obere_grenze
    im_sollbereich = (maschinendaten >= untere_grenze) & (
        maschinendaten <= obere_grenze
    )

    print("\nBoolean Arrays:")
    print(f"Zu niedrig (<{untere_grenze}): {zu_niedrig}")
    print(f"Zu hoch (>{obere_grenze}): {zu_hoch}")
    print(f"Im Sollbereich: {im_sollbereich}")

    # Gefilterte Werte extrahieren
    niedrige_werte = maschinendaten[zu_niedrig]
    hohe_werte = maschinendaten[zu_hoch]
    normale_werte = maschinendaten[im_sollbereich]

    print("\nGefilterte Werte:")
    print(f"Niedrige Werte: {niedrige_werte}")
    print(f"Hohe Werte: {hohe_werte}")
    print(f"Normale Werte: {normale_werte}")

    # Statistiken der Filtergruppen
    print("\nStatistiken:")
    print(f"Anzahl niedrige Werte: {len(niedrige_werte)}")
    print(f"Anzahl hohe Werte: {len(hohe_werte)}")
    print(f"Anzahl normale Werte: {len(normale_werte)}")
    print(
        f"Anteil im Sollbereich: {len(normale_werte) / len(maschinendaten) * 100:.1f}%"
    )

    # Indizes der problematischen Werte
    indizes_niedrig = np.where(zu_niedrig)[0]
    indizes_hoch = np.where(zu_hoch)[0]

    print("\nProblematische Indizes:")
    print(f"Zu niedrig bei Indizes: {indizes_niedrig}")
    print(f"Zu hoch bei Indizes: {indizes_hoch}")

    # Komplexere Bedingungen
    extrem_problematisch = (maschinendaten < 75) | (maschinendaten > 100)
    grenzwertig = ((maschinendaten >= 75) & (maschinendaten < 80)) | (
        (maschinendaten > 95) & (maschinendaten <= 100)
    )

    print("\nErweiterte Klassifikation:")
    print(f"Extrem problematisch: {maschinendaten[extrem_problematisch]}")
    print(f"Grenzwertig: {maschinendaten[grenzwertig]}")

    # TODO: Ergänze:
    # - Aufeinanderfolgende problematische Werte finden
    # - Relative Schwellwerte (z.B. Mittelwert ± 2*Standardabweichung)
    # - Trend-basierte Bewertung

    return maschinendaten, normale_werte, [niedrige_werte, hohe_werte]


def aufgabe_5_fancy_indexing():
    """
    Fast vollständige Lösung für Aufgabe 5: Fancy Indexing
    """
    print("\n=== Aufgabe 5: Fancy Indexing ===")

    # Sensordaten von 12 Sensoren an verschiedenen Positionen
    sensordaten = np.array(
        [
            23.1,
            24.5,
            22.8,
            25.2,
            23.9,
            24.1,  # Sensoren 0-5
            22.5,
            23.7,
            24.8,
            23.3,
            25.1,
            22.9,  # Sensoren 6-11
        ]
    )

    print(f"Sensordaten (12 Sensoren): {sensordaten}")

    # Spezifische Sensoren nach Wichtigkeit
    kritische_sensoren = [1, 5, 8, 11]  # Indizes wichtiger Sensoren
    normale_sensoren = [0, 2, 3, 4, 6, 7, 9, 10]
    redundante_sensoren = [1, 8]  # Backup-Sensoren

    kritische_werte = sensordaten[kritische_sensoren]
    normale_werte = sensordaten[normale_sensoren]

    print("\nSensor-Kategorien:")
    print(f"Kritische Sensoren {kritische_sensoren}: {kritische_werte}")
    print(f"Normale Sensoren: {normale_werte}")

    # Dynamisches Fancy Indexing
    # Finde die 5 höchsten und 3 niedrigsten Werte
    sortierte_indizes = np.argsort(sensordaten)
    niedrigste_3_indizes = sortierte_indizes[:3]
    hoechste_5_indizes = sortierte_indizes[-5:]

    print("\nDynamische Auswahl:")
    print(f"Niedrigste 3 Indizes: {niedrigste_3_indizes}")
    print(f"Niedrigste 3 Werte: {sensordaten[niedrigste_3_indizes]}")
    print(f"Höchste 5 Indizes: {hoechste_5_indizes}")
    print(f"Höchste 5 Werte: {sensordaten[hoechste_5_indizes]}")

    # Fancy Indexing mit 2D Arrays
    sensormatrix = sensordaten.reshape(3, 4)  # 3×4 Matrix
    print(f"\nSensormatrix (3×4):\n{sensormatrix}")

    # Spezifische Positionen auswählen
    zeilen_indizes = [0, 1, 2, 1]
    spalten_indizes = [1, 3, 0, 2]

    ausgewaehlte_positionen = sensormatrix[zeilen_indizes, spalten_indizes]
    print(
        f"Ausgewählte Positionen {list(zip(zeilen_indizes, spalten_indizes, strict=False))}: {ausgewaehlte_positionen}"
    )

    # Mehrere Zeilen/Spalten gleichzeitig
    ausgewaehlte_zeilen = [0, 2]  # Erste und dritte Zeile
    ausgewaehlte_spalten = [1, 3]  # Zweite und vierte Spalte

    submatrix = sensormatrix[np.ix_(ausgewaehlte_zeilen, ausgewaehlte_spalten)]
    print(
        f"Submatrix (Zeilen {ausgewaehlte_zeilen}, Spalten {ausgewaehlte_spalten}):\n{submatrix}"
    )

    # TODO: Ergänze:
    # - Zufällige Sensor-Stichprobe
    # - Clustering-basierte Auswahl
    # - Time-series Sampling

    return sensordaten, kritische_werte, sensormatrix


def bonus_erweiterte_techniken():
    """
    Bonus: Erweiterte Indexing-Techniken
    """
    print("\n=== Bonus: Erweiterte Techniken ===")

    # 3D Array für mehrtägige Daten (3 Tage × 4 Maschinen × 6 Stunden)
    mehrtaegige_daten = np.random.normal(98, 2, (3, 4, 6))
    print(f"3D Daten Shape: {mehrtaegige_daten.shape}")

    # Komplexes 3D Slicing
    tag_2_maschine_3 = mehrtaegige_daten[1, 2, :]  # Tag 2, Maschine 3, alle Stunden
    alle_tage_stunde_4 = mehrtaegige_daten[
        :, :, 3
    ]  # Alle Tage, alle Maschinen, Stunde 4

    print(f"Tag 2, Maschine 3: {tag_2_maschine_3}")
    print(f"Alle Tage, Stunde 4:\n{alle_tage_stunde_4}")

    # Kombiniertes Boolean und Fancy Indexing
    daten_1d = np.array([85, 92, 78, 95, 103, 88, 91, 76, 89, 97])

    # Finde Indizes von Werten >90, dann wähle jeden zweiten
    hohe_indizes = np.where(daten_1d > 90)[0]
    jeden_zweiten_hohen = hohe_indizes[::2]

    print(f"Hohe Werte (>90) bei Indizes: {hohe_indizes}")
    print(f"Jeden 2. hohen Wert: {daten_1d[jeden_zweiten_hohen]}")

    # View vs. Copy Demonstration
    original = np.array([1, 2, 3, 4, 5])
    view_slice = original[1:4]  # Slice = View
    copy_fancy = original[[1, 2, 3]]  # Fancy Indexing = Copy

    print("\nView vs. Copy Test:")
    print(f"Original: {original}")
    print(f"View (Slice): {view_slice}")
    print(f"Copy (Fancy): {copy_fancy}")

    # Änderung im View verändert Original
    view_slice[0] = 999
    print(f"Nach View-Änderung - Original: {original}")  # [1, 999, 3, 4, 5]

    # Änderung in Copy verändert Original NICHT
    copy_fancy[0] = 888
    print(f"Nach Copy-Änderung - Original: {original}")  # Unverändert


def vollstaendige_demo():
    """
    Führe alle Aufgaben in der richtigen Reihenfolge aus
    """
    print("🔍 NumPy Indexing & Slicing - Fast vollständige Lösung")
    print("=" * 70)

    # Alle Aufgaben durchführen
    temperaturen = aufgabe_1_einfaches_indexing()
    produktionsdaten, w1, w2 = aufgabe_2_array_slicing()
    qualitaetsdaten = aufgabe_3_2d_indexing()
    maschinendaten, normale, problematische = aufgabe_4_boolean_indexing()
    sensordaten, kritische, matrix = aufgabe_5_fancy_indexing()

    # Bonus-Material
    bonus_erweiterte_techniken()

    print("\n✅ Alle Indexing & Slicing Aufgaben demonstriert!")
    print("💡 Vervollständige die TODO-Bereiche für deine eigene Lösung.")


if __name__ == "__main__":
    vollstaendige_demo()

"""
📝 ANLEITUNG ZUR VERVOLLSTÄNDIGUNG:

1. Führe dieses Skript aus um die Grundfunktionalität zu sehen
2. Gehe durch jeden TODO-Bereich und implementiere die Ergänzungen
3. Experimentiere mit verschiedenen Slicing-Mustern
4. Teste Edge-Cases (leere Slices, out-of-bounds, etc.)
5. Erweitere um industrielle Anwendungsfälle

🎯 LERNZIELE ERREICHT?
☐ Einfaches Indexing mit positiven und negativen Indizes
☐ Array Slicing mit start:stop:step Syntax
☐ 2D Array Indexing und Submatrix-Extraktion
☐ Boolean Indexing für Datenfilterung
☐ Fancy Indexing mit Index-Arrays
☐ Unterschied zwischen Views und Copies verstehen
☐ Kombinierte Indexing-Techniken anwenden
"""
