#!/usr/bin/env python3
"""
🟢 BEGINNER: Übung 1 - Persönliche Informationen
===============================================

LERNZIELE:
- Eingabe mit input() verstehen
- Variablen verwenden
- Einfache Ausgabe mit print()
- String-Formatierung mit f-strings

AUFGABE:
Erstellen Sie ein einfaches Programm, das nach Name und Alter fragt
und eine freundliche Begrüssung ausgibt.

ZEIT: 15-25 Minuten
SCHWIERIGKEIT: 🟢 Anfänger

HILFEN VERFÜGBAR:
- hints.md - Konzeptuelle Tipps
- skeleton.py - Code-Grundgerüst
- partial.py - Teilweise implementiert
- complete.py - Vollständige Lösung
"""

# TODO 1: Fragen Sie nach dem Namen
# TIPP: Verwenden Sie input("Frage: ")
name = input("Wie heissen Sie? ")

# TODO 2: Fragen Sie nach dem Alter
# TIPP: Verwenden Sie int() um Text in Zahl umzuwandeln
alter_text = input("Wie alt sind Sie? ")
alter = int(alter_text)

# TODO 3: Berechnen Sie das Geburtsjahr
# TIPP: Aktuelles Jahr minus Alter
aktuelles_jahr = 2025
geburtsjahr = aktuelles_jahr - alter

# TODO 4: Geben Sie eine freundliche Begrüssung aus
# TIPP: Verwenden Sie f-strings: f"Hallo {name}!"
print(f"Hallo {name}!")
print(f"Sie sind {alter} Jahre alt.")
print(f"Sie wurden ungefähr im Jahr {geburtsjahr} geboren.")

# BONUS: Fügen Sie eine schöne Formatierung hinzu
print("=" * 40)
print("🎉 Willkommen bei SmartFactory!")
print("=" * 40)

"""
ERWARTETE AUSGABE:
==================
Wie heissen Sie? Max Mustermann
Wie alt sind Sie? 30

Hallo Max Mustermann!
Sie sind 30 Jahre alt.
Sie wurden ungefähr im Jahr 1995 geboren.
========================================
🎉 Willkommen bei SmartFactory!
========================================

NÄCHSTE SCHRITTE:
=================
✅ Wenn das funktioniert: Versuchen Sie die Intermediate-Version!
❓ Bei Problemen: Schauen Sie in die Hilfen (hints.md)
🎯 Verstehen Sie f-strings? Experimentieren Sie mit verschiedenen Formaten!

LERNKONTROLLE:
==============
□ Kann ich input() verwenden?
□ Kann ich Strings in Zahlen umwandeln?
□ Verstehe ich f-string Formatierung?
□ Kann ich einfache Berechnungen durchführen?
"""
