#!/usr/bin/env python3
"""
3D-Visualisierung - Beispielskript für räumliche Darstellungen

Dieses Skript demonstriert verschiedene 3D-Visualisierungstechniken
mit Matplotlib für industrielle Anwendungen bei Bystronic.
Fokus auf räumliche Daten, Oberflächen und interaktive 3D-Modelle.

Autor: Python Grundkurs Bystronic
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")


def main() -> None:
    """Hauptfunktion für 3D-Visualisierungen"""
    print("=" * 70)
    print("BYSTRONIC - 3D VISUALISIERUNGEN")
    print("=" * 70)

    print("\n🎯 3D-Visualisierungsarten:")
    print("- 3D-Scatterplots für Messpunkte")
    print("- Oberflächenplots für Spannungsfelder")
    print("- Drahtgitter-Modelle")
    print("- Volumetrische Darstellungen")
    print("- Interaktive 3D-Navigation")

    # 1. 3D Scatter Plots
    print("\n1️⃣ 3D Scatterplots")
    print("-" * 40)
    demo_3d_scatter()

    # 2. Oberflächenplots
    print("\n2️⃣ 3D-Oberflächenplots")
    print("-" * 40)
    demo_surface_plots()

    # 3. Drahtgitter und Konturen
    print("\n3️⃣ Drahtgitter-Modelle")
    print("-" * 40)
    demo_wireframe()

    # 4. Volumetrische Daten
    print("\n4️⃣ Volumetrische Darstellungen")
    print("-" * 40)
    demo_volumetric()

    # 5. Animierte 3D-Plots
    print("\n5️⃣ Animierte 3D-Visualisierungen")
    print("-" * 40)
    demo_animated_3d()

    print(f"\n{'=' * 70}")
    print("✅ 3D-Visualisierungen erfolgreich demonstriert!")
    print("🔄 Interaktive Navigation mit Maus möglich")
    print("📐 Räumliche Datenanalyse für industrielle Anwendungen")


def demo_3d_scatter() -> None:
    """3D Scatterplots für Messpunkte und Qualitätsdaten"""
    # Simulierte Messpunkte von Werkstücken
    np.random.seed(42)
    n_points = 200

    # Koordinaten der Messpunkte
    x = np.random.uniform(0, 100, n_points)  # X-Position in mm
    y = np.random.uniform(0, 50, n_points)  # Y-Position in mm
    z = np.random.uniform(0, 20, n_points)  # Z-Position in mm

    # Qualitätswerte basierend auf Position
    # Qualität nimmt zu den Rändern ab
    center_x, center_y, center_z = 50, 25, 10
    distance_from_center = np.sqrt(
        (x - center_x) ** 2 + (y - center_y) ** 2 + (z - center_z) ** 2
    )
    quality = 100 - distance_from_center * 0.5 + np.random.normal(0, 3, n_points)
    quality = np.clip(quality, 70, 100)

    # Defekte simulieren (niedrige Qualität)
    defect_indices = np.random.choice(n_points, 15, replace=False)
    quality[defect_indices] = np.random.uniform(60, 75, 15)

    # 3D Plot erstellen
    fig = plt.figure(figsize=(15, 12))

    # Hauptplot - Qualitätsverteilung
    ax1 = fig.add_subplot(221, projection="3d")
    scatter = ax1.scatter(
        x,
        y,
        z,
        c=quality,
        cmap="RdYlGn",
        s=50,
        alpha=0.8,
        edgecolors="black",
        linewidth=0.5,
    )

    ax1.set_xlabel("X-Position (mm)", fontsize=12)
    ax1.set_ylabel("Y-Position (mm)", fontsize=12)
    ax1.set_zlabel("Z-Position (mm)", fontsize=12)
    ax1.set_title("3D Qualitätsmessung Werkstück", fontsize=14, fontweight="bold")

    # Colorbar
    cbar = plt.colorbar(scatter, ax=ax1, shrink=0.8, aspect=20)
    cbar.set_label("Qualität (%)", fontsize=12)

    # Defekte hervorheben
    ax1.scatter(
        x[defect_indices],
        y[defect_indices],
        z[defect_indices],
        c="red",
        s=100,
        alpha=1,
        marker="x",
        linewidths=3,
        label="Defekte",
    )
    ax1.legend()

    # Seitenansicht - X-Z Ebene
    ax2 = fig.add_subplot(222, projection="3d")
    ax2.scatter(x, np.zeros_like(x), z, c=quality, cmap="RdYlGn", s=30, alpha=0.6)
    ax2.set_xlabel("X-Position (mm)")
    ax2.set_zlabel("Z-Position (mm)")
    ax2.set_title("Seitenansicht (X-Z)", fontsize=12)
    ax2.view_init(elev=0, azim=0)

    # Draufsicht - X-Y Ebene
    ax3 = fig.add_subplot(223, projection="3d")
    ax3.scatter(x, y, np.zeros_like(z), c=quality, cmap="RdYlGn", s=30, alpha=0.6)
    ax3.set_xlabel("X-Position (mm)")
    ax3.set_ylabel("Y-Position (mm)")
    ax3.set_title("Draufsicht (X-Y)", fontsize=12)
    ax3.view_init(elev=90, azim=0)

    # Statistiken
    ax4 = fig.add_subplot(224)
    ax4.hist(quality, bins=20, alpha=0.7, color="skyblue", edgecolor="black")
    ax4.axvline(
        np.mean(quality),
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Durchschnitt: {np.mean(quality):.1f}%",
    )
    ax4.axvline(
        85, color="orange", linestyle=":", linewidth=2, label="Mindestqualität: 85%"
    )
    ax4.set_xlabel("Qualität (%)")
    ax4.set_ylabel("Häufigkeit")
    ax4.set_title("Qualitätsverteilung")
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Analyse ausgeben
    below_threshold = np.sum(quality < 85) / len(quality) * 100
    defect_rate = len(defect_indices) / len(quality) * 100

    print(f"📊 Qualitätsanalyse ({n_points} Messpunkte):")
    print(f"  Durchschnittsqualität: {np.mean(quality):.1f}%")
    print(f"  Standardabweichung: {np.std(quality):.1f}%")
    print(f"  Unter Mindestqualität: {below_threshold:.1f}%")
    print(f"  Kritische Defekte: {defect_rate:.1f}%")
    print(f"  Qualitätsspanne: {np.min(quality):.1f}% - {np.max(quality):.1f}%")


def demo_surface_plots() -> None:
    """3D-Oberflächenplots für Spannungsfelder und Temperaturverteilungen"""
    # Temperatursimulation auf Werkstückoberfläche
    x = np.linspace(0, 100, 50)  # mm
    y = np.linspace(0, 50, 25)  # mm
    X, Y = np.meshgrid(x, y)

    # Temperaturfeld mit mehreren Wärmequellen
    def temperature_field(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        """Berechnet Temperaturfeld mit mehreren Hotspots"""
        # Hauptwärmequelle (Laserstrahl)
        temp1 = 200 * np.exp(-((x - 30) ** 2 + (y - 25) ** 2) / 100)

        # Sekundäre Wärmequelle
        temp2 = 150 * np.exp(-((x - 70) ** 2 + (y - 15) ** 2) / 150)

        # Grundtemperatur + lokale Erwärmung
        base_temp = 20 + 0.1 * x  # Gradient durch Materialflusshm

        return base_temp + temp1 + temp2

    Z_temp = temperature_field(X, Y)

    # Spannungsfeld basierend auf Temperaturgradienten
    grad_x, grad_y = np.gradient(Z_temp)
    Z_stress = np.sqrt(grad_x**2 + grad_y**2) * 10  # Vereinfachte Spannungsberechnung

    fig = plt.figure(figsize=(16, 12))

    # Temperaturverteilung
    ax1 = fig.add_subplot(221, projection="3d")
    surf1 = ax1.plot_surface(
        X, Y, Z_temp, cmap="hot", alpha=0.9, linewidth=0, antialiased=True
    )
    ax1.set_xlabel("X-Position (mm)")
    ax1.set_ylabel("Y-Position (mm)")
    ax1.set_zlabel("Temperatur (°C)")
    ax1.set_title("Temperaturverteilung", fontsize=14, fontweight="bold")
    plt.colorbar(surf1, ax=ax1, shrink=0.8, aspect=20)

    # Spannungsfeld
    ax2 = fig.add_subplot(222, projection="3d")
    surf2 = ax2.plot_surface(
        X, Y, Z_stress, cmap="plasma", alpha=0.9, linewidth=0, antialiased=True
    )
    ax2.set_xlabel("X-Position (mm)")
    ax2.set_ylabel("Y-Position (mm)")
    ax2.set_zlabel("Spannung (MPa)")
    ax2.set_title("Mechanische Spannungen", fontsize=14, fontweight="bold")
    plt.colorbar(surf2, ax=ax2, shrink=0.8, aspect=20)

    # Konturplot (2D-Draufsicht)
    ax3 = fig.add_subplot(223)
    contour = ax3.contourf(X, Y, Z_temp, levels=20, cmap="hot")
    ax3.contour(X, Y, Z_temp, levels=20, colors="black", alpha=0.3, linewidths=0.5)
    ax3.set_xlabel("X-Position (mm)")
    ax3.set_ylabel("Y-Position (mm)")
    ax3.set_title("Temperatur-Konturlinien", fontsize=14, fontweight="bold")
    plt.colorbar(contour, ax=ax3)

    # Kritische Bereiche identifizieren
    ax4 = fig.add_subplot(224)
    critical_temp = Z_temp > 150  # Kritische Temperatur
    high_stress = Z_stress > 50  # Hohe Spannung

    # Kombinierte Risikokarte
    risk_map = np.zeros_like(Z_temp)
    risk_map[critical_temp & high_stress] = 3  # Höchstes Risiko
    risk_map[critical_temp & ~high_stress] = 2  # Hohe Temperatur
    risk_map[~critical_temp & high_stress] = 1  # Hohe Spannung

    risk_colors = ["green", "yellow", "orange", "red"]
    risk_levels = ["OK", "Spannung", "Temperatur", "Kritisch"]

    ax4.contourf(
        X, Y, risk_map, levels=[0, 0.5, 1.5, 2.5, 3.5], colors=risk_colors, alpha=0.8
    )
    ax4.contour(X, Y, risk_map, levels=[0.5, 1.5, 2.5], colors="black", linewidths=1)
    ax4.set_xlabel("X-Position (mm)")
    ax4.set_ylabel("Y-Position (mm)")
    ax4.set_title("Risikobewertung", fontsize=14, fontweight="bold")

    # Legende für Risikostufen
    for _i, (color, level) in enumerate(zip(risk_colors, risk_levels, strict=False)):
        ax4.scatter([], [], c=color, s=100, label=level)
    ax4.legend()

    plt.tight_layout()
    plt.show()

    # Analyse
    max_temp = np.max(Z_temp)
    max_stress = np.max(Z_stress)
    critical_area = np.sum(risk_map >= 2) / risk_map.size * 100

    print("🔥 Temperatur- und Spannungsanalyse:")
    print(f"  Maximale Temperatur: {max_temp:.0f}°C")
    print(f"  Maximale Spannung: {max_stress:.1f} MPa")
    print(f"  Kritische Bereiche: {critical_area:.1f}% der Fläche")
    print(
        f"  Empfehlung: {'Prozessanpassung erforderlich' if critical_area > 10 else 'Prozess stabil'}"
    )


def demo_wireframe() -> None:
    """Drahtgitter-Modelle und Mesh-Visualisierungen"""
    # CAD-Modell eines einfachen Werkstücks
    print("🔧 Erstelle 3D-Werkstück-Modell...")

    fig = plt.figure(figsize=(15, 10))

    # Werkstück-Geometrie definieren
    # Grundplatte
    x_base = np.linspace(0, 50, 20)
    y_base = np.linspace(0, 30, 15)
    X_base, Y_base = np.meshgrid(x_base, y_base)
    Z_base = np.zeros_like(X_base)

    # Obere Fläche
    Z_top = np.ones_like(X_base) * 10

    # Seitenwände - vereinfacht als Funktionen
    def side_wall_1(x: np.ndarray, z: np.ndarray) -> np.ndarray:
        """Seitenwand bei Y=0"""
        return np.zeros_like(x)

    def side_wall_2(x: np.ndarray, z: np.ndarray) -> np.ndarray:
        """Seitenwand bei Y=30"""
        return np.ones_like(x) * 30

    # Drahtgitter-Darstellung
    ax1 = fig.add_subplot(221, projection="3d")

    # Grundplatte und Decke
    ax1.plot_wireframe(X_base, Y_base, Z_base, color="blue", alpha=0.6, linewidth=1)
    ax1.plot_wireframe(X_base, Y_base, Z_top, color="blue", alpha=0.6, linewidth=1)

    # Seitenwände
    for x_val in [0, 50]:
        y_wall = np.linspace(0, 30, 15)
        z_wall = np.linspace(0, 10, 10)
        Y_wall, Z_wall = np.meshgrid(y_wall, z_wall)
        X_wall = np.ones_like(Y_wall) * x_val
        ax1.plot_wireframe(
            X_wall, Y_wall, Z_wall, color="green", alpha=0.6, linewidth=1
        )

    for y_val in [0, 30]:
        x_wall = np.linspace(0, 50, 20)
        z_wall = np.linspace(0, 10, 10)
        X_wall, Z_wall = np.meshgrid(x_wall, z_wall)
        Y_wall = np.ones_like(X_wall) * y_val
        ax1.plot_wireframe(X_wall, Y_wall, Z_wall, color="red", alpha=0.6, linewidth=1)

    ax1.set_xlabel("X (mm)")
    ax1.set_ylabel("Y (mm)")
    ax1.set_zlabel("Z (mm)")
    ax1.set_title("Drahtgitter-Modell", fontsize=14, fontweight="bold")

    # Oberflächenmodell mit Mesh
    ax2 = fig.add_subplot(222, projection="3d")

    # Oberflächen mit verschiedenen Farben
    ax2.plot_surface(
        X_base, Y_base, Z_base, color="lightblue", alpha=0.7, label="Boden"
    )
    ax2.plot_surface(
        X_base, Y_base, Z_top, color="lightcoral", alpha=0.7, label="Decke"
    )

    ax2.set_xlabel("X (mm)")
    ax2.set_ylabel("Y (mm)")
    ax2.set_zlabel("Z (mm)")
    ax2.set_title("Oberflächenmodell", fontsize=14, fontweight="bold")

    # Schnittansicht
    ax3 = fig.add_subplot(223, projection="3d")

    # Schnitt bei Y = 15
    x_cut = np.linspace(0, 50, 20)
    z_cut = np.linspace(0, 10, 10)
    X_cut, Z_cut = np.meshgrid(x_cut, z_cut)
    Y_cut = np.ones_like(X_cut) * 15

    # Materializeigenschaften visualisieren
    material_density = 1 + 0.5 * np.sin(X_cut / 10) * np.cos(Z_cut / 5)

    ax3.plot_surface(
        X_cut,
        Y_cut,
        Z_cut,
        facecolors=plt.cm.viridis(material_density),
        alpha=0.8,
        linewidth=0,
    )

    ax3.set_xlabel("X (mm)")
    ax3.set_ylabel("Y (mm)")
    ax3.set_zlabel("Z (mm)")
    ax3.set_title("Schnittansicht mit Materialdichte", fontsize=14, fontweight="bold")

    # Messpoints auf dem Modell
    ax4 = fig.add_subplot(224, projection="3d")

    # Werkstück als Oberfläche
    ax4.plot_surface(X_base, Y_base, Z_top, color="lightgray", alpha=0.5)

    # Messpunkte hinzufügen
    n_measurements = 50
    np.random.seed(42)
    x_measure = np.random.uniform(5, 45, n_measurements)
    y_measure = np.random.uniform(5, 25, n_measurements)
    z_measure = np.ones(n_measurements) * 10

    # Messwerte simulieren
    measured_deviation = np.random.normal(0, 0.2, n_measurements)  # Abweichung in mm

    # Farbkodierung basierend auf Abweichung
    colors = [
        "green" if abs(dev) < 0.1 else "yellow" if abs(dev) < 0.2 else "red"
        for dev in measured_deviation
    ]

    ax4.scatter(x_measure, y_measure, z_measure, c=colors, s=100, alpha=0.8)

    ax4.set_xlabel("X (mm)")
    ax4.set_ylabel("Y (mm)")
    ax4.set_zlabel("Z (mm)")
    ax4.set_title("Qualitätsmessung 3D", fontsize=14, fontweight="bold")

    # Toleranzbereich anzeigen
    ax4.text2D(
        0.02,
        0.98,
        "Toleranzen:\n🟢 < 0.1mm\n🟡 < 0.2mm\n🔴 > 0.2mm",
        transform=ax4.transAxes,
        fontsize=10,
        verticalalignment="top",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.8},
    )

    plt.tight_layout()
    plt.show()

    # Messtechnik-Auswertung
    within_tolerance = (
        np.sum(np.abs(measured_deviation) < 0.1) / len(measured_deviation) * 100
    )
    critical_points = np.sum(np.abs(measured_deviation) > 0.2)

    print("📏 3D-Messtechnik Auswertung:")
    print(f"  Messpunkte gesamt: {n_measurements}")
    print(f"  Innerhalb Toleranz (±0.1mm): {within_tolerance:.1f}%")
    print(f"  Kritische Abweichungen: {critical_points}")
    print(
        f"  Durchschnittliche Abweichung: ±{np.mean(np.abs(measured_deviation)):.3f}mm"
    )
    print(f"  Maximale Abweichung: ±{np.max(np.abs(measured_deviation)):.3f}mm")


def demo_volumetric() -> None:
    """Volumetrische Darstellungen und 3D-Datenfelder"""
    print("📦 Volumetrische Datenanalyse...")

    # 3D-Materialverteilung simulieren
    nx, ny, nz = 20, 15, 10
    x = np.linspace(0, 50, nx)
    y = np.linspace(0, 30, ny)
    z = np.linspace(0, 20, nz)
    X, Y, Z = np.meshgrid(x, y, z, indexing="ij")

    # Material-Dichteverteilung
    density = (np.sin(X / 10) * np.cos(Y / 8) * np.exp(-Z / 15) + 1) * 2.5  # kg/m³

    # Poren/Defekte hinzufügen
    defects = np.random.random((nx, ny, nz)) < 0.05
    density[defects] = 0.1  # Niedrige Dichte für Defekte

    fig = plt.figure(figsize=(16, 12))

    # 3D Scatter für hohe/niedrige Dichtebereiche
    ax1 = fig.add_subplot(221, projection="3d")

    # Nur Punkte mit extremen Werten anzeigen
    high_density = density > 4.0
    low_density = density < 1.0

    # Hohe Dichte (gutes Material)
    if np.any(high_density):
        x_high, y_high, z_high = X[high_density], Y[high_density], Z[high_density]
        ax1.scatter(
            x_high, y_high, z_high, c="blue", s=30, alpha=0.8, label="Hohe Dichte"
        )

    # Niedrige Dichte (Defekte/Poren)
    if np.any(low_density):
        x_low, y_low, z_low = X[low_density], Y[low_density], Z[low_density]
        ax1.scatter(
            x_low,
            y_low,
            z_low,
            c="red",
            s=60,
            alpha=1.0,
            marker="x",
            linewidths=2,
            label="Defekte",
        )

    ax1.set_xlabel("X (mm)")
    ax1.set_ylabel("Y (mm)")
    ax1.set_zlabel("Z (mm)")
    ax1.set_title("3D Material-Defektanalyse", fontsize=14, fontweight="bold")
    ax1.legend()

    # Schnittebenen durch das Volumen
    ax2 = fig.add_subplot(222, projection="3d")

    # Mehrere Schnittebenen
    for z_slice in [5, 10, 15]:
        z_idx = np.argmin(np.abs(z - z_slice))
        density_slice = density[:, :, z_idx]

        # Mesh für Schnittebene
        X_slice, Y_slice = np.meshgrid(x, y, indexing="ij")
        Z_slice = np.ones_like(X_slice) * z_slice

        # Oberflächenplot mit Transparenz
        alpha_val = 0.3 + 0.3 * (z_slice / 20)  # Verschiedene Transparenzen
        ax2.plot_surface(
            X_slice,
            Y_slice,
            Z_slice,
            facecolors=plt.cm.viridis(density_slice / 5.0),
            alpha=alpha_val,
            linewidth=0,
        )

    ax2.set_xlabel("X (mm)")
    ax2.set_ylabel("Y (mm)")
    ax2.set_zlabel("Z (mm)")
    ax2.set_title("Mehrere Schnittebenen", fontsize=14, fontweight="bold")

    # Isoflächen (vereinfacht)
    ax3 = fig.add_subplot(223, projection="3d")

    # Bereiche mit bestimmter Dichte hervorheben
    target_density = 3.0
    tolerance = 0.5

    iso_condition = np.abs(density - target_density) < tolerance
    if np.any(iso_condition):
        x_iso, y_iso, z_iso = X[iso_condition], Y[iso_condition], Z[iso_condition]
        density_iso = density[iso_condition]

        scatter_iso = ax3.scatter(
            x_iso, y_iso, z_iso, c=density_iso, cmap="coolwarm", s=50, alpha=0.7
        )
        plt.colorbar(scatter_iso, ax=ax3, shrink=0.8, aspect=20, label="Dichte (kg/m³)")

    ax3.set_xlabel("X (mm)")
    ax3.set_ylabel("Y (mm)")
    ax3.set_zlabel("Z (mm)")
    ax3.set_title(
        f"Isoflächen (Dichte ≈ {target_density} kg/m³)", fontsize=14, fontweight="bold"
    )

    # Histogramm der Dichteverteilung
    ax4 = fig.add_subplot(224)

    density_flat = density.flatten()
    n, bins, patches = ax4.hist(
        density_flat, bins=30, alpha=0.7, color="skyblue", edgecolor="black"
    )

    # Farbkodierung der Histogramm-Balken
    for _i, (patch, bin_val) in enumerate(zip(patches, bins[:-1], strict=False)):
        if bin_val < 1.0:
            patch.set_facecolor("red")  # Defekte
        elif bin_val > 4.0:
            patch.set_facecolor("blue")  # Hohe Qualität
        else:
            patch.set_facecolor("lightgray")  # Normal

    ax4.axvline(
        target_density,
        color="green",
        linestyle="--",
        linewidth=2,
        label=f"Zieldichte: {target_density} kg/m³",
    )
    ax4.axvline(
        np.mean(density_flat),
        color="orange",
        linestyle=":",
        linewidth=2,
        label=f"Ist-Durchschnitt: {np.mean(density_flat):.2f} kg/m³",
    )

    ax4.set_xlabel("Dichte (kg/m³)")
    ax4.set_ylabel("Häufigkeit")
    ax4.set_title("Dichteverteilung im Volumen", fontsize=14, fontweight="bold")
    ax4.legend()
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.show()

    # Volumetrische Analyse
    total_volume = nx * ny * nz
    defect_volume = np.sum(defects) / total_volume * 100
    high_quality_volume = np.sum(density > 4.0) / total_volume * 100
    average_density = np.mean(density_flat)

    print("📊 Volumetrische Material-Analyse:")
    print(f"  Gesamtvolumen: {nx}×{ny}×{nz} = {total_volume} Voxel")
    print(f"  Defektanteil: {defect_volume:.1f}% des Volumens")
    print(f"  Hochwertige Bereiche: {high_quality_volume:.1f}% des Volumens")
    print(f"  Durchschnittsdichte: {average_density:.2f} kg/m³")
    print(
        f"  Dichtebereich: {np.min(density_flat):.2f} - {np.max(density_flat):.2f} kg/m³"
    )

    # Qualitätsbewertung
    if defect_volume > 5:
        print("⚠️ Warnung: Hoher Defektanteil detected!")
    elif defect_volume > 2:
        print("🟡 Achtung: Erhöhter Defektanteil")
    else:
        print("✅ Materialqualität im Sollbereich")


def demo_animated_3d() -> None:
    """Animierte 3D-Visualisierungen"""
    print("🎬 Animierte 3D-Rotation...")
    print("Schließen Sie das Fenster zum Beenden der Animation")

    # 3D-Funktion für Animation
    u = np.linspace(0, 2 * np.pi, 30)
    v = np.linspace(0, np.pi, 20)
    U, V = np.meshgrid(u, v)

    # Parameter für Animation
    t_values = np.linspace(0, 4 * np.pi, 60)

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection="3d")

    def animate_surface(frame: int) -> None:
        """Animiert eine sich verformende 3D-Oberfläche"""
        ax.clear()

        t = t_values[frame]

        # Zeitabhängige Oberflächendeformation
        r = 1 + 0.3 * np.sin(3 * U + t) * np.cos(2 * V + t / 2)

        # Kugelkoordinaten zu kartesischen Koordinaten
        X = r * np.sin(V) * np.cos(U)
        Y = r * np.sin(V) * np.sin(U)
        Z = r * np.cos(V)

        # Oberflächenplot mit Farbkodierung basierend auf Radius
        ax.plot_surface(
            X,
            Y,
            Z,
            facecolors=plt.cm.plasma(r),
            alpha=0.8,
            linewidth=0,
            antialiased=True,
        )

        ax.set_xlim(-2, 2)
        ax.set_ylim(-2, 2)
        ax.set_zlim(-2, 2)
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title(
            f"Animierte 3D-Oberfläche (Frame {frame + 1}/60)",
            fontsize=14,
            fontweight="bold",
        )

        # Rotiere die Ansicht
        ax.view_init(elev=20, azim=frame * 6)  # 360° in 60 Frames

    # Einfache Animation ohne FuncAnimation für bessere Kompatibilität
    for frame in range(len(t_values)):
        animate_surface(frame)
        plt.pause(0.1)  # 100ms zwischen Frames

        # Vorzeitiges Beenden möglich
        if not plt.fignum_exists(fig.number):
            break

    plt.show()

    print("✅ Animation abgeschlossen")


if __name__ == "__main__":
    main()
