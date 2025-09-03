# Datentypen Tests - test_02_datentypen.py

Diese Test-Suite validiert die Funktionalität der Datentypen-Beispiele und demonstriert bewährte Test-Patterns für numerische Berechnungen und Datenverarbeitung.

## 📋 Test-Übersicht

### **TestNumbersDemo** (8 Tests)
- ✅ **Funktion-Existenz**: Überprüft Verfügbarkeit der main() Funktion
- ✅ **Ausführbarkeit**: Testet fehlerfreie Ausführung mit Mock-Input/Output
- ✅ **Math-Operationen**: Validiert demonstrate_math_operations() Funktion
- ✅ **Produktionsmetriken**: Testet calculate_production_metrics() mit Effizienz-Berechnung
- ✅ **Materialverbrauch**: Validiert calculate_material_usage() Funktion
- ✅ **Laser-Parameter**: Testet calculate_laser_parameters() Funktion
- ✅ **Mathematische Berechnungen**: Schnittzeit, Materialausnutzung, komplexe Berechnungen
- ✅ **Komplexe Zahlen**: Impedanz-Berechnungen für Elektrotechnik-Anwendungen

### **TestStringsDemo** (4 Tests)
- ✅ **Funktion-Existenz**: Überprüft Verfügbarkeit der main() Funktion
- ✅ **Ausführbarkeit**: Testet fehlerfreie Ausführung
- ✅ **String-Operationen**: Validiert upper/lower, strip, split, f-strings
- ✅ **Bystronic-Beispiele**: Maschinennamen-Parsing und -Verarbeitung

### **TestCollectionsDemo** (6 Tests)
- ✅ **Funktion-Existenz**: Überprüft Verfügbarkeit der main() Funktion
- ✅ **Ausführbarkeit**: Testet fehlerfreie Ausführung
- ✅ **Listen-Operationen**: append, extend, Filterung, List Comprehensions
- ✅ **Dictionary-Operationen**: Zugriff, Updates, keys/values/items Methoden
- ✅ **Tuple-Operationen**: Indexing, Unpacking, Unveränderlichkeit
- ✅ **Set-Operationen**: Intersection, Union, Membership-Tests

### **TestDataTypeIntegration** (3 Tests)
- ✅ **Numerische Präzision**: Fließkomma-Genauigkeit und Toleranzberechnungen
- ✅ **Typ-Konvertierungen**: String↔Number, Boolean-Casting
- ✅ **Gesamtausführung**: Alle Beispiele zusammen testen

### **Einzelne Test-Funktionen** (2 Tests)
- ✅ **Modul-Imports**: Testet korrekte Importierbarkeit aller Module
- ✅ **Datei-Existenz**: Überprüft Verfügbarkeit der Beispieldateien

## 🚀 Tests ausführen

### Alle Datentypen-Tests
```bash
uv run python -m pytest tests/test_02_datentypen.py -v
```

### Spezifische Test-Klasse
```bash
uv run python -m pytest tests/test_02_datentypen.py::TestNumbersDemo -v
```

### Einzelner Test
```bash
uv run python -m pytest tests/test_02_datentypen.py::TestCollectionsDemo::test_dictionary_operations -v
```

### Mit Coverage-Report
```bash
uv run python -m pytest tests/test_02_datentypen.py --cov=src/02_datentypen --cov-report=html
```

## 🎯 Test-Patterns für Datentypen

### **Numerische Präzisions-Tests**
```python
def test_numeric_precision(self):
    # Fließkomma-Vergleiche mit Toleranz
    result = 0.1 + 0.2
    assert abs(result - 0.3) < 1e-10
```

### **Komplexe Zahlen-Tests**
```python
def test_complex_numbers(self):
    impedanz = 50 + 30j
    strom = 10 + 0j
    spannung = impedanz * strom
    assert spannung == 500 + 300j
```

### **String-Operationen-Tests**
```python
def test_string_operations(self):
    maschinen_name = "LASER_01_BYSTAR_FIBER"
    assert maschinen_name.startswith("LASER")
    teile = maschinen_name.split("_")
    assert len(teile) >= 3
```

### **Collection-Tests**
```python
def test_list_operations(self):
    laser_maschinen = [m for m in maschinen if m.startswith("LASER")]
    assert len(laser_maschinen) == 2
```

### **Source-Code-Analyse**
```python
def test_code_contains_patterns(self):
    import inspect
    source = inspect.getsource(module)
    assert 'f"' in source, "f-strings fehlen"
```

## 📊 Industrielle Anwendungen

Die Tests validieren typische Bystronic-Berechnungen:

### **Produktionsmetriken**
- Effizienz-Berechnung: `(produziert / geplant) * 100`
- Materialausnutzung: `(Teil-Fläche * Anzahl) / Blech-Fläche * 100`

### **Laser-Berechnungen**
- Schnittzeit: `Länge / Geschwindigkeit`
- Materialdicke-Toleranzen: `±0.1mm Genauigkeit`

### **Maschinendaten-Verarbeitung**
- Maschinennamen-Parsing: `"LASER_01_BYSTAR_FIBER".split("_")`
- Typisierung und Kategorisierung von Maschinendaten

## 🔧 Test-Dependencies

Die Tests verwenden folgende Bibliotheken:
- **pytest**: Test-Framework
- **unittest.mock**: Für Input/Output-Mocking
- **math**: Für mathematische Berechnungen und Vergleiche
- **inspect**: Für Source-Code-Analyse
- **pathlib/sys**: Für dynamische Modul-Imports

## 📈 Qualitätssicherung

Diese Tests gewährleisten:

1. **Datentyp-Korrektheit**: Alle Python-Datentypen werden korrekt verwendet
2. **Numerische Stabilität**: Fließkomma-Berechnungen mit Toleranzen
3. **String-Verarbeitung**: Robuste Text-Manipulation für Maschinendaten
4. **Collection-Handling**: Sichere Verwendung von Listen, Sets, Dictionaries
5. **Industrielle Anwendbarkeit**: Tests basieren auf realen Bystronic-Szenarien

## 🎓 Lernziele der Tests

- **Typ-System**: Verständnis für Python-Datentypen und ihre Eigenschaften
- **Numerische Präzision**: Umgang mit Fließkomma-Ungenauigkeiten
- **String-Manipulation**: Parsing und Formatierung von Textdaten
- **Collections**: Effiziente Nutzung von Listen, Dictionaries, Sets, Tuples
- **Typ-Konvertierungen**: Sichere Umwandlung zwischen Datentypen
- **Source-Code-Tests**: Analyse von Code-Qualität und -Patterns

Diese Tests bilden das Fundament für sicheres und effizientes Arbeiten mit Python-Datentypen! 🔢✨
