#!/usr/bin/env python3
"""
🟢 BEGINNER: Übung 3 - Meine Programmiersprachen-Liste
=====================================================

LERNZIELE:
- Listen erstellen und verwenden
- Elemente zu Listen hinzufügen
- Listen sortieren
- For-Schleifen verstehen
- Einfache Bedingungen (if/else)

AUFGABE:
Erstellen Sie eine Liste Ihrer Lieblings-Programmiersprachen,
fügen Sie Python hinzu und geben Sie alle Sprachen nummeriert aus.

ZEIT: 15-25 Minuten
SCHWIERIGKEIT: 🟢 Anfänger

HILFEN VERFÜGBAR:
- hints.md - Konzeptuelle Tipps
- skeleton.py - Code-Grundgerüst
- partial.py - Teilweise implementiert
- complete.py - Vollständige Lösung
"""

print("💻 MEINE PROGRAMMIERSPRACHEN-LISTE")
print("=" * 35)

# TODO 1: Erstellen Sie eine Liste mit Ihren Lieblings-Programmiersprachen
# TIPP: Verwenden Sie eckige Klammern [] und Anführungszeichen für Strings
meine_sprachen = ["Java", "C#", "JavaScript", "VBA", "SQL"]

print("Meine ursprüngliche Liste:")
print(meine_sprachen)

# TODO 2: Prüfen Sie, ob Python in der Liste ist
# TIPP: Verwenden Sie den 'in' Operator
if "Python" in meine_sprachen:
    print("\n✅ Python ist bereits in der Liste!")
else:
    print("\n➕ Python wird zur Liste hinzugefügt...")
    # TODO 3: Fügen Sie Python zur Liste hinzu
    # TIPP: Verwenden Sie die append() Methode
    meine_sprachen.append("Python")

print("\nListe nach Python-Prüfung:")
print(meine_sprachen)

# TODO 4: Sortieren Sie die Liste alphabetisch
# TIPP: Verwenden Sie die sort() Methode
meine_sprachen.sort()

print("\nAlphabetisch sortierte Liste:")
print(meine_sprachen)

# TODO 5: Geben Sie jede Sprache mit Nummer aus
# TIPP: Verwenden Sie eine for-Schleife mit enumerate()
print("\n📋 NUMMERIERTE LISTE:")
print("-" * 25)

for nummer, sprache in enumerate(meine_sprachen, 1):
    print(f"{nummer}. {sprache}")

# TODO 6: Zeigen Sie Statistiken an
anzahl_sprachen = len(meine_sprachen)
print("-" * 25)
print(f"Gesamt: {anzahl_sprachen} Programmiersprachen")

# BONUS: Finden Sie die längste und kürzeste Sprache
if meine_sprachen:  # Prüfe ob Liste nicht leer ist
    laengste = max(meine_sprachen, key=len)
    kuerzeste = min(meine_sprachen, key=len)

    print("\n📊 STATISTIKEN:")
    print(f"Längste Sprache:  {laengste} ({len(laengste)} Zeichen)")
    print(f"Kürzeste Sprache: {kuerzeste} ({len(kuerzeste)} Zeichen)")

print("\n🎉 Fertig! Sie kennen sich mit Listen aus!")

"""
ERWARTETE AUSGABE:
==================
💻 MEINE PROGRAMMIERSPRACHEN-LISTE
===================================
Meine ursprüngliche Liste:
['Java', 'C#', 'JavaScript', 'VBA', 'SQL']

➕ Python wird zur Liste hinzugefügt...

Liste nach Python-Prüfung:
['Java', 'C#', 'JavaScript', 'VBA', 'SQL', 'Python']

Alphabetisch sortierte Liste:
['C#', 'Java', 'JavaScript', 'Python', 'SQL', 'VBA']

📋 NUMMERIERTE LISTE:
-------------------------
1. C#
2. Java
3. JavaScript
4. Python
5. SQL
6. VBA
-------------------------
Gesamt: 6 Programmiersprachen

📊 STATISTIKEN:
Längste Sprache:  JavaScript (10 Zeichen)
Kürzeste Sprache: C# (2 Zeichen)

🎉 Fertig! Sie kennen sich mit Listen aus!

NÄCHSTE SCHRITTE:
=================
✅ Wenn das funktioniert: Versuchen Sie die Intermediate-Version!
❓ Bei Problemen: Schauen Sie in die Hilfen (hints.md)
🎯 Verstehen Sie Listen? Experimentieren Sie mit anderen Methoden!

LERNKONTROLLE:
==============
□ Kann ich Listen erstellen?
□ Verstehe ich den 'in' Operator?
□ Kann ich Elemente zu Listen hinzufügen?
□ Kann ich Listen sortieren?
□ Verstehe ich for-Schleifen mit enumerate()?

BONUS-AUFGABEN:
===============
🌟 Fügen Sie mehr Sprachen hinzu
🌟 Entfernen Sie eine Sprache aus der Liste
🌟 Erstellen Sie eine zweite Liste und kombinieren Sie beide
"""
