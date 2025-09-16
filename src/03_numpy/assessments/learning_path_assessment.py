#!/usr/bin/env python3
"""
🎯 NumPy Learning Path Assessment
Bystronic Python Grundkurs - Kapitel 3

Dieses Assessment bestimmt Ihren optimalen Lernpfad für NumPy basierend auf:
- Array-Grundlagen (20%)
- Mathematische Operationen (25%)
- Programmierpraxis (20%)
- Anwendungskontext (20%)
- Performance-Bewusstsein (15%)

Dauer: 7-10 Minuten
Ergebnis: Personalisierte Lernpfad-Empfehlung
"""

import json
import os
from datetime import datetime


class NumPyAssessment:
    """NumPy Learning Path Assessment System"""

    def __init__(self):
        self.questions = self._setup_questions()
        self.responses = {}
        self.results_dir = os.path.join(os.path.dirname(__file__), "results")

        # Erstelle results-Verzeichnis falls nicht vorhanden
        os.makedirs(self.results_dir, exist_ok=True)

    def _setup_questions(self) -> list[dict]:
        """Definiert alle Assessment-Fragen mit Gewichtungen"""
        return [
            # ===== KATEGORIE 1: Array-Grundlagen (20%) =====
            {
                "id": "arrays_01",
                "category": "array_basics",
                "weight": 0.20,
                "question": "Wie würden Sie Ihr aktuelles Verständnis von NumPy-Arrays beschreiben?",
                "type": "scale",
                "options": [
                    "Noch nie von NumPy gehört",
                    "Grundlagen bekannt, aber noch nie verwendet",
                    "Einfache Arrays erstellt und verwendet",
                    "Mehrdimensionale Arrays und Slicing verstanden",
                    "Erweiterte Array-Manipulationen beherrscht",
                ],
                "points": [0, 2, 5, 8, 10],
            },
            {
                "id": "arrays_02",
                "category": "array_basics",
                "weight": 0.20,
                "question": "Was ist der Hauptvorteil von NumPy-Arrays gegenüber Python-Listen?",
                "type": "multiple_choice",
                "options": [
                    "Einfachere Syntax",
                    "Performance und vektorisierte Operationen",
                    "Bessere Lesbarkeit",
                    "Automatische Fehlerbehandlung",
                    "Weiß ich nicht",
                ],
                "points": [2, 10, 1, 1, 0],
            },
            {
                "id": "arrays_03",
                "category": "array_basics",
                "weight": 0.20,
                "question": "Welche Array-Erstellungsmethoden kennen Sie? (Mehrfachauswahl möglich)",
                "type": "multiple_select",
                "options": [
                    "np.array([1, 2, 3])",
                    "np.zeros() und np.ones()",
                    "np.arange() und np.linspace()",
                    "np.random.random()",
                    "np.eye() für Einheitsmatrizen",
                    "Kenne keine davon",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            {
                "id": "arrays_04",
                "category": "array_basics",
                "weight": 0.20,
                "question": "Wie erfahren sind Sie mit Array-Indexing und Slicing?",
                "type": "scale",
                "options": [
                    "Gar nicht - verstehe nur Python-Listen",
                    "Einfaches Indexing (arr[0], arr[-1])",
                    "Grundlegendes Slicing (arr[1:5])",
                    "Mehrdimensionales Indexing (arr[0, 1:3])",
                    "Boolean Indexing und erweiterte Techniken",
                ],
                "points": [0, 2, 5, 8, 10],
            },
            {
                "id": "arrays_05",
                "category": "array_basics",
                "weight": 0.20,
                "question": "Was bedeutet 'Broadcasting' in NumPy?",
                "type": "multiple_choice",
                "options": [
                    "Verteilung von Arrays auf mehrere Prozessoren",
                    "Automatische Anpassung von Array-Shapes für Operationen",
                    "Übertragung von Daten über das Netzwerk",
                    "Erweitern von Arrays durch Kopieren",
                    "Habe noch nie davon gehört",
                ],
                "points": [1, 10, 0, 3, 0],
            },
            # ===== KATEGORIE 2: Mathematische Operationen (25%) =====
            {
                "id": "math_01",
                "category": "mathematical_operations",
                "weight": 0.25,
                "question": "Wie gut kennen Sie mathematische NumPy-Funktionen?",
                "type": "scale",
                "options": [
                    "Gar nicht - verwende nur Python-Funktionen",
                    "Grundlagen wie sum(), mean()",
                    "Erweitert: std(), var(), min(), max()",
                    "Statistische Funktionen: percentile(), corrcoef()",
                    "Trigonometrie, logarithmische und spezielle Funktionen",
                ],
                "points": [0, 3, 6, 8, 10],
            },
            {
                "id": "math_02",
                "category": "mathematical_operations",
                "weight": 0.25,
                "question": "Erfahrung mit vektorisierten Operationen:",
                "type": "scale",
                "options": [
                    "Verwende immer for-Schleifen",
                    "Verstehe das Konzept, aber selten angewendet",
                    "Verwende regelmäßig arr * 2, arr + 5, etc.",
                    "Komplexe Operationen wie np.where(), np.select()",
                    "Selbstgeschriebene vectorized functions mit np.vectorize",
                ],
                "points": [0, 2, 5, 8, 10],
            },
            {
                "id": "math_03",
                "category": "mathematical_operations",
                "weight": 0.25,
                "question": "Welche statistischen Berechnungen haben Sie bereits implementiert?",
                "type": "multiple_select",
                "options": [
                    "Mittelwert und Standardabweichung",
                    "Korrelationsanalysen",
                    "Perzentile und Quantile",
                    "Prozessfähigkeitsindizes (Cp, Cpk)",
                    "Statistische Prozesskontrolle (SPC)",
                    "Noch keine statistischen Berechnungen",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            {
                "id": "math_04",
                "category": "mathematical_operations",
                "weight": 0.25,
                "question": "Lineare Algebra mit NumPy:",
                "type": "multiple_choice",
                "options": [
                    "Keine Erfahrung mit Matrizen",
                    "Matrix-Erstellung und einfache Operationen",
                    "Matrix-Multiplikation (@ oder np.dot)",
                    "Inverse, Determinante, Eigenwerte",
                    "Lösung linearer Gleichungssysteme mit np.linalg",
                ],
                "points": [0, 3, 6, 8, 10],
            },
            # ===== KATEGORIE 3: Programmierpraxis (20%) =====
            {
                "id": "practice_01",
                "category": "programming_practice",
                "weight": 0.20,
                "question": "Ihre allgemeine Programmiererfahrung:",
                "type": "scale",
                "options": [
                    "Anfänger - erste Schritte in Python",
                    "Grundlagen - einfache Skripte und Funktionen",
                    "Intermediate - objektorientierte Programmierung",
                    "Fortgeschritten - komplexe Anwendungen",
                    "Expert - professionelle Softwareentwicklung",
                ],
                "points": [1, 3, 5, 8, 10],
            },
            {
                "id": "practice_02",
                "category": "programming_practice",
                "weight": 0.20,
                "question": "Erfahrung mit anderen numerischen Bibliotheken:",
                "type": "multiple_select",
                "options": [
                    "Pandas für Datenanalyse",
                    "SciPy für wissenschaftliche Berechnungen",
                    "Matplotlib für Visualisierungen",
                    "Sklearn/scikit-learn für Machine Learning",
                    "Andere (R, MATLAB, etc.)",
                    "Keine anderen Bibliotheken",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            {
                "id": "practice_03",
                "category": "programming_practice",
                "weight": 0.20,
                "question": "Debugging und Problemlösung:",
                "type": "scale",
                "options": [
                    "Brauche meist Hilfe bei Fehlern",
                    "Kann einfache Syntax-Fehler beheben",
                    "Verwende Print-Statements für Debugging",
                    "Nutze Debugger und verstehe Stack Traces",
                    "Systematisches Debugging und Unit Testing",
                ],
                "points": [1, 3, 5, 7, 10],
            },
            {
                "id": "practice_04",
                "category": "programming_practice",
                "weight": 0.20,
                "question": "Code-Organisation und Best Practices:",
                "type": "multiple_choice",
                "options": [
                    "Schreibe meist ein großes Skript",
                    "Teile Code in Funktionen auf",
                    "Verwende Klassen und Module",
                    "Dokumentation, Docstrings, Type Hints",
                    "Befolge PEP8 und verwende Linting",
                ],
                "points": [2, 4, 6, 8, 10],
            },
            {
                "id": "practice_05",
                "category": "programming_practice",
                "weight": 0.20,
                "question": "Mit welchen Entwicklungsumgebungen haben Sie Erfahrung?",
                "type": "multiple_select",
                "options": [
                    "Jupyter Notebooks",
                    "VS Code oder ähnliche IDEs",
                    "Command Line / Terminal",
                    "Git für Versionskontrolle",
                    "Package Manager (pip, conda, etc.)",
                    "Keine besonderen Tools",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            # ===== KATEGORIE 4: Anwendungskontext (20%) =====
            {
                "id": "context_01",
                "category": "application_context",
                "weight": 0.20,
                "question": "In welchen Bereichen haben Sie Datenanalyse betrieben?",
                "type": "multiple_select",
                "options": [
                    "Produktionsdaten und Maschinendaten",
                    "Qualitätskontrolle und Messungen",
                    "Finanz- und Geschäftsdaten",
                    "Wissenschaftliche oder technische Daten",
                    "Sensor- oder IoT-Daten",
                    "Noch keine Datenanalyse gemacht",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            {
                "id": "context_02",
                "category": "application_context",
                "weight": 0.20,
                "question": "Ihr Hintergrund in technischen/ingenieursrelevanten Berechnungen:",
                "type": "scale",
                "options": [
                    "Keine technische/ingenieurstechnische Erfahrung",
                    "Grundkenntnisse in Mathematik und Physik",
                    "Ingenieurstudium oder technische Ausbildung",
                    "Berufserfahrung in Fertigung/Produktion",
                    "Expertin/Experte in technischen Berechnungen",
                ],
                "points": [2, 4, 6, 8, 10],
            },
            {
                "id": "context_03",
                "category": "application_context",
                "weight": 0.20,
                "question": "Erfahrung mit Bystronic-spezifischen Anwendungen:",
                "type": "multiple_select",
                "options": [
                    "Laserschneidprozesse und Parameter",
                    "Blechbearbeitung und Umformung",
                    "CNC-Programmierung und Koordinaten",
                    "Qualitätskontrolle in der Fertigung",
                    "Produktionsplanung und -optimierung",
                    "Bin neu bei Bystronic/der Fertigung",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            {
                "id": "context_04",
                "category": "application_context",
                "weight": 0.20,
                "question": "Welche Art von Datenmengen verarbeiten Sie typischerweise?",
                "type": "multiple_choice",
                "options": [
                    "Kleine Datensätze (< 1000 Zeilen)",
                    "Mittlere Datensätze (1K - 100K Zeilen)",
                    "Große Datensätze (100K - 1M Zeilen)",
                    "Sehr große Datensätze (> 1M Zeilen)",
                    "Verarbeite normalerweise keine Daten",
                ],
                "points": [3, 5, 7, 10, 0],
            },
            {
                "id": "context_05",
                "category": "application_context",
                "weight": 0.20,
                "question": "Ihre Motivation für das Erlernen von NumPy:",
                "type": "multiple_select",
                "options": [
                    "Bessere Performance als pure Python",
                    "Vorbereitung für Machine Learning",
                    "Wissenschaftliche/technische Berechnungen",
                    "Integration in bestehende Workflows",
                    "Karriereentwicklung und neue Fähigkeiten",
                    "Ist Teil des Kurses",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 1],
                "max_points": 10,
            },
            # ===== KATEGORIE 5: Performance-Bewusstsein (15%) =====
            {
                "id": "performance_01",
                "category": "performance_awareness",
                "weight": 0.15,
                "question": "Ihre Erfahrung mit Performance-Optimierung:",
                "type": "scale",
                "options": [
                    "Habe noch nie über Performance nachgedacht",
                    "Weiß, dass Performance wichtig ist",
                    "Habe schon mal Laufzeiten gemessen",
                    "Kann Code-Bottlenecks identifizieren",
                    "Systematische Performance-Analyse und Profiling",
                ],
                "points": [0, 2, 4, 7, 10],
            },
            {
                "id": "performance_02",
                "category": "performance_awareness",
                "weight": 0.15,
                "question": "Was verstehen Sie unter Memory-Management?",
                "type": "multiple_choice",
                "options": [
                    "Ist für mich nicht relevant",
                    "RAM-Verbrauch des Computers",
                    "Effiziente Datenstrukturen wählen",
                    "Array-Layouts und Memory-Locality",
                    "Copy vs. View, In-Place-Operationen",
                ],
                "points": [0, 3, 5, 8, 10],
            },
            {
                "id": "performance_03",
                "category": "performance_awareness",
                "weight": 0.15,
                "question": "Kennen Sie Tools für Performance-Messung?",
                "type": "multiple_select",
                "options": [
                    "time.time() für einfache Messungen",
                    "timeit Modul für Benchmarks",
                    "cProfile für detailliertes Profiling",
                    "Memory-Profiler für RAM-Verbrauch",
                    "Jupyter %timeit magic commands",
                    "Kenne keine Tools",
                ],
                "points_per_selection": [2, 2, 2, 2, 2, 0],
                "max_points": 10,
            },
            {
                "id": "performance_04",
                "category": "performance_awareness",
                "weight": 0.15,
                "question": "Wie wichtig ist Ihnen Code-Performance in Ihren Projekten?",
                "type": "scale",
                "options": [
                    "Nicht wichtig - Hauptsache es funktioniert",
                    "Etwas wichtig - bei langsamen Programmen",
                    "Wichtig - achte auf effiziente Algorithmen",
                    "Sehr wichtig - optimiere regelmäßig",
                    "Kritisch - Performance ist entscheidend",
                ],
                "points": [1, 3, 5, 8, 10],
            },
            {
                "id": "performance_05",
                "category": "performance_awareness",
                "weight": 0.15,
                "question": "Erfahrung mit paralleler Verarbeitung oder GPU-Computing:",
                "type": "multiple_choice",
                "options": [
                    "Keine Erfahrung damit",
                    "Theoretisches Verständnis",
                    "Multiprocessing in Python verwendet",
                    "Threading für I/O-bound Tasks",
                    "GPU-Computing (CUDA, OpenCL, etc.)",
                ],
                "points": [0, 2, 5, 7, 10],
            },
        ]

    def run_assessment(self):
        """Führt das komplette Assessment durch"""
        print("🎯 NumPy Learning Path Assessment")
        print("=" * 50)
        print("Willkommen zum NumPy-Assessment des Bystronic Python Grundkurses!")
        print()
        print("Dieses Assessment dauert etwa 7-10 Minuten und hilft dabei,")
        print("Ihren optimalen Lernpfad für NumPy zu bestimmen.")
        print()
        print("📊 Bewertungskategorien:")
        print("• Array-Grundlagen (20%)")
        print("• Mathematische Operationen (25%)")
        print("• Programmierpraxis (20%)")
        print("• Anwendungskontext (20%)")
        print("• Performance-Bewusstsein (15%)")
        print()

        input("Drücken Sie Enter, um zu beginnen...")
        print()

        # Durchlaufe alle Fragen
        for i, question in enumerate(self.questions, 1):
            self._ask_question(i, question)

        # Berechne Ergebnisse
        results = self._calculate_results()

        # Zeige Ergebnisse
        self._display_results(results)

        # Speichere Ergebnisse
        self._save_results(results)

        return results

    def _ask_question(self, number: int, question: dict):
        """Stellt eine einzelne Frage"""
        total = len(self.questions)
        print(f"📝 Frage {number}/{total}")
        print("-" * 30)
        print(f"{question['question']}")
        print()

        if question["type"] == "scale":
            for i, option in enumerate(question["options"], 1):
                print(f"{i}. {option}")
            print()

            while True:
                try:
                    choice = int(input("Ihre Wahl (Nummer): "))
                    if 1 <= choice <= len(question["options"]):
                        self.responses[question["id"]] = {
                            "choice": choice - 1,
                            "text": question["options"][choice - 1],
                            "points": question["points"][choice - 1],
                        }
                        break
                    else:
                        print(
                            f"Bitte geben Sie eine Zahl zwischen 1 und {len(question['options'])} ein."
                        )
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")

        elif question["type"] == "multiple_choice":
            for i, option in enumerate(question["options"], 1):
                print(f"{i}. {option}")
            print()

            while True:
                try:
                    choice = int(input("Ihre Wahl (Nummer): "))
                    if 1 <= choice <= len(question["options"]):
                        self.responses[question["id"]] = {
                            "choice": choice - 1,
                            "text": question["options"][choice - 1],
                            "points": question["points"][choice - 1],
                        }
                        break
                    else:
                        print(
                            f"Bitte geben Sie eine Zahl zwischen 1 und {len(question['options'])} ein."
                        )
                except ValueError:
                    print("Bitte geben Sie eine gültige Zahl ein.")

        elif question["type"] == "multiple_select":
            for i, option in enumerate(question["options"], 1):
                print(f"{i}. {option}")
            print()
            print("Geben Sie mehrere Zahlen durch Komma getrennt ein (z.B. 1,3,5)")
            print("oder eine einzelne Zahl:")

            while True:
                try:
                    user_input = input("Ihre Wahl(en): ").strip()
                    choices = [int(x.strip()) - 1 for x in user_input.split(",")]

                    if all(
                        0 <= choice < len(question["options"]) for choice in choices
                    ):
                        # Berechne Punkte für Mehrfachauswahl
                        total_points = 0
                        selected_texts = []

                        for choice in choices:
                            total_points += question["points_per_selection"][choice]
                            selected_texts.append(question["options"][choice])

                        # Begrenze auf Maximum
                        total_points = min(total_points, question["max_points"])

                        self.responses[question["id"]] = {
                            "choices": choices,
                            "texts": selected_texts,
                            "points": total_points,
                        }
                        break
                    else:
                        print(
                            f"Alle Zahlen müssen zwischen 1 und {len(question['options'])} liegen."
                        )
                except ValueError:
                    print("Bitte geben Sie gültige Zahlen ein (z.B. 1,2,3).")

        print()

    def _calculate_results(self) -> dict:
        """Berechnet die Assessment-Ergebnisse"""
        category_scores = {
            "array_basics": 0,
            "mathematical_operations": 0,
            "programming_practice": 0,
            "application_context": 0,
            "performance_awareness": 0,
        }

        category_weights = {
            "array_basics": 0.20,
            "mathematical_operations": 0.25,
            "programming_practice": 0.20,
            "application_context": 0.20,
            "performance_awareness": 0.15,
        }

        category_counts = dict.fromkeys(category_scores.keys(), 0)

        # Sammle Punkte pro Kategorie
        for question in self.questions:
            category = question["category"]
            question_id = question["id"]

            if question_id in self.responses:
                points = self.responses[question_id]["points"]
                category_scores[category] += points
                category_counts[category] += 1

        # Berechne Durchschnittswerte pro Kategorie (0-10 Skala)
        category_averages = {}
        for category in category_scores:
            if category_counts[category] > 0:
                category_averages[category] = (
                    category_scores[category] / category_counts[category]
                )
            else:
                category_averages[category] = 0

        # Berechne gewichteten Gesamtscore
        total_score = sum(
            category_averages[category] * category_weights[category] * 10
            for category in category_averages
        )

        # Bestimme Lernpfad
        learning_path = self._determine_learning_path(total_score, category_averages)

        return {
            "total_score": total_score,
            "category_scores": category_averages,
            "category_weights": category_weights,
            "learning_path": learning_path,
            "responses": self.responses,
            "timestamp": datetime.now().isoformat(),
        }

    def _determine_learning_path(
        self, total_score: float, category_scores: dict
    ) -> str:
        """Bestimmt den optimalen Lernpfad basierend auf den Scores"""
        # Basis-Einteilung nach Gesamtscore
        if total_score <= 35:
            base_level = "beginner"
        elif total_score <= 65:
            base_level = "intermediate"
        else:
            base_level = "advanced"

        # Anpassungen basierend auf spezifischen Kategorien
        array_score = category_scores.get("array_basics", 0)
        performance_score = category_scores.get("performance_awareness", 0)

        # Spezielle Regeln
        if array_score < 3 and base_level != "beginner":
            # Schwache Array-Grundlagen -> immer Beginner
            return "beginner"

        if array_score >= 8 and performance_score >= 7 and total_score > 55:
            # Starke Arrays + Performance -> mindestens Intermediate
            if base_level == "beginner":
                return "intermediate"

        return base_level

    def _display_results(self, results: dict):
        """Zeigt die Assessment-Ergebnisse an"""
        print("\n" + "🎯" * 20)
        print("🎯 ASSESSMENT-ERGEBNISSE 🎯")
        print("🎯" * 20)
        print()

        # Gesamtscore
        total_score = results["total_score"]
        print(f"📊 Gesamtscore: {total_score:.1f}/100 Punkte")
        print()

        # Kategorie-Scores
        print("📋 Detaillierte Bewertung:")
        print("-" * 40)

        category_names = {
            "array_basics": "Array-Grundlagen",
            "mathematical_operations": "Mathematische Operationen",
            "programming_practice": "Programmierpraxis",
            "application_context": "Anwendungskontext",
            "performance_awareness": "Performance-Bewusstsein",
        }

        for category, score in results["category_scores"].items():
            weight = results["category_weights"][category]
            weighted_contribution = score * weight * 10

            # Visual progress bar
            bar_length = 20
            filled_length = int(bar_length * score / 10)
            bar = "█" * filled_length + "░" * (bar_length - filled_length)

            print(
                f"{category_names[category]:<25} │{bar}│ {score:.1f}/10 ({weight * 100:.0f}%)"
            )

        print()

        # Lernpfad-Empfehlung
        learning_path = results["learning_path"]
        path_info = {
            "beginner": {
                "name": "🟢 Beginner-Pfad",
                "description": "NumPy-Grundlagen und erste Schritte",
                "duration": "20-30 Minuten pro Übung",
                "focus": "Array-Basics, einfache Operationen, Bystronic-Anwendungen",
            },
            "intermediate": {
                "name": "🟡 Intermediate-Pfad",
                "description": "Erweiterte NumPy-Funktionen und Anwendungen",
                "duration": "30-45 Minuten pro Übung",
                "focus": "Broadcasting, Statistik, lineare Algebra, SPC",
            },
            "advanced": {
                "name": "🔴 Advanced-Pfad",
                "description": "Performance-Optimierung und komplexe Anwendungen",
                "duration": "45-60 Minuten pro Übung",
                "focus": "Algorithmus-Optimierung, Enterprise-Analytics, GPU-Computing",
            },
        }

        path = path_info[learning_path]
        print("🎯 EMPFOHLENER LERNPFAD:")
        print("=" * 30)
        print(f"📚 {path['name']}")
        print(f"📝 {path['description']}")
        print(f"⏱️  Dauer: {path['duration']}")
        print(f"🎯 Fokus: {path['focus']}")
        print()

        # Nächste Schritte
        print("➡️ NÄCHSTE SCHRITTE:")
        print("-" * 20)
        if learning_path == "beginner":
            print("1. 📖 Theorie studieren: theory/03_numpy.ipynb")
            print("2. 💡 Beispiele ansehen: examples/arrays_basic.py")
            print(
                "3. 🎯 Übungen starten: exercises/beginner/uebung_01_arrays_beginner.py"
            )
            print("4. 🆘 Bei Problemen: solutions/beginner/uebung_01_hints.md")

        elif learning_path == "intermediate":
            print("1. 📖 Theorie auffrischen: theory/03_numpy.ipynb")
            print("2. 💡 Performance-Demo: examples/performance_comparison.py")
            print(
                "3. 🎯 Übungen starten: exercises/intermediate/uebung_01_arrays_intermediate.py"
            )
            print("4. 🆘 Bei Problemen: solutions/intermediate/uebung_01_hints.md")

        else:  # advanced
            print("1. 💡 Performance-Vergleiche: examples/performance_comparison.py")
            print(
                "2. 🎯 Direkt zu Übungen: exercises/advanced/uebung_01_performance_advanced.py"
            )
            print("3. 🆘 Bei Bedarf: solutions/advanced/uebung_01_hints.md")
            print("4. 🔗 Integration: Eigene Projekte mit NumPy")

        print()
        print("🎓 Viel Erfolg beim Lernen von NumPy!")

    def _save_results(self, results: dict):
        """Speichert die Assessment-Ergebnisse"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"numpy_assessment_result_{timestamp}.json"
        filepath = os.path.join(self.results_dir, filename)

        try:
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(results, f, indent=2, ensure_ascii=False)

            print(f"💾 Ergebnisse gespeichert: {filepath}")
            print()

        except Exception as e:
            print(f"⚠️  Warnung: Konnte Ergebnisse nicht speichern: {e}")


def main():
    """Hauptfunktion für das Assessment"""
    try:
        assessment = NumPyAssessment()
        results = assessment.run_assessment()

        print("=" * 50)
        print("📊 Assessment erfolgreich abgeschlossen!")
        print()
        print("Sie können nun mit Ihrem empfohlenen Lernpfad beginnen.")
        print("Bei Fragen oder Problemen nutzen Sie das 4-Stufen-Hilfesystem.")

    except KeyboardInterrupt:
        print("\n\n⚠️ Assessment abgebrochen.")
        print("Sie können es jederzeit neu starten mit:")
        print("uv run python src/03_numpy/assessments/learning_path_assessment.py")

    except Exception as e:
        print(f"\n❌ Fehler beim Assessment: {e}")
        print("Bitte versuchen Sie es erneut oder wenden Sie sich an den Support.")


if __name__ == "__main__":
    main()
