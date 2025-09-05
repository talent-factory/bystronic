#!/usr/bin/env python3
"""
🟡 PARTIAL: Übung 1 - Mitarbeiterprofil-System (Intermediate)
============================================================

ANLEITUNG:
Diese Version ist fast vollständig implementiert. Nur wenige Lücken müssen
noch gefüllt werden. Perfekt, wenn Sie fast fertig sind!

HILFE:
- Die meiste Arbeit ist bereits getan
- Nur noch 4-5 kleine Ergänzungen nötig
- Schauen Sie nach den # ERGÄNZEN Kommentaren
"""

def sichere_eingabe(prompt, eingabe_typ="str", min_wert=None, max_wert=None):
    """Sichere Eingabefunktion mit Validierung."""
    while True:
        try:
            eingabe = input(prompt).strip()

            if eingabe_typ == "str":
                if not eingabe:
                    print("❌ Eingabe darf nicht leer sein!")
                    continue
                return eingabe

            elif eingabe_typ == "int":
                wert = int(eingabe)

                if min_wert is not None and wert < min_wert:
                    print(f"❌ Wert muss mindestens {min_wert} sein!")
                    continue
                if max_wert is not None and wert > max_wert:
                    print(f"❌ Wert darf höchstens {max_wert} sein!")
                    continue

                return wert

            elif eingabe_typ == "float":
                wert = float(eingabe)
                if min_wert is not None and wert < min_wert:
                    print(f"❌ Wert muss mindestens {min_wert} sein!")
                    continue
                return wert

        except ValueError:
            print(f"❌ Bitte geben Sie eine gültige {eingabe_typ}-Eingabe ein!")


def sammle_mitarbeiterdaten():
    """Sammelt alle Mitarbeiterdaten und gibt Dictionary zurück."""
    print("👤 MITARBEITERDATEN ERFASSEN")
    print("=" * 35)

    mitarbeiter = {}

    # Grunddaten sammeln
    mitarbeiter["vorname"] = sichere_eingabe("Vorname: ")
    mitarbeiter["nachname"] = sichere_eingabe("Nachname: ")
    mitarbeiter["alter"] = sichere_eingabe("Alter: ", "int", 18, 67)

    # Abteilung auswählen
    print("\nVerfügbare Abteilungen:")
    abteilungen = ["IT", "HR", "Finanzen", "Produktion", "Marketing", "Vertrieb"]
    for i, abt in enumerate(abteilungen, 1):
        print(f"  {i}. {abt}")

    auswahl = sichere_eingabe("Abteilung (1-6): ", "int", 1, 6)
    mitarbeiter["abteilung"] = abteilungen[auswahl - 1]

    # Weitere Daten
    mitarbeiter["position"] = sichere_eingabe("Position: ")
    mitarbeiter["gehalt"] = sichere_eingabe("Jahresgehalt (CHF): ", "float", 30000)

    # E-Mail behandeln
    email_eingabe = input("E-Mail (optional): ").strip()
    if email_eingabe:
        mitarbeiter["email"] = email_eingabe
    else:
        # TODO: Generieren Sie automatisch eine E-Mail
        vorname = mitarbeiter["vorname"].lower()
        nachname = mitarbeiter["nachname"].lower()
        mitarbeiter["email"] = f"# ERGÄNZEN: {vorname}.{nachname}@bystronic.com"

    return mitarbeiter


def berechne_zusatzinfos(mitarbeiter):
    """Berechnet zusätzliche Informationen basierend auf Mitarbeiterdaten."""
    zusatz = {}

    # Monatsgehalt berechnen
    zusatz["monatsgehalt"] = mitarbeiter["gehalt"] / 12

    # Altersgruppe bestimmen
    alter = mitarbeiter["alter"]
    if alter < 30:
        zusatz["altersgruppe"] = "Jung (< 30)"
    elif alter < 50:
        zusatz["altersgruppe"] = "Mittel (30-49)"
    else:
        zusatz["altersgruppe"] = "Senior (≥ 50)"

    # TODO: Berechnen Sie Jahre bis zur Rente (Rente mit 65)
    zusatz["jahre_bis_rente"] = # ERGÄNZEN

    # Gehaltskategorie bestimmen
    gehalt = mitarbeiter["gehalt"]
    if gehalt < 60000:
        zusatz["gehaltskategorie"] = "Einsteiger"
    elif gehalt < 90000:
        zusatz["gehaltskategorie"] = "Erfahren"
    else:
        zusatz["gehaltskategorie"] = "Senior"

    # TODO: Berechnen Sie das Netto-Monatsgehalt (ca. 80% vom Brutto)
    zusatz["netto_monatsgehalt"] = # ERGÄNZEN

    return zusatz


def zeige_mitarbeiterprofil(mitarbeiter, zusatzinfos):
    """Zeigt das vollständige Mitarbeiterprofil an."""
    print("\n" + "=" * 50)
    print("👤 MITARBEITERPROFIL")
    print("=" * 50)

    # Grunddaten
    print(f"Name:           {mitarbeiter['vorname']} {mitarbeiter['nachname']}")
    print(f"Alter:          {mitarbeiter['alter']} Jahre")
    print(f"Abteilung:      {mitarbeiter['abteilung']}")
    print(f"Position:       {mitarbeiter['position']}")
    print(f"E-Mail:         {mitarbeiter['email']}")

    print(f"\n💰 GEHALTSINFORMATIONEN:")
    print(f"Jahresgehalt:   CHF {mitarbeiter['gehalt']:,.2f}")
    print(f"Monatsgehalt:   CHF {zusatzinfos['monatsgehalt']:,.2f}")
    # TODO: Zeigen Sie das Netto-Monatsgehalt an
    print(f"Netto (ca.):    CHF # ERGÄNZEN")
    print(f"Kategorie:      {zusatzinfos['gehaltskategorie']}")

    print(f"\n📊 ZUSÄTZLICHE INFORMATIONEN:")
    print(f"Altersgruppe:   {zusatzinfos['altersgruppe']}")
    print(f"Jahre bis Rente: {zusatzinfos['jahre_bis_rente']}")

    # Zusätzliche Bewertungen
    if zusatzinfos["jahre_bis_rente"] > 30:
        print("💡 Tipp: Früh mit der Altersvorsorge beginnen!")
    elif zusatzinfos["jahre_bis_rente"] < 10:
        print("⏰ Hinweis: Rente rückt näher - Planung wichtig!")

    print("=" * 50)


def main():
    """Hauptfunktion des Mitarbeiterprofil-Systems."""
    print("🏢 BYSTRONIC MITARBEITERPROFIL-SYSTEM")
    print("=" * 45)
    print("Erfassen Sie Mitarbeiterdaten professionell!")

    try:
        mitarbeiter = sammle_mitarbeiterdaten()
        zusatzinfos = berechne_zusatzinfos(mitarbeiter)
        zeige_mitarbeiterprofil(mitarbeiter, zusatzinfos)

        print("\n✅ Mitarbeiterprofil erfolgreich erstellt!")

        # TODO: Fragen Sie, ob ein weiterer Mitarbeiter erfasst werden soll
        weitere = input("\nWeiteren Mitarbeiter erfassen? (j/n): ").strip().lower()
        if weitere == "j":
            print("# ERGÄNZEN: Rekursiver Aufruf oder Schleife")

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
Vorname: Max
Nachname: Mustermann
Alter: 35

Verfügbare Abteilungen:
  1. IT
  2. HR
  3. Finanzen
  4. Produktion
  5. Marketing
  6. Vertrieb
Abteilung (1-6): 4
Position: Produktionsleiter
Jahresgehalt (CHF): 85000
E-Mail (optional):

==================================================
👤 MITARBEITERPROFIL
==================================================
Name:           Max Mustermann
Alter:          35 Jahre
Abteilung:      Produktion
Position:       Produktionsleiter
E-Mail:         max.mustermann@bystronic.com

💰 GEHALTSINFORMATIONEN:
Jahresgehalt:   CHF 85,000.00
Monatsgehalt:   CHF 7,083.33
Netto (ca.):    CHF 5,666.67
Kategorie:      Erfahren

📊 ZUSÄTZLICHE INFORMATIONEN:
Altersgruppe:   Mittel (30-49)
Jahre bis Rente: 30
💡 Tipp: Früh mit der Altersvorsorge beginnen!
==================================================

✅ Mitarbeiterprofil erfolgreich erstellt!

Weiteren Mitarbeiter erfassen? (j/n): n

🎉 Vielen Dank für die Nutzung des Systems!

WAS FEHLT NOCH:
===============
□ E-Mail automatisch generieren
□ Jahre bis Rente berechnen (65 - alter)
□ Netto-Monatsgehalt berechnen (monatsgehalt * 0.8)
□ Netto-Gehalt anzeigen
□ Weiteren Mitarbeiter-Logik implementieren

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Code-Grundgerüst
3. partial.py   - Teilweise implementiert (Sie sind hier!)
4. complete.py  - Vollständige Lösung
"""
