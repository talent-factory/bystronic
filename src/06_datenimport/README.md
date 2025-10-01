# 📊 Modul 06: Datenimport und -export

## Python Grundkurs für SmartFactory-Entwickler - Modul 06

______________________________________________________________________

## 🎯 Übersicht

Dieses Modul behandelt den professionellen Import und Export von Daten in
verschiedenen Formaten, mit speziellem Fokus auf industrielle Anwendungen bei
SmartFactory. Von einfachen CSV-Dateien bis zu komplexen IoT-Sensordaten und
APIs - hier lernen Sie alle wichtigen Techniken für die Datenverarbeitung.

## 📚 Lernziele

Nach diesem Modul können Sie:

- **CSV-Dateien mit komplexen Strukturen** importieren und verarbeiten
- **Excel-Dateien mit mehreren Arbeitsblättern** effizient handhaben
- **JSON-Daten aus Dateien und APIs** laden und normalisieren
- **Datenqualität systematisch prüfen** und verbessern
- **Daten in verschiedenen Formaten exportieren** und dokumentieren
- **Produktions-taugliche Pipelines** für die Datenverarbeitung erstellen

## 📋 Modulstruktur

```text
src/06_datenimport/
├── README.md                           # Diese Datei - Übersicht und Dokumentation
├── datenimport_tutorial.ipynb          # Interaktives Jupyter Tutorial
├── beispiele/                          # Praxisnahe Implementierungsbeispiele
│   ├── csv_import_grundlagen.py        # CSV-Import: Trennzeichen, Encoding, Performance
│   ├── smartfactory_csv_parser.py         # Spezieller Parser für SmartFactory CSV-Strukturen
│   └── excel_verarbeitung.py           # Excel: Multi-Sheet, KPIs, Formatierung
└── uebungen/                           # Interaktive Übungen mit Lösungen
    └── uebung_01_csv_basics.py         # CSV-Import Grundlagen (⭐⭐☆☆)
```

## 🚀 Schnellstart

### 1. Basis-Setup

```python
import pandas as pd
import numpy as np
from pathlib import Path

# Konfiguration für bessere Darstellung
pd.set_option('display.max_columns', 20)
pd.set_option('display.max_rows', 10)
```

### 2. Einfacher CSV-Import

```python
# Standard CSV
df = pd.read_csv('datei.csv')

# Mit spezifischen Parametern
df = pd.read_csv('datei.csv',
                sep=';',           # Semikolon-getrennt
                decimal=',',       # Deutsches Dezimalformat
                encoding='utf-8',  # Encoding explizit
                parse_dates=['Datum'])  # Datum-Spalten automatisch konvertieren
```

### 3. SmartFactory CSV-Parser verwenden

```python
from src.datenimport.beispiele.smartfactory_csv_parser import SmartFactoryCSVParser

parser = SmartFactoryCSVParser()
result = parser.parse_complex_csv('V084_Scope.csv')

df = result['dataframe']
metadata = result['metadata']
```

### 4. Excel Multi-Sheet Verarbeitung

```python
# Alle Arbeitsblätter laden
excel_data = pd.read_excel('smartfactory_data.xlsx', sheet_name=None)

# Spezifische Sheets
production_df = pd.read_excel('data.xlsx', sheet_name='Produktion')
```

### 5. JSON-Daten normalisieren

```python
import json

# JSON laden
with open('sensor_data.json', 'r') as f:
    data = json.load(f)

# Zu DataFrame normalisieren
df = pd.json_normalize(data['sensors'],
                      record_path='readings',
                      meta=['id', 'type'])
```

## 🔧 Beispiele im Detail

### CSV-Import mit Problembehandlung

**Automatische Trennzeichen-Erkennung:**

```python
from src.datenimport.beispiele.csv_import_grundlagen import csv_import_beispiele

# Führt alle CSV-Import-Szenarien aus
dataframes = csv_import_beispiele()

# Zugriff auf verschiedene Formate
df_standard = dataframes['standard']    # Komma-getrennt
df_german = dataframes['semicolon']     # Semikolon, deutsche Zahlen
df_tab = dataframes['tab']              # Tab-getrennt
```

**Encoding-Probleme lösen:**

```python
from src.datenimport.beispiele.csv_import_grundlagen import csv_probleme_loesen

# Behandelt automatisch:
# - Fehlende Werte
# - Gemischte Trennzeichen
# - Encoding-Probleme (UTF-8, Latin-1, CP1252)
csv_probleme_loesen()
```

### SmartFactory CSV-Parser für komplexe Strukturen

**V084_Scope.csv Format:**

```text
Zeile 1-6:    Metadaten (Name, File, Timestamps)
Zeile 7:      Header mit "Name\tSpalte1\tName\tSpalte2..."
Zeile 8-21:   Zusätzliche Metadaten (Data-Type, etc.)
Zeile 22+:    Messdaten
```

**Parser verwenden:**

```python
from src.datenimport.beispiele.smartfactory_csv_parser import SmartFactoryCSVParser

parser = SmartFactoryCSVParser()

# Automatische Struktur-Erkennung
result = parser.parse_complex_csv('data/large/V084_Scope.csv')

# Manuelle Konfiguration
result = parser.parse_complex_csv('V084_Scope.csv',
                                 header_line=7,      # Zeile 7 für Header
                                 data_start_line=22) # Zeile 22 für Daten

df = result['dataframe']        # Parsed DataFrame
metadata = result['metadata']   # Extrahierte Metadaten
info = result['parsing_info']   # Parsing-Details
```

### Excel-Verarbeitung mit KPIs

```python
from src.datenimport.beispiele.excel_verarbeitung import SmartFactoryExcelHandler

handler = SmartFactoryExcelHandler()

# Umfassender Daten-Import
excel_data = handler.load_comprehensive_data()

# KPI-Berechnungen für Produktionsdaten
production_df = excel_data['Produktion']
kpis = handler.calculate_production_kpis(production_df)

print(f"Gesamtproduktion: {kpis['total_production']:,}")
print(f"Durchschnittliche Verfügbarkeit: {kpis['avg_availability']:.1f}%")
```

### Datenbereinigung und -validierung

```python
def clean_production_data(df):
    """Umfassende Bereinigung von Produktionsdaten"""
    df_clean = df.copy()

    # 1. Duplikate entfernen
    df_clean = df_clean.drop_duplicates()

    # 2. Unrealistische Werte korrigieren
    df_clean.loc[df_clean['Produktion'] < 0, 'Produktion'] = 0
    df_clean.loc[df_clean['Verfügbarkeit'] > 100, 'Verfügbarkeit'] = 100

    # 3. Extreme Temperaturen behandeln
    extreme_temp = (df_clean['Temperatur'] < -50) | (df_clean['Temperatur'] > 200)
    df_clean.loc[extreme_temp, 'Temperatur'] = np.nan

    # 4. Fehlende Werte mit sinnvollen Defaults ersetzen
    numeric_cols = df_clean.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if col == 'Produktion':
            df_clean[col].fillna(df_clean[col].median(), inplace=True)
        elif col == 'Temperatur':
            df_clean[col].fillna(df_clean[col].mean(), inplace=True)

    return df_clean
```

### Multi-Format Export

```python
def export_comprehensive(df, base_name, formats=['csv', 'excel', 'json']):
    """Exportiert DataFrame in verschiedene Formate mit Metadaten"""
    exported_files = []

    # CSV Export
    if 'csv' in formats:
        csv_file = f"{base_name}.csv"
        df.to_csv(csv_file, index=False, encoding='utf-8')
        exported_files.append(csv_file)

    # Excel Export mit Statistiken
    if 'excel' in formats:
        excel_file = f"{base_name}.xlsx"
        with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
            df.to_excel(writer, sheet_name='Daten', index=False)
            df.describe().to_excel(writer, sheet_name='Statistiken')
        exported_files.append(excel_file)

    # JSON Export mit Metadaten
    if 'json' in formats:
        json_file = f"{base_name}.json"
        export_data = {
            'metadata': {
                'exported_at': pd.Timestamp.now().isoformat(),
                'rows': len(df),
                'columns': len(df.columns)
            },
            'data': df.to_dict('records')
        }

        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, default=str, ensure_ascii=False)
        exported_files.append(json_file)

    return exported_files
```

## 📊 Interaktive Übungen

### Übung 1: CSV-Import Grundlagen (⭐⭐☆☆)

```python
# Ausführen der Übung
from src.datenimport.uebungen.uebung_01_csv_basics import main

main()  # Startet interaktive Übungen mit 5 Aufgaben
```

**Übungsinhalt:**

1. **Grundlegender CSV-Import** - Standard-Dateien laden
1. **Verschiedene Trennzeichen** - Komma, Semikolon, Tab
1. **Fehlende Werte behandeln** - dropna(), fillna() Strategien
1. **Datenvalidierung** - Unrealistische Werte erkennen und korrigieren
1. **Visualisierung** - Analysierte Daten grafisch darstellen

## 🔍 Performance-Tipps

### Für große Dateien (>100MB)

```python
# Chunked Reading
chunk_size = 10000
chunks = []

for chunk in pd.read_csv('large_file.csv', chunksize=chunk_size):
    processed_chunk = chunk[chunk['Status'] == 'OK']  # Filterung pro Chunk
    chunks.append(processed_chunk)

df = pd.concat(chunks, ignore_index=True)
```

### Datentyp-Optimierung

```python
dtypes = {
    'ID': 'int32',           # Statt int64
    'Kategorie': 'category',  # Für wiederkehrende Strings
    'Wert': 'float32',       # Statt float64
    'Status': 'category'
}

df = pd.read_csv('data.csv', dtype=dtypes)

# Speicher-Einsparung prüfen
memory_mb = df.memory_usage(deep=True).sum() / 1024**2
print(f"Memory Usage: {memory_mb:.1f} MB")
```

## 🛡️ Fehlerbehandlung

### Robuster CSV-Import

```python
def safe_csv_import(file_path):
    """Sicherer CSV-Import mit Fallback-Strategien"""
    encodings = ['utf-8', 'latin-1', 'cp1252']
    separators = [',', ';', '\t']

    for encoding in encodings:
        for sep in separators:
            try:
                df = pd.read_csv(file_path, encoding=encoding, sep=sep)
                if len(df) > 0 and len(df.columns) > 1:
                    print(f"✅ Erfolgreich: encoding={encoding}, sep='{sep}'")
                    return df
            except Exception:
                continue

    raise ValueError(f"❌ Konnte Datei nicht laden: {file_path}")
```

### Datenvalidierung

```python
def validate_industrial_data(df):
    """Validiert Industriedaten auf Plausibilität"""
    issues = []

    # Negative Produktionswerte
    if 'Produktion' in df.columns and (df['Produktion'] < 0).any():
        issues.append("Negative Produktionswerte gefunden")

    # Unrealistische Temperaturen
    if 'Temperatur' in df.columns:
        temp_range = df['Temperatur'].dropna()
        if len(temp_range) > 0 and (temp_range.min() < -50 or temp_range.max() > 200):
            issues.append("Unrealistische Temperaturwerte")

    # Verfügbarkeit außerhalb 0-100%
    if 'Verfügbarkeit' in df.columns:
        avail_range = df['Verfügbarkeit'].dropna()
        if len(avail_range) > 0 and (avail_range.min() < 0 or avail_range.max() > 100):
            issues.append("Verfügbarkeit außerhalb gültigen Bereichs")

    return issues
```

## 🧪 Tests ausführen

```bash
# Alle Tests für Modul 06
pytest tests/test_06_datenimport.py -v

# Nur CSV-Parser Tests
pytest tests/test_06_datenimport.py::TestSmartFactoryCSVParser -v

# Mit Coverage-Report
pytest tests/test_06_datenimport.py --cov=src.datenimport --cov-report=html
```

## 📈 Praxisbeispiele

### Komplette Datenverarbeitungs-Pipeline

```python
def smartfactory_data_pipeline(input_file, output_dir):
    """Vollständige Pipeline für SmartFactory-Datenverarbeitung"""

    # 1. Import mit speziellem Parser
    parser = SmartFactoryCSVParser()
    result = parser.parse_complex_csv(input_file)
    df_raw = result['dataframe']

    # 2. Datenqualität prüfen
    quality_issues = validate_industrial_data(df_raw)
    if quality_issues:
        print(f"⚠️ Qualitätsprobleme: {quality_issues}")

    # 3. Daten bereinigen
    df_clean = clean_production_data(df_raw)

    # 4. KPIs berechnen
    kpis = calculate_production_kpis(df_clean)

    # 5. Ergebnisse exportieren
    base_name = Path(output_dir) / "processed_data"
    exported_files = export_comprehensive(df_clean, base_name)

    # 6. Bericht generieren
    report = {
        'input_file': input_file,
        'processed_rows': len(df_clean),
        'quality_issues': quality_issues,
        'kpis': kpis,
        'exported_files': exported_files
    }

    return report

# Verwendung
report = smartfactory_data_pipeline('data/large/V084_Scope.csv', 'output/')
print(f"✅ Pipeline abgeschlossen: {report['processed_rows']:,} Zeilen verarbeitet")
```

## 📚 Weiterführende Ressourcen

### Offizielle Dokumentation

- [Pandas I/O Documentation](https://pandas.pydata.org/docs/user_guide/io.html)
- [NumPy Data Types](https://numpy.org/doc/stable/user/basics.types.html)
- [JSON Documentation](https://docs.python.org/3/library/json.html)
- [Requests Library](https://requests.readthedocs.io/)

### Performance & Best Practices

- [Pandas Performance Tips](https://pandas.pydata.org/docs/user_guide/enhancingperf.html)
- [Memory Usage Optimization](https://pandas.pydata.org/docs/user_guide/scale.html)
- [Data Validation Patterns](https://pandas.pydata.org/docs/user_guide/missing_data.html)

### Industrielle Datenverarbeitung

- [Time Series Analysis](https://pandas.pydata.org/docs/user_guide/timeseries.html)
- [Working with Large Datasets](https://pandas.pydata.org/docs/user_guide/scale.html)
- [Data Quality Assessment](https://github.com/pandas-profiling/pandas-profiling)

## 🎯 Nächste Schritte

Nach erfolgreichem Abschluss dieses Moduls sind Sie bereit für:

- **Modul 07**: Jupyter Notebooks für interaktive Datenanalyse
- **Modul 08**: GUI-Entwicklung mit PyQt/PySide und Streamlit
- **Modul 09**: Vollständige Praxisprojekte mit echter Datenverarbeitung

______________________________________________________________________

**Viel Erfolg beim Datenimport und -export!** 🚀

*Dieses Modul ist Teil des Python-Grundkurses für SmartFactory-Entwickler*
