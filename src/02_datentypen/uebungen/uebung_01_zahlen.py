#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Übung 1: Zahlenoperationen

Diese Übung behandelt:
- Integer, Float, Complex, Boolean
- Mathematische Operationen
- Praktische Berechnungen für die Fertigung
- Type Conversion und Validation
"""

import math


def aufgabe_1_grundlagen():
    """Aufgabe 1: Grundlagen der Zahlentypen"""
    print("AUFGABE 1: Zahlentypen-Grundlagen")
    print("-" * 40)

    # TODO: Erstellen Sie folgende Variablen:
    # - teile_anzahl (Integer): 1250
    # - materialdicke (Float): 2.5
    # - ist_qualitaet_ok (Boolean): True
    # - impedanz (Complex): 50 + 30j

    # Ihre Lösung hier:
    # teile_anzahl = ...
    # materialdicke = ...
    # ist_qualitaet_ok = ...
    # impedanz = ...

    # TODO: Geben Sie für jede Variable den Typ aus
    # Verwenden Sie type() und isinstance()

    # Ihre Lösung hier:

    # TODO: Prüfen Sie folgende Bedingungen:
    # - Ist teile_anzahl grösser als 1000?
    # - Ist materialdicke zwischen 2.0 und 3.0?
    # - Ist impedanz eine komplexe Zahl?

    # Ihre Lösung hier:

    print("✅ Aufgabe 1 abgeschlossen!\n")


def aufgabe_2_berechnungen():
    """Aufgabe 2: Praktische Berechnungen"""
    print("AUFGABE 2: Praktische Berechnungen")
    print("-" * 40)

    # Gegeben:
    blechlaenge = 3000  # mm
    blechbreite = 1500  # mm
    blechdicke = 2.0  # mm

    print(f"Blech: {blechlaenge} × {blechbreite} × {blechdicke} mm")

    # TODO: Berechnen Sie:
    # 1. Das Volumen des Blechs in cm³
    # 2. Das Gewicht des Blechs in kg
    # 3. Die Oberfläche des Blechs in m²

    # Ihre Lösung hier:
    # volumen_cm3 = ...
    # gewicht_kg = ...
    # oberflaeche_m2 = ...

    # TODO: Geben Sie die Ergebnisse formatiert aus

    # TODO: Berechnen Sie, wie viele rechteckige Teile
    # (150mm × 100mm) aus dem Blech geschnitten werden können

    # Ihre Lösung hier:
    # teile_pro_reihe = ...
    # reihen = ...
    # max_teile = ...
    # materialausnutzung = ...

    print("✅ Aufgabe 2 abgeschlossen!\n")


def aufgabe_3_laser_parameter():
    """Aufgabe 3: Laser-Parameter berechnen"""
    print("AUFGABE 3: Laser-Parameter")
    print("-" * 40)

    # Gegeben:

    # TODO: Berechnen Sie die Schnittzeit für verschiedene Formen:

    # 1. Rechteck: 200mm × 150mm
    rechteck_umfang = 2 * (200 + 150)  # mm

    # TODO: Schnittzeit in Minuten
    # schnittzeit_rechteck = ...

    # 2. Kreis: Durchmesser 100mm

    # TODO: Kreisumfang und Schnittzeit berechnen
    # kreis_umfang = ...
    # schnittzeit_kreis = ...

    # 3. Komplexes Teil: Kombination aus Rechteck und 4 Kreisen
    rechteck_umfang + 4 * (math.pi * 20)  # 4 Löcher à 20mm Durchmesser

    # TODO: Schnittzeit für komplexes Teil
    # schnittzeit_komplex = ...

    # TODO: Energieverbrauch für alle Teile berechnen
    # (Laserleistung × Zeit in Stunden)

    # Ihre Lösung hier:

    print("✅ Aufgabe 3 abgeschlossen!\n")


def aufgabe_4_qualitaet():
    """Aufgabe 4: Qualitätskontrolle mit Boolean Logic"""
    print("AUFGABE 4: Qualitätskontrolle")
    print("-" * 40)

    # Gegeben: Messwerte für 5 Teile
    teile = [
        {"nr": "P001", "dicke": 2.05, "breite": 49.8, "laenge": 99.2},
        {"nr": "P002", "dicke": 1.95, "breite": 50.2, "laenge": 100.8},
        {"nr": "P003", "dicke": 2.15, "breite": 49.9, "laenge": 100.1},
        {"nr": "P004", "dicke": 1.88, "breite": 50.0, "laenge": 99.9},
        {"nr": "P005", "dicke": 2.02, "breite": 50.1, "laenge": 100.0},
    ]

    # Toleranzen
    dicke_soll = 2.0
    dicke_toleranz = 0.1
    breite_soll = 50.0
    breite_toleranz = 0.2
    laenge_soll = 100.0
    laenge_toleranz = 1.0

    print("Qualitätsprüfung:")
    print(f"Dicke: {dicke_soll} ± {dicke_toleranz} mm")
    print(f"Breite: {breite_soll} ± {breite_toleranz} mm")
    print(f"Länge: {laenge_soll} ± {laenge_toleranz} mm\n")

    # TODO: Für jedes Teil prüfen Sie:
    # 1. Ist die Dicke im Toleranzbereich?
    # 2. Ist die Breite im Toleranzbereich?
    # 3. Ist die Länge im Toleranzbereich?
    # 4. Ist das Teil insgesamt OK (alle Masse im Toleranzbereich)?


    for _teil in teile:
        # TODO: Implementieren Sie die Qualitätsprüfung
        # dicke_ok = ...
        # breite_ok = ...
        # laenge_ok = ...
        # teil_ok = ...

        # TODO: Ausgabe des Prüfergebnisses
        # print(f"{teil['nr']}: ...")

        # TODO: Zähler aktualisieren
        pass

    # TODO: Zusammenfassung ausgeben
    # Gesamtanzahl, OK-Teile, NOK-Teile, Ausschussrate

    print("✅ Aufgabe 4 abgeschlossen!\n")


def aufgabe_5_produktionsmetriken():
    """Aufgabe 5: Produktionsmetriken berechnen"""
    print("AUFGABE 5: Produktionsmetriken")
    print("-" * 40)

    # Gegeben: Wochendaten
    woche = [
        {
            "tag": "Montag",
            "soll": 200,
            "ist": 195,
            "ausschuss": 8,
            "downtime": 30,
        },  # min
        {"tag": "Dienstag", "soll": 200, "ist": 188, "ausschuss": 12, "downtime": 45},
        {"tag": "Mittwoch", "soll": 200, "ist": 202, "ausschuss": 5, "downtime": 15},
        {"tag": "Donnerstag", "soll": 200, "ist": 178, "ausschuss": 15, "downtime": 75},
        {"tag": "Freitag", "soll": 200, "ist": 185, "ausschuss": 9, "downtime": 40},
    ]


    print("Wochenbericht:")
    print("-" * 60)
    print(
        f"{'Tag':<10} {'Soll':<6} {'Ist':<6} {'Aussch.':<8} {'Downtime':<8} {'Effizienz':<10} {'Verfügb.'}"
    )
    print("-" * 60)

    # TODO: Für jeden Tag berechnen Sie:
    # 1. Effizienz: (Ist-Teile / Soll-Teile) × 100
    # 2. Verfügbarkeit: ((Schichtzeit - Downtime) / Schichtzeit) × 100
    # 3. Qualitätsrate: ((Ist-Teile - Ausschuss) / Ist-Teile) × 100
    # 4. OEE (Overall Equipment Effectiveness): Effizienz × Verfügbarkeit × Qualitätsrate / 10000


    for _tag_daten in woche:
        # TODO: Berechnungen durchführen
        # effizienz = ...
        # verfuegbarkeit = ...
        # qualitaetsrate = ...
        # oee = ...

        # TODO: Ausgabe formatieren
        # print(f"{tag_daten['tag']:<10} ...")

        # TODO: Wochensummen aktualisieren
        # woche_gesamt["soll"] += ...
        pass

    print("-" * 60)

    # TODO: Wochenzusammenfassung berechnen und ausgeben
    # Gesamt-Effizienz, Gesamt-Verfügbarkeit, etc.

    print("✅ Aufgabe 5 abgeschlossen!\n")


def bonus_aufgabe_komplexe_zahlen():
    """Bonus-Aufgabe: Komplexe Zahlen für elektrische Berechnungen"""
    print("BONUS-AUFGABE: Elektrische Berechnungen")
    print("-" * 40)

    # Gegeben: Elektrische Werte für Laser-Spannungsversorgung
    spannung = 400 + 0j  # V (rein reell)
    impedanz_1 = 50 + 30j  # Ohm (Widerstand + Reaktanz)
    impedanz_2 = 75 - 25j  # Ohm
    impedanz_3 = 100 + 0j  # Ohm (rein reell)

    print("Elektrische Analyse der Laser-Spannungsversorgung:")
    print(f"Spannung: {spannung} V")
    print(f"Impedanz 1: {impedanz_1} Ω")
    print(f"Impedanz 2: {impedanz_2} Ω")
    print(f"Impedanz 3: {impedanz_3} Ω")

    # TODO: Berechnen Sie für jede Impedanz:
    # 1. Den Strom (I = U / Z)
    # 2. Die Leistung (P = |I|² × Real(Z))
    # 3. Den Betrag der Impedanz |Z|
    # 4. Den Phasenwinkel (φ = arctan(Imag(Z) / Real(Z)))

    impedanzen = [impedanz_1, impedanz_2, impedanz_3]

    for i, z in enumerate(impedanzen, 1):
        print(f"\nImpedanz {i}: {z} Ω")

        # TODO: Berechnungen durchführen
        # strom = ...
        # leistung = ...
        # betrag = ...
        # phase_rad = ...
        # phase_grad = ...

        # TODO: Ergebnisse ausgeben
        pass

    # TODO: Gesamtimpedanz bei Reihenschaltung berechnen
    # Z_gesamt = impedanz_1 + impedanz_2 + impedanz_3

    # TODO: Gesamtstrom und Gesamtleistung berechnen

    print("✅ Bonus-Aufgabe abgeschlossen!\n")


def loesung_anzeigen():
    """Zeigt die Musterlösung an"""
    antwort = input("Möchten Sie die Musterlösung anzeigen? (j/n): ").lower().strip()
    if antwort in ["j", "ja", "y", "yes"]:
        print("\n" + "=" * 50)
        print("MUSTERLÖSUNG")
        print("=" * 50)

        print(
            """
# Aufgabe 1: Grundlagen
teile_anzahl = 1250
materialdicke = 2.5
ist_qualitaet_ok = True
impedanz = 50 + 30j

print(f"teile_anzahl: {teile_anzahl}, Typ: {type(teile_anzahl)}")
print(f"Ist teile_anzahl ein Integer? {isinstance(teile_anzahl, int)}")
print(f"teile_anzahl > 1000: {teile_anzahl > 1000}")
print(f"2.0 <= materialdicke <= 3.0: {2.0 <= materialdicke <= 3.0}")

# Aufgabe 2: Berechnungen
volumen_cm3 = (blechlaenge * blechbreite * blechdicke) / 1000  # mm³ zu cm³
gewicht_kg = (volumen_cm3 * dichte_stahl) / 1000  # g zu kg
oberflaeche_m2 = (2 * (blechlaenge*blechbreite + blechlaenge*blechdicke + blechbreite*blechdicke)) / 1000000

teile_pro_reihe = blechlaenge // teil_laenge
reihen = blechbreite // teil_breite
max_teile = teile_pro_reihe * reihen
materialausnutzung = (max_teile * teil_laenge * teil_breite) / (blechlaenge * blechbreite) * 100

# Aufgabe 3: Laser-Parameter
schnittzeit_rechteck = (rechteck_umfang / 1000) / schnittgeschwindigkeit  # min
kreis_umfang = math.pi * durchmesser
schnittzeit_kreis = (kreis_umfang / 1000) / schnittgeschwindigkeit
schnittzeit_komplex = (komplex_umfang / 1000) / schnittgeschwindigkeit

energie_rechteck = laserleistung * (schnittzeit_rechteck / 60)  # kWh
energie_kreis = laserleistung * (schnittzeit_kreis / 60)
energie_komplex = laserleistung * (schnittzeit_komplex / 60)

# Aufgabe 4: Qualitätskontrolle
for teil in teile:
    dicke_ok = abs(teil['dicke'] - dicke_soll) <= dicke_toleranz
    breite_ok = abs(teil['breite'] - breite_soll) <= breite_toleranz
    laenge_ok = abs(teil['laenge'] - laenge_soll) <= laenge_toleranz
    teil_ok = dicke_ok and breite_ok and laenge_ok

    status = "✅ OK" if teil_ok else "❌ NOK"
    print(f"{teil['nr']}: {status} (D:{dicke_ok}, B:{breite_ok}, L:{laenge_ok})")

    if teil_ok:
        ok_teile += 1
    else:
        nok_teile += 1

gesamt = len(teile)
ausschussrate = (nok_teile / gesamt) * 100
print(f"\\nZusammenfassung: {ok_teile} OK, {nok_teile} NOK ({ausschussrate:.1f}% Ausschuss)")

# Aufgabe 5: Produktionsmetriken
for tag_daten in woche:
    effizienz = (tag_daten['ist'] / tag_daten['soll']) * 100
    verfuegbarkeit = ((schichtzeit - tag_daten['downtime']) / schichtzeit) * 100
    qualitaetsrate = ((tag_daten['ist'] - tag_daten['ausschuss']) / tag_daten['ist']) * 100
    oee = (effizienz * verfuegbarkeit * qualitaetsrate) / 10000

    print(f"{tag_daten['tag']:<10} {tag_daten['soll']:<6} {tag_daten['ist']:<6} {tag_daten['ausschuss']:<8} {tag_daten['downtime']:<8} {effizienz:>6.1f}% {verfuegbarkeit:>7.1f}%")

# Bonus: Komplexe Zahlen
for i, z in enumerate(impedanzen, 1):
    strom = spannung / z
    leistung = (abs(strom)**2) * z.real
    betrag = abs(z)
    phase_rad = math.atan2(z.imag, z.real)
    phase_grad = math.degrees(phase_rad)

    print(f"Impedanz {i}: Strom={strom:.2f}A, Leistung={leistung:.1f}W, |Z|={betrag:.1f}Ω, φ={phase_grad:.1f}°")
"""
        )


def main():
    """Hauptfunktion der Übung"""
    print("=" * 50)
    print("BYSTRONIC PYTHON GRUNDKURS")
    print("Kapitel 2 - Übung 1: Zahlenoperationen")
    print("=" * 50)

    print(
        """
Diese Übung behandelt die wichtigsten Zahlentypen in Python:
• Integer (ganze Zahlen)
• Float (Fliesskommazahlen)
• Complex (komplexe Zahlen)
• Boolean (Wahrheitswerte)

Bearbeiten Sie die Aufgaben der Reihe nach und implementieren
Sie die TODO-Kommentare.
"""
    )

    try:
        aufgabe_1_grundlagen()
        aufgabe_2_berechnungen()
        aufgabe_3_laser_parameter()
        aufgabe_4_qualitaet()
        aufgabe_5_produktionsmetriken()
        bonus_aufgabe_komplexe_zahlen()

        print("🎉 Alle Aufgaben abgeschlossen!")
        print("\nSie haben erfolgreich gelernt:")
        print("✓ Zahlentypen zu verwenden")
        print("✓ Mathematische Berechnungen durchzuführen")
        print("✓ Boolean Logic anzuwenden")
        print("✓ Praktische Produktionsberechnungen zu erstellen")

        loesung_anzeigen()

    except KeyboardInterrupt:
        print("\n\nÜbung durch Benutzer abgebrochen.")
    except Exception as e:
        print(f"\nFehler in der Übung: {e}")
        print("Überprüfen Sie Ihre Implementierung und versuchen Sie es erneut.")


if __name__ == "__main__":
    main()

    print("\nDrücken Sie Enter zum Beenden...")
    input()
