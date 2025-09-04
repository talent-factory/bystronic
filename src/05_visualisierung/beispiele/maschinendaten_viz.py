#!/usr/bin/env python3
"""
Maschinendaten-Visualisierung - Industrielle Datenanalyse

Dieses Skript demonstriert die Visualisierung von industriellen Maschinendaten
mit verschiedenen Plot-Techniken speziell für Bystronic-Anwendungen.

Autor: Python Grundkurs Bystronic
"""

import warnings
from datetime import datetime, timedelta

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")

# Seaborn-Stil für professionelle Plots
sns.set_style("whitegrid")
plt.rcParams["figure.facecolor"] = "white"


def main() -> None:
    """Hauptfunktion für Maschinendaten-Visualisierung"""
    print("=" * 70)
    print("BYSTRONIC - MASCHINENDATEN VISUALISIERUNG")
    print("=" * 70)

    # 1. Produktionsübersicht Dashboard
    print("\n1️⃣ Produktions-Dashboard")
    print("-" * 40)

    demo_produktions_dashboard()

    # 2. Wartungsplanung und Ausfallzeiten
    print("\n2️⃣ Wartung & Ausfallzeiten")
    print("-" * 40)

    demo_wartungsplanung()

    # 3. Qualitätskontrolle und SPC
    print("\n3️⃣ Qualitätskontrolle (SPC)")
    print("-" * 40)

    demo_qualitaetskontrolle()

    # 4. Energieverbrauch und Nachhaltigkeit
    print("\n4️⃣ Energieanalyse")
    print("-" * 40)

    demo_energieanalyse()

    # 5. OEE-Analyse (Overall Equipment Effectiveness)
    print("\n5️⃣ OEE-Analyse")
    print("-" * 40)

    demo_oee_analyse()

    print(f"\n{'=' * 70}")
    print("✅ Maschinendaten-Visualisierungen erfolgreich erstellt!")
    print("🏭 Industrielle Dashboards für Bystronic-Produktionsumgebung")
    print("📊 KPI-Tracking und Performance-Monitoring")


def demo_produktions_dashboard() -> None:
    """Erstellt ein umfassendes Produktions-Dashboard"""
    # Zeitreihen-Daten generieren
    start_date = datetime.now() - timedelta(days=7)
    timestamps = pd.date_range(start=start_date, end=datetime.now(), freq="H")

    # Verschiedene Maschinen simulieren
    maschinen = {
        "Laser_Station_1": {"base": 120, "variation": 20, "efficiency": 0.92},
        "Laser_Station_2": {"base": 115, "variation": 15, "efficiency": 0.89},
        "Biegemaschine_A": {"base": 80, "variation": 12, "efficiency": 0.87},
        "Stanzautomat_B": {"base": 200, "variation": 30, "efficiency": 0.91},
    }

    # Daten generieren
    np.random.seed(42)
    production_data = {}

    for machine, params in maschinen.items():
        # Basis-Produktionsrate
        base_production = params["base"]
        variation = params["variation"]

        # Tageszyklen simulieren (weniger Produktion nachts)
        hours = np.array([t.hour for t in timestamps])
        day_factor = 0.3 + 0.7 * np.clip(
            np.sin(2 * np.pi * hours / 24 + np.pi / 2), 0, 1
        )

        # Wochenendfaktor (reduzierte Produktion)
        weekend_factor = np.array(
            [0.5 if t.weekday() >= 5 else 1.0 for t in timestamps]
        )

        # Produktionsdaten
        production = base_production * day_factor * weekend_factor + np.random.normal(
            0, variation, len(timestamps)
        )
        production = np.maximum(production, 0)  # Keine negative Produktion

        production_data[machine] = production

    # Dashboard erstellen
    plt.figure(figsize=(16, 12))

    # Hauptplot: Produktionsverlauf über Zeit
    ax1 = plt.subplot2grid((3, 4), (0, 0), colspan=3, rowspan=1)

    colors = plt.cm.Set1(np.linspace(0, 1, len(maschinen)))

    for i, (machine, data) in enumerate(production_data.items()):
        ax1.plot(
            timestamps,
            data,
            label=machine.replace("_", " "),
            color=colors[i],
            linewidth=2,
            alpha=0.8,
        )

    ax1.set_title("Produktionsverlauf - Letzte 7 Tage", fontsize=14, fontweight="bold")
    ax1.set_ylabel("Stück/Stunde")
    ax1.legend(loc="upper right", frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3)

    # Zeitachse formatieren
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m %H:%M"))
    ax1.xaxis.set_major_locator(mdates.DayLocator())
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)

    # KPI-Übersicht (rechts oben)
    ax2 = plt.subplot2grid((3, 4), (0, 3), rowspan=1)

    # Durchschnittliche Produktion pro Maschine
    avg_production = [np.mean(data) for data in production_data.values()]
    machine_names = [name.replace("_", "\n") for name in maschinen.keys()]

    bars = ax2.bar(range(len(machine_names)), avg_production, color=colors, alpha=0.7)
    ax2.set_title("Ø Produktion\n(Stück/h)", fontsize=12, fontweight="bold")
    ax2.set_xticks(range(len(machine_names)))
    ax2.set_xticklabels(machine_names, fontsize=8)

    # Werte auf Balken
    for bar, value in zip(bars, avg_production, strict=False):
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"{value:.0f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    # Heatmap: Stündliche Produktion
    ax3 = plt.subplot2grid((3, 4), (1, 0), colspan=2, rowspan=1)

    # Daten für Heatmap vorbereiten
    hourly_data = np.zeros((len(maschinen), 24))

    for i, (_machine, data) in enumerate(production_data.items()):
        for j, timestamp in enumerate(timestamps):
            hour = timestamp.hour
            hourly_data[i, hour] += data[j]

    # Durchschnitt pro Stunde
    hour_counts = np.zeros(24)
    for timestamp in timestamps:
        hour_counts[timestamp.hour] += 1

    for hour in range(24):
        if hour_counts[hour] > 0:
            hourly_data[:, hour] /= hour_counts[hour]

    im = ax3.imshow(hourly_data, cmap="YlOrRd", aspect="auto")
    ax3.set_title("Stündliche Produktionsverteilung", fontsize=12, fontweight="bold")
    ax3.set_xlabel("Stunde")
    ax3.set_ylabel("Maschine")
    ax3.set_xticks(range(0, 24, 4))
    ax3.set_xticklabels([f"{h:02d}:00" for h in range(0, 24, 4)])
    ax3.set_yticks(range(len(machine_names)))
    ax3.set_yticklabels(machine_names, fontsize=8)

    # Colorbar
    plt.colorbar(im, ax=ax3, label="Stück/Stunde")

    # Effizienz-Radar-Chart
    ax4 = plt.subplot2grid((3, 4), (1, 2), rowspan=1, projection="polar")

    # Effizienz-Metriken
    efficiency_metrics = ["Verfügbarkeit", "Leistung", "Qualität", "OEE"]
    values = [94, 88, 96, 82]  # Beispielwerte

    angles = np.linspace(0, 2 * np.pi, len(efficiency_metrics), endpoint=False)
    values_plot = values + [values[0]]  # Kreis schließen
    angles_plot = np.concatenate([angles, [angles[0]]])

    ax4.plot(angles_plot, values_plot, "o-", linewidth=2, color="#2E86AB")
    ax4.fill(angles_plot, values_plot, alpha=0.25, color="#2E86AB")
    ax4.set_xticks(angles)
    ax4.set_xticklabels(efficiency_metrics)
    ax4.set_ylim(0, 100)
    ax4.set_title("Effizienz-KPIs\n(%)", fontsize=12, fontweight="bold", pad=20)
    ax4.grid(True)

    # Status-Übersicht
    ax5 = plt.subplot2grid((3, 4), (1, 3), rowspan=1)

    status_data = {"Betrieb": 85, "Wartung": 8, "Störung": 4, "Stillstand": 3}

    wedges, texts, autotexts = ax5.pie(
        status_data.values(),
        labels=status_data.keys(),
        autopct="%1.1f%%",
        colors=["#2E8B57", "#FFD700", "#DC143C", "#696969"],
        startangle=90,
    )
    ax5.set_title("Maschinenstatus\n(Gesamtzeit)", fontsize=12, fontweight="bold")

    # Trend-Analyse (unten)
    ax6 = plt.subplot2grid((3, 4), (2, 0), colspan=4, rowspan=1)

    # Tägliche Zusammenfassung
    daily_production = {}
    days = pd.date_range(start=start_date.date(), end=datetime.now().date(), freq="D")

    for machine, data in production_data.items():
        daily_totals = []
        for day in days:
            day_mask = pd.to_datetime(timestamps).date == day.date()
            daily_total = np.sum(np.array(data)[day_mask])
            daily_totals.append(daily_total)
        daily_production[machine] = daily_totals

    # Stacked Bar Chart
    bottom = np.zeros(len(days))
    for i, (machine, daily_data) in enumerate(daily_production.items()):
        ax6.bar(
            days,
            daily_data,
            bottom=bottom,
            label=machine.replace("_", " "),
            color=colors[i],
            alpha=0.8,
        )
        bottom += daily_data

    ax6.set_title("Tägliche Gesamtproduktion", fontsize=14, fontweight="bold")
    ax6.set_xlabel("Datum")
    ax6.set_ylabel("Stück/Tag")
    ax6.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax6.grid(True, alpha=0.3)

    # Datumsformatierung
    ax6.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
    plt.setp(ax6.xaxis.get_majorticklabels(), rotation=45)

    plt.tight_layout()
    plt.show()

    # Statistiken ausgeben
    print("📊 Produktions-Dashboard erstellt:")
    print(f"   Zeitraum: {len(days)} Tage, {len(timestamps)} Datenpunkte")
    for machine, data in production_data.items():
        total_production = np.sum(data)
        avg_hourly = np.mean(data)
        print(
            f"   {machine}: {total_production:.0f} Stück total (Ø {avg_hourly:.1f}/h)"
        )


def demo_wartungsplanung() -> None:
    """Visualisiert Wartungsplanung und Ausfallzeiten"""
    # Wartungsdaten simulieren
    maschinen = ["Laser A", "Laser B", "Presse C", "Biege D", "Stanz E"]

    # Wartungsintervalle und letzte Wartung
    np.random.seed(42)
    wartung_data = []

    base_date = datetime.now()

    for _i, maschine in enumerate(maschinen):
        # Letzte Wartungen
        letzte_wartung = base_date - timedelta(days=np.random.randint(10, 90))

        # Wartungsintervall
        intervall_tage = np.random.choice([30, 60, 90, 120])

        # Nächste Wartung
        naechste_wartung = letzte_wartung + timedelta(days=intervall_tage)

        # Ausfallzeiten in den letzten 6 Monaten
        ausfaelle = []
        for _ in range(np.random.randint(2, 8)):
            ausfall_datum = base_date - timedelta(days=np.random.randint(0, 180))
            dauer_stunden = np.random.exponential(4)  # Exponentialverteilung
            ausfaelle.append({"datum": ausfall_datum, "dauer": dauer_stunden})

        wartung_data.append(
            {
                "maschine": maschine,
                "letzte_wartung": letzte_wartung,
                "naechste_wartung": naechste_wartung,
                "intervall": intervall_tage,
                "ausfaelle": ausfaelle,
            }
        )

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Wartungsplanung Gantt-Chart
    colors = plt.cm.Set3(np.linspace(0, 1, len(maschinen)))

    for i, data in enumerate(wartung_data):
        # Wartungsbalken
        start = data["letzte_wartung"]
        ende = data["naechste_wartung"]

        # Vergangene Zeit (grün)
        vergangen = min(base_date, ende)
        ax1.barh(
            i,
            (vergangen - start).days,
            left=start,
            color="lightgreen",
            alpha=0.7,
            height=0.6,
        )

        # Verbleibende Zeit (gelb/rot)
        if base_date < ende:
            verbleibend = (ende - base_date).days
            color = "yellow" if verbleibend > 7 else "red"
            ax1.barh(i, verbleibend, left=base_date, color=color, alpha=0.7, height=0.6)

        # Wartungstermine markieren
        ax1.scatter(
            [data["letzte_wartung"], data["naechste_wartung"]],
            [i, i],
            c=["blue", "red"],
            s=100,
            zorder=10,
        )

    ax1.set_yticks(range(len(maschinen)))
    ax1.set_yticklabels(maschinen)
    ax1.set_xlabel("Datum")
    ax1.set_title("Wartungsplanung - Timeline", fontweight="bold")
    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%d.%m"))
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
    ax1.grid(True, alpha=0.3)

    # Legende
    from matplotlib.patches import Patch

    legend_elements = [
        Patch(facecolor="lightgreen", alpha=0.7, label="Seit letzter Wartung"),
        Patch(facecolor="yellow", alpha=0.7, label="Bis nächste Wartung"),
        Patch(facecolor="red", alpha=0.7, label="Überfällig/Kritisch"),
    ]
    ax1.legend(handles=legend_elements, loc="upper right")

    # 2. Ausfallzeiten-Analyse
    alle_ausfaelle = []
    for data in wartung_data:
        for ausfall in data["ausfaelle"]:
            alle_ausfaelle.append(
                {
                    "maschine": data["maschine"],
                    "dauer": ausfall["dauer"],
                    "datum": ausfall["datum"],
                }
            )

    df_ausfaelle = pd.DataFrame(alle_ausfaelle)

    # Box Plot für Ausfallzeiten
    ausfall_by_machine = [
        df_ausfaelle[df_ausfaelle["maschine"] == m]["dauer"].values for m in maschinen
    ]

    bp = ax2.boxplot(ausfall_by_machine, labels=maschinen, patch_artist=True)
    for patch, color in zip(bp["boxes"], colors, strict=False):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)

    ax2.set_title("Ausfallzeiten-Verteilung", fontweight="bold")
    ax2.set_ylabel("Dauer (Stunden)")
    ax2.set_xticklabels(maschinen, rotation=45)
    ax2.grid(True, alpha=0.3)

    # 3. Monatsübersicht Ausfälle
    monate = pd.date_range(
        start=base_date - timedelta(days=180), end=base_date, freq="M"
    )

    monthly_outages = np.zeros((len(maschinen), len(monate)))

    for i, data in enumerate(wartung_data):
        for ausfall in data["ausfaelle"]:
            for j, monat in enumerate(monate):
                if (
                    ausfall["datum"].month == monat.month
                    and ausfall["datum"].year == monat.year
                ):
                    monthly_outages[i, j] += ausfall["dauer"]

    im = ax3.imshow(monthly_outages, cmap="Reds", aspect="auto")
    ax3.set_title("Monatliche Ausfallzeiten (Stunden)", fontweight="bold")
    ax3.set_xlabel("Monat")
    ax3.set_ylabel("Maschine")
    ax3.set_xticks(range(len(monate)))
    ax3.set_xticklabels([m.strftime("%m/%y") for m in monate], rotation=45)
    ax3.set_yticks(range(len(maschinen)))
    ax3.set_yticklabels(maschinen)

    plt.colorbar(im, ax=ax3, label="Ausfallstunden")

    # 4. Wartungskosten vs. Ausfallkosten
    wartungskosten = [np.random.uniform(2000, 8000) for _ in maschinen]
    ausfallkosten = [
        np.sum(df_ausfaelle[df_ausfaelle["maschine"] == m]["dauer"]) * 500
        for m in maschinen
    ]

    x = np.arange(len(maschinen))
    width = 0.35

    bars1 = ax4.bar(
        x - width / 2,
        wartungskosten,
        width,
        label="Wartungskosten",
        color="steelblue",
        alpha=0.8,
    )
    bars2 = ax4.bar(
        x + width / 2,
        ausfallkosten,
        width,
        label="Ausfallkosten",
        color="orangered",
        alpha=0.8,
    )

    ax4.set_title("Kosten-Analyse", fontweight="bold")
    ax4.set_ylabel("Kosten (€)")
    ax4.set_xticks(x)
    ax4.set_xticklabels(maschinen, rotation=45)
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Werte auf Balken
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax4.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 100,
                f"{height:.0f}€",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    plt.tight_layout()
    plt.show()

    print("🔧 Wartungsanalyse erstellt:")
    print(f"   Überwachte Maschinen: {len(maschinen)}")
    print(f"   Erfasste Ausfälle: {len(alle_ausfaelle)}")
    print(f"   Durchschn. Ausfallzeit: {df_ausfaelle['dauer'].mean():.1f} Stunden")

    # Wartungsempfehlungen
    for data in wartung_data:
        tage_bis_wartung = (data["naechste_wartung"] - base_date).days
        if tage_bis_wartung <= 7:
            print(
                f"   ⚠️  {data['maschine']}: Wartung in {tage_bis_wartung} Tagen fällig!"
            )


def demo_qualitaetskontrolle() -> None:
    """Statistical Process Control (SPC) Visualisierung"""
    # Qualitätsdaten simulieren
    np.random.seed(42)

    # Prozessparameter
    target_thickness = 2.0  # mm
    ucl = 2.15  # Upper Control Limit
    lcl = 1.85  # Lower Control Limit
    usl = 2.20  # Upper Specification Limit
    lsl = 1.80  # Lower Specification Limit

    # Messdaten generieren (mit einigen Ausreißern)
    n_samples = 200
    measurements = np.random.normal(target_thickness, 0.08, n_samples)

    # Einige systematische Abweichungen einbauen
    measurements[50:70] += 0.1  # Werkzeugverschleiß
    measurements[120:125] = np.random.uniform(1.7, 1.8, 5)  # Materialfehler
    measurements[160:170] += 0.15  # Temperaturänderung

    sample_numbers = np.arange(1, n_samples + 1)

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # 1. Regelkarte (Control Chart)
    ax1.plot(sample_numbers, measurements, "b-", linewidth=1, alpha=0.7)
    ax1.scatter(sample_numbers, measurements, c="blue", s=20, alpha=0.6)

    # Kontrollgrenzen
    ax1.axhline(
        y=target_thickness, color="green", linestyle="-", linewidth=2, label="Sollwert"
    )
    ax1.axhline(y=ucl, color="orange", linestyle="--", linewidth=2, label="UCL/LCL")
    ax1.axhline(y=lcl, color="orange", linestyle="--", linewidth=2)
    ax1.axhline(y=usl, color="red", linestyle=":", linewidth=2, label="USL/LSL")
    ax1.axhline(y=lsl, color="red", linestyle=":", linewidth=2)

    # Ausreißer markieren
    outliers = np.where((measurements > ucl) | (measurements < lcl))[0]
    ax1.scatter(
        sample_numbers[outliers],
        measurements[outliers],
        c="red",
        s=50,
        marker="x",
        linewidth=2,
        label="Ausreißer",
    )

    ax1.set_title("Regelkarte - Materialdicke", fontweight="bold")
    ax1.set_xlabel("Probe Nr.")
    ax1.set_ylabel("Dicke (mm)")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Y-Achse begrenzen für bessere Sicht
    ax1.set_ylim(1.6, 2.4)

    # 2. Histogramm mit Normalverteilung
    ax2.hist(
        measurements,
        bins=30,
        alpha=0.7,
        color="skyblue",
        edgecolor="black",
        density=True,
    )

    # Normalverteilungskurve
    x_norm = np.linspace(measurements.min(), measurements.max(), 100)
    mean_val = np.mean(measurements)
    std_val = np.std(measurements)
    y_norm = (1 / (std_val * np.sqrt(2 * np.pi))) * np.exp(
        -0.5 * ((x_norm - mean_val) / std_val) ** 2
    )
    ax2.plot(x_norm, y_norm, "red", linewidth=2, label="Normalverteilung")

    # Spezifikationsgrenzen
    ax2.axvline(x=usl, color="red", linestyle=":", linewidth=2, label="USL/LSL")
    ax2.axvline(x=lsl, color="red", linestyle=":", linewidth=2)
    ax2.axvline(
        x=target_thickness, color="green", linestyle="-", linewidth=2, label="Sollwert"
    )

    ax2.set_title("Verteilung der Messwerte", fontweight="bold")
    ax2.set_xlabel("Dicke (mm)")
    ax2.set_ylabel("Dichte")
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # 3. Moving Range Chart
    moving_ranges = np.abs(np.diff(measurements))
    mr_mean = np.mean(moving_ranges)
    mr_ucl = mr_mean * 3.27  # Faktor für Moving Range

    ax3.plot(sample_numbers[1:], moving_ranges, "g-", linewidth=1, alpha=0.7)
    ax3.scatter(sample_numbers[1:], moving_ranges, c="green", s=20, alpha=0.6)

    ax3.axhline(
        y=mr_mean, color="blue", linestyle="-", linewidth=2, label="MR Durchschnitt"
    )
    ax3.axhline(y=mr_ucl, color="red", linestyle="--", linewidth=2, label="UCL")

    # Ausreißer in Moving Range
    mr_outliers = np.where(moving_ranges > mr_ucl)[0]
    ax3.scatter(
        sample_numbers[1:][mr_outliers],
        moving_ranges[mr_outliers],
        c="red",
        s=50,
        marker="x",
        linewidth=2,
        label="Ausreißer",
    )

    ax3.set_title("Moving Range Chart", fontweight="bold")
    ax3.set_xlabel("Probe Nr.")
    ax3.set_ylabel("Moving Range (mm)")
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. Prozessfähigkeit (Cpk-Analyse)
    # Cp und Cpk berechnen
    cp = (usl - lsl) / (6 * std_val)
    cpu = (usl - mean_val) / (3 * std_val)
    cpl = (mean_val - lsl) / (3 * std_val)
    cpk = min(cpu, cpl)

    # Prozentuale Ausschuss
    percent_above_usl = np.sum(measurements > usl) / len(measurements) * 100
    percent_below_lsl = np.sum(measurements < lsl) / len(measurements) * 100
    total_defect_rate = percent_above_usl + percent_below_lsl

    # Cpk-Bewertung visualisieren
    cpk_categories = [
        "Ungenügend\n(<1.0)",
        "Akzeptabel\n(1.0-1.33)",
        "Gut\n(1.33-1.67)",
        "Exzellent\n(>1.67)",
    ]
    cpk_values = [1.0, 1.33, 1.67, 2.0]
    cpk_colors = ["red", "orange", "yellow", "green"]

    ax4.bar(cpk_categories, cpk_values, color=cpk_colors, alpha=0.7)

    # Aktueller Cpk-Wert
    ax4.axhline(
        y=cpk,
        color="blue",
        linestyle="-",
        linewidth=3,
        label=f"Aktueller Cpk = {cpk:.2f}",
    )

    ax4.set_title("Prozessfähigkeit (Cpk)", fontweight="bold")
    ax4.set_ylabel("Cpk-Wert")
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Textinformationen hinzufügen
    stats_text = (
        f"Cp = {cp:.2f}\\nCpk = {cpk:.2f}\\nAusschuss = {total_defect_rate:.2f}%"
    )
    ax4.text(
        0.05,
        0.95,
        stats_text,
        transform=ax4.transAxes,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "wheat"},
    )

    plt.tight_layout()
    plt.show()

    print("📊 Qualitätskontrolle (SPC) erstellt:")
    print(f"   Proben analysiert: {n_samples}")
    print(f"   Durchschnitt: {mean_val:.3f} mm (Sollwert: {target_thickness:.3f} mm)")
    print(f"   Standardabweichung: {std_val:.3f} mm")
    print(f"   Cp (Prozessfähigkeit): {cp:.2f}")
    print(f"   Cpk (Prozessperformance): {cpk:.2f}")
    print(f"   Ausschussrate: {total_defect_rate:.2f}%")
    print(f"   Ausreißer in Regelkarte: {len(outliers)}")

    # Bewertung ausgeben
    if cpk >= 1.67:
        bewertung = "Exzellent 🟢"
    elif cpk >= 1.33:
        bewertung = "Gut 🟡"
    elif cpk >= 1.0:
        bewertung = "Akzeptabel 🟠"
    else:
        bewertung = "Verbesserung erforderlich 🔴"

    print(f"   Prozessbewertung: {bewertung}")


def demo_energieanalyse() -> None:
    """Visualisiert Energieverbrauch und Nachhaltigkeitskennzahlen"""
    # Energiedaten für verschiedene Bereiche
    bereiche = ["Laser-Schneiden", "Biegen", "Stanzen", "Schweißen", "Hilfssysteme"]

    # 24-Stunden Verbrauchsprofil
    stunden = np.arange(24)
    np.random.seed(42)

    # Grundlast und Produktionszeiten simulieren
    grundlast = [
        20,
        18,
        16,
        15,
        15,
        18,
        25,
        35,
        45,
        50,
        55,
        60,
        65,
        70,
        68,
        65,
        60,
        55,
        45,
        40,
        35,
        30,
        25,
        22,
    ]

    verbrauch_profile = {}
    for _i, bereich in enumerate(bereiche):
        # Individuelle Profile mit unterschiedlichen Faktoren
        if "Laser" in bereich:
            faktor = 1.5
            spitzenzeiten = [8, 9, 10, 13, 14, 15]  # Hauptproduktionszeiten
        elif "Biegen" in bereich:
            faktor = 0.8
            spitzenzeiten = [10, 11, 14, 15, 16]
        elif "Stanzen" in bereich:
            faktor = 1.2
            spitzenzeiten = [9, 10, 11, 13, 14]
        else:
            faktor = 0.6
            spitzenzeiten = [8, 9, 10, 11, 12, 13, 14, 15, 16]

        profile = np.array(grundlast) * faktor

        # Spitzenzeiten verstärken
        for spitze in spitzenzeiten:
            profile[spitze] *= 1.4

        # Rauschen hinzufügen
        profile += np.random.normal(0, profile * 0.1)
        profile = np.maximum(profile, 0)  # Keine negativen Werte

        verbrauch_profile[bereich] = profile

    plt.figure(figsize=(16, 12))

    # 1. Tagesverbrauchsprofil (Stacked Area Chart)
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2)

    # Kumulative Summen für Stacked Plot
    bottom = np.zeros(24)
    colors = plt.cm.Set2(np.linspace(0, 1, len(bereiche)))

    for i, (bereich, profile) in enumerate(verbrauch_profile.items()):
        ax1.fill_between(
            stunden, bottom, bottom + profile, label=bereich, color=colors[i], alpha=0.8
        )
        bottom += profile

    ax1.set_title("24h-Energieverbrauchsprofil", fontsize=14, fontweight="bold")
    ax1.set_xlabel("Uhrzeit")
    ax1.set_ylabel("Verbrauch (kW)")
    ax1.legend(loc="upper left", bbox_to_anchor=(1, 1))
    ax1.grid(True, alpha=0.3)

    # X-Achse formatieren
    ax1.set_xticks(range(0, 24, 4))
    ax1.set_xticklabels([f"{h:02d}:00" for h in range(0, 24, 4)])

    # 2. Verbrauch nach Bereichen (Pie Chart)
    ax2 = plt.subplot2grid((3, 3), (0, 2))

    tagesverbrauch = {
        bereich: np.sum(profile) for bereich, profile in verbrauch_profile.items()
    }

    wedges, texts, autotexts = ax2.pie(
        tagesverbrauch.values(),
        labels=tagesverbrauch.keys(),
        autopct="%1.1f%%",
        colors=colors,
        startangle=90,
    )
    ax2.set_title("Verbrauchsverteilung\n(Tagesgesamtverbrauch)", fontweight="bold")

    # Text-Größe anpassen
    for text in texts + autotexts:
        text.set_fontsize(8)

    # 3. Wöchlicher Trend
    ax3 = plt.subplot2grid((3, 3), (1, 0), colspan=2)

    # 7-Tage-Daten simulieren
    wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    wochen_faktoren = [1.0, 1.0, 1.0, 1.0, 1.0, 0.6, 0.3]  # Wochenende reduziert

    wochenverbrauch = {}
    for bereich in bereiche:
        tagesverbrauch_bereich = np.sum(verbrauch_profile[bereich])
        wochenverbrauch[bereich] = [
            tagesverbrauch_bereich * faktor for faktor in wochen_faktoren
        ]

    # Stacked Bar Chart
    bottom = np.zeros(7)
    x_pos = np.arange(len(wochentage))

    for i, bereich in enumerate(bereiche):
        ax3.bar(
            x_pos,
            wochenverbrauch[bereich],
            bottom=bottom,
            label=bereich,
            color=colors[i],
            alpha=0.8,
        )
        bottom += wochenverbrauch[bereich]

    ax3.set_title("Wöchlicher Energieverbrauch", fontweight="bold")
    ax3.set_xlabel("Wochentag")
    ax3.set_ylabel("Verbrauch (kWh/Tag)")
    ax3.set_xticks(x_pos)
    ax3.set_xticklabels(wochentage)
    ax3.legend(bbox_to_anchor=(1, 1))
    ax3.grid(True, alpha=0.3)

    # 4. Effizienz-Trends
    ax4 = plt.subplot2grid((3, 3), (1, 2))

    # KPIs für Nachhaltigkeit
    kpi_namen = [
        "Energieeffizienz\\n(kWh/Stück)",
        "CO₂ Reduzierung\\n(%)",
        "Recycling-Quote\\n(%)",
        "Abfall-Reduzierung\\n(%)",
    ]
    kpi_werte = [2.8, 15, 78, 23]
    kpi_ziele = [2.5, 20, 85, 30]

    x_kpi = np.arange(len(kpi_namen))
    width = 0.35

    bars1 = ax4.bar(
        x_kpi - width / 2,
        kpi_werte,
        width,
        label="Ist-Wert",
        color="lightblue",
        alpha=0.8,
    )
    bars2 = ax4.bar(
        x_kpi + width / 2,
        kpi_ziele,
        width,
        label="Ziel-Wert",
        color="darkgreen",
        alpha=0.8,
    )

    ax4.set_title("Nachhaltigkeits-KPIs", fontweight="bold")
    ax4.set_xticks(x_kpi)
    ax4.set_xticklabels(kpi_namen, fontsize=8)
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Werte auf Balken
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax4.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 0.5,
                f"{height:.1f}",
                ha="center",
                va="bottom",
                fontsize=8,
            )

    # 5. Kostenverlauf
    ax5 = plt.subplot2grid((3, 3), (2, 0), colspan=2)

    # 12-Monats-Kostenverlauf
    monate = [
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

    # Strompreise variieren
    strompreis_pro_kwh = 0.28  # €/kWh
    saisonale_faktoren = [1.2, 1.1, 1.0, 0.9, 0.8, 0.9, 1.1, 1.2, 1.0, 0.9, 1.1, 1.3]

    monatliche_kosten = []
    monatlicher_verbrauch = []

    for faktor in saisonale_faktoren:
        # Monatlicher Gesamtverbrauch
        tages_gesamt = sum(np.sum(profile) for profile in verbrauch_profile.values())
        monats_verbrauch = tages_gesamt * 30 * faktor  # 30 Tage/Monat
        monats_kosten = monats_verbrauch * strompreis_pro_kwh

        monatlicher_verbrauch.append(monats_verbrauch)
        monatliche_kosten.append(monats_kosten)

    ax5_twin = ax5.twinx()

    # Verbrauch (Balken)
    bars = ax5.bar(
        monate,
        monatlicher_verbrauch,
        alpha=0.6,
        color="steelblue",
        label="Verbrauch (kWh)",
    )

    # Kosten (Linie)
    ax5_twin.plot(
        monate, monatliche_kosten, "ro-", linewidth=2, markersize=6, label="Kosten (€)"
    )

    ax5.set_xlabel("Monat")
    ax5.set_ylabel("Verbrauch (kWh)", color="steelblue")
    ax5_twin.set_ylabel("Kosten (€)", color="red")
    ax5.set_title("Jahresübersicht Energieverbrauch und -kosten", fontweight="bold")
    ax5.grid(True, alpha=0.3)

    # Legende kombinieren
    lines1, labels1 = ax5.get_legend_handles_labels()
    lines2, labels2 = ax5_twin.get_legend_handles_labels()
    ax5.legend(lines1 + lines2, labels1 + labels2, loc="upper left")

    # 6. Effizienz-Heatmap
    ax6 = plt.subplot2grid((3, 3), (2, 2))

    # Effizienz-Matrix (Stunde vs. Bereich)
    effizienz_matrix = np.zeros((len(bereiche), 24))

    for i, bereich in enumerate(bereiche):
        for j in range(24):
            # Effizienz basierend auf Verbrauch und typischer Auslastung
            verbrauch = verbrauch_profile[bereich][j]
            # Effizienz sinkt bei sehr niedrigem oder sehr hohem Verbrauch
            optimal_verbrauch = np.mean(verbrauch_profile[bereich])
            effizienz = (
                100 - 20 * abs(verbrauch - optimal_verbrauch) / optimal_verbrauch
            )
            effizienz_matrix[i, j] = max(effizienz, 60)  # Minimum 60%

    im = ax6.imshow(effizienz_matrix, cmap="RdYlGn", aspect="auto", vmin=60, vmax=100)
    ax6.set_title("Stundenweise Effizienz", fontweight="bold")
    ax6.set_xlabel("Stunde")
    ax6.set_ylabel("Bereich")
    ax6.set_xticks(range(0, 24, 4))
    ax6.set_xticklabels([f"{h:02d}" for h in range(0, 24, 4)])
    ax6.set_yticks(range(len(bereiche)))
    ax6.set_yticklabels([bereich.split("-")[0] for bereich in bereiche], fontsize=8)

    plt.colorbar(im, ax=ax6, label="Effizienz (%)")

    plt.tight_layout()
    plt.show()

    # Ausgabe der Energiestatistiken
    gesamtverbrauch_tag = sum(np.sum(profile) for profile in verbrauch_profile.values())
    gesamtkosten_tag = gesamtverbrauch_tag * strompreis_pro_kwh
    co2_emission = gesamtverbrauch_tag * 0.4  # kg CO2/kWh (Deutschland-Mix)

    print("⚡ Energieanalyse erstellt:")
    print(f"   Tagesverbrauch gesamt: {gesamtverbrauch_tag:.1f} kWh")
    print(f"   Tageskosten gesamt: {gesamtkosten_tag:.2f} €")
    print(f"   CO₂-Emission pro Tag: {co2_emission:.1f} kg")
    print(f"   Jahresverbrauch (geschätzt): {gesamtverbrauch_tag * 250:.0f} kWh")
    print(f"   Jahreskosten (geschätzt): {gesamtkosten_tag * 250:.0f} €")

    # Verbrauch nach Bereichen
    print("   Verbrauch nach Bereichen:")
    for bereich, verbrauch in tagesverbrauch.items():
        anteil = verbrauch / gesamtverbrauch_tag * 100
        print(f"     {bereich}: {verbrauch:.1f} kWh ({anteil:.1f}%)")


def demo_oee_analyse() -> None:
    """Overall Equipment Effectiveness (OEE) Analyse"""
    # OEE-Daten für verschiedene Maschinen über eine Woche
    maschinen = ["Laser A", "Laser B", "Presse C", "Biege D"]
    tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    # OEE-Komponenten simulieren
    np.random.seed(42)

    # Verfügbarkeit (Availability) - Prozent der geplanten Zeit, in der produziert wird
    verfügbarkeit = {}
    # Leistung (Performance) - Prozent der theoretisch möglichen Geschwindigkeit
    leistung = {}
    # Qualität (Quality) - Prozent der fehlerfreien Teile
    qualitaet = {}
    # OEE = Verfügbarkeit × Leistung × Qualität
    oee_werte = {}

    for maschine in maschinen:
        verfügbarkeit[maschine] = []
        leistung[maschine] = []
        qualitaet[maschine] = []
        oee_werte[maschine] = []

        for tag in tage:
            # Wochenende hat andere Parameter
            if tag in ["Sa", "So"]:
                verf_base, leist_base, qual_base = 75, 70, 94
            else:
                verf_base, leist_base, qual_base = 85, 82, 96

            # Zufällige Variationen
            verf = np.clip(verf_base + np.random.normal(0, 8), 60, 100)
            leist = np.clip(leist_base + np.random.normal(0, 10), 50, 100)
            qual = np.clip(qual_base + np.random.normal(0, 4), 85, 100)

            verfügbarkeit[maschine].append(verf)
            leistung[maschine].append(leist)
            qualitaet[maschine].append(qual)
            oee_werte[maschine].append(verf * leist * qual / 10000)

    plt.figure(figsize=(16, 10))

    # 1. OEE-Übersicht (Heatmap)
    ax1 = plt.subplot2grid((2, 4), (0, 0), colspan=2)

    # OEE-Matrix für Heatmap
    oee_matrix = np.array([oee_werte[maschine] for maschine in maschinen])

    im1 = ax1.imshow(oee_matrix, cmap="RdYlGn", aspect="auto", vmin=40, vmax=80)
    ax1.set_title("OEE-Übersicht (Wochenverlauf)", fontsize=14, fontweight="bold")
    ax1.set_xlabel("Wochentag")
    ax1.set_ylabel("Maschine")
    ax1.set_xticks(range(len(tage)))
    ax1.set_xticklabels(tage)
    ax1.set_yticks(range(len(maschinen)))
    ax1.set_yticklabels(maschinen)

    # Werte in Zellen anzeigen
    for i in range(len(maschinen)):
        for j in range(len(tage)):
            ax1.text(
                j,
                i,
                f"{oee_matrix[i, j]:.1f}%",
                ha="center",
                va="center",
                color="black",
                fontweight="bold",
            )

    plt.colorbar(im1, ax=ax1, label="OEE (%)")

    # 2. Durchschnittliche OEE pro Maschine
    ax2 = plt.subplot2grid((2, 4), (0, 2))

    avg_oee = [np.mean(oee_werte[maschine]) for maschine in maschinen]
    colors = [
        "green" if oee >= 65 else "orange" if oee >= 50 else "red" for oee in avg_oee
    ]

    bars = ax2.bar(maschinen, avg_oee, color=colors, alpha=0.7)
    ax2.set_title("Durchschnittliche OEE", fontweight="bold")
    ax2.set_ylabel("OEE (%)")
    ax2.set_xticklabels(maschinen, rotation=45)

    # Werte auf Balken
    for bar, value in zip(bars, avg_oee, strict=False):
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value:.1f}%",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    # OEE-Benchmarks
    ax2.axhline(
        y=85, color="green", linestyle="--", alpha=0.7, label="World Class (85%)"
    )
    ax2.axhline(y=65, color="orange", linestyle="--", alpha=0.7, label="Gut (65%)")
    ax2.axhline(y=40, color="red", linestyle="--", alpha=0.7, label="Akzeptabel (40%)")
    ax2.legend(loc="upper right", fontsize=8)
    ax2.grid(True, alpha=0.3)

    # 3. OEE-Komponenten Analyse
    ax3 = plt.subplot2grid((2, 4), (0, 3))

    # Durchschnittswerte der Komponenten für eine Beispiel-Maschine
    beispiel_maschine = "Laser A"
    avg_verfuegbarkeit = np.mean(verfügbarkeit[beispiel_maschine])
    avg_leistung = np.mean(leistung[beispiel_maschine])
    avg_qualitaet = np.mean(qualitaet[beispiel_maschine])

    komponenten = ["Verfügbarkeit", "Leistung", "Qualität"]
    werte = [avg_verfuegbarkeit, avg_leistung, avg_qualitaet]
    komponent_colors = ["steelblue", "orange", "green"]

    bars = ax3.bar(komponenten, werte, color=komponent_colors, alpha=0.7)
    ax3.set_title(f"OEE-Komponenten\\n({beispiel_maschine})", fontweight="bold")
    ax3.set_ylabel("Prozent (%)")
    ax3.set_ylim(0, 100)
    ax3.set_xticklabels(komponenten, rotation=45)

    # Werte anzeigen
    for bar, value in zip(bars, werte, strict=False):
        ax3.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{value:.1f}%",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    ax3.grid(True, alpha=0.3)

    # 4. Trendanalyse
    ax4 = plt.subplot2grid((2, 4), (1, 0), colspan=2)

    # Trend über die Woche für alle Maschinen
    for i, maschine in enumerate(maschinen):
        ax4.plot(
            tage,
            oee_werte[maschine],
            marker="o",
            linewidth=2,
            label=maschine,
            color=plt.cm.Set1(i),
        )

    ax4.set_title("OEE-Trend (Wochenverlauf)", fontweight="bold")
    ax4.set_xlabel("Wochentag")
    ax4.set_ylabel("OEE (%)")
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    # Wochenende hervorheben
    ax4.axvspan(5.5, 6.5, alpha=0.2, color="gray", label="Wochenende")

    # 5. Verlustanalyse (Pareto-Chart)
    ax5 = plt.subplot2grid((2, 4), (1, 2))

    # Simulierte Verlustquellen
    verluste = {
        "Rüstzeiten": 12,
        "Mikrostopps": 8,
        "Geschwindigkeitsverlust": 7,
        "Ausschuss": 5,
        "Nacharbeit": 3,
        "Maschinenstörungen": 10,
        "Werkzeugwechsel": 4,
    }

    # Pareto-Analyse
    verluste_sorted = dict(sorted(verluste.items(), key=lambda x: x[1], reverse=True))
    verlust_namen = list(verluste_sorted.keys())
    verlust_werte = list(verluste_sorted.values())

    # Kumulative Prozente
    gesamt_verlust = sum(verlust_werte)
    kumulativ = np.cumsum(verlust_werte) / gesamt_verlust * 100

    # Balken
    bars = ax5.bar(verlust_namen, verlust_werte, color="salmon", alpha=0.7)

    # Kumulative Linie
    ax5_twin = ax5.twinx()
    ax5_twin.plot(
        verlust_namen, kumulativ, "ro-", color="darkred", linewidth=2, markersize=6
    )
    ax5_twin.set_ylabel("Kumulativ (%)", color="darkred")
    ax5_twin.set_ylim(0, 100)

    # 80%-Linie (Pareto-Regel)
    ax5_twin.axhline(y=80, color="blue", linestyle="--", alpha=0.7, label="80% Regel")

    ax5.set_title("Verlustanalyse (Pareto)", fontweight="bold")
    ax5.set_ylabel("Verlust (%)", color="salmon")
    ax5.set_xticklabels(verlust_namen, rotation=45, ha="right", fontsize=8)
    ax5.grid(True, alpha=0.3)

    # 6. OEE-Benchmark
    ax6 = plt.subplot2grid((2, 4), (1, 3))

    # Industriebenchmarks
    benchmark_kategorien = [
        "World\\nClass",
        "Sehr gut",
        "Gut",
        "Durchschnitt",
        "Verbesserung\\nerforderlich",
    ]
    benchmark_werte = [85, 75, 65, 55, 40]
    benchmark_colors = ["darkgreen", "green", "yellow", "orange", "red"]

    # Aktuelle OEE-Werte einordnen
    gesamt_oee = np.mean([np.mean(oee_werte[m]) for m in maschinen])

    bars = ax6.barh(
        benchmark_kategorien, benchmark_werte, color=benchmark_colors, alpha=0.7
    )

    # Aktuelle Position markieren
    ax6.axvline(
        x=gesamt_oee,
        color="blue",
        linestyle="-",
        linewidth=3,
        label=f"Aktuelle OEE: {gesamt_oee:.1f}%",
    )

    ax6.set_title("OEE-Benchmark", fontweight="bold")
    ax6.set_xlabel("OEE (%)")
    ax6.legend(loc="lower right")
    ax6.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Statistische Auswertung
    print("📊 OEE-Analyse erstellt:")
    print(f"   Analysierte Maschinen: {len(maschinen)}")
    print(f"   Zeitraum: {len(tage)} Tage")
    print(f"   Durchschnittliche Gesamt-OEE: {gesamt_oee:.1f}%")

    print("\\n   Maschinenbewertung:")
    for maschine in maschinen:
        avg_oee = np.mean(oee_werte[maschine])
        avg_verf = np.mean(verfügbarkeit[maschine])
        avg_leist = np.mean(leistung[maschine])
        avg_qual = np.mean(qualitaet[maschine])

        if avg_oee >= 65:
            bewertung = "Gut 🟢"
        elif avg_oee >= 50:
            bewertung = "Akzeptabel 🟡"
        else:
            bewertung = "Verbesserung erforderlich 🔴"

        print(f"     {maschine}: OEE {avg_oee:.1f}% ({bewertung})")
        print(
            f"       ↳ Verfügbarkeit: {avg_verf:.1f}%, Leistung: {avg_leist:.1f}%, Qualität: {avg_qual:.1f}%"
        )

    # Verbesserungsempfehlungen
    print("\\n   Hauptverlustquellen:")
    for i, (verlust, wert) in enumerate(list(verluste_sorted.items())[:3]):
        print(f"     {i + 1}. {verlust}: {wert}% der Gesamtverluste")


if __name__ == "__main__":
    main()
