#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 2
Übung 4: Datenkonvertierung und -validierung

Diese Übung behandelt:
- Type Casting zwischen verschiedenen Datentypen
- Sichere Datenkonvertierung mit Fehlerbehandlung
- Validierung von Eingabedaten
- Praktische Anwendungen für Datenimport/export
"""

import json
import csv
from io import StringIO
from datetime import datetime, date

def aufgabe_1_grundlegende_konvertierung():
    """Aufgabe 1: Grundlegende Datentyp-Konvertierung"""
    print("AUFGABE 1: Grundlegende Konvertierung")
    print("-" * 40)
    
    # Testdaten
    test_strings = ["42", "3.14", "True", "123.456", "0", "false", "", "abc123"]
    test_numbers = [42, 3.14, 0, -25, 1.23e-4]
    test_bools = [True, False, 1, 0]
    
    print("String zu anderen Typen:")
    print("-" * 25)
    
    # TODO: Implementieren Sie sichere Konvertierungsfunktionen:
    
    def sicher_zu_int(wert):
        """Konvertiert sicher zu Integer, gibt None bei Fehler zurück"""
        # try:
        #     return int(wert)
        # except (ValueError, TypeError):
        #     return None
        pass
    
    def sicher_zu_float(wert):
        """Konvertiert sicher zu Float, gibt None bei Fehler zurück"""
        # Ihre Lösung hier
        pass
    
    def sicher_zu_bool(wert):
        """Konvertiert sicher zu Boolean"""
        # Behandeln Sie verschiedene Repräsentationen:
        # "true", "True", "1", 1 -> True
        # "false", "False", "0", 0, "" -> False
        # Ihre Lösung hier
        pass
    
    # TODO: Testen Sie Ihre Funktionen
    for test_wert in test_strings:
        int_wert = sicher_zu_int(test_wert)
        float_wert = sicher_zu_float(test_wert)  
        bool_wert = sicher_zu_bool(test_wert)
        
        print(f"'{test_wert}' -> int: {int_wert}, float: {float_wert}, bool: {bool_wert}")
    
    print("\nZahlen zu anderen Typen:")
    print("-" * 25)
    
    # TODO: Konvertieren Sie Zahlen zu Strings (formatiert)
    for zahl in test_numbers:
        # string_wert = str(zahl)
        # formatiert = f"{zahl:.2f}" if isinstance(zahl, float) else str(zahl)
        # print(f"{zahl} -> string: '{string_wert}', formatiert: '{formatiert}'")
        pass
    
    print("✅ Aufgabe 1 abgeschlossen!\n")

def aufgabe_2_collections_konvertierung():
    """Aufgabe 2: Collections-Konvertierung"""
    print("AUFGABE 2: Collections-Konvertierung")
    print("-" * 40)
    
    # Testdaten
    test_liste = [1, 2, 3, 2, 4, 1, 5]
    test_string = "Python"
    test_dict = {"a": 1, "b": 2, "c": 3}
    test_set = {3, 1, 4, 1, 5, 9}
    
    print("Collections ineinander konvertieren:")
    print("-" * 35)
    
    # TODO: Führen Sie folgende Konvertierungen durch:
    
    # 1. Liste -> Set (Duplikate entfernen)
    # liste_zu_set = set(test_liste)
    
    # 2. Set -> sortierte Liste 
    # set_zu_liste = sorted(list(test_set))
    
    # 3. String -> Liste von Zeichen
    # string_zu_liste = list(test_string)
    
    # 4. Dictionary -> Listen von Keys, Values, Items
    # dict_keys = list(test_dict.keys())
    # dict_values = list(test_dict.values())
    # dict_items = list(test_dict.items())
    
    # 5. Liste von Tupeln -> Dictionary
    tupel_liste = [("name", "Max"), ("alter", 35), ("abteilung", "IT")]
    # tupel_zu_dict = dict(tupel_liste)
    
    # TODO: Geben Sie die Ergebnisse aus
    
    print("\nSpezialisierte Konvertierungen:")
    print("-" * 30)
    
    # TODO: Implementieren Sie erweiterte Konvertierungen:
    
    def liste_zu_zaehler_dict(liste):
        """Konvertiert Liste zu Dictionary mit Häufigkeiten"""
        # zaehler = {}
        # for item in liste:
        #     zaehler[item] = zaehler.get(item, 0) + 1
        # return zaehler
        pass
    
    def verschachteltes_dict_zu_flach(nested_dict, separator="_"):
        """Macht verschachteltes Dictionary flach"""
        # Beispiel: {"a": {"b": 1}} -> {"a_b": 1}
        # Ihre Lösung hier (Optional: Rekursiv implementieren)
        pass
    
    # TODO: Testen Sie Ihre Funktionen
    test_verschachtelt = {
        "maschine": {
            "id": "LASER_001",
            "specs": {
                "leistung": 6000,
                "baujahr": 2020
            }
        },
        "status": "aktiv"
    }
    
    # haeufigkeiten = liste_zu_zaehler_dict(test_liste)
    # flach = verschachteltes_dict_zu_flach(test_verschachtelt)
    
    # print(f"Häufigkeiten: {haeufigkeiten}")
    # print(f"Flaches Dict: {flach}")
    
    print("✅ Aufgabe 2 abgeschlossen!\n")

def aufgabe_3_datenvalidierung():
    """Aufgabe 3: Eingabevalidierung"""
    print("AUFGABE 3: Datenvalidierung")
    print("-" * 40)
    
    # TODO: Implementieren Sie Validierungsfunktionen:
    
    def validiere_und_konvertiere_zahl(eingabe, typ=float, min_wert=None, max_wert=None):
        """
        Validiert und konvertiert eine Zahleneingabe
        Returns: (erfolg: bool, wert: typ oder None, fehler: str)
        """
        # try:
        #     zahl = typ(eingabe)
        #     if min_wert is not None and zahl < min_wert:
        #         return False, None, f"Wert muss >= {min_wert} sein"
        #     if max_wert is not None and zahl > max_wert:
        #         return False, None, f"Wert muss <= {max_wert} sein"
        #     return True, zahl, ""
        # except (ValueError, TypeError):
        #     return False, None, f"'{eingabe}' ist keine gültige {typ.__name__}"
        pass
    
    def validiere_produktionsparameter(parameter):
        """
        Validiert Produktionsparameter Dictionary
        Erwartet: {"teile": int, "zeit": float, "material": str, "ok": bool}
        """
        erforderliche_felder = {
            "teile": (int, 1, 10000),      # min 1, max 10000
            "zeit": (float, 0.1, 24.0),   # min 0.1h, max 24h  
            "material": (str, None, None), # keine Grenzen
            "ok": (bool, None, None)       # keine Grenzen
        }
        
        fehler = []
        validierte_daten = {}
        
        # TODO: Implementieren Sie die Validierung
        # for feld, (typ, min_val, max_val) in erforderliche_felder.items():
        #     if feld not in parameter:
        #         fehler.append(f"Feld '{feld}' fehlt")
        #         continue
        #     
        #     wert = parameter[feld]
        #     erfolg, konvertiert, fehler_msg = validiere_und_konvertiere_zahl(
        #         wert, typ, min_val, max_val
        #     ) if typ in (int, float) else (True, wert, "")
        #     
        #     if not erfolg:
        #         fehler.append(f"Feld '{feld}': {fehler_msg}")
        #     else:
        #         validierte_daten[feld] = konvertiert
        
        # return len(fehler) == 0, validierte_daten, fehler
        pass
    
    # TODO: Testen Sie die Validierung
    test_parameter = [
        {"teile": "150", "zeit": "7.5", "material": "Stahl", "ok": "true"},  # OK (strings)
        {"teile": 200, "zeit": 8.2, "material": "Aluminium", "ok": True},    # OK (richtige Typen)
        {"teile": -5, "zeit": 7.5, "material": "Kupfer", "ok": True},        # Fehler: teile < 1
        {"teile": 100, "zeit": 25.0, "material": "Titan", "ok": False},      # Fehler: zeit > 24
        {"teile": 150, "material": "Stahl", "ok": True},                     # Fehler: zeit fehlt
        {"teile": "abc", "zeit": 7.5, "material": "Messing", "ok": True},    # Fehler: teile nicht int
    ]
    
    print("Validierung der Produktionsparameter:")
    print("-" * 40)
    
    for i, param in enumerate(test_parameter, 1):
        # erfolg, daten, fehler_liste = validiere_produktionsparameter(param)
        # status = "✅ Gültig" if erfolg else "❌ Ungültig"
        # print(f"Test {i}: {status}")
        # if not erfolg:
        #     for fehler in fehler_liste:
        #         print(f"  - {fehler}")
        # else:
        #     print(f"  Validierte Daten: {daten}")
        pass
    
    print("✅ Aufgabe 3 abgeschlossen!\n")

def aufgabe_4_datei_konvertierung():
    """Aufgabe 4: Datei-Format-Konvertierung"""
    print("AUFGABE 4: Datei-Format-Konvertierung")
    print("-" * 40)
    
    # Beispieldaten
    produktionsdaten = [
        {"datum": "2024-03-15", "maschine": "LASER_001", "teile": 145, "laufzeit": 7.5, "ok": True},
        {"datum": "2024-03-15", "maschine": "PRESSE_001", "teile": 89, "laufzeit": 6.8, "ok": False},
        {"datum": "2024-03-16", "maschine": "LASER_001", "teile": 152, "laufzeit": 7.8, "ok": True},
        {"datum": "2024-03-16", "maschine": "PRESSE_001", "teile": 95, "laufzeit": 7.2, "ok": True},
    ]
    
    # TODO: Implementieren Sie Konvertierungsfunktionen:
    
    def daten_zu_csv(daten, dateipfad=None):
        """Konvertiert Daten zu CSV-Format"""
        if not daten:
            return ""
        
        # CSV-String erstellen
        output = StringIO()
        # fieldnames = list(daten[0].keys())
        # writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=';')
        # writer.writeheader()
        # writer.writerows(daten)
        # csv_content = output.getvalue()
        # output.close()
        
        # if dateipfad:
        #     with open(dateipfad, 'w', encoding='utf-8') as f:
        #         f.write(csv_content)
        
        # return csv_content
        pass
    
    def csv_zu_daten(csv_string):
        """Konvertiert CSV-String zu Liste von Dictionaries"""
        input_stream = StringIO(csv_string)
        # reader = csv.DictReader(input_stream, delimiter=';')
        # daten = []
        # for row in reader:
        #     # Datentypen konvertieren
        #     konvertierte_row = {}
        #     for key, value in row.items():
        #         # Versuche intelligente Typkonvertierung
        #         if value.isdigit():
        #             konvertierte_row[key] = int(value)
        #         elif value.replace('.', '').isdigit():
        #             konvertierte_row[key] = float(value)
        #         elif value.lower() in ['true', 'false']:
        #             konvertierte_row[key] = value.lower() == 'true'
        #         else:
        #             konvertierte_row[key] = value
        #     daten.append(konvertierte_row)
        # input_stream.close()
        # return daten
        pass
    
    def daten_zu_json(daten, eingerückt=True):
        """Konvertiert Daten zu JSON-Format"""
        # return json.dumps(daten, indent=2 if eingerückt else None, 
        #                   ensure_ascii=False, default=str)
        pass
    
    def json_zu_daten(json_string):
        """Konvertiert JSON-String zu Python-Datenstrukturen"""
        # try:
        #     return json.loads(json_string)
        # except json.JSONDecodeError as e:
        #     print(f"JSON-Fehler: {e}")
        #     return None
        pass
    
    def daten_zu_html_tabelle(daten):
        """Konvertiert Daten zu HTML-Tabelle"""
        if not daten:
            return "<table></table>"
        
        # HTML-Tabelle erstellen
        # html = ["<table border='1'>"]
        # 
        # # Header
        # html.append("  <thead>")
        # html.append("    <tr>")
        # for spalte in daten[0].keys():
        #     html.append(f"      <th>{spalte.title()}</th>")
        # html.append("    </tr>")
        # html.append("  </thead>")
        # 
        # # Datenzeilen
        # html.append("  <tbody>")
        # for row in daten:
        #     html.append("    <tr>")
        #     for wert in row.values():
        #         html.append(f"      <td>{wert}</td>")
        #     html.append("    </tr>")
        # html.append("  </tbody>")
        # html.append("</table>")
        # 
        # return "\n".join(html)
        pass
    
    # TODO: Testen Sie die Konvertierungsfunktionen
    print("Datenformat-Konvertierung:")
    print("-" * 25)
    
    # CSV-Konvertierung
    # csv_output = daten_zu_csv(produktionsdaten)
    # print("CSV-Output (erste 200 Zeichen):")
    # print(csv_output[:200] + "..." if len(csv_output) > 200 else csv_output)
    
    # # JSON-Konvertierung  
    # json_output = daten_zu_json(produktionsdaten)
    # print("\nJSON-Output (erste 300 Zeichen):")
    # print(json_output[:300] + "..." if len(json_output) > 300 else json_output)
    
    # # HTML-Konvertierung
    # html_output = daten_zu_html_tabelle(produktionsdaten)
    # print("\nHTML-Output (erste 400 Zeichen):")
    # print(html_output[:400] + "..." if len(html_output) > 400 else html_output)
    
    # # Rück-Konvertierung testen
    # rueck_konvertiert = csv_zu_daten(csv_output) if csv_output else []
    # print(f"\nRück-konvertierte Daten ({len(rueck_konvertiert)} Einträge):")
    # if rueck_konvertiert:
    #     print(f"Erster Eintrag: {rueck_konvertiert[0]}")
    
    print("✅ Aufgabe 4 abgeschlossen!\n")

def aufgabe_5_datentyp_analyse():
    """Aufgabe 5: Automatische Datentyp-Analyse"""
    print("AUFGABE 5: Datentyp-Analyse")
    print("-" * 40)
    
    # TODO: Implementieren Sie ein System zur automatischen Datentyp-Erkennung
    
    def analysiere_datentyp(wert):
        """
        Analysiert einen Wert und bestimmt den wahrscheinlichsten Datentyp
        Returns: (typ_name: str, konvertierter_wert: any, vertrauen: float)
        """
        if wert is None or wert == "":
            return "null", None, 1.0
        
        wert_str = str(wert).strip()
        
        # TODO: Implementieren Sie die Analyse
        # 1. Boolean erkennen
        # if wert_str.lower() in ['true', 'false', 'ja', 'nein', 'yes', 'no']:
        #     return "boolean", wert_str.lower() in ['true', 'ja', 'yes'], 0.9
        
        # 2. Integer erkennen  
        # try:
        #     int_wert = int(wert_str)
        #     return "integer", int_wert, 0.95
        # except ValueError:
        #     pass
        
        # 3. Float erkennen
        # try:
        #     float_wert = float(wert_str)
        #     return "float", float_wert, 0.9
        # except ValueError:
        #     pass
        
        # 4. Datum erkennen (einfache Patterns)
        # datum_patterns = ["%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"]
        # for pattern in datum_patterns:
        #     try:
        #         datum = datetime.strptime(wert_str, pattern).date()
        #         return "date", datum, 0.8
        #     except ValueError:
        #         continue
        
        # 5. Zeit erkennen
        # zeit_patterns = ["%H:%M:%S", "%H:%M"]
        # for pattern in zeit_patterns:
        #     try:
        #         zeit = datetime.strptime(wert_str, pattern).time()
        #         return "time", zeit, 0.8
        #     except ValueError:
        #         continue
        
        # 6. Default: String
        # return "string", wert_str, 0.7
        pass
    
    def analysiere_datensatz(daten):
        """
        Analysiert einen kompletten Datensatz und schlägt Datentypen vor
        """
        if not daten or not isinstance(daten, list) or not daten[0]:
            return {}
        
        # Spalten identifizieren
        if isinstance(daten[0], dict):
            spalten = list(daten[0].keys())
        else:
            spalten = [f"Spalte_{i}" for i in range(len(daten[0]))]
        
        spalten_analyse = {}
        
        # TODO: Für jede Spalte Datentypen analysieren
        # for spalte in spalten:
        #     typ_zaehler = {}
        #     werte = []
        #     
        #     for row in daten:
        #         wert = row[spalte] if isinstance(row, dict) else row[spalten.index(spalte)]
        #         typ, konv_wert, vertrauen = analysiere_datentyp(wert)
        #         
        #         if typ not in typ_zaehler:
        #             typ_zaehler[typ] = {"count": 0, "confidence": 0.0}
        #         
        #         typ_zaehler[typ]["count"] += 1
        #         typ_zaehler[typ]["confidence"] += vertrauen
        #         werte.append((wert, typ, konv_wert, vertrauen))
        #     
        #     # Besten Typ ermitteln
        #     if typ_zaehler:
        #         bester_typ = max(typ_zaehler.keys(), 
        #                         key=lambda t: typ_zaehler[t]["count"] * typ_zaehler[t]["confidence"])
        #         spalten_analyse[spalte] = {
        #             "empfohlener_typ": bester_typ,
        #             "typ_verteilung": typ_zaehler,
        #             "beispiel_werte": werte[:3]
        #         }
        
        # return spalten_analyse
        pass
    
    # TODO: Testen Sie die Datentyp-Analyse
    test_daten = [
        {"id": "1", "name": "Max", "alter": "35", "gehalt": "75000.50", "aktiv": "true", "einstellung": "2020-03-15"},
        {"id": "2", "name": "Anna", "alter": "28", "gehalt": "68500.00", "aktiv": "true", "einstellung": "2021-07-22"},
        {"id": "3", "name": "Peter", "alter": "42", "gehalt": "82000.75", "aktiv": "false", "einstellung": "2019-01-10"},
        {"id": "4", "name": "Sarah", "alter": "31", "gehalt": "71200.25", "aktiv": "true", "einstellung": "2022-09-05"},
    ]
    
    print("Automatische Datentyp-Analyse:")
    print("-" * 30)
    
    # analyse = analysiere_datensatz(test_daten)
    # for spalte, info in analyse.items():
    #     print(f"\nSpalte '{spalte}':")
    #     print(f"  Empfohlener Typ: {info['empfohlener_typ']}")
    #     print(f"  Typ-Verteilung: {info['typ_verteilung']}")
    #     print(f"  Beispiel-Werte: {info['beispiel_werte']}")
    
    # TODO: Konvertierungsempfehlungen ausgeben
    print("\nKonvertierungsempfehlungen:")
    print("-" * 25)
    
    # for spalte, info in analyse.items():
    #     typ = info['empfohlener_typ']
    #     if typ == "integer":
    #         print(f"  {spalte}: int() verwenden")
    #     elif typ == "float":
    #         print(f"  {spalte}: float() verwenden")
    #     elif typ == "boolean":
    #         print(f"  {spalte}: custom boolean conversion verwenden")
    #     elif typ == "date":
    #         print(f"  {spalte}: datetime.strptime() verwenden")
    #     else:
    #         print(f"  {spalte}: als {typ} beibehalten")
    
    print("✅ Aufgabe 5 abgeschlossen!\n")

def bonus_aufgabe_serialisierung():
    """Bonus-Aufgabe: Objekt-Serialisierung"""
    print("BONUS-AUFGABE: Objekt-Serialisierung")
    print("-" * 40)
    
    # TODO: Implementieren Sie eine Klasse, die sich selbst serialisieren kann
    
    class SerializierbareMaschine:
        def __init__(self, id, typ, leistung, baujahr):
            self.id = id
            self.typ = typ
            self.leistung = leistung
            self.baujahr = baujahr
            self.wartungen = []
            self.produktionsdaten = {}
        
        def zu_dict(self):
            """Konvertiert Objekt zu Dictionary"""
            # return {
            #     "id": self.id,
            #     "typ": self.typ,
            #     "leistung": self.leistung,
            #     "baujahr": self.baujahr,
            #     "wartungen": self.wartungen,
            #     "produktionsdaten": self.produktionsdaten
            # }
            pass
        
        def zu_json(self):
            """Konvertiert Objekt zu JSON-String"""
            # return json.dumps(self.zu_dict(), indent=2, ensure_ascii=False, default=str)
            pass
        
        @classmethod
        def von_dict(cls, daten):
            """Erstellt Objekt aus Dictionary"""
            # maschine = cls(daten["id"], daten["typ"], daten["leistung"], daten["baujahr"])
            # maschine.wartungen = daten.get("wartungen", [])
            # maschine.produktionsdaten = daten.get("produktionsdaten", {})
            # return maschine
            pass
        
        @classmethod  
        def von_json(cls, json_string):
            """Erstellt Objekt aus JSON-String"""
            # try:
            #     daten = json.loads(json_string)
            #     return cls.von_dict(daten)
            # except (json.JSONDecodeError, KeyError) as e:
            #     print(f"Fehler beim JSON-Import: {e}")
            #     return None
            pass
        
        def __str__(self):
            return f"Maschine({self.id}, {self.typ}, {self.leistung}W)"
    
    # TODO: Testen Sie die Serialisierung
    print("Objekt-Serialisierung testen:")
    print("-" * 30)
    
    # Original-Objekt erstellen
    # maschine1 = SerializierbareMaschine("LASER_001", "ByStar Fiber", 6000, 2020)
    # maschine1.wartungen = ["2024-01-15", "2023-07-20"]
    # maschine1.produktionsdaten = {"heute": 145, "woche": 720}
    
    # print(f"Original: {maschine1}")
    
    # # Zu JSON serialisieren
    # json_string = maschine1.zu_json()
    # print(f"\nJSON ({len(json_string)} Zeichen):")
    # print(json_string[:200] + "..." if len(json_string) > 200 else json_string)
    
    # # Aus JSON deserialisieren
    # maschine2 = SerializierbareMaschine.von_json(json_string)
    # print(f"\nDeserialisiert: {maschine2}")
    
    # # Gleichheit prüfen
    # if maschine2:
    #     print(f"IDs gleich: {maschine1.id == maschine2.id}")
    #     print(f"Wartungen gleich: {maschine1.wartungen == maschine2.wartungen}")
    
    print("✅ Bonus-Aufgabe abgeschlossen!\n")

def loesung_anzeigen():
    """Zeigt die Musterlösung an"""
    antwort = input("Möchten Sie die Musterlösung anzeigen? (j/n): ").lower().strip()
    if antwort in ['j', 'ja', 'y', 'yes']:
        print("\n" + "="*50)
        print("MUSTERLÖSUNG")
        print("="*50)
        
        print("""
# Aufgabe 1: Grundlegende Konvertierung
def sicher_zu_int(wert):
    try:
        return int(wert)
    except (ValueError, TypeError):
        return None

def sicher_zu_float(wert):
    try:
        return float(wert)
    except (ValueError, TypeError):
        return None

def sicher_zu_bool(wert):
    if isinstance(wert, bool):
        return wert
    if isinstance(wert, (int, float)):
        return bool(wert)
    if isinstance(wert, str):
        return wert.lower() in ['true', '1', 'ja', 'yes']
    return False

# Aufgabe 2: Collections-Konvertierung
liste_zu_set = set(test_liste)
set_zu_liste = sorted(list(test_set))
string_zu_liste = list(test_string)
dict_keys = list(test_dict.keys())
dict_values = list(test_dict.values())
dict_items = list(test_dict.items())
tupel_zu_dict = dict(tupel_liste)

def liste_zu_zaehler_dict(liste):
    zaehler = {}
    for item in liste:
        zaehler[item] = zaehler.get(item, 0) + 1
    return zaehler

def verschachteltes_dict_zu_flach(nested_dict, separator="_", prefix=""):
    result = {}
    for key, value in nested_dict.items():
        new_key = f"{prefix}{separator}{key}" if prefix else key
        if isinstance(value, dict):
            result.update(verschachteltes_dict_zu_flach(value, separator, new_key))
        else:
            result[new_key] = value
    return result

# Aufgabe 3: Datenvalidierung
def validiere_und_konvertiere_zahl(eingabe, typ=float, min_wert=None, max_wert=None):
    try:
        zahl = typ(eingabe)
        if min_wert is not None and zahl < min_wert:
            return False, None, f"Wert muss >= {min_wert} sein"
        if max_wert is not None and zahl > max_wert:
            return False, None, f"Wert muss <= {max_wert} sein"
        return True, zahl, ""
    except (ValueError, TypeError):
        return False, None, f"'{eingabe}' ist keine gültige {typ.__name__}"

def validiere_produktionsparameter(parameter):
    erforderliche_felder = {
        "teile": (int, 1, 10000),
        "zeit": (float, 0.1, 24.0),
        "material": (str, None, None),
        "ok": (bool, None, None)
    }
    
    fehler = []
    validierte_daten = {}
    
    for feld, (typ, min_val, max_val) in erforderliche_felder.items():
        if feld not in parameter:
            fehler.append(f"Feld '{feld}' fehlt")
            continue
        
        wert = parameter[feld]
        
        if typ in (int, float):
            erfolg, konvertiert, fehler_msg = validiere_und_konvertiere_zahl(wert, typ, min_val, max_val)
        elif typ == bool:
            konvertiert = sicher_zu_bool(wert)
            erfolg, fehler_msg = True, ""
        else:  # str
            konvertiert = str(wert)
            erfolg, fehler_msg = True, ""
        
        if not erfolg:
            fehler.append(f"Feld '{feld}': {fehler_msg}")
        else:
            validierte_daten[feld] = konvertiert
    
    return len(fehler) == 0, validierte_daten, fehler

# Aufgabe 4: Datei-Konvertierung
def daten_zu_csv(daten, dateipfad=None):
    if not daten:
        return ""
    
    output = StringIO()
    fieldnames = list(daten[0].keys())
    writer = csv.DictWriter(output, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()
    writer.writerows(daten)
    csv_content = output.getvalue()
    output.close()
    
    if dateipfad:
        with open(dateipfad, 'w', encoding='utf-8') as f:
            f.write(csv_content)
    
    return csv_content

def csv_zu_daten(csv_string):
    input_stream = StringIO(csv_string)
    reader = csv.DictReader(input_stream, delimiter=';')
    daten = []
    
    for row in reader:
        konvertierte_row = {}
        for key, value in row.items():
            if value.isdigit():
                konvertierte_row[key] = int(value)
            elif value.replace('.', '', 1).isdigit():
                konvertierte_row[key] = float(value)
            elif value.lower() in ['true', 'false']:
                konvertierte_row[key] = value.lower() == 'true'
            else:
                konvertierte_row[key] = value
        daten.append(konvertierte_row)
    
    input_stream.close()
    return daten

def daten_zu_json(daten, eingerückt=True):
    return json.dumps(daten, indent=2 if eingerückt else None, 
                      ensure_ascii=False, default=str)

def json_zu_daten(json_string):
    try:
        return json.loads(json_string)
    except json.JSONDecodeError as e:
        print(f"JSON-Fehler: {e}")
        return None

# Aufgabe 5: Datentyp-Analyse
def analysiere_datentyp(wert):
    if wert is None or wert == "":
        return "null", None, 1.0
    
    wert_str = str(wert).strip()
    
    # Boolean
    if wert_str.lower() in ['true', 'false', 'ja', 'nein', 'yes', 'no']:
        return "boolean", wert_str.lower() in ['true', 'ja', 'yes'], 0.9
    
    # Integer
    try:
        int_wert = int(wert_str)
        return "integer", int_wert, 0.95
    except ValueError:
        pass
    
    # Float
    try:
        float_wert = float(wert_str)
        return "float", float_wert, 0.9
    except ValueError:
        pass
    
    # Datum
    datum_patterns = ["%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"]
    for pattern in datum_patterns:
        try:
            datum = datetime.strptime(wert_str, pattern).date()
            return "date", datum, 0.8
        except ValueError:
            continue
    
    return "string", wert_str, 0.7

# Bonus: Serialisierung
class SerializierbareMaschine:
    def __init__(self, id, typ, leistung, baujahr):
        self.id = id
        self.typ = typ
        self.leistung = leistung
        self.baujahr = baujahr
        self.wartungen = []
        self.produktionsdaten = {}
    
    def zu_dict(self):
        return {
            "id": self.id,
            "typ": self.typ,
            "leistung": self.leistung,
            "baujahr": self.baujahr,
            "wartungen": self.wartungen,
            "produktionsdaten": self.produktionsdaten
        }
    
    def zu_json(self):
        return json.dumps(self.zu_dict(), indent=2, ensure_ascii=False, default=str)
    
    @classmethod
    def von_dict(cls, daten):
        maschine = cls(daten["id"], daten["typ"], daten["leistung"], daten["baujahr"])
        maschine.wartungen = daten.get("wartungen", [])
        maschine.produktionsdaten = daten.get("produktionsdaten", {})
        return maschine
    
    @classmethod
    def von_json(cls, json_string):
        try:
            daten = json.loads(json_string)
            return cls.von_dict(daten)
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Fehler beim JSON-Import: {e}")
            return None
""")

def main():
    """Hauptfunktion der Übung"""
    print("=" * 50)
    print("BYSTRONIC PYTHON GRUNDKURS")
    print("Kapitel 2 - Übung 4: Datenkonvertierung")
    print("=" * 50)
    
    print("""
Diese Übung behandelt die wichtigsten Aspekte der Datenkonvertierung:
• Sichere Type-Conversion mit Fehlerbehandlung
• Collections-Konvertierung zwischen verschiedenen Datentypen
• Eingabe-Validierung für robuste Anwendungen
• Datei-Format-Konvertierung (CSV, JSON, HTML)
• Automatische Datentyp-Erkennung

Bearbeiten Sie die Aufgaben der Reihe nach und implementieren
Sie die TODO-Kommentare.
""")
    
    try:
        aufgabe_1_grundlegende_konvertierung()
        aufgabe_2_collections_konvertierung()
        aufgabe_3_datenvalidierung()
        aufgabe_4_datei_konvertierung()
        aufgabe_5_datentyp_analyse()
        bonus_aufgabe_serialisierung()
        
        print("🎉 Alle Aufgaben abgeschlossen!")
        print("\nSie haben erfolgreich gelernt:")
        print("✓ Sichere Datentyp-Konvertierung durchzuführen")
        print("✓ Collections zwischen verschiedenen Typen zu konvertieren")
        print("✓ Eingabedaten zu validieren und zu bereinigen")
        print("✓ Zwischen verschiedenen Dateiformaten zu konvertieren")
        print("✓ Datentypen automatisch zu erkennen und zu analysieren")
        print("✓ Objekte zu serialisieren und zu deserialisieren")
        
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