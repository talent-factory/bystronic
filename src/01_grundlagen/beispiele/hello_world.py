#!/usr/bin/env python3
"""
hello_world.py - Erstes Python-Programm für Bystronic-Entwickler

Dieses Programm demonstriert die Grundlagen von Python-Syntax
und zeigt einfache Ausgaben und Variablen-Verwendung.
"""


def main() -> None:
    """Hauptfunktion mit grundlegenden Python-Beispielen"""

    # Einfache Ausgabe
    print("=" * 50)
    print("Willkommen bei Python!")
    print("=" * 50)

    # Variablen definieren
    name = "Bystronic Entwickler"
    jahr = 2025
    sprache = "Python"

    # String-Formatierung mit f-strings
    print(f"Hallo {name}!")
    print(f"Das Jahr {jahr} wird grossartig für {sprache}!")

    # Verschiedene Arten der String-Formatierung
    print("\nVerschiedene Formatierungsarten:")
    print("1. Alte Art: Hallo %s, willkommen bei %s!" % (name, sprache))
    print("2. .format(): Hallo {}, willkommen bei {}!".format(name, sprache))
    print("3. f-strings: Hallo {}, willkommen bei {}!".format(name, sprache))

    # Berechnungen
    stunden_pro_tag = 8
    tage_pro_woche = 5
    wochen_im_jahr = 52

    stunden_pro_jahr = stunden_pro_tag * tage_pro_woche * wochen_im_jahr
    print(f"\nEin Vollzeit-Entwickler arbeitet ca. {stunden_pro_jahr} Stunden pro Jahr")

    # Interaktive Eingabe
    print("\n" + "-" * 30)
    benutzer_name = input("Wie ist dein Name? ")
    print(f"Hallo {benutzer_name}! Schön, dich kennenzulernen.")


if __name__ == "__main__":
    main()
