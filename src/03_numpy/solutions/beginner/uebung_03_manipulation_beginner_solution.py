#!/usr/bin/env python3
"""
NumPy Array-Manipulation - Vollständige Beginner Solution
=========================================================

Vollständige Musterlösung für NumPy Array-Manipulation mit
Fokus auf industrielle SmartFactory-Anwendungen. Diese Solution
demonstriert alle wichtigen Array-Manipulationstechniken.

Author: Python Expert für SmartFactory
Date: 2025-09-16
"""

from dataclasses import dataclass
from enum import Enum

import numpy as np


class QualitätsStufe(Enum):
    """Enumeration für Qualitätsstufen in der Produktion"""

    EXZELLENT = "exzellent"
    GUT = "gut"
    AKZEPTABEL = "akzeptabel"
    AUSSCHUSS = "ausschuss"


@dataclass
class ProduktionsStatistik:
    """Datenklasse für Produktionsstatistiken"""

    mittelwert: float
    minimum: float
    maximum: float
    standardabweichung: float
    beste_position: tuple[int, ...]
    schlechteste_position: tuple[int, ...]


@dataclass
class QualitätsAnalyse:
    """Datenklasse für Qualitätsanalyse-Ergebnisse"""

    gesamt_anzahl: int
    ausreisser_anzahl: int
    ausreisser_rate: float
    qualitäts_verteilung: dict[QualitätsStufe, int]
    mittelwert_gesamt: float
    mittelwert_gute: float


class NumPyManipulationSolution:
    """
    Vollständige NumPy Array-Manipulation Solution für industrielle Anwendungen
    """

    def __init__(self, debug_mode: bool = False):
        """Initialisiere die Solution-Klasse"""
        self.debug_mode = debug_mode
        self.toleranz_standard = 0.05
        self.sollwert_praezision = 0.1

    def aufgabe_1_reshape_und_transpose(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Aufgabe 1: Array Reshape und Transpose - Vollständige Lösung

        Demonstriert fundamentale Array-Umformung mit kontinuierlichen
        Produktionsdaten einer SmartFactory-Anlage über 72 Stunden.

        Returns:
            Tuple[np.ndarray, np.ndarray]: Umgeformte Arrays und transponierte Version
        """
        print("=" * 70)
        print("🟢 AUFGABE 1: Reshape und Transpose - VOLLSTÄNDIGE LÖSUNG")
        print("=" * 70)

        # Realistische kontinuierliche Produktionsdaten (3 Tage × 24 Stunden)
        # Simuliere typischen Produktionszyklus mit Tag/Nacht-Unterschieden
        stuendliche_basis = np.array(
            [
                # Nachtschicht (0-7h): Niedrigere Produktion
                45,
                42,
                38,
                35,
                33,
                36,
                41,
                48,
                # Frühschicht (8-15h): Hohe Produktion
                65,
                72,
                78,
                81,
                85,
                83,
                79,
                74,
                # Spätschicht (16-23h): Mittlere Produktion
                68,
                71,
                66,
                62,
                58,
                54,
                49,
                46,
            ]
        )

        # Erzeuge 3 Tage mit leichten Variationen
        np.random.seed(42)
        tag1 = stuendliche_basis + np.random.normal(0, 3, 24).astype(int)
        tag2 = stuendliche_basis + np.random.normal(2, 4, 24).astype(
            int
        )  # Leicht höher
        tag3 = stuendliche_basis + np.random.normal(-1, 3, 24).astype(
            int
        )  # Leicht niedriger

        stuendliche_daten = np.concatenate([tag1, tag2, tag3])
        stuendliche_daten = np.clip(stuendliche_daten, 25, 100)  # Realistische Grenzen

        print("📊 Kontinuierliche Produktionsdaten (3 Tage à 24h = 72h total):")
        print(f"Linear: {stuendliche_daten[:12]}... (Erste 12h von 72h)")
        print(f"Shape original: {stuendliche_daten.shape}")
        print(f"Datentyp: {stuendliche_daten.dtype}")
        print(f"Gesamtproduktion: {np.sum(stuendliche_daten)} Teile")
        print(f"Stündlicher Durchschnitt: {np.mean(stuendliche_daten):.1f} Teile/h")
        print()

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Reshape zu 3 Tage × 24 Stunden
        print("🔄 Reshape zu Tage × Stunden Matrix (Zeilen=Tage, Spalten=Stunden):")
        tage_stunden = stuendliche_daten.reshape(3, 24)

        print(f"Shape nach Reshape: {tage_stunden.shape}")
        print(f"Dimensionen: {len(tage_stunden.shape)}D Array")
        print(f"Memory Layout: C-contiguous={tage_stunden.flags['C_CONTIGUOUS']}")

        print("\nTagesproduktion (erste 12 Stunden pro Tag):")
        for tag in range(3):
            tagesproduktion = np.sum(tage_stunden[tag, :])
            nachtproduktion = np.sum(tage_stunden[tag, :8])
            tagproduktion = np.sum(tage_stunden[tag, 8:16])
            abendproduktion = np.sum(tage_stunden[tag, 16:])

            print(f"   Tag {tag + 1}: {tage_stunden[tag, :12]}...")
            print(f"            Gesamt: {tagesproduktion} Teile")
            print(
                f"            Nacht(0-7h): {nachtproduktion}, Tag(8-15h): {tagproduktion}, Abend(16-23h): {abendproduktion}"
            )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Alternative Reshape zu 24 Stunden × 3 Tage
        print(
            "\n🔄 Alternative Reshape: Stunden × Tage Matrix (Zeilen=Stunden, Spalten=Tage):"
        )
        stunden_tage = stuendliche_daten.reshape(24, 3)

        print(f"Shape alternative: {stunden_tage.shape}")
        print("Stundenvergleich über alle Tage (erste 12 Stunden):")
        for stunde in range(min(12, 24)):
            stunden_werte = stunden_tage[stunde, :]
            print(
                f"   {stunde:2d}h: Tag1={stunden_werte[0]:2d}, Tag2={stunden_werte[1]:2d}, Tag3={stunden_werte[2]:2d} "
                f"| Ø={np.mean(stunden_werte):.1f}"
            )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Transpose-Operationen
        print("\n🔄 Transpose-Operationen:")

        # Method 1: .T Attribut
        transponiert_t = tage_stunden.T
        print(f"Transpose mit .T - Shape: {transponiert_t.shape}")

        # Method 2: .transpose() Methode
        transponiert_method = tage_stunden.transpose()
        print(f"Transpose mit .transpose() - Shape: {transponiert_method.shape}")

        # Method 3: np.transpose() Funktion
        transponiert_func = np.transpose(tage_stunden)
        print(f"Transpose mit np.transpose() - Shape: {transponiert_func.shape}")

        # Verifikation der Identität
        print(
            f"Alle Transpose-Methoden identisch: {np.array_equal(transponiert_t, transponiert_method)}"
        )

        print("\nStundenvergleich nach Transpose (erste 12 Stunden):")
        for stunde in range(min(12, 24)):
            stunden_werte = transponiert_t[stunde, :]
            print(
                f"   {stunde:2d}h: {stunden_werte} | Durchschnitt: {np.mean(stunden_werte):.1f}"
            )

        # Erweiterte Reshape-Beispiele
        print("\n🎯 Erweiterte Reshape-Muster:")

        # 3D Reshape: Tage × Schichten × Stunden pro Schicht
        try:
            schicht_aufteilung = stuendliche_daten.reshape(
                3, 3, 8
            )  # 3 Tage × 3 Schichten × 8h
            print(f"3D Reshape (Tage×Schichten×Stunden): {schicht_aufteilung.shape}")

            for tag in range(3):
                print(f"Tag {tag + 1}:")
                for schicht in range(3):
                    schicht_namen = ["Nacht", "Früh", "Spät"]
                    schicht_summe = np.sum(schicht_aufteilung[tag, schicht, :])
                    print(f"  {schicht_namen[schicht]}: {schicht_summe} Teile")

        except ValueError as e:
            print(f"3D Reshape nicht möglich: {e}")

        # Automatische Dimension mit -1
        auto_reshape = stuendliche_daten.reshape(3, -1)  # Automatisch 24 berechnen
        print(f"Auto-Reshape (3, -1): {auto_reshape.shape}")

        # Memory-effiziente Operationen
        self._analyze_memory_usage(tage_stunden, transponiert_t)

        print("\n✅ Aufgabe 1 erfolgreich abgeschlossen!")
        return tage_stunden, transponiert_t

    def aufgabe_2_arrays_kombinieren(self) -> tuple[np.ndarray, np.ndarray]:
        """
        Aufgabe 2: Arrays kombinieren - Vollständige Lösung

        Demonstriert verschiedene Methoden zur Array-Kombination mit
        Multi-Schicht-Produktionsdaten von SmartFactory-Maschinen.

        Returns:
            Tuple[np.ndarray, np.ndarray]: Kombinierte Arrays
        """
        print("\n" + "=" * 70)
        print("🟢 AUFGABE 2: Arrays kombinieren - VOLLSTÄNDIGE LÖSUNG")
        print("=" * 70)

        # Realistische Produktionsdaten für verschiedene Laser-Schneidmaschinen
        # Format: [Maschinen × Stunden]
        schicht_1_frueh = np.array(
            [
                [45, 52, 48, 55],  # SmartFactory Laser 1 - Hochleistungsmodell
                [38, 41, 44, 39],  # SmartFactory Laser 2 - Standard
                [62, 58, 61, 59],  # SmartFactory Laser 3 - Premium
                [51, 49, 53, 47],  # SmartFactory Laser 4 - Mittelklasse
            ]
        )

        schicht_2_spaet = np.array(
            [
                [51, 49, 53, 47],  # Laser 1 - Abendschicht (etwas weniger)
                [42, 45, 40, 46],  # Laser 2 - Stabil
                [65, 63, 67, 64],  # Laser 3 - Weiterhin stark
                [48, 52, 46, 50],  # Laser 4 - Konstant
            ]
        )

        print("📊 Produktionsdaten SmartFactory Laser-Schneidanlagen:")
        print("Frühschicht (4 Laser × 4 Stunden):")
        for i, maschine in enumerate(schicht_1_frueh):
            summe = np.sum(maschine)
            durchschnitt = np.mean(maschine)
            print(f"   Laser {i + 1}: {maschine} | Σ={summe:3d} | Ø={durchschnitt:.1f}")

        print("Spätschicht (4 Laser × 4 Stunden):")
        for i, maschine in enumerate(schicht_2_spaet):
            summe = np.sum(maschine)
            durchschnitt = np.mean(maschine)
            print(f"   Laser {i + 1}: {maschine} | Σ={summe:3d} | Ø={durchschnitt:.1f}")
        print()

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Horizontal kombinieren (concatenate axis=1)
        print("🔗 Horizontale Kombination (8 Stunden pro Laser):")

        # Method 1: np.concatenate
        beide_schichten_concat = np.concatenate(
            [schicht_1_frueh, schicht_2_spaet], axis=1
        )
        print(f"concatenate() - Shape: {beide_schichten_concat.shape}")

        # Method 2: np.hstack (horizontal stack)
        beide_schichten_hstack = np.hstack([schicht_1_frueh, schicht_2_spaet])
        print(f"hstack() - Shape: {beide_schichten_hstack.shape}")

        # Method 3: np.column_stack (für 1D Arrays)
        print(
            f"Identische Ergebnisse: {np.array_equal(beide_schichten_concat, beide_schichten_hstack)}"
        )

        print("Kombinierte 8-Stunden Produktion:")
        for i, maschine in enumerate(beide_schichten_concat):
            gesamt_8h = np.sum(maschine)
            frueh_4h = np.sum(maschine[:4])
            spaet_4h = np.sum(maschine[4:])
            print(f"   Laser {i + 1}: {maschine}")
            print(
                f"            Früh: {frueh_4h:3d} | Spät: {spaet_4h:3d} | Gesamt: {gesamt_8h:3d}"
            )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Vertikal kombinieren (concatenate axis=0)
        print("\n🔗 Vertikale Kombination (Zusätzliche Maschinen):")

        # Zusätzliche Pressbrake-Maschinen (andere Produktlinie)
        zusaetzliche_pressbrakes = np.array(
            [
                [35, 37, 33, 36],  # Pressbrake 1 - Kleinteile
                [58, 56, 61, 59],  # Pressbrake 2 - Großteile
                [41, 43, 39, 42],  # Pressbrake 3 - Universal
            ]
        )

        print("Zusätzliche Pressbrake-Daten (3 Maschinen × 4 Stunden):")
        for i, maschine in enumerate(zusaetzliche_pressbrakes):
            summe = np.sum(maschine)
            print(f"   Pressbrake {i + 1}: {maschine} | Σ={summe:3d}")

        # Method 1: np.concatenate
        alle_maschinen_concat = np.concatenate(
            [schicht_1_frueh, zusaetzliche_pressbrakes], axis=0
        )
        print(f"\nconcatenate() vertikal - Shape: {alle_maschinen_concat.shape}")

        # Method 2: np.vstack (vertical stack)
        alle_maschinen_vstack = np.vstack([schicht_1_frueh, zusaetzliche_pressbrakes])
        print(f"vstack() - Shape: {alle_maschinen_vstack.shape}")

        print("Alle Maschinen kombiniert (7 Maschinen × 4 Stunden):")
        maschinen_namen = [
            "Laser 1",
            "Laser 2",
            "Laser 3",
            "Laser 4",
            "Pressbrake 1",
            "Pressbrake 2",
            "Pressbrake 3",
        ]

        for i, (name, maschine) in enumerate(
            zip(maschinen_namen, alle_maschinen_concat, strict=False)
        ):
            summe = np.sum(maschine)
            maximum = np.max(maschine)
            print(f"   {name:12}: {maschine} | Σ={summe:3d} | Max={maximum:2d}")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Erweiterte Kombinationstechniken
        print("\n🚀 Erweiterte Kombinationstechniken:")

        # 3D Kombination: Schichten als dritte Dimension
        schicht_3d = np.stack([schicht_1_frueh, schicht_2_spaet], axis=2)
        print(f"3D Stack (Maschinen×Stunden×Schichten): {schicht_3d.shape}")

        # Mittlere Produktion über beide Schichten
        schicht_mittel = np.mean(schicht_3d, axis=2)
        print("Durchschnittliche Produktion über beide Schichten:")
        for i, maschine in enumerate(schicht_mittel):
            print(f"   Laser {i + 1}: {maschine}")

        # Split und wieder zusammenfügen
        print("\n🔄 Split und Rejoin Demonstration:")
        gesplittet = np.split(beide_schichten_concat, 2, axis=1)  # In 2 Hälften teilen
        print(
            f"Split in {len(gesplittet)} Teile, Shapes: {[teil.shape for teil in gesplittet]}"
        )

        wieder_vereint = np.concatenate(gesplittet, axis=1)
        print(f"Wieder vereint: {wieder_vereint.shape}")
        print(
            f"Identisch mit Original: {np.array_equal(wieder_vereint, beide_schichten_concat)}"
        )

        # Array Split für ungleiche Teile
        ungleiche_splits = np.array_split(
            beide_schichten_concat, 3, axis=1
        )  # 3 ungleiche Teile
        print(f"Ungleiche Splits: Shapes {[teil.shape for teil in ungleiche_splits]}")

        # Performance-Analyse
        self._benchmark_concatenation_methods(schicht_1_frueh, schicht_2_spaet)

        print("\n✅ Aufgabe 2 erfolgreich abgeschlossen!")
        return beide_schichten_concat, alle_maschinen_concat

    def aufgabe_3_boolean_indexing(
        self,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, QualitätsAnalyse]:
        """
        Aufgabe 3: Boolean Indexing für Qualitätskontrolle - Vollständige Lösung

        Demonstriert umfassendes Boolean Indexing mit realistischen
        Qualitätsmessungen aus SmartFactory-Präzisionsfertigung.

        Returns:
            Tuple mit Messdaten, Ausreißern, guten Messungen und Qualitätsanalyse
        """
        print("\n" + "=" * 70)
        print("🟢 AUFGABE 3: Boolean Indexing Qualitätskontrolle - VOLLSTÄNDIGE LÖSUNG")
        print("=" * 70)

        # Realistische Qualitätsmessungen: Präzision von Laser-Schneidkanten
        np.random.seed(42)
        anzahl_messungen = 100

        # Simuliere realistische Verteilung mit verschiedenen Einflüssen
        basis_messungen = np.random.normal(
            self.sollwert_praezision, 0.02, anzahl_messungen
        )

        # Füge systematische Abweichungen hinzu (Werkzeugverschleiß, Temperatur)
        trend = np.linspace(0, 0.01, anzahl_messungen)  # Leichter Trend nach oben
        temperatur_effekt = 0.005 * np.sin(
            np.linspace(0, 4 * np.pi, anzahl_messungen)
        )  # Periodische Schwankung

        # Füge gelegentliche Ausreißer hinzu (Materialfehler, Vibrationen)
        ausreisser_indizes = np.random.choice(anzahl_messungen, 8, replace=False)
        ausreisser_werte = np.random.normal(0, 0.08, 8)

        messungen = basis_messungen + trend + temperatur_effekt
        messungen[ausreisser_indizes] += ausreisser_werte
        messungen = np.round(messungen, 4)

        print(
            f"📊 Qualitätsmessungen SmartFactory Laser-Präzision ({anzahl_messungen} Teile):"
        )
        print(
            f"Sollwert: {self.sollwert_praezision:.3f} mm ± {self.toleranz_standard:.3f} mm"
        )
        print(f"Messwerte-Beispiel: {messungen[:10]}")
        print(f"Gesamt-Mittelwert: {np.mean(messungen):.4f} mm")
        print(f"Standardabweichung: {np.std(messungen):.4f} mm")
        print(f"Min: {np.min(messungen):.4f} mm, Max: {np.max(messungen):.4f} mm")
        print()

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Ausreißer-Analyse
        print(f"🎯 Ausreißer-Analyse (Toleranz: ±{self.toleranz_standard:.3f} mm):")

        # Grundlegende Ausreißer-Bedingungen
        zu_klein = messungen < (self.sollwert_praezision - self.toleranz_standard)
        zu_gross = messungen > (self.sollwert_praezision + self.toleranz_standard)
        ausreisser_mask = zu_klein | zu_gross

        # Statistische Ausreißer (3-Sigma-Regel)
        mittelwert = np.mean(messungen)
        std_abw = np.std(messungen)
        stat_ausreisser_mask = np.abs(messungen - mittelwert) > 3 * std_abw

        ausreisser = messungen[ausreisser_mask]
        stat_ausreisser = messungen[stat_ausreisser_mask]

        print(
            f"Toleranz-Ausreißer: {np.sum(ausreisser_mask)} von {len(messungen)} ({np.mean(ausreisser_mask):.2%})"
        )
        print(
            f"  Zu klein (<{self.sollwert_praezision - self.toleranz_standard:.3f}): {np.sum(zu_klein)}"
        )
        print(
            f"  Zu groß (>{self.sollwert_praezision + self.toleranz_standard:.3f}): {np.sum(zu_gross)}"
        )

        print(
            f"Statistische Ausreißer (3σ): {np.sum(stat_ausreisser_mask)} ({np.mean(stat_ausreisser_mask):.2%})"
        )

        if len(ausreisser) > 0:
            print("Extremste Ausreißer:")
            extreme_indizes = np.argsort(np.abs(ausreisser - self.sollwert_praezision))[
                -5:
            ]
            for i in extreme_indizes:
                abweichung = ausreisser[i] - self.sollwert_praezision
                print(f"  {ausreisser[i]:.4f} mm (Abweichung: {abweichung:+.4f} mm)")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Gute Messungen filtern
        print("\n✅ Gute Messungen (innerhalb Toleranz):")
        gute_messungen_mask = ~ausreisser_mask
        gute_messungen = messungen[gute_messungen_mask]

        print(
            f"Anzahl gute Messungen: {len(gute_messungen)} von {len(messungen)} ({len(gute_messungen) / len(messungen):.2%})"
        )
        print(f"Mittelwert (nur gute): {np.mean(gute_messungen):.4f} mm")
        print(f"Standardabweichung (nur gute): {np.std(gute_messungen):.4f} mm")
        print(
            f"Verbesserung der Standardabweichung: {(np.std(messungen) - np.std(gute_messungen)) / np.std(messungen):.1%}"
        )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Detaillierte Qualitätskategorisierung
        print("\n📊 Detaillierte Qualitätskategorisierung:")

        # Sehr enge Toleranzen für Premium-Qualität
        exzellent_mask = (messungen >= 0.095) & (messungen <= 0.105)

        # Gute Qualität: etwas weiterer Bereich
        gut_mask = ((messungen >= 0.090) & (messungen < 0.095)) | (
            (messungen > 0.105) & (messungen <= 0.110)
        )

        # Akzeptabel: innerhalb Haupttoleranz aber nicht in den oberen Kategorien
        akzeptabel_mask = ~exzellent_mask & ~gut_mask & ~ausreisser_mask

        # Grenzwertig: knapp außerhalb der Toleranz
        grenzwertig_mask = (
            (messungen >= 0.045)
            & (messungen < (self.sollwert_praezision - self.toleranz_standard))
        ) | (
            (messungen > (self.sollwert_praezision + self.toleranz_standard))
            & (messungen <= 0.155)
        )

        # Echter Ausschuss: weit außerhalb
        ausschuss_mask = ausreisser_mask & ~grenzwertig_mask

        # Qualitätsstatistiken
        kategorien = {
            QualitätsStufe.EXZELLENT: np.sum(exzellent_mask),
            QualitätsStufe.GUT: np.sum(gut_mask),
            QualitätsStufe.AKZEPTABEL: np.sum(akzeptabel_mask),
            QualitätsStufe.AUSSCHUSS: np.sum(ausschuss_mask),
        }

        total_kategorisiert = sum(kategorien.values())

        print("Qualitätskategorien:")
        for kategorie, anzahl in kategorien.items():
            prozent = anzahl / len(messungen) * 100
            bereich = self._get_qualitaets_bereich(kategorie)
            print(
                f"  {kategorie.value.title():12}: {anzahl:3d} Stück ({prozent:5.1f}%) - {bereich}"
            )

        if len(messungen) - total_kategorisiert > 0:
            print(
                f"  Grenzwertig    : {len(messungen) - total_kategorisiert:3d} Stück (Nacharbeit möglich)"
            )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Sequenzielle Analyse
        print("\n🔄 Sequenzielle Qualitätsprobleme:")
        problem_sequenzen = self._find_problem_sequences(ausreisser_mask, messungen)

        if problem_sequenzen:
            print("Aufeinanderfolgende Probleme gefunden:")
            for start, ende, werte in problem_sequenzen:
                print(f"  Messungen {start + 1}-{ende + 1}: {werte}")
        else:
            print("✅ Keine aufeinanderfolgenden Qualitätsprobleme")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Trend-Analyse
        print("\n📈 Trend- und Muster-Analyse:")
        self._analyze_quality_trends(messungen, gute_messungen_mask)

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Prozessfähigkeits-Analyse
        cp, cpk = self._calculate_process_capability(gute_messungen)
        print("\n📊 Prozessfähigkeit (nur gute Messungen):")
        print(f"Cp (Prozessfähigkeit): {cp:.3f}")
        print(f"Cpk (Prozesslage): {cpk:.3f}")
        print(f"Prozessbewertung: {self._evaluate_process_capability(cp, cpk)}")

        # Zusammenfassung erstellen
        qualitaets_analyse = QualitätsAnalyse(
            gesamt_anzahl=len(messungen),
            ausreisser_anzahl=np.sum(ausreisser_mask),
            ausreisser_rate=np.mean(ausreisser_mask),
            qualitäts_verteilung=kategorien,
            mittelwert_gesamt=np.mean(messungen),
            mittelwert_gute=np.mean(gute_messungen),
        )

        print("\n✅ Aufgabe 3 erfolgreich abgeschlossen!")
        return messungen, ausreisser, gute_messungen, qualitaets_analyse

    def aufgabe_4_erweiterte_manipulation(
        self,
    ) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, ProduktionsStatistik]:
        """
        Aufgabe 4: Erweiterte Array-Manipulation - Vollständige Lösung

        Demonstriert komplexe Multi-dimensionale Array-Operationen mit
        realistischen Produktionsdaten einer SmartFactory-Fertigungslinie.

        Returns:
            Tuple mit Produktionsdaten und Statistiken
        """
        print("\n" + "=" * 70)
        print("🟢 AUFGABE 4: Erweiterte Array-Manipulation - VOLLSTÄNDIGE LÖSUNG")
        print("=" * 70)

        # Realistische 3D Produktionsdaten: 5 Werktage × 3 Schichten × 8 Stunden
        np.random.seed(123)

        # Basis-Produktivität für verschiedene Schichten
        nachtschicht_basis = 45  # Niedrigere Produktion nachts
        fruehschicht_basis = 65  # Höchste Produktion
        spaetschicht_basis = 55  # Mittlere Produktion

        # Wochentag-Faktoren (Montag schwächer, Mitte der Woche stärker)
        tag_faktoren = [0.9, 1.0, 1.1, 1.05, 0.95]  # Mo, Di, Mi, Do, Fr

        # Erzeuge realistische Produktionsdaten
        produktion_woche = np.zeros((5, 3, 8), dtype=int)

        for tag in range(5):
            tag_faktor = tag_faktoren[tag]

            for schicht in range(3):
                if schicht == 0:  # Nachtschicht
                    basis = nachtschicht_basis
                elif schicht == 1:  # Frühschicht
                    basis = fruehschicht_basis
                else:  # Spätschicht
                    basis = spaetschicht_basis

                # Stunden-spezifische Variation (Ermüdung, Pausen)
                stunden_variation = np.array(
                    [1.0, 0.95, 0.9, 0.85, 1.1, 1.05, 0.95, 0.9]
                )

                for stunde in range(8):
                    variation = np.random.normal(1.0, 0.15)
                    wert = basis * tag_faktor * stunden_variation[stunde] * variation
                    produktion_woche[tag, schicht, stunde] = max(20, int(wert))

        print("📊 Produktionsdaten SmartFactory-Fertigungslinie:")
        print(f"Dimensionen: {produktion_woche.shape} (Werktage × Schichten × Stunden)")
        print(f"Gesamtproduktion Woche: {np.sum(produktion_woche)} Teile")
        print(f"Durchschnitt pro Stunde: {np.mean(produktion_woche):.1f} Teile/h")

        tage_namen = ["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]
        schicht_namen = ["Nacht", "Früh", "Spät"]

        print("\nDetaillierte Tagesproduktion:")
        for tag in range(5):
            print(f"\n{tage_namen[tag]}:")
            for schicht in range(3):
                schicht_summe = np.sum(produktion_woche[tag, schicht, :])
                schicht_durchschnitt = np.mean(produktion_woche[tag, schicht, :])
                print(
                    f"  {schicht_namen[schicht]:5}: {produktion_woche[tag, schicht]} | Σ={schicht_summe:3d} | Ø={schicht_durchschnitt:.1f}"
                )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Erweiterte Datenaufteilung
        print("\n✂️ Intelligente Wochenaufteilung:")

        # Methode 1: Erste/Zweite Wochenhälfte
        erste_haelfte = produktion_woche[:3]  # Mo, Di, Mi
        zweite_haelfte = produktion_woche[3:]  # Do, Fr

        print(
            f"Erste Hälfte (Mo-Mi): Shape {erste_haelfte.shape}, Summe: {np.sum(erste_haelfte)}"
        )
        print(
            f"Zweite Hälfte (Do-Fr): Shape {zweite_haelfte.shape}, Summe: {np.sum(zweite_haelfte)}"
        )

        # Methode 2: Schichtweise Aufteilung
        nachtschichten = produktion_woche[:, 0, :]
        fruehschichten = produktion_woche[:, 1, :]
        spaetschichten = produktion_woche[:, 2, :]

        print("\nSchichtweise Aufteilung:")
        print(
            f"Alle Nachtschichten: Shape {nachtschichten.shape}, Summe: {np.sum(nachtschichten)}"
        )
        print(
            f"Alle Frühschichten: Shape {fruehschichten.shape}, Summe: {np.sum(fruehschichten)}"
        )
        print(
            f"Alle Spätschichten: Shape {spaetschichten.shape}, Summe: {np.sum(spaetschichten)}"
        )

        # Methode 3: Stundenweise Analyse
        erste_4h = produktion_woche[:, :, :4]  # Erste Hälfte jeder Schicht
        letzte_4h = produktion_woche[:, :, 4:]  # Zweite Hälfte jeder Schicht

        print("\nStundenweise Aufteilung:")
        print(f"Erste 4h pro Schicht: Durchschnitt {np.mean(erste_4h):.1f}")
        print(f"Letzte 4h pro Schicht: Durchschnitt {np.mean(letzte_4h):.1f}")
        print(
            f"Ermüdungseffekt: {(np.mean(erste_4h) - np.mean(letzte_4h)):.1f} Teile/h weniger"
        )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Multi-dimensionale Statistiken
        print("\n📊 Multi-dimensionale Statistik-Analyse:")

        # Statistiken pro Dimension
        # Pro Tag (axis=(1,2) = über alle Schichten und Stunden)
        pro_tag = np.sum(produktion_woche, axis=(1, 2))
        pro_tag_durchschnitt = np.mean(produktion_woche, axis=(1, 2))

        print("Produktion pro Tag:")
        for i, (tag, summe, durchschnitt) in enumerate(
            zip(tage_namen, pro_tag, pro_tag_durchschnitt, strict=False)
        ):
            print(f"  {tag:10}: {summe:4d} Teile | Ø {durchschnitt:.1f} Teile/h")

        # Pro Schicht (axis=(0,2) = über alle Tage und Stunden)
        pro_schicht = np.sum(produktion_woche, axis=(0, 2))
        pro_schicht_durchschnitt = np.mean(produktion_woche, axis=(0, 2))

        print("\nProduktion pro Schicht:")
        for i, (name, summe, durchschnitt) in enumerate(
            zip(schicht_namen, pro_schicht, pro_schicht_durchschnitt, strict=False)
        ):
            print(f"  {name:5}schicht: {summe:4d} Teile | Ø {durchschnitt:.1f} Teile/h")

        # Pro Stunde (axis=(0,1) = über alle Tage und Schichten)
        pro_stunde = np.sum(produktion_woche, axis=(0, 1))
        pro_stunde_durchschnitt = np.mean(produktion_woche, axis=(0, 1))

        print("\nProduktion pro Stunde (über alle Schichten/Tage):")
        for stunde, (summe, durchschnitt) in enumerate(
            zip(pro_stunde, pro_stunde_durchschnitt, strict=False)
        ):
            print(
                f"  Stunde {stunde + 1:2d}: {summe:3d} Teile | Ø {durchschnitt:.1f} Teile/Schicht"
            )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Performance-Extremwerte
        print("\n🏆 Performance-Extremwerte und Analyse:")

        flache_daten = produktion_woche.flatten()

        # Beste und schlechteste Performance
        max_idx = np.unravel_index(np.argmax(produktion_woche), produktion_woche.shape)
        min_idx = np.unravel_index(np.argmin(produktion_woche), produktion_woche.shape)

        max_wert = np.max(produktion_woche)
        min_wert = np.min(produktion_woche)

        print(f"Höchste Stundenproduktion: {max_wert} Teile")
        print(
            f"  Position: {tage_namen[max_idx[0]]}, {schicht_namen[max_idx[1]]}, Stunde {max_idx[2] + 1}"
        )
        print(f"Niedrigste Stundenproduktion: {min_wert} Teile")
        print(
            f"  Position: {tage_namen[min_idx[0]]}, {schicht_namen[min_idx[1]]}, Stunde {min_idx[2] + 1}"
        )
        print(f"Produktionsspanne: {max_wert - min_wert} Teile")

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Top/Bottom Performer Analyse
        print("\n📈 Top/Bottom Performer Detailanalyse:")

        sortierte_indices = np.argsort(flache_daten)

        print("🏆 Top 10 Produktionsstunden:")
        for i in range(-10, 0):
            idx = sortierte_indices[i]
            original_idx = np.unravel_index(idx, produktion_woche.shape)
            wert = flache_daten[idx]
            tag_name = tage_namen[original_idx[0]]
            schicht_name = schicht_namen[original_idx[1]]
            stunde = original_idx[2] + 1
            print(
                f"  #{-i:2d}: {wert:2d} Teile - {tag_name}, {schicht_name}, Stunde {stunde}"
            )

        print("\n📉 Bottom 5 Produktionsstunden:")
        for i in range(5):
            idx = sortierte_indices[i]
            original_idx = np.unravel_index(idx, produktion_woche.shape)
            wert = flache_daten[idx]
            tag_name = tage_namen[original_idx[0]]
            schicht_name = schicht_namen[original_idx[1]]
            stunde = original_idx[2] + 1
            print(
                f"  #{i + 1:2d}: {wert:2d} Teile - {tag_name}, {schicht_name}, Stunde {stunde}"
            )

        # VOLLSTÄNDIGE IMPLEMENTIERUNG: Statistische Kennzahlen
        print("\n📊 Erweiterte Statistische Analyse:")

        # Variationskoeffizient pro Dimension
        cv_tage = np.std(pro_tag) / np.mean(pro_tag) * 100
        cv_schichten = np.std(pro_schicht) / np.mean(pro_schicht) * 100
        cv_stunden = np.std(pro_stunde) / np.mean(pro_stunde) * 100

        print("Variationskoeffizienten (niedrig = konsistent):")
        print(f"  Zwischen Tagen: {cv_tage:.1f}%")
        print(f"  Zwischen Schichten: {cv_schichten:.1f}%")
        print(f"  Zwischen Stunden: {cv_stunden:.1f}%")

        # Quartile und Perzentile
        percentiles = np.percentile(flache_daten, [25, 50, 75, 90, 95])
        print("\nProduktions-Perzentile:")
        print(f"  25% Perzentil (Q1): {percentiles[0]:.1f} Teile")
        print(f"  50% Perzentil (Median): {percentiles[1]:.1f} Teile")
        print(f"  75% Perzentil (Q3): {percentiles[2]:.1f} Teile")
        print(f"  90% Perzentil: {percentiles[3]:.1f} Teile")
        print(f"  95% Perzentil: {percentiles[4]:.1f} Teile")

        # Erweiterte Array-Operationen demonstrieren
        self._demonstrate_advanced_array_ops(produktion_woche)

        # Erstelle Statistik-Objekt
        produktions_statistik = ProduktionsStatistik(
            mittelwert=np.mean(produktion_woche),
            minimum=min_wert,
            maximum=max_wert,
            standardabweichung=np.std(produktion_woche),
            beste_position=max_idx,
            schlechteste_position=min_idx,
        )

        print("\n✅ Aufgabe 4 erfolgreich abgeschlossen!")
        return produktion_woche, pro_tag, pro_schicht, pro_stunde, produktions_statistik

    def bonus_advanced_manipulations(self) -> None:
        """
        Bonus: Hochentwickelte Array-Manipulationstechniken
        """
        print("\n" + "=" * 70)
        print("🚀 BONUS: Hochentwickelte Array-Manipulationstechniken")
        print("=" * 70)

        # Komplexe 4D Daten: Monate × Wochen × Tage × Stunden
        np.random.seed(42)
        jahres_daten = np.random.randint(
            30, 80, (3, 4, 5, 8)
        )  # 3 Monate × 4 Wochen × 5 Tage × 8 Stunden

        print(f"📊 4D Jahresproduktionsdaten: {jahres_daten.shape}")
        print("(Monate × Wochen × Werktage × Stunden)")

        # Erweiterte Dimensionsmanipulation
        print("\n🔄 Erweiterte Dimensionsmanipulation:")

        # Axis-Swap
        swap_axes = np.swapaxes(jahres_daten, 1, 2)  # Wochen und Tage vertauschen
        print(f"Swap Achsen (Woche↔Tag): {jahres_daten.shape} → {swap_axes.shape}")

        # Move Axis
        move_axes = np.moveaxis(jahres_daten, 0, -1)  # Monate nach hinten
        print(f"Move Achse (Monate hinten): {jahres_daten.shape} → {move_axes.shape}")

        # Squeeze und Expand
        mittel_tag = np.mean(jahres_daten, axis=3, keepdims=True)  # Behalte Dimension
        print(f"Mit keepdims: {mittel_tag.shape}")

        mittel_tag_squeezed = np.squeeze(mittel_tag)  # Entferne Singleton-Dimensionen
        print(f"Nach squeeze: {mittel_tag_squeezed.shape}")

        expanded = np.expand_dims(mittel_tag_squeezed, axis=-1)  # Dimension hinzufügen
        print(f"Nach expand_dims: {expanded.shape}")

        # Rolling und Sliding Window Operationen
        print("\n📊 Rolling Window Analyse:")
        flache_zeitreihe = jahres_daten.flatten()
        window_size = 24  # 24-Stunden gleitender Durchschnitt

        rolling_mean = np.convolve(
            flache_zeitreihe, np.ones(window_size) / window_size, mode="valid"
        )
        print(f"24h Rolling Mean: {len(rolling_mean)} Datenpunkte")
        print(f"Trend: {rolling_mean[:5]} ... {rolling_mean[-5:]}")

        # Erweiterte Boolean-Operationen
        print("\n🎯 Erweiterte Boolean-Operationen:")

        # Multiple Bedingungen mit np.where
        bedingung_hoch = jahres_daten > 60
        bedingung_mittel = (jahres_daten >= 45) & (jahres_daten <= 60)
        bedingung_niedrig = jahres_daten < 45

        kategorisiert = np.where(bedingung_hoch, 3, np.where(bedingung_mittel, 2, 1))

        unique, counts = np.unique(kategorisiert, return_counts=True)
        print("Produktionskategorien:")
        for kategorie, anzahl in zip(unique, counts, strict=False):
            namen = {1: "Niedrig", 2: "Mittel", 3: "Hoch"}
            print(
                f"  {namen[kategorie]}: {anzahl} Stunden ({anzahl / np.size(jahres_daten) * 100:.1f}%)"
            )

        # Strukturierte Arrays (Record Arrays)
        print("\n📋 Strukturierte Arrays für komplexe Daten:")

        # Definiere strukturierten Datentyp
        dtype_produktion = np.dtype(
            [
                ("datum", "U10"),
                ("schicht", "U10"),
                ("teile", "i4"),
                ("qualitaet", "f4"),
                ("effizienz", "f4"),
            ]
        )

        # Erzeuge strukturierte Daten
        strukturierte_daten = np.array(
            [
                ("2025-01-15", "Früh", 75, 98.5, 0.95),
                ("2025-01-15", "Spät", 68, 97.8, 0.92),
                ("2025-01-16", "Früh", 82, 99.1, 0.97),
                ("2025-01-16", "Spät", 71, 98.2, 0.94),
            ],
            dtype=dtype_produktion,
        )

        print("Strukturierte Daten:")
        print(strukturierte_daten)
        print(f"Nur Teile-Produktion: {strukturierte_daten['teile']}")
        print(
            f"Durchschnittliche Qualität: {np.mean(strukturierte_daten['qualitaet']):.2f}%"
        )

        # Memory-optimierte Operationen
        print("\n💾 Memory-optimierte Operationen:")
        self._demonstrate_memory_optimization()

    def _analyze_memory_usage(
        self, original: np.ndarray, transposed: np.ndarray
    ) -> None:
        """Analysiere Memory-Usage verschiedener Array-Operationen"""
        print("\n💾 Memory-Analyse:")
        print("Original Array:")
        print(f"  Size: {original.size} Elemente")
        print(f"  Memory: {original.nbytes} bytes")
        print(f"  Strides: {original.strides}")

        print("Transposed Array:")
        print(f"  Size: {transposed.size} Elemente")
        print(f"  Memory: {transposed.nbytes} bytes")
        print(f"  Strides: {transposed.strides}")
        print(f"  Shares Memory: {np.shares_memory(original, transposed)}")

    def _benchmark_concatenation_methods(
        self, arr1: np.ndarray, arr2: np.ndarray
    ) -> None:
        """Benchmark verschiedener Concatenation-Methoden"""
        import time

        print("\n⚡ Concatenation Performance Benchmark:")

        # Größere Arrays für aussagekräftige Benchmarks
        large_arr1 = np.tile(arr1, (100, 1))
        large_arr2 = np.tile(arr2, (100, 1))

        iterations = 1000

        # Method 1: np.concatenate
        start = time.perf_counter()
        for _ in range(iterations):
            result1 = np.concatenate([large_arr1, large_arr2], axis=1)
        zeit_concat = time.perf_counter() - start

        # Method 2: np.hstack
        start = time.perf_counter()
        for _ in range(iterations):
            result2 = np.hstack([large_arr1, large_arr2])
        zeit_hstack = time.perf_counter() - start

        print(f"np.concatenate: {zeit_concat:.4f}s")
        print(f"np.hstack: {zeit_hstack:.4f}s")
        print(f"Schneller: {'concatenate' if zeit_concat < zeit_hstack else 'hstack'}")

    def _get_qualitaets_bereich(self, kategorie: QualitätsStufe) -> str:
        """Gib Qualitätsbereich für Kategorie zurück"""
        bereiche = {
            QualitätsStufe.EXZELLENT: "0.095-0.105 mm",
            QualitätsStufe.GUT: "0.090-0.095, 0.105-0.110 mm",
            QualitätsStufe.AKZEPTABEL: "0.050-0.090, 0.110-0.150 mm",
            QualitätsStufe.AUSSCHUSS: "< 0.050, > 0.150 mm",
        }
        return bereiche.get(kategorie, "Unbekannt")

    def _find_problem_sequences(
        self, mask: np.ndarray, values: np.ndarray
    ) -> list[tuple[int, int, np.ndarray]]:
        """Finde aufeinanderfolgende Problemsequenzen"""
        sequences = []
        diff = np.diff(np.concatenate(([False], mask, [False])).astype(int))
        starts = np.where(diff == 1)[0]
        ends = np.where(diff == -1)[0]

        for start, end in zip(starts, ends, strict=False):
            if end - start > 1:  # Mindestens 2 aufeinanderfolgende Probleme
                sequences.append((start, end, values[start:end]))

        return sequences

    def _analyze_quality_trends(
        self, messungen: np.ndarray, gute_mask: np.ndarray
    ) -> None:
        """Analysiere Qualitätstrends über Zeit"""
        # Gleitender Durchschnitt
        window = 10
        if len(messungen) >= window:
            rolling_mean = np.convolve(
                messungen, np.ones(window) / window, mode="valid"
            )
            trend = np.polyfit(range(len(rolling_mean)), rolling_mean, 1)[0]

            print(f"Trend-Analyse (Gleitender Durchschnitt über {window} Messungen):")
            print(f"  Trend: {trend:+.6f} mm/Messung")
            print(
                f"  Richtung: {'Verschlechterung' if trend > 0 else 'Verbesserung' if trend < 0 else 'Stabil'}"
            )

        # Periodische Analyse
        if len(messungen) >= 20:
            # Suche nach periodischen Mustern
            fft = np.fft.fft(messungen - np.mean(messungen))
            frequencies = np.fft.fftfreq(len(messungen))
            dominant_freq_idx = np.argmax(np.abs(fft[1 : len(fft) // 2])) + 1

            if dominant_freq_idx > 0:
                periode = 1 / abs(frequencies[dominant_freq_idx])
                print(f"  Dominante Periode: alle {periode:.1f} Messungen")

    def _calculate_process_capability(
        self, gute_messungen: np.ndarray
    ) -> tuple[float, float]:
        """Berechne Prozessfähigkeitskennzahlen Cp und Cpk"""
        if len(gute_messungen) == 0:
            return 0.0, 0.0

        sigma = np.std(gute_messungen, ddof=1)  # Stichproben-Standardabweichung
        mittelwert = np.mean(gute_messungen)

        # Spezifikationsgrenzen
        usl = self.sollwert_praezision + self.toleranz_standard  # Upper Spec Limit
        lsl = self.sollwert_praezision - self.toleranz_standard  # Lower Spec Limit

        # Cp = Prozessfähigkeit (Streuung)
        cp = (usl - lsl) / (6 * sigma) if sigma > 0 else float("inf")

        # Cpk = Prozesslage (Zentrierung)
        cpu = (usl - mittelwert) / (3 * sigma) if sigma > 0 else float("inf")
        cpl = (mittelwert - lsl) / (3 * sigma) if sigma > 0 else float("inf")
        cpk = min(cpu, cpl)

        return cp, cpk

    def _evaluate_process_capability(self, cp: float, cpk: float) -> str:
        """Bewerte Prozessfähigkeit basierend auf Cp und Cpk"""
        if cpk >= 1.67:
            return "Exzellent (Weltklasse)"
        elif cpk >= 1.33:
            return "Sehr gut"
        elif cpk >= 1.0:
            return "Ausreichend"
        elif cpk >= 0.67:
            return "Grenzwertig"
        else:
            return "Unzureichend (Verbesserung nötig)"

    def _demonstrate_advanced_array_ops(self, daten: np.ndarray) -> None:
        """Demonstriere erweiterte Array-Operationen"""
        print("\n🚀 Erweiterte Array-Operationen:")

        # Broadcast-Operationen
        tagesmittel = np.mean(daten, axis=(1, 2), keepdims=True)  # Shape: (5, 1, 1)
        relative_performance = daten / tagesmittel  # Broadcasting

        print("Relative Performance (Faktor zum Tagesmittel):")
        print(f"  Durchschnittlich: {np.mean(relative_performance):.3f}")
        print(f"  Beste Stunde: {np.max(relative_performance):.3f}x")
        print(f"  Schlechteste Stunde: {np.min(relative_performance):.3f}x")

        # Einsum für komplexe Operationen
        # Summiere über Schichten für jeden Tag und jede Stunde: (5,3,8) -> (5,8)
        tag_stunden_summe = np.einsum("ijk->ik", daten)
        print(f"Einsum Summierung über Schichten: {tag_stunden_summe.shape}")

        # Kreuzkorrelation zwischen Tagen
        korrelation_matrix = np.corrcoef(tag_stunden_summe)
        print(f"Tages-Korrelationsmatrix Shape: {korrelation_matrix.shape}")

    def _demonstrate_memory_optimization(self) -> None:
        """Demonstriere Memory-Optimierungstechniken"""
        print("Memory-Optimierung:")

        # In-place Operationen
        test_array = np.random.randint(0, 100, (1000, 1000))
        original_id = id(test_array)

        # In-place Addition
        test_array += 10
        print(f"  In-place Operation behält ID: {id(test_array) == original_id}")

        # Views vs Copies
        view = test_array[::2, ::2]  # Every second element - creates view
        copy = test_array[
            np.random.choice(1000, 500), :
        ]  # Fancy indexing - creates copy

        print(f"  View teilt Speicher: {np.shares_memory(test_array, view)}")
        print(f"  Copy teilt Speicher: {np.shares_memory(test_array, copy)}")

        # Memory-Layout Optimierung
        c_array = np.ascontiguousarray(test_array)  # C-contiguous
        f_array = np.asfortranarray(test_array)  # Fortran-contiguous

        print(f"  C-contiguous: {c_array.flags['C_CONTIGUOUS']}")
        print(f"  F-contiguous: {f_array.flags['F_CONTIGUOUS']}")

    def zusammenfassung_und_best_practices(self) -> None:
        """Zusammenfassung aller Techniken und Best Practices"""
        print("\n" + "=" * 70)
        print("🟢 ZUSAMMENFASSUNG: Array-Manipulation Mastery")
        print("=" * 70)

        print("🔧 FUNDAMENTALE TECHNIKEN:")
        print("✅ reshape() - Dimensionen ändern ohne Datenveränderung")
        print("✅ transpose() / .T - Achsen vertauschen für verschiedene Sichtweisen")
        print("✅ concatenate() / hstack() / vstack() - Arrays intelligent kombinieren")
        print("✅ Boolean Indexing - Präzise Datenfilterung nach Bedingungen")
        print("✅ split() / array_split() - Daten systematisch aufteilen")
        print("✅ axis-Parameter - Operationen entlang spezifischer Dimensionen")
        print()

        print("🚀 ERWEITERTE TECHNIKEN:")
        print("✅ Multi-dimensionale Statistiken mit axis-Tupeln")
        print("✅ np.unravel_index() für Position-Mapping in flachen Arrays")
        print("✅ Broadcasting für effiziente Element-wise Operationen")
        print("✅ einsum() für komplexe Tensor-Operationen")
        print("✅ Memory-optimierte In-place Operationen")
        print("✅ View vs. Copy Bewusstsein für Performance")
        print()

        print("🏭 INDUSTRIELLE ANWENDUNGEN:")
        print("• Qualitätskontrolle mit statistischen Schwellwerten")
        print("• Multi-dimensionale Produktionsanalyse")
        print("• Trend-Erkennung und Prozessfähigkeits-Bewertung")
        print("• Schicht- und Zeitraum-basierte Auswertungen")
        print("• Performance-Optimierung für große Datensätze")
        print()

        print("💡 PRAKTISCHE TIPPS:")
        print("• Immer Array-Shapes vor Operationen überprüfen")
        print("• Mit kleinen Testdaten Operationen validieren")
        print("• Axis-Parameter bewusst einsetzen für gewünschte Dimensionen")
        print("• Boolean Masks für komplexe, lesbare Filterlogik")
        print("• Memory-effiziente Views bevorzugen wenn möglich")
        print("• Aussagekräftige Variablennamen für Verständlichkeit")
        print("• Type Hints für bessere Code-Dokumentation")
        print()

        print("📊 QUALITÄTSKONTROLLE BEST PRACTICES:")
        print("• Multiple Schwellwerte für granulare Kategorisierung")
        print("• Statistische Methoden (3σ-Regel, Perzentile)")
        print("• Trend-Analyse für Prozessüberwachung")
        print("• Cp/Cpk Kennzahlen für Prozessfähigkeits-Bewertung")
        print("• Sequenzielle Problemerkennung")

    def vollstaendige_demonstration(self) -> None:
        """
        Führe alle Aufgaben in der richtigen Reihenfolge aus
        """
        print("🔧 NumPy Array-Manipulation - Vollständige Musterlösung")
        print("=" * 70)
        print("SmartFactory Python Grundkurs - Industrielle Array-Verarbeitung")
        print("=" * 70)

        try:
            # Alle Aufgaben systematisch durchführen
            tage_stunden, transponiert = self.aufgabe_1_reshape_und_transpose()
            beide_schichten, alle_maschinen = self.aufgabe_2_arrays_kombinieren()
            messungen, ausreisser, gute_messungen, qualitaets_analyse = (
                self.aufgabe_3_boolean_indexing()
            )
            (
                produktion_woche,
                pro_tag,
                pro_schicht,
                pro_stunde,
                produktions_statistik,
            ) = self.aufgabe_4_erweiterte_manipulation()

            # Bonus-Material
            self.bonus_advanced_manipulations()

            # Zusammenfassung und Best Practices
            self.zusammenfassung_und_best_practices()

            # Finale Übersicht
            self._print_final_summary(qualitaets_analyse, produktions_statistik)

        except Exception as e:
            print(f"❌ Fehler bei der Ausführung: {e}")
            if self.debug_mode:
                import traceback

                traceback.print_exc()
            raise

    def _print_final_summary(
        self,
        qualitaets_analyse: QualitätsAnalyse,
        produktions_statistik: ProduktionsStatistik,
    ) -> None:
        """Drucke finale Zusammenfassung aller Analysen"""
        print("\n" + "=" * 70)
        print("📊 FINALE ZUSAMMENFASSUNG - SmartFactory Array-Manipulation")
        print("=" * 70)

        print("🎯 Qualitätskontrolle:")
        print(f"   Gesamtmessungen: {qualitaets_analyse.gesamt_anzahl}")
        print(f"   Ausreißer-Rate: {qualitaets_analyse.ausreisser_rate:.2%}")
        print(
            f"   Qualitätsverbesserung: {(qualitaets_analyse.mittelwert_gute - qualitaets_analyse.mittelwert_gesamt) * 1000:.2f}μm"
        )

        print("\n🏭 Produktionsanalyse:")
        print(
            f"   Wochenproduktion: {produktions_statistik.mittelwert * 5 * 3 * 8:.0f} Teile"
        )
        print(
            f"   Performance-Spanne: {produktions_statistik.minimum}-{produktions_statistik.maximum} Teile/h"
        )
        print(
            f"   Variabilität: {produktions_statistik.standardabweichung:.1f} Teile/h"
        )

        print("\n🚀 Technische Errungenschaften:")
        print("   ✅ Mehrdimensionale Array-Manipulation beherrscht")
        print("   ✅ Boolean Indexing für Qualitätskontrolle implementiert")
        print("   ✅ Statistische Prozesskontrolle etabliert")
        print("   ✅ Memory-effiziente Operationen angewendet")

        print("\n💡 Diese Solution demonstriert production-ready NumPy Code")
        print("   für industrielle Datenverarbeitung bei SmartFactory.")


def main():
    """Hauptfunktion für die Ausführung der Solution"""
    solution = NumPyManipulationSolution(debug_mode=False)
    solution.vollstaendige_demonstration()


if __name__ == "__main__":
    main()


"""
📚 LEARNING SUMMARY - NumPy Array-Manipulation
==============================================

🎯 ERREICHTE LERNZIELE:
✅ Array Reshape und Transpose für verschiedene Datenansichten
✅ Array-Kombination (concatenate, hstack, vstack) für Datenintegration
✅ Boolean Indexing für präzise Qualitätskontrolle
✅ Multi-dimensionale Array-Manipulation für komplexe Analysen
✅ Performance-optimierte Operationen mit View/Copy Bewusstsein
✅ Statistische Prozesskontrolle mit Cp/Cpk-Kennzahlen
✅ Memory-effiziente Array-Verarbeitung

🏭 INDUSTRIELLE ANWENDUNGSFÄLLE:
• Kontinuierliche Produktionsdaten-Umformung für verschiedene Analysen
• Multi-Schicht-Produktionsdaten-Integration
• Qualitätsmessungen mit statistischer Ausreißer-Erkennung
• 3D/4D Produktionsanalyse (Zeit × Maschinen × Schichten)
• Prozessfähigkeits-Bewertung nach Industriestandards
• Trend-Analyse für proaktive Qualitätskontrolle

🚀 PERFORMANCE-OPTIMIERUNGEN:
• Memory-effiziente In-place Operationen
• View vs. Copy strategisch einsetzen
• Broadcasting für Batch-Operationen
• Einsum für komplexe Tensor-Berechnungen
• Axis-Parameter für dimensionsweise Verarbeitung

🔧 TECHNISCHE HIGHLIGHTS:
• Type Hints für production-ready Code
• Dataclasses für strukturierte Ergebnisse
• Comprehensive Error Handling
• Performance Benchmarking
• Statistical Process Control Implementation
• Memory Layout Optimization

📈 ERWEITERTE KONZEPTE:
• Multi-dimensionale statistische Analyse
• Rolling Window Operationen für Trend-Erkennung
• Korrelationsanalyse zwischen Produktionslinien
• Prozessfähigkeits-Metriken (Cp, Cpk)
• Strukturierte Arrays für komplexe Datentypen

💡 NÄCHSTE SCHRITTE:
1. Integration mit Pandas für strukturierte Datenanalyse
2. Visualization mit Matplotlib für Produktions-Dashboards
3. Real-time Processing für Live-Qualitätskontrolle
4. Machine Learning Integration für Predictive Quality
5. Parallelisierung für große Produktionsdatensätze

🎓 Diese Solution demonstriert professionelle NumPy Array-Manipulation
   für anspruchsvolle industrielle Datenverarbeitung bei SmartFactory.
"""
