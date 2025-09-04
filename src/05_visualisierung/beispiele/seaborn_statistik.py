#!/usr/bin/env python3
"""
Seaborn Statistische Visualisierung - Beispielskript für erweiterte Plots

Dieses Skript demonstriert die Verwendung von Seaborn für statistische
Visualisierungen mit modernem Design und erweiterten Plot-Typen
für Bystronic-Anwendungen.

Autor: Python Grundkurs Bystronic
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")

# Seaborn Style setzen
sns.set_theme(style="whitegrid", palette="husl")


def main() -> None:
    """Hauptfunktion für Seaborn-Statistik-Plots"""
    print("=" * 70)
    print("BYSTRONIC - SEABORN STATISTISCHE VISUALISIERUNG")
    print("=" * 70)

    print("\n📊 Seaborn-Features:")
    print("- Moderne, ästhetische Plot-Styles")
    print("- Erweiterte statistische Plots")
    print("- Automatische Datengruppierung")
    print("- Korrelationsmatrizen und Heatmaps")
    print("- Verteilungsanalysen")

    # 1. Datenset erstellen
    print("\n1️⃣ Maschinendaten-Generierung")
    print("-" * 40)
    df_machines = create_machine_dataset()

    # 2. Distributionsplots
    print("\n2️⃣ Verteilungsanalysen")
    print("-" * 40)
    demo_distribution_plots(df_machines)

    # 3. Korrelationsanalysen
    print("\n3️⃣ Korrelations- und Heatmaps")
    print("-" * 40)
    demo_correlation_analysis(df_machines)

    # 4. Kategorische Daten
    print("\n4️⃣ Kategorische Datenanalyse")
    print("-" * 40)
    demo_categorical_plots(df_machines)

    # 5. Pairwise Plots
    print("\n5️⃣ Paarweise Vergleiche")
    print("-" * 40)
    demo_pairwise_plots(df_machines)

    # 6. Time Series mit Seaborn
    print("\n6️⃣ Zeitreihen-Visualisierung")
    print("-" * 40)
    demo_timeseries_plots()

    print(f"\n{'=' * 70}")
    print("✅ Seaborn statistische Visualisierungen demonstriert!")
    print("🎨 Moderne Plot-Ästhetik für professionelle Präsentationen")
    print("📈 Erweiterte statistische Analysen und Darstellungen")


def create_machine_dataset() -> pd.DataFrame:
    """Erstellt ein realistisches Maschinendaten-Dataset"""
    np.random.seed(42)
    n_samples = 500

    # Maschinentypen
    machine_types = ["Laser_A", "Laser_B", "Presse_C", "Biege_D", "Stanz_E"]
    machine_weights = [0.25, 0.20, 0.20, 0.20, 0.15]  # Unterschiedliche Häufigkeiten

    # Schichten
    shifts = ["Früh", "Spät", "Nacht"]
    shift_weights = [0.4, 0.4, 0.2]

    # Daten generieren
    data = {
        "Maschine": np.random.choice(machine_types, n_samples, p=machine_weights),
        "Schicht": np.random.choice(shifts, n_samples, p=shift_weights),
        "Tag": np.random.randint(1, 31, n_samples),  # Monat mit 30 Tagen
        "Wochentag": np.random.choice(
            ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"], n_samples
        ),
    }

    df = pd.DataFrame(data)

    # Realistische Parameter basierend auf Maschinentyp
    def generate_machine_params(machine: str, shift: str) -> dict:
        """Generiert realistische Parameter für Maschinentyp und Schicht"""
        # Basis-Parameter pro Maschine
        base_params = {
            "Laser_A": {"speed": 120, "quality": 96, "energy": 45, "efficiency": 85},
            "Laser_B": {"speed": 100, "quality": 94, "energy": 40, "efficiency": 82},
            "Presse_C": {"speed": 80, "quality": 92, "energy": 60, "efficiency": 88},
            "Biege_D": {"speed": 60, "quality": 90, "energy": 35, "efficiency": 80},
            "Stanz_E": {"speed": 150, "quality": 88, "energy": 50, "efficiency": 75},
        }

        params = base_params[machine].copy()

        # Schichtfaktoren
        shift_factors = {
            "Früh": {"quality": 1.05, "efficiency": 1.02, "speed": 1.0, "energy": 1.0},
            "Spät": {"quality": 1.0, "efficiency": 1.0, "speed": 1.0, "energy": 1.0},
            "Nacht": {
                "quality": 0.95,
                "efficiency": 0.93,
                "speed": 0.98,
                "energy": 1.05,
            },
        }

        factors = shift_factors[shift]

        # Parameter anpassen und Rauschen hinzufügen
        return {
            "Geschwindigkeit": params["speed"] * factors["speed"]
            + np.random.normal(0, 10),
            "Qualitaet": params["quality"] * factors["quality"]
            + np.random.normal(0, 2),
            "Energieverbrauch": params["energy"] * factors["energy"]
            + np.random.normal(0, 5),
            "Effizienz": params["efficiency"] * factors["efficiency"]
            + np.random.normal(0, 3),
        }

    # Parameter für jede Zeile generieren
    machine_params = [
        generate_machine_params(row["Maschine"], row["Schicht"])
        for _, row in df.iterrows()
    ]

    # Parameter zu DataFrame hinzufügen
    param_df = pd.DataFrame(machine_params)
    df = pd.concat([df, param_df], axis=1)

    # Negative Werte vermeiden und realistische Bereiche sicherstellen
    df["Geschwindigkeit"] = np.clip(df["Geschwindigkeit"], 30, 200)
    df["Qualitaet"] = np.clip(df["Qualitaet"], 70, 100)
    df["Energieverbrauch"] = np.clip(df["Energieverbrauch"], 20, 80)
    df["Effizienz"] = np.clip(df["Effizienz"], 60, 95)

    # Zusätzliche abgeleitete Variablen
    df["Produktivitaet"] = df["Geschwindigkeit"] * df["Effizienz"] / 100
    df["Kosten_pro_Stueck"] = df["Energieverbrauch"] / df["Geschwindigkeit"] * 0.15  # €
    df["Qualitaetskategorie"] = pd.cut(
        df["Qualitaet"], bins=[0, 85, 92, 100], labels=["Niedrig", "Mittel", "Hoch"]
    )

    print(f"Dataset erstellt: {len(df)} Datensätze")
    print(f"Maschinen: {df['Maschine'].value_counts().to_dict()}")
    print(f"Schichten: {df['Schicht'].value_counts().to_dict()}")

    return df


def demo_distribution_plots(df: pd.DataFrame) -> None:
    """Verteilungsanalysen mit Seaborn"""
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))

    # Histogramm mit KDE
    sns.histplot(
        data=df, x="Qualitaet", hue="Maschine", kde=True, alpha=0.7, ax=axes[0, 0]
    )
    axes[0, 0].set_title(
        "Qualitätsverteilung nach Maschine", fontsize=14, fontweight="bold"
    )
    axes[0, 0].set_xlabel("Qualität (%)")

    # Box-Plot für Schichtvergleich
    sns.boxplot(data=df, x="Schicht", y="Effizienz", ax=axes[0, 1])
    axes[0, 1].set_title("Effizienz nach Schichten", fontsize=14, fontweight="bold")
    axes[0, 1].set_ylabel("Effizienz (%)")

    # Violin-Plot für detaillierte Verteilungsform
    sns.violinplot(data=df, x="Maschine", y="Geschwindigkeit", ax=axes[1, 0])
    axes[1, 0].set_title("Geschwindigkeitsverteilung", fontsize=14, fontweight="bold")
    axes[1, 0].set_ylabel("Geschwindigkeit (mm/min)")
    axes[1, 0].tick_params(axis="x", rotation=45)

    # Strip-Plot mit Jitter für alle Datenpunkte
    sns.stripplot(
        data=df,
        x="Qualitaetskategorie",
        y="Kosten_pro_Stueck",
        hue="Schicht",
        size=4,
        alpha=0.7,
        ax=axes[1, 1],
    )
    axes[1, 1].set_title(
        "Kosten nach Qualitätskategorie", fontsize=14, fontweight="bold"
    )
    axes[1, 1].set_ylabel("Kosten pro Stück (€)")

    plt.tight_layout()
    plt.show()

    # Statistische Tests
    print("📊 Verteilungsanalyse:")

    # Normalitätstest für Qualität
    _, p_value_quality = stats.shapiro(
        df["Qualitaet"].sample(5000) if len(df) > 5000 else df["Qualitaet"]
    )
    print(f"  Normalitätstest Qualität: p-Wert = {p_value_quality:.4f}")
    print(f"  {'Normalverteilt' if p_value_quality > 0.05 else 'Nicht normalverteilt'}")

    # Schichtvergleich mit ANOVA
    schicht_gruppen = [
        group["Effizienz"].values for name, group in df.groupby("Schicht")
    ]
    f_stat, p_value_anova = stats.f_oneway(*schicht_gruppen)
    print(f"  ANOVA Schichten (Effizienz): F = {f_stat:.2f}, p = {p_value_anova:.4f}")
    print(
        f"  {'Signifikanter Unterschied' if p_value_anova < 0.05 else 'Kein signifikanter Unterschied'}"
    )


def demo_correlation_analysis(df: pd.DataFrame) -> None:
    """Korrelationsanalysen und Heatmaps"""
    # Numerische Spalten für Korrelationsanalyse
    numeric_cols = [
        "Geschwindigkeit",
        "Qualitaet",
        "Energieverbrauch",
        "Effizienz",
        "Produktivitaet",
    ]
    corr_data = df[numeric_cols]

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Korrelations-Heatmap
    corr_matrix = corr_data.corr()
    mask = np.triu(
        np.ones_like(corr_matrix, dtype=bool)
    )  # Obere Dreiecksmatrix maskieren

    sns.heatmap(
        corr_matrix,
        mask=mask,
        annot=True,
        cmap="RdBu_r",
        center=0,
        square=True,
        fmt=".2f",
        cbar_kws={"shrink": 0.8},
        ax=axes[0, 0],
    )
    axes[0, 0].set_title("Korrelationsmatrix", fontsize=14, fontweight="bold")

    # Clustermap für hierarchische Clustering
    g = sns.clustermap(
        corr_matrix,
        annot=True,
        cmap="RdBu_r",
        center=0,
        square=True,
        fmt=".2f",
        figsize=(8, 6),
    )
    g.fig.suptitle(
        "Hierarchisches Clustering der Korrelationen", fontsize=14, fontweight="bold"
    )
    plt.show()  # Clustermap separat anzeigen

    # Scatter-Plot mit Regression
    sns.scatterplot(
        data=df,
        x="Energieverbrauch",
        y="Geschwindigkeit",
        hue="Maschine",
        size="Qualitaet",
        ax=axes[0, 1],
    )
    sns.regplot(
        data=df,
        x="Energieverbrauch",
        y="Geschwindigkeit",
        scatter=False,
        color="black",
        ax=axes[0, 1],
    )
    axes[0, 1].set_title("Energie vs. Geschwindigkeit", fontsize=14, fontweight="bold")
    axes[0, 1].set_xlabel("Energieverbrauch (kW)")
    axes[0, 1].set_ylabel("Geschwindigkeit (mm/min)")

    # Heatmap für Kategorien
    # Pivot-Tabelle für Durchschnittswerte
    pivot_data = df.pivot_table(
        values="Qualitaet", index="Schicht", columns="Maschine", aggfunc="mean"
    )

    sns.heatmap(
        pivot_data,
        annot=True,
        cmap="YlOrRd",
        fmt=".1f",
        cbar_kws={"label": "Durchschnittsqualität (%)"},
        ax=axes[1, 0],
    )
    axes[1, 0].set_title("Qualität: Schicht × Maschine", fontsize=14, fontweight="bold")

    # Regressionslinie mit Konfidenzintervall
    sns.regplot(data=df, x="Effizienz", y="Produktivitaet", ax=axes[1, 1])
    axes[1, 1].set_title("Effizienz vs. Produktivität", fontsize=14, fontweight="bold")
    axes[1, 1].set_xlabel("Effizienz (%)")
    axes[1, 1].set_ylabel("Produktivität")

    plt.tight_layout()
    plt.show()

    # Korrelationsanalyse ausgeben
    print("🔗 Korrelationsanalyse:")
    strong_correlations = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i + 1, len(corr_matrix.columns)):
            corr_val = corr_matrix.iloc[i, j]
            if abs(corr_val) > 0.5:  # Starke Korrelation
                strong_correlations.append(
                    (corr_matrix.columns[i], corr_matrix.columns[j], corr_val)
                )

    for var1, var2, corr in sorted(
        strong_correlations, key=lambda x: abs(x[2]), reverse=True
    ):
        direction = "positive" if corr > 0 else "negative"
        strength = (
            "sehr stark" if abs(corr) > 0.8 else "stark" if abs(corr) > 0.6 else "mäßig"
        )
        print(f"  {var1} ↔ {var2}: r = {corr:.3f} ({strength} {direction})")


def demo_categorical_plots(df: pd.DataFrame) -> None:
    """Kategorische Datenanalyse mit Seaborn"""
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Count-Plot für kategorische Verteilung
    sns.countplot(data=df, x="Wochentag", hue="Schicht", ax=axes[0, 0])
    axes[0, 0].set_title(
        "Arbeitsverteilung: Wochentag × Schicht", fontsize=14, fontweight="bold"
    )
    axes[0, 0].set_xlabel("Wochentag")
    axes[0, 0].tick_params(axis="x", rotation=45)

    # Bar-Plot mit Konfidenzintervallen
    sns.barplot(
        data=df,
        x="Maschine",
        y="Qualitaet",
        hue="Qualitaetskategorie",
        ci=95,
        ax=axes[0, 1],
    )
    axes[0, 1].set_title(
        "Durchschnittsqualität mit 95% KI", fontsize=14, fontweight="bold"
    )
    axes[0, 1].set_ylabel("Qualität (%)")
    axes[0, 1].tick_params(axis="x", rotation=45)

    # Point-Plot für Trends über Kategorien
    # Qualität über Tage des Monats
    df["Woche"] = ((df["Tag"] - 1) // 7) + 1  # Woche 1-5 im Monat
    sns.pointplot(data=df, x="Woche", y="Effizienz", hue="Maschine", ax=axes[1, 0])
    axes[1, 0].set_title(
        "Effizienztrend über Monatswochen", fontsize=14, fontweight="bold"
    )
    axes[1, 0].set_xlabel("Woche im Monat")
    axes[1, 0].set_ylabel("Effizienz (%)")

    # Swarm-Plot für detaillierte Punktverteilung
    # Sample für bessere Performance bei vielen Datenpunkten
    df_sample = df.sample(n=min(200, len(df)), random_state=42)
    sns.swarmplot(
        data=df_sample,
        x="Schicht",
        y="Energieverbrauch",
        hue="Qualitaetskategorie",
        ax=axes[1, 1],
    )
    axes[1, 1].set_title(
        "Energieverbrauch nach Schicht und Qualität", fontsize=14, fontweight="bold"
    )
    axes[1, 1].set_ylabel("Energieverbrauch (kW)")

    plt.tight_layout()
    plt.show()

    # Kategorische Statistiken
    print("📋 Kategorische Analyse:")

    # Chi-Quadrat-Test für Unabhängigkeit
    contingency_table = pd.crosstab(df["Schicht"], df["Qualitaetskategorie"])
    chi2, p_value, dof, expected = stats.chi2_contingency(contingency_table)
    print("  Chi²-Test (Schicht × Qualitätskategorie):")
    print(f"    Chi² = {chi2:.2f}, p = {p_value:.4f}")
    print(
        f"    {'Signifikante Abhängigkeit' if p_value < 0.05 else 'Keine signifikante Abhängigkeit'}"
    )

    # Beste und schlechteste Kombinationen
    mean_by_combination = df.groupby(["Schicht", "Maschine"])["Qualitaet"].mean()
    best_combo = mean_by_combination.idxmax()
    worst_combo = mean_by_combination.idxmin()

    print(
        f"  Beste Kombination: {best_combo[0]} + {best_combo[1]} "
        f"({mean_by_combination[best_combo]:.1f}% Qualität)"
    )
    print(
        f"  Schlechteste Kombination: {worst_combo[0]} + {worst_combo[1]} "
        f"({mean_by_combination[worst_combo]:.1f}% Qualität)"
    )


def demo_pairwise_plots(df: pd.DataFrame) -> None:
    """Paarweise Vergleiche und Pair-Plots"""
    print("🔍 Erstelle Paar-Plots (kann etwas dauern)...")

    # Subset für Pair-Plot (Performance)
    cols_for_pairs = ["Geschwindigkeit", "Qualitaet", "Energieverbrauch", "Effizienz"]
    df_pairs = df[cols_for_pairs + ["Maschine"]].sample(
        n=min(300, len(df)), random_state=42
    )

    # Pair-Plot
    g = sns.pairplot(
        df_pairs, hue="Maschine", diag_kind="kde", plot_kws={"alpha": 0.7, "s": 30}
    )
    g.fig.suptitle(
        "Paarweise Vergleiche aller Parameter", y=1.02, fontsize=16, fontweight="bold"
    )
    plt.show()

    # Joint-Plot für detaillierte Analyse einer Beziehung
    g2 = sns.jointplot(
        data=df,
        x="Energieverbrauch",
        y="Qualitaet",
        hue="Schicht",
        kind="scatter",
        height=8,
    )
    g2.plot_joint(sns.regplot, scatter=False, color="black")
    g2.fig.suptitle(
        "Detailanalyse: Energie vs. Qualität", y=1.02, fontsize=16, fontweight="bold"
    )
    plt.show()

    # Facet-Grid für mehrere Subplots
    g3 = sns.FacetGrid(df, col="Schicht", hue="Maschine", height=4, aspect=1.2)
    g3.map(sns.scatterplot, "Geschwindigkeit", "Qualitaet", alpha=0.7)
    g3.add_legend()
    for ax in g3.axes.flat:
        ax.set_xlim(30, 200)
        ax.set_ylim(70, 100)
    g3.fig.suptitle(
        "Geschwindigkeit vs. Qualität nach Schichten",
        y=1.02,
        fontsize=16,
        fontweight="bold",
    )
    plt.show()

    print("✅ Paar-Plots abgeschlossen")


def demo_timeseries_plots() -> None:
    """Zeitreihen-Visualisierung mit Seaborn"""
    # Zeitreihen-Daten generieren
    dates = pd.date_range("2024-01-01", periods=365, freq="D")

    # Mehrere Maschinen über ein Jahr
    machines = ["Laser_A", "Laser_B", "Presse_C"]

    ts_data = []
    for machine in machines:
        # Basis-Effizienz mit saisonalen Schwankungen
        trend = np.linspace(80, 85, len(dates))  # Leichter Aufwärtstrend
        seasonal = 5 * np.sin(
            2 * np.pi * np.arange(len(dates)) / 365.25
        )  # Jahresschwankung
        weekly = 2 * np.sin(2 * np.pi * np.arange(len(dates)) / 7)  # Wochenschwankung
        noise = np.random.normal(0, 2, len(dates))

        # Maschinenspezifische Offsets
        machine_offset = {"Laser_A": 5, "Laser_B": 0, "Presse_C": -3}[machine]

        efficiency = trend + seasonal + weekly + noise + machine_offset
        efficiency = np.clip(efficiency, 70, 95)

        for date, eff in zip(dates, efficiency, strict=False):
            ts_data.append(
                {
                    "Datum": date,
                    "Maschine": machine,
                    "Effizienz": eff,
                    "Monat": date.month,
                    "Wochentag": date.day_name(),
                }
            )

    df_ts = pd.DataFrame(ts_data)

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Zeitreihen-Plot
    sns.lineplot(data=df_ts, x="Datum", y="Effizienz", hue="Maschine", ax=axes[0, 0])
    axes[0, 0].set_title("Effizienz über Zeit (2024)", fontsize=14, fontweight="bold")
    axes[0, 0].tick_params(axis="x", rotation=45)

    # Monatliche Durchschnitte
    monthly_avg = df_ts.groupby(["Monat", "Maschine"])["Effizienz"].mean().reset_index()
    sns.lineplot(
        data=monthly_avg,
        x="Monat",
        y="Effizienz",
        hue="Maschine",
        marker="o",
        ax=axes[0, 1],
    )
    axes[0, 1].set_title(
        "Monatliche Durchschnittseffizienz", fontsize=14, fontweight="bold"
    )
    axes[0, 1].set_xticks(range(1, 13))
    axes[0, 1].set_xticklabels(
        [
            "Jan",
            "Feb",
            "Mär",
            "Apr",
            "Mai",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Okt",
            "Nov",
            "Dez",
        ]
    )

    # Wochentag-Analyse
    weekday_order = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    sns.boxplot(
        data=df_ts, x="Wochentag", y="Effizienz", order=weekday_order, ax=axes[1, 0]
    )
    axes[1, 0].set_title("Effizienz nach Wochentagen", fontsize=14, fontweight="bold")
    axes[1, 0].tick_params(axis="x", rotation=45)

    # Heatmap für Monat × Wochentag
    pivot_weekday = df_ts.pivot_table(
        values="Effizienz", index="Monat", columns="Wochentag", aggfunc="mean"
    )
    # Spalten nach Wochentag sortieren
    pivot_weekday = pivot_weekday.reindex(columns=weekday_order)

    sns.heatmap(pivot_weekday, annot=True, fmt=".1f", cmap="YlOrRd", ax=axes[1, 1])
    axes[1, 1].set_title(
        "Durchschnittseffizienz: Monat × Wochentag", fontsize=14, fontweight="bold"
    )
    axes[1, 1].set_yticklabels(
        [
            "Jan",
            "Feb",
            "Mär",
            "Apr",
            "Mai",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Okt",
            "Nov",
            "Dez",
        ]
    )

    plt.tight_layout()
    plt.show()

    # Zeitreihen-Statistiken
    print("📅 Zeitreihen-Analyse:")
    overall_trend = df_ts.groupby(df_ts["Datum"].dt.quarter)["Effizienz"].mean()
    print("  Quartalsweise Effizienz:")
    for quarter, eff in overall_trend.items():
        print(f"    Q{quarter}: {eff:.1f}%")

    # Beste und schlechteste Tage
    daily_avg = df_ts.groupby("Datum")["Effizienz"].mean()
    best_day = daily_avg.idxmax()
    worst_day = daily_avg.idxmin()

    print(f"  Bester Tag: {best_day.strftime('%d.%m.%Y')} ({daily_avg[best_day]:.1f}%)")
    print(
        f"  Schlechtester Tag: {worst_day.strftime('%d.%m.%Y')} ({daily_avg[worst_day]:.1f}%)"
    )


if __name__ == "__main__":
    # Prüfen ob alle benötigten Bibliotheken verfügbar sind
    try:
        import scipy.stats  # noqa: F401
    except ImportError:
        print("⚠️ Hinweis: scipy nicht installiert - Statistische Tests nicht verfügbar")
        print("Installation: pip install scipy")

    main()
