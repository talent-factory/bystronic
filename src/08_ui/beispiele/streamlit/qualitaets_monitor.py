#!/usr/bin/env python3
"""
Qualitäts-Monitor mit Streamlit
===============================

Echtzeit-Qualitätskontrolle und -überwachung für Bystronic-Maschinen:
- SPC (Statistical Process Control)
- Qualitätsmetriken und Trends
- Ausschuss-Tracking
- Prüfprotokoll-Management
- Korrelationsanalysen

Starten mit: streamlit run qualitaets_monitor.py

Autor: Python Grundkurs für Bystronic-Entwickler
"""

from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

# Seitenkonfiguration
st.set_page_config(
    page_title="Bystronic Qualitäts-Monitor", page_icon="🔍", layout="wide"
)


def main():
    st.title("🔍 Bystronic Qualitäts-Monitor")

    # Beispieldaten generieren
    @st.cache_data(ttl=30)
    def generate_quality_data():
        np.random.seed(42)
        timestamps = pd.date_range(
            start=datetime.now() - timedelta(hours=24), end=datetime.now(), freq="5min"
        )

        data = []
        for ts in timestamps:
            for part_id in range(1, 6):
                data.append(
                    {
                        "timestamp": ts,
                        "part_id": f"P{part_id:03d}",
                        "dimension_x": np.random.normal(100.0, 0.15),
                        "dimension_y": np.random.normal(50.0, 0.08),
                        "surface_roughness": np.random.normal(1.6, 0.3),
                        "hardness": np.random.normal(55, 2),
                        "pass_fail": np.random.choice(["Pass", "Fail"], p=[0.97, 0.03]),
                        "inspector": np.random.choice(["Schmidt", "Weber", "Mueller"]),
                        "machine": np.random.choice(["Laser 1", "Laser 2", "Stanze 1"]),
                    }
                )

        return pd.DataFrame(data)

    df = generate_quality_data()

    # Sidebar
    st.sidebar.header("🎛️ Filter-Optionen")

    selected_machines = st.sidebar.multiselect(
        "Maschinen auswählen:", df["machine"].unique(), default=df["machine"].unique()
    )

    st.sidebar.selectbox(
        "Zeitraum:", ["Letzte 4 Stunden", "Letzten 8 Stunden", "Letzten 24 Stunden"]
    )

    # Daten filtern
    filtered_df = df[df["machine"].isin(selected_machines)]

    # Hauptinhalt
    tab1, tab2, tab3, tab4 = st.tabs(
        ["📊 Übersicht", "📈 SPC Charts", "🔍 Detailanalyse", "📋 Prüfprotokoll"]
    )

    with tab1:
        show_quality_overview(filtered_df)

    with tab2:
        show_spc_charts(filtered_df)

    with tab3:
        show_detailed_analysis(filtered_df)

    with tab4:
        show_inspection_log(filtered_df)


def show_quality_overview(df):
    """Zeigt Qualitätsübersicht."""
    st.subheader("📊 Qualitätsübersicht")

    # KPIs
    col1, col2, col3, col4 = st.columns(4)

    total_parts = len(df)
    passed_parts = len(df[df["pass_fail"] == "Pass"])
    pass_rate = (passed_parts / total_parts * 100) if total_parts > 0 else 0

    with col1:
        st.metric("🔢 Geprüfte Teile", total_parts)

    with col2:
        st.metric("✅ Gutteile", passed_parts, f"{pass_rate:.1f}%")

    with col3:
        failed_parts = total_parts - passed_parts
        st.metric("❌ Ausschuss", failed_parts, f"{100 - pass_rate:.1f}%")

    with col4:
        avg_roughness = df["surface_roughness"].mean()
        st.metric("🏁 Ø Oberflächengüte", f"{avg_roughness:.2f} μm")

    # Qualitätstrend
    st.subheader("📈 Qualitätstrend")

    # Stündliche Auswertung
    hourly_quality = (
        df.groupby(df["timestamp"].dt.floor("H"))
        .agg(
            {
                "pass_fail": lambda x: (x == "Pass").mean() * 100,
                "dimension_x": "mean",
                "dimension_y": "mean",
                "surface_roughness": "mean",
            }
        )
        .reset_index()
    )

    hourly_quality = hourly_quality.rename(columns={"pass_fail": "pass_rate"})

    fig_trend = px.line(
        hourly_quality,
        x="timestamp",
        y="pass_rate",
        title="Gutteile-Rate über Zeit",
        labels={"pass_rate": "Gutteile-Rate [%]"},
    )
    fig_trend.add_hline(
        y=95, line_dash="dash", line_color="red", annotation_text="Zielwert"
    )
    st.plotly_chart(fig_trend, use_container_width=True)

    # Verteilungen
    col1, col2 = st.columns(2)

    with col1:
        fig_dist = px.histogram(
            df,
            x="dimension_x",
            title="Verteilung Maß X",
            labels={"dimension_x": "Maß X [mm]"},
        )
        fig_dist.add_vline(
            x=100.0, line_dash="dash", line_color="green", annotation_text="Sollmaß"
        )
        fig_dist.add_vline(
            x=99.7, line_dash="dot", line_color="red", annotation_text="Untergrenze"
        )
        fig_dist.add_vline(
            x=100.3, line_dash="dot", line_color="red", annotation_text="Obergrenze"
        )
        st.plotly_chart(fig_dist, use_container_width=True)

    with col2:
        fig_scatter = px.scatter(
            df,
            x="dimension_x",
            y="dimension_y",
            color="pass_fail",
            title="Korrelation Maße X/Y",
        )
        st.plotly_chart(fig_scatter, use_container_width=True)


def show_spc_charts(df):
    """Zeigt SPC (Statistical Process Control) Charts."""
    st.subheader("📈 SPC Control Charts")

    # Parameter auswählen
    parameter = st.selectbox(
        "Parameter für SPC:",
        ["dimension_x", "dimension_y", "surface_roughness", "hardness"],
    )

    # Kontrollgrenzen berechnen
    data = df[parameter].values
    mean_val = np.mean(data)
    std_val = np.std(data)

    ucl = mean_val + 3 * std_val  # Upper Control Limit
    lcl = mean_val - 3 * std_val  # Lower Control Limit

    # X-Chart (Individual measurements)
    fig_xbar = go.Figure()
    fig_xbar.add_trace(
        go.Scatter(
            x=df["timestamp"], y=df[parameter], mode="lines+markers", name="Messwerte"
        )
    )
    fig_xbar.add_hline(y=mean_val, line_color="green", annotation_text="Mittelwert")
    fig_xbar.add_hline(y=ucl, line_color="red", line_dash="dash", annotation_text="UCL")
    fig_xbar.add_hline(y=lcl, line_color="red", line_dash="dash", annotation_text="LCL")
    fig_xbar.update_layout(
        title=f"X-Chart für {parameter}", xaxis_title="Zeit", yaxis_title="Wert"
    )
    st.plotly_chart(fig_xbar, use_container_width=True)

    # Moving Range Chart
    moving_range = np.abs(np.diff(data))
    mr_mean = np.mean(moving_range)
    mr_ucl = 3.267 * mr_mean  # Konstante für Moving Range

    fig_mr = go.Figure()
    fig_mr.add_trace(
        go.Scatter(
            x=df["timestamp"][1:],
            y=moving_range,
            mode="lines+markers",
            name="Moving Range",
        )
    )
    fig_mr.add_hline(y=mr_mean, line_color="green", annotation_text="MR Mittelwert")
    fig_mr.add_hline(
        y=mr_ucl, line_color="red", line_dash="dash", annotation_text="UCL"
    )
    fig_mr.update_layout(
        title=f"Moving Range Chart für {parameter}",
        xaxis_title="Zeit",
        yaxis_title="Moving Range",
    )
    st.plotly_chart(fig_mr, use_container_width=True)

    # Prozessfähigkeitsanalyse
    st.subheader("📊 Prozessfähigkeit")

    col1, col2 = st.columns(2)

    with col1:
        # Cp und Cpk Berechnung (vereinfacht)
        if parameter == "dimension_x":
            usl = 100.3  # Upper Specification Limit
            lsl = 99.7  # Lower Specification Limit
        elif parameter == "dimension_y":
            usl = 50.15
            lsl = 49.85
        else:
            usl = mean_val + 2 * std_val
            lsl = mean_val - 2 * std_val

        cp = (usl - lsl) / (6 * std_val)
        cpu = (usl - mean_val) / (3 * std_val)
        cpl = (mean_val - lsl) / (3 * std_val)
        cpk = min(cpu, cpl)

        st.metric("Cp (Prozessfähigkeit)", f"{cp:.2f}")
        st.metric("Cpk (Prozesslage)", f"{cpk:.2f}")

        if cpk >= 1.33:
            st.success("Prozess ist fähig")
        elif cpk >= 1.0:
            st.warning("Prozess grenzwertig")
        else:
            st.error("Prozess nicht fähig")

    with col2:
        # Histogramm mit Spezifikationsgrenzen
        fig_hist = px.histogram(df, x=parameter, title=f"Verteilung {parameter}")
        fig_hist.add_vline(
            x=usl, line_color="red", line_dash="dash", annotation_text="OSG"
        )
        fig_hist.add_vline(
            x=lsl, line_color="red", line_dash="dash", annotation_text="USG"
        )
        fig_hist.add_vline(x=mean_val, line_color="green", annotation_text="Mittelwert")
        st.plotly_chart(fig_hist, use_container_width=True)


def show_detailed_analysis(df):
    """Zeigt detaillierte Qualitätsanalyse."""
    st.subheader("🔍 Detaillierte Qualitätsanalyse")

    # Korrelationsanalyse
    st.markdown("### 🔗 Korrelationsanalyse")

    numeric_cols = ["dimension_x", "dimension_y", "surface_roughness", "hardness"]
    correlation_matrix = df[numeric_cols].corr()

    fig_corr = px.imshow(
        correlation_matrix,
        title="Korrelationsmatrix Qualitätsparameter",
        color_continuous_scale="RdBu",
        aspect="auto",
    )
    st.plotly_chart(fig_corr, use_container_width=True)

    # Pareto-Analyse der Fehlerursachen
    st.markdown("### 📊 Pareto-Analyse")

    # Simulierte Fehlerursachen
    failed_parts = df[df["pass_fail"] == "Fail"]
    if not failed_parts.empty:
        error_causes = {
            "Maßabweichung X": np.sum(
                (failed_parts["dimension_x"] < 99.7)
                | (failed_parts["dimension_x"] > 100.3)
            ),
            "Maßabweichung Y": np.sum(
                (failed_parts["dimension_y"] < 49.85)
                | (failed_parts["dimension_y"] > 50.15)
            ),
            "Oberflächenfehler": np.sum(failed_parts["surface_roughness"] > 2.5),
            "Härteproblem": np.sum(
                (failed_parts["hardness"] < 50) | (failed_parts["hardness"] > 60)
            ),
            "Sonstige": len(failed_parts) // 4,
        }

        pareto_df = pd.DataFrame(
            list(error_causes.items()), columns=["Fehlerursache", "Anzahl"]
        )
        pareto_df = pareto_df.sort_values("Anzahl", ascending=False)
        pareto_df["Kumulativ %"] = (
            pareto_df["Anzahl"].cumsum() / pareto_df["Anzahl"].sum() * 100
        )

        fig_pareto = make_subplots(specs=[[{"secondary_y": True}]])
        fig_pareto.add_trace(
            go.Bar(
                x=pareto_df["Fehlerursache"],
                y=pareto_df["Anzahl"],
                name="Anzahl Fehler",
            )
        )
        fig_pareto.add_trace(
            go.Scatter(
                x=pareto_df["Fehlerursache"],
                y=pareto_df["Kumulativ %"],
                mode="lines+markers",
                name="Kumulativ %",
            ),
            secondary_y=True,
        )
        fig_pareto.update_layout(title="Pareto-Diagramm Fehlerursachen")
        fig_pareto.update_yaxes(title_text="Anzahl", secondary_y=False)
        fig_pareto.update_yaxes(title_text="Kumulativ %", secondary_y=True)
        st.plotly_chart(fig_pareto, use_container_width=True)
    else:
        st.success("Keine Fehlerteile im gewählten Zeitraum!")

    # Maschinen-Vergleich
    st.markdown("### ⚖️ Maschinen-Qualitätsvergleich")

    machine_quality = (
        df.groupby("machine")
        .agg(
            {
                "pass_fail": lambda x: (x == "Pass").mean() * 100,
                "dimension_x": ["mean", "std"],
                "dimension_y": ["mean", "std"],
                "surface_roughness": ["mean", "std"],
            }
        )
        .round(3)
    )

    # Flatten column names
    machine_quality.columns = [
        "_".join(col).strip() for col in machine_quality.columns.values
    ]
    machine_quality = machine_quality.rename(
        columns={"pass_fail_<lambda>": "Gutteile_Rate"}
    )

    st.dataframe(machine_quality, use_container_width=True)

    # Box-Plots für Maschinen-Vergleich
    fig_box = px.box(
        df, x="machine", y="dimension_x", title="Maßhaltigkeit nach Maschine"
    )
    st.plotly_chart(fig_box, use_container_width=True)


def show_inspection_log(df):
    """Zeigt Prüfprotokoll."""
    st.subheader("📋 Prüfprotokoll-Management")

    # Filter für Prüfprotokoll
    col1, col2, col3 = st.columns(3)

    with col1:
        show_failed_only = st.checkbox("Nur Fehlerteile anzeigen")

    with col2:
        selected_inspector = st.selectbox(
            "Prüfer:", ["Alle"] + list(df["inspector"].unique())
        )

    with col3:
        st.date_input("Datum:", datetime.now().date())

    # Daten filtern
    display_df = df.copy()

    if show_failed_only:
        display_df = display_df[display_df["pass_fail"] == "Fail"]

    if selected_inspector != "Alle":
        display_df = display_df[display_df["inspector"] == selected_inspector]

    # Formatierte Anzeige
    display_df["timestamp_formatted"] = display_df["timestamp"].dt.strftime("%H:%M:%S")
    display_df = display_df.round(3)

    # Farb-Coding für Pass/Fail
    def color_pass_fail(val):
        if val == "Pass":
            return "background-color: #d4edda"
        else:
            return "background-color: #f8d7da"

    styled_df = display_df.style.applymap(color_pass_fail, subset=["pass_fail"])

    st.dataframe(styled_df, use_container_width=True)

    # Export-Funktionen
    st.subheader("📤 Export-Funktionen")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("📋 Prüfprotokoll als CSV"):
            csv_data = display_df.to_csv(index=False)
            st.download_button(
                "Download CSV", csv_data, "pruefprotokoll.csv", "text/csv"
            )

    with col2:
        if st.button("📊 Qualitätsbericht generieren"):
            st.success("Qualitätsbericht wurde generiert!")
            st.info(
                "Der Bericht enthält alle relevanten Qualitätsmetriken und SPC-Charts."
            )


if __name__ == "__main__":
    main()
