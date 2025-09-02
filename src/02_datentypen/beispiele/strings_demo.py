#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Beispiel: String-Manipulation und Formatierung

Dieses Skript demonstriert die Arbeit mit Strings in Python
für typische Bystronic-Anwendungen wie Dateipfade, Teilenummern,
Berichte und Datenvalidierung.
"""

import datetime
import re


def main():
    print("=" * 50)
    print("BYSTRONIC - STRING-VERARBEITUNG")
    print("=" * 50)

    # 1. String-Erstellung
    print("\n1. STRING-ERSTELLUNG")
    print("-" * 30)
    demonstrate_string_creation()

    # 2. String-Operationen
    print("\n2. STRING-OPERATIONEN")
    print("-" * 30)
    demonstrate_string_operations()

    # 3. String-Formatierung
    print("\n3. STRING-FORMATIERUNG")
    print("-" * 30)
    demonstrate_string_formatting()

    # 4. String-Validierung
    print("\n4. STRING-VALIDIERUNG")
    print("-" * 30)
    demonstrate_string_validation()

    # 5. Praktische Anwendungen
    print("\n5. PRAKTISCHE ANWENDUNGEN")
    print("-" * 30)
    demonstrate_practical_applications()


def demonstrate_string_creation():
    """Verschiedene Arten der String-Erstellung"""
    # Einfache Strings
    firma = "Bystronic"
    maschine = "ByStar Fiber"

    # Mehrzeilige Strings
    beschreibung = """Bystronic ist ein führender Anbieter von
Blechbearbeitungsmaschinen und Automatisierungslösungen
für die industrielle Fertigung."""

    # Raw Strings (für Dateipfade, reguläre Ausdrücke)
    dateipfad = r"C:\Bystronic\Daten\Produktion\2024\März"
    regex_pattern = r"\d{4}-\d{2}-\d{2}"  # Datum-Pattern

    print(f"Firma: {firma}")
    print(f"Maschine: {maschine}")
    print(f"Beschreibung: {beschreibung[:50]}...")
    print(f"Dateipfad: {dateipfad}")
    print(f"Regex Pattern: {regex_pattern}")

    # String-Eigenschaften
    teil_nummer = "BSF-6000-2024-001"
    print(f"\nTeilnummer: {teil_nummer}")
    print(f"Länge: {len(teil_nummer)} Zeichen")
    print(f"Erstes Zeichen: '{teil_nummer[0]}'")
    print(f"Letztes Zeichen: '{teil_nummer[-1]}'")
    print(f"Mittlerer Teil: '{teil_nummer[4:8]}'")


def demonstrate_string_operations():
    """String-Manipulationen und -Methoden"""
    original = "  BYSTRONIC LASER CUTTING MACHINE  "

    print(f"Original: '{original}'")
    print(f"Kleinbuchstaben: '{original.lower()}'")
    print(f"Grossbuchstaben: '{original.upper()}'")
    print(f"Titel-Format: '{original.title()}'")
    print(f"Leerzeichen entfernt: '{original.strip()}'")
    print(f"Links ausgerichtet: '{original.strip().ljust(40, '-')}'")
    print(f"Zentriert: '{original.strip().center(40, '-')}'")

    # String-Ersetzung und Aufteilen
    text = "Laser,Presse,Stanze,Schweissroboter"
    print(f"\nMaschinen: {text}")
    print(f"Ersetzt: {text.replace('Laser', 'Plasma')}")
    print(f"Aufgeteilt: {text.split(',')}")

    # String-Verbindung
    teile = ["Gehäuse", "Deckel", "Griff", "Schraube"]
    print(f"\nTeile einzeln: {teile}")
    print(f"Verbunden: {' + '.join(teile)}")
    print(f"Als Liste: {', '.join(teile)}")


def demonstrate_string_formatting():
    """Verschiedene String-Formatierungsmethoden"""
    # Produktionsdaten
    datum = datetime.date.today()
    schicht = "Tagschicht"
    mitarbeiter = "Max Mustermann"
    teile_produziert = 1247
    soll_teile = 1200
    effizienz = (teile_produziert / soll_teile) * 100
    kosten_pro_teil = 12.75

    print("f-String Formatierung (modern, empfohlen):")
    bericht = f"""
Produktionsbericht vom {datum.strftime("%d.%m.%Y")}
{"=" * 45}
Schicht: {schicht}
Mitarbeiter: {mitarbeiter}
Produzierte Teile: {teile_produziert:,} von {soll_teile:,}
Effizienz: {effizienz:.1f}%
Kosten pro Teil: {kosten_pro_teil:.2f}€
Gesamtkosten: {teile_produziert * kosten_pro_teil:,.2f}€
"""
    print(bericht)

    print("\n.format() Methode:")
    template = "Teil {}: {} Stück à {:.2f}€ = {:.2f}€"
    print(template.format("A001", 100, 15.50, 100 * 15.50))

    print("\n% Formatierung (alt):")
    print("Maschine %s: %d%% Auslastung" % ("LASER_001", 85))

    # Erweiterte Formatierung
    print("\nErweiterte f-String Formatierung:")
    werte = [1234.567, 0.123456, 1234567.89]
    for wert in werte:
        print(f"Zahl: {wert:>12.2f}")  # Rechtsbündig, 2 Dezimalstellen
        print(f"Prozent: {wert / 100:>10.1%}")  # Als Prozent
        print(f"Wissenschaftlich: {wert:>12.2e}")  # Wissenschaftliche Notation
        print("-" * 30)


def demonstrate_string_validation():
    """String-Validierung für verschiedene Anwendungsfälle"""
    print("String-Validierung:")

    # Teilenummer validieren
    teilenummern = ["BSF-6000-001", "bsf6000002", "BSF_6000_003", "INVALID", ""]

    def ist_gueltige_teilenummer(nummer):
        """Prüft ob Teilenummer dem Format BSF-XXXX-XXX entspricht"""
        pattern = r"^BSF-\d{4}-\d{3}$"
        return bool(re.match(pattern, nummer))

    print("\nTeilenummern-Validierung:")
    for nummer in teilenummern:
        gueltig = ist_gueltige_teilenummer(nummer)
        status = "✅ Gültig" if gueltig else "❌ Ungültig"
        print(f"  '{nummer}': {status}")

    # E-Mail Validierung
    emails = [
        "max.mustermann@bystronic.com",
        "anna.mueller@bystronic.ch",
        "invalid.email",
        "test@domain",
        "",
    ]

    print("\nE-Mail Validierung:")
    for email in emails:
        # Einfache E-Mail Validierung
        gueltig = "@" in email and "." in email.split("@")[-1] if email else False
        status = "✅ Gültig" if gueltig else "❌ Ungültig"
        print(f"  '{email}': {status}")

    # String-Eigenschaften prüfen
    test_strings = ["12345", "abc123", "BYSTRONIC", "Test 123", ""]

    print("\nString-Eigenschaften:")
    for s in test_strings:
        if s:  # Nur wenn String nicht leer
            print(f"  '{s}':")
            print(f"    Numerisch: {s.isnumeric()}")
            print(f"    Alphabetisch: {s.isalpha()}")
            print(f"    Alphanumerisch: {s.isalnum()}")
            print(f"    Grossbuchstaben: {s.isupper()}")
            print(f"    Kleinbuchstaben: {s.islower()}")


def demonstrate_practical_applications():
    """Praktische String-Anwendungen für Bystronic"""

    # 1. Dateinamen generieren
    print("1. Dateinamen generieren:")
    heute = datetime.date.today()
    maschine = "LASER_001"
    schicht = "T"  # T=Tag, N=Nacht

    dateiname = f"Produktion_{maschine}_{heute.strftime('%Y%m%d')}_{schicht}.csv"
    print(f"   {dateiname}")

    # 2. Bericht erstellen
    print("\n2. Produktionsbericht erstellen:")
    erstelle_produktionsbericht()

    # 3. Konfigurationsdatei parsen
    print("\n3. Konfiguration verarbeiten:")
    parse_konfiguration()

    # 4. CSV-Daten formatieren
    print("\n4. CSV-Daten formatieren:")
    formatiere_csv_daten()


def erstelle_produktionsbericht():
    """Erstellt einen formatierten Produktionsbericht"""
    daten = {
        "datum": datetime.date.today(),
        "schicht": "Tagschicht (06:00-14:00)",
        "maschinen": [
            {"name": "LASER_001", "teile": 145, "laufzeit": 7.5, "ausfallzeit": 0.5},
            {"name": "PRESSE_002", "teile": 89, "laufzeit": 6.8, "ausfallzeit": 1.2},
            {"name": "STANZE_003", "teile": 156, "laufzeit": 7.8, "ausfallzeit": 0.2},
        ],
    }

    bericht = f"""
BYSTRONIC PRODUKTIONSBERICHT
{"=" * 50}
Datum: {daten["datum"].strftime("%d.%m.%Y")}
Schicht: {daten["schicht"]}

MASCHINENSTATUS:
{"-" * 50}
"""

    gesamt_teile = 0
    gesamt_laufzeit = 0

    for maschine in daten["maschinen"]:
        effizienz = (
            maschine["laufzeit"] / (maschine["laufzeit"] + maschine["ausfallzeit"])
        ) * 100
        teile_pro_stunde = (
            maschine["teile"] / maschine["laufzeit"] if maschine["laufzeit"] > 0 else 0
        )

        bericht += f"""
{maschine["name"]:>12}: {maschine["teile"]:>3} Teile | {maschine["laufzeit"]:>4.1f}h | {effizienz:>5.1f}% | {teile_pro_stunde:>4.1f} T/h"""

        gesamt_teile += maschine["teile"]
        gesamt_laufzeit += maschine["laufzeit"]

    bericht += f"""

{"-" * 50}
ZUSAMMENFASSUNG:
Gesamt produzierte Teile: {gesamt_teile:>6}
Durchschn. Teile/Stunde: {gesamt_teile / gesamt_laufzeit:>8.1f}
"""

    print(bericht)


def parse_konfiguration():
    """Simuliert das Parsen einer Konfigurationsdatei"""
    config_text = """
# Bystronic Maschinen-Konfiguration
LASER_POWER=6000
CUTTING_SPEED=15.5
MATERIAL_THICKNESS=2.5
OPERATOR=Max.Mustermann
SHIFT=DAY
DEBUG=true
"""

    config = {}

    for line in config_text.strip().split("\n"):
        line = line.strip()

        # Kommentare und leere Zeilen überspringen
        if line.startswith("#") or not line:
            continue

        # Key=Value aufteilen
        if "=" in line:
            key, value = line.split("=", 1)

            # Datentyp erkennen und konvertieren
            if value.lower() in ["true", "false"]:
                config[key] = value.lower() == "true"
            elif value.replace(".", "").isdigit():
                config[key] = float(value) if "." in value else int(value)
            else:
                config[key] = value

    print("   Geladene Konfiguration:")
    for key, value in config.items():
        typ = type(value).__name__
        print(f"     {key}: {value} ({typ})")


def formatiere_csv_daten():
    """Formatiert Daten für CSV-Export"""
    produktionsdaten = [
        {"Teil": "BSF-001", "Anzahl": 150, "Zeit": 2.5, "OK": True},
        {"Teil": "BSF-002", "Anzahl": 89, "Zeit": 1.8, "OK": False},
        {"Teil": "BSF-003", "Anzahl": 134, "Zeit": 3.2, "OK": True},
    ]

    # CSV-Header
    header = "Teil;Anzahl;Zeit(h);Status;Effizienz(%)"
    print(f"   {header}")
    print(f"   {'-' * len(header)}")

    # CSV-Daten
    for daten in produktionsdaten:
        effizienz = (
            (daten["Anzahl"] / daten["Zeit"]) / 60 * 100
        )  # Teile pro Stunde als %
        status = "OK" if daten["OK"] else "Fehler"

        zeile = f"{daten['Teil']};{daten['Anzahl']};{daten['Zeit']:.1f};{status};{effizienz:.1f}"
        print(f"   {zeile}")


if __name__ == "__main__":
    main()

    print("\n" + "=" * 50)
    print("Programm beendet. Drücken Sie Enter...")
    input()
