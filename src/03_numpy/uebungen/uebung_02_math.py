#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Übung 2: Mathematische Operationen mit NumPy

Diese Übung behandelt mathematische Funktionen und Berechnungen:
- Grundrechenarten und vektorisierte Operationen
- Trigonometrische Funktionen
- Exponential- und Logarithmusfunktionen
- Statistische Funktionen
- Rundung und Vergleiche
"""

import numpy as np


def uebung_2_1() -> None:
    """Übung 2.1: Grundrechenarten"""
    print("=" * 60)
    print("ÜBUNG 2.1: Grundrechenarten")
    print("=" * 60)

    # Produktionsdaten von zwei Maschinenlinien
    linie_a = np.array([850, 920, 780, 890, 950, 820, 880])  # Stück pro Tag
    linie_b = np.array([800, 880, 820, 870, 900, 850, 860])  # Stück pro Tag

    print(f"Linie A Produktion: {linie_a}")
    print(f"Linie B Produktion: {linie_b}")

    # TODO: Führen Sie verschiedene Berechnungen durch

    # a) Berechnen Sie die Gesamtproduktion pro Tag (A + B)
    gesamtproduktion = linie_a + linie_b
    print(f"\na) Gesamtproduktion pro Tag: {gesamtproduktion}")

    # b) Berechnen Sie die Differenz (A - B) pro Tag
    differenz = linie_a - linie_b
    print(f"b) Differenz A-B pro Tag: {differenz}")

    # c) Berechnen Sie das Verhältnis A/B pro Tag
    verhaeltnis = linie_a / linie_b
    print(f"c) Verhältnis A/B pro Tag: {verhaeltnis}")

    # d) Multiplizieren Sie alle Werte von Linie A mit 1.1 (10% Steigerung)
    linie_a_gesteigert = linie_a * 1.1
    print(f"d) Linie A mit 10% Steigerung: {linie_a_gesteigert}")

    # e) Berechnen Sie die Wochenproduktion für jede Linie
    wochen_a = np.sum(linie_a)
    wochen_b = np.sum(linie_b)
    print(f"e) Wochenproduktion A: {wochen_a}, B: {wochen_b}")

    # f) An welchen Tagen war Linie A besser als Linie B?
    a_besser = linie_a > linie_b
    tage_a_besser = np.sum(a_besser)
    print(f"f) Linie A besser an {tage_a_besser} von {len(linie_a)} Tagen")
    print(f"   Tage: {np.where(a_besser)[0] + 1}")  # +1 für Tag-Nummerierung


def uebung_2_2() -> None:
    """Übung 2.2: Trigonometrische Funktionen"""
    print("\n" + "=" * 60)
    print("ÜBUNG 2.2: Trigonometrische Funktionen")
    print("=" * 60)

    # Biegewinkel für verschiedene Blechteile (in Grad)
    winkel_grad = np.array([30, 45, 60, 90, 120, 135, 150])

    print(f"Biegewinkel (Grad): {winkel_grad}")

    # TODO: Berechnen Sie trigonometrische Werte

    # a) Konvertieren Sie die Winkel zu Radiant
    winkel_rad = np.radians(winkel_grad)
    print(f"\na) Winkel (Radiant): {winkel_rad}")

    # b) Berechnen Sie den Sinus aller Winkel
    sinus_werte = np.sin(winkel_rad)
    print(f"b) Sinus-Werte: {sinus_werte}")

    # c) Berechnen Sie den Cosinus aller Winkel
    cosinus_werte = np.cos(winkel_rad)
    print(f"c) Cosinus-Werte: {cosinus_werte}")

    # d) Überprüfen Sie die Identität sin²(x) + cos²(x) = 1
    identitaet = sinus_werte**2 + cosinus_werte**2
    print(f"d) sin²(x) + cos²(x): {identitaet}")
    print(f"   Alle ≈ 1? {np.allclose(identitaet, 1.0)}")

    # e) Praktische Anwendung: Kraftkomponenten
    # Eine Kraft von 1000N wirkt unter verschiedenen Winkeln
    kraft_gesamt = 1000  # N
    kraft_x = kraft_gesamt * cosinus_werte  # Horizontale Komponente
    kraft_y = kraft_gesamt * sinus_werte  # Vertikale Komponente

    print("\ne) Kraftkomponenten bei 1000N:")
    for i, winkel in enumerate(winkel_grad):
        print(f"   {winkel:3d}°: Fx={kraft_x[i]:6.1f}N, Fy={kraft_y[i]:6.1f}N")


def uebung_2_3() -> None:
    """Übung 2.3: Exponential- und Logarithmusfunktionen"""
    print("\n" + "=" * 60)
    print("ÜBUNG 2.3: Exponential- und Logarithmusfunktionen")
    print("=" * 60)

    # Abkühlungssimulation: Werkstück von 500°C auf Raumtemperatur
    zeit = np.array([0, 5, 10, 20, 30, 45, 60])  # Minuten
    start_temp = 500  # °C
    raum_temp = 20  # °C
    zeitkonstante = 0.03  # 1/min

    print(f"Zeit (min): {zeit}")
    print(f"Starttemperatur: {start_temp}°C")
    print(f"Raumtemperatur: {raum_temp}°C")

    # TODO: Berechnen Sie die Abkühlung

    # a) Berechnen Sie die Temperatur nach dem Newton'schen Abkühlungsgesetz
    # T(t) = T_raum + (T_start - T_raum) * exp(-k*t)
    temperatur = raum_temp + (start_temp - raum_temp) * np.exp(-zeitkonstante * zeit)
    print(f"\na) Temperatur nach Zeit: {temperatur.astype(int)}")

    # b) Nach welcher Zeit ist die Temperatur unter 100°C?
    # Lösen Sie: 100 = 20 + 480 * exp(-0.03*t)
    # t = -ln((100-20)/(500-20)) / 0.03
    zeit_unter_100 = (
        -np.log((100 - raum_temp) / (start_temp - raum_temp)) / zeitkonstante
    )
    print(f"b) Zeit bis unter 100°C: {zeit_unter_100:.1f} Minuten")

    # c) Berechnen Sie die natürlichen Logarithmen der Temperaturdifferenzen
    temp_diff = temperatur - raum_temp
    log_diff = np.log(temp_diff)
    print(f"c) ln(T-T_raum): {log_diff}")

    # d) pH-Wert Berechnung (Bonus)
    # Verschiedene H⁺-Konzentrationen (mol/L)
    h_konzentration = np.array([1e-1, 1e-3, 1e-7, 1e-10, 1e-14])
    ph_werte = -np.log10(h_konzentration)

    print(f"\nd) H⁺-Konzentration: {h_konzentration}")
    print(f"   pH-Werte: {ph_werte}")

    # e) Exponentielles Wachstum: Bakterienkultur
    start_bakterien = 1000
    wachstumsrate = 0.2  # pro Stunde
    stunden = np.array([0, 2, 4, 6, 8, 12])

    bakterien_anzahl = start_bakterien * np.exp(wachstumsrate * stunden)
    print("\ne) Bakterienwachstum:")
    for i, h in enumerate(stunden):
        print(f"   {h:2d}h: {bakterien_anzahl[i]:8.0f} Bakterien")


def uebung_2_4() -> None:
    """Übung 2.4: Statistische Funktionen"""
    print("\n" + "=" * 60)
    print("ÜBUNG 2.4: Statistische Funktionen")
    print("=" * 60)

    # Qualitätsmessdaten einer Charge
    np.random.seed(42)
    messdaten = np.random.normal(50.0, 2.5, 25)  # Mittel=50, StdAbw=2.5, n=25

    print("Qualitätsmessdaten (25 Messungen):")
    print(f"{messdaten}")

    # TODO: Berechnen Sie statistische Kennwerte

    # a) Grundlegende Statistiken
    mittelwert = np.mean(messdaten)
    median = np.median(messdaten)
    standardabweichung = np.std(messdaten, ddof=1)  # ddof=1 für Stichprobe
    varianz = np.var(messdaten, ddof=1)

    print("\na) Grundlegende Statistiken:")
    print(f"   Mittelwert: {mittelwert:.3f}")
    print(f"   Median: {median:.3f}")
    print(f"   Standardabweichung: {standardabweichung:.3f}")
    print(f"   Varianz: {varianz:.3f}")

    # b) Minimum und Maximum
    minimum = np.min(messdaten)
    maximum = np.max(messdaten)
    spannweite = maximum - minimum

    print("\nb) Extremwerte:")
    print(f"   Minimum: {minimum:.3f}")
    print(f"   Maximum: {maximum:.3f}")
    print(f"   Spannweite: {spannweite:.3f}")

    # c) Percentile berechnen
    q25 = np.percentile(messdaten, 25)
    q50 = np.percentile(messdaten, 50)  # = Median
    q75 = np.percentile(messdaten, 75)
    iqr = q75 - q25  # Interquartilsabstand

    print("\nc) Percentile:")
    print(f"   25. Percentil (Q1): {q25:.3f}")
    print(f"   50. Percentil (Q2/Median): {q50:.3f}")
    print(f"   75. Percentil (Q3): {q75:.3f}")
    print(f"   IQR (Q3-Q1): {iqr:.3f}")

    # d) Ausreißer identifizieren (IQR-Methode)
    untere_grenze = q25 - 1.5 * iqr
    obere_grenze = q75 + 1.5 * iqr
    ausreisser = (messdaten < untere_grenze) | (messdaten > obere_grenze)

    print("\nd) Ausreißer (IQR-Methode):")
    print(f"   Untere Grenze: {untere_grenze:.3f}")
    print(f"   Obere Grenze: {obere_grenze:.3f}")
    print(f"   Anzahl Ausreißer: {np.sum(ausreisser)}")
    if np.sum(ausreisser) > 0:
        print(f"   Ausreißer-Werte: {messdaten[ausreisser]}")

    # e) Z-Score berechnen (wie viele Standardabweichungen vom Mittelwert?)
    z_scores = (messdaten - mittelwert) / standardabweichung
    extreme_z = np.abs(z_scores) > 2.0  # |z| > 2 ist ungewöhnlich

    print("\ne) Z-Scores:")
    print(f"   Anzahl |z| > 2.0: {np.sum(extreme_z)}")
    print(f"   Max |z|: {np.max(np.abs(z_scores)):.3f}")

    # f) Prozessfähigkeit (Cp-Wert)
    toleranz = 5.0  # ±2.5 um Sollwert 50
    sollwert = 50.0
    cp_wert = toleranz / (6 * standardabweichung)
    cpk_ober = (sollwert + toleranz / 2 - mittelwert) / (3 * standardabweichung)
    cpk_unter = (mittelwert - (sollwert - toleranz / 2)) / (3 * standardabweichung)
    cpk_wert = float(np.minimum(cpk_ober, cpk_unter))

    print("\nf) Prozessfähigkeit:")
    print(f"   Cp-Wert: {cp_wert:.3f}")
    print(f"   Cpk-Wert: {cpk_wert:.3f}")
    print(
        f"   Bewertung: {'Gut' if cpk_wert > 1.33 else 'Akzeptabel' if cpk_wert > 1.0 else 'Kritisch'}"
    )


def uebung_2_5() -> None:
    """Übung 2.5: Rundung und Vergleiche"""
    print("\n" + "=" * 60)
    print("ÜBUNG 2.5: Rundung und Vergleiche")
    print("=" * 60)

    # Präzisionsmessungen mit vielen Nachkommastellen
    messungen = np.array([25.14159, 24.98765, 25.05432, 24.97891, 25.12345])

    print(f"Original-Messungen: {messungen}")

    # TODO: Verschiedene Rundungsoperationen

    # a) Auf 2 Nachkommastellen runden
    gerundet_2 = np.round(messungen, 2)
    print(f"\na) Gerundet auf 2 Stellen: {gerundet_2}")

    # b) Auf ganze Zahlen runden
    gerundet_ganz = np.round(messungen, 0)
    print(f"b) Gerundet auf ganze Zahlen: {gerundet_ganz}")

    # c) Aufrunden (ceiling)
    aufgerundet = np.ceil(messungen)
    print(f"c) Aufgerundet: {aufgerundet}")

    # d) Abrunden (floor)
    abgerundet = np.floor(messungen)
    print(f"d) Abgerundet: {abgerundet}")

    # e) Nachkommastellen abschneiden (truncate)
    abgeschnitten = np.trunc(messungen)
    print(f"e) Abgeschnitten: {abgeschnitten}")

    # f) Vergleiche mit Toleranz
    sollwert = 25.0
    toleranz = 0.1

    zu_hoch = messungen > (sollwert + toleranz)
    zu_niedrig = messungen < (sollwert - toleranz)
    in_toleranz = ~(zu_hoch | zu_niedrig)  # NOT (zu_hoch OR zu_niedrig)

    print(f"\nf) Vergleiche (Sollwert: {sollwert} ± {toleranz}):")
    print(f"   Zu hoch: {zu_hoch} ({np.sum(zu_hoch)} Stück)")
    print(f"   Zu niedrig: {zu_niedrig} ({np.sum(zu_niedrig)} Stück)")
    print(f"   In Toleranz: {in_toleranz} ({np.sum(in_toleranz)} Stück)")

    # g) Element-weise Maximum und Minimum
    vergleichswerte = np.array([25.0, 25.1, 24.9, 25.05, 25.15])

    maxima = np.maximum(messungen, vergleichswerte)
    minima = np.minimum(messungen, vergleichswerte)

    print("\ng) Element-weise Vergleiche:")
    print(f"   Messungen: {messungen}")
    print(f"   Vergleich: {vergleichswerte}")
    print(f"   Maxima: {maxima}")
    print(f"   Minima: {minima}")


def uebung_2_6() -> None:
    """Übung 2.6: Praktisches Beispiel - Energieanalyse"""
    print("\n" + "=" * 60)
    print("ÜBUNG 2.6: Praktisches Beispiel - Energieanalyse")
    print("=" * 60)

    # Energieverbrauchsdaten verschiedener Maschinen über eine Woche
    tage = np.array(["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"])

    # Energieverbrauch in kWh pro Tag
    laser_verbrauch = np.array([45.2, 52.1, 48.7, 51.3, 49.8, 35.2, 0.0])
    presse_verbrauch = np.array([32.1, 35.4, 31.8, 34.2, 33.7, 28.9, 0.0])
    foerderband_verbrauch = np.array([8.5, 8.8, 8.3, 8.7, 8.4, 7.2, 2.1])

    print("Energieverbrauch (kWh) pro Tag:")
    print("Tag     Laser  Presse  Band   Gesamt")
    print("-" * 40)

    # TODO: Energieanalyse durchführen

    # a) Berechnen Sie den Gesamtverbrauch pro Tag
    gesamt_verbrauch = laser_verbrauch + presse_verbrauch + foerderband_verbrauch

    for i, tag in enumerate(tage):
        print(
            f"{tag}     {laser_verbrauch[i]:5.1f}  {presse_verbrauch[i]:6.1f}  {foerderband_verbrauch[i]:5.1f}  {gesamt_verbrauch[i]:6.1f}"
        )

    # b) Wochenverbrauch und Durchschnitte
    wochen_laser = np.sum(laser_verbrauch)
    wochen_presse = np.sum(presse_verbrauch)
    wochen_band = np.sum(foerderband_verbrauch)
    wochen_gesamt = np.sum(gesamt_verbrauch)

    print("\nb) Wochenverbrauch:")
    print(f"   Laser: {wochen_laser:.1f} kWh")
    print(f"   Presse: {wochen_presse:.1f} kWh")
    print(f"   Förderband: {wochen_band:.1f} kWh")
    print(f"   Gesamt: {wochen_gesamt:.1f} kWh")

    # c) Durchschnitt nur für Arbeitstage (Mo-Fr)
    arbeitstage_laser = np.mean(laser_verbrauch[:5])
    arbeitstage_presse = np.mean(presse_verbrauch[:5])
    arbeitstage_gesamt = np.mean(gesamt_verbrauch[:5])

    print("\nc) Durchschnitt Arbeitstage (Mo-Fr):")
    print(f"   Laser: {arbeitstage_laser:.1f} kWh/Tag")
    print(f"   Presse: {arbeitstage_presse:.1f} kWh/Tag")
    print(f"   Gesamt: {arbeitstage_gesamt:.1f} kWh/Tag")

    # d) Relativer Anteil jeder Maschine
    laser_anteil = wochen_laser / wochen_gesamt * 100
    presse_anteil = wochen_presse / wochen_gesamt * 100
    band_anteil = wochen_band / wochen_gesamt * 100

    print("\nd) Anteil am Gesamtverbrauch:")
    print(f"   Laser: {laser_anteil:.1f}%")
    print(f"   Presse: {presse_anteil:.1f}%")
    print(f"   Förderband: {band_anteil:.1f}%")

    # e) Hochrechnungen und Prognosen
    # Strompreis und Hochrechnungen
    strompreis = 0.28  # €/kWh

    wochen_kosten = wochen_gesamt * strompreis
    monats_kosten = wochen_kosten * 4.33  # 52/12 Wochen pro Monat
    jahres_kosten = wochen_kosten * 52

    print(f"\ne) Kostenprognosen bei {strompreis:.2f} €/kWh:")
    print(f"   Woche: {wochen_kosten:.2f} €")
    print(f"   Monat: {monats_kosten:.2f} €")
    print(f"   Jahr: {jahres_kosten:.2f} €")

    # f) Einsparpotential wenn Laser 10% effizienter wäre
    laser_optimiert = laser_verbrauch * 0.9  # 10% weniger
    einsparung_woche = np.sum(laser_verbrauch - laser_optimiert)
    einsparung_jahr = einsparung_woche * 52
    einsparung_kosten_jahr = einsparung_jahr * strompreis

    print("\nf) Einsparpotential (10% Laser-Effizienz):")
    print(f"   Einsparung pro Woche: {einsparung_woche:.1f} kWh")
    print(f"   Einsparung pro Jahr: {einsparung_jahr:.1f} kWh")
    print(f"   Kosteneinsparung pro Jahr: {einsparung_kosten_jahr:.2f} €")


def hauptprogramm() -> None:
    """Hauptprogramm - alle Übungen ausführen"""
    print("🧮 NUMPY MATHEMATISCHE OPERATIONEN - ÜBUNGEN")

    try:
        uebung_2_1()
        uebung_2_2()
        uebung_2_3()
        uebung_2_4()
        uebung_2_5()
        uebung_2_6()

        print("\n" + "=" * 60)
        print("✅ ALLE ÜBUNGEN ERFOLGREICH ABGESCHLOSSEN!")
        print("=" * 60)
        print("\n📝 Was Sie gelernt haben:")
        print("• Vektorisierte Grundrechenarten")
        print("• Trigonometrische Funktionen für technische Berechnungen")
        print("• Exponential- und Logarithmusfunktionen")
        print("• Umfassende statistische Analysen")
        print("• Rundung und numerische Vergleiche")
        print("• Praktische Anwendung: Energieanalyse")

        print("\n🎯 Nächste Schritte:")
        print("• Übung 3: Datenanalyse mit statistischen Methoden")
        print("• Vertiefung: Komplexe mathematische Operationen")

    except Exception as e:
        print(f"\n❌ Fehler in den Übungen: {e}")
        print("Überprüfen Sie Ihren Code und versuchen Sie es erneut.")


if __name__ == "__main__":
    hauptprogramm()
