#!/usr/bin/env python3
"""
Tests für Modul 06: Datenimport und -export

Diese Tests überprüfen alle Funktionalitäten des Datenimport-Moduls:
- CSV-Import mit komplexen Strukturen
- Excel-Verarbeitung mit mehreren Arbeitsblättern
- JSON-Datenverarbeitung
- Bystronic CSV Parser
- Datenbereinigung
- Export-Funktionen

Autor: Python Grundkurs Bystronic
"""

import json
import sys
import tempfile
import warnings
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

warnings.filterwarnings("ignore")

# Pfad zu den Beispielen hinzufügen
beispiele_path = Path(__file__).parent.parent / "src" / "06_datenimport" / "beispiele"
sys.path.insert(0, str(beispiele_path))

# Module importieren
try:
    import csv_import_grundlagen
    from bystronic_csv_parser import BystronicCSVParser
    from csv_import_grundlagen import (
        csv_import_beispiele,
        csv_performance_optimierung,
        csv_probleme_loesen,
        visualisiere_csv_daten,
    )
    from excel_verarbeitung import BystronicExcelHandler
except ImportError as e:
    pytest.skip(
        f"Datenimport Beispiele können nicht importiert werden: {e}",
        allow_module_level=True,
    )


class TestCSVImportGrundlagen:
    """Tests für CSV-Import Grundlagen"""

    def setup_method(self):
        """Setup für jeden Test"""
        self.temp_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Cleanup nach jedem Test"""
        import shutil

        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def test_csv_import_beispiele(self):
        """Test der grundlegenden CSV-Import-Beispiele"""
        with patch("csv_import_grundlagen.get_data_path") as mock_path:
            mock_path.side_effect = lambda *args: self.temp_dir / Path(*args)

            # Führe die Import-Beispiele aus
            result = csv_import_beispiele()

            # Prüfe dass alle erwarteten DataFrames zurückgegeben wurden
            assert isinstance(result, dict)
            expected_keys = ["standard", "semicolon", "tab", "subset", "typed"]
            for key in expected_keys:
                assert key in result
                assert isinstance(result[key], pd.DataFrame)
                assert len(result[key]) > 0

    def test_csv_trennzeichen_verarbeitung(self):
        """Test verschiedener CSV-Trennzeichen"""
        # Testdaten mit verschiedenen Trennzeichen
        test_data = "Name,Wert,Einheit\nTemperatur,23.5,°C\nDruck,5.2,bar\n"

        csv_file = self.temp_dir / "test_comma.csv"
        csv_file.write_text(test_data, encoding="utf-8")

        # Test Komma-getrennt
        df_comma = pd.read_csv(csv_file, sep=",")
        assert df_comma.shape == (2, 3)
        assert "Temperatur" in df_comma["Name"].values

        # Test Semikolon-getrennt
        test_data_semi = test_data.replace(",", ";")
        csv_file_semi = self.temp_dir / "test_semi.csv"
        csv_file_semi.write_text(test_data_semi, encoding="utf-8")

        df_semi = pd.read_csv(csv_file_semi, sep=";")
        assert df_semi.shape == (2, 3)
        assert "Temperatur" in df_semi["Name"].values

    def test_csv_encoding_behandlung(self):
        """Test verschiedener Encodings"""
        # Deutsche Umlaute in verschiedenen Encodings
        test_data_utf8 = "Maschine,Größe,Qualität\nA,Groß,Ausgezeichnet\n"
        test_data_latin1 = test_data_utf8

        # UTF-8 Test
        csv_file_utf8 = self.temp_dir / "test_utf8.csv"
        csv_file_utf8.write_text(test_data_utf8, encoding="utf-8")

        df_utf8 = pd.read_csv(csv_file_utf8, encoding="utf-8")
        assert "Größe" in df_utf8.columns
        assert "Ausgezeichnet" in df_utf8["Qualität"].values

        # Latin-1 Test
        csv_file_latin1 = self.temp_dir / "test_latin1.csv"
        csv_file_latin1.write_text(test_data_latin1, encoding="latin-1")

        df_latin1 = pd.read_csv(csv_file_latin1, encoding="latin-1")
        assert "Größe" in df_latin1.columns

    def test_csv_fehlende_werte(self):
        """Test der Behandlung fehlender Werte"""
        test_data = "Maschine,Produktion,Temperatur\nA,1000,23.5\nB,,24.1\nC,950,\n"

        csv_file = self.temp_dir / "test_missing.csv"
        csv_file.write_text(test_data, encoding="utf-8")

        df = pd.read_csv(csv_file)

        # Prüfe fehlende Werte
        assert df.isnull().sum().sum() == 2
        assert df["Produktion"].isnull().sum() == 1
        assert df["Temperatur"].isnull().sum() == 1

        # Test verschiedene Behandlungsstrategien
        df_dropped = df.dropna()
        assert len(df_dropped) == 1

        df_filled = df.fillna(
            {
                "Produktion": df["Produktion"].mean(),
                "Temperatur": df["Temperatur"].mean(),
            }
        )
        assert df_filled.isnull().sum().sum() == 0

    def test_csv_performance_optimierung(self):
        """Test der Performance-Optimierungen"""
        # Erstelle eine größere Test-CSV
        large_data = {
            "ID": range(1000),
            "Wert1": np.random.randn(1000),
            "Wert2": np.random.randn(1000),
            "Kategorie": np.random.choice(["A", "B", "C"], 1000),
        }
        df_large = pd.DataFrame(large_data)

        csv_file = self.temp_dir / "large_test.csv"
        df_large.to_csv(csv_file, index=False)

        # Test Chunked Reading
        chunks = []
        for chunk in pd.read_csv(csv_file, chunksize=100):
            chunks.append(chunk)
            if len(chunks) >= 3:  # Nur erste 3 Chunks für Test
                break

        df_chunked = pd.concat(chunks, ignore_index=True)
        assert len(df_chunked) == 300

        # Test optimierte Datentypen
        dtypes = {"Kategorie": "category"}
        df_optimized = pd.read_csv(csv_file, dtype=dtypes)
        assert df_optimized["Kategorie"].dtype.name == "category"


class TestBystronicCSVParser:
    """Tests für den Bystronic CSV Parser"""

    def setup_method(self):
        """Setup für jeden Test"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.parser = BystronicCSVParser()

    def teardown_method(self):
        """Cleanup nach jedem Test"""
        import shutil

        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def create_mock_bystronic_csv(self):
        """Erstellt eine Mock Bystronic CSV-Datei"""
        mock_content = """Name	Distance Control
File	O:\\Messungen\\Test.csv
Starttime of export	133964386997165000	Montag, 1. Januar 2024	10:00:00.000
Endtime of export	133964388292505000	Montag, 1. Januar 2024	10:30:00.000


Name	TEMP_001	Name	VIBR_001	Name	POWER_001
SymbolComment		SymbolComment		SymbolComment
Data-Type	REAL64	Data-Type	REAL64	Data-Type	REAL64
SampleTime[ms]	1	SampleTime[ms]	1	SampleTime[ms]	1
VariableSize	8	VariableSize	8	VariableSize	8
SymbolBased	False	SymbolBased	False	SymbolBased	False
IndexGroup	1180416	IndexGroup	1180416	IndexGroup	1180416
IndexOffset	328147	IndexOffset	328158	IndexOffset	328020
SymbolName	TEMP::sensor_1	SymbolName	VIBR::sensor_1	SymbolName	POWER::sensor_1
NetID	192.168.1.1.1.1	NetID	192.168.1.1.1.1	NetID	192.168.1.1.1.1
Port	551	Port	551	Port	551
Offset	0	Offset	0	Offset	0
ScaleFactor	1	ScaleFactor	1	ScaleFactor	1
BitMask	0xffffffffffffffff	BitMask	0xffffffffffffffff	BitMask	0xffffffffffffffff

0	22.5	0	1.2	0	6.2
1	22.8	1	1.4	1	6.0
2	23.1	2	2.1	2	5.8
3	23.4	3	2.8	3	5.5
"""
        csv_file = self.temp_dir / "mock_bystronic.csv"
        csv_file.write_text(mock_content, encoding="utf-8")
        return csv_file

    def test_parser_initialization(self):
        """Test der Parser-Initialisierung"""
        assert "\t" in self.parser.common_delimiters
        assert "utf-8" in self.parser.supported_encodings
        assert len(self.parser.parsing_history) == 0

    def test_analyze_structure(self):
        """Test der Struktur-Analyse"""
        csv_file = self.create_mock_bystronic_csv()

        structure = self.parser.analyze_structure(str(csv_file))

        assert "header_candidates" in structure
        assert "data_start_candidates" in structure
        assert "delimiter" in structure
        assert "encoding" in structure
        assert structure["encoding"] == "utf-8"
        assert structure["delimiter"] == "\t"

    def test_extract_metadata(self):
        """Test der Metadaten-Extraktion"""
        csv_file = self.create_mock_bystronic_csv()

        # Erst die Struktur analysieren
        structure = self.parser.analyze_structure(str(csv_file))

        metadata = self.parser.parse_metadata(str(csv_file), structure)

        assert isinstance(metadata, dict)
        assert len(metadata) > 0

    def test_parse_complex_csv(self):
        """Test des kompletten CSV-Parsing"""
        csv_file = self.create_mock_bystronic_csv()

        result = self.parser.parse_complex_csv(str(csv_file))

        assert result is not None
        assert "data" in result  # Das ist der DataFrame
        assert "info" in result  # Das sind die parsing info

        df = result["data"]  # Korrigierter Zugriff
        assert not df.empty

    def test_data_validation(self):
        """Test der Datenvalidierung"""
        # Erstelle DataFrame mit problematischen Daten
        test_data = pd.DataFrame(
            {
                "temperature": [20, 25, -999, 30, 22],
                "pressure": [5.0, 6.2, 5.8, -1.0, 6.1],
                "status": ["OK", "OK", "ERROR", "WARNING", "OK"],
            }
        )

        validated_data = self.parser.validate_data(test_data)

        # Prüfe dass extreme Werte behandelt wurden
        assert validated_data["temperature"].min() >= -100  # Realistische untere Grenze
        assert validated_data["pressure"].min() >= 0  # Druck kann nicht negativ sein

    def test_error_handling(self):
        """Test der Fehlerbehandlung"""
        # Test mit nicht existierender Datei
        result = self.parser.parse_complex_csv("/nicht/existierende/datei.csv")
        assert result is None

        # Test mit ungültiger Datei
        invalid_file = self.temp_dir / "invalid.csv"
        invalid_file.write_text("Ungültiger Inhalt", encoding="utf-8")

        result = self.parser.parse_complex_csv(str(invalid_file))
        # Parser sollte auch bei ungültigen Dateien ein Ergebnis zurückgeben (evtl. leer)
        assert result is not None


class TestExcelVerarbeitung:
    """Tests für Excel-Verarbeitung"""

    def setup_method(self):
        """Setup für jeden Test"""
        self.temp_dir = Path(tempfile.mkdtemp())
        self.excel_handler = BystronicExcelHandler()

    def teardown_method(self):
        """Cleanup nach jedem Test"""
        import shutil

        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def create_test_excel(self):
        """Erstellt eine Test-Excel-Datei"""
        excel_file = self.temp_dir / "test_data.xlsx"

        # Verschiedene Arbeitsblätter erstellen
        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            # Produktionsblatt
            production_data = pd.DataFrame(
                {
                    "Datum": pd.date_range("2024-01-01", periods=10),
                    "Maschine_A": np.random.randint(800, 1200, 10),
                    "Maschine_B": np.random.randint(700, 1100, 10),
                    "Verfügbarkeit_A": np.random.uniform(80, 95, 10),
                    "Verfügbarkeit_B": np.random.uniform(75, 90, 10),
                }
            )
            production_data.to_excel(writer, sheet_name="Produktion", index=False)

            # Qualitätsblatt
            quality_data = pd.DataFrame(
                {
                    "Monat": pd.date_range("2024-01-01", periods=3, freq="M"),
                    "Ausschuss_Rate": [2.1, 1.8, 2.3],
                    "Kundenzufriedenheit": [4.2, 4.1, 4.3],
                }
            )
            quality_data.to_excel(writer, sheet_name="Qualität", index=False)

        return excel_file

    def test_excel_multi_sheet_loading(self):
        """Test des Ladens mehrerer Arbeitsblätter"""
        excel_file = self.create_test_excel()

        # Alle Arbeitsblätter laden
        excel_data = pd.read_excel(excel_file, sheet_name=None)

        assert len(excel_data) == 2
        assert "Produktion" in excel_data
        assert "Qualität" in excel_data

        production_df = excel_data["Produktion"]
        assert len(production_df) == 10
        assert "Datum" in production_df.columns
        assert "Maschine_A" in production_df.columns

    def test_excel_handler_load_comprehensive(self):
        """Test des umfassenden Excel-Ladens"""
        excel_file = self.create_test_excel()

        with patch.object(self.excel_handler, "get_data_path", return_value=excel_file):
            result = self.excel_handler.load_comprehensive_data()

        assert result is not None
        assert len(result) >= 2  # Mindestens 2 Arbeitsblätter

    def test_excel_kpi_calculation(self):
        """Test der KPI-Berechnungen"""
        excel_file = self.create_test_excel()

        # Lade Produktionsdaten
        production_df = pd.read_excel(excel_file, sheet_name="Produktion")

        # Berechne KPIs
        kpis = self.excel_handler.calculate_production_kpis(production_df)

        assert "total_production" in kpis
        assert "avg_availability" in kpis
        assert "daily_average" in kpis
        assert isinstance(kpis["total_production"], (int, float))
        assert 0 <= kpis["avg_availability"] <= 100

    def test_excel_export(self):
        """Test des Excel-Exports"""
        # Erstelle Test-DataFrame
        test_df = pd.DataFrame(
            {
                "Spalte1": range(5),
                "Spalte2": ["A", "B", "C", "D", "E"],
                "Spalte3": np.random.randn(5),
            }
        )

        output_file = self.temp_dir / "export_test.xlsx"

        # Exportiere mit mehreren Blättern
        with pd.ExcelWriter(output_file, engine="openpyxl") as writer:
            test_df.to_excel(writer, sheet_name="Daten", index=False)
            test_df.describe().to_excel(writer, sheet_name="Statistiken")

        # Prüfe dass Datei erstellt wurde
        assert output_file.exists()

        # Lade und prüfe Inhalt
        loaded_data = pd.read_excel(output_file, sheet_name=None)
        assert "Daten" in loaded_data
        assert "Statistiken" in loaded_data
        assert len(loaded_data["Daten"]) == 5


class TestJSONVerarbeitung:
    """Tests für JSON-Datenverarbeitung"""

    def setup_method(self):
        """Setup für jeden Test"""
        self.temp_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Cleanup nach jedem Test"""
        import shutil

        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def create_test_json(self):
        """Erstellt eine Test-JSON-Datei"""
        test_data = {
            "metadata": {
                "system": "Bystronic IoT Platform",
                "version": "2.1.0",
                "timestamp": "2024-01-15T08:30:00Z",
            },
            "sensors": [
                {
                    "id": "TEMP_001",
                    "type": "temperature",
                    "readings": [
                        {
                            "timestamp": "2024-01-15T08:30:00Z",
                            "value": 22.5,
                            "status": "ok",
                        },
                        {
                            "timestamp": "2024-01-15T08:31:00Z",
                            "value": 22.8,
                            "status": "ok",
                        },
                    ],
                },
                {
                    "id": "VIBR_001",
                    "type": "vibration",
                    "readings": [
                        {
                            "timestamp": "2024-01-15T08:30:00Z",
                            "value": 1.2,
                            "status": "ok",
                        },
                        {
                            "timestamp": "2024-01-15T08:31:00Z",
                            "value": 2.8,
                            "status": "error",
                        },
                    ],
                },
            ],
        }

        json_file = self.temp_dir / "test_sensors.json"
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(test_data, f, indent=2)

        return json_file, test_data

    def test_json_loading(self):
        """Test des JSON-Ladens"""
        json_file, original_data = self.create_test_json()

        with open(json_file, encoding="utf-8") as f:
            loaded_data = json.load(f)

        assert loaded_data == original_data
        assert "metadata" in loaded_data
        assert "sensors" in loaded_data
        assert len(loaded_data["sensors"]) == 2

    def test_json_normalization(self):
        """Test der JSON-Normalisierung zu DataFrame"""
        json_file, original_data = self.create_test_json()

        # Sensordaten zu flacher Struktur normalisieren
        sensor_readings = []

        for sensor in original_data["sensors"]:
            for reading in sensor["readings"]:
                sensor_readings.append(
                    {
                        "sensor_id": sensor["id"],
                        "sensor_type": sensor["type"],
                        "timestamp": reading["timestamp"],
                        "value": reading["value"],
                        "status": reading["status"],
                    }
                )

        df = pd.DataFrame(sensor_readings)

        assert len(df) == 4  # 2 Sensoren × 2 Messwerte
        assert "sensor_id" in df.columns
        assert "sensor_type" in df.columns
        assert "TEMP_001" in df["sensor_id"].values
        assert "VIBR_001" in df["sensor_id"].values

    def test_json_pandas_normalization(self):
        """Test der pandas json_normalize Funktionalität"""
        json_file, original_data = self.create_test_json()

        # Verwende pandas json_normalize
        df_normalized = pd.json_normalize(
            original_data["sensors"],
            record_path="readings",
            meta=["id", "type"],
            meta_prefix="sensor_",
        )

        assert not df_normalized.empty
        assert "sensor_id" in df_normalized.columns
        assert "sensor_type" in df_normalized.columns
        assert "value" in df_normalized.columns
        assert len(df_normalized) == 4

    def test_json_export(self):
        """Test des JSON-Exports"""
        test_df = pd.DataFrame(
            {
                "timestamp": pd.date_range("2024-01-01", periods=3),
                "value": [1.0, 2.0, 3.0],
                "status": ["ok", "warning", "error"],
            }
        )

        # Als JSON exportieren
        json_output = self.temp_dir / "export_test.json"

        # Mit Metadaten
        export_data = {
            "metadata": {
                "exported_at": pd.Timestamp.now().isoformat(),
                "rows": len(test_df),
            },
            "data": test_df.to_dict("records"),
        }

        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, default=str)

        # Prüfe dass Datei erstellt wurde
        assert json_output.exists()

        # Lade und prüfe Inhalt
        with open(json_output, encoding="utf-8") as f:
            loaded_data = json.load(f)

        assert "metadata" in loaded_data
        assert "data" in loaded_data
        assert len(loaded_data["data"]) == 3


class TestDatenbereinigung:
    """Tests für Datenbereinigungsfunktionen"""

    def create_dirty_data(self):
        """Erstellt DataFrame mit verschiedenen Datenproblemen"""
        return pd.DataFrame(
            {
                "Maschine": ["A", "B", "C", "A", "B"],
                "Produktion": [1000, -50, 1200, np.nan, 2000],  # Negative Werte, NaN
                "Temperatur": [22.5, 150.0, 23.1, 22.8, -999],  # Unrealistische Werte
                "Verfügbarkeit": [
                    85.2,
                    120.0,
                    88.5,
                    92.1,
                    -10,
                ],  # > 100%, negative Werte
                "Status": ["OK", "OK", "", "WARNING", "ERROR"],  # Leere Strings
            }
        )

    def test_detect_missing_values(self):
        """Test der Erkennung fehlender Werte"""
        df = self.create_dirty_data()

        missing_count = df.isnull().sum()
        assert missing_count["Produktion"] == 1
        assert missing_count["Temperatur"] == 0  # -999 wird nicht als NaN erkannt

        # Test mit expliziten NaN-Werten
        df_with_nan = df.copy()
        df_with_nan.loc[df_with_nan["Temperatur"] == -999, "Temperatur"] = np.nan

        missing_after = df_with_nan.isnull().sum()
        assert missing_after["Temperatur"] == 1

    def test_outlier_detection(self):
        """Test der Ausreißer-Erkennung"""
        df = self.create_dirty_data()

        # IQR-Methode für Temperatur
        temp_series = df["Temperatur"]
        Q1 = temp_series.quantile(0.25)
        Q3 = temp_series.quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = temp_series[
            (temp_series < lower_bound) | (temp_series > upper_bound)
        ]

        # -999 und 150.0 sollten als Ausreißer erkannt werden
        assert len(outliers) >= 2
        assert -999 in outliers.values
        assert 150.0 in outliers.values

    def test_data_cleaning(self):
        """Test der Datenbereinigung"""
        df = self.create_dirty_data()

        # Bereinigung implementieren
        df_clean = df.copy()

        # 1. Negative Produktionswerte auf 0 setzen
        df_clean.loc[df_clean["Produktion"] < 0, "Produktion"] = 0

        # 2. Verfügbarkeit auf 0-100% begrenzen
        df_clean.loc[df_clean["Verfügbarkeit"] > 100, "Verfügbarkeit"] = 100
        df_clean.loc[df_clean["Verfügbarkeit"] < 0, "Verfügbarkeit"] = 0

        # 3. Unrealistische Temperaturen als NaN markieren
        df_clean.loc[
            (df_clean["Temperatur"] < -50) | (df_clean["Temperatur"] > 100),
            "Temperatur",
        ] = np.nan

        # 4. Leere Strings durch NaN ersetzen
        df_clean = df_clean.replace("", np.nan)

        # Prüfungen
        assert df_clean["Produktion"].min() >= 0
        assert df_clean["Verfügbarkeit"].max() <= 100
        assert df_clean["Verfügbarkeit"].min() >= 0
        assert df_clean["Temperatur"].min() >= -50  # Nach NaN-Ersetzung

    def test_duplicate_removal(self):
        """Test der Duplikat-Entfernung"""
        df = pd.DataFrame({"A": [1, 2, 2, 3], "B": [4, 5, 5, 6], "C": [7, 8, 8, 9]})

        # Duplikate identifizieren
        duplicates = df.duplicated()
        assert duplicates.sum() == 1

        # Duplikate entfernen
        df_clean = df.drop_duplicates()
        assert len(df_clean) == 3
        assert not df_clean.duplicated().any()

    def test_data_type_optimization(self):
        """Test der Datentyp-Optimierung"""
        df = pd.DataFrame(
            {
                "ID": range(100),
                "Kategorie": ["A", "B", "C"] * 34,  # 102 Werte, aber nur 100 benötigt
                "Wert": np.random.randn(100),
                "Status": [True, False] * 50,
            }
        )
        df = df.iloc[:100]  # Nur erste 100 Zeilen

        # Memory usage vor Optimierung
        memory_before = df.memory_usage(deep=True).sum()

        # Optimiere Datentypen
        df_optimized = df.copy()
        df_optimized["ID"] = df_optimized["ID"].astype("int32")
        df_optimized["Kategorie"] = df_optimized["Kategorie"].astype("category")
        df_optimized["Wert"] = df_optimized["Wert"].astype("float32")

        # Memory usage nach Optimierung
        memory_after = df_optimized.memory_usage(deep=True).sum()

        # Sollte weniger Memory verwenden
        assert memory_after < memory_before
        assert df_optimized["Kategorie"].dtype.name == "category"
        assert df_optimized["ID"].dtype == "int32"
        assert df_optimized["Wert"].dtype == "float32"


class TestExportFunktionen:
    """Tests für Export-Funktionalitäten"""

    def setup_method(self):
        """Setup für jeden Test"""
        self.temp_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Cleanup nach jedem Test"""
        import shutil

        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def create_test_dataframe(self):
        """Erstellt einen Test-DataFrame"""
        return pd.DataFrame(
            {
                "Datum": pd.date_range("2024-01-01", periods=10),
                "Wert1": np.random.randn(10),
                "Wert2": np.random.randint(1, 100, 10),
                "Kategorie": np.random.choice(["A", "B", "C"], 10),
                "Status": np.random.choice(["OK", "WARNING", "ERROR"], 10),
            }
        )

    def test_csv_export(self):
        """Test des CSV-Exports"""
        df = self.create_test_dataframe()

        csv_file = self.temp_dir / "test_export.csv"
        df.to_csv(csv_file, index=False, encoding="utf-8")

        assert csv_file.exists()

        # Lade wieder und prüfe
        df_loaded = pd.read_csv(csv_file)
        assert len(df_loaded) == len(df)
        assert list(df_loaded.columns) == list(df.columns)

    def test_excel_export_multi_sheet(self):
        """Test des Excel-Exports mit mehreren Blättern"""
        df = self.create_test_dataframe()

        excel_file = self.temp_dir / "test_export.xlsx"

        with pd.ExcelWriter(excel_file, engine="openpyxl") as writer:
            df.to_excel(writer, sheet_name="Daten", index=False)
            df.describe().to_excel(writer, sheet_name="Statistiken")

            # Zusätzliches Aggregations-Blatt
            agg_data = (
                df.groupby("Kategorie")
                .agg({"Wert1": "mean", "Wert2": "sum"})
                .reset_index()
            )
            agg_data.to_excel(writer, sheet_name="Aggregationen", index=False)

        assert excel_file.exists()

        # Prüfe alle Blätter
        excel_data = pd.read_excel(excel_file, sheet_name=None)
        assert "Daten" in excel_data
        assert "Statistiken" in excel_data
        assert "Aggregationen" in excel_data

        assert len(excel_data["Daten"]) == 10
        assert len(excel_data["Aggregationen"]) <= 3  # Max 3 Kategorien

    def test_json_export_with_metadata(self):
        """Test des JSON-Exports mit Metadaten"""
        df = self.create_test_dataframe()

        json_file = self.temp_dir / "test_export.json"

        export_data = {
            "metadata": {
                "exported_at": pd.Timestamp.now().isoformat(),
                "rows": len(df),
                "columns": len(df.columns),
                "source": "Bystronic Test Suite",
            },
            "column_info": {col: str(dtype) for col, dtype in df.dtypes.items()},
            "data": df.to_dict("records"),
        }

        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, default=str, ensure_ascii=False)

        assert json_file.exists()

        # Lade und prüfe
        with open(json_file, encoding="utf-8") as f:
            loaded_data = json.load(f)

        assert "metadata" in loaded_data
        assert "column_info" in loaded_data
        assert "data" in loaded_data
        assert len(loaded_data["data"]) == 10
        assert loaded_data["metadata"]["rows"] == 10

    def test_parquet_export(self):
        """Test des Parquet-Exports (wenn verfügbar)"""
        df = self.create_test_dataframe()

        parquet_file = self.temp_dir / "test_export.parquet"

        try:
            df.to_parquet(parquet_file, index=False, compression="snappy")

            assert parquet_file.exists()

            # Lade wieder
            df_loaded = pd.read_parquet(parquet_file)
            assert len(df_loaded) == len(df)
            assert list(df_loaded.columns) == list(df.columns)

        except ImportError:
            # Parquet-Support ist optional
            pytest.skip("Parquet support not available")

    def test_multi_format_export(self):
        """Test des Exports in mehreren Formaten gleichzeitig"""
        df = self.create_test_dataframe()

        base_filename = "multi_export"
        formats = ["csv", "json"]  # Excel optional wegen openpyxl

        exported_files = []

        # CSV
        if "csv" in formats:
            csv_file = self.temp_dir / f"{base_filename}.csv"
            df.to_csv(csv_file, index=False)
            exported_files.append(csv_file)

        # JSON
        if "json" in formats:
            json_file = self.temp_dir / f"{base_filename}.json"
            df.to_json(json_file, orient="records", indent=2)
            exported_files.append(json_file)

        # Prüfe dass alle Dateien erstellt wurden
        for file_path in exported_files:
            assert file_path.exists()
            assert file_path.stat().st_size > 0  # Nicht leer


# Integration Tests
class TestIntegration:
    """Integration Tests für das gesamte Modul"""

    def setup_method(self):
        """Setup für jeden Test"""
        self.temp_dir = Path(tempfile.mkdtemp())

    def teardown_method(self):
        """Cleanup nach jedem Test"""
        import shutil

        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def test_complete_pipeline(self):
        """Test einer kompletten Datenverarbeitungs-Pipeline"""
        # 1. CSV erstellen
        test_data = pd.DataFrame(
            {
                "Datum": pd.date_range("2024-01-01", periods=50),
                "Maschine": np.random.choice(["A", "B", "C"], 50),
                "Produktion": np.random.randint(800, 1200, 50),
                "Temperatur": np.random.normal(23, 3, 50),
                "Status": np.random.choice(["OK", "WARNING", "ERROR"], 50),
            }
        )

        csv_input = self.temp_dir / "input.csv"
        test_data.to_csv(csv_input, index=False)

        # 2. CSV laden
        df_loaded = pd.read_csv(csv_input)
        assert len(df_loaded) == 50

        # 3. Daten bereinigen
        df_clean = df_loaded.copy()
        df_clean = df_clean.dropna()
        df_clean = df_clean.drop_duplicates()

        # 4. Aggregationen
        daily_stats = (
            df_clean.groupby("Maschine")
            .agg(
                {"Produktion": ["mean", "sum", "count"], "Temperatur": ["mean", "std"]}
            )
            .round(2)
        )

        # 5. Export in verschiedenen Formaten
        # CSV Export
        csv_output = self.temp_dir / "output_clean.csv"
        df_clean.to_csv(csv_output, index=False)

        # JSON Export mit Metadaten
        json_output = self.temp_dir / "output_stats.json"
        export_data = {
            "metadata": {
                "processing_date": pd.Timestamp.now().isoformat(),
                "input_rows": len(df_loaded),
                "output_rows": len(df_clean),
                "machines": sorted(df_clean["Maschine"].unique().tolist()),
            },
            "daily_stats": daily_stats.to_dict(),
        }

        with open(json_output, "w", encoding="utf-8") as f:
            json.dump(export_data, f, indent=2, default=str)

        # 6. Verifikation
        assert csv_output.exists()
        assert json_output.exists()

        # Lade exportierte Daten
        df_final = pd.read_csv(csv_output)
        assert len(df_final) <= 50  # Kann durch Bereinigung kleiner sein

        with open(json_output) as f:
            stats_data = json.load(f)

        assert "metadata" in stats_data
        assert "daily_stats" in stats_data
        assert stats_data["metadata"]["input_rows"] == 50


if __name__ == "__main__":
    # Führe Tests aus wenn Datei direkt aufgerufen wird
    pytest.main([__file__, "-v", "--tb=short"])
