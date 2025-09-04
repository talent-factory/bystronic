# NumPy Tests - test_03_numpy.py

Diese Test-Suite validiert die Funktionalität aller NumPy-Beispiele und
demonstriert bewährte Test-Patterns für numerische Berechnungen.

## 📋 Test-Übersicht

### **TestArraysDemo** (6 Tests)

- ✅ **Modul-Import**: Grundlegende Importfähigkeit
- ✅ **Main-Funktion**: Existenz und Ausführbarkeit
- ✅ **Array-Erstellung**: Verschiedene Erstellungsmethoden (zeros, ones, arange,
  linspace)
- ✅ **2D-Arrays**: Mehrdimensionale Operationen und Boolean-Indexing
- ✅ **Koordinatenberechnungen**: Geometrische Berechnungen für CNC-Anwendungen

### **TestMathematicalOperations** (7 Tests)

- ✅ **Vektorisierte Operationen**: Grundrechenarten mit Arrays
- ✅ **Trigonometrische Funktionen**: sin, cos, tan und trigonometrische
  Identitäten
- ✅ **Statistische Funktionen**: Mittelwert, Standardabweichung, Perzentile
- ✅ **Prozessfähigkeit**: Cp/Cpk-Berechnungen für Qualitätskontrolle
- ✅ **Exponentialfunktionen**: exp, log, ln für technische Berechnungen

### **TestArrayManipulation** (8 Tests)

- ✅ **Reshaping**: Array-Formänderungen und automatische Dimensionierung
- ✅ **Transponierung**: Matrix-Transposition und Doppeltransposition
- ✅ **Concatenation**: hstack, vstack, concatenate Operationen
- ✅ **Splitting**: hsplit, vsplit Array-Aufspaltung
- ✅ **Broadcasting**: Automatische Shape-Anpassung verschiedener Array-Größen
- ✅ **Boolean-Indexing**: Filteroperationen mit logischen Bedingungen
- ✅ **Advanced Indexing**: Fancy Indexing, argmax, argmin

### **TestLinearAlgebra** (8 Tests)

- ✅ **Matrix-Operationen**: Multiplikation, Addition, Transposition
- ✅ **Matrix-Eigenschaften**: Determinante, Spur, Rang
- ✅ **Lineare Gleichungssysteme**: Lösung von A @ x = b Systemen
- ✅ **Matrix-Inversion**: Berechnung und Verifikation von A^(-1)
- ✅ **Eigenwerte/Eigenvektoren**: Berechnung und Verifikation (A @ v = λ @ v)
- ✅ **Geometrische Transformationen**: Rotation, Translation,
  Koordinatentransformation
- ✅ **QR-Zerlegung**: Orthogonalisierung und Rekonstruktion
- ✅ **SVD**: Singulärwertzerlegung für Dimensionsreduktion

### **TestVBAvsNumPy** (5 Tests)

- ✅ **Performance-Konzepte**: Vektorisierung vs. Schleifen
- ✅ **Matrix-Vergleiche**: NumPy @ vs. manuelle Triple-Loop
- ✅ **Statistische Operationen**: NumPy-Funktionen vs. manuelle Berechnung

### **TestNumpyPerformanceAndAccuracy** (6 Tests)

- ✅ **Speicher-Layout**: C-contiguous vs. Fortran-contiguous Arrays
- ✅ **Datentyp-Präzision**: float32 vs. float64 Unterschiede
- ✅ **Numerische Stabilität**: Umgang mit großen/kleinen Zahlen
- ✅ **NaN/Inf-Handling**: Behandlung spezieller Fließkomma-Werte
- ✅ **Zufallszahlen-Reproduzierbarkeit**: Seed-basierte Wiederholbarkeit
- ✅ **Edge Cases**: Leere Arrays, Ein-Element-Arrays, Division durch Null

## 🚀 Tests ausführen

### Alle NumPy-Tests

```bash
uv run python -m pytest tests/test_03_numpy.py -v
```

### Spezifische Test-Klasse

```bash
uv run python -m pytest tests/test_03_numpy.py::TestArraysDemo -v
```

### Einzelner Test

```bash
uv run python -m pytest tests/test_03_numpy.py::TestMathematicalOperations::test_trigonometric_functions -v
```

### Mit Coverage-Report

```bash
uv run python -m pytest tests/test_03_numpy.py --cov=src/03_numpy --cov-report=html
```

## 📊 Test-Coverage

Aktuelle Coverage: **98%** (703/714 Statements)

**Nicht getestete Zeilen:**

- `if __name__ == "__main__":` Blöcke in main() Funktionen
- Einzelne Ausnahmebehandlungen in komplexen Berechnungen

## 🎯 Test-Patterns für numerische Berechnungen

### **Numerische Toleranzen**

```python
# Für Fließkomma-Vergleiche
assert np.allclose(result, expected, atol=1e-10)

# Für relative Toleranzen
assert abs(result - expected) / expected < 1e-15
```

### **Matrix-Verifikationen**

```python
# Einheitsmatrix-Check
identity = A @ A_inv
assert np.allclose(identity, np.eye(n))

# Eigenwert-Verifikation
left_side = A @ eigenvector
right_side = eigenvalue * eigenvector
assert np.allclose(left_side, right_side)
```

### **Array-Shape-Tests**

```python
# Shape-Validierung
assert array.shape == (expected_rows, expected_cols)
assert array.ndim == expected_dimensions
assert array.size == expected_total_elements
```

### **Statistical-Tests**

```python
# Plausibilitätschecks für statistische Werte
assert expected_min < mean < expected_max
assert std > 0  # Standardabweichung immer positiv
assert quartile_25 < median < quartile_75
```

### **Edge-Case-Handling**

```python
# NaN/Inf-Tests
assert np.isnan(result_with_nan)
assert np.isinf(result_with_inf)
assert np.isfinite(normal_result)

# Leere Arrays
empty = np.array([])
assert empty.size == 0
assert empty.shape == (0,)
```

## 🔧 Test-Dependencies

Die Tests verwenden folgende Bibliotheken:

- **pytest**: Test-Framework
- **numpy**: Hauptbibliothek (wird getestet)
- **warnings**: Für Warning-Unterdrückung bei numerischen Edge Cases
- **unittest.mock**: Für Print-Output-Tests
- **sys/pathlib**: Für dynamische Modul-Imports

## 📈 Qualitätssicherung

Diese Tests gewährleisten:

1. **Funktionale Korrektheit**: Alle mathematischen Operationen liefern
   erwartete Ergebnisse
1. **Numerische Stabilität**: Robuster Umgang mit Edge Cases und speziellen
   Werten
1. **Performance-Validierung**: Verifikation der vektorisierten Operationen
1. **Industrielle Anwendbarkeit**: Tests basieren auf realen
   Bystronic-Anwendungsfällen
1. **Lehrwert**: Tests dienen als Referenz für Best Practices

## 🎓 Lernziele der Tests

- **NumPy-Test-Patterns**: Wie man numerische Berechnungen korrekt testet
- **Toleranz-Management**: Umgang mit Fließkomma-Ungenauigkeiten
- **Matrix-Validierung**: Verifikation linearer Algebra Operationen
- **Edge-Case-Testing**: Robuste Behandlung von Grenzfällen
- **Performance-Testing**: Konzepte für Geschwindigkeits-Vergleiche

Diese Tests sind ein integraler Bestandteil des NumPy-Lernmoduls und
demonstrieren professionelle Test-Praktiken für numerische Software! 🧪✨
