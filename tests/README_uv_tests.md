# UI-Tests mit uv Package Manager

Anleitung für die Ausführung der UI-Tests im Bystronic Python-Grundkurs mit uv.

## Schnellstart

```bash
# Alle Dependencies installieren
uv sync --all-extras

# Test-Dependencies hinzufügen
uv add --group test pytest-qt pytest-mock psutil

# Einfache Tests ausführen
uv run pytest tests/test_08_ui_simple.py -v

# Test-Utilities prüfen
uv run pytest tests/test_08_ui_utils.py -v
```

## Verfügbare Testsuites

### 1. Basis-Tests (immer funktionsfähig)

```bash
# Grundlegende Funktionalität ohne UI-Dependencies
uv run pytest tests/test_08_ui_simple.py::TestBasicFunctionality -v

# Fehlerbehandlung
uv run pytest tests/test_08_ui_simple.py::TestErrorHandling -v
```

### 2. Datenverarbeitungs-Tests

```bash
# Benötigt: pandas, numpy (bereits in dependencies)
uv run pytest tests/test_08_ui_simple.py::TestDataProcessing -v

# Datenbank-Tests
uv run pytest tests/test_08_ui_simple.py::TestDatabaseOperations -v
```

### 3. Chart-Tests

```bash
# Benötigt: plotly (bereits in dependencies)
uv run pytest tests/test_08_ui_simple.py::TestChartGeneration -v
```

### 4. Streamlit-Tests

```bash
# Benötigt: streamlit (bereits in dependencies)
uv run pytest tests/test_08_ui_simple.py::TestStreamlitMocking -v
```

### 5. Performance-Tests

```bash
# Benötigt: psutil
uv add psutil
uv run pytest tests/test_08_ui_simple.py::TestPerformanceAndMemory -v
```

## Dependency-Management

### Aktuelle Dependencies prüfen

```bash
uv run python -c "
from tests.test_08_ui_utils import print_dependency_status
print_dependency_status()
"
```

### Fehlende Dependencies installieren

```bash
# UI-Dependencies (optional)
uv sync --extra ui

# Test-Dependencies
uv sync --extra test

# Alle Dependencies
uv sync --all-extras
```

## Test-Konfiguration

Die Tests sind so konfiguriert, dass sie automatisch übersprungen werden, wenn Dependencies fehlen:

- `@requires_data()` - Benötigt pandas, numpy
- `@requires_ui()` - Benötigt PySide6
- `@requires_charts()` - Benötigt plotly
- `@requires_streamlit()` - Benötigt streamlit

## Erweiterte Ausführung

### Mit Coverage-Report

```bash
uv run pytest tests/test_08_ui_simple.py --cov=tests --cov-report=html
```

### Parallele Ausführung

```bash
uv add pytest-xdist
uv run pytest tests/test_08_ui_simple.py -n auto
```

### Nur bestimmte Tests

```bash
# Nur Datenvalidierung
uv run pytest tests/test_08_ui_simple.py -k "validation"

# Nur Performance-Tests
uv run pytest tests/test_08_ui_simple.py -k "performance"
```

## Troubleshooting

### Problem: Import-Fehler

```bash
# Lösung: Projekt im Development-Modus installieren
uv pip install -e .
```

### Problem: PySide6-Fehler in CI

```bash
# Lösung: Virtual Display verwenden
sudo apt-get install xvfb
xvfb-run -a uv run pytest tests/test_08_ui_simple.py
```

### Problem: Coverage-Warnungen

```bash
# Lösung: Coverage auf Tests beschränken
uv run pytest tests/test_08_ui_simple.py --cov=tests --no-cov-report
```

## GitHub Actions Integration

Die Tests sind für GitHub Actions konfiguriert (siehe `.github/workflows/ui-tests.yml`):

- Läuft auf Python 3.11, 3.12, 3.13
- Verwendet uv für Dependency-Management
- Unterstützt GUI-Tests mit xvfb
- Generiert Test-Reports und Coverage

## Lokale Entwicklung

### Pre-Commit Hooks

```bash
uv add pre-commit
uv run pre-commit install
```

### Test-Driven Development

```bash
# Watch-Modus für kontinuierliche Tests
uv add pytest-watch
uv run ptw tests/test_08_ui_simple.py
```

### Debugging

```bash
# Verbose Output mit Traceback
uv run pytest tests/test_08_ui_simple.py -v -s --tb=long

# Stoppe bei erstem Fehler
uv run pytest tests/test_08_ui_simple.py -x

# Nur fehlgeschlagene Tests wiederholen
uv run pytest tests/test_08_ui_simple.py --lf
```

## Test-Struktur

```text
tests/
├── test_08_ui.py                    # Ursprüngliche umfassende Tests
├── test_08_ui_pyqt_specific.py      # PyQt-spezifische Tests
├── test_08_ui_streamlit_specific.py # Streamlit-spezifische Tests
├── test_08_ui_utils.py              # Test-Utilities und Fixtures
├── test_08_ui_simple.py             # Funktionsfähige Tests mit uv
└── README_08_ui_tests.md            # Umfassende Dokumentation
```

## Best Practices

1. **Dependency-Checks**: Verwende die bereitgestellten Decorators
2. **Mock-Strategien**: Nutze die Test-Utilities für konsistente Mocks
3. **Isolation**: Jeder Test ist unabhängig und wiederholbar
4. **Performance**: Verwende `tmp_path` für temporäre Dateien
5. **Dokumentation**: Aussagekräftige Test-Namen und Docstrings

## Beispiel-Test erstellen

```python
from tests.test_08_ui_utils import requires_data, TestDataGenerator

@requires_data()
class TestMyFeature:
    def test_data_processing(self):
        # Generiere Testdaten
        data = TestDataGenerator.create_machine_data(5)

        # Teste Funktionalität
        result = process_machine_data(data)

        # Assertions
        assert len(result) == 5
        assert all('processed' in item for item in result)
```

Diese Struktur gewährleistet robuste, wartbare Tests die mit uv optimal funktionieren.
