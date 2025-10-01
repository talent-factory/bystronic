#!/usr/bin/env python3
"""
CSV Import Grundlagen

Grundlegende Techniken für den Import von CSV-Dateien mit pandas.
Behandelt verschiedene Trennzeichen, Encodings und Datentypen.

Autor: Python Grundkurs SmartFactory
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def get_data_path(*args):
    """
    Hilfsfunktion zum korrekten Konstruieren der Datenpfade
    """
    project_root = Path(__file__).parent.parent.parent.parent
    data_path = project_root / "data"
    for arg in args:
        data_path = data_path / arg
    return data_path


def csv_import_beispiele():
    """
    Zeigt verschiedene CSV-Import-Szenarien
    """
    print("📊 CSV Import Grundlagen")
    print("=" * 40)

    # Beispiel 1: Standard CSV mit Komma
    print("\n1️⃣ Standard CSV (Komma-getrennt)")

    # Beispieldaten erstellen
    data = {
        "Datum": pd.date_range("2024-01-01", periods=100),
        "Maschine": np.random.choice(["A", "B", "C"], 100),
        "Produktion": np.random.randint(800, 1200, 100),
        "Temperatur": np.random.normal(23, 2, 100),
        "Verfügbarkeit": np.random.uniform(80, 95, 100),
    }
    df_sample = pd.DataFrame(data)

    # Als CSV speichern
    csv_file = get_data_path("examples", "sample_standard.csv")
    csv_file.parent.mkdir(parents=True, exist_ok=True)
    df_sample.to_csv(csv_file, index=False)

    # CSV laden
    df_loaded = pd.read_csv(csv_file)
    print(f"✅ Geladen: {df_loaded.shape}")
    print(df_loaded.head(3))

    # Beispiel 2: CSV mit Semikolon (deutsches Format)
    print("\n2️⃣ CSV mit Semikolon-Trennung")

    csv_file_semi = get_data_path("examples", "sample_semicolon.csv")
    df_sample.to_csv(csv_file_semi, index=False, sep=";", decimal=",")

    # Laden mit spezifischen Parametern
    df_semi = pd.read_csv(csv_file_semi, sep=";", decimal=",")
    print(f"✅ Geladen: {df_semi.shape}")

    # Beispiel 3: CSV mit Tab-Trennung
    print("\n3️⃣ CSV mit Tab-Trennung")

    csv_file_tab = get_data_path("examples", "sample_tab.csv")
    df_sample.to_csv(csv_file_tab, index=False, sep="\t")

    df_tab = pd.read_csv(csv_file_tab, sep="\t")
    print(f"✅ Geladen: {df_tab.shape}")

    # Beispiel 4: CSV mit benutzerdefinierten Spalten
    print("\n4️⃣ Spezielle Spalten auswählen")

    # Nur bestimmte Spalten laden
    specific_cols = ["Datum", "Maschine", "Produktion"]
    df_subset = pd.read_csv(csv_file, usecols=specific_cols)
    print(f"✅ Geladen (nur {len(specific_cols)} Spalten): {df_subset.shape}")
    print(df_subset.head(3))

    # Beispiel 5: Datentypen explizit definieren
    print("\n5️⃣ Explizite Datentyp-Definition")

    dtype_dict = {
        "Maschine": "category",
        "Produktion": "int32",
        "Temperatur": "float32",
        "Verfügbarkeit": "float32",
    }

    df_typed = pd.read_csv(csv_file, dtype=dtype_dict, parse_dates=["Datum"])
    print("✅ Datentypen definiert:")
    print(df_typed.dtypes)

    return {
        "standard": df_loaded,
        "semicolon": df_semi,
        "tab": df_tab,
        "subset": df_subset,
        "typed": df_typed,
    }


def csv_probleme_loesen():
    """
    Behandelt häufige CSV-Import-Probleme
    """
    print("\n🛠️ CSV-Probleme lösen")
    print("=" * 40)

    # Problem 1: Fehlende Werte
    print("\n❌ Problem 1: Fehlende Werte")

    problematic_data = """Maschine,Produktion,Temperatur,Status
A,1000,23.5,OK
B,,24.1,OK
C,950,,WARNING
D,1100,22.8,
"""

    problem_file = get_data_path("examples", "problem_missing.csv")
    problem_file.parent.mkdir(parents=True, exist_ok=True)
    with open(problem_file, "w") as f:
        f.write(problematic_data)

    # Verschiedene Strategien für fehlende Werte
    df_problem = pd.read_csv(problem_file)
    print("Original mit fehlenden Werten:")
    print(df_problem)
    print(f"Fehlende Werte: {df_problem.isnull().sum().sum()}")

    # Strategie 1: Zeilen mit fehlenden Werten entfernen
    df_dropna = df_problem.dropna()
    print(f"\n✅ Nach dropna(): {df_dropna.shape[0]} Zeilen")

    # Strategie 2: Fehlende Werte ersetzen
    df_filled = df_problem.fillna(
        {
            "Produktion": df_problem["Produktion"].mean(),
            "Temperatur": df_problem["Temperatur"].mean(),
            "Status": "UNKNOWN",
        }
    )
    print(f"✅ Nach fillna(): {df_filled.isnull().sum().sum()} fehlende Werte")

    # Problem 2: Inkonsistente Trennzeichen
    print("\n❌ Problem 2: Gemischte Trennzeichen")

    mixed_data = """Name;Wert,Einheit
"Temperatur";23,5;"°C"
"Druck",5.2;"bar"
"Geschwindigkeit";2500;"mm/min"
"""

    problem_file2 = get_data_path("examples", "problem_mixed.csv")
    with open(problem_file2, "w") as f:
        f.write(mixed_data)

    # Lösung: Manuelle Bereinigung oder komplexerer Parser
    try:
        df_mixed = pd.read_csv(problem_file2, sep=";", quotechar='"')
        print(f"✅ Gemischte Datei geladen: {df_mixed.shape}")
        print(df_mixed)
    except Exception as e:
        print(f"⚠️ Fehler: {e}")

    # Problem 3: Encoding-Probleme
    print("\n❌ Problem 3: Encoding-Probleme")

    # Simuliere Umlaute
    german_data = "Maschine,Größe,Qualität\nA,Groß,Ausgezeichnet\nB,Klein,Güt\n"

    problem_file3 = get_data_path("examples", "problem_encoding.csv")
    with open(problem_file3, "w", encoding="latin1") as f:
        f.write(german_data)

    # Verschiedene Encoding-Versuche
    encodings = ["utf-8", "latin1", "cp1252"]

    for encoding in encodings:
        try:
            df_enc = pd.read_csv(problem_file3, encoding=encoding)
            print(f"✅ Erfolgreich mit {encoding}: {df_enc.shape}")
            print(df_enc.head(1))
            break
        except UnicodeDecodeError:
            print(f"❌ Fehlgeschlagen mit {encoding}")


def csv_performance_optimierung():
    """
    Zeigt Performance-Optimierungen für große CSV-Dateien
    """
    print("\n⚡ Performance-Optimierung")
    print("=" * 40)

    # Große Beispieldatei erstellen
    print("📝 Erstelle große Testdatei...")
    large_data = {
        "ID": range(100000),
        "Timestamp": pd.date_range("2024-01-01", periods=100000, freq="1min"),
        "Maschine": np.random.choice(["A", "B", "C", "D"], 100000),
        "Wert1": np.random.randn(100000),
        "Wert2": np.random.randn(100000),
        "Wert3": np.random.randn(100000),
        "Status": np.random.choice(["OK", "WARNING", "ERROR"], 100000),
    }

    df_large = pd.DataFrame(large_data)
    large_file = get_data_path("examples", "large_sample.csv")
    df_large.to_csv(large_file, index=False)

    file_size = Path(large_file).stat().st_size / 1024 / 1024
    print(f"✅ Testdatei erstellt: {file_size:.1f} MB")

    # Methode 1: Chunked Reading
    print("\n1️⃣ Chunked Reading")

    chunk_size = 10000
    chunks = []

    for chunk in pd.read_csv(large_file, chunksize=chunk_size):
        # Verarbeitung pro Chunk
        chunk_processed = chunk[chunk["Status"] == "OK"]
        chunks.append(chunk_processed)

        if len(chunks) >= 3:  # Nur erste 3 Chunks für Demo
            break

    df_chunked = pd.concat(chunks, ignore_index=True)
    print(f"✅ Chunked processing: {df_chunked.shape}")

    # Methode 2: Spezifische Spalten laden
    print("\n2️⃣ Nur benötigte Spalten laden")

    needed_cols = ["Timestamp", "Maschine", "Wert1"]
    df_subset = pd.read_csv(large_file, usecols=needed_cols)
    print(f"✅ Subset geladen: {df_subset.shape}")

    # Methode 3: Datentypen optimieren
    print("\n3️⃣ Optimierte Datentypen")

    dtypes = {
        "ID": "int32",
        "Maschine": "category",
        "Wert1": "float32",
        "Wert2": "float32",
        "Wert3": "float32",
        "Status": "category",
    }

    df_optimized = pd.read_csv(large_file, dtype=dtypes, parse_dates=["Timestamp"])

    # Memory usage vergleichen
    memory_original = df_large.memory_usage(deep=True).sum() / 1024**2
    memory_optimized = df_optimized.memory_usage(deep=True).sum() / 1024**2

    print(f"Memory Original: {memory_original:.1f} MB")
    print(f"Memory Optimiert: {memory_optimized:.1f} MB")
    print(
        f"Einsparung: {(memory_original - memory_optimized) / memory_original * 100:.1f}%"
    )


def visualisiere_csv_daten(dataframes_dict):
    """
    Erstellt Visualisierungen der importierten CSV-Daten
    """
    print("\n📊 CSV-Daten Visualisierung")
    print("=" * 40)

    df = dataframes_dict["typed"]  # Verwende die typisierte Version

    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle("CSV Import Analyse", fontsize=16)

    # Plot 1: Produktionsverteilung pro Maschine
    production_by_machine = df.groupby("Maschine")["Produktion"].mean()
    axes[0, 0].bar(
        production_by_machine.index,
        production_by_machine.values,
        color=["steelblue", "lightcoral", "lightgreen"],
    )
    axes[0, 0].set_title("Durchschnittliche Produktion pro Maschine")
    axes[0, 0].set_ylabel("Stück pro Tag")

    # Plot 2: Temperaturverteilung
    axes[0, 1].hist(df["Temperatur"], bins=20, alpha=0.7, edgecolor="black")
    axes[0, 1].set_title("Temperaturverteilung")
    axes[0, 1].set_xlabel("Temperatur °C")
    axes[0, 1].set_ylabel("Häufigkeit")

    # Plot 3: Zeitreihe der Produktion
    df_daily = df.set_index("Datum")["Produktion"].resample("D").sum()
    axes[1, 0].plot(df_daily.index, df_daily.values, color="darkgreen")
    axes[1, 0].set_title("Tagesproduktion über Zeit")
    axes[1, 0].set_xlabel("Datum")
    axes[1, 0].set_ylabel("Gesamtproduktion")
    axes[1, 0].tick_params(axis="x", rotation=45)

    # Plot 4: Verfügbarkeit vs Produktion
    axes[1, 1].scatter(df["Verfügbarkeit"], df["Produktion"], alpha=0.6, s=30)
    axes[1, 1].set_title("Verfügbarkeit vs Produktion")
    axes[1, 1].set_xlabel("Verfügbarkeit %")
    axes[1, 1].set_ylabel("Produktion Stück")

    plt.tight_layout()
    plt.show()

    # Zusätzliche Statistiken
    print("\n📈 Datenstatistiken:")
    print(f"Gesamtproduktion: {df['Produktion'].sum():,} Stück")
    print(f"Durchschnittstemperatur: {df['Temperatur'].mean():.1f}°C")
    print(f"Durchschnittliche Verfügbarkeit: {df['Verfügbarkeit'].mean():.1f}%")
    print(
        f"Produktivste Maschine: {production_by_machine.idxmax()} ({production_by_machine.max():.0f} Stück/Tag)"
    )


def main():
    """
    Hauptfunktion - demonstriert alle CSV-Import-Techniken
    """
    print("🚀 CSV Import Grundlagen - Comprehensive Demo")
    print("=" * 60)

    # Grundlegende Import-Beispiele
    dataframes = csv_import_beispiele()

    # Probleme und Lösungen
    csv_probleme_loesen()

    # Performance-Optimierung
    csv_performance_optimierung()

    # Visualisierung
    visualisiere_csv_daten(dataframes)

    print("\n🎉 CSV Import Demo abgeschlossen!")
    print("\n💡 Wichtige Erkenntnisse:")
    print("  • Immer das richtige Trennzeichen verwenden")
    print("  • Encoding-Probleme frühzeitig erkennen")
    print("  • Datentypen für bessere Performance optimieren")
    print("  • Chunked Reading für große Dateien")
    print("  • Fehlende Werte strategisch behandeln")


if __name__ == "__main__":
    main()
