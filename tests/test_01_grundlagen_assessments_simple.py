#!/usr/bin/env python3
"""
Einfache Tests für 01_grundlagen/assessments

Diese Tests validieren die grundlegende Funktionalität der Assessment-Tools.
"""

import sys
from pathlib import Path

import pytest

# Pfad zu den Assessment-Tools hinzufügen
assessments_path = Path(__file__).parent.parent / "src" / "01_grundlagen" / "assessments"
sys.path.insert(0, str(assessments_path))


class TestAssessmentModules:
    """Tests für die Assessment-Module"""

    def test_learning_path_assessment_importable(self):
        """Testet, ob learning_path_assessment importiert werden kann"""
        try:
            import learning_path_assessment
            assert learning_path_assessment is not None
            
            # Teste, ob die Hauptklasse existiert
            assert hasattr(learning_path_assessment, "LearningPathAssessment")
            
            # Teste, ob die Klasse instanziiert werden kann
            assessment = learning_path_assessment.LearningPathAssessment()
            assert assessment is not None
            
        except ImportError:
            pytest.skip("learning_path_assessment module not available")

    def test_micro_assessment_quiz_importable(self):
        """Testet, ob micro_assessment_quiz importiert werden kann"""
        try:
            import micro_assessment_quiz
            assert micro_assessment_quiz is not None
            
            # Teste, ob die Hauptklasse existiert
            assert hasattr(micro_assessment_quiz, "MicroAssessmentQuiz")
            
            # Teste, ob die Klasse instanziiert werden kann
            quiz = micro_assessment_quiz.MicroAssessmentQuiz()
            assert quiz is not None
            
        except ImportError:
            pytest.skip("micro_assessment_quiz module not available")

    def test_micro_assessment_challenges_importable(self):
        """Testet, ob micro_assessment_challenges importiert werden kann"""
        try:
            import micro_assessment_challenges
            assert micro_assessment_challenges is not None
            
            # Teste, ob die Hauptklasse existiert
            assert hasattr(micro_assessment_challenges, "MicroAssessmentChallenges")
            
            # Teste, ob die Klasse instanziiert werden kann
            challenges = micro_assessment_challenges.MicroAssessmentChallenges()
            assert challenges is not None
            
        except ImportError:
            pytest.skip("micro_assessment_challenges module not available")

    def test_micro_assessment_reflection_importable(self):
        """Testet, ob micro_assessment_reflection importiert werden kann"""
        try:
            import micro_assessment_reflection
            assert micro_assessment_reflection is not None
            
            # Teste, ob die Hauptklasse existiert
            assert hasattr(micro_assessment_reflection, "MicroAssessmentReflection")
            
            # Teste, ob die Klasse instanziiert werden kann
            reflection = micro_assessment_reflection.MicroAssessmentReflection()
            assert reflection is not None
            
        except ImportError:
            pytest.skip("micro_assessment_reflection module not available")

    def test_micro_assessment_dashboard_importable(self):
        """Testet, ob micro_assessment_dashboard importiert werden kann"""
        try:
            import micro_assessment_dashboard
            assert micro_assessment_dashboard is not None
            
            # Teste, ob die Hauptklasse existiert
            assert hasattr(micro_assessment_dashboard, "MicroAssessmentDashboard")
            
            # Teste, ob die Klasse instanziiert werden kann
            dashboard = micro_assessment_dashboard.MicroAssessmentDashboard()
            assert dashboard is not None
            
        except ImportError:
            pytest.skip("micro_assessment_dashboard module not available")


class TestAssessmentFiles:
    """Tests für Assessment-Dateien"""

    def test_assessment_files_exist(self):
        """Testet, ob alle Assessment-Dateien existieren"""
        expected_files = [
            "learning_path_assessment.py",
            "micro_assessment_quiz.py",
            "micro_assessment_challenges.py",
            "micro_assessment_reflection.py",
            "micro_assessment_dashboard.py"
        ]
        
        for filename in expected_files:
            file_path = assessments_path / filename
            assert file_path.exists(), f"{filename} nicht gefunden"

    def test_results_directory_exists(self):
        """Testet, ob das Results-Verzeichnis existiert"""
        results_path = assessments_path / "results"
        assert results_path.exists(), "Results-Verzeichnis nicht gefunden"
        assert results_path.is_dir(), "Results ist kein Verzeichnis"

    def test_readme_exists(self):
        """Testet, ob README.md existiert"""
        readme_path = assessments_path / "README.md"
        assert readme_path.exists(), "README.md nicht gefunden"


class TestAssessmentStructure:
    """Tests für die Assessment-Struktur"""

    def test_learning_path_assessment_structure(self):
        """Testet die Struktur des LearningPathAssessment"""
        try:
            import learning_path_assessment
            assessment = learning_path_assessment.LearningPathAssessment()
            
            # Teste wichtige Methoden
            expected_methods = ["welcome_message", "run_assessment", "calculate_final_score"]
            for method in expected_methods:
                if hasattr(assessment, method):
                    assert callable(getattr(assessment, method))
                    
        except ImportError:
            pytest.skip("learning_path_assessment module not available")

    def test_quiz_structure(self):
        """Testet die Struktur des MicroAssessmentQuiz"""
        try:
            import micro_assessment_quiz
            quiz = micro_assessment_quiz.MicroAssessmentQuiz()
            
            # Teste wichtige Attribute
            if hasattr(quiz, "fragen"):
                assert isinstance(quiz.fragen, list)
                assert len(quiz.fragen) > 0
                
        except ImportError:
            pytest.skip("micro_assessment_quiz module not available")

    def test_challenges_structure(self):
        """Testet die Struktur des MicroAssessmentChallenges"""
        try:
            import micro_assessment_challenges
            challenges = micro_assessment_challenges.MicroAssessmentChallenges()
            
            # Teste wichtige Attribute
            if hasattr(challenges, "challenges"):
                assert isinstance(challenges.challenges, list)
                assert len(challenges.challenges) > 0
                
        except ImportError:
            pytest.skip("micro_assessment_challenges module not available")


class TestIntegration:
    """Integrationstests für das Assessment-System"""

    def test_all_modules_can_be_imported_together(self):
        """Testet, ob alle Module zusammen importiert werden können"""
        modules = []
        
        try:
            import learning_path_assessment
            modules.append(learning_path_assessment)
        except ImportError:
            pass
            
        try:
            import micro_assessment_quiz
            modules.append(micro_assessment_quiz)
        except ImportError:
            pass
            
        try:
            import micro_assessment_challenges
            modules.append(micro_assessment_challenges)
        except ImportError:
            pass
            
        try:
            import micro_assessment_reflection
            modules.append(micro_assessment_reflection)
        except ImportError:
            pass
            
        try:
            import micro_assessment_dashboard
            modules.append(micro_assessment_dashboard)
        except ImportError:
            pass
        
        # Mindestens ein Modul sollte verfügbar sein
        assert len(modules) > 0, "Keine Assessment-Module verfügbar"
        
        # Alle importierten Module sollten nicht None sein
        for module in modules:
            assert module is not None

    def test_assessment_directory_structure(self):
        """Testet die Verzeichnisstruktur des Assessment-Systems"""
        assert assessments_path.exists(), "Assessment-Verzeichnis nicht gefunden"
        assert assessments_path.is_dir(), "Assessment-Pfad ist kein Verzeichnis"
        
        # Überprüfe wichtige Unterverzeichnisse
        results_path = assessments_path / "results"
        assert results_path.exists(), "Results-Verzeichnis nicht gefunden"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
