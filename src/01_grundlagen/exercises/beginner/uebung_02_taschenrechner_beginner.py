#!/usr/bin/env python3
"""
🟢 BEGINNER: Übung 2 - Einfacher Taschenrechner
==============================================

LERNZIELE:
- Grundrechenarten verstehen
- Einfache Funktionen schreiben
- Benutzereingaben verarbeiten
- Grundlegende Fehlerbehandlung

AUFGABE:
Erstellen Sie einen einfachen Taschenrechner für die vier Grundrechenarten.

ZEIT: 15-25 Minuten
SCHWIERIGKEIT: 🟢 Anfänger

HILFEN VERFÜGBAR:
- hints.md - Konzeptuelle Tipps
- skeleton.py - Code-Grundgerüst
- partial.py - Teilweise implementiert
- complete.py - Vollständige Lösung
"""

print("🧮 EINFACHER TASCHENRECHNER")
print("=" * 30)

# TODO 1: Erste Zahl eingeben
print("Geben Sie zwei Zahlen ein:")
zahl1 = float(input("Erste Zahl: "))

# TODO 2: Zweite Zahl eingeben
zahl2 = float(input("Zweite Zahl: "))

# TODO 3: Operation wählen
print("\nWählen Sie eine Operation:")
print("1. Addition (+)")
print("2. Subtraktion (-)")
print("3. Multiplikation (×)")
print("4. Division (÷)")

operation = input("Ihre Wahl (1-4): ")

# TODO 4: Berechnung durchführen
print(f"\nBerechnung mit {zahl1} und {zahl2}:")

if operation == "1":
    # Addition
    ergebnis = zahl1 + zahl2
    print(f"{zahl1} + {zahl2} = {ergebnis}")

elif operation == "2":
    # Subtraktion
    ergebnis = zahl1 - zahl2
    print(f"{zahl1} - {zahl2} = {ergebnis}")

elif operation == "3":
    # Multiplikation
    ergebnis = zahl1 * zahl2
    print(f"{zahl1} × {zahl2} = {ergebnis}")

elif operation == "4":
    # Division
    if zahl2 != 0:  # Prüfe Division durch Null
        ergebnis = zahl1 / zahl2
        print(f"{zahl1} ÷ {zahl2} = {ergebnis}")
    else:
        print("❌ Fehler: Division durch Null ist nicht möglich!")

else:
    print("❌ Ungültige Auswahl!")

print("\n🎉 Vielen Dank für die Nutzung des Taschenrechners!")

"""
ERWARTETE AUSGABE:
==================
🧮 EINFACHER TASCHENRECHNER
==============================
Geben Sie zwei Zahlen ein:
Erste Zahl: 15
Zweite Zahl: 3

Wählen Sie eine Operation:
1. Addition (+)
2. Subtraktion (-)
3. Multiplikation (×)
4. Division (÷)
Ihre Wahl (1-4): 4

Berechnung mit 15.0 und 3.0:
15.0 ÷ 3.0 = 5.0

🎉 Vielen Dank für die Nutzung des Taschenrechners!

NÄCHSTE SCHRITTE:
=================
✅ Wenn das funktioniert: Versuchen Sie die Intermediate-Version!
❓ Bei Problemen: Schauen Sie in die Hilfen (hints.md)
🎯 Verstehen Sie if/elif/else? Experimentieren Sie mit verschiedenen Operationen!

LERNKONTROLLE:
==============
□ Kann ich float() für Zahlen verwenden?
□ Verstehe ich if/elif/else Bedingungen?
□ Kann ich einfache Berechnungen durchführen?
□ Verstehe ich die Division-durch-Null Prüfung?

BONUS-AUFGABEN:
===============
🌟 Fügen Sie eine Schleife hinzu, um mehrere Berechnungen zu ermöglichen
🌟 Formatieren Sie das Ergebnis auf 2 Dezimalstellen
🌟 Fügen Sie mehr Operationen hinzu (Potenz, Wurzel)
"""
