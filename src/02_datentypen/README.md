# 📊 Kapitel 2: Datentypen und Datenstrukturen

## Adaptives Lernsystem für heterogene Lerngruppen

Willkommen zum zweiten Kapitel des Python Grundkurses für Bystronic-Entwickler!
Dieses Kapitel verwendet ein **3-stufiges adaptives Lernsystem**, das sich an
Ihr Vorwissen anpasst.

## 🎯 Adaptive Lernpfade

### 🔍 Schritt 1: Assessment durchführen

```bash
# Bestimmen Sie Ihren optimalen Lernpfad (5-7 Minuten)
uv run python src/02_datentypen/assessments/learning_path_assessment.py
```

### 📚 Schritt 2: Ihren Lernpfad wählen

#### 🟢 Beginner-Pfad (0-40 Punkte)

**Zielgruppe:** Programmier-Einsteiger, erste Schritte mit Datentypen
**Dauer:** 15-25 Minuten pro Übung
**Fokus:** Grundlagen verstehen, praktische Anwendung

#### 🟡 Intermediate-Pfad (41-70 Punkte)

**Zielgruppe:** Programmiererfahrung vorhanden, erweiterte Datenverarbeitung
**Dauer:** 25-40 Minuten pro Übung
**Fokus:** Funktionale Programmierung, Statistik, Fehlerbehandlung

#### 🔴 Advanced-Pfad (71-100 Punkte)

**Zielgruppe:** Erfahrene Entwickler, professionelle Systeme
**Dauer:** 45-60 Minuten pro Übung
**Fokus:** OOP, Design Patterns, Enterprise-Standards

## 📁 Neue Struktur

### 🎓 Theory & Documentation

- **[theory/02_datentypen.ipynb](theory/02_datentypen.ipynb)** - Interaktives
  Jupyter Notebook

### 💡 Examples (für alle Levels)

- **[numbers_demo.py](examples/numbers_demo.py)** - Zahlen und mathematische
  Operationen
- **[strings_demo.py](examples/strings_demo.py)** - String-Manipulation und
  Formatierung
- **[collections_demo.py](examples/collections_demo.py)** - Listen,
  Dictionaries, Sets und Tupel
- **[vba_collections_comparison.py](examples/vba_collections_comparison.py)** -
  VBA vs Python Collections

### 🎯 Adaptive Exercises

#### 🟢 Beginner Exercises

- **[uebung_01_zahlen_beginner.py](exercises/beginner/uebung_01_zahlen_beginner.py)** -
  Grundlagen der Zahlentypen
- **[uebung_02_strings_beginner.py](exercises/beginner/uebung_02_strings_beginner.py)** -
  Einfache String-Operationen
- **[uebung_03_collections_beginner.py](exercises/beginner/uebung_03_collections_beginner.py)** -
  Listen und Dictionaries

#### 🟡 Intermediate Exercises

- **[uebung_01_zahlen_intermediate.py](exercises/intermediate/uebung_01_zahlen_intermediate.py)** -
  Erweiterte Zahlenoperationen
- **[uebung_02_strings_intermediate.py](exercises/intermediate/uebung_02_strings_intermediate.py)** -
  String-Verarbeitung und Regex
- **[uebung_03_collections_intermediate.py](exercises/intermediate/uebung_03_collections_intermediate.py)** -
  Komplexe Datenstrukturen

#### 🔴 Advanced Exercises

- **[uebung_01_zahlen_advanced.py](exercises/advanced/uebung_01_zahlen_advanced.py)** -
  OOP-Zahlenverarbeitung
- **[uebung_02_strings_advanced.py](exercises/advanced/uebung_02_strings_advanced.py)** -
  Enterprise String-Processing
- **[uebung_03_collections_advanced.py](exercises/advanced/uebung_03_collections_advanced.py)** -
  Design Patterns für Collections

### 🆘 4-Stufen-Hilfesystem

Für jede Übung verfügbar:

- **Hints:** Erste Hilfestellungen und Tipps
- **Skeleton:** Code-Gerüst mit Kommentaren
- **Partial:** Teilweise implementierte Lösung
- **Complete:** Vollständige Musterlösung mit Erklärungen

## 🚀 Schnellstart

### 1. Assessment durchführen (EMPFOHLEN)

```bash
# Bestimmen Sie Ihren optimalen Lernpfad
uv run python src/02_datentypen/assessments/learning_path_assessment.py
```

### 2. Umgebung einrichten

```bash
# Im Projektverzeichnis
uv sync
uv shell
```

### 3. Theory studieren (optional)

```bash
# Jupyter Notebook mit theoretischen Grundlagen
uv run jupyter notebook src/02_datentypen/theory/02_datentypen.ipynb
```

### 4. Examples erkunden

```bash
# Zahlen-Beispiele
uv run python src/02_datentypen/examples/numbers_demo.py

# String-Beispiele
uv run python src/02_datentypen/examples/strings_demo.py

# Collections-Beispiele
uv run python src/02_datentypen/examples/collections_demo.py

# VBA-Vergleich
uv run python src/02_datentypen/examples/vba_collections_comparison.py
```

### 5. Adaptive Übungen (nach Assessment-Ergebnis)

#### 🟢 Beginner-Pfad

```bash
uv run python src/02_datentypen/exercises/beginner/uebung_01_zahlen_beginner.py
uv run python src/02_datentypen/exercises/beginner/uebung_02_strings_beginner.py
uv run python src/02_datentypen/exercises/beginner/uebung_03_collections_beginner.py
```

#### 🟡 Intermediate-Pfad

```bash
uv run python src/02_datentypen/exercises/intermediate/uebung_01_zahlen_intermediate.py
uv run python src/02_datentypen/exercises/intermediate/uebung_02_strings_intermediate.py
uv run python src/02_datentypen/exercises/intermediate/uebung_03_collections_intermediate.py
```

#### 🔴 Advanced-Pfad

```bash
uv run python src/02_datentypen/exercises/advanced/uebung_01_zahlen_advanced.py
uv run python src/02_datentypen/exercises/advanced/uebung_02_strings_advanced.py
uv run python src/02_datentypen/exercises/advanced/uebung_03_collections_advanced.py
```

## 📖 Adaptive Lernziele

### 🟢 Beginner-Lernziele

Nach dem Beginner-Pfad können Sie:

- ✅ **Grundlegende Zahlentypen** (int, float, bool) verstehen und verwenden
- ✅ **Einfache String-Operationen** durchführen und f-strings verwenden
- ✅ **Listen und Dictionaries** erstellen und grundlegend verwenden
- ✅ **Einfache Datenkonvertierung** zwischen Typen durchführen
- ✅ **Praktische Berechnungen** für Produktionsdaten durchführen

### 🟡 Intermediate-Lernziele

Nach dem Intermediate-Pfad können Sie zusätzlich:

- ✅ **Alle Zahlentypen** inklusive complex verwenden
- ✅ **Erweiterte String-Verarbeitung** mit Regex und Formatierung
- ✅ **Komplexe Datenstrukturen** verschachteln und manipulieren
- ✅ **Statistische Berechnungen** und Qualitätskontrolle implementieren
- ✅ **Robuste Fehlerbehandlung** bei Datenkonvertierung anwenden
- ✅ **Funktionale Programmierung** mit Datentypen einsetzen

### 🔴 Advanced-Lernziele

Nach dem Advanced-Pfad können Sie zusätzlich:

- ✅ **Objektorientierte Datenmodellierung** mit Dataclasses und Enums
- ✅ **Design Patterns** für numerische Berechnungen implementieren
- ✅ **Performance-Optimierung** und Caching-Strategien anwenden
- ✅ **Enterprise-Level Fehlerbehandlung** und Logging einsetzen
- ✅ **Erweiterte statistische Analysen** und Prozessfähigkeitsindizes berechnen
- ✅ **Professionelle Dokumentation** und Unit Testing durchführen

## 🔧 Datentypen-Übersicht

### Primitive Datentypen

```python
# Zahlen
ganze_zahl = 42                    # int
komma_zahl = 3.14                  # float
komplexe_zahl = 3 + 4j             # complex
boolean_wert = True                # bool

# Text
text = "Bystronic"                 # str
mehrzeiliger_text = """
Mehrere
Zeilen
"""
```

### Collections (Sammlungen)

```python
# Liste (veränderbar)
maschinen = ["Laser", "Presse", "Stanze"]

# Tupel (unveränderbar)
koordinaten = (10, 20)

# Dictionary (Key-Value)
mitarbeiter = {
    "name": "Max Mustermann",
    "abteilung": "Produktion",
    "erfahrung": 5
}

# Set (eindeutige Elemente)
standorte = {"Bern", "Niederönz", "Sulgen"}
```

## 💡 Tipps für VBA-Entwickler

### Arrays vs Python-Listen

```vba
' VBA: Statische Arrays
Dim zahlen(1 To 5) As Integer
zahlen(1) = 10
zahlen(2) = 20
ReDim Preserve zahlen(1 To 10)  ' Umständliche Grössenänderung

' Python: Dynamische Listen
zahlen = [10, 20, 30, 40, 50]
zahlen.append(60)               # Einfach erweitern
zahlen.insert(0, 5)             # An beliebiger Position einfügen
zahlen.remove(20)               # Element entfernen
```

### Collections vs Dictionaries

```vba
' VBA: Collections (nur String-Keys)
Dim mitarbeiter As Collection
Set mitarbeiter = New Collection
mitarbeiter.Add "Max", "ID001"
mitarbeiter.Add "Anna", "ID002"

' Python: Dictionaries (beliebige Key-Typen, verschachtelt)
mitarbeiter = {
    "ID001": {
        "name": "Max",
        "abteilung": "IT",
        "gehalt": 75000,
        "kompetenzen": ["Python", "SQL", "Git"]
    },
    "ID002": {
        "name": "Anna",
        "abteilung": "Produktion",
        "gehalt": 68000,
        "kompetenzen": ["CAD", "Qualitätskontrolle"]
    }
}
```

### Variant vs Python's dynamische Typen

```vba
' VBA: Variant für verschiedene Typen
Dim wert As Variant
wert = 42          ' Integer
wert = "Text"      ' String
wert = True        ' Boolean

' Python: Natürlich dynamisch
wert = 42          # int
wert = "Text"      # str
wert = True        # bool
wert = [1, 2, 3]   # list
wert = {"key": "value"}  # dict
```

## 🔍 Datentyp-Hilfsfunktionen

```python
# Type checking
type(42)           # <class 'int'>
isinstance(42, int)  # True

# Type conversion
int("42")          # 42
float("3.14")      # 3.14
str(42)            # "42"
list("Python")     # ['P', 'y', 't', 'h', 'o', 'n']

# Information
len([1, 2, 3])     # 3
dir(str)           # Alle String-Methoden anzeigen
help(list.append)  # Hilfe zu append-Methode
```

## 🎓 Überprüfen Sie Ihr Verständnis

Bevor Sie zum nächsten Kapitel wechseln:

- [ ] Können Sie alle Python-Grundtypen benennen und verwenden?
- [ ] Verstehen Sie den Unterschied zwischen Listen und Tupeln?
- [ ] Können Sie Dictionaries für strukturierte Daten einsetzen?
- [ ] Beherrschen Sie String-Formatierung und -Manipulation?
- [ ] Können Sie zwischen Datentypen konvertieren?
- [ ] Haben Sie alle vier Übungen erfolgreich gelöst?

## 📊 Praktische Anwendungen für Bystronic

### Maschinendaten verwalten

```python
# Produktionsdaten strukturiert speichern
maschine = {
    "id": "LASER_001",
    "typ": "ByStar Fiber",
    "standort": "Halle A",
    "status": "Aktiv",
    "wartung_faellig": "2024-03-15",
    "produktionszeit": [8.5, 7.2, 9.1, 8.8],  # Stunden pro Tag
    "materialien": {"Stahl", "Aluminium", "Edelstahl"}
}
```

### Qualitätsdaten analysieren

```python
# Messwerte strukturiert erfassen
messungen = [
    {"teil": "P001", "dicke": 2.05, "toleranz": 0.1, "ok": True},
    {"teil": "P002", "dicke": 1.98, "toleranz": 0.1, "ok": True},
    {"teil": "P003", "dicke": 2.15, "toleranz": 0.1, "ok": False}
]

# Statistische Auswertung vorbereiten
dicken = [m["dicke"] for m in messungen]
fehlerhafte_teile = [m for m in messungen if not m["ok"]]
```

## 📝 Zusätzliche Ressourcen

- **Python Data Model**: <https://docs.python.org/3/reference/datamodel.html>
- **Built-in Types**: <https://docs.python.org/3/library/stdtypes.html>
- **Collections Module**: <https://docs.python.org/3/library/collections.html>

## 🎯 Assessment-System

### 📊 Learning Path Assessment

- **Dauer:** 5-7 Minuten
- **Kategorien:** Datentyp-Grundlagen, Mathematik, Programmierung,
  Datenstrukturen, Qualitätskontrolle
- **Ergebnis:** Personalisierte Lernpfad-Empfehlung
- **Speicherung:** Automatische Ergebnis-Dokumentation

### 🔄 Micro-Assessments (in Entwicklung)

- **Quiz:** Interaktive Wissensprüfung
- **Challenges:** Praktische Code-Aufgaben
- **Reflection:** Selbsteinschätzung und Lernfortschritt
- **Dashboard:** Übersicht über alle Assessment-Ergebnisse

## 🎓 Lernfortschritt überprüfen

### 🟢 Beginner-Checkliste

- [ ] Können Sie int, float und bool unterscheiden und verwenden?
- [ ] Verstehen Sie f-string Formatierung?
- [ ] Können Sie einfache Listen und Dictionaries erstellen?
- [ ] Beherrschen Sie grundlegende Datenkonvertierung?
- [ ] Haben Sie alle Beginner-Übungen erfolgreich gelöst?

### 🟡 Intermediate-Checkliste

- [ ] Können Sie mit allen Zahlentypen inklusive complex arbeiten?
- [ ] Beherrschen Sie erweiterte String-Operationen und Regex?
- [ ] Können Sie komplexe, verschachtelte Datenstrukturen verwenden?
- [ ] Verstehen Sie statistische Berechnungen und Qualitätskontrolle?
- [ ] Können Sie robuste Fehlerbehandlung implementieren?
- [ ] Haben Sie alle Intermediate-Übungen erfolgreich gelöst?

### 🔴 Advanced-Checkliste

- [ ] Können Sie objektorientierte Datenmodelle mit Dataclasses erstellen?
- [ ] Beherrschen Sie Design Patterns für numerische Berechnungen?
- [ ] Verstehen Sie Performance-Optimierung und Caching?
- [ ] Können Sie Enterprise-Level Logging und Fehlerbehandlung implementieren?
- [ ] Beherrschen Sie erweiterte statistische Analysen?
- [ ] Haben Sie alle Advanced-Übungen erfolgreich gelöst?

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels:
**→ [Kapitel 3: NumPy für numerische Berechnungen](../03_numpy/README.md)**

---

## 📊 Dieses Kapitel ist Teil des adaptiven Python Grundkurses für Bystronic-Entwickler
