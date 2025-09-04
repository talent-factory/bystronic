#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Übung 2: String-Verarbeitung

Diese Übung behandelt:
- String-Erstellung und -Manipulation
- String-Formatierung (f-Strings, .format(), %)
- String-Validierung und -Prüfung
- Praktische Anwendungen für Dateipfade und Berichte
"""

import datetime
import re


def aufgabe_1_string_grundlagen():
    """Aufgabe 1: String-Grundlagen"""
    print("AUFGABE 1: String-Grundlagen")
    print("-" * 40)

    # Gegeben:
    firma = "bystronic ag"
    maschine = "  BYSTAR FIBER 6KW  "
    beschreibung = "Hochpräzise\nLaserschneid-\nanlage"

    print(f"Firma (original): '{firma}'")
    print(f"Maschine (original): '{maschine}'")
    print(f"Beschreibung (original): '{beschreibung}'")

    # TODO: Formatieren Sie die Strings:
    # 1. firma: Erster Buchstabe gross, Rest klein
    # 2. maschine: Leerzeichen entfernen, Titel-Format
    # 3. beschreibung: Zeilenumbrüche durch Leerzeichen ersetzen

    # Ihre Lösung hier:
    # firma_formatiert = ...
    # maschine_formatiert = ...
    # beschreibung_formatiert = ...

    # TODO: Ausgabe der formatierten Strings

    # TODO: String-Eigenschaften analysieren:
    teilenummer = "BSF-6000-2024-001"
    print(f"\nTeilnummer: {teilenummer}")

    # Analysieren Sie:
    # - Länge des Strings
    # - Erstes und letztes Zeichen
    # - Mittlerer Teil (Position 4 bis 8)
    # - Aufteilen bei '-'
    # - Ersetzen von '2024' durch '2025'

    # Ihre Lösung hier:

    print("✅ Aufgabe 1 abgeschlossen!\n")


def aufgabe_2_string_formatierung():
    """Aufgabe 2: String-Formatierung"""
    print("AUFGABE 2: String-Formatierung")
    print("-" * 40)

    # Gegeben: Produktionsdaten
    datetime.date.today()

    # TODO: Erstellen Sie einen Produktionsbericht mit verschiedenen Formatierungsmethoden:

    # 1. Mit f-Strings (modern, empfohlen):
    # Erstellen Sie einen formatierten Bericht mit:
    # - Datum im Format "15.03.2024"
    # - Effizienz als Prozent (1 Dezimalstelle)
    # - Kosten formatiert mit 2 Dezimalstellen und Euro-Symbol
    # - Teile mit Tausender-Trennzeichen

    print("1. f-String Formatierung:")
    # Ihre Lösung hier:
    # bericht_f = f"""..."""
    # print(bericht_f)

    # 2. Mit .format() Methode:
    print("\n2. .format() Methode:")
    # Ihre Lösung hier:
    # bericht_format = """...""".format(...)
    # print(bericht_format)

    # 3. Mit % Formatierung (alt, aber manchmal noch verwendet):
    print("\n3. % Formatierung:")
    # Ihre Lösung hier:
    # bericht_prozent = """...""" % (...)
    # print(bericht_prozent)

    # TODO: Erweiterte Formatierung
    # Erstellen Sie eine Tabelle mit rechtsbündigen Zahlen:
    # Spalten: Tag, Soll, Ist, Effizienz%, Kosten€

    print("\n4. Tabellenformatierung:")
    print("-" * 50)
    # TODO: Implementieren Sie die Tabelle mit formatierter Ausgabe

    print("✅ Aufgabe 2 abgeschlossen!\n")


def aufgabe_3_string_validierung():
    """Aufgabe 3: String-Validierung"""
    print("AUFGABE 3: String-Validierung")
    print("-" * 40)

    # TODO: Implementieren Sie Validierungsfunktionen für:

    def ist_gueltige_teilenummer(nummer):
        """
        Prüft Teilenummer im Format: BSF-XXXX-XXXX-XXX
        BSF = Prefix, XXXX = 4 Ziffern, XXX = 3 Ziffern
        """
        # Ihre Lösung hier:
        # Verwenden Sie reguläre Ausdrücke (re.match)
        pass

    def ist_gueltige_email(email):
        """
        Prüft E-Mail Format (einfache Validierung)
        Muss @ und . nach @ enthalten
        """
        # Ihre Lösung hier:
        pass

    def ist_gueltige_maschinennummer(nummer):
        """
        Prüft Maschinennummer im Format: [TYPE]_[NNN]
        TYPE = LASER|PRESSE|STANZE|CNC (3-6 Buchstaben)
        NNN = 3 Ziffern
        """
        # Ihre Lösung hier:
        pass

    # Testdaten
    test_teilenummern = [
        "BSF-6000-2024-001",  # OK
        "BSF-6000-2024-1",  # NOK (zu kurz)
        "BSF-60000-2024-001",  # NOK (zu lang)
        "ABC-6000-2024-001",  # NOK (falscher Prefix)
        "BSF-6000-202A-001",  # NOK (Buchstabe statt Zahl)
        "",  # NOK (leer)
    ]

    test_emails = [
        "max.mustermann@bystronic.com",  # OK
        "anna@bystronic.ch",  # OK
        "invalid.email",  # NOK
        "@bystronic.com",  # NOK
        "test@",  # NOK
        "",  # NOK
    ]

    test_maschinen = [
        "LASER_001",  # OK
        "PRESSE_142",  # OK
        "CNC_099",  # OK
        "STANZE_555",  # OK
        "PLASMA_12",  # NOK (zu kurz)
        "LASER_1234",  # NOK (zu lang)
        "UNKNOWN_001",  # NOK (unbekannter Typ)
        "",  # NOK (leer)
    ]

    # TODO: Testen Sie Ihre Validierungsfunktionen
    print("Teilenummern-Validierung:")
    for _nummer in test_teilenummern:
        # gueltig = ist_gueltige_teilenummer(nummer)
        # status = "✅ Gültig" if gueltig else "❌ Ungültig"
        # print(f"  '{nummer}': {status}")
        pass

    print("\nE-Mail Validierung:")
    for _email in test_emails:
        # gueltig = ist_gueltige_email(email)
        # status = "✅ Gültig" if gueltig else "❌ Ungültig"
        # print(f"  '{email}': {status}")
        pass

    print("\nMaschinennummern-Validierung:")
    for _maschine in test_maschinen:
        # gueltig = ist_gueltige_maschinennummer(maschine)
        # status = "✅ Gültig" if gueltig else "❌ Ungültig"
        # print(f"  '{maschine}': {status}")
        pass

    print("✅ Aufgabe 3 abgeschlossen!\n")


def aufgabe_4_dateinamen_verwaltung():
    """Aufgabe 4: Dateinamen und Pfade"""
    print("AUFGABE 4: Dateinamen und Pfade")
    print("-" * 40)

    # TODO: Erstellen Sie Funktionen für die Dateinamen-Generierung:

    def generiere_produktionsdatei(maschine, datum, schicht):
        """
        Generiert Dateinamen im Format:
        Produktion_[MASCHINE]_[YYYYMMDD]_[SCHICHT].csv
        Schicht: T=Tag, N=Nacht, S=Spät
        """
        # Ihre Lösung hier:
        pass

    def generiere_backup_pfad(basis_pfad, datum):
        """
        Generiert Backup-Pfad im Format:
        [BASIS_PFAD]/Backup/[YYYY]/[MM]/[YYYY-MM-DD]/
        """
        # Ihre Lösung hier:
        pass

    def parse_log_datei(dateiname):
        """
        Extrahiert Informationen aus Log-Dateinamen:
        Format: LOG_[MASCHINE]_[YYYYMMDD]_[HHMMSS].log
        Return: Dictionary mit maschine, datum, zeit
        """
        # Ihre Lösung hier:
        pass

    # TODO: Testen Sie Ihre Funktionen
    heute = datetime.date.today()

    print("Dateinamen-Generierung:")
    maschinen = ["LASER_001", "PRESSE_142", "CNC_099"]
    schichten = [("T", "Tag"), ("N", "Nacht"), ("S", "Spät")]

    for _maschine in maschinen:
        for _schicht_code, _schicht_name in schichten:
            # dateiname = generiere_produktionsdatei(maschine, heute, schicht_code)
            # print(f"  {maschine} - {schicht_name}: {dateiname}")
            pass

    print(f"\nBackup-Pfade für {heute}:")
    basis_pfade = ["/data", "C:\\Bystronic\\Data", "\\\\server\\produktionsdaten"]

    for _pfad in basis_pfade:
        # backup_pfad = generiere_backup_pfad(pfad, heute)
        # print(f"  {pfad} -> {backup_pfad}")
        pass

    print("\nLog-Datei Parsing:")
    log_dateien = [
        "LOG_LASER_001_20240315_143022.log",
        "LOG_PRESSE_142_20240315_090515.log",
        "LOG_CNC_099_20240314_235959.log",
        "INVALID_LOG_FILE.log",
    ]

    for _log_datei in log_dateien:
        # info = parse_log_datei(log_datei)
        # if info:
        #     print(f"  {log_datei}: Maschine={info['maschine']}, Datum={info['datum']}, Zeit={info['zeit']}")
        # else:
        #     print(f"  {log_datei}: ❌ Ungültiges Format")
        pass

    print("✅ Aufgabe 4 abgeschlossen!\n")


def aufgabe_5_bericht_generierung():
    """Aufgabe 5: Automatische Bericht-Generierung"""
    print("AUFGABE 5: Bericht-Generierung")
    print("-" * 40)

    # Gegeben: Produktionsdaten der letzten Woche

    # TODO: Implementieren Sie Funktionen zur Bericht-Generierung:

    def erstelle_tageszeile(tag, daten):
        """
        Erstellt eine formatierte Zeile für den Tagesbericht
        Format: Tag | Teile | Laufzeit | Ausschuss | Effizienz
        """
        # Ihre Lösung hier:
        pass

    def berechne_wochensumme(tage_daten):
        """
        Berechnet Wochensummen aus Tagesdaten
        Return: Dictionary mit gesamt_teile, gesamt_laufzeit, gesamt_ausschuss
        """
        # Ihre Lösung hier:
        pass

    def erstelle_maschinenbericht(maschinen_id, maschinen_daten):
        """
        Erstellt vollständigen Bericht für eine Maschine
        """
        # Ihre Lösung hier:
        pass

    def erstelle_wochenbericht(wochendaten):
        """
        Erstellt den kompletten Wochenbericht
        """
        # Ihre Lösung hier:
        pass

    # TODO: Generieren Sie den Wochenbericht
    print("WOCHENBERICHT - AUTOMATISCH GENERIERT")
    print("=" * 60)

    # bericht = erstelle_wochenbericht(wochendaten)
    # print(bericht)

    # TODO: Zusätzlich: Speichern Sie den Bericht in einer Datei
    # Dateiname: Wochenbericht_KW[KW]_[JAHR].txt

    # dateiname = f"Wochenbericht_KW{wochendaten['kw']}_{wochendaten['jahr']}.txt"
    # try:
    #     with open(dateiname, 'w', encoding='utf-8') as f:
    #         f.write(bericht)
    #     print(f"\n📄 Bericht gespeichert als: {dateiname}")
    # except Exception as e:
    #     print(f"❌ Fehler beim Speichern: {e}")

    print("✅ Aufgabe 5 abgeschlossen!\n")


def bonus_aufgabe_csv_parser():
    """Bonus-Aufgabe: CSV-Parser mit Strings"""
    print("BONUS-AUFGABE: CSV-Parser")
    print("-" * 40)

    # Gegeben: CSV-Daten als String

    # TODO: Implementieren Sie einen einfachen CSV-Parser:

    def parse_csv_string(csv_string, trenner=";"):
        """
        Parst CSV-String zu Liste von Dictionaries
        Erste Zeile = Header, weitere Zeilen = Daten
        """
        # Ihre Lösung hier:
        pass

    def filtere_daten(daten, feld, wert):
        """
        Filtert Daten nach Feld=Wert
        """
        # Ihre Lösung hier:
        pass

    def berechne_statistik(daten):
        """
        Berechnet Statistiken über die Daten
        """
        # Ihre Lösung hier:
        pass

    # TODO: Testen Sie Ihren CSV-Parser
    print("CSV-Daten parsen:")
    # daten = parse_csv_string(csv_daten)
    # if daten:
    #     print(f"  {len(daten)} Datensätze geladen")
    #     for datensatz in daten:
    #         print(f"    {datensatz['Teilnummer']}: {datensatz['Material']} - {datensatz['Status']}")

    # TODO: Filtern und Statistiken
    # ok_teile = filtere_daten(daten, 'Status', 'OK')
    # print(f"\nOK-Teile: {len(ok_teile)}")

    # stahl_teile = filtere_daten(daten, 'Material', 'Stahl')
    # print(f"Stahl-Teile: {len(stahl_teile)}")

    # statistik = berechne_statistik(daten)
    # print(f"\nStatistik: {statistik}")

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
# Aufgabe 1: String-Grundlagen
firma_formatiert = firma.title()
maschine_formatiert = maschine.strip().title()
beschreibung_formatiert = beschreibung.replace('\\n', ' ')

laenge = len(teilenummer)
erstes_zeichen = teilenummer[0]
letztes_zeichen = teilenummer[-1]
mittlerer_teil = teilenummer[4:8]
teile = teilenummer.split('-')
neue_nummer = teilenummer.replace('2024', '2025')

# Aufgabe 2: String-Formatierung
effizienz = (teile_ist / teile_soll) * 100
gesamtkosten = teile_ist * kosten_pro_teil

bericht_f = f\"\"\"
PRODUKTIONSBERICHT {datum.strftime('%d.%m.%Y')}
Mitarbeiter: {mitarbeiter}
Maschine: {maschine}
Schicht: {schicht}
Teile: {teile_ist:,} von {teile_soll:,} ({effizienz:.1f}%)
Laufzeit: {laufzeit:.2f} Stunden
Gesamtkosten: {gesamtkosten:,.2f}€
"""
        )


# Tabellenformatierung
print(f"{'Tag':<10} {'Soll':<6} {'Ist':<6} {'Effizienz':<10} {'Kosten':<10}")
for tag, soll, ist, eff, kosten in wochendaten:
    print(f"{tag:<10} {soll:<6} {ist:<6} {eff:>8.1f}% {kosten:>9.2f}€")


# Aufgabe 3: Validierung
def ist_gueltige_teilenummer(nummer):
    pattern = r"^BSF-\\d{4}-\\d{4}-\\d{3}$"
    return bool(re.match(pattern, nummer)) if nummer else False


def ist_gueltige_email(email):
    return "@" in email and "." in email.split("@")[-1] if email else False


def ist_gueltige_maschinennummer(nummer):
    pattern = r"^(LASER|PRESSE|STANZE|CNC)_\\d{3}$"
    return bool(re.match(pattern, nummer)) if nummer else False


# Aufgabe 4: Dateinamen
def generiere_produktionsdatei(maschine, datum, schicht):
    datum_str = datum.strftime("%Y%m%d")
    return f"Produktion_{maschine}_{datum_str}_{schicht}.csv"


def generiere_backup_pfad(basis_pfad, datum):
    jahr = datum.strftime("%Y")
    monat = datum.strftime("%m")
    tag = datum.strftime("%Y-%m-%d")
    return f"{basis_pfad}/Backup/{jahr}/{monat}/{tag}/"


def parse_log_datei(dateiname):
    pattern = r"LOG_([A-Z]+_\\d{3})_(\\d{8})_(\\d{6})\\.log"
    match = re.match(pattern, dateiname)
    if match:
        return {
            "maschine": match.group(1),
            "datum": match.group(2),
            "zeit": match.group(3),
        }
    return None


# Aufgabe 5: Bericht-Generierung
def erstelle_tageszeile(tag, daten):
    teile = daten["teile"]
    laufzeit = daten["laufzeit"]
    ausschuss = daten["ausschuss"]
    effizienz = ((teile - ausschuss) / teile) * 100
    return f"{tag:<10} {teile:>6} {laufzeit:>8.1f}h {ausschuss:>8} {effizienz:>10.1f}%"


def berechne_wochensumme(tage_daten):
    gesamt_teile = sum(tag["teile"] for tag in tage_daten.values())
    gesamt_laufzeit = sum(tag["laufzeit"] for tag in tage_daten.values())
    gesamt_ausschuss = sum(tag["ausschuss"] for tag in tage_daten.values())
    return {
        "gesamt_teile": gesamt_teile,
        "gesamt_laufzeit": gesamt_laufzeit,
        "gesamt_ausschuss": gesamt_ausschuss,
    }


# Bonus: CSV-Parser
def parse_csv_string(csv_string, trenner=";"):
    zeilen = csv_string.strip().split("\\n")
    if not zeilen:
        return []

    header = zeilen[0].split(trenner)
    daten = []

    for zeile in zeilen[1:]:
        werte = zeile.split(trenner)
        if len(werte) == len(header):
            datensatz = dict(zip(header, werte, strict=False))
            daten.append(datensatz)

    return daten


def filtere_daten(daten, feld, wert):
    return [d for d in daten if d.get(feld) == wert]


def berechne_statistik(daten):
    ok_anzahl = len([d for d in daten if d.get("Status") == "OK"])
    gesamt_anzahl = len(daten)
    materialien = {d.get("Material", "") for d in daten}

    return {
        "gesamt": gesamt_anzahl,
        "ok": ok_anzahl,
        "ok_prozent": (ok_anzahl / gesamt_anzahl * 100) if gesamt_anzahl > 0 else 0,
        "materialien": len(materialien),
    }


def main():
    """Hauptfunktion der Übung"""
    print("=" * 50)
    print("BYSTRONIC PYTHON GRUNDKURS")
    print("Kapitel 2 - Übung 2: String-Verarbeitung")
    print("=" * 50)

    print(
        """
Diese Übung behandelt die wichtigsten String-Operationen in Python:
• String-Manipulation (strip, replace, split, join)
• String-Formatierung (f-strings, .format(), %)
• String-Validierung mit regulären Ausdrücken
• Praktische Anwendungen für Dateipfade und Berichte

Bearbeiten Sie die Aufgaben der Reihe nach und implementieren
Sie die TODO-Kommentare.
"""
    )

    try:
        aufgabe_1_string_grundlagen()
        aufgabe_2_string_formatierung()
        aufgabe_3_string_validierung()
        aufgabe_4_dateinamen_verwaltung()
        aufgabe_5_bericht_generierung()
        bonus_aufgabe_csv_parser()

        print("🎉 Alle Aufgaben abgeschlossen!")
        print("\nSie haben erfolgreich gelernt:")
        print("✓ Strings zu manipulieren und formatieren")
        print("✓ String-Validierung mit regulären Ausdrücken")
        print("✓ Dateinamen und Pfade zu verwalten")
        print("✓ Automatische Berichte zu generieren")
        print("✓ CSV-Daten mit Strings zu verarbeiten")

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
