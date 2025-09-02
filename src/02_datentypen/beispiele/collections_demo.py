#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Beispiel: Collections (Listen, Dictionaries, Sets, Tupel)

Dieses Skript demonstriert die Verwendung von Python Collections
für typische Bystronic-Anwendungen wie Produktionsdaten,
Maschinenverwaltung und Qualitätskontrolle.
"""

import random
from datetime import date, datetime


def main():
    print("=" * 50)
    print("BYSTRONIC - COLLECTIONS UND DATENSTRUKTUREN")
    print("=" * 50)

    # 1. Listen (Lists)
    print("\n1. LISTEN (LISTS)")
    print("-" * 30)
    demonstrate_lists()

    # 2. Dictionaries
    print("\n2. DICTIONARIES")
    print("-" * 30)
    demonstrate_dictionaries()

    # 3. Sets
    print("\n3. SETS (MENGEN)")
    print("-" * 30)
    demonstrate_sets()

    # 4. Tupel
    print("\n4. TUPEL")
    print("-" * 30)
    demonstrate_tuples()

    # 5. Praktische Anwendungen
    print("\n5. PRAKTISCHE ANWENDUNGEN")
    print("-" * 30)
    demonstrate_practical_applications()


def demonstrate_lists():
    """Demonstriert Listen-Operationen"""
    # Listen erstellen
    maschinen = ["Laser", "Presse", "Stanze", "Schweissroboter"]
    produktionszeiten = [8.5, 7.2, 9.1, 6.8]

    print(f"Maschinen: {maschinen}")
    print(f"Produktionszeiten: {produktionszeiten}")
    print(f"Anzahl Maschinen: {len(maschinen)}")

    # Zugriff und Änderung
    print(f"\nErste Maschine: {maschinen[0]}")
    print(f"Letzte Maschine: {maschinen[-1]}")

    maschinen[1] = "Biegemaschine"  # Ändern
    print(f"Nach Änderung: {maschinen}")

    # Listen erweitern
    maschinen.append("CNC-Fräse")
    maschinen.insert(2, "Plasma")
    print(f"Erweiterte Liste: {maschinen}")

    # Listen-Methoden
    teilenummern = ["P001", "P003", "P002", "P001", "P004"]
    print(f"\nTeilenummern: {teilenummern}")

    teilenummern_sortiert = sorted(teilenummern)
    print(f"Sortiert: {teilenummern_sortiert}")

    print(f"Anzahl P001: {teilenummern.count('P001')}")
    print(f"Index von P003: {teilenummern.index('P003')}")

    # List Comprehensions
    messungen = [2.1, 1.95, 2.05, 2.15, 1.88, 2.02]
    toleranz = 0.1
    sollwert = 2.0

    print(f"\nMessungen: {messungen}")

    # Alle Werte im Toleranzbereich
    gueltige_werte = [m for m in messungen if abs(m - sollwert) <= toleranz]
    print(f"Gültige Werte: {gueltige_werte}")

    # Abweichungen berechnen
    abweichungen = [abs(m - sollwert) for m in messungen]
    print(f"Abweichungen: {[f'{a:.3f}' for a in abweichungen]}")

    # Qualitätsbewertung
    qualitaet = ["OK" if abs(m - sollwert) <= toleranz else "NOK" for m in messungen]
    print(f"Qualität: {qualitaet}")


def demonstrate_dictionaries():
    """Demonstriert Dictionary-Operationen"""
    # Einfaches Dictionary
    maschine = {
        "id": "LASER_001",
        "typ": "ByStar Fiber",
        "leistung": 6000,  # Watt
        "baujahr": 2020,
        "aktiv": True,
    }

    print(f"Maschine: {maschine}")
    print(f"Typ: {maschine['typ']}")
    print(f"Leistung: {maschine.get('leistung', 'Unbekannt')} W")

    # Dictionary erweitern
    maschine["wartung_datum"] = "2024-03-15"
    maschine["betriebsstunden"] = 12500

    print(f"\nErweiterte Maschine: {maschine}")

    # Dictionary durchlaufen
    print("\nAlle Eigenschaften:")
    for schluessel, wert in maschine.items():
        print(f"  {schluessel}: {wert}")

    # Verschachteltes Dictionary
    produktionsanlage = {
        "standort": "Halle A",
        "maschinen": {
            "LASER_001": {
                "typ": "ByStar Fiber",
                "status": "Aktiv",
                "wartung": {
                    "letzter_service": "2024-01-15",
                    "naechster_service": "2024-07-15",
                },
                "produktion": {"heute": 145, "diese_woche": 720, "diesen_monat": 3200},
            },
            "PRESSE_002": {
                "typ": "Xpert Pro",
                "status": "Wartung",
                "wartung": {
                    "letzter_service": "2024-02-20",
                    "naechster_service": "2024-08-20",
                },
                "produktion": {"heute": 0, "diese_woche": 450, "diesen_monat": 2100},
            },
        },
        "personal": [
            {
                "name": "Max Mustermann",
                "schicht": "Tag",
                "qualifikationen": ["Laser", "Presse"],
            },
            {
                "name": "Anna Müller",
                "schicht": "Nacht",
                "qualifikationen": ["Laser", "CNC"],
            },
        ],
    }

    print(f"\n=== Produktionsanlage {produktionsanlage['standort']} ===")

    # Maschinenstatus
    print("\nMaschinenstatus:")
    for maschinen_id, daten in produktionsanlage["maschinen"].items():
        status = daten["status"]
        heute = daten["produktion"]["heute"]
        print(f"  {maschinen_id}: {status} - {heute} Teile heute")

    # Personalübersicht
    print("\nPersonal:")
    for person in produktionsanlage["personal"]:
        qualifikationen = ", ".join(person["qualifikationen"])
        print(f"  {person['name']} ({person['schicht']}): {qualifikationen}")


def demonstrate_sets():
    """Demonstriert Set-Operationen"""
    # Sets erstellen
    materialien_laser = {"Stahl", "Aluminium", "Edelstahl", "Kupfer"}
    materialien_presse = {"Aluminium", "Kupfer", "Messing", "Titan"}

    print(f"Laser-Materialien: {materialien_laser}")
    print(f"Presse-Materialien: {materialien_presse}")

    # Mengenoperationen
    alle_materialien = materialien_laser | materialien_presse
    gemeinsame = materialien_laser & materialien_presse
    nur_laser = materialien_laser - materialien_presse
    nur_presse = materialien_presse - materialien_laser

    print(f"\nAlle Materialien: {alle_materialien}")
    print(f"Gemeinsame Materialien: {gemeinsame}")
    print(f"Nur für Laser: {nur_laser}")
    print(f"Nur für Presse: {nur_presse}")

    # Praktisches Beispiel: Qualifizierte Mitarbeiter
    laser_operatoren = {"Max", "Anna", "Peter", "Sarah"}
    presse_operatoren = {"Anna", "Tom", "Sarah", "Lisa"}
    cnc_operatoren = {"Peter", "Tom", "Michael"}

    print(f"\nLaser-Operatoren: {laser_operatoren}")
    print(f"Presse-Operatoren: {presse_operatoren}")
    print(f"CNC-Operatoren: {cnc_operatoren}")

    # Wer kann beide Maschinen bedienen?
    beide_maschinen = laser_operatoren & presse_operatoren
    print(f"Kann Laser + Presse: {beide_maschinen}")

    # Alle qualifizierten Mitarbeiter
    alle_operatoren = laser_operatoren | presse_operatoren | cnc_operatoren
    print(f"Alle Operatoren: {alle_operatoren}")

    # Duplikate aus Liste entfernen
    messwerte_mit_duplikaten = [2.1, 2.0, 2.1, 1.95, 2.0, 2.05, 2.1]
    eindeutige_messwerte = list(set(messwerte_mit_duplikaten))

    print(f"\nMesswerte mit Duplikaten: {messwerte_mit_duplikaten}")
    print(f"Eindeutige Messwerte: {sorted(eindeutige_messwerte)}")


def demonstrate_tuples():
    """Demonstriert Tupel-Operationen"""
    # Koordinaten als Tupel
    position_laser = (10.5, 20.8)
    position_presse = (15.2, 35.1)

    print(f"Laser Position: {position_laser}")
    print(f"X: {position_laser[0]}, Y: {position_laser[1]}")

    # Tupel als Dictionary-Schlüssel
    maschinenpositionen = {
        (0, 0): "Lagerplatz",
        (10, 20): "Laser Station 1",
        (15, 35): "Presse Station 1",
        (25, 40): "Qualitätskontrolle",
    }

    print("\nStationen:")
    for position, name in maschinenpositionen.items():
        x, y = position
        print(f"  Position ({x}, {y}): {name}")

    # Tupel für Funktionsrückgabe
    def analysiere_produktion(teile_soll, teile_ist, zeit_soll, zeit_ist):
        """Analysiert Produktionsdaten und gibt Kennzahlen zurück"""
        effizienz_menge = (teile_ist / teile_soll) * 100
        effizienz_zeit = (zeit_soll / zeit_ist) * 100
        teile_pro_stunde = teile_ist / zeit_ist

        return effizienz_menge, effizienz_zeit, teile_pro_stunde

    # Tupel entpacken
    eff_menge, eff_zeit, teile_h = analysiere_produktion(1000, 950, 8.0, 8.2)

    print("\nProduktionsanalyse:")
    print(f"  Mengen-Effizienz: {eff_menge:.1f}%")
    print(f"  Zeit-Effizienz: {eff_zeit:.1f}%")
    print(f"  Teile/Stunde: {teile_h:.1f}")

    # Tupel für Konfigurationsdaten
    laser_parameter = (
        ("Leistung", 6000, "W"),
        ("Geschwindigkeit", 15.5, "m/min"),
        ("Gasverbrauch", 2.5, "l/min"),
        ("Fokus", -1.5, "mm"),
    )

    print("\nLaser-Parameter:")
    for name, wert, einheit in laser_parameter:
        print(f"  {name}: {wert} {einheit}")


def demonstrate_practical_applications():
    """Praktische Anwendungen mit allen Collection-Typen"""

    # 1. Produktionsplanung
    print("1. Produktionsplanung:")
    produktionsplan = erstelle_produktionsplan()
    zeige_produktionsplan(produktionsplan)

    # 2. Qualitätskontrolle
    print("\n2. Qualitätskontrolle:")
    qualitaetsdaten = simuliere_qualitaetskontrolle()
    analysiere_qualitaetsdaten(qualitaetsdaten)

    # 3. Lagerverwaltung
    print("\n3. Lagerverwaltung:")
    lager = verwalte_lager()
    zeige_lagerbestand(lager)


def erstelle_produktionsplan():
    """Erstellt einen Produktionsplan mit verschiedenen Collection-Typen"""
    # Verfügbare Maschinen und ihre Fähigkeiten
    maschinen_faehigkeiten = {
        "LASER_001": {
            "materialien": {"Stahl", "Aluminium", "Edelstahl"},
            "max_dicke": 20,
        },
        "LASER_002": {"materialien": {"Stahl", "Aluminium"}, "max_dicke": 15},
        "PRESSE_001": {"materialien": {"Aluminium", "Kupfer"}, "max_kraft": 100},
        "PRESSE_002": {"materialien": {"Stahl", "Aluminium"}, "max_kraft": 150},
    }

    # Aufträge
    auftraege = [
        {
            "id": "A001",
            "teil": "Gehäuse",
            "material": "Stahl",
            "dicke": 5,
            "anzahl": 100,
        },
        {
            "id": "A002",
            "teil": "Deckel",
            "material": "Aluminium",
            "dicke": 3,
            "anzahl": 150,
        },
        {
            "id": "A003",
            "teil": "Bracket",
            "material": "Edelstahl",
            "dicke": 2,
            "anzahl": 200,
        },
    ]

    # Produktionsplan erstellen
    plan = {}

    for auftrag in auftraege:
        material = auftrag["material"]
        dicke = auftrag["dicke"]

        # Geeignete Maschinen finden
        geeignete_maschinen = []
        for maschine, faehigkeiten in maschinen_faehigkeiten.items():
            if material in faehigkeiten["materialien"] and (
                "max_dicke" in faehigkeiten and dicke <= faehigkeiten["max_dicke"]
            ):
                geeignete_maschinen.append(maschine)

        plan[auftrag["id"]] = {
            "auftrag": auftrag,
            "geeignete_maschinen": geeignete_maschinen,
        }

    return plan


def zeige_produktionsplan(plan):
    """Zeigt den Produktionsplan an"""
    for auftrag_id, daten in plan.items():
        auftrag = daten["auftrag"]
        maschinen = ", ".join(daten["geeignete_maschinen"])

        print(
            f"   {auftrag_id}: {auftrag['teil']} ({auftrag['material']}, {auftrag['dicke']}mm)"
        )
        print(f"   Menge: {auftrag['anzahl']} Stück")
        print(f"   Geeignete Maschinen: {maschinen}")
        print()


def simuliere_qualitaetskontrolle():
    """Simuliert Qualitätskontrolldaten"""
    random.seed(42)  # Für reproduzierbare Ergebnisse

    messungen = []
    sollwerte = {"dicke": 2.0, "breite": 50.0, "laenge": 100.0}
    toleranzen = {"dicke": 0.1, "breite": 0.5, "laenge": 1.0}

    for i in range(50):
        teil_nr = f"P{i + 1:03d}"

        messung = {
            "teil_nr": teil_nr,
            "timestamp": datetime.now(),
            "werte": {},
            "qualitaet_ok": True,
            "fehler": [],
        }

        # Messwerte simulieren (mit gelegentlichen Ausreissern)
        for eigenschaft, sollwert in sollwerte.items():
            if random.random() < 0.1:  # 10% Ausreisser
                abweichung = random.uniform(
                    -toleranzen[eigenschaft] * 2, toleranzen[eigenschaft] * 2
                )
            else:
                abweichung = random.uniform(
                    -toleranzen[eigenschaft] * 0.5, toleranzen[eigenschaft] * 0.5
                )

            wert = sollwert + abweichung
            messung["werte"][eigenschaft] = round(wert, 2)

            # Qualitätsprüfung
            if abs(abweichung) > toleranzen[eigenschaft]:
                messung["qualitaet_ok"] = False
                messung["fehler"].append(eigenschaft)

        messungen.append(messung)

    return messungen


def analysiere_qualitaetsdaten(messungen):
    """Analysiert Qualitätskontrolldaten"""
    gesamt = len(messungen)
    ok_teile = sum(1 for m in messungen if m["qualitaet_ok"])
    nok_teile = gesamt - ok_teile

    print(f"   Geprüfte Teile: {gesamt}")
    print(f"   OK-Teile: {ok_teile} ({ok_teile / gesamt * 100:.1f}%)")
    print(f"   NOK-Teile: {nok_teile} ({nok_teile / gesamt * 100:.1f}%)")

    # Fehleranalyse
    fehlertypen = {}
    for messung in messungen:
        for fehler in messung["fehler"]:
            fehlertypen[fehler] = fehlertypen.get(fehler, 0) + 1

    if fehlertypen:
        print("\n   Fehlerverteilung:")
        for fehlertyp, anzahl in sorted(fehlertypen.items()):
            print(f"     {fehlertyp}: {anzahl} ({anzahl / gesamt * 100:.1f}%)")

    # Statistische Auswertung
    print("\n   Statistische Werte:")
    for eigenschaft in ["dicke", "breite", "laenge"]:
        werte = [m["werte"][eigenschaft] for m in messungen]
        mittelwert = sum(werte) / len(werte)
        minimum = min(werte)
        maximum = max(werte)

        print(
            f"     {eigenschaft}: Ø{mittelwert:.2f} (Min: {minimum:.2f}, Max: {maximum:.2f})"
        )


def verwalte_lager():
    """Lagerverwaltung mit verschiedenen Collection-Typen"""
    # Lagerbestand als Dictionary
    lagerbestand = {
        "Stahl_2mm": {"bestand": 1500, "einheit": "kg", "mindestbestand": 200},
        "Aluminium_3mm": {"bestand": 800, "einheit": "kg", "mindestbestand": 150},
        "Edelstahl_1.5mm": {"bestand": 300, "einheit": "kg", "mindestbestand": 100},
        "Kupfer_2mm": {
            "bestand": 50,
            "einheit": "kg",
            "mindestbestand": 80,
        },  # Unter Mindestbestand
    }

    # Bestellungen (Liste von Tupeln)
    bestellungen = [
        ("Stahl_2mm", 500, date(2024, 3, 20)),
        ("Aluminium_3mm", 300, date(2024, 3, 18)),
        ("Kupfer_2mm", 200, date(2024, 3, 25)),
    ]

    # Kritische Materialien (Set)
    kritische_materialien = {
        material
        for material, daten in lagerbestand.items()
        if daten["bestand"] < daten["mindestbestand"]
    }

    return {
        "bestand": lagerbestand,
        "bestellungen": bestellungen,
        "kritisch": kritische_materialien,
    }


def zeige_lagerbestand(lager):
    """Zeigt Lagerbestand und Status an"""
    print("   Aktueller Lagerbestand:")
    print("   " + "-" * 50)

    for material, daten in lager["bestand"].items():
        bestand = daten["bestand"]
        mindest = daten["mindestbestand"]
        einheit = daten["einheit"]

        status = "⚠️  KRITISCH" if bestand < mindest else "✅ OK"
        print(f"   {material:20}: {bestand:>6} {einheit} (Min: {mindest:>3}) {status}")

    if lager["kritisch"]:
        print(f"\n   Kritische Materialien: {len(lager['kritisch'])}")
        for material in sorted(lager["kritisch"]):
            print(f"     • {material}")

    print(f"\n   Offene Bestellungen: {len(lager['bestellungen'])}")
    for material, menge, lieferdatum in lager["bestellungen"]:
        print(f"     • {material}: {menge} kg (Lieferung: {lieferdatum})")


if __name__ == "__main__":
    main()

    print("\n" + "=" * 50)
    print("Programm beendet. Drücken Sie Enter...")
    input()
