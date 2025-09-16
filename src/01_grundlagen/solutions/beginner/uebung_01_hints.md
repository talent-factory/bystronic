# 💡 Tipps für Übung 1: Persönliche Informationen (Beginner)

## 🎯 Lernziele verstehen

- **input()** für Benutzereingaben verwenden
- **Variablen** zum Speichern von Daten nutzen
- **f-strings** für formatierte Ausgaben
- **print()** für die Ausgabe verwenden

## 🔍 Schritt-für-Schritt Denkansatz

### 1. Eingaben sammeln

```
Welche Informationen brauche ich?
→ Name, Alter, Wohnort, Beruf
→ Wie frage ich nach diesen Daten?
```

### 2. Daten verarbeiten

```
Wie speichere ich die Eingaben?
→ Jede Eingabe in einer eigenen Variable
→ Welche Variablennamen sind sinnvoll?
```

### 3. Ausgabe formatieren

```
Wie gebe ich die Daten schön aus?
→ f-strings verwenden: f"Hallo {name}!"
→ Mehrere Zeilen für bessere Lesbarkeit
```

## 💭 Konzeptuelle Tipps

### input() verwenden

```python
# So funktioniert input():
name = input("Wie heisst du? ")
# Der Text in den Klammern wird als Frage angezeigt
# Die Antwort wird in der Variable gespeichert
```

### Variablen benennen

```python
# Gute Variablennamen:
vorname = "Max"
alter = 25
wohnort = "Zürich"

# Schlechte Variablennamen:
x = "Max"
a = 25
data = "Zürich"
```

### f-strings für Ausgaben

```python
# Moderne Art der Formatierung:
name = "Anna"
print(f"Hallo {name}!")

# Statt der alten Art:
print("Hallo " + name + "!")
```

## 🚀 Erste Schritte

1. **Beginnen Sie einfach:**

   - Fragen Sie nur nach dem Namen
   - Geben Sie eine Begrüssung aus
   - Erweitern Sie dann schrittweise

1. **Testen Sie häufig:**

   - Nach jeder neuen Zeile das Programm ausführen
   - Schauen Sie, ob alles funktioniert
   - Dann den nächsten Schritt machen

1. **Experimentieren Sie:**

   - Probieren Sie verschiedene Fragen aus
   - Ändern Sie die Ausgabeformate
   - Fügen Sie eigene Ideen hinzu

## ❓ Häufige Fragen

**Q: Wie kann ich Zahlen eingeben?** A: input() gibt immer Text zurück. Für
Zahlen verwenden Sie int() oder float():

```python
alter = int(input("Wie alt sind Sie? "))
```

**Q: Wie mache ich mehrzeilige Ausgaben?** A: Verwenden Sie mehrere
print()-Aufrufe oder \\n:

```python
print("Zeile 1")
print("Zeile 2")
# oder:
print("Zeile 1\nZeile 2")
```

**Q: Was sind f-strings genau?** A: Eine moderne Art, Variablen in Strings
einzufügen:

```python
name = "Max"
alter = 30
print(f"Ich bin {name} und {alter} Jahre alt.")
```

## 🎯 Erfolgskriterien

✅ **Ihr Programm sollte:**

- Nach mindestens 3 Informationen fragen
- Die Eingaben in Variablen speichern
- Eine formatierte Ausgabe erstellen
- Ohne Fehler laufen

✅ **Bonus-Punkte für:**

- Freundliche Begrüssung und Verabschiedung
- Schöne Formatierung der Ausgabe
- Zusätzliche interessante Fragen

## 🔧 Debugging-Tipps

**Problem: "NameError: name 'xyz' is not defined"** → Variable wurde nicht
definiert oder falsch geschrieben

**Problem: Programm macht nichts** → Vergessen Sie nicht print() für die Ausgabe

**Problem: Seltsame Ausgabe** → Prüfen Sie die f-string Syntax: f"Text
{variable}"

## 📚 Weiterführende Konzepte

Nach dieser Übung können Sie lernen:

- **Listen** für mehrere Werte
- **Schleifen** für wiederholte Aktionen
- **Funktionen** für wiederverwendbaren Code
- **Bedingungen** für verschiedene Fälle

______________________________________________________________________

💪 **Sie schaffen das!** Beginnen Sie mit dem Einfachsten und bauen Sie Schritt
für Schritt auf.
