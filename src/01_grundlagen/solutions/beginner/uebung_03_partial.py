#!/usr/bin/env python3
"""
🟢 PARTIAL: Übung 3 - Programmiersprachen-Liste (Beginner)
==========================================================

ANLEITUNG:
Diese Version ist fast vollständig implementiert. Nur wenige Lücken müssen
noch gefüllt werden. Perfekt, wenn Sie fast fertig sind!

HILFE:
- Die meiste Arbeit ist bereits getan
- Nur noch 3-4 kleine Ergänzungen nötig
- Schauen Sie nach den # ERGÄNZEN Kommentaren
"""

print("💻 MEINE PROGRAMMIERSPRACHEN-LISTE")
print("=" * 35)

# Liste mit Programmiersprachen erstellen
meine_sprachen = ["Java", "C#", "JavaScript", "VBA", "SQL"]

print("Meine ursprüngliche Liste:")
print(meine_sprachen)

# Prüfen ob Python in der Liste ist
if "Python" in meine_sprachen:
    print("\n✅ Python ist bereits in der Liste!")
else:
    print("\n➕ Python wird zur Liste hinzugefügt...")
    meine_sprachen.append("Python")

print("\nListe nach Python-Prüfung:")
print(meine_sprachen)

# Liste alphabetisch sortieren
meine_sprachen.sort()

print("\nAlphabetisch sortierte Liste:")
print(meine_sprachen)

# Nummerierte Ausgabe
print("\n📋 NUMMERIERTE LISTE:")
print("-" * 25)

# TODO: Ergänzen Sie die for-Schleife mit enumerate
for nummer, sprache in enumerate(meine_sprachen, 1):
    # TODO: Ergänzen Sie die formatierte Ausgabe
    print(f"# ERGÄNZEN: {nummer}. {sprache}")

# Statistiken anzeigen
anzahl_sprachen = len(meine_sprachen)
print("-" * 25)
print(f"Gesamt: {anzahl_sprachen} Programmiersprachen")

# Längste und kürzeste Sprache finden
if meine_sprachen:
    # TODO: Ergänzen Sie max() und min() mit key=len
    laengste = max(meine_sprachen, key=len)
    kuerzeste = # ERGÄNZEN

    print(f"\n📊 STATISTIKEN:")
    print(f"Längste Sprache:  {laengste} ({len(laengste)} Zeichen)")
    print(f"Kürzeste Sprache: {kuerzeste} ({len(kuerzeste)} Zeichen)")

# Zusätzliche Statistiken
print(f"\n🔍 WEITERE ANALYSEN:")
print(f"Durchschnittliche Länge: {sum(len(s) for s in meine_sprachen) / len(meine_sprachen):.1f} Zeichen")

# TODO: Ergänzen Sie eine Analyse der Sprachen mit bestimmten Buchstaben
sprachen_mit_j = [s for s in meine_sprachen if 'J' in s or 'j' in s]
print(f"Sprachen mit 'J': {len(sprachen_mit_j)} → {sprachen_mit_j}")

# TODO: Ergänzen Sie eine Nachricht basierend auf der Anzahl der Sprachen
if anzahl_sprachen >= 5:
    print("# ERGÄNZEN: Nachricht für viele Sprachen (≥5)")
elif anzahl_sprachen >= 3:
    print("Das ist eine solide Basis an Programmiersprachen! 👍")
else:
    print("Ein guter Anfang - Sie können gerne mehr Sprachen lernen! 🌱")

print("\n🎉 Fertig! Sie kennen sich mit Listen aus!")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
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

🔍 WEITERE ANALYSEN:
Durchschnittliche Länge: 5.2 Zeichen
Sprachen mit 'J': 2 → ['Java', 'JavaScript']
Wow! Sie kennen schon viele Programmiersprachen! 🌟

🎉 Fertig! Sie kennen sich mit Listen aus!

WAS FEHLT NOCH:
===============
□ Formatierte Ausgabe in der for-Schleife
□ min() Funktion für kürzeste Sprache
□ Nachricht für viele Sprachen (≥5)

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Code-Grundgerüst
3. partial.py   - Teilweise implementiert (Sie sind hier!)
4. complete.py  - Vollständige Lösung
"""
