#!/usr/bin/env python3
"""
Pytest-Konfiguration für Bystronic Python Grundkurs Tests

Diese Datei enthält gemeinsame Fixtures und Konfigurationen
für alle Tests im Projekt.
"""

import tempfile
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


@pytest.fixture
def beispiele_path():
    """Fixture für den Pfad zu den Beispieldateien"""
    return Path(__file__).parent.parent / "src"


@pytest.fixture
def sample_maschinendaten():
    """Fixture für Beispiel-Maschinendaten"""
    return {
        "Maschine": ["LASER_01", "LASER_02", "PRESSE_01", "PRESSE_02", "STANZE_01"],
        "Typ": ["ByStar", "ByStar", "Xpert", "Xpert", "ByTrans"],
        "Baujahr": [2019, 2020, 2018, 2021, 2017],
        "Produktionszeit_h": [2450.5, 1890.2, 3200.8, 1250.4, 2890.1],
        "Wartung_fällig": [True, False, True, False, True],
        "Ausschussrate": [0.023, 0.045, 0.012, 0.067, 0.034],
    }


@pytest.fixture
def sample_dataframe(sample_maschinendaten):
    """Fixture für ein Beispiel-DataFrame"""
    return pd.DataFrame(sample_maschinendaten)


@pytest.fixture
def temp_csv_file():
    """Fixture für temporäre CSV-Datei"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as tmp:
        yield tmp.name


@pytest.fixture
def temp_json_file():
    """Fixture für temporäre JSON-Datei"""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tmp:
        yield tmp.name


@pytest.fixture
def produktionsdaten_sample():
    """Fixture für Beispiel-Produktionsdaten"""
    np.random.seed(42)  # Für reproduzierbare Tests

    data = []
    maschinen = ["LASER_01", "LASER_02", "PRESSE_01"]

    for woche in range(1, 5):
        for maschine in maschinen:
            data.append(
                {
                    "Woche": woche,
                    "Maschine": maschine,
                    "Geplante_Zeit": 40.0,
                    "Tatsächliche_Zeit": 40.0 + np.random.normal(0, 2),
                    "Teile_produziert": 1000 + np.random.randint(-100, 100),
                    "Ausschuss": np.random.randint(5, 25),
                }
            )

    return pd.DataFrame(data)


@pytest.fixture(autouse=True)
def setup_test_environment():
    """Automatische Fixture für Test-Umgebung Setup"""
    # Seed für reproduzierbare Tests setzen
    np.random.seed(42)

    # Pandas-Optionen für Tests
    pd.set_option("display.max_columns", None)
    pd.set_option("display.width", None)

    yield

    # Cleanup nach Tests
    pd.reset_option("display.max_columns")
    pd.reset_option("display.width")


# Marker für verschiedene Test-Kategorien
def pytest_configure(config):
    """Pytest-Konfiguration mit benutzerdefinierten Markern"""
    config.addinivalue_line("markers", "grundlagen: Tests für Python-Grundlagen")
    config.addinivalue_line(
        "markers", "datentypen: Tests für Datentypen und Operationen"
    )
    config.addinivalue_line("markers", "pandas: Tests für Pandas-Funktionalität")
    config.addinivalue_line("markers", "integration: Integrationstests")
    config.addinivalue_line("markers", "slow: Langsame Tests")


# Hilfsfunktionen für Tests
def assert_dataframe_equal_ignore_index(df1, df2):
    """Vergleicht DataFrames und ignoriert Index-Unterschiede"""
    df1_reset = df1.reset_index(drop=True)
    df2_reset = df2.reset_index(drop=True)
    pd.testing.assert_frame_equal(df1_reset, df2_reset)


def create_test_maschinendaten_csv(filepath, data=None):
    """Erstellt eine Test-CSV-Datei mit Maschinendaten"""
    if data is None:
        data = {
            "Maschine": ["LASER_01", "PRESSE_01"],
            "Produktionszeit": [2450.5, 3200.8],
            "Status": ["Aktiv", "Wartung"],
        }

    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False, encoding="utf-8")
    return filepath
