#!/usr/bin/env python3
"""
Jupyter Widgets Demo für SmartFactory

Demonstriert die Verwendung von ipywidgets für interaktive Notebooks.
Dieses Modul kann sowohl in Jupyter Notebooks als auch für Tests verwendet werden.
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    import ipywidgets as widgets
    from IPython.display import display

    WIDGETS_AVAILABLE = True
except ImportError:
    WIDGETS_AVAILABLE = False


def create_sample_machine_data(n_samples: int = 100) -> pd.DataFrame:
    """
    Erstellt Beispiel-Maschinendaten für Demonstrationszwecke.

    Args:
        n_samples: Anzahl der zu generierenden Datenpunkte

    Returns:
        DataFrame mit Maschinendaten
    """
    np.random.seed(42)

    machines = ["Laser_A", "Laser_B", "Presse_C", "Presse_D"]

    data = {
        "Maschine": np.random.choice(machines, n_samples),
        "Temperatur": np.random.normal(65, 8, n_samples),
        "Effizienz": np.random.normal(85, 12, n_samples),
        "Produktionszeit": np.random.exponential(2.5, n_samples),
        "Status": np.random.choice(
            ["Aktiv", "Wartung", "Stillstand"], n_samples, p=[0.7, 0.2, 0.1]
        ),
    }

    df = pd.DataFrame(data)

    # Realistische Constraints
    df["Temperatur"] = np.clip(df["Temperatur"], 40, 90)
    df["Effizienz"] = np.clip(df["Effizienz"], 50, 100)
    df["Produktionszeit"] = np.clip(df["Produktionszeit"], 0.1, 10)

    return df


def create_interactive_dashboard(data: pd.DataFrame) -> widgets.Widget | None:
    """
    Erstellt ein interaktives Dashboard mit Widgets.

    Args:
        data: DataFrame mit Maschinendaten

    Returns:
        Widget-Container oder None wenn Widgets nicht verfügbar
    """
    if not WIDGETS_AVAILABLE:
        print("⚠️ ipywidgets nicht verfügbar - Dashboard kann nicht erstellt werden")
        return None

    # Prüfe ob Daten vorhanden und gültig sind
    required_columns = ["Maschine", "Status"]
    if (
        data is None
        or data.empty
        or not all(col in data.columns for col in required_columns)
    ):
        print("⚠️ Keine gültigen Maschinendaten - Dashboard kann nicht erstellt werden")
        return None

    # Widget-Definitionen
    machine_dropdown = widgets.Dropdown(
        options=["Alle"] + list(data["Maschine"].unique()),
        value="Alle",
        description="Maschine:",
    )

    # Verfügbare Parameter basierend auf vorhandenen Spalten
    available_params = [
        col
        for col in ["Temperatur", "Effizienz", "Produktionszeit"]
        if col in data.columns
    ]
    if not available_params:
        available_params = ["Wert"]  # Fallback

    parameter_dropdown = widgets.Dropdown(
        options=available_params,
        value=available_params[0],
        description="Parameter:",
    )

    status_checkbox = widgets.SelectMultiple(
        options=list(data["Status"].unique()),
        value=list(data["Status"].unique()),
        description="Status:",
    )

    output = widgets.Output()

    def update_plot(*args):
        """Aktualisiert den Plot basierend auf Widget-Werten"""
        with output:
            output.clear_output(wait=True)

            # Daten filtern
            filtered_data = data.copy()

            if machine_dropdown.value != "Alle":
                filtered_data = filtered_data[
                    filtered_data["Maschine"] == machine_dropdown.value
                ]

            filtered_data = filtered_data[
                filtered_data["Status"].isin(status_checkbox.value)
            ]

            if len(filtered_data) == 0:
                print("Keine Daten für die gewählten Filter verfügbar")
                return

            # Plot erstellen
            plt.figure(figsize=(10, 6))

            if machine_dropdown.value == "Alle":
                # Boxplot für alle Maschinen
                machines = filtered_data["Maschine"].unique()
                data_by_machine = [
                    filtered_data[filtered_data["Maschine"] == m][
                        parameter_dropdown.value
                    ]
                    for m in machines
                ]
                plt.boxplot(data_by_machine, labels=machines)
                plt.title(f"{parameter_dropdown.value} nach Maschine")
            else:
                # Histogram für eine Maschine
                plt.hist(
                    filtered_data[parameter_dropdown.value],
                    bins=20,
                    alpha=0.7,
                    edgecolor="black",
                )
                plt.title(f"{parameter_dropdown.value} - {machine_dropdown.value}")

            plt.xlabel(
                "Maschine"
                if machine_dropdown.value == "Alle"
                else parameter_dropdown.value
            )
            plt.ylabel("Wert" if machine_dropdown.value == "Alle" else "Häufigkeit")
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()

            # Statistiken anzeigen
            stats = (
                filtered_data.groupby("Maschine")[parameter_dropdown.value]
                .agg(["count", "mean", "std"])
                .round(2)
            )
            print(f"\n📊 Statistiken für {parameter_dropdown.value}:")
            print(stats)

    # Event-Handler registrieren
    machine_dropdown.observe(update_plot, names="value")
    parameter_dropdown.observe(update_plot, names="value")
    status_checkbox.observe(update_plot, names="value")

    # Initialer Plot
    update_plot()

    # Layout erstellen
    controls = widgets.HBox([machine_dropdown, parameter_dropdown])
    dashboard = widgets.VBox(
        [
            widgets.HTML("<h3>🏭 SmartFactory Maschinen-Dashboard</h3>"),
            controls,
            status_checkbox,
            output,
        ]
    )

    return dashboard


def create_simple_widgets() -> dict[str, widgets.Widget]:
    """
    Erstellt einfache Widget-Beispiele für Demonstrationszwecke.

    Returns:
        Dictionary mit verschiedenen Widget-Typen
    """
    if not WIDGETS_AVAILABLE:
        return {}

    widget_examples = {
        "slider": widgets.IntSlider(
            value=50, min=0, max=100, step=1, description="Wert:"
        ),
        "text": widgets.Text(value="SmartFactory", description="Firma:"),
        "button": widgets.Button(
            description="Verarbeiten", button_style="success", icon="check"
        ),
        "checkbox": widgets.Checkbox(value=True, description="Aktiv"),
        "dropdown": widgets.Dropdown(
            options=["Option A", "Option B", "Option C"],
            value="Option A",
            description="Auswahl:",
        ),
    }

    return widget_examples


def demonstrate_magic_commands() -> list[str]:
    """
    Demonstriert verschiedene Magic Commands (als Strings für Tests).

    Returns:
        Liste von Magic Command Beispielen
    """
    magic_examples = [
        "%time result = sum(range(1000))",
        "%matplotlib inline",
        "%load_ext autoreload",
        "%autoreload 2",
        "%%time\n# Zeitbasierte Messung\nfor i in range(100000):\n    pass",
        "%%writefile example.py\n# Datei schreiben\nprint('Hello SmartFactory!')",
        "%%bash\nls -la\npwd",
    ]

    return magic_examples


def validate_notebook_security(notebook_content: str) -> dict[str, bool]:
    """
    Validiert Notebook-Inhalte auf Sicherheitsrisiken.

    Args:
        notebook_content: Notebook-Inhalt als String

    Returns:
        Dictionary mit Validierungsergebnissen
    """
    dangerous_patterns = [
        "import os",
        "subprocess",
        "!rm",
        "!sudo",
        "eval(",
        "exec(",
        "__import__",
        "open(",
        "file(",
    ]

    results = {"safe": True, "warnings": [], "blocked_patterns": []}

    for pattern in dangerous_patterns:
        if pattern in notebook_content:
            results["safe"] = False
            results["blocked_patterns"].append(pattern)
            results["warnings"].append(f"Gefährliches Pattern gefunden: {pattern}")

    return results


def performance_test_function(n: int = 1000000) -> float:
    """
    Testfunktion für Performance-Messungen.

    Args:
        n: Anzahl der Iterationen

    Returns:
        Berechnetes Ergebnis
    """
    import time

    start_time = time.time()

    result = sum(i**2 for i in range(n))

    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time


if __name__ == "__main__":
    print("🚀 Jupyter Widgets Demo für SmartFactory")
    print("=" * 50)

    # Beispieldaten erstellen
    data = create_sample_machine_data(200)
    print(f"✅ {len(data)} Datenpunkte generiert")
    print(f"📊 Maschinen: {list(data['Maschine'].unique())}")

    # Widget-Verfügbarkeit prüfen
    if WIDGETS_AVAILABLE:
        print("✅ ipywidgets verfügbar")

        # Einfache Widgets demonstrieren
        simple_widgets = create_simple_widgets()
        print(f"📱 {len(simple_widgets)} Widget-Typen erstellt")

        # Dashboard erstellen (nur in Jupyter-Umgebung sinnvoll)
        dashboard = create_interactive_dashboard(data)
        if dashboard:
            print("📈 Interaktives Dashboard erstellt")
    else:
        print("⚠️ ipywidgets nicht verfügbar - nur Basis-Funktionen")

    # Magic Commands demonstrieren
    magic_commands = demonstrate_magic_commands()
    print(f"🪄 {len(magic_commands)} Magic Command Beispiele")

    # Sicherheitsvalidierung
    test_content = "import pandas as pd\nprint('Hello')"
    security_check = validate_notebook_security(test_content)
    print(
        f"🔒 Sicherheitscheck: {'✅ Sicher' if security_check['safe'] else '⚠️ Risiken gefunden'}"
    )

    # Performance-Test
    perf_time = performance_test_function(100000)
    print(f"⚡ Performance-Test: {perf_time:.4f}s")

    print("\n🎯 Demo abgeschlossen!")
