#!/usr/bin/env python3
"""
🟢 BEGINNER - NumPy SmartFactory-Datenverarbeitung - HINT 3 (Code-Snippets)
Übung 4: Praktische SmartFactory-Datenverarbeitung

🎯 DETAILLIERTE CODE-BEISPIELE:
"""

import json
import time

import numpy as np


def beispiel_produktionsdaten_simulation():
    """📋 Beispiel für realistische Produktionsdaten-Simulation"""
    print("=" * 60)
    print("🟢 HINT 3: Produktionsdaten-Simulation")
    print("=" * 60)

    # Reproduzierbare Zufallsdaten
    np.random.seed(42)

    # Basis-Parameter
    basis_produktion = 50  # Stück pro Stunde
    schichten_namen = ["Tagschicht", "Spätschicht", "Nachtschicht"]
    schichten_faktoren = [1.0, 0.95, 0.90]  # Produktivitätsfaktoren

    print("🏭 Produktionsdaten-Simulation:")
    print(f"Basis-Produktion: {basis_produktion} Stück/Stunde")
    print()

    # 3D-Array: 3 Schichten × 8 Stunden × verschiedene Metriken
    produktion_daten = []

    for schicht_idx, (name, faktor) in enumerate(
        zip(schichten_namen, schichten_faktoren, strict=False)
    ):
        print(f"Simuliere {name} (Faktor: {faktor})...")

        stunden_produktion = []
        for stunde in range(8):
            # Basis-Wert mit Schichtfaktor
            basis_wert = basis_produktion * faktor

            # Ermüdungseffekt (Produktivität sinkt über die Schicht)
            ermuedung = 1.0 - (stunde * 0.02)  # 2% Verlust pro Stunde

            # Pauseneffekt (Stunde 4 = Pause)
            if stunde == 4:
                pausen_faktor = 0.7  # 30% weniger wegen Pause
            else:
                pausen_faktor = 1.0

            # Zufällige Schwankungen
            noise = np.random.normal(0, 3)  # ±3 Stück Standardabweichung

            # Finale Berechnung
            finale_produktion = basis_wert * ermuedung * pausen_faktor + noise
            finale_produktion = max(
                0, int(finale_produktion)
            )  # Keine negative Produktion

            stunden_produktion.append(finale_produktion)

        produktion_daten.append(stunden_produktion)
        print(f"  Stundenwerte: {stunden_produktion}")

    # Zu NumPy Array konvertieren
    produktion_array = np.array(produktion_daten)
    print(f"\nArray Shape: {produktion_array.shape}")
    print(f"Datentyp: {produktion_array.dtype}")

    return produktion_array, schichten_namen


def beispiel_qualitaetsdaten_simulation():
    """📋 Beispiel für Qualitätsdaten-Simulation"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Qualitätsdaten-Simulation")
    print("=" * 60)

    # Qualitätsdaten basierend auf Produktionsdaten
    np.random.seed(123)  # Andere Seed für verschiedene Zufallsdaten

    # Parameter für realistische Qualitätssimulation
    basis_qualitaet = 0.98  # 98% Basis-Qualitätsrate
    qualitaets_std = 0.015  # Standardabweichung

    print("🔍 Qualitätsdaten-Simulation:")
    print(f"Basis-Qualität: {basis_qualitaet:.1%}")
    print(f"Standardabweichung: {qualitaets_std:.1%}")

    # Simulation für 3 Schichten × 8 Stunden
    qualitaets_matrix = []

    for schicht in range(3):
        schicht_qualitaet = []

        for stunde in range(8):
            # Schichtspezifische Qualitätsschwankungen
            schicht_bonus = [0.01, 0.005, -0.01][schicht]  # Tag > Spät > Nacht

            # Zeitabhängige Schwankungen (Ermüdung, Aufwärmzeit)
            if stunde < 2:  # Aufwärmzeit
                zeit_faktor = -0.005
            elif stunde > 6:  # Ermüdung
                zeit_faktor = -0.01
            else:
                zeit_faktor = 0.005  # Optimale Zeit

            # Zufällige Schwankungen
            zufalls_faktor = np.random.normal(0, qualitaets_std)

            # Finale Qualitätsrate berechnen
            qualitaet = basis_qualitaet + schicht_bonus + zeit_faktor + zufalls_faktor

            # Auf realistischen Bereich begrenzen
            qualitaet = np.clip(qualitaet, 0.85, 1.0)

            schicht_qualitaet.append(qualitaet)

        qualitaets_matrix.append(schicht_qualitaet)

    qualitaets_array = np.array(qualitaets_matrix)
    print(f"Qualitäts-Array Shape: {qualitaets_array.shape}")

    # Beispiel-Ausgabe
    for i, schicht_name in enumerate(["Tagschicht", "Spätschicht", "Nachtschicht"]):
        durchschnitt = np.mean(qualitaets_array[i])
        print(f"{schicht_name}: {durchschnitt:.2%} Durchschnittsqualität")

    return qualitaets_array


def beispiel_schichtanalyse():
    """📋 Beispiel für Schichtanalyse"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Schichtanalyse")
    print("=" * 60)

    # Beispiel-Produktionsdaten
    produktion = np.array(
        [
            [52, 50, 48, 51, 35, 49, 47, 45],  # Tagschicht
            [49, 47, 45, 48, 33, 46, 44, 42],  # Spätschicht
            [45, 43, 41, 44, 30, 42, 40, 38],  # Nachtschicht
        ]
    )

    schichten_namen = ["Tagschicht", "Spätschicht", "Nachtschicht"]

    print("📊 SCHICHT-STATISTIKEN:")

    # Grundstatistiken pro Schicht
    schicht_summen = np.sum(produktion, axis=1)
    schicht_mittelwerte = np.mean(produktion, axis=1)
    schicht_std = np.std(produktion, axis=1)

    for i, name in enumerate(schichten_namen):
        print(f"\n{name}:")
        print(f"  Gesamt: {schicht_summen[i]} Stück")
        print(f"  Durchschnitt: {schicht_mittelwerte[i]:.1f} Stück/Stunde")
        print(f"  Standardabweichung: {schicht_std[i]:.1f}")

    # Vergleichsanalyse
    print("\n📈 SCHICHT-VERGLEICH:")
    gesamt_durchschnitt = np.mean(produktion)
    beste_schicht_idx = np.argmax(schicht_mittelwerte)
    schlechteste_schicht_idx = np.argmin(schicht_mittelwerte)

    print(f"Gesamt-Durchschnitt: {gesamt_durchschnitt:.1f} Stück/Stunde")
    print(
        f"Beste Schicht: {schichten_namen[beste_schicht_idx]} ({schicht_mittelwerte[beste_schicht_idx]:.1f})"
    )
    print(
        f"Schlechteste Schicht: {schichten_namen[schlechteste_schicht_idx]} ({schicht_mittelwerte[schlechteste_schicht_idx]:.1f})"
    )

    # Prozentuale Abweichungen berechnen
    print("\n📊 PROZENTUALE ABWEICHUNGEN vom Durchschnitt:")
    for i, name in enumerate(schichten_namen):
        abweichung = (
            (schicht_mittelwerte[i] - gesamt_durchschnitt) / gesamt_durchschnitt * 100
        )
        print(f"{name}: {abweichung:+.1f}%")

    return schicht_mittelwerte, schicht_summen


def beispiel_qualitaetskontrolle():
    """📋 Beispiel für Qualitätskontrolle mit Boolean Indexing"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Qualitätskontrolle")
    print("=" * 60)

    # Beispiel-Qualitätsdaten (Prozentsätze als Dezimalzahlen)
    qualitaet = np.array(
        [
            [0.98, 0.97, 0.99, 0.96, 0.94, 0.98, 0.97, 0.96],
            [0.97, 0.96, 0.98, 0.95, 0.93, 0.97, 0.96, 0.95],
            [0.95, 0.94, 0.96, 0.93, 0.91, 0.95, 0.94, 0.93],
        ]
    )

    print("🔍 QUALITÄTSKONTROLLE:")
    print("Qualitätsdaten (erste 4 Stunden pro Schicht):")
    for i, schicht in enumerate(["Tag", "Spät", "Nacht"]):
        print(f"{schicht}: {qualitaet[i, :4]}")

    # Toleranzgrenzen definieren
    min_qualitaet = 0.95  # 95% Mindestqualität
    target_qualitaet = 0.98  # 98% Zielqualität

    print("\nQualitäts-Schwellwerte:")
    print(f"Minimum: {min_qualitaet:.0%}")
    print(f"Ziel: {target_qualitaet:.0%}")

    # Boolean Masken erstellen
    print("\n🎯 QUALITÄTS-KATEGORISIERUNG:")

    # Ausschuss (unter Minimum)
    ausschuss_mask = qualitaet < min_qualitaet
    ausschuss_rate = np.mean(ausschuss_mask)
    print(f"Ausschuss (< {min_qualitaet:.0%}): {ausschuss_rate:.1%}")

    # Akzeptabel (zwischen Minimum und Ziel)
    akzeptabel_mask = (qualitaet >= min_qualitaet) & (qualitaet < target_qualitaet)
    akzeptabel_rate = np.mean(akzeptabel_mask)
    print(
        f"Akzeptabel ({min_qualitaet:.0%}-{target_qualitaet:.0%}): {akzeptabel_rate:.1%}"
    )

    # Zielqualität erreicht
    ziel_mask = qualitaet >= target_qualitaet
    ziel_rate = np.mean(ziel_mask)
    print(f"Zielqualität (≥ {target_qualitaet:.0%}): {ziel_rate:.1%}")

    # Qualität pro Schicht
    print("\n📊 QUALITÄT PRO SCHICHT:")
    schichten_namen = ["Tagschicht", "Spätschicht", "Nachtschicht"]
    for i, name in enumerate(schichten_namen):
        schicht_durchschnitt = np.mean(qualitaet[i])
        schicht_ausschuss = np.mean(ausschuss_mask[i])
        print(
            f"{name}: {schicht_durchschnitt:.1%} Ø, {schicht_ausschuss:.1%} Ausschuss"
        )

    return qualitaet, ausschuss_mask, ziel_mask


def beispiel_performance_vergleich():
    """📋 Beispiel für NumPy vs. Python Performance-Vergleich"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Performance-Vergleich")
    print("=" * 60)

    # Große Datenmengen für Performance-Test
    grosse_daten = np.random.randint(
        20, 80, size=(100, 24, 8)
    )  # 100 Tage, 24h, 8 Maschinen
    print(f"Test-Datenset: {grosse_daten.shape} = {grosse_daten.size:,} Datenpunkte")

    def numpy_analyse(daten):
        """Analyse mit NumPy"""
        gesamt_summe = np.sum(daten)
        durchschnitt = np.mean(daten)
        standardabweichung = np.std(daten)
        maximum = np.max(daten)
        minimum = np.min(daten)

        # Erweiterte Statistiken
        median = np.median(daten)
        percentile_95 = np.percentile(daten, 95)

        # Pro-Tag Summen
        tages_summen = np.sum(daten, axis=(1, 2))

        return {
            "summe": gesamt_summe,
            "durchschnitt": durchschnitt,
            "std": standardabweichung,
            "max": maximum,
            "min": minimum,
            "median": median,
            "p95": percentile_95,
            "tages_summen": tages_summen,
        }

    def python_analyse(daten):
        """Analyse mit Standard-Python (langsam!)"""
        # Daten in flache Liste konvertieren
        flache_daten = daten.flatten().tolist()

        gesamt_summe = sum(flache_daten)
        durchschnitt = gesamt_summe / len(flache_daten)

        # Standardabweichung manuell berechnen
        variance = sum((x - durchschnitt) ** 2 for x in flache_daten) / len(
            flache_daten
        )
        standardabweichung = variance**0.5

        maximum = max(flache_daten)
        minimum = min(flache_daten)

        # Median manuell
        sortierte_daten = sorted(flache_daten)
        n = len(sortierte_daten)
        median = (
            sortierte_daten[n // 2]
            if n % 2
            else (sortierte_daten[n // 2 - 1] + sortierte_daten[n // 2]) / 2
        )

        # Tages-Summen (sehr ineffizient)
        tages_summen = []
        for tag in range(daten.shape[0]):
            tag_summe = 0
            for stunde in range(daten.shape[1]):
                for maschine in range(daten.shape[2]):
                    tag_summe += daten[tag, stunde, maschine]
            tages_summen.append(tag_summe)

        return {
            "summe": gesamt_summe,
            "durchschnitt": durchschnitt,
            "std": standardabweichung,
            "max": maximum,
            "min": minimum,
            "median": median,
            "tages_summen": tages_summen,
        }

    # Performance-Test
    print("\n⚡ PERFORMANCE-TEST:")

    # NumPy Version
    start_time = time.time()
    numpy_result = numpy_analyse(grosse_daten)
    numpy_zeit = time.time() - start_time

    # Python Version
    start_time = time.time()
    python_result = python_analyse(grosse_daten)
    python_zeit = time.time() - start_time

    # Ergebnisse
    speedup = python_zeit / numpy_zeit

    print(f"NumPy Zeit: {numpy_zeit:.4f} Sekunden")
    print(f"Python Zeit: {python_zeit:.4f} Sekunden")
    print(f"Speedup: {speedup:.1f}x schneller mit NumPy!")

    # Ergebnisse vergleichen (sollten identisch sein)
    print("\nErgebnis-Vergleich (Durchschnitt):")
    print(f"NumPy: {numpy_result['durchschnitt']:.2f}")
    print(f"Python: {python_result['durchschnitt']:.2f}")

    return numpy_zeit, python_zeit, speedup


def beispiel_report_generation():
    """📋 Beispiel für automatische Berichterstellung"""
    print("\n" + "=" * 60)
    print("🟢 HINT 3: Automatische Berichterstellung")
    print("=" * 60)

    # Beispiel-Daten
    produktion = np.array([[52, 50, 48], [49, 47, 45], [45, 43, 41]])
    qualitaet = np.array([[0.98, 0.97, 0.99], [0.97, 0.96, 0.98], [0.95, 0.94, 0.96]])

    print("📋 STRUKTURIERTER PRODUKTIONSBERICHT:")

    # Report als Dictionary strukturieren
    report = {
        "meta": {
            "zeitstempel": "2024-03-15 16:30:00",
            "berichtszeitraum": "Tagesdaten",
            "anzahl_schichten": int(produktion.shape[0]),
            "stunden_pro_schicht": int(produktion.shape[1]),
        },
        "produktion": {
            "gesamt_stueck": int(np.sum(produktion)),
            "durchschnitt_pro_stunde": float(np.mean(produktion)),
            "beste_stunde": {
                "wert": int(np.max(produktion)),
                "position": {
                    "schicht": int(
                        np.unravel_index(np.argmax(produktion), produktion.shape)[0]
                    )
                    + 1,
                    "stunde": int(
                        np.unravel_index(np.argmax(produktion), produktion.shape)[1]
                    )
                    + 1,
                },
            },
            "schlechteste_stunde": {
                "wert": int(np.min(produktion)),
                "position": {
                    "schicht": int(
                        np.unravel_index(np.argmin(produktion), produktion.shape)[0]
                    )
                    + 1,
                    "stunde": int(
                        np.unravel_index(np.argmin(produktion), produktion.shape)[1]
                    )
                    + 1,
                },
            },
            "pro_schicht": {
                "tagschicht": {
                    "summe": int(np.sum(produktion[0])),
                    "durchschnitt": float(np.mean(produktion[0])),
                },
                "spaetschicht": {
                    "summe": int(np.sum(produktion[1])),
                    "durchschnitt": float(np.mean(produktion[1])),
                },
                "nachtschicht": {
                    "summe": int(np.sum(produktion[2])),
                    "durchschnitt": float(np.mean(produktion[2])),
                },
            },
        },
        "qualitaet": {
            "gesamt_rate": float(np.mean(qualitaet)),
            "beste_qualitaet": float(np.max(qualitaet)),
            "schlechteste_qualitaet": float(np.min(qualitaet)),
            "pro_schicht": {
                "tagschicht": float(np.mean(qualitaet[0])),
                "spaetschicht": float(np.mean(qualitaet[1])),
                "nachtschicht": float(np.mean(qualitaet[2])),
            },
        },
        "kpis": {
            "produktivitaet_trend": "stabil",  # Könnte berechnet werden
            "qualitaets_trend": "positiv",
            "effizienz_score": float(np.mean(produktion) * np.mean(qualitaet)),
        },
    }

    # Report anzeigen
    print(json.dumps(report, indent=2, ensure_ascii=False))

    # Report in Datei speichern (Beispiel)
    print("\n💾 Report kann gespeichert werden als:")
    print("• JSON für Weiterverarbeitung")
    print("• CSV für Excel-Import")
    print("• NumPy .npy für Python-Analyse")

    return report


if __name__ == "__main__":
    # Alle Beispiele ausführen
    produktion_array, schichten = beispiel_produktionsdaten_simulation()
    qualitaets_array = beispiel_qualitaetsdaten_simulation()
    schicht_stats = beispiel_schichtanalyse()
    qualitaets_analyse = beispiel_qualitaetskontrolle()
    performance_results = beispiel_performance_vergleich()
    report = beispiel_report_generation()

    print("\n" + "=" * 60)
    print("🎯 ALLE CODE-BEISPIELE ABGESCHLOSSEN!")
    print("Verwende diese Patterns für deine eigene Implementierung.")
    print("=" * 60)
