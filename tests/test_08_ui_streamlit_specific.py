#!/usr/bin/env python3
"""
Spezifische Tests für Streamlit-Komponenten in Modul 08
======================================================

Detaillierte Tests für einzelne Streamlit-Beispiele.

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import json
import sys
from io import BytesIO, StringIO
from pathlib import Path
from unittest.mock import Mock, patch

import numpy as np
import pandas as pd
import pytest

# Streamlit Tests
try:
    import streamlit as st

    STREAMLIT_AVAILABLE = True
except ImportError:
    STREAMLIT_AVAILABLE = False

# Plotly für Charts
try:
    import plotly.express as px
    import plotly.graph_objects as go

    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False

# Import der zu testenden Module
sys.path.append(
    str(Path(__file__).parent.parent / "src" / "08_ui" / "beispiele" / "streamlit")
)


@pytest.mark.skipif(not STREAMLIT_AVAILABLE, reason="Streamlit nicht verfügbar")
class TestStreamlitDataUpload:
    """Tests für Streamlit Daten-Upload."""

    @pytest.fixture
    def sample_csv_data(self):
        """Beispiel CSV-Daten."""
        return """Datum,Maschine,Produktion,Qualität
2024-01-01,Laser_01,245,98.5
2024-01-01,Press_01,180,97.2
2024-01-02,Laser_01,250,99.1
2024-01-02,Press_01,175,96.8"""

    @pytest.fixture
    def sample_json_data(self):
        """Beispiel JSON-Daten."""
        return {
            "machines": [
                {"id": 1, "name": "Laser_01", "type": "Laser", "status": "Active"},
                {"id": 2, "name": "Press_01", "type": "Press", "status": "Maintenance"},
            ],
            "timestamp": "2024-01-01T10:00:00Z",
        }

    def test_csv_file_processing(self, sample_csv_data):
        """Test der CSV-Datei-Verarbeitung."""
        # Simuliere Datei-Upload
        csv_buffer = StringIO(sample_csv_data)
        df = pd.read_csv(csv_buffer)

        assert len(df) == 4
        assert "Datum" in df.columns
        assert "Maschine" in df.columns
        assert "Produktion" in df.columns
        assert "Qualität" in df.columns

        # Test Datentypen
        assert df["Produktion"].dtype in ["int64", "float64"]
        assert df["Qualität"].dtype == "float64"

    def test_json_file_processing(self, sample_json_data):
        """Test der JSON-Datei-Verarbeitung."""
        # Simuliere JSON-Upload
        json_str = json.dumps(sample_json_data)
        data = json.loads(json_str)

        assert "machines" in data
        assert "timestamp" in data
        assert len(data["machines"]) == 2

        # Konvertiere zu DataFrame
        df = pd.DataFrame(data["machines"])
        assert len(df) == 2
        assert "name" in df.columns

    def test_file_validation(self):
        """Test der Datei-Validierung."""

        def validate_csv_structure(df, required_columns):
            """Validiert CSV-Struktur."""
            missing_columns = set(required_columns) - set(df.columns)
            return len(missing_columns) == 0, missing_columns

        # Test mit gültigen Daten
        valid_df = pd.DataFrame(
            {"Datum": ["2024-01-01"], "Maschine": ["Laser_01"], "Produktion": [245]}
        )

        required_cols = ["Datum", "Maschine", "Produktion"]
        is_valid, missing = validate_csv_structure(valid_df, required_cols)
        assert is_valid
        assert len(missing) == 0

        # Test mit fehlenden Spalten
        invalid_df = pd.DataFrame({"Datum": ["2024-01-01"], "Maschine": ["Laser_01"]})

        is_valid, missing = validate_csv_structure(invalid_df, required_cols)
        assert not is_valid
        assert "Produktion" in missing

    def test_data_cleaning(self):
        """Test der Datenbereinigung."""

        def clean_production_data(df):
            """Bereinigt Produktionsdaten."""
            # Entferne Duplikate
            df = df.drop_duplicates()

            # Entferne Zeilen mit fehlenden kritischen Werten
            df = df.dropna(subset=["Maschine", "Produktion"])

            # Konvertiere Datentypen
            if "Produktion" in df.columns:
                df["Produktion"] = pd.to_numeric(df["Produktion"], errors="coerce")

            # Entferne negative Produktionswerte
            if "Produktion" in df.columns:
                df = df[df["Produktion"] >= 0]

            return df

        # Test mit schmutzigen Daten
        dirty_data = pd.DataFrame(
            {
                "Maschine": ["Laser_01", "Press_01", "Laser_01", None, "Cut_01"],
                "Produktion": [245, -10, 245, 180, "invalid"],
                "Qualität": [98.5, 97.2, 98.5, 99.0, 96.8],
            }
        )

        cleaned_data = clean_production_data(dirty_data)

        # Prüfe Bereinigung
        assert len(cleaned_data) < len(dirty_data)  # Zeilen entfernt
        assert cleaned_data["Produktion"].min() >= 0  # Keine negativen Werte
        assert not cleaned_data["Maschine"].isnull().any()  # Keine None-Werte

    @patch("streamlit.file_uploader")
    def test_streamlit_file_upload_mock(self, mock_uploader):
        """Test des Streamlit File-Uploaders (gemockt)."""
        # Simuliere hochgeladene Datei
        mock_file = Mock()
        mock_file.name = "test_data.csv"
        mock_file.read.return_value = (
            b"Datum,Maschine,Produktion\n2024-01-01,Laser_01,245"
        )
        mock_uploader.return_value = mock_file

        # Simuliere Upload-Verarbeitung
        uploaded_file = mock_uploader("Datei hochladen", type=["csv"])
        if uploaded_file:
            content = uploaded_file.read().decode("utf-8")
            df = pd.read_csv(StringIO(content))

            assert len(df) == 1
            assert df.iloc[0]["Maschine"] == "Laser_01"


@pytest.mark.skipif(
    not STREAMLIT_AVAILABLE or not PLOTLY_AVAILABLE,
    reason="Streamlit oder Plotly nicht verfügbar",
)
class TestStreamlitCharts:
    """Tests für Streamlit-Charts."""

    @pytest.fixture
    def sample_time_series_data(self):
        """Beispiel Zeitreihen-Daten."""
        dates = pd.date_range("2024-01-01", periods=30, freq="D")
        return pd.DataFrame(
            {
                "Datum": dates,
                "Produktion": np.random.randint(200, 300, 30),
                "Qualität": np.random.uniform(95, 99.5, 30),
                "Temperatur": np.random.uniform(60, 70, 30),
                "Maschine": np.random.choice(["Laser_01", "Press_01", "Cut_01"], 30),
            }
        )

    def test_line_chart_creation(self, sample_time_series_data):
        """Test der Liniendiagramm-Erstellung."""
        # Erstelle Plotly Line Chart
        fig = px.line(
            sample_time_series_data,
            x="Datum",
            y="Produktion",
            color="Maschine",
            title="Produktionsverlauf",
        )

        assert fig is not None
        assert len(fig.data) > 0
        assert fig.layout.title.text == "Produktionsverlauf"

    def test_bar_chart_creation(self, sample_time_series_data):
        """Test der Balkendiagramm-Erstellung."""
        # Aggregiere Daten für Balkendiagramm
        agg_data = (
            sample_time_series_data.groupby("Maschine")["Produktion"]
            .sum()
            .reset_index()
        )

        fig = px.bar(
            agg_data,
            x="Maschine",
            y="Produktion",
            title="Gesamtproduktion pro Maschine",
        )

        assert fig is not None
        assert len(fig.data) == 1
        assert fig.layout.title.text == "Gesamtproduktion pro Maschine"

    def test_scatter_plot_creation(self, sample_time_series_data):
        """Test der Streudiagramm-Erstellung."""
        fig = px.scatter(
            sample_time_series_data,
            x="Temperatur",
            y="Qualität",
            color="Maschine",
            size="Produktion",
            title="Temperatur vs. Qualität",
        )

        assert fig is not None
        assert len(fig.data) > 0
        assert fig.layout.title.text == "Temperatur vs. Qualität"

    def test_histogram_creation(self, sample_time_series_data):
        """Test der Histogramm-Erstellung."""
        fig = px.histogram(
            sample_time_series_data, x="Qualität", nbins=10, title="Qualitätsverteilung"
        )

        assert fig is not None
        assert len(fig.data) == 1
        assert fig.layout.title.text == "Qualitätsverteilung"

    def test_pie_chart_creation(self, sample_time_series_data):
        """Test der Kreisdiagramm-Erstellung."""
        # Berechne Anteile pro Maschine
        machine_counts = sample_time_series_data["Maschine"].value_counts()

        fig = px.pie(
            values=machine_counts.values,
            names=machine_counts.index,
            title="Maschinenverteilung",
        )

        assert fig is not None
        assert len(fig.data) == 1
        assert fig.layout.title.text == "Maschinenverteilung"

    def test_multi_axis_chart(self, sample_time_series_data):
        """Test von Multi-Achsen-Diagrammen."""
        fig = go.Figure()

        # Erste Y-Achse: Produktion
        fig.add_trace(
            go.Scatter(
                x=sample_time_series_data["Datum"],
                y=sample_time_series_data["Produktion"],
                name="Produktion",
                yaxis="y",
            )
        )

        # Zweite Y-Achse: Qualität
        fig.add_trace(
            go.Scatter(
                x=sample_time_series_data["Datum"],
                y=sample_time_series_data["Qualität"],
                name="Qualität",
                yaxis="y2",
            )
        )

        # Layout mit zwei Y-Achsen
        fig.update_layout(
            title="Produktion und Qualität über Zeit",
            yaxis={"title": "Produktion"},
            yaxis2={"title": "Qualität", "overlaying": "y", "side": "right"},
        )

        assert fig is not None
        assert len(fig.data) == 2
        assert "yaxis2" in fig.layout


@pytest.mark.skipif(not STREAMLIT_AVAILABLE, reason="Streamlit nicht verfügbar")
class TestStreamlitDashboard:
    """Tests für Streamlit-Dashboard."""

    @pytest.fixture
    def dashboard_data(self):
        """Dashboard-Testdaten."""
        return {
            "kpis": {
                "total_production": 15420,
                "avg_quality": 97.8,
                "efficiency": 89.2,
                "downtime_hours": 12.5,
            },
            "machines": [
                {"name": "Laser_01", "status": "Active", "production": 245},
                {"name": "Press_01", "status": "Maintenance", "production": 0},
                {"name": "Cut_01", "status": "Active", "production": 180},
            ],
        }

    def test_kpi_calculation(self, dashboard_data):
        """Test der KPI-Berechnung."""
        kpis = dashboard_data["kpis"]

        # Test KPI-Validierung
        assert kpis["total_production"] > 0
        assert 0 <= kpis["avg_quality"] <= 100
        assert 0 <= kpis["efficiency"] <= 100
        assert kpis["downtime_hours"] >= 0

    def test_machine_status_aggregation(self, dashboard_data):
        """Test der Maschinen-Status-Aggregation."""
        machines = dashboard_data["machines"]

        # Berechne Status-Verteilung
        status_counts = {}
        for machine in machines:
            status = machine["status"]
            status_counts[status] = status_counts.get(status, 0) + 1

        assert status_counts["Active"] == 2
        assert status_counts["Maintenance"] == 1

        # Berechne Gesamtproduktion
        total_production = sum(m["production"] for m in machines)
        assert total_production == 425

    def test_alert_generation(self, dashboard_data):
        """Test der Alert-Generierung."""

        def generate_alerts(data):
            alerts = []

            # Qualitäts-Alert
            if data["kpis"]["avg_quality"] < 95:
                alerts.append(
                    {
                        "type": "warning",
                        "message": "Qualität unter Zielwert",
                        "value": data["kpis"]["avg_quality"],
                    }
                )

            # Effizienz-Alert
            if data["kpis"]["efficiency"] < 85:
                alerts.append(
                    {
                        "type": "warning",
                        "message": "Effizienz unter Zielwert",
                        "value": data["kpis"]["efficiency"],
                    }
                )

            # Wartungs-Alert
            maintenance_machines = [
                m for m in data["machines"] if m["status"] == "Maintenance"
            ]
            if len(maintenance_machines) > 0:
                alerts.append(
                    {
                        "type": "info",
                        "message": f"{len(maintenance_machines)} Maschine(n) in Wartung",
                        "machines": [m["name"] for m in maintenance_machines],
                    }
                )

            return alerts

        alerts = generate_alerts(dashboard_data)

        # Sollte mindestens Wartungs-Alert geben
        assert len(alerts) >= 1
        maintenance_alert = next((a for a in alerts if "Wartung" in a["message"]), None)
        assert maintenance_alert is not None
        assert "Press_01" in maintenance_alert["machines"]

    @patch("streamlit.metric")
    def test_metric_display(self, mock_metric, dashboard_data):
        """Test der Metrik-Anzeige."""
        kpis = dashboard_data["kpis"]

        # Simuliere Metrik-Anzeige
        mock_metric("Gesamtproduktion", kpis["total_production"], "↑ 5%")
        mock_metric(
            "Durchschnittliche Qualität", f"{kpis['avg_quality']:.1f}%", "↑ 0.2%"
        )
        mock_metric("Effizienz", f"{kpis['efficiency']:.1f}%", "↓ 1.1%")

        # Prüfe Mock-Aufrufe
        assert mock_metric.call_count == 3

    def test_data_refresh_simulation(self):
        """Test der Datenaktualisierung."""

        def simulate_real_time_data():
            """Simuliert Echtzeit-Daten."""
            return {
                "timestamp": pd.Timestamp.now(),
                "production_rate": np.random.randint(200, 300),
                "quality": np.random.uniform(95, 99.5),
                "temperature": np.random.uniform(60, 70),
                "status": np.random.choice(["Active", "Idle", "Maintenance"]),
            }

        # Generiere mehrere Datenpunkte
        data_points = [simulate_real_time_data() for _ in range(10)]

        assert len(data_points) == 10
        for point in data_points:
            assert "timestamp" in point
            assert 200 <= point["production_rate"] <= 300
            assert 95 <= point["quality"] <= 99.5
            assert point["status"] in ["Active", "Idle", "Maintenance"]


class TestStreamlitUtilities:
    """Tests für Streamlit-Hilfsfunktionen."""

    def test_session_state_management(self):
        """Test des Session State Managements."""
        # Simuliere Session State
        session_state = {}

        def init_session_state(key, default_value):
            if key not in session_state:
                session_state[key] = default_value
            return session_state[key]

        # Test Initialisierung
        counter = init_session_state("counter", 0)
        assert counter == 0

        # Test Aktualisierung
        session_state["counter"] += 1
        assert session_state["counter"] == 1

        # Test mit komplexen Objekten
        data = init_session_state("data", {"machines": []})
        assert isinstance(data, dict)
        assert "machines" in data

    def test_caching_simulation(self):
        """Test des Caching-Verhaltens."""
        cache = {}

        def cached_data_loader(file_path):
            """Simuliert @st.cache_data Verhalten."""
            if file_path not in cache:
                # Simuliere teure Datenladung
                if file_path.endswith(".csv"):
                    data = pd.DataFrame(
                        {"id": range(1000), "value": np.random.randn(1000)}
                    )
                else:
                    data = {"message": "Daten geladen"}

                cache[file_path] = data

            return cache[file_path]

        # Erste Ladung
        data1 = cached_data_loader("test.csv")
        assert len(data1) == 1000
        assert "test.csv" in cache

        # Zweite Ladung (aus Cache)
        data2 = cached_data_loader("test.csv")
        assert data1 is data2  # Gleiche Referenz

    def test_form_validation(self):
        """Test der Formular-Validierung."""

        def validate_machine_form(form_data):
            """Validiert Maschinen-Formulardaten."""
            errors = []

            # Name-Validierung
            if not form_data.get("name"):
                errors.append("Name ist erforderlich")
            elif len(form_data["name"]) < 3:
                errors.append("Name muss mindestens 3 Zeichen haben")

            # Typ-Validierung
            valid_types = ["Laser", "Press", "Cutter", "Bender"]
            if form_data.get("type") not in valid_types:
                errors.append(f"Typ muss einer von {valid_types} sein")

            # Produktionsrate-Validierung
            if "production_rate" in form_data:
                try:
                    rate = float(form_data["production_rate"])
                    if rate < 0:
                        errors.append("Produktionsrate kann nicht negativ sein")
                    elif rate > 1000:
                        errors.append("Produktionsrate scheint unrealistisch hoch")
                except (ValueError, TypeError):
                    errors.append("Produktionsrate muss eine Zahl sein")

            return len(errors) == 0, errors

        # Test gültige Daten
        valid_form = {"name": "Laser_01", "type": "Laser", "production_rate": "245.5"}

        is_valid, errors = validate_machine_form(valid_form)
        assert is_valid
        assert len(errors) == 0

        # Test ungültige Daten
        invalid_form = {
            "name": "L",  # Zu kurz
            "type": "Invalid",  # Ungültiger Typ
            "production_rate": "-10",  # Negativ
        }

        is_valid, errors = validate_machine_form(invalid_form)
        assert not is_valid
        assert len(errors) == 3

    def test_data_export_utilities(self):
        """Test der Datenexport-Hilfsfunktionen."""

        def prepare_export_data(df, format_type="csv"):
            """Bereitet Daten für Export vor."""
            if format_type == "csv":
                buffer = StringIO()
                df.to_csv(buffer, index=False)
                return buffer.getvalue()

            elif format_type == "json":
                return df.to_json(orient="records", indent=2)

            elif format_type == "excel":
                buffer = BytesIO()
                df.to_excel(buffer, index=False, engine="openpyxl")
                return buffer.getvalue()

            else:
                raise ValueError(f"Unsupported format: {format_type}")

        # Test-DataFrame
        test_df = pd.DataFrame(
            {
                "Maschine": ["Laser_01", "Press_01"],
                "Produktion": [245, 180],
                "Qualität": [98.5, 97.2],
            }
        )

        # Test CSV-Export
        csv_data = prepare_export_data(test_df, "csv")
        assert "Maschine,Produktion,Qualität" in csv_data
        assert "Laser_01,245,98.5" in csv_data

        # Test JSON-Export
        json_data = prepare_export_data(test_df, "json")
        parsed_json = json.loads(json_data)
        assert len(parsed_json) == 2
        assert parsed_json[0]["Maschine"] == "Laser_01"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
