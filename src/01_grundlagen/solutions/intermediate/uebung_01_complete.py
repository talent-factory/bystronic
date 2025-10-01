#!/usr/bin/env python3
"""
🟡 COMPLETE: Übung 1 - Mitarbeiterprofil-System (Intermediate)
=============================================================

MUSTERLÖSUNG:
Dies ist eine vollständige, professionelle Lösung der Übung.
Verwenden Sie diese nur, wenn Sie wirklich nicht weiterkommen!

LERNZIELE ERFÜLLT:
✅ Funktionen definieren und verwenden
✅ Dictionaries für strukturierte Daten
✅ try/except für robuste Fehlerbehandlung
✅ Eingabevalidierung implementieren
✅ Modulare Programmierung anwenden
"""

import re
from datetime import datetime


def sichere_eingabe(
    prompt, eingabe_typ="str", min_wert=None, max_wert=None, regex_pattern=None
):
    """
    Sichere Eingabefunktion mit umfassender Validierung.

    Args:
        prompt: Eingabeaufforderung
        eingabe_typ: "str", "int", "float", "email"
        min_wert: Minimaler Wert (für Zahlen) oder minimale Länge (für Strings)
        max_wert: Maximaler Wert (für Zahlen) oder maximale Länge (für Strings)
        regex_pattern: Regulärer Ausdruck für Validierung

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
                if min_wert and len(eingabe) < min_wert:
                    print(f"❌ Eingabe muss mindestens {min_wert} Zeichen haben!")
                    continue
                if max_wert and len(eingabe) > max_wert:
                    print(f"❌ Eingabe darf höchstens {max_wert} Zeichen haben!")
                    continue
                if regex_pattern and not re.match(regex_pattern, eingabe):
                    print("❌ Eingabe entspricht nicht dem erwarteten Format!")
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
                if max_wert is not None and wert > max_wert:
                    print(f"❌ Wert darf höchstens {max_wert} sein!")
                    continue
                return wert

            elif eingabe_typ == "email":
                if not eingabe:
                    return ""  # Leere E-Mail erlaubt
                email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
                if re.match(email_pattern, eingabe):
                    return eingabe
                else:
                    print("❌ Bitte geben Sie eine gültige E-Mail-Adresse ein!")
                    continue

        except ValueError:
            print(f"❌ Bitte geben Sie eine gültige {eingabe_typ}-Eingabe ein!")


def sammle_mitarbeiterdaten():
    """
    Sammelt alle Mitarbeiterdaten und gibt Dictionary zurück.

    Returns:
        Dictionary mit vollständigen Mitarbeiterdaten
    """
    print("👤 MITARBEITERDATEN ERFASSEN")
    print("=" * 35)

    mitarbeiter = {}

    # Grunddaten sammeln
    mitarbeiter["vorname"] = sichere_eingabe(
        "Vorname: ",
        "str",
        min_wert=2,
        max_wert=50,
        regex_pattern=r"^[a-zA-ZäöüÄÖÜß\s-]+$",
    )

    mitarbeiter["nachname"] = sichere_eingabe(
        "Nachname: ",
        "str",
        min_wert=2,
        max_wert=50,
        regex_pattern=r"^[a-zA-ZäöüÄÖÜß\s-]+$",
    )

    mitarbeiter["alter"] = sichere_eingabe("Alter: ", "int", min_wert=18, max_wert=67)

    # Abteilung auswählen
    print("\nVerfügbare Abteilungen:")
    abteilungen = [
        "IT",
        "HR",
        "Finanzen",
        "Produktion",
        "Marketing",
        "Vertrieb",
        "Qualität",
        "Einkauf",
    ]
    for i, abt in enumerate(abteilungen, 1):
        print(f"  {i}. {abt}")

    auswahl = sichere_eingabe(
        f"Abteilung (1-{len(abteilungen)}): ", "int", 1, len(abteilungen)
    )
    mitarbeiter["abteilung"] = abteilungen[auswahl - 1]

    # Position und Gehalt
    mitarbeiter["position"] = sichere_eingabe(
        "Position: ", "str", min_wert=2, max_wert=100
    )
    mitarbeiter["gehalt"] = sichere_eingabe(
        "Jahresgehalt (CHF): ", "float", min_wert=30000, max_wert=500000
    )

    # E-Mail behandeln
    email_eingabe = sichere_eingabe("E-Mail (optional): ", "email")
    if email_eingabe:
        mitarbeiter["email"] = email_eingabe
    else:
        # Automatische E-Mail-Generierung
        vorname_clean = re.sub(r"[^a-zA-Z]", "", mitarbeiter["vorname"].lower())
        nachname_clean = re.sub(r"[^a-zA-Z]", "", mitarbeiter["nachname"].lower())
        mitarbeiter["email"] = f"{vorname_clean}.{nachname_clean}@smartfactory.com"
        print(f"📧 Automatisch generierte E-Mail: {mitarbeiter['email']}")

    # Zusätzliche optionale Daten
    mitarbeiter["telefon"] = sichere_eingabe("Telefon (optional): ")
    mitarbeiter["startdatum"] = sichere_eingabe("Startdatum (YYYY-MM-DD, optional): ")

    # Erfassungsdatum hinzufügen
    mitarbeiter["erfasst_am"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return mitarbeiter


def berechne_zusatzinfos(mitarbeiter):
    """
    Berechnet zusätzliche Informationen basierend auf Mitarbeiterdaten.

    Args:
        mitarbeiter: Dictionary mit Mitarbeiterdaten

    Returns:
        Dictionary mit zusätzlichen berechneten Informationen
    """
    zusatz = {}

    # Gehaltsberechnungen
    zusatz["monatsgehalt"] = mitarbeiter["gehalt"] / 12
    zusatz["netto_monatsgehalt"] = zusatz["monatsgehalt"] * 0.8  # Grobe Schätzung
    zusatz["wochengehalt"] = mitarbeiter["gehalt"] / 52
    zusatz["tageslohn"] = mitarbeiter["gehalt"] / 250  # 250 Arbeitstage pro Jahr

    # Altersgruppe bestimmen
    alter = mitarbeiter["alter"]
    if alter < 25:
        zusatz["altersgruppe"] = "Sehr jung (< 25)"
    elif alter < 35:
        zusatz["altersgruppe"] = "Jung (25-34)"
    elif alter < 45:
        zusatz["altersgruppe"] = "Mittel (35-44)"
    elif alter < 55:
        zusatz["altersgruppe"] = "Erfahren (45-54)"
    else:
        zusatz["altersgruppe"] = "Senior (≥ 55)"

    # Renten- und Karriereberechnungen
    zusatz["jahre_bis_rente"] = max(0, 65 - alter)
    zusatz["monate_bis_rente"] = zusatz["jahre_bis_rente"] * 12

    # Gehaltskategorie nach Schweizer Standards
    gehalt = mitarbeiter["gehalt"]
    if gehalt < 50000:
        zusatz["gehaltskategorie"] = "Einsteiger"
        zusatz["gehalt_percentil"] = "Unteres Quartil"
    elif gehalt < 70000:
        zusatz["gehaltskategorie"] = "Junior"
        zusatz["gehalt_percentil"] = "Unter Durchschnitt"
    elif gehalt < 90000:
        zusatz["gehaltskategorie"] = "Erfahren"
        zusatz["gehalt_percentil"] = "Durchschnitt"
    elif gehalt < 120000:
        zusatz["gehaltskategorie"] = "Senior"
        zusatz["gehalt_percentil"] = "Über Durchschnitt"
    else:
        zusatz["gehaltskategorie"] = "Führungskraft"
        zusatz["gehalt_percentil"] = "Oberes Quartil"

    # Abteilungsspezifische Informationen
    abteilung = mitarbeiter["abteilung"]
    abteilungs_info = {
        "IT": {"durchschnittsgehalt": 85000, "wachstum": "Hoch"},
        "HR": {"durchschnittsgehalt": 70000, "wachstum": "Mittel"},
        "Finanzen": {"durchschnittsgehalt": 80000, "wachstum": "Stabil"},
        "Produktion": {"durchschnittsgehalt": 65000, "wachstum": "Mittel"},
        "Marketing": {"durchschnittsgehalt": 75000, "wachstum": "Hoch"},
        "Vertrieb": {"durchschnittsgehalt": 78000, "wachstum": "Hoch"},
        "Qualität": {"durchschnittsgehalt": 72000, "wachstum": "Stabil"},
        "Einkauf": {"durchschnittsgehalt": 68000, "wachstum": "Mittel"},
    }

    if abteilung in abteilungs_info:
        info = abteilungs_info[abteilung]
        zusatz["abteilung_durchschnittsgehalt"] = info["durchschnittsgehalt"]
        zusatz["abteilung_wachstum"] = info["wachstum"]
        zusatz["gehalt_vs_abteilung"] = gehalt - info["durchschnittsgehalt"]

    # Arbeitszeit bis Rente
    if zusatz["jahre_bis_rente"] > 0:
        zusatz["arbeitsstunden_bis_rente"] = (
            zusatz["jahre_bis_rente"] * 2000
        )  # 2000h pro Jahr
        zusatz["arbeitstage_bis_rente"] = zusatz["jahre_bis_rente"] * 250

    return zusatz


def zeige_mitarbeiterprofil(mitarbeiter, zusatzinfos):
    """
    Zeigt das vollständige Mitarbeiterprofil mit allen Informationen an.

    Args:
        mitarbeiter: Dictionary mit Grunddaten
        zusatzinfos: Dictionary mit berechneten Daten
    """
    print("\n" + "=" * 60)
    print("👤 VOLLSTÄNDIGES MITARBEITERPROFIL")
    print("=" * 60)

    # Grunddaten
    print("📋 PERSÖNLICHE DATEN:")
    print(f"Name:           {mitarbeiter['vorname']} {mitarbeiter['nachname']}")
    print(
        f"Alter:          {mitarbeiter['alter']} Jahre ({zusatzinfos['altersgruppe']})"
    )
    print(f"E-Mail:         {mitarbeiter['email']}")
    if mitarbeiter.get("telefon"):
        print(f"Telefon:        {mitarbeiter['telefon']}")

    # Berufliche Daten
    print("\n🏢 BERUFLICHE DATEN:")
    print(f"Abteilung:      {mitarbeiter['abteilung']}")
    print(f"Position:       {mitarbeiter['position']}")
    if mitarbeiter.get("startdatum"):
        print(f"Startdatum:     {mitarbeiter['startdatum']}")
    print(f"Erfasst am:     {mitarbeiter['erfasst_am']}")

    # Detaillierte Gehaltsinformationen
    print("\n💰 GEHALTSINFORMATIONEN:")
    print(f"Jahresgehalt:   CHF {mitarbeiter['gehalt']:,.2f}")
    print(f"Monatsgehalt:   CHF {zusatzinfos['monatsgehalt']:,.2f}")
    print(f"Netto (ca.):    CHF {zusatzinfos['netto_monatsgehalt']:,.2f}")
    print(f"Wochengehalt:   CHF {zusatzinfos['wochengehalt']:,.2f}")
    print(f"Tageslohn:      CHF {zusatzinfos['tageslohn']:,.2f}")
    print(
        f"Kategorie:      {zusatzinfos['gehaltskategorie']} ({zusatzinfos['gehalt_percentil']})"
    )

    # Abteilungsvergleich
    if "abteilung_durchschnittsgehalt" in zusatzinfos:
        print("\n📊 ABTEILUNGSVERGLEICH:")
        print(
            f"Abteilungs-Ø:   CHF {zusatzinfos['abteilung_durchschnittsgehalt']:,.2f}"
        )
        diff = zusatzinfos["gehalt_vs_abteilung"]
        if diff > 0:
            print(f"Differenz:      +CHF {diff:,.2f} (über Durchschnitt) ✅")
        elif diff < 0:
            print(f"Differenz:      CHF {diff:,.2f} (unter Durchschnitt) ⚠️")
        else:
            print("Differenz:      CHF 0 (genau Durchschnitt) ➖")
        print(f"Wachstumstrend: {zusatzinfos['abteilung_wachstum']}")

    # Renten- und Karriereinformationen
    print("\n⏰ RENTEN- UND KARRIEREPLANUNG:")
    if zusatzinfos["jahre_bis_rente"] > 0:
        print(
            f"Jahre bis Rente: {zusatzinfos['jahre_bis_rente']} Jahre ({zusatzinfos['monate_bis_rente']} Monate)"
        )
        print(f"Arbeitstage:     {zusatzinfos['arbeitstage_bis_rente']:,} Tage")
        print(f"Arbeitsstunden:  {zusatzinfos['arbeitsstunden_bis_rente']:,} Stunden")

        # Rentenbeiträge schätzen (grob)
        lebenseinkommen = mitarbeiter["gehalt"] * zusatzinfos["jahre_bis_rente"]
        print(f"Geschätztes Lebenseinkommen: CHF {lebenseinkommen:,.2f}")

        # Empfehlungen basierend auf Alter
        if zusatzinfos["jahre_bis_rente"] > 30:
            print("💡 Empfehlung: Früh mit Säule 3a und Altersvorsorge beginnen!")
        elif zusatzinfos["jahre_bis_rente"] > 15:
            print("💡 Empfehlung: Altersvorsorge optimieren und Weiterbildung planen!")
        elif zusatzinfos["jahre_bis_rente"] > 5:
            print("💡 Empfehlung: Pensionierung konkret planen!")
        else:
            print("💡 Empfehlung: Pensionierung steht bevor - finale Vorbereitungen!")
    else:
        print("🎉 Bereits im Rentenalter!")

    # Zusätzliche Bewertungen und Tipps
    print("\n🎯 BEWERTUNG UND EMPFEHLUNGEN:")

    # Gehaltsbewertung
    if zusatzinfos["gehaltskategorie"] in ["Einsteiger", "Junior"]:
        print(
            "📈 Karrieretipp: Weiterbildung und Zertifizierungen für Gehaltserhöhung!"
        )
    elif zusatzinfos["gehaltskategorie"] in ["Senior", "Führungskraft"]:
        print("🌟 Gratulation: Sie befinden sich in einer sehr guten Gehaltsklasse!")

    # Altersbewertung
    if mitarbeiter["alter"] < 30:
        print("🚀 Karrieretipp: Nutzen Sie die Zeit für Weiterbildung und Netzwerken!")
    elif mitarbeiter["alter"] < 50:
        print(
            "💼 Karrieretipp: Optimale Zeit für Führungsverantwortung und Spezialisierung!"
        )
    else:
        print("🎓 Karrieretipp: Mentoring und Wissenstransfer an jüngere Kollegen!")

    print("=" * 60)


def exportiere_profil(mitarbeiter, zusatzinfos, dateiname=None):
    """
    Exportiert das Mitarbeiterprofil in eine Textdatei.

    Args:
        mitarbeiter: Dictionary mit Grunddaten
        zusatzinfos: Dictionary mit berechneten Daten
        dateiname: Optionaler Dateiname
    """
    if not dateiname:
        name_clean = f"{mitarbeiter['vorname']}_{mitarbeiter['nachname']}".replace(
            " ", "_"
        )
        dateiname = f"mitarbeiterprofil_{name_clean}.txt"

    try:
        with open(dateiname, "w", encoding="utf-8") as f:
            f.write("BYSTRONIC MITARBEITERPROFIL\n")
            f.write("=" * 30 + "\n\n")
            f.write(f"Name: {mitarbeiter['vorname']} {mitarbeiter['nachname']}\n")
            f.write(f"Alter: {mitarbeiter['alter']} Jahre\n")
            f.write(f"Abteilung: {mitarbeiter['abteilung']}\n")
            f.write(f"Position: {mitarbeiter['position']}\n")
            f.write(f"Jahresgehalt: CHF {mitarbeiter['gehalt']:,.2f}\n")
            f.write(f"Monatsgehalt: CHF {zusatzinfos['monatsgehalt']:,.2f}\n")
            f.write(f"Jahre bis Rente: {zusatzinfos['jahre_bis_rente']}\n")
            f.write(f"Erfasst am: {mitarbeiter['erfasst_am']}\n")

        print(f"📄 Profil exportiert nach: {dateiname}")

    except Exception as e:
        print(f"❌ Fehler beim Export: {e}")


def main():
    """Hauptfunktion des erweiterten Mitarbeiterprofil-Systems."""
    print("🏢 BYSTRONIC MITARBEITERPROFIL-SYSTEM")
    print("=" * 45)
    print("Professionelles HR-Management-Tool")
    print("Erfassen Sie Mitarbeiterdaten umfassend und sicher!")

    mitarbeiter_liste = []

    try:
        while True:
            # Mitarbeiterdaten sammeln
            mitarbeiter = sammle_mitarbeiterdaten()
            zusatzinfos = berechne_zusatzinfos(mitarbeiter)

            # Profil anzeigen
            zeige_mitarbeiterprofil(mitarbeiter, zusatzinfos)

            # Zur Liste hinzufügen
            mitarbeiter_liste.append((mitarbeiter, zusatzinfos))

            print("\n✅ Mitarbeiterprofil erfolgreich erstellt!")

            # Export anbieten
            export_wunsch = (
                input("Profil als Datei exportieren? (j/n): ").strip().lower()
            )
            if export_wunsch == "j":
                exportiere_profil(mitarbeiter, zusatzinfos)

            # Weiteren Mitarbeiter erfassen?
            weitere = input("\nWeiteren Mitarbeiter erfassen? (j/n): ").strip().lower()
            if weitere != "j":
                break

        # Zusammenfassung aller erfassten Mitarbeiter
        if len(mitarbeiter_liste) > 1:
            print(
                f"\n📊 ZUSAMMENFASSUNG - {len(mitarbeiter_liste)} MITARBEITER ERFASST:"
            )
            print("-" * 50)

            gesamtgehalt = sum(m[0]["gehalt"] for m in mitarbeiter_liste)
            durchschnittsalter = sum(m[0]["alter"] for m in mitarbeiter_liste) / len(
                mitarbeiter_liste
            )

            print(f"Gesamte Lohnsumme: CHF {gesamtgehalt:,.2f}")
            print(f"Durchschnittsalter: {durchschnittsalter:.1f} Jahre")
            print(
                f"Durchschnittsgehalt: CHF {gesamtgehalt / len(mitarbeiter_liste):,.2f}"
            )

            # Abteilungsverteilung
            abteilungen = {}
            for m, _ in mitarbeiter_liste:
                abt = m["abteilung"]
                abteilungen[abt] = abteilungen.get(abt, 0) + 1

            print("\nAbteilungsverteilung:")
            for abt, anzahl in sorted(abteilungen.items()):
                print(f"  {abt}: {anzahl} Mitarbeiter")

    except KeyboardInterrupt:
        print("\n\n⚠️ Programm abgebrochen.")
    except Exception as e:
        print(f"\n❌ Unerwarteter Fehler: {e}")
        import traceback

        traceback.print_exc()

    print("\n🎉 Vielen Dank für die Nutzung des Mitarbeiterprofil-Systems!")
    print(f"Insgesamt {len(mitarbeiter_liste)} Mitarbeiter erfasst.")


if __name__ == "__main__":
    main()

"""
VERWENDETE KONZEPTE:
====================
✅ Funktionen definieren und verwenden
✅ Dictionaries für strukturierte Daten
✅ try/except für robuste Fehlerbehandlung
✅ Eingabevalidierung mit regulären Ausdrücken
✅ Modulare Programmierung
✅ Datei-Export
✅ Umfassende Berechnungen
✅ Benutzerfreundliche Ausgaben
✅ Mehrere Mitarbeiter verwalten
✅ Statistische Auswertungen

NÄCHSTE SCHRITTE:
=================
🎯 Verstehen Sie alle Konzepte? Probieren Sie Übung 2!
🚀 Zu einfach? Versuchen Sie die Advanced-Version!
💡 Eigene Ideen? Erweitern Sie das System mit JSON-Speicherung!
"""
