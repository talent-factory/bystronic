#!/usr/bin/env python3
"""
Datenimport und -export - Pandas Tutorial für Bystronic

Dieses Beispiel demonstriert verschiedene Import/Export-Möglichkeiten:
- CSV-Dateien lesen und schreiben
- Excel-Dateien verarbeiten
- JSON-Daten handhaben
- Verschiedene Formatierungsoptionen

Für Bystronic-Entwickler: Alternativen zu Excel-VBA für Datenverarbeitung
"""

import json
from datetime import datetime
from pathlib import Path

import numpy as np
import pandas as pd

print("=" * 60)
print("📁 PANDAS DATENIMPORT UND -EXPORT")
print("=" * 60)


# Beispieldaten erstellen für Demonstrationszwecke
def create_sample_data():
    """Erstelle Beispieldaten für verschiedene Export-Formate"""
    np.random.seed(42)

    # Produktionsdaten
    start_date = pd.Timestamp("2024-01-01")
    dates = pd.date_range(start_date, periods=30, freq="D")

    maschinen = ["Laser_01", "Laser_02", "Presse_01", "Presse_02", "Stanze_01"]
    schichten = ["Früh", "Spät", "Nacht"]

    data = []
    for i, datum in enumerate(dates):
        for maschine in maschinen:
            for schicht in schichten:
                if np.random.random() > 0.1:  # 90% Wahrscheinlichkeit für Daten
                    data.append(
                        {
                            "Datum": datum.date(),
                            "Maschine": maschine,
                            "Schicht": schicht,
                            "Produktionszeit": round(np.random.uniform(6.0, 10.0), 2),
                            "Stückzahl": np.random.randint(50, 200),
                            "Ausschuss": round(np.random.uniform(0.01, 0.08), 4),
                            "Energieverbrauch": round(np.random.uniform(150, 300), 1),
                            "Temperatur": round(np.random.uniform(18.5, 24.5), 1),
                            "Wartung_erforderlich": np.random.choice(
                                [True, False], p=[0.1, 0.9]
                            ),
                        }
                    )

    return pd.DataFrame(data)


# 1. CSV-Dateien - Der Standard für Datenaustausch
print("\n1️⃣ CSV-Dateien verarbeiten")
print("-" * 40)

# Beispieldaten erstellen
df_produktion = create_sample_data()
print(f"Beispieldaten erstellt: {len(df_produktion)} Datensätze")
print(df_produktion.head())

# CSV schreiben (Standard)
csv_datei = "data/samples/produktionsdaten.csv"
df_produktion.to_csv(csv_datei, index=False)
print(f"\n✅ CSV-Datei geschrieben: {csv_datei}")

# CSV lesen (Standard)
df_gelesen = pd.read_csv(csv_datei)
print(f"CSV-Datei gelesen: {len(df_gelesen)} Datensätze")
print("Datentypen nach CSV-Import:")
print(df_gelesen.dtypes)

# Problem: Datum als String importiert
print(f"\nDatum-Spalte Typ: {type(df_gelesen['Datum'].iloc[0])}")
print(f"Beispiel-Datum: {df_gelesen['Datum'].iloc[0]}")

# 2. CSV mit erweiterten Optionen
print("\n2️⃣ CSV mit erweiterten Optionen")
print("-" * 40)

# CSV mit deutschen Locale-Einstellungen
csv_deutsch = "produktionsdaten_deutsch.csv"
df_produktion.to_csv(
    csv_deutsch,
    index=False,
    sep=";",  # Semikolon als Trenner (Excel-Standard in Deutschland)
    decimal=",",  # Komma als Dezimaltrennzeichen
    encoding="utf-8",  # UTF-8 für Umlaute
    date_format="%d.%m.%Y",
)
print(f"✅ Deutsche CSV-Datei geschrieben: {csv_deutsch}")

# CSV mit korrekten Datentypen lesen
df_korrekt = pd.read_csv(
    csv_deutsch,
    sep=";",
    decimal=",",
    encoding="utf-8",
    parse_dates=["Datum"],  # Automatische Datum-Konvertierung
    dtype={
        "Maschine": "string",
        "Schicht": "category",
        "Wartung_erforderlich": "boolean",
    },
)
print("Datentypen nach korrektem CSV-Import:")
print(df_korrekt.dtypes)
print(f"\nDatum-Spalte Typ: {type(df_korrekt['Datum'].iloc[0])}")

# 3. Excel-Dateien verarbeiten
print("\n3️⃣ Excel-Dateien verarbeiten")
print("-" * 40)

try:
    # Excel mit mehreren Arbeitsblättern erstellen
    excel_datei = "bystronic_daten.xlsx"

    # Verschiedene Datensets für verschiedene Blätter
    df_maschinen = pd.DataFrame(
        {
            "Maschine": ["Laser_01", "Laser_02", "Presse_01", "Presse_02"],
            "Typ": ["ByStar", "ByStar", "Xpert", "Xpert"],
            "Standort": ["Halle A", "Halle A", "Halle B", "Halle B"],
            "Baujahr": [2019, 2020, 2018, 2021],
            "Anschaffung": [450000, 480000, 320000, 360000],
        }
    )

    # Monatliche Zusammenfassung
    df_monatlich = df_produktion.copy()
    df_monatlich["Monat"] = pd.to_datetime(df_monatlich["Datum"]).dt.to_period("M")
    df_zusammenfassung = (
        df_monatlich.groupby(["Monat", "Maschine"])
        .agg({"Produktionszeit": "sum", "Stückzahl": "sum", "Ausschuss": "mean"})
        .round(2)
        .reset_index()
    )

    # Excel mit mehreren Arbeitsblättern schreiben
    with pd.ExcelWriter(excel_datei, engine="openpyxl") as writer:
        df_produktion.head(100).to_excel(
            writer, sheet_name="Produktionsdaten", index=False
        )
        df_maschinen.to_excel(writer, sheet_name="Maschinen", index=False)
        df_zusammenfassung.to_excel(writer, sheet_name="Monatlich", index=False)

    print(f"✅ Excel-Datei mit 3 Arbeitsblättern erstellt: {excel_datei}")

    # Excel-Datei lesen
    # Alle Arbeitsblätter auflisten
    excel_file = pd.ExcelFile(excel_datei)
    print(f"Arbeitsblätter in Excel: {excel_file.sheet_names}")

    # Bestimmtes Arbeitsblatt lesen
    df_maschinen_gelesen = pd.read_excel(excel_datei, sheet_name="Maschinen")
    print("Maschinendaten aus Excel:")
    print(df_maschinen_gelesen)

    # Mehrere Arbeitsblätter gleichzeitig lesen
    excel_data = pd.read_excel(excel_datei, sheet_name=["Maschinen", "Monatlich"])
    print(f"Geladene Arbeitsblätter: {list(excel_data.keys())}")

except ImportError:
    print("❌ Für Excel-Support installieren: uv add openpyxl")
except Exception as e:
    print(f"Excel-Verarbeitung nicht verfügbar: {e}")

# 4. JSON-Dateien verarbeiten
print("\n4️⃣ JSON-Dateien verarbeiten")
print("-" * 40)

# Strukturierte Daten für JSON
maschinendaten_json = {
    "unternehmen": "Bystronic",
    "standort": "Niederönz",
    "erstellt_am": str(datetime.now()),
    "maschinen": [
        {
            "id": "LASER_01",
            "typ": "ByStar Fiber 4020",
            "baujahr": 2019,
            "technische_daten": {
                "leistung": "6kW",
                "arbeitsbereich": "4000x2000mm",
                "max_blechdicke": "25mm",
            },
            "wartungshistorie": [
                {"datum": "2024-01-15", "typ": "Routinewartung", "dauer_h": 4},
                {"datum": "2024-02-20", "typ": "Reparatur", "dauer_h": 8},
            ],
            "produktionsdaten_ytd": {
                "betriebsstunden": 2450.5,
                "stückzahl": 15678,
                "ausschussrate": 0.023,
            },
        },
        {
            "id": "PRESSE_01",
            "typ": "Xpert 150",
            "baujahr": 2018,
            "technische_daten": {
                "presskraft": "150t",
                "arbeitsbereich": "3000x1500mm",
                "max_blechdicke": "10mm",
            },
            "wartungshistorie": [
                {"datum": "2024-01-10", "typ": "Routinewartung", "dauer_h": 6}
            ],
            "produktionsdaten_ytd": {
                "betriebsstunden": 3200.8,
                "stückzahl": 8934,
                "ausschussrate": 0.045,
            },
        },
    ],
}

# JSON schreiben
json_datei = "maschinendaten.json"
with open(json_datei, "w", encoding="utf-8") as f:
    json.dump(maschinendaten_json, f, indent=2, ensure_ascii=False)
print(f"✅ JSON-Datei geschrieben: {json_datei}")

# JSON lesen und in DataFrame konvertieren
with open(json_datei, encoding="utf-8") as f:
    daten = json.load(f)

# Maschinen-Grunddaten extrahieren
maschinen_liste = []
for maschine in daten["maschinen"]:
    maschinen_liste.append(
        {
            "ID": maschine["id"],
            "Typ": maschine["typ"],
            "Baujahr": maschine["baujahr"],
            "Betriebsstunden": maschine["produktionsdaten_ytd"]["betriebsstunden"],
            "Stückzahl": maschine["produktionsdaten_ytd"]["stückzahl"],
            "Ausschussrate": maschine["produktionsdaten_ytd"]["ausschussrate"],
        }
    )

df_aus_json = pd.DataFrame(maschinen_liste)
print("DataFrame aus JSON erstellt:")
print(df_aus_json)

# 5. Pandas JSON-Funktionen
print("\n5️⃣ Pandas JSON-Funktionen")
print("-" * 40)

# DataFrame direkt zu JSON
df_sample = df_produktion.head(5)
json_string = df_sample.to_json(orient="records", date_format="iso")
print("DataFrame als JSON (erste 5 Zeilen, gekürzt):")
print(json_string[:200] + "...")

# JSON zurück zu DataFrame
df_from_json_string = pd.read_json(json_string, orient="records")
print("DataFrame aus JSON-String wiederhergestellt:")
print(df_from_json_string)

# 6. Datenbereinigung beim Import
print("\n6️⃣ Datenbereinigung beim Import")
print("-" * 40)

# CSV mit "schmutzigen" Daten erstellen
schmutzige_daten = pd.DataFrame(
    {
        "Maschine": ["Laser_01", "  Presse_01  ", "STANZE_01", None, "Laser_02"],
        "Produktionszeit": ["8.5", "  7.2  ", "invalid", "9.1", "6.8"],
        "Datum": ["2024-01-01", "01.02.2024", "2024/03/01", "2024-04-01", None],
        "Status": ["OK", "ok", "OK", "Fehler", "OK"],
    }
)

schmutzige_csv = "schmutzige_daten.csv"
schmutzige_daten.to_csv(schmutzige_csv, index=False)
print("Schmutzige Daten erstellt:")
print(schmutzige_daten)

# Daten mit Bereinigung lesen
df_bereinigt = pd.read_csv(schmutzige_csv)

# Bereinigungsschritte
print("\nBereinigung der Daten:")

# Whitespace entfernen
df_bereinigt["Maschine"] = df_bereinigt["Maschine"].str.strip()
print("1. Whitespace entfernt")

# Gross-/Kleinschreibung normalisieren
df_bereinigt["Maschine"] = df_bereinigt["Maschine"].str.title()
print("2. Gross-/Kleinschreibung normalisiert")

# Numerische Werte bereinigen
df_bereinigt["Produktionszeit"] = pd.to_numeric(
    df_bereinigt["Produktionszeit"].str.strip(),
    errors="coerce",  # Ungültige Werte werden zu NaN
)
print("3. Numerische Werte bereinigt")

# Status normalisieren
df_bereinigt["Status"] = df_bereinigt["Status"].str.upper()
print("4. Status normalisiert")

print("Bereinigte Daten:")
print(df_bereinigt)
print(f"Fehlende Werte: {df_bereinigt.isnull().sum().sum()}")

# 7. Grosse Dateien effizient verarbeiten
print("\n7️⃣ Grosse Dateien effizient verarbeiten")
print("-" * 40)

# Chunked Reading für grosse CSV-Dateien
chunk_size = 50  # In der Praxis: 10000 oder mehr
total_rows = 0
produktionszeit_sum = 0

print(f"Verarbeite CSV in Chunks à {chunk_size} Zeilen:")
for chunk in pd.read_csv("data/samples/produktionsdaten.csv", chunksize=chunk_size):
    total_rows += len(chunk)
    produktionszeit_sum += chunk["Produktionszeit"].sum()
    print(f"  Chunk verarbeitet: {len(chunk)} Zeilen")

print(f"Insgesamt {total_rows} Zeilen verarbeitet")
print(f"Gesamte Produktionszeit: {produktionszeit_sum:.2f} Stunden")

# 8. Datenvalidierung beim Import
print("\n8️⃣ Datenvalidierung beim Import")
print("-" * 40)


def validate_production_data(df):
    """Validiert Produktionsdaten nach Bystronic-Standards"""
    errors = []

    # Pflichtfelder prüfen
    required_columns = ["Datum", "Maschine", "Schicht", "Produktionszeit"]
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        errors.append(f"Fehlende Spalten: {missing_columns}")

    # Datentypen prüfen
    if "Produktionszeit" in df.columns:
        if not pd.api.types.is_numeric_dtype(df["Produktionszeit"]):
            errors.append("Produktionszeit muss numerisch sein")
        elif (df["Produktionszeit"] < 0).any():
            errors.append("Produktionszeit kann nicht negativ sein")
        elif (df["Produktionszeit"] > 24).any():
            errors.append("Produktionszeit kann nicht über 24h sein")

    # Geschäftsregeln prüfen
    if "Ausschuss" in df.columns:
        if (df["Ausschuss"] < 0).any() or (df["Ausschuss"] > 1).any():
            errors.append("Ausschussrate muss zwischen 0 und 1 liegen")

    return errors


# Validation testen
validation_errors = validate_production_data(df_produktion)
if validation_errors:
    print("❌ Validierungsfehler gefunden:")
    for error in validation_errors:
        print(f"  • {error}")
else:
    print("✅ Alle Validierungsprüfungen bestanden")

# 9. Export mit Formatierung
print("\n9️⃣ Export mit Formatierung")
print("-" * 40)

# Zusammenfassung für Export erstellen
export_df = (
    df_produktion.groupby(["Maschine"])
    .agg({"Produktionszeit": ["sum", "mean"], "Stückzahl": "sum", "Ausschuss": "mean"})
    .round(2)
)

# Spalten flach machen
export_df.columns = ["_".join(col).strip() for col in export_df.columns]
export_df = export_df.reset_index()

print("Export-DataFrame erstellt:")
print(export_df.head())

# CSV mit deutscher Formatierung exportieren
export_csv = "export_zusammenfassung.csv"
export_df.to_csv(
    export_csv,
    index=False,
    sep=";",
    decimal=",",
    encoding="utf-8-sig",  # BOM für Excel-Kompatibilität
    float_format="%.2f",
)
print(f"✅ Formatierte CSV-Datei exportiert: {export_csv}")

# Aufräumen - Temporäre Dateien löschen (optional)
temp_files = [
    "data/generated/produktionsdaten.csv",
    "data/generated/produktionsdaten_deutsch.csv",
    "data/generated/maschinendaten.json",
    "data/generated/schmutzige_daten.csv",
    "export_zusammenfassung.csv",
]

print("\n🧹 Temporäre Dateien erstellt (werden von .gitignore ignoriert):")
for file in temp_files:
    if Path(file).exists():
        print(f"  • {file}")

print("\n" + "=" * 60)
print("🎯 ZUSAMMENFASSUNG: DATENIMPORT UND -EXPORT")
print("=" * 60)
print("✅ CSV-Dateien mit verschiedenen Optionen")
print("✅ Excel-Dateien mit mehreren Arbeitsblättern")
print("✅ JSON-Daten strukturiert verarbeiten")
print("✅ Datenbereinigung beim Import")
print("✅ Chunked Reading für grosse Dateien")
print("✅ Datenvalidierung implementieren")
print("✅ Formatierter Export für verschiedene Systeme")
print("\n💡 Als Bystronic-Entwickler können Sie jetzt alle gängigen")
print("   Datenformate effizient mit Pandas verarbeiten!")
print("   Nächster Schritt: Datenbereinigung und -validierung")
