# 🎯 Exercises - Adaptive Übungen

Dieses Verzeichnis enthält **adaptive Übungen** in drei Schwierigkeitsstufen,
die sich an Ihr Vorwissen anpassen.

## 🔍 Lernpfad bestimmen

**WICHTIG:** Führen Sie zuerst das Assessment durch, um Ihren optimalen Lernpfad
zu bestimmen:

```bash
uv run python src/02_datentypen/assessments/learning_path_assessment.py
```

## 📚 Adaptive Lernpfade

### 🟢 Beginner-Pfad (0-40 Punkte)

**Zielgruppe:** Programmier-Einsteiger, erste Schritte mit Datentypen  
**Dauer:** 15-25 Minuten pro Übung  
**Fokus:** Grundlagen verstehen, praktische Anwendung

#### Übungen:

- **[uebung_01_zahlen_beginner.py](beginner/uebung_01_zahlen_beginner.py)** - Grundlagen der Zahlentypen
- **[uebung_02_strings_beginner.py](beginner/uebung_02_strings_beginner.py)** - Einfache String-Operationen
- **[uebung_03_collections_beginner.py](beginner/uebung_03_collections_beginner.py)** - Listen und Dictionaries

### 🟡 Intermediate-Pfad (41-70 Punkte)

**Zielgruppe:** Programmiererfahrung vorhanden, erweiterte Datenverarbeitung  
**Dauer:** 25-40 Minuten pro Übung  
**Fokus:** Funktionale Programmierung, Statistik, Fehlerbehandlung

#### Übungen:

- **[uebung_01_zahlen_intermediate.py](intermediate/uebung_01_zahlen_intermediate.py)** - Erweiterte Zahlenoperationen
- **[uebung_02_strings_intermediate.py](intermediate/uebung_02_strings_intermediate.py)** - String-Verarbeitung und Regex
- **[uebung_03_collections_intermediate.py](intermediate/uebung_03_collections_intermediate.py)** - Komplexe Datenstrukturen

### 🔴 Advanced-Pfad (71-100 Punkte)

**Zielgruppe:** Erfahrene Entwickler, professionelle Systeme  
**Dauer:** 45-60 Minuten pro Übung  
**Fokus:** OOP, Design Patterns, Enterprise-Standards

#### Übungen:

- **[uebung_01_zahlen_advanced.py](advanced/uebung_01_zahlen_advanced.py)** - OOP-Zahlenverarbeitung
- **[uebung_02_strings_advanced.py](advanced/uebung_02_strings_advanced.py)** - Enterprise String-Processing
- **[uebung_03_collections_advanced.py](advanced/uebung_03_collections_advanced.py)** - Design Patterns für Collections

## 🆘 4-Stufen-Hilfesystem

Für jede Übung stehen vier Hilfeebenen zur Verfügung:

1. **Hints** - Erste Hilfestellungen und Tipps
2. **Skeleton** - Code-Gerüst mit Kommentaren
3. **Partial** - Teilweise implementierte Lösung
4. **Complete** - Vollständige Musterlösung mit Erklärungen

Verfügbar unter: **[Solutions](../solutions/)**

## 🚀 Ausführung

### Beginner-Übungen

```bash
uv run python src/02_datentypen/exercises/beginner/uebung_01_zahlen_beginner.py
uv run python src/02_datentypen/exercises/beginner/uebung_02_strings_beginner.py
uv run python src/02_datentypen/exercises/beginner/uebung_03_collections_beginner.py
```

### Intermediate-Übungen

```bash
uv run python src/02_datentypen/exercises/intermediate/uebung_01_zahlen_intermediate.py
uv run python src/02_datentypen/exercises/intermediate/uebung_02_strings_intermediate.py
uv run python src/02_datentypen/exercises/intermediate/uebung_03_collections_intermediate.py
```

### Advanced-Übungen

```bash
uv run python src/02_datentypen/exercises/advanced/uebung_01_zahlen_advanced.py
uv run python src/02_datentypen/exercises/advanced/uebung_02_strings_advanced.py
uv run python src/02_datentypen/exercises/advanced/uebung_03_collections_advanced.py
```

## 📖 Lernziele nach Level

### 🟢 Beginner-Ziele

- ✅ Grundlegende Zahlentypen (int, float, bool) verstehen
- ✅ Einfache String-Operationen durchführen
- ✅ Listen und Dictionaries erstellen und verwenden
- ✅ Praktische Berechnungen für Produktionsdaten

### 🟡 Intermediate-Ziele

- ✅ Alle Zahlentypen inklusive complex verwenden
- ✅ Erweiterte String-Verarbeitung mit Regex
- ✅ Komplexe Datenstrukturen verschachteln
- ✅ Statistische Berechnungen implementieren
- ✅ Robuste Fehlerbehandlung anwenden

### 🔴 Advanced-Ziele

- ✅ Objektorientierte Datenmodellierung
- ✅ Design Patterns implementieren
- ✅ Performance-Optimierung anwenden
- ✅ Enterprise-Level Fehlerbehandlung
- ✅ Professionelle Dokumentation erstellen

## 💡 Tipps

- **Folgen Sie Ihrem Assessment-Ergebnis** für optimale Lernerfahrung
- **Nutzen Sie das Hilfesystem** bei Schwierigkeiten
- **Experimentieren Sie** mit den Code-Beispielen
- **Verstehen Sie die Bystronic-Kontexte** in den Übungen

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss der Übungen:
→ **[Kapitel 3: NumPy](../../03_numpy/)** - Numerische Berechnungen
