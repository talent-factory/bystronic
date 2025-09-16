#!/usr/bin/env python3
"""
🟢 SKELETON: Übung 2 - Taschenrechner (Beginner)
================================================

ANLEITUNG:
Füllen Sie die TODO-Bereiche aus. Das Grundgerüst ist bereits vorhanden.
Folgen Sie den Kommentaren Schritt für Schritt.

HILFE:
- Verwenden Sie float() für Zahlen-Eingaben
- Verwenden Sie if/elif/else für verschiedene Operationen
- Prüfen Sie Division durch Null!
"""

# TODO 1: Begrüssung ausgeben
print("🧮 EINFACHER TASCHENRECHNER")
print("=" * 30)
print("Führen Sie einfache Berechnungen durch!")

# TODO 2: Zahlen eingeben
print("\nGeben Sie zwei Zahlen ein:")

# Erste Zahl eingeben
# TODO: Ergänzen Sie die Eingabe für die erste Zahl
zahl1 = float(input("Erste Zahl: "))

# Zweite Zahl eingeben
# TODO: Ergänzen Sie die Eingabe für die zweite Zahl
zahl2 = # HIER ERGÄNZEN

# TODO 3: Operation wählen
print("\nVerfügbare Operationen:")
print("+ für Addition")
print("- für Subtraktion")
print("* für Multiplikation")
print("/ für Division")

# TODO: Ergänzen Sie die Eingabe für die Operation
operation = # HIER ERGÄNZEN

# TODO 4: Berechnung durchführen
print(f"\nBerechnung: {zahl1} {operation} {zahl2}")

# TODO: Ergänzen Sie die if/elif/else Struktur
if operation == "+":
    # TODO: Addition berechnen
    ergebnis = # HIER ERGÄNZEN
    print(f"Ergebnis: {ergebnis}")

elif operation == "-":
    # TODO: Subtraktion berechnen
    ergebnis = # HIER ERGÄNZEN
    print(f"Ergebnis: {ergebnis}")

elif operation == "*":
    # TODO: Multiplikation berechnen
    ergebnis = # HIER ERGÄNZEN
    print(f"Ergebnis: {ergebnis}")

elif operation == "/":
    # TODO: Division mit Null-Prüfung
    if zahl2 != 0:
        ergebnis = # HIER ERGÄNZEN
        print(f"Ergebnis: {ergebnis}")
    else:
        print("❌ Fehler: Division durch Null ist nicht möglich!")

else:
    # TODO: Fehlermeldung für ungültige Operation
    print("# HIER FEHLERMELDUNG ERGÄNZEN")

# TODO 5: Verabschiedung
print("\nVielen Dank für die Nutzung des Taschenrechners! 🧮")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
🧮 EINFACHER TASCHENRECHNER
==============================
Führen Sie einfache Berechnungen durch!

Geben Sie zwei Zahlen ein:
Erste Zahl: 15
Zweite Zahl: 3

Verfügbare Operationen:
+ für Addition
- für Subtraktion
* für Multiplikation
/ für Division
Operation (+, -, *, /): /

Berechnung: 15.0 / 3.0
Ergebnis: 5.0

Vielen Dank für die Nutzung des Taschenrechners! 🧮

TESTFÄLLE:
==========
✅ Addition: 5 + 3 = 8
✅ Subtraktion: 10 - 4 = 6
✅ Multiplikation: 7 * 2 = 14
✅ Division: 15 / 3 = 5.0
❌ Division durch Null: 5 / 0 → Fehlermeldung
❌ Ungültige Operation: 5 % 3 → Fehlermeldung

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Dieses Grundgerüst (Sie sind hier!)
3. partial.py   - Teilweise implementiert
4. complete.py  - Vollständige Lösung
"""
