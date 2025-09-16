#!/usr/bin/env python3
"""
🎯 MICRO-ASSESSMENT: Interaktives Wissensquiz für Kapitel 01
===========================================================

ZWECK:
Kontinuierliche Lernkontrolle durch interaktive Quizfragen zu allen
wichtigen Konzepten von Kapitel 01 (Python Grundlagen).

FEATURES:
- Multiple-Choice und Code-Fragen
- Sofortiges Feedback mit Erklärungen
- Adaptive Schwierigkeit
- Detaillierte Auswertung
- Empfehlungen für Vertiefung

ZEIT: 10-15 Minuten
"""

import json
import random
from datetime import datetime
from typing import Any


class MicroAssessmentQuiz:
    """Interaktives Quiz-System für Kapitel 01 Grundlagen."""

    def __init__(self):
        self.fragen = self._lade_fragen()
        self.antworten = []
        self.punkte = 0
        self.max_punkte = 0
        self.start_zeit = None

    def _lade_fragen(self) -> list[dict[str, Any]]:
        """Lädt alle Quizfragen für Kapitel 01."""
        return [
            # GRUNDLAGEN: Variablen und Datentypen
            {
                "id": "var_01",
                "kategorie": "Variablen",
                "schwierigkeit": "leicht",
                "frage": "Welcher Code erstellt eine Variable mit dem Namen 'alter' und dem Wert 25?",
                "typ": "multiple_choice",
                "optionen": [
                    "alter = 25",
                    "25 = alter",
                    "var alter = 25",
                    "int alter = 25",
                ],
                "korrekt": 0,
                "erklaerung": "In Python wird eine Variable mit 'name = wert' erstellt. Keine Typdeklaration nötig!",
                "punkte": 1,
            },
            {
                "id": "var_02",
                "kategorie": "Datentypen",
                "schwierigkeit": "leicht",
                "frage": "Was ist der Datentyp von: name = 'Max'",
                "typ": "multiple_choice",
                "optionen": ["int", "str", "float", "bool"],
                "korrekt": 1,
                "erklaerung": "Text in Anführungszeichen ist immer vom Typ 'str' (String).",
                "punkte": 1,
            },
            {
                "id": "input_01",
                "kategorie": "Ein-/Ausgabe",
                "schwierigkeit": "leicht",
                "frage": "Welche Funktion wird für Benutzereingaben verwendet?",
                "typ": "multiple_choice",
                "optionen": ["get()", "input()", "read()", "scan()"],
                "korrekt": 1,
                "erklaerung": "input() ist die Standard-Funktion für Benutzereingaben in Python.",
                "punkte": 1,
            },
            {
                "id": "input_02",
                "kategorie": "Ein-/Ausgabe",
                "schwierigkeit": "mittel",
                "frage": "Was gibt input() immer zurück?",
                "typ": "multiple_choice",
                "optionen": ["int", "float", "str", "den eingegebenen Typ"],
                "korrekt": 2,
                "erklaerung": "input() gibt IMMER einen String zurück, auch bei Zahlen-Eingaben!",
                "punkte": 2,
            },
            # LISTEN UND OPERATIONEN
            {
                "id": "list_01",
                "kategorie": "Listen",
                "schwierigkeit": "leicht",
                "frage": "Wie erstellt man eine leere Liste?",
                "typ": "multiple_choice",
                "optionen": ["list = {}", "list = []", "list = ()", "list = <>"],
                "korrekt": 1,
                "erklaerung": "Eckige Klammern [] erstellen Listen. {} sind Dictionaries, () sind Tupel.",
                "punkte": 1,
            },
            {
                "id": "list_02",
                "kategorie": "Listen",
                "schwierigkeit": "mittel",
                "frage": "Was macht liste.append('Python')?",
                "typ": "multiple_choice",
                "optionen": [
                    "Fügt 'Python' am Anfang hinzu",
                    "Fügt 'Python' am Ende hinzu",
                    "Ersetzt alle Elemente mit 'Python'",
                    "Löscht 'Python' aus der Liste",
                ],
                "korrekt": 1,
                "erklaerung": "append() fügt Elemente immer am Ende der Liste hinzu.",
                "punkte": 2,
            },
            {
                "id": "list_03",
                "kategorie": "Listen",
                "schwierigkeit": "schwer",
                "frage": "Was ist das Ergebnis von: liste = [1, 2, 3]; liste[1]",
                "typ": "multiple_choice",
                "optionen": ["1", "2", "3", "Fehler"],
                "korrekt": 1,
                "erklaerung": "Listen-Indizes beginnen bei 0! liste[1] ist das ZWEITE Element (2).",
                "punkte": 3,
            },
            # SCHLEIFEN UND BEDINGUNGEN
            {
                "id": "loop_01",
                "kategorie": "Schleifen",
                "schwierigkeit": "mittel",
                "frage": "Welche Schleife durchläuft alle Elemente einer Liste?",
                "typ": "multiple_choice",
                "optionen": [
                    "while liste:",
                    "for element in liste:",
                    "loop liste:",
                    "each element in liste:",
                ],
                "korrekt": 1,
                "erklaerung": "for element in liste: ist die Standard-Syntax für Listen-Iteration.",
                "punkte": 2,
            },
            {
                "id": "cond_01",
                "kategorie": "Bedingungen",
                "schwierigkeit": "leicht",
                "frage": "Welches Schlüsselwort prüft eine Bedingung?",
                "typ": "multiple_choice",
                "optionen": ["when", "if", "check", "test"],
                "korrekt": 1,
                "erklaerung": "'if' ist das Schlüsselwort für Bedingungen in Python.",
                "punkte": 1,
            },
            {
                "id": "cond_02",
                "kategorie": "Bedingungen",
                "schwierigkeit": "mittel",
                "frage": "Was prüft: if 'Python' in liste:",
                "typ": "multiple_choice",
                "optionen": [
                    "Ob 'Python' das erste Element ist",
                    "Ob 'Python' irgendwo in der Liste ist",
                    "Ob die Liste nur 'Python' enthält",
                    "Ob 'Python' das letzte Element ist",
                ],
                "korrekt": 1,
                "erklaerung": "Der 'in' Operator prüft, ob ein Element irgendwo in der Liste vorhanden ist.",
                "punkte": 2,
            },
            # CODE-VERSTÄNDNIS FRAGEN
            {
                "id": "code_01",
                "kategorie": "Code-Verständnis",
                "schwierigkeit": "mittel",
                "frage": "Was gibt dieser Code aus?\n\nname = 'Anna'\nalter = 25\nprint(f'Ich bin {name} und {alter} Jahre alt.')",
                "typ": "code_output",
                "korrekt_antwort": "Ich bin Anna und 25 Jahre alt.",
                "erklaerung": "f-strings erlauben das Einsetzen von Variablen mit {variable_name}.",
                "punkte": 2,
            },
            {
                "id": "code_02",
                "kategorie": "Code-Verständnis",
                "schwierigkeit": "schwer",
                "frage": "Was ist das Ergebnis?\n\nliste = ['A', 'B', 'C']\nfor i, buchstabe in enumerate(liste):\n    print(f'{i}: {buchstabe}')",
                "typ": "code_output",
                "korrekt_antwort": "0: A\n1: B\n2: C",
                "erklaerung": "enumerate() gibt Paare von (Index, Element) zurück, beginnend bei 0.",
                "punkte": 3,
            },
            # FEHLERSUCHE
            {
                "id": "debug_01",
                "kategorie": "Debugging",
                "schwierigkeit": "mittel",
                "frage": "Was ist falsch an diesem Code?\n\nalter = input('Alter: ')\nif alter > 18:\n    print('Volljährig')",
                "typ": "multiple_choice",
                "optionen": [
                    "input() funktioniert nicht",
                    "alter muss zu int konvertiert werden",
                    "if-Syntax ist falsch",
                    "print() ist falsch geschrieben",
                ],
                "korrekt": 1,
                "erklaerung": "input() gibt String zurück. Für Zahlenvergleich: alter = int(input('Alter: '))",
                "punkte": 2,
            },
            {
                "id": "debug_02",
                "kategorie": "Debugging",
                "schwierigkeit": "schwer",
                "frage": "Warum gibt es einen Fehler?\n\nliste = [1, 2, 3]\nprint(liste[3])",
                "typ": "multiple_choice",
                "optionen": [
                    "Liste ist zu kurz",
                    "Index 3 existiert nicht (IndexError)",
                    "print() ist falsch",
                    "Liste enthält nur Zahlen",
                ],
                "korrekt": 1,
                "erklaerung": "Liste hat Indizes 0, 1, 2. Index 3 existiert nicht → IndexError!",
                "punkte": 3,
            },
        ]

    def starte_quiz(
        self, anzahl_fragen: int = 10, schwierigkeit: str = "gemischt"
    ) -> None:
        """
        Startet das interaktive Quiz.

        Args:
            anzahl_fragen: Anzahl der zu stellenden Fragen
            schwierigkeit: "leicht", "mittel", "schwer", "gemischt"
        """
        print("🎯 MICRO-ASSESSMENT: Python Grundlagen Quiz")
        print("=" * 50)
        print("Testen Sie Ihr Wissen zu Kapitel 01!")
        print(f"📝 {anzahl_fragen} Fragen, Schwierigkeit: {schwierigkeit}")
        print("=" * 50)

        self.start_zeit = datetime.now()

        # Fragen nach Schwierigkeit filtern und auswählen
        gefilterte_fragen = self._filtere_fragen(schwierigkeit)
        ausgewaehlte_fragen = random.sample(
            gefilterte_fragen, min(anzahl_fragen, len(gefilterte_fragen))
        )

        # Quiz durchführen
        for i, frage in enumerate(ausgewaehlte_fragen, 1):
            print(f"\n📋 FRAGE {i}/{len(ausgewaehlte_fragen)}")
            print(
                f"Kategorie: {frage['kategorie']} | Schwierigkeit: {frage['schwierigkeit']}"
            )
            print("-" * 40)

            if frage["typ"] == "multiple_choice":
                punkte = self._stelle_multiple_choice_frage(frage)
            elif frage["typ"] == "code_output":
                punkte = self._stelle_code_frage(frage)

            self.punkte += punkte
            self.max_punkte += frage["punkte"]

            # Antwort speichern
            self.antworten.append(
                {
                    "frage_id": frage["id"],
                    "kategorie": frage["kategorie"],
                    "punkte_erhalten": punkte,
                    "punkte_max": frage["punkte"],
                }
            )

        # Auswertung anzeigen
        self._zeige_auswertung()

    def _filtere_fragen(self, schwierigkeit: str) -> list[dict[str, Any]]:
        """Filtert Fragen nach Schwierigkeit."""
        if schwierigkeit == "gemischt":
            return self.fragen
        return [f for f in self.fragen if f["schwierigkeit"] == schwierigkeit]

    def _stelle_multiple_choice_frage(self, frage: dict[str, Any]) -> int:
        """Stellt eine Multiple-Choice-Frage."""
        print(frage["frage"])
        print()

        for i, option in enumerate(frage["optionen"]):
            print(f"  {i + 1}. {option}")

        while True:
            try:
                antwort = (
                    int(input(f"\nIhre Antwort (1-{len(frage['optionen'])}): ")) - 1
                )
                if 0 <= antwort < len(frage["optionen"]):
                    break
                else:
                    print("❌ Ungültige Auswahl!")
            except ValueError:
                print("❌ Bitte geben Sie eine Zahl ein!")

        # Feedback geben
        if antwort == frage["korrekt"]:
            print("✅ Richtig!")
            print(f"💡 {frage['erklaerung']}")
            return frage["punkte"]
        else:
            print("❌ Falsch!")
            print(f"✅ Korrekt wäre: {frage['optionen'][frage['korrekt']]}")
            print(f"💡 {frage['erklaerung']}")
            return 0

    def _stelle_code_frage(self, frage: dict[str, Any]) -> int:
        """Stellt eine Code-Verständnis-Frage."""
        print(frage["frage"])
        print("\nWas ist die Ausgabe? (Geben Sie die exakte Ausgabe ein)")

        antwort = input("Ihre Antwort: ").strip()

        # Flexible Antwortprüfung
        korrekt_antwort = frage["korrekt_antwort"].strip()

        if antwort.lower() == korrekt_antwort.lower():
            print("✅ Richtig!")
            print(f"💡 {frage['erklaerung']}")
            return frage["punkte"]
        else:
            print("❌ Falsch!")
            print(f"✅ Korrekte Ausgabe:\n{korrekt_antwort}")
            print(f"💡 {frage['erklaerung']}")
            return 0

    def _zeige_auswertung(self) -> None:
        """Zeigt die detaillierte Quiz-Auswertung."""
        end_zeit = datetime.now()
        dauer = (end_zeit - self.start_zeit).total_seconds()

        print("\n" + "=" * 60)
        print("📊 QUIZ-AUSWERTUNG")
        print("=" * 60)

        # Gesamtergebnis
        prozent = (self.punkte / self.max_punkte) * 100 if self.max_punkte > 0 else 0
        print(
            f"🎯 Gesamtergebnis: {self.punkte}/{self.max_punkte} Punkte ({prozent:.1f}%)"
        )
        print(f"⏱️  Benötigte Zeit: {dauer:.0f} Sekunden")

        # Bewertung
        if prozent >= 90:
            bewertung = "🌟 Ausgezeichnet!"
            kommentar = "Sie beherrschen die Grundlagen perfekt!"
        elif prozent >= 75:
            bewertung = "✅ Sehr gut!"
            kommentar = "Solide Kenntnisse, kleine Lücken schliessen."
        elif prozent >= 60:
            bewertung = "👍 Gut!"
            kommentar = "Grundlagen verstanden, Übung macht den Meister."
        elif prozent >= 40:
            bewertung = "⚠️ Verbesserungsbedarf"
            kommentar = "Wiederholen Sie die Grundlagen und üben Sie mehr."
        else:
            bewertung = "❌ Ungenügend"
            kommentar = "Arbeiten Sie die Theorie nochmals durch."

        print(f"\n{bewertung}")
        print(f"💬 {kommentar}")

        # Kategorien-Analyse
        kategorien = {}
        for antwort in self.antworten:
            kat = antwort["kategorie"]
            if kat not in kategorien:
                kategorien[kat] = {"erhalten": 0, "max": 0}
            kategorien[kat]["erhalten"] += antwort["punkte_erhalten"]
            kategorien[kat]["max"] += antwort["punkte_max"]

        print("\n📈 LEISTUNG NACH KATEGORIEN:")
        print("-" * 40)
        for kategorie, punkte in kategorien.items():
            kat_prozent = (
                (punkte["erhalten"] / punkte["max"]) * 100 if punkte["max"] > 0 else 0
            )
            balken = "█" * int(kat_prozent / 10) + "░" * (10 - int(kat_prozent / 10))
            print(
                f"{kategorie:<15} {balken} {kat_prozent:5.1f}% ({punkte['erhalten']}/{punkte['max']})"
            )

        # Empfehlungen
        self._gib_empfehlungen(kategorien, prozent)

        # Ergebnis speichern
        self._speichere_ergebnis(prozent, kategorien, dauer)

    def _gib_empfehlungen(
        self, kategorien: dict[str, dict[str, int]], gesamt_prozent: float
    ) -> None:
        """Gibt personalisierte Lernempfehlungen."""
        print("\n💡 PERSONALISIERTE EMPFEHLUNGEN:")
        print("-" * 40)

        # Schwache Kategorien identifizieren
        schwache_kategorien = []
        for kat, punkte in kategorien.items():
            prozent = (
                (punkte["erhalten"] / punkte["max"]) * 100 if punkte["max"] > 0 else 0
            )
            if prozent < 60:
                schwache_kategorien.append(kat)

        if schwache_kategorien:
            print("🎯 Fokus-Bereiche für Vertiefung:")
            for kat in schwache_kategorien:
                if kat == "Variablen":
                    print("   • Wiederholen: Variablen erstellen und verwenden")
                    print("   • Übung: uebung_01_personal_info_beginner.py")
                elif kat == "Listen":
                    print("   • Wiederholen: Listen-Operationen (append, sort, in)")
                    print("   • Übung: uebung_03_programmiersprachen_beginner.py")
                elif kat == "Ein-/Ausgabe":
                    print("   • Wiederholen: input() und print() Funktionen")
                    print("   • Übung: Alle Beginner-Übungen nochmals machen")
                elif kat == "Schleifen":
                    print("   • Wiederholen: for-Schleifen und enumerate()")
                    print("   • Übung: Listen durchlaufen und ausgeben")
                elif kat == "Bedingungen":
                    print("   • Wiederholen: if/elif/else Strukturen")
                    print("   • Übung: uebung_02_taschenrechner_beginner.py")
                elif kat == "Code-Verständnis":
                    print("   • Übung: Code Zeile für Zeile durchgehen")
                    print("   • Tipp: Verwenden Sie print() zum Debuggen")
                elif kat == "Debugging":
                    print("   • Wiederholen: Häufige Fehlertypen")
                    print("   • Tipp: Fehlermeldungen genau lesen")

        # Allgemeine Empfehlungen basierend auf Gesamtergebnis
        if gesamt_prozent < 60:
            print("\n🔄 Allgemeine Empfehlungen:")
            print("   • Arbeiten Sie alle Beginner-Übungen nochmals durch")
            print("   • Nutzen Sie die hints.md Dateien für Konzepte")
            print("   • Beginnen Sie mit skeleton.py Dateien")
            print("   • Fragen Sie bei Unklarheiten nach!")
        elif gesamt_prozent < 80:
            print("\n🚀 Nächste Schritte:")
            print("   • Probieren Sie die Intermediate-Übungen")
            print("   • Vertiefen Sie schwache Bereiche")
            print("   • Experimentieren Sie mit eigenen Variationen")
        else:
            print("\n🌟 Weiterführende Herausforderungen:")
            print("   • Versuchen Sie die Advanced-Übungen")
            print("   • Entwickeln Sie eigene kleine Projekte")
            print("   • Helfen Sie anderen beim Lernen")

    def _speichere_ergebnis(
        self, prozent: float, kategorien: dict, dauer: float
    ) -> None:
        """Speichert das Quiz-Ergebnis für Verlaufsverfolgung."""
        ergebnis = {
            "datum": datetime.now().isoformat(),
            "punkte": self.punkte,
            "max_punkte": self.max_punkte,
            "prozent": prozent,
            "dauer_sekunden": dauer,
            "kategorien": kategorien,
            "antworten": self.antworten,
        }

        try:
            # Versuche vorherige Ergebnisse zu laden
            try:
                with open("quiz_verlauf.json", encoding="utf-8") as f:
                    verlauf = json.load(f)
            except FileNotFoundError:
                verlauf = []

            # Neues Ergebnis hinzufügen
            verlauf.append(ergebnis)

            # Speichern
            with open("quiz_verlauf.json", "w", encoding="utf-8") as f:
                json.dump(verlauf, f, indent=2, ensure_ascii=False)

            print("\n💾 Ergebnis gespeichert in quiz_verlauf.json")

        except Exception as e:
            print(f"\n⚠️ Konnte Ergebnis nicht speichern: {e}")


def main():
    """Hauptfunktion für das Micro-Assessment Quiz."""
    print("🎓 BYSTRONIC PYTHON GRUNDKURS")
    print("Micro-Assessment für Kapitel 01")
    print("=" * 40)

    quiz = MicroAssessmentQuiz()

    # Benutzer-Optionen
    print("Wählen Sie Ihre Quiz-Einstellungen:")
    print("1. Schnelltest (5 Fragen, gemischt)")
    print("2. Standardtest (10 Fragen, gemischt)")
    print("3. Umfassender Test (15 Fragen, gemischt)")
    print("4. Nur leichte Fragen (8 Fragen)")
    print("5. Nur schwere Fragen (6 Fragen)")

    while True:
        try:
            wahl = int(input("\nIhre Wahl (1-5): "))
            if 1 <= wahl <= 5:
                break
            print("❌ Bitte wählen Sie 1-5!")
        except ValueError:
            print("❌ Bitte geben Sie eine Zahl ein!")

    # Quiz starten basierend auf Wahl
    if wahl == 1:
        quiz.starte_quiz(5, "gemischt")
    elif wahl == 2:
        quiz.starte_quiz(10, "gemischt")
    elif wahl == 3:
        quiz.starte_quiz(15, "gemischt")
    elif wahl == 4:
        quiz.starte_quiz(8, "leicht")
    elif wahl == 5:
        quiz.starte_quiz(6, "schwer")

    print("\n🎉 Quiz beendet! Vielen Dank für Ihre Teilnahme!")
    print("💡 Nutzen Sie die Empfehlungen für gezieltes Lernen.")


if __name__ == "__main__":
    main()

"""
VERWENDUNG:
===========
python micro_assessment_quiz.py

FEATURES:
=========
✅ 15+ Fragen zu allen wichtigen Konzepten
✅ Multiple-Choice und Code-Verständnis Fragen
✅ Adaptive Schwierigkeitsgrade
✅ Sofortiges Feedback mit Erklärungen
✅ Detaillierte Kategorien-Analyse
✅ Personalisierte Lernempfehlungen
✅ Verlaufsspeicherung in JSON
✅ Verschiedene Quiz-Modi

LERNKONTROLLE:
==============
□ Verstehe ich Variablen und Datentypen?
□ Kann ich mit Listen arbeiten?
□ Beherrsche ich Ein-/Ausgabe-Funktionen?
□ Verstehe ich Schleifen und Bedingungen?
□ Kann ich einfachen Code lesen und verstehen?
□ Erkenne ich häufige Programmierfehler?
"""
