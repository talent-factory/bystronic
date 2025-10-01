#!/usr/bin/env python3
"""
🟢 BEGINNER - SmartFactory Python Grundkurs - Kapitel 3
Übung 3: Array-Manipulation (Einsteigerfreundlich)

🎯 LERNZIELE (20-25 Minuten):
- Array-Shapes verstehen und ändern (reshape)
- Arrays kombinieren und trennen (concatenate, split)
- Erweiterte Indexing-Techniken anwenden
- Boolean Indexing für Datenfilterung
- Praktische Datenumstrukturierung für SmartFactory

📚 HILFSMITTEL:
- Hints: solutions/beginner/uebung_03_hints.md
- Skeleton: solutions/beginner/uebung_03_skeleton.py
- Partial: solutions/beginner/uebung_03_partial.py
- Complete: solutions/beginner/uebung_03_complete.py

🏭 BYSTRONIC-KONTEXT:
Array-Manipulation für Produktionsdaten:
Maschinendaten umstrukturieren, Schichtdaten kombinieren, Qualitätsdaten filtern.
"""

import numpy as np


def aufgabe_1_reshape_und_transpose():
    """🎯 Aufgabe 1: Arrays umformen und transponieren"""
    print("=" * 60)
    print("🟢 AUFGABE 1: Reshape und Transpose")
    print("=" * 60)

    # Stündliche Produktionsdaten für 3 Tage (24 Stunden × 3 Tage = 72 Werte)
    stuendliche_daten = np.arange(1, 73)  # 1 bis 72
    print("📊 Stündliche Produktionsdaten (3 Tage):")
    print(f"Linear: {stuendliche_daten[:12]}... (72 Werte total)")
    print(f"Shape: {stuendliche_daten.shape}")
    print()

    # TODO 1: Reshape zu 3 Tage × 24 Stunden
    print("🔄 Reshape zu Tage × Stunden Matrix:")
    tage_stunden = stuendliche_daten.reshape(3, 24)
    print(f"Shape nach Reshape: {tage_stunden.shape}")
    print("Erste 8 Stunden pro Tag:")
    for tag in range(3):
        print(f"   Tag {tag + 1}: {tage_stunden[tag, :8]}")
    print()

    # TODO 2: Alternative Reshape zu 24 Stunden × 3 Tage
    print("🔄 Alternative: Stunden × Tage Matrix:")
    stunden_tage = stuendliche_daten.reshape(24, 3)
    print(f"Shape: {stunden_tage.shape}")
    print("Erste 5 Stunden (alle Tage):")
    for stunde in range(5):
        print(f"   Stunde {stunde + 1:2d}: {stunden_tage[stunde]}")
    print()

    # TODO 3: Transponieren
    print("↔️ Transponieren:")
    tage_stunden_T = tage_stunden.T  # oder tage_stunden.transpose()
    print(f"Original Shape: {tage_stunden.shape}")
    print(f"Transponiert:   {tage_stunden_T.shape}")
    print("Jetzt: Stunden × Tage (wie oben, aber durch Transposition)")
    print()

    # TODO 4: Praktische Anwendung - Schichtdaten
    print("🏭 Praktisch: Umformung zu Schichtdaten")
    # 24 Stunden → 3 Schichten × 8 Stunden

    # Nehme nur den ersten Tag
    ein_tag = tage_stunden[0]  # 24 Stunden
    schichten = ein_tag.reshape(3, 8)  # 3 Schichten × 8 Stunden

    schicht_namen = ["Frühschicht", "Spätschicht", "Nachtschicht"]
    print("Schichtaufteilung:")
    for i, name in enumerate(schicht_namen):
        schicht_summe = np.sum(schichten[i])
        print(f"   {name}: {schichten[i]} (Summe: {schicht_summe})")
    print()

    # TODO 5: Automatisches Reshape mit -1
    print("🎯 Automatisches Reshape:")
    # -1 bedeutet: "Berechne diese Dimension automatisch"
    auto_reshape = stuendliche_daten.reshape(-1, 12)  # ? × 12
    print(f"Reshape zu (-1, 12): {auto_reshape.shape}")

    auto_reshape2 = stuendliche_daten.reshape(8, -1)  # 8 × ?
    print(f"Reshape zu (8, -1):  {auto_reshape2.shape}")
    print()

    print("✅ Aufgabe 1 abgeschlossen!")
    return tage_stunden, schichten


def aufgabe_2_concatenate_und_split():
    """🎯 Aufgabe 2: Arrays kombinieren und trennen"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 2: Concatenate und Split")
    print("=" * 60)

    # Produktionsdaten verschiedener Maschinen
    laser_woche1 = np.array([1200, 1180, 1250, 1190, 1220])
    laser_woche2 = np.array([1150, 1200, 1280, 1160, 1240])

    presse_woche1 = np.array([1100, 1150, 1120, 1080, 1140])
    presse_woche2 = np.array([1080, 1120, 1160, 1100, 1130])

    print("📊 Produktionsdaten (Stück/Tag):")
    print(f"Laser Woche 1:  {laser_woche1}")
    print(f"Laser Woche 2:  {laser_woche2}")
    print(f"Presse Woche 1: {presse_woche1}")
    print(f"Presse Woche 2: {presse_woche2}")
    print()

    # TODO 1: Horizontales Concatenate (Wochen kombinieren)
    print("➡️ Horizontales Concatenate: Wochen kombinieren")
    laser_2wochen = np.concatenate([laser_woche1, laser_woche2])
    presse_2wochen = np.concatenate([presse_woche1, presse_woche2])

    print(f"Laser 2 Wochen:  {laser_2wochen}")
    print(f"Presse 2 Wochen: {presse_2wochen}")
    print(f"Shape: {laser_2wochen.shape}")
    print()

    # TODO 2: Vertikales Concatenate (Maschinen kombinieren)
    print("⬇️ Vertikales Concatenate: Maschinen kombinieren")

    # Erst zu 2D-Arrays umformen
    woche1_matrix = np.array([laser_woche1, presse_woche1])
    woche2_matrix = np.array([laser_woche2, presse_woche2])

    print("Woche 1 Matrix (2 Maschinen × 5 Tage):")
    print(woche1_matrix)
    print("Woche 2 Matrix:")
    print(woche2_matrix)

    # Vertikal kombinieren (axis=0 = neue Zeilen hinzufügen)
    alle_daten_vertikal = np.concatenate([woche1_matrix, woche2_matrix], axis=0)
    print("\nAlle Daten vertikal (4 × 5):")
    print(alle_daten_vertikal)
    print(f"Shape: {alle_daten_vertikal.shape}")
    print()

    # TODO 3: Horizontal kombinieren (neue Spalten)
    print("➡️ Horizontal kombinieren: Wochen als Spalten")
    alle_daten_horizontal = np.concatenate([woche1_matrix, woche2_matrix], axis=1)
    print("Alle Daten horizontal (2 × 10):")
    print(alle_daten_horizontal)
    print(f"Shape: {alle_daten_horizontal.shape}")
    print()

    # TODO 4: Vereinfachte Syntax mit hstack und vstack
    print("🔧 Vereinfachte Syntax:")

    # hstack = horizontal stack (gleich wie axis=1)
    h_stacked = np.hstack([woche1_matrix, woche2_matrix])
    print(f"hstack result: {h_stacked.shape}")

    # vstack = vertical stack (gleich wie axis=0)
    v_stacked = np.vstack([woche1_matrix, woche2_matrix])
    print(f"vstack result: {v_stacked.shape}")
    print()

    # TODO 5: Arrays trennen (Split)
    print("✂️ Arrays trennen:")

    # Split der 10-Tage-Daten zurück in 2 Wochen
    woche1_wieder, woche2_wieder = np.hsplit(alle_daten_horizontal, 2)
    print("Nach hsplit (horizontal split):")
    print(f"Woche 1 wieder: {woche1_wieder.shape}")
    print(woche1_wieder)
    print()

    # Split der 4-Maschinen-Daten in einzelne Maschinen
    if alle_daten_vertikal.shape[0] == 4:  # 4 Zeilen (2 Maschinen × 2 Wochen)
        laser_w1, presse_w1, laser_w2, presse_w2 = np.vsplit(alle_daten_vertikal, 4)
        print("Nach vsplit (vertical split) - jede Zeile einzeln:")
        print(f"Laser W1: {laser_w1.flatten()}")  # flatten macht 1D draus
        print(f"Presse W1: {presse_w1.flatten()}")
    print()

    # TODO 6: Split an spezifischen Positionen
    print("🎯 Split an spezifischen Positionen:")

    # 10-Tage-Daten in ungleiche Teile: [3 Tage][4 Tage][3 Tage]
    teil1, teil2, teil3 = np.hsplit(alle_daten_horizontal, [3, 7])
    print(f"Teil 1 (erste 3 Tage): {teil1.shape}")
    print(f"Teil 2 (Tag 4-7):      {teil2.shape}")
    print(f"Teil 3 (letzte 3 Tage): {teil3.shape}")
    print()

    print("✅ Aufgabe 2 abgeschlossen!")
    return alle_daten_horizontal, alle_daten_vertikal


def aufgabe_3_erweiterte_indexierung():
    """🎯 Aufgabe 3: Erweiterte Indexing-Techniken"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 3: Erweiterte Indexierung")
    print("=" * 60)

    # Produktionsmatrix: 5 Maschinen × 6 Kennwerte
    # [Stückzahl, Laufzeit, Effizienz, Energie, Ausschuss, Wartung]
    np.random.seed(42)
    produktionsmatrix = np.array(
        [
            [1200, 8.5, 0.92, 45.2, 12, 0],  # Maschine 1
            [1150, 8.2, 0.89, 42.1, 18, 1],  # Maschine 2
            [1380, 9.1, 0.95, 48.7, 8, 0],  # Maschine 3
            [980, 7.8, 0.85, 38.5, 25, 1],  # Maschine 4
            [1250, 8.8, 0.91, 46.3, 15, 0],  # Maschine 5
        ]
    )

    kennwerte = [
        "Stückzahl",
        "Laufzeit_h",
        "Effizienz_%",
        "Energie_kWh",
        "Ausschuss",
        "Wartung",
    ]
    maschinen = [f"M{i + 1}" for i in range(5)]

    print("📊 Produktionsmatrix (5 Maschinen × 6 Kennwerte):")
    print("      ", "  ".join(f"{kw:>10}" for kw in kennwerte))
    for i, zeile in enumerate(produktionsmatrix):
        werte = "  ".join(f"{val:>10.1f}" for val in zeile)
        print(f"{maschinen[i]:3} {werte}")
    print()

    # TODO 1: Fancy Indexing - Spezifische Zeilen/Spalten
    print("🎯 Fancy Indexing:")

    # Bestimmte Maschinen auswählen (Index-Arrays)
    interessante_maschinen = [0, 2, 4]  # M1, M3, M5
    ausgewaehlte_daten = produktionsmatrix[interessante_maschinen]
    print("Ausgewählte Maschinen (M1, M3, M5):")
    for i, zeile in enumerate(ausgewaehlte_daten):
        print(f"   {maschinen[interessante_maschinen[i]]}: {zeile}")
    print()

    # Bestimmte Kennwerte auswählen
    wichtige_kennwerte = [0, 2, 4]  # Stückzahl, Effizienz, Ausschuss
    wichtige_daten = produktionsmatrix[:, wichtige_kennwerte]
    print("Wichtige Kennwerte (alle Maschinen):")
    wichtige_namen = [kennwerte[i] for i in wichtige_kennwerte]
    print("      ", "  ".join(f"{kw:>10}" for kw in wichtige_namen))
    for i, zeile in enumerate(wichtige_daten):
        werte = "  ".join(f"{val:>10.1f}" for val in zeile)
        print(f"{maschinen[i]:3} {werte}")
    print()

    # TODO 2: Boolean Indexing - Bedingte Auswahl
    print("🔍 Boolean Indexing:")

    # Maschinen mit hoher Effizienz (> 90%)
    effizienz_spalte = produktionsmatrix[:, 2]  # Spalte 2 = Effizienz
    hohe_effizienz = effizienz_spalte > 0.90

    print(f"Effizienz-Werte: {effizienz_spalte}")
    print(f"Hohe Effizienz (>90%): {hohe_effizienz}")
    print("Maschinen mit hoher Effizienz:")

    effiziente_maschinen = produktionsmatrix[hohe_effizienz]
    effiziente_indices = np.where(hohe_effizienz)[0]

    for i, zeile in enumerate(effiziente_maschinen):
        maschine_idx = effiziente_indices[i]
        print(f"   {maschinen[maschine_idx]}: Effizienz {zeile[2]:.1%}")
    print()

    # TODO 3: Mehrere Bedingungen kombinieren
    print("🎯 Kombinierte Bedingungen:")

    # Maschinen mit hoher Effizienz UND niedrigem Ausschuss
    hohe_effizienz = produktionsmatrix[:, 2] > 0.90  # Effizienz > 90%
    niedriger_ausschuss = produktionsmatrix[:, 4] < 15  # Ausschuss < 15

    # Logisches UND mit &
    top_maschinen = hohe_effizienz & niedriger_ausschuss
    print(f"Hohe Effizienz: {hohe_effizienz}")
    print(f"Niedriger Ausschuss: {niedriger_ausschuss}")
    print(f"Beide Bedingungen: {top_maschinen}")

    if np.any(top_maschinen):
        print("Top-Maschinen (hohe Effizienz + niedriger Ausschuss):")
        top_daten = produktionsmatrix[top_maschinen]
        top_indices = np.where(top_maschinen)[0]

        for i, zeile in enumerate(top_daten):
            maschine_idx = top_indices[i]
            print(
                f"   {maschinen[maschine_idx]}: Effizienz {zeile[2]:.1%}, Ausschuss {zeile[4]:.0f}"
            )
    print()

    # TODO 4: Where-Funktion für bedingte Operationen
    print("🔧 np.where für bedingte Operationen:")

    # Wartungsstatus als Text
    wartung_status = np.where(produktionsmatrix[:, 5] == 1, "Wartung fällig", "OK")
    print("Wartungsstatus:")
    for i, status in enumerate(wartung_status):
        print(f"   {maschinen[i]}: {status}")
    print()

    # Effizienz-Kategorien
    effizienz = produktionsmatrix[:, 2]
    kategorien = np.where(
        effizienz > 0.92, "Hoch", np.where(effizienz > 0.88, "Mittel", "Niedrig")
    )

    print("Effizienz-Kategorien:")
    for i, kategorie in enumerate(kategorien):
        print(f"   {maschinen[i]}: {effizienz[i]:.1%} → {kategorie}")
    print()

    # TODO 5: Argmax/Argmin für beste/schlechteste Werte
    print("🏆 Beste und schlechteste Maschinen:")

    # Beste Effizienz
    beste_effizienz_idx = np.argmax(produktionsmatrix[:, 2])
    beste_effizienz = produktionsmatrix[beste_effizienz_idx, 2]
    print(f"Beste Effizienz: {maschinen[beste_effizienz_idx]} ({beste_effizienz:.1%})")

    # Höchste Produktion
    hoechste_produktion_idx = np.argmax(produktionsmatrix[:, 0])
    hoechste_produktion = produktionsmatrix[hoechste_produktion_idx, 0]
    print(
        f"Höchste Produktion: {maschinen[hoechste_produktion_idx]} ({hoechste_produktion:.0f} Stück)"
    )

    # Niedrigster Ausschuss
    niedrigster_ausschuss_idx = np.argmin(produktionsmatrix[:, 4])
    niedrigster_ausschuss = produktionsmatrix[niedrigster_ausschuss_idx, 4]
    print(
        f"Niedrigster Ausschuss: {maschinen[niedrigster_ausschuss_idx]} ({niedrigster_ausschuss:.0f} Stück)"
    )
    print()

    print("✅ Aufgabe 3 abgeschlossen!")
    return produktionsmatrix, top_maschinen


def aufgabe_4_datenfilterung():
    """🎯 Aufgabe 4: Erweiterte Datenfilterung"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 4: Datenfilterung und -auswahl")
    print("=" * 60)

    # Qualitätsmessungen über eine Woche
    np.random.seed(123)
    n_messungen = 50

    # Simuliere Messungen mit verschiedenen Toleranzbereichen
    sollwert = 25.0
    messungen = np.random.normal(sollwert, 0.4, n_messungen)

    # Füge bewusst einige Ausreißer hinzu
    messungen[5] = 26.8  # Leicht außerhalb
    messungen[15] = 24.1  # Leicht außerhalb
    messungen[25] = 27.2  # Deutlich außerhalb
    messungen[35] = 23.5  # Deutlich außerhalb

    print(f"📏 Qualitätsmessungen: {n_messungen} Werte (Sollwert: {sollwert} mm)")
    print(f"Wertebereich: {messungen.min():.2f} - {messungen.max():.2f} mm")
    print(f"Erste 10 Werte: {messungen[:10].round(2)}")
    print()

    # TODO 1: Einfache Toleranzprüfung
    print("🎯 Toleranzprüfung:")

    toleranz_eng = 0.3  # ±0.3 mm (enge Toleranz)
    toleranz_weit = 0.8  # ±0.8 mm (weite Toleranz)

    # Boolean Arrays für verschiedene Toleranzen
    in_toleranz_eng = np.abs(messungen - sollwert) <= toleranz_eng
    in_toleranz_weit = np.abs(messungen - sollwert) <= toleranz_weit

    print(
        f"Enge Toleranz (±{toleranz_eng}mm): {np.sum(in_toleranz_eng)}/{n_messungen} OK ({np.mean(in_toleranz_eng) * 100:.1f}%)"
    )
    print(
        f"Weite Toleranz (±{toleranz_weit}mm): {np.sum(in_toleranz_weit)}/{n_messungen} OK ({np.mean(in_toleranz_weit) * 100:.1f}%)"
    )
    print()

    # TODO 2: Kategorisierung der Messungen
    print("📊 Kategorisierung:")

    # Verschiedene Kategorien basierend auf Abweichung
    abweichung = np.abs(messungen - sollwert)

    perfekt = abweichung <= 0.1
    gut = (abweichung > 0.1) & (abweichung <= 0.3)
    akzeptabel = (abweichung > 0.3) & (abweichung <= 0.8)
    ausschuss = abweichung > 0.8

    print(
        f"Perfekt (≤0.1mm):     {np.sum(perfekt):2d} ({np.mean(perfekt) * 100:4.1f}%)"
    )
    print(f"Gut (0.1-0.3mm):      {np.sum(gut):2d} ({np.mean(gut) * 100:4.1f}%)")
    print(
        f"Akzeptabel (0.3-0.8mm): {np.sum(akzeptabel):2d} ({np.mean(akzeptabel) * 100:4.1f}%)"
    )
    print(
        f"Ausschuss (>0.8mm):   {np.sum(ausschuss):2d} ({np.mean(ausschuss) * 100:4.1f}%)"
    )
    print()

    # TODO 3: Ausreißer-Identifikation
    print("🔍 Ausreißer-Identifikation:")

    # Statistische Methode: 3-Sigma-Regel
    mittelwert = np.mean(messungen)
    std_abweichung = np.std(messungen, ddof=1)

    # Grenzen für Ausreißer
    untere_grenze = mittelwert - 3 * std_abweichung
    obere_grenze = mittelwert + 3 * std_abweichung

    # Ausreißer finden
    ausreisser = (messungen < untere_grenze) | (messungen > obere_grenze)
    ausreisser_werte = messungen[ausreisser]
    ausreisser_indices = np.where(ausreisser)[0]

    print(f"Mittelwert: {mittelwert:.3f} mm")
    print(f"Std.-Abweichung: {std_abweichung:.3f} mm")
    print(f"3σ-Grenzen: {untere_grenze:.3f} - {obere_grenze:.3f} mm")
    print(f"Ausreißer gefunden: {len(ausreisser_werte)}")

    if len(ausreisser_werte) > 0:
        print("Ausreißer-Details:")
        for i, wert in enumerate(ausreisser_werte):
            idx = ausreisser_indices[i]
            abw = abs(wert - sollwert)
            print(f"   Index {idx:2d}: {wert:.3f} mm (Abweichung: {abw:.3f} mm)")
    print()

    # TODO 4: Datenbereinigung
    print("🧹 Datenbereinigung:")

    # Bereinigte Daten ohne Ausreißer
    bereinigte_messungen = messungen[~ausreisser]  # ~ ist logisches NOT

    print(f"Original: {len(messungen)} Messungen")
    print(f"Bereinigt: {len(bereinigte_messungen)} Messungen")
    print(f"Entfernt: {len(messungen) - len(bereinigte_messungen)} Ausreißer")
    print()

    # Vergleich der Statistiken
    print("Statistik-Vergleich (vor/nach Bereinigung):")
    print(
        f"   Mittelwert: {np.mean(messungen):.3f} → {np.mean(bereinigte_messungen):.3f} mm"
    )
    print(
        f"   Std.-Abw.: {np.std(messungen, ddof=1):.3f} → {np.std(bereinigte_messungen, ddof=1):.3f} mm"
    )
    print(
        f"   Min/Max: {messungen.min():.3f}/{messungen.max():.3f} → {bereinigte_messungen.min():.3f}/{bereinigte_messungen.max():.3f} mm"
    )
    print()

    # TODO 5: Trend-Analyse mit gleitendem Fenster
    print("📈 Trend-Analyse:")

    # Gleitender Durchschnitt (5-Punkte-Fenster)
    fenstergroesse = 5
    if len(messungen) >= fenstergroesse:
        # Gleitender Durchschnitt mit Convolution
        gleitender_durchschnitt = np.convolve(
            messungen, np.ones(fenstergroesse) / fenstergroesse, mode="valid"
        )

        print(f"Gleitender Durchschnitt ({fenstergroesse}-Punkte-Fenster):")
        print(f"   Anzahl Werte: {len(gleitender_durchschnitt)}")
        print(
            f"   Bereich: {gleitender_durchschnitt.min():.3f} - {gleitender_durchschnitt.max():.3f} mm"
        )

        # Trend berechnen (einfache lineare Regression)
        x = np.arange(len(gleitender_durchschnitt))
        trend_koeff = np.polyfit(x, gleitender_durchschnitt, 1)[0]  # Steigung

        if abs(trend_koeff) < 0.001:
            trend_text = "stabil ➡️"
        elif trend_koeff > 0:
            trend_text = f"steigend ↗️ (+{trend_koeff * 1000:.1f} µm/Messung)"
        else:
            trend_text = f"fallend ↘️ ({trend_koeff * 1000:.1f} µm/Messung)"

        print(f"   Trend: {trend_text}")
    print()

    # TODO 6: Qualitätsbericht
    print("📋 Qualitätsbericht:")

    ausschuss_rate = np.mean(ausschuss) * 100
    cp_wert = (2 * toleranz_weit) / (6 * std_abweichung)  # Vereinfachter Cp-Wert

    print(f"🎯 Zusammenfassung ({n_messungen} Messungen):")
    print(f"   • Sollwert: {sollwert} mm")
    print(f"   • Ist-Mittelwert: {mittelwert:.3f} mm")
    print(f"   • Abweichung: {abs(mittelwert - sollwert) * 1000:.0f} µm")
    print(f"   • Ausschussrate: {ausschuss_rate:.1f}%")
    print(f"   • Cp-Wert: {cp_wert:.2f}")
    print(f"   • Ausreißer: {len(ausreisser_werte)}")

    # Gesamtbewertung
    if cp_wert >= 1.33 and ausschuss_rate < 5:
        bewertung = "✅ Hervorragend"
    elif cp_wert >= 1.0 and ausschuss_rate < 10:
        bewertung = "🟡 Gut"
    else:
        bewertung = "❌ Verbesserung nötig"

    print(f"   • Bewertung: {bewertung}")
    print()

    print("✅ Aufgabe 4 abgeschlossen!")
    return bereinigte_messungen, cp_wert


def aufgabe_5_praktische_datenorganisation():
    """🎯 Aufgabe 5: Praktische Datenorganisation"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 5: Praktische Datenorganisation")
    print("=" * 60)

    # Komplexes Szenario: Mehrere Maschinen, mehrere Tage, mehrere Schichten
    print("🏭 SZENARIO: Produktionsanalyse nach Umstrukturierung")
    print("=" * 55)

    # 3 Maschinen × 5 Tage × 3 Schichten
    np.random.seed(456)
    basis_werte = [150, 180, 200]  # Basis-Stückzahl pro Schicht

    # Generiere realistische Daten
    produktions_data = []
    for maschine in range(3):
        for tag in range(5):
            for schicht in range(3):
                basis = basis_werte[schicht]
                variation = np.random.uniform(0.85, 1.15)
                wert = int(basis * variation)
                produktions_data.append(wert)

    # Als 3D-Array strukturieren
    produktion_3d = np.array(produktions_data).reshape(3, 5, 3)

    print(f"📊 Produktionsdaten: {produktion_3d.shape} (Maschinen × Tage × Schichten)")
    print(f"Gesamtdatenpunkte: {produktion_3d.size}")
    print()

    # TODO 1: Verschiedene Ansichten der Daten
    print("👁️ Verschiedene Datenansichten:")

    maschinen_namen = ["Laser_01", "Presse_02", "Stanze_03"]
    schicht_namen = ["Früh", "Spät", "Nacht"]
    tag_namen = ["Mo", "Di", "Mi", "Do", "Fr"]

    # Ansicht 1: Pro Maschine
    print("Ansicht 1 - Pro Maschine (Tage × Schichten):")
    for m, maschine in enumerate(maschinen_namen):
        print(f"   {maschine}:")
        maschinen_data = produktion_3d[m]  # Shape: (5, 3)
        print("        ", "  ".join(f"{s:>6}" for s in schicht_namen))
        for t, tag in enumerate(tag_namen):
            werte = "  ".join(f"{maschinen_data[t, s]:6d}" for s in range(3))
            print(f"      {tag} {werte}")
        print()

    # TODO 2: Aggregationen über verschiedene Dimensionen
    print("📊 Aggregationen:")

    # Summe pro Maschine (über alle Tage und Schichten)
    summe_pro_maschine = np.sum(produktion_3d, axis=(1, 2))
    print("Wochenproduktion pro Maschine:")
    for m, maschine in enumerate(maschinen_namen):
        print(f"   {maschine}: {summe_pro_maschine[m]:,} Stück")

    # Summe pro Tag (über alle Maschinen und Schichten)
    summe_pro_tag = np.sum(produktion_3d, axis=(0, 2))
    print("\nTagesproduktion (alle Maschinen):")
    for t, tag in enumerate(tag_namen):
        print(f"   {tag}: {summe_pro_tag[t]:,} Stück")

    # Summe pro Schicht (über alle Maschinen und Tage)
    summe_pro_schicht = np.sum(produktion_3d, axis=(0, 1))
    print("\nSchichtproduktion (alle Maschinen, ganze Woche):")
    for s, schicht in enumerate(schicht_namen):
        print(f"   {schicht}: {summe_pro_schicht[s]:,} Stück")
    print()

    # TODO 3: Reshape für verschiedene Analysen
    print("🔄 Datenumstrukturierung für Analysen:")

    # Flatten zu 1D für Gesamtstatistik
    alle_werte = produktion_3d.flatten()
    print(f"Flatten zu 1D: {alle_werte.shape}")
    print(
        f"   Gesamtstatistik: Min={alle_werte.min()}, Max={alle_werte.max()}, Ø={alle_werte.mean():.0f}"
    )

    # Reshape zu 2D: (Maschinen × Alles andere)
    maschinen_matrix = produktion_3d.reshape(3, -1)  # 3 × 15
    print(f"\nReshape zu Maschinen-Matrix: {maschinen_matrix.shape}")
    print("   Pro Maschine - Min, Max, Durchschnitt:")
    for m, maschine in enumerate(maschinen_namen):
        zeile = maschinen_matrix[m]
        print(
            f"      {maschine}: {zeile.min():3d}, {zeile.max():3d}, {zeile.mean():5.0f}"
        )

    # Reshape zu 2D: (Schichten × Alles andere)
    schichten_matrix = produktion_3d.transpose(2, 0, 1).reshape(3, -1)  # 3 × 15
    print(f"\nReshape zu Schichten-Matrix: {schichten_matrix.shape}")
    print("   Pro Schicht - Min, Max, Durchschnitt:")
    for s, schicht in enumerate(schicht_namen):
        zeile = schichten_matrix[s]
        print(
            f"      {schicht}: {zeile.min():3d}, {zeile.max():3d}, {zeile.mean():5.0f}"
        )
    print()

    # TODO 4: Komplexe Filterung
    print("🔍 Komplexe Datenfilterung:")

    # Finde überdurchschnittliche Schichten
    durchschnitt_gesamt = np.mean(produktion_3d)
    ueberdurchschnittlich = produktion_3d > durchschnitt_gesamt

    anzahl_ueber = np.sum(ueberdurchschnittlich)
    print(f"Gesamtdurchschnitt: {durchschnitt_gesamt:.0f} Stück/Schicht")
    print(f"Überdurchschnittliche Schichten: {anzahl_ueber}/{produktion_3d.size}")

    # Details der besten Schichten
    beste_werte = produktion_3d[ueberdurchschnittlich]
    if len(beste_werte) > 0:
        print(f"Beste Schicht-Werte: {beste_werte.max()} Stück")

        # Finde Position der besten Schicht
        beste_position = np.unravel_index(np.argmax(produktion_3d), produktion_3d.shape)
        beste_maschine, bester_tag, beste_schicht = beste_position

        print(
            f"Beste Schicht: {maschinen_namen[beste_maschine]}, {tag_namen[bester_tag]}, {schicht_namen[beste_schicht]}"
        )
        print(f"   Wert: {produktion_3d[beste_position]} Stück")
    print()

    # TODO 5: Datenexport-Vorbereitung
    print("💾 Datenexport-Vorbereitung:")

    # Erstelle strukturierte Tabelle für Export
    export_daten = []
    for m in range(3):
        for t in range(5):
            for s in range(3):
                wert = produktion_3d[m, t, s]
                export_daten.append(
                    [maschinen_namen[m], tag_namen[t], schicht_namen[s], wert]
                )

    export_array = np.array(export_daten)
    print(f"Export-Format: {export_array.shape} (Zeilen × Spalten)")
    print("Spalten: Maschine, Tag, Schicht, Stückzahl")
    print("Erste 5 Zeilen:")
    for i in range(5):
        print(f"   {export_array[i]}")

    # Zusammenfassung für Management
    print("\n📋 Management-Summary:")
    print(f"   • Gesamtproduktion: {np.sum(produktion_3d):,} Stück")
    print(f"   • Durchschnitt/Schicht: {np.mean(produktion_3d):.0f} Stück")
    print(f"   • Beste Maschine: {maschinen_namen[np.argmax(summe_pro_maschine)]}")
    print(f"   • Beste Schicht: {schicht_namen[np.argmax(summe_pro_schicht)]}")
    print(
        f"   • Variationskoeffizient: {np.std(produktion_3d) / np.mean(produktion_3d) * 100:.1f}%"
    )
    print()

    print("✅ Aufgabe 5 abgeschlossen!")
    return produktion_3d, export_array


def main():
    """🚀 Hauptprogramm - Alle Aufgaben ausführen"""
    print("🟢 BEGINNER: Array-Manipulation mit NumPy für SmartFactory")
    print("=" * 70)
    print("📚 Lernen Sie Arrays umzuformen, zu kombinieren und zu filtern!")
    print("🎯 Ziel: Flexible Datenorganisation für komplexe Produktionsanalysen")
    print()

    try:
        # Aufgabe 1: Reshape und Transpose
        tage_matrix, schicht_data = aufgabe_1_reshape_und_transpose()

        # Aufgabe 2: Concatenate und Split
        horizontal_data, vertikal_data = aufgabe_2_concatenate_und_split()

        # Aufgabe 3: Erweiterte Indexierung
        produktions_matrix, top_maschinen = aufgabe_3_erweiterte_indexierung()

        # Aufgabe 4: Datenfilterung
        bereinigte_daten, cp_wert = aufgabe_4_datenfilterung()

        # Aufgabe 5: Praktische Datenorganisation
        produktion_3d, export_daten = aufgabe_5_praktische_datenorganisation()

        # Erfolgreicher Abschluss
        print("\n" + "🎉" * 30)
        print("🎉 HERZLICHEN GLÜCKWUNSCH! 🎉")
        print("🎉" * 30)
        print("✅ Sie haben alle Beginner-Aufgaben zur Array-Manipulation gemeistert!")
        print()
        print("🎓 Sie können jetzt:")
        print("   • Arrays flexibel umformen (reshape, transpose)")
        print("   • Arrays kombinieren und trennen (concatenate, split)")
        print("   • Erweiterte Indexing-Techniken anwenden")
        print("   • Boolean Indexing für Datenfilterung")
        print("   • Komplexe Datenstrukturen organisieren")
        print()
        print("➡️ NÄCHSTE SCHRITTE:")
        print("📚 Übung 4: SmartFactory-Produktionsdaten")
        print(
            "🚀 uv run python exercises/beginner/uebung_04_smartfactory_daten_beginner.py"
        )

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
        print("💡 Sie können jederzeit weitermachen!")

    except Exception as e:
        print(f"\n❌ Fehler aufgetreten: {e}")
        print(
            "💡 Tipp: Überprüfen Sie die Hints in solutions/beginner/uebung_03_hints.md"
        )


if __name__ == "__main__":
    main()
