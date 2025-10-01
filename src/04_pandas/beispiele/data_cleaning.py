#!/usr/bin/env python3
"""
Datenbereinigung - Pandas Tutorial für SmartFactory

Dieses Beispiel demonstriert wichtige Datenbereinigungstechniken:
- Umgang mit fehlenden Werten (NaN)
- Erkennen und Behandeln von Duplikaten
- Datentyp-Konvertierung
- Ausreisser-Behandlung
- String-Bereinigung

Für SmartFactory-Entwickler: Robuste Datenverarbeitung für Produktionsdaten
"""

import warnings
from datetime import datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

print("=" * 60)
print("🧹 PANDAS DATENBEREINIGUNG")
print("=" * 60)


# Beispieldaten mit typischen Problemen erstellen
def create_messy_data():
    """Erstelle Beispieldaten mit typischen Datenproblemen"""
    np.random.seed(42)

    data = {
        "Datum": [
            "2024-01-01",
            "01.02.2024",
            "2024/03/01",
            "2024-04-01",
            "invalid_date",
            "2024-05-01",
            None,
            "2024-06-01",
        ],
        "Maschine": [
            "Laser_01",
            "  laser_01  ",
            "LASER_01",
            "Presse_01",
            "presse_01",
            "Stanze_01",
            "",
            "Laser_02",
        ],
        "Temperatur": [
            "20.5",
            "21.2",
            "invalid",
            "19.8",
            "22.1",
            "150.0",  # Ausreisser
            None,
            "20.1",
        ],
        "Produktionszeit": [
            8.5,
            7.2,
            9.1,
            None,
            8.8,
            -2.0,  # Negativer Wert
            7.5,
            8.0,
        ],
        "Status": ["OK", "ok", "OK", "Fehler", "FEHLER", "Ok", "OK", "fehler"],
        "Kommentar": [
            "Normal",
            "Alles gut",
            "",
            "Störung Sensor 3",
            "   ",
            "Wartung erforderlich",
            None,
            "Normal",
        ],
    }

    # Duplikate hinzufügen
    df = pd.DataFrame(data)

    # Einige Zeilen duplizieren
    duplicate_row = df.iloc[0].copy()
    duplicate_row["Datum"] = "2024-01-01"  # Exaktes Duplikat
    df = pd.concat([df, pd.DataFrame([duplicate_row])], ignore_index=True)

    # Ähnliches Duplikat (nur Gross-/Kleinschreibung unterschiedlich)
    similar_row = df.iloc[1].copy()
    similar_row["Maschine"] = "LASER_01"
    df = pd.concat([df, pd.DataFrame([similar_row])], ignore_index=True)

    return df


# 1. Problematische Daten laden
print("\n1️⃣ Problematische Daten analysieren")
print("-" * 40)

df_messy = create_messy_data()
print("Original-Daten mit Problemen:")
print(df_messy)
print(f"\nDataFrame Shape: {df_messy.shape}")
print(f"Datentypen:\n{df_messy.dtypes}")

# 2. Überblick über Datenqualitätsprobleme
print("\n2️⃣ Datenqualitätsprobleme identifizieren")
print("-" * 40)

print("Fehlende Werte pro Spalte:")
missing_values = df_messy.isnull().sum()
print(missing_values)

print(f"\nFehlende Werte gesamt: {df_messy.isnull().sum().sum()}")
print(
    f"Prozent fehlender Werte: {(df_messy.isnull().sum().sum() / df_messy.size * 100):.1f}%"
)

print("\nEindeutige Werte pro Spalte:")
for col in df_messy.columns:
    unique_count = df_messy[col].nunique()
    print(f"{col}: {unique_count} eindeutige Werte")

# Duplikate identifizieren
print(f"\nDuplizierte Zeilen: {df_messy.duplicated().sum()}")
print("Duplizierte Zeilen anzeigen:")
duplicates = df_messy[df_messy.duplicated(keep=False)]
print(duplicates)

# 3. String-Bereinigung
print("\n3️⃣ String-Bereinigung")
print("-" * 40)

df_clean = df_messy.copy()

# Whitespace entfernen
print("Vorher - Maschinennamen:")
print(df_clean["Maschine"].tolist())

df_clean["Maschine"] = df_clean["Maschine"].astype(str).str.strip()
print("\nNach Whitespace-Entfernung:")
print(df_clean["Maschine"].tolist())

# Gross-/Kleinschreibung normalisieren
df_clean["Maschine"] = df_clean["Maschine"].str.title()
df_clean["Status"] = df_clean["Status"].str.upper()

print("\nNach Normalisierung:")
print(f"Maschinen: {df_clean['Maschine'].tolist()}")
print(f"Status: {df_clean['Status'].tolist()}")

# Leere Strings zu NaN konvertieren
df_clean["Maschine"] = df_clean["Maschine"].replace("", np.nan)
df_clean["Kommentar"] = df_clean["Kommentar"].replace(["", "   "], np.nan)

print("\nNach Behandlung leerer Strings - NaN Count:")
print(df_clean.isnull().sum())

# 4. Datentyp-Konvertierung
print("\n4️⃣ Datentyp-Konvertierung")
print("-" * 40)

# Datum konvertieren mit Fehlerbehandlung
print("Datum-Konvertierung:")
df_clean["Datum_Original"] = df_clean["Datum"].copy()


# Verschiedene Datumsformate versuchen
def parse_date_flexible(date_str):
    """Flexibles Datum-Parsing für verschiedene Formate"""
    if pd.isna(date_str):
        return np.nan

    formats = ["%Y-%m-%d", "%d.%m.%Y", "%Y/%m/%d"]
    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue
    return np.nan


df_clean["Datum"] = df_clean["Datum"].apply(parse_date_flexible)
print(f"Erfolgreich konvertierte Daten: {df_clean['Datum'].notna().sum()}")
print(f"Fehlgeschlagene Konvertierungen: {df_clean['Datum'].isna().sum()}")

# Numerische Werte bereinigen
print("\nTemperatur-Konvertierung:")
df_clean["Temperatur_Original"] = df_clean["Temperatur"].copy()
df_clean["Temperatur"] = pd.to_numeric(df_clean["Temperatur"], errors="coerce")

print(f"Gültige Temperaturen: {df_clean['Temperatur'].notna().sum()}")
print(f"Ungültige Temperaturen: {df_clean['Temperatur'].isna().sum()}")

# 5. Ausreisser-Behandlung
print("\n5️⃣ Ausreisser-Behandlung")
print("-" * 40)

# Statistische Analyse der numerischen Spalten
numeric_cols = ["Temperatur", "Produktionszeit"]

for col in numeric_cols:
    if col in df_clean.columns:
        print(f"\n{col} - Statistische Übersicht:")
        print(df_clean[col].describe())

        # Quartilsabstände-Methode (IQR)
        Q1 = df_clean[col].quantile(0.25)
        Q3 = df_clean[col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = df_clean[
            (df_clean[col] < lower_bound) | (df_clean[col] > upper_bound)
        ]

        print(f"Ausreisser-Grenzen: {lower_bound:.2f} bis {upper_bound:.2f}")
        print(f"Gefundene Ausreisser: {len(outliers)}")

        if not outliers.empty:
            print("Ausreisser-Werte:")
            print(outliers[[col]].dropna())

# Geschäftslogik-basierte Bereinigung
print("\nGeschäftslogik-basierte Bereinigung:")

# Negative Produktionszeit korrigieren
negative_prod = df_clean["Produktionszeit"] < 0
if negative_prod.any():
    print(f"Negative Produktionszeiten gefunden: {negative_prod.sum()}")
    df_clean.loc[negative_prod, "Produktionszeit"] = np.nan

# Unrealistische Temperaturwerte
unrealistic_temp = (df_clean["Temperatur"] < -10) | (df_clean["Temperatur"] > 60)
if unrealistic_temp.any():
    print(f"Unrealistische Temperaturen gefunden: {unrealistic_temp.sum()}")
    df_clean.loc[unrealistic_temp, "Temperatur"] = np.nan

# 6. Duplikate behandeln
print("\n6️⃣ Duplikate behandeln")
print("-" * 40)

print(f"Duplikate vor Bereinigung: {df_clean.duplicated().sum()}")

# Exakte Duplikate entfernen
df_clean = df_clean.drop_duplicates()
print(f"Nach Entfernung exakter Duplikate: {len(df_clean)} Zeilen")

# Ähnliche Duplikate behandeln (basierend auf Schlüsselspalten)
key_columns = ["Datum", "Maschine"]
similar_duplicates = df_clean.duplicated(subset=key_columns, keep=False)
if similar_duplicates.any():
    print(
        f"Ähnliche Duplikate (basierend auf {key_columns}): {similar_duplicates.sum()}"
    )
    print("Ähnliche Duplikate:")
    print(df_clean[similar_duplicates].sort_values(key_columns))

    # Neueste Version beibehalten (wenn Datum verfügbar)
    df_clean = df_clean.sort_values("Datum").drop_duplicates(
        subset=key_columns, keep="last"
    )
    print(f"Nach Bereinigung ähnlicher Duplikate: {len(df_clean)} Zeilen")

# 7. Fehlende Werte behandeln
print("\n7️⃣ Fehlende Werte behandeln")
print("-" * 40)

print("Fehlende Werte vor Behandlung:")
print(df_clean.isnull().sum())

# Strategie 1: Forward Fill für Maschinennamen (letzter bekannter Wert)
if df_clean["Maschine"].isnull().any():
    df_clean["Maschine"] = df_clean["Maschine"].fillna(method="ffill")
    print("Maschinennamen mit Forward Fill ergänzt")

# Strategie 2: Median für numerische Werte
for col in ["Temperatur", "Produktionszeit"]:
    if col in df_clean.columns and df_clean[col].isnull().any():
        median_value = df_clean[col].median()
        df_clean[col] = df_clean[col].fillna(median_value)
        print(f"{col} fehlende Werte mit Median ({median_value:.2f}) ergänzt")

# Strategie 3: Modus für kategorische Werte
if df_clean["Status"].isnull().any():
    mode_value = df_clean["Status"].mode()[0]
    df_clean["Status"] = df_clean["Status"].fillna(mode_value)
    print(f"Status fehlende Werte mit Modus ('{mode_value}') ergänzt")

# Strategie 4: Spezifische Geschäftslogik
if df_clean["Kommentar"].isnull().any():
    df_clean["Kommentar"] = df_clean["Kommentar"].fillna("Kein Kommentar")
    print("Kommentare mit Standardtext ergänzt")

print("\nFehlende Werte nach Behandlung:")
print(df_clean.isnull().sum())

# 8. Erweiterte Bereinigungstechniken
print("\n8️⃣ Erweiterte Bereinigungstechniken")
print("-" * 40)

# Konsistenz-Checks
print("Konsistenz-Checks:")

# Status-Werte normalisieren
valid_statuses = ["OK", "FEHLER"]
invalid_status = ~df_clean["Status"].isin(valid_statuses)
if invalid_status.any():
    print(f"Ungültige Status-Werte gefunden: {invalid_status.sum()}")
    # Ähnliche Werte zuordnen
    status_mapping = {
        "FEHLER": ["FEHLER", "FEHLR"],  # Typos
        "OK": ["OK", "O"],
    }

    for correct_status, variations in status_mapping.items():
        for variation in variations:
            df_clean.loc[df_clean["Status"] == variation, "Status"] = correct_status

# Plausibilitätsprüfungen hinzufügen
df_clean["Data_Quality_Score"] = 100.0

# Abzug für fehlende Originaldaten
if "Datum_Original" in df_clean.columns:
    invalid_dates = df_clean["Datum"].isnull() & df_clean["Datum_Original"].notna()
    df_clean.loc[invalid_dates, "Data_Quality_Score"] -= 20

# Abzug für Ausreisser-Korrekturen
temp_corrections = (
    df_clean["Temperatur"].isnull() & df_clean["Temperatur_Original"].notna()
)
df_clean.loc[temp_corrections, "Data_Quality_Score"] -= 15

# 9. Validierungsregeln implementieren
print("\n9️⃣ Validierungsregeln implementieren")
print("-" * 40)


def validate_cleaned_data(df):
    """Umfassende Validierung der bereinigten Daten"""
    validation_results = {}

    # 1. Vollständigkeits-Check
    completeness = (df.notna().sum() / len(df) * 100).round(2)
    validation_results["completeness"] = completeness

    # 2. Konsistenz-Check
    consistency_issues = []

    # Datum-Konsistenz
    if df["Datum"].notna().any():
        future_dates = df["Datum"] > pd.Timestamp.now()
        if future_dates.any():
            consistency_issues.append(f"Zukunftsdaten: {future_dates.sum()}")

    # Numerische Konsistenz
    if "Produktionszeit" in df.columns:
        invalid_prod_time = (df["Produktionszeit"] < 0) | (df["Produktionszeit"] > 24)
        if invalid_prod_time.any():
            consistency_issues.append(
                f"Ungültige Produktionszeit: {invalid_prod_time.sum()}"
            )

    validation_results["consistency_issues"] = consistency_issues

    # 3. Eindeutigkeit-Check
    duplicates = df.duplicated().sum()
    validation_results["duplicates"] = duplicates

    return validation_results


validation_results = validate_cleaned_data(df_clean)
print("Validierungsergebnisse:")
print(f"Vollständigkeit:\n{validation_results['completeness']}")
print(f"Konsistenz-Probleme: {validation_results['consistency_issues']}")
print(f"Duplikate: {validation_results['duplicates']}")

# 10. Bereinigungsbericht erstellen
print("\n🔟 Bereinigungsbericht erstellen")
print("-" * 40)


def create_cleaning_report(df_original, df_cleaned):
    """Erstellt einen detaillierten Bereinigungsbericht"""
    report = {
        "Verarbeitungsdatum": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "Ursprüngliche_Zeilen": len(df_original),
        "Bereinigte_Zeilen": len(df_cleaned),
        "Entfernte_Zeilen": len(df_original) - len(df_cleaned),
        "Spalten": list(df_cleaned.columns),
        "Datentyp_Änderungen": {},
    }

    # Datentyp-Änderungen dokumentieren
    for col in df_original.columns:
        if col in df_cleaned.columns:
            old_type = df_original[col].dtype
            new_type = df_cleaned[col].dtype
            if old_type != new_type:
                report["Datentyp_Änderungen"][col] = {
                    "vorher": str(old_type),
                    "nachher": str(new_type),
                }

    # Qualitäts-Metriken
    report["Datenqualität"] = {
        "Vollständigkeit_vorher": f"{((df_original.notna().sum().sum() / df_original.size) * 100):.1f}%",
        "Vollständigkeit_nachher": f"{((df_cleaned.notna().sum().sum() / df_cleaned.size) * 100):.1f}%",
        "Duplikate_entfernt": len(df_original) - len(df_cleaned.drop_duplicates()),
    }

    return report


cleaning_report = create_cleaning_report(df_messy, df_clean)
print("📊 Bereinigungsbericht:")
for key, value in cleaning_report.items():
    if isinstance(value, dict):
        print(f"{key}:")
        for sub_key, sub_value in value.items():
            print(f"  {sub_key}: {sub_value}")
    else:
        print(f"{key}: {value}")

# 11. Finaler Vergleich
print("\n1️⃣1️⃣ Vorher/Nachher Vergleich")
print("-" * 40)

print("🔴 VORHER (Problematische Daten):")
print(df_messy.head())
print(f"Datentypen: {dict(df_messy.dtypes)}")
print(f"Fehlende Werte: {df_messy.isnull().sum().sum()}")
print(f"Duplikate: {df_messy.duplicated().sum()}")

print("\n🟢 NACHHER (Bereinigte Daten):")
print(df_clean.head())
print(f"Datentypen: {dict(df_clean.dtypes)}")
print(f"Fehlende Werte: {df_clean.isnull().sum().sum()}")
print(f"Duplikate: {df_clean.duplicated().sum()}")

# 12. Export der bereinigten Daten
print("\n1️⃣2️⃣ Export der bereinigten Daten")
print("-" * 40)

# Bereinigungsdokumentation als zusätzliche Spalten
df_export = df_clean.copy()
df_export["Bereinigt_Am"] = datetime.now().strftime("%Y-%m-%d")
df_export["Qualitätsscore"] = df_export["Data_Quality_Score"]

# Export als CSV
export_file = "data/generated/bereinigte_produktionsdaten.csv"
df_export.to_csv(export_file, index=False, encoding="utf-8")
print(f"✅ Bereinigte Daten exportiert: {export_file}")

# Bereinigungsprotokoll als JSON
import json

protocol_file = "data/generated/bereinigungsprotokoll.json"
with open(protocol_file, "w", encoding="utf-8") as f:
    json.dump(cleaning_report, f, indent=2, ensure_ascii=False, default=str)
print(f"✅ Bereinigungsprotokoll exportiert: {protocol_file}")

print("\n" + "=" * 60)
print("🎯 ZUSAMMENFASSUNG: DATENBEREINIGUNG")
print("=" * 60)
print("✅ Datenqualitätsprobleme identifizieren")
print("✅ String-Bereinigung und Normalisierung")
print("✅ Datentyp-Konvertierung mit Fehlerbehandlung")
print("✅ Ausreisser-Erkennung und -Behandlung")
print("✅ Intelligente Duplikate-Bereinigung")
print("✅ Verschiedene Strategien für fehlende Werte")
print("✅ Validierungsregeln implementieren")
print("✅ Bereinigungsprotokoll erstellen")
print("✅ Qualitäts-Metriken berechnen")
print("\n💡 Als SmartFactory-Entwickler können Sie jetzt robuste")
print("   Datenbereinigung für Produktionsdaten implementieren!")
print("   Nächster Schritt: Erweiterte Datenanalyse und Aggregationen")
