#!/usr/bin/env python3
"""
Bystronic CSV Parser - Spezieller Parser für komplexe CSV-Strukturen

Dieses Modul bietet intelligente Parsing-Funktionen für CSV-Dateien mit
komplexen Strukturen, wie sie in industriellen Anwendungen häufig vorkommen.

Autor: Python Grundkurs Bystronic
Datum: 2024
"""

import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")


def get_data_path(*args):
    """
    Hilfsfunktion zum korrekten Konstruieren der Datenpfade
    """
    project_root = Path(__file__).parent.parent.parent.parent
    data_path = project_root / "data"
    for arg in args:
        data_path = data_path / arg
    return data_path


class BystronicCSVParser:
    """
    Intelligenter CSV-Parser für Bystronic-Maschinendaten

    Unterstützt:
    - Automatische Header-Erkennung
    - Flexible Trennzeichen
    - Metadaten-Extraktion
    - Datentyp-Inferenz
    - Strukturvalidierung
    """

    def __init__(self):
        self.supported_encodings = ["utf-8", "latin1", "cp1252", "iso-8859-1"]
        self.common_delimiters = ["\t", ",", ";", "|"]
        self.parsing_history = []

    def detect_encoding(self, file_path: str) -> str:
        """
        Erkennt automatisch das Encoding einer Datei

        Parameters:
        -----------
        file_path : str
            Pfad zur CSV-Datei

        Returns:
        --------
        str
            Erkanntes Encoding
        """
        for encoding in self.supported_encodings:
            try:
                with open(file_path, encoding=encoding) as f:
                    # Versuche die ersten 1000 Zeichen zu lesen
                    f.read(1000)
                print(f"✅ Encoding erkannt: {encoding}")
                return encoding
            except UnicodeDecodeError:
                continue

        print("⚠️ Fallback auf utf-8 mit Fehlerbehandlung")
        return "utf-8"

    def detect_delimiter(
        self, file_path: str, encoding: str, sample_lines: int = 10
    ) -> str:
        """
        Erkennt automatisch das Trennzeichen

        Parameters:
        -----------
        file_path : str
            Pfad zur CSV-Datei
        encoding : str
            Encoding der Datei
        sample_lines : int
            Anzahl der Zeilen für die Analyse

        Returns:
        --------
        str
            Erkanntes Trennzeichen
        """
        with open(file_path, encoding=encoding, errors="ignore") as f:
            sample_lines_content = [f.readline() for _ in range(sample_lines)]

        delimiter_scores = {}

        for delimiter in self.common_delimiters:
            scores = []
            for line in sample_lines_content:
                if line.strip():
                    count = line.count(delimiter)
                    scores.append(count)

            if scores:
                # Bewerte Konsistenz der Spaltenanzahl
                avg_count = np.mean(scores)
                std_count = np.std(scores)
                consistency_score = avg_count / (
                    std_count + 1
                )  # +1 zur Vermeidung Division durch 0
                delimiter_scores[delimiter] = consistency_score

        if delimiter_scores:
            best_delimiter = max(delimiter_scores.items(), key=lambda x: x[1])[0]
            print(
                f"✅ Trennzeichen erkannt: {'Tab' if best_delimiter == '\\t' else repr(best_delimiter)}"
            )
            return best_delimiter

        print("⚠️ Fallback auf Tab-Trennzeichen")
        return "\t"

    def analyze_structure(
        self, file_path: str, encoding: str = None, delimiter: str = None
    ) -> dict:
        """
        Analysiert die Struktur einer CSV-Datei

        Parameters:
        -----------
        file_path : str
            Pfad zur CSV-Datei
        encoding : str, optional
            Encoding (automatisch erkannt wenn None)
        delimiter : str, optional
            Trennzeichen (automatisch erkannt wenn None)

        Returns:
        --------
        Dict
            Struktur-Informationen
        """
        print(f"🔍 Analysiere Dateistruktur: {file_path}")

        if encoding is None:
            encoding = self.detect_encoding(file_path)

        if delimiter is None:
            delimiter = self.detect_delimiter(file_path, encoding)

        with open(file_path, encoding=encoding, errors="ignore") as f:
            lines = f.readlines()

        structure_info = {
            "total_lines": len(lines),
            "encoding": encoding,
            "delimiter": delimiter,
            "header_candidates": [],
            "data_start_candidates": [],
            "metadata_sections": {},
        }

        # Suche nach Header-Kandidaten (Zeilen mit "Name" Tags)
        for i, line in enumerate(lines):
            line_content = line.strip()

            # Potentielle Header-Zeile
            if line_content.startswith("Name" + delimiter):
                parts = line_content.split(delimiter)
                column_names = []
                for j in range(1, len(parts), 2):  # Jede zweite Spalte nach "Name"
                    if j < len(parts):
                        column_names.append(parts[j])

                structure_info["header_candidates"].append(
                    {
                        "line": i + 1,
                        "columns": column_names,
                        "column_count": len(column_names),
                    }
                )

            # Metadaten-Bereiche erkennen
            if any(
                keyword in line_content
                for keyword in ["File", "Starttime", "Endtime", "Data-Type"]
            ):
                parts = line_content.split(delimiter, 1)
                if len(parts) == 2:
                    key = parts[0]
                    value = parts[1]
                    structure_info["metadata_sections"][key] = {
                        "line": i + 1,
                        "value": value,
                    }

        # Suche nach Datenbereich
        for i, line in enumerate(lines):
            line_content = line.strip()
            if line_content and not any(
                keyword in line_content
                for keyword in [
                    "Name",
                    "Data-Type",
                    "SampleTime",
                    "SymbolComment",
                    "File",
                    "Starttime",
                ]
            ):
                parts = line_content.split(delimiter)
                numeric_count = 0

                # Prüfe erste 10 Spalten auf numerische Werte
                for part in parts[:10]:
                    try:
                        float(part)
                        numeric_count += 1
                    except ValueError:
                        pass

                # Wenn >= 70% der Werte numerisch sind, ist das wahrscheinlich Datenbereich
                if len(parts) >= 5 and numeric_count >= len(parts[:10]) * 0.7:
                    structure_info["data_start_candidates"].append(
                        {
                            "line": i + 1,
                            "numeric_ratio": numeric_count / len(parts[:10]),
                            "column_count": len(parts),
                        }
                    )
                    break  # Nehme den ersten gefundenen Datenbereich

        print("📋 Struktur analysiert:")
        print(f"  - Gesamtzeilen: {structure_info['total_lines']}")
        print(f"  - Header-Kandidaten: {len(structure_info['header_candidates'])}")
        print(
            f"  - Datenbereich-Kandidaten: {len(structure_info['data_start_candidates'])}"
        )
        print(f"  - Metadaten-Bereiche: {len(structure_info['metadata_sections'])}")

        return structure_info

    def parse_metadata(self, file_path: str, structure_info: dict) -> dict:
        """
        Extrahiert Metadaten aus der CSV-Datei

        Parameters:
        -----------
        file_path : str
            Pfad zur CSV-Datei
        structure_info : Dict
            Struktur-Informationen

        Returns:
        --------
        Dict
            Extrahierte Metadaten
        """
        metadata = {}
        encoding = structure_info["encoding"]
        delimiter = structure_info["delimiter"]

        with open(file_path, encoding=encoding, errors="ignore") as f:
            lines = f.readlines()

        # Basis-Metadaten aus den ersten Zeilen
        for i in range(min(10, len(lines))):
            line = lines[i].strip()
            if delimiter in line:
                parts = line.split(delimiter, 1)
                if len(parts) == 2:
                    key = parts[0].strip()
                    value = parts[1].strip()

                    # Spezielle Behandlung für bekannte Schlüssel
                    if key in ["Name", "File", "Starttime", "Endtime"]:
                        metadata[key] = value

        # Zusätzliche Metadaten aus Struktur-Info
        metadata.update(
            {
                "total_lines": structure_info["total_lines"],
                "encoding": encoding,
                "delimiter": "Tab" if delimiter == "\t" else delimiter,
                "analysis_timestamp": pd.Timestamp.now().isoformat(),
            }
        )

        return metadata

    def parse_complex_csv(
        self,
        file_path: str,
        header_line: int = None,
        data_start_line: int = None,
        encoding: str = None,
        delimiter: str = None,
        max_rows: int = None,
    ) -> dict:
        """
        Hauptfunktion zum Parsen komplexer CSV-Dateien

        Parameters:
        -----------
        file_path : str
            Pfad zur CSV-Datei
        header_line : int, optional
            Zeilennummer für Header (automatisch erkannt wenn None)
        data_start_line : int, optional
            Zeilennummer für Datenbeginn (automatisch erkannt wenn None)
        encoding : str, optional
            Encoding (automatisch erkannt wenn None)
        delimiter : str, optional
            Trennzeichen (automatisch erkannt wenn None)
        max_rows : int, optional
            Maximale Anzahl der zu lesenden Datenzeilen

        Returns:
        --------
        Dict
            Parsing-Ergebnisse mit 'metadata', 'data', 'info'
        """
        print(f"🚀 Starte komplexes CSV-Parsing: {Path(file_path).name}")

        # Struktur analysieren
        structure_info = self.analyze_structure(file_path, encoding, delimiter)

        # Metadaten extrahieren
        metadata = self.parse_metadata(file_path, structure_info)

        # Header und Datenbeginn bestimmen
        if header_line is None and structure_info["header_candidates"]:
            header_info = structure_info["header_candidates"][0]
            header_line = header_info["line"]
            columns = header_info["columns"]
        else:
            columns = None

        if data_start_line is None and structure_info["data_start_candidates"]:
            data_start_line = structure_info["data_start_candidates"][0]["line"]

        # DataFrame erstellen
        df = pd.DataFrame()

        if header_line and data_start_line and columns:
            try:
                with open(
                    file_path, encoding=structure_info["encoding"], errors="ignore"
                ) as f:
                    lines = f.readlines()

                # Datenzeilen extrahieren
                data_lines = lines[data_start_line - 1 :]  # -1 wegen 0-basiertem Index

                if max_rows:
                    data_lines = data_lines[:max_rows]

                parsed_data = []
                for line_num, line in enumerate(data_lines):
                    parts = line.strip().split(structure_info["delimiter"])
                    if len(parts) >= len(columns):
                        parsed_data.append(parts[: len(columns)])

                    # Progress für große Dateien
                    if len(data_lines) > 1000 and line_num % 1000 == 0:
                        print(f"  📊 Verarbeitet: {line_num:,} Zeilen")

                if parsed_data:
                    df = pd.DataFrame(parsed_data, columns=columns)

                    # Datentyp-Konvertierung
                    print("🔄 Konvertiere Datentypen...")
                    for col in df.columns:
                        try:
                            # Versuche numerische Konvertierung
                            df[col] = pd.to_numeric(df[col], errors="coerce")
                        except:
                            # Behalte als String bei Fehlern
                            pass

                    print(
                        f"✅ DataFrame erstellt: {df.shape[0]:,} Zeilen × {df.shape[1]} Spalten"
                    )
                else:
                    print("⚠️ Keine gültigen Datenzeilen gefunden")

            except Exception as e:
                print(f"❌ Fehler beim DataFrame-Erstellen: {e}")

        # Parsing-Historie aktualisieren
        parsing_result = {
            "file_path": file_path,
            "timestamp": pd.Timestamp.now().isoformat(),
            "success": not df.empty,
            "rows_parsed": len(df) if not df.empty else 0,
            "columns_found": len(columns) if columns else 0,
        }
        self.parsing_history.append(parsing_result)

        return {
            "metadata": metadata,
            "data": df,
            "info": {
                "structure": structure_info,
                "header_line": header_line,
                "data_start_line": data_start_line,
                "columns": columns if columns else [],
                "parsing_success": not df.empty,
            },
        }

    def export_parsing_report(self, output_path: str) -> None:
        """
        Exportiert einen Bericht über alle Parsing-Vorgänge

        Parameters:
        -----------
        output_path : str
            Pfad für den Bericht
        """
        if not self.parsing_history:
            print("⚠️ Keine Parsing-Historie verfügbar")
            return

        report = {
            "summary": {
                "total_files_parsed": len(self.parsing_history),
                "successful_parses": sum(
                    1 for p in self.parsing_history if p["success"]
                ),
                "total_rows_processed": sum(
                    p["rows_parsed"] for p in self.parsing_history
                ),
                "report_generated": pd.Timestamp.now().isoformat(),
            },
            "parsing_history": self.parsing_history,
        }

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2, ensure_ascii=False)

        print(f"📊 Parsing-Bericht exportiert: {output_path}")


def main():
    """
    Beispiel für die Verwendung des Bystronic CSV Parsers
    """
    print("🔧 Bystronic CSV Parser - Demo")
    print("=" * 50)

    # Parser initialisieren
    parser = BystronicCSVParser()

    # Beispiel-CSV-Datei (angenommen sie existiert)
    csv_file = get_data_path("large", "V084_Scope.csv")

    if Path(csv_file).exists():
        print(f"📁 Verarbeite: {csv_file}")

        # CSV parsen
        result = parser.parse_complex_csv(
            csv_file,
            max_rows=1000,  # Limitiere auf 1000 Zeilen für Demo
        )

        # Ergebnisse anzeigen
        print("\n📋 Metadaten:")
        for key, value in result["metadata"].items():
            print(f"  {key}: {value}")

        df = result["data"]
        if not df.empty:
            print("\n📊 DataFrame Info:")
            print(f"  Shape: {df.shape}")
            print(
                f"  Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB"
            )

            print(f"\n🔢 Spalten ({len(df.columns)}):")
            for i, col in enumerate(df.columns[:10]):  # Erste 10 Spalten
                print(f"  {i + 1:2d}. {col}")
            if len(df.columns) > 10:
                print(f"     ... und {len(df.columns) - 10} weitere")

            print("\n📈 Erste 5 Zeilen:")
            print(df.head().to_string())

            print("\n📈 Statistische Übersicht (erste 5 numerische Spalten):")
            numeric_cols = df.select_dtypes(include=[np.number]).columns[:5]
            if len(numeric_cols) > 0:
                print(df[numeric_cols].describe().to_string())

            # Export-Beispiel
            output_file = get_data_path("examples", "parsed_bystronic_data.csv")
            df.to_csv(output_file, index=False)
            print(f"\n💾 Daten exportiert: {output_file}")

        # Parsing-Bericht erstellen
        report_file = get_data_path("examples", "parsing_report.json")
        parser.export_parsing_report(report_file)

    else:
        print(f"❌ Datei nicht gefunden: {csv_file}")

        # Erstelle Beispiel-CSV für Demo
        print("\n📝 Erstelle Beispiel-CSV...")
        create_sample_complex_csv(get_data_path("examples", "sample_complex.csv"))

        # Parse die Beispiel-Datei
        result = parser.parse_complex_csv(
            get_data_path("examples", "sample_complex.csv")
        )

        df = result["data"]
        if not df.empty:
            print(f"\n✅ Beispiel-CSV erfolgreich geparst: {df.shape}")


def create_sample_complex_csv(output_path: str) -> None:
    """
    Erstellt eine Beispiel-CSV mit komplexer Struktur
    """
    content = """Name\tDistance Control
File\tO:\\Messungen\\Sample\\V001_Demo.csv
Starttime of export\t133964386997165000\tDienstag, 8. Juli 2025\t09:58:19.716
Endtime of export\t133964388292505000\tDienstag, 8. Juli 2025\t10:00:29.250


Name\tTEMP_01\tName\tVIBR_01\tName\tPOWER_01\tName\tPRESS_01\tName\tSPEED_01
SymbolComment\tTemperatur\tSymbolComment\tVibration\tSymbolComment\tLeistung\tSymbolComment\tDruck\tSymbolComment\tGeschwindigkeit
Data-Type\tREAL64\tData-Type\tREAL64\tData-Type\tREAL64\tData-Type\tREAL64\tData-Type\tREAL64
SampleTime[ms]\t1000\tSampleTime[ms]\t1000\tSampleTime[ms]\t1000\tSampleTime[ms]\t1000\tSampleTime[ms]\t1000
VariableSize\t8\tVariableSize\t8\tVariableSize\t8\tVariableSize\t8\tVariableSize\t8

0\t22.5\t0\t1.2\t0\t6200\t0\t5.2\t0\t2500
1\t22.8\t1\t1.4\t1\t6180\t1\t5.1\t1\t2480
2\t23.1\t2\t1.1\t2\t6220\t2\t5.3\t2\t2520
3\t23.4\t3\t1.3\t3\t6190\t3\t5.2\t3\t2510
4\t22.9\t4\t1.5\t4\t6210\t4\t5.4\t4\t2490
5\t22.6\t5\t1.2\t5\t6180\t5\t5.1\t5\t2505
"""

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"✅ Beispiel-CSV erstellt: {output_path}")


if __name__ == "__main__":
    main()
