# 📊 Kapitel 3: NumPy für numerische Berechnungen

## Adaptives Lernsystem für heterogene Lerngruppen

Willkommen zum dritten Kapitel des Python Grundkurses für Bystronic-Entwickler!
Dieses Kapitel verwendet ein **3-stufiges adaptives Lernsystem**, das sich an
Ihr Vorwissen anpasst und NumPy als mächtigste Python-Bibliothek für numerische
Berechnungen vermittelt.

## 🎯 Adaptive Lernpfade

### 🔍 Schritt 1: Assessment durchführen

```bash
# Bestimmen Sie Ihren optimalen Lernpfad (7-10 Minuten)
uv run python src/03_numpy/assessments/learning_path_assessment.py
```

### 📚 Schritt 2: Ihren Lernpfad wählen

#### 🟢 Beginner-Pfad (0-35 Punkte)

**Zielgruppe:** NumPy-Einsteiger, Grundlagen der numerischen Programmierung
**Dauer:** 20-30 Minuten pro Übung **Fokus:** Array-Grundlagen, einfache
Operationen, Bystronic-Anwendungen

#### 🟡 Intermediate-Pfad (36-65 Punkte)

**Zielgruppe:** Programmiererfahrung, erweiterte Datenanalyse **Dauer:** 30-45
Minuten pro Übung **Fokus:** Statistische Analysen, Broadcasting, lineare
Algebra

#### 🔴 Advanced-Pfad (66-100 Punkte)

**Zielgruppe:** Erfahrene Entwickler, Enterprise-Anwendungen **Dauer:** 45-60
Minuten pro Übung **Fokus:** Algorithmus-Optimierung, komplexe Analysen,
Integration

## 📁 Neue Struktur

### 🎓 Theory & Documentation

- **[theory/03_numpy.ipynb](theory/03_numpy.ipynb)** - Interaktives Jupyter
  Notebook mit allen NumPy-Konzepten

### 💡 Examples (für alle Levels)

- **[arrays_basic.py](examples/arrays_basic.py)** - Array-Grundlagen und erste
  Operationen
- **[mathematical_operations.py](examples/mathematical_operations.py)** -
  Mathematische Funktionen und Berechnungen
- **[array_manipulation.py](examples/array_manipulation.py)** - Reshaping,
  Slicing und Indexing
- **[linear_algebra.py](examples/linear_algebra.py)** - Lineare Algebra
  Operationen
- **[vba_vs_numpy.py](examples/vba_vs_numpy.py)** - Vergleich Excel/VBA zu NumPy
- **[performance_comparison.py](examples/performance_comparison.py)** -
  Performance-Demonstrationen

### 🎯 Adaptive Exercises

#### 🟢 Beginner Exercises

- **[uebung_01_arrays_beginner.py](exercises/beginner/uebung_01_arrays_beginner.py)**
  \- Array-Grundlagen und erste Schritte
- **[uebung_02_mathematik_beginner.py](exercises/beginner/uebung_02_mathematik_beginner.py)**
  \- Einfache mathematische Operationen
- **[uebung_03_manipulation_beginner.py](exercises/beginner/uebung_03_manipulation_beginner.py)**
  \- Grundlegende Array-Manipulation
- **[uebung_04_bystronic_daten_beginner.py](exercises/beginner/uebung_04_bystronic_daten_beginner.py)**
  \- Praktische Produktionsdaten-Verarbeitung

#### 🟡 Intermediate Exercises

- **[uebung_01_arrays_intermediate.py](exercises/intermediate/uebung_01_arrays_intermediate.py)**
  \- Erweiterte Array-Operationen und Broadcasting
- **[uebung_02_statistik_intermediate.py](exercises/intermediate/uebung_02_statistik_intermediate.py)**
  \- Statistische Prozesskontrolle (SPC)
- **[uebung_03_linalg_intermediate.py](exercises/intermediate/uebung_03_linalg_intermediate.py)**
  \- Lineare Algebra und Matrix-Operationen
- **[uebung_04_produktionsanalyse_intermediate.py](exercises/intermediate/uebung_04_produktionsanalyse_intermediate.py)**
  \- Erweiterte Maschinendaten-Analyse

#### 🔴 Advanced Exercises

- **[uebung_01_performance_advanced.py](exercises/advanced/uebung_01_performance_advanced.py)**
  \- Performance-Optimierung und Profiling
- **[uebung_02_algorithmen_advanced.py](exercises/advanced/uebung_02_algorithmen_advanced.py)**
  \- Numerische Algorithmen und Eigenwert-Probleme
- **[uebung_03_optimierung_advanced.py](exercises/advanced/uebung_03_optimierung_advanced.py)**
  \- Optimierungsverfahren und Curve Fitting
- **[uebung_04_enterprise_analytics_advanced.py](exercises/advanced/uebung_04_enterprise_analytics_advanced.py)**
  \- Enterprise-Level Analytics und Big Data

### 🆘 4-Stufen-Hilfesystem

Für jede Übung verfügbar:

- **Hints:** Erste Hilfestellungen und NumPy-Konzepte
- **Skeleton:** Code-Gerüst mit strukturierten TODOs
- **Partial:** Teilweise implementierte Lösung mit strategischen Lücken
- **Complete:** Vollständige Musterlösung mit Performance-Optimierungen

## 🚀 Schnellstart

### 1. Assessment durchführen (EMPFOHLEN)

```bash
# Bestimmen Sie Ihren optimalen Lernpfad
uv run python src/03_numpy/assessments/learning_path_assessment.py
```

### 2. Umgebung einrichten

```bash
# Im Projektverzeichnis
uv sync
uv shell
```

### 3. Theory studieren (optional)

```bash
# Jupyter Notebook mit NumPy-Grundlagen
uv run jupyter notebook src/03_numpy/theory/03_numpy.ipynb
```

### 4. Examples erkunden

```bash
# Array-Grundlagen
uv run python src/03_numpy/examples/arrays_basic.py

# Mathematische Operationen
uv run python src/03_numpy/examples/mathematical_operations.py

# Array-Manipulation
uv run python src/03_numpy/examples/array_manipulation.py

# Lineare Algebra
uv run python src/03_numpy/examples/linear_algebra.py

# VBA-Vergleich
uv run python src/03_numpy/examples/vba_vs_numpy.py

# Performance-Demo
uv run python src/03_numpy/examples/performance_comparison.py
```

### 5. Adaptive Übungen (nach Assessment-Ergebnis)

#### 🟢 Beginner-Pfad

```bash
uv run python src/03_numpy/exercises/beginner/uebung_01_arrays_beginner.py
uv run python src/03_numpy/exercises/beginner/uebung_02_mathematik_beginner.py
uv run python src/03_numpy/exercises/beginner/uebung_03_manipulation_beginner.py
uv run python src/03_numpy/exercises/beginner/uebung_04_bystronic_daten_beginner.py
```

#### 🟡 Intermediate-Pfad

```bash
uv run python src/03_numpy/exercises/intermediate/uebung_01_arrays_intermediate.py
uv run python src/03_numpy/exercises/intermediate/uebung_02_statistik_intermediate.py
uv run python src/03_numpy/exercises/intermediate/uebung_03_linalg_intermediate.py
uv run python src/03_numpy/exercises/intermediate/uebung_04_produktionsanalyse_intermediate.py
```

#### 🔴 Advanced-Pfad

```bash
uv run python src/03_numpy/exercises/advanced/uebung_01_performance_advanced.py
uv run python src/03_numpy/exercises/advanced/uebung_02_algorithmen_advanced.py
uv run python src/03_numpy/exercises/advanced/uebung_03_optimierung_advanced.py
uv run python src/03_numpy/exercises/advanced/uebung_04_enterprise_analytics_advanced.py
```

## 📖 Adaptive Lernziele

### 🟢 Beginner-Lernziele

Nach dem Beginner-Pfad können Sie:

- ✅ **NumPy-Arrays** erstellen, verstehen und grundlegend verwenden
- ✅ **Vektorisierte Operationen** anstelle von Python-Schleifen einsetzen
- ✅ **Grundlegende Mathematik** mit NumPy durchführen (Summe, Mittelwert, etc.)
- ✅ **Array-Indexing** und einfaches Slicing verwenden
- ✅ **Performance-Vorteile** von NumPy gegenüber Pure Python verstehen
- ✅ **Produktionsdaten** mit NumPy verarbeiten und analysieren

### 🟡 Intermediate-Lernziele

Nach dem Intermediate-Pfad können Sie zusätzlich:

- ✅ **Broadcasting-Regeln** verstehen und komplexe Array-Operationen durchführen
- ✅ **Statistische Prozesskontrolle** (SPC) mit NumPy implementieren
- ✅ **Matrix-Operationen** und lineare Algebra anwenden
- ✅ **Mehrdimensionale Arrays** effizient manipulieren und transformieren
- ✅ **Qualitätskontroll-Algorithmen** für Bystronic-Prozesse entwickeln
- ✅ **Performance-bewusste** NumPy-Programmierung betreiben

### 🔴 Advanced-Lernziele

Nach dem Advanced-Pfad können Sie zusätzlich:

- ✅ **Memory-effiziente** NumPy-Algorithmen entwickeln und optimieren
- ✅ **Eigenwertalgorithmen** und numerische Verfahren implementieren
- ✅ **Custom NumPy-Funktionen** mit C-Performance schreiben
- ✅ **Big Data-Verarbeitung** mit NumPy und Integration in Enterprise-Systeme
- ✅ **Algorithmus-Design** für produktionsrelevante Optimierungsprobleme
- ✅ **Parallel Computing** und GPU-Acceleration mit NumPy verstehen

## 🔧 NumPy-Kernkonzepte

### ndarray vs Python-Listen

```python
import numpy as np

# Python-Liste (langsam)
python_liste = [1, 2, 3, 4, 5]
result = [x * 2 for x in python_liste]

# NumPy-Array (schnell)
numpy_array = np.array([1, 2, 3, 4, 5])
result = numpy_array * 2  # Vektorisierte Operation!
```

### Performance-Vorteil

```python
# Benchmark: 1 Million Elemente
import time

# NumPy (schnell)
start = time.time()
arr = np.random.random(1000000)
result_numpy = np.sqrt(arr**2 + 1)
numpy_time = time.time() - start

# Pure Python (langsam)
start = time.time()
python_list = list(arr)
result_python = [(x**2 + 1)**0.5 for x in python_list]
python_time = time.time() - start

print(f"NumPy: {numpy_time:.4f}s")
print(f"Python: {python_time:.4f}s")
print(f"Speedup: {python_time/numpy_time:.0f}x")
```

### Array-Erstellung

```python
# Verschiedene Methoden der Array-Erstellung
np.array([1, 2, 3, 4])           # Aus Liste
np.zeros((3, 4))                 # Nullen
np.ones((2, 3))                  # Einsen
np.arange(0, 10, 2)              # Sequenz: [0, 2, 4, 6, 8]
np.linspace(0, 1, 5)             # Linear verteilt: [0, 0.25, 0.5, 0.75, 1]
np.random.random((3, 3))         # Zufallszahlen
```

### Wichtige NumPy-Operationen

```python
# Mathematische Operationen
arr = np.array([1, 2, 3, 4, 5])
arr.sum()                        # Summe
arr.mean()                       # Durchschnitt
arr.std()                        # Standardabweichung
arr.max(), arr.min()             # Maximum, Minimum

# Array-Manipulation
arr.reshape((5, 1))              # Form ändern
arr[arr > 3]                     # Filtern
np.concatenate([arr1, arr2])     # Zusammenfügen

# Lineare Algebra
matrix = np.array([[1, 2], [3, 4]])
np.linalg.inv(matrix)            # Matrix-Inversion
np.dot(matrix1, matrix2)         # Matrix-Multiplikation
```

## 💡 Tipps für Excel/VBA-Entwickler

### Arrays vs Excel-Bereiche

```vba
' VBA: Arbeiten mit Ranges (langsam)
Dim rng As Range
Set rng = Range("A1:A1000")
Dim i As Integer
For i = 1 To rng.Rows.Count
    rng.Cells(i, 1).Value = rng.Cells(i, 1).Value * 2
Next i

' NumPy: Vektorisierte Operationen (schnell)
import numpy as np
data = np.random.random(1000)
result = data * 2  # Alle 1000 Werte in einem Schritt!
```

### Formeln vs NumPy-Funktionen

```vba
' VBA/Excel: Einzelne Formeln
=SUM(A1:A100)      ' Summe
=AVERAGE(A1:A100)  ' Durchschnitt
=STDEV(A1:A100)    ' Standardabweichung

' NumPy: Direkte Funktionen
data = np.array(range(1, 101))
data.sum()         # Summe
data.mean()        # Durchschnitt
data.std()         # Standardabweichung
```

### Matrix-Operationen

```vba
' VBA: Matrix-Multiplikation (umständlich)
Dim result() As Double
ReDim result(1 To 3, 1 To 3)
For i = 1 To 3
    For j = 1 To 3
        For k = 1 To 3
            result(i, j) = result(i, j) + matrix1(i, k) * matrix2(k, j)
        Next k
    Next j
Next i

' NumPy: Eine Zeile!
result = np.dot(matrix1, matrix2)
# oder noch einfacher:
result = matrix1 @ matrix2
```

## 📊 Praktische Anwendungen für Bystronic

### Produktionsdaten-Analyse

```python
# Maschinenlaufzeiten analysieren
import numpy as np

# Produktionszeiten verschiedener Maschinen (Stunden)
laser_zeiten = np.array([8.5, 7.2, 9.1, 8.8, 7.9, 8.3, 9.0])
presse_zeiten = np.array([6.8, 7.5, 6.2, 7.1, 6.9, 7.3, 6.5])

# Statistische Auswertung
print(f"Laser - Durchschnitt: {laser_zeiten.mean():.1f}h")
print(f"Laser - Standardabweichung: {laser_zeiten.std():.1f}h")
print(f"Presse - Durchschnitt: {presse_zeiten.mean():.1f}h")
print(f"Presse - Effizienz vs Laser: {(presse_zeiten.mean()/laser_zeiten.mean()*100):.1f}%")

# Trends und Korrelationen
gesamtzeit = laser_zeiten + presse_zeiten
korrelation = np.corrcoef(laser_zeiten, presse_zeiten)[0, 1]
```

### Qualitätskontrolle mit Statistik

```python
# Messwerte analysieren
messwerte = np.array([2.05, 1.98, 2.02, 2.07, 1.95, 2.01, 2.04, 1.99])
sollwert = 2.0
toleranz = 0.1

# Statistische Prozesskontrolle
mittelwert = messwerte.mean()
std_abweichung = messwerte.std()
cp_wert = toleranz / (3 * std_abweichung)  # Prozessfähigkeit

# Ausreisser identifizieren (3-Sigma-Regel)
grenzen = (mittelwert - 3*std_abweichung, mittelwert + 3*std_abweichung)
ausreisser = messwerte[(messwerte < grenzen[0]) | (messwerte > grenzen[1])]

print(f"Cp-Wert: {cp_wert:.2f}")
print(f"Ausreisser: {len(ausreisser)} von {len(messwerte)}")
```

## 🎓 Überprüfen Sie Ihr Verständnis

Bevor Sie zum nächsten Kapitel wechseln:

- [ ] Können Sie NumPy-Arrays erstellen und grundlegende Operationen
  durchführen?
- [ ] Verstehen Sie den Unterschied zwischen NumPy-Arrays und Python-Listen?
- [ ] Können Sie vektorisierte Operationen anwenden?
- [ ] Beherrschen Sie Array-Indexing und Slicing?
- [ ] Können Sie statistische Berechnungen durchführen?
- [ ] Verstehen Sie Broadcasting-Regeln?
- [ ] Können Sie Matrix-Operationen anwenden?
- [ ] Haben Sie alle Übungen Ihres Levels erfolgreich gelöst?

## 📝 Zusätzliche Ressourcen

- **NumPy Documentation**: <https://numpy.org/doc/stable/>
- **NumPy Quickstart**: <https://numpy.org/doc/stable/user/quickstart.html>
- **From Python to NumPy**:
  <https://www.labri.fr/perso/nrougier/from-python-to-numpy/>

## 🎯 Assessment-System

### 📊 Learning Path Assessment

- **Dauer:** 7-10 Minuten
- **Kategorien:** Array-Grundlagen, Mathematik, Programmierpraxis,
  Anwendungskontext, Performance-Bewusstsein
- **Ergebnis:** Personalisierte Lernpfad-Empfehlung mit NumPy-Fokus
- **Speicherung:** Automatische Ergebnis-Dokumentation

### 🔄 Micro-Assessments (in Entwicklung)

- **Quiz:** Interaktive NumPy-Wissensprüfung
- **Challenges:** Praktische Programmieraufgaben
- **Reflection:** Selbsteinschätzung der NumPy-Kompetenzen
- **Dashboard:** Übersicht über alle Assessment-Ergebnisse

## 🎓 Lernfortschritt überprüfen

### 🟢 Beginner-Checkliste

- [ ] Können Sie NumPy-Arrays erstellen und verstehen?
- [ ] Verstehen Sie vektorisierte vs. skalare Operationen?
- [ ] Können Sie grundlegende Array-Manipulation durchführen?
- [ ] Beherrschen Sie einfache mathematische NumPy-Funktionen?
- [ ] Haben Sie alle Beginner-Übungen erfolgreich gelöst?

### 🟡 Intermediate-Checkliste

- [ ] Können Sie Broadcasting-Regeln anwenden?
- [ ] Beherrschen Sie statistische Analysen mit NumPy?
- [ ] Verstehen Sie Matrix-Operationen und lineare Algebra?
- [ ] Können Sie mehrdimensionale Arrays effizient manipulieren?
- [ ] Haben Sie alle Intermediate-Übungen erfolgreich gelöst?

### 🔴 Advanced-Checkliste

- [ ] Können Sie memory-effiziente NumPy-Algorithmen entwickeln?
- [ ] Beherrschen Sie Eigenwertalgorithmen und numerische Verfahren?
- [ ] Verstehen Sie NumPy-Performance-Optimierung?
- [ ] Können Sie NumPy für Enterprise-Analytics einsetzen?
- [ ] Haben Sie alle Advanced-Übungen erfolgreich gelöst?

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels: **→
[Kapitel 4: Pandas für Datenanalyse](../04_pandas/README.md)**

______________________________________________________________________

## 📊 Dieses Kapitel ist Teil des adaptiven Python Grundkurses für Bystronic-Entwickler
