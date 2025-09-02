#!/usr/bin/env python3
"""
Übung 1: Persönliche Informationen

Aufgabe:
1. Fragen Sie nach Name, Alter, Abteilung
2. Berechnen Sie das Geburtsjahr
3. Geben Sie eine schöne Zusammenfassung aus
4. BONUS: Bestimmen Sie den Erfahrungsgrad basierend auf dem Alter

TIPP: Verwenden Sie input() für Eingaben und int() für Zahlenkonvertierung
"""


def sammle_informationen():
    """
    TODO: Implementieren Sie die Informationssammlung

    Sammeln Sie:
    - Name (String)
    - Alter (Integer)
    - Abteilung (String)
    - Jahre Berufserfahrung (Integer) - BONUS

    Geben Sie ein Dictionary mit den Informationen zurück
    """
    # Ihre Implementierung hier:
    pass


def berechne_geburtsjahr(alter: int, aktuelles_jahr: int = 2025) -> int:
    """
    TODO: Berechnen Sie das Geburtsjahr basierend auf dem Alter

    Args:
        alter: Alter der Person
        aktuelles_jahr: Aktuelles Jahr (default: 2025)

    Returns:
        Geschätztes Geburtsjahr
    """
    # Ihre Implementierung hier:
    pass


def bestimme_erfahrungsgrad(alter: int, berufserfahrung: int = None) -> str:
    """
    TODO: Bestimmen Sie den Erfahrungsgrad

    Regeln:
    - Unter 25 Jahre: "Nachwuchstalent"
    - 25-35 Jahre: "Junior" (bei < 5 Jahren Erfahrung) oder "Senior"
    - Über 35 Jahre: "Senior" oder "Expert" (bei > 10 Jahren Erfahrung)

    Args:
        alter: Alter der Person
        berufserfahrung: Jahre der Berufserfahrung (optional)

    Returns:
        Erfahrungsgrad als String
    """
    # Ihre Implementierung hier:
    pass


def formatiere_ausgabe(infos: dict) -> None:
    """
    TODO: Erstellen Sie eine schöne formatierte Ausgabe

    Die Ausgabe soll enthalten:
    - Überschrift mit Name
    - Alter und Geburtsjahr
    - Abteilung
    - Erfahrungsgrad
    - Schöne Formatierung mit Linien/Boxen
    """
    # Ihre Implementierung hier:
    pass


def main():
    """
    Hauptfunktion - orchestriert die gesamte Anwendung
    """
    print("=== Persönliche Informationen - Bystronic Mitarbeiterprofil ===")
    print()

    # TODO: Rufen Sie die Funktionen in der richtigen Reihenfolge auf

    print("\nVielen Dank für Ihre Teilnahme! 🎉")


# Lösungsvorschlag (auskommentiert - versuchen Sie es zuerst selbst!)
"""
def sammle_informationen():
    infos = {}

    infos['name'] = input("Wie heissen Sie? ")
    infos['alter'] = int(input("Wie alt sind Sie? "))
    infos['abteilung'] = input("In welcher Abteilung arbeiten Sie? ")

    # BONUS: Berufserfahrung
    erfahrung_input = input("Wie viele Jahre Berufserfahrung haben Sie? (optional, Enter für überspringen): ")
    infos['berufserfahrung'] = int(erfahrung_input) if erfahrung_input.strip() else None

    return infos

def berechne_geburtsjahr(alter: int, aktuelles_jahr: int = 2025) -> int:
    return aktuelles_jahr - alter

def bestimme_erfahrungsgrad(alter: int, berufserfahrung: int = None) -> str:
    if alter < 25:
        return "Nachwuchstalent"
    elif alter <= 35:
        if berufserfahrung and berufserfahrung >= 5:
            return "Senior"
        return "Junior"
    else:
        if berufserfahrung and berufserfahrung > 10:
            return "Expert"
        return "Senior"

def formatiere_ausgabe(infos: dict) -> None:
    name = infos['name']
    alter = infos['alter']
    abteilung = infos['abteilung']

    geburtsjahr = berechne_geburtsjahr(alter)
    grad = bestimme_erfahrungsgrad(alter, infos.get('berufserfahrung'))

    # Schöne Formatierung
    print("\n" + "="*60)
    print(f"📋 Mitarbeiterprofil: {name}")
    print("="*60)
    print(f"👤 Alter:           {alter} Jahre (geboren ca. {geburtsjahr})")
    print(f"🏢 Abteilung:       {abteilung}")
    print(f"📊 Erfahrungsgrad:  {grad}")

    if infos.get('berufserfahrung'):
        print(f"💼 Berufserfahrung: {infos['berufserfahrung']} Jahre")

    print("="*60)
"""

if __name__ == "__main__":
    main()
