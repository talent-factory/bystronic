#!/usr/bin/env python3
"""
Hilfe Stufe 2: Konkrete Hinweise für NumPy Indexing & Slicing
============================================================

💡 HINT 2 - Konkrete Ansätze

🔹 Aufgabe 1 - Einfaches Indexing:
   ```python
   arr = np.array([10, 20, 30, 40, 50])

   # Einzelne Elemente
   erstes = arr[0]        # 10
   letztes = arr[-1]      # 50
   drittes = arr[2]       # 30
   ```

🔹 Aufgabe 2 - Array Slicing:
   ```python
   # Bereiche extrahieren
   erste_drei = arr[:3]    # [10, 20, 30]
   letzte_zwei = arr[-2:]  # [40, 50]
   jedes_zweite = arr[::2] # [10, 30, 50]
   rueckwaerts = arr[::-1] # [50, 40, 30, 20, 10]
   ```

🔹 Aufgabe 3 - 2D Array Indexing:
   ```python
   matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

   # Element in Zeile 1, Spalte 2
   element = matrix[1, 2]  # 6

   # Ganze Zeile oder Spalte
   erste_zeile = matrix[0, :]   # [1, 2, 3]
   zweite_spalte = matrix[:, 1] # [2, 5, 8]
   ```

🔹 Aufgabe 4 - Boolean Indexing:
   ```python
   # Elemente nach Bedingung filtern
   grosse_werte = arr[arr > 25]  # [30, 40, 50]

   # Komplexere Bedingungen
   mittlere_werte = arr[(arr > 15) & (arr < 45)]
   ```

🔹 Aufgabe 5 - Fancy Indexing:
   ```python
   # Spezifische Indizes auswählen
   indizes = [0, 2, 4]
   ausgewaehlte = arr[indizes]  # [10, 30, 50]
   ```

🎯 Tipp: Experimentiere mit verschiedenen Kombinationen von Start:Stop:Step!
"""
