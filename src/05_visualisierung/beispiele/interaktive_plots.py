#!/usr/bin/env python3
"""
Interaktive Plots - Beispielskript für dynamische Visualisierungen

Dieses Skript demonstriert die Erstellung interaktiver Visualisierungen
mit Matplotlib Widgets und verschiedenen Interaktionsmöglichkeiten
für Bystronic-Anwendungen.

Autor: Python Grundkurs Bystronic
"""

import warnings

import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import numpy as np
from matplotlib.animation import FuncAnimation

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")


def main() -> None:
    """Hauptfunktion für interaktive Plots"""
    print("=" * 70)
    print("BYSTRONIC - INTERAKTIVE VISUALISIERUNGEN")
    print("=" * 70)

    print("\n🎮 Interaktive Funktionen:")
    print("- Slider zur Parameteränderung")
    print("- Zoom und Pan in Plots")
    print("- Animationen und Updates")
    print("- Button-Interaktionen")
    print("\nWählen Sie eine Demo:")
    print("1️⃣ Interaktive Parameteranpassung")
    print("2️⃣ Animation: Produktionsprozess")
    print("3️⃣ Zoom und Pan Demo")
    print("4️⃣ Alle Demos nacheinander")

    choice = input("\nIhre Wahl (1-4): ").strip()

    if choice == "1":
        demo_interactive_parameters()
    elif choice == "2":
        demo_animation()
    elif choice == "3":
        demo_zoom_pan()
    elif choice == "4":
        demo_interactive_parameters()
        demo_animation()
        demo_zoom_pan()
    else:
        print("Ungültige Eingabe. Starte alle Demos...")
        demo_interactive_parameters()
        demo_animation()
        demo_zoom_pan()

    print(f"\n{'=' * 70}")
    print("✅ Interaktive Visualisierungen erfolgreich demonstriert!")
    print("🎮 Verschiedene Interaktionsmöglichkeiten für Benutzer")
    print("🔄 Dynamische Updates und Animationen")


def demo_interactive_parameters() -> None:
    """Interaktive Parameteranpassung mit Slidern"""
    print("\n1️⃣ Interaktive Parameteranpassung")
    print("-" * 40)
    print("Verwenden Sie die Slider zur Anpassung der Schneidparameter!")

    # Daten für Schneidprozess
    x = np.linspace(0, 10, 1000)

    # Subplot-Layout erstellen
    fig, ax = plt.subplots(figsize=(12, 8))
    plt.subplots_adjust(bottom=0.3)

    # Initiale Parameter
    initial_speed = 100  # mm/min
    initial_power = 80  # %
    initial_freq = 20  # kHz

    # Initiale Berechnung der Schnittqualität
    def calculate_quality(speed: float, power: float, frequency: float) -> np.ndarray:
        """Berechnet die Schnittqualität basierend auf Parametern"""
        # Vereinfachtes Modell
        base_quality = 90
        speed_effect = -0.2 * (speed - 100) ** 2 / 1000
        power_effect = -0.1 * (power - 80) ** 2 / 100
        freq_effect = 5 * np.sin(frequency * x / 10)
        noise = np.random.normal(0, 1, len(x))

        quality = base_quality + speed_effect + power_effect + freq_effect + noise
        return np.clip(quality, 70, 100)

    # Initiale Plots
    (line1,) = ax.plot(
        x,
        calculate_quality(initial_speed, initial_power, initial_freq),
        "b-",
        linewidth=2,
        label="Schnittqualität",
    )
    (line2,) = ax.plot(x, [85] * len(x), "r--", linewidth=2, label="Mindestqualität")

    ax.set_xlim(0, 10)
    ax.set_ylim(70, 100)
    ax.set_xlabel("Position (m)")
    ax.set_ylabel("Qualität (%)")
    ax.set_title("Schneidqualität in Echtzeit", fontsize=14, fontweight="bold")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Slider erstellen
    ax_speed = plt.axes([0.2, 0.15, 0.5, 0.03])
    slider_speed = widgets.Slider(
        ax_speed,
        "Geschwindigkeit (mm/min)",
        50,
        200,
        valinit=initial_speed,
        valfmt="%d",
    )

    ax_power = plt.axes([0.2, 0.1, 0.5, 0.03])
    slider_power = widgets.Slider(
        ax_power, "Laserleistung (%)", 50, 100, valinit=initial_power, valfmt="%d"
    )

    ax_freq = plt.axes([0.2, 0.05, 0.5, 0.03])
    slider_freq = widgets.Slider(
        ax_freq, "Frequenz (kHz)", 10, 50, valinit=initial_freq, valfmt="%d"
    )

    # Textfeld für Statistiken
    stats_text = ax.text(
        0.02,
        0.98,
        "",
        transform=ax.transAxes,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "lightblue", "alpha": 0.8},
    )

    # Update-Funktion
    def update_plot(val: float) -> None:
        """Aktualisiert den Plot basierend auf Slider-Werten"""
        speed = slider_speed.val
        power = slider_power.val
        freq = slider_freq.val

        # Neue Qualitätsdaten berechnen
        quality = calculate_quality(speed, power, freq)
        line1.set_ydata(quality)

        # Statistiken aktualisieren
        mean_quality = np.mean(quality)
        min_quality = np.min(quality)
        below_threshold = np.sum(quality < 85) / len(quality) * 100

        stats_text.set_text(
            f"Schnittparameter:\n"
            f"Geschw.: {speed:.0f} mm/min\n"
            f"Leistung: {power:.0f}%\n"
            f"Frequenz: {freq:.0f} kHz\n\n"
            f"Qualitätskennzahlen:\n"
            f"Ø Qualität: {mean_quality:.1f}%\n"
            f"Min. Qualität: {min_quality:.1f}%\n"
            f"Unter Grenze: {below_threshold:.1f}%"
        )

        # Farbe basierend auf Qualität ändern
        if mean_quality > 95:
            line1.set_color("green")
        elif mean_quality > 90:
            line1.set_color("blue")
        elif mean_quality > 85:
            line1.set_color("orange")
        else:
            line1.set_color("red")

        fig.canvas.draw_idle()

    # Slider mit Update-Funktion verbinden
    slider_speed.on_changed(update_plot)
    slider_power.on_changed(update_plot)
    slider_freq.on_changed(update_plot)

    # Reset-Button
    ax_reset = plt.axes([0.8, 0.15, 0.1, 0.04])
    button_reset = widgets.Button(ax_reset, "Reset")

    def reset_sliders(event) -> None:
        """Setzt alle Slider auf Initialwerte zurück"""
        slider_speed.reset()
        slider_power.reset()
        slider_freq.reset()

    button_reset.on_clicked(reset_sliders)

    # Initiale Statistiken anzeigen
    update_plot(0)

    print("📊 Slider-Kontrollen:")
    print("- Geschwindigkeit: Beeinflusst Gesamtqualität")
    print("- Laserleistung: Optimaler Bereich um 80%")
    print("- Frequenz: Erzeugt Oberflächenstrukturen")
    print("- Reset: Setzt alle Parameter zurück")

    plt.show()


def demo_animation() -> None:
    """Animierte Darstellung eines Produktionsprozesses"""
    print("\n2️⃣ Animation: Produktionsprozess")
    print("-" * 40)
    print("Beobachten Sie die Live-Simulation des Produktionsprozesses!")

    # Setup für Animation
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

    # Zeitachse
    time_data = []
    production_data = []
    temperature_data = []
    quality_data = []

    # Simulation Parameter
    max_points = 100
    time_step = 0.1

    # Plot-Initialisierung
    (line_production,) = ax1.plot([], [], "b-", linewidth=2, label="Stückzahl/h")
    (line_temp,) = ax1.plot([], [], "r-", linewidth=2, label="Temperatur (°C)")
    ax1_twin = ax1.twinx()
    (line_quality,) = ax1_twin.plot([], [], "g-", linewidth=2, label="Qualität (%)")

    ax1.set_xlim(0, max_points * time_step)
    ax1.set_ylim(0, 200)
    ax1_twin.set_ylim(80, 100)
    ax1.set_xlabel("Zeit (min)")
    ax1.set_ylabel("Produktion & Temperatur", color="b")
    ax1_twin.set_ylabel("Qualität (%)", color="g")
    ax1.set_title("Live Produktionsüberwachung", fontsize=14, fontweight="bold")
    ax1.grid(True, alpha=0.3)
    ax1.legend(loc="upper left")
    ax1_twin.legend(loc="upper right")

    # Histogramm für Qualitätsverteilung
    ax2.set_xlim(80, 100)
    ax2.set_ylim(0, 20)
    ax2.set_xlabel("Qualität (%)")
    ax2.set_ylabel("Häufigkeit")
    ax2.set_title("Qualitätsverteilung (Live)")

    # Status-Text
    status_text = fig.text(
        0.02,
        0.02,
        "",
        fontsize=10,
        bbox={"boxstyle": "round", "facecolor": "lightyellow"},
    )

    # Animation-Funktion
    def animate(frame: int) -> tuple:
        """Animationsschritt"""
        current_time = frame * time_step

        # Produktionsrate mit Zufallsschwankungen
        base_production = 120 + 30 * np.sin(current_time / 5)
        production = base_production + np.random.normal(0, 10)
        production = max(0, production)

        # Temperatur korreliert mit Produktion
        temperature = 150 + production * 0.2 + np.random.normal(0, 5)

        # Qualität hängt von Temperatur ab
        optimal_temp = 170
        temp_deviation = abs(temperature - optimal_temp)
        quality = 98 - temp_deviation * 0.1 + np.random.normal(0, 1)
        quality = np.clip(quality, 80, 100)

        # Daten hinzufügen
        time_data.append(current_time)
        production_data.append(production)
        temperature_data.append(temperature)
        quality_data.append(quality)

        # Maximale Anzahl Punkte begrenzen
        if len(time_data) > max_points:
            time_data.pop(0)
            production_data.pop(0)
            temperature_data.pop(0)
            quality_data.pop(0)

        # Plots aktualisieren
        line_production.set_data(time_data, production_data)
        line_temp.set_data(time_data, temperature_data)
        line_quality.set_data(time_data, quality_data)

        # Histogramm aktualisieren
        if len(quality_data) > 10:
            ax2.clear()
            ax2.hist(quality_data, bins=15, alpha=0.7, color="green", edgecolor="black")
            ax2.set_xlim(80, 100)
            ax2.set_xlabel("Qualität (%)")
            ax2.set_ylabel("Häufigkeit")
            ax2.set_title("Qualitätsverteilung (Live)")
            ax2.axvline(
                np.mean(quality_data),
                color="red",
                linestyle="--",
                label=f"Durchschnitt: {np.mean(quality_data):.1f}%",
            )
            ax2.legend()

        # Status aktualisieren
        if len(production_data) > 0:
            avg_production = np.mean(production_data[-10:])  # Letzte 10 Werte
            avg_quality = np.mean(quality_data[-10:])
            current_temp = temperature_data[-1]

            # Status bestimmen
            if avg_quality > 95 and avg_production > 100:
                status = "🟢 OPTIMAL"
            elif avg_quality > 90 and avg_production > 80:
                status = "🟡 GUT"
            else:
                status = "🔴 KRITISCH"

            status_text.set_text(
                f"Zeit: {current_time:.1f} min | "
                f"Produktion: {avg_production:.0f}/h | "
                f"Temp: {current_temp:.0f}°C | "
                f"Qualität: {avg_quality:.1f}% | "
                f"Status: {status}"
            )

        return line_production, line_temp, line_quality

    # Animation starten
    print("🎬 Starte Live-Animation...")
    print("- Produktionsrate schwankt um 120 Stück/h")
    print("- Temperatur beeinflusst die Qualität")
    print("- Schließen Sie das Fenster zum Beenden")

    FuncAnimation(fig, animate, frames=200, interval=200, blit=False, repeat=True)
    plt.tight_layout()
    plt.show()


def demo_zoom_pan() -> None:
    """Demonstration von Zoom und Pan Funktionalität"""
    print("\n3️⃣ Zoom und Pan Demo")
    print("-" * 40)
    print("Verwenden Sie Maus-Interaktionen:")
    print("- Linke Maustaste: Pan (Verschieben)")
    print("- Rechte Maustaste: Zoom")
    print("- Mausrad: Zoom")
    print("- 'r' Taste: Reset Zoom")

    # Komplexe Maschinendaten generieren
    np.random.seed(42)
    n_points = 5000
    t = np.linspace(0, 50, n_points)

    # Verschiedene Signale überlagern
    signal1 = 10 * np.sin(2 * np.pi * 0.5 * t)  # Langsame Schwingung
    signal2 = 5 * np.sin(2 * np.pi * 5 * t)  # Schnelle Schwingung
    signal3 = 2 * np.sin(2 * np.pi * 20 * t)  # Hochfrequenz
    noise = np.random.normal(0, 1, n_points)  # Rauschen

    # Kombiniertes Signal
    vibration = signal1 + signal2 + signal3 + noise

    # Plot erstellen
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

    # Haupt-Vibrationssignal
    ax1.plot(t, vibration, "b-", linewidth=0.8, alpha=0.7, label="Vibrationssignal")
    ax1.plot(t, signal1, "r--", linewidth=2, label="Grundschwingung")
    ax1.set_xlabel("Zeit (s)")
    ax1.set_ylabel("Amplitude (mm/s²)")
    ax1.set_title(
        "Maschinenvibration - Zoom/Pan möglich", fontsize=14, fontweight="bold"
    )
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Frequenzanalyse (vereinfacht)
    from scipy.fft import fft, fftfreq

    # FFT berechnen
    yf = fft(vibration)
    xf = fftfreq(n_points, t[1] - t[0])

    # Nur positive Frequenzen
    positive_freq_idx = xf > 0
    frequencies = xf[positive_freq_idx]
    amplitudes = 2.0 / n_points * np.abs(yf[positive_freq_idx])

    # Frequenzspektrum plotten
    ax2.plot(frequencies, amplitudes, "g-", linewidth=1)
    ax2.set_xlabel("Frequenz (Hz)")
    ax2.set_ylabel("Amplitude")
    ax2.set_title("Frequenzspektrum - Zoom für Details", fontsize=14, fontweight="bold")
    ax2.set_xlim(0, 30)
    ax2.grid(True, alpha=0.3)

    # Navigation toolbar aktivieren (automatisch verfügbar)
    # Zusätzliche Interaktivität

    # Klick-Event für Marker
    def on_click(event) -> None:
        """Behandelt Mausklicks für Marker-Platzierung"""
        if event.inaxes == ax1 and event.button == 2:  # Mittlere Maustaste
            ax1.axvline(event.xdata, color="red", linestyle=":", alpha=0.8)
            ax1.text(
                event.xdata,
                ax1.get_ylim()[1] * 0.9,
                f"{event.xdata:.2f}s",
                rotation=90,
                verticalalignment="top",
                fontsize=8,
            )
            fig.canvas.draw()
            print(f"Marker gesetzt bei: {event.xdata:.2f}s")

    # Key-Event für Reset
    def on_key(event) -> None:
        """Behandelt Tastendruck für Reset"""
        if event.key == "r":
            ax1.set_xlim(t[0], t[-1])
            ax1.set_ylim(np.min(vibration) * 1.1, np.max(vibration) * 1.1)
            ax2.set_xlim(0, 30)
            ax2.set_ylim(0, np.max(amplitudes) * 1.1)
            fig.canvas.draw()
            print("Zoom zurückgesetzt")
        elif event.key == "c":
            # Alle Marker löschen
            for line in ax1.lines[:]:
                if line.get_linestyle() == ":":
                    line.remove()
            for text in ax1.texts[:]:
                text.remove()
            fig.canvas.draw()
            print("Marker gelöscht")

    # Events verbinden
    fig.canvas.mpl_connect("button_press_event", on_click)
    fig.canvas.mpl_connect("key_press_event", on_key)

    # Informationsbox
    fig.text(
        0.02,
        0.98,
        "Interaktionen:\n"
        "• Linke Maus: Pan\n"
        "• Rechte Maus: Zoom\n"
        "• Mausrad: Zoom\n"
        "• Mittlere Maus: Marker\n"
        '• "r": Reset\n'
        '• "c": Clear Marker',
        fontsize=9,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "lightgreen", "alpha": 0.8},
    )

    plt.tight_layout()
    plt.show()

    print("\n📊 Analyse-Ergebnisse:")

    # Schwingungsanalyse
    max_amplitude = np.max(np.abs(vibration))
    rms_value = np.sqrt(np.mean(vibration**2))

    # Dominante Frequenzen finden
    peak_indices = np.argsort(amplitudes)[-3:]  # Top 3 Frequenzen
    dominant_freqs = frequencies[peak_indices]
    dominant_amps = amplitudes[peak_indices]

    print("Schwingungsanalyse:")
    print(f"  Max. Amplitude: {max_amplitude:.2f} mm/s²")
    print(f"  RMS-Wert: {rms_value:.2f} mm/s²")
    print("Dominante Frequenzen:")
    for freq, amp in zip(dominant_freqs, dominant_amps, strict=False):
        print(f"    {freq:.1f} Hz: {amp:.2f} mm/s²")

    # Bewertung
    if rms_value > 10:
        print("⚠️ Warnung: Hohe Vibrationen detected!")
    elif rms_value > 5:
        print("🟡 Achtung: Erhöhte Vibrationen")
    else:
        print("✅ Vibrationen im Normalbereich")


if __name__ == "__main__":
    # Import scipy für FFT prüfen
    try:
        import scipy.fft  # noqa: F401
    except ImportError:
        print("⚠️ Hinweis: scipy nicht installiert - Frequenzanalyse nicht verfügbar")
        print("Installation: pip install scipy")

    main()
