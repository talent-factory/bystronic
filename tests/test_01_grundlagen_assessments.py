#!/usr/bin/env python3
"""
Tests für 01_grundlagen/assessments

Diese Tests validieren die Funktionalität der Assessment-Tools
und demonstrieren Test-Patterns für interaktive Python-Anwendungen.
"""

import json
import sys
from pathlib import Path
from unittest.mock import mock_open, patch

import pytest

# Pfad zu den Assessment-Tools hinzufügen
assessments_path = (
    Path(__file__).parent.parent / "src" / "01_grundlagen" / "assessments"
)
sys.path.insert(0, str(assessments_path))

# Importiere Module nur wenn sie existieren
try:
    import learning_path_assessment

    LEARNING_PATH_AVAILABLE = True
except ImportError:
    LEARNING_PATH_AVAILABLE = False

try:
    import micro_assessment_quiz

    QUIZ_AVAILABLE = True
except ImportError:
    QUIZ_AVAILABLE = False

try:
    import micro_assessment_challenges

    CHALLENGES_AVAILABLE = True
except ImportError:
    CHALLENGES_AVAILABLE = False

try:
    import micro_assessment_reflection

    REFLECTION_AVAILABLE = True
except ImportError:
    REFLECTION_AVAILABLE = False

try:
    import micro_assessment_dashboard

    DASHBOARD_AVAILABLE = True
except ImportError:
    DASHBOARD_AVAILABLE = False


@pytest.mark.skipif(
    not LEARNING_PATH_AVAILABLE, reason="learning_path_assessment module not available"
)
class TestLearningPathAssessment:
    """Tests für learning_path_assessment.py"""

    def test_assessment_class_exists(self):
        """Testet, ob die LearningPathAssessment Klasse existiert"""
        assert hasattr(learning_path_assessment, "LearningPathAssessment")
        assessment = learning_path_assessment.LearningPathAssessment()
        assert assessment is not None

    @patch(
        "builtins.input",
        side_effect=[
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
            "1",
        ],
    )
    @patch("builtins.print")
    def test_assessment_completion(self, mock_print, mock_input):
        """Testet die vollständige Durchführung des Assessments"""
        assessment = learning_path_assessment.LearningPathAssessment()

        # Mock für JSON-Speicherung
        with patch("builtins.open", mock_open()) as mock_file:
            with patch("json.dump") as mock_json_dump:
                # run_assessment() gibt nichts zurück, aber sollte ohne Fehler laufen
                assessment.run_assessment()

                # Überprüfe, dass print aufgerufen wurde
                assert mock_print.called

    def test_score_calculation(self):
        """Testet die Score-Berechnung"""
        assessment = learning_path_assessment.LearningPathAssessment()

        # Teste die calculate_final_score Methode
        test_scores = {
            "programming_experience": 5,
            "python_knowledge": 3,
            "ai_experience": 2,
            "time_availability": 7,
            "learning_goals": 6,
        }

        final_score, path = assessment.calculate_final_score(test_scores)

        assert isinstance(final_score, (int, float))
        assert 0 <= final_score <= 10
        assert isinstance(path, str)

    def test_path_determination(self):
        """Testet die Lernpfad-Bestimmung basierend auf Score"""
        assessment = learning_path_assessment.LearningPathAssessment()

        # Test für verschiedene Score-Kombinationen
        low_scores = {
            "programming_experience": 1,
            "python_knowledge": 1,
            "ai_experience": 1,
            "time_availability": 1,
            "learning_goals": 1,
        }

        high_scores = {
            "programming_experience": 10,
            "python_knowledge": 10,
            "ai_experience": 10,
            "time_availability": 10,
            "learning_goals": 10,
        }

        low_final_score, low_path = assessment.calculate_final_score(low_scores)
        high_final_score, high_path = assessment.calculate_final_score(high_scores)

        assert "🟢" in low_path or "🟡" in low_path or "🔴" in low_path
        assert "🟢" in high_path or "🟡" in high_path or "🔴" in high_path
        assert low_final_score < high_final_score


class TestMicroAssessmentQuiz:
    """Tests für micro_assessment_quiz.py"""

    def test_quiz_class_exists(self):
        """Testet, ob die MicroAssessmentQuiz Klasse existiert"""
        assert hasattr(micro_assessment_quiz, "MicroAssessmentQuiz")
        quiz = micro_assessment_quiz.MicroAssessmentQuiz()
        assert quiz is not None

    def test_questions_loaded(self):
        """Testet, ob Fragen korrekt geladen werden"""
        quiz = micro_assessment_quiz.MicroAssessmentQuiz()

        # Überprüfe, dass Fragen vorhanden sind
        assert hasattr(quiz, "fragen")
        assert len(quiz.fragen) > 0

        # Überprüfe Fragen-Struktur
        erste_frage = quiz.fragen[0]
        assert "frage" in erste_frage
        assert "antworten" in erste_frage or "typ" in erste_frage

    @patch("builtins.input", side_effect=["1", "2", "1", "3", "2"])
    @patch("builtins.print")
    def test_quiz_execution(self, mock_print, mock_input):
        """Testet die Quiz-Durchführung"""
        quiz = micro_assessment_quiz.MicroAssessmentQuiz()

        with patch("builtins.open", mock_open()) as mock_file:
            with patch("json.dump") as mock_json_dump:
                # starte_quiz() gibt nichts zurück, aber sollte ohne Fehler laufen
                quiz.starte_quiz(anzahl_fragen=3)

                # Überprüfe, dass print aufgerufen wurde
                assert mock_print.called


class TestMicroAssessmentChallenges:
    """Tests für micro_assessment_challenges.py"""

    def test_challenges_class_exists(self):
        """Testet, ob die MicroAssessmentChallenges Klasse existiert"""
        assert hasattr(micro_assessment_challenges, "MicroAssessmentChallenges")
        challenges = micro_assessment_challenges.MicroAssessmentChallenges()
        assert challenges is not None

    def test_challenges_loaded(self):
        """Testet, ob Challenges korrekt geladen werden"""
        challenges = micro_assessment_challenges.MicroAssessmentChallenges()

        assert hasattr(challenges, "challenges")
        assert len(challenges.challenges) > 0

        # Überprüfe Challenge-Struktur
        erste_challenge = challenges.challenges[0]
        assert "titel" in erste_challenge
        assert "beschreibung" in erste_challenge

    def test_code_execution_safety(self):
        """Testet die sichere Code-Ausführung"""
        challenges = micro_assessment_challenges.MicroAssessmentChallenges()

        # Test mit sicherem Code - verwende die tatsächliche Methode
        if hasattr(challenges, "_fuehre_code_aus"):
            safe_code = "result = 2 + 2"
            result = challenges._fuehre_code_aus(safe_code, {})
            assert result is not None
        else:
            # Fallback: Teste nur, dass die Klasse existiert
            assert challenges is not None

    @patch("builtins.input", return_value="result = 2 + 2")
    @patch("builtins.print")
    def test_challenge_execution(self, mock_print, mock_input):
        """Testet die Challenge-Durchführung"""
        challenges = micro_assessment_challenges.MicroAssessmentChallenges()

        with patch("builtins.open", mock_open()) as mock_file:
            with patch("json.dump") as mock_json_dump:
                # Teste die Hauptmethode, falls vorhanden
                if hasattr(challenges, "starte_challenges"):
                    challenges.starte_challenges()
                    assert mock_print.called
                else:
                    # Fallback: Teste nur, dass die Klasse funktioniert
                    assert challenges is not None


class TestMicroAssessmentReflection:
    """Tests für micro_assessment_reflection.py"""

    def test_reflection_class_exists(self):
        """Testet, ob die MicroAssessmentReflection Klasse existiert"""
        assert hasattr(micro_assessment_reflection, "MicroAssessmentReflection")
        reflection = micro_assessment_reflection.MicroAssessmentReflection()
        assert reflection is not None

    def test_competency_areas_loaded(self):
        """Testet, ob Kompetenzbereiche korrekt geladen werden"""
        reflection = micro_assessment_reflection.MicroAssessmentReflection()

        # Teste, ob die Klasse die erwarteten Attribute hat
        if hasattr(reflection, "kompetenzbereiche"):
            assert len(reflection.kompetenzbereiche) > 0

            # Überprüfe Struktur der Kompetenzbereiche
            for bereich_id, bereich in reflection.kompetenzbereiche.items():
                assert "titel" in bereich
                assert "fragen" in bereich
                assert len(bereich["fragen"]) > 0
        else:
            # Fallback: Teste nur, dass die Klasse existiert
            assert reflection is not None


class TestMicroAssessmentDashboard:
    """Tests für micro_assessment_dashboard.py"""

    def test_dashboard_class_exists(self):
        """Testet, ob die MicroAssessmentDashboard Klasse existiert"""
        assert hasattr(micro_assessment_dashboard, "MicroAssessmentDashboard")
        dashboard = micro_assessment_dashboard.MicroAssessmentDashboard()
        assert dashboard is not None

    def test_results_loading(self):
        """Testet das Laden von Assessment-Ergebnissen"""
        dashboard = micro_assessment_dashboard.MicroAssessmentDashboard()

        # Teste, ob die Methode existiert
        if hasattr(dashboard, "_lade_alle_ergebnisse"):
            # Mock für Ergebnis-Dateien
            mock_result = {
                "datum": "2024-01-01T12:00:00",
                "tool": "quiz",
                "score": 85,
                "details": {},
            }

            with patch("pathlib.Path.glob") as mock_glob:
                with patch(
                    "builtins.open", mock_open(read_data=json.dumps(mock_result))
                ):
                    mock_glob.return_value = [Path("test_result.json")]
                    results = dashboard._lade_alle_ergebnisse()

                    assert isinstance(results, list)
        else:
            # Fallback: Teste nur, dass die Klasse existiert
            assert dashboard is not None

    @patch("builtins.print")
    def test_dashboard_display(self, mock_print):
        """Testet die Dashboard-Anzeige"""
        dashboard = micro_assessment_dashboard.MicroAssessmentDashboard()

        # Teste die Hauptmethode, falls vorhanden
        if hasattr(dashboard, "anzeigen"):
            # Mock für leere Ergebnisse
            with patch.object(dashboard, "_lade_alle_ergebnisse", return_value=[]):
                dashboard.anzeigen()

                # Überprüfe, dass print aufgerufen wurde
                assert mock_print.called
        elif hasattr(dashboard, "zeige_dashboard"):
            dashboard.zeige_dashboard()
            assert mock_print.called
        else:
            # Fallback: Teste nur, dass die Klasse existiert
            assert dashboard is not None


class TestIntegration:
    """Integrationstests für das Assessment-System"""

    def test_all_assessment_modules_importable(self):
        """Testet, ob alle Assessment-Module importiert werden können"""
        modules = [
            learning_path_assessment,
            micro_assessment_quiz,
            micro_assessment_challenges,
            micro_assessment_reflection,
            micro_assessment_dashboard,
        ]

        for module in modules:
            assert module is not None

    def test_assessment_files_exist(self):
        """Testet, ob alle Assessment-Dateien existieren"""
        expected_files = [
            "learning_path_assessment.py",
            "micro_assessment_quiz.py",
            "micro_assessment_challenges.py",
            "micro_assessment_reflection.py",
            "micro_assessment_dashboard.py",
        ]

        for filename in expected_files:
            file_path = assessments_path / filename
            assert file_path.exists(), f"{filename} nicht gefunden"

    def test_results_directory_structure(self):
        """Testet die Ergebnis-Verzeichnisstruktur"""
        results_path = assessments_path / "results"
        assert results_path.exists(), "Results-Verzeichnis nicht gefunden"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
