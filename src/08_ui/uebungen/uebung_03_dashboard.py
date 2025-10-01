#!/usr/bin/env python3
"""
Übung 3: Streamlit-Dashboard entwickeln
=======================================

Lernziele:
- Streamlit-App mit mehreren Seiten erstellen
- Interaktive Widgets verwenden
- Datenvisualisierung implementieren
- Session State für Zustandserhaltung
- Export-Funktionen implementieren

Schwierigkeitsgrad: ⭐⭐⭐⭐☆ (Fortgeschritten)

Starten mit: uv run streamlit run src/08_ui/uebungen/uebung_03_dashboard.py

Autor: Daniel Senften
"""

import pandas as pd
import streamlit as st

# Seitenkonfiguration
st.set_page_config(page_title="Übung 3: Dashboard", page_icon="📊", layout="wide")


# TODO: Aufgabe 1 - Implementieren Sie die Dateninitialisierung
def init_session_state():
    """Initialisiert den Session State."""
    # TODO: Implementieren Sie die Initialisierung von:
    # - 'machine_data' als leere Liste
    # - 'production_log' als leere Liste
    # - 'dashboard_active' als False
    # - 'current_shift' als 1
    pass


# TODO: Aufgabe 2 - Implementieren Sie die Datengenerierung
@st.cache_data(ttl=10)  # Cache für 10 Sekunden
def generate_sample_data():
    """Generiert Beispiel-Maschinendaten."""
    # TODO: Generieren Sie DataFrame mit folgenden Spalten:
    # - timestamp (letzte 24 Stunden, stündlich)
    # - machine ('Laser 1', 'Laser 2', 'Stanze 1', 'Biegemaschine')
    # - temperature (Normal: 65±5°C)
    # - efficiency (Normal: 85±10%)
    # - production_rate (Normal: 250±30 Teile/h)
    # - quality_score (Normal: 98±2%)
    # - operator ('Schmidt', 'Mueller', 'Weber')
    # - status ('Läuft', 'Wartung', 'Stopp')

    # LÖSUNG (entkommentieren):
    # np.random.seed(42)
    # timestamps = pd.date_range(start=datetime.now()-timedelta(hours=24),
    #                           end=datetime.now(), freq='H')
    # machines = ['Laser 1', 'Laser 2', 'Stanze 1', 'Biegemaschine']
    # operators = ['Schmidt', 'Mueller', 'Weber']
    # statuses = ['Läuft', 'Wartung', 'Stopp']
    #
    # data = []
    # for ts in timestamps:
    #     for machine in machines:
    #         data.append({
    #             'timestamp': ts,
    #             'machine': machine,
    #             'temperature': np.random.normal(65, 5),
    #             'efficiency': np.random.normal(85, 10),
    #             'production_rate': np.random.normal(250, 30),
    #             'quality_score': np.random.normal(98, 2),
    #             'operator': np.random.choice(operators),
    #             'status': np.random.choice(statuses, p=[0.7, 0.2, 0.1])
    #         })
    #
    # return pd.DataFrame(data)

    # Für jetzt: leeres DataFrame zurückgeben
    return pd.DataFrame()


def main():
    """Hauptfunktion der Streamlit-App."""

    # TODO: Aufgabe 3 - Implementieren Sie den Haupt-Titel
    # st.title("🏭 SmartFactory Produktions-Dashboard")
    # st.markdown("**Übung 3:** Entwickeln Sie Ihr eigenes Dashboard")

    # Session State initialisieren
    init_session_state()

    # TODO: Aufgabe 4 - Implementieren Sie die Sidebar-Navigation
    # st.sidebar.title("🎛️ Navigation")
    # page = st.sidebar.radio(
    #     "Seite auswählen:",
    #     ["📊 Übersicht", "📈 Datenvisualisierung", "⚙️ Einstellungen", "📝 Logs"]
    # )

    # Für jetzt: Standard-Seite
    page = "📊 Übersicht"

    # TODO: Aufgabe 5 - Implementieren Sie die Seitenauswahl
    if page == "📊 Übersicht":
        show_overview_page()
    elif page == "📈 Datenvisualisierung":
        show_visualization_page()
    elif page == "⚙️ Einstellungen":
        show_settings_page()
    elif page == "📝 Logs":
        show_logs_page()


# TODO: Aufgabe 6 - Implementieren Sie die Übersichtsseite
def show_overview_page():
    """Zeigt die Dashboard-Übersicht."""
    st.header("📊 Produktionsübersicht")

    # TODO: Daten laden
    df = generate_sample_data()

    if df.empty:
        st.warning(
            "⚠️ Keine Daten verfügbar. Implementieren Sie zuerst die Datengenerierung!"
        )
        st.info(
            "💡 Tipp: Entkommentieren Sie den Code in der generate_sample_data() Funktion"
        )
        return

    # TODO: Aufgabe 6a - KPI-Metriken implementieren
    # st.subheader("📈 Key Performance Indicators")
    # col1, col2, col3, col4 = st.columns(4)
    #
    # # Berechnen Sie:
    # # - Durchschnittliche Effizienz
    # # - Gesamtproduktion (Summe production_rate wo status='Läuft')
    # # - Durchschnittliche Qualität
    # # - Anzahl laufender Maschinen
    #
    # with col1:
    #     avg_efficiency = df['efficiency'].mean()
    #     st.metric("⚡ Durchschn. Effizienz", f"{avg_efficiency:.1f}%")
    #
    # with col2:
    #     running_production = df[df['status'] == 'Läuft']['production_rate'].sum()
    #     st.metric("📦 Gesamtproduktion/h", f"{running_production:.0f}")
    #
    # # TODO: Ergänzen Sie col3 und col4

    # TODO: Aufgabe 6b - Maschinenstatus-Übersicht
    # st.subheader("🏭 Maschinenstatus")
    #
    # # Erstellen Sie eine Tabelle mit:
    # # - Maschine, Status, Temperatur, Effizienz, Operator
    #
    # current_status = df.groupby('machine').last().reset_index()
    #
    # # Status-Färbung implementieren
    # def color_status(val):
    #     if val == 'Läuft':
    #         return 'background-color: lightgreen'
    #     elif val == 'Wartung':
    #         return 'background-color: lightyellow'
    #     else:
    #         return 'background-color: lightcoral'
    #
    # styled_df = current_status.style.applymap(color_status, subset=['status'])
    # st.dataframe(styled_df, use_container_width=True)

    # TODO: Aufgabe 6c - Einfaches Diagramm
    # st.subheader("📊 Effizienz-Trend")
    #
    # # Erstellen Sie ein Liniendiagramm der Effizienz über Zeit
    # fig = px.line(df, x='timestamp', y='efficiency', color='machine',
    #               title='Effizienz-Verlauf nach Maschine')
    # st.plotly_chart(fig, use_container_width=True)


# TODO: Aufgabe 7 - Implementieren Sie die Visualisierungsseite
def show_visualization_page():
    """Zeigt erweiterte Datenvisualisierungen."""
    st.header("📈 Erweiterte Datenvisualisierung")

    df = generate_sample_data()

    if df.empty:
        st.warning("Keine Daten für Visualisierung verfügbar!")
        return

    # TODO: Aufgabe 7a - Parameter-Auswahl
    # st.subheader("🎯 Visualisierungsoptionen")
    #
    # col1, col2 = st.columns(2)
    # with col1:
    #     selected_machines = st.multiselect(
    #         "Maschinen auswählen:",
    #         df['machine'].unique(),
    #         default=df['machine'].unique()
    #     )
    #
    # with col2:
    #     chart_type = st.selectbox(
    #         "Diagrammtyp:",
    #         ["Liniendiagramm", "Balkendiagramm", "Scatter Plot", "Heatmap"]
    #     )

    # TODO: Aufgabe 7b - Datenfilterung
    # filtered_df = df[df['machine'].isin(selected_machines)]

    # TODO: Aufgabe 7c - Dynamische Charts
    # if chart_type == "Liniendiagramm":
    #     parameter = st.selectbox("Parameter:", ['temperature', 'efficiency', 'production_rate', 'quality_score'])
    #     fig = px.line(filtered_df, x='timestamp', y=parameter, color='machine',
    #                   title=f'{parameter} über Zeit')
    #     st.plotly_chart(fig, use_container_width=True)
    #
    # elif chart_type == "Balkendiagramm":
    #     # Durchschnittswerte pro Maschine
    #     avg_data = filtered_df.groupby('machine')[['efficiency', 'production_rate', 'quality_score']].mean().reset_index()
    #     parameter = st.selectbox("Parameter:", ['efficiency', 'production_rate', 'quality_score'])
    #     fig = px.bar(avg_data, x='machine', y=parameter, title=f'Durchschnittlicher {parameter}')
    #     st.plotly_chart(fig, use_container_width=True)
    #
    # # TODO: Implementieren Sie die anderen Diagrammtypen

    # TODO: Aufgabe 7d - Interaktive Filter
    # st.subheader("🔍 Erweiterte Filter")
    #
    # temp_range = st.slider("Temperaturbereich [°C]:",
    #                       float(df['temperature'].min()),
    #                       float(df['temperature'].max()),
    #                       (60.0, 80.0))
    #
    # eff_threshold = st.number_input("Mindest-Effizienz [%]:",
    #                                min_value=0.0, max_value=100.0, value=70.0)
    #
    # # Filter anwenden und Ergebnis zeigen
    # filtered_advanced = filtered_df[
    #     (filtered_df['temperature'] >= temp_range[0]) &
    #     (filtered_df['temperature'] <= temp_range[1]) &
    #     (filtered_df['efficiency'] >= eff_threshold)
    # ]
    #
    # st.write(f"**Gefilterte Daten:** {len(filtered_advanced)} von {len(filtered_df)} Einträgen")
    # st.dataframe(filtered_advanced.head(10), use_container_width=True)


# TODO: Aufgabe 8 - Implementieren Sie die Einstellungsseite
def show_settings_page():
    """Zeigt Einstellungen und Konfiguration."""
    st.header("⚙️ Dashboard-Einstellungen")

    # TODO: Aufgabe 8a - Benutzereinstellungen
    # st.subheader("👤 Benutzereinstellungen")
    #
    # user_name = st.text_input("Benutzername:", value="Operator")
    # shift_number = st.selectbox("Schicht:", [1, 2, 3])
    # auto_refresh = st.checkbox("Auto-Refresh aktivieren")
    #
    # if auto_refresh:
    #     refresh_interval = st.slider("Refresh-Intervall (Sekunden):", 5, 60, 10)

    # TODO: Aufgabe 8b - Systemkonfiguration
    # st.subheader("🖥️ System-Konfiguration")
    #
    # col1, col2 = st.columns(2)
    #
    # with col1:
    #     st.write("**Datenquellen:**")
    #     db_connection = st.text_input("Datenbank-URL:", "localhost:5432")
    #     api_endpoint = st.text_input("API-Endpoint:", "http://api.smartfactory.local")
    #
    # with col2:
    #     st.write("**Alarm-Einstellungen:**")
    #     temp_alarm = st.number_input("Temperatur-Alarm [°C]:", value=85.0)
    #     efficiency_alarm = st.number_input("Effizienz-Alarm [%]:", value=60.0)

    # TODO: Aufgabe 8c - Einstellungen speichern
    # if st.button("💾 Einstellungen speichern"):
    #     # Session State aktualisieren
    #     st.session_state.update({
    #         'user_name': user_name,
    #         'current_shift': shift_number,
    #         'auto_refresh': auto_refresh,
    #         'temp_alarm': temp_alarm,
    #         'efficiency_alarm': efficiency_alarm
    #     })
    #     st.success("✅ Einstellungen gespeichert!")

    # TODO: Aufgabe 8d - Export-Funktionen
    # st.subheader("📤 Export-Funktionen")
    #
    # export_format = st.radio("Export-Format:", ["CSV", "Excel", "JSON"])
    #
    # if st.button("📥 Daten exportieren"):
    #     df = generate_sample_data()
    #     if not df.empty:
    #         if export_format == "CSV":
    #             csv_data = df.to_csv(index=False)
    #             st.download_button("Download CSV", csv_data, "maschinendaten.csv", "text/csv")
    #         # TODO: Implementieren Sie Excel und JSON Export
    #         st.success("Export vorbereitet!")
    #     else:
    #         st.error("Keine Daten zum Exportieren!")


# TODO: Aufgabe 9 - Implementieren Sie die Logs-Seite
def show_logs_page():
    """Zeigt System-Logs und Ereignisse."""
    st.header("📝 System-Logs")

    # TODO: Aufgabe 9a - Log-Einträge anzeigen
    # if 'production_log' not in st.session_state:
    #     st.session_state.production_log = []
    #
    # st.subheader("📋 Produktions-Log")
    #
    # # Neue Log-Einträge hinzufügen
    # col1, col2 = st.columns([3, 1])
    #
    # with col1:
    #     new_log_message = st.text_input("Neue Log-Nachricht:")
    #
    # with col2:
    #     log_level = st.selectbox("Level:", ["INFO", "WARNING", "ERROR"])
    #
    # if st.button("➕ Log hinzufügen") and new_log_message:
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     log_entry = f"[{timestamp}] {log_level}: {new_log_message}"
    #     st.session_state.production_log.append(log_entry)
    #     st.success("Log-Eintrag hinzugefügt!")

    # TODO: Aufgabe 9b - Log-Anzeige
    # st.subheader("📖 Aktuelle Log-Einträge")
    #
    # if st.session_state.production_log:
    #     # Neueste Einträge zuerst
    #     for log_entry in reversed(st.session_state.production_log[-20:]):
    #         if "ERROR" in log_entry:
    #             st.error(log_entry)
    #         elif "WARNING" in log_entry:
    #             st.warning(log_entry)
    #         else:
    #             st.info(log_entry)
    #
    #     # Log-Verwaltung
    #     col1, col2 = st.columns(2)
    #     with col1:
    #         if st.button("🗑️ Logs löschen"):
    #             st.session_state.production_log = []
    #             st.success("Logs gelöscht!")
    #
    #     with col2:
    #         if st.button("📥 Logs exportieren"):
    #             log_text = "\n".join(st.session_state.production_log)
    #             st.download_button("Download Logs", log_text, "production_logs.txt", "text/plain")
    # else:
    #     st.info("Keine Log-Einträge vorhanden.")

    # TODO: Aufgabe 9c - Automatische System-Events
    # st.subheader("🔔 System-Events")
    #
    # if st.button("🎲 Zufälliges Event generieren"):
    #     events = [
    #         "Maschine Laser 1 gestartet",
    #         "Wartung an Stanze 1 abgeschlossen",
    #         "Temperaturwarnung bei Laser 2",
    #         "Schichtwechsel durchgeführt",
    #         "Qualitätsprüfung bestanden"
    #     ]
    #     event = np.random.choice(events)
    #     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    #     log_entry = f"[{timestamp}] INFO: {event}"
    #     st.session_state.production_log.append(log_entry)
    #     st.success(f"Event generiert: {event}")


if __name__ == "__main__":
    main()


"""
LÖSUNGSHINWEISE:
===============

Aufgabe 1 - Session State:
- Verwenden Sie st.session_state['key'] = value
- Prüfen Sie mit 'key' not in st.session_state

Aufgabe 2 - Datengenerierung:
- Verwenden Sie pd.date_range() für Zeitstempel
- np.random.normal() für realistische Werte
- np.random.choice() für kategorische Daten

Aufgabe 3-9 - Seitenaufbau:
- st.title(), st.header(), st.subheader() für Struktur
- st.columns() für Layout
- st.metric() für KPIs
- px.line(), px.bar() für Charts
- st.dataframe() für Tabellen
- st.download_button() für Export

Wichtige Streamlit-Konzepte:
- @st.cache_data für Performance
- st.session_state für Zustandserhaltung
- st.sidebar für Navigation
- st.columns für Layout
- st.rerun() für Updates

ERWARTETE FUNKTIONEN:
====================

✅ Multi-Page Navigation funktioniert
✅ Daten werden generiert und angezeigt
✅ KPI-Metriken werden berechnet
✅ Charts sind interaktiv und filterbar
✅ Einstellungen können gespeichert werden
✅ Export-Funktionen arbeiten
✅ Logs können verwaltet werden
✅ Session State erhält Zustand
✅ Responsive Layout auf verschiedenen Bildschirmgrößen

BONUS-FEATURES:
==============
✅ Echtzeitdaten-Simulation
✅ Erweiterte Filter-Optionen
✅ Custom CSS Styling
✅ Automatische Alerts bei kritischen Werten
✅ Historische Daten-Analyse
✅ Multi-Chart Dashboard
✅ Benutzer-Authentifizierung
✅ Mobile-optimierte Ansicht
"""
