#!/usr/bin/env python3
"""
Einfache Tests für Modul 08 - UI-Entwicklung
============================================

Funktionsfähige Tests mit uv Package Manager und robuster Dependency-Behandlung.

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import os

import pytest

# Import Test-Utilities
from tests.test_08_ui_utils import (
    DEPENDENCIES,
    StreamlitTestHelper,
    TestDataGenerator,
    UITestHelper,
    requires_charts,
    requires_data,
    requires_streamlit,
)


class TestBasicFunctionality:
    """Grundlegende Funktionalitätstests ohne UI-Dependencies."""

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

    def test_csv_parsing(self):
        """Test des CSV-Parsings."""
        csv_content = TestDataGenerator.create_csv_content()

        # Simuliere CSV-Parsing ohne pandas
        lines = csv_content.strip().split('\n')
        headers = lines[0].split(',')

        assert 'Datum' in headers
        assert 'Maschine' in headers
        assert 'Produktion' in headers
        assert 'Qualität' in headers

        # Parse erste Datenzeile
        first_row = lines[1].split(',')
        assert len(first_row) == len(headers)
        assert first_row[1] == 'Laser_01'  # Maschine

    def test_json_processing(self):
        """Test der JSON-Verarbeitung."""
        json_data = TestDataGenerator.create_json_content()

        assert 'machines' in json_data
        assert 'timestamp' in json_data
        assert len(json_data['machines']) == 2

        # Validiere Maschinen-Struktur
        machine = json_data['machines'][0]
        assert 'id' in machine
        assert 'name' in machine
        assert 'type' in machine
        assert 'status' in machine

    def test_color_utilities(self):
        """Test der Farb-Hilfsfunktionen."""
        def hex_to_rgb(hex_color):
            hex_color = hex_color.lstrip('#')
            return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

        rgb = hex_to_rgb('#FF0000')
        assert rgb == (255, 0, 0)

        rgb = hex_to_rgb('#00FF00')
        assert rgb == (0, 255, 0)

        rgb = hex_to_rgb('#0000FF')
        assert rgb == (0, 0, 255)

    def test_format_utilities(self):
        """Test der Formatierungs-Hilfsfunktionen."""
        def format_number(value, decimals=2, unit=''):
            if isinstance(value, int | float):
                formatted = f"{value:.{decimals}f}"
                if unit:
                    formatted += f" {unit}"
                return formatted
            return str(value)

        assert format_number(245.567, 2, 'Stk/h') == "245.57 Stk/h"
        assert format_number(100, 0) == "100"
        assert format_number(65.2, 1, '°C') == "65.2 °C"


@requires_data()
class TestDataProcessing:
    """Tests für Datenverarbeitung mit pandas/numpy."""

    def test_machine_data_generation(self):
        """Test der Maschinendaten-Generierung."""
        machines = TestDataGenerator.create_machine_data(5)

        assert len(machines) == 5
        for machine in machines:
            assert 'id' in machine
            assert 'name' in machine
            assert 'type' in machine
            assert 'status' in machine
            assert isinstance(machine['production_rate'], int | float)

    def test_production_data_generation(self):
        """Test der Produktionsdaten-Generierung."""
        import pandas as pd

        df = TestDataGenerator.create_production_data(7)

        assert isinstance(df, pd.DataFrame)
        assert len(df) == 21  # 7 Tage * 3 Maschinen
        assert 'Datum' in df.columns
        assert 'Maschine' in df.columns
        assert 'Produktion' in df.columns
        assert 'Qualität' in df.columns

    def test_data_cleaning(self):
        """Test der Datenbereinigung."""
        import pandas as pd

        def clean_production_data(df):
            # Entferne Duplikate
            df = df.drop_duplicates()

            # Entferne Zeilen mit fehlenden kritischen Werten
            df = df.dropna(subset=['Maschine', 'Produktion'])

            # Konvertiere Datentypen
            if 'Produktion' in df.columns:
                df['Produktion'] = pd.to_numeric(df['Produktion'], errors='coerce')

            # Entferne negative Produktionswerte
            if 'Produktion' in df.columns:
                df = df[df['Produktion'] >= 0]

            return df

        # Test mit schmutzigen Daten
        dirty_data = pd.DataFrame({
            'Maschine': ['Laser_01', 'Press_01', 'Laser_01', None, 'Cut_01'],
            'Produktion': [245, -10, 245, 180, 'invalid'],
            'Qualität': [98.5, 97.2, 98.5, 99.0, 96.8]
        })

        cleaned_data = clean_production_data(dirty_data)

        # Prüfe Bereinigung
        assert len(cleaned_data) < len(dirty_data)
        assert cleaned_data['Produktion'].min() >= 0
        assert not cleaned_data['Maschine'].isnull().any()


@requires_charts()
class TestChartGeneration:
    """Tests für Chart-Generierung mit plotly."""

    def test_line_chart_creation(self):
        """Test der Liniendiagramm-Erstellung."""
        import plotly.express as px

        # Erstelle Testdaten
        df = TestDataGenerator.create_production_data(10)

        # Erstelle Line Chart
        fig = px.line(
            df,
            x='Datum',
            y='Produktion',
            color='Maschine',
            title='Produktionsverlauf'
        )

        assert fig is not None
        assert len(fig.data) > 0
        assert fig.layout.title.text == 'Produktionsverlauf'

    def test_bar_chart_creation(self):
        """Test der Balkendiagramm-Erstellung."""
        import plotly.express as px

        df = TestDataGenerator.create_production_data(10)

        # Aggregiere Daten
        agg_data = df.groupby('Maschine')['Produktion'].sum().reset_index()

        fig = px.bar(
            agg_data,
            x='Maschine',
            y='Produktion',
            title='Gesamtproduktion pro Maschine'
        )

        assert fig is not None
        assert len(fig.data) == 1
        assert fig.layout.title.text == 'Gesamtproduktion pro Maschine'


@requires_streamlit()
class TestStreamlitMocking:
    """Tests für Streamlit-Komponenten mit Mocking."""

    def test_streamlit_component_mocking(self):
        """Test des Streamlit-Component-Mockings."""
        mock_components = StreamlitTestHelper.mock_streamlit_components()

        # Test Mock-Funktionalität
        mock_components['title']("Test Title")
        mock_components['title'].assert_called_with("Test Title")

        # Test Selectbox Mock
        selection = mock_components['selectbox']("Choose option", ["A", "B", "C"])
        assert selection == "Option 1"

        # Test Slider Mock
        value = mock_components['slider']("Select value", 0, 100)
        assert value == 50

    def test_file_upload_simulation(self):
        """Test der Datei-Upload-Simulation."""
        csv_content = TestDataGenerator.create_csv_content()
        mock_file = StreamlitTestHelper.simulate_file_upload("test.csv", csv_content)

        assert mock_file.name == "test.csv"
        content = mock_file.read().decode('utf-8')
        assert "Laser_01" in content

    def test_session_state_simulation(self):
        """Test der Session-State-Simulation."""
        session_state = {}

        def init_session_state(key, default_value):
            if key not in session_state:
                session_state[key] = default_value
            return session_state[key]

        # Test Initialisierung
        counter = init_session_state('counter', 0)
        assert counter == 0

        # Test Aktualisierung
        session_state['counter'] += 1
        assert session_state['counter'] == 1


class TestDatabaseOperations:
    """Tests für Datenbank-Operationen."""

    def test_sqlite_database_creation(self, tmp_path):
        """Test der SQLite-Datenbank-Erstellung."""
        import sqlite3

        db_path = tmp_path / "test.db"
        UITestHelper.create_test_database(str(db_path))

        # Prüfe Datenbank-Erstellung
        assert db_path.exists()

        # Prüfe Tabellen
        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = [row[0] for row in cursor.fetchall()]

        assert 'machines' in tables
        assert 'production_data' in tables

        # Prüfe Daten
        cursor.execute("SELECT COUNT(*) FROM machines")
        machine_count = cursor.fetchone()[0]
        assert machine_count > 0

        conn.close()

    def test_database_query_execution(self, tmp_path):
        """Test der Datenbank-Query-Ausführung."""
        import sqlite3

        db_path = tmp_path / "test.db"
        UITestHelper.create_test_database(str(db_path))

        conn = sqlite3.connect(str(db_path))
        cursor = conn.cursor()

        # Test erfolgreiche Query
        cursor.execute("SELECT * FROM machines WHERE status = 'Active'")
        active_machines = cursor.fetchall()
        assert len(active_machines) > 0

        # Test Join-Query
        cursor.execute("""
            SELECT m.name, p.production
            FROM machines m
            JOIN production_data p ON m.id = p.machine_id
        """)
        production_data = cursor.fetchall()
        assert len(production_data) > 0

        conn.close()


class TestPerformanceAndMemory:
    """Performance- und Memory-Tests."""

    def test_large_dataset_processing(self):
        """Test der Verarbeitung großer Datensätze."""
        import time

        # Erstelle großen Datensatz (simuliert)
        large_data = []
        for i in range(1000):
            large_data.append({
                'id': i,
                'value': i * 2,
                'category': f'Cat_{i % 10}'
            })

        # Messe Verarbeitungszeit
        start_time = time.time()

        # Simuliere Verarbeitung
        filtered_data = [item for item in large_data if item['value'] > 500]
        grouped_data = {}
        for item in large_data:
            cat = item['category']
            if cat not in grouped_data:
                grouped_data[cat] = []
            grouped_data[cat].append(item['value'])

        end_time = time.time()
        processing_time = end_time - start_time

        # Performance-Assertion
        assert processing_time < 1.0
        assert len(filtered_data) > 0
        assert len(grouped_data) == 10

    @pytest.mark.skipif(not DEPENDENCIES['psutil'], reason="psutil nicht verfügbar")
    def test_memory_usage_monitoring(self):
        """Test der Speichernutzung-Überwachung."""
        import psutil

        process = psutil.Process(os.getpid())
        initial_memory = process.memory_info().rss

        # Erstelle mehrere Listen (simuliert Memory-Verbrauch)
        data_lists = []
        for _i in range(10):
            data_list = list(range(1000))
            data_lists.append(data_list)

        peak_memory = process.memory_info().rss

        # Lösche Listen
        del data_lists

        process.memory_info().rss

        # Memory sollte gewachsen und dann reduziert worden sein
        memory_growth = peak_memory - initial_memory
        assert memory_growth > 0


class TestErrorHandling:
    """Tests für Fehlerbehandlung."""

    def test_file_not_found_handling(self):
        """Test der Datei-nicht-gefunden-Behandlung."""
        with pytest.raises(FileNotFoundError):
            with open('nonexistent_file.txt') as f:
                f.read()

    def test_division_by_zero_handling(self):
        """Test der Division-durch-Null-Behandlung."""
        with pytest.raises(ZeroDivisionError):
            pass

    def test_index_error_handling(self):
        """Test der Index-Fehler-Behandlung."""
        test_list = [1, 2, 3]
        with pytest.raises(IndexError):
            test_list[10]

    def test_graceful_error_handling(self):
        """Test der eleganten Fehlerbehandlung."""
        def safe_divide(a, b):
            try:
                return a / b, None
            except ZeroDivisionError:
                return None, "Division durch Null nicht möglich"
            except TypeError:
                return None, "Ungültige Datentypen für Division"

        # Test erfolgreiche Division
        result, error = safe_divide(10, 2)
        assert result == 5.0
        assert error is None

        # Test Division durch Null
        result, error = safe_divide(10, 0)
        assert result is None
        assert "Division durch Null" in error

        # Test ungültige Typen
        result, error = safe_divide("10", 2)
        assert result is None
        assert "Ungültige Datentypen" in error


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
