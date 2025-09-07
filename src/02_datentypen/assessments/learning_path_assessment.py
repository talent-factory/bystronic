#!/usr/bin/env python3
"""
🎯 Bystronic Python Grundkurs - Kapitel 2: Datentypen
Learning Path Assessment - Adaptive Lernpfad-Bestimmung

Dieses Assessment bestimmt den optimalen Lernpfad basierend auf:
- Vorwissen zu Datentypen und Programmierung
- Erfahrung mit numerischen Berechnungen
- Verständnis von Datenstrukturen
- Mathematische Kenntnisse
- Qualitätskontrolle-Erfahrung

🟢 Beginner (0-40 Punkte): Grundlagen der Datentypen
🟡 Intermediate (41-70 Punkte): Erweiterte Datenverarbeitung
🔴 Advanced (71-100 Punkte): Professionelle OOP-Datenmodellierung
"""

import json
import os
from datetime import datetime


class LearningPathAssessment:
    """Assessment-System für Kapitel 2: Datentypen"""

    def __init__(self):
        self.fragen = self._lade_fragen()
        self.antworten = {}
        self.gewichtungen = {
            "datentyp_grundlagen": 0.25,
            "mathematik_kenntnisse": 0.20,
            "programmier_erfahrung": 0.20,
            "datenstrukturen": 0.20,
            "qualitaetskontrolle": 0.15,
        }

    def _lade_fragen(self) -> dict:
        """Lädt die Assessment-Fragen für Datentypen"""
        return {
            "datentyp_grundlagen": [
                {
                    "frage": "Wie gut kennen Sie die Unterschiede zwischen verschiedenen Zahlentypen (int, float, complex)?",
                    "optionen": [
                        ("Kenne ich gar nicht", 0),
                        ("Habe davon gehört", 5),
                        ("Grundlegendes Verständnis", 10),
                        ("Kann sie unterscheiden und verwenden", 15),
                        ("Kenne alle Details und Anwendungsfälle", 20),
                    ],
                },
                {
                    "frage": "Wie vertraut sind Sie mit String-Operationen und Formatierung?",
                    "optionen": [
                        ("Noch nie verwendet", 0),
                        ("Einfache Ausgaben mit print()", 3),
                        ("String-Verkettung und grundlegende Methoden", 8),
                        ("f-strings und erweiterte Formatierung", 12),
                        ("Regex und komplexe String-Verarbeitung", 15),
                    ],
                },
            ],
            "mathematik_kenntnisse": [
                {
                    "frage": "Wie sicher sind Sie bei mathematischen Berechnungen in der Programmierung?",
                    "optionen": [
                        ("Nur Grundrechenarten", 0),
                        ("Einfache Formeln", 5),
                        ("Statistische Berechnungen", 10),
                        ("Komplexe mathematische Funktionen", 15),
                        ("Numerische Algorithmen und Optimierung", 20),
                    ],
                },
                {
                    "frage": "Haben Sie Erfahrung mit statistischen Auswertungen?",
                    "optionen": [
                        ("Nein, noch nie", 0),
                        ("Mittelwert und einfache Kennzahlen", 4),
                        ("Standardabweichung und Varianz", 8),
                        ("Verteilungen und Hypothesentests", 12),
                        ("Erweiterte statistische Modelle", 15),
                    ],
                },
            ],
            "programmier_erfahrung": [
                {
                    "frage": "Wie viel Programmiererfahrung haben Sie insgesamt?",
                    "optionen": [
                        ("Kompletter Anfänger", 0),
                        ("Wenige Monate Erfahrung", 5),
                        ("1-2 Jahre Erfahrung", 10),
                        ("3-5 Jahre Erfahrung", 15),
                        ("Mehr als 5 Jahre Erfahrung", 20),
                    ],
                },
                {
                    "frage": "Wie vertraut sind Sie mit Fehlerbehandlung und Debugging?",
                    "optionen": [
                        ("Kenne ich nicht", 0),
                        ("Kann einfache Fehler finden", 3),
                        ("Verwende try/except gelegentlich", 8),
                        ("Systematisches Debugging", 12),
                        ("Professionelle Fehlerbehandlung und Logging", 15),
                    ],
                },
            ],
            "datenstrukturen": [
                {
                    "frage": "Wie gut kennen Sie Listen, Dictionaries und andere Datenstrukturen?",
                    "optionen": [
                        ("Noch nie verwendet", 0),
                        ("Einfache Listen erstellen", 4),
                        ("Listen und Dictionaries verwenden", 10),
                        ("Verschachtelte Strukturen und Sets", 15),
                        ("Komplexe Datenmodellierung", 20),
                    ],
                },
                {
                    "frage": "Haben Sie Erfahrung mit Datenkonvertierung zwischen Typen?",
                    "optionen": [
                        ("Nein", 0),
                        ("int() und str() verwendet", 3),
                        ("Verschiedene Konvertierungen", 8),
                        ("Validierung und Fehlerbehandlung", 12),
                        ("Robuste Parsing-Systeme", 15),
                    ],
                },
            ],
            "qualitaetskontrolle": [
                {
                    "frage": "Haben Sie Erfahrung mit Qualitätskontrolle und Messdatenauswertung?",
                    "optionen": [
                        ("Nein, noch nie", 0),
                        ("Grundlegende Toleranzprüfungen", 5),
                        ("Statistische Qualitätskontrolle", 10),
                        ("SPC und Prozessfähigkeitsindizes", 15),
                        ("Erweiterte QM-Systeme", 20),
                    ],
                },
                {
                    "frage": "Wie vertraut sind Sie mit Bystronic-Produktionsdaten?",
                    "optionen": [
                        ("Noch nie damit gearbeitet", 0),
                        ("Grundlegende Kenntnisse", 3),
                        ("Regelmässige Arbeit mit Produktionsdaten", 8),
                        ("Datenanalyse und Reporting", 12),
                        ("Automatisierte Datenverarbeitung", 15),
                    ],
                },
            ],
        }

    def starte_assessment(self) -> dict:
        """Startet das interaktive Assessment"""
        print("🎯 LEARNING PATH ASSESSMENT - KAPITEL 2: DATENTYPEN")
        print("=" * 60)
        print("📊 Dieses Assessment bestimmt Ihren optimalen Lernpfad")
        print("⏱️  Dauer: ca. 5-7 Minuten")
        print("🎯 Ehrliche Antworten führen zum besten Lernergebnis!")
        print()

        gesamtpunkte = 0
        kategorie_punkte = {}

        for kategorie, fragen in self.fragen.items():
            print(f"\n📋 KATEGORIE: {kategorie.replace('_', ' ').title()}")
            print("-" * 40)

            kategorie_score = 0
            for i, frage_data in enumerate(fragen, 1):
                print(f"\n❓ Frage {i}: {frage_data['frage']}")
                print()

                for j, (option, punkte) in enumerate(frage_data["optionen"], 1):
                    print(f"  {j}. {option}")

                while True:
                    try:
                        antwort = input(
                            f"\nIhre Antwort (1-{len(frage_data['optionen'])}): "
                        ).strip()
                        antwort_idx = int(antwort) - 1

                        if 0 <= antwort_idx < len(frage_data["optionen"]):
                            punkte = frage_data["optionen"][antwort_idx][1]
                            kategorie_score += punkte
                            print(f"✅ Antwort gespeichert ({punkte} Punkte)")
                            break
                        else:
                            print(
                                "❌ Ungültige Eingabe. Bitte wählen Sie eine gültige Option."
                            )
                    except ValueError:
                        print("❌ Bitte geben Sie eine Zahl ein.")

            kategorie_punkte[kategorie] = kategorie_score
            gewichtete_punkte = kategorie_score * self.gewichtungen[kategorie]
            gesamtpunkte += gewichtete_punkte

            print(
                f"\n📊 Kategorie-Score: {kategorie_score} Punkte (gewichtet: {gewichtete_punkte:.1f})"
            )

        # Lernpfad bestimmen
        lernpfad = self._bestimme_lernpfad(gesamtpunkte)

        # Ergebnis anzeigen
        self._zeige_ergebnis(gesamtpunkte, kategorie_punkte, lernpfad)

        # Ergebnis speichern
        ergebnis = self._speichere_ergebnis(gesamtpunkte, kategorie_punkte, lernpfad)

        return ergebnis

    def _bestimme_lernpfad(self, punkte: float) -> dict:
        """Bestimmt den Lernpfad basierend auf den Punkten"""
        if punkte <= 40:
            return {
                "level": "beginner",
                "symbol": "🟢",
                "name": "Beginner",
                "beschreibung": "Grundlagen der Datentypen",
                "dauer": "15-25 Minuten pro Übung",
                "fokus": [
                    "Zahlentypen verstehen (int, float, bool)",
                    "Einfache String-Operationen",
                    "Grundlegende Listen und Dictionaries",
                    "Erste Schritte mit Datenkonvertierung",
                    "Praktische Anwendungen in der Produktion",
                ],
            }
        elif punkte <= 70:
            return {
                "level": "intermediate",
                "symbol": "🟡",
                "name": "Intermediate",
                "beschreibung": "Erweiterte Datenverarbeitung",
                "dauer": "25-40 Minuten pro Übung",
                "fokus": [
                    "Alle Zahlentypen inklusive complex",
                    "Erweiterte String-Formatierung und Regex",
                    "Komplexe Datenstrukturen und Verschachtelung",
                    "Statistische Berechnungen",
                    "Robuste Fehlerbehandlung",
                    "Qualitätskontrolle-Algorithmen",
                ],
            }
        else:
            return {
                "level": "advanced",
                "symbol": "🔴",
                "name": "Advanced",
                "beschreibung": "Professionelle OOP-Datenmodellierung",
                "dauer": "45-60 Minuten pro Übung",
                "fokus": [
                    "Objektorientierte Datenmodellierung",
                    "Design Patterns für numerische Berechnungen",
                    "Performance-Optimierung und Caching",
                    "Enterprise-Level Fehlerbehandlung",
                    "Erweiterte statistische Analysen",
                    "Automatisierte Qualitätssysteme",
                    "Professionelle Dokumentation und Testing",
                ],
            }

    def _zeige_ergebnis(
        self, gesamtpunkte: float, kategorie_punkte: dict, lernpfad: dict
    ):
        """Zeigt das Assessment-Ergebnis an"""
        print("\n" + "🎉" * 20)
        print("🎉 ASSESSMENT ABGESCHLOSSEN! 🎉")
        print("🎉" * 20)

        print("\n📊 IHRE ERGEBNISSE:")
        print("-" * 30)
        print(f"Gesamtpunkte: {gesamtpunkte:.1f}/100")
        print(f"Empfohlener Lernpfad: {lernpfad['symbol']} {lernpfad['name']}")
        print(f"Beschreibung: {lernpfad['beschreibung']}")
        print(f"Geschätzte Dauer: {lernpfad['dauer']}")

        print("\n📋 KATEGORIE-BREAKDOWN:")
        print("-" * 30)
        for kategorie, punkte in kategorie_punkte.items():
            max_punkte = sum(
                max(f["optionen"], key=lambda x: x[1])[1]
                for f in self.fragen[kategorie]
            )
            prozent = (punkte / max_punkte) * 100
            print(
                f"{kategorie.replace('_', ' ').title()}: {punkte}/{max_punkte} ({prozent:.0f}%)"
            )

        print("\n🎯 IHR LERNFOKUS:")
        print("-" * 30)
        for punkt in lernpfad["fokus"]:
            print(f"• {punkt}")

        print("\n📚 EMPFOHLENE ÜBUNGEN:")
        print("-" * 30)
        if lernpfad["level"] == "beginner":
            print("• exercises/beginner/uebung_01_zahlen_beginner.py")
            print("• exercises/beginner/uebung_02_strings_beginner.py")
            print("• exercises/beginner/uebung_03_collections_beginner.py")
        elif lernpfad["level"] == "intermediate":
            print("• exercises/intermediate/uebung_01_zahlen_intermediate.py")
            print("• exercises/intermediate/uebung_02_strings_intermediate.py")
            print("• exercises/intermediate/uebung_03_collections_intermediate.py")
        else:
            print("• exercises/advanced/uebung_01_zahlen_advanced.py")
            print("• exercises/advanced/uebung_02_strings_advanced.py")
            print("• exercises/advanced/uebung_03_collections_advanced.py")

    def _speichere_ergebnis(
        self, gesamtpunkte: float, kategorie_punkte: dict, lernpfad: dict
    ) -> dict:
        """Speichert das Assessment-Ergebnis"""
        ergebnis = {
            "timestamp": datetime.now().isoformat(),
            "kapitel": "Kapitel 2: Datentypen",
            "gesamtpunkte": gesamtpunkte,
            "kategorie_punkte": kategorie_punkte,
            "lernpfad": lernpfad,
            "gewichtungen": self.gewichtungen,
        }

        # Ergebnis-Verzeichnis erstellen
        os.makedirs("src/02_datentypen/assessments/results", exist_ok=True)

        # Dateiname mit Zeitstempel
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        dateiname = (
            f"src/02_datentypen/assessments/results/assessment_result_{timestamp}.json"
        )

        # Speichern
        with open(dateiname, "w", encoding="utf-8") as f:
            json.dump(ergebnis, f, indent=2, ensure_ascii=False)

        print(f"\n💾 Ergebnis gespeichert: {dateiname}")

        return ergebnis


def main():
    """Hauptfunktion für das Assessment"""
    assessment = LearningPathAssessment()
    ergebnis = assessment.starte_assessment()

    print(
        f"\n🚀 Starten Sie jetzt mit Ihrem {ergebnis['lernpfad']['symbol']} {ergebnis['lernpfad']['name']}-Lernpfad!"
    )


if __name__ == "__main__":
    main()
