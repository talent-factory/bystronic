#!/usr/bin/env python3
"""
Daten-Upload und -verarbeitung mit Streamlit
============================================

Beispiel für Datei-Upload, -verarbeitung und -analyse:
- CSV/Excel Upload
- Datenvalidierung
- Interaktive Datenexploration
- Datenbereinigung
- Export-Funktionen

Starten mit: streamlit run daten_upload.py

Autor: Python Grundkurs für Bystronic-Entwickler
"""

from io import BytesIO

import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Bystronic Daten-Upload", page_icon="📁", layout="wide")


def main():
    st.title("📁 Daten-Upload und -verarbeitung")

    uploaded_file = st.file_uploader(
        "Wählen Sie eine Datei aus:",
        type=["csv", "xlsx", "xls"],
        help="Unterstützte Formate: CSV, Excel (xlsx, xls)",
    )

    if uploaded_file is not None:
        # Datei laden
        try:
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
            else:
                df = pd.read_excel(uploaded_file)

            st.success(f"✅ Datei '{uploaded_file.name}' erfolgreich geladen!")

            # Tabs für verschiedene Analysen
            tab1, tab2, tab3, tab4 = st.tabs(
                ["📊 Übersicht", "🔍 Exploration", "🧹 Bereinigung", "📤 Export"]
            )

            with tab1:
                show_data_overview(df)

            with tab2:
                show_data_exploration(df)

            with tab3:
                show_data_cleaning(df)

            with tab4:
                show_export_options(df)

        except Exception as e:
            st.error(f"❌ Fehler beim Laden der Datei: {e}")
            st.info("Bitte überprüfen Sie das Dateiformat und versuchen Sie es erneut.")

    else:
        # Demo-Daten anbieten
        st.info("💡 Laden Sie eine Datei hoch oder verwenden Sie die Demo-Daten")

        if st.button("🎯 Demo-Daten laden"):
            demo_df = create_demo_data()
            st.session_state["demo_data"] = demo_df
            st.success("Demo-Daten geladen!")
            st.rerun()

        if "demo_data" in st.session_state:
            df = st.session_state["demo_data"]

            tab1, tab2, tab3, tab4 = st.tabs(
                ["📊 Übersicht", "🔍 Exploration", "🧹 Bereinigung", "📤 Export"]
            )

            with tab1:
                show_data_overview(df)

            with tab2:
                show_data_exploration(df)

            with tab3:
                show_data_cleaning(df)

            with tab4:
                show_export_options(df)


def create_demo_data():
    """Erstellt Demo-Maschinendaten."""
    np.random.seed(42)

    timestamps = pd.date_range(start="2024-09-01", end="2024-09-04", freq="H")
    machines = ["Laser_1", "Laser_2", "Stanze_1", "Biegemaschine"]

    data = []
    for ts in timestamps:
        for machine in machines:
            data.append(
                {
                    "Timestamp": ts,
                    "Machine": machine,
                    "Temperature": np.random.normal(65, 5),
                    "Pressure": np.random.normal(8.2, 0.8),
                    "Speed": np.random.normal(2.5, 0.3),
                    "Parts_Produced": np.random.poisson(25),
                    "Quality_Index": np.random.normal(98.5, 1.5),
                    "Operator": np.random.choice(["Schmidt", "Mueller", "Weber"]),
                    "Shift": np.random.choice([1, 2, 3]),
                }
            )

    return pd.DataFrame(data)


def show_data_overview(df):
    """Zeigt Datenübersicht."""
    st.subheader("📊 Daten-Übersicht")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("📏 Zeilen", f"{len(df):,}")

    with col2:
        st.metric("📐 Spalten", len(df.columns))

    with col3:
        missing_values = df.isnull().sum().sum()
        st.metric("❓ Fehlende Werte", missing_values)

    with col4:
        memory_usage = df.memory_usage(deep=True).sum() / 1024**2
        st.metric("💾 Speicher", f"{memory_usage:.2f} MB")

    # Erste Zeilen anzeigen
    st.subheader("👀 Erste Zeilen")
    st.dataframe(df.head(10), use_container_width=True)

    # Datentypen
    st.subheader("🔍 Datentyp-Information")

    dtype_info = pd.DataFrame(
        {
            "Spalte": df.columns,
            "Datentyp": df.dtypes,
            "Nicht-Null Werte": df.count(),
            "Fehlende Werte": df.isnull().sum(),
            "Eindeutige Werte": df.nunique(),
        }
    )

    st.dataframe(dtype_info, use_container_width=True)

    # Statistische Zusammenfassung
    st.subheader("📈 Statistische Zusammenfassung")

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    if not numeric_cols.empty:
        st.dataframe(df[numeric_cols].describe(), use_container_width=True)
    else:
        st.info("Keine numerischen Spalten gefunden.")


def show_data_exploration(df):
    """Zeigt interaktive Datenexploration."""
    st.subheader("🔍 Datenexploration")

    # Spalten-Auswahl für Analyse
    numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object", "category"]).columns.tolist()

    if numeric_cols:
        st.markdown("### 📊 Numerische Daten")

        selected_numeric = st.multiselect(
            "Numerische Spalten für Visualisierung:",
            numeric_cols,
            default=numeric_cols[:2] if len(numeric_cols) >= 2 else numeric_cols,
        )

        if selected_numeric:
            viz_type = st.selectbox(
                "Visualisierungstyp:",
                [
                    "Histogramm",
                    "Box Plot",
                    "Scatter Plot",
                    "Korrelationsmatrix",
                    "Zeitreihe",
                ],
            )

            if viz_type == "Histogramm":
                col = st.selectbox("Spalte:", selected_numeric)
                fig = px.histogram(df, x=col, title=f"Verteilung: {col}")
                st.plotly_chart(fig, use_container_width=True)

            elif viz_type == "Box Plot":
                col = st.selectbox("Spalte:", selected_numeric)
                if categorical_cols:
                    group_col = st.selectbox("Gruppierung:", [None] + categorical_cols)
                    fig = px.box(df, y=col, x=group_col, title=f"Box Plot: {col}")
                else:
                    fig = px.box(df, y=col, title=f"Box Plot: {col}")
                st.plotly_chart(fig, use_container_width=True)

            elif viz_type == "Scatter Plot" and len(selected_numeric) >= 2:
                col1 = st.selectbox("X-Achse:", selected_numeric)
                col2 = st.selectbox(
                    "Y-Achse:", [c for c in selected_numeric if c != col1]
                )
                color_col = st.selectbox("Farbe:", [None] + categorical_cols)

                fig = px.scatter(
                    df,
                    x=col1,
                    y=col2,
                    color=color_col,
                    title=f"Scatter Plot: {col1} vs {col2}",
                )
                st.plotly_chart(fig, use_container_width=True)

            elif viz_type == "Korrelationsmatrix":
                corr_matrix = df[selected_numeric].corr()
                fig = px.imshow(
                    corr_matrix,
                    title="Korrelationsmatrix",
                    color_continuous_scale="RdBu",
                    aspect="auto",
                )
                st.plotly_chart(fig, use_container_width=True)

            elif viz_type == "Zeitreihe":
                date_cols = df.select_dtypes(include=["datetime64"]).columns.tolist()
                if date_cols:
                    date_col = st.selectbox("Zeitstempel-Spalte:", date_cols)
                    value_col = st.selectbox("Wert-Spalte:", selected_numeric)

                    fig = px.line(
                        df, x=date_col, y=value_col, title=f"Zeitreihe: {value_col}"
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("Keine Zeitstempel-Spalten gefunden.")

    if categorical_cols:
        st.markdown("### 📋 Kategorische Daten")

        selected_categorical = st.selectbox("Kategorische Spalte:", categorical_cols)

        value_counts = df[selected_categorical].value_counts()

        col1, col2 = st.columns(2)

        with col1:
            fig_bar = px.bar(
                x=value_counts.index,
                y=value_counts.values,
                title=f"Häufigkeit: {selected_categorical}",
            )
            fig_bar.update_xaxes(title=selected_categorical)
            fig_bar.update_yaxes(title="Anzahl")
            st.plotly_chart(fig_bar, use_container_width=True)

        with col2:
            fig_pie = px.pie(
                values=value_counts.values,
                names=value_counts.index,
                title=f"Verteilung: {selected_categorical}",
            )
            st.plotly_chart(fig_pie, use_container_width=True)


def show_data_cleaning(df):
    """Zeigt Datenbereinigungsoptionen."""
    st.subheader("🧹 Datenbereinigung")

    cleaned_df = df.copy()

    # Fehlende Werte behandeln
    st.markdown("### ❓ Fehlende Werte")

    missing_summary = df.isnull().sum()
    missing_cols = missing_summary[missing_summary > 0]

    if len(missing_cols) > 0:
        st.warning(f"Gefunden: {len(missing_cols)} Spalten mit fehlenden Werten")

        for col in missing_cols.index:
            st.write(f"**{col}**: {missing_cols[col]} fehlende Werte")

            action = st.selectbox(
                f"Aktion für {col}:",
                [
                    "Beibehalten",
                    "Zeilen löschen",
                    "Mittelwert",
                    "Median",
                    "Modus",
                    "Konstante",
                ],
                key=f"action_{col}",
            )

            if action == "Zeilen löschen":
                cleaned_df = cleaned_df.dropna(subset=[col])
            elif action == "Mittelwert" and df[col].dtype in ["int64", "float64"]:
                cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].mean())
            elif action == "Median" and df[col].dtype in ["int64", "float64"]:
                cleaned_df[col] = cleaned_df[col].fillna(cleaned_df[col].median())
            elif action == "Modus":
                mode_val = cleaned_df[col].mode()
                if not mode_val.empty:
                    cleaned_df[col] = cleaned_df[col].fillna(mode_val[0])
            elif action == "Konstante":
                fill_value = st.text_input(f"Füllwert für {col}:", key=f"fill_{col}")
                if fill_value:
                    cleaned_df[col] = cleaned_df[col].fillna(fill_value)
    else:
        st.success("✅ Keine fehlenden Werte gefunden!")

    # Duplikate behandeln
    st.markdown("### 👥 Duplikate")

    duplicates = df.duplicated().sum()
    if duplicates > 0:
        st.warning(f"Gefunden: {duplicates} doppelte Zeilen")

        if st.checkbox("Duplikate entfernen"):
            cleaned_df = cleaned_df.drop_duplicates()
            st.success(f"✅ {duplicates} Duplikate entfernt")
    else:
        st.success("✅ Keine Duplikate gefunden!")

    # Ausreißer erkennen
    st.markdown("### 📊 Ausreißer-Erkennung")

    numeric_cols = cleaned_df.select_dtypes(include=[np.number]).columns.tolist()

    if numeric_cols:
        outlier_col = st.selectbox("Spalte für Ausreißer-Analyse:", numeric_cols)

        Q1 = cleaned_df[outlier_col].quantile(0.25)
        Q3 = cleaned_df[outlier_col].quantile(0.75)
        IQR = Q3 - Q1

        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        outliers = cleaned_df[
            (cleaned_df[outlier_col] < lower_bound)
            | (cleaned_df[outlier_col] > upper_bound)
        ]

        st.write(f"**{outlier_col}**: {len(outliers)} Ausreißer gefunden")

        if len(outliers) > 0:
            fig_box = px.box(
                cleaned_df, y=outlier_col, title=f"Ausreißer in {outlier_col}"
            )
            st.plotly_chart(fig_box, use_container_width=True)

            if st.checkbox(f"Ausreißer in {outlier_col} entfernen"):
                cleaned_df = cleaned_df[
                    (cleaned_df[outlier_col] >= lower_bound)
                    & (cleaned_df[outlier_col] <= upper_bound)
                ]
                st.success(f"✅ {len(outliers)} Ausreißer entfernt")

    # Ergebnis der Bereinigung
    st.markdown("### 📋 Bereinigungsresultat")

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Original:**")
        st.write(f"Zeilen: {len(df)}")
        st.write(f"Fehlende Werte: {df.isnull().sum().sum()}")

    with col2:
        st.write("**Bereinigt:**")
        st.write(f"Zeilen: {len(cleaned_df)}")
        st.write(f"Fehlende Werte: {cleaned_df.isnull().sum().sum()}")

    # Bereinigte Daten im Session State speichern
    if st.button("💾 Bereinigte Daten übernehmen"):
        st.session_state["cleaned_data"] = cleaned_df
        st.success("✅ Bereinigte Daten gespeichert!")

    return cleaned_df


def show_export_options(df):
    """Zeigt Export-Optionen."""
    st.subheader("📤 Export-Optionen")

    # Daten auswählen (original oder bereinigt)
    data_source = st.radio(
        "Welche Daten exportieren?",
        ["Original-Daten", "Bereinigte Daten (falls verfügbar)"],
    )

    export_df = df
    if (
        data_source == "Bereinigte Daten (falls verfügbar)"
        and "cleaned_data" in st.session_state
    ):
        export_df = st.session_state["cleaned_data"]
        st.info("✅ Verwende bereinigte Daten für Export")

    # Export-Format
    export_format = st.selectbox("Export-Format:", ["CSV", "Excel (xlsx)", "JSON"])

    # Spalten-Auswahl
    selected_cols = st.multiselect(
        "Spalten für Export (alle wenn leer):", export_df.columns.tolist(), default=[]
    )

    if selected_cols:
        final_df = export_df[selected_cols]
    else:
        final_df = export_df

    # Vorschau
    st.markdown("### 👀 Export-Vorschau")
    st.write(f"Zeilen: {len(final_df)}, Spalten: {len(final_df.columns)}")
    st.dataframe(final_df.head(), use_container_width=True)

    # Download-Buttons
    col1, col2, col3 = st.columns(3)

    with col1:
        if export_format == "CSV":
            csv_data = final_df.to_csv(index=False)
            st.download_button(
                "📥 CSV Download",
                csv_data,
                file_name=f"export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv",
                mime="text/csv",
            )

    with col2:
        if export_format == "Excel (xlsx)":
            buffer = BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                final_df.to_excel(writer, index=False, sheet_name="Data")

            st.download_button(
                "📥 Excel Download",
                buffer.getvalue(),
                file_name=f"export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )

    with col3:
        if export_format == "JSON":
            json_data = final_df.to_json(orient="records", indent=2)
            st.download_button(
                "📥 JSON Download",
                json_data,
                file_name=f"export_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.json",
                mime="application/json",
            )


if __name__ == "__main__":
    main()
