# 💡 NumPy Examples

## Übersicht

Diese Examples demonstrieren NumPy-Konzepte mit praxisrelevanten
SmartFactory-Anwendungen. Alle Beispiele sind vollständig ausführbar und
erklären die Konzepte schrittweise.

## 📁 Verfügbare Examples

### 1. Array-Grundlagen

**Datei:** `arrays_basic.py` **Dauer:** 10-15 Minuten **Inhalt:**

- Array-Erstellung mit verschiedenen Methoden
- Array-Eigenschaften und Datentypen
- Grundlegende Operationen
- Indexing und Slicing
- Mehrdimensionale Arrays

**Lernziele:**

- NumPy-Arrays erstellen und verstehen
- Unterschied zu Python-Listen erkennen
- Erste vektorisierte Operationen anwenden

```bash
uv run python src/03_numpy/examples/arrays_basic.py
```

### 2. Mathematische Operationen

**Datei:** `mathematical_operations.py` **Dauer:** 15-20 Minuten **Inhalt:**

- Grundrechenarten (vektorisiert)
- Trigonometrische Funktionen
- Statistische Funktionen
- Aggregationen und Reduzierungen
- Broadcasting-Grundlagen

**Lernziele:**

- Vektorisierte Operationen verstehen
- Mathematische NumPy-Funktionen anwenden
- Broadcasting-Konzept kennenlernen

```bash
uv run python src/03_numpy/examples/mathematical_operations.py
```

### 3. Array-Manipulation

**Datei:** `array_manipulation.py` **Dauer:** 15-20 Minuten **Inhalt:**

- Reshaping und Transponierung
- Concatenation und Splitting
- Erweiterte Indexing-Techniken
- Boolean Indexing
- Array-Stacking

**Lernziele:**

- Arrays flexibel umformen
- Komplexe Indexing-Operationen
- Arrays effizient kombinieren

```bash
uv run python src/03_numpy/examples/array_manipulation.py
```

### 4. Lineare Algebra

**Datei:** `linear_algebra.py` **Dauer:** 20-25 Minuten **Inhalt:**

- Matrix-Operationen
- Gleichungssysteme lösen
- Eigenwerte und Eigenvektoren
- Geometrische Transformationen
- CNC-relevante Berechnungen

**Lernziele:**

- Matrix-Operationen beherrschen
- Lineare Gleichungssysteme lösen
- Koordinatentransformationen für CNC

```bash
uv run python src/03_numpy/examples/linear_algebra.py
```

### 5. VBA vs NumPy

**Datei:** `vba_vs_numpy.py` **Dauer:** 10-15 Minuten **Inhalt:**

- Direkte Vergleiche VBA ↔ NumPy
- Performance-Unterschiede
- Syntax-Vergleiche
- Migrationstipps

**Lernziele:**

- VBA-Kenntnisse zu NumPy übertragen
- Performance-Vorteile verstehen
- Umstiegshilfen nutzen

```bash
uv run python src/03_numpy/examples/vba_vs_numpy.py
```

### 6. Performance-Vergleich

**Datei:** `performance_comparison.py` **Dauer:** 15-20 Minuten **Inhalt:**

- Umfassende Performance-Benchmarks
- Memory-Verbrauchsanalyse
- Skalierbarkeits-Tests
- Real-World SmartFactory-Szenarien

**Lernziele:**

- Performance-Vorteile quantifizieren
- Memory-Effizienz verstehen
- Anwendung auf reale Probleme

```bash
uv run python src/03_numpy/examples/performance_comparison.py
```

## 🎯 Empfohlene Reihenfolge

### Für Beginner

1. `arrays_basic.py` - Fundament legen
1. `mathematical_operations.py` - Erste Berechnungen
1. `vba_vs_numpy.py` - Vergleich zu bekannten Konzepten
1. `performance_comparison.py` - Motivation durch Performance

### Für Intermediate

1. `mathematical_operations.py` - Auffrischung
1. `array_manipulation.py` - Erweiterte Techniken
1. `linear_algebra.py` - Matrix-Operationen
1. `performance_comparison.py` - Optimierungsaspekte

### Für Advanced

1. `performance_comparison.py` - Performance-Fokus
1. `linear_algebra.py` - Numerische Algorithmen
1. Eigene Implementierungen basierend auf Examples

## 📊 SmartFactory-Integration

### Produktionsrelevante Themen

- **Qualitätskontrolle:** Toleranzprüfungen, SPC, Cp/Cpk-Werte
- **CNC-Programmierung:** Koordinatentransformationen, Geometrie
- **Datenanalyse:** Trend-Erkennung, Korrelationen, Statistik
- **Performance:** Echtzeit-Verarbeitung, Memory-Effizienz

### Realitätsnahe Daten

- Maschinenlaufzeiten und Produktionszahlen
- Qualitätsmessungen mit realistischen Toleranzen
- CNC-Koordinaten und Transformationen
- Sensor- und IoT-Daten

## 🔧 Technische Hinweise

### Anforderungen

```bash
# NumPy ist bereits in den Projektabhängigkeiten
uv sync
```

### Interaktive Ausführung

Alle Examples können auch in Jupyter Notebooks ausgeführt werden:

```bash
uv run jupyter notebook
# Dann Examples kopieren und einzeln ausführen
```

### Debugging-Tipps

```python
# Array-Eigenschaften prüfen
print(f"Shape: {arr.shape}")
print(f"Dtype: {arr.dtype}")
print(f"Size: {arr.size}")
print(f"Memory: {arr.nbytes} bytes")

# Wertebereich prüfen
print(f"Min/Max: {arr.min():.3f} / {arr.max():.3f}")
print(f"Mean: {arr.mean():.3f}")
```

## 📈 Performance-Monitoring

### Zeitmessungen

```python
import time

start = time.time()
# NumPy-Operation
result = np.operation(data)
duration = time.time() - start
print(f"Duration: {duration:.4f}s")
```

### Memory-Monitoring

```python
import sys

# Memory-Verbrauch prüfen
memory_mb = sys.getsizeof(array) / (1024 * 1024)
print(f"Memory: {memory_mb:.2f} MB")
```

## 🎓 Lernziele der Examples

### Nach allen Examples können Sie

- ✅ **Arrays effizient** erstellen und manipulieren
- ✅ **Vektorisierte Operationen** statt Schleifen verwenden
- ✅ **Performance-Vorteile** von NumPy quantifizieren
- ✅ **Broadcasting-Regeln** verstehen und anwenden
- ✅ **Matrix-Operationen** für technische Berechnungen
- ✅ **Memory-effiziente** Programmierung betreiben
- ✅ **VBA-Kenntnisse** zu NumPy übertragen
- ✅ **Real-World Probleme** mit NumPy lösen

## 🔗 Weiterführende Links

- **NumPy Documentation:** <https://numpy.org/doc/stable/>
- **Performance Guide:** <https://numpy.org/doc/stable/user/performance.html>
- **Broadcasting Rules:**
  <https://numpy.org/doc/stable/user/basics.broadcasting.html>

## 💡 Tipps für eigene Projekte

### Code-Organisation

```python
import numpy as np

# Verwenden Sie aussagekräftige Variablennamen
production_data = np.array([...])
quality_measurements = np.array([...])

# Dokumentieren Sie Array-Shapes
# production_data.shape = (days, machines, hours)
# quality_measurements.shape = (parts, measurements_per_part)
```

### Performance-Optimierung

```python
# Vermeiden Sie Schleifen, nutzen Sie Vektorisierung
# Schlecht:
result = []
for value in array:
    result.append(value ** 2)

# Gut:
result = array ** 2

# Nutzen Sie In-Place-Operationen wenn möglich
array *= 2  # statt array = array * 2
```

### Fehlerbehandlung

```python
# Prüfen Sie Array-Shapes vor Operationen
if array1.shape != array2.shape:
    raise ValueError(f"Shape mismatch: {array1.shape} vs {array2.shape}")

# Behandeln Sie Division durch Null
result = np.divide(a, b, out=np.zeros_like(a), where=b!=0)
```

______________________________________________________________________

## 🎯 Diese Examples sind der praktische Einstieg in die NumPy-Welt für SmartFactory-Entwickler
