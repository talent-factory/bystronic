import pandas as pd
import streamlit as st

st.title("CSV Viewer mit Header-Auswahl")

uploaded_file = st.file_uploader("Wähle eine CSV-Datei aus", type=["csv"])

if uploaded_file:
    st.write(f"Datei hochgeladen: {uploaded_file.name}")

    try:
        # Lese die ersten 25 Zeilen manuell ohne pandas
        uploaded_file.seek(0)
        content = uploaded_file.read().decode("utf-8")
        lines = content.split("\n")[:25]

        # Zeige Vorschau der ersten 25 Zeilen
        st.write("**Vorschau der ersten 25 Zeilen:**")
        preview_data = []
        for i, line in enumerate(lines):
            if line.strip():  # Nur nicht-leere Zeilen
                cols = line.split("\t")
                preview_data.append(
                    [f"Zeile {i}"] + cols[:10]
                )  # Erste 10 Spalten + Zeilennummer

        if preview_data:
            preview_df = pd.DataFrame(preview_data)
            preview_df.columns = ["Zeile"] + [
                f"Spalte {i}" for i in range(len(preview_df.columns) - 1)
            ]
            st.dataframe(preview_df, use_container_width=True)

            # Benutzer-Eingaben für Header und Datenzeilen
            col1, col2 = st.columns(2)
            with col1:
                header_zeile = st.number_input(
                    "Header-Zeile (0-basiert)",
                    min_value=0,
                    max_value=len(lines) - 1,
                    value=6,
                    help="Zeile mit den Spaltennamen",
                )
            with col2:
                daten_zeile = st.number_input(
                    "Erste Datenzeile (0-basiert)",
                    min_value=0,
                    max_value=len(lines) - 1,
                    value=21,
                    help="Erste Zeile mit tatsächlichen Daten",
                )

            if st.button("Daten mit gewählten Einstellungen laden"):
                try:
                    # Jetzt pandas mit den gewählten Einstellungen verwenden
                    uploaded_file.seek(0)

                    # Lade nur ab der Datenzeile
                    df = pd.read_csv(
                        uploaded_file,
                        sep="\t",
                        encoding="utf-8",
                        skiprows=daten_zeile,
                        header=None,
                        on_bad_lines="skip",
                    )

                    # Setze Header aus der gewählten Header-Zeile
                    if header_zeile < len(lines):
                        header_line = lines[header_zeile]
                        headers = header_line.split("\t")

                        # Bereinige Header
                        clean_headers = []
                        for i, h in enumerate(headers):
                            if h.strip() and h.strip() != "Name":
                                clean_headers.append(h.strip())
                            else:
                                clean_headers.append(f"Spalte_{i}")

                        # Setze Header (nur so viele wie Spalten vorhanden)
                        if len(clean_headers) >= len(df.columns):
                            df.columns = clean_headers[: len(df.columns)]
                        else:
                            df.columns = clean_headers + [
                                f"Spalte_{i}"
                                for i in range(len(clean_headers), len(df.columns))
                            ]

                    st.success(
                        f"Daten erfolgreich geladen: {len(df)} Zeilen, {len(df.columns)} Spalten"
                    )
                    st.write("**Erste 10 Datensätze:**")
                    st.dataframe(df.head(10))

                    # Zeige Spalteninfo
                    st.write("**Spalten-Übersicht:**")
                    col_info = pd.DataFrame(
                        {
                            "Spalte": df.columns,
                            "Datentyp": df.dtypes,
                            "Nicht-null Werte": df.count(),
                        }
                    )
                    st.dataframe(col_info)

                except Exception as e:
                    st.error(f"Fehler beim Laden der Daten: {e}")
        else:
            st.warning("Keine Daten in der Datei gefunden.")

    except Exception as e:
        st.error(f"Fehler beim Einlesen der Datei: {e}")
