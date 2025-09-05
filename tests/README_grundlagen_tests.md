# Grundlagen Tests - test_01_grundlagen.py

Diese Test-Suite validiert die Funktionalität der Python-Grundlagen-Beispiele
und demonstriert bewährte Test-Patterns für Python-Anfänger.

**🔄 AKTUALISIERT für neue adaptive Struktur:**
- Tests angepasst für `examples/` statt `beispiele/`
- Neue Assessment-Tests hinzugefügt
- Kompatibel mit 3-Tier-Lernsystem

## 📋 Test-Übersicht

### **TestHelloWorld** (4 Tests)

- ✅ **Funktion-Existenz**: Überprüft, ob main() Funktion vorhanden und aufrufbar
  ist
- ✅ **Ausführbarkeit**: Testet fehlerfreie Ausführung mit Mock-Input/Output
- ✅ **String-Formatierung**: Validiert korrekte Ausgabe und f-string Verwendung
- ✅ **Berechnungslogik**: Testet Arbeitsstunden-Berechnung (8h × 5d × 52w =
  2080h)

### **TestVbaVsPython** (6 Tests)

- ✅ **Funktion-Existenz**: Überprüft Verfügbarkeit aller Hauptfunktionen
- ✅ **Ausführbarkeit**: Testet fehlerfreie Ausführung der main() Funktion
- ✅ **Listen-Demonstrationen**: Validiert demonstriere_listen() Funktion
- ✅ **Dictionary-Demonstrationen**: Validiert demonstriere_dictionaries()
  Funktion
- ✅ **Listen-Operationen**: Testet append, extend, List Comprehensions,
  Filterung
- ✅ **Mathematische Operationen**: Testet sum, max, min, Durchschnitt mit Listen

### **TestIntegration** (2 Tests)

- ✅ **Gesamtausführung**: Testet alle Beispiele zusammen
- ✅ **Lernkonzepte-Abdeckung**: Validiert, dass wichtige Python-Konzepte
  enthalten sind

### **Einzelne Test-Funktionen** (2 Tests)

- ✅ **Modul-Imports**: Testet korrekte Importierbarkeit aller Module
- ✅ **Datei-Existenz**: Überprüft Verfügbarkeit der Beispieldateien

## 🚀 Tests ausführen

### Alle Grundlagen-Tests

```bash
uv run python -m pytest tests/test_01_grundlagen.py -v
```

### Spezifische Test-Klasse

```bash
uv run python -m pytest tests/test_01_grundlagen.py::TestHelloWorld -v
```

### Einzelner Test

```bash
uv run python -m pytest tests/test_01_grundlagen.py::TestVbaVsPython::test_list_operations_logic -v
```

### Mit Coverage-Report

```bash
uv run python -m pytest tests/test_01_grundlagen.py --cov=src/01_grundlagen --cov-report=html
```

## 🎯 Test-Patterns für Python-Anfänger

### **Mock-basierte Tests**

```python
@patch("builtins.input", return_value="Test User")
@patch("builtins.print")
def test_user_interaction(self, mock_print, mock_input):
    # Testet Benutzerinteraktion ohne echte Ein-/Ausgabe
    function_under_test()
    assert mock_print.called
    assert mock_input.called
```

### **Ausgabe-Validierung**

```python
# Sammle alle print-Aufrufe
print_calls = [call[0][0] for call in mock_print.call_args_list]

# Überprüfe spezifische Ausgaben
welcome_found = any("Willkommen" in call for call in print_calls)
assert welcome_found, "Willkommensnachricht nicht gefunden"
```

### **Funktions-Existenz-Tests**

```python
def test_function_exists(self):
    assert hasattr(module, "function_name")
    assert callable(module.function_name)
```

### **Logik-Validierung**

```python
def test_calculation_logic(self):
    # Simuliere Berechnungen aus den Beispielen
    result = calculate_something(input_values)
    assert result == expected_value
```

## 🔧 Test-Dependencies

Die Tests verwenden folgende Bibliotheken:

- **pytest**: Test-Framework
- **unittest.mock**: Für Input/Output-Mocking und Patch-Funktionalität
- **pathlib/sys**: Für dynamische Modul-Imports und Pfad-Management

## 📈 Qualitätssicherung

Diese Tests gewährleisten:

1. **Funktionale Korrektheit**: Alle Grundlagen-Funktionen arbeiten wie erwartet
1. **Robustheit**: Tests funktionieren unabhängig von Benutzeringaben
1. **Lehrwert**: Tests demonstrieren wichtige Python-Konzepte für Anfänger
1. **VBA-Migration**: Tests validieren den Übergang von VBA zu Python-Patterns

## 🎓 Lernziele der Tests

- **Mocking-Konzepte**: Wie man Benutzereingaben und Ausgaben testet
- **Funktions-Tests**: Überprüfung von Funktionsexistenz und -aufrufbarkeit
- **String-Validierung**: Tests für formatierte Ausgaben und f-strings
- **Listen-Operationen**: Validierung von Python-Listen vs. VBA-Arrays
- **Integration-Tests**: Wie man mehrere Module zusammen testet

Diese Tests sind der Einstiegspunkt für das Erlernen von Test-Driven Development
in Python! 🐍✨

## 🆕 Assessment-Tests

### **test_01_grundlagen_assessments.py**

Zusätzliche Tests für die neuen Assessment-Tools:

- ✅ **LearningPathAssessment**: Tests für Eingangsassessment und Lernpfad-Bestimmung
- ✅ **MicroAssessmentQuiz**: Tests für interaktives Quiz-System
- ✅ **MicroAssessmentChallenges**: Tests für praktische Code-Challenges
- ✅ **MicroAssessmentReflection**: Tests für Selbstreflexions-Tool
- ✅ **MicroAssessmentDashboard**: Tests für zentrales Dashboard

### Assessment-Tests ausführen

```bash
uv run python -m pytest tests/test_01_grundlagen_assessments.py -v
```

### Alle Grundlagen-Tests zusammen

```bash
uv run python -m pytest tests/test_01_grundlagen*.py -v
```

## 📊 Test-Abdeckung

Die Tests decken jetzt ab:
- **Beispiele** (`examples/`): hello_world.py, vba_vs_python.py
- **Assessment-Tools** (`assessments/`): 5 interaktive Tools
- **Struktur-Validierung**: Neue adaptive Verzeichnisstruktur
- **Integration**: Zusammenspiel aller Komponenten
