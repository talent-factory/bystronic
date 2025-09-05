# 💡 Tipps für Übung 2: Taschenrechner (Beginner)

## 🎯 Lernziele verstehen

- **if/elif/else** für verschiedene Fälle verwenden
- **int()** und **float()** für Zahlenkonvertierung
- **Mathematische Operatoren** (+, -, \*, /) anwenden
- **Fehlerbehandlung** für Division durch Null

## 🔍 Schritt-für-Schritt Denkansatz

### 1. Programm-Struktur planen

```
Was soll mein Taschenrechner können?
→ Zwei Zahlen eingeben
→ Operation wählen (+, -, *, /)
→ Ergebnis berechnen und anzeigen
→ Fehler abfangen (Division durch 0)
```

### 2. Eingaben sammeln

```
Welche Eingaben brauche ich?
→ Erste Zahl (als float)
→ Zweite Zahl (als float)
→ Operation (als String)
```

### 3. Entscheidungslogik

```
Wie entscheide ich, welche Berechnung?
→ if operation == "+"
→ elif operation == "-"
→ elif operation == "*"
→ elif operation == "/"
→ else: Ungültige Operation
```

## 💭 Konzeptuelle Tipps

### Zahlen-Eingabe mit Konvertierung

```python
# input() gibt immer String zurück
zahl_text = input("Zahl: ")
zahl = float(zahl_text)

# Oder direkt:
zahl = float(input("Zahl: "))

# Für ganze Zahlen:
zahl = int(input("Zahl: "))
```

### if/elif/else Struktur

```python
operation = input("Operation (+, -, *, /): ")

if operation == "+":
    ergebnis = zahl1 + zahl2
elif operation == "-":
    ergebnis = zahl1 - zahl2
elif operation == "*":
    ergebnis = zahl1 * zahl2
elif operation == "/":
    # Hier Division durch Null prüfen!
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
    else:
        print("Fehler: Division durch Null!")
else:
    print("Ungültige Operation!")
```

### Division durch Null vermeiden

```python
# Immer prüfen vor Division:
if zahl2 == 0:
    print("Fehler: Division durch Null ist nicht möglich!")
else:
    ergebnis = zahl1 / zahl2
    print(f"Ergebnis: {ergebnis}")
```

## 🚀 Erste Schritte

1. **Beginnen Sie mit Addition:**

   - Zwei Zahlen eingeben
   - Addieren und ausgeben
   - Dann andere Operationen hinzufügen

1. **Testen Sie jede Operation:**

   - Addition: 5 + 3 = 8
   - Subtraktion: 5 - 3 = 2
   - Multiplikation: 5 * 3 = 15
   - Division: 6 / 3 = 2.0

1. **Testen Sie Fehlerfälle:**

   - Division durch 0: 5 / 0 → Fehlermeldung
   - Ungültige Operation: 5 % 3 → Fehlermeldung

## ❓ Häufige Fragen

**Q: Warum float() statt int()?** A: float() kann auch Kommazahlen verarbeiten:

```python
# float() ist flexibler:
float("5")    → 5.0
float("5.5")  → 5.5

# int() nur für ganze Zahlen:
int("5")      → 5
int("5.5")    → Fehler!
```

**Q: Wie erkenne ich ungültige Eingaben?** A: Mit try/except (fortgeschritten)
oder einfacher Prüfung:

```python
# Einfache Prüfung:
if operation in ["+", "-", "*", "/"]:
    # Gültige Operation
else:
    print("Ungültige Operation!")
```

**Q: Wie formatiere ich das Ergebnis schön?** A: Mit f-strings und Rundung:

```python
ergebnis = 10 / 3  # 3.3333333...
print(f"Ergebnis: {ergebnis:.2f}")  # 3.33
```

## 🎯 Erfolgskriterien

✅ **Ihr Taschenrechner sollte:**

- Zwei Zahlen eingeben können
- Alle vier Grundrechenarten beherrschen
- Division durch Null abfangen
- Ungültige Operationen erkennen
- Ergebnisse schön formatiert ausgeben

✅ **Bonus-Punkte für:**

- Benutzerfreundliche Menüführung
- Mehrere Berechnungen hintereinander
- Zusätzliche Operationen (Potenz, Wurzel)

## 🔧 Debugging-Tipps

**Problem: "ValueError: could not convert string to float"** → Benutzer hat Text
statt Zahl eingegeben

**Problem: "ZeroDivisionError: float division by zero"** → Division durch Null
nicht abgefangen

**Problem: Falsche Ergebnisse** → Prüfen Sie die Operator-Reihenfolge und
Klammern

**Problem: Programm macht nichts bei ungültiger Operation** → Vergessen Sie
nicht den else-Zweig

## 📚 Mathematische Operatoren in Python

```python
# Grundrechenarten:
+   # Addition
-   # Subtraktion
*   # Multiplikation
/   # Division (Ergebnis immer float)
//  # Ganzzahl-Division
%   # Modulo (Rest)
**  # Potenz

# Beispiele:
10 / 3   → 3.3333333333333335
10 // 3  → 3
10 % 3   → 1
2 ** 3   → 8
```

## 🔄 Programm-Fluss

```
1. Begrüssung anzeigen
2. Erste Zahl eingeben
3. Zweite Zahl eingeben
4. Operation wählen
5. Gültigkeit prüfen
6. Berechnung durchführen
7. Ergebnis anzeigen
8. Verabschiedung
```

______________________________________________________________________

💪 **Tipp:** Beginnen Sie mit einer einfachen Addition und erweitern Sie dann
schrittweise!
