#!/usr/bin/env python3
"""
🟡 INTERMEDIATE: Übung 3 - Skill-Management-System
==================================================

LERNZIELE:
- Dictionaries für strukturierte Daten
- List Comprehensions
- Erweiterte Datenmanipulation
- Such- und Filterfunktionen
- JSON-Export für Datenpersistierung
- Modulare Funktionen

AUFGABE:
Entwickeln Sie ein Skill-Management-System, das Programmiersprachen
mit Kategorien, Erfahrungslevels und Bewertungen verwaltet.

ZEIT: 25-40 Minuten
SCHWIERIGKEIT: 🟡 Fortgeschritten

ANFORDERUNGEN:
- Dictionary-basierte Datenstrukturen
- Such- und Filterfunktionen
- Datenexport und -import
- Statistische Auswertungen
"""

import json
from datetime import datetime


def erstelle_skill_datenbank() -> dict[str, dict]:
    """
    Erstellt eine umfassende Skill-Datenbank mit Kategorien und Bewertungen.

    Returns:
        Dictionary mit Programmiersprachen und deren Eigenschaften
    """
    skills = {
        "Python": {
            "kategorie": "Data Science",
            "erfahrung_jahre": 2,
            "skill_level": 7,  # 1-10 Skala
            "letzte_nutzung": "2024-12-01",
            "projekte": ["Datenanalyse", "Automatisierung", "Web Scraping"],
            "zertifizierungen": ["Python Institute PCAP"],
        },
        "Java": {
            "kategorie": "Enterprise",
            "erfahrung_jahre": 5,
            "skill_level": 8,
            "letzte_nutzung": "2024-11-15",
            "projekte": ["ERP-System", "Microservices", "Android App"],
            "zertifizierungen": ["Oracle Certified Java Programmer"],
        },
        "JavaScript": {
            "kategorie": "Web Development",
            "erfahrung_jahre": 3,
            "skill_level": 6,
            "letzte_nutzung": "2024-12-03",
            "projekte": ["React Dashboard", "Node.js API", "Frontend"],
            "zertifizierungen": [],
        },
        "C#": {
            "kategorie": "Desktop",
            "erfahrung_jahre": 4,
            "skill_level": 7,
            "letzte_nutzung": "2024-10-20",
            "projekte": ["WPF Anwendung", ".NET Core API"],
            "zertifizierungen": ["Microsoft Certified Developer"],
        },
        "SQL": {
            "kategorie": "Database",
            "erfahrung_jahre": 6,
            "skill_level": 9,
            "letzte_nutzung": "2024-12-04",
            "projekte": ["Data Warehouse", "Reporting", "Performance Tuning"],
            "zertifizierungen": ["Microsoft SQL Server Specialist"],
        },
        "VBA": {
            "kategorie": "Office Automation",
            "erfahrung_jahre": 8,
            "skill_level": 9,
            "letzte_nutzung": "2024-11-28",
            "projekte": ["Excel Automatisierung", "Access Datenbank"],
            "zertifizierungen": [],
        },
    }

    return skills


def zeige_skill_uebersicht(skills: dict[str, dict]) -> None:
    """Zeigt eine übersichtliche Darstellung aller Skills."""
    print("\n" + "=" * 80)
    print("📊 SKILL-MANAGEMENT-SYSTEM - ÜBERSICHT")
    print("=" * 80)

    # Header
    print(
        f"{'Sprache':<15} {'Kategorie':<18} {'Level':<6} {'Jahre':<6} {'Projekte':<10} {'Zert.':<5}"
    )
    print("-" * 80)

    # Sortiere nach Skill-Level (absteigend)
    sortierte_skills = sorted(
        skills.items(), key=lambda x: x[1]["skill_level"], reverse=True
    )

    for sprache, daten in sortierte_skills:
        kategorie = daten["kategorie"]
        level = daten["skill_level"]
        jahre = daten["erfahrung_jahre"]
        projekte_anzahl = len(daten["projekte"])
        zert_anzahl = len(daten["zertifizierungen"])

        # Level-Balken erstellen
        level_bar = "█" * level + "░" * (10 - level)

        print(
            f"{sprache:<15} {kategorie:<18} {level_bar} {level:<2}/10 {jahre:<6} {projekte_anzahl:<10} {zert_anzahl:<5}"
        )

    print("-" * 80)


def analysiere_skills(skills: dict[str, dict]) -> dict[str, any]:
    """
    Führt statistische Analysen der Skills durch.

    Returns:
        Dictionary mit Analyseergebnissen
    """
    if not skills:
        return {}

    # Grundstatistiken
    skill_levels = [daten["skill_level"] for daten in skills.values()]
    erfahrung_jahre = [daten["erfahrung_jahre"] for daten in skills.values()]

    # Kategorien analysieren
    kategorien = {}
    for daten in skills.values():
        kategorie = daten["kategorie"]
        kategorien[kategorie] = kategorien.get(kategorie, 0) + 1

    # Top Skills ermitteln
    top_skills = sorted(
        skills.items(), key=lambda x: x[1]["skill_level"], reverse=True
    )[:3]

    # Zertifizierungen zählen
    gesamt_zertifizierungen = sum(
        len(daten["zertifizierungen"]) for daten in skills.values()
    )

    analyse = {
        "gesamt_skills": len(skills),
        "durchschnitt_level": sum(skill_levels) / len(skill_levels),
        "durchschnitt_erfahrung": sum(erfahrung_jahre) / len(erfahrung_jahre),
        "hoechstes_level": max(skill_levels),
        "niedrigstes_level": min(skill_levels),
        "kategorien_verteilung": kategorien,
        "top_3_skills": [(name, daten["skill_level"]) for name, daten in top_skills],
        "gesamt_zertifizierungen": gesamt_zertifizierungen,
        "skills_mit_zertifizierung": len(
            [s for s in skills.values() if s["zertifizierungen"]]
        ),
    }

    return analyse


def zeige_analyse(analyse: dict[str, any]) -> None:
    """Zeigt die Skill-Analyse an."""
    print("\n" + "=" * 60)
    print("📈 SKILL-ANALYSE")
    print("=" * 60)

    print(f"📊 Gesamt Skills:              {analyse['gesamt_skills']}")
    print(f"⭐ Durchschnittliches Level:   {analyse['durchschnitt_level']:.1f}/10")
    print(
        f"📅 Durchschnittliche Erfahrung: {analyse['durchschnitt_erfahrung']:.1f} Jahre"
    )
    print(f"🏆 Höchstes Level:             {analyse['hoechstes_level']}/10")
    print(f"📜 Zertifizierungen:           {analyse['gesamt_zertifizierungen']} total")
    print(f"✅ Skills mit Zertifizierung:  {analyse['skills_mit_zertifizierung']}")

    print("\n🏅 TOP 3 SKILLS:")
    for i, (name, level) in enumerate(analyse["top_3_skills"], 1):
        print(f"  {i}. {name} (Level {level}/10)")

    print("\n📂 KATEGORIEN-VERTEILUNG:")
    for kategorie, anzahl in sorted(analyse["kategorien_verteilung"].items()):
        print(f"  {kategorie:<20} {anzahl} Skills")


def suche_skills(skills: dict[str, dict], suchbegriff: str) -> dict[str, dict]:
    """
    Sucht Skills basierend auf verschiedenen Kriterien.

    Args:
        skills: Skill-Datenbank
        suchbegriff: Suchbegriff (case-insensitive)

    Returns:
        Gefilterte Skills
    """
    suchbegriff = suchbegriff.lower()
    gefundene_skills = {}

    for name, daten in skills.items():
        # Suche in Name, Kategorie und Projekten
        if (
            suchbegriff in name.lower()
            or suchbegriff in daten["kategorie"].lower()
            or any(suchbegriff in projekt.lower() for projekt in daten["projekte"])
        ):
            gefundene_skills[name] = daten

    return gefundene_skills


def filtere_nach_level(
    skills: dict[str, dict], min_level: int, max_level: int = 10
) -> dict[str, dict]:
    """Filtert Skills nach Skill-Level."""
    return {
        name: daten
        for name, daten in skills.items()
        if min_level <= daten["skill_level"] <= max_level
    }


def filtere_nach_kategorie(skills: dict[str, dict], kategorie: str) -> dict[str, dict]:
    """Filtert Skills nach Kategorie."""
    return {
        name: daten
        for name, daten in skills.items()
        if daten["kategorie"].lower() == kategorie.lower()
    }


def empfehle_weiterbildung(skills: dict[str, dict]) -> list[tuple[str, str]]:
    """
    Empfiehlt Weiterbildungsmöglichkeiten basierend auf Skills.

    Returns:
        Liste von (Skill, Empfehlung) Tupeln
    """
    empfehlungen = []

    for name, daten in skills.items():
        level = daten["skill_level"]
        kategorie = daten["kategorie"]
        zertifizierungen = len(daten["zertifizierungen"])

        if level < 5:
            empfehlungen.append((name, "Grundlagen vertiefen - Online-Kurs empfohlen"))
        elif level < 8 and zertifizierungen == 0:
            empfehlungen.append((name, "Zertifizierung anstreben"))
        elif level >= 8:
            empfehlungen.append((name, "Mentoring oder Advanced-Projekte"))

    return empfehlungen


def exportiere_skills(
    skills: dict[str, dict], dateiname: str = "skills_export.json"
) -> None:
    """Exportiert Skills als JSON-Datei."""
    try:
        export_daten = {
            "export_datum": datetime.now().isoformat(),
            "skills": skills,
            "analyse": analysiere_skills(skills),
        }

        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump(export_daten, f, indent=2, ensure_ascii=False)

        print(f"✅ Skills erfolgreich exportiert nach: {dateiname}")

    except Exception as e:
        print(f"❌ Fehler beim Export: {e}")


def interaktives_menu(skills: dict[str, dict]) -> None:
    """Interaktives Menü für das Skill-Management."""
    while True:
        print("\n" + "=" * 50)
        print("🛠️  SKILL-MANAGEMENT-SYSTEM")
        print("=" * 50)
        print("1. Alle Skills anzeigen")
        print("2. Skill-Analyse anzeigen")
        print("3. Skills suchen")
        print("4. Nach Level filtern")
        print("5. Nach Kategorie filtern")
        print("6. Weiterbildungsempfehlungen")
        print("7. Skills exportieren")
        print("0. Beenden")
        print("=" * 50)

        wahl = input("Ihre Wahl (0-7): ").strip()

        if wahl == "0":
            break
        elif wahl == "1":
            zeige_skill_uebersicht(skills)
        elif wahl == "2":
            analyse = analysiere_skills(skills)
            zeige_analyse(analyse)
        elif wahl == "3":
            suchbegriff = input("Suchbegriff: ").strip()
            gefunden = suche_skills(skills, suchbegriff)
            if gefunden:
                print(f"\n🔍 {len(gefunden)} Skills gefunden:")
                zeige_skill_uebersicht(gefunden)
            else:
                print("❌ Keine Skills gefunden.")
        elif wahl == "4":
            try:
                min_level = int(input("Minimales Level (1-10): "))
                max_level = int(input("Maximales Level (1-10): "))
                gefiltert = filtere_nach_level(skills, min_level, max_level)
                if gefiltert:
                    zeige_skill_uebersicht(gefiltert)
                else:
                    print("❌ Keine Skills in diesem Level-Bereich.")
            except ValueError:
                print("❌ Ungültige Eingabe!")
        elif wahl == "5":
            kategorien = set(daten["kategorie"] for daten in skills.values())
            print(f"Verfügbare Kategorien: {', '.join(sorted(kategorien))}")
            kategorie = input("Kategorie: ").strip()
            gefiltert = filtere_nach_kategorie(skills, kategorie)
            if gefiltert:
                zeige_skill_uebersicht(gefiltert)
            else:
                print("❌ Keine Skills in dieser Kategorie.")
        elif wahl == "6":
            empfehlungen = empfehle_weiterbildung(skills)
            print("\n💡 WEITERBILDUNGSEMPFEHLUNGEN:")
            print("-" * 40)
            for skill, empfehlung in empfehlungen:
                print(f"📚 {skill}: {empfehlung}")
        elif wahl == "7":
            dateiname = input("Dateiname (Enter für Standard): ").strip()
            if not dateiname:
                dateiname = "skills_export.json"
            exportiere_skills(skills, dateiname)
        else:
            print("❌ Ungültige Auswahl!")


def main():
    """Hauptfunktion des Skill-Management-Systems."""
    print("🏢 BYSTRONIC SKILL-MANAGEMENT-SYSTEM")
    print("=" * 45)
    print("Verwalten Sie Ihre Programmiersprachen-Skills professionell!")

    # Skill-Datenbank erstellen
    skills = erstelle_skill_datenbank()

    # Kurze Übersicht zeigen
    zeige_skill_uebersicht(skills)

    # Interaktives Menü starten
    interaktives_menu(skills)

    print("\n🎉 Vielen Dank für die Nutzung des Skill-Management-Systems!")


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE:
==================
🏢 BYSTRONIC SKILL-MANAGEMENT-SYSTEM
=============================================
Verwalten Sie Ihre Programmiersprachen-Skills professionell!

================================================================================
📊 SKILL-MANAGEMENT-SYSTEM - ÜBERSICHT
================================================================================
Sprache         Kategorie          Level  Jahre  Projekte   Zert.
--------------------------------------------------------------------------------
SQL             Database           ██████████ 9/10 6      3          1
VBA             Office Automation  ██████████ 9/10 8      2          0
Java            Enterprise         ████████░░ 8/10 5      3          1
Python          Data Science       ███████░░░ 7/10 2      3          1
C#              Desktop            ███████░░░ 7/10 4      2          1
JavaScript      Web Development    ██████░░░░ 6/10 3      3          0
--------------------------------------------------------------------------------

==================================================
🛠️  SKILL-MANAGEMENT-SYSTEM
==================================================
1. Alle Skills anzeigen
2. Skill-Analyse anzeigen
3. Skills suchen
4. Nach Level filtern
5. Nach Kategorie filtern
6. Weiterbildungsempfehlungen
7. Skills exportieren
0. Beenden
==================================================
Ihre Wahl (0-7): 2

============================================================
📈 SKILL-ANALYSE
============================================================
📊 Gesamt Skills:              6
⭐ Durchschnittliches Level:   7.7/10
📅 Durchschnittliche Erfahrung: 4.7 Jahre
🏆 Höchstes Level:             9/10
📜 Zertifizierungen:           4 total
✅ Skills mit Zertifizierung:  4

🏅 TOP 3 SKILLS:
  1. SQL (Level 9/10)
  2. VBA (Level 9/10)
  3. Java (Level 8/10)

📂 KATEGORIEN-VERTEILUNG:
  Data Science         1 Skills
  Database             1 Skills
  Desktop              1 Skills
  Enterprise           1 Skills
  Office Automation    1 Skills
  Web Development      1 Skills

LERNKONTROLLE:
==============
□ Verstehe ich Dictionary-Datenstrukturen?
□ Kann ich komplexe Datenmanipulationen durchführen?
□ Beherrsche ich Such- und Filterfunktionen?
□ Kann ich JSON-Export implementieren?
□ Verstehe ich statistische Auswertungen?
"""
