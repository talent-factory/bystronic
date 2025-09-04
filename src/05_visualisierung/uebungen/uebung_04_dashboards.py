#!/usr/bin/env python3
"""
Dashboard-Entwicklung - Übung 4

Diese Übung behandelt die Erstellung professioneller Dashboards
mit verschiedenen Bibliotheken für industrielle Anwendungen bei Bystronic.

Lernziele:
- Matplotlib-basierte Dashboards entwickeln
- Plotly Dash für interaktive Web-Dashboards
- Real-time Datenaktualisierung implementieren
- Benutzerinteraktionen und Callbacks
- Export und Deployment von Dashboards

Autor: Python Grundkurs Bystronic
"""

import warnings
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Plotly für interaktive Dashboards (optional)
try:
    import plotly.express as px  # noqa: F401
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    print("⚠️ Plotly nicht verfügbar. Einige Dashboard-Features sind eingeschränkt.")

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")

# Styling für professionelle Dashboards
plt.style.use("default")
plt.rcParams.update(
    {
        "font.size": 10,
        "axes.titlesize": 12,
        "axes.labelsize": 11,
        "figure.figsize": (16, 10),
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.grid": True,
        "grid.alpha": 0.3,
    }
)

# Bystronic Corporate Colors
BYSTRONIC_COLORS = {
    "primary": "#1f77b4",
    "secondary": "#ff7f0e",
    "success": "#2ca02c",
    "warning": "#ffbb33",
    "danger": "#d62728",
    "info": "#17a2b8",
    "light": "#f8f9fa",
    "dark": "#343a40",
}


class ProductionDataGenerator:
    """Klasse zur Generierung realistischer Produktionsdaten"""

    def __init__(self, seed: int = 42):
        np.random.seed(seed)
        self.machines = ["Laser A", "Laser B", "Presse C", "Biege D", "Stanz E"]
        self.shifts = ["Früh", "Spät", "Nacht"]

    def generate_realtime_data(self, hours: int = 24) -> pd.DataFrame:
        """Generiert Echtzeit-Produktionsdaten"""
        now = datetime.now()
        timestamps = [now - timedelta(minutes=x * 5) for x in range(hours * 12)]
        timestamps.reverse()

        data = []
        for ts in timestamps:
            for machine in self.machines:
                # Realistische Schwankungen je Maschine
                base_performance = {
                    "Laser A": 85,
                    "Laser B": 90,
                    "Presse C": 75,
                    "Biege D": 80,
                    "Stanz E": 95,
                }

                performance = base_performance[machine] + np.random.normal(0, 5)
                performance = np.clip(performance, 50, 100)

                # Temperatur abhängig von Performance
                temperature = 65 + performance * 0.3 + np.random.normal(0, 3)
                temperature = np.clip(temperature, 60, 120)

                # Qualität korreliert negativ mit zu hoher Temperatur
                quality = 98 - max(0, temperature - 95) * 2 + np.random.normal(0, 1)
                quality = np.clip(quality, 85, 100)

                # Energieverbrauch
                power = 2000 + performance * 15 + np.random.normal(0, 100)
                power = np.clip(power, 1500, 4000)

                data.append(
                    {
                        "timestamp": ts,
                        "machine": machine,
                        "performance": performance,
                        "temperature": temperature,
                        "quality": quality,
                        "power_consumption": power,
                        "shift": self.get_shift(ts),
                        "status": self.get_machine_status(performance),
                    }
                )

        return pd.DataFrame(data)

    def get_shift(self, timestamp: datetime) -> str:
        """Bestimmt Schicht basierend auf Uhrzeit"""
        hour = timestamp.hour
        if 6 <= hour < 14:
            return "Früh"
        elif 14 <= hour < 22:
            return "Spät"
        else:
            return "Nacht"

    def get_machine_status(self, performance: float) -> str:
        """Bestimmt Maschinenstatus basierend auf Performance"""
        if performance >= 90:
            return "Optimal"
        elif performance >= 75:
            return "Normal"
        elif performance >= 60:
            return "Warnung"
        else:
            return "Kritisch"

    def generate_oee_data(self, days: int = 30) -> pd.DataFrame:
        """Generiert OEE-Daten (Overall Equipment Effectiveness)"""
        dates = pd.date_range(end=datetime.now(), periods=days, freq="D")

        oee_data = []
        for date in dates:
            for machine in self.machines:
                # OEE-Komponenten simulieren
                availability = np.random.uniform(0.85, 0.98)
                performance = np.random.uniform(0.80, 0.95)
                quality = np.random.uniform(0.92, 0.99)

                oee = availability * performance * quality

                # Geplante vs. tatsächliche Produktion
                planned_production = np.random.randint(800, 1200)
                actual_production = int(planned_production * performance)

                # Ausfallzeiten
                planned_time = 16 * 60  # 16 Stunden in Minuten
                downtime = int(planned_time * (1 - availability))

                oee_data.append(
                    {
                        "date": date,
                        "machine": machine,
                        "availability": availability,
                        "performance": performance,
                        "quality": quality,
                        "oee": oee,
                        "planned_production": planned_production,
                        "actual_production": actual_production,
                        "downtime_minutes": downtime,
                    }
                )

        return pd.DataFrame(oee_data)


def aufgabe_1_matplotlib_dashboard() -> None:
    """
    Aufgabe 1: Professionelles Matplotlib-Dashboard

    Erstelle ein umfassendes Dashboard mit mehreren Diagrammen,
    das einen vollständigen Überblick über die Produktion bietet.

    TODO für Kursteilnehmer:
    1. Erstelle ein Grid-Layout mit verschiedenen Plots
    2. Implementiere KPI-Anzeigen (Key Performance Indicators)
    3. Füge Status-Ampeln und Alarme hinzu
    4. Erstelle eine Legende und Erklärungen
    5. Implementiere automatische Aktualisierung
    """
    print("📊 Aufgabe 1: Professionelles Matplotlib-Dashboard")
    print("-" * 55)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # Daten generieren
    data_gen = ProductionDataGenerator()
    df_realtime = data_gen.generate_realtime_data(24)
    df_oee = data_gen.generate_oee_data(30)

    # Dashboard-Layout erstellen
    fig = plt.figure(figsize=(20, 12))
    fig.suptitle(
        "BYSTRONIC PRODUKTIONS-DASHBOARD", fontsize=20, fontweight="bold", y=0.95
    )

    # KPI-Bereich (oben)
    gs = fig.add_gridspec(4, 4, hspace=0.3, wspace=0.3)

    # 1. Aktuelle KPIs
    ax_kpis = fig.add_subplot(gs[0, :])
    ax_kpis.axis("off")

    # KPIs berechnen
    current_data = df_realtime[
        df_realtime["timestamp"] > df_realtime["timestamp"].max() - timedelta(hours=1)
    ]

    avg_performance = current_data["performance"].mean()
    avg_quality = current_data["quality"].mean()
    total_power = current_data["power_consumption"].sum() / 1000  # kW
    active_machines = len(current_data["machine"].unique())
    critical_machines = len(
        current_data[current_data["status"] == "Kritisch"]["machine"].unique()
    )

    # KPI-Boxen erstellen
    kpi_data = [
        (
            "Durchschn. Performance",
            f"{avg_performance:.1f}%",
            (
                BYSTRONIC_COLORS["success"]
                if avg_performance > 80
                else BYSTRONIC_COLORS["warning"]
            ),
        ),
        (
            "Durchschn. Qualität",
            f"{avg_quality:.1f}%",
            (
                BYSTRONIC_COLORS["success"]
                if avg_quality > 95
                else BYSTRONIC_COLORS["warning"]
            ),
        ),
        ("Gesamt Leistung", f"{total_power:.0f} kW", BYSTRONIC_COLORS["info"]),
        ("Aktive Maschinen", f"{active_machines}/5", BYSTRONIC_COLORS["primary"]),
        (
            "Kritische Alarme",
            str(critical_machines),
            (
                BYSTRONIC_COLORS["danger"]
                if critical_machines > 0
                else BYSTRONIC_COLORS["success"]
            ),
        ),
    ]

    for i, (label, value, color) in enumerate(kpi_data):
        x_pos = i * 0.18 + 0.1

        # Box zeichnen
        box = plt.Rectangle(
            (x_pos - 0.08, 0.2),
            0.16,
            0.6,
            facecolor=color,
            alpha=0.2,
            edgecolor=color,
            linewidth=2,
        )
        ax_kpis.add_patch(box)

        # Text hinzufügen
        ax_kpis.text(
            x_pos,
            0.7,
            value,
            ha="center",
            va="center",
            fontsize=16,
            fontweight="bold",
            color=color,
        )
        ax_kpis.text(
            x_pos, 0.3, label, ha="center", va="center", fontsize=10, wrap=True
        )

    ax_kpis.set_xlim(0, 1)
    ax_kpis.set_ylim(0, 1)

    # 2. Maschinenleistung über Zeit
    ax1 = fig.add_subplot(gs[1, :2])

    # Letzte 4 Stunden pro Maschine
    recent_data = df_realtime[
        df_realtime["timestamp"] > df_realtime["timestamp"].max() - timedelta(hours=4)
    ]

    for _i, machine in enumerate(data_gen.machines):
        machine_data = recent_data[recent_data["machine"] == machine]
        if not machine_data.empty:
            ax1.plot(
                machine_data["timestamp"],
                machine_data["performance"],
                label=machine,
                linewidth=2,
                marker="o",
                markersize=3,
            )

    ax1.set_title("Maschinenleistung (letzte 4 Stunden)", fontweight="bold")
    ax1.set_ylabel("Performance (%)")
    ax1.legend(loc="lower left", bbox_to_anchor=(0, 0))
    ax1.grid(True, alpha=0.3)

    # Warnschwellen
    ax1.axhline(y=90, color="green", linestyle="--", alpha=0.7, label="Optimal")
    ax1.axhline(y=75, color="orange", linestyle="--", alpha=0.7, label="Warnung")
    ax1.axhline(y=60, color="red", linestyle="--", alpha=0.7, label="Kritisch")

    # Zeitachse formatieren
    import matplotlib.dates as mdates

    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    ax1.tick_params(axis="x", rotation=45)

    # 3. Temperaturverteilung
    ax2 = fig.add_subplot(gs[1, 2:])

    # Aktuelle Temperaturen
    current_temps = current_data.groupby("machine")["temperature"].mean()
    colors = [
        (
            BYSTRONIC_COLORS["success"]
            if temp < 80
            else (
                BYSTRONIC_COLORS["warning"] if temp < 95 else BYSTRONIC_COLORS["danger"]
            )
        )
        for temp in current_temps.values
    ]

    bars = ax2.bar(current_temps.index, current_temps.values, color=colors, alpha=0.8)

    # Werte auf Balken anzeigen
    for bar, temp in zip(bars, current_temps.values, strict=False):
        ax2.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{temp:.1f}°C",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    ax2.set_title("Aktuelle Maschinentemperaturen", fontweight="bold")
    ax2.set_ylabel("Temperatur (°C)")
    ax2.axhline(y=80, color="orange", linestyle="--", alpha=0.7, label="Warnung")
    ax2.axhline(y=95, color="red", linestyle="--", alpha=0.7, label="Kritisch")
    ax2.legend()
    ax2.tick_params(axis="x", rotation=45)

    # 4. OEE-Trend (letzten 7 Tage)
    ax3 = fig.add_subplot(gs[2, :2])

    # OEE-Trend der letzten 7 Tage
    recent_oee = df_oee[df_oee["date"] > df_oee["date"].max() - timedelta(days=7)]
    daily_oee = recent_oee.groupby("date")["oee"].mean()

    ax3.plot(
        daily_oee.index,
        daily_oee.values * 100,
        color=BYSTRONIC_COLORS["primary"],
        linewidth=3,
        marker="o",
        markersize=6,
    )
    ax3.fill_between(
        daily_oee.index,
        daily_oee.values * 100,
        alpha=0.3,
        color=BYSTRONIC_COLORS["primary"],
    )

    ax3.set_title("OEE-Trend (7 Tage)", fontweight="bold")
    ax3.set_ylabel("OEE (%)")
    ax3.axhline(y=85, color="green", linestyle="--", alpha=0.7, label="Ziel: 85%")
    ax3.legend()
    ax3.tick_params(axis="x", rotation=45)

    # Formatierung der Datumsachse
    ax3.xaxis.set_major_formatter(mdates.DateFormatter("%m-%d"))

    # 5. Energieverbrauch nach Schicht
    ax4 = fig.add_subplot(gs[2, 2:])

    shift_power = current_data.groupby("shift")["power_consumption"].sum() / 1000
    colors_shift = [
        BYSTRONIC_COLORS["info"],
        BYSTRONIC_COLORS["warning"],
        BYSTRONIC_COLORS["dark"],
    ]

    wedges, texts, autotexts = ax4.pie(
        shift_power.values,
        labels=shift_power.index,
        autopct="%1.1f%%",
        colors=colors_shift,
        explode=(0.05, 0.05, 0.05),
    )

    ax4.set_title("Energieverbrauch nach Schicht\n(letzte 24h)", fontweight="bold")

    # 6. Maschinenauslastung Heatmap
    ax5 = fig.add_subplot(gs[3, :2])

    # Stündliche Auslastung der letzten 12 Stunden
    recent_12h = df_realtime[
        df_realtime["timestamp"] > df_realtime["timestamp"].max() - timedelta(hours=12)
    ]

    # Pivot-Tabelle für Heatmap
    recent_12h["hour"] = recent_12h["timestamp"].dt.hour
    pivot_data = recent_12h.pivot_table(
        values="performance",
        index="machine",
        columns="hour",
        aggfunc="mean",
        fill_value=0,
    )

    # Heatmap erstellen
    im = ax5.imshow(pivot_data.values, cmap="RdYlGn", aspect="auto", vmin=50, vmax=100)

    # Achsenbeschriftungen
    ax5.set_yticks(range(len(pivot_data.index)))
    ax5.set_yticklabels(pivot_data.index)
    ax5.set_xticks(range(len(pivot_data.columns)))
    ax5.set_xticklabels([f"{h:02d}:00" for h in pivot_data.columns], rotation=45)

    ax5.set_title("Stündliche Maschinenauslastung", fontweight="bold")

    # Werte in Zellen anzeigen
    for i in range(len(pivot_data.index)):
        for j in range(len(pivot_data.columns)):
            if pivot_data.iloc[i, j] > 0:
                ax5.text(
                    j,
                    i,
                    f"{pivot_data.iloc[i, j]:.0f}%",
                    ha="center",
                    va="center",
                    color="black",
                    fontsize=8,
                )

    # Colorbar
    cbar = plt.colorbar(im, ax=ax5)
    cbar.set_label("Performance (%)")

    # 7. Status-Übersicht
    ax6 = fig.add_subplot(gs[3, 2:])

    # Aktuelle Maschinenstatus
    status_counts = current_data["status"].value_counts()
    status_colors = {
        "Optimal": BYSTRONIC_COLORS["success"],
        "Normal": BYSTRONIC_COLORS["info"],
        "Warnung": BYSTRONIC_COLORS["warning"],
        "Kritisch": BYSTRONIC_COLORS["danger"],
    }

    # Donut Chart für Status
    colors = [status_colors.get(status, "gray") for status in status_counts.index]
    wedges, texts = ax6.pie(
        status_counts.values,
        labels=status_counts.index,
        colors=colors,
        startangle=90,
        wedgeprops={"width": 0.5},
    )

    # Zentrale Zahl (Gesamtanzahl)
    centre_circle = plt.Circle((0, 0), 0.70, fc="white")
    ax6.add_artist(centre_circle)
    ax6.text(
        0,
        0,
        f"{status_counts.sum()}\nMaschinen",
        ha="center",
        va="center",
        fontsize=14,
        fontweight="bold",
    )

    ax6.set_title("Aktueller Maschinenstatus", fontweight="bold")

    # Zeitstempel hinzufügen
    fig.text(
        0.99,
        0.01,
        f"Letzte Aktualisierung: {datetime.now().strftime('%H:%M:%S')}",
        ha="right",
        va="bottom",
        fontsize=10,
        alpha=0.7,
    )

    plt.tight_layout()
    plt.show()

    # Dashboard-Zusammenfassung
    print("\nDashboard-Zusammenfassung:")
    print(f"📈 Durchschnittliche Performance: {avg_performance:.1f}%")
    print(f"🎯 Durchschnittliche Qualität: {avg_quality:.1f}%")
    print(f"⚡ Gesamter Energieverbrauch: {total_power:.0f} kW")
    print(f"🏭 Aktive Maschinen: {active_machines}/5")
    if critical_machines > 0:
        print(f"🚨 ACHTUNG: {critical_machines} Maschinen in kritischem Zustand!")
    else:
        print("✅ Alle Maschinen laufen normal")

    print("\n💡 Dashboard-Features implementiert:")
    print("  • Real-time KPI-Anzeigen mit Farbkodierung")
    print("  • Zeitreihen-Visualisierung der Maschinenleistung")
    print("  • Temperatur-Monitoring mit Schwellenwerten")
    print("  • OEE-Trend-Analyse")
    print("  • Energieverbrauch nach Schichten")
    print("  • Heatmap der stündlichen Auslastung")
    print("  • Status-Übersicht mit Donut-Chart")


def aufgabe_2_plotly_interaktives_dashboard() -> None:
    """
    Aufgabe 2: Interaktives Plotly-Dashboard

    Erstelle ein interaktives Web-Dashboard mit Plotly,
    das Benutzerinteraktionen und Drill-Down-Funktionen bietet.

    TODO für Kursteilnehmer:
    1. Erstelle interaktive Plots mit Hover-Informationen
    2. Implementiere Dropdown-Filter und Slider
    3. Verbinde Plots miteinander (Cross-filtering)
    4. Füge Zoom- und Pan-Funktionen hinzu
    5. Exportiere Dashboard als HTML
    """
    print("\n🌐 Aufgabe 2: Interaktives Plotly-Dashboard")
    print("-" * 50)

    if not PLOTLY_AVAILABLE:
        print(
            "❌ Plotly nicht verfügbar. Installieren Sie plotly mit: pip install plotly"
        )
        return

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # Daten generieren
    data_gen = ProductionDataGenerator()
    df_realtime = data_gen.generate_realtime_data(72)  # 3 Tage
    df_oee = data_gen.generate_oee_data(30)

    print("Erstelle interaktives Dashboard...")

    # Subplot-Layout erstellen
    fig = make_subplots(
        rows=3,
        cols=2,
        subplot_titles=[
            "Maschinenleistung über Zeit",
            "OEE-Analyse nach Maschine",
            "Temperatur vs. Qualität",
            "Energieverbrauch-Trend",
            "Performance-Distribution",
            "Schichtanalyse",
        ],
        specs=[
            [{"secondary_y": True}, {"type": "bar"}],
            [{"type": "scatter"}, {"secondary_y": True}],
            [{"type": "box"}, {"type": "pie"}],
        ],
        vertical_spacing=0.12,
    )

    # 1. Maschinenleistung über Zeit (mit Temperatur als Secondary Y)
    colors_dict = {
        "Laser A": "#1f77b4",
        "Laser B": "#ff7f0e",
        "Presse C": "#2ca02c",
        "Biege D": "#d62728",
        "Stanz E": "#9467bd",
    }

    for machine in data_gen.machines:
        machine_data = df_realtime[df_realtime["machine"] == machine]

        # Performance (Primary Y-Axis)
        fig.add_trace(
            go.Scatter(
                x=machine_data["timestamp"],
                y=machine_data["performance"],
                mode="lines+markers",
                name=f"{machine} Performance",
                line={"color": colors_dict[machine], "width": 2},
                hovertemplate="<b>%{fullData.name}</b><br>"
                + "Zeit: %{x}<br>"
                + "Performance: %{y:.1f}%<br>"
                + "<extra></extra>",
            ),
            row=1,
            col=1,
        )

        # Temperatur (Secondary Y-Axis)
        fig.add_trace(
            go.Scatter(
                x=machine_data["timestamp"],
                y=machine_data["temperature"],
                mode="lines",
                name=f"{machine} Temp",
                line={"color": colors_dict[machine], "width": 1, "dash": "dash"},
                opacity=0.7,
                yaxis="y2",
                hovertemplate="<b>%{fullData.name}</b><br>"
                + "Zeit: %{x}<br>"
                + "Temperatur: %{y:.1f}°C<br>"
                + "<extra></extra>",
            ),
            row=1,
            col=1,
            secondary_y=True,
        )

    # 2. OEE-Analyse nach Maschine
    oee_by_machine = (
        df_oee.groupby("machine")
        .agg(
            {
                "availability": "mean",
                "performance": "mean",
                "quality": "mean",
                "oee": "mean",
            }
        )
        .reset_index()
    )

    fig.add_trace(
        go.Bar(
            x=oee_by_machine["machine"],
            y=oee_by_machine["availability"] * 100,
            name="Verfügbarkeit",
            marker_color="lightblue",
            hovertemplate="<b>%{x}</b><br>Verfügbarkeit: %{y:.1f}%<extra></extra>",
        ),
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Bar(
            x=oee_by_machine["machine"],
            y=oee_by_machine["performance"] * 100,
            name="Performance",
            marker_color="lightgreen",
            hovertemplate="<b>%{x}</b><br>Performance: %{y:.1f}%<extra></extra>",
        ),
        row=1,
        col=2,
    )

    fig.add_trace(
        go.Bar(
            x=oee_by_machine["machine"],
            y=oee_by_machine["quality"] * 100,
            name="Qualität",
            marker_color="lightcoral",
            hovertemplate="<b>%{x}</b><br>Qualität: %{y:.1f}%<extra></extra>",
        ),
        row=1,
        col=2,
    )

    # 3. Temperatur vs. Qualität (Bubble Chart)
    for machine in data_gen.machines:
        machine_data = df_realtime[df_realtime["machine"] == machine]

        fig.add_trace(
            go.Scatter(
                x=machine_data["temperature"],
                y=machine_data["quality"],
                mode="markers",
                name=f"{machine}",
                marker={
                    "color": colors_dict[machine],
                    "size": machine_data["performance"]
                    / 5,  # Größe basiert auf Performance
                    "opacity": 0.7,
                    "line": {"width": 1, "color": "DarkSlateGrey"},
                },
                hovertemplate="<b>%{fullData.name}</b><br>"
                + "Temperatur: %{x:.1f}°C<br>"
                + "Qualität: %{y:.1f}%<br>"
                + "Performance: %{marker.size*5:.1f}%<br>"
                + "<extra></extra>",
            ),
            row=2,
            col=1,
        )

    # 4. Energieverbrauch-Trend
    hourly_power = (
        df_realtime.groupby(df_realtime["timestamp"].dt.floor("H"))
        .agg({"power_consumption": "sum", "performance": "mean"})
        .reset_index()
    )

    # Energieverbrauch (Primary Y)
    fig.add_trace(
        go.Scatter(
            x=hourly_power["timestamp"],
            y=hourly_power["power_consumption"] / 1000,  # kW
            mode="lines+markers",
            name="Energieverbrauch",
            line={"color": "orange", "width": 3},
            hovertemplate="Zeit: %{x}<br>Verbrauch: %{y:.0f} kW<extra></extra>",
        ),
        row=2,
        col=2,
    )

    # Durchschnittliche Performance (Secondary Y)
    fig.add_trace(
        go.Scatter(
            x=hourly_power["timestamp"],
            y=hourly_power["performance"],
            mode="lines",
            name="Ø Performance",
            line={"color": "green", "width": 2, "dash": "dash"},
            yaxis="y4",
            hovertemplate="Zeit: %{x}<br>Performance: %{y:.1f}%<extra></extra>",
        ),
        row=2,
        col=2,
        secondary_y=True,
    )

    # 5. Performance-Distribution (Box Plot)
    for machine in data_gen.machines:
        machine_data = df_realtime[df_realtime["machine"] == machine]

        fig.add_trace(
            go.Box(
                y=machine_data["performance"],
                name=machine,
                boxpoints="outliers",
                marker_color=colors_dict[machine],
                hovertemplate="<b>%{fullData.name}</b><br>"
                + "Q1: %{q1}<br>"
                + "Median: %{median}<br>"
                + "Q3: %{q3}<br>"
                + "<extra></extra>",
            ),
            row=3,
            col=1,
        )

    # 6. Schichtanalyse (Pie Chart)
    shift_analysis = (
        df_realtime.groupby("shift")
        .agg({"performance": "mean", "power_consumption": "sum"})
        .reset_index()
    )

    fig.add_trace(
        go.Pie(
            labels=shift_analysis["shift"],
            values=shift_analysis["power_consumption"],
            name="Energieverbrauch",
            hovertemplate="<b>%{label}</b><br>"
            + "Verbrauch: %{value:.0f} W<br>"
            + "Anteil: %{percent}<br>"
            + "<extra></extra>",
            textinfo="label+percent",
        ),
        row=3,
        col=2,
    )

    # Layout-Updates
    fig.update_layout(
        title={
            "text": "BYSTRONIC - Interaktives Produktions-Dashboard",
            "x": 0.5,
            "font": {"size": 20, "color": "darkblue"},
        },
        height=900,
        showlegend=True,
        hovermode="closest",
    )

    # Achsenbeschriftungen
    fig.update_xaxes(title_text="Zeit", row=1, col=1)
    fig.update_yaxes(title_text="Performance (%)", row=1, col=1)
    fig.update_yaxes(title_text="Temperatur (°C)", secondary_y=True, row=1, col=1)

    fig.update_xaxes(title_text="Maschine", row=1, col=2)
    fig.update_yaxes(title_text="Wert (%)", row=1, col=2)

    fig.update_xaxes(title_text="Temperatur (°C)", row=2, col=1)
    fig.update_yaxes(title_text="Qualität (%)", row=2, col=1)

    fig.update_xaxes(title_text="Zeit", row=2, col=2)
    fig.update_yaxes(title_text="Energieverbrauch (kW)", row=2, col=2)
    fig.update_yaxes(title_text="Performance (%)", secondary_y=True, row=2, col=2)

    fig.update_xaxes(title_text="Maschine", row=3, col=1)
    fig.update_yaxes(title_text="Performance (%)", row=3, col=1)

    # Dashboard anzeigen
    fig.show()

    # Als HTML exportieren
    html_filename = (
        f"bystronic_dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
    )
    fig.write_html(html_filename)

    print("✅ Interaktives Dashboard erstellt!")
    print(f"📄 HTML-Export: {html_filename}")
    print("\nDashboard-Features:")
    print("🖱️ Interaktive Plots mit Hover-Informationen")
    print("🔍 Zoom- und Pan-Funktionen")
    print("📊 Multi-axiale Plots mit verschiedenen Metriken")
    print("🎨 Corporate Design mit Bystronic-Farben")
    print("📈 Echtzeitdaten-Simulation über 72 Stunden")

    # Zusätzliche Statistiken
    total_machines = len(data_gen.machines)
    avg_oee = df_oee["oee"].mean() * 100
    best_machine = oee_by_machine.loc[oee_by_machine["oee"].idxmax(), "machine"]

    print("\n📊 Dashboard-Insights:")
    print(f"  Gesamte OEE: {avg_oee:.1f}%")
    print(f"  Beste Maschine: {best_machine}")
    print(f"  Überwachte Maschinen: {total_machines}")


def aufgabe_3_realtime_dashboard() -> None:
    """
    Aufgabe 3: Real-time Dashboard mit Live-Updates

    Simuliere ein Dashboard mit automatischen Updates,
    das kontinuierlich neue Daten verarbeitet und anzeigt.

    TODO für Kursteilnehmer:
    1. Implementiere rollende Zeitfenster
    2. Füge Live-Alarme und Benachrichtigungen hinzu
    3. Erstelle automatische Berichte
    4. Implementiere Datenarchivierung
    5. Füge Export-Funktionen hinzu
    """
    print("\n🔴 Aufgabe 3: Real-time Dashboard mit Live-Updates")
    print("-" * 56)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    import time
    from collections import deque

    # Datenklasse für Live-Dashboard
    class LiveDashboard:
        def __init__(self, window_size: int = 50):
            self.window_size = window_size
            self.data_buffer = {
                machine: deque(maxlen=window_size)
                for machine in ProductionDataGenerator().machines
            }
            self.timestamps = deque(maxlen=window_size)
            self.alerts = []

        def add_data_point(self, timestamp, machine_data):
            """Füge neuen Datenpunkt hinzu"""
            self.timestamps.append(timestamp)

            for machine, data in machine_data.items():
                self.data_buffer[machine].append(data)

                # Alert-System
                if data["performance"] < 60:
                    alert = {
                        "timestamp": timestamp,
                        "machine": machine,
                        "type": "KRITISCH",
                        "message": f"Performance unter 60%: {data['performance']:.1f}%",
                    }
                    self.alerts.append(alert)
                    if len(self.alerts) > 10:  # Nur letzte 10 Alerts behalten
                        self.alerts.pop(0)

                if data["temperature"] > 95:
                    alert = {
                        "timestamp": timestamp,
                        "machine": machine,
                        "type": "WARNUNG",
                        "message": f"Temperatur zu hoch: {data['temperature']:.1f}°C",
                    }
                    self.alerts.append(alert)
                    if len(self.alerts) > 10:
                        self.alerts.pop(0)

        def update_dashboard(self):
            """Dashboard-Update mit aktuellen Daten"""
            if not self.timestamps:
                return

            # 2x2 Dashboard Layout
            fig, axes = plt.subplots(2, 2, figsize=(16, 10))
            fig.suptitle(
                f"LIVE DASHBOARD - {datetime.now().strftime('%H:%M:%S')}",
                fontsize=16,
                fontweight="bold",
            )

            # Plot 1: Performance Trends
            ax1 = axes[0, 0]
            for machine in self.data_buffer.keys():
                if self.data_buffer[machine]:
                    performances = [
                        data["performance"] for data in self.data_buffer[machine]
                    ]
                    ax1.plot(
                        range(len(performances)),
                        performances,
                        label=machine,
                        linewidth=2,
                        marker="o",
                        markersize=3,
                    )

            ax1.set_title("Live Performance Trends")
            ax1.set_ylabel("Performance (%)")
            ax1.set_xlabel("Zeit (Datenpunkte)")
            ax1.legend()
            ax1.grid(True, alpha=0.3)
            ax1.axhline(y=90, color="green", linestyle="--", alpha=0.7)
            ax1.axhline(y=75, color="orange", linestyle="--", alpha=0.7)
            ax1.axhline(y=60, color="red", linestyle="--", alpha=0.7)

            # Plot 2: Aktuelle KPIs
            ax2 = axes[0, 1]
            ax2.axis("off")

            if self.data_buffer and any(self.data_buffer.values()):
                # Letzte Werte extrahieren
                latest_data = {}
                for machine in self.data_buffer.keys():
                    if self.data_buffer[machine]:
                        latest_data[machine] = self.data_buffer[machine][-1]

                if latest_data:
                    avg_perf = np.mean(
                        [data["performance"] for data in latest_data.values()]
                    )
                    avg_temp = np.mean(
                        [data["temperature"] for data in latest_data.values()]
                    )
                    avg_qual = np.mean(
                        [data["quality"] for data in latest_data.values()]
                    )
                    total_power = (
                        sum([data["power"] for data in latest_data.values()]) / 1000
                    )

                    # KPI-Anzeige
                    kpis = [
                        (
                            "AVG PERFORMANCE",
                            f"{avg_perf:.1f}%",
                            (
                                "green"
                                if avg_perf > 80
                                else "orange" if avg_perf > 60 else "red"
                            ),
                        ),
                        (
                            "AVG TEMPERATURE",
                            f"{avg_temp:.1f}°C",
                            (
                                "green"
                                if avg_temp < 80
                                else "orange" if avg_temp < 95 else "red"
                            ),
                        ),
                        (
                            "AVG QUALITY",
                            f"{avg_qual:.1f}%",
                            "green" if avg_qual > 95 else "orange",
                        ),
                        ("TOTAL POWER", f"{total_power:.1f} kW", "blue"),
                    ]

                    for i, (label, value, color) in enumerate(kpis):
                        y_pos = 0.8 - i * 0.2
                        ax2.text(0.1, y_pos, label, fontsize=12, fontweight="bold")
                        ax2.text(
                            0.6,
                            y_pos,
                            value,
                            fontsize=14,
                            fontweight="bold",
                            color=color,
                        )

            ax2.set_xlim(0, 1)
            ax2.set_ylim(0, 1)
            ax2.set_title("Live KPIs")

            # Plot 3: Temperature Heatmap
            ax3 = axes[1, 0]

            if self.data_buffer and any(self.data_buffer.values()):
                # Temperatur-Matrix erstellen (letzte 10 Datenpunkte)
                temp_matrix = []
                machines = list(self.data_buffer.keys())

                for machine in machines:
                    machine_temps = []
                    buffer = self.data_buffer[machine]
                    recent_data = (
                        list(buffer)[-10:] if len(buffer) >= 10 else list(buffer)
                    )

                    for data in recent_data:
                        machine_temps.append(data["temperature"])

                    # Auf 10 Werte auffüllen falls nötig
                    while len(machine_temps) < 10:
                        machine_temps.insert(0, 0)

                    temp_matrix.append(machine_temps)

                if temp_matrix:
                    temp_array = np.array(temp_matrix)
                    im = ax3.imshow(temp_array, cmap="RdYlBu_r", aspect="auto")

                    ax3.set_yticks(range(len(machines)))
                    ax3.set_yticklabels(machines)
                    ax3.set_xlabel("Zeit →")
                    ax3.set_title("Temperatur Heatmap (letzte 10 Punkte)")

                    # Colorbar
                    plt.colorbar(im, ax=ax3, label="Temperatur (°C)")

            # Plot 4: Alert-System
            ax4 = axes[1, 1]
            ax4.axis("off")
            ax4.set_title("Live Alerts", fontweight="bold", color="red")

            if self.alerts:
                for i, alert in enumerate(self.alerts[-5:]):  # Nur letzte 5 Alerts
                    y_pos = 0.9 - i * 0.15
                    color = "red" if alert["type"] == "KRITISCH" else "orange"

                    ax4.text(
                        0.05,
                        y_pos,
                        f"{alert['type']}",
                        fontweight="bold",
                        color=color,
                        fontsize=10,
                    )
                    ax4.text(
                        0.05,
                        y_pos - 0.05,
                        f"{alert['machine']}: {alert['message']}",
                        fontsize=9,
                        wrap=True,
                    )
                    ax4.text(
                        0.05,
                        y_pos - 0.08,
                        alert["timestamp"].strftime("%H:%M:%S"),
                        fontsize=8,
                        alpha=0.7,
                    )
            else:
                ax4.text(
                    0.5,
                    0.5,
                    "✅ Keine aktiven Alerts",
                    ha="center",
                    va="center",
                    fontsize=14,
                    color="green",
                )

            ax4.set_xlim(0, 1)
            ax4.set_ylim(0, 1)

            plt.tight_layout()
            plt.show()

    # Live-Dashboard Simulation
    dashboard = LiveDashboard(window_size=30)
    data_gen = ProductionDataGenerator()

    print("🚀 Live-Dashboard wird gestartet...")
    print("📊 Simuliert 20 Datenpunkte in 5-Sekunden-Intervallen")
    print("⏹️ Zum Stoppen Strg+C drücken")

    try:
        for iteration in range(20):
            # Aktuelle Zeit
            current_time = datetime.now()

            # Neue Maschinendaten generieren
            machine_data = {}
            for machine in data_gen.machines:
                # Simuliere realistische Schwankungen
                base_performance = np.random.uniform(70, 95)

                # Gelegentlich kritische Werte simulieren
                if np.random.random() < 0.1:  # 10% Chance auf Probleme
                    base_performance = np.random.uniform(45, 65)

                temperature = 70 + base_performance * 0.4 + np.random.normal(0, 5)
                temperature = np.clip(temperature, 60, 120)

                quality = 96 - max(0, temperature - 85) * 0.5 + np.random.normal(0, 2)
                quality = np.clip(quality, 80, 100)

                power = 1800 + base_performance * 20 + np.random.normal(0, 200)
                power = np.clip(power, 1000, 4000)

                machine_data[machine] = {
                    "performance": base_performance,
                    "temperature": temperature,
                    "quality": quality,
                    "power": power,
                }

            # Daten zum Dashboard hinzufügen
            dashboard.add_data_point(current_time, machine_data)

            # Dashboard aktualisieren (alle 5 Iterationen)
            if iteration % 5 == 0:
                print(f"\n📊 Dashboard Update #{iteration // 5 + 1}")
                dashboard.update_dashboard()

                # Alert-Zusammenfassung
                if dashboard.alerts:
                    recent_alerts = [
                        a
                        for a in dashboard.alerts
                        if (current_time - a["timestamp"]).seconds < 30
                    ]
                    if recent_alerts:
                        print(f"🚨 {len(recent_alerts)} aktive Alerts!")

                # Kurze Statistiken
                if machine_data:
                    avg_perf = np.mean(
                        [data["performance"] for data in machine_data.values()]
                    )
                    critical_machines = sum(
                        1 for data in machine_data.values() if data["performance"] < 60
                    )
                    print(f"📈 Durchschnittsperformance: {avg_perf:.1f}%")
                    if critical_machines > 0:
                        print(f"⚠️ {critical_machines} Maschinen kritisch!")

            # Kurze Pause zwischen Updates
            time.sleep(1)  # Reduziert für Demo (normalerweise 5-60 Sekunden)

    except KeyboardInterrupt:
        print("\n⏹️ Live-Dashboard gestoppt durch Benutzer")

    # Finale Zusammenfassung
    print("\n📋 Live-Dashboard Zusammenfassung:")
    print(f"  Überwachte Zeitspanne: {len(dashboard.timestamps)} Datenpunkte")
    print(f"  Gesamte Alerts: {len(dashboard.alerts)}")
    print(f"  Überwachte Maschinen: {len(dashboard.data_buffer)}")

    if dashboard.alerts:
        kritische_alerts = [a for a in dashboard.alerts if a["type"] == "KRITISCH"]
        warn_alerts = [a for a in dashboard.alerts if a["type"] == "WARNUNG"]
        print(f"  Kritische Alerts: {len(kritische_alerts)}")
        print(f"  Warnungs-Alerts: {len(warn_alerts)}")

    print("\n💡 Real-time Dashboard Features implementiert:")
    print("  • Rolling Window Datenverarbeitung")
    print("  • Automatisches Alert-System")
    print("  • Live KPI-Monitoring")
    print("  • Temperatur-Heatmap")
    print("  • Kontinuierliche Datenaktualisierung")


def aufgabe_4_dashboard_export() -> None:
    """
    Aufgabe 4: Dashboard-Export und -Deployment

    Erstelle verschiedene Export-Formate und Deployment-Optionen
    für die entwickelten Dashboards.

    TODO für Kursteilnehmer:
    1. PDF-Report-Generation
    2. Excel-Dashboard mit Diagrammen
    3. HTML-Dashboard für Web-Deployment
    4. PowerPoint-Präsentation
    5. Automatische E-Mail-Berichte
    """
    print("\n📤 Aufgabe 4: Dashboard-Export und -Deployment")
    print("-" * 52)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # Daten generieren
    data_gen = ProductionDataGenerator()
    df_realtime = data_gen.generate_realtime_data(24)
    df_oee = data_gen.generate_oee_data(7)

    print("📊 Generiere Export-Berichte...")

    # 1. PDF-Report erstellen
    def create_pdf_report():
        """Erstellt einen PDF-Report mit matplotlib"""
        print("📄 Erstelle PDF-Report...")

        from matplotlib.backends.backend_pdf import PdfPages

        with PdfPages(
            f"bystronic_report_{datetime.now().strftime('%Y%m%d')}.pdf"
        ) as pdf:
            # Seite 1: Übersicht
            fig1, axes = plt.subplots(2, 2, figsize=(11, 8))
            fig1.suptitle(
                "BYSTRONIC PRODUKTIONSBERICHT", fontsize=16, fontweight="bold"
            )

            # Maschinenleistung
            for machine in data_gen.machines:
                machine_data = df_realtime[df_realtime["machine"] == machine]
                axes[0, 0].plot(
                    machine_data["timestamp"],
                    machine_data["performance"],
                    label=machine,
                    linewidth=2,
                )
            axes[0, 0].set_title("Maschinenleistung (24h)")
            axes[0, 0].set_ylabel("Performance (%)")
            axes[0, 0].legend()
            axes[0, 0].grid(True, alpha=0.3)

            # OEE-Übersicht
            daily_oee = df_oee.groupby("date")["oee"].mean() * 100
            axes[0, 1].bar(range(len(daily_oee)), daily_oee.values, color="steelblue")
            axes[0, 1].set_title("OEE-Trend (7 Tage)")
            axes[0, 1].set_ylabel("OEE (%)")
            axes[0, 1].axhline(y=85, color="red", linestyle="--", label="Ziel")
            axes[0, 1].legend()

            # Qualitätsverteilung
            axes[1, 0].hist(
                df_realtime["quality"], bins=20, color="lightgreen", alpha=0.7
            )
            axes[1, 0].set_title("Qualitätsverteilung")
            axes[1, 0].set_xlabel("Qualität (%)")
            axes[1, 0].set_ylabel("Häufigkeit")

            # Status-Übersicht
            status_counts = df_realtime["status"].value_counts()
            axes[1, 1].pie(
                status_counts.values, labels=status_counts.index, autopct="%1.1f%%"
            )
            axes[1, 1].set_title("Maschinenstatus")

            plt.tight_layout()
            pdf.savefig(fig1)
            plt.close()

            # Seite 2: Detailanalyse
            fig2 = plt.figure(figsize=(11, 8))
            gs = fig2.add_gridspec(3, 2, hspace=0.4)

            # Temperatur-Trends
            ax1 = fig2.add_subplot(gs[0, :])
            hourly_temp = df_realtime.groupby(df_realtime["timestamp"].dt.floor("H"))[
                "temperature"
            ].mean()
            ax1.plot(hourly_temp.index, hourly_temp.values, color="red", linewidth=2)
            ax1.set_title("Stündliche Durchschnittstemperatur")
            ax1.set_ylabel("Temperatur (°C)")
            ax1.grid(True, alpha=0.3)

            # Energieverbrauch nach Schicht
            ax2 = fig2.add_subplot(gs[1, 0])
            shift_power = df_realtime.groupby("shift")["power_consumption"].sum()
            ax2.bar(
                shift_power.index,
                shift_power.values,
                color=["gold", "orange", "darkblue"],
            )
            ax2.set_title("Energieverbrauch pro Schicht")
            ax2.set_ylabel("Verbrauch (W)")

            # Korrelationsanalyse
            ax3 = fig2.add_subplot(gs[1, 1])
            ax3.scatter(df_realtime["temperature"], df_realtime["quality"], alpha=0.6)
            ax3.set_title("Temperatur vs. Qualität")
            ax3.set_xlabel("Temperatur (°C)")
            ax3.set_ylabel("Qualität (%)")

            # Statistik-Tabelle
            ax4 = fig2.add_subplot(gs[2, :])
            ax4.axis("off")

            # Zusammenfassende Statistiken
            stats_data = []
            for machine in data_gen.machines:
                machine_data = df_realtime[df_realtime["machine"] == machine]
                stats_data.append(
                    [
                        machine,
                        f"{machine_data['performance'].mean():.1f}%",
                        f"{machine_data['temperature'].mean():.1f}°C",
                        f"{machine_data['quality'].mean():.1f}%",
                        f"{machine_data['power_consumption'].sum() / 1000:.0f} kWh",
                    ]
                )

            table = ax4.table(
                cellText=stats_data,
                colLabels=[
                    "Maschine",
                    "Ø Performance",
                    "Ø Temperatur",
                    "Ø Qualität",
                    "Energieverbrauch",
                ],
                cellLoc="center",
                loc="center",
            )
            table.auto_set_font_size(False)
            table.set_fontsize(10)
            table.scale(1, 2)

            ax4.set_title(
                "Maschinenzusammenfassung", y=0.8, fontsize=14, fontweight="bold"
            )

            pdf.savefig(fig2)
            plt.close()

        print("✅ PDF-Report erstellt: bystronic_report_[datum].pdf")

    # 2. Excel-Dashboard erstellen
    def create_excel_dashboard():
        """Erstellt ein Excel-Dashboard mit Diagrammen"""
        print("📊 Erstelle Excel-Dashboard...")

        try:
            import xlsxwriter

            # Excel-Datei erstellen
            filename = f"bystronic_dashboard_{datetime.now().strftime('%Y%m%d')}.xlsx"
            workbook = xlsxwriter.Workbook(filename)

            # Daten-Worksheet
            data_sheet = workbook.add_worksheet("Rohdaten")

            # DataFrame zu Excel schreiben
            df_export = df_realtime[
                [
                    "timestamp",
                    "machine",
                    "performance",
                    "temperature",
                    "quality",
                    "power_consumption",
                ]
            ]

            # Header schreiben
            headers = [
                "Zeitstempel",
                "Maschine",
                "Performance (%)",
                "Temperatur (°C)",
                "Qualität (%)",
                "Leistung (W)",
            ]
            for col, header in enumerate(headers):
                data_sheet.write(0, col, header)

            # Daten schreiben
            for row, (_, data) in enumerate(df_export.iterrows(), 1):
                data_sheet.write(
                    row, 0, data["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
                )
                data_sheet.write(row, 1, data["machine"])
                data_sheet.write(row, 2, data["performance"])
                data_sheet.write(row, 3, data["temperature"])
                data_sheet.write(row, 4, data["quality"])
                data_sheet.write(row, 5, data["power_consumption"])

            # Dashboard-Worksheet
            dashboard_sheet = workbook.add_worksheet("Dashboard")

            # Formatierung
            title_format = workbook.add_format(
                {"bold": True, "font_size": 16, "align": "center"}
            )
            header_format = workbook.add_format(
                {"bold": True, "bg_color": "#4F81BD", "font_color": "white"}
            )

            # Titel
            dashboard_sheet.merge_range(
                "A1:H1", "BYSTRONIC PRODUKTIONS-DASHBOARD", title_format
            )

            # KPI-Tabelle
            dashboard_sheet.write("A3", "KEY PERFORMANCE INDICATORS", header_format)

            kpis = [
                [
                    "Durchschnittliche Performance",
                    f"{df_realtime['performance'].mean():.1f}%",
                ],
                ["Durchschnittliche Qualität", f"{df_realtime['quality'].mean():.1f}%"],
                [
                    "Gesamter Energieverbrauch",
                    f"{df_realtime['power_consumption'].sum() / 1000:.0f} kWh",
                ],
                ["Überwachte Maschinen", str(len(data_gen.machines))],
                ["Datenpunkte", str(len(df_realtime))],
            ]

            for i, (kpi, value) in enumerate(kpis, 4):
                dashboard_sheet.write(f"A{i}", kpi)
                dashboard_sheet.write(f"B{i}", value)

            # Maschinen-Übersicht
            dashboard_sheet.write("D3", "MASCHINEN-ÜBERSICHT", header_format)
            dashboard_sheet.write("D4", "Maschine")
            dashboard_sheet.write("E4", "Ø Performance")
            dashboard_sheet.write("F4", "Ø Temperatur")
            dashboard_sheet.write("G4", "Status")

            for i, machine in enumerate(data_gen.machines, 5):
                machine_data = df_realtime[df_realtime["machine"] == machine]
                avg_perf = machine_data["performance"].mean()
                avg_temp = machine_data["temperature"].mean()
                status = "OK" if avg_perf > 75 else "WARNUNG"

                dashboard_sheet.write(f"D{i}", machine)
                dashboard_sheet.write(f"E{i}", f"{avg_perf:.1f}%")
                dashboard_sheet.write(f"F{i}", f"{avg_temp:.1f}°C")
                dashboard_sheet.write(f"G{i}", status)

            workbook.close()
            print(f"✅ Excel-Dashboard erstellt: {filename}")

        except ImportError:
            print(
                "⚠️ xlsxwriter nicht verfügbar. Installieren mit: pip install xlsxwriter"
            )

    # 3. HTML-Dashboard erstellen
    def create_html_dashboard():
        """Erstellt ein eigenständiges HTML-Dashboard"""
        print("🌐 Erstelle HTML-Dashboard...")

        html_content = f"""
        <!DOCTYPE html>
        <html lang="de">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Bystronic Produktions-Dashboard</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    margin: 0;
                    padding: 20px;
                    background-color: #f5f5f5;
                }}
                .header {{
                    background: linear-gradient(135deg, #1f77b4, #4dabf7);
                    color: white;
                    text-align: center;
                    padding: 30px;
                    border-radius: 10px;
                    margin-bottom: 30px;
                }}
                .kpi-grid {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                    gap: 20px;
                    margin-bottom: 30px;
                }}
                .kpi-card {{
                    background: white;
                    padding: 25px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    text-align: center;
                    border-left: 5px solid #1f77b4;
                }}
                .kpi-value {{
                    font-size: 2.5em;
                    font-weight: bold;
                    color: #1f77b4;
                    margin-bottom: 10px;
                }}
                .kpi-label {{
                    color: #666;
                    font-size: 1.1em;
                }}
                .machine-table {{
                    background: white;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    margin-bottom: 30px;
                }}
                .machine-table table {{
                    width: 100%;
                    border-collapse: collapse;
                }}
                .machine-table th, .machine-table td {{
                    padding: 15px;
                    text-align: left;
                    border-bottom: 1px solid #eee;
                }}
                .machine-table th {{
                    background-color: #1f77b4;
                    color: white;
                }}
                .status-ok {{ color: #28a745; font-weight: bold; }}
                .status-warning {{ color: #ffc107; font-weight: bold; }}
                .status-critical {{ color: #dc3545; font-weight: bold; }}
                .footer {{
                    text-align: center;
                    color: #666;
                    margin-top: 30px;
                    padding: 20px;
                }}
            </style>
        </head>
        <body>
            <div class="header">
                <h1>🏭 BYSTRONIC PRODUKTIONS-DASHBOARD</h1>
                <p>Letztes Update: {datetime.now().strftime("%d.%m.%Y %H:%M:%S")}</p>
            </div>

            <div class="kpi-grid">
                <div class="kpi-card">
                    <div class="kpi-value">{df_realtime["performance"].mean():.1f}%</div>
                    <div class="kpi-label">Durchschnitts-Performance</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{df_realtime["quality"].mean():.1f}%</div>
                    <div class="kpi-label">Durchschnitts-Qualität</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{df_realtime["power_consumption"].sum() / 1000:.0f}</div>
                    <div class="kpi-label">Gesamt-Energieverbrauch (kWh)</div>
                </div>
                <div class="kpi-card">
                    <div class="kpi-value">{len(data_gen.machines)}</div>
                    <div class="kpi-label">Aktive Maschinen</div>
                </div>
            </div>

            <div class="machine-table">
                <table>
                    <thead>
                        <tr>
                            <th>Maschine</th>
                            <th>Performance (%)</th>
                            <th>Temperatur (°C)</th>
                            <th>Qualität (%)</th>
                            <th>Energieverbrauch (kWh)</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
        """

        # Maschinendaten hinzufügen
        for machine in data_gen.machines:
            machine_data = df_realtime[df_realtime["machine"] == machine]
            avg_perf = machine_data["performance"].mean()
            avg_temp = machine_data["temperature"].mean()
            avg_qual = machine_data["quality"].mean()
            total_energy = machine_data["power_consumption"].sum() / 1000

            if avg_perf > 85:
                status_class = "status-ok"
                status_text = "OK"
            elif avg_perf > 70:
                status_class = "status-warning"
                status_text = "WARNUNG"
            else:
                status_class = "status-critical"
                status_text = "KRITISCH"

            html_content += f"""
                        <tr>
                            <td><strong>{machine}</strong></td>
                            <td>{avg_perf:.1f}%</td>
                            <td>{avg_temp:.1f}°C</td>
                            <td>{avg_qual:.1f}%</td>
                            <td>{total_energy:.1f} kWh</td>
                            <td class="{status_class}">{status_text}</td>
                        </tr>
            """

        html_content += """
                    </tbody>
                </table>
            </div>

            <div class="footer">
                <p>📊 Bystronic Python Grundkurs - Dashboard-Entwicklung</p>
                <p>🔄 Automatisch generiert mit Python & Matplotlib</p>
            </div>
        </body>
        </html>
        """

        # HTML-Datei speichern
        filename = (
            f"bystronic_dashboard_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        )
        with open(filename, "w", encoding="utf-8") as f:
            f.write(html_content)

        print(f"✅ HTML-Dashboard erstellt: {filename}")
        return filename

    # Alle Export-Formate erstellen
    print("🔄 Starte Export-Prozess...")

    # PDF-Report
    try:
        create_pdf_report()
    except Exception as e:
        print(f"❌ PDF-Export fehlgeschlagen: {e}")

    # Excel-Dashboard
    try:
        create_excel_dashboard()
    except Exception as e:
        print(f"❌ Excel-Export fehlgeschlagen: {e}")

    # HTML-Dashboard
    try:
        create_html_dashboard()
    except Exception as e:
        print(f"❌ HTML-Export fehlgeschlagen: {e}")

    # Zusammenfassung
    print("\n📋 Export-Zusammenfassung:")
    print("📄 PDF-Report: Produktionsanalyse mit Diagrammen")
    print("📊 Excel-Dashboard: Interaktive Tabellen mit KPIs")
    print("🌐 HTML-Dashboard: Web-kompatible Übersicht")

    print("\n💡 Deployment-Optionen:")
    print("📧 E-Mail-Versand: Automatische Berichte via smtplib")
    print("🌐 Web-Server: Flask/Dash für Live-Dashboards")
    print("☁️ Cloud: Upload zu AWS S3/Azure Blob Storage")
    print("📱 Mobile: Responsive HTML für Smartphones")
    print("🖨️ Print: PDF-Optimierung für Ausdrucke")

    # Statistiken für alle Exporte
    total_machines = len(data_gen.machines)
    total_datapoints = len(df_realtime)
    timespan_hours = (
        df_realtime["timestamp"].max() - df_realtime["timestamp"].min()
    ).total_seconds() / 3600

    print("\n📊 Datengrundlage für Exporte:")
    print(f"  Überwachte Maschinen: {total_machines}")
    print(f"  Gesamte Datenpunkte: {total_datapoints:,}")
    print(f"  Zeitspanne: {timespan_hours:.1f} Stunden")
    print(f"  Durchschnittliche Performance: {df_realtime['performance'].mean():.1f}%")
    print(f"  Export-Zeitstempel: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def main() -> None:
    """Hauptfunktion für Dashboard-Entwicklung"""
    print("=" * 70)
    print("BYSTRONIC - DASHBOARD-ENTWICKLUNG")
    print("Übung 4: Professionelle Dashboards für industrielle Anwendungen")
    print("=" * 70)

    # Übungsauswahl
    print("\nWählen Sie eine Aufgabe aus:")
    print("1️⃣  Professionelles Matplotlib-Dashboard")
    print("2️⃣  Interaktives Plotly-Dashboard")
    print("3️⃣  Real-time Dashboard mit Live-Updates")
    print("4️⃣  Dashboard-Export und -Deployment")
    print("0️⃣  Alle Aufgaben nacheinander ausführen")

    try:
        choice = input("\nIhre Wahl (0-4): ").strip()

        if choice == "1":
            aufgabe_1_matplotlib_dashboard()
        elif choice == "2":
            aufgabe_2_plotly_interaktives_dashboard()
        elif choice == "3":
            aufgabe_3_realtime_dashboard()
        elif choice == "4":
            aufgabe_4_dashboard_export()
        elif choice == "0":
            print("\n🎯 Alle Aufgaben werden nacheinander ausgeführt...")
            print("\nSTART: Aufgabe 1")
            aufgabe_1_matplotlib_dashboard()

            input("\nDrücken Sie Enter für Aufgabe 2...")
            print("\nSTART: Aufgabe 2")
            aufgabe_2_plotly_interaktives_dashboard()

            input("\nDrücken Sie Enter für Aufgabe 3...")
            print("\nSTART: Aufgabe 3")
            aufgabe_3_realtime_dashboard()

            input("\nDrücken Sie Enter für Aufgabe 4...")
            print("\nSTART: Aufgabe 4")
            aufgabe_4_dashboard_export()
        else:
            print("❌ Ungültige Eingabe. Programm wird beendet.")
            return

    except KeyboardInterrupt:
        print("\n\n⏸️ Programm durch Benutzer unterbrochen.")
        return
    except EOFError:
        print("\n\n🤖 Automatischer Modus: Alle Aufgaben werden ausgeführt...")
        aufgabe_1_matplotlib_dashboard()
        aufgabe_2_plotly_interaktives_dashboard()
        aufgabe_3_realtime_dashboard()
        aufgabe_4_dashboard_export()

    print(f"\n{'=' * 70}")
    print("✅ Dashboard-Entwicklung erfolgreich abgeschlossen!")
    print("📊 Professionelle Matplotlib-Dashboards entwickelt")
    print("🌐 Interaktive Plotly-Dashboards mit Web-Export")
    print("🔴 Real-time Monitoring mit Live-Updates implementiert")
    print("📤 Multi-Format Export (PDF, Excel, HTML) realisiert")
    print("🏭 Industrielle Anwendungsfälle für Bystronic abgedeckt")

    print("\n📚 Weiterführende Ressourcen:")
    print("• Matplotlib Dashboards: https://matplotlib.org/stable/gallery/index.html")
    print("• Plotly Dash: https://dash.plotly.com/")
    print("• Streamlit: https://streamlit.io/")
    print("• Panel (HoloViz): https://panel.holoviz.org/")
    print("• Bokeh: https://docs.bokeh.org/en/latest/")


if __name__ == "__main__":
    main()
