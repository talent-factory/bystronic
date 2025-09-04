#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Übung 3: Datenanalyse mit NumPy

Diese Übung behandelt statistische Datenanalyse:
- Deskriptive Statistik und Verteilungen
- Korrelationsanalyse
- Zeitreihenanalyse
- Qualitätskontrolle (SPC)
- Trend- und Musteranalyse
"""

import numpy as np


def uebung_3_1() -> None:
    """Übung 3.1: Deskriptive Statistik"""
    print("=" * 60)
    print("ÜBUNG 3.1: Deskriptive Statistik")
    print("=" * 60)

    # Simuliere Produktionszeiten von 50 Aufträgen (in Stunden)
    np.random.seed(123)
    produktionszeiten = np.random.normal(8.5, 1.2, 50)  # Mittel=8.5h, StdAbw=1.2h

    print("Produktionszeiten (erste 10):")
    print(f"{produktionszeiten[:10]}")
    print(f"Gesamt: {len(produktionszeiten)} Aufträge")

    # TODO: Führen Sie eine vollständige deskriptive Analyse durch

    # a) Lagemaße
    mittelwert = np.mean(produktionszeiten)
    median = np.median(produktionszeiten)
    modus_index = np.argmax(np.bincount(produktionszeiten.astype(int)))

    print("\na) Lagemaße:")
    print(f"   Mittelwert: {mittelwert:.3f} Stunden")
    print(f"   Median: {median:.3f} Stunden")
    print(f"   Häufigster Ganzzahlwert: {modus_index} Stunden")

    # b) Streuungsmaße
    varianz = np.var(produktionszeiten, ddof=1)
    standardabweichung = np.std(produktionszeiten, ddof=1)
    spannweite = np.max(produktionszeiten) - np.min(produktionszeiten)

    q25 = np.percentile(produktionszeiten, 25)
    q75 = np.percentile(produktionszeiten, 75)
    iqr = q75 - q25

    print("\nb) Streuungsmaße:")
    print(f"   Varianz: {varianz:.3f}")
    print(f"   Standardabweichung: {standardabweichung:.3f} Stunden")
    print(f"   Spannweite: {spannweite:.3f} Stunden")
    print(f"   IQR: {iqr:.3f} Stunden")

    # c) Form der Verteilung (Schiefe und Kurtosis)
    # Schiefe (Skewness) - vereinfachte Berechnung
    schiefe = np.mean(((produktionszeiten - mittelwert) / standardabweichung) ** 3)

    # Kurtosis - vereinfachte Berechnung
    kurtosis = np.mean(((produktionszeiten - mittelwert) / standardabweichung) ** 4)

    print("\nc) Form der Verteilung:")
    print(
        f"   Schiefe: {schiefe:.3f} ({'Rechtsschief' if schiefe > 0.5 else 'Linksschief' if schiefe < -0.5 else 'Symmetrisch'})"
    )
    print(
        f"   Kurtosis: {kurtosis:.3f} ({'Spitz' if kurtosis > 3.5 else 'Flach' if kurtosis < 2.5 else 'Normal'})"
    )

    # d) Ausreißer identifizieren (Z-Score Methode)
    z_scores = np.abs((produktionszeiten - mittelwert) / standardabweichung)
    ausreisser_indices = z_scores > 2.5  # |z| > 2.5 als Grenzwert

    print("\nd) Ausreißer-Analyse:")
    print(f"   Anzahl Ausreißer (|z| > 2.5): {np.sum(ausreisser_indices)}")
    if np.sum(ausreisser_indices) > 0:
        print(f"   Ausreißer-Werte: {produktionszeiten[ausreisser_indices]}")

    # e) Konfidenzintervall für den Mittelwert (95%)
    n = len(produktionszeiten)
    standardfehler = standardabweichung / np.sqrt(n)
    # Für große Stichproben: ~1.96 für 95% Konfidenz
    konfidenz_95 = 1.96 * standardfehler

    print("\ne) 95% Konfidenzintervall für Mittelwert:")
    print(
        f"   {mittelwert - konfidenz_95:.3f} bis {mittelwert + konfidenz_95:.3f} Stunden"
    )


def uebung_3_2() -> None:
    """Übung 3.2: Korrelationsanalyse"""
    print("\n" + "=" * 60)
    print("ÜBUNG 3.2: Korrelationsanalyse")
    print("=" * 60)

    # Simuliere Maschinendaten: Temperatur, Druck, Geschwindigkeit, Qualität
    np.random.seed(456)
    n_messungen = 30

    temperatur = np.random.normal(75, 8, n_messungen)
    # Druck korreliert positiv mit Temperatur
    druck = 2.5 + 0.4 * temperatur + np.random.normal(0, 3, n_messungen)
    # Geschwindigkeit korreliert negativ mit Temperatur
    geschwindigkeit = 120 - 0.8 * temperatur + np.random.normal(0, 5, n_messungen)
    # Qualität hängt von Temperatur und Druck ab
    qualitaet = (
        85 + 0.2 * temperatur + 0.3 * druck + np.random.normal(0, 2, n_messungen)
    )

    print("Maschinendaten generiert:")
    print(f"Temperatur (°C): {temperatur[:5]}... (erste 5 von {n_messungen})")
    print(f"Druck (bar): {druck[:5]}...")
    print(f"Geschwindigkeit (m/min): {geschwindigkeit[:5]}...")
    print(f"Qualität (%): {qualitaet[:5]}...")

    # TODO: Korrelationsanalyse durchführen

    # a) Korrelationsmatrix berechnen
    daten_matrix = np.column_stack([temperatur, druck, geschwindigkeit, qualitaet])
    korrelation_matrix = np.corrcoef(daten_matrix.T)

    variablen = ["Temperatur", "Druck", "Geschwindigkeit", "Qualität"]
    print("\na) Korrelationsmatrix:")
    print("           ", end="")
    for var in variablen:
        print(f"{var:>12}", end="")
    print()

    for i, var in enumerate(variablen):
        print(f"{var:>11}", end="")
        for j in range(len(variablen)):
            print(f"{korrelation_matrix[i, j]:>12.3f}", end="")
        print()

    # b) Starke Korrelationen identifizieren
    print("\nb) Starke Korrelationen (|r| > 0.7):")
    for i in range(len(variablen)):
        for j in range(i + 1, len(variablen)):
            r = korrelation_matrix[i, j]
            if abs(r) > 0.7:
                typ = "positive" if r > 0 else "negative"
                print(f"   {variablen[i]} ↔ {variablen[j]}: r = {r:.3f} ({typ})")

    # c) Einzelne Korrelationen analysieren
    r_temp_qualitaet = np.corrcoef(temperatur, qualitaet)[0, 1]
    r_druck_geschwindigkeit = np.corrcoef(druck, geschwindigkeit)[0, 1]

    print("\nc) Einzelne Korrelationen:")
    print(f"   Temperatur ↔ Qualität: r = {r_temp_qualitaet:.3f}")
    print(f"   Druck ↔ Geschwindigkeit: r = {r_druck_geschwindigkeit:.3f}")

    # d) Bestimmheitsmaß (R²)
    r_squared_temp_qualitaet = r_temp_qualitaet**2
    print("\nd) Bestimmheitsmaß (R²):")
    print(
        f"   Temperatur erklärt {r_squared_temp_qualitaet * 100:.1f}% der Qualitäts-Varianz"
    )

    # e) Rangkorrelation (Spearman) - vereinfacht
    def spearman_korr(x: np.ndarray, y: np.ndarray) -> float:
        rank_x = np.argsort(np.argsort(x))
        rank_y = np.argsort(np.argsort(y))
        return float(np.corrcoef(rank_x, rank_y)[0, 1])

    spearman_temp_qual = spearman_korr(temperatur, qualitaet)
    print("\ne) Spearman-Rangkorrelation:")
    print(f"   Temperatur ↔ Qualität: rs = {spearman_temp_qual:.3f}")


def uebung_3_3() -> None:
    """Übung 3.3: Zeitreihenanalyse"""
    print("\n" + "=" * 60)
    print("ÜBUNG 3.3: Zeitreihenanalyse")
    print("=" * 60)

    # Simuliere tägliche Produktionsdaten über 3 Monate
    np.random.seed(789)
    tage = 90

    # Trend + Saisonalität + Rauschen
    t = np.arange(tage)
    trend = 1000 + 2 * t  # Steigender Trend
    saison = 100 * np.sin(2 * np.pi * t / 7)  # Wöchentliche Schwankung
    rauschen = np.random.normal(0, 30, tage)
    produktion = trend + saison + rauschen

    print(f"Produktionsdaten über {tage} Tage generiert")
    print(f"Erste 10 Tage: {produktion[:10].astype(int)}")
    print(f"Letzte 10 Tage: {produktion[-10:].astype(int)}")

    # TODO: Zeitreihenanalyse durchführen

    # a) Gleitende Durchschnitte berechnen
    def gleitender_durchschnitt(daten: np.ndarray, fenster: int) -> np.ndarray:
        return np.convolve(daten, np.ones(fenster) / fenster, mode="valid")

    ma_7 = gleitender_durchschnitt(produktion, 7)  # 7-Tage-Durchschnitt
    ma_14 = gleitender_durchschnitt(produktion, 14)  # 14-Tage-Durchschnitt

    print("\na) Gleitende Durchschnitte:")
    print(f"   7-Tage MA (Tag 7-12): {ma_7[:6].astype(int)}")
    print(f"   14-Tage MA (Tag 14-19): {ma_14[:6].astype(int)}")

    # b) Trend berechnen (lineare Regression)
    # y = a * x + b
    A = np.column_stack([t, np.ones(len(t))])
    koeffizienten = np.linalg.lstsq(A, produktion, rcond=None)[0]
    trend_linie = koeffizienten[0] * t + koeffizienten[1]

    print("\nb) Trendanalyse:")
    print(f"   Steigung: {koeffizienten[0]:.2f} Stück/Tag")
    print(f"   Y-Achsenabschnitt: {koeffizienten[1]:.1f} Stück")
    print(f"   Prognose Tag 100: {koeffizienten[0] * 100 + koeffizienten[1]:.0f} Stück")

    # c) Saisonalität extrahieren (detrended data)
    detrended = produktion - trend_linie

    # Wochenmuster berechnen
    wochentag_mittel = np.zeros(7)
    for wt in range(7):
        wochentag_indices = np.arange(wt, len(detrended), 7)
        if len(wochentag_indices) > 0:
            wochentag_mittel[wt] = np.mean(detrended[wochentag_indices])

    wochentage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    print("\nc) Saisonales Muster (Wochentage):")
    for i, tag in enumerate(wochentage):
        print(f"   {tag}: {wochentag_mittel[i]:+6.1f} Stück")

    # d) Volatilität berechnen (rollende Standardabweichung)
    def rollende_std(daten: np.ndarray, fenster: int) -> np.ndarray:
        volatilitaet = np.zeros(len(daten) - fenster + 1)
        for i in range(len(volatilitaet)):
            volatilitaet[i] = np.std(daten[i : i + fenster])
        return volatilitaet

    volatilitaet_14 = rollende_std(produktion, 14)

    print("\nd) Volatilität (14-Tage rollende Std.abw.):")
    print(f"   Durchschnitt: {np.mean(volatilitaet_14):.1f} Stück")
    print(f"   Maximum: {np.max(volatilitaet_14):.1f} Stück")
    print(f"   Minimum: {np.min(volatilitaet_14):.1f} Stück")

    # e) Ausreißer in der Zeitreihe
    z_scores = np.abs((produktion - np.mean(produktion)) / np.std(produktion))
    ausreisser_tage = np.where(z_scores > 2.5)[0]

    print("\ne) Ausreißer-Tage (|z| > 2.5):")
    print(f"   Anzahl: {len(ausreisser_tage)}")
    if len(ausreisser_tage) > 0:
        for tag in ausreisser_tage[:5]:  # Erste 5 zeigen
            print(
                f"   Tag {tag + 1}: {produktion[tag]:.0f} Stück (z={z_scores[tag]:.2f})"
            )


def uebung_3_4() -> None:
    """Übung 3.4: Statistische Prozesskontrolle (SPC)"""
    print("\n" + "=" * 60)
    print("ÜBUNG 3.4: Statistische Prozesskontrolle (SPC)")
    print("=" * 60)

    # Simuliere Qualitätsmessdaten (Durchmesser in mm)
    np.random.seed(101112)
    sollwert = 25.0  # mm

    # Normale Prozessvariation für erste 40 Messungen
    normale_messungen = np.random.normal(sollwert, 0.15, 40)

    # Prozessverschiebung ab Messung 41
    verschobene_messungen = np.random.normal(sollwert + 0.3, 0.15, 20)

    # Erhöhte Variation ab Messung 61
    variable_messungen = np.random.normal(sollwert, 0.4, 15)

    alle_messungen = np.concatenate(
        [normale_messungen, verschobene_messungen, variable_messungen]
    )

    print(f"Qualitätsmessdaten: {len(alle_messungen)} Messungen")
    print(f"Sollwert: {sollwert} mm")
    print(f"Erste 10 Messungen: {normale_messungen[:10]}")

    # TODO: SPC-Analyse durchführen

    # a) Kontrollgrenzen berechnen (basierend auf ersten 20 Messungen)
    referenz_daten = alle_messungen[:20]
    prozess_mittel = np.mean(referenz_daten)
    prozess_std = np.std(referenz_daten, ddof=1)

    # 3-Sigma Grenzen
    ucl = prozess_mittel + 3 * prozess_std  # Upper Control Limit
    lcl = prozess_mittel - 3 * prozess_std  # Lower Control Limit
    uwl = prozess_mittel + 2 * prozess_std  # Upper Warning Limit
    lwl = prozess_mittel - 2 * prozess_std  # Lower Warning Limit

    print("\na) Kontrollgrenzen (basierend auf ersten 20 Messungen):")
    print(f"   Prozessmittel: {prozess_mittel:.4f} mm")
    print(f"   UCL (+3σ): {ucl:.4f} mm")
    print(f"   UWL (+2σ): {uwl:.4f} mm")
    print(f"   LWL (-2σ): {lwl:.4f} mm")
    print(f"   LCL (-3σ): {lcl:.4f} mm")

    # b) Regelkarten-Verletzungen identifizieren
    ueber_ucl = alle_messungen > ucl
    unter_lcl = alle_messungen < lcl
    ueber_uwl = alle_messungen > uwl
    unter_lwl = alle_messungen < lwl

    print("\nb) Regelkarten-Verletzungen:")
    print(f"   Über UCL: {np.sum(ueber_ucl)} Messungen")
    print(f"   Unter LCL: {np.sum(unter_lcl)} Messungen")
    print(
        f"   Warnbereich: {np.sum(ueber_uwl | unter_lwl) - np.sum(ueber_ucl | unter_lcl)} Messungen"
    )

    if np.sum(ueber_ucl) > 0:
        verletzungen = np.where(ueber_ucl)[0]
        print(f"   UCL-Verletzungen bei Messung: {verletzungen + 1}")

    # c) Prozessfähigkeit berechnen
    toleranz_ober = sollwert + 0.5  # ±0.5mm Toleranz
    toleranz_unter = sollwert - 0.5

    cp = (toleranz_ober - toleranz_unter) / (6 * prozess_std)
    cpk_ober = (toleranz_ober - prozess_mittel) / (3 * prozess_std)
    cpk_unter = (prozess_mittel - toleranz_unter) / (3 * prozess_std)
    cpk = min(cpk_ober, cpk_unter)

    print("\nc) Prozessfähigkeit:")
    print(f"   Cp: {cp:.3f}")
    print(f"   Cpk: {cpk:.3f}")
    print(
        f"   Bewertung: {'Sehr gut' if cpk > 1.67 else 'Gut' if cpk > 1.33 else 'Akzeptabel' if cpk > 1.0 else 'Ungenügend'}"
    )

    # d) Trends erkennen (7 aufeinanderfolgende Punkte auf einer Seite)
    def trend_erkennung(
        daten: np.ndarray, referenz: float, mindest_laenge: int = 7
    ) -> list[tuple[int, int, str]]:
        trends: list[tuple[int, int, str]] = []
        aktuelle_serie = 0
        letzte_seite: str | None = None

        for i, wert in enumerate(daten):
            seite = "oben" if wert > referenz else "unten"

            if seite == letzte_seite:
                aktuelle_serie += 1
            else:
                if aktuelle_serie >= mindest_laenge and letzte_seite is not None:
                    trends.append((i - aktuelle_serie, i - 1, letzte_seite))
                aktuelle_serie = 1
                letzte_seite = seite

        # Letzten Trend prüfen
        if aktuelle_serie >= mindest_laenge and letzte_seite is not None:
            trends.append((len(daten) - aktuelle_serie, len(daten) - 1, letzte_seite))

        return trends

    trends = trend_erkennung(alle_messungen, prozess_mittel)

    print("\nd) Trend-Erkennung (≥7 aufeinanderfolgende Punkte):")
    if trends:
        for start, end, seite in trends:
            print(f"   Messungen {start + 1}-{end + 1}: Trend nach {seite}")
    else:
        print("   Keine signifikanten Trends erkannt")

    # e) Laufende Statistiken
    laufender_mittel = np.zeros(len(alle_messungen))
    laufende_std = np.zeros(len(alle_messungen))

    for i in range(1, len(alle_messungen) + 1):
        laufender_mittel[i - 1] = np.mean(alle_messungen[:i])
        if i > 1:
            laufende_std[i - 1] = np.std(alle_messungen[:i], ddof=1)

    print("\ne) Laufende Statistiken:")
    print(f"   Messung 20: μ={laufender_mittel[19]:.4f}, σ={laufende_std[19]:.4f}")
    print(f"   Messung 40: μ={laufender_mittel[39]:.4f}, σ={laufende_std[39]:.4f}")
    print(f"   Messung 60: μ={laufender_mittel[59]:.4f}, σ={laufende_std[59]:.4f}")
    print(f"   Final: μ={laufender_mittel[-1]:.4f}, σ={laufende_std[-1]:.4f}")


def uebung_3_5() -> None:
    """Übung 3.5: Multivariate Datenanalyse"""
    print("\n" + "=" * 60)
    print("ÜBUNG 3.5: Multivariate Datenanalyse")
    print("=" * 60)

    # Simuliere Maschinendaten mit mehreren Variablen
    np.random.seed(131415)
    n_maschinen = 25

    # Korrelierte Maschinendaten generieren
    # Basis-Zufallsvariablen
    z1 = np.random.normal(0, 1, n_maschinen)
    z2 = np.random.normal(0, 1, n_maschinen)
    z3 = np.random.normal(0, 1, n_maschinen)

    # Korrelierte Variablen erstellen
    alter = 5 + 15 * np.abs(z1)  # 5-20 Jahre
    wartungskosten = 1000 + 200 * alter + 300 * z2  # Korreliert mit Alter
    effizienz = 95 - 2 * alter + 5 * z3  # Negativ korreliert mit Alter
    ausfallzeit = 10 + 0.5 * alter + 2 * np.abs(z2)  # Korreliert mit Alter und Kosten

    # In Matrix zusammenfassen
    maschinendaten = np.column_stack([alter, wartungskosten, effizienz, ausfallzeit])
    variablen_namen = ["Alter", "Wartungskosten", "Effizienz", "Ausfallzeit"]

    print(f"Maschinendaten: {n_maschinen} Maschinen, {len(variablen_namen)} Variablen")
    print("\nErste 5 Maschinen:")
    print(f"{'ID':<3} {'Alter':<6} {'Kosten':<8} {'Effizienz':<9} {'Ausfallzeit'}")
    print("-" * 40)
    for i in range(5):
        print(
            f"{i + 1:<3} {maschinendaten[i, 0]:6.1f} {maschinendaten[i, 1]:8.0f} "
            f"{maschinendaten[i, 2]:9.1f} {maschinendaten[i, 3]:6.1f}"
        )

    # TODO: Multivariate Analyse durchführen

    # a) Deskriptive Statistiken für alle Variablen
    print("\na) Deskriptive Statistiken:")
    print(f"{'Variable':<15} {'Mittel':<8} {'Std.Abw.':<8} {'Min':<8} {'Max'}")
    print("-" * 55)

    for i, name in enumerate(variablen_namen):
        mittel = np.mean(maschinendaten[:, i])
        std = np.std(maschinendaten[:, i], ddof=1)
        minimum = np.min(maschinendaten[:, i])
        maximum = np.max(maschinendaten[:, i])
        print(f"{name:<15} {mittel:<8.2f} {std:<8.2f} {minimum:<8.2f} {maximum:<8.2f}")

    # b) Vollständige Korrelationsmatrix
    korr_matrix = np.corrcoef(maschinendaten.T)

    print("\nb) Korrelationsmatrix:")
    print(f"{'Variable':<15}", end="")
    for name in variablen_namen:
        print(f"{name[:8]:<10}", end="")
    print()
    print("-" * 65)

    for i, name in enumerate(variablen_namen):
        print(f"{name:<15}", end="")
        for j in range(len(variablen_namen)):
            print(f"{korr_matrix[i, j]:10.3f}", end="")
        print()

    # c) Mahalanobis-Distanz für Ausreißer-Erkennung
    def mahalanobis_distanz(daten: np.ndarray) -> np.ndarray:
        mittelwerte = np.mean(daten, axis=0)
        kovarianz = np.cov(daten.T)
        inv_kovarianz = np.linalg.inv(kovarianz)

        distanzen = np.zeros(len(daten))
        for i, punkt in enumerate(daten):
            diff = punkt - mittelwerte
            distanzen[i] = np.sqrt(diff @ inv_kovarianz @ diff)

        return distanzen

    maha_dist = mahalanobis_distanz(maschinendaten)

    # Grenzwert für Ausreißer (Chi-Quadrat-Verteilung, 4 Variablen, α=0.01)
    grenzwert = 3.5  # Approximation
    ausreisser_mask = maha_dist > grenzwert

    print("\nc) Ausreißer-Erkennung (Mahalanobis-Distanz):")
    print(f"   Grenzwert: {grenzwert:.2f}")
    print(f"   Anzahl Ausreißer: {np.sum(ausreisser_mask)}")

    if np.sum(ausreisser_mask) > 0:
        ausreisser_indices = np.where(ausreisser_mask)[0]
        print("   Ausreißer-Maschinen:")
        for idx in ausreisser_indices[:3]:  # Erste 3 zeigen
            print(f"   Maschine {idx + 1}: Distanz={maha_dist[idx]:.2f}")

    # d) Hauptkomponentenanalyse (vereinfacht)
    # Daten standardisieren
    standardisiert = (maschinendaten - np.mean(maschinendaten, axis=0)) / np.std(
        maschinendaten, axis=0, ddof=1
    )

    # Kovarianzmatrix der standardisierten Daten
    kovarianz_std = np.cov(standardisiert.T)

    # Eigenwerte und Eigenvektoren
    eigenwerte, eigenvektoren = np.linalg.eig(kovarianz_std)

    # Nach Eigenwerten sortieren (absteigend)
    sort_indices = np.argsort(eigenwerte)[::-1]
    eigenwerte = eigenwerte[sort_indices]
    eigenvektoren = eigenvektoren[:, sort_indices]

    # Erklärte Varianz
    erklaerte_varianz = eigenwerte / np.sum(eigenwerte) * 100
    kumulativ_varianz = np.cumsum(erklaerte_varianz)

    print("\nd) Hauptkomponentenanalyse:")
    print(f"{'PC':<3} {'Eigenwert':<10} {'Var. %':<8} {'Kumulativ %'}")
    print("-" * 35)
    for i in range(len(eigenwerte)):
        print(
            f"{i + 1:<3} {eigenwerte[i]:<10.3f} {erklaerte_varianz[i]:<8.1f} {kumulativ_varianz[i]:<8.1f}"
        )

    # Erste Hauptkomponente interpretieren
    print("\nErste Hauptkomponente (Ladungen):")
    for i, name in enumerate(variablen_namen):
        print(f"   {name}: {eigenvektoren[i, 0]:.3f}")

    # e) Clustering-Vorbereitung (K-Means vereinfacht)
    def einfaches_k_means(
        daten: np.ndarray, k: int = 3, max_iter: int = 10
    ) -> tuple[np.ndarray, np.ndarray]:
        # Zufällige Initialisierung der Zentren
        np.random.seed(42)
        zentren = daten[np.random.choice(len(daten), k, replace=False)]

        for _ in range(max_iter):
            # Distanzen zu allen Zentren berechnen
            distanzen = np.zeros((len(daten), k))
            for i, zentrum in enumerate(zentren):
                distanzen[:, i] = np.sqrt(np.sum((daten - zentrum) ** 2, axis=1))

            # Zugehörigkeiten bestimmen
            zugehoerigkeiten = np.argmin(distanzen, axis=1)

            # Neue Zentren berechnen
            neue_zentren = np.zeros_like(zentren)
            for i in range(k):
                if np.sum(zugehoerigkeiten == i) > 0:
                    neue_zentren[i] = np.mean(daten[zugehoerigkeiten == i], axis=0)
                else:
                    neue_zentren[i] = zentren[i]

            # Konvergenz prüfen
            if np.allclose(zentren, neue_zentren, rtol=0.01):
                break

            zentren = neue_zentren

        return zugehoerigkeiten, zentren

    cluster_labels, cluster_zentren = einfaches_k_means(standardisiert, k=3)

    print("\ne) Clustering (K-Means, k=3):")
    for i in range(3):
        anzahl_im_cluster = np.sum(cluster_labels == i)
        print(f"   Cluster {i + 1}: {anzahl_im_cluster} Maschinen")

    # Cluster-Charakteristika
    print("\nCluster-Zentren (standardisiert):")
    print(f"{'Variable':<15}", end="")
    for i in range(3):
        print(f"Cluster {i + 1:<2}", end="")
    print()
    print("-" * 45)

    for i, name in enumerate(variablen_namen):
        print(f"{name:<15}", end="")
        for j in range(3):
            print(f"{cluster_zentren[j, i]:>10.2f}", end="")
        print()


def hauptprogramm() -> None:
    """Hauptprogramm - alle Übungen ausführen"""
    print("📊 NUMPY DATENANALYSE - ÜBUNGEN")

    try:
        uebung_3_1()
        uebung_3_2()
        uebung_3_3()
        uebung_3_4()
        uebung_3_5()

        print("\n" + "=" * 60)
        print("✅ ALLE ÜBUNGEN ERFOLGREICH ABGESCHLOSSEN!")
        print("=" * 60)
        print("\n📝 Was Sie gelernt haben:")
        print("• Umfassende deskriptive Statistik")
        print("• Korrelationsanalyse und Zusammenhänge")
        print("• Zeitreihenanalyse mit Trend und Saisonalität")
        print("• Statistische Prozesskontrolle (SPC)")
        print("• Multivariate Datenanalyse und Dimensionsreduktion")

        print("\n🎯 Nächste Schritte:")
        print("• Übung 4: Lineare Algebra für technische Anwendungen")
        print("• Vertiefung: Machine Learning mit NumPy")

    except Exception as e:
        print(f"\n❌ Fehler in den Übungen: {e}")
        print("Überprüfen Sie Ihren Code und versuchen Sie es erneut.")


if __name__ == "__main__":
    hauptprogramm()
