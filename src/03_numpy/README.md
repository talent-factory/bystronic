# Kapitel 3: NumPy für numerische Berechnungen

Willkommen zum dritten Kapitel des Python Grundkurses für Bystronic-Entwickler! 🔢📐

## 📚 Inhalte dieses Kapitels

### Hauptdokumentation
- **[03_numpy.ipynb](03_numpy.ipynb)** - Interaktives Jupyter Notebook mit NumPy-Grundlagen

### 💡 Beispiele
- **[arrays_demo.py](beispiele/arrays_demo.py)** - Array-Erstellung und grundlegende Operationen
- **[mathematical_operations.py](beispiele/mathematical_operations.py)** - Mathematische Funktionen und Berechnungen
- **[array_manipulation.py](beispiele/array_manipulation.py)** - Reshaping, Slicing und Indexing
- **[linear_algebra.py](beispiele/linear_algebra.py)** - Lineare Algebra Operationen
- **[vba_vs_numpy.py](beispiele/vba_vs_numpy.py)** - Vergleich Excel/VBA zu NumPy

### 🎯 Übungen
- **[Übung 1: Array-Grundlagen](uebungen/uebung_01_arrays.py)** - Erstellen und Manipulieren von Arrays
- **[Übung 2: Mathematische Operationen](uebungen/uebung_02_math.py)** - Berechnungen mit NumPy
- **[Übung 3: Datenanalyse](uebungen/uebung_03_analysis.py)** - Statistische Auswertungen
- **[Übung 4: Lineare Algebra](uebungen/uebung_04_linalg.py)** - Matrix-Operationen und Geometrie

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
uv run jupyter notebook src/03_numpy/03_numpy.ipynb
```

### 3. Beispiele ausführen
```bash
# Array-Grundlagen
uv run python src/03_numpy/beispiele/arrays_demo.py

# Mathematische Operationen
uv run python src/03_numpy/beispiele/mathematical_operations.py

# Array-Manipulation
uv run python src/03_numpy/beispiele/array_manipulation.py

# Lineare Algebra
uv run python src/03_numpy/beispiele/linear_algebra.py

# VBA-Vergleich
uv run python src/03_numpy/beispiele/vba_vs_numpy.py
```

### 4. Übungen bearbeiten
```bash
# Übung 1 - Array-Grundlagen
uv run python src/03_numpy/uebungen/uebung_01_arrays.py

# Übung 2 - Mathematische Operationen
uv run python src/03_numpy/uebungen/uebung_02_math.py

# Übung 3 - Datenanalyse
uv run python src/03_numpy/uebungen/uebung_03_analysis.py

# Übung 4 - Lineare Algebra
uv run python src/03_numpy/uebungen/uebung_04_linalg.py
```

## 📖 Lernziele

Nach diesem Kapitel können Sie:

✅ **Arrays**: NumPy-Arrays erstellen, manipulieren und verwenden
✅ **Datentypen**: Numerische Datentypen verstehen und optimal nutzen
✅ **Operationen**: Vektorisierte mathematische Operationen durchführen
✅ **Broadcasting**: Array-Operationen mit verschiedenen Shapes
✅ **Indexing**: Erweiterte Indexierung und Slicing-Techniken
✅ **Lineare Algebra**: Matrix-Operationen und geometrische Berechnungen
✅ **Performance**: Effiziente numerische Berechnungen implementieren
✅ **Integration**: NumPy mit anderen Libraries (pandas, matplotlib) nutzen

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

- [ ] Können Sie NumPy-Arrays erstellen und grundlegende Operationen durchführen?
- [ ] Verstehen Sie den Unterschied zwischen NumPy-Arrays und Python-Listen?
- [ ] Können Sie vektorisierte Operationen anwenden?
- [ ] Beherrschen Sie Array-Indexing und Slicing?
- [ ] Können Sie statistische Berechnungen durchführen?
- [ ] Verstehen Sie Broadcasting-Regeln?
- [ ] Können Sie Matrix-Operationen anwenden?
- [ ] Haben Sie alle vier Übungen erfolgreich gelöst?

## 📝 Zusätzliche Ressourcen

- **NumPy Documentation**: https://numpy.org/doc/stable/
- **NumPy Quickstart**: https://numpy.org/doc/stable/user/quickstart.html
- **From Python to NumPy**: https://www.labri.fr/perso/nrougier/from-python-to-numpy/

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels:
**→ [Kapitel 4: Pandas für Datenanalyse](../04_pandas/README.md)**

---
*Dieses Kapitel ist Teil des Python Grundkurses für Bystronic-Entwickler*
