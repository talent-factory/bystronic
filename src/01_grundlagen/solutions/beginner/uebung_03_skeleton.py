#!/usr/bin/env python3
"""
🟢 SKELETON: Übung 3 - Programmiersprachen-Liste (Beginner)
===========================================================

ANLEITUNG:
Füllen Sie die TODO-Bereiche aus. Das Grundgerüst ist bereits vorhanden.
Folgen Sie den Kommentaren Schritt für Schritt.

HILFE:
- Verwenden Sie eckige Klammern [] für Listen
- Verwenden Sie append() zum Hinzufügen
- Verwenden Sie enumerate() für nummerierte Ausgaben
"""

print("💻 MEINE PROGRAMMIERSPRACHEN-LISTE")
print("=" * 35)

# TODO 1: Erstellen Sie eine Liste mit Ihren Lieblings-Programmiersprachen
# TIPP: Verwenden Sie eckige Klammern [] und Anführungszeichen für Strings
meine_sprachen = # HIER IHRE LISTE ERSTELLEN

print("Meine ursprüngliche Liste:")
print(meine_sprachen)

# TODO 2: Prüfen Sie, ob Python in der Liste ist
# TIPP: Verwenden Sie den 'in' Operator
if # HIER PRÜFUNG ERGÄNZEN:
    print("\n✅ Python ist bereits in der Liste!")
else:
    print("\n➕ Python wird zur Liste hinzugefügt...")
    # TODO 3: Fügen Sie Python zur Liste hinzu
    # TIPP: Verwenden Sie die append() Methode
    # HIER PYTHON HINZUFÜGEN

print("\nListe nach Python-Prüfung:")
print(meine_sprachen)

# TODO 4: Sortieren Sie die Liste alphabetisch
# TIPP: Verwenden Sie die sort() Methode
# HIER SORTIEREN

print("\nAlphabetisch sortierte Liste:")
print(meine_sprachen)

# TODO 5: Geben Sie jede Sprache mit Nummer aus
# TIPP: Verwenden Sie eine for-Schleife mit enumerate()
print("\n📋 NUMMERIERTE LISTE:")
print("-" * 25)

# HIER FOR-SCHLEIFE MIT ENUMERATE ERGÄNZEN
for # HIER ERGÄNZEN:
    print(f"# HIER FORMATIERTE AUSGABE")

# TODO 6: Zeigen Sie Statistiken an
# TIPP: Verwenden Sie len() für die Anzahl
anzahl_sprachen = # HIER ERGÄNZEN
print("-" * 25)
print(f"Gesamt: {anzahl_sprachen} Programmiersprachen")

# BONUS: Finden Sie die längste und kürzeste Sprache
if meine_sprachen:  # Prüfe ob Liste nicht leer ist
    # TODO: Verwenden Sie max() und min() mit key=len
    laengste = # HIER ERGÄNZEN
    kuerzeste = # HIER ERGÄNZEN

    print(f"\n📊 STATISTIKEN:")
    print(f"Längste Sprache:  {laengste} ({len(laengste)} Zeichen)")
    print(f"Kürzeste Sprache: {kuerzeste} ({len(kuerzeste)} Zeichen)")

print("\n🎉 Fertig! Sie kennen sich mit Listen aus!")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
💻 MEINE PROGRAMMIERSPRACHEN-LISTE
===================================
Meine ursprüngliche Liste:
['Java', 'C#', 'JavaScript']

➕ Python wird zur Liste hinzugefügt...

Liste nach Python-Prüfung:
['Java', 'C#', 'JavaScript', 'Python']

Alphabetisch sortierte Liste:
['C#', 'Java', 'JavaScript', 'Python']

📋 NUMMERIERTE LISTE:
-------------------------
1. C#
2. Java
3. JavaScript
4. Python
-------------------------
Gesamt: 4 Programmiersprachen

📊 STATISTIKEN:
Längste Sprache:  JavaScript (10 Zeichen)
Kürzeste Sprache: C# (2 Zeichen)

🎉 Fertig! Sie kennen sich mit Listen aus!

HILFEN ZUM AUSFÜLLEN:
=====================
□ Liste erstellen: ["Sprache1", "Sprache2", "Sprache3"]
□ Python prüfen: "Python" in meine_sprachen
□ Python hinzufügen: meine_sprachen.append("Python")
□ Sortieren: meine_sprachen.sort()
□ Enumerate: for nummer, sprache in enumerate(meine_sprachen, 1)
□ Ausgabe: print(f"{nummer}. {sprache}")
□ Anzahl: len(meine_sprachen)
□ Längste: max(meine_sprachen, key=len)
□ Kürzeste: min(meine_sprachen, key=len)

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Dieses Grundgerüst (Sie sind hier!)
3. partial.py   - Teilweise implementiert
4. complete.py  - Vollständige Lösung
"""
