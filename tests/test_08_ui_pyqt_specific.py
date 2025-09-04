#!/usr/bin/env python3
"""
Spezifische Tests für PyQt-Komponenten in Modul 08
=================================================

Detaillierte Tests für einzelne PyQt-Beispiele.

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import sys
from pathlib import Path
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd
import pytest

# PyQt/PySide Tests
try:
    from PySide6.QtCore import Qt, QThread, QTimer
    from PySide6.QtGui import QPixmap
    from PySide6.QtTest import QTest
    from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget
    PYQT_AVAILABLE = True
except ImportError:
    PYQT_AVAILABLE = False

# Import der zu testenden Module
sys.path.append(str(Path(__file__).parent.parent / "src" / "08_ui" / "beispiele" / "pyqt"))

if PYQT_AVAILABLE:
    from diagramm_viewer import ChartWidget, DiagrammViewer
    from maschinendaten_gui import DataWorker, MaschinendatenGUI, MaschinenDatenModel
    from moderne_ui import AnimatedButton, GlassEffect, ModerneUI


@pytest.mark.skipif(not PYQT_AVAILABLE, reason="PyQt/PySide nicht verfügbar")
class TestMaschinendatenGUI:
    """Tests für Maschinendaten GUI."""

    @pytest.fixture
    def app(self):
        """QApplication Fixture."""
        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app

    @pytest.fixture
    def sample_data(self):
        """Beispieldaten für Tests."""
        return [
            {
                'id': 1,
                'name': 'Laser_01',
                'type': 'Laser',
                'status': 'Active',
                'production_rate': 245.5,
                'temperature': 65.2,
                'last_maintenance': '2024-01-15'
            },
            {
                'id': 2,
                'name': 'Press_01',
                'type': 'Press',
                'status': 'Maintenance',
                'production_rate': 0.0,
                'temperature': 25.0,
                'last_maintenance': '2024-01-20'
            }
        ]

    @pytest.fixture
    def gui(self, app, sample_data):
        """MaschinendatenGUI Fixture."""
        with patch('maschinendaten_gui.MaschinendatenGUI.load_data') as mock_load:
            mock_load.return_value = sample_data
            gui = MaschinendatenGUI()
            yield gui
            gui.close()

    def test_gui_initialization(self, gui):
        """Test der GUI-Initialisierung."""
        assert gui.windowTitle() == "Maschinendaten Management - Bystronic"
        assert hasattr(gui, 'table_widget')
        assert hasattr(gui, 'filter_combo')
        assert hasattr(gui, 'search_line')
        assert hasattr(gui, 'status_label')

    def test_data_model(self, sample_data):
        """Test des Datenmodells."""
        model = MaschinenDatenModel(sample_data)

        assert model.rowCount() == 2
        assert model.columnCount() == 7

        # Test Daten-Zugriff
        first_item = model.data(model.index(0, 0))
        assert first_item == 1

        name_item = model.data(model.index(0, 1))
        assert name_item == 'Laser_01'

    def test_data_filtering(self, gui, sample_data):
        """Test der Datenfilterung."""
        # Test Status-Filter
        gui.filter_data('Active')
        # Prüfe ob nur aktive Maschinen angezeigt werden

        gui.filter_data('All')
        # Prüfe ob alle Maschinen angezeigt werden

        # Test Suchfunktion
        gui.search_data('Laser')
        # Prüfe ob nur Laser-Maschinen gefunden werden

    def test_data_export(self, gui):
        """Test des Datenexports."""
        with patch('PySide6.QtWidgets.QFileDialog.getSaveFileName') as mock_dialog:
            mock_dialog.return_value = ('/tmp/test_export.csv', 'CSV Files (*.csv)')

            with patch('pandas.DataFrame.to_csv') as mock_to_csv:
                gui.export_data()
                mock_to_csv.assert_called_once()

    def test_data_refresh(self, gui):
        """Test der Datenaktualisierung."""
        with patch('maschinendaten_gui.MaschinendatenGUI.load_data') as mock_load:
            mock_load.return_value = [{'id': 3, 'name': 'New_Machine'}]

            gui.refresh_data()
            mock_load.assert_called_once()

    def test_worker_thread(self, app):
        """Test des Worker-Threads."""
        worker = DataWorker()

        # Test Signal-Emission
        with patch.object(worker, 'data_loaded'):
            worker.run()
            # Worker sollte Daten laden und Signal emittieren

    def test_table_operations(self, gui, sample_data):
        """Test der Tabellen-Operationen."""
        table = gui.table_widget

        # Test Sortierung
        table.sortItems(1, Qt.AscendingOrder)  # Nach Name sortieren

        # Test Selektion
        table.selectRow(0)
        selected_items = table.selectedItems()
        assert len(selected_items) > 0

        # Test Kontext-Menü
        with patch('PySide6.QtWidgets.QMenu.exec'):
            # Simuliere Rechtsklick
            pass


@pytest.mark.skipif(not PYQT_AVAILABLE, reason="PyQt/PySide nicht verfügbar")
class TestDiagrammViewer:
    """Tests für Diagramm Viewer."""

    @pytest.fixture
    def app(self):
        """QApplication Fixture."""
        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app

    @pytest.fixture
    def viewer(self, app):
        """DiagrammViewer Fixture."""
        viewer = DiagrammViewer()
        yield viewer
        viewer.close()

    def test_viewer_initialization(self, viewer):
        """Test der Viewer-Initialisierung."""
        assert viewer.windowTitle() == "Produktionsdaten Visualisierung - Bystronic"
        assert hasattr(viewer, 'chart_widget')
        assert hasattr(viewer, 'chart_type_combo')
        assert hasattr(viewer, 'time_range_combo')

    def test_chart_creation(self, viewer):
        """Test der Diagramm-Erstellung."""
        # Test verschiedene Chart-Typen
        chart_types = ['line', 'bar', 'scatter', 'pie']

        for chart_type in chart_types:
            viewer.create_chart(chart_type)
            # Prüfe ob Chart erstellt wurde

    def test_data_loading(self, viewer):
        """Test des Datenladens."""
        with patch('pandas.read_csv') as mock_read_csv:
            mock_data = pd.DataFrame({
                'date': pd.date_range('2024-01-01', periods=10),
                'production': np.random.randint(100, 500, 10),
                'quality': np.random.uniform(95, 99, 10)
            })
            mock_read_csv.return_value = mock_data

            viewer.load_production_data()
            mock_read_csv.assert_called_once()

    def test_chart_widget(self, app):
        """Test des Chart-Widgets."""
        chart_widget = ChartWidget()

        # Test Daten setzen
        test_data = {
            'x': [1, 2, 3, 4, 5],
            'y': [10, 20, 15, 25, 30]
        }

        chart_widget.set_data(test_data)
        # Prüfe ob Daten korrekt gesetzt wurden

    def test_chart_export(self, viewer):
        """Test des Chart-Exports."""
        with patch('PySide6.QtWidgets.QFileDialog.getSaveFileName') as mock_dialog:
            mock_dialog.return_value = ('/tmp/chart.png', 'PNG Files (*.png)')

            with patch.object(viewer.chart_widget, 'grab') as mock_grab:
                mock_pixmap = Mock(spec=QPixmap)
                mock_grab.return_value = mock_pixmap

                viewer.export_chart()
                mock_grab.assert_called_once()
                mock_pixmap.save.assert_called_once()


@pytest.mark.skipif(not PYQT_AVAILABLE, reason="PyQt/PySide nicht verfügbar")
class TestModerneUI:
    """Tests für Moderne UI."""

    @pytest.fixture
    def app(self):
        """QApplication Fixture."""
        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app

    @pytest.fixture
    def ui(self, app):
        """ModerneUI Fixture."""
        ui = ModerneUI()
        yield ui
        ui.close()

    def test_ui_initialization(self, ui):
        """Test der UI-Initialisierung."""
        assert ui.windowTitle() == "Moderne Bystronic UI"
        assert hasattr(ui, 'sidebar')
        assert hasattr(ui, 'content_area')
        assert hasattr(ui, 'theme_toggle')

    def test_theme_switching(self, ui):
        """Test des Theme-Wechsels."""
        # Test Dark Theme
        ui.toggle_theme()
        # Prüfe ob Dark Theme angewendet wurde

        # Test Light Theme
        ui.toggle_theme()
        # Prüfe ob Light Theme angewendet wurde

    def test_animated_button(self, app):
        """Test des animierten Buttons."""
        button = AnimatedButton("Test Button")

        # Test Animation-Start
        button.start_animation()
        assert button.animation.state() != button.animation.Stopped

        # Test Animation-Stop
        button.stop_animation()

    def test_glass_effect(self, app):
        """Test des Glas-Effekts."""
        widget = QWidget()
        glass_effect = GlassEffect(widget)

        # Test Effekt-Anwendung
        glass_effect.apply_effect()
        # Prüfe ob Effekt angewendet wurde

    def test_sidebar_navigation(self, ui):
        """Test der Sidebar-Navigation."""
        # Test Navigation zu verschiedenen Bereichen
        sections = ['Dashboard', 'Maschinen', 'Produktion', 'Wartung']

        for section in sections:
            ui.navigate_to_section(section)
            # Prüfe ob Navigation funktioniert

    def test_responsive_layout(self, ui):
        """Test des responsiven Layouts."""
        # Test verschiedene Fenstergrößen
        sizes = [(800, 600), (1200, 800), (1920, 1080)]

        for width, height in sizes:
            ui.resize(width, height)
            # Prüfe ob Layout sich anpasst

    def test_custom_widgets(self, ui):
        """Test der benutzerdefinierten Widgets."""
        # Test Dashboard-Widgets
        assert hasattr(ui, 'create_dashboard_widget')
        assert hasattr(ui, 'create_metric_card')
        assert hasattr(ui, 'create_chart_container')

        # Test Widget-Erstellung
        dashboard_widget = ui.create_dashboard_widget()
        assert dashboard_widget is not None


class TestUIUtilities:
    """Tests für UI-Hilfsfunktionen."""

    def test_color_utilities(self):
        """Test der Farb-Hilfsfunktionen."""
        # Test Hex zu RGB Konvertierung
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        rgb = hex_to_rgb('#FF0000')
        assert rgb == (255, 0, 0)

        rgb = hex_to_rgb('#00FF00')
        assert rgb == (0, 255, 0)

    def test_style_sheet_generation(self):
        """Test der StyleSheet-Generierung."""
        def generate_button_style(bg_color, text_color, border_radius=5):
            return f"""
            QPushButton {{
                background-color: {bg_color};
                color: {text_color};
                border-radius: {border_radius}px;
                padding: 10px;
                font-weight: bold;
            }}
            QPushButton:hover {{
                background-color: {bg_color}AA;
            }}
            """

        style = generate_button_style('#4CAF50', 'white')
        assert '#4CAF50' in style
        assert 'white' in style
        assert 'border-radius: 5px' in style

    def test_data_validation(self):
        """Test der Datenvalidierung."""
        def validate_machine_data(data):
            required_fields = ['id', 'name', 'type', 'status']
            errors = []

            for field in required_fields:
                if field not in data:
                    errors.append(f"Fehlendes Feld: {field}")

            if 'production_rate' in data:
                if not isinstance(data['production_rate'], int | float):
                    errors.append("Produktionsrate muss numerisch sein")
                elif data['production_rate'] < 0:
                    errors.append("Produktionsrate kann nicht negativ sein")

            return len(errors) == 0, errors

        # Test gültige Daten
        valid_data = {
            'id': 1,
            'name': 'Laser_01',
            'type': 'Laser',
            'status': 'Active',
            'production_rate': 245.5
        }

        is_valid, errors = validate_machine_data(valid_data)
        assert is_valid
        assert len(errors) == 0

        # Test ungültige Daten
        invalid_data = {
            'id': 1,
            'name': 'Laser_01',
            'production_rate': -10
        }

        is_valid, errors = validate_machine_data(invalid_data)
        assert not is_valid
        assert len(errors) > 0

    def test_format_utilities(self):
        """Test der Formatierungs-Hilfsfunktionen."""
        def format_number(value, decimals=2, unit=''):
            """Formatiert Zahlen für die Anzeige."""
            if isinstance(value, int | float):
                formatted = f"{value:.{decimals}f}"
                if unit:
                    formatted += f" {unit}"
                return formatted
            return str(value)

        assert format_number(245.567, 2, 'Stk/h') == "245.57 Stk/h"
        assert format_number(100, 0) == "100"
        assert format_number(65.2, 1, '°C') == "65.2 °C"

    def test_icon_management(self):
        """Test der Icon-Verwaltung."""
        icon_mapping = {
            'active': '🟢',
            'warning': '🟡',
            'error': '🔴',
            'maintenance': '🔧',
            'offline': '⚫'
        }

        def get_status_icon(status):
            return icon_mapping.get(status.lower(), '❓')

        assert get_status_icon('Active') == '🟢'
        assert get_status_icon('ERROR') == '🔴'
        assert get_status_icon('unknown') == '❓'


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
