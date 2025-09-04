#!/usr/bin/env python3
"""
Übung 2: Datenimport - Pandas Tutorial für Bystronic

AUFGABENSTELLUNG:
In dieser Übung lernen Sie verschiedene Datenquellen zu importieren,
zu bereinigen und zu validieren. Sie arbeiten mit CSV, Excel und
JSON-Daten und lernen robuste Import-Strategien.

SCHWIERIGKEITSGRAD: Beginner bis Intermediate
ZEITAUFWAND: 45-60 Minuten

LERNZIELE:
- CSV-Dateien mit verschiedenen Optionen importieren
- Excel-Dateien mit mehreren Arbeitsblättern verarbeiten
- JSON-Daten strukturiert laden
- Datenvalidierung beim Import implementieren
- Robuste Fehlerbehandlung anwenden
"""

import json
import warnings
from datetime import datetime, timedelta
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

print("=" * 60)
print("📁 ÜBUNG 2: DATENIMPORT")
print("=" * 60)

# =============================================================================
# VORBEREITUNG: Testdaten erstellen
# =============================================================================

print("\n🔧 Vorbereitung: Erstelle Testdateien für Import-Übungen...")


# 1. CSV-Testdaten erstellen
def create_test_csv():
    """Erstelle CSV-Testdaten mit typischen Problemen"""
    np.random.seed(42)

    data = []
    maschinen = ["Laser_01", "Laser_02", "Presse_01", "Presse_02"]

    start_date = datetime(2024, 1, 1)
    for i in range(50):
        date = start_date + timedelta(days=i)
        for maschine in maschinen:
            if np.random.random() > 0.1:  # 10% fehlende Daten
                data.append(
                    {
                        "Datum": date.strftime("%Y-%m-%d"),
                        "Maschine": maschine,
                        "Produktionszeit": round(np.random.uniform(6, 10), 2),
                        "Stückzahl": np.random.randint(50, 200),
                        "Ausschuss_Rate": round(np.random.uniform(0.01, 0.08), 4),
                        "Temperatur": round(np.random.uniform(18, 30), 1),
                        "Schicht": np.random.choice(["Früh", "Spät", "Nacht"]),
                        "Bediener": f"BY{np.random.randint(100, 999)}",
                    }
                )

    df = pd.DataFrame(data)
    df.to_csv("test_produktionsdaten.csv", index=False)

    # Deutsche Version mit Semikolon
    df.to_csv("test_produktionsdaten_deutsch.csv", index=False, sep=";", decimal=",")

    return df


# 2. Excel-Testdaten erstellen
def create_test_excel():
    """Erstelle Excel-Testdaten mit mehreren Arbeitsblättern"""
    # Maschinenstammdaten
    df_maschinen = pd.DataFrame(
        {
            "Maschine": ["Laser_01", "Laser_02", "Presse_01", "Presse_02"],
            "Typ": ["ByStar", "ByStar", "Xpert", "Xpert"],
            "Baujahr": [2019, 2020, 2018, 2021],
            "Standort": ["Halle A", "Halle A", "Halle B", "Halle B"],
            "Anschaffungswert": [450000, 480000, 320000, 360000],
        }
    )

    # Wartungshistorie
    df_wartung = pd.DataFrame(
        {
            "Maschine": ["Laser_01", "Laser_01", "Laser_02", "Presse_01"],
            "Wartungsdatum": ["2024-01-15", "2023-10-10", "2024-02-01", "2024-01-10"],
            "Wartungstyp": ["Routine", "Reparatur", "Routine", "Routine"],
            "Kosten": [1200, 3500, 1100, 800],
            "Dauer_h": [4, 12, 3, 5],
        }
    )

    # In Excel schreiben
    with pd.ExcelWriter("test_maschinendaten.xlsx", engine="openpyxl") as writer:
        df_maschinen.to_excel(writer, sheet_name="Maschinen", index=False)
        df_wartung.to_excel(writer, sheet_name="Wartung", index=False)

    return df_maschinen, df_wartung


# 3. JSON-Testdaten erstellen
def create_test_json():
    """Erstelle JSON-Testdaten"""
    data = {
        "unternehmen": "Bystronic AG",
        "standort": "Niederönz",
        "export_datum": "2024-03-15T10:30:00",
        "produktionslinien": [
            {
                "id": "LINIE_A",
                "halle": "A",
                "maschinen": [
                    {
                        "id": "LASER_01",
                        "typ": "ByStar Fiber 4020",
                        "status": "Aktiv",
                        "parameter": {
                            "leistung_kw": 6.0,
                            "arbeitsbereich_x": 4000,
                            "arbeitsbereich_y": 2000,
                            "max_blechdicke_mm": 25,
                        },
                        "sensordaten": [
                            {
                                "timestamp": "2024-03-15T08:00:00",
                                "temperatur": 22.5,
                                "druck": 12.3,
                            },
                            {
                                "timestamp": "2024-03-15T09:00:00",
                                "temperatur": 23.1,
                                "druck": 12.1,
                            },
                            {
                                "timestamp": "2024-03-15T10:00:00",
                                "temperatur": 22.8,
                                "druck": 12.5,
                            },
                        ],
                    }
                ],
            },
            {
                "id": "LINIE_B",
                "halle": "B",
                "maschinen": [
                    {
                        "id": "PRESSE_01",
                        "typ": "Xpert 150",
                        "status": "Wartung",
                        "parameter": {
                            "presskraft_t": 150,
                            "arbeitsbereich_x": 3000,
                            "arbeitsbereich_y": 1500,
                            "max_blechdicke_mm": 10,
                        },
                        "sensordaten": [],
                    }
                ],
            },
        ],
    }

    with open("test_anlagendaten.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return data


# Testdaten erstellen
print("Erstelle CSV-Testdaten...")
df_csv_original = create_test_csv()
print("✅ CSV-Testdaten erstellt")

print("Erstelle Excel-Testdaten...")
df_maschinen_original, df_wartung_original = create_test_excel()
print("✅ Excel-Testdaten erstellt")

print("Erstelle JSON-Testdaten...")
json_original = create_test_json()
print("✅ JSON-Testdaten erstellt")

# =============================================================================
# AUFGABE 1: Einfacher CSV-Import (10 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 1: Einfacher CSV-Import")
print("-" * 40)

print(
    """
TODO: Importieren Sie die Datei 'test_produktionsdaten.csv'

a) Laden Sie die CSV-Datei als DataFrame
b) Inspizieren Sie die ersten 5 Zeilen und die Datentypen
c) Prüfen Sie die DataFrame-Größe und fehlende Werte
d) Konvertieren Sie die Datum-Spalte zum datetime-Typ
"""
)

print("a) CSV-Datei laden:")
# IHRE LÖSUNG HIER:
df_produktion = pd.read_csv("test_produktionsdaten.csv")
print(
    f"✅ Datei geladen: {len(df_produktion)} Zeilen, {len(df_produktion.columns)} Spalten"
)

print("\nb) Erste 5 Zeilen und Datentypen:")
# IHRE LÖSUNG HIER:
print("Erste 5 Zeilen:")
print(df_produktion.head())
print("\\nDatentypen:")
print(df_produktion.dtypes)

print("\nc) DataFrame-Größe und fehlende Werte:")
# IHRE LÖSUNG HIER:
print(f"Shape: {df_produktion.shape}")
print("Fehlende Werte pro Spalte:")
print(df_produktion.isnull().sum())

print("\nd) Datum konvertieren:")
# IHRE LÖSUNG HIER:
df_produktion["Datum"] = pd.to_datetime(df_produktion["Datum"])
print(f"Datum-Typ nach Konvertierung: {df_produktion['Datum'].dtype}")
print(f"Beispiel-Datum: {df_produktion['Datum'].iloc[0]}")

# Validierung
try:
    assert len(df_produktion) > 100, "Sollte mehr als 100 Zeilen haben"
    assert (
        df_produktion["Datum"].dtype == "datetime64[ns]"
    ), "Datum sollte datetime sein"
    print("\n✅ Aufgabe 1 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 1: {e}")

# =============================================================================
# AUFGABE 2: CSV-Import mit erweiterten Optionen (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 2: CSV-Import mit erweiterten Optionen")
print("-" * 40)

print(
    """
TODO: Importieren Sie 'test_produktionsdaten_deutsch.csv' korrekt

a) Laden Sie die deutsche CSV mit korrekten Separatoren
b) Definieren Sie Datentypen beim Import
c) Parsen Sie Datumsfelder direkt beim Import
d) Behandeln Sie fehlende Werte als NaN
"""
)

print("a) Deutsche CSV mit korrekten Separatoren:")
# IHRE LÖSUNG HIER:
df_deutsch = pd.read_csv("test_produktionsdaten_deutsch.csv", sep=";", decimal=",")
print(f"✅ Deutsche CSV geladen: {len(df_deutsch)} Zeilen")

print("\nb) Mit Datentyp-Definitionen:")
# IHRE LÖSUNG HIER:
df_deutsch_typed = pd.read_csv(
    "test_produktionsdaten_deutsch.csv",
    sep=";",
    decimal=",",
    dtype={"Maschine": "string", "Schicht": "category", "Bediener": "string"},
)
print("Datentypen mit Definitionen:")
print(df_deutsch_typed.dtypes)

print("\nc) Mit direktem Datums-Parsing:")
# IHRE LÖSUNG HIER:
df_deutsch_final = pd.read_csv(
    "test_produktionsdaten_deutsch.csv",
    sep=";",
    decimal=",",
    parse_dates=["Datum"],
    dtype={"Maschine": "string", "Schicht": "category", "Bediener": "string"},
)
print(f"Datum-Typ: {df_deutsch_final['Datum'].dtype}")

print("\nd) Fehlende Werte behandeln:")
# IHRE LÖSUNG HIER:
missing_info = df_deutsch_final.isnull().sum()
print("Fehlende Werte nach Import:")
print(missing_info)
print(f"Gesamt fehlende Werte: {missing_info.sum()}")

# Validierung
try:
    assert (
        df_deutsch_final["Schicht"].dtype.name == "category"
    ), "Schicht sollte category sein"
    assert (
        df_deutsch_final["Datum"].dtype == "datetime64[ns]"
    ), "Datum sollte datetime sein"
    print("\n✅ Aufgabe 2 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 2: {e}")

# =============================================================================
# AUFGABE 3: Excel-Import (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 3: Excel-Import")
print("-" * 40)

print(
    """
TODO: Importieren Sie 'test_maschinendaten.xlsx'

a) Listen Sie alle Arbeitsblätter auf
b) Laden Sie das Arbeitsblatt 'Maschinen'
c) Laden Sie das Arbeitsblatt 'Wartung'
d) Führen Sie beide DataFrames zusammen (JOIN)
"""
)

print("a) Arbeitsblätter auflisten:")
# IHRE LÖSUNG HIER:
try:
    excel_file = pd.ExcelFile("test_maschinendaten.xlsx")
    sheet_names = excel_file.sheet_names
    print(f"Verfügbare Arbeitsblätter: {sheet_names}")
except Exception as e:
    print(f"❌ Excel-Datei konnte nicht geöffnet werden: {e}")
    print("💡 Installieren Sie openpyxl: uv add openpyxl")
    sheet_names = ["Maschinen", "Wartung"]  # Fallback

print("\\nb) Arbeitsblatt 'Maschinen' laden:")
# IHRE LÖSUNG HIER:
try:
    df_maschinen = pd.read_excel("test_maschinendaten.xlsx", sheet_name="Maschinen")
    print(f"✅ Maschinen-Daten geladen: {len(df_maschinen)} Zeilen")
    print(df_maschinen.head())
except Exception as e:
    print(f"❌ Fehler beim Laden: {e}")
    # Fallback mit Original-Daten
    df_maschinen = df_maschinen_original.copy()

print("\\nc) Arbeitsblatt 'Wartung' laden:")
# IHRE LÖSUNG HIER:
try:
    df_wartung = pd.read_excel("test_maschinendaten.xlsx", sheet_name="Wartung")
    print(f"✅ Wartungs-Daten geladen: {len(df_wartung)} Zeilen")
    print(df_wartung.head())
except Exception as e:
    print(f"❌ Fehler beim Laden: {e}")
    # Fallback mit Original-Daten
    df_wartung = df_wartung_original.copy()

print("\\nd) DataFrames zusammenführen (JOIN):")
# IHRE LÖSUNG HIER:
df_combined = df_maschinen.merge(df_wartung, on="Maschine", how="left")
print(f"✅ JOIN durchgeführt: {len(df_combined)} Zeilen")
print("Erste 3 Zeilen des kombinierten DataFrames:")
print(df_combined.head(3))

# Validierung
try:
    assert (
        "Maschine" in df_maschinen.columns
    ), "Maschinen-DataFrame sollte 'Maschine' Spalte haben"
    assert (
        "Wartungsdatum" in df_wartung.columns
    ), "Wartungs-DataFrame sollte 'Wartungsdatum' haben"
    assert len(df_combined) >= len(
        df_wartung
    ), "Combined DataFrame sollte mindestens so viele Zeilen haben"
    print("\n✅ Aufgabe 3 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 3: {e}")

# =============================================================================
# AUFGABE 4: JSON-Import (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 4: JSON-Import")
print("-" * 40)

print(
    """
TODO: Importieren Sie 'test_anlagendaten.json' und extrahieren Sie strukturierte Daten

a) Laden Sie die JSON-Datei
b) Extrahieren Sie Maschinendaten in einen DataFrame
c) Extrahieren Sie Sensordaten in einen separaten DataFrame
d) Analysieren Sie die Struktur der importierten Daten
"""
)

print("a) JSON-Datei laden:")
# IHRE LÖSUNG HIER:
with open("test_anlagendaten.json", encoding="utf-8") as f:
    json_data = json.load(f)
print("✅ JSON geladen")
print(f"Unternehmen: {json_data['unternehmen']}")
print(f"Standort: {json_data['standort']}")
print(f"Anzahl Produktionslinien: {len(json_data['produktionslinien'])}")

print("\\nb) Maschinendaten extrahieren:")
# IHRE LÖSUNG HIER:
maschinen_liste = []
for linie in json_data["produktionslinien"]:
    for maschine in linie["maschinen"]:
        maschinen_liste.append(
            {
                "Linie_ID": linie["id"],
                "Halle": linie["halle"],
                "Maschine_ID": maschine["id"],
                "Typ": maschine["typ"],
                "Status": maschine["status"],
                "Leistung_kW": maschine["parameter"].get("leistung_kw", None),
                "Presskraft_t": maschine["parameter"].get("presskraft_t", None),
                "Arbeitsbereich_X": maschine["parameter"]["arbeitsbereich_x"],
                "Arbeitsbereich_Y": maschine["parameter"]["arbeitsbereich_y"],
                "Max_Blechdicke": maschine["parameter"]["max_blechdicke_mm"],
            }
        )

df_maschinen_json = pd.DataFrame(maschinen_liste)
print(f"✅ Maschinendaten extrahiert: {len(df_maschinen_json)} Maschinen")
print(df_maschinen_json)

print("\\nc) Sensordaten extrahieren:")
# IHRE LÖSUNG HIER:
sensor_liste = []
for linie in json_data["produktionslinien"]:
    for maschine in linie["maschinen"]:
        for sensor_reading in maschine["sensordaten"]:
            sensor_liste.append(
                {
                    "Maschine_ID": maschine["id"],
                    "Timestamp": sensor_reading["timestamp"],
                    "Temperatur": sensor_reading["temperatur"],
                    "Druck": sensor_reading["druck"],
                }
            )

df_sensoren = pd.DataFrame(sensor_liste)
if len(df_sensoren) > 0:
    df_sensoren["Timestamp"] = pd.to_datetime(df_sensoren["Timestamp"])
    print(f"✅ Sensordaten extrahiert: {len(df_sensoren)} Messwerte")
    print(df_sensoren.head())
else:
    print("ℹ️ Keine Sensordaten vorhanden")

print("\\nd) Struktur-Analyse:")
# IHRE LÖSUNG HIER:
print("JSON-Struktur Analyse:")
print(f"• Toplevel Keys: {list(json_data.keys())}")
print(f"• Produktionslinien: {len(json_data['produktionslinien'])}")
print(f"• Maschinen total: {len(df_maschinen_json)}")
print(
    f"• Aktive Maschinen: {len(df_maschinen_json[df_maschinen_json['Status'] == 'Aktiv'])}"
)
print(
    f"• Maschinen in Wartung: {len(df_maschinen_json[df_maschinen_json['Status'] == 'Wartung'])}"
)

# Validierung
try:
    assert len(df_maschinen_json) > 0, "Sollte Maschinendaten extrahiert haben"
    assert "Maschine_ID" in df_maschinen_json.columns, "Sollte Maschine_ID Spalte haben"
    print("\n✅ Aufgabe 4 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 4: {e}")

# =============================================================================
# AUFGABE 5: Datenvalidierung beim Import (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 5: Datenvalidierung beim Import")
print("-" * 40)

print(
    """
TODO: Implementieren Sie eine robuste Validierung für die importierten Daten

a) Erstellen Sie eine Validierungsfunktion für Produktionsdaten
b) Prüfen Sie Datentypen und Wertebereich
c) Identifizieren Sie Ausreisser und Inkonsistenzen
d) Erstellen Sie einen Validierungsreport
"""
)

print("a) Validierungsfunktion erstellen:")


# IHRE LÖSUNG HIER:
def validate_production_data(df, report_name="Import"):
    """
    Umfassende Validierung von Produktionsdaten
    """
    validation_report = {
        "dataset": report_name,
        "timestamp": datetime.now(),
        "total_records": len(df),
        "errors": [],
        "warnings": [],
        "info": [],
    }

    # Pflichtfelder prüfen
    required_fields = ["Datum", "Maschine", "Produktionszeit", "Stückzahl"]
    missing_fields = [field for field in required_fields if field not in df.columns]
    if missing_fields:
        validation_report["errors"].append(f"Fehlende Pflichtfelder: {missing_fields}")

    # Datentypen prüfen
    if "Produktionszeit" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["Produktionszeit"]):
            validation_report["errors"].append("Produktionszeit muss numerisch sein")
        else:
            # Wertebereich prüfen
            invalid_prod_time = (df["Produktionszeit"] < 0) | (
                df["Produktionszeit"] > 24
            )
            if invalid_prod_time.any():
                validation_report["warnings"].append(
                    f"Ungültige Produktionszeiten: {invalid_prod_time.sum()} Datensätze"
                )

    # Fehlende Werte
    missing_values = df.isnull().sum()
    total_missing = missing_values.sum()
    if total_missing > 0:
        validation_report["info"].append(f"Fehlende Werte gesamt: {total_missing}")
        for col, count in missing_values.items():
            if count > 0:
                validation_report["info"].append(f"  {col}: {count}")

    # Duplikate
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        validation_report["warnings"].append(f"Duplikate gefunden: {duplicates}")

    return validation_report


print("Validierungsfunktion erstellt ✅")

print("\\nb) Produktionsdaten validieren:")
# IHRE LÖSUNG HIER:
validation_result = validate_production_data(df_produktion, "Produktionsdaten CSV")
print("Validierungsergebnis:")
print(f"Dataset: {validation_result['dataset']}")
print(f"Datensätze: {validation_result['total_records']}")
print(f"Errors: {len(validation_result['errors'])}")
print(f"Warnings: {len(validation_result['warnings'])}")
print(f"Info: {len(validation_result['info'])}")

print("\\nc) Detaillierte Prüfungen:")
# IHRE LÖSUNG HIER:
# Temperatur-Ausreisser
if "Temperatur" in df_produktion.columns:
    temp_outliers = (df_produktion["Temperatur"] < 10) | (
        df_produktion["Temperatur"] > 40
    )
    print(f"Temperatur-Ausreisser: {temp_outliers.sum()}")

# Produktionszeit-Anomalien
if "Produktionszeit" in df_produktion.columns:
    prod_stats = df_produktion["Produktionszeit"].describe()
    print("Produktionszeit Statistiken:")
    print(f"  Min: {prod_stats['min']:.2f}h")
    print(f"  Max: {prod_stats['max']:.2f}h")
    print(f"  Median: {prod_stats['50%']:.2f}h")

# Maschinen-Konsistenz
maschinen_unique = df_produktion["Maschine"].nunique()
print(f"Eindeutige Maschinen: {maschinen_unique}")

print("\\nd) Validierungsreport erstellen:")


# IHRE LÖSUNG HIER:
def print_validation_report(report):
    """Formatierter Ausgabe des Validierungsreports"""
    print(f"\\n{'=' * 50}")
    print(f"VALIDIERUNGSREPORT: {report['dataset']}")
    print(f"{'=' * 50}")
    print(f"Zeitstempel: {report['timestamp'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Datensätze: {report['total_records']:,}")

    if report["errors"]:
        print(f"\\n❌ FEHLER ({len(report['errors'])}):")
        for error in report["errors"]:
            print(f"  • {error}")

    if report["warnings"]:
        print(f"\\n⚠️  WARNUNGEN ({len(report['warnings'])}):")
        for warning in report["warnings"]:
            print(f"  • {warning}")

    if report["info"]:
        print(f"\\nℹ️  INFORMATIONEN ({len(report['info'])}):")
        for info in report["info"]:
            print(f"  • {info}")

    # Qualitäts-Score berechnen
    error_penalty = len(report["errors"]) * 20
    warning_penalty = len(report["warnings"]) * 5
    quality_score = max(0, 100 - error_penalty - warning_penalty)

    print(f"\\n🎯 QUALITÄTS-SCORE: {quality_score}/100")
    return quality_score


quality_score = print_validation_report(validation_result)

# Validierung
try:
    assert "validate_production_data" in locals(), "Validierungsfunktion fehlt"
    assert validation_result["total_records"] > 0, "Sollte Datensätze validiert haben"
    print("\n✅ Aufgabe 5 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 5: {e}")

# =============================================================================
# AUFGABE 6: Robuste Import-Pipeline (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 6: Robuste Import-Pipeline")
print("-" * 40)

print(
    """
TODO: Erstellen Sie eine robuste Import-Pipeline

a) Erstellen Sie eine universelle Import-Funktion
b) Implementieren Sie Fehlerbehandlung
c) Testen Sie die Pipeline mit verschiedenen Dateien
d) Erstellen Sie ein Import-Log
"""
)

print("a) Universelle Import-Funktion:")


# IHRE LÖSUNG HIER:
def robust_import(file_path, file_type=None, **kwargs):
    """
    Robuste Import-Funktion für verschiedene Dateiformate
    """
    import_log = {
        "file_path": str(file_path),
        "timestamp": datetime.now(),
        "success": False,
        "error": None,
        "records_imported": 0,
        "warnings": [],
    }

    try:
        # Dateityp automatisch erkennen
        if file_type is None:
            if str(file_path).endswith(".csv"):
                file_type = "csv"
            elif str(file_path).endswith((".xls", ".xlsx")):
                file_type = "excel"
            elif str(file_path).endswith(".json"):
                file_type = "json"
            else:
                raise ValueError(f"Unbekannter Dateityp: {file_path}")

        # Datei importieren
        if file_type == "csv":
            # Automatische Separator-Erkennung
            with open(file_path) as f:
                first_line = f.readline()
                if ";" in first_line:
                    separator = ";"
                    decimal = ","
                else:
                    separator = ","
                    decimal = "."

            df = pd.read_csv(file_path, sep=separator, decimal=decimal, **kwargs)

        elif file_type == "excel":
            df = pd.read_excel(file_path, **kwargs)

        elif file_type == "json":
            with open(file_path, encoding="utf-8") as f:
                json_data = json.load(f)
            # Für JSON: Vereinfachte DataFrame-Erstellung
            df = pd.json_normalize(json_data)

        else:
            raise ValueError(f"Nicht unterstützter Dateityp: {file_type}")

        # Erfolg protokollieren
        import_log["success"] = True
        import_log["records_imported"] = len(df)

        return df, import_log

    except Exception as e:
        import_log["error"] = str(e)
        return None, import_log


print("✅ Universelle Import-Funktion erstellt")

print("\\nb) Import-Pipeline testen:")
# IHRE LÖSUNG HIER:
test_files = [
    "test_produktionsdaten.csv",
    "test_produktionsdaten_deutsch.csv",
    "test_maschinendaten.xlsx",
]

import_results = []
for file_path in test_files:
    if Path(file_path).exists():
        print(f"\\nTeste Import: {file_path}")
        df, log = robust_import(file_path)
        import_results.append(log)

        if log["success"]:
            print(f"  ✅ Erfolg: {log['records_imported']} Datensätze")
        else:
            print(f"  ❌ Fehler: {log['error']}")
    else:
        print(f"  ⚠️  Datei nicht gefunden: {file_path}")

print("\\nc) Fehlerbehandlung demonstrieren:")
# IHRE LÖSUNG HIER:
# Test mit nicht-existierender Datei
print("Test mit nicht-existierender Datei:")
df_error, log_error = robust_import("nicht_vorhanden.csv")
print(f"Erfolg: {log_error['success']}")
print(f"Fehler: {log_error['error']}")

print("\\nd) Import-Log erstellen:")


# IHRE LÖSUNG HIER:
def create_import_summary(import_results):
    """Erstellt eine Zusammenfassung der Import-Ergebnisse"""
    summary = {
        "total_imports": len(import_results),
        "successful_imports": sum(1 for r in import_results if r["success"]),
        "failed_imports": sum(1 for r in import_results if not r["success"]),
        "total_records": sum(r.get("records_imported", 0) for r in import_results),
        "import_log": import_results,
    }
    return summary


import_summary = create_import_summary(import_results)
print("\\n📊 IMPORT-ZUSAMMENFASSUNG:")
print(f"Gesamte Imports: {import_summary['total_imports']}")
print(f"Erfolgreiche Imports: {import_summary['successful_imports']}")
print(f"Fehlgeschlagene Imports: {import_summary['failed_imports']}")
print(f"Datensätze gesamt: {import_summary['total_records']:,}")

# Validierung
try:
    assert "robust_import" in locals(), "Import-Funktion fehlt"
    assert import_summary["total_imports"] > 0, "Sollte Imports durchgeführt haben"
    print("\n✅ Aufgabe 6 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 6: {e}")

# =============================================================================
# ZUSAMMENFASSUNG UND BEWERTUNG
# =============================================================================

print("\n" + "=" * 60)
print("🎯 ÜBUNG 2 ABGESCHLOSSEN")
print("=" * 60)

print("\n📊 ZUSAMMENFASSUNG DER IMPORTIERTEN DATEN:")
datasets_summary = {
    "CSV_Produktionsdaten": len(df_produktion) if "df_produktion" in locals() else 0,
    "CSV_Deutsch": len(df_deutsch_final) if "df_deutsch_final" in locals() else 0,
    "Excel_Maschinen": len(df_maschinen) if "df_maschinen" in locals() else 0,
    "Excel_Wartung": len(df_wartung) if "df_wartung" in locals() else 0,
    "JSON_Maschinen": len(df_maschinen_json) if "df_maschinen_json" in locals() else 0,
    "JSON_Sensoren": len(df_sensoren) if "df_sensoren" in locals() else 0,
}

total_records = sum(datasets_summary.values())
print(f"Datensätze gesamt importiert: {total_records:,}")

for dataset, count in datasets_summary.items():
    if count > 0:
        print(f"• {dataset}: {count:,} Datensätze")

print("\n📈 WICHTIGSTE ERKENNTNISSE:")
print("• CSV-Import mit verschiedenen Formaten (deutsch/international)")
print("• Excel-Import mit mehreren Arbeitsblättern")
print("• JSON-Import mit strukturierten Daten")
print("• Robuste Fehlerbehandlung implementiert")
print("• Datenvalidierung beim Import")
print("• Automatische Datentyp-Erkennung")

print("\n✅ LERNZIELE ERREICHT:")
print("• Verschiedene Dateiformate importieren")
print("• Import-Optionen und -Parameter verstehen")
print("• Datenvalidierung und Qualitätsprüfung")
print("• Robuste Error-Handling-Strategien")
print("• Automatisierte Import-Pipelines")
print("• JSON-Daten strukturiert verarbeiten")

print("\n🎓 NÄCHSTE SCHRITTE:")
print("• Übung 3: Datenbereinigung und -transformation")
print("• Große Dateien mit Chunking verarbeiten")
print("• Datenbankverbindungen für Import/Export")
print("• API-Integration für Live-Daten")

# Aufräumen - Temporäre Dateien optional löschen
temp_files = [
    "test_produktionsdaten.csv",
    "test_produktionsdaten_deutsch.csv",
    "test_maschinendaten.xlsx",
    "test_anlagendaten.json",
]

print("\n🧹 Temporäre Testdateien erstellt:")
for file in temp_files:
    if Path(file).exists():
        print(f"  • {file}")

print("\n💡 Als Bystronic-Entwickler können Sie jetzt professionell")
print("   Daten aus verschiedenen Quellen importieren und validieren!")
