#!/usr/bin/env python3
"""
Übung 01: CSV Import Basics

Lernziele:
- CSV-Dateien mit verschiedenen Trennzeichen importieren
- Datentypen korrekt erkennen und konvertieren
- Fehlende Werte behandeln
- Basis-Validierung implementieren

Schwierigkeitsgrad: ⭐⭐☆☆
Geschätzte Zeit: 30-45 Minuten
"""

from pathlib import Path

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


def setup_test_data():
    """
    Erstellt Testdaten für die Übungen
    """
    print("🏗️ Erstelle Testdaten für CSV-Übungen...")

    # Testdaten-Verzeichnis erstellen
    test_dir = get_data_path("uebungen", "csv_basics")
    test_dir.mkdir(parents=True, exist_ok=True)

    # 1. Standard CSV mit Komma
    standard_data = {
        "Datum": pd.date_range("2024-01-01", periods=50),
        "Maschine": np.random.choice(["Alpha", "Beta", "Gamma"], 50),
        "Produktion": np.random.randint(500, 1500, 50),
        "Temperatur": np.round(np.random.normal(23, 3, 50), 1),
        "Status": np.random.choice(["OK", "WARNING", "ERROR"], 50, p=[0.7, 0.2, 0.1]),
    }
    df_standard = pd.DataFrame(standard_data)
    df_standard.to_csv(test_dir / "standard_data.csv", index=False)

    # 2. CSV mit Semikolon und deutschen Dezimaltrennern
    german_data = df_standard.copy()
    german_file = test_dir / "german_format.csv"
    german_data.to_csv(german_file, index=False, sep=";", decimal=",")

    # 3. CSV mit Tab-Trennung
    tab_file = test_dir / "tab_separated.csv"
    df_standard.to_csv(tab_file, index=False, sep="\t")

    # 4. CSV mit fehlenden Werten
    missing_data = df_standard.copy()
    # Zufällig einige Werte auf NaN setzen
    missing_indices = np.random.choice(len(missing_data), size=15, replace=False)
    missing_data.loc[missing_indices, "Produktion"] = np.nan
    missing_indices = np.random.choice(len(missing_data), size=8, replace=False)
    missing_data.loc[missing_indices, "Temperatur"] = np.nan
    missing_data.to_csv(test_dir / "data_with_missing.csv", index=False)

    # 5. Problematische CSV mit inkonsistenten Daten
    problematic_data = """Maschine;Produktion;Temperatur;Verfuegbarkeit
Alpha;1000;22.5;95.0
Beta;;23.1;88.5
Gamma;1200;-999;92.0
Delta;800;24.2;
Alpha;1500;25.8;120.5
Beta;FEHLER;21.3;85.2
Gamma;900;0;75.0"""

    with open(test_dir / "problematic_data.csv", "w") as f:
        f.write(problematic_data)

    print(f"✅ Testdaten erstellt in: {test_dir}")
    return test_dir


# =============================================================================
# AUFGABEN - Lösen Sie die folgenden Übungen
# =============================================================================


def aufgabe_1_grundlegender_import():
    """
    AUFGABE 1: Grundlegender CSV-Import (⭐⭐☆☆)

    TODO: Implementieren Sie eine Funktion, die:
    1. Die Datei 'standard_data.csv' importiert
    2. Die ersten und letzten 3 Zeilen anzeigt
    3. Die Datentypen aller Spalten ausgibt
    4. Die Dimensionen (Zeilen × Spalten) anzeigt

    Tipps:
    - Verwenden Sie pd.read_csv()
    - Nutzen Sie .head() und .tail() für die Anzeige
    - .dtypes zeigt die Datentypen
    - .shape gibt die Dimensionen zurück
    """
    print("\n" + "=" * 50)
    print("📝 AUFGABE 1: Grundlegender CSV-Import")
    print("=" * 50)

    # TODO: Ihren Code hier einfügen

    # Laden Sie die CSV-Datei
    csv_file = get_data_path("uebungen", "csv_basics", "standard_data.csv")

    # LÖSUNG VERSTECKT - Entfernen Sie diese Kommentare für die Musterlösung:
    """
    df = pd.read_csv(csv_file)

    print(f"📊 Dataset geladen: {df.shape[0]} Zeilen × {df.shape[1]} Spalten")

    print("\\n🔼 Erste 3 Zeilen:")
    print(df.head(3))

    print("\\n🔽 Letzte 3 Zeilen:")
    print(df.tail(3))

    print("\\n📋 Datentypen:")
    print(df.dtypes)

    return df
    """

    # Ihre Implementierung:
    pass  # Ersetzen Sie 'pass' durch Ihren Code


def aufgabe_2_verschiedene_trennzeichen():
    """
    AUFGABE 2: Verschiedene Trennzeichen handhaben (⭐⭐☆☆)

    TODO: Implementieren Sie eine Funktion, die:
    1. Alle CSV-Dateien mit verschiedenen Trennzeichen lädt:
       - german_format.csv (Semikolon, Komma als Dezimaltrenner)
       - tab_separated.csv (Tab-getrennt)
    2. Überprüft, ob alle DataFrames identische Inhalte haben
    3. Die verwendeten Trennzeichen dokumentiert

    Tipps:
    - Parameter 'sep' für Trennzeichen
    - Parameter 'decimal' für Dezimaltrenner
    - Verwenden Sie .equals() zum Vergleichen von DataFrames
    """
    print("\n" + "=" * 50)
    print("📝 AUFGABE 2: Verschiedene Trennzeichen")
    print("=" * 50)

    # TODO: Ihren Code hier einfügen

    # LÖSUNG VERSTECKT:
    """
    files_and_params = [
        (get_data_path("uebungen", "csv_basics", "standard_data.csv"), ',', '.'),
        (get_data_path("uebungen", "csv_basics", "german_format.csv"), ';', ','),
        (get_data_path("uebungen", "csv_basics", "tab_separated.csv"), '\\t', '.')
    ]

    dataframes = []

    for file_path, sep, decimal in files_and_params:
        df = pd.read_csv(file_path, sep=sep, decimal=decimal)
        dataframes.append((Path(file_path).name, df, sep, decimal))
        print(f"✅ {Path(file_path).name} geladen (sep='{sep}', decimal='{decimal}'): {df.shape}")

    # Vergleiche alle DataFrames
    base_df = dataframes[0][1]
    for name, df, sep, decimal in dataframes[1:]:
        if base_df.equals(df):
            print(f"✅ {name} ist identisch mit Standard-CSV")
        else:
            print(f"❌ {name} unterscheidet sich von Standard-CSV")

    return dataframes
    """

    # Ihre Implementierung:
    pass


def aufgabe_3_fehlende_werte_behandeln():
    """
    AUFGABE 3: Fehlende Werte erkennen und behandeln (⭐⭐⭐☆)

    TODO: Implementieren Sie eine Funktion, die:
    1. Die Datei 'data_with_missing.csv' lädt
    2. Fehlende Werte pro Spalte zählt und anzeigt
    3. Drei verschiedene Strategien zur Behandlung implementiert:
       - Zeilen mit fehlenden Werten entfernen
       - Fehlende Werte durch Durchschnitt ersetzen
       - Fehlende Werte durch Median ersetzen
    4. Die Ergebnisse aller Strategien vergleicht

    Tipps:
    - .isnull().sum() zählt fehlende Werte
    - .dropna() entfernt Zeilen mit NaN
    - .fillna() ersetzt fehlende Werte
    - .mean() und .median() für Ersatzwerte
    """
    print("\n" + "=" * 50)
    print("📝 AUFGABE 3: Fehlende Werte behandeln")
    print("=" * 50)

    # TODO: Ihren Code hier einfügen

    # LÖSUNG VERSTECKT:
    """
    csv_file = get_data_path("uebungen", "csv_basics", "data_with_missing.csv")
    df_original = pd.read_csv(csv_file)

    print(f"📊 Original Dataset: {df_original.shape}")

    # Fehlende Werte analysieren
    missing_count = df_original.isnull().sum()
    print("\\n❌ Fehlende Werte pro Spalte:")
    for col, count in missing_count.items():
        if count > 0:
            percentage = (count / len(df_original)) * 100
            print(f"  {col}: {count} ({percentage:.1f}%)")

    # Strategie 1: Zeilen entfernen
    df_dropped = df_original.dropna()
    print(f"\\n🗑️ Nach dropna(): {df_dropped.shape[0]} Zeilen ({len(df_original) - len(df_dropped)} entfernt)")

    # Strategie 2: Durchschnitt
    df_mean_filled = df_original.copy()
    numeric_columns = df_original.select_dtypes(include=[np.number]).columns
    for col in numeric_columns:
        if col in missing_count and missing_count[col] > 0:
            mean_value = df_original[col].mean()
            df_mean_filled[col].fillna(mean_value, inplace=True)
            print(f"✅ {col}: Fehlende Werte durch Durchschnitt ersetzt ({mean_value:.2f})")

    # Strategie 3: Median
    df_median_filled = df_original.copy()
    for col in numeric_columns:
        if col in missing_count and missing_count[col] > 0:
            median_value = df_original[col].median()
            df_median_filled[col].fillna(median_value, inplace=True)
            print(f"✅ {col}: Fehlende Werte durch Median ersetzt ({median_value:.2f})")

    # Vergleich der Strategien
    strategies = {
        'Original': df_original,
        'Dropped': df_dropped,
        'Mean Filled': df_mean_filled,
        'Median Filled': df_median_filled
    }

    print("\\n📊 Strategien-Vergleich:")
    for name, df in strategies.items():
        missing = df.isnull().sum().sum()
        print(f"  {name}: {df.shape[0]} Zeilen, {missing} fehlende Werte")

    return strategies
    """

    # Ihre Implementierung:
    pass


def aufgabe_4_datenvalidierung():
    """
    AUFGABE 4: Datenvalidierung implementieren (⭐⭐⭐⭐)

    TODO: Implementieren Sie eine Funktion, die:
    1. Die Datei 'problematic_data.csv' lädt
    2. Datenqualitätsprobleme erkennt und behebt:
       - Negative Temperaturen (< -50°C als unrealistisch markieren)
       - Verfügbarkeit > 100% korrigieren
       - Nicht-numerische Produktionswerte behandeln
       - Leere Strings in numerischen Spalten
    3. Einen Validierungsbericht erstellt
    4. Die bereinigten Daten exportiert

    Tipps:
    - pd.to_numeric() mit errors='coerce' für robuste Konvertierung
    - Boolesche Indexierung für Datenfilterung
    - .describe() für statistische Übersicht
    """
    print("\n" + "=" * 50)
    print("📝 AUFGABE 4: Datenvalidierung")
    print("=" * 50)

    # TODO: Ihren Code hier einfügen

    # LÖSUNG VERSTECKT:
    """
    csv_file = get_data_path("uebungen", "csv_basics", "problematic_data.csv")
    df_raw = pd.read_csv(csv_file, sep=';')

    print(f"📊 Rohdaten geladen: {df_raw.shape}")
    print("\\n🔍 Rohdaten (erste 5 Zeilen):")
    print(df_raw.head())

    # Validierungsbericht initialisieren
    validation_report = {
        'issues_found': [],
        'fixes_applied': [],
        'original_rows': len(df_raw),
        'final_rows': 0
    }

    df_clean = df_raw.copy()

    # Problem 1: Produktionswerte bereinigen
    print("\\n🔧 Bereinige Produktionswerte...")
    df_clean['Produktion'] = pd.to_numeric(df_clean['Produktion'], errors='coerce')
    production_issues = df_raw[df_raw['Produktion'].str.contains('FEHLER', na=False)]
    if not production_issues.empty:
        validation_report['issues_found'].append(f"Nicht-numerische Produktionswerte: {len(production_issues)}")
        validation_report['fixes_applied'].append("Konvertierung zu NaN für weitere Behandlung")

    # Problem 2: Unrealistische Temperaturen
    print("🌡️ Prüfe Temperaturwerte...")
    df_clean['Temperatur'] = pd.to_numeric(df_clean['Temperatur'], errors='coerce')
    unrealistic_temp = df_clean['Temperatur'] < -50
    if unrealistic_temp.sum() > 0:
        validation_report['issues_found'].append(f"Unrealistische Temperaturen: {unrealistic_temp.sum()}")
        df_clean.loc[unrealistic_temp, 'Temperatur'] = np.nan
        validation_report['fixes_applied'].append("Unrealistische Temperaturen auf NaN gesetzt")

    # Problem 3: Verfügbarkeit > 100%
    print("📊 Prüfe Verfügbarkeitsswerte...")
    df_clean['Verfuegbarkeit'] = pd.to_numeric(df_clean['Verfuegbarkeit'], errors='coerce')
    high_availability = df_clean['Verfuegbarkeit'] > 100
    if high_availability.sum() > 0:
        validation_report['issues_found'].append(f"Verfügbarkeit > 100%: {high_availability.sum()}")
        df_clean.loc[high_availability, 'Verfuegbarkeit'] = 100.0
        validation_report['fixes_applied'].append("Verfügbarkeit > 100% auf 100% korrigiert")

    # Problem 4: Fehlende Werte behandeln
    missing_before = df_clean.isnull().sum().sum()
    print(f"🔍 Behandle fehlende Werte: {missing_before} gefunden")

    # Produktions-Mittelwert für fehlende Werte
    production_mean = df_clean['Produktion'].mean()
    df_clean['Produktion'].fillna(production_mean, inplace=True)

    # Verfügbarkeits-Median für fehlende Werte
    availability_median = df_clean['Verfuegbarkeit'].median()
    df_clean['Verfuegbarkeit'].fillna(availability_median, inplace=True)

    missing_after = df_clean.isnull().sum().sum()
    validation_report['fixes_applied'].append(f"Fehlende Werte reduziert: {missing_before} → {missing_after}")

    # Finale Statistiken
    validation_report['final_rows'] = len(df_clean)

    print("\\n📋 Validierungsbericht:")
    print(f"  Ursprüngliche Zeilen: {validation_report['original_rows']}")
    print(f"  Finale Zeilen: {validation_report['final_rows']}")
    print(f"  Gefundene Probleme: {len(validation_report['issues_found'])}")
    for issue in validation_report['issues_found']:
        print(f"    • {issue}")
    print(f"  Angewandte Korrekturen: {len(validation_report['fixes_applied'])}")
    for fix in validation_report['fixes_applied']:
        print(f"    • {fix}")

    # Bereinigte Daten exportieren
    output_file = get_data_path("uebungen", "csv_basics", "cleaned_data.csv")
    df_clean.to_csv(output_file, index=False)
    print(f"\\n💾 Bereinigte Daten exportiert: {output_file}")

    print("\\n📊 Bereinigte Daten (Übersicht):")
    print(df_clean.describe())

    return df_clean, validation_report
    """

    # Ihre Implementierung:
    pass


def aufgabe_5_visualisierung():
    """
    AUFGABE 5: CSV-Daten visualisieren (⭐⭐⭐☆)

    TODO: Erstellen Sie Visualisierungen für die bereinigten Daten:
    1. Histogramm der Produktionsverteilung
    2. Boxplot der Temperatur nach Maschine
    3. Balkendiagramm der durchschnittlichen Verfügbarkeit pro Maschine
    4. Zeitreihenplot der täglichen Gesamtproduktion

    Tipps:
    - Verwenden Sie matplotlib.pyplot
    - plt.subplots() für mehrere Plots
    - .hist(), .boxplot(), .bar() für verschiedene Diagrammtypen
    - .groupby() für Aggregationen
    """
    print("\n" + "=" * 50)
    print("📝 AUFGABE 5: Daten visualisieren")
    print("=" * 50)

    # Laden Sie die bereinigten Daten (falls verfügbar)
    try:
        df_clean = pd.read_csv(
            get_data_path("uebungen", "csv_basics", "cleaned_data.csv")
        )
        print(f"✅ Bereinigte Daten geladen: {df_clean.shape}")
    except FileNotFoundError:
        print("⚠️ Keine bereinigten Daten gefunden. Lade Standarddaten...")
        df_clean = pd.read_csv(
            get_data_path("uebungen", "csv_basics", "standard_data.csv")
        )

    # TODO: Ihren Code hier einfügen

    # LÖSUNG VERSTECKT:
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    fig.suptitle('CSV-Daten Analyse Dashboard', fontsize=16)

    # Plot 1: Produktionsverteilung
    axes[0,0].hist(df_clean['Produktion'], bins=20, alpha=0.7, edgecolor='black')
    axes[0,0].set_title('Produktionsverteilung')
    axes[0,0].set_xlabel('Produktion (Stück)')
    axes[0,0].set_ylabel('Häufigkeit')
    axes[0,0].grid(True, alpha=0.3)

    # Plot 2: Temperatur nach Maschine
    machines = df_clean['Maschine'].unique()
    temp_data = [df_clean[df_clean['Maschine'] == machine]['Temperatur'].dropna() for machine in machines]

    axes[0,1].boxplot(temp_data, labels=machines)
    axes[0,1].set_title('Temperaturverteilung pro Maschine')
    axes[0,1].set_ylabel('Temperatur (°C)')
    axes[0,1].grid(True, alpha=0.3)

    # Plot 3: Verfügbarkeit pro Maschine
    if 'Verfuegbarkeit' in df_clean.columns:
        avg_availability = df_clean.groupby('Maschine')['Verfuegbarkeit'].mean()
        axes[1,0].bar(avg_availability.index, avg_availability.values, color='lightgreen', alpha=0.7)
        axes[1,0].set_title('Durchschnittliche Verfügbarkeit pro Maschine')
        axes[1,0].set_ylabel('Verfügbarkeit (%)')
        axes[1,0].grid(True, alpha=0.3)
    else:
        # Alternative: Status-Verteilung
        status_counts = df_clean['Status'].value_counts()
        axes[1,0].bar(status_counts.index, status_counts.values,
                      color=['green', 'orange', 'red'][:len(status_counts)])
        axes[1,0].set_title('Status-Verteilung')
        axes[1,0].set_ylabel('Anzahl')

    # Plot 4: Zeitreihe (falls Datum verfügbar)
    if 'Datum' in df_clean.columns:
        df_clean['Datum'] = pd.to_datetime(df_clean['Datum'])
        daily_production = df_clean.groupby('Datum')['Produktion'].sum()

        axes[1,1].plot(daily_production.index, daily_production.values, 'b-', alpha=0.7)
        axes[1,1].set_title('Tägliche Gesamtproduktion')
        axes[1,1].set_xlabel('Datum')
        axes[1,1].set_ylabel('Gesamtproduktion')
        axes[1,1].tick_params(axis='x', rotation=45)
        axes[1,1].grid(True, alpha=0.3)
    else:
        # Alternative: Produktion pro Maschine
        prod_by_machine = df_clean.groupby('Maschine')['Produktion'].mean()
        axes[1,1].pie(prod_by_machine.values, labels=prod_by_machine.index, autopct='%1.1f%%')
        axes[1,1].set_title('Produktionsverteilung pro Maschine')

    plt.tight_layout()
    plt.show()

    # Zusätzliche Statistiken
    print("\\n📈 Datenstatistiken:")
    print(f"  Gesamtproduktion: {df_clean['Produktion'].sum():,.0f} Stück")
    print(f"  Durchschnittsproduktion: {df_clean['Produktion'].mean():.0f} Stück/Tag")
    print(f"  Produktivste Maschine: {df_clean.groupby('Maschine')['Produktion'].mean().idxmax()}")
    print(f"  Temperaturbereich: {df_clean['Temperatur'].min():.1f}°C bis {df_clean['Temperatur'].max():.1f}°C")
    """

    # Ihre Implementierung:
    pass


def bonus_aufgabe_performance_vergleich():
    """
    BONUS AUFGABE: Performance-Vergleich (⭐⭐⭐⭐⭐)

    TODO: Erstellen Sie eine Studie, die verschiedene CSV-Import-Methoden vergleicht:
    1. Standard pd.read_csv()
    2. Chunked Reading
    3. Optimierte Datentypen
    4. Nur benötigte Spalten laden

    Messen Sie Ladezeit und Speicherverbrauch für jede Methode.
    """
    print("\n" + "=" * 50)
    print("🏆 BONUS: Performance-Vergleich")
    print("=" * 50)

    # TODO: Implementieren Sie einen Performance-Vergleich verschiedener Import-Methoden

    # Ihre Implementierung hier...
    pass


def main():
    """
    Hauptfunktion - führt alle Übungen aus
    """
    print("🚀 CSV Import Übungen - Interaktives Lernmodul")
    print("=" * 60)

    # Testdaten vorbereiten
    test_dir = setup_test_data()

    print("\n📚 Verfügbare Übungen:")
    print("1. Grundlegender CSV-Import (⭐⭐☆☆)")
    print("2. Verschiedene Trennzeichen (⭐⭐☆☆)")
    print("3. Fehlende Werte behandeln (⭐⭐⭐☆)")
    print("4. Datenvalidierung (⭐⭐⭐⭐)")
    print("5. Visualisierung (⭐⭐⭐☆)")
    print("B. Bonus: Performance-Vergleich (⭐⭐⭐⭐⭐)")

    # Alle Übungen durchführen (entkommentieren zum Aktivieren)
    """
    aufgabe_1_grundlegender_import()
    aufgabe_2_verschiedene_trennzeichen()
    aufgabe_3_fehlende_werte_behandeln()
    aufgabe_4_datenvalidierung()
    aufgabe_5_visualisierung()
    bonus_aufgabe_performance_vergleich()
    """

    print("\n💡 Hinweise zum Lösen der Übungen:")
    print("  • Entkommentieren Sie die TODO-Bereiche")
    print("  • Ersetzen Sie 'pass' durch Ihren Code")
    print("  • Testen Sie jede Funktion einzeln")
    print("  • Die Musterlösung ist als Kommentar verfügbar")

    print("\n🎯 Lernziele erreichen:")
    print("  ✓ CSV-Dateien sicher importieren")
    print("  ✓ Verschiedene Formate handhaben")
    print("  ✓ Datenqualität sicherstellen")
    print("  ✓ Probleme systematisch lösen")


if __name__ == "__main__":
    main()
