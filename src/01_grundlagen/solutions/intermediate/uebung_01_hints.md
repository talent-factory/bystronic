# 💡 Tipps für Übung 1: Mitarbeiterprofil-System (Intermediate)

## 🎯 Lernziele verstehen

- **Funktionen** definieren und verwenden
- **Dictionaries** für strukturierte Daten
- **try/except** für robuste Fehlerbehandlung
- **Eingabevalidierung** implementieren
- **Modulare Programmierung** anwenden

## 🔍 Schritt-für-Schritt Denkansatz

### 1. Funktionale Struktur planen

```
Welche Funktionen brauche ich?
→ sammle_mitarbeiterdaten() - Eingaben sammeln
→ validiere_eingabe() - Daten prüfen
→ zeige_profil() - Ausgabe formatieren
→ main() - Hauptprogramm koordinieren
```

### 2. Datenstruktur entwerfen

```
Wie organisiere ich die Daten?
→ Dictionary für Mitarbeiterdaten
→ Schlüssel: "name", "alter", "abteilung", etc.
→ Werte: Benutzereingaben
```

### 3. Fehlerbehandlung einbauen

```
Was kann schiefgehen?
→ Ungültige Zahlen-Eingaben
→ Leere Eingaben
→ Unerwartete Werte
→ try/except für jeden kritischen Bereich
```

## 💭 Konzeptuelle Tipps

### Funktionen definieren und verwenden

```python
def sammle_daten():
    """Sammelt Benutzerdaten und gibt Dictionary zurück."""
    daten = {}
    daten["name"] = input("Name: ")
    daten["alter"] = int(input("Alter: "))
    return daten

# Funktion aufrufen:
mitarbeiter = sammle_daten()
```

### Dictionaries für strukturierte Daten

```python
# Dictionary erstellen:
person = {
    "name": "Max Mustermann",
    "alter": 30,
    "abteilung": "IT",
    "gehalt": 75000
}

# Zugriff auf Werte:
print(person["name"])
person["alter"] = 31  # Wert ändern
person["email"] = "max@firma.com"  # Neuen Schlüssel hinzufügen
```

### try/except für Fehlerbehandlung

```python
def sichere_zahl_eingabe(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein!")

# Verwendung:
alter = sichere_zahl_eingabe("Alter: ")
```

### Eingabevalidierung

```python
def validiere_name(name):
    if not name.strip():
        return False, "Name darf nicht leer sein!"
    if len(name) < 2:
        return False, "Name muss mindestens 2 Zeichen haben!"
    return True, "OK"

# Verwendung:
gueltig, nachricht = validiere_name(eingabe)
if not gueltig:
    print(f"Fehler: {nachricht}")
```

## 🚀 Erste Schritte

1. **Beginnen Sie mit einer einfachen Funktion:**

   - Nur Name eingeben und ausgeben
   - Dann schrittweise erweitern

1. **Bauen Sie das Dictionary auf:**

   - Erst ein Feld, dann mehr hinzufügen
   - Testen Sie nach jedem neuen Feld

1. **Fügen Sie Validierung hinzu:**

   - Erst einfache Prüfungen
   - Dann robuste try/except Blöcke

## ❓ Häufige Fragen

**Q: Wann sollte ich Funktionen verwenden?** A: Immer wenn Sie Code
wiederverwenden oder strukturieren möchten:

```python
# Statt Wiederholung:
name1 = input("Name 1: ").strip().title()
name2 = input("Name 2: ").strip().title()

# Besser mit Funktion:
def hole_name(prompt):
    return input(prompt).strip().title()

name1 = hole_name("Name 1: ")
name2 = hole_name("Name 2: ")
```

**Q: Wie gebe ich mehrere Werte aus einer Funktion zurück?** A: Mit Tupeln oder
Dictionaries:

```python
def validiere_daten(name, alter):
    fehler = []
    if not name:
        fehler.append("Name fehlt")
    if alter < 0:
        fehler.append("Alter ungültig")
    return len(fehler) == 0, fehler

# Verwendung:
gueltig, fehler_liste = validiere_daten("Max", 25)
```

**Q: Wie funktioniert try/except genau?** A: try/except fängt Fehler ab und
behandelt sie:

```python
try:
    # Code der Fehler verursachen könnte
    zahl = int(input("Zahl: "))
    ergebnis = 10 / zahl
except ValueError:
    print("Keine gültige Zahl!")
except ZeroDivisionError:
    print("Division durch Null!")
except Exception as e:
    print(f"Unerwarteter Fehler: {e}")
```

## 🎯 Erfolgskriterien

✅ **Ihr System sollte:**

- Mitarbeiterdaten in Funktionen sammeln
- Dictionary für Datenorganisation verwenden
- Eingaben validieren und Fehler abfangen
- Professionelle Ausgabe formatieren
- Modularen, wiederverwendbaren Code haben

✅ **Bonus-Punkte für:**

- Umfassende Eingabevalidierung
- Benutzerfreundliche Fehlermeldungen
- Zusätzliche Mitarbeiter-Features
- Saubere Code-Organisation

## 🔧 Debugging-Tipps

**Problem: "NameError: name 'variable' is not defined"** → Variable wurde in
Funktion definiert, aber ausserhalb verwendet

**Problem: "KeyError: 'schluessel'"** → Dictionary-Schlüssel existiert nicht,
prüfen Sie die Schreibweise

**Problem: Funktion gibt None zurück** → Vergessen Sie nicht das 'return'
Statement

**Problem: Endlosschleife bei Eingabevalidierung** → Stellen Sie sicher, dass
die Schleife eine Ausstiegsbedingung hat

## 📚 Dictionary-Operationen

```python
# Dictionary erstellen:
person = {}
person = dict()
person = {"name": "Max", "alter": 30}

# Werte hinzufügen/ändern:
person["email"] = "max@firma.com"
person.update({"telefon": "123456", "stadt": "Zürich"})

# Werte abrufen:
name = person["name"]                    # Fehler wenn Schlüssel fehlt
name = person.get("name", "Unbekannt")   # Standardwert wenn Schlüssel fehlt

# Prüfen ob Schlüssel existiert:
if "email" in person:
    print(person["email"])

# Alle Schlüssel/Werte:
for schluessel in person.keys():
    print(schluessel)
for wert in person.values():
    print(wert)
for schluessel, wert in person.items():
    print(f"{schluessel}: {wert}")
```

## 🔄 Programm-Fluss

```
1. Hauptfunktion main() starten
2. Begrüssung anzeigen
3. sammle_mitarbeiterdaten() aufrufen
   a. Jede Eingabe validieren
   b. Bei Fehlern erneut fragen
   c. Dictionary mit Daten füllen
4. zeige_profil() aufrufen
   a. Dictionary formatiert ausgeben
   b. Zusätzliche Berechnungen
5. Verabschiedung anzeigen
```

## 🌟 Erweiterte Konzepte

Nach der Grundübung können Sie probieren:

- **Mehrere Mitarbeiter** in einer Liste verwalten
- **Daten speichern** in JSON-Datei
- **Suchfunktionen** implementieren
- **Datenvalidierung** mit regulären Ausdrücken

______________________________________________________________________

💪 **Tipp:** Funktionen machen Ihren Code sauberer und wiederverwendbarer!
