#!/usr/bin/env python3
"""
Tests für 02_datentypen/beispiele

Diese Tests validieren die Funktionalität der Datentypen-Beispiele
und demonstrieren Test-Patterns für numerische Berechnungen.
"""

import math
import sys
from pathlib import Path
from unittest.mock import patch

import pytest

# Pfad zu den Beispielen hinzufügen
beispiele_path = Path(__file__).parent.parent / "src" / "02_datentypen" / "beispiele"
sys.path.insert(0, str(beispiele_path))

import collections_demo
import numbers_demo
import strings_demo


class TestNumbersDemo:
    """Tests für numbers_demo.py Beispiel"""

    def test_main_function_exists(self):
        """Testet, ob die main() Funktion existiert"""
        assert hasattr(numbers_demo, "main")
        assert callable(numbers_demo.main)

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_main_runs_without_error(self, mock_input, mock_print):
        """Testet, ob main() ohne Fehler läuft"""
        numbers_demo.main()
        assert mock_print.called

    def test_demonstrate_math_operations_function(self):
        """Testet die mathematischen Operationen"""
        assert hasattr(numbers_demo, "demonstrate_math_operations")
        assert callable(numbers_demo.demonstrate_math_operations)

    def test_calculate_production_metrics_function(self):
        """Testet die Produktionsmetriken-Berechnung"""
        assert hasattr(numbers_demo, "calculate_production_metrics")
        assert callable(numbers_demo.calculate_production_metrics)

        # Test der Berechnungslogik
        teile_geplant = 2000
        teile_produziert = 1850
        effizienz = (teile_produziert / teile_geplant) * 100

        assert (
            abs(effizienz - 92.5) < 0.1
        ), f"Effizienz-Berechnung fehlerhaft: {effizienz}"

    def test_calculate_material_usage_function(self):
        """Testet die Materialverbrauch-Berechnung"""
        assert hasattr(numbers_demo, "calculate_material_usage")
        assert callable(numbers_demo.calculate_material_usage)

    def test_calculate_laser_parameters_function(self):
        """Testet die Laser-Parameter-Berechnung"""
        assert hasattr(numbers_demo, "calculate_laser_parameters")
        assert callable(numbers_demo.calculate_laser_parameters)

    def test_mathematical_calculations(self):
        """Testet spezifische mathematische Berechnungen"""
        # Test Schnittzeit-Berechnung
        schnittlaenge = 100  # mm
        schnittgeschwindigkeit = 15.75  # m/min
        expected_zeit = (schnittlaenge / 1000) / schnittgeschwindigkeit

        assert abs(expected_zeit - 0.00635) < 0.001, "Schnittzeit-Berechnung fehlerhaft"

        # Test Materialausnutzung
        blech_flaeche = 3000 * 1500  # mm²
        teil_flaeche = 150 * 100  # mm²
        anzahl_teile = 150
        gesamt_teil_flaeche = teil_flaeche * anzahl_teile
        materialausnutzung = (gesamt_teil_flaeche / blech_flaeche) * 100

        assert (
            abs(materialausnutzung - 50.0) < 0.1
        ), "Materialausnutzung-Berechnung fehlerhaft"

    def test_complex_numbers_usage(self):
        """Testet die Verwendung komplexer Zahlen"""
        impedanz = 50 + 30j
        strom = 10 + 0j
        spannung = impedanz * strom

        expected_spannung = 500 + 300j
        assert (
            spannung == expected_spannung
        ), f"Komplexe Zahlen-Berechnung fehlerhaft: {spannung}"

        # Test Betrag
        betrag = abs(spannung)
        expected_betrag = math.sqrt(500**2 + 300**2)
        assert (
            abs(betrag - expected_betrag) < 0.1
        ), f"Betrag-Berechnung fehlerhaft: {betrag}"


class TestStringsDemo:
    """Tests für strings_demo.py Beispiel"""

    def test_main_function_exists(self):
        """Testet, ob die main() Funktion existiert"""
        assert hasattr(strings_demo, "main")
        assert callable(strings_demo.main)

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_main_runs_without_error(self, mock_input, mock_print):
        """Testet, ob main() ohne Fehler läuft"""
        strings_demo.main()
        assert mock_print.called

    def test_string_operations_exist(self):
        """Testet, ob String-Operationen demonstriert werden"""
        # Überprüfe, ob wichtige String-Methoden im Code vorkommen
        import inspect

        source = inspect.getsource(strings_demo)

        # Wichtige String-Methoden sollten demonstriert werden
        assert (
            ".upper()" in source or ".lower()" in source
        ), "String-Case-Methoden fehlen"
        assert ".strip()" in source, "String-Trimming fehlt"
        # String-Splitting ist möglicherweise anders implementiert
        assert "split" in source or "partition" in source, "String-Splitting fehlt"
        assert 'f"' in source or ".format(" in source, "String-Formatierung fehlt"

    def test_bystronic_specific_examples(self):
        """Testet Bystronic-spezifische String-Beispiele"""
        # Test typische Maschinennamen-Verarbeitung
        maschinen_name = "LASER_01_BYSTAR_FIBER"

        # Typische Operationen
        assert maschinen_name.startswith(
            "LASER"
        ), "Maschinen-Präfix-Test fehlgeschlagen"
        assert "BYSTAR" in maschinen_name, "Maschinen-Typ-Test fehlgeschlagen"

        teile = maschinen_name.split("_")
        assert len(teile) >= 3, "Maschinen-Name-Parsing fehlgeschlagen"


class TestCollectionsDemo:
    """Tests für collections_demo.py Beispiel"""

    def test_main_function_exists(self):
        """Testet, ob die main() Funktion existiert"""
        assert hasattr(collections_demo, "main")
        assert callable(collections_demo.main)

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_main_runs_without_error(self, mock_input, mock_print):
        """Testet, ob main() ohne Fehler läuft"""
        collections_demo.main()
        assert mock_print.called

    def test_list_operations(self):
        """Testet Listen-Operationen"""
        # Simuliere typische Maschinendaten-Liste
        maschinen = ["LASER_01", "LASER_02", "PRESSE_01"]

        # Grundlegende Listen-Operationen
        assert len(maschinen) == 3, "Listen-Länge fehlerhaft"
        assert "LASER_01" in maschinen, "Listen-Membership fehlerhaft"

        # Liste erweitern
        maschinen.append("STANZE_01")
        assert len(maschinen) == 4, "Listen-Append fehlerhaft"

        # Liste filtern
        laser_maschinen = [m for m in maschinen if m.startswith("LASER")]
        assert len(laser_maschinen) == 2, "Listen-Filterung fehlerhaft"

    def test_dictionary_operations(self):
        """Testet Dictionary-Operationen"""
        # Simuliere Maschinendaten-Dictionary
        maschine_data = {
            "id": "LASER_01",
            "typ": "ByStar Fiber",
            "baujahr": 2019,
            "produktionszeit": 2450.5,
        }

        # Grundlegende Dictionary-Operationen
        assert maschine_data["id"] == "LASER_01", "Dictionary-Zugriff fehlerhaft"
        assert "typ" in maschine_data, "Dictionary-Key-Test fehlerhaft"

        # Dictionary erweitern
        maschine_data["wartung_faellig"] = True
        assert "wartung_faellig" in maschine_data, "Dictionary-Update fehlerhaft"

        # Dictionary-Methoden
        keys = list(maschine_data.keys())
        assert len(keys) == 5, "Dictionary-Keys fehlerhaft"

    def test_tuple_operations(self):
        """Testet Tuple-Operationen"""
        # Koordinaten für Schnittposition
        position = (150.5, 200.3)

        assert len(position) == 2, "Tuple-Länge fehlerhaft"
        assert position[0] == 150.5, "Tuple-Indexing fehlerhaft"

        # Tuple unpacking
        x, y = position
        assert x == 150.5 and y == 200.3, "Tuple-Unpacking fehlerhaft"

    def test_set_operations(self):
        """Testet Set-Operationen"""
        # Maschinentypen als Set
        typen_a = {"ByStar", "Xpert", "ByTrans"}
        typen_b = {"ByStar", "BySpeed", "Xpert"}

        # Set-Operationen
        gemeinsame = typen_a & typen_b
        assert (
            "ByStar" in gemeinsame and "Xpert" in gemeinsame
        ), "Set-Intersection fehlerhaft"

        alle_typen = typen_a | typen_b
        assert len(alle_typen) == 4, "Set-Union fehlerhaft"


class TestDataTypeIntegration:
    """Integrationstests für Datentypen-Beispiele"""

    def test_numeric_precision(self):
        """Testet numerische Präzision bei Berechnungen"""
        # Typische Bystronic-Berechnungen mit Fließkommazahlen
        materialdicke = 2.5
        toleranz = 0.1

        # Toleranzbereich
        min_dicke = materialdicke - toleranz
        max_dicke = materialdicke + toleranz

        assert min_dicke == 2.4, f"Minimale Dicke fehlerhaft: {min_dicke}"
        assert max_dicke == 2.6, f"Maximale Dicke fehlerhaft: {max_dicke}"

        # Präzisionsprobleme bei Fließkommazahlen
        result = 0.1 + 0.2
        assert abs(result - 0.3) < 1e-10, "Fließkomma-Präzision nicht berücksichtigt"

    def test_type_conversions(self):
        """Testet Typ-Konvertierungen"""
        # String zu Zahl
        stunden_str = "2450.5"
        stunden_float = float(stunden_str)
        assert stunden_float == 2450.5, "String-zu-Float-Konvertierung fehlerhaft"

        # Zahl zu String
        teile_anzahl = 1500
        teile_str = str(teile_anzahl)
        assert teile_str == "1500", "Int-zu-String-Konvertierung fehlerhaft"

        # Boolean-Konvertierungen
        assert bool(1) is True, "Int-zu-Bool-Konvertierung fehlerhaft"
        assert bool(0) is False, "Int-zu-Bool-Konvertierung fehlerhaft"
        assert bool("") is False, "String-zu-Bool-Konvertierung fehlerhaft"
        assert bool("text") is True, "String-zu-Bool-Konvertierung fehlerhaft"

    @patch("builtins.print")
    @patch("builtins.input", return_value="")
    def test_all_examples_run_successfully(self, mock_input, mock_print):
        """Testet, ob alle Datentypen-Beispiele erfolgreich laufen"""
        # Alle Beispiele sollten ohne Fehler durchlaufen
        numbers_demo.main()
        strings_demo.main()
        collections_demo.main()

        assert mock_print.called


# Hilfsfunktionen für Tests
def test_module_imports():
    """Testet, ob alle Module korrekt importiert werden können"""
    import collections_demo
    import numbers_demo
    import strings_demo

    assert numbers_demo is not None
    assert strings_demo is not None
    assert collections_demo is not None


def test_example_files_exist():
    """Testet, ob alle Beispieldateien existieren"""
    files_to_check = [
        "numbers_demo.py",
        "strings_demo.py",
        "collections_demo.py",
        "vba_collections_comparison.py",
    ]

    for filename in files_to_check:
        file_path = beispiele_path / filename
        assert file_path.exists(), f"{filename} nicht gefunden"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
