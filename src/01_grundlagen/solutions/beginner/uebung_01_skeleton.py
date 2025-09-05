#!/usr/bin/env python3
"""
🟢 SKELETON: Übung 1 - Persönliche Informationen (Beginner)
===========================================================

ANLEITUNG:
Füllen Sie die TODO-Bereiche aus. Das Grundgerüst ist bereits vorhanden.
Folgen Sie den Kommentaren Schritt für Schritt.

HILFE:
- Verwenden Sie input() für Eingaben
- Verwenden Sie f-strings für formatierte Ausgaben
- Testen Sie nach jedem Schritt
"""

# TODO 1: Begrüssung ausgeben
print("=" * 40)
print("WILLKOMMEN BEI BYSTRONIC!")
print("=" * 40)
print("Erzählen Sie uns etwas über sich...")

# TODO 2: Nach persönlichen Informationen fragen
# TIPP: Verwenden Sie input() und speichern Sie in Variablen

# Frage nach dem Namen
name = input("Wie heissen Sie? ")

# Frage nach dem Alter
# TODO: Ergänzen Sie hier die Eingabe für das Alter
alter = # HIER ERGÄNZEN

# Frage nach dem Wohnort
# TODO: Ergänzen Sie hier die Eingabe für den Wohnort
wohnort = # HIER ERGÄNZEN

# Frage nach dem Beruf
# TODO: Ergänzen Sie hier die Eingabe für den Beruf
beruf = # HIER ERGÄNZEN

# TODO 3: Zusammenfassung ausgeben
print("\n" + "=" * 40)
print("IHRE ANGABEN:")
print("=" * 40)

# TODO: Geben Sie alle Informationen formatiert aus
# TIPP: Verwenden Sie f-strings wie f"Name: {name}"

print(f"Name:     {name}")
# TODO: Ergänzen Sie die anderen Ausgaben
print(f"Alter:    # HIER ERGÄNZEN")
print(f"Wohnort:  # HIER ERGÄNZEN")
print(f"Beruf:    # HIER ERGÄNZEN")

# TODO 4: Persönliche Nachricht erstellen
print("\n" + "-" * 40)
# TODO: Erstellen Sie eine persönliche Nachricht mit allen Daten
# BEISPIEL: f"Hallo {name}! Schön, dass Sie aus {wohnort} zu uns gefunden haben!"

print(f"# HIER EINE PERSÖNLICHE NACHRICHT ERSTELLEN")

# TODO 5: Verabschiedung
print("-" * 40)
print("Vielen Dank für Ihre Angaben!")
print("Willkommen im Bystronic Python-Kurs! 🐍")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
========================================
WILLKOMMEN BEI BYSTRONIC!
========================================
Erzählen Sie uns etwas über sich...
Wie heissen Sie? Max Mustermann
Wie alt sind Sie? 28
Wo wohnen Sie? Zürich
Was ist Ihr Beruf? Ingenieur

========================================
IHRE ANGABEN:
========================================
Name:     Max Mustermann
Alter:    28
Wohnort:  Zürich
Beruf:    Ingenieur

----------------------------------------
Hallo Max Mustermann! Schön, dass Sie aus Zürich zu uns gefunden haben!
Als Ingenieur werden Sie sicher viel Freude an der Programmierung haben.
----------------------------------------
Vielen Dank für Ihre Angaben!
Willkommen im Bystronic Python-Kurs! 🐍

NÄCHSTE SCHRITTE:
=================
✅ Wenn das funktioniert: Versuchen Sie eigene Verbesserungen!
❓ Bei Problemen: Schauen Sie in partial.py für mehr Hilfe
🎯 Verstehen Sie alles? Probieren Sie die Intermediate-Version!

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Dieses Grundgerüst (Sie sind hier!)
3. partial.py   - Teilweise implementiert
4. complete.py  - Vollständige Lösung
"""
