#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
VBA vs Python: Collections-Vergleich

Dieses Skript zeigt die Unterschiede zwischen VBA und Python
bei der Arbeit mit Collections/Datenstrukturen anhand
praktischer Bystronic-Beispiele.
"""


def main():
    print("=" * 60)
    print("VBA vs PYTHON: COLLECTIONS-VERGLEICH")
    print("=" * 60)

    print(
        """
Dieser Vergleich zeigt, wie Collections und Datenstrukturen
in VBA vs Python für typische Bystronic-Aufgaben verwendet werden.
"""
    )

    # 1. Arrays vs Listen
    print("\n1. ARRAYS vs LISTEN")
    print("=" * 40)
    compare_arrays_vs_lists()

    # 2. Collections vs Dictionaries
    print("\n2. COLLECTIONS vs DICTIONARIES")
    print("=" * 40)
    compare_collections_vs_dictionaries()

    # 3. Sets - Neu in Python
    print("\n3. SETS - MENGEN (NEU IN PYTHON)")
    print("=" * 40)
    demonstrate_sets_python_only()

    # 4. Verschachtelte Strukturen
    print("\n4. VERSCHACHTELTE DATENSTRUKTUREN")
    print("=" * 40)
    compare_nested_structures()

    # 5. Praktisches Beispiel
    print("\n5. PRAKTISCHES BEISPIEL: PRODUKTIONSDATEN")
    print("=" * 40)
    practical_production_example()


def compare_arrays_vs_lists():
    """Vergleicht VBA Arrays mit Python Listen"""

    print(
        """
VBA - STATISCHE ARRAYS:
-----------------------"""
    )

    vba_code = """
' VBA: Arrays sind statisch und müssen deklariert werden
Dim maschinen(1 To 4) As String
maschinen(1) = "Laser"
maschinen(2) = "Presse"
maschinen(3) = "Stanze"
maschinen(4) = "CNC"

' Grösse ändern ist umständlich
ReDim Preserve maschinen(1 To 5)
maschinen(5) = "Plasma"

' Durchlaufen
For i = 1 To UBound(maschinen)
    Debug.Print maschinen(i)
Next i
"""
    print(vba_code)

    print(
        """
PYTHON - DYNAMISCHE LISTEN:
---------------------------"""
    )

    # Python: Listen sind dynamisch
    maschinen = ["Laser", "Presse", "Stanze", "CNC"]
    print(f"Ursprüngliche Liste: {maschinen}")

    # Einfach erweitern
    maschinen.append("Plasma")
    maschinen.insert(2, "Biege")  # An Position 2 einfügen
    print(f"Nach Erweiterung: {maschinen}")

    # Durchlaufen (mehrere Möglichkeiten)
    print("\nDurchlaufen - Methode 1:")
    for maschine in maschinen:
        print(f"  {maschine}")

    print("\nDurchlaufen - Methode 2 (mit Index):")
    for i, maschine in enumerate(maschinen):
        print(f"  {i + 1}: {maschine}")

    # Praktische Listen-Operationen
    produktionszeiten = [8.5, 7.2, 9.1, 6.8, 8.0, 7.5]

    print(f"\nProduktionszeiten: {produktionszeiten}")
    print(f"Durchschnitt: {sum(produktionszeiten) / len(produktionszeiten):.1f}h")
    print(f"Maximum: {max(produktionszeiten)}h")
    print(f"Minimum: {min(produktionszeiten)}h")
    print(f"Sortiert: {sorted(produktionszeiten)}")

    # List Comprehensions (gibt es in VBA nicht)
    ueberstunden = [zeit - 8.0 for zeit in produktionszeiten if zeit > 8.0]
    print(f"Überstunden: {ueberstunden}")

    print(
        """
VORTEILE PYTHON LISTEN:
• Dynamische Grösse
• Viele eingebaute Methoden
• List Comprehensions
• Können verschiedene Datentypen enthalten
• Negative Indizierung möglich
"""
    )


def compare_collections_vs_dictionaries():
    """Vergleicht VBA Collections mit Python Dictionaries"""

    print(
        """
VBA - COLLECTIONS:
------------------"""
    )

    vba_code = """
' VBA: Collections für Key-Value Paare
Dim mitarbeiter As Collection
Set mitarbeiter = New Collection

mitarbeiter.Add "Max Mustermann", "ID001"
mitarbeiter.Add "Anna Müller", "ID002"

' Zugriff nur über Key
Debug.Print mitarbeiter("ID001")

' Durchlaufen nur über Werte, nicht über Keys
For Each name In mitarbeiter
    Debug.Print name
Next
"""
    print(vba_code)

    print(
        """
PYTHON - DICTIONARIES:
----------------------"""
    )

    # Python: Dictionaries sind viel mächtiger
    mitarbeiter = {
        "ID001": {
            "name": "Max Mustermann",
            "abteilung": "Produktion",
            "gehalt": 75000,
            "qualifikationen": ["Laser", "Presse"],
            "aktiv": True,
        },
        "ID002": {
            "name": "Anna Müller",
            "abteilung": "Qualität",
            "gehalt": 68000,
            "qualifikationen": ["Messtechnik", "CAD"],
            "aktiv": True,
        },
    }

    print("Mitarbeiter-Dictionary:")
    for id, daten in mitarbeiter.items():
        print(f"  {id}: {daten['name']} - {daten['abteilung']}")
        print(f"    Qualifikationen: {', '.join(daten['qualifikationen'])}")

    # Flexible Zugriffe
    print(f"\nMax's Gehalt: {mitarbeiter['ID001']['gehalt']}€")
    print(f"Anna's Qualifikationen: {mitarbeiter['ID002']['qualifikationen']}")

    # Dictionary-Methoden
    print(f"\nAlle IDs: {list(mitarbeiter.keys())}")
    print(f"Alle Namen: {[d['name'] for d in mitarbeiter.values()]}")

    # Neue Daten hinzufügen
    mitarbeiter["ID003"] = {
        "name": "Peter Schmidt",
        "abteilung": "IT",
        "gehalt": 80000,
        "qualifikationen": ["Python", "SQL"],
        "aktiv": True,
    }

    print(f"Nach Hinzufügung: {len(mitarbeiter)} Mitarbeiter")

    # Auswertungen
    durchschnitts_gehalt = sum(m["gehalt"] for m in mitarbeiter.values()) / len(
        mitarbeiter
    )
    print(f"Durchschnittsgehalt: {durchschnitts_gehalt:.0f}€")

    # Mitarbeiter nach Abteilung
    abteilungen = {}
    for daten in mitarbeiter.values():
        abt = daten["abteilung"]
        if abt not in abteilungen:
            abteilungen[abt] = []
        abteilungen[abt].append(daten["name"])

    print("\nMitarbeiter nach Abteilung:")
    for abteilung, namen in abteilungen.items():
        print(f"  {abteilung}: {', '.join(namen)}")

    print(
        """
VORTEILE PYTHON DICTIONARIES:
• Verschachtelte Strukturen möglich
• Flexible Key-Typen (nicht nur Strings)
• Durchlaufen von Keys, Values und Items
• Viele eingebaute Methoden
• Dictionary Comprehensions
• Sehr schneller Zugriff
"""
    )


def demonstrate_sets_python_only():
    """Zeigt Sets - gibt es in VBA nicht"""

    print(
        """
Python Sets haben KEIN Äquivalent in VBA!
Sets sind Sammlungen eindeutiger Elemente.
"""
    )

    # Beispiel: Materialien pro Maschine
    laser_materialien = {"Stahl", "Aluminium", "Edelstahl", "Kupfer"}
    presse_materialien = {"Aluminium", "Kupfer", "Messing", "Titan"}
    cnc_materialien = {"Stahl", "Aluminium", "Titan", "Kunststoff"}

    print(f"Laser kann schneiden: {laser_materialien}")
    print(f"Presse kann verformen: {presse_materialien}")
    print(f"CNC kann bearbeiten: {cnc_materialien}")

    # Mengenoperationen
    print(
        f"\nAlle verfügbaren Materialien: {laser_materialien | presse_materialien | cnc_materialien}"
    )
    print(f"Laser + Presse gemeinsam: {laser_materialien & presse_materialien}")
    print(f"Nur Laser (nicht Presse): {laser_materialien - presse_materialien}")

    # Praktisches Beispiel: Qualifizierte Operatoren
    laser_operatoren = {"Max", "Anna", "Peter"}
    presse_operatoren = {"Anna", "Tom", "Sarah"}
    cnc_operatoren = {"Peter", "Tom", "Michael"}

    print("\nOperatoren-Qualifikationen:")
    print(f"Laser: {laser_operatoren}")
    print(f"Presse: {presse_operatoren}")
    print(f"CNC: {cnc_operatoren}")

    # Wer kann was?
    universal_operatoren = laser_operatoren & presse_operatoren & cnc_operatoren
    laser_und_presse = laser_operatoren & presse_operatoren

    print(f"\nUniversal (alle 3 Maschinen): {universal_operatoren}")
    print(f"Laser + Presse: {laser_und_presse}")
    print(f"Alle Operatoren: {laser_operatoren | presse_operatoren | cnc_operatoren}")

    # Duplikate entfernen
    messwerte_mit_duplikaten = [2.1, 2.0, 2.1, 1.95, 2.0, 2.05, 2.1]
    eindeutige_werte = list(set(messwerte_mit_duplikaten))

    print(f"\nMesswerte mit Duplikaten: {messwerte_mit_duplikaten}")
    print(f"Eindeutige Werte: {sorted(eindeutige_werte)}")

    print(
        """
SET-VORTEILE:
• Automatisch eindeutige Elemente
• Sehr schnelle Mitgliedschaftstests (in/not in)
• Mengenoperationen (Vereinigung, Schnitt, Differenz)
• Duplikate entfernen
"""
    )


def compare_nested_structures():
    """Vergleicht verschachtelte Datenstrukturen"""

    print(
        """
VBA - BEGRENZTE VERSCHACHTELUNG:
--------------------------------"""
    )

    vba_code = """
' VBA: Verschachtelte Collections sind umständlich
Dim produktionsanlage As Collection
Set produktionsanlage = New Collection

Dim maschine1 As Collection
Set maschine1 = New Collection
maschine1.Add "ByStar Fiber", "typ"
maschine1.Add "Aktiv", "status"

produktionsanlage.Add maschine1, "LASER_001"

' Zugriff ist umständlich
Debug.Print produktionsanlage("LASER_001")("typ")
"""
    print(vba_code)

    print(
        """
PYTHON - FLEXIBLE VERSCHACHTELUNG:
----------------------------------"""
    )

    # Komplexe verschachtelte Struktur
    produktionsanlage = {
        "standort": "Niederönz",
        "hallen": {
            "A": {
                "flaeche": 2000,  # m²
                "maschinen": {
                    "LASER_001": {
                        "typ": "ByStar Fiber 6kW",
                        "status": "Aktiv",
                        "position": (10, 20),
                        "wartung": {
                            "letzter_service": "2024-01-15",
                            "naechster_service": "2024-07-15",
                            "wartungskosten": [1500, 1200, 1800],
                        },
                        "produktion": {
                            "2024-03": {"teile": 3200, "stunden": 160},
                            "2024-02": {"teile": 2950, "stunden": 155},
                            "2024-01": {"teile": 3100, "stunden": 158},
                        },
                    }
                },
            },
            "B": {
                "flaeche": 1500,
                "maschinen": {
                    "PRESSE_001": {
                        "typ": "Xpert Pro 150",
                        "status": "Wartung",
                        "position": (15, 30),
                        "wartung": {
                            "letzter_service": "2024-02-20",
                            "naechster_service": "2024-08-20",
                            "wartungskosten": [2000, 1500, 2200],
                        },
                    }
                },
            },
        },
        "personal": {
            "tagschicht": [
                {"name": "Max", "qualifikationen": ["Laser", "Presse"]},
                {"name": "Anna", "qualifikationen": ["Laser", "CNC"]},
            ],
            "nachtschicht": [
                {"name": "Tom", "qualifikationen": ["Presse"]},
                {"name": "Sarah", "qualifikationen": ["Laser"]},
            ],
        },
    }

    # Einfache Navigation durch komplexe Strukturen
    print(f"Standort: {produktionsanlage['standort']}")

    # Alle Maschinen und deren Status
    print("\nMaschinenstatus:")
    for halle, halle_daten in produktionsanlage["hallen"].items():
        print(f"  Halle {halle} ({halle_daten['flaeche']}m²):")
        for maschine, daten in halle_daten["maschinen"].items():
            print(f"    {maschine}: {daten['typ']} - {daten['status']}")

    # Wartungskosten auswerten
    print("\nWartungskosten:")
    for halle_daten in produktionsanlage["hallen"].values():
        for maschine, daten in halle_daten["maschinen"].items():
            kosten = daten["wartung"]["wartungskosten"]
            durchschnitt = sum(kosten) / len(kosten)
            print(f"  {maschine}: Ø {durchschnitt:.0f}€ (Gesamt: {sum(kosten)}€)")

    # Personalauswertung
    print("\nPersonal:")
    for schicht, mitarbeiter in produktionsanlage["personal"].items():
        print(f"  {schicht}: {len(mitarbeiter)} Mitarbeiter")
        for person in mitarbeiter:
            qualifikationen = ", ".join(person["qualifikationen"])
            print(f"    {person['name']}: {qualifikationen}")

    print(
        """
PYTHON VERSCHACHTELUNG:
• Beliebig tiefe Strukturen möglich
• Listen in Dictionaries in Listen...
• Einfache Navigation mit []
• Flexible Datenmodellierung
• JSON-kompatibel
"""
    )


def practical_production_example():
    """Praktisches Beispiel mit allen Datentypen"""

    print(
        """
PRAKTISCHES BEISPIEL: PRODUKTIONSAUSWERTUNG
------------------------------------------
Dieses Beispiel zeigt, wie Python's Collections
für eine komplette Produktionsauswertung verwendet werden.
"""
    )

    # Produktionsdaten der letzten Woche
    wochendaten = {
        "kw": 12,
        "jahr": 2024,
        "tage": {
            "montag": {
                "datum": "2024-03-18",
                "schichten": {
                    "tag": {
                        "stunden": 8,
                        "mitarbeiter": 3,
                        "maschinen": ["LASER_001", "PRESSE_001"],
                    },
                    "nacht": {
                        "stunden": 8,
                        "mitarbeiter": 2,
                        "maschinen": ["LASER_001"],
                    },
                },
                "produktion": {"LASER_001": 145, "PRESSE_001": 89},
                "ausschuss": {"LASER_001": 3, "PRESSE_001": 7},
                "ausfallzeiten": {"LASER_001": 0.5, "PRESSE_001": 1.2},  # Stunden
            },
            "dienstag": {
                "datum": "2024-03-19",
                "schichten": {
                    "tag": {
                        "stunden": 8,
                        "mitarbeiter": 3,
                        "maschinen": ["LASER_001", "PRESSE_001"],
                    },
                    "nacht": {
                        "stunden": 8,
                        "mitarbeiter": 2,
                        "maschinen": ["LASER_001"],
                    },
                },
                "produktion": {"LASER_001": 152, "PRESSE_001": 76},
                "ausschuss": {"LASER_001": 2, "PRESSE_001": 5},
                "ausfallzeiten": {"LASER_001": 0.2, "PRESSE_001": 2.1},
            },
            # Weitere Tage...
            "mittwoch": {
                "datum": "2024-03-20",
                "schichten": {
                    "tag": {
                        "stunden": 8,
                        "mitarbeiter": 3,
                        "maschinen": ["LASER_001", "PRESSE_001"],
                    },
                    "nacht": {
                        "stunden": 8,
                        "mitarbeiter": 2,
                        "maschinen": ["LASER_001"],
                    },
                },
                "produktion": {"LASER_001": 138, "PRESSE_001": 92},
                "ausschuss": {"LASER_001": 4, "PRESSE_001": 3},
                "ausfallzeiten": {"LASER_001": 1.0, "PRESSE_001": 0.8},
            },
        },
    }

    # Auswertung mit allen Collection-Typen

    # 1. Listen für Berechnungen
    laser_produktion = []
    presse_produktion = []
    gesamt_ausschuss = []

    for tag_daten in wochendaten["tage"].values():
        laser_produktion.append(tag_daten["produktion"]["LASER_001"])
        presse_produktion.append(tag_daten["produktion"]["PRESSE_001"])

        tag_ausschuss = sum(tag_daten["ausschuss"].values())
        gesamt_ausschuss.append(tag_ausschuss)

    print(f"Laser Produktion: {laser_produktion}")
    print(f"Presse Produktion: {presse_produktion}")
    print(f"Täglicher Ausschuss: {gesamt_ausschuss}")

    # 2. Dictionary für Zusammenfassungen
    zusammenfassung = {
        "gesamt_teile": sum(laser_produktion) + sum(presse_produktion),
        "laser_durchschnitt": sum(laser_produktion) / len(laser_produktion),
        "presse_durchschnitt": sum(presse_produktion) / len(presse_produktion),
        "ausschuss_rate": sum(gesamt_ausschuss)
        / (sum(laser_produktion) + sum(presse_produktion))
        * 100,
    }

    print("\nZusammenfassung:")
    for key, value in zusammenfassung.items():
        if isinstance(value, float):
            print(f"  {key}: {value:.1f}")
        else:
            print(f"  {key}: {value}")

    # 3. Sets für eindeutige Werte
    verwendete_maschinen = set()
    arbeitstage = set()

    for tag, daten in wochendaten["tage"].items():
        arbeitstage.add(tag)
        for schicht_daten in daten["schichten"].values():
            verwendete_maschinen.update(schicht_daten["maschinen"])

    print(f"\nVerfügbare Maschinen: {verwendete_maschinen}")
    print(f"Arbeitstage: {arbeitstage}")

    # 4. Tupel für Koordination
    effizienzen = []
    for tag, daten in wochendaten["tage"].items():
        for maschine in ["LASER_001", "PRESSE_001"]:
            produktion = daten["produktion"][maschine]
            ausschuss = daten["ausschuss"][maschine]
            ausfallzeit = daten["ausfallzeiten"][maschine]

            # Effizienz als Tupel (Tag, Maschine, Produktion, Qualitätsrate, Verfügbarkeit)
            qualitaetsrate = ((produktion - ausschuss) / produktion) * 100
            verfügbarkeit = ((8 - ausfallzeit) / 8) * 100

            effizienzen.append(
                (tag, maschine, produktion, qualitaetsrate, verfügbarkeit)
            )

    print("\nEffizienz-Analyse:")
    print(f"{'Tag':<10} {'Maschine':<12} {'Teile':<6} {'Qualität':<8} {'Verfügbar.'}")
    print("-" * 50)

    for tag, maschine, teile, qualitaet, verfuegbar in effizienzen:
        print(
            f"{tag:<10} {maschine:<12} {teile:<6} {qualitaet:>6.1f}% {verfuegbar:>8.1f}%"
        )

    # Beste und schlechteste Werte finden
    beste_qualitaet = max(effizienzen, key=lambda x: x[3])
    schlechteste_verfügbar = min(effizienzen, key=lambda x: x[4])

    print(
        f"\nBeste Qualität: {beste_qualitaet[1]} am {beste_qualitaet[0]} ({beste_qualitaet[3]:.1f}%)"
    )
    print(
        f"Schlechteste Verfügbarkeit: {schlechteste_verfügbar[1]} am {schlechteste_verfügbar[0]} ({schlechteste_verfügbar[4]:.1f}%)"
    )

    print(
        """
ZUSAMMENFASSUNG DES VERGLEICHS:
==============================

VBA LIMITATIONS:
• Statische Arrays
• Begrenzte Collections
• Keine Sets/Mengen
• Umständliche Verschachtelung
• Wenig eingebaute Funktionen

PYTHON VORTEILE:
• Dynamische Listen mit vielen Methoden
• Mächtige Dictionaries für strukturierte Daten
• Sets für Mengenoperationen
• Beliebige Verschachtelung möglich
• List/Dict/Set Comprehensions
• Sehr lesbare und kompakte Syntax
• Bessere Performance bei grossen Datenmengen

→ Python ist für Datenanalyse deutlich besser geeignet!
"""
    )


if __name__ == "__main__":
    main()

    print("\n" + "=" * 60)
    print("Vergleich beendet. Drücken Sie Enter...")
    input()
