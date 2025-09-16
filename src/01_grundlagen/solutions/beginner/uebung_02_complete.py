#!/usr/bin/env python3
"""
🟢 COMPLETE: Übung 2 - Taschenrechner (Beginner)
================================================

MUSTERLÖSUNG:
Dies ist eine vollständige, professionelle Lösung der Übung.
Verwenden Sie diese nur, wenn Sie wirklich nicht weiterkommen!

LERNZIELE ERFÜLLT:
✅ if/elif/else für verschiedene Fälle
✅ float() für Zahlenkonvertierung
✅ Mathematische Operatoren (+, -, *, /)
✅ Fehlerbehandlung für Division durch Null
✅ Eingabevalidierung
"""

# Begrüssung ausgeben
print("🧮 EINFACHER TASCHENRECHNER")
print("=" * 30)
print("Führen Sie einfache Berechnungen durch!")
print("Unterstützte Operationen: +, -, *, /")

# Zahlen eingeben mit Fehlerbehandlung
print("\nGeben Sie zwei Zahlen ein:")

try:
    zahl1 = float(input("Erste Zahl: "))
    zahl2 = float(input("Zweite Zahl: "))

    # Operation wählen
    print("\nVerfügbare Operationen:")
    print("+ für Addition")
    print("- für Subtraktion")
    print("* für Multiplikation")
    print("/ für Division")

    operation = input("Operation (+, -, *, /): ").strip()

    # Berechnung durchführen
    print(f"\nBerechnung: {zahl1} {operation} {zahl2}")

    if operation == "+":
        ergebnis = zahl1 + zahl2
        operation_name = "Addition"

    elif operation == "-":
        ergebnis = zahl1 - zahl2
        operation_name = "Subtraktion"

    elif operation == "*":
        ergebnis = zahl1 * zahl2
        operation_name = "Multiplikation"

    elif operation == "/":
        if zahl2 != 0:
            ergebnis = zahl1 / zahl2
            operation_name = "Division"
        else:
            print("❌ Fehler: Division durch Null ist nicht möglich!")
            print("Tipp: Die zweite Zahl darf nicht 0 sein.")
            exit()

    else:
        print(f"❌ Fehler: '{operation}' ist keine gültige Operation!")
        print("Verwenden Sie nur: +, -, *, /")
        exit()

    # Ergebnis anzeigen
    print(f"Ergebnis: {ergebnis}")

    # Zusätzliche Informationen
    print("\n📊 BERECHNUNGSDETAILS:")
    print(f"Operation:     {operation_name}")
    print(f"Erste Zahl:    {zahl1}")
    print(f"Zweite Zahl:   {zahl2}")
    print(f"Ergebnis:      {ergebnis}")

    # Ergebnis klassifizieren
    if ergebnis > 0:
        print("Klassifikation: Das Ergebnis ist positiv! ✅")
    elif ergebnis < 0:
        print("Klassifikation: Das Ergebnis ist negativ! ⚠️")
    else:
        print("Klassifikation: Das Ergebnis ist Null! 🔄")

    # Ergebnis formatieren
    if ergebnis == int(ergebnis):
        print(f"Ganzzahl:      {int(ergebnis)}")
    else:
        print(f"Gerundet:      {ergebnis:.2f}")

    # Zusätzliche mathematische Informationen
    print("\n🔢 ZUSÄTZLICHE INFOS:")

    # Absolutwert
    print(f"Absolutwert:   {abs(ergebnis)}")

    # Ist das Ergebnis gerade oder ungerade? (nur bei ganzen Zahlen)
    if ergebnis == int(ergebnis):
        if int(ergebnis) % 2 == 0:
            print("Parität:       Gerade Zahl")
        else:
            print("Parität:       Ungerade Zahl")

    # Umkehrrechnung anzeigen
    if operation == "+":
        print(f"Umkehrrechnung: {ergebnis} - {zahl2} = {zahl1}")
    elif operation == "-":
        print(f"Umkehrrechnung: {ergebnis} + {zahl2} = {zahl1}")
    elif operation == "*":
        if zahl2 != 0:
            print(f"Umkehrrechnung: {ergebnis} / {zahl2} = {zahl1}")
    elif operation == "/":
        print(f"Umkehrrechnung: {ergebnis} * {zahl2} = {zahl1}")

    # Motivierende Nachricht
    print("\n🎉 ERFOLGREICH!")
    print("Sie haben erfolgreich eine Berechnung durchgeführt!")

    if abs(ergebnis) > 100:
        print("Wow! Das ist ein grosses Ergebnis! 🚀")
    elif abs(ergebnis) < 1 and ergebnis != 0:
        print("Das ist ein sehr kleines Ergebnis! 🔍")
    elif ergebnis == 0:
        print("Null ist ein besonderes Ergebnis! 🎯")

except ValueError:
    print("❌ Fehler: Bitte geben Sie gültige Zahlen ein!")
    print("Beispiele für gültige Zahlen: 5, 3.14, -2.5, 0")

except KeyboardInterrupt:
    print("\n\n⚠️ Programm abgebrochen.")

# Verabschiedung
print("\nVielen Dank für die Nutzung des Taschenrechners! 🧮")
print("Bis zum nächsten Mal! 👋")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
🧮 EINFACHER TASCHENRECHNER
==============================
Führen Sie einfache Berechnungen durch!
Unterstützte Operationen: +, -, *, /

Geben Sie zwei Zahlen ein:
Erste Zahl: 15
Zweite Zahl: 4

Verfügbare Operationen:
+ für Addition
- für Subtraktion
* für Multiplikation
/ für Division
Operation (+, -, *, /): /

Berechnung: 15.0 / 4.0
Ergebnis: 3.75

📊 BERECHNUNGSDETAILS:
Operation:     Division
Erste Zahl:    15.0
Zweite Zahl:   4.0
Ergebnis:      3.75
Klassifikation: Das Ergebnis ist positiv! ✅
Gerundet:      3.75

🔢 ZUSÄTZLICHE INFOS:
Absolutwert:   3.75
Umkehrrechnung: 3.75 * 4.0 = 15.0

🎉 ERFOLGREICH!
Sie haben erfolgreich eine Berechnung durchgeführt!

Vielen Dank für die Nutzung des Taschenrechners! 🧮
Bis zum nächsten Mal! 👋

VERWENDETE KONZEPTE:
====================
✅ if/elif/else - Bedingte Ausführung
✅ float() - Zahlenkonvertierung
✅ Mathematische Operatoren (+, -, *, /)
✅ Fehlerbehandlung (try/except)
✅ Division durch Null Prüfung
✅ String-Methoden (.strip())
✅ Eingabevalidierung
✅ Formatierte Ausgaben (f-strings)
✅ Mathematische Funktionen (abs(), int())
✅ Modulo-Operator (%)

TESTFÄLLE:
==========
✅ Addition: 5 + 3 = 8.0
✅ Subtraktion: 10 - 4 = 6.0
✅ Multiplikation: 7 * 2 = 14.0
✅ Division: 15 / 3 = 5.0
❌ Division durch Null: 5 / 0 → Fehlermeldung
❌ Ungültige Operation: 5 % 3 → Fehlermeldung
❌ Ungültige Zahl: "abc" → Fehlermeldung

NÄCHSTE SCHRITTE:
=================
🎯 Verstehen Sie alle Konzepte? Probieren Sie Übung 3!
🚀 Zu einfach? Versuchen Sie die Intermediate-Version!
💡 Eigene Ideen? Erweitern Sie den Taschenrechner!
"""
