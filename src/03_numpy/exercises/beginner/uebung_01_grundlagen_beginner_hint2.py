#!/usr/bin/env python3
"""
Hilfe Stufe 2: Konkrete Hinweise für NumPy Grundlagen
====================================================

💡 HINT 2 - Konkrete Ansätze

🔹 Aufgabe 1 - Array-Erstellung:
   ```python
   # Listen zu Arrays konvertieren
   zahlen = [1, 2, 3, 4, 5]
   arr = np.array(zahlen)

   # Spezielle Arrays erstellen
   nullen = np.zeros(10)        # 10 Nullen
   einsen = np.ones((3, 4))     # 3x4 Matrix mit Einsen
   sequenz = np.arange(0, 20, 2) # 0, 2, 4, ... 18
   ```

🔹 Aufgabe 2 - Array-Eigenschaften:
   ```python
   # Shape, dtype, size abfragen
   print(f"Shape: {arr.shape}")
   print(f"Datentyp: {arr.dtype}")
   print(f"Anzahl Elemente: {arr.size}")
   ```

🔹 Aufgabe 3 - Grundrechenarten:
   ```python
   # Elementweise Operationen
   a = np.array([1, 2, 3])
   b = np.array([4, 5, 6])
   summe = a + b
   produkt = a * b
   ```

🔹 Aufgabe 4 - Aggregationsfunktionen:
   ```python
   # Statistische Funktionen
   mittelwert = np.mean(arr)
   summe = np.sum(arr)
   maximum = np.max(arr)
   ```

🎯 Tipp: Probiere jede Operation einzeln aus und schaue dir das Ergebnis an!
"""
