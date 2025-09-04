# CLAUDE.md - Python Grundkurs Bystronic

## Projektübersicht

Dieses Projekt ist ein umfassender Python-Grundkurs für Bystronic-Entwickler mit
Fokus auf Datenanalyse und praktische Anwendungen.

## Wichtige Befehle

### Entwicklungsumgebung

```bash
# Projekt initialisieren und Abhängigkeiten installieren
uv sync

# Development-Tools installieren (ruff, black, pytest, etc.)
uv sync --extra dev

# Makefile verwenden (empfohlen):
make help              # Zeige alle verfügbaren Kommandos
make dev-install       # Installiere alle Dependencies
make format            # Code formatieren
make lint              # Code prüfen
make test              # Tests ausführen
make notebook          # Jupyter Notebook starten

# Oder direkt mit uv:
uv run jupyter notebook    # Jupyter Notebook starten
uv run black src/          # Code formatieren
uv run ruff check src/     # Linting
uv run pytest             # Tests ausführen
uv run python script.py   # Python-Script ausführen
```

### Projektstruktur

Das Projekt ist in thematische Module unter `src/` unterteilt:

- `src/01_grundlagen/` - Python Basics
- `src/02_datentypen/` - Datentypen und Strukturen
- `src/03_numpy/` - NumPy für numerische Berechnungen
- `src/04_pandas/` - Pandas für Datenanalyse
- `src/05_visualisierung/` - Matplotlib, Seaborn, Plotly
- `src/06_datenimport/` - CSV, Excel, JSON, APIs
- `src/07_jupyter/` - Jupyter Notebooks
- `src/08_ui/` - PyQt/PySide, Streamlit, Dash
- `src/09_projekte/` - Praxisprojekte

Zusätzliche Verzeichnisse:

- `data/` - Beispieldaten für Übungen
- `docs/` - Dokumentation und Anleitungen

## Kursziele

1. **Grundlagen**: Python-Syntax, Programmstruktur, VS Code Setup
1. **Datentypen**: Listen, Dictionaries, Sets, etc.
1. **Libraries**: NumPy, Pandas, Matplotlib schwerpunktmässig
1. **Datenanalyse**: Grosse Datenmengen verarbeiten und visualisieren
1. **Import/Export**: CSV, Excel, JSON, Datenbanken
1. **UI**: Einfache Benutzeroberflächen erstellen
1. **KI-Integration**: Programmieren mit KI-Unterstützung

## Zielgruppe

Bystronic-Entwickler, die von VBA zu Python wechseln möchten und sich auf
Datenanalyse konzentrieren wollen.

## Technische Details

- **Python Version**: 3.13+
- **Hauptbibliotheken**: NumPy, Pandas, Matplotlib, Seaborn, Plotly, Jupyter
- **IDE**: Visual Studio Code
- **Package Manager**: uv

## Besonderheiten

- Schwerpunkt auf Datenanalyse und Visualisierung
- Jupyter Notebooks für interaktive Entwicklung
- Vergleiche und Migration von VBA zu Python
- KI-gestützte Programmierung als Lernziel
- Praxisorientierte Beispiele aus der Industrie
