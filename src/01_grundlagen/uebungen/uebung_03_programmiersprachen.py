#!/usr/bin/env python3
"""
Übung 3: Liste von Programmiersprachen

Aufgabe:
1. Erstellen Sie eine Liste Ihrer Lieblings-Programmiersprachen
2. Fügen Sie "Python" hinzu, falls nicht vorhanden
3. Sortieren Sie die Liste alphabetisch
4. Geben Sie jede Sprache mit Nummer aus
5. BONUS: Kategorisieren Sie die Sprachen (Web, Desktop, Data Science, etc.)
6. BONUS: Implementieren Sie Such- und Filterfunktionen

TIPP: Verwenden Sie Listen-Methoden wie append(), sort(), in-Operator
"""


def erstelle_programmiersprachenliste() -> list[str]:
    """
    TODO: Erstellen Sie eine Liste mit Ihren Lieblings-Programmiersprachen

    Beispiele: Java, C#, JavaScript, Python, VBA, SQL, etc.

    Returns:
        Liste von Programmiersprachen als Strings
    """
    # Ihre Implementierung hier:
    pass


def fuege_python_hinzu(sprachen: list[str]) -> list[str]:
    """
    TODO: Fügen Sie "Python" zur Liste hinzu, falls nicht vorhanden

    TIPP: Verwenden Sie den 'in' Operator zur Überprüfung

    Args:
        sprachen: Bestehende Liste von Programmiersprachen

    Returns:
        Aktualisierte Liste mit Python (falls hinzugefügt)
    """
    # Ihre Implementierung hier:
    pass


def sortiere_alphabetisch(sprachen: list[str]) -> list[str]:
    """
    TODO: Sortieren Sie die Liste alphabetisch

    TIPP: Verwenden Sie sort() oder sorted()

    Args:
        sprachen: Unsortierte Liste

    Returns:
        Alphabetisch sortierte Liste
    """
    # Ihre Implementierung hier:
    pass


def zeige_nummerierte_liste(sprachen: list[str]) -> None:
    """
    TODO: Geben Sie jede Sprache mit Nummer aus

    Format: "1. Python", "2. Java", etc.

    Args:
        sprachen: Liste der Programmiersprachen
    """
    # Ihre Implementierung hier:
    pass


# BONUS-Funktionen


def kategorisiere_sprachen(sprachen: list[str]) -> dict[str, list[str]]:
    """
    BONUS: Kategorisieren Sie Programmiersprachen nach Anwendungsbereich

    Kategorien könnten sein:
    - Web Development: JavaScript, PHP, HTML/CSS
    - Desktop: Java, C#, C++
    - Data Science: Python, R, Julia
    - Database: SQL, MongoDB
    - Legacy: VBA, COBOL

    Args:
        sprachen: Liste der Programmiersprachen

    Returns:
        Dictionary mit Kategorien als Keys und Listen von Sprachen als Values
    """
    # Definieren Sie die Kategorien
    kategorien = {
        "Web Development": ["JavaScript", "TypeScript", "PHP", "HTML", "CSS"],
        "Desktop Applications": ["Java", "C#", "C++", "Swift", "Kotlin"],
        "Data Science": ["Python", "R", "Julia", "MATLAB"],
        "Databases": ["SQL", "MongoDB", "PostgreSQL"],
        "Systems Programming": ["C", "C++", "Rust", "Go"],
        "Legacy/Office": ["VBA", "COBOL", "Fortran"],
        "Mobile": ["Swift", "Kotlin", "Java", "Dart"],
        "Andere": [],
    }

    # TODO: Implementieren Sie die Kategorisierung
    # Durchlaufen Sie Ihre Sprachen und ordnen Sie sie den Kategorien zu
    # Sprachen, die in keiner Kategorie gefunden werden, kommen in "Andere"

    # Ihre Implementierung hier:
    pass


def suche_sprache(sprachen: list[str], suchbegriff: str) -> list[str]:
    """
    BONUS: Suchen Sie nach Sprachen, die den Suchbegriff enthalten

    Args:
        sprachen: Liste der Programmiersprachen
        suchbegriff: Suchbegriff (case-insensitive)

    Returns:
        Liste der gefundenen Sprachen
    """
    # TODO: Implementieren Sie die Suche
    # TIPP: Verwenden Sie List Comprehension und .lower() für case-insensitive Suche
    pass


def filtere_nach_laenge(
    sprachen: list[str], min_laenge: int = 0, max_laenge: int = 50
) -> list[str]:
    """
    BONUS: Filtern Sie Sprachen nach Namenlänge

    Args:
        sprachen: Liste der Programmiersprachen
        min_laenge: Minimale Länge des Namens
        max_laenge: Maximale Länge des Namens

    Returns:
        Gefilterte Liste
    """
    # TODO: Implementieren Sie den Filter
    pass


def interaktives_menu(sprachen: list[str]) -> None:
    """
    BONUS: Implementieren Sie ein interaktives Menü für verschiedene Operationen
    """
    while True:
        print("\n" + "=" * 50)
        print("🔧 PROGRAMMIERSPRACHEN VERWALTUNG")
        print("=" * 50)
        print("1. Alle Sprachen anzeigen")
        print("2. Sprache hinzufügen")
        print("3. Sprache entfernen")
        print("4. Kategorien anzeigen")
        print("5. Suche")
        print("6. Nach Länge filtern")
        print("0. Beenden")
        print("=" * 50)

        wahl = input("Ihre Wahl (0-6): ")

        # TODO: Implementieren Sie die Menülogik
        if wahl == "0":
            break
        # Weitere Optionen implementieren...

        print("🚧 Diese Funktion ist noch nicht implementiert!")


def main():
    """
    Hauptfunktion - orchestriert alle Operationen
    """
    print("=== Programmiersprachen Manager ===")
    print("Willkommen beim Bystronic Programmiersprachen-Tool! 💻")

    # TODO: Implementieren Sie die Hauptlogik:
    # 1. Liste erstellen
    # 2. Python hinzufügen
    # 3. Sortieren
    # 4. Anzeigen

    # Schritt 1: Liste erstellen
    # meine_sprachen = erstelle_programmiersprachenliste()

    # Weitere Schritte...

    print("\n🎉 Vielen Dank für die Nutzung des Programmiersprachen-Tools!")


# Lösungsvorschläge (auskommentiert):
"""
def erstelle_programmiersprachenliste() -> List[str]:
    # Beispiel-Liste - passen Sie sie an Ihre Erfahrungen an
    return ["Java", "C#", "JavaScript", "VBA", "SQL", "PowerShell"]

def fuege_python_hinzu(sprachen: List[str]) -> List[str]:
    if "Python" not in sprachen:
        sprachen.append("Python")
        print("✅ Python wurde zur Liste hinzugefügt!")
    else:
        print("ℹ️  Python ist bereits in der Liste vorhanden.")
    return sprachen

def sortiere_alphabetisch(sprachen: List[str]) -> List[str]:
    return sorted(sprachen)  # Oder sprachen.sort() für in-place sorting

def zeige_nummerierte_liste(sprachen: List[str]) -> None:
    print("\\n📋 Ihre Programmiersprachen:")
    print("-" * 30)
    for i, sprache in enumerate(sprachen, 1):
        print(f"{i:2d}. {sprache}")
    print("-" * 30)
    print(f"Gesamt: {len(sprachen)} Sprachen")

def kategorisiere_sprachen(sprachen: List[str]) -> Dict[str, List[str]]:
    kategorien = {
        "Web Development": ["JavaScript", "TypeScript", "PHP", "HTML", "CSS"],
        "Desktop Applications": ["Java", "C#", "C++", "Swift", "Kotlin"],
        "Data Science": ["Python", "R", "Julia", "MATLAB"],
        "Databases": ["SQL", "MongoDB", "PostgreSQL"],
        "Systems Programming": ["C", "C++", "Rust", "Go"],
        "Legacy/Office": ["VBA", "COBOL", "Fortran"],
        "Mobile": ["Swift", "Kotlin", "Java", "Dart"],
        "Andere": []
    }

    ergebnis = {k: [] for k in kategorien.keys()}

    for sprache in sprachen:
        gefunden = False
        for kategorie, sprachen_in_kategorie in kategorien.items():
            if sprache in sprachen_in_kategorie:
                ergebnis[kategorie].append(sprache)
                gefunden = True
                break
        if not gefunden:
            ergebnis["Andere"].append(sprache)

    # Leere Kategorien entfernen
    return {k: v for k, v in ergebnis.items() if v}

def suche_sprache(sprachen: List[str], suchbegriff: str) -> List[str]:
    return [s for s in sprachen if suchbegriff.lower() in s.lower()]

def filtere_nach_laenge(sprachen: List[str], min_laenge: int = 0, max_laenge: int = 50) -> List[str]:
    return [s for s in sprachen if min_laenge <= len(s) <= max_laenge]
"""

if __name__ == "__main__":
    main()
