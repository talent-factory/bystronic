#!/usr/bin/env python3
"""
🟡 INTERMEDIATE: Übung 1 - Mitarbeiterprofil-System
==================================================

LERNZIELE:
- Funktionen definieren und verwenden
- Dictionaries für strukturierte Daten
- Fehlerbehandlung mit try/except
- Erweiterte String-Formatierung
- Code-Organisation und Modularität

AUFGABE:
Erstellen Sie ein professionelles Mitarbeiterprofil-System mit
Validierung, Fehlerbehandlung und schöner Ausgabe.

ZEIT: 25-40 Minuten
SCHWIERIGKEIT: 🟡 Fortgeschritten

ANFORDERUNGEN:
- Funktionale Programmierung
- Eingabevalidierung
- Professionelle Ausgabe
- Fehlerbehandlung
"""


def sammle_mitarbeiterdaten() -> dict:
    """
    Sammelt Mitarbeiterdaten mit Validierung.

    Returns:
        Dictionary mit validierten Mitarbeiterdaten
    """
    mitarbeiter = {}

    # TODO 1: Name sammeln (nicht leer)
    while True:
        name = input("Vollständiger Name: ").strip()
        if name:  # Prüfe ob nicht leer
            mitarbeiter["name"] = name
            break
        print("❌ Name darf nicht leer sein!")

    # TODO 2: Alter sammeln (mit Validierung)
    while True:
        try:
            alter = int(input("Alter: "))
            if 16 <= alter <= 100:  # Realistische Grenzen
                mitarbeiter["alter"] = alter
                break
            else:
                print("❌ Alter muss zwischen 16 und 100 Jahren liegen!")
        except ValueError:
            print("❌ Bitte geben Sie eine gültige Zahl ein!")

    # TODO 3: Abteilung sammeln
    abteilungen = ["Engineering", "Production", "Sales", "HR", "IT", "Finance"]
    print(f"\nVerfügbare Abteilungen: {', '.join(abteilungen)}")

    while True:
        abteilung = input("Abteilung: ").strip()
        if abteilung in abteilungen:
            mitarbeiter["abteilung"] = abteilung
            break
        print("❌ Bitte wählen Sie eine der verfügbaren Abteilungen!")

    # TODO 4: Berufserfahrung (optional)
    while True:
        erfahrung_input = input(
            "Jahre Berufserfahrung (Enter für überspringen): "
        ).strip()
        if not erfahrung_input:  # Leer = überspringen
            mitarbeiter["berufserfahrung"] = None
            break
        try:
            erfahrung = int(erfahrung_input)
            if 0 <= erfahrung <= 50:
                mitarbeiter["berufserfahrung"] = erfahrung
                break
            else:
                print("❌ Berufserfahrung muss zwischen 0 und 50 Jahren liegen!")
        except ValueError:
            print("❌ Bitte geben Sie eine gültige Zahl ein!")

    return mitarbeiter


def berechne_zusatzinfos(mitarbeiter: dict) -> dict:
    """
    Berechnet zusätzliche Informationen basierend auf den Grunddaten.

    Args:
        mitarbeiter: Dictionary mit Grunddaten

    Returns:
        Erweitertes Dictionary mit berechneten Werten
    """
    # TODO 5: Geburtsjahr berechnen
    aktuelles_jahr = 2025
    mitarbeiter["geburtsjahr"] = aktuelles_jahr - mitarbeiter["alter"]

    # TODO 6: Erfahrungsgrad bestimmen
    alter = mitarbeiter["alter"]
    erfahrung = mitarbeiter.get("berufserfahrung", 0) or 0

    if alter < 25:
        grad = "Nachwuchstalent 🌱"
    elif alter <= 35:
        grad = "Junior Professional 📈" if erfahrung < 5 else "Senior Professional 🎯"
    else:
        grad = "Senior Professional 🎯" if erfahrung <= 10 else "Expert 🏆"

    mitarbeiter["erfahrungsgrad"] = grad

    return mitarbeiter


def formatiere_profil(mitarbeiter: dict) -> None:
    """
    Erstellt eine professionell formatierte Ausgabe des Mitarbeiterprofils.

    Args:
        mitarbeiter: Dictionary mit allen Mitarbeiterdaten
    """
    # TODO 7: Professionelle Ausgabe erstellen
    name = mitarbeiter["name"]

    print("\n" + "=" * 60)
    print(f"📋 MITARBEITERPROFIL: {name.upper()}")
    print("=" * 60)

    # Grunddaten
    print(f"👤 Name:              {mitarbeiter['name']}")
    print(f"🎂 Alter:             {mitarbeiter['alter']} Jahre")
    print(f"📅 Geburtsjahr:       ca. {mitarbeiter['geburtsjahr']}")
    print(f"🏢 Abteilung:         {mitarbeiter['abteilung']}")
    print(f"📊 Erfahrungsgrad:    {mitarbeiter['erfahrungsgrad']}")

    # Berufserfahrung (falls vorhanden)
    if mitarbeiter["berufserfahrung"] is not None:
        print(f"💼 Berufserfahrung:   {mitarbeiter['berufserfahrung']} Jahre")

    print("=" * 60)

    # TODO 8: Personalisierte Nachricht
    abteilung = mitarbeiter["abteilung"]
    if abteilung == "Engineering":
        print("🔧 Willkommen im Engineering-Team!")
    elif abteilung == "Production":
        print("⚙️ Willkommen im Production-Team!")
    elif abteilung == "IT":
        print("💻 Willkommen im IT-Team!")
    else:
        print(f"🎉 Willkommen im {abteilung}-Team!")


def main():
    """
    Hauptfunktion - orchestriert das gesamte Mitarbeiterprofil-System.
    """
    print("🏢 BYSTRONIC MITARBEITERPROFIL-SYSTEM")
    print("=" * 50)
    print("Erstellen Sie Ihr professionelles Mitarbeiterprofil!\n")

    try:
        # Schritt 1: Daten sammeln
        mitarbeiter = sammle_mitarbeiterdaten()

        # Schritt 2: Zusatzinfos berechnen
        mitarbeiter = berechne_zusatzinfos(mitarbeiter)

        # Schritt 3: Profil anzeigen
        formatiere_profil(mitarbeiter)

        print("\n✅ Profil erfolgreich erstellt!")

    except KeyboardInterrupt:
        print("\n\n⚠️ Vorgang abgebrochen.")
    except Exception as e:
        print(f"\n❌ Ein unerwarteter Fehler ist aufgetreten: {e}")


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE:
==================
🏢 BYSTRONIC MITARBEITERPROFIL-SYSTEM
==================================================
Erstellen Sie Ihr professionelles Mitarbeiterprofil!

Vollständiger Name: Anna Müller
Alter: 28
Verfügbare Abteilungen: Engineering, Production, Sales, HR, IT, Finance
Abteilung: Engineering
Jahre Berufserfahrung (Enter für überspringen): 6

============================================================
📋 MITARBEITERPROFIL: ANNA MÜLLER
============================================================
👤 Name:              Anna Müller
🎂 Alter:             28 Jahre
📅 Geburtsjahr:       ca. 1997
🏢 Abteilung:         Engineering
📊 Erfahrungsgrad:    Senior Professional 🎯
💼 Berufserfahrung:   6 Jahre
============================================================
🔧 Willkommen im Engineering-Team!

✅ Profil erfolgreich erstellt!

LERNKONTROLLE:
==============
□ Kann ich Funktionen definieren und verwenden?
□ Verstehe ich Dictionaries?
□ Kann ich Eingaben validieren?
□ Beherrsche ich try/except Fehlerbehandlung?
□ Kann ich Code modular organisieren?
"""
