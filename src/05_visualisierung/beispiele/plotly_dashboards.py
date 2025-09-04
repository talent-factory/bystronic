#!/usr/bin/env python3
"""
Plotly Dashboards - Moderne Web-Visualisierungen

Dieses Skript demonstriert die Erstellung interaktiver Web-Visualisierungen
mit Plotly für moderne Dashboard-Anwendungen bei Bystronic.

Autor: Python Grundkurs Bystronic
"""

import warnings
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.subplots import make_subplots

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")


def main() -> None:
    """Hauptfunktion für Plotly-Dashboard-Demonstrationen"""
    print("=" * 70)
    print("BYSTRONIC - PLOTLY DASHBOARDS")
    print("=" * 70)

    # 1. Interaktive 3D-Visualisierungen
    print("\n1️⃣ Interaktive 3D-Plots")
    print("-" * 40)

    demo_3d_interaktiv()

    # 2. Real-time Dashboard
    print("\n2️⃣ Real-time Dashboard")
    print("-" * 40)

    demo_realtime_dashboard()

    # 3. Statistische Interaktivität
    print("\n3️⃣ Statistische Plots mit Widgets")
    print("-" * 40)

    demo_statistische_plots()

    # 4. Geo-Visualisierungen
    print("\n4️⃣ Geo-Daten und Karten")
    print("-" * 40)

    demo_geo_visualisierung()

    # 5. Animationen und Zeitreihen
    print("\n5️⃣ Animierte Visualisierungen")
    print("-" * 40)

    demo_animationen()

    print(f"\n{'=' * 70}")
    print("✅ Plotly-Dashboard-Beispiele erfolgreich erstellt!")
    print("🌐 Interaktive Web-Visualisierungen für moderne Dashboards")
    print("🚀 Skalierbare und responsive Plot-Komponenten")


def demo_3d_interaktiv() -> None:
    """Demonstriert interaktive 3D-Visualisierungen"""
    # 3D-Scatter mit Maschinendaten
    np.random.seed(42)
    n_points = 200

    temperatur = np.random.normal(75, 10, n_points)
    druck = np.random.normal(50, 8, n_points)
    geschwindigkeit = np.random.normal(100, 15, n_points)
    qualitaet = (
        100
        - 0.1 * (temperatur - 75) ** 2
        - 0.05 * (druck - 50) ** 2
        - 0.02 * (geschwindigkeit - 100) ** 2
        + np.random.normal(0, 2, n_points)
    )
    qualitaet = np.clip(qualitaet, 80, 100)

    # Status basierend auf Qualität
    status = [
        "Exzellent" if q >= 95 else "Gut" if q >= 90 else "Akzeptabel"
        for q in qualitaet
    ]

    fig = go.Figure(
        data=go.Scatter3d(
            x=temperatur,
            y=druck,
            z=geschwindigkeit,
            mode="markers",
            marker={
                "size": 8,
                "color": qualitaet,
                "colorscale": "Viridis",
                "colorbar": {"title": "Qualität (%)"},
                "opacity": 0.8,
            },
            text=[
                f"T: {t:.1f}°C<br>P: {p:.1f} bar<br>v: {v:.1f} mm/min<br>Q: {q:.1f}%<br>Status: {s}"
                for t, p, v, q, s in zip(
                    temperatur, druck, geschwindigkeit, qualitaet, status, strict=False
                )
            ],
            hovertemplate="%{text}<extra></extra>",
        )
    )

    fig.update_layout(
        title={"text": "3D Prozessparameter-Analyse", "x": 0.5, "font": {"size": 16}},
        scene={
            "xaxis_title": "Temperatur (°C)",
            "yaxis_title": "Druck (bar)",
            "zaxis_title": "Geschwindigkeit (mm/min)",
            "camera": {"eye": {"x": 1.2, "y": 1.2, "z": 1.2}},
        },
        width=800,
        height=600,
    )

    pyo.plot(fig, filename="3d_prozessparameter.html", auto_open=False)
    print("📊 3D-Prozessparameter-Analyse erstellt (3d_prozessparameter.html)")
    print(f"   Datenpunkte: {n_points}")
    print(f"   Durchschnittsqualität: {np.mean(qualitaet):.1f}%")

    # 3D-Surface für Funktionsanalyse
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2)) * np.exp(-0.1 * (X**2 + Y**2))

    fig_surface = go.Figure(
        data=go.Surface(
            z=Z,
            x=x,
            y=y,
            colorscale="Plasma",
            showscale=True,
            colorbar={"title": "Amplitude"},
        )
    )

    fig_surface.update_layout(
        title="3D-Surface: Schwingungsanalyse",
        scene={
            "xaxis_title": "X-Position (mm)",
            "yaxis_title": "Y-Position (mm)",
            "zaxis_title": "Amplitude",
            "aspectmode": "cube",
        },
        width=800,
        height=600,
    )

    pyo.plot(fig_surface, filename="3d_surface_analyse.html", auto_open=False)
    print("🌊 3D-Surface-Analyse erstellt (3d_surface_analyse.html)")


def demo_realtime_dashboard() -> None:
    """Erstellt ein Dashboard mit mehreren Subplots"""
    # Simulierte Echtzeitdaten
    timestamps = pd.date_range(
        start=datetime.now() - timedelta(hours=24), end=datetime.now(), freq="H"
    )

    # Maschinendaten generieren
    np.random.seed(42)
    base_production = 1000
    production_data = (
        base_production
        + 200 * np.sin(np.arange(len(timestamps)) / 4)
        + np.random.normal(0, 50, len(timestamps))
    )

    temperature_data = (
        75
        + 10 * np.sin(np.arange(len(timestamps)) / 6)
        + np.random.normal(0, 3, len(timestamps))
    )

    efficiency_data = (
        85
        + 10 * np.sin(np.arange(len(timestamps)) / 8)
        + np.random.normal(0, 4, len(timestamps))
    )
    efficiency_data = np.clip(efficiency_data, 60, 100)

    # Dashboard mit Subplots
    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Stündliche Produktion",
            "Temperaturverlauf",
            "Effizienz-Trend",
            "Verteilung Heute",
        ),
        specs=[
            [{"secondary_y": False}, {"secondary_y": False}],
            [{"secondary_y": False}, {"type": "histogram"}],
        ],
    )

    # Produktionslinie
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=production_data,
            mode="lines+markers",
            name="Produktion",
            line={"color": "#1f77b4", "width": 3},
            marker={"size": 6},
            hovertemplate="Zeit: %{x}<br>Stück: %{y:.0f}<extra></extra>",
        ),
        row=1,
        col=1,
    )

    # Temperaturverlauf
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=temperature_data,
            mode="lines",
            name="Temperatur",
            line={"color": "#ff7f0e", "width": 2},
            fill="tonexty",
            hovertemplate="Zeit: %{x}<br>Temp: %{y:.1f}°C<extra></extra>",
        ),
        row=1,
        col=2,
    )

    # Effizienz mit Farbkodierung
    colors = [
        "red" if e < 70 else "orange" if e < 80 else "green" for e in efficiency_data
    ]
    fig.add_trace(
        go.Scatter(
            x=timestamps,
            y=efficiency_data,
            mode="markers+lines",
            name="Effizienz",
            marker={"color": colors, "size": 8},
            line={"color": "gray", "width": 1},
            hovertemplate="Zeit: %{x}<br>Effizienz: %{y:.1f}%<extra></extra>",
        ),
        row=2,
        col=1,
    )

    # Verteilungshistogramm (nur aktuelle Daten)
    current_data = efficiency_data[-6:]  # Letzte 6 Stunden
    fig.add_trace(
        go.Histogram(
            x=current_data,
            nbinsx=10,
            name="Effizienz Heute",
            marker={"color": "skyblue", "opacity": 0.7},
            hovertemplate="Effizienz: %{x:.1f}%<br>Häufigkeit: %{y}<extra></extra>",
        ),
        row=2,
        col=2,
    )

    # Layout anpassen
    fig.update_layout(
        title={
            "text": "Bystronic Produktions-Dashboard (Live)",
            "x": 0.5,
            "font": {"size": 18},
        },
        showlegend=False,
        height=700,
        width=1200,
        plot_bgcolor="white",
    )

    # Achsen-Labels
    fig.update_xaxes(title_text="Zeit", row=1, col=1)
    fig.update_yaxes(title_text="Stückzahl", row=1, col=1)
    fig.update_xaxes(title_text="Zeit", row=1, col=2)
    fig.update_yaxes(title_text="Temperatur (°C)", row=1, col=2)
    fig.update_xaxes(title_text="Zeit", row=2, col=1)
    fig.update_yaxes(title_text="Effizienz (%)", row=2, col=1)
    fig.update_xaxes(title_text="Effizienz (%)", row=2, col=2)
    fig.update_yaxes(title_text="Häufigkeit", row=2, col=2)

    pyo.plot(fig, filename="dashboard_realtime.html", auto_open=False)
    print("📊 Real-time Dashboard erstellt (dashboard_realtime.html)")
    print("   Zeitraum: 24 Stunden")
    print(f"   Durchschnittsproduktion: {np.mean(production_data):.0f} Stück/h")
    print(f"   Durchschnittstemperatur: {np.mean(temperature_data):.1f}°C")
    print(f"   Durchschnittseffizienz: {np.mean(efficiency_data):.1f}%")


def demo_statistische_plots() -> None:
    """Demonstriert interaktive statistische Visualisierungen"""
    # Datensatz mit verschiedenen Maschinen
    machines = ["Laser A", "Laser B", "Presse C", "Biege D", "Stanz E"]

    # Performance-Daten für jede Maschine
    np.random.seed(42)
    data_dict = {}

    for i, machine in enumerate(machines):
        # Verschiedene Verteilungen für unterschiedliche Maschinen
        if "Laser" in machine:
            base_performance = 85 + i * 3
            data = np.random.normal(base_performance, 8, 100)
        elif "Presse" in machine:
            base_performance = 78 + i * 2
            data = np.random.exponential(base_performance / 2, 100)
        else:
            base_performance = 90 + i * 2
            data = np.random.gamma(2, base_performance / 2, 100)

        data = np.clip(data, 60, 100)
        data_dict[machine] = data

    # DataFrame erstellen
    pd.DataFrame(
        [
            {"Maschine": machine, "Performance": value}
            for machine, values in data_dict.items()
            for value in values
        ]
    )

    # Box Plot mit Violinen
    fig_box = go.Figure()

    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"]

    for i, machine in enumerate(machines):
        data = data_dict[machine]
        fig_box.add_trace(
            go.Box(
                y=data,
                name=machine,
                boxpoints="outliers",
                marker_color=colors[i],
                line={"width": 2},
                fillcolor=colors[i],
                opacity=0.7,
                hovertemplate=f"Maschine: {machine}<br>Performance: %{{y:.1f}}%<extra></extra>",
            )
        )

    fig_box.update_layout(
        title="Performance-Verteilung nach Maschinen",
        yaxis_title="Performance (%)",
        xaxis_title="Maschine",
        showlegend=False,
        width=800,
        height=500,
    )

    pyo.plot(fig_box, filename="boxplot_maschinen.html", auto_open=False)

    # Korrelationsmatrix als Heatmap
    correlation_data = np.random.rand(5, 5)
    correlation_data = (correlation_data + correlation_data.T) / 2  # Symmetrisch machen
    np.fill_diagonal(correlation_data, 1)  # Diagonale = 1

    fig_heatmap = go.Figure(
        data=go.Heatmap(
            z=correlation_data,
            x=machines,
            y=machines,
            colorscale="RdBu",
            zmid=0,
            colorbar={"title": "Korrelation"},
            hoverongaps=False,
            hovertemplate="%{x} vs %{y}<br>Korrelation: %{z:.2f}<extra></extra>",
        )
    )

    fig_heatmap.update_layout(
        title="Korrelationsmatrix - Maschinenperformance", width=600, height=600
    )

    pyo.plot(fig_heatmap, filename="korrelation_heatmap.html", auto_open=False)
    print("📈 Statistische Plots erstellt:")
    print("   - Box-Plot Analyse (boxplot_maschinen.html)")
    print("   - Korrelations-Heatmap (korrelation_heatmap.html)")

    for machine in machines:
        performance = data_dict[machine]
        print(
            f"   {machine}: Ø {np.mean(performance):.1f}% (σ={np.std(performance):.1f})"
        )


def demo_geo_visualisierung() -> None:
    """Demonstriert Geo-Visualisierungen für Standort-Analysen"""
    # Bystronic Standorte (vereinfacht)
    standorte = {
        "Niederönz (CH)": {
            "lat": 47.2160,
            "lon": 7.8705,
            "mitarbeiter": 850,
            "produktion": 95,
        },
        "Shanghai (CN)": {
            "lat": 31.2304,
            "lon": 121.4737,
            "mitarbeiter": 320,
            "produktion": 87,
        },
        "Hoffman Estates (US)": {
            "lat": 42.0431,
            "lon": -88.1273,
            "mitarbeiter": 180,
            "produktion": 82,
        },
        "Pune (IN)": {
            "lat": 18.5204,
            "lon": 73.8567,
            "mitarbeiter": 95,
            "produktion": 79,
        },
        "Gotha (DE)": {
            "lat": 50.9487,
            "lon": 10.7022,
            "mitarbeiter": 125,
            "produktion": 88,
        },
    }

    # Daten für Plotly vorbereiten
    lats = [info["lat"] for info in standorte.values()]
    lons = [info["lon"] for info in standorte.values()]
    namen = list(standorte.keys())
    mitarbeiter = [info["mitarbeiter"] for info in standorte.values()]
    produktion = [info["produktion"] for info in standorte.values()]

    fig_geo = go.Figure()

    fig_geo.add_trace(
        go.Scattergeo(
            lon=lons,
            lat=lats,
            text=namen,
            mode="markers+text",
            textposition="top center",
            marker={
                "size": [m / 10 for m in mitarbeiter],  # Größe nach Mitarbeiterzahl
                "color": produktion,
                "colorscale": "Viridis",
                "sizemode": "area",
                "sizemin": 8,
                "colorbar": {"title": "Produktionsindex"},
                "line": {"width": 2, "color": "white"},
            },
            hovertemplate="<b>%{text}</b><br>"
            + "Mitarbeiter: %{customdata[0]}<br>"
            + "Produktionsindex: %{customdata[1]}%<extra></extra>",
            customdata=list(zip(mitarbeiter, produktion, strict=False)),
        )
    )

    fig_geo.update_layout(
        title={"text": "Bystronic Standorte Weltweit", "x": 0.5},
        geo={
            "showland": True,
            "landcolor": "rgb(243, 243, 243)",
            "coastlinecolor": "rgb(204, 204, 204)",
            "projection_type": "natural earth",
        },
        width=1000,
        height=600,
    )

    pyo.plot(fig_geo, filename="standorte_weltweit.html", auto_open=False)
    print("🌍 Geo-Visualisierung erstellt (standorte_weltweit.html)")
    print(f"   Standorte: {len(standorte)}")
    print(f"   Gesamtmitarbeiter: {sum(mitarbeiter)}")
    print(f"   Durchschn. Produktionsindex: {np.mean(produktion):.1f}%")


def demo_animationen() -> None:
    """Demonstriert animierte Visualisierungen"""
    # Zeitreihen-Animation für Produktionsentwicklung
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

    maschinen = ["Laser A", "Laser B", "Presse C", "Biege D"]
    jahre = ["2022", "2023", "2024"]

    # Daten für Animation generieren
    np.random.seed(42)
    frames = []

    for jahr in jahre:
        jahr_data = []
        for maschine in maschinen:
            # Saisonaler Trend simulieren
            base_values = 1000 + 200 * np.sin(np.arange(12) / 12 * 2 * np.pi)

            # Jährliches Wachstum
            growth_factor = 1 + (int(jahr) - 2022) * 0.15

            # Maschinentypische Anpassung
            if "Laser" in maschine:
                machine_factor = 1.2
            elif "Presse" in maschine:
                machine_factor = 0.9
            else:
                machine_factor = 1.0

            values = base_values * growth_factor * machine_factor
            values += np.random.normal(0, 50, 12)  # Rauschen hinzufügen

            jahr_data.extend(
                [
                    {
                        "Monat": monat,
                        "Maschine": maschine,
                        "Produktion": wert,
                        "Jahr": jahr,
                    }
                    for monat, wert in zip(monate, values, strict=False)
                ]
            )

        frames.append(jahr_data)

    # Animationsdaten vorbereiten
    all_data = []
    for frame_data in frames:
        all_data.extend(frame_data)

    df_anim = pd.DataFrame(all_data)

    # Animierte Balkendiagramm
    fig_anim = px.bar(
        df_anim,
        x="Monat",
        y="Produktion",
        color="Maschine",
        animation_frame="Jahr",
        animation_group="Maschine",
        title="Produktionsentwicklung 2022-2024",
        labels={"Produktion": "Stückzahl", "Monat": "Monat"},
        range_y=[0, df_anim["Produktion"].max() * 1.1],
    )

    fig_anim.update_layout(
        xaxis={"categoryorder": "array", "categoryarray": monate}, width=900, height=600
    )

    # Animation-Einstellungen
    fig_anim.layout.updatemenus[0].buttons[0].args[1]["frame"]["duration"] = 1000
    fig_anim.layout.updatemenus[0].buttons[0].args[1]["transition"]["duration"] = 500

    pyo.plot(fig_anim, filename="produktion_animation.html", auto_open=False)

    # Scatter-Animation für Prozessoptimierung
    n_frames = 20
    scatter_frames = []

    for frame in range(n_frames):
        # Parameter über Zeit variieren
        angle = frame / n_frames * 2 * np.pi
        temp_offset = 10 * np.sin(angle)
        speed_offset = 20 * np.cos(angle)

        temp_data = 75 + temp_offset + np.random.normal(0, 3, 50)
        speed_data = 100 + speed_offset + np.random.normal(0, 10, 50)
        quality_data = 95 - 0.1 * (temp_data - 75) ** 2 - 0.05 * (speed_data - 100) ** 2
        quality_data += np.random.normal(0, 2, 50)
        quality_data = np.clip(quality_data, 80, 100)

        scatter_frames.append(
            go.Frame(
                data=go.Scatter(
                    x=temp_data,
                    y=speed_data,
                    mode="markers",
                    marker={
                        "color": quality_data,
                        "colorscale": "Viridis",
                        "size": 8,
                        "colorbar": {"title": "Qualität (%)"},
                    },
                    text=[f"Q: {q:.1f}%" for q in quality_data],
                    hovertemplate="Temp: %{x:.1f}°C<br>Speed: %{y:.1f}<br>%{text}<extra></extra>",
                ),
                name=f"Frame {frame}",
            )
        )

    fig_scatter = go.Figure(data=scatter_frames[0].data, frames=scatter_frames)

    fig_scatter.update_layout(
        title="Prozessoptimierung - Parameter vs. Qualität",
        xaxis_title="Temperatur (°C)",
        yaxis_title="Geschwindigkeit (mm/min)",
        width=800,
        height=600,
        updatemenus=[
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"duration": 200, "redraw": True},
                                "fromcurrent": True,
                            },
                        ],
                    }
                ],
            }
        ],
    )

    pyo.plot(fig_scatter, filename="prozess_animation.html", auto_open=False)

    print("🎬 Animationen erstellt:")
    print("   - Produktionsentwicklung (produktion_animation.html)")
    print("   - Prozessoptimierung (prozess_animation.html)")
    print(f"   Animation-Dauer: {n_frames} Frames")


if __name__ == "__main__":
    main()
