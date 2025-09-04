#!/usr/bin/env python3
"""
Test-Utilities für Modul 08 - UI-Entwicklung
============================================

Hilfsfunktionen und Fixtures für UI-Tests mit uv Package Manager.

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import tempfile
from unittest.mock import Mock

import numpy as np
import pandas as pd
import pytest

# Dependency-Checks
DEPENDENCIES = {
    'pandas': False,
    'numpy': False,
    'pyside6': False,
    'streamlit': False,
    'plotly': False,
    'psutil': False
}

# Prüfe verfügbare Dependencies
try:
    import pandas as pd
    DEPENDENCIES['pandas'] = True
except ImportError:
    pass

try:
    import numpy as np
    DEPENDENCIES['numpy'] = True
except ImportError:
    pass

try:
    from PySide6.QtCore import Qt, QTimer, Signal  # Signal statt pyqtSignal
    from PySide6.QtWidgets import QApplication
    DEPENDENCIES['pyside6'] = True
except ImportError:
    pass

try:
    import streamlit as st
    DEPENDENCIES['streamlit'] = True
except ImportError:
    pass

try:
    import plotly.express as px
    import plotly.graph_objects as go
    DEPENDENCIES['plotly'] = True
except ImportError:
    pass

try:
    import psutil
    DEPENDENCIES['psutil'] = True
except ImportError:
    pass


class TestDataGenerator:
    """Generiert Testdaten für UI-Tests."""

    @staticmethod
    def create_machine_data(count=5):
        """Erstellt Beispiel-Maschinendaten."""
        if not DEPENDENCIES['pandas']:
            return []

        machines = []
        for i in range(count):
            machines.append({
                'id': i + 1,
                'name': f'Machine_{i+1:02d}',
                'type': ['Laser', 'Press', 'Cutter', 'Bender'][i % 4],
                'status': ['Active', 'Maintenance', 'Offline'][i % 3],
                'production_rate': round(np.random.uniform(100, 300), 1) if DEPENDENCIES['numpy'] else 200.0,
                'temperature': round(np.random.uniform(60, 80), 1) if DEPENDENCIES['numpy'] else 70.0,
                'last_maintenance': f'2024-01-{(i % 30) + 1:02d}'
            })
        return machines

    @staticmethod
    def create_production_data(days=30):
        """Erstellt Produktionsdaten für Zeitreihen."""
        if not DEPENDENCIES['pandas']:
            return pd.DataFrame() if DEPENDENCIES['pandas'] else []

        dates = pd.date_range('2024-01-01', periods=days, freq='D')
        data = []

        for date in dates:
            for machine in ['Laser_01', 'Press_01', 'Cut_01']:
                data.append({
                    'Datum': date,
                    'Maschine': machine,
                    'Produktion': np.random.randint(150, 350) if DEPENDENCIES['numpy'] else 250,
                    'Qualität': round(np.random.uniform(95, 99.5), 2) if DEPENDENCIES['numpy'] else 97.5,
                    'Effizienz': round(np.random.uniform(80, 95), 1) if DEPENDENCIES['numpy'] else 87.5,
                    'Temperatur': round(np.random.uniform(60, 75), 1) if DEPENDENCIES['numpy'] else 67.5
                })

        return pd.DataFrame(data)

    @staticmethod
    def create_csv_content():
        """Erstellt CSV-Testinhalt."""
        return """Datum,Maschine,Produktion,Qualität
2024-01-01,Laser_01,245,98.5
2024-01-01,Press_01,180,97.2
2024-01-02,Laser_01,250,99.1
2024-01-02,Press_01,175,96.8"""

    @staticmethod
    def create_json_content():
        """Erstellt JSON-Testinhalt."""
        return {
            "machines": [
                {"id": 1, "name": "Laser_01", "type": "Laser", "status": "Active"},
                {"id": 2, "name": "Press_01", "type": "Press", "status": "Maintenance"}
            ],
            "timestamp": "2024-01-01T10:00:00Z"
        }


class MockQApplication:
    """Mock für QApplication wenn PySide6 nicht verfügbar."""

    def __init__(self, *args):
        self.args = args

    @staticmethod
    def instance():
        return None

    def exec(self):
        return 0

    def setStyle(self, style):
        pass


class MockWidget:
    """Mock für Qt-Widgets."""

    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        self._text = ""
        self._value = 0
        self._items = []
        self._style_sheet = ""

    def setText(self, text):
        self._text = text

    def text(self):
        return self._text

    def setValue(self, value):
        self._value = value

    def value(self):
        return self._value

    def addItems(self, items):
        self._items.extend(items)

    def setStyleSheet(self, style):
        self._style_sheet = style

    def styleSheet(self):
        return self._style_sheet

    def show(self):
        pass

    def close(self):
        pass


@pytest.fixture
def temp_directory():
    """Temporäres Verzeichnis für Tests."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def sample_machine_data():
    """Beispiel-Maschinendaten."""
    return TestDataGenerator.create_machine_data(3)


@pytest.fixture
def sample_production_data():
    """Beispiel-Produktionsdaten."""
    return TestDataGenerator.create_production_data(7)


@pytest.fixture
def mock_qapp():
    """Mock QApplication für Tests ohne PySide6."""
    if DEPENDENCIES['pyside6']:
        if not QApplication.instance():
            app = QApplication([])
        else:
            app = QApplication.instance()
        yield app
    else:
        yield MockQApplication([])


@pytest.fixture
def csv_test_data():
    """CSV-Testdaten."""
    return TestDataGenerator.create_csv_content()


@pytest.fixture
def json_test_data():
    """JSON-Testdaten."""
    return TestDataGenerator.create_json_content()


def skip_if_missing(*dependencies):
    """Decorator zum Überspringen von Tests bei fehlenden Dependencies."""
    missing = [dep for dep in dependencies if not DEPENDENCIES.get(dep, False)]

    if missing:
        return pytest.mark.skip(reason=f"Missing dependencies: {', '.join(missing)}")
    return lambda func: func


def requires_ui():
    """Decorator für Tests die UI-Dependencies benötigen."""
    return skip_if_missing('pyside6')


def requires_data():
    """Decorator für Tests die Daten-Dependencies benötigen."""
    return skip_if_missing('pandas', 'numpy')


def requires_charts():
    """Decorator für Tests die Chart-Dependencies benötigen."""
    return skip_if_missing('plotly')


def requires_streamlit():
    """Decorator für Tests die Streamlit benötigen."""
    return skip_if_missing('streamlit')


class UITestHelper:
    """Hilfsfunktionen für UI-Tests."""

    @staticmethod
    def validate_widget_properties(widget, expected_props):
        """Validiert Widget-Eigenschaften."""
        for prop, expected_value in expected_props.items():
            if hasattr(widget, prop):
                actual_value = getattr(widget, prop)
                if callable(actual_value):
                    actual_value = actual_value()
                assert actual_value == expected_value, f"Property {prop}: expected {expected_value}, got {actual_value}"

    @staticmethod
    def simulate_user_input(widget, input_type, value):
        """Simuliert Benutzereingaben."""
        if input_type == 'text':
            widget.setText(str(value))
        elif input_type == 'value':
            widget.setValue(value)
        elif input_type == 'selection':
            if hasattr(widget, 'setCurrentIndex'):
                widget.setCurrentIndex(value)

    @staticmethod
    def create_test_database(db_path):
        """Erstellt Test-Datenbank."""
        import sqlite3

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Erstelle Tabellen
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS machines (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                type TEXT NOT NULL,
                status TEXT NOT NULL,
                production_rate REAL,
                temperature REAL
            )
        ''')

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS production_data (
                id INTEGER PRIMARY KEY,
                machine_id INTEGER,
                date TEXT,
                production INTEGER,
                quality REAL,
                FOREIGN KEY (machine_id) REFERENCES machines (id)
            )
        ''')

        # Füge Testdaten ein
        test_machines = [
            (1, 'Laser_01', 'Laser', 'Active', 245.5, 65.2),
            (2, 'Press_01', 'Press', 'Maintenance', 0.0, 25.0),
            (3, 'Cut_01', 'Cutter', 'Active', 180.0, 70.1)
        ]

        cursor.executemany(
            'INSERT OR REPLACE INTO machines VALUES (?, ?, ?, ?, ?, ?)',
            test_machines
        )

        test_production = [
            (1, 1, '2024-01-01', 245, 98.5),
            (2, 1, '2024-01-02', 250, 99.1),
            (3, 2, '2024-01-01', 180, 97.2),
            (4, 3, '2024-01-01', 175, 96.8)
        ]

        cursor.executemany(
            'INSERT OR REPLACE INTO production_data VALUES (?, ?, ?, ?, ?)',
            test_production
        )

        conn.commit()
        conn.close()


class StreamlitTestHelper:
    """Hilfsfunktionen für Streamlit-Tests."""

    @staticmethod
    def mock_streamlit_components():
        """Erstellt Mock-Objekte für Streamlit-Komponenten."""
        return {
            'title': Mock(),
            'header': Mock(),
            'subheader': Mock(),
            'write': Mock(),
            'markdown': Mock(),
            'selectbox': Mock(return_value="Option 1"),
            'slider': Mock(return_value=50),
            'button': Mock(return_value=False),
            'file_uploader': Mock(return_value=None),
            'columns': Mock(return_value=[Mock(), Mock()]),
            'metric': Mock(),
            'line_chart': Mock(),
            'bar_chart': Mock(),
            'plotly_chart': Mock(),
            'dataframe': Mock(),
            'session_state': {},
            'sidebar': Mock()
        }

    @staticmethod
    def simulate_file_upload(filename, content):
        """Simuliert Datei-Upload."""
        mock_file = Mock()
        mock_file.name = filename
        mock_file.read.return_value = content.encode('utf-8') if isinstance(content, str) else content
        return mock_file

    @staticmethod
    def validate_chart_data(chart_data, expected_columns):
        """Validiert Chart-Daten."""
        if DEPENDENCIES['pandas'] and isinstance(chart_data, pd.DataFrame):
            for col in expected_columns:
                assert col in chart_data.columns, f"Missing column: {col}"
            assert len(chart_data) > 0, "Chart data is empty"


def get_dependency_status():
    """Gibt Status aller Dependencies zurück."""
    return DEPENDENCIES.copy()


def print_dependency_status():
    """Druckt Dependency-Status für Debugging."""
    print("\nDependency Status:")
    print("-" * 30)
    for dep, available in DEPENDENCIES.items():
        status = "✓" if available else "✗"
        print(f"{status} {dep}")
    print("-" * 30)


# Test der Utilities selbst
class TestUITestUtils:
    """Tests für die Test-Utilities."""

    def test_dependency_detection(self):
        """Test der Dependency-Erkennung."""
        deps = get_dependency_status()
        assert isinstance(deps, dict)
        assert 'pandas' in deps
        assert 'numpy' in deps
        assert 'pyside6' in deps

    def test_data_generator(self):
        """Test des Daten-Generators."""
        machines = TestDataGenerator.create_machine_data(3)
        assert len(machines) == 3

        if machines:
            assert 'id' in machines[0]
            assert 'name' in machines[0]
            assert 'type' in machines[0]

    def test_csv_content_generation(self):
        """Test der CSV-Inhalt-Generierung."""
        csv_content = TestDataGenerator.create_csv_content()
        assert 'Datum,Maschine,Produktion,Qualität' in csv_content
        assert 'Laser_01' in csv_content

    def test_json_content_generation(self):
        """Test der JSON-Inhalt-Generierung."""
        json_content = TestDataGenerator.create_json_content()
        assert 'machines' in json_content
        assert 'timestamp' in json_content
        assert len(json_content['machines']) == 2

    def test_mock_widget(self):
        """Test des Mock-Widgets."""
        widget = MockWidget()

        widget.setText("Test")
        assert widget.text() == "Test"

        widget.setValue(42)
        assert widget.value() == 42

        widget.setStyleSheet("color: red;")
        assert "color: red;" in widget.styleSheet()


if __name__ == "__main__":
    print_dependency_status()
    pytest.main([__file__, "-v"])
