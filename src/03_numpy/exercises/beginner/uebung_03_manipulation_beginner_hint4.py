#!/usr/bin/env python3
"""
🟢 BEGINNER - NumPy Array-Manipulation - HINT 4 (Fast vollständige Lösung)
Übung 3: Array-Manipulation für Bystronic Produktionsdaten

🎯 FAST VOLLSTÄNDIGE LÖSUNG mit TODO-Bereichen:
Nur wenige Zeilen müssen noch ergänzt werden!
"""

import numpy as np


def aufgabe_1_reshape_und_transpose():
    """🎯 Aufgabe 1: Arrays umformen und transponieren - FAST VOLLSTÄNDIG"""
    print("=" * 60)
    print("🟢 AUFGABE 1: Reshape und Transpose - LÖSUNG")
    print("=" * 60)

    # Stündliche Produktionsdaten für 3 Tage (24 Stunden × 3 Tage = 72 Werte)
    stuendliche_daten = np.arange(1, 73)  # 1 bis 72
    print("📊 Stündliche Produktionsdaten (3 Tage):")
    print(f"Linear: {stuendliche_daten[:12]}... (72 Werte total)")
    print(f"Shape: {stuendliche_daten.shape}")
    print()

    # TODO 1: Reshape zu 3 Tage × 24 Stunden
    print("🔄 Reshape zu Tage × Stunden Matrix:")
    tage_stunden = stuendliche_daten.reshape(
        3, 24
    )  # TODO: Ergänze die reshape-Parameter
    print(f"Shape nach Reshape: {tage_stunden.shape}")
    print("Erste 8 Stunden pro Tag:")
    for tag in range(3):
        print(f"   Tag {tag + 1}: {tage_stunden[tag, :8]}")
    print()

    # TODO 2: Alternative Reshape zu 24 Stunden × 3 Tage
    print("🔄 Alternative: Stunden × Tage Matrix:")
    stunden_tage = stuendliche_daten.reshape(
        24, 3
    )  # TODO: Ergänze die reshape-Parameter
    print(f"Shape: {stunden_tage.shape}")
    print("Erste 8 Stunden für alle Tage:")
    print(stunden_tage[:8])  # Erste 8 Zeilen (Stunden)
    print()

    # TODO 3: Transponiere die erste Matrix
    print("🔄 Transponieren der Tage×Stunden Matrix:")
    transponiert = tage_stunden.T  # TODO: Ergänze .T oder .transpose()
    print(f"Shape nach Transpose: {transponiert.shape}")
    print("Erste 8 Stunden für alle Tage (transponiert):")
    print(transponiert[:8])

    print("\n✅ Aufgabe 1 abgeschlossen!")
    return tage_stunden, transponiert


def aufgabe_2_arrays_kombinieren():
    """🎯 Aufgabe 2: Arrays kombinieren - FAST VOLLSTÄNDIG"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 2: Arrays kombinieren - LÖSUNG")
    print("=" * 60)

    # Produktionsdaten für 2 Schichten
    schicht_1 = np.array(
        [
            [45, 52, 48, 55],  # Maschine 1
            [38, 41, 44, 39],  # Maschine 2
            [62, 58, 61, 59],
        ]
    )  # Maschine 3

    schicht_2 = np.array(
        [
            [51, 49, 53, 47],  # Maschine 1
            [42, 45, 40, 46],  # Maschine 2
            [65, 63, 67, 64],
        ]
    )  # Maschine 3

    print("Schicht 1 (3 Maschinen × 4 Stunden):")
    print(schicht_1)
    print("Schicht 2 (3 Maschinen × 4 Stunden):")
    print(schicht_2)
    print()

    # TODO 1: Horizontal kombinieren (beide Schichten nebeneinander)
    print("🔗 Horizontal kombinieren (8 Stunden pro Maschine):")
    beide_schichten = np.concatenate(
        [schicht_1, schicht_2], axis=1
    )  # TODO: Ergänze axis-Parameter
    print(f"Shape: {beide_schichten.shape}")
    print(beide_schichten)
    print()

    # TODO 2: Vertikal kombinieren (weitere Maschinen hinzufügen)
    zusaetzliche_maschinen = np.array(
        [
            [35, 37, 33, 36],  # Maschine 4
            [58, 56, 61, 59],
        ]
    )  # Maschine 5

    print("🔗 Vertikal kombinieren (5 Maschinen total):")
    alle_maschinen = np.concatenate(
        [schicht_1, zusaetzliche_maschinen], axis=0
    )  # TODO: Ergänze axis-Parameter
    print(f"Shape: {alle_maschinen.shape}")
    print(alle_maschinen)

    print("\n✅ Aufgabe 2 abgeschlossen!")
    return beide_schichten, alle_maschinen


def aufgabe_3_boolean_indexing():
    """🎯 Aufgabe 3: Boolean Indexing für Qualitätskontrolle - FAST VOLLSTÄNDIG"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 3: Boolean Indexing - LÖSUNG")
    print("=" * 60)

    # Qualitätsmessungen (Präzision in mm)
    np.random.seed(42)  # Für reproduzierbare Ergebnisse
    messungen = np.random.normal(0.1, 0.03, 50)  # 50 Messungen um 0.1mm
    messungen = np.round(messungen, 4)  # Auf 4 Dezimalstellen runden

    print("📊 50 Qualitätsmessungen (Präzision in mm):")
    print(f"Erste 10: {messungen[:10]}")
    print(f"Mittelwert: {np.mean(messungen):.4f} mm")
    print(f"Standardabweichung: {np.std(messungen):.4f} mm")
    print()

    # TODO 1: Ausreißer identifizieren (außerhalb ±0.05mm vom Sollwert 0.1mm)
    sollwert = 0.1
    toleranz = 0.05

    print(f"🎯 Ausreißer-Analyse (Sollwert: {sollwert} ± {toleranz} mm):")
    ausreisser_mask = (messungen < sollwert - toleranz) | (
        messungen > sollwert + toleranz
    )  # TODO: Ergänze Bedingung
    ausreisser = messungen[ausreisser_mask]

    print(f"Anzahl Ausreißer: {np.sum(ausreisser_mask)} von {len(messungen)}")
    print(f"Ausreißer-Rate: {np.mean(ausreisser_mask):.2%}")
    if len(ausreisser) > 0:
        print(f"Ausreißer-Werte: {ausreisser}")
    print()

    # TODO 2: Gute Messungen filtern
    gute_messungen_mask = ~ausreisser_mask  # TODO: Ergänze ~ (Negation)
    gute_messungen = messungen[gute_messungen_mask]

    print(f"✅ Gute Messungen: {len(gute_messungen)} von {len(messungen)}")
    print(f"Mittelwert (nur gute): {np.mean(gute_messungen):.4f} mm")
    print(f"Standardabweichung (nur gute): {np.std(gute_messungen):.4f} mm")
    print()

    # TODO 3: Kategorisierung in Qualitätsstufen
    exzellent = (messungen >= 0.095) & (messungen <= 0.105)  # TODO: Ergänze Bedingung
    gut = ((messungen >= 0.09) & (messungen < 0.095)) | (
        (messungen > 0.105) & (messungen <= 0.11)
    )
    akzeptabel = ~exzellent & ~gut & ~ausreisser_mask

    print("📊 Qualitätskategorisierung:")
    print(
        f"Exzellent (0.095-0.105): {np.sum(exzellent)} Stück ({np.mean(exzellent):.1%})"
    )
    print(f"Gut (0.09-0.095, 0.105-0.11): {np.sum(gut)} Stück ({np.mean(gut):.1%})")
    print(
        f"Akzeptabel (Rest in Toleranz): {np.sum(akzeptabel)} Stück ({np.mean(akzeptabel):.1%})"
    )
    print(
        f"Ausschuss (Ausreißer): {np.sum(ausreisser_mask)} Stück ({np.mean(ausreisser_mask):.1%})"
    )

    print("\n✅ Aufgabe 3 abgeschlossen!")
    return messungen, ausreisser, gute_messungen


def aufgabe_4_erweiterte_manipulation():
    """🎯 Aufgabe 4: Erweiterte Array-Manipulation - FAST VOLLSTÄNDIG"""
    print("\n" + "=" * 60)
    print("🟢 AUFGABE 4: Erweiterte Manipulation - LÖSUNG")
    print("=" * 60)

    # Wöchentliche Produktionsdaten (5 Tage × 3 Schichten × 4 Stunden)
    np.random.seed(123)
    produktion_woche = np.random.randint(40, 70, size=(5, 3, 4))

    print("📊 Produktionsdaten (5 Tage × 3 Schichten × 4 Stunden):")
    for tag in range(5):
        print(f"Tag {tag + 1}: {produktion_woche[tag]}")
    print(f"Shape: {produktion_woche.shape}")
    print()

    # TODO 1: Daten aufteilen in erste und zweite Wochenhälfte
    print("✂️ Woche aufteilen:")
    erste_haelfte = produktion_woche[:3]  # TODO: Ergänze Slice für erste 3 Tage
    zweite_haelfte = produktion_woche[3:]  # TODO: Ergänze Slice für letzte 2 Tage

    print(f"Erste Hälfte Shape: {erste_haelfte.shape}")
    print(f"Zweite Hälfte Shape: {zweite_haelfte.shape}")
    print()

    # TODO 2: Statistiken pro Dimension berechnen
    print("📊 Statistiken pro Dimension:")

    # Pro Tag (über alle Schichten und Stunden)
    pro_tag = np.mean(produktion_woche, axis=(1, 2))  # TODO: Ergänze axis-Parameter
    print(f"Durchschnitt pro Tag: {pro_tag}")

    # Pro Schicht (über alle Tage und Stunden)
    pro_schicht = np.mean(produktion_woche, axis=(0, 2))  # TODO: Ergänze axis-Parameter
    print(f"Durchschnitt pro Schicht: {pro_schicht}")

    # Pro Stunde (über alle Tage und Schichten)
    pro_stunde = np.mean(produktion_woche, axis=(0, 1))  # TODO: Ergänze axis-Parameter
    print(f"Durchschnitt pro Stunde: {pro_stunde}")
    print()

    # TODO 3: Beste und schlechteste Performance finden
    print("🏆 Performance-Analyse:")
    flache_daten = produktion_woche.flatten()  # TODO: Ergänze .flatten()

    bester_tag_idx = np.unravel_index(
        np.argmax(produktion_woche), produktion_woche.shape
    )
    schlechtester_tag_idx = np.unravel_index(
        np.argmin(produktion_woche), produktion_woche.shape
    )

    print(f"Höchste Produktion: {np.max(produktion_woche)} Stück")
    print(
        f"Position: Tag {bester_tag_idx[0] + 1}, Schicht {bester_tag_idx[1] + 1}, Stunde {bester_tag_idx[2] + 1}"
    )
    print(f"Niedrigste Produktion: {np.min(produktion_woche)} Stück")
    print(
        f"Position: Tag {schlechtester_tag_idx[0] + 1}, Schicht {schlechtester_tag_idx[1] + 1}, Stunde {schlechtester_tag_idx[2] + 1}"
    )

    # TODO 4: Sortierte Übersicht erstellen
    print("\n📈 Top/Bottom Performer:")
    sortierte_indices = np.argsort(flache_daten)  # TODO: Ergänze np.argsort()

    print("Top 5 Produktionsstunden:")
    for i in range(-5, 0):  # Letzten 5 (höchste Werte)
        idx = sortierte_indices[i]
        original_idx = np.unravel_index(idx, produktion_woche.shape)
        wert = flache_daten[idx]
        print(
            f"  {wert} Stück - Tag {original_idx[0] + 1}, Schicht {original_idx[1] + 1}, Stunde {original_idx[2] + 1}"
        )

    print("\n✅ Aufgabe 4 abgeschlossen!")
    return produktion_woche, pro_tag, pro_schicht, pro_stunde


def zusammenfassung_und_tipps():
    """Zusammenfassung der wichtigsten Lösungsansätze"""
    print("\n" + "=" * 60)
    print("🟢 ZUSAMMENFASSUNG: Wichtigste Techniken")
    print("=" * 60)

    print("🔧 ARRAY-MANIPULATION MASTERY:")
    print("✅ reshape() - Dimensionen ändern ohne Daten zu verändern")
    print("✅ transpose() / .T - Zeilen und Spalten vertauschen")
    print("✅ concatenate() - Arrays entlang verschiedener Achsen verbinden")
    print("✅ Boolean Indexing - Daten nach Bedingungen filtern")
    print("✅ split() / array_split() - Arrays in Teile aufteilen")
    print("✅ axis-Parameter - Operationen entlang bestimmter Dimensionen")
    print()

    print("💡 PRAKTISCHE TIPPS:")
    print("• Immer zuerst die Shapes überprüfen")
    print("• Mit kleinen Testdaten beginnen")
    print("• Eine Operation nach der anderen")
    print("• Aussagekräftige Variablennamen verwenden")
    print("• Boolean Masks für komplexe Filterungen")
    print("• axis=0 für Zeilen, axis=1 für Spalten")


if __name__ == "__main__":
    # Alle Aufgaben ausführen
    tage_stunden, transponiert = aufgabe_1_reshape_und_transpose()
    beide_schichten, alle_maschinen = aufgabe_2_arrays_kombinieren()
    messungen, ausreisser, gute_messungen = aufgabe_3_boolean_indexing()
    produktion_woche, pro_tag, pro_schicht, pro_stunde = (
        aufgabe_4_erweiterte_manipulation()
    )

    zusammenfassung_und_tipps()

    print("\n" + "=" * 60)
    print("🎉 ALLE AUFGABEN ABGESCHLOSSEN!")
    print("🎯 Du beherrschst jetzt Array-Manipulation in NumPy!")
    print("=" * 60)
