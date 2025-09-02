# Kapitel 2: Datentypen und Datenstrukturen

Willkommen zum zweiten Kapitel des Python Grundkurses für Bystronic-Entwickler! 📊

## 📚 Inhalte dieses Kapitels

### Hauptdokumentation
- **[02_datentypen.ipynb](02_datentypen.ipynb)** - Interaktives Jupyter Notebook mit allen Datentypen

### 💡 Beispiele
- **[numbers_demo.py](beispiele/numbers_demo.py)** - Zahlen und mathematische Operationen
- **[strings_demo.py](beispiele/strings_demo.py)** - String-Manipulation und Formatierung
- **[collections_demo.py](beispiele/collections_demo.py)** - Listen, Dictionaries, Sets und Tupel
- **[vba_collections_comparison.py](beispiele/vba_collections_comparison.py)** - VBA vs Python Collections

### 🎯 Übungen
- **[Übung 1: Zahlenoperationen](uebungen/uebung_01_zahlen.py)** - Arbeiten mit int, float, complex
- **[Übung 2: String-Verarbeitung](uebungen/uebung_02_strings.py)** - Textmanipulation und Formatierung
- **[Übung 3: Listen und Dictionaries](uebungen/uebung_03_collections.py)** - Datenstrukturen beherrschen
- **[Übung 4: Datenkonvertierung](uebungen/uebung_04_conversion.py)** - Type Casting und Validierung

## 🚀 Schnellstart

### 1. Umgebung einrichten
```bash
# Im Projektverzeichnis
uv sync
uv shell
```

### 2. Jupyter Notebook starten
```bash
# Haupttutorial öffnen
uv run jupyter notebook src/02_datentypen/02_datentypen.ipynb
```

### 3. Beispiele ausführen
```bash
# Zahlen-Beispiele
uv run python src/02_datentypen/beispiele/numbers_demo.py

# String-Beispiele
uv run python src/02_datentypen/beispiele/strings_demo.py

# Collections-Beispiele
uv run python src/02_datentypen/beispiele/collections_demo.py

# VBA-Vergleich
uv run python src/02_datentypen/beispiele/vba_collections_comparison.py
```

### 4. Übungen bearbeiten
```bash
# Übung 1 - Zahlenoperationen
uv run python src/02_datentypen/uebungen/uebung_01_zahlen.py

# Übung 2 - String-Verarbeitung
uv run python src/02_datentypen/uebungen/uebung_02_strings.py

# Übung 3 - Listen und Dictionaries
uv run python src/02_datentypen/uebungen/uebung_03_collections.py

# Übung 4 - Datenkonvertierung
uv run python src/02_datentypen/uebungen/uebung_04_conversion.py
```

## 📖 Lernziele

Nach diesem Kapitel können Sie:

✅ **Zahlentypen**: int, float, complex verstehen und verwenden  
✅ **Strings**: Texte manipulieren, formatieren und durchsuchen  
✅ **Listen**: Dynamische Arrays erstellen und bearbeiten  
✅ **Dictionaries**: Key-Value-Paare für strukturierte Daten nutzen  
✅ **Sets**: Eindeutige Elemente verwalten und Mengenoperationen durchführen  
✅ **Tupel**: Unveränderliche Datenstrukturen verwenden  
✅ **Konvertierung**: Zwischen Datentypen wechseln und validieren  
✅ **Collections**: Komplexe Datenstrukturen verschachteln  

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

- **Python Data Model**: https://docs.python.org/3/reference/datamodel.html
- **Built-in Types**: https://docs.python.org/3/library/stdtypes.html
- **Collections Module**: https://docs.python.org/3/library/collections.html

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels:
**→ [Kapitel 3: NumPy für numerische Berechnungen](../03_numpy/README.md)**

---
*Dieses Kapitel ist Teil des Python Grundkurses für Bystronic-Entwickler*