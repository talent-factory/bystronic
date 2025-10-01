#!/usr/bin/env python3
"""
NumPy Übung 4: Praktische SmartFactory-Datenverarbeitung (Beginner)
SmartFactory Python Grundkurs - Kapitel 3

Diese Übung kombiniert alle bisherigen NumPy-Konzepte in einem realistischen
SmartFactory-Produktionsszenario mit echten Datenverarbeitungsaufgaben.

Lernziele:
- Kombination aller NumPy-Grundlagen in einem praktischen Projekt
- Realistische Produktionsdatenverarbeitung
- Performance-optimierte Datenanalyse
- Qualitätskontrolle und statistische Auswertung
- Vorbereitung für Intermediate-Level Konzepte

Schwierigkeitsgrad: 🟢 Beginner
Geschätzte Bearbeitungszeit: 25-30 Minuten
"""

import json
import time

import numpy as np


def main():
    """Hauptfunktion für alle Übungsaufgaben"""
    print("🏭 NUMPY ÜBUNG 4: PRAKTISCHE BYSTRONIC-DATENVERARBEITUNG")
    print("=" * 65)
    print("Diese Übung simuliert einen echten Produktionstag bei SmartFactory")
    print("mit realistischen Datenmengen und Qualitätsanforderungen.")
    print()

    # Simuliere echte Produktionsdaten
    production_data = generate_production_data()

    print("📊 PRODUKTIONSDATEN GENERIERT:")
    print(f"  • {production_data['parts_produced']:,} produzierte Teile")
    print(f"  • {production_data['total_measurements']:,} Qualitätsmessungen")
    print(f"  • {production_data['machine_count']} Maschinen")
    print(f"  • {production_data['shift_count']} Schichten")
    print()

    try:
        # Aufgabe 1: Produktionseffizienz analysieren
        aufgabe_1_produktionseffizienz(production_data)

        # Aufgabe 2: Qualitätskontrolle durchführen
        aufgabe_2_qualitaetskontrolle(production_data)

        # Aufgabe 3: Maschinenperformance vergleichen
        aufgabe_3_maschinenperformance(production_data)

        # Aufgabe 4: Trend-Analyse und Prognose
        aufgabe_4_trend_analyse(production_data)

        # Aufgabe 5: Gesamtauswertung und Report
        aufgabe_5_gesamtauswertung(production_data)

        print("\n" + "🎉" * 50)
        print("🎉 ALLE ÜBUNGSAUFGABEN ERFOLGREICH ABGESCHLOSSEN! 🎉")
        print("🎉" * 50)
        print("\n📋 ZUSAMMENFASSUNG DER GELERNTEN KONZEPTE:")
        print("✅ Array-Erstellung und -Manipulation für große Datenmengen")
        print("✅ Vektorisierte Operationen für Performance-Optimierung")
        print("✅ Statistische Auswertungen und Qualitätskennzahlen")
        print("✅ Boolean Indexing für Datenfilterung")
        print("✅ Broadcasting für effiziente Berechnungen")
        print("✅ Array-Formen und mehrdimensionale Datenorganisation")
        print("\n🚀 SIE SIND BEREIT FÜR INTERMEDIATE NUMPY-KONZEPTE!")

    except KeyboardInterrupt:
        print("\n\n⚠️ Übung abgebrochen.")
    except Exception as e:
        print(f"\n❌ Fehler in der Übung: {e}")
        print("💡 Tipp: Prüfen Sie Ihre Array-Shapes und Datentypen!")


def generate_production_data() -> dict:
    """Generiert realistische Produktionsdaten für eine Woche"""
    np.random.seed(42)  # Für reproduzierbare Ergebnisse

    # Produktionsparameter
    machines = 8  # 8 Produktionsmaschinen
    shifts_per_day = 3  # 3 Schichten pro Tag
    days = 5  # Arbeitswoche
    parts_per_shift_per_machine = np.random.poisson(
        150, (machines, shifts_per_day * days)
    )

    # Qualitätsmessungen pro Teil (3 Messungen: Länge, Breite, Dicke)
    measurements_per_part = 3

    # Berechne Gesamtzahlen
    total_parts = np.sum(parts_per_shift_per_machine)
    total_measurements = total_parts * measurements_per_part

    # Generiere Qualitätsdaten
    # Sollwerte und Toleranzen für die drei Maße
    target_values = np.array([25.0, 15.5, 8.2])  # mm
    tolerances = np.array([0.1, 0.05, 0.02])  # mm

    # Simuliere Messwerte mit realistischen Verteilungen
    quality_data = np.random.normal(
        target_values.reshape(1, -1),  # Broadcasting: (1, 3)
        (tolerances / 3).reshape(1, -1),  # Sigma = tolerance/3
        (total_parts, measurements_per_part),  # Shape: (parts, measurements)
    )

    # Maschinenzeiten (Zykluszeiten in Sekunden)
    cycle_times = np.random.normal(45.0, 3.0, total_parts)

    # Maschinenstatus (0=Produktion, 1=Wartung, 2=Störung)
    machine_status = np.random.choice(
        [0, 1, 2], size=(machines, shifts_per_day * days), p=[0.85, 0.10, 0.05]
    )

    # Produktive Zeiten pro Schicht (8 Stunden = 480 Minuten)
    productive_times = np.random.normal(420, 30, (machines, shifts_per_day * days))
    productive_times = np.clip(productive_times, 300, 480)  # Min 5h, Max 8h

    return {
        "parts_produced": int(total_parts),
        "total_measurements": int(total_measurements),
        "machine_count": machines,
        "shift_count": shifts_per_day * days,
        "parts_per_shift": parts_per_shift_per_machine,
        "quality_measurements": quality_data,
        "target_values": target_values,
        "tolerances": tolerances,
        "cycle_times": cycle_times,
        "machine_status": machine_status,
        "productive_times": productive_times,
        "measurement_names": ["Länge", "Breite", "Dicke"],
    }


def aufgabe_1_produktionseffizienz(data: dict):
    """Aufgabe 1: Analysiere die Produktionseffizienz aller Maschinen"""
    print("🎯 AUFGABE 1: PRODUKTIONSEFFIZIENZ ANALYSIEREN")
    print("-" * 50)
    print("Ziel: Berechne KPIs für alle Maschinen und identifiziere Top-Performer")
    print()

    start_time = time.time()

    # 1.1 Gesamtproduktion pro Maschine
    print("📊 1.1 Produktionszahlen pro Maschine:")
    parts_per_machine = np.sum(data["parts_per_shift"], axis=1)

    for machine_id, parts in enumerate(parts_per_machine):
        print(f"  Maschine {machine_id + 1:2d}: {parts:4d} Teile")

    print("\n📈 Statistik:")
    print(f"  Durchschnitt: {np.mean(parts_per_machine):.1f} Teile/Maschine")
    print(
        f"  Beste Maschine: {np.max(parts_per_machine)} Teile (Maschine {np.argmax(parts_per_machine) + 1})"
    )
    print(
        f"  Schlechteste: {np.min(parts_per_machine)} Teile (Maschine {np.argmin(parts_per_machine) + 1})"
    )
    print(f"  Standardabw.: {np.std(parts_per_machine):.1f} Teile")

    # 1.2 Produktivitätsrate (Teile pro Stunde)
    print("\n📊 1.2 Produktivitätsraten:")
    total_productive_hours = (
        np.sum(data["productive_times"], axis=1) / 60
    )  # Minuten -> Stunden
    productivity_rates = parts_per_machine / total_productive_hours

    for machine_id, rate in enumerate(productivity_rates):
        print(f"  Maschine {machine_id + 1:2d}: {rate:.1f} Teile/Stunde")

    # 1.3 Maschinenauslastung
    print("\n📊 1.3 Maschinenauslastung (Verfügbarkeit):")
    max_possible_time = data["shift_count"] * 480  # 8h pro Schicht in Minuten
    availability = np.sum(data["productive_times"], axis=1) / max_possible_time * 100

    for machine_id, avail in enumerate(availability):
        status = "🟢" if avail >= 85 else "🟡" if avail >= 70 else "🔴"
        print(f"  Maschine {machine_id + 1:2d}: {avail:.1f}% {status}")

    # 1.4 Top-Performer identifizieren
    print("\n🏆 1.4 Top-Performer:")
    # Kombiniere Produktivität und Verfügbarkeit
    performance_score = productivity_rates * (availability / 100)
    top_machines = np.argsort(performance_score)[::-1][:3]

    for rank, machine_idx in enumerate(top_machines, 1):
        print(
            f"  {rank}. Platz: Maschine {machine_idx + 1} (Score: {performance_score[machine_idx]:.1f})"
        )

    duration = time.time() - start_time
    print(f"\n⚡ Berechnung in {duration:.3f} Sekunden abgeschlossen")
    print("💡 NumPy ermöglicht diese komplexe Analyse in Millisekunden!")
    print()


def aufgabe_2_qualitaetskontrolle(data: dict):
    """Aufgabe 2: Umfassende Qualitätskontrolle aller Messungen"""
    print("🎯 AUFGABE 2: QUALITÄTSKONTROLLE DURCHFÜHREN")
    print("-" * 50)
    print("Ziel: Analysiere alle Qualitätsmessungen und berechne Qualitätskennzahlen")
    print()

    start_time = time.time()

    quality_data = data["quality_measurements"]
    targets = data["target_values"]
    tolerances = data["tolerances"]
    names = data["measurement_names"]

    print("📊 2.1 Toleranzprüfung für alle Messungen:")

    # 2.1 Toleranzprüfung mit Broadcasting
    deviations = np.abs(
        quality_data - targets
    )  # Broadcasting: (n_parts, 3) - (3,) = (n_parts, 3)
    in_tolerance = deviations <= tolerances  # Element-wise Vergleich

    # Ausschussrate pro Messung
    reject_rates = (1 - np.mean(in_tolerance, axis=0)) * 100

    for i, (name, rate) in enumerate(zip(names, reject_rates, strict=False)):
        parts_ok = np.sum(in_tolerance[:, i])
        total_parts = len(quality_data)
        status = "🟢" if rate < 1.0 else "🟡" if rate < 3.0 else "🔴"
        print(
            f"  {name:6s}: {parts_ok:5d}/{total_parts:5d} OK ({rate:4.1f}% Ausschuss) {status}"
        )

    # 2.2 Statistische Prozesskontrolle (SPC)
    print("\n📊 2.2 Statistische Kennwerte:")

    means = np.mean(quality_data, axis=0)
    stds = np.std(quality_data, axis=0, ddof=1)  # Stichproben-Standardabweichung

    # Prozessfähigkeiten berechnen
    cp_values = tolerances / (3 * stds)  # Cp = Toleranz / (6σ)

    # Cpk (berücksichtigt Zentrierung)
    upper_limits = targets + tolerances / 2
    lower_limits = targets - tolerances / 2
    cpk_upper = (upper_limits - means) / (3 * stds)
    cpk_lower = (means - lower_limits) / (3 * stds)
    cpk_values = np.minimum(cpk_upper, cpk_lower)

    for i, name in enumerate(names):
        cp_status = (
            "🟢" if cp_values[i] >= 1.33 else "🟡" if cp_values[i] >= 1.0 else "🔴"
        )
        cpk_status = (
            "🟢" if cpk_values[i] >= 1.33 else "🟡" if cpk_values[i] >= 1.0 else "🔴"
        )

        print(f"  {name}:")
        print(f"    μ = {means[i]:6.3f} mm, σ = {stds[i]:6.4f} mm")
        print(
            f"    Cp = {cp_values[i]:4.2f} {cp_status}, Cpk = {cpk_values[i]:4.2f} {cpk_status}"
        )

    # 2.3 Ausreißer-Detektion (3-Sigma-Regel)
    print("\n📊 2.3 Ausreißer-Detektion (3σ-Regel):")

    z_scores = np.abs((quality_data - means) / stds)  # Z-Scores für alle Messungen
    outliers = z_scores > 3  # Ausreißer mit |z| > 3

    outlier_counts = np.sum(outliers, axis=0)
    outlier_rates = outlier_counts / len(quality_data) * 100

    for i, (name, count, rate) in enumerate(
        zip(names, outlier_counts, outlier_rates, strict=False)
    ):
        status = "🟢" if rate < 0.1 else "🟡" if rate < 0.5 else "🔴"
        print(f"  {name}: {count:3d} Ausreißer ({rate:.2f}%) {status}")

    # 2.4 Korrelationsanalyse
    print("\n📊 2.4 Korrelationsanalyse zwischen Messungen:")

    correlation_matrix = np.corrcoef(
        quality_data.T
    )  # Transponieren für richtige Korrelation

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            corr = correlation_matrix[i, j]
            strength = (
                "stark"
                if abs(corr) > 0.7
                else "mittel" if abs(corr) > 0.3 else "schwach"
            )
            direction = "positiv" if corr > 0 else "negativ"
            print(
                f"  {names[i]} ↔ {names[j]}: r = {corr:5.3f} ({strength} {direction})"
            )

    duration = time.time() - start_time
    print(f"\n⚡ Qualitätsanalyse in {duration:.3f} Sekunden abgeschlossen")
    print(
        f"📊 {len(quality_data):,} Teile mit {len(quality_data) * 3:,} Messungen analysiert!"
    )
    print()


def aufgabe_3_maschinenperformance(data: dict):
    """Aufgabe 3: Detaillierte Maschinenperformance-Analyse"""
    print("🎯 AUFGABE 3: MASCHINENPERFORMANCE VERGLEICHEN")
    print("-" * 50)
    print("Ziel: Analysiere Zykluszeiten und identifiziere Optimierungspotential")
    print()

    start_time = time.time()

    # 3.1 Zykluszeit-Analyse
    print("📊 3.1 Zykluszeit-Statistiken:")

    cycle_times = data["cycle_times"]
    parts_per_shift = data["parts_per_shift"]

    # Simuliere Zuordnung von Zykluszeiten zu Maschinen
    # (vereinfacht: teile Zykluszeiten entsprechend der Produktionsmenge auf)
    cumulative_parts = np.cumsum(parts_per_shift.flatten())
    machine_assignments = np.zeros(len(cycle_times), dtype=int)

    start_idx = 0
    for machine_id in range(data["machine_count"]):
        machine_parts = np.sum(parts_per_shift[machine_id, :])
        end_idx = start_idx + machine_parts
        if end_idx <= len(cycle_times):
            machine_assignments[start_idx:end_idx] = machine_id
        start_idx = end_idx

    print("  Zykluszeiten pro Maschine:")
    machine_cycle_stats = []

    for machine_id in range(data["machine_count"]):
        machine_cycles = cycle_times[machine_assignments == machine_id]
        if len(machine_cycles) > 0:
            mean_cycle = np.mean(machine_cycles)
            std_cycle = np.std(machine_cycles)
            min_cycle = np.min(machine_cycles)
            max_cycle = np.max(machine_cycles)

            machine_cycle_stats.append(
                {
                    "machine": machine_id + 1,
                    "mean": mean_cycle,
                    "std": std_cycle,
                    "min": min_cycle,
                    "max": max_cycle,
                    "count": len(machine_cycles),
                }
            )

            efficiency = (
                "🟢" if mean_cycle <= 45 else "🟡" if mean_cycle <= 50 else "🔴"
            )
            print(
                f"    Maschine {machine_id + 1:2d}: μ={mean_cycle:5.1f}s, σ={std_cycle:4.1f}s "
                f"[{min_cycle:4.1f}-{max_cycle:4.1f}s] {efficiency}"
            )

    # 3.2 Effizienz-Ranking
    print("\n📊 3.2 Effizienz-Ranking (nach mittlerer Zykluszeit):")

    if machine_cycle_stats:
        # Sortiere nach mittlerer Zykluszeit (aufsteigend = besser)
        sorted_machines = sorted(machine_cycle_stats, key=lambda x: x["mean"])

        for rank, machine_data in enumerate(sorted_machines[:5], 1):
            improvement_potential = machine_data["mean"] - sorted_machines[0]["mean"]
            print(
                f"    {rank}. Maschine {machine_data['machine']:2d}: "
                f"{machine_data['mean']:5.1f}s (+{improvement_potential:4.1f}s zur Besten)"
            )

    # 3.3 Variabilität-Analyse
    print("\n📊 3.3 Prozessstabilität (Variabilität):")

    if machine_cycle_stats:
        for machine_data in machine_cycle_stats:
            cv = (
                machine_data["std"] / machine_data["mean"] * 100
            )  # Variationskoeffizient
            stability = "🟢" if cv <= 5 else "🟡" if cv <= 10 else "🔴"
            print(
                f"    Maschine {machine_data['machine']:2d}: CV = {cv:4.1f}% {stability}"
            )

    # 3.4 Gesamtperformance-Score
    print("\n📊 3.4 Gesamtperformance-Score:")

    if machine_cycle_stats:
        for machine_data in machine_cycle_stats:
            # Score basiert auf Geschwindigkeit (niedriger = besser) und Stabilität
            speed_score = 50 / machine_data["mean"]  # Basis: 50s Zykluszeit
            stability_score = 10 / (
                machine_data["std"] / machine_data["mean"] * 100
            )  # Basis: 10% CV
            total_score = (speed_score + stability_score) / 2

            rating = (
                "⭐⭐⭐"
                if total_score >= 1.2
                else "⭐⭐" if total_score >= 1.0 else "⭐"
            )
            print(
                f"    Maschine {machine_data['machine']:2d}: Score = {total_score:.2f} {rating}"
            )

    duration = time.time() - start_time
    print(f"\n⚡ Performance-Analyse in {duration:.3f} Sekunden abgeschlossen")
    print(
        "💡 Mit NumPy können Millionen von Zykluszeiten in Sekunden analysiert werden!"
    )
    print()


def aufgabe_4_trend_analyse(data: dict):
    """Aufgabe 4: Trend-Analyse und einfache Prognose"""
    print("🎯 AUFGABE 4: TREND-ANALYSE UND PROGNOSE")
    print("-" * 50)
    print("Ziel: Erkenne Trends in Qualität und Produktivität über die Zeit")
    print()

    start_time = time.time()

    # 4.1 Qualitätstrend über die Zeit
    print("📈 4.1 Qualitätstrend-Analyse:")

    quality_data = data["quality_measurements"]
    names = data["measurement_names"]
    n_parts = len(quality_data)

    # Simuliere zeitliche Reihenfolge (jedes Teil hat einen Zeitstempel)
    window_size = 500  # Gleitender Durchschnitt über 500 Teile

    for i, name in enumerate(names):
        measurements = quality_data[:, i]

        # Berechne gleitenden Durchschnitt
        if n_parts >= window_size:
            moving_avg = np.convolve(
                measurements, np.ones(window_size) / window_size, mode="valid"
            )

            # Trend-Berechnung (lineare Regression vereinfacht)
            x = np.arange(len(moving_avg))
            trend_slope = np.polyfit(x, moving_avg, 1)[0]  # Steigung der Trendlinie

            # Trend-Richtung bestimmen
            if abs(trend_slope) < 0.001:
                trend_direction = "→ stabil"
                trend_icon = "🟢"
            elif trend_slope > 0:
                trend_direction = "↗️ steigend"
                trend_icon = "🟡" if trend_slope > 0.005 else "🟢"
            else:
                trend_direction = "↘️ fallend"
                trend_icon = "🟡" if trend_slope < -0.005 else "🟢"

            print(
                f"  {name}: {trend_direction} (Steigung: {trend_slope:+.6f}) {trend_icon}"
            )
        else:
            print(f"  {name}: Zu wenig Daten für Trend-Analyse")

    # 4.2 Produktivitätstrend
    print("\n📈 4.2 Produktivitätstrend pro Schicht:")

    parts_per_shift = data["parts_per_shift"]
    shifts = parts_per_shift.shape[1]

    # Durchschnittliche Produktion pro Schicht über alle Maschinen
    avg_production_per_shift = np.mean(parts_per_shift, axis=0)

    # Trend über Schichten
    shift_numbers = np.arange(shifts)
    production_trend = np.polyfit(shift_numbers, avg_production_per_shift, 1)[0]

    print("  Durchschnittliche Produktion pro Schicht:")
    for shift_id, production in enumerate(avg_production_per_shift):
        day = shift_id // 3 + 1
        shift_in_day = shift_id % 3 + 1
        print(f"    Tag {day}, Schicht {shift_in_day}: {production:.1f} Teile")

    if production_trend > 1:
        trend_text = "↗️ Produktivität steigt"
        trend_icon = "🟢"
    elif production_trend < -1:
        trend_text = "↘️ Produktivität fällt"
        trend_icon = "🔴"
    else:
        trend_text = "→ Produktivität stabil"
        trend_icon = "🟢"

    print(
        f"\n  Trend: {trend_text} ({production_trend:+.1f} Teile/Schicht) {trend_icon}"
    )

    # 4.3 Einfache Prognose für nächste Schicht
    print("\n📈 4.3 Prognose für nächste Schicht:")

    # Lineare Extrapolation
    next_shift_prediction = avg_production_per_shift[-1] + production_trend
    total_prediction = next_shift_prediction * data["machine_count"]

    # Konfidenzintervall basierend auf historischer Variabilität
    historical_std = np.std(avg_production_per_shift)
    confidence_lower = total_prediction - 1.96 * historical_std * data["machine_count"]
    confidence_upper = total_prediction + 1.96 * historical_std * data["machine_count"]

    print(f"  Erwartete Produktion: {total_prediction:.0f} Teile")
    print(
        f"  95% Konfidenzintervall: {confidence_lower:.0f} - {confidence_upper:.0f} Teile"
    )

    # 4.4 Qualitäts-Prognose
    print("\n📈 4.4 Qualitäts-Prognose:")

    targets = data["target_values"]
    recent_quality = quality_data[-1000:] if len(quality_data) >= 1000 else quality_data
    recent_means = np.mean(recent_quality, axis=0)

    for i, (name, recent_mean, target) in enumerate(
        zip(names, recent_means, targets, strict=False)
    ):
        deviation = recent_mean - target
        if abs(deviation) <= data["tolerances"][i] / 4:
            status = "🟢 Im Zielbereich"
        elif abs(deviation) <= data["tolerances"][i] / 2:
            status = "🟡 Aufmerksamkeit erforderlich"
        else:
            status = "🔴 Korrektur notwendig"

        print(f"  {name}: {recent_mean:.3f} mm (Ziel: {target:.1f} mm) {status}")

    duration = time.time() - start_time
    print(f"\n⚡ Trend-Analyse in {duration:.3f} Sekunden abgeschlossen")
    print("📊 NumPy macht komplexe statistische Analysen trivial!")
    print()


def aufgabe_5_gesamtauswertung(data: dict):
    """Aufgabe 5: Zusammenfassende Gesamtauswertung und Report-Generierung"""
    print("🎯 AUFGABE 5: GESAMTAUSWERTUNG UND REPORT")
    print("-" * 50)
    print("Ziel: Erstelle einen umfassenden Produktionsreport")
    print()

    start_time = time.time()

    # 5.1 Key Performance Indicators (KPIs)
    print("📊 5.1 KEY PERFORMANCE INDICATORS (KPIs):")
    print("-" * 40)

    # Produktions-KPIs
    total_parts = data["parts_produced"]
    total_time_hours = np.sum(data["productive_times"]) / 60  # Minuten -> Stunden
    overall_productivity = total_parts / total_time_hours

    # Qualitäts-KPIs
    quality_data = data["quality_measurements"]
    targets = data["target_values"]
    tolerances = data["tolerances"]

    all_deviations = np.abs(quality_data - targets)
    all_in_tolerance = all_deviations <= tolerances
    overall_quality_rate = np.mean(all_in_tolerance) * 100

    # Effizienz-KPIs
    cycle_times = data["cycle_times"]
    avg_cycle_time = np.mean(cycle_times)
    theoretical_max_parts = total_time_hours * 3600 / 45  # Bei 45s Zielzykluszeit
    efficiency = (total_parts / theoretical_max_parts) * 100

    print("  🏭 PRODUKTION:")
    print(f"    • Gesamtproduktion:     {total_parts:,} Teile")
    print(f"    • Produktivität:        {overall_productivity:.1f} Teile/Stunde")
    print(f"    • Effizienz:           {efficiency:.1f}% der theoretischen Kapazität")
    print()
    print("  ✅ QUALITÄT:")
    print(f"    • Gesamtqualitätsrate: {overall_quality_rate:.1f}%")
    print(f"    • Mittlere Zykluszeit:  {avg_cycle_time:.1f}s")
    print(f"    • Ausschussrate:       {100 - overall_quality_rate:.2f}%")

    # 5.2 Performance-Matrix
    print("\n📊 5.2 PERFORMANCE-MATRIX:")
    print("-" * 40)

    # Erstelle Performance-Matrix für alle Maschinen
    parts_per_machine = np.sum(data["parts_per_shift"], axis=1)
    productive_hours_per_machine = np.sum(data["productive_times"], axis=1) / 60
    productivity_per_machine = parts_per_machine / productive_hours_per_machine

    # Kategorisiere Maschinen
    high_productivity_threshold = np.percentile(productivity_per_machine, 75)
    low_productivity_threshold = np.percentile(productivity_per_machine, 25)

    performance_categories = {
        "top_performer": [],
        "average_performer": [],
        "needs_attention": [],
    }

    for machine_id, productivity in enumerate(productivity_per_machine):
        if productivity >= high_productivity_threshold:
            performance_categories["top_performer"].append(machine_id + 1)
        elif productivity <= low_productivity_threshold:
            performance_categories["needs_attention"].append(machine_id + 1)
        else:
            performance_categories["average_performer"].append(machine_id + 1)

    print(
        f"  🏆 Top-Performer:      Maschinen {performance_categories['top_performer']}"
    )
    print(
        f"  📊 Durchschnitt:       Maschinen {performance_categories['average_performer']}"
    )
    print(
        f"  ⚠️  Aufmerksamkeit:     Maschinen {performance_categories['needs_attention']}"
    )

    # 5.3 Handlungsempfehlungen
    print("\n📋 5.3 HANDLUNGSEMPFEHLUNGEN:")
    print("-" * 40)

    recommendations = []

    # Qualitätsempfehlungen
    quality_rates_per_measurement = np.mean(all_in_tolerance, axis=0) * 100
    for i, (name, rate) in enumerate(
        zip(data["measurement_names"], quality_rates_per_measurement, strict=False)
    ):
        if rate < 95:
            recommendations.append(
                f"🔧 {name}: Qualitätsrate {rate:.1f}% - Maschinenjustierung erforderlich"
            )

    # Produktivitätsempfehlungen
    if efficiency < 80:
        recommendations.append(
            f"⚡ Effizienz {efficiency:.1f}% - Zykluszeit-Optimierung prüfen"
        )

    # Wartungsempfehlungen
    machine_availability = (
        np.sum(data["productive_times"], axis=1) / (data["shift_count"] * 480) * 100
    )
    for machine_id, availability in enumerate(machine_availability):
        if availability < 75:
            recommendations.append(
                f"🔧 Maschine {machine_id + 1}: Verfügbarkeit {availability:.1f}% - Wartung planen"
            )

    if recommendations:
        for i, rec in enumerate(recommendations, 1):
            print(f"  {i}. {rec}")
    else:
        print("  ✅ Alle KPIs im Zielbereich - keine Maßnahmen erforderlich")

    # 5.4 Report-Export (Simulation)
    print("\n📄 5.4 REPORT-EXPORT:")
    print("-" * 40)

    # Erstelle Report-Datenstruktur
    report_data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "summary": {
            "total_parts": int(total_parts),
            "productivity": round(overall_productivity, 1),
            "quality_rate": round(overall_quality_rate, 1),
            "efficiency": round(efficiency, 1),
        },
        "machines": {
            f"machine_{i + 1}": {
                "parts_produced": int(parts),
                "productivity": round(prod, 1),
                "availability": round(avail, 1),
            }
            for i, (parts, prod, avail) in enumerate(
                zip(
                    parts_per_machine,
                    productivity_per_machine,
                    machine_availability,
                    strict=False,
                )
            )
        },
        "quality": {
            name: {
                "quality_rate": round(rate, 1),
                "mean_value": round(np.mean(quality_data[:, i]), 3),
                "std_deviation": round(np.std(quality_data[:, i], ddof=1), 4),
            }
            for i, (name, rate) in enumerate(
                zip(
                    data["measurement_names"],
                    quality_rates_per_measurement,
                    strict=False,
                )
            )
        },
        "recommendations": recommendations,
    }

    # Simuliere JSON-Export
    report_json = json.dumps(report_data, indent=2, ensure_ascii=False)

    print(f"  📊 Report generiert: {len(report_json):,} Zeichen")
    print("  📁 Exportformat: JSON")
    print(f"  🕒 Zeitstempel: {report_data['timestamp']}")
    print(
        f"  📈 Enthält: {len(report_data['machines'])} Maschinen, {len(report_data['quality'])} Qualitätsmerkmale"
    )

    # Beispiel-Ausgabe (erste paar Zeilen)
    print("\n  📝 Report-Auszug:")
    for line in report_json.split("\n")[:10]:
        print(f"    {line}")
    print("    ...")

    duration = time.time() - start_time
    print(f"\n⚡ Gesamtauswertung in {duration:.3f} Sekunden abgeschlossen")
    print(
        f"🚀 {total_parts:,} Teile mit {len(quality_data) * 3:,} Messungen ausgewertet!"
    )
    print()

    # 5.5 Performance-Zusammenfassung
    print("📊 5.5 PERFORMANCE-ZUSAMMENFASSUNG:")
    print("-" * 40)
    print(f"  • Datenverarbeitung:   {len(quality_data):,} Datensätze")
    print(f"  • Berechnungszeit:     {duration:.3f} Sekunden")
    print(
        f"  • Verarbeitungsrate:   {len(quality_data) / duration:.0f} Datensätze/Sekunde"
    )
    print("  • Memory-Effizienz:    NumPy Arrays vs. Python Listen")
    print("  • Skalierbarkeit:      Linear mit Datenmenge")
    print()
    print("💡 Diese Analyse wäre mit Excel/VBA 10-100x langsamer!")


if __name__ == "__main__":
    main()
