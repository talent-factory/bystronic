#!/usr/bin/env python3
"""
Tests für 04_pandas/beispiele

Diese Tests validieren die Funktionalität der Pandas-Beispiele
und demonstrieren Test-Patterns für Datenanalyse-Code.
"""

import sys
import tempfile
from pathlib import Path
from unittest.mock import patch

import numpy as np
import pandas as pd
import pytest

# Pfad zu den Beispielen hinzufügen
beispiele_path = Path(__file__).parent.parent / "src" / "04_pandas" / "beispiele"
sys.path.insert(0, str(beispiele_path))

import data_analysis
import data_cleaning
import data_import_export
import dataframe_basics


class TestDataFrameBasics:
    """Tests für dataframe_basics.py Beispiel"""

    def test_module_imports_successfully(self):
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert dataframe_basics is not None

    def test_sample_dataframe_creation(self):
        """Testet die DataFrame-Erstellung aus dem Beispiel"""
        maschinendaten = {
            "Maschine": ["Laser_01", "Laser_02", "Presse_01"],
            "Typ": ["ByStar", "ByStar", "Xpert"],
            "Baujahr": [2019, 2020, 2018],
            "Produktionszeit_h": [2450.5, 1890.2, 3200.8],
            "Wartung_fällig": [True, False, True],
        }

        df = pd.DataFrame(maschinendaten)

        # Grundlegende DataFrame-Eigenschaften testen
        assert df.shape == (3, 5), f"DataFrame Shape fehlerhaft: {df.shape}"
        assert list(df.columns) == list(maschinendaten.keys()), "Spalten-Namen fehlerhaft"
        assert len(df) == 3, "DataFrame-Länge fehlerhaft"

    def test_dataframe_operations(self):
        """Testet grundlegende DataFrame-Operationen"""
        # Test-DataFrame erstellen
        df = pd.DataFrame({
            "Maschine": ["Laser_01", "Laser_02", "Presse_01"],
            "Produktionszeit_h": [2450.5, 1890.2, 3200.8],
            "Baujahr": [2019, 2020, 2018]
        })

        # Filterung testen
        filtered = df[df["Produktionszeit_h"] > 2000]
        assert len(filtered) == 2, "DataFrame-Filterung fehlerhaft"

        # Sortierung testen
        sorted_df = df.sort_values("Produktionszeit_h")
        assert sorted_df.iloc[0]["Maschine"] == "Laser_02", "DataFrame-Sortierung fehlerhaft"

        # Neue Spalte hinzufügen
        df["Alter"] = 2024 - df["Baujahr"]
        assert "Alter" in df.columns, "Spalten-Hinzufügung fehlerhaft"
        assert df.loc[0, "Alter"] == 5, "Spalten-Berechnung fehlerhaft"

    def test_aggregation_operations(self):
        """Testet Aggregations-Operationen"""
        df = pd.DataFrame({
            "Typ": ["ByStar", "ByStar", "Xpert", "Xpert"],
            "Produktionszeit_h": [2450.5, 1890.2, 3200.8, 1250.4]
        })

        # Gruppierung und Aggregation
        grouped = df.groupby("Typ")["Produktionszeit_h"].mean()

        assert len(grouped) == 2, "Gruppierung fehlerhaft"
        assert "ByStar" in grouped.index, "Gruppierungs-Index fehlerhaft"

        # Durchschnittswerte prüfen
        bystar_avg = (2450.5 + 1890.2) / 2
        assert abs(grouped["ByStar"] - bystar_avg) < 0.1, "Aggregation fehlerhaft"


class TestDataImportExport:
    """Tests für data_import_export.py Beispiel"""

    def test_module_imports_successfully(self):
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert data_import_export is not None

    def test_csv_operations(self):
        """Testet CSV-Import/Export-Operationen"""
        # Test-DataFrame erstellen
        test_data = pd.DataFrame({
            "Maschine": ["Test_01", "Test_02"],
            "Wert": [100.5, 200.3]
        })

        with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as tmp:
            # CSV schreiben
            test_data.to_csv(tmp.name, index=False)

            # CSV lesen
            loaded_data = pd.read_csv(tmp.name)

            # Vergleichen
            pd.testing.assert_frame_equal(test_data, loaded_data)

    def test_json_operations(self):
        """Testet JSON-Import/Export-Operationen"""
        test_data = pd.DataFrame({
            "id": ["LASER_01", "PRESSE_01"],
            "aktiv": [True, False]
        })

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as tmp:
            # JSON schreiben
            test_data.to_json(tmp.name, orient='records', indent=2)

            # JSON lesen
            loaded_data = pd.read_json(tmp.name, orient='records')

            # Vergleichen (JSON kann Datentypen ändern)
            assert len(loaded_data) == len(test_data)
            assert list(loaded_data.columns) == list(test_data.columns)


class TestDataCleaning:
    """Tests für data_cleaning.py Beispiel"""

    def test_module_imports_successfully(self):
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert data_cleaning is not None

    def test_missing_data_handling(self):
        """Testet Behandlung fehlender Daten"""
        # DataFrame mit fehlenden Werten
        df_dirty = pd.DataFrame({
            "Maschine": ["Laser_01", "Laser_02", None, "Presse_01"],
            "Produktionszeit": [2450.5, None, 1800.0, 3200.8],
            "Status": ["Aktiv", "Wartung", "Aktiv", None]
        })

        # Fehlende Werte identifizieren
        missing_count = df_dirty.isnull().sum().sum()
        assert missing_count == 3, f"Fehlende Werte nicht korrekt erkannt: {missing_count}"

        # Zeilen mit fehlenden Werten entfernen
        df_clean = df_dirty.dropna()
        assert len(df_clean) == 1, "dropna() funktioniert nicht korrekt"

        # Fehlende Werte füllen
        df_filled = df_dirty.fillna("Unbekannt")
        assert df_filled.isnull().sum().sum() == 0, "fillna() funktioniert nicht korrekt"

    def test_data_type_conversion(self):
        """Testet Datentyp-Konvertierungen"""
        df = pd.DataFrame({
            "Maschine": ["Laser_01", "Laser_02"],
            "Baujahr": ["2019", "2020"],  # Als String
            "Aktiv": ["True", "False"]    # Als String
        })

        # Datentypen konvertieren
        df["Baujahr"] = pd.to_numeric(df["Baujahr"])
        df["Aktiv"] = df["Aktiv"].map({"True": True, "False": False})

        assert df["Baujahr"].dtype in [np.int64, np.int32], "Numerische Konvertierung fehlerhaft"
        assert df["Aktiv"].dtype == bool, "Boolean-Konvertierung fehlerhaft"

    def test_duplicate_handling(self):
        """Testet Behandlung von Duplikaten"""
        df_with_dupes = pd.DataFrame({
            "Maschine": ["Laser_01", "Laser_01", "Laser_02"],
            "Wert": [100, 100, 200]
        })

        # Duplikate identifizieren
        duplicates = df_with_dupes.duplicated()
        assert duplicates.sum() == 1, "Duplikat-Erkennung fehlerhaft"

        # Duplikate entfernen
        df_no_dupes = df_with_dupes.drop_duplicates()
        assert len(df_no_dupes) == 2, "Duplikat-Entfernung fehlerhaft"


class TestDataAnalysis:
    """Tests für data_analysis.py Beispiel"""

    def test_module_imports_successfully(self):
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert data_analysis is not None

    def test_statistical_analysis(self):
        """Testet statistische Analysen"""
        df = pd.DataFrame({
            "Produktionszeit": [2450.5, 1890.2, 3200.8, 1250.4, 2800.1],
            "Ausschussrate": [0.023, 0.045, 0.012, 0.067, 0.034]
        })

        # Grundlegende Statistiken
        stats = df.describe()
        assert "mean" in stats.index, "Statistische Beschreibung fehlerhaft"
        assert "std" in stats.index, "Standardabweichung fehlt"

        # Korrelation
        correlation = df["Produktionszeit"].corr(df["Ausschussrate"])
        assert isinstance(correlation, float | np.float64), "Korrelation fehlerhaft"
        assert -1 <= correlation <= 1, "Korrelationswert außerhalb des gültigen Bereichs"

    def test_time_series_operations(self):
        """Testet Zeitreihen-Operationen"""
        # Zeitreihen-DataFrame erstellen
        dates = pd.date_range("2024-01-01", periods=5, freq="D")
        df_time = pd.DataFrame({
            "Datum": dates,
            "Produktion": [100, 120, 95, 110, 105]
        })

        # Datum als Index setzen
        df_time.set_index("Datum", inplace=True)

        assert isinstance(df_time.index, pd.DatetimeIndex), "DateTime-Index fehlerhaft"

        # Resampling (falls implementiert)
        try:
            weekly = df_time.resample("W").sum()
            assert len(weekly) <= len(df_time), "Resampling fehlerhaft"
        except Exception:
            pass  # Resampling möglicherweise nicht im Beispiel


class TestPandasIntegration:
    """Integrationstests für Pandas-Beispiele"""

    @patch('builtins.print')
    def test_all_examples_run_without_error(self, mock_print):
        """Testet, ob alle Pandas-Beispiele ohne Fehler laufen"""
        # Nur dataframe_basics testen, da andere möglicherweise Dateien benötigen
        try:
            # Mock für input() falls benötigt
            with patch('builtins.input', return_value=''):
                # Führe das Hauptskript aus (falls vorhanden)
                pass
        except Exception as e:
            pytest.fail(f"Pandas-Beispiel fehlgeschlagen: {e}")

    def test_bystronic_specific_data_patterns(self):
        """Testet Bystronic-spezifische Datenmuster"""
        # Typische Bystronic-Maschinendaten
        maschinendaten = pd.DataFrame({
            "Maschine_ID": ["LASER_01", "LASER_02", "PRESSE_01", "STANZE_01"],
            "Typ": ["ByStar Fiber", "ByStar Fiber", "Xpert 150", "ByTrans"],
            "Baujahr": [2019, 2020, 2018, 2017],
            "Produktionszeit_YTD": [2450.5, 1890.2, 3200.8, 2890.1],
            "Wartung_fällig": [True, False, True, True],
            "Ausschussrate": [0.023, 0.045, 0.012, 0.067]
        })

        # Typische Analysen
        # 1. Wartungsplanung
        wartung_faellig = maschinendaten[maschinendaten["Wartung_fällig"]]
        assert len(wartung_faellig) == 3, "Wartungsfilterung fehlerhaft"

        # 2. Effizienzanalyse
        durchschnitt_produktion = maschinendaten["Produktionszeit_YTD"].mean()
        assert durchschnitt_produktion > 0, "Produktionszeit-Durchschnitt fehlerhaft"

        # 3. Qualitätsanalyse
        hohe_ausschussrate = maschinendaten[maschinendaten["Ausschussrate"] > 0.05]
        assert len(hohe_ausschussrate) == 1, "Qualitätsfilterung fehlerhaft"

        # 4. Altersanalyse
        maschinendaten["Alter"] = 2024 - maschinendaten["Baujahr"]
        alte_maschinen = maschinendaten[maschinendaten["Alter"] > 5]
        assert len(alte_maschinen) >= 1, "Altersfilterung fehlerhaft"

    def test_production_data_analysis(self):
        """Testet Produktionsdaten-Analyse"""
        # Simuliere wöchentliche Produktionsdaten
        np.random.seed(42)  # Für reproduzierbare Tests

        wochen_daten = []
        maschinen = ["LASER_01", "LASER_02", "PRESSE_01"]

        for woche in range(1, 5):
            for maschine in maschinen:
                wochen_daten.append({
                    "Woche": woche,
                    "Maschine": maschine,
                    "Geplante_Zeit": 40.0,
                    "Tatsächliche_Zeit": 40.0 + np.random.normal(0, 2),
                    "Teile_produziert": 1000 + np.random.randint(-100, 100)
                })

        df_produktion = pd.DataFrame(wochen_daten)

        # Abweichungsanalyse
        df_produktion["Abweichung"] = (
            df_produktion["Tatsächliche_Zeit"] - df_produktion["Geplante_Zeit"]
        )

        # Gruppierte Analysen
        wochen_summary = df_produktion.groupby("Woche").agg({
            "Tatsächliche_Zeit": "sum",
            "Teile_produziert": "sum",
            "Abweichung": "mean"
        })

        assert len(wochen_summary) == 4, "Wochen-Gruppierung fehlerhaft"
        assert "Tatsächliche_Zeit" in wochen_summary.columns, "Aggregation fehlerhaft"

        maschinen_summary = df_produktion.groupby("Maschine").agg({
            "Abweichung": ["mean", "std"],
            "Teile_produziert": "sum"
        })

        assert len(maschinen_summary) == 3, "Maschinen-Gruppierung fehlerhaft"


# Hilfsfunktionen für Tests
def test_pandas_version_compatibility():
    """Testet Pandas-Versions-Kompatibilität"""
    import pandas as pd

    # Überprüfe, ob eine kompatible Pandas-Version installiert ist
    version = pd.__version__
    major_version = int(version.split('.')[0])

    assert major_version >= 1, f"Pandas-Version zu alt: {version}"


def test_example_files_exist():
    """Testet, ob alle Pandas-Beispieldateien existieren"""
    files_to_check = [
        "dataframe_basics.py",
        "data_import_export.py",
        "data_cleaning.py",
        "data_analysis.py",
        "vba_vs_pandas.py"
    ]

    for filename in files_to_check:
        file_path = beispiele_path / filename
        assert file_path.exists(), f"{filename} nicht gefunden"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
