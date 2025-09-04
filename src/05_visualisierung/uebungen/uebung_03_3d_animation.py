#!/usr/bin/env python3
"""
3D-Visualisierung und Animationen - Übung 3

Diese Übung behandelt erweiterte 3D-Visualisierungen und Animationstechniken
für industrielle Anwendungen bei Bystronic.

Lernziele:
- 3D-Scatter-, Surface- und Mesh-Plots erstellen
- Animationen für Zeitreihendaten entwickeln
- Interaktive 3D-Navigation implementieren
- Räumliche Datenanalyse durchführen

Autor: Python Grundkurs Bystronic
"""

import warnings

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")

# Styling für professionelle Visualisierungen
plt.style.use("default")
plt.rcParams.update(
    {
        "font.size": 10,
        "axes.titlesize": 14,
        "axes.labelsize": 12,
        "figure.figsize": (12, 8),
    }
)


def aufgabe_1_3d_scatter() -> None:
    """
    Aufgabe 1: 3D-Scatter-Plot für Maschinendaten

    Erstelle einen 3D-Scatter-Plot, der die Beziehung zwischen
    Geschwindigkeit, Leistung und Qualität visualisiert.

    TODO für Kursteilnehmer:
    1. Generiere 200 Datenpunkte für Geschwindigkeit (50-150 mm/min)
    2. Generiere entsprechende Leistungswerte (1000-3000 W)
    3. Berechne Qualitätswerte basierend auf beiden Parametern
    4. Erstelle einen 3D-Scatter-Plot mit Farbkodierung
    5. Füge Achsenbeschriftungen und Titel hinzu
    """
    print("📊 Aufgabe 1: 3D-Scatter-Plot für Maschinendaten")
    print("-" * 50)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # Daten generieren
    np.random.seed(42)
    n_points = 200

    geschwindigkeit = np.random.uniform(50, 150, n_points)
    leistung = np.random.uniform(1000, 3000, n_points)

    # Qualität abhängig von Geschwindigkeit und Leistung
    # Optimum bei mittlerer Geschwindigkeit und hoher Leistung
    qualitaet = (
        95
        - 0.02 * (geschwindigkeit - 100) ** 2
        + 0.001 * (leistung - 1500)
        + np.random.normal(0, 2, n_points)
    )
    qualitaet = np.clip(qualitaet, 70, 100)

    # 3D-Plot erstellen
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection="3d")

    scatter = ax.scatter(
        geschwindigkeit,
        leistung,
        qualitaet,
        c=qualitaet,
        cmap="RdYlGn",
        s=60,
        alpha=0.7,
        edgecolors="black",
        linewidth=0.5,
    )

    # Achsenbeschriftungen
    ax.set_xlabel("Geschwindigkeit (mm/min)", fontsize=12)
    ax.set_ylabel("Leistung (W)", fontsize=12)
    ax.set_zlabel("Qualität (%)", fontsize=12)
    ax.set_title(
        "3D-Analyse: Geschwindigkeit vs. Leistung vs. Qualität", fontsize=14, pad=20
    )

    # Colorbar hinzufügen
    cbar = plt.colorbar(scatter, shrink=0.8, aspect=20)
    cbar.set_label("Qualität (%)", rotation=270, labelpad=20)

    # Optimaler Bereich markieren
    # Bester Qualitätsbereich
    best_mask = qualitaet > 95
    if np.any(best_mask):
        ax.scatter(
            geschwindigkeit[best_mask],
            leistung[best_mask],
            qualitaet[best_mask],
            c="gold",
            s=100,
            marker="*",
            edgecolors="black",
            linewidth=1,
            label="Optimal (>95%)",
        )
        ax.legend()

    plt.tight_layout()
    plt.show()

    # Statistiken ausgeben
    print(f"Datenpunkte analysiert: {n_points}")
    print(f"Durchschnittsqualität: {np.mean(qualitaet):.1f}%")
    print(
        f"Optimale Punkte (>95%): {np.sum(best_mask)} ({np.sum(best_mask) / n_points * 100:.1f}%)"
    )
    print(
        f"Korrelation Geschwindigkeit-Qualität: {np.corrcoef(geschwindigkeit, qualitaet)[0, 1]:.3f}"
    )
    print(
        f"Korrelation Leistung-Qualität: {np.corrcoef(leistung, qualitaet)[0, 1]:.3f}"
    )


def aufgabe_2_surface_plot() -> None:
    """
    Aufgabe 2: 3D-Surface-Plot für Temperaturverteilung

    Erstelle einen 3D-Surface-Plot, der die Temperaturverteilung
    auf einer Werkstückoberfläche zeigt.

    TODO für Kursteilnehmer:
    1. Erstelle ein 2D-Gitter für X/Y-Koordinaten (0-100mm)
    2. Definiere eine Temperaturfunktion mit Hotspots
    3. Erstelle einen Surface-Plot mit entsprechender Colormap
    4. Füge Konturlinien hinzu
    5. Implementiere interaktive Rotation
    """
    print("\n🌡️ Aufgabe 2: 3D-Surface-Plot für Temperaturverteilung")
    print("-" * 55)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # Koordinatengitter erstellen
    x = np.linspace(0, 100, 50)
    y = np.linspace(0, 100, 50)
    X, Y = np.meshgrid(x, y)

    # Temperaturverteilung mit mehreren Hotspots
    # Hotspot 1: Laserfokus bei (25, 25)
    hotspot1 = 150 * np.exp(-((X - 25) ** 2 + (Y - 25) ** 2) / 200)
    # Hotspot 2: Sekundärer Erhitzungspunkt bei (75, 75)
    hotspot2 = 120 * np.exp(-((X - 75) ** 2 + (Y - 75) ** 2) / 300)
    # Grundtemperatur mit leichtem Gradienten
    grundtemp = 20 + 0.3 * X + 0.2 * Y

    # Gesamttemperatur
    Z = grundtemp + hotspot1 + hotspot2

    # 3D-Surface-Plot
    fig = plt.figure(figsize=(15, 5))

    # Plot 1: Standard Surface Plot
    ax1 = fig.add_subplot(131, projection="3d")
    ax1.plot_surface(X, Y, Z, cmap="hot", alpha=0.9, linewidth=0.2, antialiased=True)
    ax1.set_title("Temperaturverteilung\n(Surface Plot)")
    ax1.set_xlabel("X-Position (mm)")
    ax1.set_ylabel("Y-Position (mm)")
    ax1.set_zlabel("Temperatur (°C)")

    # Plot 2: Wireframe mit Konturlinien
    ax2 = fig.add_subplot(132, projection="3d")
    ax2.plot_wireframe(X, Y, Z, alpha=0.6, color="blue", linewidth=0.5)
    # Konturlinien am Boden
    ax2.contour(X, Y, Z, levels=20, zdir="z", offset=np.min(Z) - 10, cmap="coolwarm")
    ax2.set_title("Wireframe mit\nKonturlinien")
    ax2.set_xlabel("X-Position (mm)")
    ax2.set_ylabel("Y-Position (mm)")
    ax2.set_zlabel("Temperatur (°C)")

    # Plot 3: Filled Contour (2D Projektion)
    ax3 = fig.add_subplot(133)
    contour_filled = ax3.contourf(X, Y, Z, levels=30, cmap="hot")
    contour_lines = ax3.contour(
        X, Y, Z, levels=15, colors="black", alpha=0.4, linewidths=0.5
    )
    ax3.clabel(contour_lines, inline=True, fontsize=8, fmt="%1.0f°C")
    ax3.set_title("2D-Konturplot")
    ax3.set_xlabel("X-Position (mm)")
    ax3.set_ylabel("Y-Position (mm)")

    # Colorbar für 2D-Plot
    plt.colorbar(contour_filled, ax=ax3, label="Temperatur (°C)")

    plt.tight_layout()
    plt.show()

    # Temperaturanalyse
    max_temp = np.max(Z)
    min_temp = np.min(Z)
    avg_temp = np.mean(Z)

    # Position der Maximaltemperatur
    max_pos = np.unravel_index(np.argmax(Z), Z.shape)
    max_x = X[max_pos]
    max_y = Y[max_pos]

    print("Temperaturanalyse:")
    print(f"  Maximaltemperatur: {max_temp:.1f}°C bei ({max_x:.1f}, {max_y:.1f}) mm")
    print(f"  Minimaltemperatur: {min_temp:.1f}°C")
    print(f"  Durchschnittstemperatur: {avg_temp:.1f}°C")
    print(f"  Temperaturgradient: {max_temp - min_temp:.1f}°C")


def aufgabe_3_animation_zeitreihe() -> None:
    """
    Aufgabe 3: Animierte Visualisierung von Zeitreihendaten

    Erstelle eine Animation, die die zeitliche Entwicklung
    von Produktionsparametern zeigt.

    TODO für Kursteilnehmer:
    1. Erstelle Zeitreihendaten für mehrere Parameter
    2. Implementiere eine Animation mit matplotlib.animation
    3. Zeige rollende Durchschnitte
    4. Füge Schwellenwerte und Alarmbereiche hinzu
    5. Speichere Animation als GIF (optional)
    """
    print("\n🎬 Aufgabe 3: Animierte Zeitreihen-Visualisierung")
    print("-" * 52)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # Zeitreihendaten generieren
    np.random.seed(42)
    time_points = 200
    time = np.linspace(0, 10, time_points)

    # Verschiedene Produktionsparameter simulieren
    # Geschwindigkeit mit Trend und Rauschen
    geschwindigkeit = 100 + 20 * np.sin(time * 2) + np.random.normal(0, 5, time_points)
    # Temperatur mit saisonalen Schwankungen
    temperatur = (
        75 + 10 * np.sin(time * 1.5 + np.pi / 4) + np.random.normal(0, 3, time_points)
    )
    # Qualität korreliert mit Temperaturstabilität
    qualitaet = 95 - 0.5 * np.abs(temperatur - 75) + np.random.normal(0, 2, time_points)
    qualitaet = np.clip(qualitaet, 80, 100)

    # Animation setup
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    fig.suptitle("Echtzeit-Produktionsmonitoring", fontsize=16, fontweight="bold")

    # Leere Linien für Animation
    (line1,) = ax1.plot([], [], "b-", linewidth=2, label="Geschwindigkeit")
    (line1_avg,) = ax1.plot([], [], "r--", linewidth=2, alpha=0.7, label="Ø 10 Punkte")

    (line2,) = ax2.plot([], [], "g-", linewidth=2, label="Temperatur")
    (line2_avg,) = ax2.plot(
        [], [], "orange", linestyle="--", linewidth=2, alpha=0.7, label="Ø 10 Punkte"
    )

    (line3,) = ax3.plot([], [], "purple", linewidth=2, label="Qualität")
    (line3_avg,) = ax3.plot(
        [], [], "red", linestyle="--", linewidth=2, alpha=0.7, label="Ø 10 Punkte"
    )

    # Achsen konfigurieren
    def setup_axes():
        # Geschwindigkeit
        ax1.set_xlim(0, 10)
        ax1.set_ylim(60, 140)
        ax1.set_ylabel("Geschwindigkeit\n(mm/min)")
        ax1.grid(True, alpha=0.3)
        ax1.legend(loc="upper right")
        ax1.axhline(y=120, color="red", linestyle=":", alpha=0.7, label="Maximal")
        ax1.axhline(y=80, color="red", linestyle=":", alpha=0.7, label="Minimal")

        # Temperatur
        ax2.set_xlim(0, 10)
        ax2.set_ylim(50, 100)
        ax2.set_ylabel("Temperatur\n(°C)")
        ax2.grid(True, alpha=0.3)
        ax2.legend(loc="upper right")
        ax2.axhspan(70, 80, color="green", alpha=0.1, label="Optimal")

        # Qualität
        ax3.set_xlim(0, 10)
        ax3.set_ylim(80, 100)
        ax3.set_ylabel("Qualität\n(%)")
        ax3.set_xlabel("Zeit (min)")
        ax3.grid(True, alpha=0.3)
        ax3.legend(loc="upper right")
        ax3.axhline(
            y=90, color="red", linestyle=":", alpha=0.7, label="Mindestqualität"
        )

    setup_axes()

    # Rollender Durchschnitt berechnen
    def rolling_average(data, window=10):
        """Berechnet rollenden Durchschnitt"""
        if len(data) < window:
            return data
        return np.convolve(data, np.ones(window) / window, mode="valid")

    # Animationsfunktion
    def animate(frame):
        """Update-Funktion für Animation"""
        # Anzahl der anzuzeigenden Punkte
        end_frame = min(frame + 1, len(time))

        if end_frame < 2:
            return line1, line1_avg, line2, line2_avg, line3, line3_avg

        # Aktuelle Daten
        current_time = time[:end_frame]
        current_speed = geschwindigkeit[:end_frame]
        current_temp = temperatur[:end_frame]
        current_qual = qualitaet[:end_frame]

        # Linien aktualisieren
        line1.set_data(current_time, current_speed)
        line2.set_data(current_time, current_temp)
        line3.set_data(current_time, current_qual)

        # Rollende Durchschnitte berechnen und anzeigen
        if end_frame >= 10:
            avg_speed = rolling_average(current_speed, 10)
            avg_temp = rolling_average(current_temp, 10)
            avg_qual = rolling_average(current_qual, 10)

            # Zeitpunkte für Durchschnitte (versetzt wegen rolling window)
            avg_time = current_time[9 : 9 + len(avg_speed)]

            line1_avg.set_data(avg_time, avg_speed)
            line2_avg.set_data(avg_time, avg_temp)
            line3_avg.set_data(avg_time, avg_qual)

        # Titel mit aktuellen Werten aktualisieren
        if end_frame > 0:
            current_values = (
                f"Aktuelle Werte - "
                f"Geschw: {current_speed[-1]:.1f} mm/min, "
                f"Temp: {current_temp[-1]:.1f}°C, "
                f"Qual: {current_qual[-1]:.1f}%"
            )
            fig.suptitle(
                f"Echtzeit-Produktionsmonitoring\n{current_values}",
                fontsize=14,
                fontweight="bold",
            )

        return line1, line1_avg, line2, line2_avg, line3, line3_avg

    print("Animation wird gestartet (dauert ca. 10 Sekunden)...")
    print("Schließen Sie das Fenster, um fortzufahren.")

    # Animation erstellen und starten
    anim = animation.FuncAnimation(
        fig, animate, frames=time_points, interval=50, blit=True, repeat=True
    )

    plt.tight_layout()
    plt.show()

    # Animation optional als GIF speichern
    # HINWEIS: Benötigt ImageMagick oder pillow
    save_gif = False  # Auf True setzen, um zu speichern
    if save_gif:
        try:
            anim.save("produktions_animation.gif", writer="pillow", fps=20)
            print("Animation als 'produktions_animation.gif' gespeichert!")
        except Exception as e:
            print(f"Animation konnte nicht gespeichert werden: {e}")

    # Finale Statistiken
    print("\nStatistische Auswertung der Zeitreihe:")
    print(
        f"  Geschwindigkeit: Ø {np.mean(geschwindigkeit):.1f} mm/min "
        f"(σ = {np.std(geschwindigkeit):.1f})"
    )
    print(f"  Temperatur: Ø {np.mean(temperatur):.1f}°C (σ = {np.std(temperatur):.1f})")
    print(f"  Qualität: Ø {np.mean(qualitaet):.1f}% (σ = {np.std(qualitaet):.1f})")


def aufgabe_4_interaktive_3d_rotation() -> None:
    """
    Aufgabe 4: Interaktive 3D-Objektrotation

    Erstelle eine interaktive 3D-Visualisierung eines Werkstücks
    mit automatischer Rotation und Benutzerinteraktion.

    TODO für Kursteilnehmer:
    1. Modelliere ein einfaches 3D-Werkstück (z.B. Würfel mit Löchern)
    2. Implementiere automatische Rotation
    3. Füge verschiedene Ansichtsmodi hinzu
    4. Erstelle eine Materialanalyse-Visualisierung
    5. Implementiere Zoom- und Pan-Funktionen
    """
    print("\n🔄 Aufgabe 4: Interaktive 3D-Rotation und Objektanalyse")
    print("-" * 58)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    def create_cube_with_holes():
        """Erstellt ein 3D-Werkstück: Würfel mit zylindrischen Bohrungen"""
        # Würfel-Grundgerüst (8 Eckpunkte)
        vertices = (
            np.array(
                [
                    [0, 0, 0],
                    [1, 0, 0],
                    [1, 1, 0],
                    [0, 1, 0],  # Untere Fläche
                    [0, 0, 1],
                    [1, 0, 1],
                    [1, 1, 1],
                    [0, 1, 1],  # Obere Fläche
                ]
            )
            * 50
        )  # Skalierung auf 50mm

        # Würfelkanten definieren
        edges = [
            [0, 1],
            [1, 2],
            [2, 3],
            [3, 0],  # Untere Fläche
            [4, 5],
            [5, 6],
            [6, 7],
            [7, 4],  # Obere Fläche
            [0, 4],
            [1, 5],
            [2, 6],
            [3, 7],  # Vertikale Kanten
        ]

        return vertices, edges

    def create_drilling_pattern():
        """Erstellt Bohrungsmuster für Werkstück"""
        # Bohrungspositionen (x, y, Durchmesser)
        bohrungen = [
            (15, 15, 8),  # Bohrung 1
            (35, 15, 6),  # Bohrung 2
            (15, 35, 6),  # Bohrung 3
            (35, 35, 10),  # Bohrung 4 (größer)
            (25, 25, 4),  # Zentrale kleine Bohrung
        ]
        return bohrungen

    # Werkstück erstellen
    vertices, edges = create_cube_with_holes()
    bohrungen = create_drilling_pattern()

    # Mehrere Ansichten in einem Dashboard
    fig = plt.figure(figsize=(16, 12))

    # Hauptansicht: Rotierendes Werkstück
    ax1 = fig.add_subplot(221, projection="3d")

    # Würfel zeichnen
    for edge in edges:
        points = vertices[edge]
        ax1.plot3D(points[:, 0], points[:, 1], points[:, 2], "b-", linewidth=2)

    # Eckpunkte markieren
    ax1.scatter(
        vertices[:, 0], vertices[:, 1], vertices[:, 2], color="red", s=100, alpha=0.8
    )

    # Bohrungen als Zylinder approximieren
    for x, y, durchmesser in bohrungen:
        # Zylindrische Bohrung durch Kreis an Ober- und Unterseite
        theta = np.linspace(0, 2 * np.pi, 20)
        radius = durchmesser / 2

        # Unterer Kreis (z=0)
        x_circle = x + radius * np.cos(theta)
        y_circle = y + radius * np.sin(theta)
        z_circle = np.zeros_like(theta)
        ax1.plot(x_circle, y_circle, z_circle, "r-", alpha=0.7, linewidth=1.5)

        # Oberer Kreis (z=50)
        z_circle_top = np.ones_like(theta) * 50
        ax1.plot(x_circle, y_circle, z_circle_top, "r-", alpha=0.7, linewidth=1.5)

        # Verbindungslinien (vereinfacht)
        for i in range(0, len(theta), 5):
            ax1.plot(
                [x_circle[i], x_circle[i]],
                [y_circle[i], y_circle[i]],
                [0, 50],
                "r--",
                alpha=0.5,
                linewidth=0.5,
            )

    ax1.set_title("3D-Werkstück mit Bohrungen", fontsize=12, fontweight="bold")
    ax1.set_xlabel("X (mm)")
    ax1.set_ylabel("Y (mm)")
    ax1.set_zlabel("Z (mm)")
    ax1.set_box_aspect([1, 1, 1])

    # Ansicht 2: Draufsicht (Bohrungsplan)
    ax2 = fig.add_subplot(222)

    # Werkstück als Rechteck
    rect = plt.Rectangle(
        (0, 0), 50, 50, linewidth=2, edgecolor="blue", facecolor="lightblue", alpha=0.3
    )
    ax2.add_patch(rect)

    # Bohrungen als Kreise
    for x, y, durchmesser in bohrungen:
        circle = plt.Circle((x, y), durchmesser / 2, color="red", alpha=0.7)
        ax2.add_patch(circle)
        # Durchmesser beschriften
        ax2.text(
            x,
            y,
            f"⌀{durchmesser}",
            ha="center",
            va="center",
            fontweight="bold",
            color="white",
            fontsize=8,
        )

    ax2.set_xlim(-5, 55)
    ax2.set_ylim(-5, 55)
    ax2.set_aspect("equal")
    ax2.set_title("Bohrungsplan (Draufsicht)", fontsize=12, fontweight="bold")
    ax2.set_xlabel("X (mm)")
    ax2.set_ylabel("Y (mm)")
    ax2.grid(True, alpha=0.3)

    # Ansicht 3: Materialanalyse
    ax3 = fig.add_subplot(223)

    # Materialvolumen berechnen
    gesamt_volumen = 50 * 50 * 50  # mm³
    bohrvolumen = sum(np.pi * (d / 2) ** 2 * 50 for _, _, d in bohrungen)
    material_volumen = gesamt_volumen - bohrvolumen

    # Balkendiagramm
    kategorien = ["Gesamtvolumen", "Materialvolumen", "Bohrvolumen"]
    volumina = [
        gesamt_volumen / 1000,
        material_volumen / 1000,
        bohrvolumen / 1000,
    ]  # in cm³
    farben = ["lightgray", "steelblue", "lightcoral"]

    bars = ax3.bar(kategorien, volumina, color=farben, alpha=0.8, edgecolor="black")

    # Werte auf Balken anzeigen
    for bar, vol in zip(bars, volumina, strict=False):
        ax3.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{vol:.1f} cm³",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    ax3.set_title("Materialvolumen-Analyse", fontsize=12, fontweight="bold")
    ax3.set_ylabel("Volumen (cm³)")
    ax3.grid(True, alpha=0.3, axis="y")

    # Ansicht 4: Rotationssequenz (verschiedene Blickwinkel)
    ax4 = fig.add_subplot(224, projection="3d")

    # Mehrere Rotationswinkel zeigen
    elevations = [20, 45, 70]
    azimuths = [0, 60, 120]
    colors = ["blue", "green", "red"]

    for i, (_elev, _azim, color) in enumerate(
        zip(elevations, azimuths, colors, strict=False)
    ):
        # Transparente Darstellung für überlagerte Ansichten
        alpha = 0.6 if i > 0 else 1.0

        for edge in edges:
            points = vertices[edge]
            ax4.plot3D(
                points[:, 0],
                points[:, 1],
                points[:, 2],
                color=color,
                alpha=alpha,
                linewidth=1.5,
            )

    ax4.set_title(
        "Mehrfach-Ansichten\n(Blau: 20°, Grün: 45°, Rot: 70°)",
        fontsize=10,
        fontweight="bold",
    )
    ax4.set_xlabel("X (mm)")
    ax4.set_ylabel("Y (mm)")
    ax4.set_zlabel("Z (mm)")

    plt.tight_layout()
    plt.show()

    # Detaillierte Analyse ausgeben
    print("Werkstück-Analyse:")
    print("  Abmessungen: 50 × 50 × 50 mm")
    print(f"  Gesamtvolumen: {gesamt_volumen / 1000:.1f} cm³")
    print(f"  Materialvolumen: {material_volumen / 1000:.1f} cm³")
    print(f"  Bohrvolumen: {bohrvolumen / 1000:.1f} cm³")
    print(f"  Materialanteil: {(material_volumen / gesamt_volumen * 100):.1f}%")
    print("\nBohrungsdetails:")

    for i, (x, y, d) in enumerate(bohrungen, 1):
        vol = np.pi * (d / 2) ** 2 * 50 / 1000  # cm³
        print(f"  Bohrung {i}: Position ({x}, {y}) mm, ⌀{d} mm, Volumen {vol:.2f} cm³")

    # Interaktive Rotation simulieren
    print("\n🔄 Für interaktive 3D-Rotation:")
    print("  - Mausklick + Ziehen: Objekt rotieren")
    print("  - Mausrad: Zoom")
    print("  - Rechtsklick + Ziehen: Pan")

    # Automatische Rotation demonstrieren (optional)
    demo_auto_rotation = False  # Auf True setzen für Demo
    if demo_auto_rotation:
        print("\nAutomatische Rotation wird demonstriert...")

        fig_rot = plt.figure(figsize=(10, 8))
        ax_rot = fig_rot.add_subplot(111, projection="3d")

        def animate_rotation(frame):
            ax_rot.clear()

            # Würfel neu zeichnen
            for edge in edges:
                points = vertices[edge]
                ax_rot.plot3D(
                    points[:, 0], points[:, 1], points[:, 2], "b-", linewidth=2
                )

            # Rotation einstellen
            ax_rot.view_init(elev=20, azim=frame * 6)  # 360° in 60 frames
            ax_rot.set_title(f"Automatische Rotation - Frame {frame}")
            ax_rot.set_xlabel("X (mm)")
            ax_rot.set_ylabel("Y (mm)")
            ax_rot.set_zlabel("Z (mm)")

            return []

        animation.FuncAnimation(
            fig_rot, animate_rotation, frames=60, interval=100, repeat=True
        )
        plt.show()


def aufgabe_5_bonus_volumetric() -> None:
    """
    Bonus-Aufgabe 5: Volumetrische Datenvisualisierung

    Erstelle eine erweiterte 3D-Visualisierung mit volumetrischen Daten,
    z.B. für Materialverteilungen oder Spannungsanalysen.

    TODO für Kursteilnehmer:
    1. Generiere 3D-Volumendaten (z.B. Spannungsverteilung)
    2. Erstelle Isoflächen für verschiedene Wertebereiche
    3. Implementiere Schnittebenen durch das Volumen
    4. Visualisiere Gradienten und Vektorfelder
    5. Füge interaktive Kontroller hinzu
    """
    print("\n🎁 Bonus-Aufgabe: Volumetrische 3D-Visualisierung")
    print("-" * 51)

    # TODO: Implementierung durch Kursteilnehmer
    # Beispiel-Lösung (kommentiert):

    # 3D-Volumendaten für Spannungsanalyse generieren
    x = np.linspace(-2, 2, 20)
    y = np.linspace(-2, 2, 20)
    z = np.linspace(-2, 2, 20)
    X, Y, Z = np.meshgrid(x, y, z)

    # Spannungsfeld simulieren (z.B. um eine zentrale Belastung)
    # Komplexere Spannungsverteilung
    stress_1 = 100 * np.exp(-(X**2 + Y**2 + Z**2))  # Zentrale Spannung
    stress_2 = 50 * np.exp(-((X - 1) ** 2 + (Y - 1) ** 2 + Z**2))  # Seitliche Spannung
    stress_field = stress_1 + stress_2

    # Mehrere Visualisierungsarten
    fig = plt.figure(figsize=(16, 12))

    # Plot 1: Isoflächen (vereinfacht mit Scatter)
    ax1 = fig.add_subplot(221, projection="3d")

    # Verschiedene Spannungsniveaus als Punktwolken
    levels = [20, 40, 60, 80]
    colors = ["blue", "green", "orange", "red"]
    alphas = [0.3, 0.4, 0.5, 0.6]

    for level, color, alpha in zip(levels, colors, alphas, strict=False):
        # Punkte finden, die nahe dem gewünschten Level sind
        mask = (stress_field >= level - 5) & (stress_field <= level + 5)
        if np.any(mask):
            ax1.scatter(
                X[mask],
                Y[mask],
                Z[mask],
                c=color,
                alpha=alpha,
                s=30,
                label=f"{level}±5 MPa",
            )

    ax1.set_title("Spannungsisoflächen", fontsize=12, fontweight="bold")
    ax1.set_xlabel("X (mm)")
    ax1.set_ylabel("Y (mm)")
    ax1.set_zlabel("Z (mm)")
    ax1.legend()

    # Plot 2: Schnittebene Z=0
    ax2 = fig.add_subplot(222)

    # Mittelschnitt durch Z=0
    z_idx = len(z) // 2
    stress_slice = stress_field[:, :, z_idx]
    X_slice = X[:, :, z_idx]
    Y_slice = Y[:, :, z_idx]

    contour = ax2.contourf(
        X_slice, Y_slice, stress_slice, levels=20, cmap="viridis", alpha=0.8
    )
    ax2.contour(
        X_slice,
        Y_slice,
        stress_slice,
        levels=10,
        colors="white",
        alpha=0.6,
        linewidths=0.5,
    )

    plt.colorbar(contour, ax=ax2, label="Spannung (MPa)")
    ax2.set_title(
        "Spannungsverteilung\n(Schnittebene Z=0)", fontsize=12, fontweight="bold"
    )
    ax2.set_xlabel("X (mm)")
    ax2.set_ylabel("Y (mm)")
    ax2.set_aspect("equal")

    # Plot 3: Gradient/Vektorfeld (2D-Projektion)
    ax3 = fig.add_subplot(223)

    # Gradienten berechnen (vereinfacht)
    dy, dx = np.gradient(stress_slice)

    # Vektorfeld mit reduzierter Dichte
    skip = 2
    ax3.quiver(
        X_slice[::skip, ::skip],
        Y_slice[::skip, ::skip],
        dx[::skip, ::skip],
        dy[::skip, ::skip],
        stress_slice[::skip, ::skip],
        cmap="plasma",
        alpha=0.8,
        scale=100,
    )

    ax3.set_title("Spannungsgradienten\n(Vektorfeld)", fontsize=12, fontweight="bold")
    ax3.set_xlabel("X (mm)")
    ax3.set_ylabel("Y (mm)")
    ax3.set_aspect("equal")

    # Plot 4: 3D-Spannungsverteilung mit Farbkodierung
    ax4 = fig.add_subplot(224, projection="3d")

    # Hochbelastete Bereiche hervorheben
    high_stress_mask = stress_field > 60
    medium_stress_mask = (stress_field > 30) & (stress_field <= 60)
    low_stress_mask = stress_field <= 30

    # Verschiedene Spannungsbereiche in verschiedenen Farben
    if np.any(high_stress_mask):
        ax4.scatter(
            X[high_stress_mask],
            Y[high_stress_mask],
            Z[high_stress_mask],
            c="red",
            alpha=0.8,
            s=50,
            label="Hoch (>60 MPa)",
        )

    if np.any(medium_stress_mask):
        ax4.scatter(
            X[medium_stress_mask],
            Y[medium_stress_mask],
            Z[medium_stress_mask],
            c="orange",
            alpha=0.6,
            s=30,
            label="Mittel (30-60 MPa)",
        )

    if np.any(low_stress_mask):
        ax4.scatter(
            X[low_stress_mask],
            Y[low_stress_mask],
            Z[low_stress_mask],
            c="blue",
            alpha=0.4,
            s=15,
            label="Niedrig (<30 MPa)",
        )

    ax4.set_title("3D-Spannungsklassifizierung", fontsize=12, fontweight="bold")
    ax4.set_xlabel("X (mm)")
    ax4.set_ylabel("Y (mm)")
    ax4.set_zlabel("Z (mm)")
    ax4.legend()

    plt.tight_layout()
    plt.show()

    # Volumetrische Analyse
    total_volume = len(x) * len(y) * len(z)
    high_stress_volume = np.sum(high_stress_mask)
    medium_stress_volume = np.sum(medium_stress_mask)
    low_stress_volume = np.sum(low_stress_mask)

    max_stress = np.max(stress_field)
    avg_stress = np.mean(stress_field)

    # Position der maximalen Spannung
    max_pos = np.unravel_index(np.argmax(stress_field), stress_field.shape)
    max_coords = (x[max_pos[2]], y[max_pos[1]], z[max_pos[0]])

    print("Volumetrische Spannungsanalyse:")
    print(f"  Maximale Spannung: {max_stress:.1f} MPa bei {max_coords}")
    print(f"  Durchschnittliche Spannung: {avg_stress:.1f} MPa")
    print("  Volumenverteilung:")
    print(f"    Hochbelastet (>60 MPa): {high_stress_volume / total_volume * 100:.1f}%")
    print(
        f"    Mittelbelastet (30-60 MPa): {medium_stress_volume / total_volume * 100:.1f}%"
    )
    print(
        f"    Niedrig belastet (<30 MPa): {low_stress_volume / total_volume * 100:.1f}%"
    )

    print("\n💡 Erweiterte Techniken für volumetrische Daten:")
    print("  - Marching Cubes Algorithmus für echte Isoflächen")
    print("  - Volume Rendering mit VTK oder PyVista")
    print("  - Interaktive Schnittebenen mit ipywidgets")
    print("  - GPU-beschleunigte Visualisierung")


def main() -> None:
    """Hauptfunktion für 3D-Visualisierung und Animationen"""
    print("=" * 70)
    print("BYSTRONIC - 3D-VISUALISIERUNG UND ANIMATIONEN")
    print("Übung 3: Erweiterte dreidimensionale Datenanalyse")
    print("=" * 70)

    # Übungsauswahl
    print("\nWählen Sie eine Aufgabe aus:")
    print("1️⃣  3D-Scatter-Plot für Maschinendaten")
    print("2️⃣  3D-Surface-Plot für Temperaturverteilung")
    print("3️⃣  Animierte Zeitreihen-Visualisierung")
    print("4️⃣  Interaktive 3D-Objektrotation")
    print("5️⃣  Bonus: Volumetrische Datenvisualisierung")
    print("0️⃣  Alle Aufgaben nacheinander ausführen")

    try:
        choice = input("\nIhre Wahl (0-5): ").strip()

        if choice == "1":
            aufgabe_1_3d_scatter()
        elif choice == "2":
            aufgabe_2_surface_plot()
        elif choice == "3":
            aufgabe_3_animation_zeitreihe()
        elif choice == "4":
            aufgabe_4_interaktive_3d_rotation()
        elif choice == "5":
            aufgabe_5_bonus_volumetric()
        elif choice == "0":
            print("\n🎯 Alle Aufgaben werden nacheinander ausgeführt...")
            print("\nSTART: Aufgabe 1")
            aufgabe_1_3d_scatter()

            input("\nDrücken Sie Enter für Aufgabe 2...")
            print("\nSTART: Aufgabe 2")
            aufgabe_2_surface_plot()

            input("\nDrücken Sie Enter für Aufgabe 3...")
            print("\nSTART: Aufgabe 3")
            aufgabe_3_animation_zeitreihe()

            input("\nDrücken Sie Enter für Aufgabe 4...")
            print("\nSTART: Aufgabe 4")
            aufgabe_4_interaktive_3d_rotation()

            input("\nDrücken Sie Enter für Bonus-Aufgabe...")
            print("\nSTART: Bonus-Aufgabe")
            aufgabe_5_bonus_volumetric()
        else:
            print("❌ Ungültige Eingabe. Programm wird beendet.")
            return

    except KeyboardInterrupt:
        print("\n\n⏸️ Programm durch Benutzer unterbrochen.")
        return
    except EOFError:
        print("\n\n🤖 Automatischer Modus: Alle Aufgaben werden ausgeführt...")
        aufgabe_1_3d_scatter()
        aufgabe_2_surface_plot()
        aufgabe_3_animation_zeitreihe()
        aufgabe_4_interaktive_3d_rotation()
        aufgabe_5_bonus_volumetric()

    print(f"\n{'=' * 70}")
    print("✅ 3D-Visualisierung und Animationen erfolgreich abgeschlossen!")
    print("📈 Erweiterte Kenntnisse in dreidimensionaler Datenanalyse erworben")
    print("🎨 Professionelle 3D-Plots für Bystronic-Anwendungen entwickelt")
    print("🎬 Animationstechniken für dynamische Visualisierungen implementiert")
    print("🔄 Interaktive 3D-Navigation und Rotation gemeistert")
    print("💎 Volumetrische Datenvisualisierung als Bonus-Skill erlernt")

    print("\n📚 Weiterführende Ressourcen:")
    print(
        "• Matplotlib 3D: https://matplotlib.org/stable/tutorials/toolkits/mplot3d.html"
    )
    print("• Animation Guide: https://matplotlib.org/stable/api/animation_api.html")
    print("• PyVista für erweiterte 3D: https://docs.pyvista.org/")
    print("• Plotly 3D: https://plotly.com/python/3d-charts/")


if __name__ == "__main__":
    main()
