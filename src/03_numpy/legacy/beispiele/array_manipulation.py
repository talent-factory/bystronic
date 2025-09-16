#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Beispiel: Array-Manipulation mit NumPy

Dieses Skript zeigt fortgeschrittene Array-Operationen wie
Reshaping, Slicing, Indexing und Broadcasting für industrielle
Datenverarbeitung.
"""

import numpy as np


def main() -> None:
    print("=" * 60)
    print("BYSTRONIC - ARRAY-MANIPULATION MIT NUMPY")
    print("=" * 60)

    # 1. Indexing und Slicing (Erweitert)
    print("\n1️⃣ Indexing und Slicing")
    print("-" * 40)

    # Produktionsdaten: 7 Tage, 3 Schichten, 4 Maschinen
    produktionsdaten = np.random.randint(800, 1200, size=(7, 3, 4))
    print(f"Produktionsdaten Shape: {produktionsdaten.shape}")
    print("(7 Tage, 3 Schichten, 4 Maschinen)\n")

    # Einzelne Elemente
    tag_1_schicht_2_maschine_3 = produktionsdaten[0, 1, 2]
    print(f"Tag 1, Schicht 2, Maschine 3: {tag_1_schicht_2_maschine_3} Stück")

    # Slicing: Erste 3 Tage, alle Schichten, Maschine 1
    erste_3_tage_m1 = produktionsdaten[:3, :, 0]
    print(f"Erste 3 Tage, Maschine 1:\n{erste_3_tage_m1}")

    # Negative Indizes: Letzten 2 Tage
    letzte_2_tage = produktionsdaten[-2:, :, :]
    print(f"Letzte 2 Tage Shape: {letzte_2_tage.shape}")

    # 2. Boolean Indexing (Filtering)
    print("\n2️⃣ Boolean Indexing - Daten filtern")
    print("-" * 40)

    # Qualitätsmessdaten
    messwerte = np.array([2.05, 1.95, 2.12, 1.88, 2.03, 1.92, 2.08, 2.15])
    sollwert = 2.0
    toleranz = 0.1

    print(f"Messwerte:        {messwerte}")
    print(f"Sollwert:         {sollwert} ± {toleranz}")

    # Boolean-Arrays erstellen
    zu_hoch = messwerte > (sollwert + toleranz)
    zu_niedrig = messwerte < (sollwert - toleranz)
    in_toleranz = (messwerte >= sollwert - toleranz) & (
        messwerte <= sollwert + toleranz
    )

    print(f"Zu hoch:          {zu_hoch}")
    print(f"Zu niedrig:       {zu_niedrig}")
    print(f"In Toleranz:      {in_toleranz}")

    # Werte extrahieren
    ausreisser = messwerte[zu_hoch | zu_niedrig]
    gute_werte = messwerte[in_toleranz]

    print(f"Ausreißer:        {ausreisser}")
    print(f"Gute Werte:       {gute_werte}")
    print(f"Ausschussrate:    {len(ausreisser) / len(messwerte) * 100:.1f}%")

    # 3. Reshaping - Array-Form ändern
    print("\n3️⃣ Reshaping - Array-Form ändern")
    print("-" * 40)

    # Maschinendaten umformen
    linear_daten = np.arange(1, 25)  # 24 Werte
    print(f"Lineare Daten:    {linear_daten}")
    print(f"Shape:            {linear_daten.shape}")

    # Verschiedene Formen
    matrix_4x6 = linear_daten.reshape(4, 6)  # 4 Zeilen, 6 Spalten
    print(f"\n4x6 Matrix:\n{matrix_4x6}")

    matrix_2x3x4 = linear_daten.reshape(2, 3, 4)  # 3D: 2 Ebenen, 3 Zeilen, 4 Spalten
    print(f"\n2x3x4 3D-Array Shape: {matrix_2x3x4.shape}")
    print(f"Erste Ebene:\n{matrix_2x3x4[0]}")

    # Automatische Dimension mit -1
    auto_reshape = linear_daten.reshape(-1, 8)  # Automatisch 3x8
    print(f"Auto-Reshape (-1, 8): {auto_reshape.shape}")
    print(f"Ergebnis:\n{auto_reshape}")

    # 4. Transponierung
    print("\n4️⃣ Transponierung")
    print("-" * 40)

    # Maschinendaten: 5 Maschinen, 3 Kennwerte
    maschinen_kennwerte = np.array(
        [
            [8.5, 0.92, 45.2],  # Maschine 1
            [7.2, 0.88, 38.7],  # Maschine 2
            [9.1, 0.95, 52.3],  # Maschine 3
            [6.8, 0.85, 35.1],  # Maschine 4
            [8.3, 0.90, 47.8],  # Maschine 5
        ]
    )

    print("Original (Maschinen x Kennwerte):")
    print(maschinen_kennwerte)
    print(f"Shape: {maschinen_kennwerte.shape}")

    # Transponiert: Kennwerte x Maschinen
    transponiert = maschinen_kennwerte.T  # oder .transpose()
    print("\nTransponiert (Kennwerte x Maschinen):")
    print(transponiert)
    print(f"Shape: {transponiert.shape}")

    # Kennwerte einzeln extrahieren
    laufzeiten = transponiert[0]  # Erste Zeile = alle Laufzeiten
    effizienzen = transponiert[1]  # Zweite Zeile = alle Effizienzen
    energien = transponiert[2]  # Dritte Zeile = alle Energiewerte

    print(f"\nLaufzeiten:   {laufzeiten}")
    print(f"Effizienzen:  {effizienzen}")
    print(f"Energien:     {energien}")

    # 5. Concatenation - Arrays zusammenfügen
    print("\n5️⃣ Arrays zusammenfügen")
    print("-" * 40)

    # Produktionsdaten verschiedener Monate
    januar = np.array([[1000, 1100], [950, 1050]])
    februar = np.array([[1200, 1150], [1080, 1190]])
    maerz = np.array([[1300, 1250], [1220, 1280]])

    print("Januar:")
    print(januar)
    print("Februar:")
    print(februar)
    print("März:")
    print(maerz)

    # Horizontal zusammenfügen (axis=1)
    horizontal = np.concatenate([januar, februar, maerz], axis=1)
    print(f"\nHorizontal zusammengefügt:\n{horizontal}")
    print(f"Shape: {horizontal.shape}")

    # Vertikal zusammenfügen (axis=0)
    vertikal = np.concatenate([januar, februar, maerz], axis=0)
    print(f"\nVertikal zusammengefügt:\n{vertikal}")
    print(f"Shape: {vertikal.shape}")

    # Mit vstack und hstack (vereinfachte Syntax)
    v_stack = np.vstack([januar, februar, maerz])  # Vertikal
    h_stack = np.hstack([januar, februar, maerz])  # Horizontal

    print(f"vstack gleich vertikal: {np.array_equal(vertikal, v_stack)}")
    print(f"hstack gleich horizontal: {np.array_equal(horizontal, h_stack)}")

    # 6. Splitting - Arrays aufteilen
    print("\n6️⃣ Arrays aufteilen")
    print("-" * 40)

    # Große Produktionsdatenreihe aufteilen
    grosse_datenreihe = np.arange(1, 25).reshape(4, 6)
    print("Große Datenreihe:")
    print(grosse_datenreihe)

    # Horizontal aufteilen (Spalten)
    links, mitte, rechts = np.hsplit(grosse_datenreihe, 3)  # In 3 Teile
    print(f"\nLinks ({links.shape}):\n{links}")
    print(f"Mitte ({mitte.shape}):\n{mitte}")
    print(f"Rechts ({rechts.shape}):\n{rechts}")

    # Vertikal aufteilen (Zeilen)
    oben, unten = np.vsplit(grosse_datenreihe, 2)  # In 2 Teile
    print(f"\nOben ({oben.shape}):\n{oben}")
    print(f"Unten ({unten.shape}):\n{unten}")

    # 7. Broadcasting - Arrays mit verschiedenen Shapes
    print("\n7️⃣ Broadcasting - Verschiedene Array-Größen")
    print("-" * 40)

    # Basis-Produktionszeiten für 4 Maschinen
    basis_zeiten = np.array([8.0, 7.5, 8.5, 7.8])  # (4,)
    print(f"Basis-Zeiten:     {basis_zeiten}")

    # Wochenfaktoren für 5 Arbeitstage
    wochenfaktoren = np.array([1.0, 1.1, 0.9, 1.05, 0.95]).reshape(5, 1)  # (5, 1)
    print(f"Wochenfaktoren:\n{wochenfaktoren}")

    # Broadcasting: (5, 1) * (4,) -> (5, 4)
    wochen_zeiten = wochenfaktoren * basis_zeiten
    print(f"Wochen-Zeiten:\n{wochen_zeiten}")
    print(f"Shape: {wochen_zeiten.shape} (5 Tage x 4 Maschinen)")

    # Weitere Broadcasting-Beispiele
    einzelwert = 1.1  # Skalar
    alle_erhoeht = basis_zeiten * einzelwert  # Broadcasting mit Skalar
    print(f"Alle um 10% erhöht: {alle_erhoeht}")

    # 8. Erweiterte Indexierung
    print("\n8️⃣ Erweiterte Indexierung")
    print("-" * 40)

    # Maschinendaten
    daten_matrix = np.random.randint(800, 1200, (6, 4))  # 6 Zeilen, 4 Spalten
    print("Datenmatrix:")
    print(daten_matrix)

    # Fancy Indexing - Bestimmte Zeilen und Spalten
    zeilen_indizes = [0, 2, 4]  # Erste, dritte, fünfte Zeile
    spalten_indizes = [1, 3]  # Zweite und vierte Spalte

    teilmatrix = daten_matrix[np.ix_(zeilen_indizes, spalten_indizes)]
    print(f"\nTeilmatrix (Zeilen {zeilen_indizes}, Spalten {spalten_indizes}):")
    print(teilmatrix)

    # Argmax und Argmin - Indizes der Extremwerte
    flache_daten = daten_matrix.flatten()
    max_index = np.argmax(flache_daten)
    min_index = np.argmin(flache_daten)

    print(f"\nMaximum-Wert: {flache_daten[max_index]} at Index {max_index}")
    print(f"Minimum-Wert: {flache_daten[min_index]} at Index {min_index}")

    # 2D-Indizes zurückgewinnen
    max_2d = np.unravel_index(max_index, daten_matrix.shape)
    min_2d = np.unravel_index(min_index, daten_matrix.shape)
    print(f"Maximum 2D-Position: {max_2d}")
    print(f"Minimum 2D-Position: {min_2d}")

    # 9. Praktisches Beispiel: Datenvorverarbeitung
    print("\n9️⃣ Praktisches Beispiel: Sensordaten aufbereiten")
    print("-" * 50)

    # Simulierte Sensordaten mit Rauschen
    np.random.seed(42)
    zeit = np.arange(0, 100, 0.5)  # 200 Zeitpunkte
    signal = 50 + 10 * np.sin(0.1 * zeit)  # Sinussignal
    rauschen = np.random.normal(0, 2, len(zeit))  # Rauschen
    messdaten = signal + rauschen

    print(f"Zeitpunkte: {len(zeit)}")
    print(f"Signal-Bereich: {signal.min():.1f} - {signal.max():.1f}")
    print(f"Messdaten-Bereich: {messdaten.min():.1f} - {messdaten.max():.1f}")

    # Datenvorverarbeitung
    # 1. Ausreißer entfernen (> 3 Standardabweichungen)
    mittel = np.mean(messdaten)
    std = np.std(messdaten)
    ausreisser_maske = np.abs(messdaten - mittel) < 3 * std
    bereinigte_daten = messdaten[ausreisser_maske]

    print(f"Vor Bereinigung: {len(messdaten)} Datenpunkte")
    print(f"Nach Bereinigung: {len(bereinigte_daten)} Datenpunkte")
    print(f"Entfernt: {len(messdaten) - len(bereinigte_daten)} Ausreißer")

    # 2. Gleitender Durchschnitt (Simple Moving Average)
    fenster_groesse = 5
    glaettung = np.convolve(
        bereinigte_daten, np.ones(fenster_groesse) / fenster_groesse, mode="valid"
    )
    print(f"Geglättete Daten: {len(glaettung)} Punkte")

    # 3. Daten in Chunks aufteilen
    chunk_groesse = 20
    anzahl_chunks = len(glaettung) // chunk_groesse
    chunks = glaettung[: anzahl_chunks * chunk_groesse].reshape(-1, chunk_groesse)

    print(f"Aufgeteilt in {anzahl_chunks} Chunks à {chunk_groesse} Punkte")
    print(f"Chunks Shape: {chunks.shape}")

    # Statistiken pro Chunk
    chunk_mittel = np.mean(chunks, axis=1)
    chunk_std = np.std(chunks, axis=1)

    print(f"Chunk-Mittelwerte: {chunk_mittel[:5]}... (erste 5)")
    print(f"Chunk-Std.abw.:    {chunk_std[:5]}... (erste 5)")

    print(f"\n{'=' * 60}")
    print("✅ Array-Manipulation erfolgreich demonstriert!")
    print("🔄 Reshaping, Slicing und Broadcasting sind sehr mächtig")
    print("📊 Ideal für komplexe Datenvorverarbeitung")


if __name__ == "__main__":
    main()
