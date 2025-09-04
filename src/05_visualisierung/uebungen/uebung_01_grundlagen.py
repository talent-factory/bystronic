#!/usr/bin/env python3
"""
Übung 1: Matplotlib Grundlagen - Erste Schritte mit Datenvisualisierung

Diese Übung führt Sie durch die Grundlagen der Datenvisualisierung mit Matplotlib.
Sie lernen verschiedene Plot-Typen kennen und erstellen eigene Visualisierungen.

Autor: Python Grundkurs Bystronic
Schwierigkeitsgrad: ⭐⭐⭐ (Grundlagen)
Geschätzte Bearbeitungszeit: 45-60 Minuten
"""

import warnings
from datetime import datetime, timedelta

import matplotlib.pyplot as plt
import numpy as np

warnings.filterwarnings("ignore")


def main() -> None:
    """Hauptfunktion für Übung 1 - Matplotlib Grundlagen"""
    print("=" * 70)
    print("ÜBUNG 1: MATPLOTLIB GRUNDLAGEN")
    print("=" * 70)
    print("🎯 Lernziele:")
    print("   - Linien- und Balkendiagramme erstellen")
    print("   - Plots anpassen und formatieren")
    print("   - Subplots verwenden")
    print("   - Beschriftungen und Legenden hinzufügen")
    print("   - Industrielle Daten visualisieren")

    print(f"\n{'=' * 70}")
    print("📝 AUFGABEN")
    print("=" * 70)

    # Aufgabe 1: Einfacher Linienplot
    print("\n📊 Aufgabe 1: Einfacher Linienplot")
    print("-" * 40)
    aufgabe_1_linienplot()

    # Aufgabe 2: Balkendiagramm mit Anpassungen
    print("\n📊 Aufgabe 2: Balkendiagramm erstellen")
    print("-" * 40)
    aufgabe_2_balkendiagramm()

    # Aufgabe 3: Subplots verwenden
    print("\n📊 Aufgabe 3: Subplots und Layouts")
    print("-" * 40)
    aufgabe_3_subplots()

    # Aufgabe 4: Streudiagramm und Korrelation
    print("\n📊 Aufgabe 4: Streudiagramm-Analyse")
    print("-" * 40)
    aufgabe_4_streudiagramm()

    # Aufgabe 5: Industrielle Anwendung
    print("\n📊 Aufgabe 5: Industrielle Datenvisualisierung")
    print("-" * 40)
    aufgabe_5_industrielle_anwendung()

    print(f"\n{'=' * 70}")
    print("🎉 HERZLICHEN GLÜCKWUNSCH!")
    print("Sie haben die Grundlagen von Matplotlib erfolgreich gemeistert!")
    print("➡️  Nächste Übung: uebung_02_statistik.py")
    print("=" * 70)


def aufgabe_1_linienplot() -> None:
    """
    Aufgabe 1: Erstellen Sie einen einfachen Linienplot

    TODO für Teilnehmer:
    1. Erstellen Sie x-Werte von 0 bis 10 mit 100 Punkten
    2. Berechnen Sie y = sin(x) und y2 = cos(x)
    3. Plotten Sie beide Funktionen in einem Diagramm
    4. Fügen Sie Titel, Achsenbeschriftungen und eine Legende hinzu
    5. Aktivieren Sie das Grid
    """
    print("🔨 Ihre Aufgabe:")
    print("   Erstellen Sie einen Linienplot mit sin(x) und cos(x) Funktionen")

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben
    # Musterlösung (auskommentiert für Übung):

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    x = np.linspace(0, 10, 100)
    y_sin = np.sin(x)
    y_cos = np.cos(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_sin, "b-", linewidth=2, label="sin(x)")
    plt.plot(x, y_cos, "r--", linewidth=2, label="cos(x)")
    plt.title("Trigonometrische Funktionen", fontsize=14, fontweight="bold")
    plt.xlabel("x-Werte")
    plt.ylabel("y-Werte")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
    # ============================================

    print("✅ Aufgabe 1 abgeschlossen!")
    print("   Tipp: Experimentieren Sie mit verschiedenen Linienstilen:")
    print("   '-' (durchgezogen), '--' (gestrichelt), ':' (gepunktet)")


def aufgabe_2_balkendiagramm() -> None:
    """
    Aufgabe 2: Erstellen Sie ein ansprechendes Balkendiagramm

    TODO für Teilnehmer:
    1. Verwenden Sie die gegebenen Maschinendaten
    2. Erstellen Sie ein Balkendiagramm
    3. Färben Sie die Balken basierend auf der Leistung (rot < 70%, gelb < 85%, grün >= 85%)
    4. Fügen Sie die Prozentwerte auf den Balken hinzu
    5. Rotieren Sie die x-Achsen-Beschriftungen um 45°
    """
    print("🔨 Ihre Aufgabe:")
    print("   Visualisieren Sie die Maschinenleistung mit einem Balkendiagramm")

    # Gegebene Daten
    maschinen = [
        "Laser-Schneider A",
        "Laser-Schneider B",
        "Biegepresse C",
        "Stanzautomat D",
        "Schweißroboter E",
    ]
    leistung_prozent = [92, 78, 85, 95, 67]

    print("   Gegebene Daten:")
    for maschine, leistung in zip(maschinen, leistung_prozent, strict=False):
        print(f"   - {maschine}: {leistung}%")

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    # Farben basierend auf Leistung
    farben = []
    for leistung in leistung_prozent:
        if leistung >= 85:
            farben.append("green")
        elif leistung >= 70:
            farben.append("orange")
        else:
            farben.append("red")

    plt.figure(figsize=(12, 6))
    bars = plt.bar(
        maschinen, leistung_prozent, color=farben, alpha=0.7, edgecolor="black"
    )

    # Werte auf Balken hinzufügen
    for bar, wert in zip(bars, leistung_prozent, strict=False):
        plt.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 1,
            f"{wert}%",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    plt.title(
        "Maschinenleistung - Bystronic Produktionslinie", fontsize=14, fontweight="bold"
    )
    plt.xlabel("Maschinen")
    plt.ylabel("Leistung (%)")
    plt.xticks(rotation=45, ha="right")
    plt.ylim(0, 105)
    plt.grid(True, alpha=0.3, axis="y")
    plt.tight_layout()
    plt.show()
    # ============================================

    print("✅ Aufgabe 2 abgeschlossen!")
    print("   Tipp: Verwenden Sie plt.tight_layout() für bessere Formatierung")


def aufgabe_3_subplots() -> None:
    """
    Aufgabe 3: Erstellen Sie ein 2x2 Subplot-Layout

    TODO für Teilnehmer:
    1. Erstellen Sie ein 2x2 Subplot-Raster
    2. Oben links: Liniendiagramm der Tagesproduktion
    3. Oben rechts: Histogramm der Temperaturverteilung
    4. Unten links: Pie-Chart der Schichtverteilung
    5. Unten rechts: Box-Plot der Qualitätswerte verschiedener Tage
    """
    print("🔨 Ihre Aufgabe:")
    print("   Erstellen Sie ein Dashboard mit 4 verschiedenen Plot-Typen")

    # Simulierte Daten
    np.random.seed(42)

    # Tagesproduktion (30 Tage)
    tage = np.arange(1, 31)
    produktion = 1000 + 100 * np.sin(tage / 5) + np.random.normal(0, 30, 30)

    # Temperaturverteilung
    temperaturen = np.random.normal(75, 8, 200)

    # Schichtverteilung
    schichten = ["Frühschicht", "Spätschicht", "Nachtschicht"]
    schicht_anteile = [45, 35, 20]

    # Qualitätswerte nach Wochentagen
    qualitaet_mo = np.random.normal(95, 3, 30)
    qualitaet_di = np.random.normal(96, 2.5, 30)
    qualitaet_mi = np.random.normal(94, 4, 30)
    qualitaet_do = np.random.normal(97, 2, 30)
    qualitaet_fr = np.random.normal(93, 5, 30)

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 10))

    # Oben links: Tagesproduktion
    ax1.plot(tage, produktion, "b-o", linewidth=2, markersize=4)
    ax1.set_title("Tagesproduktion (30 Tage)")
    ax1.set_xlabel("Tag")
    ax1.set_ylabel("Stückzahl")
    ax1.grid(True, alpha=0.3)

    # Oben rechts: Temperaturhistogramm
    ax2.hist(temperaturen, bins=20, alpha=0.7, color="orange", edgecolor="black")
    ax2.set_title("Temperaturverteilung")
    ax2.set_xlabel("Temperatur (°C)")
    ax2.set_ylabel("Häufigkeit")
    ax2.axvline(
        np.mean(temperaturen),
        color="red",
        linestyle="--",
        label=f"Mittelwert: {np.mean(temperaturen):.1f}°C",
    )
    ax2.legend()
    ax2.grid(True, alpha=0.3)

    # Unten links: Schichtverteilung
    ax3.pie(
        schicht_anteile,
        labels=schichten,
        autopct="%1.1f%%",
        colors=["gold", "lightblue", "lightcoral"],
        startangle=90,
    )
    ax3.set_title("Schichtverteilung")

    # Unten rechts: Qualitäts-Box-Plot
    qualitaet_data = [
        qualitaet_mo,
        qualitaet_di,
        qualitaet_mi,
        qualitaet_do,
        qualitaet_fr,
    ]
    wochentage = ["Mo", "Di", "Mi", "Do", "Fr"]

    ax4.boxplot(qualitaet_data, labels=wochentage)
    ax4.set_title("Qualität nach Wochentagen")
    ax4.set_xlabel("Wochentag")
    ax4.set_ylabel("Qualität (%)")
    ax4.grid(True, alpha=0.3)

    plt.suptitle("Bystronic Produktions-Dashboard", fontsize=16, fontweight="bold")
    plt.tight_layout()
    plt.show()
    # ============================================

    print("✅ Aufgabe 3 abgeschlossen!")
    print("   Tipp: plt.suptitle() erstellt einen Haupttitel für alle Subplots")


def aufgabe_4_streudiagramm() -> None:
    """
    Aufgabe 4: Analysieren Sie Zusammenhänge mit Streudiagrammen

    TODO für Teilnehmer:
    1. Erstellen Sie ein Streudiagramm für Schnittgeschwindigkeit vs. Qualität
    2. Färben Sie die Punkte nach der Materialdicke
    3. Fügen Sie eine Trendlinie hinzu
    4. Berechnen und zeigen Sie den Korrelationskoeffizienten
    5. Interpretieren Sie das Ergebnis
    """
    print("🔨 Ihre Aufgabe:")
    print("   Untersuchen Sie den Zusammenhang zwischen Geschwindigkeit und Qualität")

    # Simulierte Laser-Schneidedaten
    np.random.seed(42)
    n_punkte = 150

    # Schnittgeschwindigkeit (mm/min)
    geschwindigkeit = np.random.uniform(50, 200, n_punkte)

    # Materialdicke (mm) - beeinflusst optimale Geschwindigkeit
    materialdicke = np.random.choice([1, 2, 3, 5, 8], n_punkte)

    # Qualität hängt von Geschwindigkeit ab (optimaler Bereich)
    qualitaet = []
    for v, dicke in zip(geschwindigkeit, materialdicke, strict=False):
        # Optimale Geschwindigkeit hängt von Materialdicke ab
        optimal_v = 150 - dicke * 10

        # Qualität sinkt bei Abweichung vom Optimum
        abweichung = abs(v - optimal_v)
        basis_qualitaet = 98 - (abweichung / 20) ** 2

        # Rauschen hinzufügen
        qualitaet_wert = basis_qualitaet + np.random.normal(0, 2)
        qualitaet.append(max(qualitaet_wert, 70))  # Minimum 70%

    qualitaet = np.array(qualitaet)

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    plt.figure(figsize=(12, 8))

    # Streudiagramm mit Farbkodierung nach Materialdicke
    scatter = plt.scatter(
        geschwindigkeit,
        qualitaet,
        c=materialdicke,
        cmap="viridis",
        alpha=0.7,
        s=60,
        edgecolors="black",
        linewidth=0.5,
    )

    # Farbbalken hinzufügen
    colorbar = plt.colorbar(scatter)
    colorbar.set_label("Materialdicke (mm)", fontsize=12)

    # Trendlinie berechnen und hinzufügen
    z = np.polyfit(geschwindigkeit, qualitaet, 1)  # Lineare Regression
    p = np.poly1d(z)
    x_trend = np.linspace(geschwindigkeit.min(), geschwindigkeit.max(), 100)
    plt.plot(x_trend, p(x_trend), "r--", linewidth=2, alpha=0.8, label="Trendlinie")

    # Korrelationskoeffizient berechnen
    korrelation = np.corrcoef(geschwindigkeit, qualitaet)[0, 1]

    # Beschriftungen und Formatierung
    plt.title(
        "Laser-Schnitt-Analyse: Geschwindigkeit vs. Qualität",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Schnittgeschwindigkeit (mm/min)")
    plt.ylabel("Qualität (%)")
    plt.legend()
    plt.grid(True, alpha=0.3)

    # Korrelationskoeffizient anzeigen
    plt.text(
        0.05,
        0.95,
        f"Korrelation: r = {korrelation:.3f}",
        transform=plt.gca().transAxes,
        bbox={"boxstyle": "round,pad=0.3", "facecolor": "yellow", "alpha": 0.7},
        fontsize=12,
        fontweight="bold",
    )

    plt.tight_layout()
    plt.show()
    # ============================================

    print("✅ Aufgabe 4 abgeschlossen!")
    print(f"   📊 Korrelationskoeffizient: {korrelation:.3f}")

    # Interpretation
    if abs(korrelation) > 0.7:
        staerke = "starke"
    elif abs(korrelation) > 0.3:
        staerke = "moderate"
    else:
        staerke = "schwache"

    richtung = "negative" if korrelation < 0 else "positive"

    print(f"   📝 Interpretation: {staerke} {richtung} Korrelation")
    print("   💡 Tipp: |r| > 0.7 = stark, 0.3-0.7 = moderat, < 0.3 = schwach")


def aufgabe_5_industrielle_anwendung() -> None:
    """
    Aufgabe 5: Komplexe industrielle Datenvisualisierung

    TODO für Teilnehmer:
    1. Erstellen Sie ein umfassendes Dashboard für eine Produktionslinie
    2. Verwenden Sie verschiedene Plot-Typen in einem Layout
    3. Implementieren Sie professionelle Formatierung
    4. Fügen Sie aussagekräftige Titel und Beschriftungen hinzu
    5. Interpretieren Sie die Ergebnisse
    """
    print("🔨 Ihre Aufgabe:")
    print("   Erstellen Sie ein professionelles Produktions-Dashboard")

    # Umfangreiche Simulationsdaten
    np.random.seed(42)

    # Zeitreihen-Daten (eine Arbeitswoche)
    start_zeit = datetime(2024, 1, 15, 6, 0)  # Montag 6:00 Uhr
    zeiten = [
        start_zeit + timedelta(hours=h) for h in range(0, 120, 2)
    ]  # 5 Tage, 2h Intervalle

    # Produktionsdaten mit realistischen Mustern
    produktionsdaten = []
    for _i, zeit in enumerate(zeiten):
        # Tageszyklen (weniger Produktion nachts und am Wochenende)
        stunde = zeit.hour
        wochentag = zeit.weekday()  # 0=Montag, 6=Sonntag

        # Basis-Produktionsrate
        if 6 <= stunde <= 22:  # Arbeitszeit
            basis_rate = 120
        else:  # Nachtschicht
            basis_rate = 60

        # Wochenendfaktor
        if wochentag < 5:  # Montag-Freitag
            wochen_faktor = 1.0
        else:
            wochen_faktor = 0.3

        # Produktionsrate berechnen
        rate = basis_rate * wochen_faktor + np.random.normal(0, 15)
        produktionsdaten.append(max(rate, 0))

    # Qualitätsdaten
    qualitaetsdaten = [96 + np.random.normal(0, 3) for _ in zeiten]
    qualitaetsdaten = [
        max(min(q, 100), 80) for q in qualitaetsdaten
    ]  # Zwischen 80-100%

    # Maschinenstatus
    status_kategorien = ["Betrieb", "Wartung", "Störung", "Stillstand"]
    status_zeiten = [85, 8, 4, 3]  # Prozentual

    # Temperatur- und Druckdaten
    temperaturen = [
        75 + 5 * np.sin(i / 10) + np.random.normal(0, 2) for i in range(len(zeiten))
    ]
    druecke = [
        50 + 3 * np.cos(i / 8) + np.random.normal(0, 1.5) for i in range(len(zeiten))
    ]

    # TODO: Hier sollten die Teilnehmer ihren Code schreiben
    # Hinweis: Verwenden Sie ein großes Figure mit mehreren Subplots

    # ========== MUSTERLÖSUNG (für Trainer) ==========
    plt.figure(figsize=(18, 12))

    # Layout: 3 Zeilen, 3 Spalten
    # Zeile 1: Produktionsverlauf (breit), Status-Pie (schmal)
    ax1 = plt.subplot2grid((3, 4), (0, 0), colspan=3)
    ax2 = plt.subplot2grid((3, 4), (0, 3))

    # Zeile 2: Qualitätstrend, Temperatur/Druck
    ax3 = plt.subplot2grid((3, 4), (1, 0), colspan=2)
    ax4 = plt.subplot2grid((3, 4), (1, 2), colspan=2)

    # Zeile 3: Korrelation, Tagesstatistiken
    ax5 = plt.subplot2grid((3, 4), (2, 0), colspan=2)
    ax6 = plt.subplot2grid((3, 4), (2, 2), colspan=2)

    # 1. Produktionsverlauf über die Woche
    ax1.plot(zeiten, produktionsdaten, "b-", linewidth=2, alpha=0.8)
    ax1.fill_between(zeiten, produktionsdaten, alpha=0.3, color="blue")
    ax1.set_title("Produktionsverlauf - 5 Arbeitstage", fontsize=12, fontweight="bold")
    ax1.set_ylabel("Stück/2h")
    ax1.grid(True, alpha=0.3)

    # Arbeitszeiten hervorheben
    for _i, zeit in enumerate(zeiten):
        if 6 <= zeit.hour <= 22 and zeit.weekday() < 5:
            ax1.axvspan(zeit, zeit + timedelta(hours=2), alpha=0.1, color="green")

    # X-Achse formatieren
    import matplotlib.dates as mdates

    ax1.xaxis.set_major_formatter(mdates.DateFormatter("%a %H:%M"))
    ax1.tick_params(axis="x", rotation=45)

    # 2. Maschinenstatus
    wedges, texts, autotexts = ax2.pie(
        status_zeiten,
        labels=status_kategorien,
        autopct="%1.1f%%",
        startangle=90,
        colors=["lightgreen", "gold", "salmon", "lightgray"],
    )
    ax2.set_title("Maschinenstatus\\n(Wochenübersicht)", fontsize=10, fontweight="bold")

    # 3. Qualitätstrend
    ax3.plot(zeiten, qualitaetsdaten, "g-", linewidth=2, alpha=0.8)
    ax3.axhline(y=95, color="orange", linestyle="--", label="Zielwert 95%")
    ax3.axhline(y=90, color="red", linestyle="--", label="Mindestqualität 90%")
    ax3.set_title("Qualitätsverlauf", fontsize=12, fontweight="bold")
    ax3.set_ylabel("Qualität (%)")
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    ax3.set_ylim(85, 100)

    # 4. Temperatur und Druck (zwei Y-Achsen)
    ax4_temp = ax4
    ax4_druck = ax4.twinx()

    line1 = ax4_temp.plot(zeiten, temperaturen, "r-", linewidth=2, label="Temperatur")
    line2 = ax4_druck.plot(zeiten, druecke, "b-", linewidth=2, label="Druck")

    ax4_temp.set_ylabel("Temperatur (°C)", color="red")
    ax4_druck.set_ylabel("Druck (bar)", color="blue")
    ax4_temp.set_title("Prozessparameter", fontsize=12, fontweight="bold")

    # Kombinierte Legende
    lines = line1 + line2
    labels = [line.get_label() for line in lines]
    ax4_temp.legend(lines, labels, loc="upper left")
    ax4_temp.grid(True, alpha=0.3)

    # 5. Korrelationsanalyse
    ax5.scatter(
        temperaturen,
        qualitaetsdaten,
        alpha=0.6,
        c=produktionsdaten,
        cmap="viridis",
        s=30,
    )

    # Trendlinie
    z = np.polyfit(temperaturen, qualitaetsdaten, 1)
    p = np.poly1d(z)
    temp_range = np.linspace(min(temperaturen), max(temperaturen), 50)
    ax5.plot(temp_range, p(temp_range), "r--", linewidth=2, alpha=0.8)

    korr_temp_qual = np.corrcoef(temperaturen, qualitaetsdaten)[0, 1]
    ax5.set_title(
        f"Temperatur vs. Qualität\\n(r = {korr_temp_qual:.3f})",
        fontsize=12,
        fontweight="bold",
    )
    ax5.set_xlabel("Temperatur (°C)")
    ax5.set_ylabel("Qualität (%)")
    ax5.grid(True, alpha=0.3)

    # 6. Tagesstatistiken
    # Daten nach Wochentagen gruppieren
    wochentag_namen = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
    tages_produktion = [[] for _ in range(5)]

    for zeit, prod in zip(zeiten, produktionsdaten, strict=False):
        if zeit.weekday() < 5:  # Nur Werktage
            tages_produktion[zeit.weekday()].append(prod)

    # Box-Plot für tägliche Produktion
    tages_mittelwerte = [
        np.mean(tag_data) if tag_data else 0 for tag_data in tages_produktion
    ]

    bars = ax6.bar(
        wochentag_namen,
        tages_mittelwerte,
        color=["lightblue", "lightgreen", "lightyellow", "lightcoral", "lightpink"],
        alpha=0.7,
        edgecolor="black",
    )

    # Werte auf Balken
    for bar, wert in zip(bars, tages_mittelwerte, strict=False):
        ax6.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 2,
            f"{wert:.0f}",
            ha="center",
            va="bottom",
            fontweight="bold",
        )

    ax6.set_title("Durchschnittsproduktion pro Tag", fontsize=12, fontweight="bold")
    ax6.set_ylabel("Ø Stück/2h")
    ax6.tick_params(axis="x", rotation=45)
    ax6.grid(True, alpha=0.3, axis="y")

    # Haupttitel
    plt.suptitle(
        "BYSTRONIC PRODUKTIONS-DASHBOARD - WOCHENÜBERSICHT",
        fontsize=16,
        fontweight="bold",
        y=0.98,
    )

    plt.tight_layout()
    plt.show()
    # ============================================

    # Statistiken ausgeben
    gesamt_produktion = sum(produktionsdaten)
    avg_qualitaet = np.mean(qualitaetsdaten)
    avg_temperatur = np.mean(temperaturen)

    print("✅ Aufgabe 5 abgeschlossen!")
    print("   📊 Dashboard-Statistiken:")
    print(f"   - Gesamtproduktion: {gesamt_produktion:.0f} Stück")
    print(f"   - Durchschnittsqualität: {avg_qualitaet:.1f}%")
    print(f"   - Durchschnittstemperatur: {avg_temperatur:.1f}°C")
    print(f"   - Korrelation Temp-Qualität: {korr_temp_qual:.3f}")

    # Bewertung der Woche
    betriebszeit_prozent = status_zeiten[0]
    if betriebszeit_prozent >= 90:
        bewertung = "Exzellent 🟢"
    elif betriebszeit_prozent >= 80:
        bewertung = "Gut 🟡"
    else:
        bewertung = "Verbesserungsbedarf 🔴"

    print(f"   - Wochenbewertung: {bewertung}")
    print("   💡 Profitipp: Nutzen Sie plt.subplot2grid() für flexible Layouts!")


if __name__ == "__main__":
    main()
