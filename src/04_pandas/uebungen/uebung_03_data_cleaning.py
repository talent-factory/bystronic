#!/usr/bin/env python3
"""
Übung 3: Datenbereinigung - Pandas Tutorial für SmartFactory

AUFGABENSTELLUNG:
In dieser Übung lernen Sie systematische Datenbereinigung für
Produktionsdaten. Sie behandeln fehlende Werte, Ausreisser,
Duplikate und inkonsistente Daten.

SCHWIERIGKEITSGRAD: Intermediate
ZEITAUFWAND: 60-75 Minuten

LERNZIELE:
- Datenqualitätsprobleme systematisch identifizieren
- Verschiedene Strategien für fehlende Werte anwenden
- Ausreisser erkennen und behandeln
- Duplikate intelligent bereinigen
- Validierungsregeln implementieren
- Bereinigungsprotokoll erstellen
"""

import warnings
from datetime import datetime

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

print("=" * 60)
print("🧹 ÜBUNG 3: DATENBEREINIGUNG")
print("=" * 60)

# =============================================================================
# VORBEREITUNG: Problematische Testdaten erstellen
# =============================================================================

print("\n🔧 Vorbereitung: Erstelle problematische Testdaten...")


def create_messy_production_data():
    """Erstelle realistische Produktionsdaten mit typischen Qualitätsproblemen"""
    np.random.seed(42)

    # Basis-Daten
    dates = pd.date_range("2024-01-01", periods=200, freq="H")
    maschinen = ["Laser_01", "Laser_02", "Presse_01", "Presse_02", "Stanze_01"]
    schichten = ["Früh", "Spät", "Nacht"]
    produkte = ["Teil_A", "Teil_B", "Teil_C"]

    data = []
    for _i, date in enumerate(dates):
        # 15% Wahrscheinlichkeit für fehlende Datensätze
        if np.random.random() < 0.85:
            maschine = np.random.choice(maschinen)

            # Problematische Daten einbauen

            # Datum - manchmal in verschiedenen Formaten oder ungültig
            if np.random.random() < 0.05:  # 5% ungültige Daten
                datum_str = np.random.choice(["invalid_date", "", "2024-13-45", "NULL"])
            elif np.random.random() < 0.1:  # 10% verschiedene Formate
                datum_str = date.strftime(
                    np.random.choice(["%d.%m.%Y", "%Y/%m/%d", "%m-%d-%Y"])
                )
            else:
                datum_str = date.strftime("%Y-%m-%d")

            # Maschinennamen - Inkonsistenzen
            if np.random.random() < 0.1:  # 10% Inconsistent naming
                maschine_name = np.random.choice(
                    [
                        f"  {maschine}  ",  # Whitespace
                        maschine.lower(),  # Lowercase
                        maschine.replace("_", "-"),  # Different separators
                        "",  # Empty
                    ]
                )
            else:
                maschine_name = maschine

            # Produktionszeit - Ausreisser und fehlerhafte Werte
            if np.random.random() < 0.05:  # 5% ungültige Werte
                prod_zeit = np.random.choice([-5.0, 25.0, None, "invalid"])
            else:
                prod_zeit = round(np.random.uniform(6, 10), 2)
                # 2% Ausreisser
                if np.random.random() < 0.02:
                    prod_zeit = round(np.random.uniform(15, 20), 2)

            # Temperatur - Sensor-Ausfälle und Ausreisser
            if np.random.random() < 0.08:  # 8% Sensor-Probleme
                temperatur = np.random.choice([None, -999.0, "ERROR", ""])
            else:
                temperatur = round(np.random.uniform(18, 30), 1)
                # 3% Ausreisser (Sensorfehler)
                if np.random.random() < 0.03:
                    temperatur = round(np.random.uniform(60, 80), 1)

            # Stückzahl - manchmal als String oder mit Einheit
            stueckzahl = np.random.randint(50, 200)
            if np.random.random() < 0.05:  # 5% String-Probleme
                stueckzahl = np.random.choice(
                    [
                        f"{stueckzahl} Stück",  # Mit Einheit
                        f"{stueckzahl:,}".replace(",", "."),  # Deutsche Formatierung
                        "",  # Leer
                        "N/A",  # Nicht verfügbar
                    ]
                )

            # Qualität - Inkonsistente Werte
            if np.random.random() < 0.05:  # 5% inkonsistent
                qualitaet = np.random.choice(
                    ["OK", "ok", "Ok", "NOK", "nok", "FEHLER", "Error", ""]
                )
            else:
                qualitaet = np.random.choice(["OK", "NOK"], p=[0.92, 0.08])

            # Schicht - Tippfehler
            if np.random.random() < 0.03:  # 3% Tippfehler
                schicht_wert = np.random.choice(["Fruh", "Spaet", "Nacht_", ""])
            else:
                schicht_wert = np.random.choice(schichten)

            # Bediener - Verschiedene Formate
            bediener_id = np.random.randint(100, 999)
            if np.random.random() < 0.1:  # 10% Format-Inkonsistenzen
                bediener = np.random.choice(
                    [
                        f"BY{bediener_id}",
                        f"by{bediener_id}",
                        f"Bediener {bediener_id}",
                        str(bediener_id),
                        "",
                    ]
                )
            else:
                bediener = f"BY{bediener_id}"

            data.append(
                {
                    "Timestamp": datum_str,
                    "Maschine": maschine_name,
                    "Produktionszeit_h": prod_zeit,
                    "Temperatur_C": temperatur,
                    "Stückzahl": stueckzahl,
                    "Qualität": qualitaet,
                    "Schicht": schicht_wert,
                    "Bediener": bediener,
                    "Produkt": np.random.choice(produkte),
                    "Kommentar": np.random.choice(
                        [
                            "Normal",
                            "Störung Sensor",
                            "",
                            "   ",
                            "Wartung erforderlich",
                            None,
                            "Alles OK",
                        ]
                    ),
                }
            )

    df = pd.DataFrame(data)

    # Einige echte Duplikate hinzufügen
    for _ in range(5):
        random_row = df.sample(1).copy()
        df = pd.concat([df, random_row], ignore_index=True)

    return df


# Problematische Daten erstellen
df_messy = create_messy_production_data()
print(f"✅ Problematische Testdaten erstellt: {len(df_messy)} Datensätze")
print("Erste 5 Zeilen:")
print(df_messy.head())

print("\nDatentypen:")
print(df_messy.dtypes)

# =============================================================================
# AUFGABE 1: Datenqualitäts-Assessment (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 1: Datenqualitäts-Assessment")
print("-" * 40)

print(
    """
TODO: Führen Sie eine umfassende Analyse der Datenqualität durch:

a) Analysieren Sie fehlende Werte pro Spalte
b) Identifizieren Sie Duplikate
c) Prüfen Sie Datentyp-Inkonsistenzen
d) Erstellen Sie ein Datenqualitäts-Dashboard
"""
)

print("a) Fehlende Werte analysieren:")
# IHRE LÖSUNG HIER:
print("Fehlende Werte pro Spalte:")
missing_analysis = df_messy.isnull().sum()
missing_percentage = (df_messy.isnull().sum() / len(df_messy) * 100).round(2)
missing_summary = pd.DataFrame(
    {"Fehlende_Werte": missing_analysis, "Prozent": missing_percentage}
)
print(missing_summary)

# Zusätzlich: Leere Strings als fehlend behandeln
print("\\nLeere Strings und Whitespace:")
empty_strings = {}
for col in df_messy.select_dtypes(include=["object"]).columns:
    empty_count = df_messy[col].astype(str).str.strip().eq("").sum()
    empty_strings[col] = empty_count
empty_df = pd.DataFrame(
    list(empty_strings.items()), columns=["Spalte", "Leere_Strings"]
)
print(empty_df)

print("\\nb) Duplikate identifizieren:")
# IHRE LÖSUNG HIER:
total_duplicates = df_messy.duplicated().sum()
print(f"Exakte Duplikate: {total_duplicates}")

# Duplikate basierend auf Schlüssel-Spalten
key_columns = ["Timestamp", "Maschine", "Schicht"]
key_duplicates = df_messy.duplicated(subset=key_columns).sum()
print(f"Duplikate basierend auf {key_columns}: {key_duplicates}")

if total_duplicates > 0:
    print("\\nBeispiel-Duplikate:")
    duplicate_examples = df_messy[df_messy.duplicated(keep=False)].head()
    print(duplicate_examples[["Timestamp", "Maschine", "Produktionszeit_h"]])

print("\\nc) Datentyp-Inkonsistenzen:")
# IHRE LÖSUNG HIER:
print("Aktuelle Datentypen:")
print(df_messy.dtypes)

# Numerische Spalten prüfen
numeric_columns = ["Produktionszeit_h", "Temperatur_C", "Stückzahl"]
type_issues = {}
for col in numeric_columns:
    if col in df_messy.columns:
        non_numeric = pd.to_numeric(df_messy[col], errors="coerce").isna().sum()
        original_na = df_messy[col].isna().sum()
        type_issues[col] = non_numeric - original_na

print("\\nTyp-Konvertierungsprobleme (nicht-numerische Werte):")
for col, issues in type_issues.items():
    if issues > 0:
        print(f"  {col}: {issues} nicht-numerische Werte")

print("\\nd) Datenqualitäts-Dashboard:")


# IHRE LÖSUNG HIER:
def create_quality_dashboard(df):
    """Erstellt ein umfassendes Datenqualitäts-Dashboard"""
    dashboard = {
        "Datensatz-Info": {
            "Gesamte_Zeilen": len(df),
            "Gesamte_Spalten": len(df.columns),
            "Speicher_MB": df.memory_usage(deep=True).sum() / 1024**2,
        },
        "Vollständigkeit": {
            "Vollständige_Zeilen": len(df.dropna()),
            "Zeilen_mit_Lücken": len(df) - len(df.dropna()),
            "Vollständigkeits_Rate": (len(df.dropna()) / len(df) * 100),
        },
        "Eindeutigkeit": {
            "Exakte_Duplikate": df.duplicated().sum(),
            "Eindeutige_Zeilen": len(df.drop_duplicates()),
        },
        "Konsistenz": {
            "Datentyp_Probleme": sum(type_issues.values()),
            "Leere_Strings": sum(empty_strings.values()),
        },
    }
    return dashboard


quality_dashboard = create_quality_dashboard(df_messy)
print("\\n📊 DATENQUALITÄTS-DASHBOARD:")
for kategorie, metriken in quality_dashboard.items():
    print(f"\\n{kategorie}:")
    for metrik, wert in metriken.items():
        if isinstance(wert, float):
            print(f"  {metrik}: {wert:.2f}")
        else:
            print(f"  {metrik}: {wert:,}")

# Validierung
try:
    assert missing_analysis.sum() > 0, "Sollte fehlende Werte gefunden haben"
    assert "quality_dashboard" in locals(), "Dashboard fehlt"
    print("\\n✅ Aufgabe 1 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 1: {e}")

# =============================================================================
# AUFGABE 2: String-Bereinigung und Normalisierung (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 2: String-Bereinigung und Normalisierung")
print("-" * 40)

print(
    """
TODO: Bereinigen Sie string-basierte Spalten:

a) Bereinigen Sie die 'Maschine'-Spalte (Whitespace, Konsistenz)
b) Normalisieren Sie die 'Qualität'-Spalte
c) Korrigieren Sie die 'Schicht'-Spalte
d) Standardisieren Sie die 'Bediener'-Spalte
"""
)

# Arbeits-DataFrame erstellen
df_clean = df_messy.copy()

print("a) Maschinen-Namen bereinigen:")
# IHRE LÖSUNG HIER:
print("Vorher - Eindeutige Maschinen-Namen:")
print(df_clean["Maschine"].value_counts())

# Whitespace entfernen
df_clean["Maschine"] = df_clean["Maschine"].astype(str).str.strip()

# Leere Strings zu NaN
df_clean["Maschine"] = df_clean["Maschine"].replace("", np.nan)

# Konsistenz: Alles in Titel-Case
df_clean["Maschine"] = df_clean["Maschine"].str.title()

# Trennzeichen normalisieren
df_clean["Maschine"] = df_clean["Maschine"].str.replace("-", "_")

print("\\nNachher - Eindeutige Maschinen-Namen:")
print(df_clean["Maschine"].value_counts())

print("\\nb) Qualität normalisieren:")
# IHRE LÖSUNG HIER:
print("Vorher - Qualitätswerte:")
print(df_clean["Qualität"].value_counts())

# String zu uppercase und trimmen
df_clean["Qualität"] = df_clean["Qualität"].astype(str).str.strip().str.upper()

# Leere Strings und 'NAN' zu echtem NaN
df_clean["Qualität"] = df_clean["Qualität"].replace(["", "NAN"], np.nan)

# Konsistente Werte-Mapping
qualitaets_mapping = {"OK": "OK", "NOK": "NOK", "FEHLER": "NOK", "ERROR": "NOK"}

df_clean["Qualität"] = df_clean["Qualität"].replace(qualitaets_mapping)

# Ungültige Werte als NaN markieren
gültige_qualität = ["OK", "NOK"]
df_clean.loc[~df_clean["Qualität"].isin(gültige_qualität), "Qualität"] = np.nan

print("\\nNachher - Qualitätswerte:")
print(df_clean["Qualität"].value_counts())

print("\\nc) Schicht-Werte korrigieren:")
# IHRE LÖSUNG HIER:
print("Vorher - Schicht-Werte:")
print(df_clean["Schicht"].value_counts())

# Basis-Bereinigung
df_clean["Schicht"] = df_clean["Schicht"].astype(str).str.strip()

# Tippfehler korrigieren
schicht_mapping = {
    "Fruh": "Früh",
    "Früh": "Früh",
    "Spaet": "Spät",
    "Spät": "Spät",
    "Nacht_": "Nacht",
    "Nacht": "Nacht",
}

df_clean["Schicht"] = df_clean["Schicht"].replace(schicht_mapping)

# Leere und ungültige Werte
df_clean["Schicht"] = df_clean["Schicht"].replace(["", "nan"], np.nan)

# Nur gültige Schichten behalten
gültige_schichten = ["Früh", "Spät", "Nacht"]
df_clean.loc[~df_clean["Schicht"].isin(gültige_schichten), "Schicht"] = np.nan

print("\\nNachher - Schicht-Werte:")
print(df_clean["Schicht"].value_counts())

print("\\nd) Bediener-IDs standardisieren:")
# IHRE LÖSUNG HIER:
print("Vorher - Bediener-Formate (erste 10):")
print(df_clean["Bediener"].head(10).tolist())


def standardize_bediener_id(bediener_str):
    """Standardisiert Bediener-IDs zu BY### Format"""
    if pd.isna(bediener_str) or str(bediener_str).strip() == "":
        return np.nan

    # String bereinigen
    clean_str = str(bediener_str).strip().upper()

    # Nur Zahlen extrahieren
    import re

    zahlen = re.findall(r"\d+", clean_str)

    if zahlen:
        # Erste gefundene Zahl verwenden
        nummer = int(zahlen[0])
        return f"BY{nummer:03d}"  # Format: BY001, BY002, etc.
    else:
        return np.nan


df_clean["Bediener"] = df_clean["Bediener"].apply(standardize_bediener_id)

print("\\nNachher - Bediener-Formate (erste 10):")
print(df_clean["Bediener"].head(10).tolist())
print(f"Eindeutige Bediener: {df_clean['Bediener'].nunique()}")

# Validierung
try:
    maschinen_nach_bereinigung = df_clean["Maschine"].nunique()
    qualitaet_werte = df_clean["Qualität"].dropna().unique()
    gültige_qual_check = all(q in ["OK", "NOK"] for q in qualitaet_werte)

    assert (
        maschinen_nach_bereinigung <= 6
    ), "Sollte maximal 6 eindeutige Maschinen haben"
    assert gültige_qual_check, "Qualität sollte nur OK/NOK enthalten"
    print("\\n✅ Aufgabe 2 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 2: {e}")

# =============================================================================
# AUFGABE 3: Numerische Datenbereinigung (25 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 3: Numerische Datenbereinigung")
print("-" * 40)

print(
    """
TODO: Bereinigen Sie numerische Spalten:

a) Konvertieren Sie 'Produktionszeit_h' zu numeric
b) Behandeln Sie Ausreisser in 'Temperatur_C'
c) Bereinigen Sie 'Stückzahl' (String-Probleme)
d) Implementieren Sie geschäftslogik-basierte Validierung
"""
)

print("a) Produktionszeit zu numeric konvertieren:")
# IHRE LÖSUNG HIER:
print("Vorher - Produktionszeit Datentyp und Beispiele:")
print(f"Typ: {df_clean['Produktionszeit_h'].dtype}")
print("Erste 10 Werte:")
print(df_clean["Produktionszeit_h"].head(10).tolist())

# Problematische Werte identifizieren
problematic_prod = df_clean["Produktionszeit_h"].apply(
    lambda x: not (pd.isna(x) or (isinstance(x, int | float) and x >= 0))
)
print(f"\\nProblematische Produktionszeit-Werte: {problematic_prod.sum()}")

# Zu numeric konvertieren
df_clean["Produktionszeit_h"] = pd.to_numeric(
    df_clean["Produktionszeit_h"], errors="coerce"
)

print(f"\\nNachher - Typ: {df_clean['Produktionszeit_h'].dtype}")
print(f"Gültige Werte: {df_clean['Produktionszeit_h'].notna().sum()}")
print(f"NaN-Werte: {df_clean['Produktionszeit_h'].isna().sum()}")

print("\\nb) Temperatur-Ausreisser behandeln:")
# IHRE LÖSUNG HIER:
print("Temperatur-Statistiken vor Bereinigung:")
print(df_clean["Temperatur_C"].describe())

# Zu numeric konvertieren
df_clean["Temperatur_C"] = pd.to_numeric(df_clean["Temperatur_C"], errors="coerce")

# Ausreisser definieren (realistische Temperaturen für Produktion)
temp_min, temp_max = 10, 50  # SmartFactory Produktionsumgebung
temp_outliers = (df_clean["Temperatur_C"] < temp_min) | (
    df_clean["Temperatur_C"] > temp_max
)
print(
    f"\\nTemperatur-Ausreisser (< {temp_min}°C oder > {temp_max}°C): {temp_outliers.sum()}"
)

if temp_outliers.any():
    print("Beispiele für Ausreisser:")
    print(df_clean.loc[temp_outliers, ["Maschine", "Temperatur_C"]].head())

    # Ausreisser zu NaN setzen
    df_clean.loc[temp_outliers, "Temperatur_C"] = np.nan

print("\\nTemperatur-Statistiken nach Bereinigung:")
print(df_clean["Temperatur_C"].describe())

print("\\nc) Stückzahl bereinigen:")
# IHRE LÖSUNG HIER:
print("Stückzahl - Problematische Werte identifizieren:")
print("Beispiele aktueller Werte:")
print(df_clean["Stückzahl"].head(10).tolist())


def clean_stueckzahl(value):
    """Bereinigt Stückzahl-Werte"""
    if pd.isna(value):
        return np.nan

    value_str = str(value).strip()

    # Leer oder 'N/A'
    if value_str in ["", "N/A", "nan"]:
        return np.nan

    # Nur Zahlen extrahieren
    import re

    # Alle Zahlen finden (auch mit deutschen Tausender-Trennzeichen)
    numbers = re.findall(r"\d+", value_str.replace(".", ""))

    if numbers:
        # Erste (längste) Zahl verwenden
        return int("".join(numbers))
    else:
        return np.nan


df_clean["Stückzahl"] = df_clean["Stückzahl"].apply(clean_stueckzahl)

print("\\nNach Bereinigung:")
print(f"Typ: {df_clean['Stückzahl'].dtype}")
print(f"Gültige Werte: {df_clean['Stückzahl'].notna().sum()}")
print("Statistiken:")
print(df_clean["Stückzahl"].describe())

print("\\nd) Geschäftslogik-Validierung:")


# IHRE LÖSUNG HIER:
def validate_business_rules(df):
    """Implementiert SmartFactory-spezifische Geschäftsregeln"""
    validation_errors = []

    # Regel 1: Produktionszeit zwischen 0 und 24 Stunden
    invalid_prod_time = df["Produktionszeit_h"].notna() & (
        (df["Produktionszeit_h"] < 0) | (df["Produktionszeit_h"] > 24)
    )
    if invalid_prod_time.any():
        validation_errors.append(
            f"Produktionszeit außerhalb 0-24h: {invalid_prod_time.sum()}"
        )
        df.loc[invalid_prod_time, "Produktionszeit_h"] = np.nan

    # Regel 2: Stückzahl sollte positiv sein
    invalid_stueckzahl = df["Stückzahl"].notna() & (df["Stückzahl"] <= 0)
    if invalid_stueckzahl.any():
        validation_errors.append(f"Stückzahl <= 0: {invalid_stueckzahl.sum()}")
        df.loc[invalid_stueckzahl, "Stückzahl"] = np.nan

    # Regel 3: Sehr hohe Stückzahlen sind verdächtig (> 1000 pro Messung)
    suspicious_stueckzahl = df["Stückzahl"].notna() & (df["Stückzahl"] > 1000)
    if suspicious_stueckzahl.any():
        validation_errors.append(
            f"Verdächtig hohe Stückzahl >1000: {suspicious_stueckzahl.sum()}"
        )

    # Regel 4: Temperatur sollte bei Laser-Maschinen höher sein
    laser_temp_check = (
        df["Maschine"].str.contains("Laser", na=False)
        & df["Temperatur_C"].notna()
        & (df["Temperatur_C"] < 20)
    )
    if laser_temp_check.any():
        validation_errors.append(
            f"Laser-Temperaturen unter 20°C: {laser_temp_check.sum()}"
        )

    return validation_errors


business_errors = validate_business_rules(df_clean)
print("Geschäftsregeln-Validierung:")
if business_errors:
    for error in business_errors:
        print(f"  ⚠️ {error}")
else:
    print("  ✅ Alle Geschäftsregeln erfüllt")

# Validierung
try:
    assert df_clean["Produktionszeit_h"].dtype in [
        "float64",
        "int64",
    ], "Produktionszeit sollte numerisch sein"
    assert df_clean["Stückzahl"].dtype in [
        "float64",
        "int64",
    ], "Stückzahl sollte numerisch sein"
    print("\\n✅ Aufgabe 3 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 3: {e}")

# =============================================================================
# AUFGABE 4: Datum-Zeit-Bereinigung (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 4: Datum-Zeit-Bereinigung")
print("-" * 40)

print(
    """
TODO: Bereinigen Sie die Timestamp-Spalte:

a) Konvertieren Sie verschiedene Datumsformate
b) Behandeln Sie ungültige Datumswerte
c) Validieren Sie Datumsplausibilität
d) Erstellen Sie abgeleitete Zeitfelder
"""
)

print("a) Verschiedene Datumsformate konvertieren:")
# IHRE LÖSUNG HIER:
print("Beispiele aktueller Timestamp-Werte:")
print(df_clean["Timestamp"].head(10).tolist())


def flexible_date_parser(date_str):
    """Parst Daten in verschiedenen Formaten"""
    if pd.isna(date_str) or str(date_str).strip() == "":
        return np.nan

    date_str = str(date_str).strip()

    # Ungültige Werte abfangen
    if date_str in ["invalid_date", "NULL", "nan"]:
        return np.nan

    # Verschiedene Formate versuchen
    formats = [
        "%Y-%m-%d",  # 2024-01-01
        "%d.%m.%Y",  # 01.01.2024
        "%Y/%m/%d",  # 2024/01/01
        "%m-%d-%Y",  # 01-01-2024
        "%Y-%m-%d %H:%M:%S",  # Mit Zeit
        "%d.%m.%Y %H:%M",  # Deutsche Format mit Zeit
    ]

    for fmt in formats:
        try:
            return pd.to_datetime(date_str, format=fmt)
        except (ValueError, TypeError):
            continue

    # Pandas automatisches Parsing als Fallback
    try:
        return pd.to_datetime(date_str)
    except:
        return np.nan


print("Konvertiere Timestamps...")
df_clean["Timestamp"] = df_clean["Timestamp"].apply(flexible_date_parser)

print(f"Erfolgreich konvertierte Daten: {df_clean['Timestamp'].notna().sum()}")
print(f"Fehlgeschlagene Konvertierungen: {df_clean['Timestamp'].isna().sum()}")

print("\\nb) Ungültige Datumswerte behandeln:")
# IHRE LÖSUNG HIER:
# Datumsbereich-Validierung (nur 2024 Daten erwartet)
valid_date_range = (df_clean["Timestamp"] >= "2024-01-01") & (
    df_clean["Timestamp"] <= "2024-12-31"
)
invalid_dates = df_clean["Timestamp"].notna() & ~valid_date_range

print(f"Daten außerhalb 2024: {invalid_dates.sum()}")
if invalid_dates.any():
    print("Beispiele ungültiger Daten:")
    print(df_clean.loc[invalid_dates, "Timestamp"].head())
    df_clean.loc[invalid_dates, "Timestamp"] = np.nan

print("\\nc) Datumsplausibilität validieren:")
# IHRE LÖSUNG HIER:
# Zukunftsdaten prüfen
heute = pd.Timestamp.now()
zukunft_daten = df_clean["Timestamp"] > heute
print(f"Zukunftsdaten: {zukunft_daten.sum()}")

# Wochenend-Produktionsdaten prüfen (ungewöhnlich für SmartFactory)
weekend_data = df_clean["Timestamp"].dt.weekday >= 5  # Samstag=5, Sonntag=6
weekend_count = weekend_data.sum() if df_clean["Timestamp"].notna().any() else 0
print(f"Wochenend-Produktionsdaten: {weekend_count} (ungewöhnlich)")

print("\\nd) Abgeleitete Zeitfelder erstellen:")
# IHRE LÖSUNG HIER:
# Nur für gültige Timestamps
valid_timestamps = df_clean["Timestamp"].notna()

df_clean["Datum"] = df_clean["Timestamp"].dt.date
df_clean["Stunde"] = df_clean["Timestamp"].dt.hour
df_clean["Wochentag"] = df_clean["Timestamp"].dt.day_name()
df_clean["Kalenderwoche"] = df_clean["Timestamp"].dt.isocalendar().week
df_clean["Quartal"] = df_clean["Timestamp"].dt.quarter


# Schicht-Validierung basierend auf Stunde
def determine_shift_from_hour(hour):
    """Bestimmt Schicht basierend auf Stunde"""
    if pd.isna(hour):
        return np.nan
    if 6 <= hour < 14:
        return "Früh"
    elif 14 <= hour < 22:
        return "Spät"
    else:
        return "Nacht"


df_clean["Schicht_Berechnet"] = df_clean["Stunde"].apply(determine_shift_from_hour)

print("Neue Zeitfelder erstellt:")
time_fields = [
    "Datum",
    "Stunde",
    "Wochentag",
    "Kalenderwoche",
    "Quartal",
    "Schicht_Berechnet",
]
for field in time_fields:
    if field in df_clean.columns:
        valid_count = df_clean[field].notna().sum()
        print(f"  {field}: {valid_count} gültige Werte")

# Schicht-Konsistenz prüfen
if "Schicht_Berechnet" in df_clean.columns and "Schicht" in df_clean.columns:
    beide_verfügbar = (
        df_clean["Schicht"].notna() & df_clean["Schicht_Berechnet"].notna()
    )
    inkonsistenz = beide_verfügbar & (
        df_clean["Schicht"] != df_clean["Schicht_Berechnet"]
    )
    print(f"\\nSchicht-Inkonsistenzen: {inkonsistenz.sum()}")

# Validierung
try:
    assert (
        df_clean["Timestamp"].dtype == "datetime64[ns]"
    ), "Timestamp sollte datetime sein"
    assert "Stunde" in df_clean.columns, "Stunde-Feld sollte erstellt werden"
    print("\\n✅ Aufgabe 4 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 4: {e}")

# =============================================================================
# AUFGABE 5: Duplikate-Bereinigung (10 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 5: Duplikate-Bereinigung")
print("-" * 40)

print(
    """
TODO: Intelligente Duplikate-Behandlung:

a) Identifizieren Sie verschiedene Arten von Duplikaten
b) Implementieren Sie Duplikate-Bereinigungsstrategie
c) Behandeln Sie Quasi-Duplikate (ähnlich, aber nicht identisch)
d) Dokumentieren Sie entfernte Duplikate
"""
)

print("a) Duplikate-Arten identifizieren:")
# IHRE LÖSUNG HIER:
print(f"Datensatz vor Duplikate-Bereinigung: {len(df_clean)} Zeilen")

# 1. Exakte Duplikate
exakte_duplikate = df_clean.duplicated().sum()
print(f"\\nExakte Duplikate: {exakte_duplikate}")

# 2. Duplikate basierend auf Schlüsselfeldern
key_columns = ["Timestamp", "Maschine"]
key_duplikate = df_clean.duplicated(subset=key_columns).sum()
print(f"Duplikate nach Timestamp+Maschine: {key_duplikate}")

# 3. Quasi-Duplikate (ähnliche Zeiten)
# Gruppiere nach Maschine und prüfe auf sehr ähnliche Timestamps
quasi_duplikate_count = 0
if df_clean["Timestamp"].notna().any():
    df_clean_sorted = df_clean.sort_values(["Maschine", "Timestamp"]).reset_index(
        drop=True
    )

    # Zeitdifferenz zur vorherigen Zeile für gleiche Maschine
    df_clean_sorted["Zeit_Diff"] = df_clean_sorted.groupby("Maschine")[
        "Timestamp"
    ].diff()

    # Quasi-Duplikate: Weniger als 1 Minute Abstand bei gleicher Maschine
    quasi_duplikate = df_clean_sorted["Zeit_Diff"] < pd.Timedelta(minutes=1)
    quasi_duplikate_count = quasi_duplikate.sum()

print(f"Quasi-Duplikate (<1min Abstand): {quasi_duplikate_count}")

print("\\nb) Duplikate-Bereinigungsstrategie:")
# IHRE LÖSUNG HIER:
duplikate_log = {
    "exakte_duplikate_entfernt": 0,
    "key_duplikate_entfernt": 0,
    "quasi_duplikate_entfernt": 0,
    "ursprungszeilen": len(df_clean),
}

# Strategie 1: Exakte Duplikate entfernen
if exakte_duplikate > 0:
    df_clean = df_clean.drop_duplicates()
    duplikate_log["exakte_duplikate_entfernt"] = exakte_duplikate
    print(f"✅ {exakte_duplikate} exakte Duplikate entfernt")

# Strategie 2: Key-basierte Duplikate - neuesten Wert behalten
if key_duplikate > 0:
    vorher_count = len(df_clean)
    # Nach Timestamp sortieren und letzten Wert behalten
    df_clean = df_clean.sort_values("Timestamp").drop_duplicates(
        subset=key_columns, keep="last"
    )
    key_entfernt = vorher_count - len(df_clean)
    duplikate_log["key_duplikate_entfernt"] = key_entfernt
    print(f"✅ {key_entfernt} Key-Duplikate entfernt (neuester Wert behalten)")

print(f"\\nNach Standard-Duplikate-Bereinigung: {len(df_clean)} Zeilen")

print("\\nc) Quasi-Duplikate behandeln:")


# IHRE LÖSUNG HIER:
def remove_quasi_duplicates(df, time_window_minutes=1):
    """Entfernt Quasi-Duplikate basierend auf Zeitfenster"""
    if df["Timestamp"].isna().all():
        return df, 0

    df_sorted = df.sort_values(["Maschine", "Timestamp"]).reset_index(drop=True)

    # Markiere Zeilen zum Behalten
    keep_rows = []

    for maschine in df_sorted["Maschine"].dropna().unique():
        maschine_data = df_sorted[df_sorted["Maschine"] == maschine].copy()

        if len(maschine_data) <= 1:
            keep_rows.extend(maschine_data.index.tolist())
            continue

        # Erste Zeile immer behalten
        last_kept_time = None
        for idx, row in maschine_data.iterrows():
            current_time = row["Timestamp"]

            if pd.isna(current_time):
                keep_rows.append(idx)
            elif last_kept_time is None:
                # Erste gültige Zeit
                keep_rows.append(idx)
                last_kept_time = current_time
            else:
                # Prüfe Zeitdifferenz
                time_diff = current_time - last_kept_time
                if time_diff >= pd.Timedelta(minutes=time_window_minutes):
                    keep_rows.append(idx)
                    last_kept_time = current_time
                # Sonst: Quasi-Duplikat, nicht behalten

    df_cleaned = df_sorted.iloc[keep_rows].copy()
    removed_count = len(df_sorted) - len(df_cleaned)

    return df_cleaned, removed_count


df_clean, quasi_entfernt = remove_quasi_duplicates(df_clean)
duplikate_log["quasi_duplikate_entfernt"] = quasi_entfernt
print(f"✅ {quasi_entfernt} Quasi-Duplikate entfernt")

print("\\nd) Duplikate-Dokumentation:")
# IHRE LÖSUNG HIER:
duplikate_log["endzeilen"] = len(df_clean)
duplikate_log["gesamt_entfernt"] = (
    duplikate_log["ursprungszeilen"] - duplikate_log["endzeilen"]
)
duplikate_log["bereinigungs_rate"] = (
    duplikate_log["gesamt_entfernt"] / duplikate_log["ursprungszeilen"] * 100
)

print("\\n📊 DUPLIKATE-BEREINIGUNGSPROTOKOLL:")
print(f"Ursprüngliche Zeilen: {duplikate_log['ursprungszeilen']:,}")
print(f"Exakte Duplikate entfernt: {duplikate_log['exakte_duplikate_entfernt']:,}")
print(f"Key-Duplikate entfernt: {duplikate_log['key_duplikate_entfernt']:,}")
print(f"Quasi-Duplikate entfernt: {duplikate_log['quasi_duplikate_entfernt']:,}")
print(f"Zeilen nach Bereinigung: {duplikate_log['endzeilen']:,}")
print(f"Gesamt entfernt: {duplikate_log['gesamt_entfernt']:,}")
print(f"Bereinigungsrate: {duplikate_log['bereinigungs_rate']:.2f}%")

# Validierung
try:
    assert len(df_clean) < len(df_messy), "Sollte Duplikate entfernt haben"
    assert duplikate_log["gesamt_entfernt"] > 0, "Sollte Duplikate dokumentiert haben"
    print("\\n✅ Aufgabe 5 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 5: {e}")

# =============================================================================
# AUFGABE 6: Fehlende Werte intelligent behandeln (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 6: Fehlende Werte intelligent behandeln")
print("-" * 40)

print(
    """
TODO: Implementieren Sie verschiedene Strategien für fehlende Werte:

a) Forward/Backward Fill für Maschinendaten
b) Median/Mean Imputation für numerische Werte
c) Mode Imputation für kategorische Werte
d) Erstellen Sie Imputation-Protokoll
"""
)

print("a) Forward/Backward Fill für Maschinendaten:")
# IHRE LÖSUNG HIER:
print("Fehlende Werte vor Imputation:")
missing_before = df_clean.isnull().sum()
print(missing_before)

# Maschinen-Namen: Forward Fill (letzter bekannter Wert)
maschine_missing_before = df_clean["Maschine"].isna().sum()
if maschine_missing_before > 0:
    df_clean["Maschine"] = df_clean["Maschine"].fillna(method="ffill")
    maschine_missing_after = df_clean["Maschine"].isna().sum()
    print(
        f"\\nMaschine Forward Fill: {maschine_missing_before} → {maschine_missing_after}"
    )

# Produkt: Auch Forward Fill
if "Produkt" in df_clean.columns:
    produkt_missing_before = df_clean["Produkt"].isna().sum()
    if produkt_missing_before > 0:
        df_clean["Produkt"] = df_clean["Produkt"].fillna(method="ffill")
        print(
            f"Produkt Forward Fill: {produkt_missing_before} → {df_clean['Produkt'].isna().sum()}"
        )

print("\\nb) Median/Mean Imputation für numerische Werte:")
# IHRE LÖSUNG HIER:
numeric_columns = ["Produktionszeit_h", "Temperatur_C", "Stückzahl"]
imputation_log = {}

for col in numeric_columns:
    if col in df_clean.columns:
        missing_count = df_clean[col].isna().sum()
        if missing_count > 0:
            # Strategie basierend auf Datenverteilung wählen
            if col == "Produktionszeit_h":
                # Median für Produktionszeit (robuster gegen Ausreisser)
                fill_value = df_clean[col].median()
                strategy = "median"
            elif col == "Temperatur_C":
                # Mean für Temperatur (normalverteilte Daten)
                fill_value = df_clean[col].mean()
                strategy = "mean"
            else:  # Stückzahl
                # Median für Stückzahl (robuster)
                fill_value = df_clean[col].median()
                strategy = "median"

            df_clean[col] = df_clean[col].fillna(fill_value)
            imputation_log[col] = {
                "missing_count": missing_count,
                "fill_value": fill_value,
                "strategy": strategy,
            }
            print(
                f"{col}: {missing_count} Werte mit {strategy} ({fill_value:.2f}) gefüllt"
            )

print("\\nc) Mode Imputation für kategorische Werte:")
# IHRE LÖSUNG HIER:
categorical_columns = ["Qualität", "Schicht", "Bediener"]

for col in categorical_columns:
    if col in df_clean.columns:
        missing_count = df_clean[col].isna().sum()
        if missing_count > 0:
            mode_value = df_clean[col].mode()
            if len(mode_value) > 0:
                fill_value = mode_value[0]
                df_clean[col] = df_clean[col].fillna(fill_value)
                imputation_log[col] = {
                    "missing_count": missing_count,
                    "fill_value": fill_value,
                    "strategy": "mode",
                }
                print(f"{col}: {missing_count} Werte mit Mode ('{fill_value}') gefüllt")

# Spezialfall: Kommentare
if "Kommentar" in df_clean.columns:
    kommentar_missing = df_clean["Kommentar"].isna().sum()
    if kommentar_missing > 0:
        df_clean["Kommentar"] = df_clean["Kommentar"].fillna("Kein Kommentar")
        print(f"Kommentar: {kommentar_missing} Werte mit 'Kein Kommentar' gefüllt")

print("\\nd) Imputation-Protokoll erstellen:")
# IHRE LÖSUNG HIER:
missing_after = df_clean.isnull().sum()

print("\\n📊 IMPUTATION-PROTOKOLL:")
print(f"{'Spalte':<20} {'Vorher':<8} {'Nachher':<8} {'Strategie':<10} {'Wert':<15}")
print("-" * 70)

for col in df_clean.columns:
    before_count = missing_before.get(col, 0)
    after_count = missing_after.get(col, 0)

    if col in imputation_log:
        strategy = imputation_log[col]["strategy"]
        fill_value = str(imputation_log[col]["fill_value"])[:13]
    else:
        strategy = "keine" if before_count == after_count else "manual"
        fill_value = "-"

    if before_count > 0 or after_count > 0:
        print(
            f"{col:<20} {before_count:<8} {after_count:<8} {strategy:<10} {fill_value:<15}"
        )

total_missing_before = missing_before.sum()
total_missing_after = missing_after.sum()
imputation_success_rate = (
    (total_missing_before - total_missing_after) / total_missing_before * 100
    if total_missing_before > 0
    else 100
)

print("\\nZusammenfassung:")
print(f"Fehlende Werte vorher: {total_missing_before:,}")
print(f"Fehlende Werte nachher: {total_missing_after:,}")
print(f"Imputation Erfolgsrate: {imputation_success_rate:.2f}%")

# Validierung
try:
    assert (
        total_missing_after < total_missing_before
    ), "Sollte fehlende Werte reduziert haben"
    assert len(imputation_log) > 0, "Sollte Imputationen dokumentiert haben"
    print("\\n✅ Aufgabe 6 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 6: {e}")

# =============================================================================
# ZUSAMMENFASSUNG UND FINAL-VALIDIERUNG
# =============================================================================

print("\n" + "=" * 60)
print("🎯 ÜBUNG 3 ABGESCHLOSSEN - FINAL-VALIDIERUNG")
print("=" * 60)

# Finale Datenqualitäts-Bewertung
final_quality = create_quality_dashboard(df_clean)
print("\\n📊 FINALE DATENQUALITÄT:")
final_quality_score = print_validation_report(
    {
        "dataset": "Bereinigte Daten",
        "timestamp": datetime.now(),
        "total_records": final_quality["Datensatz-Info"]["Gesamte_Zeilen"],
        "errors": [],
        "warnings": [],
        "info": [
            f"Vollständigkeitsrate: {final_quality['Vollständigkeit']['Vollständigkeits_Rate']:.2f}%",
            f"Eindeutige Zeilen: {final_quality['Eindeutigkeit']['Eindeutige_Zeilen']:,}",
            f"Speicherverbrauch: {final_quality['Datensatz-Info']['Speicher_MB']:.2f} MB",
        ],
    }
)

# Bereinigungszusammenfassung
print("\\n📈 BEREINIGUNGSZUSAMMENFASSUNG:")
print(f"{'Metrik':<30} {'Vorher':<15} {'Nachher':<15} {'Verbesserung':<15}")
print("-" * 75)

metrics = [
    ("Datensätze", len(df_messy), len(df_clean)),
    ("Fehlende Werte", missing_before.sum(), missing_after.sum()),
    ("Duplikate", df_messy.duplicated().sum(), df_clean.duplicated().sum()),
    ("Vollständige Zeilen", len(df_messy.dropna()), len(df_clean.dropna())),
]

for metric, before, after in metrics:
    if before > 0:
        improvement = f"{((before - after) / before * 100):+.1f}%"
    else:
        improvement = "N/A"

    print(f"{metric:<30} {before:<15,} {after:<15,} {improvement:<15}")

print("\\n✅ LERNZIELE ERREICHT:")
print("• Datenqualitätsprobleme systematisch identifiziert")
print("• String-Bereinigung und -Normalisierung implementiert")
print("• Numerische Ausreisser erkannt und behandelt")
print("• Datum-Zeit-Daten flexibel konvertiert")
print("• Intelligente Duplikate-Bereinigung durchgeführt")
print("• Verschiedene Imputation-Strategien angewendet")
print("• Umfassendes Bereinigungsprotokoll erstellt")

print("\\n🎓 NÄCHSTE SCHRITTE:")
print("• Übung 4: Erweiterte Datenanalyse und Aggregationen")
print("• Automatisierte Bereinigungspipelines entwickeln")
print("• Machine Learning für Anomalie-Erkennung")
print("• Real-time Datenqualitäts-Monitoring")

# Bereinigte Daten exportieren
export_filename = "uebung_03_bereinigte_daten.csv"
df_clean.to_csv(export_filename, index=False, encoding="utf-8")

# Bereinigungsprotokoll als JSON
bereinigungsprotokoll = {
    "bereinigung_timestamp": datetime.now().isoformat(),
    "ursprungsdaten": {
        "zeilen": len(df_messy),
        "fehlende_werte": int(missing_before.sum()),
        "duplikate": int(df_messy.duplicated().sum()),
    },
    "bereinigte_daten": {
        "zeilen": len(df_clean),
        "fehlende_werte": int(missing_after.sum()),
        "duplikate": int(df_clean.duplicated().sum()),
    },
    "duplikate_log": duplikate_log,
    "imputation_log": {
        k: {
            kk: (float(vv) if isinstance(vv, int | float) else str(vv))
            for kk, vv in v.items()
        }
        for k, v in imputation_log.items()
    },
    "qualitaets_score": float(final_quality_score),
}

import json

with open("uebung_03_bereinigungsprotokoll.json", "w", encoding="utf-8") as f:
    json.dump(bereinigungsprotokoll, f, indent=2, ensure_ascii=False)

print("\\n💾 Ergebnisse exportiert:")
print(f"• Bereinigte Daten: {export_filename}")
print("• Bereinigungsprotokoll: uebung_03_bereinigungsprotokoll.json")

print("\\n💡 Als SmartFactory-Entwickler beherrschen Sie jetzt")
print("   professionelle Datenbereinigung für Produktionsdaten!")
