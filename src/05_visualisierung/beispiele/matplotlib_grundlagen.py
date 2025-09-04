#!/usr/bin/env python3
"""
Matplotlib Grundlagen - Beispielskript für 2D-Diagramme

Dieses Skript demonstriert die grundlegenden Funktionen von Matplotlib
für die Erstellung verschiedener 2D-Diagramme mit Fokus auf industrielle
Anwendungen bei Bystronic.

Autor: Python Grundkurs Bystronic
"""

import warnings

import matplotlib.pyplot as plt
import numpy as np

# Warnings für bessere Lesbarkeit unterdrücken
warnings.filterwarnings("ignore")


def main() -> None:
    """Hauptfunktion für Matplotlib-Grundlagen"""
    print("=" * 70)
    print("BYSTRONIC - MATPLOTLIB GRUNDLAGEN")
    print("=" * 70)

    # 1. Einfacher Linienplot
    print("\n1️⃣ Liniendiagramme")
    print("-" * 40)

    # Produktionsdaten über Zeit
    tage = np.arange(1, 31)  # 30 Tage
    np.random.seed(42)
    produktion = 1000 + 200 * np.sin(tage / 5) + np.random.normal(0, 50, 30)

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1)
    plt.plot(tage, produktion, "b-", linewidth=2, marker="o", markersize=4)
    plt.title("Tägliche Produktion")
    plt.xlabel("Tag")
    plt.ylabel("Stückzahl")
    plt.grid(True, alpha=0.3)

    print(f"Durchschnittsproduktion: {np.mean(produktion):.1f} Stück/Tag")
    print(f"Max. Produktion: {np.max(produktion):.1f} Stück")
    print(f"Min. Produktion: {np.min(produktion):.1f} Stück")

    # 2. Balkendiagramm
    print("\n2️⃣ Balkendiagramme")
    print("-" * 40)

    maschinen = ["Laser A", "Laser B", "Presse C", "Biege D", "Stanz E"]
    auslastung = [85, 92, 78, 88, 95]  # Prozent

    plt.subplot(2, 2, 2)
    bars = plt.bar(
        maschinen,
        auslastung,
        color=["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd"],
    )
    plt.title("Maschinenauslastung")
    plt.ylabel("Auslastung (%)")
    plt.xticks(rotation=45)

    # Werte auf Balken anzeigen
    for bar, wert in zip(bars, auslastung, strict=False):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{wert}%",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    print("Auslastungsübersicht:")
    for maschine, wert in zip(maschinen, auslastung, strict=False):
        status = (
            "🟢 Optimal" if wert >= 90 else "🟡 Gut" if wert >= 80 else "🔴 Niedrig"
        )
        print(f"  {maschine}: {wert}% {status}")

    # 3. Scatterplot für Korrelationen
    print("\n3️⃣ Streudiagramme")
    print("-" * 40)

    # Geschwindigkeit vs. Qualität
    geschwindigkeit = np.random.uniform(50, 150, 100)  # mm/min
    # Qualität nimmt bei zu hoher Geschwindigkeit ab
    qualitaet = (
        98 - 0.3 * (geschwindigkeit - 100) ** 2 / 100 + np.random.normal(0, 2, 100)
    )
    qualitaet = np.clip(qualitaet, 70, 100)  # Begrenzen auf realistischen Bereich

    plt.subplot(2, 2, 3)
    scatter = plt.scatter(
        geschwindigkeit, qualitaet, c=qualitaet, cmap="RdYlGn", alpha=0.7, s=50
    )
    plt.colorbar(scatter, label="Qualität (%)")
    plt.title("Geschwindigkeit vs. Qualität")
    plt.xlabel("Geschwindigkeit (mm/min)")
    plt.ylabel("Qualität (%)")
    plt.grid(True, alpha=0.3)

    # Korrelationskoeffizient
    korrelation = np.corrcoef(geschwindigkeit, qualitaet)[0, 1]
    plt.text(
        0.05,
        0.95,
        f"Korrelation: r = {korrelation:.3f}",
        transform=plt.gca().transAxes,
        bbox={"boxstyle": "round", "facecolor": "wheat"},
    )

    print(f"Korrelation Geschwindigkeit-Qualität: r = {korrelation:.3f}")

    # 4. Histogramm für Verteilungen
    print("\n4️⃣ Histogramme")
    print("-" * 40)

    # Temperaturverteilung
    temperaturen = np.random.normal(75, 8, 500)  # Normalverteilung um 75°C

    plt.subplot(2, 2, 4)
    n, bins, patches = plt.hist(
        temperaturen, bins=30, alpha=0.7, color="skyblue", edgecolor="black"
    )
    plt.title("Temperaturverteilung")
    plt.xlabel("Temperatur (°C)")
    plt.ylabel("Häufigkeit")

    # Statistiken hinzufügen
    mean_temp = np.mean(temperaturen)
    std_temp = np.std(temperaturen)
    plt.axvline(
        mean_temp,
        color="red",
        linestyle="--",
        linewidth=2,
        label=f"Mittelwert: {mean_temp:.1f}°C",
    )
    plt.axvline(
        mean_temp + std_temp,
        color="orange",
        linestyle="--",
        label=f"±1σ: ±{std_temp:.1f}°C",
    )
    plt.axvline(mean_temp - std_temp, color="orange", linestyle="--")
    plt.legend()

    print("Temperaturstatistiken:")
    print(f"  Mittelwert: {mean_temp:.2f}°C")
    print(f"  Standardabweichung: {std_temp:.2f}°C")
    print(
        f"  Temperaturbereich: {np.min(temperaturen):.1f}°C - {np.max(temperaturen):.1f}°C"
    )

    plt.tight_layout()
    plt.show()

    # 5. Erweiterte Styling-Optionen
    print("\n5️⃣ Professionelles Styling")
    print("-" * 40)

    demo_styling()

    # 6. Subplots und komplexere Layouts
    print("\n6️⃣ Komplexe Layouts")
    print("-" * 40)

    demo_komplexe_layouts()

    print(f"\n{'=' * 70}")
    print("✅ Matplotlib-Grundlagen erfolgreich demonstriert!")
    print("🎨 Verschiedene Diagrammtypen für industrielle Anwendungen")
    print("📊 Professionelle Visualisierungen für Bystronic-Daten")


def demo_styling() -> None:
    """Demonstriert erweiterte Styling-Optionen"""
    # Stil-Parameter setzen
    plt.style.use("seaborn-v0_8-whitegrid")

    # Daten für Energie-Monitoring
    stunden = np.arange(0, 24)
    verbrauch_laser = 45 + 15 * np.sin(stunden / 3) + np.random.normal(0, 3, 24)
    verbrauch_presse = 35 + 10 * np.sin((stunden + 2) / 4) + np.random.normal(0, 2, 24)

    plt.figure(figsize=(12, 6))

    # Definierte Farben für Corporate Design
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c"]

    plt.plot(
        stunden,
        verbrauch_laser,
        color=colors[0],
        linewidth=3,
        label="Laser-Anlage",
        marker="s",
        markersize=6,
    )
    plt.plot(
        stunden,
        verbrauch_presse,
        color=colors[1],
        linewidth=3,
        label="Presse",
        marker="^",
        markersize=6,
    )

    # Professionelle Beschriftungen
    plt.title("24-Stunden Energieverbrauch", fontsize=16, fontweight="bold", pad=20)
    plt.xlabel("Uhrzeit", fontsize=12)
    plt.ylabel("Verbrauch (kW)", fontsize=12)

    # Angepasste Achsen
    plt.xticks(range(0, 25, 4), [f"{h:02d}:00" for h in range(0, 25, 4)])
    plt.xlim(-0.5, 23.5)
    plt.ylim(0, 80)

    # Legende und Grid
    plt.legend(loc="upper right", frameon=True, fancybox=True, shadow=True)
    plt.grid(True, alpha=0.3)

    # Hintergrundfarben für Arbeitszeit
    plt.axvspan(6, 18, alpha=0.1, color="green", label="Arbeitszeit")

    plt.tight_layout()
    plt.show()

    print("Energieverbrauch-Analyse:")
    print(f"  Laser durchschnittlich: {np.mean(verbrauch_laser):.1f} kW")
    print(f"  Presse durchschnittlich: {np.mean(verbrauch_presse):.1f} kW")
    print(
        f"  Gesamtverbrauch/Tag: {np.sum(verbrauch_laser + verbrauch_presse):.0f} kWh"
    )


def demo_komplexe_layouts() -> None:
    """Demonstriert komplexe Subplot-Layouts"""
    # Dashboard-ähnliches Layout
    plt.figure(figsize=(15, 10))

    # Hauptplot (große Fläche)
    ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=2, rowspan=2)

    # Produktionsverlauf über Wochen
    wochen = np.arange(1, 13)
    produktion_plan = np.array(
        [1000, 1100, 1200, 1150, 1300, 1400, 1350, 1250, 1450, 1500, 1400, 1550]
    )
    produktion_ist = produktion_plan + np.random.normal(0, 80, 12)

    ax1.plot(wochen, produktion_plan, "g--", linewidth=3, label="Geplant", marker="o")
    ax1.plot(wochen, produktion_ist, "b-", linewidth=2, label="Ist", marker="s")
    ax1.fill_between(wochen, produktion_plan, produktion_ist, alpha=0.3)
    ax1.set_title("Jahresproduktion 2024", fontsize=14, fontweight="bold")
    ax1.set_xlabel("Monat")
    ax1.set_ylabel("Stückzahl")
    ax1.legend()
    ax1.grid(True, alpha=0.3)

    # Kleine Plots rechts
    ax2 = plt.subplot2grid((3, 3), (0, 2))
    ax3 = plt.subplot2grid((3, 3), (1, 2))

    # Ausfallzeiten als Pie Chart
    labels = ["Wartung", "Störung", "Umbau", "Betrieb"]
    sizes = [5, 3, 2, 90]
    colors = ["gold", "lightcoral", "lightskyblue", "lightgreen"]

    ax2.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
    ax2.set_title("Maschinenverfügbarkeit", fontsize=10)

    # Qualitätstrend
    qualitaet_werte = [96.5, 97.2, 96.8, 98.1, 97.5, 98.3, 97.9, 98.6]
    ax3.bar(range(len(qualitaet_werte)), qualitaet_werte, color="lightblue")
    ax3.set_title("Qualitätstrend", fontsize=10)
    ax3.set_ylabel("Qualität (%)")
    ax3.set_ylim(95, 100)

    # Unterer Bereich - Heatmap
    ax4 = plt.subplot2grid((3, 3), (2, 0), colspan=3)

    # Schichtdaten simulieren
    schichten = ["Früh", "Spät", "Nacht"]
    tage_woche = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]

    # Zufällige Produktivitätsdaten
    np.random.seed(42)
    produktivitaet = np.random.uniform(70, 100, (len(schichten), len(tage_woche)))

    im = ax4.imshow(produktivitaet, cmap="RdYlGn", aspect="auto", vmin=70, vmax=100)
    ax4.set_xticks(range(len(tage_woche)))
    ax4.set_xticklabels(tage_woche)
    ax4.set_yticks(range(len(schichten)))
    ax4.set_yticklabels(schichten)
    ax4.set_title("Schichtproduktivität (%)", fontsize=12)

    # Werte in Zellen anzeigen
    for i in range(len(schichten)):
        for j in range(len(tage_woche)):
            ax4.text(
                j,
                i,
                f"{produktivitaet[i, j]:.0f}%",
                ha="center",
                va="center",
                color="black",
                fontweight="bold",
            )

    # Colorbar
    plt.colorbar(im, ax=ax4, orientation="horizontal", pad=0.1)

    plt.suptitle("Bystronic Produktions-Dashboard", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()

    # Statistiken ausgeben
    print("Dashboard-Übersicht:")
    abweichung = np.mean(np.abs(produktion_ist - produktion_plan))
    print(f"  Durchschnittliche Plan-Abweichung: ±{abweichung:.0f} Stück")
    print(f"  Maschinenverfügbarkeit: {100 - sum(sizes[:3]):.1f}%")
    print(f"  Durchschnittsqualität: {np.mean(qualitaet_werte):.1f}%")

    # Beste und schlechteste Schicht
    beste_schicht = np.unravel_index(np.argmax(produktivitaet), produktivitaet.shape)
    print(
        f"  Beste Schicht: {schichten[beste_schicht[0]]} {tage_woche[beste_schicht[1]]} "
        f"({produktivitaet[beste_schicht]:.0f}%)"
    )


if __name__ == "__main__":
    main()
