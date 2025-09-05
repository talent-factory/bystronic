#!/usr/bin/env python3
"""
🟢 COMPLETE: Übung 3 - Programmiersprachen-Liste (Beginner)
===========================================================

MUSTERLÖSUNG:
Dies ist eine vollständige, professionelle Lösung der Übung.
Verwenden Sie diese nur, wenn Sie wirklich nicht weiterkommen!

LERNZIELE ERFÜLLT:
✅ Listen erstellen und verwenden
✅ append() zum Hinzufügen von Elementen
✅ sort() zum Sortieren von Listen
✅ for-Schleifen mit enumerate() für nummerierte Ausgaben
✅ 'in' Operator zum Prüfen von Inhalten
✅ len(), max(), min() für Statistiken
"""

print("💻 MEINE PROGRAMMIERSPRACHEN-LISTE")
print("=" * 35)

# Liste mit Lieblings-Programmiersprachen erstellen
meine_sprachen = ["Java", "C#", "JavaScript", "VBA", "SQL", "TypeScript"]

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

# Nummerierte Ausgabe mit schöner Formatierung
print("\n📋 NUMMERIERTE LISTE:")
print("-" * 25)

for nummer, sprache in enumerate(meine_sprachen, 1):
    print(f"{nummer:2d}. {sprache}")

# Grundstatistiken
anzahl_sprachen = len(meine_sprachen)
print("-" * 25)
print(f"Gesamt: {anzahl_sprachen} Programmiersprachen")

# Längste und kürzeste Sprache finden
if meine_sprachen:
    laengste = max(meine_sprachen, key=len)
    kuerzeste = min(meine_sprachen, key=len)

    print("\n📊 LÄNGEN-STATISTIKEN:")
    print(f"Längste Sprache:  {laengste} ({len(laengste)} Zeichen)")
    print(f"Kürzeste Sprache: {kuerzeste} ({len(kuerzeste)} Zeichen)")

    # Durchschnittliche Länge berechnen
    durchschnitt = sum(len(sprache) for sprache in meine_sprachen) / len(meine_sprachen)
    print(f"Durchschnittliche Länge: {durchschnitt:.1f} Zeichen")

# Erweiterte Analysen
print("\n🔍 ERWEITERTE ANALYSEN:")

# Sprachen nach Kategorien
web_sprachen = [
    s for s in meine_sprachen if s in ["JavaScript", "TypeScript", "HTML", "CSS", "PHP"]
]
system_sprachen = [
    s for s in meine_sprachen if s in ["C", "C++", "C#", "Java", "Rust", "Go"]
]
script_sprachen = [
    s for s in meine_sprachen if s in ["Python", "JavaScript", "VBA", "PowerShell"]
]

print(f"Web-Sprachen:    {len(web_sprachen)} → {web_sprachen}")
print(f"System-Sprachen: {len(system_sprachen)} → {system_sprachen}")
print(f"Script-Sprachen: {len(script_sprachen)} → {script_sprachen}")

# Sprachen mit bestimmten Buchstaben
sprachen_mit_j = [s for s in meine_sprachen if "J" in s or "j" in s]
sprachen_mit_s = [s for s in meine_sprachen if s.startswith("S") or s.startswith("s")]

print(f"Sprachen mit 'J': {len(sprachen_mit_j)} → {sprachen_mit_j}")
print(f"Sprachen mit 'S': {len(sprachen_mit_s)} → {sprachen_mit_s}")

# Sprachen nach Länge sortiert
print("\n📏 NACH LÄNGE SORTIERT:")
sprachen_nach_laenge = sorted(meine_sprachen, key=len)
for i, sprache in enumerate(sprachen_nach_laenge, 1):
    balken = "█" * len(sprache)
    print(f"{i:2d}. {sprache:<12} {balken} ({len(sprache)})")

# Bewertung basierend auf Anzahl
print("\n🎯 BEWERTUNG:")
if anzahl_sprachen >= 7:
    print("Wow! Sie kennen schon sehr viele Programmiersprachen! 🌟")
    print("Sie sind ein echter Polyglott-Programmierer!")
elif anzahl_sprachen >= 5:
    print("Beeindruckend! Das ist eine solide Basis an Programmiersprachen! 👍")
    print("Sie haben eine gute Vielfalt an Technologien!")
elif anzahl_sprachen >= 3:
    print("Das ist ein guter Start! Sie kennen die wichtigsten Sprachen! 🚀")
    print("Perfekt für die meisten Entwicklungsprojekte!")
else:
    print("Ein guter Anfang - Sie können gerne mehr Sprachen lernen! 🌱")
    print("Jede neue Sprache erweitert Ihren Horizont!")

# Empfehlungen basierend auf vorhandenen Sprachen
print("\n💡 EMPFEHLUNGEN:")
if "JavaScript" in meine_sprachen and "TypeScript" not in meine_sprachen:
    print("• Da Sie JavaScript kennen, wäre TypeScript ein logischer nächster Schritt!")
if "Python" in meine_sprachen and "Java" not in meine_sprachen:
    print("• Python-Kenntnisse helfen beim Erlernen von Java!")
if "C#" in meine_sprachen and "Java" not in meine_sprachen:
    print("• C# und Java sind sehr ähnlich - Java wäre einfach zu lernen!")
if len([s for s in meine_sprachen if s in ["HTML", "CSS", "JavaScript"]]) < 2:
    print("• Für Web-Entwicklung sind HTML, CSS und JavaScript essentiell!")

# Motivierende Abschlussnachricht
print("\n🎉 GRATULATION!")
print("Sie haben erfolgreich mit Listen gearbeitet!")
print("Listen sind eine der wichtigsten Datenstrukturen in Python.")

# Interessante Fakten
print("\n🤓 WUSSTEN SIE SCHON?")
gesamtzeichen = sum(len(sprache) for sprache in meine_sprachen)
print(f"• Ihre Sprachen haben zusammen {gesamtzeichen} Zeichen")
print(
    f"• Das sind durchschnittlich {gesamtzeichen / anzahl_sprachen:.1f} Zeichen pro Sprache"
)

# Zeige alle einzigartigen Buchstaben
alle_buchstaben = set("".join(meine_sprachen).lower())
print(f"• Ihre Sprachen verwenden {len(alle_buchstaben)} verschiedene Buchstaben")

print("\n🎯 NÄCHSTE SCHRITTE:")
print("✅ Listen verstanden? Probieren Sie Dictionaries!")
print("✅ Zu einfach? Versuchen Sie die Intermediate-Version!")
print("✅ Neugierig? Experimentieren Sie mit List Comprehensions!")

print("\n🎉 Fertig! Sie sind jetzt ein Listen-Experte! 🐍")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
💻 MEINE PROGRAMMIERSPRACHEN-LISTE
===================================
Meine ursprüngliche Liste:
['Java', 'C#', 'JavaScript', 'VBA', 'SQL', 'TypeScript']

➕ Python wird zur Liste hinzugefügt...

Liste nach Python-Prüfung:
['Java', 'C#', 'JavaScript', 'VBA', 'SQL', 'TypeScript', 'Python']

Alphabetisch sortierte Liste:
['C#', 'Java', 'JavaScript', 'Python', 'SQL', 'TypeScript', 'VBA']

📋 NUMMERIERTE LISTE:
-------------------------
 1. C#
 2. Java
 3. JavaScript
 4. Python
 5. SQL
 6. TypeScript
 7. VBA
-------------------------
Gesamt: 7 Programmiersprachen

📊 LÄNGEN-STATISTIKEN:
Längste Sprache:  JavaScript (10 Zeichen)
Kürzeste Sprache: C# (2 Zeichen)
Durchschnittliche Länge: 6.1 Zeichen

🔍 ERWEITERTE ANALYSEN:
Web-Sprachen:    2 → ['JavaScript', 'TypeScript']
System-Sprachen: 2 → ['C#', 'Java']
Script-Sprachen: 3 → ['JavaScript', 'Python', 'VBA']
Sprachen mit 'J': 2 → ['Java', 'JavaScript']
Sprachen mit 'S': 1 → ['SQL']

📏 NACH LÄNGE SORTIERT:
 1. C#           ██ (2)
 2. SQL          ███ (3)
 3. VBA          ███ (3)
 4. Java         ████ (4)
 5. Python       ██████ (6)
 6. JavaScript   ██████████ (10)
 7. TypeScript   ██████████ (10)

🎯 BEWERTUNG:
Wow! Sie kennen schon sehr viele Programmiersprachen! 🌟
Sie sind ein echter Polyglott-Programmierer!

💡 EMPFEHLUNGEN:
• Für Web-Entwicklung sind HTML, CSS und JavaScript essentiell!

🎉 GRATULATION!
Sie haben erfolgreich mit Listen gearbeitet!
Listen sind eine der wichtigsten Datenstrukturen in Python.

🤓 WUSSTEN SIE SCHON?
• Ihre Sprachen haben zusammen 43 Zeichen
• Das sind durchschnittlich 6.1 Zeichen pro Sprache
• Ihre Sprachen verwenden 16 verschiedene Buchstaben

🎯 NÄCHSTE SCHRITTE:
✅ Listen verstanden? Probieren Sie Dictionaries!
✅ Zu einfach? Versuchen Sie die Intermediate-Version!
✅ Neugierig? Experimentieren Sie mit List Comprehensions!

🎉 Fertig! Sie sind jetzt ein Listen-Experte! 🐍

VERWENDETE KONZEPTE:
====================
✅ Listen erstellen und manipulieren
✅ append() - Elemente hinzufügen
✅ sort() - Listen sortieren
✅ 'in' Operator - Inhalte prüfen
✅ enumerate() - Nummerierte Iteration
✅ len(), max(), min() - Statistiken
✅ List Comprehensions - Erweiterte Filterung
✅ String-Methoden - startswith(), lower()
✅ set() - Eindeutige Elemente
✅ sorted() mit key Parameter
✅ f-strings mit Formatierung

NÄCHSTE SCHRITTE:
=================
🎯 Verstehen Sie alle Konzepte? Probieren Sie die Intermediate-Version!
🚀 Zu einfach? Experimentieren Sie mit eigenen Listen!
💡 Neugierig? Lernen Sie über Dictionaries und Tupel!
"""
