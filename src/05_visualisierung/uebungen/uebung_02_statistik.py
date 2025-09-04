#!/usr/bin/env python3
"""
Übung 2: Statistische Visualisierungen - Verteilungen und Zusammenhänge

Diese Übung vertieft Ihr Verständnis für statistische Visualisierungen.
Sie lernen Histogramme, Box-Plots, Heatmaps und Seaborn kennen.

Autor: Python Grundkurs Bystronic
Schwierigkeitsgrad: ⭐⭐⭐⭐ (Fortgeschritten)
Geschätzte Bearbeitungszeit: 60-90 Minuten
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats

warnings.filterwarnings("ignore")

# Seaborn-Stil aktivieren
sns.set_style("whitegrid")
plt.rcParams["figure.facecolor"] = "white"


def main() -> None:
    """Hauptfunktion für Übung 2 - Statistische Visualisierungen"""
    print("=" * 70)
    print("ÜBUNG 2: STATISTISCHE VISUALISIERUNGEN")
    print("=" * 70)
    print("🎯 Lernziele:")
    print("   - Histogramme mit Normalverteilungskurven")
    print("   - Box-Plots für Verteilungsvergleiche")
    print("   - Korrelationsmatrizen und Heatmaps")
    print("   - Seaborn für moderne statistische Plots")
    print("   - Statistische Tests und Interpretation")

    print(f"\n{'=' * 70}")
    print("📝 AUFGABEN")
    print("=" * 70)

    # Aufgabe 1: Erweiterte Histogramm-Analyse
    print("\n📊 Aufgabe 1: Histogramm-Analyse mit Statistiken")
    print("-" * 50)
    aufgabe_1_histogramm_analyse()

    # Aufgabe 2: Box-Plot Vergleiche
    print("\n📊 Aufgabe 2: Box-Plot Vergleiche")
    print("-" * 40)
    aufgabe_2_boxplot_vergleiche()

    # Aufgabe 3: Korrelationsmatrix
    print("\n📊 Aufgabe 3: Korrelationsmatrix-Analyse")
    print("-" * 45)
    aufgabe_3_korrelationsmatrix()

    # Aufgabe 4: Seaborn Pairplot
    print("\n📊 Aufgabe 4: Seaborn Pairplot-Analyse")
    print("-" * 45)
    aufgabe_4_seaborn_pairplot()

    # Aufgabe 5: Statistische Qualitätskontrolle
    print("\n📊 Aufgabe 5: Statistische Prozesskontrolle")
    print("-" * 48)
    aufgabe_5_statistische_qualitaetskontrolle()

    print(f"\n{'=' * 70}")
    print("🎉 GLÜCKWUNSCH ZUR STATISTIK-MEISTERSCHAFT!")
    print("Sie können nun komplexe statistische Analysen visualisieren!")
    print("➡️  Nächste Übung: uebung_03_3d_animation.py")
    print("=" * 70)


def aufgabe_1_histogramm_analyse() -> None:
    """
    Aufgabe 1: Erweiterte Histogramm-Analyse

    TODO für Teilnehmer:
    1. Erstellen Sie Histogramme für drei verschiedene Materialtypen
    2. Überlagern Sie Normalverteilungskurven
    3. Berechnen Sie statistische Kennwerte (Mittelwert, Standardabweichung)
    4. Führen Sie Normalitätstests durch
    5. Interpretieren Sie die Verteilungen
    """
    print("🔨 Ihre Aufgabe:")
    print("   Analysieren Sie die Materialfestigkeit verschiedener Chargen")

    # Simulierte Materialfestigkeitsdaten (N/mm²)
    np.random.seed(42)

    # Verschiedene Materialchargen mit unterschiedlichen Eigenschaften
    material_a = np.random.normal(380, 25, 200)  # Normalverteilung
    material_b = np.random.gamma(2, 90) + 200  # Rechtsschief
    material_c = np.random.uniform(320, 420, 200)  # Gleichverteilung

    print("   Gegeben: Festigkeitsdaten für drei Materialchargen")
    print(f"   - Material A: {len(material_a)} Proben")
    print(f"   - Material B: {len(material_b)} Proben")
    print(f"   - Material C: {len(material_c)} Proben")

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))

    materialien = [material_a, material_b, material_c]
    namen = ["Material A (Normal)", "Material B (Gamma)", "Material C (Uniform)"]
    farben = ["skyblue", "lightgreen", "salmon"]

    # Einzelhistogramme
    for i, (data, name, farbe) in enumerate(
        zip(materialien, namen, farben, strict=False)
    ):
        if i < 3:  # Erste drei Subplots
            ax = axes[0, i] if i < 2 else axes[1, 0]

            # Histogramm
            n, bins, patches = ax.hist(
                data, bins=25, alpha=0.7, color=farbe, edgecolor="black", density=True
            )

            # Normalverteilungskurve überlagern
            mu, sigma = np.mean(data), np.std(data)
            x = np.linspace(data.min(), data.max(), 100)
            normal_curve = stats.norm.pdf(x, mu, sigma)
            ax.plot(x, normal_curve, "r-", linewidth=2, label="Normalverteilung")

            # Statistische Kennwerte
            ax.axvline(mu, color="red", linestyle="--", linewidth=2, alpha=0.8)
            ax.axvline(mu + sigma, color="orange", linestyle=":", alpha=0.8)
            ax.axvline(mu - sigma, color="orange", linestyle=":", alpha=0.8)

            # Normalitätstest
            shapiro_stat, shapiro_p = stats.shapiro(data)
            normalitaet = "Normal" if shapiro_p > 0.05 else "Nicht normal"

            ax.set_title(
                f"{name}\\nμ={mu:.1f}, σ={sigma:.1f}\\n{normalitaet} (p={shapiro_p:.3f})"
            )
            ax.set_xlabel("Festigkeit (N/mm²)")
            ax.set_ylabel("Dichte")
            ax.legend()
            ax.grid(True, alpha=0.3)

    # Vergleichs-Plot (alle Materialien)
    ax_vergleich = axes[1, 1]

    # Alle Histogramme überlagert
    ax_vergleich.hist(
        [material_a, material_b, material_c],
        bins=20,
        alpha=0.6,
        label=namen,
        color=farben,
        edgecolor="black",
    )
    ax_vergleich.set_title("Vergleich aller Materialien")
    ax_vergleich.set_xlabel("Festigkeit (N/mm²)")
    ax_vergleich.set_ylabel("Häufigkeit")
    ax_vergleich.legend()
    ax_vergleich.grid(True, alpha=0.3)

    plt.suptitle(
        "Materialfestigkeit - Statistische Analyse", fontsize=16, fontweight="bold"
    )
    plt.tight_layout()
    plt.show()

    # Statistische Auswertung
    print("\\n📈 Statistische Auswertung:")
    for name, data in zip(namen, materialien, strict=False):
        mean_val = np.mean(data)
        std_val = np.std(data)
        shapiro_stat, shapiro_p = stats.shapiro(data)

        print(f"   {name}:")
        print(f"     Mittelwert: {mean_val:.2f} N/mm²")
        print(f"     Standardabw.: {std_val:.2f} N/mm²")
        print(
            f"     Normalitätstest: {'✓' if shapiro_p > 0.05 else '✗'} (p={shapiro_p:.3f})"
        )
    # ============================================

    print("✅ Aufgabe 1 abgeschlossen!")
    print("   💡 Tipp: stats.shapiro() testet auf Normalverteilung (p > 0.05 = normal)")


def aufgabe_2_boxplot_vergleiche() -> None:
    """
    Aufgabe 2: Box-Plot Vergleiche für Gruppendaten

    TODO für Teilnehmer:
    1. Erstellen Sie Box-Plots für Produktionsleistung verschiedener Schichten
    2. Identifizieren Sie Ausreißer
    3. Vergleichen Sie Median, Quartile und Variabilität
    4. Führen Sie einen statistischen Test auf Gruppenunterschiede durch
    5. Interpretieren Sie die Ergebnisse
    """
    print("🔨 Ihre Aufgabe:")
    print("   Vergleichen Sie die Produktionsleistung verschiedener Schichten")

    # Simulierte Schichtdaten
    np.random.seed(42)

    # Verschiedene Schichten mit charakteristischen Leistungsmustern
    fruehschicht = np.random.normal(1200, 150, 50)  # Stabile Leistung
    spaetschicht = np.random.normal(1100, 200, 50)  # Etwas variabler
    nachtschicht = np.random.normal(950, 180, 50)  # Geringere Leistung

    # Einige Ausreißer hinzufügen
    fruehschicht = np.concatenate([fruehschicht, [1800, 1850]])  # Sehr gute Tage
    spaetschicht = np.concatenate([spaetschicht, [500, 600]])  # Probleme
    nachtschicht = np.concatenate([nachtschicht, [1400]])  # Ausnahmeleistung

    schichtdaten = [fruehschicht, spaetschicht, nachtschicht]
    schichtnamen = ["Frühschicht", "Spätschicht", "Nachtschicht"]

    print(
        f"   Datensätze: {[len(data) for data in schichtdaten]} Messwerte pro Schicht"
    )

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Standard Box-Plot
    ax1.boxplot(
        schichtdaten,
        labels=schichtnamen,
        patch_artist=True,
        boxprops={"facecolor": "lightblue", "alpha": 0.7},
        medianprops={"color": "red", "linewidth": 2},
    )

    ax1.set_title("Produktionsleistung nach Schichten", fontweight="bold")
    ax1.set_ylabel("Stück pro Schicht")
    ax1.grid(True, alpha=0.3)

    # Mediane hervorheben
    mediane = [np.median(data) for data in schichtdaten]
    for i, median in enumerate(mediane):
        ax1.text(
            i + 1,
            median + 50,
            f"{median:.0f}",
            ha="center",
            fontweight="bold",
            bbox={"boxstyle": "round,pad=0.3", "facecolor": "yellow"},
        )

    # 2. Violin Plot (zeigt Verteilungsform)
    parts = ax2.violinplot(
        schichtdaten,
        positions=range(1, len(schichtdaten) + 1),
        showmeans=True,
        showmedians=True,
    )

    # Farben anpassen
    colors = ["lightcoral", "lightgreen", "lightskyblue"]
    for pc, color in zip(parts["bodies"], colors, strict=False):
        pc.set_facecolor(color)
        pc.set_alpha(0.7)

    ax2.set_title("Verteilungsformen (Violin Plot)", fontweight="bold")
    ax2.set_ylabel("Stück pro Schicht")
    ax2.set_xticks(range(1, len(schichtdaten) + 1))
    ax2.set_xticklabels(schichtnamen)
    ax2.grid(True, alpha=0.3)

    # 3. Ausreißer-Analyse
    ax3.boxplot(schichtdaten, labels=schichtnamen, patch_artist=True)

    # Ausreißer identifizieren und markieren
    for i, data in enumerate(schichtdaten):
        Q1, Q3 = np.percentile(data, [25, 75])
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        ausreisser = data[(data < lower_bound) | (data > upper_bound)]
        print(f"\\n   {schichtnamen[i]} Ausreißer: {len(ausreisser)} Werte")
        for ausreisser_wert in ausreisser:
            print(f"     - {ausreisser_wert:.0f} Stück")
            # Ausreißer extra markieren
            ax3.scatter(
                i + 1, ausreisser_wert, color="red", s=50, marker="x", linewidth=2
            )

    ax3.set_title("Ausreißer-Identifikation", fontweight="bold")
    ax3.set_ylabel("Stück pro Schicht")
    ax3.grid(True, alpha=0.3)

    # 4. Statistische Tests
    # ANOVA-Test für Gruppenunterschiede
    from scipy.stats import f_oneway, kruskal

    f_stat, anova_p = f_oneway(*schichtdaten)
    h_stat, kruskal_p = kruskal(*schichtdaten)

    # Paarweise t-Tests
    from scipy.stats import ttest_ind

    test_ergebnisse = []
    vergleiche = [
        ("Früh vs Spät", 0, 1),
        ("Früh vs Nacht", 0, 2),
        ("Spät vs Nacht", 1, 2),
    ]

    for name, idx1, idx2 in vergleiche:
        t_stat, t_p = ttest_ind(schichtdaten[idx1], schichtdaten[idx2])
        test_ergebnisse.append((name, t_p))

    # Ergebnisse visualisieren
    ax4.text(
        0.1,
        0.9,
        "Statistische Tests:",
        fontsize=14,
        fontweight="bold",
        transform=ax4.transAxes,
    )

    y_pos = 0.75
    ax4.text(
        0.1,
        y_pos,
        f"ANOVA: F={f_stat:.2f}, p={anova_p:.4f}",
        transform=ax4.transAxes,
        fontsize=12,
    )

    y_pos -= 0.1
    signifikanz = "Signifikant ✓" if anova_p < 0.05 else "Nicht signifikant ✗"
    ax4.text(
        0.1,
        y_pos,
        f"Gruppenunterschied: {signifikanz}",
        transform=ax4.transAxes,
        fontsize=12,
        color="green" if anova_p < 0.05 else "red",
    )

    y_pos -= 0.15
    ax4.text(
        0.1,
        y_pos,
        "Paarweise Vergleiche:",
        fontsize=12,
        fontweight="bold",
        transform=ax4.transAxes,
    )

    for name, p_val in test_ergebnisse:
        y_pos -= 0.1
        signif = "✓" if p_val < 0.05 else "✗"
        ax4.text(
            0.1,
            y_pos,
            f"{name}: p={p_val:.4f} {signif}",
            transform=ax4.transAxes,
            fontsize=10,
        )

    # Quartile anzeigen
    y_pos -= 0.15
    ax4.text(
        0.1,
        y_pos,
        "Quartile (Q1, Median, Q3):",
        fontsize=12,
        fontweight="bold",
        transform=ax4.transAxes,
    )

    for _i, (name, data) in enumerate(zip(schichtnamen, schichtdaten, strict=False)):
        Q1, median, Q3 = np.percentile(data, [25, 50, 75])
        y_pos -= 0.08
        ax4.text(
            0.1,
            y_pos,
            f"{name}: {Q1:.0f}, {median:.0f}, {Q3:.0f}",
            transform=ax4.transAxes,
            fontsize=10,
        )

    ax4.set_xlim(0, 1)
    ax4.set_ylim(0, 1)
    ax4.axis("off")
    ax4.set_title("Statistische Auswertung", fontweight="bold")

    plt.suptitle(
        "Schichtvergleich - Statistische Analyse", fontsize=16, fontweight="bold"
    )
    plt.tight_layout()
    plt.show()
    # ============================================

    print("\\n✅ Aufgabe 2 abgeschlossen!")
    print(
        f"   📊 ANOVA-Test: {'Signifikante' if anova_p < 0.05 else 'Keine'} Gruppenunterschiede"
    )
    print("   💡 Tipp: Box-Plots zeigen Median, Quartile und Ausreißer auf einen Blick")


def aufgabe_3_korrelationsmatrix() -> None:
    """
    Aufgabe 3: Korrelationsmatrix-Analyse

    TODO für Teilnehmer:
    1. Erstellen Sie einen DataFrame mit mehreren Prozessvariablen
    2. Berechnen Sie die Korrelationsmatrix
    3. Visualisieren Sie diese als Heatmap
    4. Identifizieren Sie starke Korrelationen
    5. Interpretieren Sie die praktischen Implikationen
    """
    print("🔨 Ihre Aufgabe:")
    print("   Analysieren Sie Zusammenhänge zwischen Prozessparametern")

    # Simulierte Prozessdaten
    np.random.seed(42)
    n_samples = 300

    # Basis-Parameter
    temperatur = np.random.normal(80, 10, n_samples)

    # Abhängige Parameter (mit realistischen Korrelationen)
    druck = 50 + 0.3 * temperatur + np.random.normal(0, 5, n_samples)
    geschwindigkeit = 120 - 0.2 * temperatur + np.random.normal(0, 15, n_samples)
    qualitaet = (
        95
        - 0.1 * (temperatur - 80) ** 2
        - 0.05 * (druck - 65) ** 2
        + np.random.normal(0, 3, n_samples)
    )
    energie = 100 + 0.4 * temperatur + 0.2 * druck + np.random.normal(0, 8, n_samples)
    verschleiss = (
        0.5
        + 0.02 * temperatur
        + 0.01 * geschwindigkeit
        + np.random.normal(0, 0.3, n_samples)
    )
    ausfallzeit = np.maximum(
        0, 2 - 0.05 * qualitaet + 2 * verschleiss + np.random.normal(0, 1, n_samples)
    )

    # DataFrame erstellen
    prozess_data = pd.DataFrame(
        {
            "Temperatur_°C": temperatur,
            "Druck_bar": druck,
            "Geschwindigkeit_mm/min": geschwindigkeit,
            "Qualität_%": qualitaet,
            "Energieverbrauch_kW": energie,
            "Werkzeugverschleiß_mm": verschleiss,
            "Ausfallzeit_h": ausfallzeit,
        }
    )

    print(f"   Dataset: {n_samples} Messungen, {len(prozess_data.columns)} Parameter")
    print(f"   Parameter: {', '.join(prozess_data.columns)}")

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    plt.figure(figsize=(16, 12))

    # 1. Korrelationsmatrix berechnen
    korrelation = prozess_data.corr()

    # 2. Heatmap erstellen (Hauptplot)
    ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=2, rowspan=2)

    # Maske für obere Dreieck (symmetrische Matrix)
    mask = np.triu(np.ones_like(korrelation, dtype=bool))

    # Heatmap mit Seaborn
    sns.heatmap(
        korrelation,
        annot=True,
        cmap="RdBu_r",
        center=0,
        square=True,
        fmt=".2f",
        cbar_kws={"shrink": 0.8},
        mask=mask,
        ax=ax1,
        linewidths=0.5,
    )

    ax1.set_title(
        "Korrelationsmatrix - Prozessparameter", fontsize=14, fontweight="bold"
    )

    # 3. Stärkste Korrelationen identifizieren
    ax2 = plt.subplot2grid((2, 3), (0, 2))

    # Korrelationen extrahieren (ohne Diagonale)
    korr_values = []
    korr_pairs = []

    for i in range(len(korrelation.columns)):
        for j in range(i + 1, len(korrelation.columns)):
            korr_val = korrelation.iloc[i, j]
            korr_values.append(abs(korr_val))
            korr_pairs.append(
                (korrelation.columns[i], korrelation.columns[j], korr_val)
            )

    # Top 5 stärkste Korrelationen
    sorted_korr = sorted(zip(korr_values, korr_pairs, strict=False), reverse=True)
    top_5 = sorted_korr[:5]

    # Balkendiagramm der stärksten Korrelationen
    top_names = [
        f"{pair[0].split('_')[0]}\\nvs\\n{pair[1].split('_')[0]}" for _, pair in top_5
    ]
    top_values = [abs(pair[2]) for _, pair in top_5]
    colors_corr = ["darkred" if pair[2] < 0 else "darkblue" for _, pair in top_5]

    bars = ax2.barh(range(len(top_names)), top_values, color=colors_corr, alpha=0.7)
    ax2.set_yticks(range(len(top_names)))
    ax2.set_yticklabels(top_names, fontsize=8)
    ax2.set_xlabel("|Korrelation|")
    ax2.set_title("Top 5\\nKorrelationen", fontsize=12, fontweight="bold")
    ax2.grid(True, alpha=0.3, axis="x")

    # Werte auf Balken
    for _i, (bar, (_, pair)) in enumerate(zip(bars, top_5, strict=False)):
        ax2.text(
            bar.get_width() + 0.02,
            bar.get_y() + bar.get_height() / 2,
            f"{pair[2]:.2f}",
            va="center",
            fontsize=9,
            fontweight="bold",
        )

    # 4. Scatter Plot Matrix (Auswahl wichtiger Parameter)
    wichtige_parameter = [
        "Temperatur_°C",
        "Qualität_%",
        "Energieverbrauch_kW",
        "Ausfallzeit_h",
    ]
    prozess_data[wichtige_parameter]

    ax3 = plt.subplot2grid((2, 3), (1, 2))

    # Pairplot-ähnliche Visualisierung (vereinfacht)
    # Zeige nur ein beispielhaft wichtiges Scatter Plot
    param1, param2 = "Temperatur_°C", "Qualität_%"

    scatter = ax3.scatter(
        prozess_data[param1],
        prozess_data[param2],
        c=prozess_data["Ausfallzeit_h"],
        cmap="Reds",
        alpha=0.6,
        s=30,
        edgecolors="black",
        linewidth=0.5,
    )

    # Trendlinie
    z = np.polyfit(prozess_data[param1], prozess_data[param2], 1)
    p = np.poly1d(z)
    x_trend = np.linspace(prozess_data[param1].min(), prozess_data[param1].max(), 50)
    ax3.plot(x_trend, p(x_trend), "r--", linewidth=2, alpha=0.8)

    # Korrelationskoeffizient anzeigen
    korr_val = korrelation.loc[param1, param2]
    ax3.text(
        0.05,
        0.95,
        f"r = {korr_val:.3f}",
        transform=ax3.transAxes,
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "yellow"},
        fontsize=12,
        fontweight="bold",
    )

    ax3.set_xlabel(param1)
    ax3.set_ylabel(param2)
    ax3.set_title(
        "Temperatur vs Qualität\\n(Farbe = Ausfallzeit)", fontsize=10, fontweight="bold"
    )
    ax3.grid(True, alpha=0.3)

    # Colorbar für Ausfallzeit
    plt.colorbar(scatter, ax=ax3, label="Ausfallzeit (h)", shrink=0.8)

    plt.suptitle(
        "Prozessparameter - Korrelationsanalyse", fontsize=16, fontweight="bold"
    )
    plt.tight_layout()
    plt.show()

    # Statistische Interpretation
    print("\\n📈 Korrelationsanalyse:")
    print("   Stärkste Zusammenhänge:")
    for i, (_, pair) in enumerate(top_5):
        korr_val = pair[2]
        param1_short = pair[0].split("_")[0]
        param2_short = pair[1].split("_")[0]

        if abs(korr_val) > 0.7:
            staerke = "Stark"
        elif abs(korr_val) > 0.3:
            staerke = "Moderat"
        else:
            staerke = "Schwach"

        richtung = "negativ" if korr_val < 0 else "positiv"
        print(
            f"   {i + 1}. {param1_short} ↔ {param2_short}: {korr_val:.3f} ({staerke} {richtung})"
        )

    # Praktische Implikationen
    print("\\n💡 Praktische Implikationen:")
    if korrelation.loc["Temperatur_°C", "Qualität_%"] < -0.3:
        print("   - Höhere Temperaturen reduzieren die Qualität → Kühlung optimieren")
    if korrelation.loc["Energieverbrauch_kW", "Temperatur_°C"] > 0.3:
        print("   - Energieverbrauch steigt mit Temperatur → Effizienz verbessern")
    if korrelation.loc["Werkzeugverschleiß_mm", "Ausfallzeit_h"] > 0.3:
        print("   - Werkzeugverschleiß führt zu Ausfällen → Präventive Wartung")
    # ============================================

    print("\\n✅ Aufgabe 3 abgeschlossen!")
    print("   💡 Tipp: |r| > 0.7 = stark, 0.3-0.7 = moderat, < 0.3 = schwach")


def aufgabe_4_seaborn_pairplot() -> None:
    """
    Aufgabe 4: Seaborn Pairplot für multivariate Analyse

    TODO für Teilnehmer:
    1. Erstellen Sie einen Pairplot mit Seaborn
    2. Gruppieren Sie nach Kategorien (z.B. Schichten)
    3. Anpassung der Diagonal-Plots (Histogramme vs KDE)
    4. Interpretation der Verteilungsunterschiede
    5. Identifizierung von Clustern oder Mustern
    """
    print("🔨 Ihre Aufgabe:")
    print("   Erstellen Sie einen Pairplot zur multivariaten Datenanalyse")

    # Erweiterte Datensimulation
    np.random.seed(42)
    n_per_group = 100

    # Drei verschiedene Betriebsmodi
    daten_liste = []

    for _i, (modus, temp_base, speed_base, qual_base) in enumerate(
        [
            ("Normalbetrieb", 75, 100, 95),
            ("Hochleistung", 85, 120, 92),
            ("Sparbetrieb", 65, 80, 97),
        ]
    ):
        # Parameter mit Modi-spezifischen Charakteristika
        temperatur = np.random.normal(temp_base, 8, n_per_group)
        geschwindigkeit = np.random.normal(speed_base, 12, n_per_group) + 0.2 * (
            temperatur - temp_base
        )
        qualitaet = np.random.normal(qual_base, 3, n_per_group) - 0.1 * abs(
            temperatur - temp_base
        )
        energie = (
            50
            + 0.5 * geschwindigkeit
            + 0.3 * temperatur
            + np.random.normal(0, 5, n_per_group)
        )

        # DataFrame für diese Gruppe
        gruppe_df = pd.DataFrame(
            {
                "Temperatur": temperatur,
                "Geschwindigkeit": geschwindigkeit,
                "Qualität": qualitaet,
                "Energie": energie,
                "Modus": modus,
            }
        )

        daten_liste.append(gruppe_df)

    # Kombinierter DataFrame
    combined_df = pd.concat(daten_liste, ignore_index=True)

    print(
        f"   Dataset: {len(combined_df)} Datenpunkte, {len(combined_df['Modus'].unique())} Modi"
    )
    print(f"   Modi: {', '.join(combined_df['Modus'].unique())}")

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    # Seaborn Stil setzen
    sns.set_palette("husl")

    plt.figure(figsize=(16, 12))

    # 1. Hauptpairplot
    ax_main = plt.subplot2grid((2, 2), (0, 0), colspan=2, rowspan=2)
    plt.sca(ax_main)  # Setze aktuellen Achsenbereich

    # Pairplot erstellen
    numerische_spalten = ["Temperatur", "Geschwindigkeit", "Qualität", "Energie"]

    pairplot = sns.pairplot(
        data=combined_df,
        vars=numerische_spalten,
        hue="Modus",
        diag_kind="kde",
        plot_kws={"alpha": 0.7, "s": 30},
        diag_kws={"alpha": 0.7},
    )

    # Anpassungen für bessere Lesbarkeit
    pairplot.fig.suptitle(
        "Multivariate Analyse - Betriebsmodi Vergleich",
        fontsize=16,
        fontweight="bold",
        y=1.02,
    )

    # Zeige den Pairplot
    plt.show()

    # Zusätzliche Detailanalyse
    fig2, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Verteilungsvergleich für einen Parameter
    for modus in combined_df["Modus"].unique():
        data = combined_df[combined_df["Modus"] == modus]["Qualität"]
        ax1.hist(data, alpha=0.6, label=modus, bins=20, density=True)
        ax1.axvline(
            np.mean(data),
            linestyle="--",
            alpha=0.8,
            label=f"{modus} Mittelwert: {np.mean(data):.1f}",
        )

    ax1.set_title("Qualitätsverteilung nach Betriebsmodus", fontweight="bold")
    ax1.set_xlabel("Qualität (%)")
    ax1.set_ylabel("Dichte")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # 2. Box Plot Vergleich
    sns.boxplot(data=combined_df, x="Modus", y="Energie", ax=ax2)
    ax2.set_title("Energieverbrauch nach Betriebsmodus", fontweight="bold")
    ax2.tick_params(axis="x", rotation=45)
    ax2.grid(True, alpha=0.3)

    # 3. Scatter mit Regression Lines
    sns.scatterplot(data=combined_df, x="Temperatur", y="Qualität", hue="Modus", ax=ax3)

    # Regressionsgerade für jeden Modus
    for modus in combined_df["Modus"].unique():
        subset = combined_df[combined_df["Modus"] == modus]
        sns.regplot(
            data=subset,
            x="Temperatur",
            y="Qualität",
            ax=ax3,
            scatter=False,
            label=f"{modus} Trend",
        )

    ax3.set_title("Temperatur vs Qualität (mit Trends)", fontweight="bold")
    ax3.grid(True, alpha=0.3)

    # 4. Korrelationsmatrizen nach Gruppen
    korrelationen = {}
    for modus in combined_df["Modus"].unique():
        subset = combined_df[combined_df["Modus"] == modus][numerische_spalten]
        korrelationen[modus] = subset.corr()

    # Durchschnittliche Korrelation visualisieren
    avg_korr = sum(korrelationen.values()) / len(korrelationen)
    mask = np.triu(np.ones_like(avg_korr, dtype=bool))

    sns.heatmap(
        avg_korr,
        annot=True,
        cmap="RdBu_r",
        center=0,
        ax=ax4,
        mask=mask,
        square=True,
        fmt=".2f",
        cbar_kws={"shrink": 0.8},
    )
    ax4.set_title("Durchschnittliche Korrelationen", fontweight="bold")

    plt.suptitle(
        "Detailanalyse - Betriebsmodi Charakteristika", fontsize=16, fontweight="bold"
    )
    plt.tight_layout()
    plt.show()

    # Statistische Auswertung nach Gruppen
    print("\\n📊 Gruppenvergleich:")
    for spalte in numerische_spalten:
        print(f"\\n   {spalte}:")
        for modus in combined_df["Modus"].unique():
            data = combined_df[combined_df["Modus"] == modus][spalte]
            print(f"     {modus}: μ={np.mean(data):.1f}, σ={np.std(data):.1f}")

        # ANOVA Test
        gruppen = [
            combined_df[combined_df["Modus"] == modus][spalte]
            for modus in combined_df["Modus"].unique()
        ]
        f_stat, p_val = stats.f_oneway(*gruppen)
        signifikanz = "✓" if p_val < 0.05 else "✗"
        print(f"     ANOVA: F={f_stat:.2f}, p={p_val:.4f} {signifikanz}")
    # ============================================

    print("\\n✅ Aufgabe 4 abgeschlossen!")
    print("   💡 Tipp: Pairplots zeigen alle Variablen-Paare gleichzeitig")


def aufgabe_5_statistische_qualitaetskontrolle() -> None:
    """
    Aufgabe 5: Statistische Prozesskontrolle (SPC)

    TODO für Teilnehmer:
    1. Erstellen Sie Regelkarten (Control Charts)
    2. Berechnen Sie Kontrollgrenzen (UCL, LCL)
    3. Identifizieren Sie "Out of Control" Punkte
    4. Analysieren Sie Trends und Patterns
    5. Bewerten Sie die Prozessfähigkeit (Cp, Cpk)
    """
    print("🔨 Ihre Aufgabe:")
    print("   Implementieren Sie statistische Prozesskontrolle (SPC)")

    # Simulierte Produktionsdaten mit verschiedenen Störungen
    np.random.seed(42)

    # Sollwert und Spezifikationen
    target = 50.0  # mm
    usl = 52.0  # Upper Specification Limit
    lsl = 48.0  # Lower Specification Limit

    # Produktionsdaten mit eingebauten Problemen
    n_samples = 200
    measurements = []
    sample_groups = []

    for i in range(n_samples):
        if i < 50:  # Normaler Betrieb
            value = np.random.normal(target, 0.5)
        elif i < 80:  # Systematische Verschiebung
            value = np.random.normal(target + 1, 0.5)
        elif i < 120:  # Erhöhte Variabilität
            value = np.random.normal(target, 1.2)
        elif i < 150:  # Trend
            trend_offset = (i - 120) * 0.03
            value = np.random.normal(target + trend_offset, 0.5)
        else:  # Zurück zur Normalität
            value = np.random.normal(target, 0.5)

        measurements.append(value)
        sample_groups.append(i // 5 + 1)  # Gruppen von je 5 Messungen

    measurements = np.array(measurements)

    print(f"   Dataset: {n_samples} Messungen, Target: {target} mm")
    print(f"   Spezifikationen: LSL={lsl}, USL={usl}")

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    plt.figure(figsize=(16, 12))

    # 1. X-Chart (Individual Values)
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)

    # Kontrollgrenzen berechnen (erste 50 Werte als Referenz)
    reference_data = measurements[:50]
    mean_ref = np.mean(reference_data)
    std_ref = np.std(reference_data)

    ucl = mean_ref + 3 * std_ref
    lcl = mean_ref - 3 * std_ref

    # Plot erstellen
    ax1.plot(
        range(1, len(measurements) + 1), measurements, "b-", linewidth=1, alpha=0.7
    )
    ax1.scatter(
        range(1, len(measurements) + 1), measurements, c="blue", s=20, alpha=0.6
    )

    # Kontrollgrenzen
    ax1.axhline(
        y=mean_ref, color="green", linestyle="-", linewidth=2, label="Mittelwert"
    )
    ax1.axhline(y=ucl, color="red", linestyle="--", linewidth=2, label="UCL")
    ax1.axhline(y=lcl, color="red", linestyle="--", linewidth=2, label="LCL")

    # Spezifikationsgrenzen
    ax1.axhline(y=usl, color="orange", linestyle=":", linewidth=2, label="USL")
    ax1.axhline(y=lsl, color="orange", linestyle=":", linewidth=2, label="LSL")

    # Out-of-control Punkte markieren
    out_of_control = np.where((measurements > ucl) | (measurements < lcl))[0]
    ax1.scatter(
        out_of_control + 1,
        measurements[out_of_control],
        c="red",
        s=60,
        marker="x",
        linewidth=3,
        label="Ausreißer",
    )

    # Problembereiche hervorheben
    ax1.axvspan(50, 80, alpha=0.2, color="yellow", label="Verschiebung")
    ax1.axvspan(80, 120, alpha=0.2, color="orange", label="Variabilität")
    ax1.axvspan(120, 150, alpha=0.2, color="red", label="Trend")

    ax1.set_title("X-Chart - Einzelwerte mit Kontrollgrenzen", fontweight="bold")
    ax1.set_xlabel("Probe Nr.")
    ax1.set_ylabel("Messwert (mm)")
    ax1.legend(bbox_to_anchor=(1.05, 1), loc="upper left")
    ax1.grid(True, alpha=0.3)

    # 2. Moving Range Chart
    ax2 = plt.subplot2grid((3, 3), (0, 2))

    moving_ranges = np.abs(np.diff(measurements))
    mr_mean = np.mean(moving_ranges[:49])  # Referenzdaten
    mr_ucl = mr_mean * 3.267  # Faktor für Moving Range

    ax2.plot(
        range(2, len(measurements) + 1), moving_ranges, "g-", linewidth=1, alpha=0.7
    )
    ax2.scatter(
        range(2, len(measurements) + 1), moving_ranges, c="green", s=20, alpha=0.6
    )

    ax2.axhline(y=mr_mean, color="blue", linestyle="-", linewidth=2, label="MR̄")
    ax2.axhline(y=mr_ucl, color="red", linestyle="--", linewidth=2, label="UCL")

    ax2.set_title("Moving Range Chart", fontweight="bold")
    ax2.set_xlabel("Probe Nr.")
    ax2.set_ylabel("Moving Range")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # 3. Histogramm mit Normalverteilung
    ax3 = plt.subplot2grid((3, 3), (1, 0))

    ax3.hist(
        measurements,
        bins=30,
        alpha=0.7,
        color="skyblue",
        density=True,
        edgecolor="black",
    )

    # Normalverteilungskurve
    x_norm = np.linspace(measurements.min(), measurements.max(), 100)
    mean_all = np.mean(measurements)
    std_all = np.std(measurements)
    y_norm = stats.norm.pdf(x_norm, mean_all, std_all)
    ax3.plot(x_norm, y_norm, "red", linewidth=2, label="Normalverteilung")

    # Grenzen markieren
    ax3.axvline(x=usl, color="orange", linestyle=":", linewidth=2)
    ax3.axvline(x=lsl, color="orange", linestyle=":", linewidth=2)
    ax3.axvline(x=target, color="green", linestyle="-", linewidth=2)

    ax3.set_title("Verteilungsanalyse", fontweight="bold")
    ax3.set_xlabel("Messwert (mm)")
    ax3.set_ylabel("Dichte")
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. Prozessfähigkeit
    ax4 = plt.subplot2grid((3, 3), (1, 1))

    # Cp und Cpk berechnen
    cp = (usl - lsl) / (6 * std_all)
    cpu = (usl - mean_all) / (3 * std_all)
    cpl = (mean_all - lsl) / (3 * std_all)
    cpk = min(cpu, cpl)

    # Prozentuale Ausschuss
    percent_above_usl = np.sum(measurements > usl) / len(measurements) * 100
    percent_below_lsl = np.sum(measurements < lsl) / len(measurements) * 100

    # Cpk Bewertung
    cpk_categories = [
        "Ungenügend\\n<1.0",
        "Akzeptabel\\n1.0-1.33",
        "Gut\\n1.33-1.67",
        "Exzellent\\n>1.67",
    ]
    cpk_values = [1.0, 1.33, 1.67, 2.0]
    cpk_colors = ["red", "orange", "yellow", "green"]

    ax4.bar(cpk_categories, cpk_values, color=cpk_colors, alpha=0.7)
    ax4.axhline(
        y=cpk,
        color="blue",
        linestyle="-",
        linewidth=3,
        label=f"Aktueller Cpk = {cpk:.2f}",
    )

    ax4.set_title("Prozessfähigkeit\\n(Cpk)", fontweight="bold")
    ax4.set_ylabel("Cpk-Wert")
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # 5. Regelkarten-Regeln (Western Electric Rules)
    ax5 = plt.subplot2grid((3, 3), (1, 2))

    # Regel-Verletzungen identifizieren
    regel_verletzungen = {
        "Regel 1 (außerhalb 3σ)": len(out_of_control),
        "Regel 2 (2/3 außerhalb 2σ)": 0,  # Vereinfacht
        "Regel 3 (4/5 außerhalb 1σ)": 0,  # Vereinfacht
        "Regel 4 (8 aufeinander folgende auf einer Seite)": 0,  # Vereinfacht
    }

    # Vereinfachte Implementierung für Regel 4 (8 aufeinander folgende Punkte)
    consecutive_above = 0
    consecutive_below = 0
    max_consecutive = 0

    for val in measurements:
        if val > mean_ref:
            consecutive_above += 1
            consecutive_below = 0
        else:
            consecutive_below += 1
            consecutive_above = 0

        max_consecutive = max(max_consecutive, consecutive_above, consecutive_below)

    regel_verletzungen["Regel 4 (8 aufeinander folgende auf einer Seite)"] = (
        max_consecutive >= 8
    )

    # Regel-Status visualisieren
    regel_namen = list(regel_verletzungen.keys())
    regel_status = [
        "✓" if not verletzung else "✗" for verletzung in regel_verletzungen.values()
    ]
    farben_regeln = ["green" if status == "✓" else "red" for status in regel_status]

    y_pos = np.arange(len(regel_namen))
    ax5.barh(y_pos, [1] * len(regel_namen), color=farben_regeln, alpha=0.7)

    # Status-Text hinzufügen
    for i, (status, verletzung) in enumerate(
        zip(regel_status, regel_verletzungen.values(), strict=False)
    ):
        text = (
            f"{status} ({verletzung})"
            if isinstance(verletzung, int | float)
            else status
        )
        ax5.text(
            0.5, i, text, ha="center", va="center", fontweight="bold", color="white"
        )

    ax5.set_yticks(y_pos)
    ax5.set_yticklabels([name.split(" (")[0] for name in regel_namen], fontsize=8)
    ax5.set_xlim(0, 1)
    ax5.set_title("Regelkarten-Regeln\\n(Western Electric)", fontweight="bold")
    ax5.set_xticks([])

    # 6. Zeitreihen-Trend-Analyse
    ax6 = plt.subplot2grid((3, 3), (2, 0), colspan=3)

    # Gleitender Durchschnitt
    window_size = 10
    rolling_mean = pd.Series(measurements).rolling(window=window_size).mean()
    rolling_std = pd.Series(measurements).rolling(window=window_size).std()

    ax6.plot(
        range(1, len(measurements) + 1), measurements, "b-", alpha=0.3, label="Rohdaten"
    )
    ax6.plot(
        range(1, len(measurements) + 1),
        rolling_mean,
        "r-",
        linewidth=2,
        label=f"Gleitender Mittelwert ({window_size})",
    )
    ax6.fill_between(
        range(1, len(measurements) + 1),
        rolling_mean - 2 * rolling_std,
        rolling_mean + 2 * rolling_std,
        alpha=0.2,
        color="red",
        label="±2σ Bereich",
    )

    ax6.axhline(y=target, color="green", linestyle="-", linewidth=2, label="Sollwert")

    # Phasen markieren
    ax6.text(
        25,
        52.5,
        "Normal",
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "lightgreen"},
    )
    ax6.text(
        65,
        52.5,
        "Verschiebung",
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "yellow"},
    )
    ax6.text(
        100,
        52.5,
        "Variabilität",
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "orange"},
    )
    ax6.text(135, 52.5, "Trend", bbox={"boxstyle": "round,pad=0.3", "facecolor": "red"})
    ax6.text(
        175,
        52.5,
        "Korrigiert",
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "lightgreen"},
    )

    ax6.set_title("Trend-Analyse mit gleitendem Durchschnitt", fontweight="bold")
    ax6.set_xlabel("Probe Nr.")
    ax6.set_ylabel("Messwert (mm)")
    ax6.legend()
    ax6.grid(True, alpha=0.3)

    plt.suptitle(
        "Statistische Prozesskontrolle (SPC) - Vollständige Analyse",
        fontsize=16,
        fontweight="bold",
    )
    plt.tight_layout()
    plt.show()

    # Umfassende Auswertung
    print("\\n📊 SPC-Auswertung:")
    print("   Prozess-Statistiken:")
    print(f"     Mittelwert: {mean_all:.3f} mm (Sollwert: {target:.3f} mm)")
    print(f"     Standardabweichung: {std_all:.3f} mm")
    print(f"     Spannweite: {np.max(measurements) - np.min(measurements):.3f} mm")

    print("\\n   Prozessfähigkeit:")
    print(f"     Cp (Prozessfähigkeit): {cp:.3f}")
    print(f"     Cpk (Prozessleistung): {cpk:.3f}")

    if cpk >= 1.67:
        bewertung = "Exzellent 🟢"
    elif cpk >= 1.33:
        bewertung = "Gut 🟡"
    elif cpk >= 1.0:
        bewertung = "Akzeptabel 🟠"
    else:
        bewertung = "Verbesserung erforderlich 🔴"

    print(f"     Bewertung: {bewertung}")

    print("\\n   Ausschuss:")
    print(f"     Oberhalb USL: {percent_above_usl:.2f}%")
    print(f"     Unterhalb LSL: {percent_below_lsl:.2f}%")
    print(f"     Gesamt-Ausschuss: {percent_above_usl + percent_below_lsl:.2f}%")

    print("\\n   Kontrollgrenzen-Verletzungen:")
    print(f"     Ausreißer (außerhalb 3σ): {len(out_of_control)}")
    print(f"     Längste Sequenz gleicher Seite: {max_consecutive}")
    # ============================================

    print("\\n✅ Aufgabe 5 abgeschlossen!")
    print("   💡 Tipp: SPC hilft bei der frühzeitigen Erkennung von Prozessstörungen")


if __name__ == "__main__":
    main()
