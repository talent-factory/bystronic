# Jupyter Tests - SmartFactory Python Grundkurs

## Übersicht

Die Jupyter-Tests validieren die Funktionalität der erweiterten Jupyter-Features
und Deployment-Komponenten. Diese Tests demonstrieren professionelle
Test-Patterns für Notebook-Code und interaktive Widgets.

## Test-Struktur

### `test_07_jupyter.py`

**Getestete Module:**

- `jupyter_widgets_demo.py` - Interaktive Widgets und Dashboards
- `jupyter_extensions_demo.py` - Extension-Management und Konfiguration

**Test-Kategorien:**

#### 1. TestJupyterWidgetsDemo

Tests für interaktive Jupyter-Widgets und Dashboard-Funktionalität:

- **Datenerstellung**: Validierung der Maschinendaten-Generierung
- **Widget-Funktionalität**: Tests für ipywidgets-Integration
- **Dashboard-Erstellung**: Interaktive Dashboard-Komponenten
- **Magic Commands**: Demonstration von Jupyter Magic Commands
- **Sicherheitsvalidierung**: Notebook-Sicherheitsprüfungen
- **Performance-Tests**: Ausführungszeit-Messungen

#### 2. TestJupyterExtensionsDemo

Tests für Jupyter-Extensions und Konfiguration:

- **Extension Manager**: Installation und Verwaltung von Extensions
- **Konfigurationserstellung**: Jupyter-Konfigurationsdateien
- **JupyterLab Settings**: Benutzereinstellungen und Themes
- **Test-Notebooks**: Automatische Notebook-Generierung
- **Extension-Validierung**: Überprüfung installierter Extensions

#### 3. TestJupyterNotebookHandling

Tests für Notebook-spezifische Funktionalität:

- **JSON-Struktur**: Validierung der Notebook-Struktur
- **Zell-Validierung**: Überprüfung von Notebook-Zellen
- **Sicherheitsintegration**: Integration von Sicherheitschecks

#### 4. TestJupyterDeploymentIntegration

Tests für Deployment-Integration:

- **Dockerfile-Validierung**: Überprüfung der Docker-Konfiguration
- **Docker-Compose**: Validierung der Service-Konfiguration
- **Deployment-Dateien**: Existenz und Inhalt der Deployment-Dateien

#### 5. TestJupyterIntegration

Integrationstests für vollständige Workflows:

- **Workflow-Simulation**: End-to-End Jupyter-Workflows
- **Fehlerbehandlung**: Robustheit bei ungültigen Eingaben

## Ausführung der Tests

### Alle Jupyter-Tests ausführen

```bash
# Mit uv (empfohlen)
uv run python -m pytest tests/test_07_jupyter.py -v

# Mit pytest direkt
pytest tests/test_07_jupyter.py -v
```

### Spezifische Test-Kategorien

```bash
# Nur Widget-Tests
uv run python -m pytest tests/test_07_jupyter.py::TestJupyterWidgetsDemo -v

# Nur Extension-Tests
uv run python -m pytest tests/test_07_jupyter.py::TestJupyterExtensionsDemo -v

# Nur Integrationstests
uv run python -m pytest tests/test_07_jupyter.py::TestJupyterIntegration -v
```

### Mit Coverage-Report

```bash
uv run python -m pytest tests/test_07_jupyter.py --cov=src/07_jupyter --cov-report=html
```

## Test-Ergebnisse

**Aktuelle Statistiken:**

- ✅ 34 Tests erfolgreich
- ⚠️ 1 Test mit internem pytest-cov Fehler (nicht kritisch)
- 📊 Hohe Code-Coverage für alle Jupyter-Komponenten

## Besondere Test-Features

### 1. Widget-Verfügbarkeit

Tests berücksichtigen automatisch, ob `ipywidgets` verfügbar ist:

```python
@pytest.mark.skipif(not jupyter_widgets_demo.WIDGETS_AVAILABLE,
                   reason="ipywidgets nicht verfügbar")
def test_create_interactive_dashboard_with_widgets(self):
    # Test nur wenn Widgets verfügbar sind
```

### 2. Subprocess-Mocking

Extension-Tests verwenden Mocking für sichere Subprocess-Aufrufe:

```python
@patch('subprocess.run')
def test_validate_extension_installation_success(self, mock_run):
    mock_run.return_value.returncode = 0
    # Test ohne echte Systemaufrufe
```

### 3. Sicherheitstests

Umfassende Tests für Notebook-Sicherheit:

```python
def test_validate_notebook_security_dangerous_content(self):
    dangerous_content = "import os\nos.system('rm -rf /')"
    validation = validate_notebook_security(dangerous_content)
    assert validation['safe'] is False
```

### 4. Performance-Benchmarks

Zeitmessungen für Performance-kritische Funktionen:

```python
def test_performance_test_function_scaling(self):
    time_small = performance_test_function(100)
    time_large = performance_test_function(1000)
    assert time_large >= time_small  # Skalierung prüfen
```

## Lernziele für Studierende

### Test-Driven Development (TDD)

- Verstehen von Test-First-Ansätzen
- Implementierung von Mock-Objekten
- Fehlerbehandlung und Edge-Cases

### Jupyter-spezifische Tests

- Testing von interaktiven Komponenten
- Validierung von Notebook-Strukturen
- Sicherheitstests für Code-Ausführung

### Integration Testing

- End-to-End Workflow-Tests
- Docker-Integration testen
- Performance-Benchmarking

## Übungen für Studierende

Die Übungsteile (`src/07_jupyter/uebungen/`) sind bewusst nicht getestet, damit
Studierende dort selbstständig arbeiten können:

### `uebung_01_widgets.py`

- Implementierung interaktiver Dashboards
- Widget-Event-Handling
- Datenvisualisierung mit Matplotlib/Plotly

### `uebung_02_deployment.py`

- Jupyter-Konfiguration für verschiedene Umgebungen
- Sicherheitsvalidierung von Notebooks
- Docker-basierte Deployment-Strategien

## Debugging und Troubleshooting

### Häufige Probleme

1. **ipywidgets nicht verfügbar**

   ```bash
   pip install ipywidgets
   jupyter nbextension enable --py widgetsnbextension
   ```

1. **Subprocess-Timeouts**

   - Tests verwenden 15s Timeout für Extension-Checks
   - Bei langsamen Systemen ggf. Timeout erhöhen

1. **Docker-Tests schlagen fehl**

   - Prüfen Sie, ob Docker-Dateien im deployment/ Ordner existieren
   - Validieren Sie YAML-Syntax in docker-compose.yml

### Test-Debugging

```bash
# Verbose Output mit Fehlern
uv run python -m pytest tests/test_07_jupyter.py -v -s

# Nur fehlgeschlagene Tests
uv run python -m pytest tests/test_07_jupyter.py --lf

# Test-Profiling
uv run python -m pytest tests/test_07_jupyter.py --profile
```

## Integration mit anderen Modulen

Die Jupyter-Tests nutzen Patterns aus anderen Test-Modulen:

- **pandas/numpy**: Datenvalidierung und -manipulation
- **matplotlib**: Visualisierungs-Tests
- **subprocess**: System-Integration

## Erweiterungsmöglichkeiten

### Zusätzliche Test-Szenarien

1. **Notebook-Konvertierung**: Tests für nbconvert
1. **JupyterHub-Integration**: Multi-User-Szenarien
1. **Cloud-Deployment**: AWS/Azure-spezifische Tests
1. **Performance-Monitoring**: Langzeit-Performance-Tests

### Automatisierung

- CI/CD-Integration für automatische Tests
- Nightly-Builds für Performance-Regression
- Automatische Sicherheitschecks für neue Notebooks

## Fazit

Die Jupyter-Tests bieten eine umfassende Validierung aller Jupyter-Komponenten
und demonstrieren moderne Test-Praktiken für interaktive Notebook-Umgebungen.
Sie unterstützen sowohl die Qualitätssicherung als auch das Lernen von
Test-Driven Development für Studierende.
