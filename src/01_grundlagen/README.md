# Kapitel 1: Python Grundlagen

Willkommen zum ersten Kapitel des Python Grundkurses für Bystronic-Entwickler! 🐍

## 📚 Inhalte dieses Kapitels

### Hauptdokumentation

- **[01_python_grundlagen.adoc](01_python_grundlagen.adoc)** - Umfassendes
  Tutorial mit Installation, Grundlagen und Übungen

### 💡 Beispiele

- **[hello_world.py](beispiele/hello_world.py)** - Ihr erstes Python-Programm
- **[vba_vs_python.py](beispiele/vba_vs_python.py)** - Praktischer Vergleich
  zwischen VBA und Python

### 🎯 Übungen

- **[Übung 1: Persönliche Informationen](uebungen/uebung_01_personal_info.py)**
  \- Eingabe, Verarbeitung, Ausgabe
- **[Übung 2: Taschenrechner](uebungen/uebung_02_taschenrechner.py)** -
  Funktionen und Fehlerbehandlung
- **[Übung 3: Programmiersprachen](uebungen/uebung_03_programmiersprachen.py)**
  \- Listen und Datenstrukturen

## 🚀 Schnellstart

### 1. Umgebung einrichten

```bash
# Im Projektverzeichnis
uv sync
uv shell
```

### 2. Erstes Programm ausführen

```bash
# Hello World Beispiel
uv run python src/01_grundlagen/beispiele/hello_world.py

# VBA vs Python Vergleich
uv run python src/01_grundlagen/beispiele/vba_vs_python.py
```

### 3. Übungen bearbeiten

```bash
# Übung 1 - Persönliche Informationen
uv run python src/01_grundlagen/uebungen/uebung_01_personal_info.py

# Übung 2 - Taschenrechner
uv run python src/01_grundlagen/uebungen/uebung_02_taschenrechner.py

# Übung 3 - Programmiersprachen
uv run python src/01_grundlagen/uebungen/uebung_03_programmiersprachen.py
```

## 📖 Lernziele

Nach diesem Kapitel können Sie:

✅ **Installation**: Python, Git, uv und VS Code einrichten ✅ **Grundlagen**:
Python-Syntax, Variablen, Operatoren verstehen ✅ **Kontrollstrukturen**:
if-statements und Schleifen verwenden ✅ **Funktionen**: Eigene Funktionen
definieren und aufrufen ✅ **Datenstrukturen**: Listen und Dictionaries
grundlegend nutzen ✅ **VBA-Vergleich**: Unterschiede und Vorteile von Python
erkennen

## 🔧 Benötigte Tools

- **Python 3.13+** - Programmiersprache
- **Git** - Versionskontrolle
- **uv** - Package Manager
- **Visual Studio Code** - IDE mit Python-Extensions

## 💡 Tipps für VBA-Entwickler

### Syntax-Unterschiede

```python
# VBA: If...Then...End If
If alter > 18 Then
    MsgBox "Volljährig"
End If

# Python: if...else (Einrückung statt End If!)
if alter > 18:
    print("Volljährig")
```

### Arrays vs Listen

```vba
' VBA: Arrays sind statisch
Dim zahlen(1 to 5) As Integer

' Python: Listen sind dynamisch
zahlen = [1, 2, 3, 4, 5]
zahlen.append(6)  # Einfach erweitern!
```

### Collections vs Dictionaries

```vba
' VBA: Collections
Dim mitarbeiter As Collection
mitarbeiter.Add "Max", "ID001"

' Python: Dictionaries (viel mächtiger!)
mitarbeiter = {
    "ID001": {"name": "Max", "abteilung": "IT"}
}
```

## 🎓 Überprüfen Sie Ihr Verständnis

Bevor Sie zum nächsten Kapitel wechseln:

- [ ] Haben Sie alle drei Übungen erfolgreich gelöst?
- [ ] Verstehen Sie den Unterschied zwischen VBA und Python?
- [ ] Können Sie einfache Python-Programme schreiben?
- [ ] Ist Ihre Entwicklungsumgebung korrekt eingerichtet?

## 📝 Zusätzliche Ressourcen

- **Python.org Tutorial**: <https://docs.python.org/3/tutorial/>
- **Automate the Boring Stuff**: <https://automatetheboringstuff.com/>
- **Real Python**: <https://realpython.com/>

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels: **→
[Kapitel 2: Datentypen im Detail](../02_datentypen/README.md)**

______________________________________________________________________

*Dieses Kapitel ist Teil des Python Grundkurses für Bystronic-Entwickler*
