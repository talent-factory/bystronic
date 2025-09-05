#!/usr/bin/env python3
"""
Eingangsassessment für Kapitel 01: Python Grundlagen
====================================================

Dieses interaktive Assessment hilft Teilnehmern dabei, ihren optimalen
Lernpfad zu bestimmen basierend auf:
- Vorerfahrung mit Programmierung
- Python-Kenntnisse
- Verfügbare Lernzeit
- Lernziele und Motivation

Ergebnis: Empfehlung für 🟢 Beginner, 🟡 Intermediate oder 🔴 Advanced Pfad

Autor: Daniel Senften
"""

import json
from datetime import datetime
from pathlib import Path


class LearningPathAssessment:
    """Klasse für das Eingangsassessment zur Lernpfad-Bestimmung"""

    def __init__(self):
        self.responses: dict = {}
        self.score_weights = {
            "programming_experience": 0.3,
            "python_knowledge": 0.25,
            "ai_experience": 0.2,
            "time_availability": 0.15,
            "learning_goals": 0.1,
        }

    def welcome_message(self) -> None:
        """Zeigt Begrussungsnachricht und Erklärung"""
        print("=" * 70)
        print("🎯 EINGANGSASSESSMENT - Python Grundlagen Kapitel 01")
        print("=" * 70)
        print()
        print("Willkommen zum Bystronic Python Grundkurs!")
        print()
        print("Dieses Assessment hilft uns dabei, den optimalen Lernpfad für Sie")
        print("zu bestimmen. Es dauert etwa 5-7 Minuten und berücksichtigt:")
        print()
        print("📊 Ihre Programmiererfahrung")
        print("🐍 Vorhandene Python-Kenntnisse")
        print("🤖 Erfahrung mit KI-Tools")
        print("⏰ Verfügbare Lernzeit")
        print("🎯 Ihre Lernziele")
        print()
        print("Basierend auf Ihren Antworten empfehlen wir:")
        print("🟢 Beginner-Pfad (15-25 Min/Übung)")
        print("🟡 Intermediate-Pfad (25-40 Min/Übung)")
        print("🔴 Advanced-Pfad (45-60 Min/Übung)")
        print()
        input("Drücken Sie Enter um zu beginnen...")
        print()

    def assess_programming_experience(self) -> int:
        """Bewertet allgemeine Programmiererfahrung (0-10 Punkte)"""
        print("📊 PROGRAMMIERERFAHRUNG")
        print("-" * 30)

        questions = [
            {
                "question": "Wie würden Sie Ihre allgemeine Programmiererfahrung einschätzen?",
                "options": [
                    "Keine Erfahrung - ich bin kompletter Neuling",
                    "Grundlagen - ich habe schon mal einfache Skripte geschrieben",
                    "Fortgeschritten - ich programmiere regelmässig (VBA, etc.)",
                    "Erfahren - ich entwickle komplexe Anwendungen",
                    "Experte - ich bin professioneller Softwareentwickler",
                ],
                "scores": [0, 2, 5, 8, 10],
            },
            {
                "question": "Mit welchen Programmiersprachen haben Sie bereits gearbeitet?",
                "options": [
                    "Keine",
                    "Nur VBA/Excel-Makros",
                    "VBA + eine weitere Sprache (SQL, etc.)",
                    "Mehrere Sprachen (Java, C#, JavaScript, etc.)",
                    "Viele Sprachen + moderne Frameworks",
                ],
                "scores": [0, 1, 3, 6, 9],
            },
        ]

        total_score = 0
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question']}")
            for j, option in enumerate(q["options"], 1):
                print(f"   {j}) {option}")

            while True:
                try:
                    choice = int(input("\nIhre Wahl (1-5): ")) - 1
                    if 0 <= choice < len(q["options"]):
                        score = q["scores"][choice]
                        total_score += score
                        self.responses[f"programming_q{i}"] = {
                            "answer": q["options"][choice],
                            "score": score,
                        }
                        break
                    else:
                        print("Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")

        return min(total_score, 10)  # Max 10 Punkte

    def assess_python_knowledge(self) -> int:
        """Bewertet Python-spezifische Kenntnisse (0-10 Punkte)"""
        print("\n🐍 PYTHON-KENNTNISSE")
        print("-" * 25)

        questions = [
            {
                "question": "Haben Sie schon einmal Python-Code geschrieben?",
                "options": [
                    "Nein, noch nie",
                    "Ja, ein paar Zeilen ausprobiert",
                    "Ja, einfache Skripte geschrieben",
                    "Ja, regelmässig für Automatisierung",
                    "Ja, komplexe Anwendungen entwickelt",
                ],
                "scores": [0, 1, 3, 6, 10],
            },
            {
                "question": "Welche Python-Konzepte kennen Sie bereits?",
                "options": [
                    "Keine",
                    "Grundlagen (Variablen, print, input)",
                    "Listen, Dictionaries, Funktionen",
                    "Klassen, Module, Fehlerbehandlung",
                    "Decorators, Generators, async/await",
                ],
                "scores": [0, 2, 4, 7, 10],
            },
        ]

        total_score = 0
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question']}")
            for j, option in enumerate(q["options"], 1):
                print(f"   {j}) {option}")

            while True:
                try:
                    choice = int(input("\nIhre Wahl (1-5): ")) - 1
                    if 0 <= choice < len(q["options"]):
                        score = q["scores"][choice]
                        total_score += score
                        self.responses[f"python_q{i}"] = {
                            "answer": q["options"][choice],
                            "score": score,
                        }
                        break
                    else:
                        print("Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")

        return min(total_score, 10)  # Max 10 Punkte

    def assess_ai_experience(self) -> int:
        """Bewertet Erfahrung mit KI-Tools (0-10 Punkte)"""
        print("\n🤖 KI-TOOLS ERFAHRUNG")
        print("-" * 25)

        questions = [
            {
                "question": "Haben Sie schon mit KI-Tools programmiert (ChatGPT, GitHub Copilot, etc.)?",
                "options": [
                    "Nein, noch nie",
                    "Ja, gelegentlich für einfache Fragen",
                    "Ja, regelmässig für Code-Generierung",
                    "Ja, täglich für komplexe Entwicklung",
                    "Ja, ich bin Experte im Prompt Engineering",
                ],
                "scores": [0, 2, 5, 8, 10],
            },
            {
                "question": "Wie erfolgreich waren Sie beim KI-assistierten Programmieren?",
                "options": [
                    "Keine Erfahrung",
                    "Gemischte Ergebnisse, oft Probleme",
                    "Meist erfolgreich bei einfachen Aufgaben",
                    "Sehr erfolgreich, auch bei komplexen Projekten",
                    "Experte - ich kann KI optimal für Entwicklung nutzen",
                ],
                "scores": [0, 1, 4, 7, 10],
            },
        ]

        total_score = 0
        for i, q in enumerate(questions, 1):
            print(f"\n{i}. {q['question']}")
            for j, option in enumerate(q["options"], 1):
                print(f"   {j}) {option}")

            while True:
                try:
                    choice = int(input("\nIhre Wahl (1-5): ")) - 1
                    if 0 <= choice < len(q["options"]):
                        score = q["scores"][choice]
                        total_score += score
                        self.responses[f"ai_q{i}"] = {
                            "answer": q["options"][choice],
                            "score": score,
                        }
                        break
                    else:
                        print("Bitte wählen Sie eine Zahl zwischen 1 und 5.")
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")

        return min(total_score, 10)  # Max 10 Punkte

    def assess_time_availability(self) -> int:
        """Bewertet verfügbare Lernzeit (0-10 Punkte)"""
        print("\n⏰ VERFÜGBARE LERNZEIT")
        print("-" * 25)

        question = {
            "question": "Wie viel Zeit können Sie pro Woche für das Python-Lernen aufwenden?",
            "options": [
                "1-2 Stunden (sehr wenig Zeit)",
                "3-4 Stunden (begrenzte Zeit)",
                "5-6 Stunden (moderate Zeit)",
                "7-10 Stunden (viel Zeit)",
                "10+ Stunden (sehr viel Zeit)",
            ],
            "scores": [2, 4, 6, 8, 10],
        }

        print(f"\n{question['question']}")
        for j, option in enumerate(question["options"], 1):
            print(f"   {j}) {option}")

        while True:
            try:
                choice = int(input("\nIhre Wahl (1-5): ")) - 1
                if 0 <= choice < len(question["options"]):
                    score = question["scores"][choice]
                    self.responses["time_availability"] = {
                        "answer": question["options"][choice],
                        "score": score,
                    }
                    return score
                else:
                    print("Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")

    def assess_learning_goals(self) -> int:
        """Bewertet Lernziele und Motivation (0-10 Punkte)"""
        print("\n🎯 LERNZIELE")
        print("-" * 15)

        question = {
            "question": "Was ist Ihr Hauptziel mit Python?",
            "options": [
                "Grundlagen verstehen, langsam lernen",
                "VBA-Kenntnisse zu Python übertragen",
                "Schnell produktiv werden für Projekte",
                "Professionelle Entwicklung, Best Practices",
                "Experte werden, andere mentorieren",
            ],
            "scores": [2, 4, 6, 8, 10],
        }

        print(f"\n{question['question']}")
        for j, option in enumerate(question["options"], 1):
            print(f"   {j}) {option}")

        while True:
            try:
                choice = int(input("\nIhre Wahl (1-5): ")) - 1
                if 0 <= choice < len(question["options"]):
                    score = question["scores"][choice]
                    self.responses["learning_goals"] = {
                        "answer": question["options"][choice],
                        "score": score,
                    }
                    return score
                else:
                    print("Bitte wählen Sie eine Zahl zwischen 1 und 5.")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein.")

    def calculate_final_score(self, scores: dict[str, int]) -> tuple[float, str]:
        """Berechnet Gesamtscore und bestimmt Lernpfad"""
        weighted_score = 0
        for category, score in scores.items():
            weight = self.score_weights.get(category, 0)
            weighted_score += score * weight

        # Bestimme Lernpfad basierend auf Score
        if weighted_score <= 3.5:
            path = "beginner"
            emoji = "🟢"
            description = "Beginner"
        elif weighted_score <= 6.5:
            path = "intermediate"
            emoji = "🟡"
            description = "Intermediate"
        else:
            path = "advanced"
            emoji = "🔴"
            description = "Advanced"

        return weighted_score, f"{emoji} {description}"

    def generate_recommendations(self, path: str, scores: dict[str, int]) -> list[str]:
        """Generiert personalisierte Empfehlungen basierend auf Lernpfad"""
        recommendations = []

        if path.startswith("🟢"):
            recommendations.extend(
                [
                    "📚 Beginnen Sie mit der Theorie in 'theory/01_python_grundlagen.adoc'",
                    "💡 Schauen Sie sich die Beispiele in 'examples/' an",
                    "🎯 Starten Sie mit den Beginner-Übungen in 'exercises/beginner/'",
                    "💭 Nutzen Sie alle 4 Hilfsstufen (Hints → Skeleton → Partial → Complete)",
                    "⏰ Planen Sie 15-25 Minuten pro Übung ein",
                    "🤝 Zögern Sie nicht, Fragen zu stellen!",
                ]
            )

            if scores.get("time_availability", 0) <= 4:
                recommendations.append(
                    "⚡ Bei wenig Zeit: Fokus auf eine Übung pro Woche"
                )

        elif path.startswith("🟡"):
            recommendations.extend(
                [
                    "📖 Überfliegen Sie die Theorie, fokussieren Sie auf neue Konzepte",
                    "🚀 Beginnen Sie direkt mit Intermediate-Übungen in 'exercises/intermediate/'",
                    "🎯 Nutzen Sie Hints nur bei Blockaden",
                    "💎 Achten Sie auf Code-Qualität und Best Practices",
                    "⏰ Planen Sie 25-40 Minuten pro Übung ein",
                    "🔄 Vergleichen Sie Ihre Lösungen mit den Musterlösungen",
                ]
            )

            if scores.get("ai_experience", 0) >= 5:
                recommendations.append("🤖 Nutzen Sie KI-Tools zur Code-Optimierung")

        else:  # Advanced
            recommendations.extend(
                [
                    "🏗️ Fokussieren Sie auf Architektur und Design Patterns",
                    "🔴 Bearbeiten Sie die Advanced-Übungen in 'exercises/advanced/'",
                    "🎓 Übernehmen Sie Mentoring-Aufgaben für andere Teilnehmer",
                    "⚡ Optimieren Sie für Performance und Skalierbarkeit",
                    "⏰ Planen Sie 45-60 Minuten pro Übung ein",
                    "🌟 Entwickeln Sie eigene innovative Lösungsansätze",
                ]
            )

            if scores.get("programming_experience", 0) >= 8:
                recommendations.append(
                    "🚀 Erwägen Sie Beiträge zu Open Source Projekten"
                )

        return recommendations

    def show_results(self, scores: dict[str, int]) -> None:
        """Zeigt Ergebnisse und Empfehlungen an"""
        final_score, path = self.calculate_final_score(scores)
        recommendations = self.generate_recommendations(path, scores)

        print("\n" + "=" * 70)
        print("🎉 ASSESSMENT ABGESCHLOSSEN - IHRE ERGEBNISSE")
        print("=" * 70)
        print()
        print(f"📊 Ihr Gesamtscore: {final_score:.1f}/10.0")
        print(f"🎯 Empfohlener Lernpfad: {path}")
        print()

        # Detaillierte Scores anzeigen
        print("📈 DETAILLIERTE BEWERTUNG:")
        print("-" * 30)
        categories = {
            "programming_experience": "Programmiererfahrung",
            "python_knowledge": "Python-Kenntnisse",
            "ai_experience": "KI-Tools Erfahrung",
            "time_availability": "Verfügbare Zeit",
            "learning_goals": "Lernziele",
        }

        for key, label in categories.items():
            score = scores.get(key, 0)
            weight = self.score_weights[key]
            weighted = score * weight
            print(f"{label:20} {score:2}/10 (Gewicht: {weight:.0%}) = {weighted:.1f}")

        print()
        print("🎯 PERSONALISIERTE EMPFEHLUNGEN:")
        print("-" * 35)
        for i, rec in enumerate(recommendations, 1):
            print(f"{i:2}. {rec}")

        print()
        print("📁 NÄCHSTE SCHRITTE:")
        print("-" * 20)

        if path.startswith("🟢"):
            print("→ Öffnen Sie: src/01_grundlagen/theory/README.md")
            print("→ Dann: src/01_grundlagen/exercises/beginner/README.md")
        elif path.startswith("🟡"):
            print("→ Öffnen Sie: src/01_grundlagen/exercises/intermediate/README.md")
            print("→ Optional: src/01_grundlagen/theory/ für Referenz")
        else:
            print("→ Öffnen Sie: src/01_grundlagen/exercises/advanced/README.md")
            print("→ Erwägen Sie: Mentoring für andere Teilnehmer")

        print()
        print(
            "💡 TIPP: Sie können jederzeit zwischen den Schwierigkeitsgraden wechseln!"
        )
        print("📞 Bei Fragen: Wenden Sie sich an den Kursleiter")

    def save_results(self, scores: dict[str, int]) -> None:
        """Speichert Ergebnisse für spätere Analyse"""
        final_score, path = self.calculate_final_score(scores)

        result_data = {
            "timestamp": datetime.now().isoformat(),
            "scores": scores,
            "final_score": final_score,
            "recommended_path": path,
            "responses": self.responses,
        }

        # Erstelle results Verzeichnis falls nicht vorhanden
        results_dir = Path(__file__).parent / "results"
        results_dir.mkdir(exist_ok=True)

        # Speichere mit Timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"assessment_result_{timestamp}.json"
        filepath = results_dir / filename

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(result_data, f, indent=2, ensure_ascii=False)
            print(f"\n💾 Ergebnisse gespeichert in: {filepath}")
        except Exception as e:
            print(f"\n⚠️ Fehler beim Speichern: {e}")

    def run_assessment(self) -> None:
        """Führt das komplette Assessment durch"""
        self.welcome_message()

        # Sammle alle Scores
        scores = {
            "programming_experience": self.assess_programming_experience(),
            "python_knowledge": self.assess_python_knowledge(),
            "ai_experience": self.assess_ai_experience(),
            "time_availability": self.assess_time_availability(),
            "learning_goals": self.assess_learning_goals(),
        }

        # Zeige Ergebnisse
        self.show_results(scores)

        # Speichere Ergebnisse
        self.save_results(scores)

        print("\n" + "=" * 70)
        print("Viel Erfolg beim Python-Lernen! 🐍✨")
        print("=" * 70)


def main():
    """Hauptfunktion"""
    try:
        assessment = LearningPathAssessment()
        assessment.run_assessment()
    except KeyboardInterrupt:
        print("\n\n⚠️ Assessment abgebrochen.")
        print("Sie können es jederzeit erneut starten!")
    except Exception as e:
        print(f"\n❌ Ein Fehler ist aufgetreten: {e}")
        print("Bitte wenden Sie sich an den Kursleiter.")


if __name__ == "__main__":
    main()
