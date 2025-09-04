#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Beispiel: NumPy Array-Grundlagen

Dieses Skript demonstriert die Grundlagen von NumPy-Arrays
für typische Bystronic-Anwendungen wie Messdaten, Koordinaten
und Maschinendaten.
"""

import numpy as np


def main() -> None:
    print("=" * 60)
    print("BYSTRONIC - NUMPY ARRAY-GRUNDLAGEN")
    print("=" * 60)

    # 1. Array-Erstellung aus Listen
    print("\n1️⃣ Array-Erstellung aus Listen")
    print("-" * 40)

    # Messwerte einer Qualitätskontrolle
    messwerte_liste = [2.05, 1.98, 2.02, 2.07, 1.95, 2.01, 2.04, 1.99]
    messwerte_array = np.array(messwerte_liste)

    print(f"Python-Liste: {messwerte_liste}")
    print(f"NumPy-Array:  {messwerte_array}")
    print(f"Array-Typ:    {type(messwerte_array)}")
    print(f"Element-Typ:  {messwerte_array.dtype}")
    print(f"Array-Shape:  {messwerte_array.shape}")

    # 2. Verschiedene Array-Erstellungsmethoden
    print("\n2️⃣ Array-Erstellungsmethoden")
    print("-" * 40)

    # Nullen für Initialisierung
    produktionszeiten = np.zeros(7)  # 7 Tage
    print(f"Nullen-Array (7 Tage):     {produktionszeiten}")

    # Einsen für Standardwerte
    effizienz = np.ones(5) * 0.85  # 5 Maschinen mit 85% Effizienz
    print(f"Effizienz-Array (85%):     {effizienz}")

    # Sequenzen für Zeitreihen
    stunden = np.arange(8, 17)  # Arbeitszeit 8-16 Uhr
    print(f"Arbeitsstunden:            {stunden}")

    # Linear verteilte Werte
    temperaturen = np.linspace(20, 80, 7)  # 20-80°C in 7 Schritten
    print(f"Temperaturreihe:           {temperaturen}")

    # 3. Zufällige Daten für Simulation
    print("\n3️⃣ Zufällige Daten generieren")
    print("-" * 40)

    # Zufällige Messwerte (normalverteilt)
    np.random.seed(42)  # Für reproduzierbare Ergebnisse
    messwerte_simulation = np.random.normal(2.0, 0.05, 20)  # Mittel=2.0, StdDev=0.05
    print(f"Simulierte Messwerte (20): {messwerte_simulation[:5]}... (erste 5)")
    print(f"Mittelwert: {messwerte_simulation.mean():.3f}")
    print(f"Std.abw.:   {messwerte_simulation.std():.3f}")

    # Zufällige ganze Zahlen (Stückzahlen)
    stueckzahlen = np.random.randint(800, 1200, 10)  # 800-1199 Stück
    print(f"Stückzahlen pro Tag:       {stueckzahlen}")

    # 4. Mehrdimensionale Arrays
    print("\n4️⃣ Mehrdimensionale Arrays")
    print("-" * 40)

    # 2D-Array für Maschinendaten (5 Maschinen, 3 Kennwerte)
    maschinendaten = np.array(
        [
            [8.5, 0.92, 45.2],  # Maschine 1: Laufzeit, Effizienz, Energieverbrauch
            [7.2, 0.88, 38.7],  # Maschine 2
            [9.1, 0.95, 52.3],  # Maschine 3
            [6.8, 0.85, 35.1],  # Maschine 4
            [8.3, 0.90, 47.8],  # Maschine 5
        ]
    )

    print(f"Maschinendaten (5x3):\n{maschinendaten}")
    print(f"Shape: {maschinendaten.shape}")
    print(f"Dimensionen: {maschinendaten.ndim}")
    print(f"Gesamtelemente: {maschinendaten.size}")

    # Spalten extrahieren
    laufzeiten = maschinendaten[:, 0]  # Erste Spalte (alle Zeilen)
    effizienzen = maschinendaten[:, 1]  # Zweite Spalte

    print(f"\nLaufzeiten:   {laufzeiten}")
    print(f"Effizienzen:  {effizienzen}")

    # 5. Array-Eigenschaften und -Informationen
    print("\n5️⃣ Array-Eigenschaften")
    print("-" * 40)

    qualitaetsdaten = np.random.normal(50, 10, (4, 6))  # 4 Teile, 6 Messungen

    print(f"Qualitätsdaten Shape:      {qualitaetsdaten.shape}")
    print(f"Datentyp:                  {qualitaetsdaten.dtype}")
    print(f"Speicherbedarf:            {qualitaetsdaten.nbytes} Bytes")
    print(f"Itemsize:                  {qualitaetsdaten.itemsize} Bytes pro Element")

    # 6. Array-Kopien vs Views
    print("\n6️⃣ Array-Kopien vs Views")
    print("-" * 40)

    original = np.array([1, 2, 3, 4, 5])

    # View (teilt Speicher)
    view = original[1:4]
    print(f"Original:     {original}")
    print(f"View:         {view}")

    # Änderung im View beeinflusst Original
    view[0] = 999
    print("Nach View-Änderung:")
    print(f"Original:     {original}")
    print(f"View:         {view}")

    # Kopie (eigener Speicher)
    original = np.array([1, 2, 3, 4, 5])  # Zurücksetzen
    kopie = original.copy()
    kopie[0] = 888
    print("\nNach Kopie-Änderung:")
    print(f"Original:     {original}")
    print(f"Kopie:        {kopie}")

    # 7. Datentypen optimieren
    print("\n7️⃣ Datentypen optimieren")
    print("-" * 40)

    # Standard: float64 (8 Bytes pro Element)
    standard = np.array([1.5, 2.7, 3.2])
    print(f"Standard float64: {standard.dtype}, {standard.nbytes} Bytes")

    # Optimiert: float32 (4 Bytes pro Element)
    optimiert = np.array([1.5, 2.7, 3.2], dtype=np.float32)
    print(f"Float32:      {optimiert.dtype}, {optimiert.nbytes} Bytes")

    # Ganzzahlen: verschiedene Größen
    kleine_zahlen = np.array([1, 2, 3, 4, 5], dtype=np.int8)  # -128 bis 127
    grosse_zahlen = np.array([1000, 2000, 3000], dtype=np.int32)

    print(f"Int8:         {kleine_zahlen.dtype}, {kleine_zahlen.nbytes} Bytes")
    print(f"Int32:        {grosse_zahlen.dtype}, {grosse_zahlen.nbytes} Bytes")

    # 8. Praktisches Beispiel: Koordinatensystem
    print("\n8️⃣ Praktisches Beispiel: 2D-Koordinaten")
    print("-" * 40)

    # Schnittkoordinaten für CNC-Programmierung
    punkte = np.array(
        [
            [0, 0],  # Startpunkt
            [50, 0],  # Rechts
            [50, 30],  # Hoch
            [25, 45],  # Diagonal
            [0, 30],  # Links
            [0, 0],  # Zurück zum Start
        ]
    )

    print("Schnittkoordinaten (X, Y):")
    for i, punkt in enumerate(punkte):
        print(f"  P{i}: ({punkt[0]:2.0f}, {punkt[1]:2.0f})")

    # Entfernungen zwischen aufeinanderfolgenden Punkten
    entfernungen = np.sqrt(np.sum(np.diff(punkte, axis=0) ** 2, axis=1))
    gesamtentfernung = np.sum(entfernungen)

    print(f"\nTeilentfernungen: {entfernungen}")
    print(f"Gesamtschnittlänge: {gesamtentfernung:.1f} mm")

    print(f"\n{'=' * 60}")
    print("✅ Array-Grundlagen erfolgreich demonstriert!")
    print("💡 NumPy-Arrays sind effizienter als Python-Listen")
    print("📊 Perfekt für numerische Berechnungen und Datenanalyse")


if __name__ == "__main__":
    main()
