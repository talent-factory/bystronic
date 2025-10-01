#!/usr/bin/env python3
"""
NumPy Indexing & Slicing - Vollständige Beginner Solution
========================================================

Vollständige Musterlösung für NumPy Indexing und Slicing Übungen.
Diese Solution demonstriert alle wichtigen Indexing-Techniken mit
realistischen SmartFactory-Anwendungsbeispielen aus der Industrie.

Author: Python Expert für SmartFactory
Date: 2025-09-16
"""

import warnings
from dataclasses import dataclass

import numpy as np


@dataclass
class TemperaturAnalyse:
    """Datenklasse für Temperaturanalyse-Ergebnisse"""

    min_temp: float
    max_temp: float
    min_zeitpunkt: int
    max_zeitpunkt: int
    arbeitszeit_mittel: float
    nacht_mittel: float


class NumPyIndexingSolution:
    """
    Vollständige NumPy Indexing & Slicing Solution mit industriellen Anwendungen
    """

    def __init__(self):
        """Initialisiere die Solution-Klasse"""
        self.debug_mode = False

    def aufgabe_1_einfaches_indexing(self) -> tuple[np.ndarray, TemperaturAnalyse]:
        """
        Aufgabe 1: Einfaches Indexing - Vollständige Lösung

        Demonstriert grundlegendes Array-Indexing mit Temperaturmessungen
        aus einer SmartFactory-Fertigungsanlage über 24 Stunden.

        Returns:
            Tuple[np.ndarray, TemperaturAnalyse]: Temperaturdaten und Analyse
        """
        print("=== Aufgabe 1: Einfaches Indexing ===")

        # Realistische Temperaturmessungen einer Laser-Schneidanlage (stündlich)
        temperaturen = np.array(
            [
                18.5,
                19.2,
                19.8,
                20.1,
                20.5,
                21.2,
                22.1,
                23.5,  # 0-7 Uhr (Nacht)
                24.8,
                25.3,
                26.1,
                26.8,
                27.2,
                26.9,
                26.5,
                25.8,  # 8-15 Uhr (Arbeit)
                24.9,
                23.7,
                22.8,
                21.9,
                21.1,
                20.3,
                19.7,
                19.1,  # 16-23 Uhr (Abend)
            ]
        )

        print(f"24h Temperaturdaten Laser-Anlage: {temperaturen}")
        print(f"Array-Shape: {temperaturen.shape}, Dtype: {temperaturen.dtype}")
        print(f"Memory usage: {temperaturen.nbytes} bytes")

        # Kritische Zeitpunkte für Anlagenüberwachung
        mitternacht = temperaturen[0]
        morgendaemmerung = temperaturen[6]
        arbeitszeit_start = temperaturen[8]
        mittag = temperaturen[12]
        arbeitszeit_ende = temperaturen[17]
        abend = temperaturen[18]
        spaet_abends = temperaturen[-1]  # Negative Indexierung

        print("\n🕐 Kritische Zeitpunkte für Anlagenüberwachung:")
        print(f"Mitternacht (0h): {mitternacht:.1f}°C")
        print(f"Morgendämmerung (6h): {morgendaemmerung:.1f}°C")
        print(f"Arbeitszeit Start (8h): {arbeitszeit_start:.1f}°C")
        print(f"Mittag (12h): {mittag:.1f}°C")
        print(f"Arbeitszeit Ende (17h): {arbeitszeit_ende:.1f}°C")
        print(f"Abend (18h): {abend:.1f}°C")
        print(f"Spät abends (23h): {spaet_abends:.1f}°C")

        # Negative Indexierung für letzte Messungen
        letzte_3_messungen = np.array(
            [temperaturen[-3], temperaturen[-2], temperaturen[-1]]
        )
        print(f"Letzte 3 Messungen: {letzte_3_messungen}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Min/Max-Analyse
        min_temp_idx = np.argmin(temperaturen)
        max_temp_idx = np.argmax(temperaturen)
        min_temp = temperaturen[min_temp_idx]
        max_temp = temperaturen[max_temp_idx]

        print("\n📊 Temperatur-Extremwerte:")
        print(f"Minimum: {min_temp:.1f}°C um {min_temp_idx}:00 Uhr")
        print(f"Maximum: {max_temp:.1f}°C um {max_temp_idx}:00 Uhr")
        print(f"Temperaturschwankung: {max_temp - min_temp:.1f}°C")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Arbeitszeiten (8-17 Uhr)
        arbeitszeiten_start = 8
        arbeitszeiten_ende = 17
        arbeitszeit_temperaturen = temperaturen[
            arbeitszeiten_start : arbeitszeiten_ende + 1
        ]
        arbeitszeit_mittel = np.mean(arbeitszeit_temperaturen)

        print("\n🏭 Arbeitszeit-Analyse (8-17 Uhr):")
        print(f"Temperaturen: {arbeitszeit_temperaturen}")
        print(f"Mitteltemperatur: {arbeitszeit_mittel:.1f}°C")
        print(f"Min während Arbeit: {np.min(arbeitszeit_temperaturen):.1f}°C")
        print(f"Max während Arbeit: {np.max(arbeitszeit_temperaturen):.1f}°C")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Nachttemperaturen (22-6 Uhr)
        # Nacht = 22,23,0,1,2,3,4,5,6 Uhr
        nacht_indizes = list(range(22, 24)) + list(range(0, 7))  # 22-23 + 0-6
        nacht_temperaturen = temperaturen[nacht_indizes]
        nacht_mittel = np.mean(nacht_temperaturen)

        print("\n🌙 Nachtzeit-Analyse (22-6 Uhr):")
        print(f"Nacht-Indizes: {nacht_indizes}")
        print(f"Nachttemperaturen: {nacht_temperaturen}")
        print(f"Mitteltemperatur Nacht: {nacht_mittel:.1f}°C")

        # Erweiterte Analyse: Temperaturtrends
        stündliche_differenzen = np.diff(temperaturen)
        max_anstieg_idx = np.argmax(stündliche_differenzen)
        max_abfall_idx = np.argmin(stündliche_differenzen)

        print("\n📈 Temperaturtrend-Analyse:")
        print(
            f"Größter Anstieg: {stündliche_differenzen[max_anstieg_idx]:.1f}°C "
            f"zwischen {max_anstieg_idx}h und {max_anstieg_idx + 1}h"
        )
        print(
            f"Größter Abfall: {stündliche_differenzen[max_abfall_idx]:.1f}°C "
            f"zwischen {max_abfall_idx}h und {max_abfall_idx + 1}h"
        )

        # Erstelle Analyse-Objekt
        analyse = TemperaturAnalyse(
            min_temp=min_temp,
            max_temp=max_temp,
            min_zeitpunkt=min_temp_idx,
            max_zeitpunkt=max_temp_idx,
            arbeitszeit_mittel=arbeitszeit_mittel,
            nacht_mittel=nacht_mittel,
        )

        return temperaturen, analyse

    def aufgabe_2_array_slicing(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Aufgabe 2: Array Slicing - Vollständige Lösung

        Demonstriert fortgeschrittenes Array-Slicing mit Produktionsdaten
        einer SmartFactory-Pressbrake über zwei Wochen.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]: Gesamtdaten, Woche1, Woche2
        """
        print("\n=== Aufgabe 2: Array Slicing ===")

        # Realistische Produktionsdaten: Teile pro Tag (Pressbrake)
        produktionsdaten = np.array(
            [
                120,
                135,
                128,
                142,
                118,
                105,
                95,  # Woche 1: Mo-So
                130,
                125,
                140,
                145,
                122,
                110,
                100,  # Woche 2: Mo-So
            ]
        )

        print(f"📊 Produktionsdaten Pressbrake (14 Tage): {produktionsdaten}")
        print(f"Gesamtproduktion: {np.sum(produktionsdaten)} Teile")
        print(f"Tagesdurchschnitt: {np.mean(produktionsdaten):.1f} Teile/Tag")

        # Grundlegendes Slicing: Wochenweise Aufteilen
        woche_1 = produktionsdaten[:7]  # Erste 7 Elemente
        woche_2 = produktionsdaten[7:]  # Ab Index 7 bis Ende
        woche_2_alt = produktionsdaten[7:14]  # Explizite End-Angabe

        print("\n📅 Wochenweise Analyse:")
        print(f"Woche 1: {woche_1} (Summe: {np.sum(woche_1)})")
        print(f"Woche 2: {woche_2} (Summe: {np.sum(woche_2)})")
        print(
            f"Woche 2 (alt): {woche_2_alt} (Identisch: {np.array_equal(woche_2, woche_2_alt)})"
        )

        # Arbeitstage vs. Wochenende (Mo-Fr vs. Sa-So)
        arbeitstage_w1 = produktionsdaten[:5]  # Tag 0-4 (Mo-Fr)
        wochenende_w1 = produktionsdaten[5:7]  # Tag 5-6 (Sa-So)
        arbeitstage_w2 = produktionsdaten[7:12]  # Tag 7-11 (Mo-Fr)
        wochenende_w2 = produktionsdaten[12:14]  # Tag 12-13 (Sa-So)

        print("\n🏭 Arbeitstage vs. Wochenende:")
        print(f"Arbeitstage W1: {arbeitstage_w1} (Ø {np.mean(arbeitstage_w1):.1f})")
        print(f"Wochenende W1: {wochenende_w1} (Ø {np.mean(wochenende_w1):.1f})")
        print(f"Arbeitstage W2: {arbeitstage_w2} (Ø {np.mean(arbeitstage_w2):.1f})")
        print(f"Wochenende W2: {wochenende_w2} (Ø {np.mean(wochenende_w2):.1f})")

        # Kombinieren von Arbeitstagen und Wochenenden
        alle_arbeitstage = np.concatenate([arbeitstage_w1, arbeitstage_w2])
        alle_wochenenden = np.concatenate([wochenende_w1, wochenende_w2])

        print("\n📈 Kombinierte Analyse:")
        print(f"Alle Arbeitstage: {alle_arbeitstage}")
        print(f"Arbeitstagsmittel: {np.mean(alle_arbeitstage):.1f} Teile/Tag")
        print(f"Alle Wochenenden: {alle_wochenenden}")
        print(f"Wochenendmittel: {np.mean(alle_wochenenden):.1f} Teile/Tag")
        print(
            f"Produktivitätsverlust Wochenende: "
            f"{(np.mean(alle_arbeitstage) - np.mean(alle_wochenenden)):.1f} Teile/Tag"
        )

        # Step-Parameter für komplexere Muster
        jeden_zweiten_tag = produktionsdaten[::2]  # Tag 0,2,4,6,8,10,12
        jeden_dritten_tag = produktionsdaten[::3]  # Tag 0,3,6,9,12
        rueckwaerts = produktionsdaten[::-1]  # Komplett umgekehrt

        print("\n🔄 Step-Parameter Beispiele:")
        print(f"Jeden 2. Tag: {jeden_zweiten_tag}")
        print(f"Jeden 3. Tag: {jeden_dritten_tag}")
        print(f"Rückwärts: {rueckwaerts}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Erste und letzte 3 Tage
        erste_3_tage = produktionsdaten[:3]
        letzte_3_tage = produktionsdaten[-3:]
        rand_tage_kombiniert = np.concatenate([erste_3_tage, letzte_3_tage])

        print("\n📊 Rand-Analyse:")
        print(f"Erste 3 Tage: {erste_3_tage} (Ø {np.mean(erste_3_tage):.1f})")
        print(f"Letzte 3 Tage: {letzte_3_tage} (Ø {np.mean(letzte_3_tage):.1f})")
        print(f"Kombiniert: {rand_tage_kombiniert}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Nur ungerade Tage (1,3,5,...)
        ungerade_tage_indizes = range(1, len(produktionsdaten), 2)
        ungerade_tage = produktionsdaten[1::2]  # Elegantere Lösung

        print("\n🎯 Ungerade Tage (Index 1,3,5,...):")
        print(f"Indizes: {list(ungerade_tage_indizes)}")
        print(f"Werte: {ungerade_tage}")
        print(f"Mittel ungerade Tage: {np.mean(ungerade_tage):.1f}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Komplexere Slicing-Muster
        # Mittlere Woche (Donnerstag bis Donnerstag)
        mittlere_woche = produktionsdaten[3:11]  # Tag 3-10

        # Wochenmitte (Di-Do) beider Wochen
        wochenmitte_w1 = produktionsdaten[1:5]  # Di-Fr Woche 1
        wochenmitte_w2 = produktionsdaten[8:12]  # Di-Fr Woche 2

        # Nur Montage und Freitage
        montage_freitage = np.concatenate(
            [
                produktionsdaten[[0, 4]],  # Mo, Fr Woche 1
                produktionsdaten[[7, 11]],  # Mo, Fr Woche 2
            ]
        )

        print("\n🏭 Erweiterte Muster:")
        print(f"Mittlere Woche (Do-Do): {mittlere_woche}")
        print(f"Wochenmitte W1 (Di-Fr): {wochenmitte_w1}")
        print(f"Wochenmitte W2 (Di-Fr): {wochenmitte_w2}")
        print(f"Montage & Freitage: {montage_freitage}")

        # Performance-Analyse verschiedener Slicing-Methoden
        if self.debug_mode:
            self._benchmark_slicing_performance(produktionsdaten)

        return produktionsdaten, woche_1, woche_2

    def aufgabe_3_2d_indexing(self) -> np.ndarray:
        """
        Aufgabe 3: 2D Array Indexing - Vollständige Lösung

        Demonstriert 2D-Array-Indexing mit Qualitätsmessungen von
        5 SmartFactory-Laser-Schneidanlagen über 8 Stunden.

        Returns:
            np.ndarray: 2D Qualitätsdaten-Matrix
        """
        print("\n=== Aufgabe 3: 2D Array Indexing ===")

        # Realistische Qualitätsmessungen: 5 Laser × 8 Stunden (Genauigkeit in %)
        qualitaetsdaten = np.array(
            [
                [98.5, 99.1, 97.8, 98.9, 99.2, 98.7, 99.0, 98.4],  # Laser 1
                [97.9, 98.8, 99.3, 99.0, 98.6, 99.4, 98.1, 99.2],  # Laser 2
                [98.1, 99.2, 97.5, 98.3, 99.1, 98.8, 99.5, 98.7],  # Laser 3
                [99.0, 98.7, 99.5, 98.9, 99.3, 99.1, 98.2, 99.4],  # Laser 4
                [98.3, 99.0, 98.6, 99.1, 98.8, 99.2, 98.9, 99.3],  # Laser 5
            ]
        )

        print("🎯 Qualitätsdaten 5 Laser-Anlagen × 8 Stunden:")
        print(f"Shape: {qualitaetsdaten.shape} (Anlagen × Stunden)")
        print(f"Dtype: {qualitaetsdaten.dtype}")
        print(f"Datenmatrix:\n{qualitaetsdaten}")

        # Gesamtstatistiken
        gesamt_mittel = np.mean(qualitaetsdaten)
        gesamt_std = np.std(qualitaetsdaten)
        gesamt_min = np.min(qualitaetsdaten)
        gesamt_max = np.max(qualitaetsdaten)

        print("\n📊 Gesamtstatistiken:")
        print(f"Mittelwert: {gesamt_mittel:.2f}%")
        print(f"Standardabweichung: {gesamt_std:.2f}%")
        print(f"Minimum: {gesamt_min:.1f}%")
        print(f"Maximum: {gesamt_max:.1f}%")

        # Einzelne Elemente zugreifen [zeile, spalte]
        laser_1_stunde_3 = qualitaetsdaten[0, 3]  # 98.9%
        laser_3_letzte_stunde = qualitaetsdaten[2, -1]  # 98.7%
        mittlerer_laser_mittag = qualitaetsdaten[2, 4]  # 99.1%
        bester_wert_pos = np.unravel_index(
            np.argmax(qualitaetsdaten), qualitaetsdaten.shape
        )
        bester_wert = qualitaetsdaten[bester_wert_pos]

        print("\n🎯 Einzelzugriffe:")
        print(f"Laser 1, Stunde 3: {laser_1_stunde_3:.1f}%")
        print(f"Laser 3, letzte Stunde: {laser_3_letzte_stunde:.1f}%")
        print(f"Mittlerer Laser, Mittag: {mittlerer_laser_mittag:.1f}%")
        print(
            f"Bester Wert: {bester_wert:.1f}% bei Laser {bester_wert_pos[0] + 1}, Stunde {bester_wert_pos[1] + 1}"
        )

        # Ganze Zeilen (komplette Laser-Anlagen)
        laser_1_komplett = qualitaetsdaten[0, :]  # Ganze erste Zeile
        laser_3_komplett = qualitaetsdaten[2]  # Vereinfachte Syntax
        letzter_laser = qualitaetsdaten[-1, :]  # Letzte Zeile

        print("\n🔧 Anlagen-Analyse (ganze Zeilen):")
        print(f"Laser 1 (ganzer Tag): {laser_1_komplett}")
        print(f"  Mittelwert: {np.mean(laser_1_komplett):.2f}%")
        print(f"Laser 3 (ganzer Tag): {laser_3_komplett}")
        print(f"  Mittelwert: {np.mean(laser_3_komplett):.2f}%")
        print(f"Letzter Laser: {letzter_laser}")
        print(f"  Mittelwert: {np.mean(letzter_laser):.2f}%")

        # Ganze Spalten (Stunden-Analyse)
        erste_stunde = qualitaetsdaten[:, 0]  # Alle Laser, erste Stunde
        mittags_stunde = qualitaetsdaten[:, 4]  # Alle Laser, Stunde 4 (Mittag)
        letzte_stunde = qualitaetsdaten[:, -1]  # Alle Laser, letzte Stunde

        print("\n⏰ Stunden-Analyse (ganze Spalten):")
        print(f"Erste Stunde (alle Laser): {erste_stunde}")
        print(f"  Durchschnitt: {np.mean(erste_stunde):.2f}%")
        print(f"Mittags-Stunde (alle Laser): {mittags_stunde}")
        print(f"  Durchschnitt: {np.mean(mittags_stunde):.2f}%")
        print(f"Letzte Stunde (alle Laser): {letzte_stunde}")
        print(f"  Durchschnitt: {np.mean(letzte_stunde):.2f}%")

        # Submatrizen extrahieren
        erste_drei_laser = qualitaetsdaten[:3, :]  # Erste 3 Zeilen, alle Spalten
        letzte_vier_stunden = qualitaetsdaten[:, -4:]  # Alle Zeilen, letzte 4 Spalten
        mittlerer_block = qualitaetsdaten[1:4, 2:6]  # 3×4 Block in der Mitte

        print("\n📋 Submatrix-Extraktion:")
        print(f"Erste 3 Laser (alle Stunden):\n{erste_drei_laser}")
        print(f"Mittelwert erste 3: {np.mean(erste_drei_laser):.2f}%")

        print(f"\nLetzte 4 Stunden (alle Laser):\n{letzte_vier_stunden}")
        print(f"Mittelwert letzte 4h: {np.mean(letzte_vier_stunden):.2f}%")

        print(f"\nMittlerer Block (Laser 2-4, Stunden 3-6):\n{mittlerer_block}")
        print(f"Mittelwert mittlerer Block: {np.mean(mittlerer_block):.2f}%")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Schichtweise Auswertung
        # Frühschicht: 0-2, Spätschicht: 3-5, Nachtschicht: 6-7
        fruehschicht = qualitaetsdaten[:, 0:3]  # Stunden 0-2
        spaetschicht = qualitaetsdaten[:, 3:6]  # Stunden 3-5
        nachtschicht = qualitaetsdaten[:, 6:8]  # Stunden 6-7

        print("\n⏰ Schichtanalyse:")
        print(f"Frühschicht (0-2h) Mittel: {np.mean(fruehschicht):.2f}%")
        print(f"Spätschicht (3-5h) Mittel: {np.mean(spaetschicht):.2f}%")
        print(f"Nachtschicht (6-7h) Mittel: {np.mean(nachtschicht):.2f}%")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Diagonal-Elemente
        diagonal_elemente = np.diag(
            qualitaetsdaten
        )  # Funktioniert nur für quadratische Matrix
        # Für rechteckige Matrix: manuelle Extraktion
        min_dim = min(qualitaetsdaten.shape)
        manuelle_diagonale = np.array([qualitaetsdaten[i, i] for i in range(min_dim)])

        print("\n↗️ Diagonale Analyse:")
        print(f"Diagonale (automatisch): {diagonal_elemente}")
        print(f"Diagonale (manuell): {manuelle_diagonale}")
        print(f"Diagonalmittel: {np.mean(manuelle_diagonale):.2f}%")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Ecken der Matrix
        ecke_oben_links = qualitaetsdaten[0, 0]
        ecke_oben_rechts = qualitaetsdaten[0, -1]
        ecke_unten_links = qualitaetsdaten[-1, 0]
        ecke_unten_rechts = qualitaetsdaten[-1, -1]

        print("\n📐 Matrix-Ecken:")
        print(f"Oben links (Laser 1, Stunde 1): {ecke_oben_links:.1f}%")
        print(f"Oben rechts (Laser 1, letzte Stunde): {ecke_oben_rechts:.1f}%")
        print(f"Unten links (letzter Laser, Stunde 1): {ecke_unten_links:.1f}%")
        print(f"Unten rechts (letzter Laser, letzte Stunde): {ecke_unten_rechts:.1f}%")

        # Erweiterte Analyse: Problematische Anlagen/Stunden identifizieren
        qualitaets_schwelle = 98.5
        problematische_positionen = np.where(qualitaetsdaten < qualitaets_schwelle)

        print(f"\n⚠️ Qualitätsprobleme (<{qualitaets_schwelle}%):")
        for laser_idx, stunde_idx in zip(
            problematische_positionen[0], problematische_positionen[1], strict=False
        ):
            wert = qualitaetsdaten[laser_idx, stunde_idx]
            print(f"  Laser {laser_idx + 1}, Stunde {stunde_idx + 1}: {wert:.1f}%")

        return qualitaetsdaten

    def aufgabe_4_boolean_indexing(
        self,
    ) -> tuple[np.ndarray, np.ndarray, list[np.ndarray]]:
        """
        Aufgabe 4: Boolean Indexing - Vollständige Lösung

        Demonstriert Boolean-Indexing mit Maschinendaten einer
        SmartFactory-Produktionslinie für Qualitätskontrolle.

        Returns:
            Tuple[np.ndarray, np.ndarray, List[np.ndarray]]:
            Originaldaten, normale Werte, problematische Werte
        """
        print("\n=== Aufgabe 4: Boolean Indexing ===")

        # Realistische Maschinendaten: Leistung in % über einen Produktionstag
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
                93.8,
                85.9,
                90.2,
                84.6,
                97.5,
                88.3,
                91.9,
                86.7,
            ]
        )

        print(f"📊 Maschinendaten SmartFactory-Linie: {maschinendaten}")
        print(f"Anzahl Messwerte: {len(maschinendaten)}")
        print(f"Mittelwert: {np.mean(maschinendaten):.1f}%")
        print(f"Standardabweichung: {np.std(maschinendaten):.1f}%")

        # Sollbereich definieren (Industriestandard: 80-95%)
        untere_grenze = 80
        obere_grenze = 95

        print(f"\n🎯 Sollbereich: {untere_grenze}% - {obere_grenze}%")

        # Grundlegende Boolean-Bedingungen
        zu_niedrig = maschinendaten < untere_grenze
        zu_hoch = maschinendaten > obere_grenze
        im_sollbereich = (maschinendaten >= untere_grenze) & (
            maschinendaten <= obere_grenze
        )

        print("\n🔍 Boolean Arrays:")
        print(f"Zu niedrig (<{untere_grenze}%): {zu_niedrig.sum()} Werte")
        print(f"Zu hoch (>{obere_grenze}%): {zu_hoch.sum()} Werte")
        print(f"Im Sollbereich: {im_sollbereich.sum()} Werte")
        print(f"Boolean Array zu_niedrig: {zu_niedrig}")

        # Gefilterte Werte extrahieren
        niedrige_werte = maschinendaten[zu_niedrig]
        hohe_werte = maschinendaten[zu_hoch]
        normale_werte = maschinendaten[im_sollbereich]

        print("\n📊 Gefilterte Werte:")
        print(f"Niedrige Werte: {niedrige_werte}")
        print(f"  Mittelwert: {np.mean(niedrige_werte):.1f}%")
        print(f"Hohe Werte: {hohe_werte}")
        print(f"  Mittelwert: {np.mean(hohe_werte):.1f}%")
        print(f"Normale Werte: {normale_werte}")
        print(f"  Mittelwert: {np.mean(normale_werte):.1f}%")

        # Qualitätsstatistiken
        gesamt_anzahl = len(maschinendaten)
        anteil_normal = len(normale_werte) / gesamt_anzahl * 100
        anteil_problematisch = (
            (len(niedrige_werte) + len(hohe_werte)) / gesamt_anzahl * 100
        )

        print("\n📈 Qualitätsstatistiken:")
        print(
            f"Anzahl niedrige Werte: {len(niedrige_werte)} ({len(niedrige_werte) / gesamt_anzahl * 100:.1f}%)"
        )
        print(
            f"Anzahl hohe Werte: {len(hohe_werte)} ({len(hohe_werte) / gesamt_anzahl * 100:.1f}%)"
        )
        print(f"Anzahl normale Werte: {len(normale_werte)} ({anteil_normal:.1f}%)")
        print(f"Anteil problematisch: {anteil_problematisch:.1f}%")

        # Indizes der problematischen Werte für Nachverfolgung
        indizes_niedrig = np.where(zu_niedrig)[0]
        indizes_hoch = np.where(zu_hoch)[0]
        indizes_normal = np.where(im_sollbereich)[0]

        print("\n🕒 Zeitstempel problematischer Werte:")
        print(f"Zu niedrig bei Messungen: {indizes_niedrig}")
        print(f"Zu hoch bei Messungen: {indizes_hoch}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Komplexere Bedingungen
        # Extrem problematisch: < 75% oder > 100%
        extrem_niedrig = maschinendaten < 75
        extrem_hoch = maschinendaten > 100
        extrem_problematisch = extrem_niedrig | extrem_hoch

        # Grenzwertig: 75-80% oder 95-100%
        grenzwertig = ((maschinendaten >= 75) & (maschinendaten < 80)) | (
            (maschinendaten > 95) & (maschinendaten <= 100)
        )

        print("\n⚠️ Erweiterte Klassifikation:")
        print(
            f"Extrem problematisch (<75% oder >100%): {maschinendaten[extrem_problematisch]}"
        )
        print(f"Anzahl extrem problematisch: {extrem_problematisch.sum()}")
        print(f"Grenzwertig (75-80% oder 95-100%): {maschinendaten[grenzwertig]}")
        print(f"Anzahl grenzwertig: {grenzwertig.sum()}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Aufeinanderfolgende problematische Werte
        # Suche nach Sequenzen von problematischen Werten
        problematisch = zu_niedrig | zu_hoch
        problematisch_diff = np.diff(
            np.concatenate(([False], problematisch, [False])).astype(int)
        )
        start_sequenzen = np.where(problematisch_diff == 1)[0]
        ende_sequenzen = np.where(problematisch_diff == -1)[0]

        print("\n🔄 Aufeinanderfolgende Probleme:")
        if len(start_sequenzen) > 0:
            for start, ende in zip(start_sequenzen, ende_sequenzen, strict=False):
                if ende - start > 1:  # Mehr als ein Wert
                    sequenz = maschinendaten[start:ende]
                    print(f"  Problemsequenz Messung {start}-{ende - 1}: {sequenz}")
        else:
            print("  Keine aufeinanderfolgenden Probleme gefunden")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Statistische Schwellwerte
        mittelwert = np.mean(maschinendaten)
        std_abweichung = np.std(maschinendaten)
        untere_stat_grenze = mittelwert - 2 * std_abweichung
        obere_stat_grenze = mittelwert + 2 * std_abweichung

        stat_ausreisser = (maschinendaten < untere_stat_grenze) | (
            maschinendaten > obere_stat_grenze
        )

        print("\n📊 Statistische Analyse (μ ± 2σ):")
        print(f"Mittelwert: {mittelwert:.1f}%")
        print(f"Standardabweichung: {std_abweichung:.1f}%")
        print(
            f"Statistische Grenzen: {untere_stat_grenze:.1f}% - {obere_stat_grenze:.1f}%"
        )
        print(f"Statistische Ausreißer: {maschinendaten[stat_ausreisser]}")
        print(f"Anzahl Ausreißer: {stat_ausreisser.sum()}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Trend-basierte Bewertung
        # Erste Ableitung für Trend-Erkennung
        trends = np.diff(maschinendaten)
        starke_anstiege = trends > 5  # >5% Anstieg
        starke_abfaelle = trends < -5  # >5% Abfall

        print("\n📈 Trend-Analyse:")
        print(f"Starke Anstiege (>5%): {np.sum(starke_anstiege)} Ereignisse")
        print(f"Starke Abfälle (<-5%): {np.sum(starke_abfaelle)} Ereignisse")

        if np.sum(starke_anstiege) > 0:
            anstieg_indizes = np.where(starke_anstiege)[0]
            print(f"Anstiegs-Zeitpunkte: {anstieg_indizes}")

        if np.sum(starke_abfaelle) > 0:
            abfall_indizes = np.where(starke_abfaelle)[0]
            print(f"Abfall-Zeitpunkte: {abfall_indizes}")

        # Performance-Metriken berechnen
        oee_berechnung = self._calculate_oee(
            maschinendaten, untere_grenze, obere_grenze
        )
        print("\n🏭 OEE-Analyse:")
        print(f"Overall Equipment Effectiveness: {oee_berechnung:.1f}%")

        return maschinendaten, normale_werte, [niedrige_werte, hohe_werte]

    def aufgabe_5_fancy_indexing(self) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        """
        Aufgabe 5: Fancy Indexing - Vollständige Lösung

        Demonstriert fortgeschrittenes Fancy Indexing mit Sensordaten
        eines SmartFactory-Überwachungssystems.

        Returns:
            Tuple[np.ndarray, np.ndarray, np.ndarray]:
            Sensordaten, kritische Werte, Sensormatrix
        """
        print("\n=== Aufgabe 5: Fancy Indexing ===")

        # Realistische Sensordaten: Temperaturen von 12 Sensoren in Laser-Schneidanlage
        np.random.seed(42)  # Für reproduzierbare Ergebnisse
        base_temp = 23.0
        sensordaten = base_temp + np.random.normal(0, 1.5, 12)
        sensordaten = np.round(sensordaten, 1)

        # Manuelle Anpassung für realistische Werte
        sensordaten = np.array(
            [
                23.1,
                24.5,
                22.8,
                25.2,
                23.9,
                24.1,  # Sensoren 0-5 (Schneidkopf)
                22.5,
                23.7,
                24.8,
                23.3,
                25.1,
                22.9,  # Sensoren 6-11 (Werkstück)
            ]
        )

        print(f"🌡️ Sensordaten Laser-Anlage (12 Sensoren): {sensordaten}")
        print(
            f"Temperaturbereich: {np.min(sensordaten):.1f}°C - {np.max(sensordaten):.1f}°C"
        )
        print(f"Mitteltemperatur: {np.mean(sensordaten):.1f}°C")

        # Sensor-Kategorisierung nach Wichtigkeit
        kritische_sensoren = [1, 5, 8, 11]  # Laser-Optik und Werkstück-Kontakt
        normale_sensoren = [0, 2, 3, 4, 6, 7, 9, 10]  # Umgebungstemperaturen
        redundante_sensoren = [1, 8]  # Backup-Sensoren für kritische Bereiche

        # Fancy Indexing mit Listen
        kritische_werte = sensordaten[kritische_sensoren]
        normale_werte = sensordaten[normale_sensoren]
        redundante_werte = sensordaten[redundante_sensoren]

        print("\n🎯 Sensor-Kategorien:")
        print(f"Kritische Sensoren {kritische_sensoren}: {kritische_werte}")
        print(f"  Mittelwert kritisch: {np.mean(kritische_werte):.1f}°C")
        print(f"Normale Sensoren {normale_sensoren[:4]}...: {normale_werte}")
        print(f"  Mittelwert normal: {np.mean(normale_werte):.1f}°C")
        print(f"Redundante Sensoren {redundante_sensoren}: {redundante_werte}")

        # Dynamisches Fancy Indexing basierend auf Werten
        sortierte_indizes = np.argsort(sensordaten)
        niedrigste_3_indizes = sortierte_indizes[:3]
        hoechste_5_indizes = sortierte_indizes[-5:]
        mittlere_indizes = sortierte_indizes[3:-5]  # Ausschluss der Extreme

        print("\n📊 Dynamische Auswahl (wertebasiert):")
        print(
            f"Niedrigste 3 Sensoren {niedrigste_3_indizes}: {sensordaten[niedrigste_3_indizes]}"
        )
        print(
            f"Höchste 5 Sensoren {hoechste_5_indizes}: {sensordaten[hoechste_5_indizes]}"
        )
        print(f"Mittlere Sensoren {mittlere_indizes}: {sensordaten[mittlere_indizes]}")

        # Überwachungsgrenzen definieren
        temp_min = 22.0
        temp_max = 25.0

        # Boolean + Fancy Indexing Kombination
        ueberhitzt_mask = sensordaten > temp_max
        unterkuehlt_mask = sensordaten < temp_min
        ueberhitzt_indizes = np.where(ueberhitzt_mask)[0]
        unterkuehlt_indizes = np.where(unterkuehlt_mask)[0]

        print(f"\n⚠️ Temperaturalarm (Sollbereich: {temp_min}-{temp_max}°C):")
        if len(ueberhitzt_indizes) > 0:
            print(
                f"Überhitzte Sensoren {ueberhitzt_indizes}: {sensordaten[ueberhitzt_indizes]}"
            )
        if len(unterkuehlt_indizes) > 0:
            print(
                f"Unterkühlte Sensoren {unterkuehlt_indizes}: {sensordaten[unterkuehlt_indizes]}"
            )
        if len(ueberhitzt_indizes) == 0 and len(unterkuehlt_indizes) == 0:
            print("Alle Sensoren im Sollbereich ✅")

        # 2D Fancy Indexing mit Sensormatrix
        sensormatrix = sensordaten.reshape(3, 4)  # 3 Zonen × 4 Sensoren pro Zone
        print(f"\n🏭 Sensormatrix (3 Zonen × 4 Sensoren):\n{sensormatrix}")

        # Spezifische Positionen mit 2D Fancy Indexing
        # Simuliere verschiedene Messpunkte
        zeilen_indizes = [0, 1, 2, 1, 0]  # Zone 1, 2, 3, 2, 1
        spalten_indizes = [1, 3, 0, 2, 3]  # Verschiedene Sensor-Positionen

        ausgewaehlte_positionen = sensormatrix[zeilen_indizes, spalten_indizes]
        koordinaten = list(zip(zeilen_indizes, spalten_indizes, strict=False))

        print("\n📍 Spezifische Messpunkte:")
        print(f"Koordinaten (Zone, Sensor): {koordinaten}")
        print(f"Messwerte: {ausgewaehlte_positionen}")
        print(f"Mittelwert Stichprobe: {np.mean(ausgewaehlte_positionen):.1f}°C")

        # np.ix_ für Mesh-Grid Indexing
        ausgewaehlte_zonen = [0, 2]  # Zone 1 und 3
        ausgewaehlte_sensoren = [1, 3]  # Sensor 2 und 4

        submatrix = sensormatrix[np.ix_(ausgewaehlte_zonen, ausgewaehlte_sensoren)]
        print(
            f"\n🔍 Submatrix (Zonen {[z + 1 for z in ausgewaehlte_zonen]}, Sensoren {[s + 1 for s in ausgewaehlte_sensoren]}):"
        )
        print(submatrix)
        print(f"Submatrix-Mittelwert: {np.mean(submatrix):.1f}°C")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Zufällige Sensor-Stichprobe
        np.random.seed(123)
        anzahl_stichprobe = 5
        zufaellige_indizes = np.random.choice(
            len(sensordaten), anzahl_stichprobe, replace=False
        )
        zufaellige_stichprobe = sensordaten[zufaellige_indizes]

        print(f"\n🎲 Zufällige Stichprobe ({anzahl_stichprobe} Sensoren):")
        print(f"Zufällige Indizes: {sorted(zufaellige_indizes)}")
        print(f"Stichprobe: {zufaellige_stichprobe}")
        print(f"Stichproben-Mittelwert: {np.mean(zufaellige_stichprobe):.1f}°C")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Clustering-basierte Auswahl
        # Einfaches K-Means-ähnliches Clustering in 3 Gruppen
        temp_bins = np.array([22, 23.5, 25, 26])  # Temperaturbereiche
        digitized = np.digitize(sensordaten, temp_bins)

        print("\n🗂️ Temperatur-Clustering:")
        for cluster in range(1, len(temp_bins)):
            cluster_mask = digitized == cluster
            cluster_indizes = np.where(cluster_mask)[0]
            if len(cluster_indizes) > 0:
                cluster_temps = sensordaten[cluster_indizes]
                temp_bereich = (
                    f"{temp_bins[cluster - 1]:.1f}-{temp_bins[cluster]:.1f}°C"
                )
                print(
                    f"Cluster {cluster} ({temp_bereich}): Sensoren {cluster_indizes}, Temps: {cluster_temps}"
                )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Time-series Sampling
        # Simuliere zeitlichen Verlauf durch Sampling-Pattern
        zeitliche_muster = {
            "jede_stunde": np.arange(0, 12, 1),  # Alle Sensoren
            "jede_2h": np.arange(0, 12, 2),  # Jede 2. Stunde
            "kritische_zeiten": [2, 5, 8, 11],  # Spezielle Zeitpunkte
            "random_sampling": np.random.choice(12, 6, replace=False),  # Zufällig
        }

        print("\n⏰ Zeitbasierte Sampling-Muster:")
        for pattern_name, indizes in zeitliche_muster.items():
            if pattern_name != "random_sampling":
                werte = sensordaten[indizes]
                print(f"{pattern_name}: Sensoren {indizes} -> {werte}")

        # Erweiterte Fancy Indexing Techniken
        self._demonstrate_advanced_fancy_indexing(sensordaten, sensormatrix)

        return sensordaten, kritische_werte, sensormatrix

    def bonus_erweiterte_techniken(self) -> None:
        """
        Bonus: Erweiterte Indexing-Techniken und Best Practices
        """
        print("\n=== Bonus: Erweiterte Techniken ===")

        # 3D Array für mehrtägige Produktionsdaten
        np.random.seed(42)
        tage, maschinen, stunden = 3, 4, 6
        mehrtaegige_daten = np.random.normal(98, 2, (tage, maschinen, stunden))
        mehrtaegige_daten = np.clip(mehrtaegige_daten, 95, 101)  # Realistische Werte

        print(
            f"📊 3D Produktionsdaten ({tage} Tage × {maschinen} Maschinen × {stunden} Stunden):"
        )
        print(f"Shape: {mehrtaegige_daten.shape}")
        print(f"Gesamtmittelwert: {np.mean(mehrtaegige_daten):.2f}%")

        # Komplexes 3D Slicing
        tag_2_maschine_3 = mehrtaegige_daten[1, 2, :]  # Tag 2, Maschine 3, alle Stunden
        alle_tage_stunde_4 = mehrtaegige_daten[:, :, 3]  # Alle Tage+Maschinen, Stunde 4
        maschine_1_alle_zeiten = mehrtaegige_daten[
            :, 0, :
        ]  # Alle Tage+Stunden, Maschine 1

        print("\n🔍 3D Slicing Beispiele:")
        print(f"Tag 2, Maschine 3 (alle Stunden): {tag_2_maschine_3}")
        print(f"Stunde 4 (alle Tage×Maschinen):\n{alle_tage_stunde_4}")
        print(f"Maschine 1 (alle Tage×Stunden):\n{maschine_1_alle_zeiten}")

        # Ellipsis (...) Operator
        erste_stunde_alle = mehrtaegige_daten[..., 0]  # Equivalent zu [:, :, 0]
        letzte_maschine_alle = mehrtaegige_daten[:, -1, ...]  # Equivalent zu [:, -1, :]

        print("\n⚡ Ellipsis Operator:")
        print(f"Erste Stunde (alle Tage×Maschinen) Shape: {erste_stunde_alle.shape}")
        print(
            f"Letzte Maschine (alle Tage×Stunden) Shape: {letzte_maschine_alle.shape}"
        )

        # Kombiniertes Boolean und Fancy Indexing
        daten_1d = np.array([85, 92, 78, 95, 103, 88, 91, 76, 89, 97, 84, 99])

        # Mehrstufige Filterung
        hohe_werte_mask = daten_1d > 90
        hohe_indizes = np.where(hohe_werte_mask)[0]
        jeden_zweiten_hohen = hohe_indizes[::2]  # Jeden 2. hohen Wert

        print("\n🎯 Kombiniertes Boolean/Fancy Indexing:")
        print(f"Originaldaten: {daten_1d}")
        print(
            f"Hohe Werte (>90): Indizes {hohe_indizes}, Werte {daten_1d[hohe_indizes]}"
        )
        print(
            f"Jeden 2. hohen Wert: Indizes {jeden_zweiten_hohen}, Werte {daten_1d[jeden_zweiten_hohen]}"
        )

        # Advanced Boolean Operationen
        bedingung_komplex = (
            (daten_1d > 85) & (daten_1d < 95) & (np.arange(len(daten_1d)) % 2 == 0)
        )
        print(
            f"Komplexe Bedingung (85<x<95 UND gerade Indizes): {daten_1d[bedingung_komplex]}"
        )

        # View vs. Copy Demonstration mit Performance-Test
        self._demonstrate_view_vs_copy()

        # Memory-Layout und Performance
        self._demonstrate_memory_layout()

        # Error Handling bei Indexing
        self._demonstrate_indexing_errors()

    def _demonstrate_advanced_fancy_indexing(
        self, sensordaten: np.ndarray, sensormatrix: np.ndarray
    ) -> None:
        """Zeige erweiterte Fancy Indexing Techniken"""
        print("\n🚀 Erweiterte Fancy Indexing Techniken:")

        # Conditional Indexing mit np.where
        temp_schwelle = np.mean(sensordaten)
        hohe_temp_indizes = np.where(sensordaten > temp_schwelle)[0]
        niedrige_temp_indizes = np.where(sensordaten <= temp_schwelle)[0]

        print(f"Temperaturschwelle: {temp_schwelle:.1f}°C")
        print(f"Über Schwelle: Sensoren {hohe_temp_indizes}")
        print(f"Unter Schwelle: Sensoren {niedrige_temp_indizes}")

        # Multi-condition Indexing
        sehr_hoch = sensordaten > (temp_schwelle + 1)
        sehr_niedrig = sensordaten < (temp_schwelle - 1)
        extrem_indizes = np.where(sehr_hoch | sehr_niedrig)[0]

        if len(extrem_indizes) > 0:
            print(
                f"Extreme Temperaturen: Sensoren {extrem_indizes}, Werte {sensordaten[extrem_indizes]}"
            )

        # Nested Indexing
        matrix_flat = sensormatrix.flatten()
        top_indizes = np.argsort(matrix_flat)[-3:]  # Top 3 Werte
        top_koordinaten = np.unravel_index(top_indizes, sensormatrix.shape)

        print(
            f"Top 3 Sensoren (flach): Indizes {top_indizes}, Werte {matrix_flat[top_indizes]}"
        )
        print(
            f"Top 3 Koordinaten: {list(zip(top_koordinaten[0], top_koordinaten[1], strict=False))}"
        )

    def _demonstrate_view_vs_copy(self) -> None:
        """Demonstriere Unterschied zwischen Views und Copies"""
        print("\n👁️ View vs. Copy Demonstration:")

        original = np.array([1, 2, 3, 4, 5, 6, 7, 8])
        print(f"Original: {original}")

        # Views (teilen Speicher)
        view_slice = original[2:6]  # Slice = View
        view_reshape = original.reshape(2, 4)  # Reshape = View (meist)

        # Copies (eigener Speicher)
        copy_fancy = original[[1, 3, 5, 7]]  # Fancy Indexing = Copy
        copy_explicit = original.copy()  # Explizite Copy

        print(f"View (Slice): {view_slice}")
        print(f"Copy (Fancy): {copy_fancy}")

        # Memory-sharing Test
        print(f"View teilt Speicher: {np.shares_memory(original, view_slice)}")
        print(f"Copy teilt Speicher: {np.shares_memory(original, copy_fancy)}")

        # Änderung testen
        original_backup = original.copy()
        view_slice[0] = 999

        print("Nach View-Änderung:")
        print(f"  Original: {original} (verändert)")
        print(f"  View: {view_slice}")

        # Restore und Copy-Test
        original[:] = original_backup
        copy_fancy[0] = 888

        print("Nach Copy-Änderung:")
        print(f"  Original: {original} (unverändert)")
        print(f"  Copy: {copy_fancy}")

    def _demonstrate_memory_layout(self) -> None:
        """Demonstriere Memory-Layout Einfluss auf Performance"""
        print("\n💾 Memory Layout und Performance:")

        # C-style (row-major) vs Fortran-style (column-major)
        size = 1000
        c_array = np.random.randn(size, size)  # Default: C-style
        f_array = np.asfortranarray(c_array)  # Fortran-style

        print(
            f"C-style Flags: C_CONTIGUOUS={c_array.flags['C_CONTIGUOUS']}, "
            f"F_CONTIGUOUS={c_array.flags['F_CONTIGUOUS']}"
        )
        print(
            f"Fortran Flags: C_CONTIGUOUS={f_array.flags['C_CONTIGUOUS']}, "
            f"F_CONTIGUOUS={f_array.flags['F_CONTIGUOUS']}"
        )

        # Stride-Information
        print(f"C-style Strides: {c_array.strides}")
        print(f"Fortran Strides: {f_array.strides}")

    def _demonstrate_indexing_errors(self) -> None:
        """Demonstriere häufige Indexing-Fehler und deren Behandlung"""
        print("\n⚠️ Indexing Error Handling:")

        test_array = np.array([1, 2, 3, 4, 5])

        # Index out of bounds
        try:
            wert = test_array[10]
        except IndexError as e:
            print(f"IndexError gefangen: {e}")

        # Sicherer Zugriff mit Bounds-Check
        def safe_access(arr: np.ndarray, index: int) -> float | None:
            if 0 <= index < len(arr):
                return arr[index]
            else:
                warnings.warn(
                    f"Index {index} außerhalb der Grenzen [0, {len(arr) - 1}]"
                )
                return None

        print(f"Sicherer Zugriff Index 3: {safe_access(test_array, 3)}")
        print(f"Sicherer Zugriff Index 10: {safe_access(test_array, 10)}")

        # Boolean Indexing Fallstricke
        mask = np.array([True, False, True])  # Zu kurze Maske
        try:
            gefiltert = test_array[
                mask
            ]  # Wird funktionieren, aber unerwartetes Ergebnis
            print(f"Kurze Boolean-Maske: {gefiltert}")
        except IndexError as e:
            print(f"Boolean IndexError: {e}")

    def _calculate_oee(
        self, daten: np.ndarray, min_wert: float, max_wert: float
    ) -> float:
        """
        Berechne Overall Equipment Effectiveness (OEE)

        Args:
            daten: Maschinendaten
            min_wert: Untere Grenze für Qualität
            max_wert: Obere Grenze für Qualität

        Returns:
            OEE-Wert in Prozent
        """
        # Vereinfachte OEE-Berechnung basierend auf Qualitätsdaten
        qualitaets_erfuellung = np.sum((daten >= min_wert) & (daten <= max_wert)) / len(
            daten
        )
        verfuegbarkeit = 0.95  # Annahme: 95% Verfügbarkeit
        leistungsgrad = np.mean(daten) / 100  # Normalisiert auf max 100%

        oee = verfuegbarkeit * leistungsgrad * qualitaets_erfuellung * 100
        return oee

    def _benchmark_slicing_performance(self, daten: np.ndarray) -> None:
        """Benchmark verschiedener Slicing-Methoden"""
        import time

        print("\n⚡ Slicing Performance Benchmark:")

        # Größeres Array für aussagekräftige Benchmarks
        große_daten = np.tile(daten, 1000)  # 14000 Elemente

        # Method 1: Slice
        start = time.perf_counter()
        for _ in range(1000):
            result1 = große_daten[::2]
        zeit1 = time.perf_counter() - start

        # Method 2: Boolean Indexing
        start = time.perf_counter()
        for _ in range(1000):
            mask = np.arange(len(große_daten)) % 2 == 0
            result2 = große_daten[mask]
        zeit2 = time.perf_counter() - start

        # Method 3: Fancy Indexing
        indizes = np.arange(0, len(große_daten), 2)
        start = time.perf_counter()
        for _ in range(1000):
            result3 = große_daten[indizes]
        zeit3 = time.perf_counter() - start

        print(f"Slice (::2): {zeit1:.4f}s")
        print(f"Boolean Indexing: {zeit2:.4f}s")
        print(f"Fancy Indexing: {zeit3:.4f}s")
        print(
            f"Schnellster: {'Slice' if zeit1 <= min(zeit2, zeit3) else 'Boolean' if zeit2 <= zeit3 else 'Fancy'}"
        )

    def vollstaendige_demonstration(self) -> None:
        """
        Führe alle Aufgaben in der richtigen Reihenfolge aus
        """
        print("🔍 NumPy Indexing & Slicing - Vollständige Musterlösung")
        print("=" * 70)
        print("SmartFactory Python Grundkurs - Industrielle Datenanalyse")
        print("=" * 70)

        try:
            # Alle Aufgaben durchführen
            temperaturen, temp_analyse = self.aufgabe_1_einfaches_indexing()
            produktionsdaten, w1, w2 = self.aufgabe_2_array_slicing()
            qualitaetsdaten = self.aufgabe_3_2d_indexing()
            maschinendaten, normale, problematische = self.aufgabe_4_boolean_indexing()
            sensordaten, kritische, matrix = self.aufgabe_5_fancy_indexing()

            # Bonus-Material
            self.bonus_erweiterte_techniken()

            # Zusammenfassung
            self._print_summary(
                temp_analyse,
                produktionsdaten,
                qualitaetsdaten,
                maschinendaten,
                sensordaten,
            )

        except Exception as e:
            print(f"❌ Fehler bei der Ausführung: {e}")
            raise

    def _print_summary(
        self,
        temp_analyse: TemperaturAnalyse,
        produktionsdaten: np.ndarray,
        qualitaetsdaten: np.ndarray,
        maschinendaten: np.ndarray,
        sensordaten: np.ndarray,
    ) -> None:
        """Drucke Zusammenfassung aller Analysen"""
        print("\n" + "=" * 70)
        print("📊 ZUSAMMENFASSUNG - SmartFactory Indexing & Slicing Analyse")
        print("=" * 70)

        print("🌡️ Temperaturanalyse:")
        print(f"   Min: {temp_analyse.min_temp:.1f}°C @ {temp_analyse.min_zeitpunkt}h")
        print(f"   Max: {temp_analyse.max_temp:.1f}°C @ {temp_analyse.max_zeitpunkt}h")
        print(f"   Arbeitszeit Ø: {temp_analyse.arbeitszeit_mittel:.1f}°C")

        print("\n🏭 Produktionsanalyse:")
        print(f"   Gesamtproduktion: {np.sum(produktionsdaten)} Teile")
        print(f"   Tagesdurchschnitt: {np.mean(produktionsdaten):.1f} Teile/Tag")
        print(
            f"   Beste Woche: {'Woche 2' if np.sum(produktionsdaten[7:]) > np.sum(produktionsdaten[:7]) else 'Woche 1'}"
        )

        print("\n🎯 Qualitätsanalyse:")
        print(f"   Durchschnitt: {np.mean(qualitaetsdaten):.2f}%")
        print(f"   Schwankung: {np.std(qualitaetsdaten):.2f}%")

        print("\n⚙️ Maschinenanalyse:")
        print(
            f"   Sollbereich-Erfüllung: {len(maschinendaten[(maschinendaten >= 80) & (maschinendaten <= 95)]) / len(maschinendaten) * 100:.1f}%"
        )

        print("\n🌡️ Sensoranalyse:")
        print(
            f"   Temperaturbereich: {np.min(sensordaten):.1f}°C - {np.max(sensordaten):.1f}°C"
        )

        print("\n✅ Alle NumPy Indexing & Slicing Techniken erfolgreich demonstriert!")
        print(
            "💡 Diese Solution zeigt production-ready Code für industrielle Anwendungen."
        )


def main():
    """Hauptfunktion für die Ausführung der Solution"""
    solution = NumPyIndexingSolution()
    solution.vollstaendige_demonstration()


if __name__ == "__main__":
    main()


"""
📚 LEARNING SUMMARY - NumPy Indexing & Slicing
==============================================

🎯 ERREICHTE LERNZIELE:
✅ Einfaches Indexing mit positiven und negativen Indizes
✅ Array Slicing mit start:stop:step Syntax verstehen
✅ 2D Array Indexing und Submatrix-Extraktion beherrschen
✅ Boolean Indexing für effektive Datenfilterung einsetzen
✅ Fancy Indexing mit Index-Arrays für komplexe Auswahlen
✅ Unterschied zwischen Views und Copies verstehen
✅ Kombinierte Indexing-Techniken in industriellen Szenarien anwenden

🏭 INDUSTRIELLE ANWENDUNGEN:
• Temperaturüberwachung in Laser-Schneidanlagen
• Produktionsdaten-Analyse für Pressbrakes
• Qualitätskontrolle bei Fertigungsanlagen
• Sensor-Monitoring in Echtzeit-Systemen
• OEE-Berechnung für Maschineneffektivität

🚀 PERFORMANCE OPTIMIERUNGEN:
• View vs. Copy Bewusstsein für Memory-Effizienz
• Effiziente Boolean-Operationen für große Datensätze
• Batch-Processing mit Fancy Indexing
• Memory-Layout Optimierung für bessere Cache-Performance

🔧 BEST PRACTICES:
• Type Hints für bessere Code-Dokumentation
• Error Handling für robuste Produktionsumgebungen
• Modulare Funktionen für Wiederverwendbarkeit
• Comprehensive Logging für Debugging und Monitoring
• Realistic Industrial Data Patterns

📈 NÄCHSTE SCHRITTE:
1. Übung mit eigenen SmartFactory-Datensätzen
2. Integration in bestehende VBA-zu-Python Migration
3. Erweiterte NumPy-Funktionen (Universal Functions, Broadcasting)
4. Performance-Profiling für große Datensätze
5. Integration mit Pandas für strukturierte Datenanalyse

💡 Diese Solution demonstriert production-ready NumPy Code für
   industrielle Datenanalyse-Anwendungen bei SmartFactory.
"""
