# Pandas Tests - test_04_pandas.py

Diese Test-Suite validiert die Funktionalität der Pandas-Beispiele und demonstriert bewährte Test-Patterns für Datenanalyse-Code und DataFrame-Operationen.

## 📋 Test-Übersicht

### **TestDataFrameBasics** (4 Tests)

- ✅ **Modul-Import**: Erfolgreiche Importierbarkeit des dataframe_basics Moduls
- ✅ **DataFrame-Erstellung**: Validiert korrekte DataFrame-Erstellung mit Maschinendaten
- ✅ **DataFrame-Operationen**: Filterung, Sortierung, Spalten-Hinzufügung und -Berechnung
- ✅ **Aggregations-Operationen**: Gruppierung und statistische Berechnungen

### **TestDataImportExport** (3 Tests)

- ✅ **Modul-Import**: Erfolgreiche Importierbarkeit des data_import_export Moduls
- ✅ **CSV-Operationen**: Import/Export-Roundtrip mit Integritätsprüfung
- ✅ **JSON-Operationen**: JSON-Serialisierung und -Deserialisierung

### **TestDataCleaning** (4 Tests)

- ✅ **Modul-Import**: Erfolgreiche Importierbarkeit des data_cleaning Moduls
- ✅ **Missing Data**: Behandlung fehlender Werte mit dropna() und fillna()
- ✅ **Datentyp-Konvertierung**: String-zu-Numeric und Boolean-Konvertierungen
- ✅ **Duplikat-Behandlung**: Erkennung und Entfernung von Duplikaten

### **TestDataAnalysis** (4 Tests)

- ✅ **Modul-Import**: Erfolgreiche Importierbarkeit des data_analysis Moduls
- ✅ **Deskriptive Statistiken**: Grundstatistiken für numerische Spalten
- ✅ **Maschinen-Performance**: Komplexe Analyse von Maschinenlaufzeiten und -effizienz
- ✅ **Produktionsdaten-Analyse**: Zeitreihen-Analyse mit Gruppierungen und Aggregationen

### **Einzelne Test-Funktionen** (2 Tests)

- ✅ **Pandas-Version-Kompatibilität**: Überprüft kompatible Pandas-Installation (≥1.0)
- ✅ **Datei-Existenz**: Validiert Verfügbarkeit aller Beispieldateien

## 🚀 Tests ausführen

### Alle Pandas-Tests

```bash
uv run python -m pytest tests/test_04_pandas.py -v
```

### Spezifische Test-Klasse

```bash
uv run python -m pytest tests/test_04_pandas.py::TestDataFrameBasics -v
```

### Einzelner Test

```bash
uv run python -m pytest tests/test_04_pandas.py::TestDataAnalysis::test_production_data_analysis -v
```

### Mit Coverage-Report

```bash
uv run python -m pytest tests/test_04_pandas.py --cov=src/04_pandas --cov-report=html
```

## 🎯 Test-Patterns für Datenanalyse

### **DataFrame-Vergleiche**

```python
def test_dataframe_equality(self):
    # Exakte DataFrame-Vergleiche
    pd.testing.assert_frame_equal(expected_df, actual_df)

    # Mit Toleranz für numerische Werte
    pd.testing.assert_frame_equal(expected_df, actual_df, atol=1e-5)
```

### **Temporäre Dateien für I/O-Tests**

```python
def test_csv_roundtrip(self):
    with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as tmp:
        test_data.to_csv(tmp.name, index=False)
        loaded_data = pd.read_csv(tmp.name)
        pd.testing.assert_frame_equal(test_data, loaded_data)
```

### **Missing Data Tests**

```python
def test_missing_values(self):
    missing_count = df.isnull().sum().sum()
    assert missing_count == expected_missing

    # Nach Behandlung sollten keine NaN-Werte vorhanden sein
    cleaned_df = df.fillna("Unbekannt")
    assert cleaned_df.isnull().sum().sum() == 0
```

### **Datentyp-Validierung**

```python
def test_data_types(self):
    assert df["Baujahr"].dtype in [np.int64, np.int32]
    assert df["Aktiv"].dtype == bool
    assert pd.api.types.is_string_dtype(df["Maschine"])
```

### **Aggregation und Gruppierung**

```python
def test_groupby_operations(self):
    grouped = df.groupby("Typ")["Wert"].agg(["mean", "std", "count"])
    assert len(grouped) == expected_groups
    assert "mean" in grouped.columns
```

## 📊 Industrielle Datenanalyse-Patterns

### **Maschinendaten-Analysen**

- **Effizienz-Berechnung**: `(Ist_Zeit / Soll_Zeit) * 100`
- **Altersanalyse**: `2024 - Baujahr > Schwellenwert`
- **Wartungsplanung**: Basierend auf Laufzeiten und Zustand

### **Produktionsdaten-Tracking**

- **Abweichungsanalyse**: `Ist_Wert - Soll_Wert`
- **Trendanalyse**: Zeitliche Entwicklung von KPIs
- **Kapazitätsplanung**: Aggregierte Maschinenlaufzeiten

### **Qualitätskontrolle**

- **Ausschuss-Raten**: `(Fehlerhafte_Teile / Gesamt_Teile) * 100`
- **Toleranz-Überwachung**: Statistische Prozesskontrolle
- **Prozessfähigkeit**: Cp/Cpk-Berechnungen

## 🛠️ Test-Dependencies

- **pytest**: Test-Framework für strukturierte Tests
- **pandas**: Hauptbibliothek für Datenanalyse (wird getestet)
- **numpy**: Für numerische Operationen und Zufallsdaten
- **tempfile**: Für sichere temporäre Datei-Operationen
- **unittest.mock**: Für Mocking und Patching
- **pathlib/sys**: Für dynamische Modul-Imports

## 📈 Qualitätssicherung

Diese Tests gewährleisten:

1. **Datenintegrität**: DataFrames behalten ihre Struktur und Inhalte
2. **I/O-Robustheit**: Sichere Import/Export-Operationen für verschiedene Formate
3. **Data Cleaning**: Zuverlässige Behandlung von fehlenden und fehlerhaften Daten
4. **Analytical Correctness**: Korrekte statistische und aggregierte Berechnungen
5. **Performance Tracking**: Validierung industrieller KPIs und Metriken
6. **Version Compatibility**: Kompatibilität mit aktuellen Pandas-Versionen

## 🎓 Lernziele der Tests

- **DataFrame-Operationen**: Grundlegende und erweiterte DataFrame-Manipulationen
- **Data I/O**: Sichere Datenimport/-export-Patterns für CSV, JSON, Excel
- **Data Cleaning**: Professionelle Datenbereinigung und -validierung
- **Statistical Analysis**: Deskriptive Statistiken und Aggregationen
- **Groupby Operations**: Komplexe Gruppierungen und Multi-Level-Aggregationen
- **Time Series**: Zeitreihenanalyse für Produktionsdaten
- **Quality Assurance**: Test-Patterns für reproduzierbare Datenanalyse

Diese Tests sind essentiell für verlässliche Datenanalyse-Pipelines in der industriellen Anwendung! 📊✨
