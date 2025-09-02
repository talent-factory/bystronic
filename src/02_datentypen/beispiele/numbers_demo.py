#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Beispiel: Zahlen und mathematische Operationen

Dieses Skript demonstriert die Verwendung von Zahlen in Python
für typische Bystronic-Anwendungen wie Berechnungen von Materialdicken,
Schnittgeschwindigkeiten und Produktionszeiten.
"""

import math


def main():
    print("=" * 50)
    print("BYSTRONIC - ZAHLEN UND BERECHNUNGEN")
    print("=" * 50)

    # 1. Integer (Ganze Zahlen)
    print("\n1. INTEGER - Ganze Zahlen")
    print("-" * 30)

    anzahl_teile = 1500
    schichtdauer = 8  # Stunden
    mitarbeiter = 12

    print(f"Teile pro Schicht: {anzahl_teile}")
    print(f"Schichtdauer: {schichtdauer} Stunden")
    print(f"Mitarbeiter: {mitarbeiter}")
    print(f"Teile pro Mitarbeiter: {anzahl_teile // mitarbeiter}")

    # 2. Float (Fliesskommazahlen)
    print("\n2. FLOAT - Fliesskommazahlen")
    print("-" * 30)

    materialdicke = 2.5  # mm
    schnittgeschwindigkeit = 15.75  # m/min
    laserleistung = 6.0  # kW
    toleranz = 0.1  # mm

    print(f"Materialdicke: {materialdicke} mm")
    print(f"Schnittgeschwindigkeit: {schnittgeschwindigkeit} m/min")
    print(f"Laserleistung: {laserleistung} kW")
    print(f"Toleranz: ±{toleranz} mm")

    # Berechnung der Schnittzeit für einen 100mm Schnitt
    schnittlaenge = 100  # mm
    schnittzeit = (schnittlaenge / 1000) / schnittgeschwindigkeit  # in Minuten
    print(f"\nSchnittzeit für {schnittlaenge}mm: {schnittzeit:.2f} Minuten")

    # 3. Complex (Komplexe Zahlen) - für elektrische Berechnungen
    print("\n3. COMPLEX - Komplexe Zahlen")
    print("-" * 30)

    impedanz = 50 + 30j  # Ohm (Widerstand + j*Reaktanz)
    strom = 10 + 0j  # Ampere

    spannung = impedanz * strom
    print(f"Impedanz: {impedanz} Ω")
    print(f"Strom: {strom} A")
    print(f"Spannung: {spannung} V")
    print(f"Betrag der Spannung: {abs(spannung):.1f} V")

    # 4. Boolean (Wahrheitswerte)
    print("\n4. BOOLEAN - Wahrheitswerte")
    print("-" * 30)

    maschine_aktiv = True
    wartung_faellig = False
    temperatur_ok = materialdicke >= 1.0 and materialdicke <= 5.0

    print(f"Maschine aktiv: {maschine_aktiv}")
    print(f"Wartung fällig: {wartung_faellig}")
    print(f"Temperatur OK: {temperatur_ok}")
    print(f"Bereit für Produktion: {maschine_aktiv and not wartung_faellig}")

    # 5. Mathematische Operationen
    print("\n5. MATHEMATISCHE OPERATIONEN")
    print("-" * 30)

    demonstrate_math_operations()

    # 6. Praktische Berechnungen für Bystronic
    print("\n6. PRAKTISCHE BERECHNUNGEN")
    print("-" * 30)

    calculate_production_metrics()
    calculate_material_usage()
    calculate_laser_parameters()


def demonstrate_math_operations():
    """Demonstriert mathematische Operationen"""
    a = 25
    b = 4

    print(f"a = {a}, b = {b}")
    print(f"Addition: {a} + {b} = {a + b}")
    print(f"Subtraktion: {a} - {b} = {a - b}")
    print(f"Multiplikation: {a} * {b} = {a * b}")
    print(f"Division: {a} / {b} = {a / b}")
    print(f"Ganzzahldivision: {a} // {b} = {a // b}")
    print(f"Modulo (Rest): {a} % {b} = {a % b}")
    print(f"Potenz: {a} ** {b} = {a ** b}")

    # Weitere mathematische Funktionen
    zahl = 16.7
    print(f"\nWeitere Funktionen mit {zahl}:")
    print(f"Absoluter Wert: {abs(zahl)}")
    print(f"Aufrunden: {math.ceil(zahl)}")
    print(f"Abrunden: {math.floor(zahl)}")
    print(f"Runden: {round(zahl, 1)}")
    print(f"Quadratwurzel: {math.sqrt(zahl):.2f}")


def calculate_production_metrics():
    """Berechnet Produktionsmetriken"""
    print("Produktionsmetriken:")

    # Eingangsdaten
    teile_geplant = 2000
    teile_produziert = 1850
    sollzeit = 480  # Minuten (8 Stunden)
    istzeit = 465  # Minuten
    ausschuss = 25  # Teile

    # Berechnungen
    effizienz = (teile_produziert / teile_geplant) * 100
    zeiteffizienz = (sollzeit / istzeit) * 100
    ausschussrate = (ausschuss / teile_produziert) * 100
    gute_teile = teile_produziert - ausschuss

    print(f"  Geplant: {teile_geplant} Teile")
    print(f"  Produziert: {teile_produziert} Teile")
    print(f"  Gute Teile: {gute_teile} Teile")
    print(f"  Effizienz: {effizienz:.1f}%")
    print(f"  Zeiteffizienz: {zeiteffizienz:.1f}%")
    print(f"  Ausschussrate: {ausschussrate:.1f}%")


def calculate_material_usage():
    """Berechnet Materialverbrauch"""
    print("\nMaterialverbrauch:")

    # Blechdaten
    blech_laenge = 3000  # mm
    blech_breite = 1500  # mm
    blech_dicke = 2.0  # mm
    dichte_stahl = 7.85  # g/cm³

    # Teil-Daten
    teil_laenge = 150  # mm
    teil_breite = 100  # mm
    anzahl_teile = 150

    # Berechnungen
    blech_volumen = blech_laenge * blech_breite * blech_dicke  # mm³
    blech_gewicht = (blech_volumen / 1000) * dichte_stahl  # g

    teil_flaeche = teil_laenge * teil_breite
    gesamt_teil_flaeche = teil_flaeche * anzahl_teile
    blech_flaeche = blech_laenge * blech_breite

    materialausnutzung = (gesamt_teil_flaeche / blech_flaeche) * 100
    verschnitt = 100 - materialausnutzung

    print(f"  Blechgrösse: {blech_laenge} × {blech_breite} × {blech_dicke} mm")
    print(f"  Blechgewicht: {blech_gewicht/1000:.1f} kg")
    print(f"  Teilgrösse: {teil_laenge} × {teil_breite} mm")
    print(f"  Anzahl Teile: {anzahl_teile}")
    print(f"  Materialausnutzung: {materialausnutzung:.1f}%")
    print(f"  Verschnitt: {verschnitt:.1f}%")


def calculate_laser_parameters():
    """Berechnet Laser-Parameter"""
    print("\nLaser-Parameter:")

    # Eingangsdaten
    materialdicke = 5.0  # mm
    schnittgeschwindigkeit = 2.5  # m/min
    umfang_pro_teil = 400  # mm
    anzahl_teile = 100

    # Berechnungen
    gesamter_schnittweg = (umfang_pro_teil * anzahl_teile) / 1000  # m
    reine_schnittzeit = gesamter_schnittweg / schnittgeschwindigkeit  # min

    # Zusätzliche Zeit für Positionierung etc.
    zusatzzeit_faktor = 1.3
    gesamtzeit = reine_schnittzeit * zusatzzeit_faktor

    # Energieverbrauch (grobe Schätzung)
    laserleistung = 6.0  # kW
    energieverbrauch = (laserleistung * gesamtzeit) / 60  # kWh

    print(f"  Materialdicke: {materialdicke} mm")
    print(f"  Schnittgeschwindigkeit: {schnittgeschwindigkeit} m/min")
    print(f"  Gesamter Schnittweg: {gesamter_schnittweg:.1f} m")
    print(f"  Reine Schnittzeit: {reine_schnittzeit:.1f} min")
    print(f"  Geschätzte Gesamtzeit: {gesamtzeit:.1f} min")
    print(f"  Energieverbrauch: {energieverbrauch:.2f} kWh")


if __name__ == "__main__":
    main()

    print("\n" + "=" * 50)
    print("Programm beendet. Drücken Sie Enter...")
    input()
