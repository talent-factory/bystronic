#!/usr/bin/env python3
"""
🟢 BEGINNER - Bystronic Python Grundkurs - Kapitel 3
Übung 2: Mathematische Operationen (Einsteigerfreundlich)

🎯 LERNZIELE (20-25 Minuten):
- Vektorisierte mathematische Operationen verstehen
- Grundlegende NumPy-Funktionen anwenden
- Statistische Berechnungen für Qualitätskontrolle
- Broadcasting-Grundlagen kennenlernen
- Praktische Anwendung für Produktionsdaten

📚 HILFSMITTEL:
- Hints: solutions/beginner/uebung_02_hints.md
- Skeleton: solutions/beginner/uebung_02_skeleton.py
- Partial: solutions/beginner/uebung_02_partial.py
- Complete: solutions/beginner/uebung_02_complete.py

🏭 BYSTRONIC-KONTEXT:
Mathematische Berechnungen für die Produktion:
Qualitätskontrolle, Effizienzberechnungen, Trendanalysen.
"""

import numpy as np


def aufgabe_1_grundrechenarten():
    """🎯 Aufgabe 1: Vektorisierte Grundrechenarten"""
    print("=" * 60)
    print("🟢 AUFGABE 1: Vektorisierte Grundrechenarten")
    print("=" * 60)

    # Produktionsdaten für 5 Maschinen
    stueckzahlen_tag1 = np.array([1200, 1150, 1380, 1090, 1250])
    stueckzahlen_tag2 = np.array([1180, 1200, 1420, 1100, 1280])
    maschinen = ["Laser_01", "Presse_02", "Stanze_03", "Biege_04", "Schweiss_05"]

    print("📊 Produktionsdaten (2 Tage, 5 Maschinen):")
    print(f"Tag 1: {stueckzahlen_tag1}")
    print(f"Tag 2: {stueckzahlen_tag2}")
    print()

    # TODO 1: Addition - Gesamtproduktion
    print("➕ Addition: Gesamtproduktion beider Tage")
    gesamtproduktion = stueckzahlen_tag1 + stueckzahlen_tag2
    print(f"Gesamt: {gesamtproduktion}")
    for i, maschine in enumerate(maschinen):
        print(f"   {maschine}: {gesamtproduktion[i]:,} Stück")
    print()

    # TODO 2: Subtraktion - Tägliche Veränderung
    print("➖ Subtraktion: Veränderung Tag 2 vs Tag 1")
    veraenderung = stueckzahlen_tag2 - stueckzahlen_tag1
    print(f"Veränderung: {veraenderung}")
    for i, maschine in enumerate(maschinen):
        if veraenderung[i] > 0:
            print(f"   {maschine}: +{veraenderung[i]} Stück ⬆️")
        elif veraenderung[i] < 0:
            print(f"   {maschine}: {veraenderung[i]} Stück ⬇️")
        else:
            print(f"   {maschine}: unverändert ➡️")
    print()

    # TODO 3: Multiplikation - Wochenproduktion hochrechnen
    print("✖️ Multiplikation: Wochenproduktion (5 Arbeitstage)")
    arbeitstage = 5
    wochenproduktion = gesamtproduktion / 2 * arbeitstage  # Durchschnitt * 5 Tage
    print(f"Hochrechnung: {wochenproduktion.astype(int)}")
    print(f"Wochensumme: {np.sum(wochenproduktion):,.0f} Stück")
    print()

    # TODO 4: Division - Stück pro Stunde
    print("➗ Division: Stück pro Stunde (8h Schichten)")
    arbeitsstunden = 8
    stueck_pro_stunde_tag1 = stueckzahlen_tag1 / arbeitsstunden
    stueck_pro_stunde_tag2 = stueckzahlen_tag2 / arbeitsstunden

    print("Produktivität (Stück/Stunde):")
    for i, maschine in enumerate(maschinen):
        print(
            f"   {maschine}: Tag1={stueck_pro_stunde_tag1[i]:.1f}, Tag2={stueck_pro_stunde_tag2[i]:.1f}"
        )
    print()

    print("✅ Aufgabe 1 abgeschlossen!")
    return gesamtproduktion, stueck_pro_stunde_tag1


def aufgabe_2_statistische_funktionen():
    """🎯 Aufgabe 2: Statistische NumPy-Funktionen"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 2: Statistische Funktionen")
    print("=" * 60)

    # Qualitätsmessungen einer Woche (7 Tage × 10 Messungen)
    np.random.seed(42)  # Für reproduzierbare Ergebnisse
    sollwert = 25.0  # mm
    messungen = np.random.normal(sollwert, 0.3, 70)  # 70 Messungen, Normalverteilt

    print(f"📏 Qualitätsmessungen: {len(messungen)} Werte (Sollwert: {sollwert} mm)")
    print(f"Erste 10 Werte: {messungen[:10].round(3)}")
    print()

    # TODO 1: Grundlegende Statistiken
    print("📊 Grundlegende Statistiken:")
    print(f"   Minimum: {np.min(messungen):.3f} mm")
    print(f"   Maximum: {np.max(messungen):.3f} mm")
    print(f"   Mittelwert: {np.mean(messungen):.3f} mm")
    print(f"   Median: {np.median(messungen):.3f} mm")
    print(
        f"   Standardabweichung: {np.std(messungen, ddof=1):.3f} mm"
    )  # ddof=1 für Stichprobe
    print(f"   Spannweite: {np.ptp(messungen):.3f} mm")  # ptp = peak-to-peak
    print()

    # TODO 2: Perzentile (Quartile)
    print("📈 Perzentile (Quartile):")
    p25 = np.percentile(messungen, 25)
    p50 = np.percentile(messungen, 50)  # = Median
    p75 = np.percentile(messungen, 75)
    print(f"   25. Perzentil (Q1): {p25:.3f} mm")
    print(f"   50. Perzentil (Q2): {p50:.3f} mm")
    print(f"   75. Perzentil (Q3): {p75:.3f} mm")
    print(f"   Interquartilsabstand: {p75 - p25:.3f} mm")
    print()

    # TODO 3: Qualitätsbewertung
    print("🎯 Qualitätsbewertung:")
    toleranz = 0.5  # ±0.5 mm

    # Boolean Array: Welche Messungen sind in Toleranz?
    in_toleranz = np.abs(messungen - sollwert) <= toleranz
    anzahl_ok = np.sum(in_toleranz)  # True wird als 1 gezählt
    ausschuss_rate = (1 - anzahl_ok / len(messungen)) * 100

    print(f"   Toleranz: ±{toleranz} mm")
    print(
        f"   In Toleranz: {anzahl_ok}/{len(messungen)} ({anzahl_ok / len(messungen) * 100:.1f}%)"
    )
    print(f"   Ausschussrate: {ausschuss_rate:.2f}%")
    print()

    # TODO 4: Prozessfähigkeit (vereinfacht)
    print("📊 Prozessfähigkeit (Cp-Wert):")
    sigma = np.std(messungen, ddof=1)
    cp_wert = (2 * toleranz) / (6 * sigma)  # Cp = Toleranzbreite / (6 × σ)

    print(f"   Standardabweichung: {sigma:.4f} mm")
    print(f"   Cp-Wert: {cp_wert:.3f}")

    if cp_wert >= 1.67:
        bewertung = "Sehr gut (6σ)"
    elif cp_wert >= 1.33:
        bewertung = "Gut (4σ)"
    elif cp_wert >= 1.0:
        bewertung = "Akzeptabel (3σ)"
    else:
        bewertung = "Ungenügend"

    print(f"   Bewertung: {bewertung}")
    print()

    print("✅ Aufgabe 2 abgeschlossen!")
    return messungen, cp_wert


def aufgabe_3_broadcasting():
    """🎯 Aufgabe 3: Broadcasting-Grundlagen"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 3: Broadcasting verstehen")
    print("=" * 60)

    # Produktionsdaten: 4 Maschinen × 5 Tage
    produktion = np.array(
        [
            [1200, 1180, 1250, 1190, 1220],  # Maschine 1
            [1100, 1150, 1120, 1080, 1140],  # Maschine 2
            [1350, 1380, 1400, 1360, 1390],  # Maschine 3
            [980, 1020, 990, 1010, 1000],  # Maschine 4
        ]
    )

    print("📊 Produktionsdaten (4 Maschinen × 5 Tage):")
    print(produktion)
    print(f"Shape: {produktion.shape}")
    print()

    # TODO 1: Skalar mit Array (Broadcasting)
    print("🎯 Broadcasting 1: Skalar mit Array")
    print("Alle Werte um 50 Stück erhöhen (Optimierung):")

    optimiert = (
        produktion + 50
    )  # Broadcasting: Skalar wird auf alle Elemente angewendet
    print("Vorher - Nachher Vergleich (erste Maschine):")
    print(f"   Vorher: {produktion[0]}")
    print(f"   Nachher: {optimiert[0]}")
    print()

    # TODO 2: 1D-Array mit 2D-Array (Broadcasting)
    print("🎯 Broadcasting 2: Tagesfaktoren anwenden")

    # Verschiedene Tagesfaktoren (Mo-Fr)
    tagesfaktoren = np.array([1.0, 0.95, 1.05, 0.98, 1.02])
    print(f"Tagesfaktoren: {tagesfaktoren}")
    print(f"Shape Produktion: {produktion.shape}")
    print(f"Shape Faktoren: {tagesfaktoren.shape}")

    # Broadcasting: (4,5) * (5,) = (4,5)
    angepasste_produktion = produktion * tagesfaktoren
    print("\nAngepasste Produktion (erste Maschine):")
    print(f"   Original: {produktion[0]}")
    print(f"   Angepasst: {angepasste_produktion[0].astype(int)}")
    print()

    # TODO 3: Maschinenfaktoren (Broadcasting anders herum)
    print("🎯 Broadcasting 3: Maschinenfaktoren")

    # Effizienzfaktoren pro Maschine
    maschinenfaktoren = np.array([1.05, 0.98, 1.10, 0.92])  # 4 Werte
    print(f"Maschinenfaktoren: {maschinenfaktoren}")

    # Reshape für Broadcasting: (4,) → (4,1)
    maschinenfaktoren_reshaped = maschinenfaktoren.reshape(-1, 1)
    print(f"Shape nach Reshape: {maschinenfaktoren_reshaped.shape}")

    # Broadcasting: (4,5) * (4,1) = (4,5)
    effizienz_angepasst = produktion * maschinenfaktoren_reshaped

    print("\nEffizienz-angepasste Produktion:")
    print("Original → Angepasst (alle Maschinen, Tag 1):")
    for i in range(len(maschinenfaktoren)):
        original = produktion[i, 0]
        angepasst = effizienz_angepasst[i, 0]
        print(
            f"   Maschine {i + 1}: {original:4d} → {angepasst:6.0f} (Faktor: {maschinenfaktoren[i]})"
        )
    print()

    # TODO 4: Kombination von Broadcasting-Operationen
    print("🎯 Broadcasting 4: Komplexe Berechnung")
    print("Zielwert-Vergleich mit individuellen Zielen pro Maschine:")

    # Individuelle Tagesziele pro Maschine
    tagesziele = np.array([1200, 1100, 1350, 1000])  # 4 Ziele
    tagesziele_reshaped = tagesziele.reshape(-1, 1)  # (4,1) für Broadcasting

    # Abweichung vom Ziel berechnen
    abweichung = produktion - tagesziele_reshaped  # (4,5) - (4,1) = (4,5)

    # Prozentuale Abweichung
    prozent_abweichung = (abweichung / tagesziele_reshaped) * 100

    print("Prozentuale Abweichung vom Tagesziel:")
    tage = ["Mo", "Di", "Mi", "Do", "Fr"]
    for i, tag in enumerate(tage):
        print(f"   {tag}: {prozent_abweichung[:, i].round(1)}%")

    # Durchschnittliche Zielerreichung pro Maschine
    durchschnitt_abweichung = np.mean(prozent_abweichung, axis=1)
    print(
        f"\nDurchschnittliche Abweichung pro Maschine: {durchschnitt_abweichung.round(1)}%"
    )
    print()

    print("✅ Aufgabe 3 abgeschlossen!")
    return angepasste_produktion, prozent_abweichung


def aufgabe_4_numpy_funktionen():
    """🎯 Aufgabe 4: Wichtige NumPy-Funktionen"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 4: Wichtige NumPy-Funktionen")
    print("=" * 60)

    # Energieverbrauch verschiedener Maschinen über eine Woche
    energieverbrauch = np.array(
        [
            [45.2, 43.8, 46.1, 44.5, 45.9, 38.2, 35.1],  # Laser (7 Tage)
            [52.3, 51.8, 53.1, 52.0, 53.5, 42.1, 40.3],  # Presse
            [38.7, 39.2, 38.1, 39.8, 38.5, 32.1, 30.8],  # Stanze
            [41.5, 42.1, 41.8, 42.3, 41.2, 35.5, 34.2],  # Biege
        ]
    )

    maschinen = ["Laser", "Presse", "Stanze", "Biege"]
    wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    print("⚡ Energieverbrauch (kWh) - 4 Maschinen × 7 Tage:")
    print("     ", "  ".join(f"{tag:>5}" for tag in wochentage))
    for i, maschine in enumerate(maschinen):
        werte = "  ".join(f"{val:5.1f}" for val in energieverbrauch[i])
        print(f"{maschine:6} {werte}")
    print()

    # TODO 1: Aggregationen entlang verschiedener Achsen
    print("📊 Aggregationen:")

    # Summe pro Maschine (über alle Tage)
    summe_pro_maschine = np.sum(energieverbrauch, axis=1)
    print("Wochensumme pro Maschine:")
    for i, maschine in enumerate(maschinen):
        print(f"   {maschine}: {summe_pro_maschine[i]:.1f} kWh")

    # Summe pro Tag (über alle Maschinen)
    summe_pro_tag = np.sum(energieverbrauch, axis=0)
    print("\nTagesverbrauch (alle Maschinen):")
    for i, tag in enumerate(wochentage):
        print(f"   {tag}: {summe_pro_tag[i]:.1f} kWh")

    # Gesamtverbrauch
    gesamtverbrauch = np.sum(energieverbrauch)
    print(f"\nGesamtverbrauch Woche: {gesamtverbrauch:.1f} kWh")
    print()

    # TODO 2: Mittelwerte und Trends
    print("📈 Mittelwerte und Trends:")

    # Durchschnitt pro Maschine
    durchschnitt_maschine = np.mean(energieverbrauch, axis=1)
    print("Durchschnittsverbrauch pro Tag:")
    for i, maschine in enumerate(maschinen):
        print(f"   {maschine}: {durchschnitt_maschine[i]:.1f} kWh/Tag")

    # Arbeitstagsdurchschnitt (Mo-Fr) vs Wochenende (Sa-So)
    arbeitstage = energieverbrauch[:, :5]  # Spalten 0-4 (Mo-Fr)
    wochenende = energieverbrauch[:, 5:]  # Spalten 5-6 (Sa-So)

    durchschnitt_arbeit = np.mean(arbeitstage, axis=1)
    durchschnitt_wochenende = np.mean(wochenende, axis=1)

    print("\nVergleich Arbeitstage vs Wochenende:")
    for i, maschine in enumerate(maschinen):
        einsparung = durchschnitt_arbeit[i] - durchschnitt_wochenende[i]
        prozent = (einsparung / durchschnitt_arbeit[i]) * 100
        print(
            f"   {maschine}: {durchschnitt_arbeit[i]:.1f} → {durchschnitt_wochenende[i]:.1f} kWh (-{prozent:.1f}%)"
        )
    print()

    # TODO 3: Min/Max und Argmin/Argmax
    print("🔍 Extremwerte finden:")

    # Globale Extremwerte
    min_verbrauch = np.min(energieverbrauch)
    max_verbrauch = np.max(energieverbrauch)

    # Position der Extremwerte finden
    min_pos = np.unravel_index(np.argmin(energieverbrauch), energieverbrauch.shape)
    max_pos = np.unravel_index(np.argmax(energieverbrauch), energieverbrauch.shape)

    print(
        f"Minimum: {min_verbrauch:.1f} kWh ({maschinen[min_pos[0]]}, {wochentage[min_pos[1]]})"
    )
    print(
        f"Maximum: {max_verbrauch:.1f} kWh ({maschinen[max_pos[0]]}, {wochentage[max_pos[1]]})"
    )

    # Extremwerte pro Maschine
    print("\nExtremwerte pro Maschine:")
    for i, maschine in enumerate(maschinen):
        min_tag = np.argmin(energieverbrauch[i])
        max_tag = np.argmax(energieverbrauch[i])
        min_wert = energieverbrauch[i, min_tag]
        max_wert = energieverbrauch[i, max_tag]
        print(
            f"   {maschine}: Min {min_wert:.1f} ({wochentage[min_tag]}) - Max {max_wert:.1f} ({wochentage[max_tag]})"
        )
    print()

    # TODO 4: Runden und Formatierung
    print("🔢 Runden und Formatierung:")

    # Verschiedene Rundungsmethoden
    beispiel_werte = energieverbrauch[0, :3]  # Erste 3 Werte der ersten Maschine
    print(f"Original-Werte: {beispiel_werte}")
    print(f"Auf ganze Zahlen: {np.round(beispiel_werte, 0).astype(int)}")
    print(f"Eine Dezimalstelle: {np.round(beispiel_werte, 1)}")
    print(f"Ceiling (aufrunden): {np.ceil(beispiel_werte)}")
    print(f"Floor (abrunden): {np.floor(beispiel_werte)}")
    print()

    print("✅ Aufgabe 4 abgeschlossen!")
    return energieverbrauch, durchschnitt_maschine


def aufgabe_5_praktische_anwendung():
    """🎯 Aufgabe 5: Praktische Gesamtanwendung"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 5: Praktische Gesamtanwendung")
    print("=" * 60)

    # Komplexes Szenario: Monatsauswertung Produktion
    print("🏭 SZENARIO: Monatsauswertung Bystronic-Produktion")
    print("=" * 50)

    # Simuliere Produktionsdaten für 4 Wochen
    np.random.seed(123)

    # 4 Maschinen × 4 Wochen × 5 Arbeitstage
    basis_produktion = np.array([1200, 1100, 1350, 1000])  # Basis pro Maschine

    # Zufällige Variation ±10%
    variation = np.random.uniform(0.9, 1.1, (4, 4, 5))  # (Maschinen, Wochen, Tage)
    monatsproduktion = basis_produktion.reshape(-1, 1, 1) * variation

    print("Produktionsdaten: 4 Maschinen × 4 Wochen × 5 Tage")
    print(f"Array-Shape: {monatsproduktion.shape}")
    print()

    # TODO 1: Verschiedene Aggregationen
    print("📊 Monatsstatistiken:")

    # Gesamtproduktion
    gesamtproduktion = np.sum(monatsproduktion)
    print(f"Gesamtproduktion Monat: {gesamtproduktion:,.0f} Stück")

    # Pro Maschine
    produktion_pro_maschine = np.sum(
        monatsproduktion, axis=(1, 2)
    )  # Summe über Wochen und Tage
    maschinen = ["Laser_01", "Presse_02", "Stanze_03", "Biege_04"]

    print("\nProduktion pro Maschine:")
    for i, maschine in enumerate(maschinen):
        anteil = produktion_pro_maschine[i] / gesamtproduktion * 100
        print(f"   {maschine}: {produktion_pro_maschine[i]:,.0f} Stück ({anteil:.1f}%)")

    # Pro Woche
    produktion_pro_woche = np.sum(
        monatsproduktion, axis=(0, 2)
    )  # Summe über Maschinen und Tage
    print("\nProduktion pro Woche:")
    for woche, produktion in enumerate(produktion_pro_woche, 1):
        print(f"   Woche {woche}: {produktion:,.0f} Stück")
    print()

    # TODO 2: Qualitätsanalyse
    print("🎯 Zielvergleich und Effizienz:")

    # Sollwerte pro Maschine pro Tag
    tagesziele = np.array([1200, 1100, 1350, 1000])

    # Tägliche Zielerreichung berechnen
    zielerreichung = monatsproduktion / tagesziele.reshape(-1, 1, 1) * 100

    # Durchschnittliche Zielerreichung pro Maschine
    durchschnitt_zielerreichung = np.mean(zielerreichung, axis=(1, 2))

    print("Durchschnittliche Zielerreichung:")
    for i, maschine in enumerate(maschinen):
        erreicht = durchschnitt_zielerreichung[i]
        status = "✅" if erreicht >= 95 else "⚠️" if erreicht >= 90 else "❌"
        print(f"   {maschine}: {erreicht:.1f}% {status}")

    # Beste und schlechteste Tage finden
    tagesproduktion = np.sum(monatsproduktion, axis=0)  # (4 Wochen, 5 Tage)
    bester_tag_pos = np.unravel_index(np.argmax(tagesproduktion), tagesproduktion.shape)
    schlechtester_tag_pos = np.unravel_index(
        np.argmin(tagesproduktion), tagesproduktion.shape
    )

    print(
        f"\nBester Tag: Woche {bester_tag_pos[0] + 1}, Tag {bester_tag_pos[1] + 1} ({tagesproduktion[bester_tag_pos]:,.0f} Stück)"
    )
    print(
        f"Schlechtester Tag: Woche {schlechtester_tag_pos[0] + 1}, Tag {schlechtester_tag_pos[1] + 1} ({tagesproduktion[schlechtester_tag_pos]:,.0f} Stück)"
    )
    print()

    # TODO 3: Trend-Analyse
    print("📈 Trend-Analyse:")

    # Wöchentliche Trends pro Maschine
    wochentrends = np.mean(monatsproduktion, axis=2)  # Durchschnitt pro Woche

    print("Wöchentliche Entwicklung pro Maschine:")
    for i, maschine in enumerate(maschinen):
        trend_daten = wochentrends[i]
        # Einfache Trend-Berechnung (letzte - erste Woche)
        trend = trend_daten[-1] - trend_daten[0]
        trend_prozent = (trend / trend_daten[0]) * 100

        if trend_prozent > 2:
            trend_symbol = "📈 steigend"
        elif trend_prozent < -2:
            trend_symbol = "📉 fallend"
        else:
            trend_symbol = "➡️ stabil"

        print(f"   {maschine}: {trend_symbol} ({trend_prozent:+.1f}%)")
        print(f"      Wochen: {' → '.join(f'{val:.0f}' for val in trend_daten)}")
    print()

    # TODO 4: Zusammenfassung und Empfehlungen
    print("💡 Zusammenfassung und Empfehlungen:")

    # Beste und schlechteste Maschine
    beste_maschine_idx = np.argmax(durchschnitt_zielerreichung)
    schlechteste_maschine_idx = np.argmin(durchschnitt_zielerreichung)

    print(
        f"🏆 Beste Maschine: {maschinen[beste_maschine_idx]} ({durchschnitt_zielerreichung[beste_maschine_idx]:.1f}% Zielerreichung)"
    )
    print(
        f"⚠️ Verbesserungsbedarf: {maschinen[schlechteste_maschine_idx]} ({durchschnitt_zielerreichung[schlechteste_maschine_idx]:.1f}% Zielerreichung)"
    )

    # Gesamtbewertung
    durchschnitt_gesamt = np.mean(durchschnitt_zielerreichung)
    if durchschnitt_gesamt >= 100:
        bewertung = "Hervorragend! Alle Ziele übertroffen."
    elif durchschnitt_gesamt >= 95:
        bewertung = "Sehr gut! Ziele fast erreicht."
    elif durchschnitt_gesamt >= 90:
        bewertung = "Gut. Leichte Optimierungen möglich."
    else:
        bewertung = "Verbesserungen erforderlich."

    print(f"📊 Gesamtbewertung: {bewertung} (⌀ {durchschnitt_gesamt:.1f}%)")
    print()

    print("✅ Aufgabe 5 abgeschlossen!")
    return monatsproduktion, durchschnitt_zielerreichung


def main():
    """🚀 Hauptprogramm - Alle Aufgaben ausführen"""
    print("🟢 BEGINNER: Mathematische Operationen mit NumPy für Bystronic")
    print("=" * 70)
    print("📚 Lernen Sie vektorisierte Berechnungen und statistische Funktionen!")
    print("🎯 Ziel: Effiziente mathematische Operationen für Produktionsdaten")
    print()

    try:
        # Aufgabe 1: Grundrechenarten
        gesamtproduktion, produktivitaet = aufgabe_1_grundrechenarten()

        # Aufgabe 2: Statistische Funktionen
        messungen, cp_wert = aufgabe_2_statistische_funktionen()

        # Aufgabe 3: Broadcasting
        angepasste_prod, abweichungen = aufgabe_3_broadcasting()

        # Aufgabe 4: NumPy-Funktionen
        energiedaten, durchschnitt = aufgabe_4_numpy_funktionen()

        # Aufgabe 5: Praktische Anwendung
        monatsdata, zielerreichung = aufgabe_5_praktische_anwendung()

        # Erfolgreicher Abschluss
        print("\n" + "🎉" * 30)
        print("🎉 HERZLICHEN GLÜCKWUNSCH! 🎉")
        print("🎉" * 30)
        print(
            "✅ Sie haben alle Beginner-Aufgaben zu mathematischen Operationen gemeistert!"
        )
        print()
        print("🎓 Sie können jetzt:")
        print("   • Vektorisierte Grundrechenarten anwenden")
        print("   • Statistische NumPy-Funktionen nutzen")
        print("   • Broadcasting-Regeln verstehen")
        print("   • Komplexe Aggregationen durchführen")
        print("   • Produktionsdaten mathematisch analysieren")
        print()
        print("➡️ NÄCHSTE SCHRITTE:")
        print("📚 Übung 3: Array-Manipulation")
        print("🚀 uv run python exercises/beginner/uebung_03_manipulation_beginner.py")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
        print("💡 Sie können jederzeit weitermachen!")

    except Exception as e:
        print(f"\n❌ Fehler aufgetreten: {e}")
        print(
            "💡 Tipp: Überprüfen Sie die Hints in solutions/beginner/uebung_02_hints.md"
        )


if __name__ == "__main__":
    main()
