# Tests für Modul 08 - UI-Entwicklung

Umfassende Testdokumentation für PyQt und Streamlit Beispiele im Bystronic
Python-Grundkurs.

## Übersicht

Die Tests für Modul 08 sind in drei Hauptdateien organisiert:

- `test_08_ui.py` - Grundlegende Tests und Integrationstests
- `test_08_ui_pyqt_specific.py` - Spezifische PyQt/PySide-Tests
- `test_08_ui_streamlit_specific.py` - Spezifische Streamlit-Tests

## Teststruktur

### 1. Grundlegende UI-Tests (`test_08_ui.py`)

#### TestPyQTGrundlagen

- **Widget-Initialisierung**: Prüft korrekte Erstellung der Hauptkomponenten
- **Menüleisten-Tests**: Validiert Menü-Struktur und -Funktionalität
- **Tab-Erstellung**: Überprüft alle vier Haupttabs
- **Eingabe-Widgets**: Testet Textfelder, Spinboxen, Slider, Comboboxen
- **Progress-Demo**: Validiert Timer-basierte Fortschrittsanzeige
- **Status-Updates**: Prüft Maschinen-Status-Änderungen

#### TestDatenbankBrowser

- **Datenbank-Initialisierung**: Erstellt temporäre SQLite-Datenbank
- **Tabellen-Erstellung**: Validiert Schema für machines, production_data,
  maintenance
- **Query-Ausführung**: Testet SQL-Abfragen und Fehlerbehandlung
- **Beispieldaten**: Überprüft Einfügung von Testdaten

#### TestStreamlitComponents

- **Import-Tests**: Validiert verfügbare Streamlit-Module
- **Daten-Generierung**: Testet Produktionsdaten-Erstellung
- **Konfiguration**: Prüft Seiten-Setup und Parameter

### 2. PyQt-spezifische Tests (`test_08_ui_pyqt_specific.py`)

#### TestMaschinendatenGUI

- **Datenmodell**: Testet MaschinenDatenModel mit Beispieldaten
- **Filterung**: Validiert Status- und Suchfilter
- **Export-Funktionalität**: Prüft CSV-Export
- **Worker-Thread**: Testet asynchrone Datenladung
- **Tabellen-Operationen**: Sortierung, Selektion, Kontextmenüs

#### TestDiagrammViewer

- **Chart-Erstellung**: Testet verschiedene Diagrammtypen (Line, Bar, Scatter,
  Pie)
- **Datenladung**: Validiert CSV-Import für Visualisierung
- **Chart-Export**: Prüft PNG-Export-Funktionalität
- **Chart-Widget**: Testet benutzerdefinierte Chart-Komponenten

#### TestModerneUI

- **Theme-Switching**: Testet Dark/Light-Theme-Wechsel
- **Animierte Buttons**: Validiert Button-Animationen
- **Glas-Effekte**: Prüft visuelle Effekte
- **Responsive Layout**: Testet Anpassung an verschiedene Fenstergrößen

### 3. Streamlit-spezifische Tests (`test_08_ui_streamlit_specific.py`)

#### TestStreamlitDataUpload

- **CSV-Verarbeitung**: Testet Upload und Parsing von CSV-Dateien
- **JSON-Verarbeitung**: Validiert JSON-Datenimport
- **Datei-Validierung**: Prüft Struktur und erforderliche Spalten
- **Datenbereinigung**: Testet Duplikat-Entfernung und Datentyp-Konvertierung

#### TestStreamlitCharts

- **Plotly-Integration**: Testet verschiedene Chart-Typen
- **Zeitreihen-Visualisierung**: Line Charts für Produktionsdaten
- **Aggregations-Charts**: Bar Charts für zusammengefasste Daten
- **Multi-Achsen-Diagramme**: Komplexe Visualisierungen

#### TestStreamlitDashboard

- **KPI-Berechnung**: Validiert Kennzahlen-Generierung
- **Status-Aggregation**: Testet Maschinen-Status-Zusammenfassung
- **Alert-System**: Prüft automatische Warnungen
- **Echtzeit-Simulation**: Testet Datenaktualisierung

## Ausführung der Tests

### Voraussetzungen

```bash
# Basis-Dependencies
pip install pytest pytest-cov pandas numpy

# PyQt-Tests (optional)
pip install PySide6

# Streamlit-Tests (optional)
pip install streamlit plotly

# Performance-Tests
pip install psutil
```

### Alle Tests ausführen

```bash
# Alle UI-Tests
python -m pytest tests/test_08_ui*.py -v

# Mit Coverage-Report
python -m pytest tests/test_08_ui*.py --cov=src/08_ui --cov-report=html

# Nur PyQt-Tests
python -m pytest tests/test_08_ui_pyqt_specific.py -v

# Nur Streamlit-Tests
python -m pytest tests/test_08_ui_streamlit_specific.py -v
```

### Spezifische Testgruppen

```bash
# Nur Grundlagen-Tests
python -m pytest tests/test_08_ui.py::TestPyQTGrundlagen -v

# Nur Datenbank-Tests
python -m pytest tests/test_08_ui.py::TestDatenbankBrowser -v

# Nur Performance-Tests
python -m pytest tests/test_08_ui.py::TestPerformance -v

# Tests mit bestimmten Markern
python -m pytest -m "not slow" tests/test_08_ui*.py
```

## Test-Fixtures und Mocks

### Wichtige Fixtures

- **app**: QApplication-Instanz für PyQt-Tests
- **temp_db**: Temporäre SQLite-Datenbank
- **sample_data**: Beispiel-Maschinendaten
- **mock_streamlit**: Gemockte Streamlit-Komponenten

### Mock-Strategien

- **Datei-I/O**: Verwendung von StringIO/BytesIO für Datei-Simulation
- **Datenbank**: Temporäre In-Memory-Datenbanken
- **UI-Komponenten**: Mock-Objekte für Widget-Tests
- **Externe APIs**: Patch-Decorators für HTTP-Requests

## Testdaten

### Maschinendaten-Schema

```python
{
    'id': int,
    'name': str,
    'type': str,  # 'Laser', 'Press', 'Cutter', 'Bender'
    'status': str,  # 'Active', 'Maintenance', 'Offline'
    'production_rate': float,
    'temperature': float,
    'last_maintenance': str  # ISO-Format
}
```

### Produktionsdaten-Schema

```python
{
    'Datum': datetime,
    'Maschine': str,
    'Produktion': int,
    'Qualität': float,  # Prozent
    'Effizienz': float,  # Prozent
    'Temperatur': float  # Celsius
}
```

## Fehlerbehandlung und Edge Cases

### Getestete Szenarien

- **Fehlende Dependencies**: Graceful Degradation bei fehlenden Paketen
- **Ungültige Daten**: Robuste Behandlung von Malformed Data
- **Datenbankfehler**: SQL-Exceptions und Connection-Probleme
- **UI-Exceptions**: Widget-Erstellungsfehler und Event-Handling
- **Performance-Limits**: Große Datensätze und Memory-Management

### Erwartete Fehler

```python
# Beispiel für erwartete Exceptions
with pytest.raises(FileNotFoundError):
    load_nonexistent_file()

with pytest.raises(ValueError):
    validate_invalid_data()
```

## Performance-Tests

### Metriken

- **Datenverarbeitung**: < 1 Sekunde für 10.000 Datensätze
- **UI-Responsiveness**: Widget-Erstellung < 100ms
- **Memory-Usage**: Kontrolliertes Wachstum und Cleanup
- **Chart-Rendering**: < 500ms für komplexe Visualisierungen

### Benchmarks

```python
def test_large_dataset_performance():
    start_time = time.time()
    process_large_dataset(10000)
    processing_time = time.time() - start_time
    assert processing_time < 1.0
```

## Continuous Integration

### GitHub Actions Konfiguration

```yaml
- name: Test UI Components
  run: |
    python -m pytest tests/test_08_ui*.py \
      --cov=src/08_ui \
      --cov-report=xml \
      --junit-xml=test-results.xml
```

### Test-Marker

- `@pytest.mark.slow` - Langsame Tests (> 1 Sekunde)
- `@pytest.mark.integration` - Integrationstests
- `@pytest.mark.ui` - UI-spezifische Tests
- `@pytest.mark.skipif` - Bedingte Tests (abhängig von Dependencies)

## Debugging und Troubleshooting

### Häufige Probleme

1. **PyQt nicht verfügbar**: Tests werden automatisch übersprungen
1. **Display-Probleme**: Verwendung von Xvfb in CI-Umgebungen
1. **Timing-Issues**: QTest.qWait() für asynchrone Operationen
1. **Memory-Leaks**: Explizites Widget-Cleanup in Fixtures

### Debug-Optionen

```bash
# Verbose Output mit Traceback
python -m pytest tests/test_08_ui.py -v -s --tb=long

# Nur fehlgeschlagene Tests
python -m pytest tests/test_08_ui.py --lf

# Stoppe bei erstem Fehler
python -m pytest tests/test_08_ui.py -x
```

## Erweiterung der Tests

### Neue Tests hinzufügen

1. **Neue Testklasse erstellen**:

   ```python
   class TestNeueKomponente:
       @pytest.fixture
       def setup_data(self):
           return test_data

       def test_neue_funktionalität(self, setup_data):
           assert expected_behavior()
   ```

1. **Fixtures erweitern**:

   ```python
   @pytest.fixture
   def complex_data():
       return generate_complex_test_data()
   ```

1. **Mock-Strategien anpassen**:

   ```python
   @patch('module.external_dependency')
   def test_with_mock(self, mock_dep):
       mock_dep.return_value = expected_value
       assert test_function() == expected_result
   ```

## Best Practices

### Test-Design

- **Isolation**: Jeder Test ist unabhängig
- **Determinismus**: Reproduzierbare Ergebnisse
- **Klarheit**: Aussagekräftige Test- und Assertion-Namen
- **Coverage**: Kritische Pfade und Edge Cases abdecken

### Code-Qualität

- **DRY-Prinzip**: Wiederverwendbare Fixtures und Hilfsfunktionen
- **Dokumentation**: Docstrings für komplexe Test-Szenarien
- **Wartbarkeit**: Modulare Test-Struktur
- **Performance**: Effiziente Test-Ausführung

## Metriken und Reporting

### Coverage-Ziele

- **Gesamt-Coverage**: > 90%
- **Kritische Funktionen**: 100%
- **UI-Komponenten**: > 85%
- **Fehlerbehandlung**: > 95%

### Test-Reports

```bash
# HTML-Coverage-Report
python -m pytest --cov=src/08_ui --cov-report=html
open htmlcov/index.html

# JUnit-XML für CI
python -m pytest --junit-xml=test-results.xml

# JSON-Report für Analyse
python -m pytest --json-report --json-report-file=report.json
```

______________________________________________________________________

**Hinweis**: Diese Tests sind speziell für den Bystronic Python-Grundkurs
entwickelt und demonstrieren professionelle Test-Techniken für UI-Anwendungen.
Sie dienen sowohl der Qualitätssicherung als auch als Lernmaterial für die
Kursteilnehmer.
