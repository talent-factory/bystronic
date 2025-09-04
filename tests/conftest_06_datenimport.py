#!/usr/bin/env python3
"""
Test-Fixtures für Modul 06: Datenimport und -export

Diese Datei stellt wiederverwendbare Test-Fixtures bereit, die von allen
Tests im Datenimport-Modul verwendet werden können. Fixtures sorgen für
konsistente und isolierte Test-Umgebungen.

Autor: Python Grundkurs Bystronic
"""

import pytest
import pandas as pd
import numpy as np
import json
import tempfile
from pathlib import Path
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')


@pytest.fixture(scope="session")
def test_data_directory():
    """
    Erstellt ein temporäres Verzeichnis für Test-Daten.
    Wird einmal pro Test-Session erstellt und am Ende aufgeräumt.
    """
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)
        yield temp_path


@pytest.fixture
def sample_csv_data():
    """
    Standard Test-DataFrame für CSV-Tests
    """
    np.random.seed(42)  # Für reproduzierbare Ergebnisse
    
    dates = pd.date_range('2024-01-01', periods=100, freq='D')
    machines = ['Maschine_A', 'Maschine_B', 'Maschine_C']
    
    return pd.DataFrame({
        'Datum': dates,
        'Maschine': np.random.choice(machines, 100),
        'Produktion': np.random.randint(800, 1200, 100),
        'Temperatur': np.round(np.random.normal(23, 3, 100), 1),
        'Verfügbarkeit': np.round(np.random.uniform(80, 95, 100), 1),
        'Status': np.random.choice(['OK', 'WARNING', 'ERROR'], 100, p=[0.8, 0.15, 0.05])
    })


@pytest.fixture
def dirty_data():
    """
    DataFrame mit verschiedenen Datenproblemen für Bereinigungstests
    """
    return pd.DataFrame({
        'Maschine': ['A', 'B', 'C', 'A', 'B', 'A', 'B'],  # Duplikat-Kandidaten
        'Produktion': [1000, -50, 1200, np.nan, 2000, 1000, -50],  # Negative Werte, NaN, Duplikate
        'Temperatur': [22.5, 150.0, 23.1, 22.8, -999, 22.5, 150.0],  # Unrealistische Werte
        'Verfügbarkeit': [85.2, 120.0, 88.5, 92.1, -10, 85.2, 120.0],  # >100%, negative Werte
        'Status': ['OK', 'OK', '', 'WARNING', 'ERROR', 'OK', 'OK'],  # Leere Strings
        'Kommentar': ['Normal', None, 'Test', '', 'Fehler', 'Normal', None]  # Gemischte Missing Values
    })


@pytest.fixture
def sample_csv_files(test_data_directory, sample_csv_data):
    """
    Erstellt verschiedene CSV-Test-Dateien
    """
    files = {}
    
    # Standard CSV (Komma-getrennt)
    standard_file = test_data_directory / "standard.csv"
    sample_csv_data.to_csv(standard_file, index=False, encoding='utf-8')
    files['standard'] = standard_file
    
    # Deutsches Format (Semikolon-getrennt, Komma als Dezimaltrenner)
    german_file = test_data_directory / "german.csv"
    sample_csv_data.to_csv(german_file, index=False, sep=';', decimal=',', encoding='utf-8')
    files['german'] = german_file
    
    # Tab-getrennt
    tab_file = test_data_directory / "tab_separated.csv"
    sample_csv_data.to_csv(tab_file, index=False, sep='\t', encoding='utf-8')
    files['tab'] = tab_file
    
    # Mit Encoding-Problemen (Latin-1)
    latin1_file = test_data_directory / "latin1.csv"
    sample_data_latin1 = sample_csv_data.copy()
    sample_data_latin1.loc[0, 'Status'] = 'Größe'  # Umlaut für Encoding-Test
    sample_data_latin1.to_csv(latin1_file, index=False, encoding='latin-1')
    files['latin1'] = latin1_file
    
    # Problematische CSV mit Mixed Content
    problem_content = """Maschine;Produktion;Temperatur;Status
A;1000;23,5;OK
B;;24,1;OK
C;950;;WARNING
D;1100;22,8;
E;FEHLER;25,0;ERROR"""
    
    problem_file = test_data_directory / "problematic.csv"
    problem_file.write_text(problem_content, encoding='utf-8')
    files['problematic'] = problem_file
    
    return files


@pytest.fixture
def bystronic_csv_mock():
    """
    Mock-Content für Bystronic CSV im V084_Scope Format
    """
    content = """Name	Distance Control
File	O:\\Messungen\\NDC\\Test_V084_Scope.csv
Starttime of export	133964386997165000	Montag, 1. Januar 2024	10:00:00.000
Endtime of export	133964388292505000	Montag, 1. Januar 2024	10:30:00.000
Duration of export	0:30:02.505


Name	TEMP_001	Name	VIBR_001	Name	POWER_001	Name	STATUS_001
SymbolComment		SymbolComment		SymbolComment		SymbolComment	
Data-Type	REAL64	Data-Type	REAL64	Data-Type	REAL64	Data-Type	UINT16
SampleTime[ms]	1	SampleTime[ms]	1	SampleTime[ms]	1	SampleTime[ms]	1
VariableSize	8	VariableSize	8	VariableSize	8	VariableSize	2
SymbolBased	False	SymbolBased	False	SymbolBased	False	SymbolBased	False
IndexGroup	1180416	IndexGroup	1180416	IndexGroup	1180416	IndexGroup	1180416
IndexOffset	328147	IndexOffset	328158	IndexOffset	328020	IndexOffset	328023
SymbolName	TEMP::sensor_1	SymbolName	VIBR::sensor_1	SymbolName	POWER::sensor_1	SymbolName	STATUS::machine_1
NetID	192.168.1.1.1.1	NetID	192.168.1.1.1.1	NetID	192.168.1.1.1.1	NetID	192.168.1.1.1.1
Port	551	Port	551	Port	551	Port	551
Offset	0	Offset	0	Offset	0	Offset	0
ScaleFactor	1	ScaleFactor	1	ScaleFactor	1	ScaleFactor	1
BitMask	0xffffffffffffffff	BitMask	0xffffffffffffffff	BitMask	0xffffffffffffffff	BitMask	0xffff

0	22.5	0	1.2	0	6.2	0	1
1	22.8	1	1.4	1	6.0	1	1
2	23.1	2	2.1	2	5.8	2	1
3	23.4	3	2.8	3	5.5	3	2
4	23.0	4	1.5	4	6.1	4	1
5	22.7	5	1.3	5	6.3	5	1"""
    
    return content


@pytest.fixture
def bystronic_csv_file(test_data_directory, bystronic_csv_mock):
    """
    Erstellt eine Mock Bystronic CSV-Datei
    """
    csv_file = test_data_directory / "bystronic_mock.csv"
    csv_file.write_text(bystronic_csv_mock, encoding='utf-8')
    return csv_file


@pytest.fixture
def sample_excel_data():
    """
    Sample-Daten für Excel-Tests mit verschiedenen Arbeitsblättern
    """
    np.random.seed(42)
    
    # Produktionsdaten
    production_dates = pd.date_range('2024-01-01', periods=365, freq='D')
    production_data = pd.DataFrame({
        'Datum': production_dates,
        'Maschine_A_Stück': np.random.randint(800, 1200, 365),
        'Maschine_B_Stück': np.random.randint(700, 1100, 365),
        'Maschine_C_Stück': np.random.randint(900, 1300, 365),
        'Verfügbarkeit_A_%': np.round(np.random.uniform(80, 95, 365), 1),
        'Verfügbarkeit_B_%': np.round(np.random.uniform(75, 90, 365), 1),
        'Verfügbarkeit_C_%': np.round(np.random.uniform(85, 95, 365), 1),
        'Gesamttemperatur_°C': np.round(np.random.normal(23, 3, 365), 1)
    })
    
    # Qualitätsdaten (monatlich)
    quality_dates = pd.date_range('2024-01-01', periods=12, freq='M')
    quality_data = pd.DataFrame({
        'Monat': quality_dates,
        'Ausschuss_Rate_%': np.round(np.random.uniform(1.5, 3.0, 12), 2),
        'Nacharbeit_Rate_%': np.round(np.random.uniform(0.8, 2.0, 12), 2),
        'Kundenzufriedenheit': np.round(np.random.uniform(4.0, 4.5, 12), 1),
        'Reklamationen_Anzahl': np.random.poisson(3, 12)
    })
    
    # Wartungsdaten
    maintenance_dates = pd.date_range('2024-01-01', periods=50, freq='W')
    maintenance_data = pd.DataFrame({
        'Datum': maintenance_dates[:50],
        'Maschine': np.random.choice(['A', 'B', 'C'], 50),
        'Wartungstyp': np.random.choice(['Präventiv', 'Korrektiv', 'Inspektion'], 50),
        'Dauer_Stunden': np.round(np.random.exponential(2.5, 50), 1),
        'Kosten_EUR': np.round(np.random.gamma(2, 300, 50), 2),
        'Techniker': np.random.choice(['Schmidt', 'Müller', 'Weber', 'Fischer'], 50)
    })
    
    return {
        'Produktion': production_data,
        'Qualität': quality_data,
        'Wartung': maintenance_data
    }


@pytest.fixture
def sample_excel_file(test_data_directory, sample_excel_data):
    """
    Erstellt eine Excel-Datei mit mehreren Arbeitsblättern
    """
    excel_file = test_data_directory / "bystronic_test_data.xlsx"
    
    with pd.ExcelWriter(excel_file, engine='openpyxl') as writer:
        for sheet_name, df in sample_excel_data.items():
            df.to_excel(writer, sheet_name=sheet_name, index=False)
    
    return excel_file


@pytest.fixture
def sample_json_data():
    """
    Sample IoT-Sensordaten im JSON-Format
    """
    return {
        "metadata": {
            "system": "Bystronic IoT Platform",
            "version": "2.1.0", 
            "timestamp": "2024-01-15T08:30:00Z",
            "location": "Werk_Niederönz",
            "export_id": "EXP_2024_001"
        },
        "sensors": [
            {
                "id": "TEMP_001",
                "type": "temperature",
                "location": "Laser_Cutting_1",
                "unit": "celsius",
                "calibration_date": "2024-01-01",
                "readings": [
                    {"timestamp": "2024-01-15T08:30:00Z", "value": 22.5, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:31:00Z", "value": 22.8, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:32:00Z", "value": 23.1, "status": "ok", "quality": 95},
                    {"timestamp": "2024-01-15T08:33:00Z", "value": 23.4, "status": "warning", "quality": 90},
                    {"timestamp": "2024-01-15T08:34:00Z", "value": 23.7, "status": "warning", "quality": 85}
                ]
            },
            {
                "id": "VIBR_001", 
                "type": "vibration",
                "location": "Laser_Cutting_1",
                "unit": "mm/s",
                "calibration_date": "2024-01-01",
                "readings": [
                    {"timestamp": "2024-01-15T08:30:00Z", "value": 1.2, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:31:00Z", "value": 1.4, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:32:00Z", "value": 2.1, "status": "warning", "quality": 90},
                    {"timestamp": "2024-01-15T08:33:00Z", "value": 2.8, "status": "error", "quality": 70},
                    {"timestamp": "2024-01-15T08:34:00Z", "value": 3.2, "status": "error", "quality": 60}
                ]
            },
            {
                "id": "POWER_001",
                "type": "power", 
                "location": "Laser_Cutting_1",
                "unit": "kW",
                "calibration_date": "2024-01-01",
                "readings": [
                    {"timestamp": "2024-01-15T08:30:00Z", "value": 6.2, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:31:00Z", "value": 6.0, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:32:00Z", "value": 5.8, "status": "ok", "quality": 98},
                    {"timestamp": "2024-01-15T08:33:00Z", "value": 5.5, "status": "ok", "quality": 95},
                    {"timestamp": "2024-01-15T08:34:00Z", "value": 5.9, "status": "ok", "quality": 100}
                ]
            },
            {
                "id": "PRESS_001",
                "type": "pressure",
                "location": "Hydraulic_System",
                "unit": "bar",
                "calibration_date": "2024-01-01", 
                "readings": [
                    {"timestamp": "2024-01-15T08:30:00Z", "value": 150.2, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:31:00Z", "value": 149.8, "status": "ok", "quality": 100},
                    {"timestamp": "2024-01-15T08:32:00Z", "value": 151.1, "status": "ok", "quality": 98},
                    {"timestamp": "2024-01-15T08:33:00Z", "value": 148.9, "status": "warning", "quality": 85},
                    {"timestamp": "2024-01-15T08:34:00Z", "value": 147.5, "status": "warning", "quality": 80}
                ]
            }
        ],
        "alerts": [
            {
                "id": "ALT_001",
                "timestamp": "2024-01-15T08:33:00Z",
                "severity": "high",
                "sensor_id": "VIBR_001",
                "message": "Vibration level exceeds threshold",
                "threshold_value": 2.5,
                "actual_value": 2.8,
                "acknowledged": False,
                "operator": None
            },
            {
                "id": "ALT_002",
                "timestamp": "2024-01-15T08:33:00Z",
                "severity": "medium",
                "sensor_id": "PRESS_001",
                "message": "Pressure below optimal range",
                "threshold_value": 150.0,
                "actual_value": 148.9,
                "acknowledged": True,
                "operator": "Schmidt"
            }
        ],
        "system_status": {
            "overall_health": "warning",
            "active_alerts": 2,
            "sensors_online": 4,
            "sensors_offline": 0,
            "last_maintenance": "2024-01-10T14:30:00Z"
        }
    }


@pytest.fixture  
def sample_json_file(test_data_directory, sample_json_data):
    """
    Erstellt eine JSON-Datei mit IoT-Sensordaten
    """
    json_file = test_data_directory / "sensor_data.json"
    
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(sample_json_data, f, indent=2, ensure_ascii=False)
    
    return json_file


@pytest.fixture
def large_dataset():
    """
    Großer Datensatz für Performance-Tests
    """
    np.random.seed(42)
    size = 100000  # 100k Zeilen für Performance-Tests
    
    return pd.DataFrame({
        'ID': range(size),
        'Timestamp': pd.date_range('2024-01-01', periods=size, freq='1min'),
        'Maschine': np.random.choice(['A', 'B', 'C', 'D', 'E'], size),
        'Sensor_1': np.random.normal(100, 15, size),
        'Sensor_2': np.random.normal(50, 8, size),  
        'Sensor_3': np.random.exponential(2, size),
        'Status': np.random.choice(['OK', 'WARNING', 'ERROR', 'MAINTENANCE'], size, p=[0.85, 0.10, 0.03, 0.02]),
        'Kategorie': np.random.choice(['Production', 'Quality', 'Maintenance'], size, p=[0.7, 0.2, 0.1])
    })


@pytest.fixture
def performance_csv_file(test_data_directory, large_dataset):
    """
    Große CSV-Datei für Performance-Tests
    """
    csv_file = test_data_directory / "large_performance_test.csv"
    large_dataset.to_csv(csv_file, index=False)
    return csv_file


@pytest.fixture
def expected_kpis():
    """
    Erwartete KPI-Werte für Validierungstests
    """
    return {
        'total_production_range': (250000, 350000),  # Erwarteter Bereich für Gesamtproduktion
        'avg_availability_range': (75, 95),          # Erwarteter Verfügbarkeitsbereich in %
        'temperature_range': (15, 35),               # Erwarteter Temperaturbereich in °C
        'min_daily_production': 500,                 # Minimum Tagesproduktion pro Maschine
        'max_daily_production': 1500,                # Maximum Tagesproduktion pro Maschine
        'acceptable_error_rate': 0.1,               # Maximal akzeptable Fehlerrate (10%)
        'min_data_completeness': 0.95               # Mindest-Vollständigkeit der Daten (95%)
    }


@pytest.fixture
def sample_api_responses():
    """
    Mock API-Responses für API-Integration Tests
    """
    return {
        'production': {
            "status": "success",
            "timestamp": "2024-01-15T10:30:00Z",
            "data": {
                "machines": [
                    {
                        "id": "LC001",
                        "name": "Laser_Cutting_1",
                        "status": "running", 
                        "current_job": "JOB_2024_001",
                        "parts_produced_today": 1050,
                        "efficiency": 92.5,
                        "temperature": 23.2,
                        "last_update": "2024-01-15T10:29:45Z"
                    },
                    {
                        "id": "LC002", 
                        "name": "Laser_Cutting_2",
                        "status": "maintenance",
                        "current_job": None,
                        "parts_produced_today": 0,
                        "efficiency": 0,
                        "temperature": 19.8,
                        "last_update": "2024-01-15T08:15:30Z"
                    },
                    {
                        "id": "BR001",
                        "name": "Press_Brake_1", 
                        "status": "running",
                        "current_job": "JOB_2024_002",
                        "parts_produced_today": 875,
                        "efficiency": 88.3,
                        "temperature": 26.1,
                        "last_update": "2024-01-15T10:29:50Z"
                    }
                ],
                "summary": {
                    "total_parts_today": 1925,
                    "active_machines": 2,
                    "overall_efficiency": 90.4,
                    "average_temperature": 23.0
                }
            }
        },
        'quality': {
            "status": "success",
            "timestamp": "2024-01-15T10:30:00Z",
            "data": {
                "daily_summary": {
                    "total_parts": 2450,
                    "defective_parts": 35,
                    "defect_rate": 1.43,
                    "rework_rate": 0.8,
                    "scrap_rate": 0.63
                },
                "defect_types": [
                    {"type": "dimensional", "count": 15, "percentage": 42.9},
                    {"type": "surface", "count": 12, "percentage": 34.3},
                    {"type": "material", "count": 8, "percentage": 22.8}
                ],
                "trends": {
                    "defect_rate_trend": -0.12,  # Verbesserung
                    "rework_trend": 0.05,        # Leichte Verschlechterung  
                    "quality_score": 97.2
                }
            }
        },
        'error_response': {
            "status": "error",
            "error_code": "UNAUTHORIZED",
            "message": "Invalid API key or expired token",
            "timestamp": "2024-01-15T10:30:00Z"
        },
        'timeout_simulation': {
            "status": "timeout",
            "message": "Request timed out after 30 seconds"
        }
    }


@pytest.fixture  
def validation_test_cases():
    """
    Test-Cases für Datenvalidierung mit erwarteten Ergebnissen
    """
    return [
        {
            'name': 'negative_production',
            'data': pd.DataFrame({'Produktion': [-100, 1000, 500]}),
            'expected_issues': ['Negative Produktionswerte gefunden'],
            'should_fail': True
        },
        {
            'name': 'extreme_temperature',
            'data': pd.DataFrame({'Temperatur': [-60, 25, 250]}),
            'expected_issues': ['Unrealistische Temperaturwerte'],
            'should_fail': True
        },
        {
            'name': 'invalid_availability', 
            'data': pd.DataFrame({'Verfügbarkeit': [85, 120, -5]}),
            'expected_issues': ['Verfügbarkeit außerhalb gültigen Bereichs'],
            'should_fail': True
        },
        {
            'name': 'valid_data',
            'data': pd.DataFrame({
                'Produktion': [800, 1000, 1200],
                'Temperatur': [20, 25, 30],
                'Verfügbarkeit': [85, 90, 95]
            }),
            'expected_issues': [],
            'should_fail': False
        }
    ]


@pytest.fixture
def export_format_configs():
    """
    Konfigurationen für verschiedene Export-Formate
    """
    return {
        'csv': {
            'extension': '.csv',
            'params': {'index': False, 'encoding': 'utf-8'},
            'expected_size_range': (1024, 1024*1024)  # 1KB bis 1MB für Testdaten
        },
        'excel': {
            'extension': '.xlsx',
            'params': {'index': False},
            'expected_size_range': (2048, 2*1024*1024),  # 2KB bis 2MB
            'sheets': ['Daten', 'Statistiken', 'Metadaten']
        },
        'json': {
            'extension': '.json',
            'params': {'indent': 2, 'ensure_ascii': False, 'default': str},
            'expected_size_range': (1024, 5*1024*1024),  # 1KB bis 5MB
            'required_keys': ['metadata', 'data']
        },
        'parquet': {
            'extension': '.parquet',
            'params': {'index': False, 'compression': 'snappy'},
            'expected_size_range': (512, 512*1024),  # 512B bis 512KB (compressed)
            'optional': True  # Nur wenn pyarrow verfügbar
        }
    }


# Utility-Funktionen für Tests

def create_temp_file(directory, filename, content, encoding='utf-8'):
    """
    Hilfsfunktion zum Erstellen temporärer Dateien
    """
    file_path = Path(directory) / filename
    if isinstance(content, str):
        file_path.write_text(content, encoding=encoding)
    elif isinstance(content, bytes):
        file_path.write_bytes(content)
    else:
        raise ValueError("Content must be string or bytes")
    return file_path


def assert_dataframe_quality(df, min_rows=1, required_columns=None, allow_na=True):
    """
    Hilfsfunktion für DataFrame-Qualitätsprüfungen
    """
    assert len(df) >= min_rows, f"DataFrame hat nur {len(df)} Zeilen, erwartet mindestens {min_rows}"
    
    if required_columns:
        missing_cols = set(required_columns) - set(df.columns)
        assert not missing_cols, f"Fehlende Spalten: {missing_cols}"
    
    if not allow_na:
        na_count = df.isnull().sum().sum()
        assert na_count == 0, f"DataFrame enthält {na_count} NaN-Werte"


def validate_file_structure(file_path, expected_extension=None, min_size=0, max_size=None):
    """
    Validiert grundlegende Dateieigenschaften
    """
    file_path = Path(file_path)
    
    assert file_path.exists(), f"Datei existiert nicht: {file_path}"
    
    if expected_extension:
        assert file_path.suffix == expected_extension, f"Falsche Erweiterung: {file_path.suffix}, erwartet {expected_extension}"
    
    file_size = file_path.stat().st_size
    assert file_size >= min_size, f"Datei zu klein: {file_size} Bytes, erwartet mindestens {min_size}"
    
    if max_size:
        assert file_size <= max_size, f"Datei zu groß: {file_size} Bytes, maximum {max_size}"
    
    return file_size


# Cleanup Helpers

@pytest.fixture(autouse=True)
def cleanup_warnings():
    """
    Automatisches Cleanup von Warnings nach jedem Test
    """
    yield
    warnings.resetwarnings()


@pytest.fixture
def memory_monitor():
    """
    Überwacht Memory-Usage für Performance-Tests
    """
    import psutil
    import os
    
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024  # MB
    
    yield initial_memory
    
    final_memory = process.memory_info().rss / 1024 / 1024  # MB
    memory_diff = final_memory - initial_memory
    
    # Warnung bei Memory-Leaks > 100MB
    if memory_diff > 100:
        pytest.warn(f"Möglicher Memory-Leak: {memory_diff:.1f} MB zusätzlich verwendet")


# Test-Parameter für parametrized Tests

CSV_SEPARATORS = [',', ';', '\t', '|']
ENCODINGS = ['utf-8', 'latin-1', 'cp1252']
EXCEL_ENGINES = ['openpyxl']  # xlrd für .xls-Dateien wurde deprecated
JSON_ORIENTATIONS = ['records', 'index', 'values', 'split', 'table']
EXPORT_FORMATS = ['csv', 'excel', 'json']  # parquet optional

# Erweiterte Test-Konfiguration
TEST_CONFIG = {
    'performance': {
        'max_import_time': 10.0,      # Sekunden für große Datei-Imports
        'max_export_time': 15.0,      # Sekunden für Multi-Format-Exports  
        'max_memory_usage': 500.0,    # MB für Memory-Tests
        'chunk_sizes': [1000, 5000, 10000, 50000]  # Verschiedene Chunk-Größen
    },
    'data_quality': {
        'max_missing_percentage': 10.0,  # Maximal 10% fehlende Werte
        'outlier_threshold': 3.0,        # Z-Score Threshold für Ausreißer
        'min_data_completeness': 0.95    # 95% Vollständigkeit erforderlich
    },
    'validation_rules': {
        'temperature_range': (-50, 200),   # °C
        'production_range': (0, 10000),    # Stück pro Tag
        'availability_range': (0, 100),    # Prozent
        'pressure_range': (0, 1000)        # bar
    }
}