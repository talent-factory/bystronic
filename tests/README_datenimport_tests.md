# 📊 Tests für Modul 06: Datenimport und -export

## 🎯 Übersicht

Diese Test-Suite überprüft alle Funktionalitäten des Datenimport-Moduls (Modul 06) des Python Grundkurses für Bystronic-Entwickler. Die Tests decken CSV-Import mit komplexen Strukturen, Excel-Verarbeitung, JSON-Datenverarbeitung, Datenbereinigung und Export-Funktionen ab.

## 📋 Test-Kategorien

### 1. CSV-Import Tests (`TestCSVImportGrundlagen`)

**Zweck**: Überprüfung der grundlegenden CSV-Import-Funktionalitäten

**Getestete Funktionen**:

- `csv_import_beispiele()` - Grundlegende CSV-Import-Szenarien
- Verschiedene Trennzeichen (Komma, Semikolon, Tab)
- Encoding-Behandlung (UTF-8, Latin-1)
- Fehlende Werte und deren Behandlung
- Performance-Optimierungen (Chunked Reading, Datentyp-Optimierung)

**Wichtige Tests**:

```python
def test_csv_import_beispiele(self):
    """Test der grundlegenden CSV-Import-Beispiele"""
    # Testet Standard-, Semikolon- und Tab-getrennte CSV-Dateien
    # Überprüft korrekte DataFrame-Erstellung und Datentypen

def test_csv_trennzeichen_verarbeitung(self):
    """Test verschiedener CSV-Trennzeichen"""
    # Stellt sicher, dass verschiedene Trennzeichen korrekt verarbeitet werden

def test_csv_fehlende_werte(self):
    """Test der Behandlung fehlender Werte"""
    # Überprüft verschiedene Strategien: dropna(), fillna() mit mean/median
```

### 2. Bystronic CSV Parser Tests (`TestBystronicCSVParser`)

**Zweck**: Spezielle Tests für den industriellen Bystronic CSV Parser

**Getestete Funktionen**:

- `BystronicCSVParser` - Klasse für komplexe CSV-Strukturen
- Automatische Struktur-Erkennung
- Metadaten-Extraktion
- Datenvalidierung
- Fehlerbehandlung

**Mock-Daten Struktur**:

```
Zeile 1-4: Metadaten (Name, File, Timestamps)
Zeile 7: Header mit alternierenden "Name" und Spaltennamen
Zeile 8-21: Zusätzliche Metadaten (SymbolComment, Data-Type, etc.)
Zeile 22+: Messdaten
```

**Wichtige Tests**:

```python
def test_detect_structure(self):
    """Test der Struktur-Erkennung"""
    # Erkennt automatisch Header-Zeile und Datenstart

def test_parse_complex_csv(self):
    """Test des kompletten CSV-Parsing"""
    # Vollständiger Parse-Workflow mit realistischen Daten

def test_data_validation(self):
    """Test der Datenvalidierung"""
    # Behandlung von extremen Werten und unrealistischen Daten
```

### 3. Excel-Verarbeitung Tests (`TestExcelVerarbeitung`)

**Zweck**: Tests für Excel-Import/Export mit mehreren Arbeitsblättern

**Getestete Funktionen**:

- Bystronic_Maschinen_Export_2024.csvsende Excel-Verarbeitung
- Multi-Sheet Loading
- KPI-Berechnungen
- Excel-Export mit Formatierung

**Test-Excel-Struktur**:

- **Produktion**: Datum, Maschinen-Daten, Verfügbarkeit
- **Qualität**: Monatliche Qualitätskennzahlen

**Wichtige Tests**:

```python
def test_excel_multi_sheet_loading(self):
    """Test des Ladens mehrerer Arbeitsblätter"""
    # Lädt alle Sheets gleichzeitig und prüft Struktur

def test_excel_kpi_calculation(self):
    """Test der KPI-Berechnungen"""
    # Berechnet Produktions-KPIs: Gesamtproduktion, Verfügbarkeit, etc.
```

### 4. JSON-Verarbeitung Tests (`TestJSONVerarbeitung`)

**Zweck**: Tests für IoT-Sensordaten und API-Integration

**Getestete Funktionen**:

- JSON-Loading und -Parsing
- Normalisierung hierarchischer Strukturen
- pandas `json_normalize` Integration
- JSON-Export with Metadaten

**Test-JSON-Struktur**:

```json
{
  "metadata": {
    "system": "Bystronic IoT Platform",
    "timestamp": "2024-01-15T08:30:00Z"
  },
  "sensors": [
    {
      "id": "TEMP_001",
      "type": "temperature",
      "readings": [...]
    }
  ]
}
```

**Wichtige Tests**:

```python
def test_json_normalization(self):
    """Test der JSON-Normalisierung zu DataFrame"""
    # Konvertiert hierarchische JSON-Daten zu flacher Tabellenstruktur

def test_json_pandas_normalization(self):
    """Test der pandas json_normalize Funktionalität"""
    # Nutzt pandas-eigene Normalisierungsfunktionen
```

### 5. Datenbereinigung Tests (`TestDatenbereinigung`)

**Zweck**: Validation und Cleaning von industriellen Daten

**Getestete Szenarien**:

- Fehlende Werte (NaN, leere Strings)
- Unrealistische Werte (negative Produktionszahlen, extreme Temperaturen)
- Ausreißer-Erkennung (IQR-Methode)
- Duplikat-Entfernung
- Datentyp-Optimierung für Memory-Effizienz

**Problematische Test-Daten**:

```python
{
    'Produktion': [1000, -50, 1200, np.nan, 2000],    # Negative Werte, NaN
    'Temperatur': [22.5, 150.0, 23.1, 22.8, -999],   # Unrealistische Werte
    'Verfügbarkeit': [85.2, 120.0, 88.5, 92.1, -10], # >100%, negative Werte
}
```

**Wichtige Tests**:

```python
def test_outlier_detection(self):
    """Test der Ausreißer-Erkennung"""
    # IQR-Methode: Q3 + 1.5*IQR als obere Grenze

def test_data_cleaning(self):
    """Test der Datenbereinigung"""
    # Systematische Bereinigung aller Problemkategorien

def test_data_type_optimization(self):
    """Test der Datentyp-Optimierung"""
    # Memory-Optimierung durch category, int32, float32
```

### 6. Export-Funktionen Tests (`TestExportFunktionen`)

**Zweck**: Tests für verschiedene Export-Formate und -Strategien

**Getestete Formate**:

- **CSV**: UTF-8 Encoding, verschiedene Separatoren
- **Excel**: Multi-Sheet Export mit Metadaten
- **JSON**: Mit Metadaten und strukturierten Informationen
- **Parquet**: Komprimierung und Performance (optional)

**Wichtige Tests**:

```python
def test_excel_export_multi_sheet(self):
    """Test des Excel-Exports mit mehreren Blättern"""
    # Daten + Statistiken + Aggregationen in separaten Sheets

def test_json_export_with_metadata(self):
    """Test des JSON-Exports mit Metadaten"""
    # Vollständiger Export mit Metadaten, Spalteninfo und Daten

def test_multi_format_export(self):
    """Test des Exports in mehreren Formaten gleichzeitig"""
    # Pipeline für gleichzeitigen Export in verschiedene Formate
```

### 7. Integration Tests (`TestIntegration`)

**Zweck**: End-to-End Tests der kompletten Datenverarbeitungs-Pipeline

**Pipeline-Schritte**:

1. **Daten-Import**: CSV mit komplexen Strukturen
2. **Datenbereinigung**: NaN-Behandlung, Duplikate entfernen
3. **Aggregation**: Maschinenbezogene Statistiken
4. **Export**: CSV + JSON mit Metadaten
5. **Verification**: Vollständigkeitsprüfung

**Wichtiger Test**:

```python
def test_complete_pipeline(self):
    """Test einer kompletten Datenverarbeitungs-Pipeline"""
    # Kompletter Workflow: Import → Clean → Aggregate → Export → Verify
```

## 🚀 Test-Ausführung

### Alle Tests ausführen

```bash
# Komplette Test-Suite
pytest tests/test_06_datenimport.py -v

# Nur CSV-Tests
pytest tests/test_06_datenimport.py::TestCSVImportGrundlagen -v

# Mit Coverage-Report
pytest tests/test_06_datenimport.py --cov=src.datenimport --cov-report=html
```

### Spezifische Test-Kategorien

```bash
# Nur Parser-Tests
pytest tests/test_06_datenimport.py::TestBystronicCSVParser -v

# Nur Integration-Tests
pytest tests/test_06_datenimport.py::TestIntegration -v

# Mit detaillierter Ausgabe
pytest tests/test_06_datenimport.py -v --tb=long -s
```

## 🔧 Test-Konfiguration

### Fixtures und Setup

- **Temporäre Verzeichnisse**: Jeder Test verwendet eigene temp-Directories
- **Mock-Daten**: Realistische Bystronic-Datenstrukturen
- **Automatisches Cleanup**: Temp-Files werden nach Tests entfernt

### Abhängigkeiten

```python
# Erforderliche Packages
import pandas as pd
import numpy as np
import pytest
import tempfile
from pathlib import Path
from unittest.mock import patch, mock_open

# Optional (für Parquet-Tests)
import pyarrow as pa  # Wird graceful gehandhabt wenn nicht verfügbar
```

## 📊 Test-Daten

### CSV-Test-Strukturen

1. **Standard CSV**: Komma-getrennt, UTF-8
2. **Deutsches Format**: Semikolon-getrennt, Komma als Dezimaltrenner
3. **Tab-Format**: Tab-getrennt, für technische Daten
4. **Problematische Daten**: Fehlende Werte, Encoding-Probleme

### Bystronic CSV Spezial-Format

```
Name    Distance Control
File    O:\Messungen\Test.csv
Name    TEMP_001    Name    VIBR_001    Name    POWER_001
[Metadaten-Zeilen]
0       22.5        0       1.2         0       6.2
1       22.8        1       1.4         1       6.0
```

### Excel-Test-Strukturen

- **Multi-Sheet**: Produktion, Qualität, Wartung, Konfiguration
- **Aggregierte Daten**: KPIs, Statistiken, Trends
- **Formatierte Ausgaben**: Mit Styling und Metadaten

### JSON-IoT-Strukturen

```json
{
  "sensors": [
    {
      "readings": [
        {"timestamp": "...", "value": 22.5, "status": "ok"}
      ]
    }
  ],
  "alerts": [...]
}
```

## 📈 Test-Metriken

### Coverage-Ziele

- **CSV-Import**: >95% Line Coverage
- **Excel-Handling**: >90% Line Coverage
- **JSON-Processing**: >95% Line Coverage
- **Data Cleaning**: >90% Line Coverage
- **Export Functions**: >95% Line Coverage

### Performance-Benchmarks

- **CSV-Import (1MB)**: <2 Sekunden
- **Excel Multi-Sheet**: <5 Sekunden
- **JSON Normalization**: <1 Sekunde
- **Data Cleaning (10k Zeilen)**: <3 Sekunden

## 🛡️ Fehlerbehandlung

### Getestete Fehlerszenarien

1. **Datei nicht gefunden**: Graceful handling mit aussagekräftigen Fehlermeldungen
2. **Encoding-Probleme**: Automatische Encoding-Erkennung und Fallbacks
3. **Ungültige Datenstrukturen**: Robuste Parser mit Validierung
4. **Memory-Probleme**: Chunked Processing und Streaming
5. **Korrupte Daten**: Datenvalidierung und Bereinigung

### Logging und Debugging

- **Test-spezifische Logs**: Detaillierte Informationen für Debugging
- **Intermediate Results**: Speicherung von Zwischenergebnissen für Analyse
- **Performance Timing**: Messung kritischer Operationen

## 📚 Verwendung in der Praxis

### Für Entwickler

```python
# Test einzeln ausführen
pytest tests/test_06_datenimport.py::TestCSVImportGrundlagen::test_csv_import_beispiele -v

# Mit Debug-Output
pytest tests/test_06_datenimport.py -v -s --tb=long

# Kontinuierliche Tests während Entwicklung
pytest-watch tests/test_06_datenimport.py
```

### Für CI/CD-Pipeline

```yaml
# GitHub Actions / GitLab CI
- name: Run Data Import Tests
  run: |
    pytest tests/test_06_datenimport.py \
      --junitxml=test-results/datenimport.xml \
      --cov=src.datenimport \
      --cov-report=xml
```

### Für Qualitätssicherung

- **Regressions-Tests**: Automatische Ausführung bei Code-Änderungen
- **Performance-Tests**: Überwachung der Verarbeitungszeiten
- **Datenvalidierung**: Sicherstellung korrekter Datenverarbeitung

Diese umfassende Test-Suite stellt sicher, dass alle Komponenten des Datenimport-Moduls korrekt funktionieren und industrielle Anforderungen erfüllen.
