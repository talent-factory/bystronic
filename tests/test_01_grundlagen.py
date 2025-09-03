#!/usr/bin/env python3
"""
Tests für 01_grundlagen/beispiele

Diese Tests validieren die Funktionalität der Grundlagen-Beispiele
und demonstrieren Test-Patterns für Python-Anfänger.
"""

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Pfad zu den Beispielen hinzufügen
beispiele_path = Path(__file__).parent.parent / "src" / "01_grundlagen" / "beispiele"
sys.path.insert(0, str(beispiele_path))

import hello_world
import vba_vs_python


class TestHelloWorld:
    """Tests für hello_world.py Beispiel"""

    def test_main_function_exists(self):
        """Testet, ob die main() Funktion existiert"""
        assert hasattr(hello_world, 'main')
        assert callable(hello_world.main)

    @patch('builtins.input', return_value='Test User')
    @patch('builtins.print')
    def test_main_function_runs_without_error(self, mock_print, mock_input):
        """Testet, ob main() ohne Fehler ausgeführt wird"""
        # Sollte keine Exception werfen
        hello_world.main()

        # Überprüft, ob print aufgerufen wurde
        assert mock_print.called

        # Überprüft, ob input aufgerufen wurde
        assert mock_input.called

    @patch('builtins.input', return_value='Bystronic Entwickler')
    @patch('builtins.print')
    def test_string_formatting_output(self, mock_print, mock_input):
        """Testet die String-Formatierung in der Ausgabe"""
        hello_world.main()

        # Sammle alle print-Aufrufe
        print_calls = [call[0][0] for call in mock_print.call_args_list]

        # Überprüfe, ob bestimmte Ausgaben vorhanden sind
        welcome_found = any("Willkommen bei Python!" in call for call in print_calls)
        assert welcome_found, "Willkommensnachricht nicht gefunden"

        # Überprüfe f-string Verwendung
        greeting_found = any("Hallo Bystronic Entwickler!" in call for call in print_calls)
        assert greeting_found, "Personalisierte Begrüßung nicht gefunden"

    def test_calculation_logic(self):
        """Testet die Berechnungslogik für Arbeitsstunden"""
        # Simuliere die Berechnung aus dem Beispiel
        stunden_pro_tag = 8
        tage_pro_woche = 5
        wochen_im_jahr = 52

        expected_stunden = stunden_pro_tag * tage_pro_woche * wochen_im_jahr
        assert expected_stunden == 2080, f"Erwartete 2080 Stunden, bekommen {expected_stunden}"


class TestVbaVsPython:
    """Tests für vba_vs_python.py Beispiel"""

    def test_main_function_exists(self):
        """Testet, ob die main() Funktion existiert"""
        assert hasattr(vba_vs_python, 'main')
        assert callable(vba_vs_python.main)

    @patch('builtins.print')
    def test_main_runs_without_error(self, mock_print):
        """Testet, ob main() ohne Fehler läuft"""
        vba_vs_python.main()
        assert mock_print.called

    def test_demonstriere_listen_function_exists(self):
        """Testet, ob demonstriere_listen Funktion existiert"""
        assert hasattr(vba_vs_python, 'demonstriere_listen')
        assert callable(vba_vs_python.demonstriere_listen)

    def test_demonstriere_dictionaries_function_exists(self):
        """Testet, ob demonstriere_dictionaries Funktion existiert"""
        assert hasattr(vba_vs_python, 'demonstriere_dictionaries')
        assert callable(vba_vs_python.demonstriere_dictionaries)

    def test_list_operations_logic(self):
        """Testet grundlegende Listen-Operationen aus dem Beispiel"""
        # Simuliere die Listen-Operationen aus dem Beispiel
        zahlen = [1, 2, 3, 4, 5]
        zahlen.append(6)
        zahlen.extend([7, 8, 9])

        assert len(zahlen) == 9, "Listen-Erweiterung fehlerhaft"

        # List Comprehensions
        quadrate = [x**2 for x in zahlen]
        assert quadrate[0] == 1 and quadrate[1] == 4, "List Comprehension fehlerhaft"

        # Filtern
        gerade = [x for x in zahlen if x % 2 == 0]
        ungerade = [x for x in zahlen if x % 2 == 1]

        assert len(gerade) + len(ungerade) == len(zahlen), "Filterung fehlerhaft"

    def test_mathematical_operations(self):
        """Testet mathematische Operationen mit Listen"""
        zahlen = [1, 2, 3, 4, 5]

        summe = sum(zahlen)
        durchschnitt = sum(zahlen) / len(zahlen)
        maximum = max(zahlen)
        minimum = min(zahlen)

        assert summe == 15, f"Summe fehlerhaft: {summe}"
        assert durchschnitt == 3.0, f"Durchschnitt fehlerhaft: {durchschnitt}"
        assert maximum == 5, f"Maximum fehlerhaft: {maximum}"
        assert minimum == 1, f"Minimum fehlerhaft: {minimum}"


class TestIntegration:
    """Integrationstests für das gesamte Grundlagen-Modul"""

    @patch('builtins.input', return_value='Test')
    @patch('builtins.print')
    def test_all_examples_run_successfully(self, mock_print, mock_input):
        """Testet, ob alle Beispiele erfolgreich ausgeführt werden können"""
        # Test hello_world
        hello_world.main()

        # Test vba_vs_python
        vba_vs_python.main()

        # Beide sollten ohne Fehler durchlaufen
        assert mock_print.called

    def test_educational_concepts_coverage(self):
        """Testet, ob wichtige Lernkonzepte abgedeckt sind"""
        # Überprüfe, ob wichtige Python-Konzepte in den Beispielen vorkommen

        # String-Formatierung
        assert hasattr(hello_world, 'main'), "String-Formatierung Beispiel fehlt"

        # Funktionen und Listen-Operationen
        assert hasattr(vba_vs_python, 'demonstriere_listen'), "Listen-Beispiel fehlt"

        # Dictionary-Operationen
        assert hasattr(vba_vs_python, 'demonstriere_dictionaries'), "Dictionary-Beispiel fehlt"


# Hilfsfunktionen für Tests
def test_module_imports():
    """Testet, ob alle Module korrekt importiert werden können"""
    import hello_world
    import vba_vs_python

    assert hello_world is not None
    assert vba_vs_python is not None


def test_example_files_exist():
    """Testet, ob alle Beispieldateien existieren"""
    hello_world_path = beispiele_path / "hello_world.py"
    vba_vs_python_path = beispiele_path / "vba_vs_python.py"

    assert hello_world_path.exists(), "hello_world.py nicht gefunden"
    assert vba_vs_python_path.exists(), "vba_vs_python.py nicht gefunden"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
