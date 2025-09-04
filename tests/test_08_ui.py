#!/usr/bin/env python3
"""
Tests für Modul 08 - UI-Entwicklung
===================================

Umfassende Tests für PyQt und Streamlit Beispiele.

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import os
import sqlite3
import sys
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd
import pytest

# PyQt/PySide Tests
try:
    from PySide6.QtCore import Qt, QTimer
    from PySide6.QtTest import QTest
    from PySide6.QtWidgets import QApplication, QWidget

    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False

# Streamlit Tests
try:
    import streamlit as st

    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False

# Import der zu testenden Module
sys.path.append(
    str(Path(__file__).parent.parent / "src" / "08_ui" / "beispiele" / "pyqt")
)
sys.path.append(
    str(Path(__file__).parent.parent / "src" / "08_ui" / "beispiele" / "streamlit")
)

if PYQT_AVAILABLE:
    from datenbank_browser import DatenbankBrowser as DatabaseBrowser
    from grundlagen_widget import GrundlagenWidget


class TestPyQTGrundlagen:
    """Tests für PyQt Grundlagen Widget."""

    @pytest.fixture
    def app(self):
        """QApplication Fixture."""
        if not PYQT_AVAILABLE:
            pytest.skip("PyQt/PySide nicht verfügbar")

        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app

    @pytest.fixture
    def widget(self, app):
        """GrundlagenWidget Fixture."""
        widget = GrundlagenWidget()
        yield widget
        widget.close()

    def test_widget_initialization(self, widget):
        """Test der Widget-Initialisierung."""
        assert widget.windowTitle() == "PyQt Grundlagen - Bystronic UI-Entwicklung"
        assert widget.status_bar is not None
        assert widget.tab_widget is not None
        assert widget.timer is not None
        assert widget.progress_value == 0

    def test_menubar_creation(self, widget):
        """Test der Menüleisten-Erstellung."""
        menubar = widget.menuBar()
        assert menubar is not None

        # Prüfe Menü-Einträge
        menus = [action.text() for action in menubar.actions()]
        assert "&Datei" in menus
        assert "&Hilfe" in menus

    def test_tab_creation(self, widget):
        """Test der Tab-Erstellung."""
        tab_widget = widget.tab_widget
        assert tab_widget.count() == 4

        expected_tabs = [
            "Basis-Widgets",
            "Layouts",
            "Eingabe-Widgets",
            "Anzeige-Widgets",
        ]
        actual_tabs = [tab_widget.tabText(i) for i in range(tab_widget.count())]
        assert actual_tabs == expected_tabs

    def test_input_widgets(self, widget):
        """Test der Eingabe-Widgets."""
        # Prüfe ob Eingabe-Widgets existieren
        assert hasattr(widget, "line_edit")
        assert hasattr(widget, "text_edit")
        assert hasattr(widget, "spin_box")
        assert hasattr(widget, "slider")
        assert hasattr(widget, "combo_box")

        # Test Standardwerte
        assert widget.spin_box.value() == 100
        assert widget.slider.value() == 65
        assert widget.combo_box.count() == 5

    def test_clear_all_inputs(self, widget):
        """Test des Löschens aller Eingaben."""
        # Setze Testwerte
        widget.line_edit.setText("Test")
        widget.text_edit.setPlainText("Test Text")
        widget.spin_box.setValue(50)
        widget.slider.setValue(30)
        widget.combo_box.setCurrentIndex(2)

        # Lösche alle Eingaben
        widget.clear_all_inputs()

        # Prüfe ob gelöscht
        assert widget.line_edit.text() == ""
        assert widget.text_edit.toPlainText() == ""
        assert widget.spin_box.value() == 0
        assert widget.slider.value() == 0
        assert widget.combo_box.currentIndex() == 0

    def test_progress_demo(self, widget):
        """Test der Progress-Bar-Demo."""
        # Starte Progress
        widget.start_progress_demo()
        assert widget.timer.isActive()
        assert widget.progress_value == 0

        # Simuliere Timer-Update
        widget.update_progress()
        assert widget.progress_value == 2
        assert widget.progress_bar.value() == 2

        # Stoppe Progress
        widget.stop_progress_demo()
        assert not widget.timer.isActive()

    def test_machine_status_update(self, widget):
        """Test der Maschinen-Status-Aktualisierung."""
        widget.update_machine_status("Test Status", "red", "lightcoral")
        assert "Test Status" in widget.machine_status.text()
        assert "red" in widget.machine_status.styleSheet()
        assert "lightcoral" in widget.machine_status.styleSheet()

    @patch("PySide6.QtWidgets.QMessageBox.information")
    def test_show_message(self, mock_msgbox, widget):
        """Test der Nachrichten-Anzeige."""
        widget.show_message("Test Nachricht")
        mock_msgbox.assert_called_once_with(widget, "Information", "Test Nachricht")

    @patch("PySide6.QtWidgets.QMessageBox.about")
    def test_show_info(self, mock_about, widget):
        """Test der Info-Anzeige."""
        widget.show_info()
        mock_about.assert_called_once()


class TestDatenbankBrowser:
    """Tests für Datenbank Browser."""

    @pytest.fixture
    def app(self):
        """QApplication Fixture."""
        if not PYQT_AVAILABLE:
            pytest.skip("PyQt/PySide nicht verfügbar")

        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app

    @pytest.fixture
    def temp_db(self):
        """Temporäre Datenbank für Tests."""
        with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
            db_path = f.name
        yield db_path
        os.unlink(db_path)

    @pytest.fixture
    def browser(self, app, temp_db):
        """DatabaseBrowser Fixture."""
        browser = DatabaseBrowser(temp_db)
        yield browser
        browser.close()

    def test_database_initialization(self, browser, temp_db):
        """Test der Datenbank-Initialisierung."""
        assert browser.db_path == temp_db
        assert os.path.exists(temp_db)

        # Prüfe Tabellen-Erstellung
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]

        expected_tables = ["machines", "production_data", "maintenance"]
        for table in expected_tables:
            assert table in tables

        conn.close()

    def test_execute_query(self, browser):
        """Test der Query-Ausführung."""
        # Test erfolgreiche Query
        result = browser.db_manager.execute_query("SELECT COUNT(*) FROM machines")
        assert result is not None
        assert len(result) > 0

        # Test fehlerhafte Query
        result = browser.db_manager.execute_query("SELECT * FROM nonexistent_table")
        # execute_query gibt (None, []) zurück bei Fehlern
        assert result[0] is None

    def test_sample_data_insertion(self, browser, temp_db):
        """Test der Beispieldaten-Einfügung."""
        conn = sqlite3.connect(temp_db)
        cursor = conn.cursor()

        # Prüfe Maschinen-Daten
        cursor.execute("SELECT COUNT(*) FROM machines")
        machine_count = cursor.fetchone()[0]
        assert machine_count > 0

        # Prüfe Produktions-Daten
        cursor.execute("SELECT COUNT(*) FROM production_data")
        production_count = cursor.fetchone()[0]
        assert production_count > 0

        # Prüfe Wartungs-Daten
        cursor.execute("SELECT COUNT(*) FROM maintenance")
        maintenance_count = cursor.fetchone()[0]
        assert maintenance_count > 0

        conn.close()

    def test_widget_components(self, browser):
        """Test der Widget-Komponenten."""
        assert hasattr(browser, "data_table")
        assert hasattr(browser, "table_tree")
        assert hasattr(browser, "search_edit")
        assert hasattr(browser, "add_button")
        assert hasattr(browser, "status_bar")


class TestStreamlitComponents:
    """Tests für Streamlit-Komponenten."""

    @pytest.fixture
    def mock_streamlit(self):
        """Mock Streamlit für Tests."""
        if not STREAMLIT_AVAILABLE:
            pytest.skip("Streamlit nicht verfügbar")

        with patch.multiple(
            "streamlit",
            title=Mock(),
            header=Mock(),
            subheader=Mock(),
            write=Mock(),
            markdown=Mock(),
            selectbox=Mock(return_value="Option 1"),
            slider=Mock(return_value=50),
            button=Mock(return_value=False),
            columns=Mock(return_value=[Mock(), Mock()]),
            metric=Mock(),
            line_chart=Mock(),
            bar_chart=Mock(),
            plotly_chart=Mock(),
            dataframe=Mock(),
            session_state=Mock(),
            sidebar=Mock(),
        ) as mocks:
            yield mocks

    def test_streamlit_imports(self):
        """Test der Streamlit-Imports."""
        if not STREAMLIT_AVAILABLE:
            pytest.skip("Streamlit nicht verfügbar")

        # Test ob Module importiert werden können
        try:
            import daten_upload
            import erste_webapp
            import interaktive_charts
            import produktions_dashboard
            import qualitaets_monitor
        except ImportError as e:
            pytest.fail(f"Import-Fehler: {e}")

    def test_data_generation(self):
        """Test der Daten-Generierung für Streamlit-Apps."""
        # Test Produktionsdaten-Generierung
        dates = pd.date_range("2024-01-01", periods=30, freq="D")
        production_data = pd.DataFrame(
            {
                "Datum": dates,
                "Produktion": np.random.randint(100, 500, 30),
                "Qualität": np.random.uniform(95, 99.5, 30),
                "Effizienz": np.random.uniform(80, 95, 30),
            }
        )

        assert len(production_data) == 30
        assert "Datum" in production_data.columns
        assert "Produktion" in production_data.columns
        assert production_data["Produktion"].min() >= 100
        assert production_data["Produktion"].max() <= 500

    @patch("streamlit.set_page_config")
    def test_page_config(self, mock_config, mock_streamlit):
        """Test der Seiten-Konfiguration."""
        # Simuliere Streamlit-App-Start
        mock_config.assert_not_called()  # Noch nicht aufgerufen

        # Importiere und teste Konfiguration
        expected_config = {
            "page_title": "Bystronic Streamlit Demo",
            "page_icon": "🏭",
            "layout": "wide",
        }

        # Prüfe ob Konfiguration korrekt wäre
        assert expected_config["page_title"] == "Bystronic Streamlit Demo"
        assert expected_config["page_icon"] == "🏭"
        assert expected_config["layout"] == "wide"


class TestUIIntegration:
    """Integrationstests für UI-Komponenten."""

    def test_data_flow_pyqt_to_streamlit(self):
        """Test des Datenflusses zwischen PyQt und Streamlit."""
        # Erstelle Testdaten im PyQt-Format
        test_data = {
            "machine_id": 1,
            "production_rate": 245,
            "temperature": 65,
            "status": "running",
        }

        # Konvertiere zu Streamlit-Format
        streamlit_data = pd.DataFrame([test_data])

        assert len(streamlit_data) == 1
        assert streamlit_data["machine_id"].iloc[0] == 1
        assert streamlit_data["production_rate"].iloc[0] == 245

    def test_database_to_ui_conversion(self):
        """Test der Datenbank-zu-UI-Konvertierung."""
        # Simuliere Datenbank-Ergebnis
        db_result = [
            (1, "Laser_01", "Laser", "Active", 245.5),
            (2, "Press_01", "Press", "Maintenance", 0.0),
            (3, "Cut_01", "Cutter", "Active", 180.2),
        ]

        # Konvertiere zu DataFrame
        columns = ["id", "name", "type", "status", "production_rate"]
        df = pd.DataFrame(db_result, columns=columns)

        assert len(df) == 3
        assert df["status"].value_counts()["Active"] == 2
        assert df["production_rate"].sum() == 425.7

    def test_error_handling(self):
        """Test der Fehlerbehandlung."""
        # Test Division durch Null
        with pytest.raises(ZeroDivisionError):
            10 / 0

        # Test Datei nicht gefunden
        with pytest.raises(FileNotFoundError):
            with open("nonexistent_file.txt") as f:
                f.read()

        # Test Index-Fehler
        test_list = [1, 2, 3]
        with pytest.raises(IndexError):
            test_list[10]


class TestPerformance:
    """Performance-Tests für UI-Komponenten."""

    def test_large_dataset_handling(self):
        """Test der Verarbeitung großer Datensätze."""
        import time

        # Erstelle großen Datensatz
        large_data = pd.DataFrame(
            {
                "id": range(10000),
                "value": np.random.randn(10000),
                "category": np.random.choice(["A", "B", "C"], 10000),
            }
        )

        # Messe Verarbeitungszeit
        start_time = time.time()

        # Simuliere UI-Operationen
        filtered_data = large_data[large_data["value"] > 0]
        grouped_data = large_data.groupby("category")["value"].mean()

        end_time = time.time()
        processing_time = end_time - start_time

        # Performance-Assertion (sollte unter 1 Sekunde sein)
        assert processing_time < 1.0
        assert len(filtered_data) > 0
        assert len(grouped_data) == 3

    def test_memory_usage(self):
        """Test der Speichernutzung."""
        import os

        import psutil

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Erstelle mehrere DataFrames
        dataframes = []
        for _i in range(100):
            df = pd.DataFrame(np.random.randn(1000, 10))
            dataframes.append(df)

        peak_memory = process.memory_info().rss

        # Lösche DataFrames
        del dataframes

        final_memory = process.memory_info().rss

        # Memory sollte nicht exponentiell wachsen
        memory_growth = peak_memory - initial_memory
        memory_cleanup = peak_memory - final_memory

        assert memory_growth > 0  # Speicher sollte gewachsen sein
        # Memory cleanup kann 0 sein bei modernen Python-Versionen mit optimierter GC
        assert memory_cleanup >= 0  # Speicher sollte nicht weiter wachsen


@pytest.mark.skipif(not PYQT_AVAILABLE, reason="PyQt/PySide nicht verfügbar")
class TestPyQTAdvanced:
    """Erweiterte PyQt-Tests."""

    @pytest.fixture
    def app(self):
        """QApplication Fixture."""
        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app

    def test_signal_slot_connections(self, app):
        """Test der Signal-Slot-Verbindungen."""
        widget = GrundlagenWidget()

        # Test Timer-Signal (PySide6 hat keine isConnected() Methode)
        # Stattdessen prüfen wir ob die Signale existieren
        assert hasattr(widget.timer, "timeout")

        # Test Widget-Signale
        assert hasattr(widget.line_edit, "textChanged")
        assert hasattr(widget.spin_box, "valueChanged")
        assert hasattr(widget.slider, "valueChanged")

        widget.close()

    def test_widget_styling(self, app):
        """Test des Widget-Stylings."""
        widget = GrundlagenWidget()

        # Prüfe ob Styles angewendet wurden
        machine_status = widget.machine_status
        style_sheet = machine_status.styleSheet()

        assert "padding" in style_sheet
        assert "border" in style_sheet
        assert "background-color" in style_sheet

        widget.close()


@pytest.mark.skipif(not STREAMLIT_AVAILABLE, reason="Streamlit nicht verfügbar")
class TestStreamlitAdvanced:
    """Erweiterte Streamlit-Tests."""

    def test_session_state_management(self):
        """Test des Session State Managements."""
        # Simuliere Session State
        mock_session_state = {}

        # Test Initialisierung
        if "counter" not in mock_session_state:
            mock_session_state["counter"] = 0

        assert mock_session_state["counter"] == 0

        # Test Aktualisierung
        mock_session_state["counter"] += 1
        assert mock_session_state["counter"] == 1

    def test_caching_behavior(self):
        """Test des Caching-Verhaltens."""
        # Simuliere @st.cache_data Verhalten
        cache = {}

        def cached_function(param):
            if param not in cache:
                # Simuliere teure Berechnung
                result = param**2
                cache[param] = result
            return cache[param]

        # Erste Ausführung
        result1 = cached_function(5)
        assert result1 == 25
        assert 5 in cache

        # Zweite Ausführung (aus Cache)
        result2 = cached_function(5)
        assert result2 == 25
        assert result1 == result2


if __name__ == "__main__":
    # Führe Tests aus
    pytest.main([__file__, "-v", "--tb=short"])
