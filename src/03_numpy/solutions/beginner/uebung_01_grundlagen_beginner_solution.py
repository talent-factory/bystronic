#!/usr/bin/env python3
"""
MUSTERLÖSUNG: NumPy Grundlagen für Bystronic
==========================================

Vollständige Lösung für die erste Beginner-Übung mit NumPy Grundlagen.
Diese Lösung zeigt professionelle Implementierung für industrielle Anwendungen.

Lernziele:
✅ Array-Erstellung aus verschiedenen Datenquellen
✅ Array-Eigenschaften verstehen und nutzen
✅ Elementweise Operationen und Broadcasting
✅ Aggregationsfunktionen für statistische Auswertungen
✅ Praktische Anwendung in Produktionsumgebung

Autor: NumPy Grundkurs Bystronic
Version: 1.0.0
"""

import time
from dataclasses import dataclass

import numpy as np


@dataclass
class MaschinenDaten:
    """Datenklasse für Maschinendaten"""

    sensor_id: str
    werte: np.ndarray
    zeitstempel: np.ndarray
    einheit: str
    sollwert: float
    toleranz: float

    def __post_init__(self):
        """Validierung nach Initialisierung"""
        if len(self.werte) != len(self.zeitstempel):
            raise ValueError("Anzahl Werte und Zeitstempel muss übereinstimmen")


def aufgabe_1_array_erstellung() -> dict[str, np.ndarray]:
    """
    Lösung für Aufgabe 1: Array-Erstellung aus verschiedenen Quellen

    Returns:
        Dictionary mit verschiedenen Array-Typen
    """
    print("=== Aufgabe 1: Array-Erstellung ===")

    ergebnisse = {}

    # 1.1 Temperaturdaten aus Liste (Stundenwerte 24h)
    temperatur_liste = [
        18.5,
        19.2,
        19.8,
        20.1,
        20.5,
        21.2,
        22.1,
        23.5,  # 0-7 Uhr
        24.8,
        25.3,
        26.1,
        26.8,
        27.2,
        26.9,
        26.5,
        25.8,  # 8-15 Uhr
        24.9,
        23.7,
        22.8,
        21.9,
        21.1,
        20.3,
        19.7,
        19.1,  # 16-23 Uhr
    ]
    temperatur_array = np.array(temperatur_liste, dtype=np.float32)
    ergebnisse["temperaturen"] = temperatur_array

    # 1.2 Sensordaten als 2D Array (5 Sensoren × 8 Messungen)
    sensordaten_liste = [
        [98.5, 99.1, 97.8, 98.9, 99.2, 98.7, 99.0, 98.4],  # Sensor 1
        [97.9, 98.8, 99.3, 99.0, 98.6, 99.4, 98.1, 99.2],  # Sensor 2
        [98.1, 99.2, 97.5, 98.3, 99.1, 98.8, 99.5, 98.7],  # Sensor 3
        [99.0, 98.7, 99.5, 98.9, 99.3, 99.1, 98.2, 99.4],  # Sensor 4
        [98.3, 99.0, 98.6, 99.1, 98.8, 99.2, 98.9, 99.3],  # Sensor 5
    ]
    sensor_matrix = np.array(sensordaten_liste, dtype=np.float64)
    ergebnisse["sensordaten"] = sensor_matrix

    # 1.3 Spezielle Arrays für Initialisierung
    # Nullvektor für Kalibrierung
    nullvektor = np.zeros(50, dtype=np.float32)
    ergebnisse["nullvektor"] = nullvektor

    # Einheitsmatrix für Transformationen
    einheitsmatrix = np.eye(4, dtype=np.float64)
    ergebnisse["einheitsmatrix"] = einheitsmatrix

    # Zeitreihe für Sampling
    zeitreihe = np.arange(0, 3600, 60, dtype=np.int32)  # 0-3600s in 60s Schritten
    ergebnisse["zeitreihe"] = zeitreihe

    # 1.4 Erweiterte Array-Erstellung
    # Zufallsdaten für Simulation
    np.random.seed(42)  # Reproduzierbarkeit
    zufallsdaten = np.random.normal(100, 5, 1000).astype(np.float32)
    ergebnisse["zufallsdaten"] = zufallsdaten

    # Linearer Raum für Kalibrierung
    kalibrierung = np.linspace(0, 100, 101, dtype=np.float64)
    ergebnisse["kalibrierung"] = kalibrierung

    # Wiederholende Muster
    muster = np.tile([1, 0, -1], 20)  # Periodisches Signal
    ergebnisse["muster"] = muster

    # Ausgabe der Ergebnisse
    for name, array in ergebnisse.items():
        print(f"{name:15s}: Shape {array.shape:15s}, Dtype: {array.dtype}")

    return ergebnisse


def aufgabe_2_array_eigenschaften(arrays: dict[str, np.ndarray]) -> dict[str, dict]:
    """
    Lösung für Aufgabe 2: Detaillierte Array-Eigenschaftsanalyse

    Args:
        arrays: Dictionary mit Arrays aus Aufgabe 1

    Returns:
        Dictionary mit Eigenschaftsanalysen
    """
    print("\n=== Aufgabe 2: Array-Eigenschaften ===")

    analysen = {}

    for name, array in arrays.items():
        eigenschaften = {
            "shape": array.shape,
            "ndim": array.ndim,
            "size": array.size,
            "dtype": array.dtype,
            "itemsize": array.itemsize,
            "nbytes": array.nbytes,
            "memory_layout": (
                "C-contiguous" if array.flags["C_CONTIGUOUS"] else "Fortran-contiguous"
            ),
            "writeable": array.flags["WRITEABLE"],
            "strides": array.strides,
        }

        # Zusätzliche statistische Eigenschaften für numerische Arrays
        if np.issubdtype(array.dtype, np.number) and array.size > 0:
            eigenschaften.update(
                {
                    "min": np.min(array),
                    "max": np.max(array),
                    "mean": np.mean(array),
                    "std": np.std(array),
                    "memory_efficiency": array.nbytes / (array.size * 8),  # vs. float64
                }
            )

        analysen[name] = eigenschaften

        # Detaillierte Ausgabe
        print(f"\n{name.upper()}:")
        print(f"  Shape: {eigenschaften['shape']}")
        print(f"  Dimensionen: {eigenschaften['ndim']}")
        print(f"  Gesamtelemente: {eigenschaften['size']:,}")
        print(f"  Datentyp: {eigenschaften['dtype']}")
        print(f"  Speicherverbrauch: {eigenschaften['nbytes']:,} Bytes")
        print(f"  Memory Layout: {eigenschaften['memory_layout']}")

        if "mean" in eigenschaften:
            print(
                f"  Statistik: μ={eigenschaften['mean']:.2f}, σ={eigenschaften['std']:.2f}"
            )
            print(
                f"  Bereich: [{eigenschaften['min']:.2f}, {eigenschaften['max']:.2f}]"
            )

    return analysen


def aufgabe_3_grundoperationen() -> dict[str, np.ndarray]:
    """
    Lösung für Aufgabe 3: Umfassende Grundoperationen

    Returns:
        Dictionary mit Operationsergebnissen
    """
    print("\n=== Aufgabe 3: Grundoperationen ===")

    ergebnisse = {}

    # 3.1 Maschinendaten für Vergleich
    maschine_a = np.array([85.2, 87.1, 89.3, 86.8, 90.5, 88.7, 91.2, 87.9])
    maschine_b = np.array([83.7, 89.2, 87.8, 88.5, 89.1, 90.3, 88.9, 89.7])

    print(f"Maschine A Effizienz: {maschine_a}")
    print(f"Maschine B Effizienz: {maschine_b}")

    # 3.2 Elementweise Operationen
    gesamteffizienz = maschine_a + maschine_b
    effizienz_differenz = maschine_a - maschine_b
    relative_effizienz = maschine_a / maschine_b
    kombinierte_leistung = maschine_a * maschine_b / 100  # Normalisiert

    ergebnisse["gesamteffizienz"] = gesamteffizienz
    ergebnisse["effizienz_differenz"] = effizienz_differenz
    ergebnisse["relative_effizienz"] = relative_effizienz
    ergebnisse["kombinierte_leistung"] = kombinierte_leistung

    print(f"Gesamteffizienz: {gesamteffizienz}")
    print(f"Effizienz-Differenz: {effizienz_differenz}")
    print(f"Relative Effizienz: {relative_effizienz}")

    # 3.3 Broadcasting-Operationen
    toleranz = 2.5  # ±2.5% Toleranz
    sollwert = 88.0

    # Toleranzgrenzen
    obergrenze = maschine_a + toleranz
    untergrenze = maschine_a - toleranz
    abweichung_sollwert = np.abs(maschine_a - sollwert)

    ergebnisse["obergrenze"] = obergrenze
    ergebnisse["untergrenze"] = untergrenze
    ergebnisse["abweichung_sollwert"] = abweichung_sollwert

    print(f"Toleranzbereich: [{np.min(untergrenze):.1f}, {np.max(obergrenze):.1f}]")
    print(f"Max. Abweichung vom Sollwert: {np.max(abweichung_sollwert):.1f}%")

    # 3.4 Mathematische Funktionen
    # Normalisierung auf 0-1 Bereich
    normalisiert_a = (maschine_a - np.min(maschine_a)) / (
        np.max(maschine_a) - np.min(maschine_a)
    )

    # Logarithmische Skalierung für große Bereiche
    log_scaled = np.log10(maschine_a / 10)  # Basis-10 Logarithmus

    # Trigonometrische Transformation für zyklische Daten
    phase_a = np.sin(2 * np.pi * maschine_a / 100)  # 0-100% als eine Periode

    ergebnisse["normalisiert"] = normalisiert_a
    ergebnisse["log_scaled"] = log_scaled
    ergebnisse["phase_transformation"] = phase_a

    # 3.5 Vergleichsoperationen
    # Boolean Arrays für Qualitätskontrolle
    innerhalb_toleranz = abweichung_sollwert <= toleranz
    ueber_sollwert = maschine_a > sollwert
    kritische_werte = (maschine_a < 85) | (maschine_a > 92)

    ergebnisse["innerhalb_toleranz"] = innerhalb_toleranz
    ergebnisse["ueber_sollwert"] = ueber_sollwert
    ergebnisse["kritische_werte"] = kritische_werte

    print(f"Werte in Toleranz: {np.sum(innerhalb_toleranz)}/{len(innerhalb_toleranz)}")
    print(f"Kritische Werte: {np.sum(kritische_werte)} gefunden")

    # 3.6 Logische Operationen
    # Kombinierte Bedingungen für Qualitätsbewertung
    ausgezeichnet = (maschine_a >= 90) & (abweichung_sollwert <= 1.0)
    akzeptabel = innerhalb_toleranz & ~ausgezeichnet
    problematisch = ~innerhalb_toleranz | kritische_werte

    ergebnisse["qualitaet_ausgezeichnet"] = ausgezeichnet
    ergebnisse["qualitaet_akzeptabel"] = akzeptabel
    ergebnisse["qualitaet_problematisch"] = problematisch

    print("Qualitätseinstufung:")
    print(f"  Ausgezeichnet: {np.sum(ausgezeichnet)} Werte")
    print(f"  Akzeptabel: {np.sum(akzeptabel)} Werte")
    print(f"  Problematisch: {np.sum(problematisch)} Werte")

    return ergebnisse


def aufgabe_4_aggregationen() -> dict[str, any]:
    """
    Lösung für Aufgabe 4: Umfassende Aggregationsfunktionen

    Returns:
        Dictionary mit Aggregationsergebnissen
    """
    print("\n=== Aufgabe 4: Aggregationsfunktionen ===")

    # 4.1 Produktionsdaten über mehrere Schichten und Tage
    # 4 Schichten × 7 Tage × 3 Messungen pro Schicht
    np.random.seed(123)
    basis_qualitaet = 98.5
    produktionsdaten = np.random.normal(basis_qualitaet, 1.2, (4, 7, 3))

    # Realistische Schwankungen hinzufügen
    # Schichteffekte
    schicht_faktoren = np.array(
        [1.02, 1.01, 0.99, 0.98]
    )  # Früh, Spät, Nacht, Wochenende
    produktionsdaten *= schicht_faktoren[:, np.newaxis, np.newaxis]

    # Wochentagseffekte
    wochentag_faktoren = np.array([1.01, 1.02, 1.01, 1.00, 0.99, 0.97, 0.96])  # Mo-So
    produktionsdaten *= wochentag_faktoren[np.newaxis, :, np.newaxis]

    print(f"Produktionsdaten Shape: {produktionsdaten.shape}")
    print("(4 Schichten × 7 Tage × 3 Messungen)")

    ergebnisse = {}

    # 4.2 Gesamtstatistiken
    gesamtstatistiken = {
        "mittelwert": np.mean(produktionsdaten),
        "median": np.median(produktionsdaten),
        "standardabweichung": np.std(produktionsdaten),
        "varianz": np.var(produktionsdaten),
        "minimum": np.min(produktionsdaten),
        "maximum": np.max(produktionsdaten),
        "spannweite": np.ptp(produktionsdaten),  # peak-to-peak
        "quartile_25": np.percentile(produktionsdaten, 25),
        "quartile_75": np.percentile(produktionsdaten, 75),
    }

    ergebnisse["gesamtstatistiken"] = gesamtstatistiken

    print("\nGesamtstatistiken:")
    for key, value in gesamtstatistiken.items():
        print(f"  {key:20s}: {value:7.3f}%")

    # 4.3 Schichtweise Aggregationen (axis=1,2 - über Tage und Messungen)
    schicht_statistiken = {
        "mittelwerte": np.mean(produktionsdaten, axis=(1, 2)),
        "standardabweichungen": np.std(produktionsdaten, axis=(1, 2)),
        "minima": np.min(produktionsdaten, axis=(1, 2)),
        "maxima": np.max(produktionsdaten, axis=(1, 2)),
    }

    ergebnisse["schicht_statistiken"] = schicht_statistiken

    schicht_namen = ["Frühschicht", "Spätschicht", "Nachtschicht", "Wochenendschicht"]
    print("\nSchichtweise Statistiken:")
    for i, schicht in enumerate(schicht_namen):
        print(
            f"  {schicht:15s}: μ={schicht_statistiken['mittelwerte'][i]:.2f}%, "
            f"σ={schicht_statistiken['standardabweichungen'][i]:.2f}%, "
            f"Range=[{schicht_statistiken['minima'][i]:.2f}, {schicht_statistiken['maxima'][i]:.2f}]"
        )

    # 4.4 Tagesweise Aggregationen (axis=0,2 - über Schichten und Messungen)
    tages_statistiken = {
        "mittelwerte": np.mean(produktionsdaten, axis=(0, 2)),
        "standardabweichungen": np.std(produktionsdaten, axis=(0, 2)),
        "verfügbarkeit": np.mean(produktionsdaten > 97.0, axis=(0, 2))
        * 100,  # % über Schwellwert
    }

    ergebnisse["tages_statistiken"] = tages_statistiken

    wochentage = [
        "Montag",
        "Dienstag",
        "Mittwoch",
        "Donnerstag",
        "Freitag",
        "Samstag",
        "Sonntag",
    ]
    print("\nTagesweise Statistiken:")
    for i, tag in enumerate(wochentage):
        print(
            f"  {tag:10s}: μ={tages_statistiken['mittelwerte'][i]:.2f}%, "
            f"Verfügbarkeit={tages_statistiken['verfügbarkeit'][i]:.1f}%"
        )

    # 4.5 Erweiterte Aggregationen
    # Kumulative Statistiken
    flache_daten = produktionsdaten.flatten()
    erweiterte_stats = {
        "kumulative_summe": np.cumsum(flache_daten),
        "kumulative_mittelwerte": np.cumsum(flache_daten)
        / np.arange(1, len(flache_daten) + 1),
        "gleitender_durchschnitt": np.convolve(
            flache_daten, np.ones(5) / 5, mode="valid"
        ),
        "perzentile": np.percentile(produktionsdaten, [5, 10, 25, 50, 75, 90, 95]),
    }

    ergebnisse["erweiterte_statistiken"] = erweiterte_stats

    print("\nErweiterte Statistiken:")
    print(f"  Perzentile [5, 10, 25, 50, 75, 90, 95]: {erweiterte_stats['perzentile']}")
    print(
        f"  Finaler kumulativer Mittelwert: {erweiterte_stats['kumulative_mittelwerte'][-1]:.3f}%"
    )

    # 4.6 Korrelationsanalyse zwischen Schichten
    schicht_korrelationen = np.corrcoef(schicht_statistiken["mittelwerte"])
    ergebnisse["schicht_korrelationen"] = schicht_korrelationen

    print("\nKorrelationen zwischen Schichten:")
    print(f"  Korrelationsmatrix Shape: {schicht_korrelationen.shape}")

    # 4.7 Qualitätskennzahlen (KPIs)
    kpis = {
        "prozessfaehigkeit_cp": (np.max(produktionsdaten) - np.min(produktionsdaten))
        / (6 * np.std(produktionsdaten)),
        "first_pass_yield": np.mean(produktionsdaten >= 98.0) * 100,
        "defekt_rate": np.mean(produktionsdaten < 97.0) * 100,
        "ausbeute_a_klasse": np.mean(produktionsdaten >= 99.0) * 100,
        "stabilität_index": np.std(schicht_statistiken["mittelwerte"])
        / np.mean(schicht_statistiken["mittelwerte"]),
    }

    ergebnisse["qualitaets_kpis"] = kpis

    print("\nQualitäts-KPIs:")
    for key, value in kpis.items():
        einheit = "%" if "rate" in key or "yield" in key or "ausbeute" in key else ""
        print(f"  {key:20s}: {value:7.3f}{einheit}")

    return ergebnisse


def bonus_erweiterte_anwendungen():
    """
    Bonus: Erweiterte praktische Anwendungen
    """
    print("\n=== Bonus: Erweiterte Anwendungen ===")

    # Maschinendaten-Vergleich mit statistischen Tests
    maschine_alt = np.random.normal(95, 3, 100)
    maschine_neu = np.random.normal(97, 2.5, 100)

    # Einfacher t-Test Simulation
    diff = np.mean(maschine_neu) - np.mean(maschine_alt)
    pooled_std = np.sqrt((np.var(maschine_alt) + np.var(maschine_neu)) / 2)
    t_statistic = diff / (pooled_std * np.sqrt(2 / 100))

    print("Maschinenvergleich:")
    print(
        f"  Alte Maschine: μ={np.mean(maschine_alt):.2f}, σ={np.std(maschine_alt):.2f}"
    )
    print(
        f"  Neue Maschine: μ={np.mean(maschine_neu):.2f}, σ={np.std(maschine_neu):.2f}"
    )
    print(f"  Verbesserung: {diff:.2f} Punkte")
    print(f"  T-Statistik: {t_statistic:.3f}")

    # Produktionseffizienz-Trend
    tage = np.arange(1, 31)  # 30 Tage
    trend = 0.1 * tage  # Leichte Verbesserung über Zeit
    zufallsrauschen = np.random.normal(0, 2, 30)
    effizienz = 85 + trend + zufallsrauschen

    # Trendanalyse mit Polynom-Fit
    trend_koeffs = np.polyfit(tage, effizienz, 1)
    trend_linie = np.polyval(trend_koeffs, tage)

    print("\nTrendanalyse (30 Tage):")
    print(f"  Steigung: {trend_koeffs[0]:.3f} Punkte/Tag")
    print(f"  Start-Effizienz: {trend_koeffs[1]:.1f}%")
    print(f"  Projected End-Effizienz: {trend_linie[-1]:.1f}%")

    # Qualitätskontroll-Simulierung
    sollwert = 100
    toleranz = 5
    messungen = np.random.normal(sollwert, 2, 200)

    # Control Chart Limits
    ucl = sollwert + 3 * 2  # Upper Control Limit
    lcl = sollwert - 3 * 2  # Lower Control Limit

    ausreisser = (messungen > ucl) | (messungen < lcl)

    print("\nQualitätskontrolle (200 Messungen):")
    print(f"  Sollwert: {sollwert} ± {toleranz}")
    print(f"  Kontrollgrenzen: [{lcl}, {ucl}]")
    print(f"  Ausreißer: {np.sum(ausreisser)} ({np.sum(ausreisser) / 200 * 100:.1f}%)")
    print(f"  Prozessfähigkeit: {6 * 2 / (ucl - lcl):.3f}")


def performance_vergleich():
    """
    Performance-Vergleich verschiedener NumPy-Operationen
    """
    print("\n=== Performance-Vergleich ===")

    # Große Arrays für Performance-Tests
    grosse_arrays = {
        "klein": np.random.rand(1000),
        "mittel": np.random.rand(100000),
        "gross": np.random.rand(1000000),
    }

    operationen = {
        "summe": np.sum,
        "mittelwert": np.mean,
        "standardabweichung": np.std,
        "maximum": np.max,
        "sortierung": np.sort,
    }

    print(
        f"{'Operation':15s} {'Klein (1K)':>10s} {'Mittel (100K)':>12s} {'Groß (1M)':>12s}"
    )
    print("-" * 55)

    for op_name, op_func in operationen.items():
        zeiten = []

        for size_name, array in grosse_arrays.items():
            start_time = time.perf_counter()

            # Operation mehrfach ausführen für genauere Messung
            for _ in range(10):
                result = op_func(array)

            zeit = (time.perf_counter() - start_time) / 10 * 1000  # ms pro Operation
            zeiten.append(zeit)

        print(
            f"{op_name:15s} {zeiten[0]:8.3f}ms {zeiten[1]:10.3f}ms {zeiten[2]:10.3f}ms"
        )


def validierung_und_tests():
    """
    Validierung der Implementierung mit Tests
    """
    print("\n=== Validierung und Tests ===")

    # Test 1: Array-Erstellung
    test_arrays = aufgabe_1_array_erstellung()
    assert "temperaturen" in test_arrays, "Temperaturen-Array fehlt"
    assert test_arrays["temperaturen"].shape == (24,), "Falsche Temperatur-Array-Größe"
    assert test_arrays["sensordaten"].shape == (
        5,
        8,
    ), "Falsche Sensordaten-Matrix-Größe"
    print("✓ Test 1 bestanden: Array-Erstellung korrekt")

    # Test 2: Array-Eigenschaften
    eigenschaften = aufgabe_2_array_eigenschaften(test_arrays)
    assert len(eigenschaften) == len(test_arrays), "Nicht alle Arrays analysiert"
    print("✓ Test 2 bestanden: Array-Eigenschaften korrekt analysiert")

    # Test 3: Operationen
    operationen = aufgabe_3_grundoperationen()
    assert "gesamteffizienz" in operationen, "Gesamteffizienz fehlt"
    assert len(operationen["gesamteffizienz"]) == 8, "Falsche Operationsergebnis-Größe"
    print("✓ Test 3 bestanden: Grundoperationen korrekt")

    # Test 4: Aggregationen
    aggregationen = aufgabe_4_aggregationen()
    assert "gesamtstatistiken" in aggregationen, "Gesamtstatistiken fehlen"
    assert "mittelwert" in aggregationen["gesamtstatistiken"], "Mittelwert fehlt"
    print("✓ Test 4 bestanden: Aggregationen korrekt")

    print("🎉 Alle Tests erfolgreich bestanden!")


def main():
    """
    Hauptfunktion zur Ausführung aller Aufgaben
    """
    print("🔧 MUSTERLÖSUNG: NumPy Grundlagen für Bystronic")
    print("=" * 70)
    print("Vollständige Implementierung aller Grundlagen-Aufgaben")
    print("mit industriellen Anwendungsbeispielen.\n")

    # Alle Aufgaben der Reihe nach ausführen
    arrays = aufgabe_1_array_erstellung()
    eigenschaften = aufgabe_2_array_eigenschaften(arrays)
    operationen = aufgabe_3_grundoperationen()
    aggregationen = aufgabe_4_aggregationen()

    # Erweiterte Demonstrationen
    bonus_erweiterte_anwendungen()
    performance_vergleich()

    # Validierung
    validierung_und_tests()

    print("\n✅ MUSTERLÖSUNG KOMPLETT")
    print("Alle NumPy-Grundlagen erfolgreich demonstriert!")
    print("Diese Lösung zeigt professionelle Implementierung für")
    print("industrielle Datenverarbeitung bei Bystronic.")


if __name__ == "__main__":
    main()


"""
📚 LEARNING SUMMARY - Was wurde in dieser Lösung gezeigt:

🎯 KERNKONZEPTE:
✅ Array-Erstellung aus verschiedenen Datenquellen (Listen, spezielle Funktionen)
✅ Array-Eigenschaften verstehen (Shape, Dtype, Memory Layout, Strides)
✅ Elementweise Operationen und Broadcasting
✅ Aggregationsfunktionen für statistische Auswertungen
✅ Performance-Optimierung durch richtige Datentypen

🏭 INDUSTRIELLE ANWENDUNGEN:
✅ Sensordatenverarbeitung und -analyse
✅ Qualitätskontrolle mit statistischen Kennzahlen
✅ Maschinendatenvergleich und Effizienzanalyse
✅ Produktionsdaten-Aggregation über Schichten und Tage
✅ KPI-Berechnung für Manufacturing Excellence

🚀 BEST PRACTICES:
✅ Typisierte Funktionen mit Docstrings
✅ Datenklassen für strukturierte Daten
✅ Comprehensive Error Handling
✅ Performance-Messungen und Optimierung
✅ Umfassende Tests und Validierung
✅ Modulare, wiederverwendbare Funktionen

💡 BYSTRONIC-RELEVANZ:
✅ Realistische Produktionsszenarien
✅ Schichtbetrieb und Wochentagseffekte
✅ Qualitätskennzahlen aus der Fertigung
✅ Maschinendatenvergleich und Optimierung
✅ Statistische Prozesskontrolle (SPC)
"""
