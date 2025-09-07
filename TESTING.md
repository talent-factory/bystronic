# Testing Guide - Bystronic Python Grundkurs

## 🧪 Lokale Test-Ausführung

### Alle Tests ausführen

```bash
# Alle Tests
uv run pytest

# Mit Coverage-Report
uv run pytest --cov=src --cov-report=term-missing

# Nur bestimmte Module
uv run pytest tests/test_01_grundlagen.py
uv run pytest tests/test_02_datentypen.py
```

### UI-Tests (erfordern GUI-Umgebung)

```bash
# Einfache UI-Tests
uv run pytest tests/test_08_ui_simple.py

# PyQt-spezifische Tests (benötigen Display)
uv run pytest tests/test_08_ui_pyqt_specific.py

# Streamlit-Tests
uv run pytest tests/test_08_ui_streamlit_specific.py
```

### Test-Kategorien

#### ✅ Immer verfügbar

- **Grundlagen**: `tests/test_01_grundlagen*.py`
- **Datentypen**: `tests/test_02_datentypen.py`
- **NumPy**: `tests/test_03_numpy.py`
- **Pandas**: `tests/test_04_pandas.py`

#### 🖥️ GUI-abhängig

- **UI-Tests**: `tests/test_08_ui*.py`
- Benötigen aktive Display-Umgebung
- Können in Headless-Umgebungen fehlschlagen

## 🔧 Pre-commit Hooks

### Installation

```bash
# Pre-commit installieren
uv add --group dev pre-commit

# Hooks aktivieren
uv run pre-commit install
```

### Manuelle Ausführung

```bash
# Alle Hooks auf alle Dateien
uv run pre-commit run --all-files

# Nur auf geänderte Dateien
uv run pre-commit run
```

### Enthaltene Checks

- **Code-Qualität**: ruff, black, mypy
- **Dokumentation**: markdownlint, mdformat
- **Allgemein**: trailing-whitespace, yaml-check

## 🚀 Empfohlener Workflow

### 1. Entwicklung

```bash
# Code ändern
# ...

# Tests lokal ausführen
uv run pytest tests/test_XX_relevant.py

# Pre-commit prüfen
uv run pre-commit run
```

### 2. Commit

```bash
# Pre-commit läuft automatisch
git commit -m "feat: neue Funktionalität"

# Bei Fehlern: Fixes anwenden und erneut committen
```

### 3. Push

```bash
# Kein CI - lokale Tests sind ausreichend
git push origin feature-branch
```

## 🎯 Warum keine GitHub Actions?

- **Lokale Tests sind zuverlässiger** für GUI-Komponenten
- **Pre-commit verhindert** fehlerhafte Commits
- **Weniger Komplexität** in der CI/CD-Pipeline
- **Schnelleres Feedback** für Entwickler

## 📋 Test-Checkliste

Vor jedem Commit:

- [ ] Relevante Tests lokal ausgeführt
- [ ] Pre-commit Hooks erfolgreich
- [ ] Neue Tests für neue Funktionalität geschrieben
- [ ] Dokumentation aktualisiert

## 🔍 Debugging

### Test-Fehler analysieren

```bash
# Verbose Output
uv run pytest -v tests/test_XX.py

# Mit Traceback
uv run pytest --tb=long tests/test_XX.py

# Einzelnen Test ausführen
uv run pytest tests/test_XX.py::TestClass::test_method
```

### UI-Test-Probleme

```bash
# Display-Umgebung prüfen
echo $DISPLAY

# Qt-Konfiguration
export QT_QPA_PLATFORM=offscreen

# Mit xvfb (Linux)
xvfb-run -a uv run pytest tests/test_08_ui*.py
```

## 📚 Weitere Informationen

- **pytest Dokumentation**: <https://docs.pytest.org/>
- **Coverage Reports**: `htmlcov/index.html` nach `--cov-report=html`
- **Test-Patterns**: Siehe `tests/README_*.md` Dateien
