#!/usr/bin/env python3
"""
🟡 INTERMEDIATE: Übung 2 - Wissenschaftlicher Taschenrechner
===========================================================

LERNZIELE:
- Modulare Funktionen entwickeln
- Umfassende Fehlerbehandlung mit try/except
- Benutzerfreundliche Menüführung
- Erweiterte mathematische Operationen
- Code-Organisation und Best Practices

AUFGABE:
Entwickeln Sie einen wissenschaftlichen Taschenrechner mit erweiterten
Funktionen, Verlaufspeicher und benutzerfreundlicher Oberfläche.

ZEIT: 25-40 Minuten
SCHWIERIGKEIT: 🟡 Fortgeschritten

ANFORDERUNGEN:
- Funktionale Programmierung
- Robuste Fehlerbehandlung
- Erweiterte mathematische Operationen
- Verlaufspeicher
- Benutzerfreundliche Menüs
"""

import math


class TaschenrechnerVerlauf:
    """Klasse zur Verwaltung des Berechnungsverlaufs."""

    def __init__(self):
        self.verlauf: list[str] = []

    def hinzufuegen(self, berechnung: str) -> None:
        """Fügt eine Berechnung zum Verlauf hinzu."""
        self.verlauf.append(berechnung)

    def anzeigen(self) -> None:
        """Zeigt den kompletten Verlauf an."""
        if not self.verlauf:
            print("📝 Verlauf ist leer.")
            return

        print("\n📜 BERECHNUNGSVERLAUF:")
        print("-" * 40)
        for i, berechnung in enumerate(self.verlauf, 1):
            print(f"{i:2d}. {berechnung}")
        print("-" * 40)

    def leeren(self) -> None:
        """Löscht den Verlauf."""
        self.verlauf.clear()
        print("🗑️ Verlauf wurde geleert.")


def sichere_zahleneingabe(prompt: str) -> float:
    """
    Sichere Eingabe einer Zahl mit Fehlerbehandlung.

    Args:
        prompt: Eingabeaufforderung

    Returns:
        Eingegebene Zahl als float
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")


def addition(a: float, b: float) -> float:
    """Addiert zwei Zahlen."""
    return a + b


def subtraktion(a: float, b: float) -> float:
    """Subtrahiert zwei Zahlen."""
    return a - b


def multiplikation(a: float, b: float) -> float:
    """Multipliziert zwei Zahlen."""
    return a * b


def division(a: float, b: float) -> float:
    """
    Dividiert zwei Zahlen mit Fehlerbehandlung.

    Raises:
        ZeroDivisionError: Bei Division durch Null
    """
    if b == 0:
        raise ZeroDivisionError("Division durch Null ist nicht erlaubt!")
    return a / b


def potenz(a: float, b: float) -> float:
    """Berechnet a hoch b."""
    return a**b


def wurzel(a: float) -> float:
    """
    Berechnet die Quadratwurzel.

    Raises:
        ValueError: Bei negativer Zahl
    """
    if a < 0:
        raise ValueError("Quadratwurzel aus negativer Zahl ist nicht möglich!")
    return math.sqrt(a)


def logarithmus(a: float, basis: float | None = None) -> float:
    """
    Berechnet den Logarithmus.

    Args:
        a: Zahl für Logarithmus
        basis: Basis (None für natürlichen Logarithmus)

    Raises:
        ValueError: Bei ungültigen Werten
    """
    if a <= 0:
        raise ValueError("Logarithmus ist nur für positive Zahlen definiert!")

    if basis is None:
        return math.log(a)  # Natürlicher Logarithmus

    if basis <= 0 or basis == 1:
        raise ValueError("Basis muss positiv und ungleich 1 sein!")

    return math.log(a, basis)


def sinus(a: float, grad: bool = True) -> float:
    """Berechnet den Sinus (Eingabe in Grad oder Radiant)."""
    if grad:
        a = math.radians(a)
    return math.sin(a)


def cosinus(a: float, grad: bool = True) -> float:
    """Berechnet den Cosinus (Eingabe in Grad oder Radiant)."""
    if grad:
        a = math.radians(a)
    return math.cos(a)


def tangens(a: float, grad: bool = True) -> float:
    """Berechnet den Tangens (Eingabe in Grad oder Radiant)."""
    if grad:
        a = math.radians(a)
    return math.tan(a)


def zeige_hauptmenu() -> None:
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 50)
    print("🧮 WISSENSCHAFTLICHER TASCHENRECHNER")
    print("=" * 50)
    print("GRUNDRECHENARTEN:")
    print("  1. Addition (+)")
    print("  2. Subtraktion (-)")
    print("  3. Multiplikation (×)")
    print("  4. Division (÷)")
    print()
    print("ERWEITERTE FUNKTIONEN:")
    print("  5. Potenz (^)")
    print("  6. Quadratwurzel (√)")
    print("  7. Logarithmus (log)")
    print()
    print("TRIGONOMETRIE:")
    print("  8. Sinus")
    print("  9. Cosinus")
    print(" 10. Tangens")
    print()
    print("VERLAUF:")
    print(" 11. Verlauf anzeigen")
    print(" 12. Verlauf löschen")
    print()
    print("  0. Beenden")
    print("=" * 50)


def waehle_operation() -> str:
    """Lässt den Benutzer eine Operation wählen."""
    while True:
        wahl = input("Ihre Wahl (0-12): ").strip()
        if wahl in [str(i) for i in range(13)]:
            return wahl
        print("❌ Ungültige Auswahl! Bitte wählen Sie 0-12.")


def fuehre_berechnung_aus(operation: str, verlauf: TaschenrechnerVerlauf) -> bool:
    """
    Führt die gewählte Berechnung aus.

    Args:
        operation: Gewählte Operation
        verlauf: Verlaufs-Objekt

    Returns:
        True wenn weiter gemacht werden soll, False zum Beenden
    """
    try:
        if operation == "0":
            return False

        elif operation == "11":
            verlauf.anzeigen()
            return True

        elif operation == "12":
            verlauf.leeren()
            return True

        # Operationen mit zwei Zahlen
        elif operation in ["1", "2", "3", "4", "5", "7"]:
            a = sichere_zahleneingabe("Erste Zahl: ")

            if operation == "7":  # Logarithmus
                basis_input = input(
                    "Basis (Enter für natürlichen Logarithmus): "
                ).strip()
                basis = float(basis_input) if basis_input else None
                resultat = logarithmus(a, basis)

                if basis is None:
                    berechnung = f"ln({a}) = {resultat:.6f}"
                else:
                    berechnung = f"log_{basis}({a}) = {resultat:.6f}"
            else:
                b = sichere_zahleneingabe("Zweite Zahl: ")

                if operation == "1":
                    resultat = addition(a, b)
                    berechnung = f"{a} + {b} = {resultat}"
                elif operation == "2":
                    resultat = subtraktion(a, b)
                    berechnung = f"{a} - {b} = {resultat}"
                elif operation == "3":
                    resultat = multiplikation(a, b)
                    berechnung = f"{a} × {b} = {resultat}"
                elif operation == "4":
                    resultat = division(a, b)
                    berechnung = f"{a} ÷ {b} = {resultat}"
                elif operation == "5":
                    resultat = potenz(a, b)
                    berechnung = f"{a}^{b} = {resultat}"

        # Operationen mit einer Zahl
        elif operation in ["6", "8", "9", "10"]:
            a = sichere_zahleneingabe("Zahl: ")

            if operation == "6":
                resultat = wurzel(a)
                berechnung = f"√{a} = {resultat}"
            else:
                # Trigonometrische Funktionen
                grad_input = (
                    input("Eingabe in Grad? (j/n, Standard: j): ").strip().lower()
                )
                grad = grad_input != "n"

                if operation == "8":
                    resultat = sinus(a, grad)
                    einheit = "°" if grad else " rad"
                    berechnung = f"sin({a}{einheit}) = {resultat:.6f}"
                elif operation == "9":
                    resultat = cosinus(a, grad)
                    einheit = "°" if grad else " rad"
                    berechnung = f"cos({a}{einheit}) = {resultat:.6f}"
                elif operation == "10":
                    resultat = tangens(a, grad)
                    einheit = "°" if grad else " rad"
                    berechnung = f"tan({a}{einheit}) = {resultat:.6f}"

        # Ergebnis anzeigen und zum Verlauf hinzufügen
        print(f"\n➡️  {berechnung}")
        verlauf.hinzufuegen(berechnung)

    except (ZeroDivisionError, ValueError) as e:
        print(f"❌ Mathematischer Fehler: {e}")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")

    return True


def main():
    """Hauptfunktion des Taschenrechners."""
    verlauf = TaschenrechnerVerlauf()

    print("Willkommen beim wissenschaftlichen Taschenrechner! 🧮")

    try:
        while True:
            zeige_hauptmenu()
            operation = waehle_operation()

            if not fuehre_berechnung_aus(operation, verlauf):
                break

            # Frage nach weiterer Berechnung
            weiter = input("\nWeitere Berechnung? (j/n): ").strip().lower()
            if weiter == "n":
                break

    except KeyboardInterrupt:
        print("\n\n⚠️ Programm abgebrochen.")

    print("\n🎉 Vielen Dank für die Nutzung des Taschenrechners!")
    print("Auf Wiedersehen! 👋")


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE:
==================
Willkommen beim wissenschaftlichen Taschenrechner! 🧮

==================================================
🧮 WISSENSCHAFTLICHER TASCHENRECHNER
==================================================
GRUNDRECHENARTEN:
  1. Addition (+)
  2. Subtraktion (-)
  3. Multiplikation (×)
  4. Division (÷)

ERWEITERTE FUNKTIONEN:
  5. Potenz (^)
  6. Quadratwurzel (√)
  7. Logarithmus (log)

TRIGONOMETRIE:
  8. Sinus
  9. Cosinus
 10. Tangens

VERLAUF:
 11. Verlauf anzeigen
 12. Verlauf löschen

  0. Beenden
==================================================
Ihre Wahl (0-12): 5
Erste Zahl: 2
Zweite Zahl: 8

➡️  2.0^8.0 = 256.0

Weitere Berechnung? (j/n): j

[... weitere Berechnungen ...]

LERNKONTROLLE:
==============
□ Kann ich modulare Funktionen schreiben?
□ Verstehe ich try/except Fehlerbehandlung?
□ Kann ich Klassen für Datenorganisation verwenden?
□ Beherrsche ich erweiterte mathematische Operationen?
□ Kann ich benutzerfreundliche Menüs erstellen?
"""
