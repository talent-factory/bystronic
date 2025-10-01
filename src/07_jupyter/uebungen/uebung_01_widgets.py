#!/usr/bin/env python3
"""
Übung 1: Jupyter Widgets für interaktive Datenanalyse

Lernziele:
- Verwendung von ipywidgets für interaktive Notebooks
- Erstellung von Dashboards für Maschinendaten
- Event-Handling und Widget-Interaktionen

AUFGABEN:
1. Implementieren Sie die fehlenden Funktionen
2. Testen Sie Ihre Implementierung
3. Erweitern Sie das Dashboard um zusätzliche Features
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    import ipywidgets as widgets
    from IPython.display import display

    WIDGETS_AVAILABLE = True
except ImportError:
    print(
        "⚠️ ipywidgets nicht installiert. Installieren Sie mit: pip install ipywidgets"
    )
    WIDGETS_AVAILABLE = False


def erstelle_maschinendaten(anzahl_datenpunkte: int = 200) -> pd.DataFrame:
    """
    AUFGABE 1: Erstellen Sie realistische Maschinendaten

    Erstellen Sie einen DataFrame mit folgenden Spalten:
    - MaschinenID: Eindeutige IDs (M001, M002, etc.)
    - Typ: Maschinentyp (Laser, Presse, Stanzer)
    - Temperatur: Betriebstemperatur (40-80°C)
    - Druck: Arbeitsdruck (10-50 bar)
    - Geschwindigkeit: Arbeitsgeschwindigkeit (50-200 m/min)
    - Effizienz: Effizienz in % (70-100%)
    - Status: Betriebsstatus (Aktiv, Wartung, Stillstand)
    - Schicht: Arbeitsschicht (Früh, Spät, Nacht)

    Args:
        anzahl_datenpunkte: Anzahl der zu generierenden Datenpunkte

    Returns:
        DataFrame mit Maschinendaten

    HINWEIS: Verwenden Sie np.random.seed(42) für reproduzierbare Ergebnisse
    """
    # TODO: Implementieren Sie diese Funktion
    np.random.seed(42)

    # Beispiel-Implementierung (erweitern Sie diese):
    data = {
        "MaschinenID": [f"M{i:03d}" for i in range(1, anzahl_datenpunkte + 1)],
        # TODO: Fügen Sie die anderen Spalten hinzu
    }

    return pd.DataFrame(data)


def erstelle_filter_widgets(data: pd.DataFrame) -> dict[str, widgets.Widget]:
    """
    AUFGABE 2: Erstellen Sie Filter-Widgets für das Dashboard

    Erstellen Sie folgende Widgets:
    - Dropdown für Maschinentyp (mit "Alle" Option)
    - MultiSelect für Status
    - IntRangeSlider für Temperaturbereich
    - Dropdown für Schicht
    - Checkbox für "Nur aktive Maschinen"

    Args:
        data: DataFrame mit Maschinendaten

    Returns:
        Dictionary mit Widgets
    """
    if not WIDGETS_AVAILABLE:
        return {}

    filter_widgets = {}

    # TODO: Implementieren Sie die Filter-Widgets
    # Beispiel:
    # filter_widgets['typ'] = widgets.Dropdown(
    #     options=['Alle'] + list(data['Typ'].unique()),
    #     value='Alle',
    #     description='Typ:'
    # )

    return filter_widgets


def erstelle_visualisierung_widgets() -> dict[str, widgets.Widget]:
    """
    AUFGABE 3: Erstellen Sie Widgets für Visualisierungsoptionen

    Erstellen Sie folgende Widgets:
    - Dropdown für Y-Achse Parameter
    - RadioButtons für Diagrammtyp (Boxplot, Histogram, Scatter)
    - Checkbox für Trendlinie anzeigen
    - IntSlider für Anzahl Bins (bei Histogram)

    Returns:
        Dictionary mit Visualisierungs-Widgets
    """
    if not WIDGETS_AVAILABLE:
        return {}

    viz_widgets = {}

    # TODO: Implementieren Sie die Visualisierungs-Widgets

    return viz_widgets


def filtere_daten(data: pd.DataFrame, filter_values: dict) -> pd.DataFrame:
    """
    AUFGABE 4: Implementieren Sie die Datenfilterung

    Filtern Sie die Daten basierend auf den Widget-Werten:
    - Nach Maschinentyp (wenn nicht "Alle")
    - Nach Status (MultiSelect)
    - Nach Temperaturbereich
    - Nach Schicht
    - Nach aktivem Status

    Args:
        data: Original DataFrame
        filter_values: Dictionary mit Filter-Werten aus Widgets

    Returns:
        Gefilterte Daten
    """
    gefilterte_daten = data.copy()

    # TODO: Implementieren Sie die Filterlogik
    # Beispiel:
    # if filter_values.get('typ') != 'Alle':
    #     gefilterte_daten = gefilterte_daten[
    #         gefilterte_daten['Typ'] == filter_values['typ']
    #     ]

    return gefilterte_daten


def erstelle_diagramm(data: pd.DataFrame, viz_options: dict) -> None:
    """
    AUFGABE 5: Erstellen Sie verschiedene Diagrammtypen

    Implementieren Sie folgende Diagrammtypen:
    - Boxplot: Verteilung nach Maschinentyp
    - Histogram: Häufigkeitsverteilung
    - Scatter: Korrelation zwischen zwei Parametern

    Args:
        data: Gefilterte Daten
        viz_options: Visualisierungsoptionen aus Widgets
    """
    if data.empty:
        print("⚠️ Keine Daten für die gewählten Filter verfügbar")
        return

    plt.figure(figsize=(12, 6))

    # TODO: Implementieren Sie die verschiedenen Diagrammtypen
    # Beispiel für Boxplot:
    # if viz_options.get('diagramm_typ') == 'Boxplot':
    #     data.boxplot(column=viz_options['y_parameter'], by='Typ')
    #     plt.title(f'{viz_options["y_parameter"]} nach Maschinentyp')

    plt.tight_layout()
    plt.show()


def berechne_statistiken(data: pd.DataFrame) -> pd.DataFrame:
    """
    AUFGABE 6: Berechnen Sie Statistiken für das Dashboard

    Berechnen Sie folgende Statistiken gruppiert nach Maschinentyp:
    - Anzahl Maschinen
    - Durchschnittliche Temperatur
    - Durchschnittliche Effizienz
    - Anzahl aktive/wartung/stillstand
    - Standardabweichung der wichtigsten Parameter

    Args:
        data: Gefilterte Daten

    Returns:
        DataFrame mit Statistiken
    """
    if data.empty:
        return pd.DataFrame()

    # TODO: Implementieren Sie die Statistik-Berechnung
    statistiken = pd.DataFrame()

    return statistiken


def erstelle_interaktives_dashboard(data: pd.DataFrame) -> widgets.Widget | None:
    """
    AUFGABE 7: Kombinieren Sie alle Komponenten zu einem Dashboard

    Erstellen Sie ein vollständiges interaktives Dashboard mit:
    - Filter-Widgets oben
    - Visualisierungs-Optionen in der Mitte
    - Diagramm-Output unten
    - Statistik-Tabelle rechts

    Args:
        data: Maschinendaten

    Returns:
        Vollständiges Dashboard-Widget
    """
    if not WIDGETS_AVAILABLE:
        print("⚠️ ipywidgets nicht verfügbar")
        return None

    # Widgets erstellen
    filter_widgets = erstelle_filter_widgets(data)
    viz_widgets = erstelle_visualisierung_widgets()

    # Output-Bereiche
    plot_output = widgets.Output()
    stats_output = widgets.Output()

    def update_dashboard(*args):
        """Aktualisiert das Dashboard bei Widget-Änderungen"""
        # TODO: Implementieren Sie die Update-Logik

        with plot_output:
            plot_output.clear_output(wait=True)
            # Daten filtern und visualisieren

        with stats_output:
            stats_output.clear_output(wait=True)
            # Statistiken berechnen und anzeigen

    # TODO: Event-Handler für alle Widgets registrieren

    # TODO: Layout erstellen und zurückgeben
    dashboard = widgets.VBox(
        [
            widgets.HTML("<h2>🏭 SmartFactory Maschinen-Dashboard</h2>"),
            # TODO: Fügen Sie Widgets und Layout hinzu
        ]
    )

    # Initialer Update
    update_dashboard()

    return dashboard


def validiere_implementierung():
    """
    AUFGABE 8: Testen Sie Ihre Implementierung

    Erstellen Sie Tests für Ihre Funktionen:
    - Testen Sie die Datenerstellung
    - Validieren Sie die Filterung
    - Prüfen Sie die Statistik-Berechnung
    """
    print("🧪 Teste Implementierung...")

    # Test 1: Datenerstellung
    try:
        test_data = erstelle_maschinendaten(50)
        assert not test_data.empty, "Daten sollten nicht leer sein"
        assert len(test_data) == 50, "Falsche Anzahl Datenpunkte"
        print("✅ Test 1: Datenerstellung erfolgreich")
    except Exception as e:
        print(f"❌ Test 1 fehlgeschlagen: {e}")

    # Test 2: Widget-Erstellung
    try:
        test_data = erstelle_maschinendaten(10)
        filter_widgets = erstelle_filter_widgets(test_data)
        viz_widgets = erstelle_visualisierung_widgets()
        print("✅ Test 2: Widget-Erstellung erfolgreich")
    except Exception as e:
        print(f"❌ Test 2 fehlgeschlagen: {e}")

    # TODO: Fügen Sie weitere Tests hinzu

    print("🎯 Implementierung getestet!")


def erweiterte_aufgaben():
    """
    BONUS-AUFGABEN für fortgeschrittene Studierende:

    1. Fügen Sie Echtzeit-Updates hinzu (simuliert mit Timer)
    2. Implementieren Sie Export-Funktionalität für Diagramme
    3. Erstellen Sie ein Alarm-System für kritische Werte
    4. Fügen Sie Vorhersage-Funktionalität hinzu
    5. Implementieren Sie Daten-Import aus CSV-Dateien
    """
    print("🚀 Erweiterte Aufgaben:")
    print("1. Echtzeit-Updates mit Timer-Widget")
    print("2. Export-Funktionalität für Diagramme")
    print("3. Alarm-System für kritische Werte")
    print("4. Vorhersage-Funktionalität")
    print("5. CSV-Import-Funktionalität")


if __name__ == "__main__":
    print("📚 Jupyter Widgets Übung - SmartFactory")
    print("=" * 50)

    if not WIDGETS_AVAILABLE:
        print("⚠️ Installieren Sie ipywidgets für die vollständige Übung:")
        print("   pip install ipywidgets")
        print("   jupyter nbextension enable --py widgetsnbextension")
        return

    print("🎯 Aufgaben:")
    print("1. Implementieren Sie erstelle_maschinendaten()")
    print("2. Erstellen Sie Filter-Widgets")
    print("3. Implementieren Sie Visualisierungs-Widgets")
    print("4. Programmieren Sie die Datenfilterung")
    print("5. Erstellen Sie verschiedene Diagrammtypen")
    print("6. Berechnen Sie Statistiken")
    print("7. Kombinieren Sie alles zu einem Dashboard")
    print("8. Testen Sie Ihre Implementierung")

    # Beispiel-Ausführung
    print("\n🔧 Teste Basis-Funktionalität...")
    test_data = erstelle_maschinendaten(20)
    print(f"📊 {len(test_data)} Datenpunkte erstellt")

    if len(test_data.columns) > 1:  # Wenn implementiert
        dashboard = erstelle_interaktives_dashboard(test_data)
        if dashboard:
            print("📈 Dashboard erstellt - bereit für Jupyter Notebook!")
            # display(dashboard)  # Uncomment in Jupyter

    print("\n🧪 Führen Sie validiere_implementierung() aus, um Ihre Lösung zu testen")
    print("🚀 Schauen Sie sich erweiterte_aufgaben() für Bonus-Challenges an")
