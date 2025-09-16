#!/usr/bin/env python3
"""
🟢 PARTIAL: Übung 2 - Taschenrechner (Beginner)
===============================================

ANLEITUNG:
Diese Version ist fast vollständig implementiert. Nur wenige Lücken müssen
noch gefüllt werden. Perfekt, wenn Sie fast fertig sind!

HILFE:
- Die meiste Arbeit ist bereits getan
- Nur noch 2-3 kleine Ergänzungen nötig
- Schauen Sie nach den # ERGÄNZEN Kommentaren
"""

# Begrüssung ausgeben
print("🧮 EINFACHER TASCHENRECHNER")
print("=" * 30)
print("Führen Sie einfache Berechnungen durch!")

# Zahlen eingeben
print("\nGeben Sie zwei Zahlen ein:")
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

# Operation wählen
print("\nVerfügbare Operationen:")
print("+ für Addition")
print("- für Subtraktion")
print("* für Multiplikation")
print("/ für Division")

operation = input("Operation (+, -, *, /): ")

# Berechnung durchführen
print(f"\nBerechnung: {zahl1} {operation} {zahl2}")

if operation == "+":
    ergebnis = zahl1 + zahl2
    print(f"Ergebnis: {ergebnis}")

elif operation == "-":
    ergebnis = zahl1 - zahl2
    print(f"Ergebnis: {ergebnis}")

elif operation == "*":
    # TODO: Ergänzen Sie die Multiplikation
    ergebnis = # ERGÄNZEN
    print(f"Ergebnis: {ergebnis}")

elif operation == "/":
    if zahl2 != 0:
        ergebnis = zahl1 / zahl2
        print(f"Ergebnis: {ergebnis}")
    else:
        print("❌ Fehler: Division durch Null ist nicht möglich!")

else:
    # TODO: Ergänzen Sie eine Fehlermeldung für ungültige Operationen
    print("# ERGÄNZEN: Fehlermeldung für ungültige Operation")

# Zusätzliche Informationen anzeigen
print(f"\n📊 DETAILS:")
print(f"Erste Zahl:  {zahl1}")
print(f"Zweite Zahl: {zahl2}")
print(f"Operation:   {operation}")

# TODO: Ergänzen Sie eine Klassifizierung des Ergebnisses
if operation in ["+", "-", "*", "/"]:
    if 'ergebnis' in locals():  # Prüft ob ergebnis existiert
        if ergebnis > 0:
            print("Das Ergebnis ist positiv! ✅")
        elif ergebnis < 0:
            print("Das Ergebnis ist negativ! ⚠️")
        else:
            # TODO: Was soll bei Ergebnis = 0 ausgegeben werden?
            print("# ERGÄNZEN: Nachricht für Ergebnis = 0")

# Verabschiedung
print("\nVielen Dank für die Nutzung des Taschenrechners! 🧮")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
🧮 EINFACHER TASCHENRECHNER
==============================
Führen Sie einfache Berechnungen durch!

Geben Sie zwei Zahlen ein:
Erste Zahl: 12
Zweite Zahl: 4

Verfügbare Operationen:
+ für Addition
- für Subtraktion
* für Multiplikation
/ für Division
Operation (+, -, *, /): *

Berechnung: 12.0 * 4.0
Ergebnis: 48.0

📊 DETAILS:
Erste Zahl:  12.0
Zweite Zahl: 4.0
Operation:   *
Das Ergebnis ist positiv! ✅

Vielen Dank für die Nutzung des Taschenrechners! 🧮

WAS FEHLT NOCH:
===============
□ Multiplikation implementieren (zahl1 * zahl2)
□ Fehlermeldung für ungültige Operation
□ Nachricht für Ergebnis = 0

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Code-Grundgerüst
3. partial.py   - Teilweise implementiert (Sie sind hier!)
4. complete.py  - Vollständige Lösung
"""
