# CLAUDE.md - Python Grundkurs Bystronic

## Projektübersicht

Dieses Projekt ist ein umfassender Python-Grundkurs für Bystronic-Entwickler mit Fokus auf Datenanalyse und praktische Anwendungen.

## Wichtige Befehle

### Entwicklungsumgebung
```bash
# Projekt initialisieren und Abhängigkeiten installieren
uv sync

# In die uv-Umgebung wechseln
uv shell

# Jupyter Notebook starten
uv run jupyter notebook

# Tests ausführen (falls vorhanden)
uv run pytest

# Code-Formatierung
uv run black .

# Python-Script ausführen
uv run python script.py
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
- `src/08_ui/` - Tkinter, Streamlit, Dash
- `src/09_projekte/` - Praxisprojekte

Zusätzliche Verzeichnisse:
- `data/` - Beispieldaten für Übungen
- `docs/` - Dokumentation und Anleitungen

## Kursziele

1. **Grundlagen**: Python-Syntax, Programmstruktur, VS Code Setup
2. **Datentypen**: Listen, Dictionaries, Sets, etc.
3. **Libraries**: NumPy, Pandas, Matplotlib schwerpunktmässig
4. **Datenanalyse**: Grosse Datenmengen verarbeiten und visualisieren
5. **Import/Export**: CSV, Excel, JSON, Datenbanken
6. **UI**: Einfache Benutzeroberflächen erstellen
7. **KI-Integration**: Programmieren mit KI-Unterstützung

## Zielgruppe

Bystronic-Entwickler, die von VBA zu Python wechseln möchten und sich auf Datenanalyse konzentrieren wollen.

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