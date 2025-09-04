#!/usr/bin/env python3
"""
Produktions-Dashboard mit Streamlit
==================================

Ein vollständiges Produktionsüberwachungs-Dashboard für Bystronic-Maschinen:
- Echtzeit-Maschinendaten
- KPI-Überwachung
- Produktionsplanung
- Qualitätskontrolle
- Alarm-Management

Starten mit: streamlit run produktions_dashboard.py

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import time
from datetime import date, datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

# Seitenkonfiguration
st.set_page_config(
    page_title="Bystronic Produktions-Dashboard",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS für industrielles Design
st.markdown(
    """
<style>
    .main-title {
        color: #1f4e79;
        text-align: center;
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
        padding: 1rem;
        background: linear-gradient(90deg, #f0f2f6 0%, #ffffff 50%, #f0f2f6 100%);
        border-radius: 10px;
    }

    .metric-container {
        background-color: #ffffff;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #1f4e79;
        margin-bottom: 1rem;
    }

    .status-running {
        background-color: #d4edda;
        border-left-color: #28a745;
    }

    .status-maintenance {
        background-color: #fff3cd;
        border-left-color: #ffc107;
    }

    .status-error {
        background-color: #f8d7da;
        border-left-color: #dc3545;
    }

    .alert-critical {
        background-color: #f8d7da;
        color: #721c24;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #f5c6cb;
    }

    .alert-warning {
        background-color: #fff3cd;
        color: #856404;
        padding: 1rem;
        border-radius: 5px;
        border: 1px solid #ffeaa7;
    }

    .machine-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin: 0.5rem 0;
    }
</style>
""",
    unsafe_allow_html=True,
)


class ProductionData:
    """Klasse zur Verwaltung der Produktionsdaten."""

    @staticmethod
    @st.cache_data(ttl=60)  # Cache für 1 Minute
    def generate_machine_data():
        """Generiert realistische Maschinendaten."""
        machines = ["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"]

        data = []
        base_time = datetime.now()

        for i in range(100):
            timestamp = base_time - timedelta(minutes=i * 5)

            for machine in machines:
                # Maschinentypspezifische Parameter
                if "Laser" in machine:
                    base_temp = 65
                    base_power = 75
                    base_speed = 2.5
                elif "Stanze" in machine:
                    base_temp = 45
                    base_power = 60
                    base_speed = 1.8
                else:  # Biegemaschine
                    base_temp = 35
                    base_power = 40
                    base_speed = 1.2

                # Realistische Schwankungen
                temp_variation = np.random.normal(0, 3)
                power_variation = np.random.normal(0, 8)
                speed_variation = np.random.normal(0, 0.2)

                # Gelegentliche "Probleme" simulieren
                status = "Normal"
                if np.random.random() < 0.05:  # 5% Chance auf Warnung
                    status = "Warnung"
                    temp_variation += 10
                elif np.random.random() < 0.02:  # 2% Chance auf Fehler
                    status = "Fehler"
                    power_variation -= 20

                data.append(
                    {
                        "timestamp": timestamp,
                        "machine": machine,
                        "temperature": max(20, base_temp + temp_variation),
                        "power_consumption": max(10, base_power + power_variation),
                        "cutting_speed": max(0.5, base_speed + speed_variation),
                        "parts_produced": np.random.poisson(25),
                        "quality_index": np.random.normal(98.5, 1.5),
                        "operator": np.random.choice(
                            ["Schmidt", "Müller", "Weber", "Meyer"]
                        ),
                        "shift": ((timestamp.hour // 8) % 3) + 1,
                        "status": status,
                    }
                )

        return pd.DataFrame(data)

    @staticmethod
    @st.cache_data(ttl=300)  # Cache für 5 Minuten
    def generate_production_orders():
        """Generiert Produktionsaufträge."""
        orders = []

        order_types = [
            "Flansch 150mm",
            "Gehäuse Typ A",
            "Blech 5mm Steel",
            "Halterung verzinkt",
            "Träger L-Profil",
            "Platte 10mm Alu",
        ]

        statuses = ["Geplant", "Läuft", "Wartend", "Abgeschlossen", "Pause"]
        priorities = ["Normal", "Hoch", "Kritisch"]

        for i in range(15):
            start_time = datetime.now() - timedelta(hours=np.random.randint(0, 48))

            orders.append(
                {
                    "order_id": f"PO-{2024}{i + 1:03d}",
                    "part_name": np.random.choice(order_types),
                    "quantity_planned": np.random.randint(50, 500),
                    "quantity_completed": np.random.randint(0, 450),
                    "machine_assigned": np.random.choice(
                        ["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"]
                    ),
                    "operator": np.random.choice(
                        ["Schmidt", "Müller", "Weber", "Meyer"]
                    ),
                    "priority": np.random.choice(priorities, p=[0.6, 0.3, 0.1]),
                    "status": np.random.choice(statuses, p=[0.2, 0.3, 0.1, 0.3, 0.1]),
                    "start_time": start_time,
                    "estimated_end": start_time
                    + timedelta(hours=np.random.randint(2, 12)),
                    "material": np.random.choice(["Stahl", "Aluminium", "Edelstahl"]),
                    "thickness": np.random.choice([3, 5, 8, 10, 12]),
                }
            )

        return pd.DataFrame(orders)

    @staticmethod
    def get_kpi_data(df):
        """Berechnet KPI-Metriken aus den Maschinendaten."""
        current_data = df[df["timestamp"] >= datetime.now() - timedelta(hours=1)]

        if current_data.empty:
            return {
                "overall_efficiency": 0,
                "total_production": 0,
                "avg_quality": 0,
                "active_alarms": 0,
                "avg_temperature": 0,
                "power_consumption": 0,
            }

        return {
            "overall_efficiency": current_data["power_consumption"].mean() / 100 * 100,
            "total_production": current_data["parts_produced"].sum(),
            "avg_quality": current_data["quality_index"].mean(),
            "active_alarms": len(current_data[current_data["status"] != "Normal"]),
            "avg_temperature": current_data["temperature"].mean(),
            "power_consumption": current_data["power_consumption"].sum(),
        }


def main():
    """Hauptfunktion des Dashboards."""

    # Titel
    st.markdown(
        '<div class="main-title">🏭 Bystronic Produktions-Dashboard</div>',
        unsafe_allow_html=True,
    )

    # Daten laden
    machine_df = ProductionData.generate_machine_data()
    orders_df = ProductionData.generate_production_orders()
    kpis = ProductionData.get_kpi_data(machine_df)

    # Sidebar-Navigation
    st.sidebar.title("🎛️ Dashboard-Navigation")

    dashboard_mode = st.sidebar.radio(
        "Bereich auswählen:",
        [
            "📊 Übersicht",
            "🏭 Maschinenstatus",
            "📋 Produktionsaufträge",
            "📈 Analytics",
            "🚨 Alarme",
            "⚙️ Einstellungen",
        ],
    )

    # Datum/Zeit-Filter in Sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("🕐 Zeitfilter")

    st.sidebar.date_input(
        "Datum auswählen:",
        value=datetime.now().date(),
        min_value=date(2024, 1, 1),
        max_value=datetime.now().date(),
    )

    st.sidebar.selectbox(
        "Zeitraum:",
        [
            "Letzte Stunde",
            "Letzten 4 Stunden",
            "Letzten 8 Stunden",
            "Letzten 24 Stunden",
            "Aktuelle Schicht",
        ],
    )

    # Auto-Refresh Option
    st.sidebar.markdown("---")
    auto_refresh = st.sidebar.checkbox("🔄 Auto-Refresh (30s)", value=False)

    if st.sidebar.button("🔄 Manuell aktualisieren"):
        st.cache_data.clear()
        st.rerun()

    # Hauptinhalt basierend auf Navigation
    if dashboard_mode == "📊 Übersicht":
        show_overview(machine_df, orders_df, kpis)
    elif dashboard_mode == "🏭 Maschinenstatus":
        show_machine_status(machine_df)
    elif dashboard_mode == "📋 Produktionsaufträge":
        show_production_orders(orders_df)
    elif dashboard_mode == "📈 Analytics":
        show_analytics(machine_df, orders_df)
    elif dashboard_mode == "🚨 Alarme":
        show_alarms(machine_df)
    elif dashboard_mode == "⚙️ Einstellungen":
        show_settings()

    # Auto-Refresh Implementierung
    if auto_refresh:
        time.sleep(30)
        st.rerun()


def show_overview(machine_df, orders_df, kpis):
    """Zeigt die Dashboard-Übersicht."""

    # KPI-Metriken
    st.subheader("📈 Key Performance Indicators")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        efficiency = kpis["overall_efficiency"]
        delta_eff = np.random.uniform(-2, 5)  # Simulierte Veränderung
        st.metric(
            "🏭 Gesamteffizienz",
            f"{efficiency:.1f}%",
            f"{delta_eff:+.1f}%",
            help="Durchschnittliche Maschinenauslastung",
        )

    with col2:
        production = kpis["total_production"]
        delta_prod = np.random.randint(-10, 25)
        st.metric(
            "📦 Stündliche Produktion",
            f"{production}",
            f"{delta_prod:+d}",
            help="Produzierte Teile in der letzten Stunde",
        )

    with col3:
        quality = kpis["avg_quality"]
        delta_qual = np.random.uniform(-0.5, 0.8)
        st.metric(
            "✅ Qualitätsindex",
            f"{quality:.1f}%",
            f"{delta_qual:+.1f}%",
            help="Durchschnittliche Qualitätsbewertung",
        )

    with col4:
        alarms = kpis["active_alarms"]
        st.metric(
            "🚨 Aktive Alarme", f"{alarms}", help="Anzahl aktiver Warnungen und Fehler"
        )

    # Produktionsstatus-Übersicht
    st.subheader("🏭 Produktionsstatus")

    # Aktuelle Maschinenstatus
    latest_data = machine_df.groupby("machine").last().reset_index()

    status_col1, status_col2 = st.columns(2)

    with status_col1:
        st.markdown("### Maschinenübersicht")

        for _, machine in latest_data.iterrows():
            status_class = ""
            if machine["status"] == "Normal":
                status_class = "status-running"
                status_icon = "✅"
            elif machine["status"] == "Warnung":
                status_class = "status-maintenance"
                status_icon = "⚠️"
            else:
                status_class = "status-error"
                status_icon = "❌"

            st.markdown(
                f"""
            <div class="machine-card {status_class}">
                <h4>{status_icon} {machine["machine"]}</h4>
                <p><strong>Status:</strong> {machine["status"]}</p>
                <p><strong>Temperatur:</strong> {machine["temperature"]:.1f}°C</p>
                <p><strong>Leistung:</strong> {machine["power_consumption"]:.0f}%</p>
                <p><strong>Operator:</strong> {machine["operator"]}</p>
            </div>
            """,
                unsafe_allow_html=True,
            )

    with status_col2:
        st.markdown("### Aktuelle Aufträge")

        running_orders = orders_df[orders_df["status"] == "Läuft"].head(4)

        if not running_orders.empty:
            for _, order in running_orders.iterrows():
                progress = (
                    order["quantity_completed"] / order["quantity_planned"]
                ) * 100

                st.markdown(
                    f"""
                <div class="machine-card">
                    <h4>📋 {order["order_id"]}</h4>
                    <p><strong>Teil:</strong> {order["part_name"]}</p>
                    <p><strong>Fortschritt:</strong> {order["quantity_completed"]}/{order["quantity_planned"]} ({progress:.0f}%)</p>
                    <p><strong>Maschine:</strong> {order["machine_assigned"]}</p>
                </div>
                """,
                    unsafe_allow_html=True,
                )
        else:
            st.info("Keine aktiven Produktionsaufträge")

    # Produktionsdiagramm
    st.subheader("📊 Produktionsverlauf")

    # Stundenweise Aggregation
    hourly_production = (
        machine_df.groupby([machine_df["timestamp"].dt.floor("H"), "machine"])[
            "parts_produced"
        ]
        .sum()
        .reset_index()
    )

    fig_production = px.line(
        hourly_production,
        x="timestamp",
        y="parts_produced",
        color="machine",
        title="Stündliche Produktion nach Maschine",
        labels={"parts_produced": "Produzierte Teile", "timestamp": "Zeit"},
    )
    fig_production.update_layout(height=400)
    st.plotly_chart(fig_production, use_container_width=True)

    # Temperatur- und Leistungsübersicht
    temp_col, power_col = st.columns(2)

    with temp_col:
        st.subheader("🌡️ Temperaturübersicht")

        temp_data = machine_df.groupby("machine")["temperature"].last().reset_index()
        fig_temp = px.bar(
            temp_data,
            x="machine",
            y="temperature",
            title="Aktuelle Temperaturen",
            color="temperature",
            color_continuous_scale="RdYlBu_r",
        )
        fig_temp.add_hline(
            y=70, line_dash="dash", line_color="red", annotation_text="Warnschwelle"
        )
        st.plotly_chart(fig_temp, use_container_width=True)

    with power_col:
        st.subheader("⚡ Leistungsverteilung")

        power_data = (
            machine_df.groupby("machine")["power_consumption"].last().reset_index()
        )
        fig_power = px.pie(
            power_data,
            values="power_consumption",
            names="machine",
            title="Leistungsverteilung",
        )
        st.plotly_chart(fig_power, use_container_width=True)


def show_machine_status(machine_df):
    """Zeigt detaillierte Maschinenstatus."""

    st.header("🏭 Detaillierter Maschinenstatus")

    # Maschinen-Auswahl
    selected_machines = st.multiselect(
        "Maschinen auswählen:",
        machine_df["machine"].unique(),
        default=machine_df["machine"].unique(),
    )

    if not selected_machines:
        st.warning("Bitte wählen Sie mindestens eine Maschine aus.")
        return

    filtered_df = machine_df[machine_df["machine"].isin(selected_machines)]

    # Echtzeit-Status
    st.subheader("⏱️ Echtzeit-Status")

    latest_status = filtered_df.groupby("machine").last().reset_index()

    for _, machine in latest_status.iterrows():
        with st.container():
            col1, col2, col3, col4 = st.columns(4)

            # Machine Name und Status
            status_color = (
                "🟢"
                if machine["status"] == "Normal"
                else "🟡" if machine["status"] == "Warnung" else "🔴"
            )
            st.subheader(f"{status_color} {machine['machine']}")

            with col1:
                st.metric("🌡️ Temperatur", f"{machine['temperature']:.1f}°C")

            with col2:
                st.metric("⚡ Leistung", f"{machine['power_consumption']:.0f}%")

            with col3:
                st.metric("🚀 Geschwindigkeit", f"{machine['cutting_speed']:.1f} m/min")

            with col4:
                st.metric("📦 Teile/h", f"{machine['parts_produced']}")

            # Detailierte Informationen
            with st.expander(f"📊 Details für {machine['machine']}"):
                detail_col1, detail_col2 = st.columns(2)

                with detail_col1:
                    st.write(f"**Operator:** {machine['operator']}")
                    st.write(f"**Schicht:** {machine['shift']}")
                    st.write(f"**Qualitätsindex:** {machine['quality_index']:.2f}%")
                    st.write(
                        f"**Letztes Update:** {machine['timestamp'].strftime('%H:%M:%S')}"
                    )

                with detail_col2:
                    # Verlaufsdiagramm für diese Maschine
                    machine_history = filtered_df[
                        filtered_df["machine"] == machine["machine"]
                    ].tail(20)

                    fig_history = make_subplots(
                        rows=2,
                        cols=2,
                        subplot_titles=(
                            "Temperatur",
                            "Leistung",
                            "Geschwindigkeit",
                            "Qualität",
                        ),
                        vertical_spacing=0.1,
                    )

                    fig_history.add_trace(
                        go.Scatter(
                            x=machine_history["timestamp"],
                            y=machine_history["temperature"],
                            name="Temperatur",
                            line={"color": "red"},
                        ),
                        row=1,
                        col=1,
                    )

                    fig_history.add_trace(
                        go.Scatter(
                            x=machine_history["timestamp"],
                            y=machine_history["power_consumption"],
                            name="Leistung",
                            line={"color": "blue"},
                        ),
                        row=1,
                        col=2,
                    )

                    fig_history.add_trace(
                        go.Scatter(
                            x=machine_history["timestamp"],
                            y=machine_history["cutting_speed"],
                            name="Geschwindigkeit",
                            line={"color": "green"},
                        ),
                        row=2,
                        col=1,
                    )

                    fig_history.add_trace(
                        go.Scatter(
                            x=machine_history["timestamp"],
                            y=machine_history["quality_index"],
                            name="Qualität",
                            line={"color": "orange"},
                        ),
                        row=2,
                        col=2,
                    )

                    fig_history.update_layout(height=400, showlegend=False)
                    st.plotly_chart(fig_history, use_container_width=True)

            st.markdown("---")

    # Vergleichsdiagramme
    st.subheader("📊 Maschinenvergleich")

    comparison_metric = st.selectbox(
        "Vergleichsmetrik:",
        [
            "temperature",
            "power_consumption",
            "cutting_speed",
            "quality_index",
            "parts_produced",
        ],
    )

    metric_labels = {
        "temperature": "Temperatur [°C]",
        "power_consumption": "Leistung [%]",
        "cutting_speed": "Geschwindigkeit [m/min]",
        "quality_index": "Qualitätsindex [%]",
        "parts_produced": "Teile/Zeitraum",
    }

    comparison_df = (
        filtered_df.groupby(["timestamp", "machine"])[comparison_metric]
        .mean()
        .reset_index()
    )

    fig_comparison = px.line(
        comparison_df,
        x="timestamp",
        y=comparison_metric,
        color="machine",
        title=f"Verlauf: {metric_labels[comparison_metric]}",
        labels={comparison_metric: metric_labels[comparison_metric]},
    )
    fig_comparison.update_layout(height=500)
    st.plotly_chart(fig_comparison, use_container_width=True)


def show_production_orders(orders_df):
    """Zeigt Produktionsaufträge."""

    st.header("📋 Produktionsaufträge")

    # Filter-Optionen
    filter_col1, filter_col2, filter_col3 = st.columns(3)

    with filter_col1:
        status_filter = st.multiselect(
            "Status filtern:",
            orders_df["status"].unique(),
            default=orders_df["status"].unique(),
        )

    with filter_col2:
        machine_filter = st.multiselect(
            "Maschine filtern:",
            orders_df["machine_assigned"].unique(),
            default=orders_df["machine_assigned"].unique(),
        )

    with filter_col3:
        priority_filter = st.multiselect(
            "Priorität filtern:",
            orders_df["priority"].unique(),
            default=orders_df["priority"].unique(),
        )

    # Gefilterte Daten
    filtered_orders = orders_df[
        (orders_df["status"].isin(status_filter))
        & (orders_df["machine_assigned"].isin(machine_filter))
        & (orders_df["priority"].isin(priority_filter))
    ]

    # Übersicht der Aufträge nach Status
    st.subheader("📊 Auftragsübersicht")

    status_summary = (
        filtered_orders.groupby("status")
        .agg(
            {
                "order_id": "count",
                "quantity_planned": "sum",
                "quantity_completed": "sum",
            }
        )
        .rename(columns={"order_id": "Anzahl Aufträge"})
        .reset_index()
    )

    status_summary["Completion Rate [%]"] = (
        status_summary["quantity_completed"] / status_summary["quantity_planned"] * 100
    ).fillna(0)

    col1, col2 = st.columns(2)

    with col1:
        fig_status = px.pie(
            status_summary,
            values="Anzahl Aufträge",
            names="status",
            title="Aufträge nach Status",
        )
        st.plotly_chart(fig_status, use_container_width=True)

    with col2:
        fig_completion = px.bar(
            status_summary,
            x="status",
            y="Completion Rate [%]",
            title="Completion Rate nach Status",
        )
        st.plotly_chart(fig_completion, use_container_width=True)

    # Detaillierte Auftragstabelle
    st.subheader("📝 Detaillierte Auftragsliste")

    # Fortschrittsberechnung
    filtered_orders["progress"] = (
        filtered_orders["quantity_completed"]
        / filtered_orders["quantity_planned"]
        * 100
    ).fillna(0)

    # Formatierte Anzeige
    display_orders = filtered_orders.copy()
    display_orders["start_time"] = display_orders["start_time"].dt.strftime(
        "%d.%m.%Y %H:%M"
    )
    display_orders["estimated_end"] = display_orders["estimated_end"].dt.strftime(
        "%d.%m.%Y %H:%M"
    )
    display_orders["progress"] = display_orders["progress"].round(1)

    # Prioritäts-basierte Farben
    def color_priority(val):
        if val == "Kritisch":
            return "background-color: #ffebee"
        elif val == "Hoch":
            return "background-color: #fff3e0"
        else:
            return ""

    # Status-basierte Farben
    def color_status(val):
        colors = {
            "Läuft": "background-color: #e8f5e8",
            "Abgeschlossen": "background-color: #e3f2fd",
            "Wartend": "background-color: #fff8e1",
            "Pause": "background-color: #fafafa",
            "Geplant": "background-color: #f3e5f5",
        }
        return colors.get(val, "")

    styled_orders = display_orders.style.applymap(
        color_priority, subset=["priority"]
    ).applymap(color_status, subset=["status"])

    st.dataframe(styled_orders, use_container_width=True)

    # Produktionsplanung
    st.subheader("📅 Produktionsplanung")

    # Gantt-Chart ähnliche Visualisierung
    planning_orders = filtered_orders[
        filtered_orders["status"].isin(["Geplant", "Läuft", "Wartend"])
    ]

    if not planning_orders.empty:
        fig_gantt = px.timeline(
            planning_orders,
            x_start="start_time",
            x_end="estimated_end",
            y="machine_assigned",
            color="priority",
            title="Produktionsplanung Timeline",
            labels={"machine_assigned": "Maschine"},
        )
        fig_gantt.update_layout(height=400)
        st.plotly_chart(fig_gantt, use_container_width=True)
    else:
        st.info("Keine Aufträge für Planung verfügbar")

    # Neuer Auftrag hinzufügen (Simulation)
    with st.expander("➕ Neuen Auftrag hinzufügen"):
        with st.form("new_order_form"):
            col1, col2, col3 = st.columns(3)

            with col1:
                new_part = st.text_input("Teilename", "Neues Teil")
                new_quantity = st.number_input("Menge", min_value=1, value=100)

            with col2:
                new_machine = st.selectbox(
                    "Maschine", orders_df["machine_assigned"].unique()
                )
                new_priority = st.selectbox("Priorität", ["Normal", "Hoch", "Kritisch"])

            with col3:
                st.selectbox("Material", ["Stahl", "Aluminium", "Edelstahl"])
                st.selectbox("Stärke [mm]", [3, 5, 8, 10, 12])

            submitted = st.form_submit_button("Auftrag erstellen")

            if submitted:
                st.success(f"✅ Auftrag für {new_quantity}x {new_part} wurde erstellt!")
                st.info(f"Zugewiesen an: {new_machine} | Priorität: {new_priority}")


def show_analytics(machine_df, orders_df):
    """Zeigt erweiterte Analytics."""

    st.header("📈 Produktions-Analytics")

    # Zeitraum-Auswahl für Analytics
    analysis_period = st.selectbox(
        "Analysezeitraum:",
        ["Letzten 4 Stunden", "Letzten 24 Stunden", "Letzte Woche", "Letzter Monat"],
    )

    # Entsprechende Datenfilterung
    if analysis_period == "Letzten 4 Stunden":
        cutoff_time = datetime.now() - timedelta(hours=4)
    elif analysis_period == "Letzten 24 Stunden":
        cutoff_time = datetime.now() - timedelta(hours=24)
    elif analysis_period == "Letzte Woche":
        cutoff_time = datetime.now() - timedelta(days=7)
    else:  # Letzter Monat
        cutoff_time = datetime.now() - timedelta(days=30)

    filtered_analytics = machine_df[machine_df["timestamp"] >= cutoff_time]

    # KPI-Entwicklung
    st.subheader("📊 KPI-Entwicklung")

    # Stündliche Aggregation für KPIs
    hourly_kpis = (
        filtered_analytics.groupby(filtered_analytics["timestamp"].dt.floor("H"))
        .agg(
            {
                "parts_produced": "sum",
                "quality_index": "mean",
                "temperature": "mean",
                "power_consumption": "mean",
            }
        )
        .reset_index()
    )

    kpi_col1, kpi_col2 = st.columns(2)

    with kpi_col1:
        fig_production_trend = px.line(
            hourly_kpis, x="timestamp", y="parts_produced", title="Produktionstrend"
        )
        st.plotly_chart(fig_production_trend, use_container_width=True)

        fig_quality_trend = px.line(
            hourly_kpis, x="timestamp", y="quality_index", title="Qualitätstrend"
        )
        fig_quality_trend.add_hline(y=95, line_dash="dash", line_color="red")
        st.plotly_chart(fig_quality_trend, use_container_width=True)

    with kpi_col2:
        fig_temp_trend = px.line(
            hourly_kpis, x="timestamp", y="temperature", title="Temperaturtrend"
        )
        fig_temp_trend.add_hline(y=70, line_dash="dash", line_color="red")
        st.plotly_chart(fig_temp_trend, use_container_width=True)

        fig_power_trend = px.line(
            hourly_kpis, x="timestamp", y="power_consumption", title="Leistungstrend"
        )
        st.plotly_chart(fig_power_trend, use_container_width=True)

    # Korrelationsanalyse
    st.subheader("🔍 Korrelationsanalyse")

    correlation_data = filtered_analytics[
        [
            "temperature",
            "power_consumption",
            "cutting_speed",
            "parts_produced",
            "quality_index",
        ]
    ].corr()

    fig_correlation = px.imshow(
        correlation_data,
        title="Korrelationsmatrix der Produktionsparameter",
        color_continuous_scale="RdBu",
        aspect="auto",
    )
    st.plotly_chart(fig_correlation, use_container_width=True)

    # Maschinenvergleich
    st.subheader("⚖️ Maschinenvergleich")

    machine_comparison = (
        filtered_analytics.groupby("machine")
        .agg(
            {
                "parts_produced": ["sum", "mean"],
                "quality_index": "mean",
                "temperature": "mean",
                "power_consumption": "mean",
                "cutting_speed": "mean",
            }
        )
        .round(2)
    )

    # Flatten column names
    machine_comparison.columns = [
        "Gesamt Produktion",
        "Ø Produktion/Zeitraum",
        "Ø Qualität [%]",
        "Ø Temperatur [°C]",
        "Ø Leistung [%]",
        "Ø Geschwindigkeit [m/min]",
    ]

    st.dataframe(machine_comparison, use_container_width=True)

    # Top-Performer und Problembereiche
    perf_col1, perf_col2 = st.columns(2)

    with perf_col1:
        st.subheader("🏆 Top-Performer")

        # Beste Maschine nach Gesamtproduktion
        top_producer = machine_comparison["Gesamt Produktion"].idxmax()
        top_production = machine_comparison.loc[top_producer, "Gesamt Produktion"]

        st.success(f"**Beste Produktion:** {top_producer}")
        st.write(f"Gesamtproduktion: {top_production}")

        # Beste Qualität
        top_quality_machine = machine_comparison["Ø Qualität [%]"].idxmax()
        top_quality = machine_comparison.loc[top_quality_machine, "Ø Qualität [%]"]

        st.success(f"**Beste Qualität:** {top_quality_machine}")
        st.write(f"Durchschnittliche Qualität: {top_quality:.2f}%")

    with perf_col2:
        st.subheader("⚠️ Problembereiche")

        # Niedrigste Qualität
        low_quality_machine = machine_comparison["Ø Qualität [%]"].idxmin()
        low_quality = machine_comparison.loc[low_quality_machine, "Ø Qualität [%]"]

        st.warning(f"**Niedrigste Qualität:** {low_quality_machine}")
        st.write(f"Durchschnittliche Qualität: {low_quality:.2f}%")

        # Höchste Temperatur
        high_temp_machine = machine_comparison["Ø Temperatur [°C]"].idxmax()
        high_temp = machine_comparison.loc[high_temp_machine, "Ø Temperatur [°C]"]

        if high_temp > 70:
            st.error(f"**Kritische Temperatur:** {high_temp_machine}")
            st.write(f"Durchschnittstemperatur: {high_temp:.1f}°C")
        else:
            st.info("Alle Temperaturen im Normalbereich")


def show_alarms(machine_df):
    """Zeigt Alarm-Management."""

    st.header("🚨 Alarm-Management")

    # Aktuelle Alarme
    current_alarms = machine_df[machine_df["status"] != "Normal"]
    current_alarms = current_alarms.sort_values("timestamp", ascending=False)

    if not current_alarms.empty:
        st.subheader("🔴 Aktive Alarme")

        for _, alarm in current_alarms.head(10).iterrows():
            severity = "🔴 KRITISCH" if alarm["status"] == "Fehler" else "🟡 WARNUNG"

            with st.container():
                alarm_col1, alarm_col2, alarm_col3 = st.columns([2, 2, 1])

                with alarm_col1:
                    st.markdown(f"**{severity}**")
                    st.write(f"**Maschine:** {alarm['machine']}")
                    st.write(
                        f"**Zeit:** {alarm['timestamp'].strftime('%d.%m.%Y %H:%M:%S')}"
                    )

                with alarm_col2:
                    if alarm["status"] == "Fehler":
                        st.write("**Problem:** Kritischer Systemfehler")
                        if alarm["temperature"] > 80:
                            st.write("- Überhitzung erkannt")
                        if alarm["power_consumption"] < 30:
                            st.write("- Niedrige Leistung")
                    else:
                        st.write("**Problem:** Überwachung erforderlich")
                        if alarm["temperature"] > 70:
                            st.write("- Erhöhte Temperatur")
                        if alarm["quality_index"] < 95:
                            st.write("- Qualitätsabweichung")

                with alarm_col3:
                    if st.button(
                        "✅ Quittieren",
                        key=f"ack_{alarm['machine']}_{alarm['timestamp']}",
                    ):
                        st.success("Alarm quittiert!")

                st.markdown("---")
    else:
        st.success("🟢 Keine aktiven Alarme - Alle Systeme normal")

    # Alarm-Statistiken
    st.subheader("📊 Alarm-Statistiken")

    # Alarmverteilung der letzten 24h
    last_24h = machine_df[
        machine_df["timestamp"] >= datetime.now() - timedelta(hours=24)
    ]
    alarm_stats = (
        last_24h.groupby(["machine", "status"]).size().reset_index(name="count")
    )

    if not alarm_stats.empty:
        stat_col1, stat_col2 = st.columns(2)

        with stat_col1:
            fig_alarm_machine = px.bar(
                alarm_stats,
                x="machine",
                y="count",
                color="status",
                title="Alarme nach Maschine (24h)",
            )
            st.plotly_chart(fig_alarm_machine, use_container_width=True)

        with stat_col2:
            alarm_summary = alarm_stats.groupby("status")["count"].sum().reset_index()
            fig_alarm_summary = px.pie(
                alarm_summary,
                values="count",
                names="status",
                title="Alarmverteilung (24h)",
            )
            st.plotly_chart(fig_alarm_summary, use_container_width=True)

    # Alarm-Verlauf
    st.subheader("📈 Alarm-Verlauf")

    # Stündliche Alarmzählung
    hourly_alarms = (
        machine_df.groupby([machine_df["timestamp"].dt.floor("H"), "status"])
        .size()
        .reset_index(name="alarm_count")
    )

    hourly_alarms = hourly_alarms[hourly_alarms["status"] != "Normal"]

    if not hourly_alarms.empty:
        fig_alarm_trend = px.line(
            hourly_alarms,
            x="timestamp",
            y="alarm_count",
            color="status",
            title="Alarm-Häufigkeit über Zeit",
        )
        st.plotly_chart(fig_alarm_trend, use_container_width=True)
    else:
        st.info("Keine Alarme im gewählten Zeitraum")

    # Alarm-Einstellungen
    with st.expander("⚙️ Alarm-Einstellungen"):
        st.subheader("Schwellenwerte konfigurieren")

        config_col1, config_col2 = st.columns(2)

        with config_col1:
            st.number_input(
                "Temperatur Warnung [°C]", value=70, min_value=50, max_value=100
            )
            st.number_input(
                "Temperatur Kritisch [°C]", value=85, min_value=70, max_value=120
            )

            st.number_input(
                "Qualität Warnung [%]",
                value=95.0,
                min_value=90.0,
                max_value=99.0,
                step=0.1,
            )

        with config_col2:
            st.number_input(
                "Leistung Warnung (Min) [%]", value=30, min_value=10, max_value=50
            )

            st.checkbox("E-Mail Benachrichtigungen", value=True)
            st.checkbox("SMS Benachrichtigungen", value=False)

        if st.button("💾 Einstellungen speichern"):
            st.success("Alarm-Einstellungen gespeichert!")


def show_settings():
    """Zeigt System-Einstellungen."""

    st.header("⚙️ Dashboard-Einstellungen")

    # System-Konfiguration
    st.subheader("🖥️ System-Konfiguration")

    config_col1, config_col2 = st.columns(2)

    with config_col1:
        st.markdown("**Anzeige-Einstellungen:**")

        st.selectbox("Theme", ["Hell", "Dunkel", "Auto"])
        st.selectbox("Sprache", ["Deutsch", "English", "Français"])

        st.slider("Auto-Refresh Rate [Sekunden]", 5, 300, 30)

        st.markdown("**Daten-Einstellungen:**")
        st.selectbox("Datenaufbewahrung", ["7 Tage", "30 Tage", "90 Tage", "1 Jahr"])

    with config_col2:
        st.markdown("**Benachrichtigungen:**")

        email_notifications = st.checkbox("E-Mail Benachrichtigungen", value=True)
        if email_notifications:
            st.text_input("E-Mail Adresse", "admin@bystronic.com")

        st.checkbox("Push-Benachrichtigungen", value=True)
        st.checkbox("Ton-Alarme", value=False)

        st.markdown("**Export-Einstellungen:**")
        st.selectbox("Standard Export-Format", ["CSV", "Excel", "JSON", "PDF"])

    # Benutzer-Management
    st.subheader("👥 Benutzer-Management")

    users_data = {
        "Benutzer": ["admin", "operator1", "operator2", "maintenance"],
        "Rolle": ["Administrator", "Operator", "Operator", "Wartung"],
        "Letzter Login": [
            "2024-09-04 08:30",
            "2024-09-04 06:00",
            "2024-09-03 22:15",
            "2024-09-04 09:00",
        ],
        "Status": ["Aktiv", "Aktiv", "Aktiv", "Aktiv"],
    }

    users_df = pd.DataFrame(users_data)
    st.dataframe(users_df, use_container_width=True)

    # Backup und Export
    st.subheader("💾 Backup und Export")

    backup_col1, backup_col2 = st.columns(2)

    with backup_col1:
        st.markdown("**Automatische Backups:**")
        backup_enabled = st.checkbox("Automatische Backups aktiviert", value=True)

        if backup_enabled:
            st.time_input(
                "Backup-Zeit", value=datetime.now().time().replace(hour=2, minute=0)
            )
            st.selectbox("Häufigkeit", ["Täglich", "Wöchentlich", "Monatlich"])

        if st.button("🔄 Backup jetzt erstellen"):
            with st.spinner("Erstelle Backup..."):
                time.sleep(2)  # Simulation
            st.success("✅ Backup erfolgreich erstellt!")

    with backup_col2:
        st.markdown("**Daten-Export:**")

        st.multiselect(
            "Datentypen für Export:",
            [
                "Maschinendaten",
                "Produktionsaufträge",
                "Qualitätsdaten",
                "Alarm-Historie",
            ],
            default=["Maschinendaten"],
        )

        st.selectbox(
            "Export-Zeitraum:",
            ["Letzte Woche", "Letzter Monat", "Letztes Quartal", "Benutzerdefiniert"],
        )

        if st.button("📥 Daten exportieren"):
            st.success("✅ Export-Datei wurde erstellt!")
            st.info("Download-Link wurde an Ihre E-Mail-Adresse gesendet.")

    # System-Status
    st.subheader("💻 System-Status")

    status_col1, status_col2, status_col3 = st.columns(3)

    with status_col1:
        st.metric("🖥️ CPU Auslastung", "23%", "2%")
        st.metric("💾 RAM Nutzung", "4.2 GB", "0.1 GB")

    with status_col2:
        st.metric("💽 Festplatte", "67%", "3%")
        st.metric("🌐 Netzwerk", "1.2 MB/s", "0.3 MB/s")

    with status_col3:
        st.metric("🔗 Verbindungen", "12", "1")
        st.metric("⏱️ Uptime", "12d 5h", "")

    # Einstellungen speichern
    st.markdown("---")
    if st.button("💾 Alle Einstellungen speichern", type="primary"):
        st.success("✅ Einstellungen erfolgreich gespeichert!")


if __name__ == "__main__":
    main()
