#!/usr/bin/env python3
"""
🟡 INTERMEDIATE - NumPy Broadcasting - HINT 3 (Code-Snippets)
Übung 1: Broadcasting für Bystronic Produktionsoptimierung

🎯 DETAILLIERTE CODE-BEISPIELE:
"""

import time

import numpy as np


def beispiel_maschinenkalibrierung():
    """📋 Beispiel für Aufgabe 1: Maschinenkalibrierung"""
    print("=" * 60)
    print("🟡 HINT 3: Maschinenkalibrierung mit Broadcasting")
    print("=" * 60)

    # Beispiel-Rohdaten: 4 Maschinen × 8 Stunden
    np.random.seed(42)
    rohdaten = np.random.normal(50, 5, (4, 8)).round(1)
    print("Rohdaten (4 Maschinen × 8 Stunden):")
    print(rohdaten)
    print(f"Shape: {rohdaten.shape}")
    print()

    # Kalibrierungs-Offsets pro Maschine
    kalibrierung_offsets = np.array([2.5, -1.2, 0.8, -0.5])
    print("Kalibrierungs-Offsets pro Maschine:")
    print(kalibrierung_offsets)
    print(f"Shape: {kalibrierung_offsets.shape}")
    print()

    # Broadcasting-Demonstration
    print("🔄 BROADCASTING-KOMPATIBILITÄT:")
    print(f"Rohdaten Shape:    {rohdaten.shape}")
    print(f"Offsets Shape:     {kalibrierung_offsets.shape}")
    print("Für Broadcasting brauchen wir: (4, 8) + (4, 1)")
    print()

    # Methode 1: Explizite Umformung
    print("Methode 1: Explizite reshape")
    offsets_2d = kalibrierung_offsets.reshape(-1, 1)
    print(f"Offsets reshaped:  {offsets_2d.shape}")
    kalibriert_v1 = rohdaten + offsets_2d
    print("Erste 2 Maschinen nach Kalibrierung:")
    print(kalibriert_v1[:2])
    print()

    # Methode 2: newaxis verwenden
    print("Methode 2: Mit np.newaxis")
    kalibriert_v2 = rohdaten + kalibrierung_offsets[:, np.newaxis]
    print(
        "Überprüfung: Ergebnisse identisch?", np.allclose(kalibriert_v1, kalibriert_v2)
    )
    print()

    # Methode 3: Automatisches Broadcasting (funktioniert nicht!)
    print("Methode 3: Warum automatisches Broadcasting hier NICHT funktioniert:")
    try:
        # Das würde einen Fehler geben
        automatisch = rohdaten + kalibrierung_offsets
        print("Automatisch funktioniert:", automatisch.shape)
    except ValueError as e:
        print(f"Fehler: {e}")
        print("Grund: (4,8) und (4,) sind nicht kompatibel für Broadcasting!")
    print()

    # Performance-Vergleich
    print("⚡ PERFORMANCE-VERGLEICH:")

    def mit_broadcasting():
        return rohdaten + kalibrierung_offsets[:, np.newaxis]

    def mit_loop():
        result = np.zeros_like(rohdaten)
        for i in range(rohdaten.shape[0]):
            result[i] = rohdaten[i] + kalibrierung_offsets[i]
        return result

    # Zeitmessungen
    start = time.time()
    for _ in range(1000):
        _ = mit_broadcasting()
    broadcast_time = time.time() - start

    start = time.time()
    for _ in range(1000):
        _ = mit_loop()
    loop_time = time.time() - start

    print(f"Broadcasting: {broadcast_time:.4f}s")
    print(f"Loop:         {loop_time:.4f}s")
    print(f"Speedup:      {loop_time / broadcast_time:.1f}x")

    return kalibriert_v1


def beispiel_schichtweise_normalisierung():
    """📋 Beispiel für Aufgabe 2: Schichtweise Normalisierung"""
    print("\n" + "=" * 60)
    print("🟡 HINT 3: Schichtweise Normalisierung")
    print("=" * 60)

    # 3D-Daten: 3 Schichten × 4 Maschinen × 8 Stunden
    np.random.seed(123)
    base_production = np.random.randint(40, 60, (3, 4, 8))

    # Schichtspezifische Variation hinzufügen
    schicht_faktoren = np.array([1.0, 0.95, 0.85])  # Tag, Spät, Nacht
    for schicht in range(3):
        base_production[schicht] = (
            base_production[schicht] * schicht_faktoren[schicht]
        ).astype(int)

    print("Produktionsdaten (3 Schichten × 4 Maschinen × 8 Stunden):")
    print(f"Shape: {base_production.shape}")
    for schicht in range(3):
        schicht_namen = ["Tagschicht", "Spätschicht", "Nachtschicht"]
        print(f"\n{schicht_namen[schicht]} - Durchschnitt pro Maschine:")
        print(np.mean(base_production[schicht], axis=1).round(1))

    # Normalisierungsfaktoren (auf Tagschicht-Niveau)
    referenz_faktoren = np.array(
        [1.0, 1.0 / 0.95, 1.0 / 0.85]
    )  # Umkehrung der Schichtfaktoren
    print(f"\nNormalisierungsfaktoren: {referenz_faktoren}")
    print(f"Shape: {referenz_faktoren.shape}")
    print()

    # Broadcasting für Normalisierung
    print("🔄 BROADCASTING-NORMALISIERUNG:")
    print(f"Daten Shape:    {base_production.shape}")
    print(f"Faktoren Shape: {referenz_faktoren.shape}")
    print("Benötigt: (3, 4, 8) * (3, 1, 1)")
    print()

    # Faktoren für Broadcasting vorbereiten
    faktoren_3d = referenz_faktoren[:, np.newaxis, np.newaxis]
    print(f"Faktoren 3D Shape: {faktoren_3d.shape}")

    # Normalisierung durchführen
    normalisiert = base_production * faktoren_3d

    print("Nach Normalisierung - Durchschnitt pro Maschine:")
    for schicht in range(3):
        schicht_namen = ["Tagschicht", "Spätschicht", "Nachtschicht"]
        print(
            f"{schicht_namen[schicht]}: {np.mean(normalisiert[schicht], axis=1).round(1)}"
        )

    # Validierung: Alle Schichten sollten ähnliche Durchschnitte haben
    schicht_durchschnitte = np.mean(normalisiert, axis=(1, 2))
    print(
        f"\nSchicht-Gesamtdurchschnitte nach Normalisierung: {schicht_durchschnitte.round(1)}"
    )
    print(f"Standardabweichung zwischen Schichten: {np.std(schicht_durchschnitte):.2f}")

    return normalisiert


def beispiel_effizienz_benchmarking():
    """📋 Beispiel für Aufgabe 3: Effizienz-Benchmarking"""
    print("\n" + "=" * 60)
    print("🟡 HINT 3: Effizienz-Benchmarking")
    print("=" * 60)

    # Ist-Leistung: 5 Maschinen × 12 Monate
    np.random.seed(456)
    ist_leistung = np.random.normal(85, 10, (5, 12)).round(1)
    ist_leistung = np.clip(ist_leistung, 60, 100)  # Realistische Werte

    print("Ist-Leistung (5 Maschinen × 12 Monate, in %):")
    print(ist_leistung)
    print()

    # Verschiedene Soll-Szenarien
    print("🎯 VERSCHIEDENE SOLL-SZENARIEN:")

    # Szenario 1: Feste Sollwerte pro Maschine
    soll_pro_maschine = np.array([90, 85, 88, 92, 87])
    print(f"Szenario 1 - Soll pro Maschine: {soll_pro_maschine}")
    print(f"Shape: {soll_pro_maschine.shape}")

    # Broadcasting: (5, 12) / (5,) -> (5, 12)
    effizienz_maschine = ist_leistung / soll_pro_maschine[:, np.newaxis] * 100
    print("Effizienz pro Maschine (% vom Soll):")
    print(effizienz_maschine.round(1))
    print()

    # Szenario 2: Saisonale Sollwerte (alle Maschinen gleich)
    soll_saisonal = np.array(
        [88, 89, 90, 92, 95, 98, 95, 92, 90, 88, 85, 87]
    )  # 12 Monate
    print(f"Szenario 2 - Saisonale Sollwerte: {soll_saisonal}")
    print(f"Shape: {soll_saisonal.shape}")

    # Broadcasting: (5, 12) / (12,) -> (5, 12)
    effizienz_saisonal = ist_leistung / soll_saisonal[np.newaxis, :] * 100
    print("Effizienz saisonal (% vom Soll):")
    print(effizienz_saisonal.round(1))
    print()

    # Szenario 3: Individuelle Sollwerte (Matrix)
    soll_matrix = np.outer(soll_pro_maschine, np.ones(12)) * (
        soll_saisonal / np.mean(soll_saisonal)
    )
    print("Szenario 3 - Kombinierte Sollwerte (Maschine + Saison):")
    print(f"Shape: {soll_matrix.shape}")

    # Direkter Vergleich (gleiche Shapes)
    effizienz_kombiniert = ist_leistung / soll_matrix * 100
    print("Kombinierte Effizienz:")
    print(effizienz_kombiniert.round(1))
    print()

    # Zusammenfassung der Ergebnisse
    print("📊 EFFIZIENZ-ZUSAMMENFASSUNG:")
    print(f"Durchschn. Effizienz Maschinen-Soll: {np.mean(effizienz_maschine):.1f}%")
    print(f"Durchschn. Effizienz Saison-Soll:    {np.mean(effizienz_saisonal):.1f}%")
    print(f"Durchschn. Effizienz Kombiniert:     {np.mean(effizienz_kombiniert):.1f}%")

    return effizienz_maschine, effizienz_saisonal, effizienz_kombiniert


def beispiel_mehrdimensionale_korrekturen():
    """📋 Beispiel für Aufgabe 4: Mehrdimensionale Korrekturen"""
    print("\n" + "=" * 60)
    print("🟡 HINT 3: Mehrdimensionale Korrekturen")
    print("=" * 60)

    # 4D-Daten: 7 Tage × 3 Schichten × 5 Maschinen × 8 Stunden
    np.random.seed(789)
    rohdaten = np.random.normal(50, 8, (7, 3, 5, 8)).round(1)

    print("Rohdaten (7 Tage × 3 Schichten × 5 Maschinen × 8 Stunden):")
    print(f"Shape: {rohdaten.shape}")
    print(f"Gesamtdurchschnitt: {np.mean(rohdaten):.1f}")
    print()

    # Verschiedene Korrektur-Ebenen definieren
    print("🔧 KORREKTUR-EBENEN DEFINIEREN:")

    # Temperatur-Korrektur pro Tag
    temperatur_korrektur = np.array([0.5, -1.2, 0.8, -0.3, 1.1, -0.7, 0.2])
    print(f"Temperatur-Korrektur (7 Tage): {temperatur_korrektur}")

    # Schicht-Korrektur
    schicht_korrektur = np.array([0.0, -0.5, -1.0])  # Tag, Spät, Nacht
    print(f"Schicht-Korrektur (3 Schichten): {schicht_korrektur}")

    # Maschinen-Kalibrierung
    maschinen_korrektur = np.array([1.2, -0.8, 0.5, -0.3, 0.9])
    print(f"Maschinen-Korrektur (5 Maschinen): {maschinen_korrektur}")

    # Stunden-basierte Drift-Korrektur
    stunden_korrektur = np.array([0.0, 0.1, 0.2, 0.2, 0.1, 0.3, 0.4, 0.5])
    print(f"Stunden-Korrektur (8 Stunden): {stunden_korrektur}")
    print()

    # Shapes für Broadcasting vorbereiten
    print("🔄 BROADCASTING-SHAPES VORBEREITEN:")
    temp_korr = temperatur_korrektur[:, np.newaxis, np.newaxis, np.newaxis]
    schicht_korr = schicht_korrektur[np.newaxis, :, np.newaxis, np.newaxis]
    masch_korr = maschinen_korrektur[np.newaxis, np.newaxis, :, np.newaxis]
    stunden_korr = stunden_korrektur[np.newaxis, np.newaxis, np.newaxis, :]

    print(f"Original:      {rohdaten.shape}")
    print(f"Temperatur:    {temp_korr.shape}")
    print(f"Schicht:       {schicht_korr.shape}")
    print(f"Maschinen:     {masch_korr.shape}")
    print(f"Stunden:       {stunden_korr.shape}")
    print()

    # Korrekturen anwenden
    print("⚡ KORREKTUREN ANWENDEN:")

    # Schritt für Schritt
    nach_temp = rohdaten + temp_korr
    nach_schicht = nach_temp + schicht_korr
    nach_maschinen = nach_schicht + masch_korr
    korrigierte_daten = nach_maschinen + stunden_korr

    print(f"Nach Temperatur-Korrektur: Ø {np.mean(nach_temp):.1f}")
    print(f"Nach Schicht-Korrektur:    Ø {np.mean(nach_schicht):.1f}")
    print(f"Nach Maschinen-Korrektur:  Ø {np.mean(nach_maschinen):.1f}")
    print(f"Final korrigiert:          Ø {np.mean(korrigierte_daten):.1f}")
    print()

    # Alternative: Alle Korrekturen in einem Schritt
    print("🚀 ALTERNATIVE: Kombinierte Korrektur in einem Schritt")
    korrigiert_einschritt = (
        rohdaten + temp_korr + schicht_korr + masch_korr + stunden_korr
    )

    # Verifikation
    identisch = np.allclose(korrigierte_daten, korrigiert_einschritt)
    print(f"Ergebnisse identisch: {identisch}")
    print()

    # Analyse der Korrekturen
    print("📊 KORREKTUR-ANALYSE:")
    gesamt_korrektur = korrigierte_daten - rohdaten
    print(f"Durchschnittliche Gesamt-Korrektur: {np.mean(gesamt_korrektur):.2f}")
    print(
        f"Korrektur-Spannweite: {np.min(gesamt_korrektur):.2f} bis {np.max(gesamt_korrektur):.2f}"
    )

    # Korrektur-Effekt pro Dimension
    temp_effekt = np.mean(gesamt_korrektur, axis=(1, 2, 3))
    schicht_effekt = np.mean(gesamt_korrektur, axis=(0, 2, 3))
    maschinen_effekt = np.mean(gesamt_korrektur, axis=(0, 1, 3))

    print(f"Temperatur-Effekt pro Tag: {temp_effekt.round(2)}")
    print(f"Schicht-Effekt: {schicht_effekt.round(2)}")
    print(f"Maschinen-Effekt: {maschinen_effekt.round(2)}")

    return korrigierte_daten, gesamt_korrektur


def beispiel_memory_effizienz():
    """📋 Beispiel für Aufgabe 5: Memory-effiziente Operationen"""
    print("\n" + "=" * 60)
    print("🟡 HINT 3: Memory-effiziente Broadcasting-Operationen")
    print("=" * 60)

    # Große Datenmengen simulieren
    print("💾 MEMORY-EFFIZIENZ DEMONSTRATION:")

    # Mittlere Datengröße
    daten = np.random.random((1000, 500))  # 1000 × 500 = 500,000 Elemente
    faktoren = np.random.random(500)  # 500 Elemente

    print(f"Daten Shape: {daten.shape}")
    print(f"Faktoren Shape: {faktoren.shape}")
    print(f"Daten Memory: ~{daten.nbytes / 1024**2:.1f} MB")
    print(f"Faktoren Memory: ~{faktoren.nbytes / 1024:.1f} KB")
    print()

    # Ineffiziente Methode: Explizite Vervielfältigung
    print("❌ INEFFIZIENTE METHODE:")
    start_time = time.time()

    # Faktoren auf Datengröße erweitern (erstellt Kopie!)
    faktoren_expanded = np.tile(faktoren, (1000, 1))
    result_ineffizient = daten * faktoren_expanded

    ineffizient_time = time.time() - start_time
    print(f"Expanded Faktoren Memory: ~{faktoren_expanded.nbytes / 1024**2:.1f} MB")
    print(f"Zeit: {ineffizient_time:.4f}s")
    print()

    # Effiziente Methode: Broadcasting
    print("✅ EFFIZIENTE METHODE (Broadcasting):")
    start_time = time.time()

    # Direktes Broadcasting - keine Kopien!
    result_broadcast = daten * faktoren[np.newaxis, :]

    broadcast_time = time.time() - start_time
    print("Zusätzlicher Memory: 0 MB (nur Views)")
    print(f"Zeit: {broadcast_time:.4f}s")
    print(f"Speedup: {ineffizient_time / broadcast_time:.1f}x")
    print()

    # Verifikation
    print("🔍 ERGEBNIS-VERIFIKATION:")
    identisch = np.allclose(result_ineffizient, result_broadcast)
    print(f"Ergebnisse identisch: {identisch}")

    # Memory-Footprint Vergleich
    print("\nMemory-Vergleich:")
    print(f"Ineffizient: {(daten.nbytes + faktoren_expanded.nbytes) / 1024**2:.1f} MB")
    print(f"Broadcast:   {daten.nbytes / 1024**2:.1f} MB")
    memory_saving = (faktoren_expanded.nbytes) / 1024**2
    print(f"Ersparnis:   {memory_saving:.1f} MB")

    # In-place Operationen
    print("\n⚡ IN-PLACE OPERATIONEN:")
    daten_copy = daten.copy()

    start_time = time.time()
    daten_copy *= faktoren[np.newaxis, :]  # In-place Multiplikation
    inplace_time = time.time() - start_time

    print(f"In-place Zeit: {inplace_time:.4f}s")
    print("Memory-Overhead: 0 (modifiziert Original)")
    print("Hinweis: Verwende in-place nur wenn Original nicht mehr benötigt wird!")

    return result_broadcast


def broadcasting_shape_tricks():
    """Nützliche Shape-Manipulation Tricks"""
    print("\n" + "=" * 60)
    print("🟡 HINT 3: Broadcasting Shape-Tricks")
    print("=" * 60)

    print("🛠️ NÜTZLICHE SHAPE-TRICKS:")

    # Beispiel-Array
    arr = np.arange(24).reshape(4, 6)
    print(f"Basis-Array: {arr.shape}")
    print(arr)
    print()

    # Verschiedene Broadcasting-Vorbereitungen
    print("Shape-Manipulation Techniken:")

    # Spaltenvektor
    col_vector = np.array([1, 2, 3, 4])
    print(f"1. Spaltenvektor: {col_vector.shape} -> {col_vector[:, np.newaxis].shape}")

    # Zeilenvektor
    row_vector = np.array([10, 20, 30, 40, 50, 60])
    print(f"2. Zeilenvektor: {row_vector.shape} -> {row_vector[np.newaxis, :].shape}")

    # Mehrere neue Dimensionen
    scalar_like = np.array([100])
    print(
        f"3. Pseudo-Skalar: {scalar_like.shape} -> {scalar_like[:, np.newaxis, np.newaxis].shape}"
    )

    # Mit reshape
    print(f"4. Reshape-Trick: {col_vector.shape} -> {col_vector.reshape(-1, 1).shape}")

    # expand_dims
    print(
        f"5. expand_dims: {row_vector.shape} -> {np.expand_dims(row_vector, 0).shape}"
    )
    print()

    # Praktische Anwendung
    print("🔧 PRAKTISCHE ANWENDUNG:")
    result1 = arr + col_vector[:, np.newaxis]  # Broadcasting über Spalten
    result2 = arr + row_vector[np.newaxis, :]  # Broadcasting über Zeilen

    print("Broadcasting über Spalten (jede Zeile + Wert):")
    print(result1)
    print("\nBroadcasting über Zeilen (jede Spalte + Wert):")
    print(result2)


if __name__ == "__main__":
    # Alle Beispiele ausführen
    print("🎯 ALLE BROADCASTING-BEISPIELE:")

    kalibriert = beispiel_maschinenkalibrierung()
    normalisiert = beispiel_schichtweise_normalisierung()
    effizienz_results = beispiel_effizienz_benchmarking()
    korrigiert, korrekturen = beispiel_mehrdimensionale_korrekturen()
    memory_result = beispiel_memory_effizienz()
    broadcasting_shape_tricks()

    print("\n" + "=" * 60)
    print("🎉 ALLE CODE-BEISPIELE ABGESCHLOSSEN!")
    print("Verwende diese Patterns für elegante Broadcasting-Lösungen.")
    print("=" * 60)
