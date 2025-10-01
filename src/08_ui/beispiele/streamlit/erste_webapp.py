"""
Erste Streamlit Web-App
======================

Dieses Beispiel zeigt die Grundlagen von Streamlit:
- Seitenlayout und Komponenten
- Interaktive Widgets
- Datenvisualisierung
- Session State
- Multi-Page Apps

Starten mit: uv run streamlit run src/08_ui/beispiele/streamlit/erste_webapp.py

Autor: Daniel Senften
"""

import time
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

# Seitenkonfiguration
st.set_page_config(
    page_title="SmartFactory Streamlit Demo",
    page_icon="🏭",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Custom CSS für besseres Aussehen
st.markdown(
    """
<style>
.main-header {
    font-size: 3rem;
    color: #1f77b4;
    text-align: center;
    margin-bottom: 2rem;
}

.metric-card {
    background-color: #f0f2f6;
    padding: 1rem;
    border-radius: 0.5rem;
    border-left: 5px solid #1f77b4;
}

.success-metric {
    border-left-color: #00cc88;
}

.warning-metric {
    border-left-color: #ffaa00;
}

.danger-metric {
    border-left-color: #ff6666;
}
</style>
""",
    unsafe_allow_html=True,
)


def main():
    """Hauptfunktion der Streamlit-App."""

    # Titel der Anwendung
    st.markdown(
        '<h1 class="main-header">🏭 SmartFactory Streamlit Dashboard</h1>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Sidebar für Navigation
    st.sidebar.title("Navigation")

    # App-Modus wählen
    app_mode = st.sidebar.selectbox(
        "Wählen Sie einen Bereich:",
        [
            "🏠 Übersicht",
            "📊 Widgets Demo",
            "📈 Datenvisualisierung",
            "🎮 Interaktive Elemente",
            "📱 Layout Demo",
            "🔄 Echtzeitdaten",
        ],
    )

    # Sidebar-Info
    st.sidebar.markdown("---")
    st.sidebar.info(
        "💡 **Tipp:** Diese Demo zeigt die wichtigsten Streamlit-Features "
        "für industrielle Dashboards."
    )

    # Je nach ausgewähltem Modus verschiedene Seiten anzeigen
    if app_mode == "🏠 Übersicht":
        show_overview()
    elif app_mode == "📊 Widgets Demo":
        show_widgets_demo()
    elif app_mode == "📈 Datenvisualisierung":
        show_visualization_demo()
    elif app_mode == "🎮 Interaktive Elemente":
        show_interactive_elements()
    elif app_mode == "📱 Layout Demo":
        show_layout_demo()
    elif app_mode == "🔄 Echtzeitdaten":
        show_realtime_demo()


def show_overview():
    """Zeigt die Übersichtsseite."""

    st.header("Willkommen bei Streamlit!")

    st.markdown(
        """
    **Streamlit** ist ein Python-Framework zur schnellen Erstellung von
    Web-Dashboards und Datenvisualisierung-Apps. Perfekt für:

    - 📊 **Daten-Dashboards** - Schnelle Visualisierung von Produktionsdaten
    - 🏭 **Industrielle Überwachung** - Echtzeitmonitoring von Maschinen
    - 📈 **Business Intelligence** - KPI-Tracking und Reporting
    - 🔬 **Datenanalyse** - Interaktive Datenexploration
    """
    )

    # Beispiel-Metriken
    st.subheader("📋 Aktuelle Systemübersicht")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="🏭 Maschinenauslastung",
            value="87%",
            delta="5.2%",
            help="Durchschnittliche Auslastung aller Maschinen",
        )

    with col2:
        st.metric(
            label="⚡ Energieverbrauch",
            value="145 kWh",
            delta="-12 kWh",
            help="Aktueller Stromverbrauch",
        )

    with col3:
        st.metric(
            label="📦 Tagesproduktion",
            value="1,247",
            delta="89",
            help="Produzierte Teile heute",
        )

    with col4:
        st.metric(
            label="✅ Qualitätsindex",
            value="98.5%",
            delta="0.3%",
            help="Aktuelle Qualitätsbewertung",
        )

    # Quick Status Cards
    st.subheader("🚦 System Status")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.success("✅ **Laser 1** - Läuft normal")
        st.info("ℹ️ **Laser 2** - Wartung geplant")

    with col2:
        st.success("✅ **Stanze 1** - Optimal")
        st.warning("⚠️ **Biegemaschine** - Überwachung")

    with col3:
        st.success("✅ **Qualitätsprüfung** - Aktiv")
        st.error("❌ **Sensor 5** - Offline")

    # Fortschrittsbalken
    st.subheader("📈 Produktionsfortschritt")

    progress_col1, progress_col2 = st.columns(2)

    with progress_col1:
        st.write("**Tagesziel Fortschritt:**")
        progress = st.progress(0)
        for i in range(72):  # 72% erreicht
            progress.progress(i + 1)
            time.sleep(0.01)
        st.write("72% des Tagesziels erreicht")

    with progress_col2:
        st.write("**Qualitätsziel:**")
        st.progress(98, text="98% Qualitätsindex")


def show_widgets_demo():
    """Demonstriert verschiedene Streamlit-Widgets."""

    st.header("📊 Streamlit Widgets Demo")

    st.markdown("Diese Seite zeigt die wichtigsten interaktiven Elemente:")

    # Eingabe-Widgets
    st.subheader("📝 Eingabe-Widgets")

    col1, col2 = st.columns(2)

    with col1:
        # Text-Eingaben
        st.write("**Text-Eingaben:**")
        operator_name = st.text_input("Operator Name", "Mustermann")
        st.text_area("Schichtnotizen", "Alles läuft normal...")

        # Numerische Eingaben
        st.write("**Numerische Eingaben:**")
        target_production = st.number_input(
            "Tagesziel", min_value=100, max_value=3000, value=2000
        )
        temperature_limit = st.slider("Temperaturgrenze [°C]", 50, 100, 75)

        # Datum/Zeit
        maintenance_date = st.date_input("Nächste Wartung", datetime.now().date())

    with col2:
        # Auswahl-Widgets
        st.write("**Auswahl-Widgets:**")
        machine_type = st.selectbox(
            "Maschinentyp", ["Laser-Schneidmaschine", "Stanzmaschine", "Biegemaschine"]
        )

        st.multiselect(
            "Qualitätsprüfungen",
            [
                "Maßhaltigkeit",
                "Oberflächengüte",
                "Materialfestigkeit",
                "Kantenqualität",
            ],
            default=["Maßhaltigkeit", "Oberflächengüte"],
        )

        # Checkboxen und Radio
        enable_alerts = st.checkbox("E-Mail Benachrichtigungen", value=True)

        priority_level = st.radio(
            "Prioritätsstufe", ["Normal", "Hoch", "Kritisch"], horizontal=True
        )

        # Buttons
        st.write("**Aktions-Buttons:**")
        col_btn1, col_btn2, col_btn3 = st.columns(3)

        with col_btn1:
            if st.button("▶️ Start", type="primary"):
                st.success("Produktion gestartet!")

        with col_btn2:
            if st.button("⏸️ Pause"):
                st.warning("Produktion pausiert!")

        with col_btn3:
            if st.button("⏹️ Stopp"):
                st.error("Produktion gestoppt!")

    # Ergebnisse anzeigen
    st.subheader("📋 Eingegebene Werte")

    results_data = {
        "Parameter": [
            "Operator",
            "Maschinentyp",
            "Tagesziel",
            "Temperaturgrenze",
            "Wartungsdatum",
            "Priorität",
            "Benachrichtigungen",
        ],
        "Wert": [
            operator_name,
            machine_type,
            f"{target_production:,} Stück",
            f"{temperature_limit}°C",
            maintenance_date.strftime("%d.%m.%Y"),
            priority_level,
            "Aktiviert" if enable_alerts else "Deaktiviert",
        ],
    }

    results_df = pd.DataFrame(results_data)
    st.table(results_df)


def show_visualization_demo():
    """Zeigt Datenvisualisierung-Beispiele."""

    st.header("📈 Datenvisualisierung mit Streamlit")

    # Beispieldaten generieren
    @st.cache_data
    def generate_production_data():
        """Generiert Beispiel-Produktionsdaten."""
        dates = pd.date_range(start="2024-09-01", end="2024-09-04", freq="h")

        data = {
            "timestamp": dates,
            "production_rate": np.random.normal(250, 30, len(dates)),
            "temperature": np.random.normal(65, 8, len(dates)),
            "quality_index": np.random.normal(98, 2, len(dates)),
            "machine": np.random.choice(["Laser 1", "Laser 2", "Stanze 1"], len(dates)),
            "shift": [(hour % 24) // 8 + 1 for hour in range(len(dates))],
        }

        return pd.DataFrame(data)

    df = generate_production_data()

    # Charts nebeneinander
    st.subheader("📊 Produktions-Charts")

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        # Liniendiagramm - Produktionsrate
        fig_line = px.line(
            df,
            x="timestamp",
            y="production_rate",
            color="machine",
            title="Produktionsrate über Zeit",
            labels={"production_rate": "Teile/Stunde", "timestamp": "Zeit"},
        )
        fig_line.update_layout(height=400)
        st.plotly_chart(fig_line, width="stretch")

    with chart_col2:
        # Streudiagramm - Temperatur vs Qualität
        fig_scatter = px.scatter(
            df,
            x="temperature",
            y="quality_index",
            color="machine",
            size="production_rate",
            title="Temperatur vs. Qualitätsindex",
            labels={"temperature": "Temperatur [°C]", "quality_index": "Qualität [%]"},
        )
        fig_scatter.update_layout(height=400)
        st.plotly_chart(fig_scatter, width="stretch")

    # Histogramm und Boxplot
    hist_col1, hist_col2 = st.columns(2)

    with hist_col1:
        # Histogramm
        fig_hist = px.histogram(
            df,
            x="quality_index",
            nbins=20,
            title="Qualitätsverteilung",
            labels={"quality_index": "Qualitätsindex [%]", "count": "Häufigkeit"},
        )
        fig_hist.update_layout(height=350)
        st.plotly_chart(fig_hist, width="stretch")

    with hist_col2:
        # Boxplot
        fig_box = px.box(
            df,
            x="machine",
            y="production_rate",
            title="Produktionsrate nach Maschine",
            labels={"production_rate": "Teile/Stunde", "machine": "Maschine"},
        )
        fig_box.update_layout(height=350)
        st.plotly_chart(fig_box, width="stretch")

    # Heatmap
    st.subheader("🔥 Korrelations-Heatmap")

    # Numerische Spalten für Korrelation
    numeric_df = df[["production_rate", "temperature", "quality_index"]].corr()

    fig_heatmap = px.imshow(
        numeric_df,
        title="Korrelation zwischen Produktionsparametern",
        color_continuous_scale="RdBu",
        aspect="auto",
    )
    fig_heatmap.update_layout(height=400)
    st.plotly_chart(fig_heatmap, width="stretch")

    # Daten-Tabelle
    st.subheader("📋 Rohdaten")

    # Filter-Optionen
    col_filter1, col_filter2 = st.columns(2)

    with col_filter1:
        selected_machines = st.multiselect(
            "Maschinen auswählen:",
            df["machine"].unique(),
            default=df["machine"].unique(),
        )

    with col_filter2:
        date_range = st.date_input(
            "Datumsbereich:",
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

    # Formatierte Tabelle anzeigen
    display_df = filtered_df.copy()
    display_df["timestamp"] = display_df["timestamp"].dt.strftime("%d.%m.%Y %H:%M")
    display_df["production_rate"] = display_df["production_rate"].round(1)
    display_df["temperature"] = display_df["temperature"].round(1)
    display_df["quality_index"] = display_df["quality_index"].round(2)

    st.dataframe(display_df, width="stretch")

    # Download-Button
    csv_data = display_df.to_csv(index=False)
    st.download_button(
        label="📥 Daten als CSV herunterladen",
        data=csv_data,
        file_name=f"produktionsdaten_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
        mime="text/csv",
    )


def show_interactive_elements():
    """Zeigt interaktive Streamlit-Elemente."""

    st.header("🎮 Interaktive Elemente")

    # Session State Demo
    st.subheader("💾 Session State - Zustandserhaltung")

    # Zähler im Session State
    if "counter" not in st.session_state:
        st.session_state.counter = 0

    if "production_log" not in st.session_state:
        st.session_state.production_log = []

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("➕ Zähler erhöhen"):
            st.session_state.counter += 1

    with col2:
        if st.button("➖ Zähler verringern"):
            st.session_state.counter -= 1

    with col3:
        if st.button("🔄 Reset"):
            st.session_state.counter = 0

    st.write(f"**Aktueller Zähler:** {st.session_state.counter}")

    # Produktions-Log
    st.subheader("📝 Produktions-Log")

    log_col1, log_col2 = st.columns([3, 1])

    with log_col1:
        log_message = st.text_input("Neue Meldung:", key="log_input")

    with log_col2:
        if st.button("➕ Hinzufügen") and log_message:
            timestamp = datetime.now().strftime("%H:%M:%S")
            st.session_state.production_log.append(f"[{timestamp}] {log_message}")
            st.session_state.log_input = ""  # Input leeren
            st.rerun()

    if st.session_state.production_log:
        st.write("**Aktuelle Log-Einträge:**")
        for entry in reversed(
            st.session_state.production_log[-10:]
        ):  # Letzte 10 anzeigen
            st.text(entry)

        if st.button("🗑️ Log löschen"):
            st.session_state.production_log = []
            st.rerun()

    # File Upload Demo
    st.subheader("📁 Datei-Upload")

    uploaded_file = st.file_uploader(
        "CSV-Datei hochladen:",
        type=["csv", "xlsx"],
        help="Laden Sie Maschinendaten oder Produktionsdaten hoch",
    )

    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success(f"✅ Datei erfolgreich geladen: {uploaded_file.name}")
            st.write(f"**Dimensionen:** {df.shape[0]} Zeilen, {df.shape[1]} Spalten")

            # Erste Zeilen anzeigen
            st.write("**Vorschau:**")
            st.dataframe(df.head())

            # Basis-Statistiken
            if st.checkbox("📊 Statistiken anzeigen"):
                st.write("**Statistische Übersicht:**")
                st.dataframe(df.describe())

        except Exception as e:
            st.error(f"❌ Fehler beim Laden der Datei: {e}")

    # Sidebar-Elemente
    st.subheader("🔧 Sidebar-Integration")

    # Diese werden in der Sidebar angezeigt
    with st.sidebar:
        st.markdown("### 🎛️ Maschinensteuerung")

        machine_power = st.slider("Maschinenleistung [%]", 0, 100, 85)
        cooling_temp = st.number_input("Kühltemperatur [°C]", 15, 25, 20)

        st.markdown("### 🔔 Alarme")

        if st.button("🚨 Test-Alarm"):
            st.error("Test-Alarm ausgelöst!")

        st.markdown("### 📊 Quick Stats")
        st.metric("Leistung", f"{machine_power}%")
        st.metric("Kühlung", f"{cooling_temp}°C")

    # Hauptbereich zeigt die Sidebar-Werte
    st.write("**Aktuelle Einstellungen aus der Sidebar:**")
    settings_df = pd.DataFrame(
        {
            "Parameter": ["Maschinenleistung", "Kühltemperatur"],
            "Wert": [f"{machine_power}%", f"{cooling_temp}°C"],
            "Status": ["Normal", "Normal"],
        }
    )
    st.table(settings_df)


def show_layout_demo():
    """Demonstriert Layout-Möglichkeiten."""

    st.header("📱 Layout-Möglichkeiten")

    # Columns Layout
    st.subheader("📐 Columns Layout")

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.info("**Schmale Spalte**\n\nStatus-Anzeigen")
        st.metric("Temp", "65°C")
        st.metric("Druck", "8.2 bar")

    with col2:
        st.success("**Breite Hauptspalte**\n\nHauptcontent und Charts")

        # Beispiel-Chart
        data = pd.DataFrame({"x": range(10), "y": np.random.randn(10).cumsum()})
        st.line_chart(data.set_index("x"))

    with col3:
        st.warning("**Rechte Spalte**\n\nSteuerung")

        if st.button("Start"):
            st.success("Gestartet!")
        if st.button("Stopp"):
            st.error("Gestoppt!")

    # Tabs Layout
    st.subheader("📂 Tabs Layout")

    tab1, tab2, tab3, tab4 = st.tabs(
        ["🏭 Produktion", "🔧 Wartung", "📊 Qualität", "⚙️ Einstellungen"]
    )

    with tab1:
        st.write("**Produktionsübersicht**")
        prod_data = pd.DataFrame(
            {
                "Stunde": [f"{i:02d}:00" for i in range(8, 16)],
                "Produktion": np.random.randint(200, 300, 8),
            }
        )
        st.bar_chart(prod_data.set_index("Stunde"))

    with tab2:
        st.write("**Wartungsplanung**")
        maintenance_data = {
            "Maschine": ["Laser 1", "Laser 2", "Stanze 1"],
            "Nächste Wartung": ["05.09.2024", "12.09.2024", "08.09.2024"],
            "Typ": ["Routine", "Reparatur", "Kalibrierung"],
        }
        st.table(pd.DataFrame(maintenance_data))

    with tab3:
        st.write("**Qualitätskontrolle**")
        quality_data = np.random.normal(98, 2, 50)
        st.histogram(quality_data)
        st.write(f"Durchschnitt: {quality_data.mean():.2f}%")

    with tab4:
        st.write("**Systemeinstellungen**")
        st.selectbox("Sprache", ["Deutsch", "English", "Français"])
        st.checkbox("Dark Mode")
        st.slider("Refresh Rate [s]", 1, 60, 5)

    # Expandable Sections
    st.subheader("📋 Expandable Sections")

    with st.expander("🔍 Detaillierte Maschinenparameter"):
        st.write("Hier sind alle detaillierten Parameter:")

        param_data = pd.DataFrame(
            {
                "Parameter": [
                    "Temperatur Kopf 1",
                    "Temperatur Kopf 2",
                    "Schnittgeschwindigkeit",
                    "Laserstrom",
                    "Hilfsgas-Druck",
                    "Fokus-Position",
                ],
                "Aktuell": [
                    "64.2°C",
                    "65.8°C",
                    "2.4 m/min",
                    "180A",
                    "8.1 bar",
                    "-2.1mm",
                ],
                "Sollwert": ["65°C", "65°C", "2.5 m/min", "175A", "8.0 bar", "-2.0mm"],
                "Toleranz": ["±3°C", "±3°C", "±0.2", "±10A", "±0.5 bar", "±0.3mm"],
            }
        )
        st.dataframe(param_data, width="stretch")

    with st.expander("📈 Produktionsstatistiken"):
        st.write("Erweiterte Statistiken für die letzte Woche:")

        # Beispiel-Statistiken
        stats_data = {
            "Metrik": [
                "Gesamtproduktion",
                "Durchschn. Stückzahl/Tag",
                "Qualitätsindex",
                "Ausschussrate",
                "Betriebszeit",
                "Ungeplante Stillstände",
            ],
            "Wert": [
                "14,250 Teile",
                "2,036 Teile",
                "98.4%",
                "1.6%",
                "165h 30min",
                "4h 15min",
            ],
            "Trend": ["↗ +8.2%", "↗ +5.1%", "→ +0.1%", "↘ -0.3%", "↗ +2.1%", "↘ -1.2h"],
        }
        st.table(pd.DataFrame(stats_data))

    # Container für bessere Strukturierung
    st.subheader("📦 Container")

    with st.container():
        st.write("**Container 1: Alarme und Warnungen**")

        alert_col1, alert_col2 = st.columns(2)

        with alert_col1:
            st.error("🚨 Kritischer Alarm: Temperatur zu hoch!")
            st.warning("⚠️ Warnung: Wartung fällig")

        with alert_col2:
            st.info("ℹ️ Info: Schichtwechsel in 30 min")
            st.success("✅ Alle Systeme normal")


def show_realtime_demo():
    """Zeigt Echtzeit-Daten-Updates."""

    st.header("🔄 Echtzeitdaten-Simulation")

    st.markdown(
        """
    Diese Seite simuliert Echtzeitdaten-Updates. In einer echten Anwendung
    würden hier live Daten von Maschinen oder Datenbanken geladen werden.
    """
    )

    # Auto-Refresh aktivieren
    auto_refresh = st.checkbox("🔄 Auto-Refresh (alle 2 Sekunden)", value=False)

    if auto_refresh:
        # Placeholder für Live-Updates
        placeholder = st.empty()

        # Simulierte Live-Daten
        while auto_refresh:
            with placeholder.container():
                # Aktuelle Zeit
                current_time = datetime.now().strftime("%H:%M:%S")
                st.subheader(f"🕐 Live-Daten - {current_time}")

                # Live-Metriken
                col1, col2, col3, col4 = st.columns(4)

                with col1:
                    temp = 65 + np.random.normal(0, 3)
                    st.metric("🌡️ Temperatur", f"{temp:.1f}°C", f"{temp - 65:.1f}")

                with col2:
                    pressure = 8.2 + np.random.normal(0, 0.5)
                    st.metric(
                        "💨 Druck", f"{pressure:.1f} bar", f"{pressure - 8.2:.1f}"
                    )

                with col3:
                    production = np.random.randint(240, 260)
                    st.metric("📦 Stückzahl/h", production, production - 250)

                with col4:
                    quality = 98.5 + np.random.normal(0, 0.5)
                    st.metric("✅ Qualität", f"{quality:.1f}%", f"{quality - 98.5:.1f}")

                # Live-Chart
                chart_data = pd.DataFrame(
                    {
                        "Zeit": pd.date_range(
                            start=datetime.now() - timedelta(minutes=30),
                            end=datetime.now(),
                            freq="1min",
                        ),
                        "Temperatur": 65 + np.random.normal(0, 2, 31).cumsum() * 0.1,
                        "Druck": 8.2 + np.random.normal(0, 0.3, 31).cumsum() * 0.05,
                    }
                )

                st.line_chart(chart_data.set_index("Zeit"))

            # 2 Sekunden warten
            time.sleep(2)
    else:
        # Statische Ansicht
        st.info("Aktivieren Sie Auto-Refresh für Live-Updates")

        # Manueller Refresh-Button
        if st.button("🔄 Manuell aktualisieren"):
            st.rerun()

    # Historische Daten
    st.subheader("📊 Historische Daten")

    # Zeitraum-Auswahl
    time_range = st.selectbox(
        "Zeitraum:",
        ["Letzte Stunde", "Letzten 4 Stunden", "Letzten 24 Stunden", "Letzte Woche"],
    )

    # Entsprechende Daten generieren
    if time_range == "Letzte Stunde":
        periods = 60
        freq = "1min"
    elif time_range == "Letzten 4 Stunden":
        periods = 240
        freq = "1min"
    elif time_range == "Letzten 24 Stunden":
        periods = 24
        freq = "1h"
    else:  # Letzte Woche
        periods = 168
        freq = "1h"

    hist_data = pd.DataFrame(
        {
            "timestamp": pd.date_range(end=datetime.now(), periods=periods, freq=freq),
            "temperature": 65 + np.random.normal(0, 3, periods),
            "pressure": 8.2 + np.random.normal(0, 0.5, periods),
            "production_rate": np.random.normal(250, 20, periods),
        }
    )

    # Charts
    chart_tab1, chart_tab2, chart_tab3 = st.tabs(["Temperatur", "Druck", "Produktion"])

    with chart_tab1:
        fig_temp = px.line(
            hist_data, x="timestamp", y="temperature", title="Temperaturverlauf"
        )
        st.plotly_chart(fig_temp, width="stretch")

    with chart_tab2:
        fig_press = px.line(
            hist_data, x="timestamp", y="pressure", title="Druckverlauf"
        )
        st.plotly_chart(fig_press, width="stretch")

    with chart_tab3:
        fig_prod = px.line(
            hist_data, x="timestamp", y="production_rate", title="Produktionsrate"
        )
        st.plotly_chart(fig_prod, width="stretch")


if __name__ == "__main__":
    main()
