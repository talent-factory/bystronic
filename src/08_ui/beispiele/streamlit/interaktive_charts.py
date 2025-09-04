#!/usr/bin/env python3
"""
Interaktive Charts mit Streamlit und Plotly
===========================================

Erweiterte interaktive Visualisierungen für industrielle Daten:
- Dynamische Filterung
- Drill-Down Funktionalität
- Animation und Echtzeit-Updates
- Custom Widgets
- Advanced Plotly Features

Starten mit: streamlit run interaktive_charts.py

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import time
from datetime import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

st.set_page_config(page_title="Interaktive Charts", page_icon="📊", layout="wide")


def main():
    st.title("📊 Interaktive Charts und Visualisierungen")
    st.markdown("Erweiterte Plotly-Visualisierungen für industrielle Datenanalyse")

    # Demo-Daten generieren
    @st.cache_data
    def generate_demo_data():
        np.random.seed(42)

        # Zeitreihen-Daten
        timestamps = pd.date_range(start="2024-09-01", periods=168, freq="H")  # 1 Woche
        machines = ["Laser_1", "Laser_2", "Stanze_1", "Biegemaschine"]

        data = []
        for ts in timestamps:
            for machine in machines:
                # Realistische Schwankungen mit Trends
                hour = ts.hour
                day_effect = np.sin(2 * np.pi * ts.dayofyear / 365) * 5
                hour_effect = np.sin(2 * np.pi * hour / 24) * 3

                data.append(
                    {
                        "timestamp": ts,
                        "machine": machine,
                        "temperature": 65
                        + day_effect
                        + hour_effect
                        + np.random.normal(0, 2),
                        "pressure": 8.2 + np.random.normal(0, 0.3),
                        "power": 75 + day_effect * 2 + np.random.normal(0, 5),
                        "efficiency": 85
                        + day_effect
                        + hour_effect
                        + np.random.normal(0, 3),
                        "parts_per_hour": np.random.poisson(250),
                        "quality_score": np.random.beta(9, 1)
                        * 100,  # Konzentriert um 90%
                        "operator": np.random.choice(
                            ["Schmidt", "Mueller", "Weber", "Fischer"]
                        ),
                        "shift": ((hour // 8) % 3) + 1,
                    }
                )

        return pd.DataFrame(data)

    df = generate_demo_data()

    # Sidebar für globale Filter
    st.sidebar.header("🎛️ Globale Filter")

    # Maschinen-Filter
    selected_machines = st.sidebar.multiselect(
        "Maschinen auswählen:", df["machine"].unique(), default=df["machine"].unique()
    )

    # Zeitraum-Filter
    date_range = st.sidebar.date_input(
        "Zeitraum:",
        value=[df["timestamp"].min().date(), df["timestamp"].max().date()],
        min_value=df["timestamp"].min().date(),
        max_value=df["timestamp"].max().date(),
    )

    # Daten filtern
    filtered_df = df[
        (df["machine"].isin(selected_machines))
        & (df["timestamp"].dt.date >= date_range[0])
        & (df["timestamp"].dt.date <= date_range[1])
    ]

    # Tab-Navigation
    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "🎯 Interactive Dashboards",
            "📈 Time Series Analysis",
            "🔍 Drill-Down Analysis",
            "🎬 Animated Charts",
        ]
    )

    with tab1:
        show_interactive_dashboard(filtered_df)

    with tab2:
        show_time_series_analysis(filtered_df)

    with tab3:
        show_drill_down_analysis(filtered_df)

    with tab4:
        show_animated_charts(filtered_df)


def show_interactive_dashboard(df):
    """Interaktives Dashboard mit verknüpften Charts."""
    st.subheader("🎯 Interaktives Produktions-Dashboard")

    # KPI-Metriken
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        avg_temp = df["temperature"].mean()
        st.metric("🌡️ Ø Temperatur", f"{avg_temp:.1f}°C")

    with col2:
        avg_efficiency = df["efficiency"].mean()
        st.metric("⚡ Ø Effizienz", f"{avg_efficiency:.1f}%")

    with col3:
        total_parts = df["parts_per_hour"].sum()
        st.metric("📦 Gesamt Produktion", f"{total_parts:,}")

    with col4:
        avg_quality = df["quality_score"].mean()
        st.metric("✅ Ø Qualität", f"{avg_quality:.1f}%")

    # Hauptcharts
    col_left, col_right = st.columns([2, 1])

    with col_left:
        # Multi-Parameter Zeitreihe
        st.markdown("### 📊 Multi-Parameter Übersicht")

        # Parameter-Auswahl
        parameters = st.multiselect(
            "Parameter anzeigen:",
            ["temperature", "pressure", "power", "efficiency", "quality_score"],
            default=["temperature", "efficiency"],
            key="dashboard_params",
        )

        if parameters:
            # Normalisierte Darstellung für bessere Vergleichbarkeit
            fig_multi = go.Figure()

            colors = px.colors.qualitative.Set1
            for i, param in enumerate(parameters):
                # Daten normalisieren (0-100 Skala)
                normalized_data = (
                    (df[param] - df[param].min())
                    / (df[param].max() - df[param].min())
                    * 100
                )

                fig_multi.add_trace(
                    go.Scatter(
                        x=df["timestamp"],
                        y=normalized_data,
                        name=param.replace("_", " ").title(),
                        line={"color": colors[i % len(colors)]},
                        hovertemplate=f"<b>{param}</b><br>"
                        + "Zeit: %{x}<br>"
                        + f"Normalisiert: %{y:.1f}<br>"
                        + f"Original: {df[param].iloc[0]:.1f}<extra></extra>",
                    )
                )

            fig_multi.update_layout(
                title="Normalisierte Parameter-Verläufe (0-100 Skala)",
                xaxis_title="Zeit",
                yaxis_title="Normalisierte Werte",
                hovermode="x unified",
                height=400,
            )

            st.plotly_chart(fig_multi, use_container_width=True)

    with col_right:
        # Maschinen-Performance Radar Chart
        st.markdown("### 🎯 Maschinen-Performance")

        machine_stats = (
            df.groupby("machine")
            .agg(
                {
                    "temperature": "mean",
                    "pressure": "mean",
                    "power": "mean",
                    "efficiency": "mean",
                    "quality_score": "mean",
                }
            )
            .round(2)
        )

        # Radar Chart erstellen
        fig_radar = go.Figure()

        categories = ["Temperatur", "Druck", "Leistung", "Effizienz", "Qualität"]

        for machine in machine_stats.index:
            values = [
                machine_stats.loc[machine, "temperature"],
                machine_stats.loc[machine, "pressure"]
                * 10,  # Skalierung für bessere Darstellung
                machine_stats.loc[machine, "power"],
                machine_stats.loc[machine, "efficiency"],
                machine_stats.loc[machine, "quality_score"],
            ]

            fig_radar.add_trace(
                go.Scatterpolar(
                    r=values, theta=categories, fill="toself", name=machine, opacity=0.6
                )
            )

        fig_radar.update_layout(
            polar={"radialaxis": {"visible": True, "range": [0, 100]}},
            showlegend=True,
            title="Maschinen-Performance Vergleich",
            height=400,
        )

        st.plotly_chart(fig_radar, use_container_width=True)

    # Korrelations-Heatmap mit Interaktivität
    st.markdown("### 🔥 Parameter-Korrelationen")

    numeric_cols = [
        "temperature",
        "pressure",
        "power",
        "efficiency",
        "parts_per_hour",
        "quality_score",
    ]
    correlation_matrix = df[numeric_cols].corr()

    fig_heatmap = px.imshow(
        correlation_matrix,
        title="Korrelationsmatrix der Produktionsparameter",
        color_continuous_scale="RdBu",
        aspect="auto",
        labels={"color": "Korrelation"},
    )

    fig_heatmap.update_layout(height=400)
    st.plotly_chart(fig_heatmap, use_container_width=True)


def show_time_series_analysis(df):
    """Erweiterte Zeitreihenanalyse."""
    st.subheader("📈 Zeitreihen-Analyse")

    # Parameter-Auswahl
    analysis_param = st.selectbox(
        "Parameter für Analyse:",
        [
            "temperature",
            "pressure",
            "power",
            "efficiency",
            "parts_per_hour",
            "quality_score",
        ],
        key="timeseries_param",
    )

    # Aggregations-Level
    aggregation = st.selectbox(
        "Aggregation:", ["Stündlich", "Täglich", "Schichtweise"], key="timeseries_agg"
    )

    # Daten aggregieren
    if aggregation == "Stündlich":
        df_agg = (
            df.groupby([df["timestamp"].dt.floor("H"), "machine"])[analysis_param]
            .mean()
            .reset_index()
        )
    elif aggregation == "Täglich":
        df_agg = (
            df.groupby([df["timestamp"].dt.date, "machine"])[analysis_param]
            .mean()
            .reset_index()
        )
        df_agg["timestamp"] = pd.to_datetime(df_agg["timestamp"])
    else:  # Schichtweise
        df_agg = df.groupby(["shift", "machine"])[analysis_param].mean().reset_index()

    # Haupt-Zeitreihenchart
    if aggregation != "Schichtweise":
        fig_ts = px.line(
            df_agg,
            x="timestamp",
            y=analysis_param,
            color="machine",
            title=f"{analysis_param.replace('_', ' ').title()} - {aggregation}e Analyse",
        )

        # Trend-Linien hinzufügen
        if st.checkbox("Trend-Linien anzeigen", key="trend_lines"):
            for machine in df_agg["machine"].unique():
                machine_data = df_agg[df_agg["machine"] == machine]

                # Polynomal-Fit
                x_numeric = np.arange(len(machine_data))
                z = np.polyfit(x_numeric, machine_data[analysis_param], 2)
                p = np.poly1d(z)

                fig_ts.add_trace(
                    go.Scatter(
                        x=machine_data["timestamp"],
                        y=p(x_numeric),
                        mode="lines",
                        name=f"{machine} Trend",
                        line={"dash": "dash"},
                        opacity=0.7,
                    )
                )

        fig_ts.update_layout(height=500, hovermode="x unified")
        st.plotly_chart(fig_ts, use_container_width=True)

    else:  # Schichtweise Analyse
        fig_shift = px.bar(
            df_agg,
            x="shift",
            y=analysis_param,
            color="machine",
            title=f"{analysis_param.replace('_', ' ').title()} nach Schicht",
            barmode="group",
        )
        fig_shift.update_layout(height=400)
        st.plotly_chart(fig_shift, use_container_width=True)

    # Statistische Analyse
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 📊 Verteilungsanalyse")

        # Verteilung pro Maschine
        fig_dist = px.violin(
            df,
            x="machine",
            y=analysis_param,
            box=True,
            title=f"Verteilung: {analysis_param.replace('_', ' ').title()}",
        )
        st.plotly_chart(fig_dist, use_container_width=True)

    with col2:
        st.markdown("### 🎯 Control Chart")

        # Einfaches Control Chart
        overall_mean = df[analysis_param].mean()
        overall_std = df[analysis_param].std()

        ucl = overall_mean + 3 * overall_std
        lcl = overall_mean - 3 * overall_std

        # Zeitlich sortierte Daten für Control Chart
        df_sorted = df.sort_values("timestamp").reset_index(drop=True)

        fig_control = go.Figure()

        fig_control.add_trace(
            go.Scatter(
                x=df_sorted.index,
                y=df_sorted[analysis_param],
                mode="lines+markers",
                name="Messwerte",
                marker={"size": 4},
            )
        )

        fig_control.add_hline(
            y=overall_mean,
            line_dash="dash",
            line_color="green",
            annotation_text="Mittelwert",
        )
        fig_control.add_hline(
            y=ucl, line_dash="dash", line_color="red", annotation_text="UCL"
        )
        fig_control.add_hline(
            y=lcl, line_dash="dash", line_color="red", annotation_text="LCL"
        )

        fig_control.update_layout(
            title=f"Control Chart: {analysis_param.replace('_', ' ').title()}",
            xaxis_title="Messung #",
            yaxis_title=analysis_param.replace("_", " ").title(),
        )

        st.plotly_chart(fig_control, use_container_width=True)


def show_drill_down_analysis(df):
    """Drill-Down Analyse mit hierarchischen Daten."""
    st.subheader("🔍 Drill-Down Analyse")

    # Sunburst Chart für hierarchische Datenexploration
    st.markdown("### ☀️ Hierarchische Datenexploration")

    # Daten für Sunburst vorbereiten
    drill_param = st.selectbox(
        "Metrik für Drill-Down:",
        ["parts_per_hour", "efficiency", "quality_score"],
        key="drill_param",
    )

    # Aggregierte Daten erstellen
    sunburst_data = (
        df.groupby(["machine", "operator", "shift"])[drill_param].sum().reset_index()
    )

    fig_sunburst = px.sunburst(
        sunburst_data,
        path=["machine", "operator", "shift"],
        values=drill_param,
        title=f"Drill-Down: {drill_param.replace('_', ' ').title()} nach Maschine → Operator → Schicht",
    )
    fig_sunburst.update_layout(height=500)
    st.plotly_chart(fig_sunburst, use_container_width=True)

    # Interactive Treemap
    st.markdown("### 🗺️ Treemap Analyse")

    fig_treemap = px.treemap(
        sunburst_data,
        path=[px.Constant("Gesamt"), "machine", "operator"],
        values=drill_param,
        title=f"Treemap: {drill_param.replace('_', ' ').title()}",
    )
    fig_treemap.update_layout(height=400)
    st.plotly_chart(fig_treemap, use_container_width=True)

    # Dynamische Filter-Interaktion
    st.markdown("### 🎛️ Dynamische Filter")

    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        selected_machine = st.selectbox(
            "Maschine fokussieren:",
            ["Alle"] + list(df["machine"].unique()),
            key="drill_machine",
        )

    with filter_col2:
        selected_operator = st.selectbox(
            "Operator fokussieren:",
            ["Alle"] + list(df["operator"].unique()),
            key="drill_operator",
        )

    with filter_col3:
        selected_shift = st.selectbox(
            "Schicht fokussieren:", ["Alle"] + [1, 2, 3], key="drill_shift"
        )

    # Daten entsprechend filtern
    drill_filtered = df.copy()

    if selected_machine != "Alle":
        drill_filtered = drill_filtered[drill_filtered["machine"] == selected_machine]

    if selected_operator != "Alle":
        drill_filtered = drill_filtered[drill_filtered["operator"] == selected_operator]

    if selected_shift != "Alle":
        drill_filtered = drill_filtered[drill_filtered["shift"] == selected_shift]

    # Detail-Charts basierend auf Filtern
    detail_col1, detail_col2 = st.columns(2)

    with detail_col1:
        if len(drill_filtered) > 0:
            fig_detail_scatter = px.scatter(
                drill_filtered,
                x="efficiency",
                y="quality_score",
                size="parts_per_hour",
                color="temperature",
                hover_data=["machine", "operator", "shift"],
                title="Effizienz vs. Qualität (gefilterte Daten)",
            )
            st.plotly_chart(fig_detail_scatter, use_container_width=True)

    with detail_col2:
        if len(drill_filtered) > 0:
            fig_detail_hist = px.histogram(
                drill_filtered,
                x=drill_param,
                color="machine",
                title=f"Verteilung {drill_param} (gefilterte Daten)",
            )
            st.plotly_chart(fig_detail_hist, use_container_width=True)

    # Detaillierte Statistiken
    if len(drill_filtered) > 0:
        st.markdown("### 📋 Detail-Statistiken")

        detail_stats = (
            drill_filtered.groupby(["machine", "operator"])
            .agg(
                {
                    "temperature": ["mean", "std"],
                    "efficiency": ["mean", "std"],
                    "quality_score": ["mean", "std"],
                    "parts_per_hour": ["sum", "mean"],
                }
            )
            .round(2)
        )

        # Flatten column names
        detail_stats.columns = [
            "_".join(col).strip() for col in detail_stats.columns.values
        ]

        st.dataframe(detail_stats, use_container_width=True)
    else:
        st.warning("Keine Daten für die gewählten Filter vorhanden.")


def show_animated_charts(df):
    """Animierte Charts und Echtzeit-Simulationen."""
    st.subheader("🎬 Animierte Charts")

    # Animierte Zeitreihe
    st.markdown("### 🎭 Animierte Zeitreihen-Entwicklung")

    animation_param = st.selectbox(
        "Parameter für Animation:",
        ["temperature", "efficiency", "quality_score"],
        key="animation_param",
    )

    # Button zum Starten der Animation
    if st.button("🎬 Animation starten", key="start_animation"):
        # Tagweise Animation
        daily_data = (
            df.groupby([df["timestamp"].dt.date, "machine"])[animation_param]
            .mean()
            .reset_index()
        )
        daily_data["timestamp"] = pd.to_datetime(daily_data["timestamp"])

        fig_animated = px.line(
            daily_data,
            x="timestamp",
            y=animation_param,
            color="machine",
            title=f"Animierte Entwicklung: {animation_param.replace('_', ' ').title()}",
            animation_frame="timestamp",
            range_y=[
                daily_data[animation_param].min() * 0.9,
                daily_data[animation_param].max() * 1.1,
            ],
        )

        fig_animated.update_layout(height=500)
        st.plotly_chart(fig_animated, use_container_width=True)

    # Racing Bar Chart
    st.markdown("### 🏁 Racing Bar Chart")

    if st.button("🏁 Racing Bars starten", key="start_racing"):
        # Stündliche Produktion für Racing Chart
        hourly_production = (
            df.groupby([df["timestamp"].dt.floor("H"), "machine"])["parts_per_hour"]
            .sum()
            .reset_index()
        )
        hourly_production = hourly_production.sort_values("timestamp")

        # Kumulativ für Racing Effect
        hourly_production["cumulative"] = hourly_production.groupby("machine")[
            "parts_per_hour"
        ].cumsum()

        fig_racing = px.bar(
            hourly_production,
            x="cumulative",
            y="machine",
            animation_frame="timestamp",
            orientation="h",
            title="Kumulierte Produktion - Racing Chart",
        )

        fig_racing.update_layout(height=400)
        st.plotly_chart(fig_racing, use_container_width=True)

    # Echtzeit-Simulation
    st.markdown("### ⚡ Echtzeit-Simulation")

    simulate_realtime = st.checkbox(
        "Echtzeit-Simulation aktivieren", key="realtime_sim"
    )

    if simulate_realtime:
        # Placeholder für Live-Updates
        chart_placeholder = st.empty()
        metrics_placeholder = st.empty()

        # Simulation Loop
        for i in range(20):  # 20 Updates
            # Neue "Live" Daten generieren
            current_time = datetime.now()

            live_data = []
            for machine in df["machine"].unique():
                live_data.append(
                    {
                        "timestamp": current_time,
                        "machine": machine,
                        "temperature": 65 + np.random.normal(0, 3),
                        "efficiency": 85 + np.random.normal(0, 5),
                        "parts_per_hour": np.random.poisson(250),
                    }
                )

            live_df = pd.DataFrame(live_data)

            # Aktuelle Metriken
            with metrics_placeholder.container():
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    st.metric(
                        "🌡️ Ø Temperatur", f"{live_df['temperature'].mean():.1f}°C"
                    )

                with col2:
                    st.metric("⚡ Ø Effizienz", f"{live_df['efficiency'].mean():.1f}%")

                with col3:
                    st.metric("📦 Gesamt/h", f"{live_df['parts_per_hour'].sum():,}")

                with col4:
                    st.metric("🕐 Update", f"#{i + 1}")

            # Live-Chart
            with chart_placeholder.container():
                fig_live = px.bar(
                    live_df,
                    x="machine",
                    y="efficiency",
                    title=f"Live Effizienz - Update #{i + 1}",
                    color="temperature",
                    color_continuous_scale="RdYlBu_r",
                )
                fig_live.update_layout(height=400)
                st.plotly_chart(fig_live, use_container_width=True)

            # Warten vor nächstem Update
            time.sleep(1)

        st.success("✅ Echtzeit-Simulation abgeschlossen!")

    # 3D Scatter Animation
    st.markdown("### 🌐 3D Animation")

    if st.button("🌐 3D Animation starten", key="start_3d"):
        # 3D Scatter mit Animation über Zeit
        df_3d = df.sample(200)  # Sample für bessere Performance

        fig_3d = px.scatter_3d(
            df_3d,
            x="temperature",
            y="efficiency",
            z="quality_score",
            color="machine",
            size="parts_per_hour",
            animation_frame=df_3d["timestamp"].dt.hour,
            title="3D Parameter-Raum Animation",
        )

        fig_3d.update_layout(height=600)
        st.plotly_chart(fig_3d, use_container_width=True)


if __name__ == "__main__":
    main()
