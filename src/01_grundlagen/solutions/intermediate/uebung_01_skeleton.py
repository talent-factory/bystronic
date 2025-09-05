#!/usr/bin/env python3
"""
🟡 SKELETON: Übung 1 - Mitarbeiterprofil-System (Intermediate)
=============================================================

ANLEITUNG:
Füllen Sie die TODO-Bereiche aus. Das Grundgerüst mit Funktionen ist bereits vorhanden.
Folgen Sie den Kommentaren Schritt für Schritt.

HILFE:
- Verwenden Sie Dictionaries für strukturierte Daten
- Implementieren Sie try/except für Fehlerbehandlung
- Jede Funktion hat einen spezifischen Zweck
"""

def sichere_eingabe(prompt, eingabe_typ="str", min_wert=None, max_wert=None):
    """
    Sichere Eingabefunktion mit Validierung.

    Args:
        prompt: Eingabeaufforderung
        eingabe_typ: "str", "int", "float"
        min_wert: Minimaler Wert (für Zahlen)
        max_wert: Maximaler Wert (für Zahlen)

    Returns:
        Validierte Eingabe
    """
    while True:
        try:
            eingabe = input(prompt).strip()

            if eingabe_typ == "str":
                if not eingabe:
                    print("❌ Eingabe darf nicht leer sein!")
                    continue
                return eingabe

            elif eingabe_typ == "int":
                # TODO: Konvertieren Sie die Eingabe zu int
                wert = # HIER ERGÄNZEN

                # TODO: Prüfen Sie min_wert und max_wert
                if min_wert is not None and wert < min_wert:
                    print(f"❌ Wert muss mindestens {min_wert} sein!")
                    continue
                if max_wert is not None and wert > max_wert:
                    print(f"❌ Wert darf höchstens {max_wert} sein!")
                    continue

                return wert

            elif eingabe_typ == "float":
                # TODO: Implementieren Sie float-Konvertierung
                wert = # HIER ERGÄNZEN
                return wert

        except ValueError:
            print(f"❌ Bitte geben Sie eine gültige {eingabe_typ}-Eingabe ein!")


def sammle_mitarbeiterdaten():
    """
    Sammelt alle Mitarbeiterdaten und gibt Dictionary zurück.

    Returns:
        Dictionary mit Mitarbeiterdaten
    """
    print("👤 MITARBEITERDATEN ERFASSEN")
    print("=" * 35)

    # TODO: Erstellen Sie ein leeres Dictionary
    mitarbeiter = # HIER ERGÄNZEN

    # Grunddaten sammeln
    mitarbeiter["vorname"] = sichere_eingabe("Vorname: ")
    mitarbeiter["nachname"] = sichere_eingabe("Nachname: ")

    # TODO: Sammeln Sie das Alter mit Validierung (18-67 Jahre)
    mitarbeiter["alter"] = sichere_eingabe(
        "Alter: ",
        eingabe_typ="int",
        min_wert=# HIER ERGÄNZEN,
        max_wert=# HIER ERGÄNZEN
    )

    # Abteilung auswählen
    print("\nVerfügbare Abteilungen:")
    abteilungen = ["IT", "HR", "Finanzen", "Produktion", "Marketing", "Vertrieb"]
    for i, abt in enumerate(abteilungen, 1):
        print(f"  {i}. {abt}")

    while True:
        try:
            # TODO: Implementieren Sie Abteilungsauswahl
            auswahl = sichere_eingabe("Abteilung (1-6): ", "int", 1, 6)
            mitarbeiter["abteilung"] = abteilungen[auswahl - 1]
            break
        except (ValueError, IndexError):
            print("❌ Ungültige Auswahl!")

    # TODO: Sammeln Sie weitere Daten
    mitarbeiter["position"] = sichere_eingabe("Position: ")
    mitarbeiter["gehalt"] = sichere_eingabe(
        "Jahresgehalt (CHF): ",
        "float",
        min_wert=# HIER ERGÄNZEN
    )

    # Optionale Daten
    mitarbeiter["email"] = sichere_eingabe("E-Mail (optional): ")
    if not mitarbeiter["email"]:
        # TODO: Generieren Sie automatisch eine E-Mail
        mitarbeiter["email"] = f"# HIER EMAIL GENERIEREN"

    return mitarbeiter


def berechne_zusatzinfos(mitarbeiter):
    """
    Berechnet zusätzliche Informationen basierend auf Mitarbeiterdaten.

    Args:
        mitarbeiter: Dictionary mit Mitarbeiterdaten

    Returns:
        Dictionary mit zusätzlichen Informationen
    """
    zusatz = {}

    # TODO: Berechnen Sie das Monatsgehalt
    zusatz["monatsgehalt"] = # HIER ERGÄNZEN

    # TODO: Bestimmen Sie die Altersgruppe
    alter = mitarbeiter["alter"]
    if alter < 30:
        zusatz["altersgruppe"] = "Jung (< 30)"
    elif alter < 50:
        zusatz["altersgruppe"] = # HIER ERGÄNZEN
    else:
        zusatz["altersgruppe"] = # HIER ERGÄNZEN

    # TODO: Berechnen Sie Jahre bis zur Rente (Rente mit 65)
    zusatz["jahre_bis_rente"] = # HIER ERGÄNZEN

    # Gehaltskategorie bestimmen
    gehalt = mitarbeiter["gehalt"]
    if gehalt < 60000:
        zusatz["gehaltskategorie"] = "Einsteiger"
    elif gehalt < 90000:
        zusatz["gehaltskategorie"] = "Erfahren"
    else:
        zusatz["gehaltskategorie"] = "Senior"

    return zusatz


def zeige_mitarbeiterprofil(mitarbeiter, zusatzinfos):
    """
    Zeigt das vollständige Mitarbeiterprofil an.

    Args:
        mitarbeiter: Dictionary mit Grunddaten
        zusatzinfos: Dictionary mit berechneten Daten
    """
    print("\n" + "=" * 50)
    print("👤 MITARBEITERPROFIL")
    print("=" * 50)

    # TODO: Zeigen Sie die Grunddaten an
    print(f"Name:           {mitarbeiter['vorname']} {mitarbeiter['nachname']}")
    print(f"Alter:          # HIER ERGÄNZEN")
    print(f"Abteilung:      # HIER ERGÄNZEN")
    print(f"Position:       # HIER ERGÄNZEN")
    print(f"E-Mail:         # HIER ERGÄNZEN")

    print(f"\n💰 GEHALTSINFORMATIONEN:")
    print(f"Jahresgehalt:   CHF {mitarbeiter['gehalt']:,.2f}")
    # TODO: Zeigen Sie das Monatsgehalt an
    print(f"Monatsgehalt:   CHF # HIER ERGÄNZEN")
    print(f"Kategorie:      {zusatzinfos['gehaltskategorie']}")

    print(f"\n📊 ZUSÄTZLICHE INFORMATIONEN:")
    # TODO: Zeigen Sie Altersgruppe und Jahre bis Rente an
    print(f"Altersgruppe:   # HIER ERGÄNZEN")
    print(f"Jahre bis Rente: # HIER ERGÄNZEN")

    print("=" * 50)


def main():
    """Hauptfunktion des Mitarbeiterprofil-Systems."""
    print("🏢 BYSTRONIC MITARBEITERPROFIL-SYSTEM")
    print("=" * 45)
    print("Erfassen Sie Mitarbeiterdaten professionell!")

    try:
        # TODO: Rufen Sie die Funktionen in der richtigen Reihenfolge auf
        mitarbeiter = # HIER FUNKTION AUFRUFEN
        zusatzinfos = # HIER FUNKTION AUFRUFEN
        # HIER PROFIL ANZEIGEN

        print("\n✅ Mitarbeiterprofil erfolgreich erstellt!")

    except KeyboardInterrupt:
        print("\n\n⚠️ Programm abgebrochen.")
    except Exception as e:
        print(f"\n❌ Unerwarteter Fehler: {e}")

    print("\n🎉 Vielen Dank für die Nutzung des Systems!")


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE (Beispiel):
=============================
🏢 BYSTRONIC MITARBEITERPROFIL-SYSTEM
=============================================
Erfassen Sie Mitarbeiterdaten professionell!

👤 MITARBEITERDATEN ERFASSEN
===================================
Vorname: Anna
Nachname: Müller
Alter: 28

Verfügbare Abteilungen:
  1. IT
  2. HR
  3. Finanzen
  4. Produktion
  5. Marketing
  6. Vertrieb
Abteilung (1-6): 1
Position: Software-Entwicklerin
Jahresgehalt (CHF): 75000
E-Mail (optional): anna.mueller@bystronic.com

==================================================
👤 MITARBEITERPROFIL
==================================================
Name:           Anna Müller
Alter:          28 Jahre
Abteilung:      IT
Position:       Software-Entwicklerin
E-Mail:         anna.mueller@bystronic.com

💰 GEHALTSINFORMATIONEN:
Jahresgehalt:   CHF 75,000.00
Monatsgehalt:   CHF 6,250.00
Kategorie:      Erfahren

📊 ZUSÄTZLICHE INFORMATIONEN:
Altersgruppe:   Jung (< 30)
Jahre bis Rente: 37
==================================================

✅ Mitarbeiterprofil erfolgreich erstellt!

🎉 Vielen Dank für die Nutzung des Systems!

HILFEN ZUM AUSFÜLLEN:
=====================
□ Dictionary erstellen: {}
□ int() für Zahlenkonvertierung
□ Alter-Validierung: min_wert=18, max_wert=67
□ Monatsgehalt: gehalt / 12
□ Altersgruppe: "Mittel (30-49)" und "Senior (≥ 50)"
□ Jahre bis Rente: 65 - alter
□ E-Mail generieren: f"{vorname.lower()}.{nachname.lower()}@bystronic.com"

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Dieses Grundgerüst (Sie sind hier!)
3. partial.py   - Teilweise implementiert
4. complete.py  - Vollständige Lösung
"""
