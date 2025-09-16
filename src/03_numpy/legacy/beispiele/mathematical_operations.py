#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Beispiel: Mathematische Operationen mit NumPy

Dieses Skript zeigt mathematische Funktionen und Berechnungen
für industrielle Anwendungen bei Bystronic.
"""

import math

import numpy as np


def main() -> None:
    print("=" * 60)
    print("BYSTRONIC - MATHEMATISCHE OPERATIONEN MIT NUMPY")
    print("=" * 60)

    # 1. Grundrechenarten (Vektorisiert)
    print("\n1️⃣ Grundrechenarten - Vektorisierte Operationen")
    print("-" * 50)

    # Produktionszeiten verschiedener Maschinen
    laser_zeiten = np.array([8.5, 7.2, 9.1, 8.8, 7.9])
    presse_zeiten = np.array([6.8, 7.5, 6.2, 7.1, 6.9])

    print(f"Laser-Zeiten:     {laser_zeiten}")
    print(f"Presse-Zeiten:    {presse_zeiten}")

    # Vektorisierte Operationen
    gesamtzeiten = laser_zeiten + presse_zeiten
    differenzen = laser_zeiten - presse_zeiten
    verhaeltnisse = laser_zeiten / presse_zeiten

    print(f"Gesamtzeiten:     {gesamtzeiten}")
    print(f"Differenzen:      {differenzen}")
    print(f"Verhältnisse:     {verhaeltnisse}")

    # Vergleich mit Python-Schleifen
    print("\n🔄 Vergleich: NumPy vs Python-Schleife")
    # NumPy: Eine Zeile
    numpy_summe = laser_zeiten + presse_zeiten

    # Python: Schleife erforderlich
    python_summe = []
    for i in range(len(laser_zeiten)):
        python_summe.append(laser_zeiten[i] + presse_zeiten[i])

    print(f"NumPy-Summe:      {numpy_summe}")
    print(f"Python-Summe:     {python_summe}")

    # 2. Trigonometrische Funktionen
    print("\n2️⃣ Trigonometrische Funktionen")
    print("-" * 50)

    # Winkel für Biegungen (in Grad)
    winkel_grad = np.array([30, 45, 60, 90, 120])
    winkel_rad = np.radians(winkel_grad)  # Konvertierung zu Radiant

    print(f"Winkel (Grad):    {winkel_grad}")
    print(f"Winkel (Rad):     {winkel_rad}")

    # Trigonometrische Werte
    sinus = np.sin(winkel_rad)
    cosinus = np.cos(winkel_rad)
    tangens = np.tan(winkel_rad)

    print(f"Sinus:            {sinus}")
    print(f"Cosinus:          {cosinus}")
    print(f"Tangens:          {tangens}")

    # Praktisches Beispiel: Biegekraft berechnen
    print("\n🔧 Praktisches Beispiel: Biegekraft-Berechnung")
    materialdicke = 2.0  # mm
    biegewinkel = np.radians(90)  # 90 Grad Biegung

    # Vereinfachte Formel (abhängig vom Material und Geometrie)
    grundkraft = 1000  # N
    winkelfaktor = 1 / np.cos(biegewinkel / 2)
    dickenfaktor = materialdicke**1.5

    biegekraft = grundkraft * winkelfaktor * dickenfaktor
    print(
        f"Biegekraft für {materialdicke}mm bei {np.degrees(biegewinkel)}°: {biegekraft:.1f} N"
    )

    # 3. Exponential- und Logarithmusfunktionen
    print("\n3️⃣ Exponential- und Logarithmusfunktionen")
    print("-" * 50)

    # Abkühlkurve eines Materials
    zeit = np.array([0, 1, 2, 5, 10, 15, 20])  # Minuten
    start_temperatur = 800  # °C
    umgebungstemperatur = 20  # °C
    zeitkonstante = 0.1

    # Exponentieller Abfall: T(t) = T_umgebung + (T_start - T_umgebung) * exp(-t/tau)
    temperatur = umgebungstemperatur + (
        start_temperatur - umgebungstemperatur
    ) * np.exp(-zeitkonstante * zeit)

    print(f"Zeit (min):       {zeit}")
    print(f"Temperatur (°C):  {temperatur.astype(int)}")

    # Logarithmische Berechnungen
    print("\n📈 Logarithmische Skalierung")
    intensitaeten = np.array([1, 10, 100, 1000, 10000])
    dezibel = 20 * np.log10(intensitaeten)

    print(f"Intensitäten:     {intensitaeten}")
    print(f"Dezibel (dB):     {dezibel}")

    # 4. Statistische Funktionen
    print("\n4️⃣ Statistische Funktionen")
    print("-" * 50)

    # Qualitätsmessdaten
    messwerte = np.array([2.02, 1.98, 2.05, 1.97, 2.01, 1.99, 2.03, 2.00, 1.96, 2.04])
    sollwert = 2.0

    print(f"Messwerte:        {messwerte}")
    print(f"Sollwert:         {sollwert}")

    # Grundlegende Statistiken
    mittelwert = np.mean(messwerte)
    median = np.median(messwerte)
    standardabweichung = np.std(messwerte)
    varianz = np.var(messwerte)
    minimum = np.min(messwerte)
    maximum = np.max(messwerte)

    print("\n📊 Statistische Kennwerte:")
    print(f"Mittelwert:       {mittelwert:.4f}")
    print(f"Median:           {median:.4f}")
    print(f"Std.abweichung:   {standardabweichung:.4f}")
    print(f"Varianz:          {varianz:.6f}")
    print(f"Minimum:          {minimum:.4f}")
    print(f"Maximum:          {maximum:.4f}")
    print(f"Spannweite:       {maximum - minimum:.4f}")

    # Prozessfähigkeit (Cp-Wert)
    toleranz = 0.1  # ±0.05
    cp_wert = toleranz / (6 * standardabweichung)
    print(
        f"Cp-Wert:          {cp_wert:.3f} ({'✅ Gut' if cp_wert > 1.33 else '⚠️ Kritisch' if cp_wert > 1.0 else '❌ Schlecht'})"
    )

    # 5. Rundung und Diskretisierung
    print("\n5️⃣ Rundung und Diskretisierung")
    print("-" * 50)

    # Messwerte mit verschiedenen Rundungen
    praezisionswerte = np.array([2.14159, 1.98765, 2.05432, 1.97891])

    print(f"Original:         {praezisionswerte}")
    print(f"Gerundet (2 St.): {np.round(praezisionswerte, 2)}")
    print(f"Aufgerundet:      {np.ceil(praezisionswerte)}")
    print(f"Abgerundet:       {np.floor(praezisionswerte)}")
    print(f"Abgeschnitten:    {np.trunc(praezisionswerte)}")

    # 6. Minimum/Maximum und Vergleiche
    print("\n6️⃣ Minimum/Maximum und Vergleiche")
    print("-" * 50)

    # Maschinendaten vergleichen
    maschine_a = np.array([8.5, 7.8, 9.2, 8.1, 7.6])
    maschine_b = np.array([7.9, 8.3, 8.8, 7.7, 8.0])

    print(f"Maschine A:       {maschine_a}")
    print(f"Maschine B:       {maschine_b}")

    # Element-weise Vergleiche
    besser = np.maximum(maschine_a, maschine_b)  # Maximum jedes Paars
    schlechter = np.minimum(maschine_a, maschine_b)  # Minimum jedes Paars

    print(f"Bessere Werte:    {besser}")
    print(f"Schlechtere:      {schlechter}")

    # Boolean-Arrays
    a_besser = maschine_a > maschine_b
    print(f"A besser als B:   {a_besser}")
    print(f"Anzahl A besser:  {np.sum(a_besser)}")

    # 7. Erweiterte mathematische Funktionen
    print("\n7️⃣ Erweiterte mathematische Funktionen")
    print("-" * 50)

    # Materialeigenschaften berechnen
    temperaturen = np.array([20, 100, 200, 300, 400, 500])  # °C

    # Wärmeausdehnung (linear approximiert)
    alpha = 1.2e-5  # Ausdehnungskoeffizient für Stahl (1/°C)
    laenge_0 = 1000  # mm Ausgangslänge
    delta_t = temperaturen - 20  # Temperaturdifferenz

    laengen_ausdehnung = laenge_0 * (1 + alpha * delta_t)

    print(f"Temperaturen:     {temperaturen}")
    print(f"Längen (mm):      {laengen_ausdehnung}")

    # Potenz- und Wurzelfunktionen
    flaechen = np.array([100, 400, 900, 1600])  # mm²
    seitenlaengen = np.sqrt(flaechen)  # Quadratwurzel
    volumina = seitenlaengen**3  # Kubik (Potenz)

    print(f"\nFlächen (mm²):    {flaechen}")
    print(f"Seitenlängen:     {seitenlaengen}")
    print(f"Volumina (mm³):   {volumina}")

    # 8. Performance-Vergleich: NumPy vs Pure Python
    print("\n8️⃣ Performance-Vergleich")
    print("-" * 50)

    import time

    # Große Datenmengen für Performance-Test
    grosse_daten = np.random.random(100000)

    # NumPy-Version
    start_time = time.time()
    _ = np.sqrt(grosse_daten**2 + 1)
    numpy_time = time.time() - start_time

    # Python-Version
    start_time = time.time()
    _ = [math.sqrt(x**2 + 1) for x in grosse_daten]
    python_time = time.time() - start_time

    print(f"NumPy-Zeit:       {numpy_time:.4f} Sekunden")
    print(f"Python-Zeit:      {python_time:.4f} Sekunden")
    print(f"Speedup:          {python_time / numpy_time:.1f}x schneller")

    print(f"\n{'=' * 60}")
    print("✅ Mathematische Operationen erfolgreich demonstriert!")
    print("🚀 NumPy ist deutlich schneller als Pure Python")
    print("📊 Perfekt für komplexe numerische Berechnungen")


if __name__ == "__main__":
    main()
