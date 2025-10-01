#!/usr/bin/env python3
"""
🟡 INTERMEDIATE - SmartFactory Python Grundkurs - Kapitel 2
Übung 1: Erweiterte Zahlenoperationen

🎯 LERNZIELE (25-35 Minuten):
- Alle Zahlentypen beherrschen (int, float, complex, bool)
- Mathematische Module verwenden (math, statistics)
- Fehlerbehandlung bei Konvertierungen
- Funktionale Programmierung mit Zahlen
- Datenvalidierung und Qualitätskontrolle

📚 HILFSMITTEL:
- Hints: solutions/intermediate/uebung_01_hints.md
- Skeleton: solutions/intermediate/uebung_01_skeleton.py
- Partial: solutions/intermediate/uebung_01_partial.py
- Complete: solutions/intermediate/uebung_01_complete.py

🏭 BYSTRONIC-KONTEXT:
Entwickeln Sie robuste Berechnungsfunktionen für Produktionsdaten,
Qualitätskontrolle und statistische Auswertungen.
"""

import statistics


def validiere_eingabe(
    wert: str, typ: str, min_wert: float | None = None, max_wert: float | None = None
) -> int | float:
    """
    🎯 Aufgabe 1: Robuste Eingabevalidierung

    Erstellen Sie eine Funktion, die Benutzereingaben validiert und konvertiert.

    Args:
        wert: String-Eingabe des Benutzers
        typ: Gewünschter Typ ("int" oder "float")
        min_wert: Minimaler erlaubter Wert (optional)
        max_wert: Maximaler erlaubter Wert (optional)

    Returns:
        Konvertierter und validierter Wert

    Raises:
        ValueError: Bei ungültigen Eingaben
    """
    try:
        # TODO: Implementieren Sie die Konvertierung
        if typ == "int":
            konvertiert = int(wert)
        elif typ == "float":
            konvertiert = float(wert)
        else:
            raise ValueError(f"Unbekannter Typ: {typ}")

        # TODO: Implementieren Sie die Bereichsprüfung
        if min_wert is not None and konvertiert < min_wert:
            raise ValueError(f"Wert {konvertiert} ist kleiner als Minimum {min_wert}")

        if max_wert is not None and konvertiert > max_wert:
            raise ValueError(f"Wert {konvertiert} ist grösser als Maximum {max_wert}")

        return konvertiert

    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError(f"'{wert}' ist keine gültige {typ}-Zahl")
        raise


def berechne_produktionsstatistiken(teile_pro_tag: list[int]) -> dict:
    """
    🎯 Aufgabe 2: Statistische Auswertungen

    Berechnen Sie umfassende Statistiken für Produktionsdaten.

    Args:
        teile_pro_tag: Liste der täglich produzierten Teile

    Returns:
        Dictionary mit statistischen Kennwerten
    """
    if not teile_pro_tag:
        raise ValueError("Liste darf nicht leer sein")

    stats = {}

    # TODO: Grundlegende Statistiken
    stats["anzahl_tage"] = len(teile_pro_tag)
    stats["gesamt"] = sum(teile_pro_tag)
    stats["durchschnitt"] = statistics.mean(teile_pro_tag)
    stats["median"] = statistics.median(teile_pro_tag)

    # TODO: Erweiterte Statistiken
    stats["minimum"] = min(teile_pro_tag)
    stats["maximum"] = max(teile_pro_tag)
    stats["spannweite"] = stats["maximum"] - stats["minimum"]

    # TODO: Streuungsmaße
    if len(teile_pro_tag) > 1:
        stats["standardabweichung"] = statistics.stdev(teile_pro_tag)
        stats["varianz"] = statistics.variance(teile_pro_tag)
    else:
        stats["standardabweichung"] = 0.0
        stats["varianz"] = 0.0

    # TODO: Qualitätsindikatoren
    stats["variationskoeffizient"] = (
        stats["standardabweichung"] / stats["durchschnitt"]
    ) * 100

    return stats


def qualitaetskontrolle_komplex(
    messungen: list[float], sollwert: float, toleranz: float
) -> tuple[list[bool], dict]:
    """
    🎯 Aufgabe 3: Erweiterte Qualitätskontrolle

    Führen Sie eine umfassende Qualitätskontrolle durch.

    Args:
        messungen: Liste der Messwerte
        sollwert: Zielwert
        toleranz: Erlaubte Abweichung

    Returns:
        Tuple aus (Liste der OK-Flags, Qualitätsstatistiken)
    """
    if not messungen:
        raise ValueError("Messungen dürfen nicht leer sein")

    # TODO: Toleranzprüfung für jeden Messwert
    ok_flags = []
    for messung in messungen:
        abweichung = abs(messung - sollwert)
        ist_ok = abweichung <= toleranz
        ok_flags.append(ist_ok)

    # TODO: Qualitätsstatistiken berechnen
    anzahl_ok = sum(ok_flags)
    anzahl_nok = len(ok_flags) - anzahl_ok
    ausschussquote = (anzahl_nok / len(messungen)) * 100

    # TODO: Prozessfähigkeitsindizes (vereinfacht)
    mittelwert = statistics.mean(messungen)
    standardabweichung = statistics.stdev(messungen) if len(messungen) > 1 else 0

    # Cp-Wert (Prozessfähigkeit)
    cp = (
        (2 * toleranz) / (6 * standardabweichung)
        if standardabweichung > 0
        else float("inf")
    )

    # Cpk-Wert (Prozesslage)
    cpk_oben = (
        (sollwert + toleranz - mittelwert) / (3 * standardabweichung)
        if standardabweichung > 0
        else float("inf")
    )
    cpk_unten = (
        (mittelwert - (sollwert - toleranz)) / (3 * standardabweichung)
        if standardabweichung > 0
        else float("inf")
    )
    cpk = min(cpk_oben, cpk_unten)

    qualitaets_stats = {
        "anzahl_messungen": len(messungen),
        "anzahl_ok": anzahl_ok,
        "anzahl_nok": anzahl_nok,
        "ausschussquote_prozent": ausschussquote,
        "mittelwert": mittelwert,
        "standardabweichung": standardabweichung,
        "cp_wert": cp,
        "cpk_wert": cpk,
        "prozess_faehig": cp >= 1.33 and cpk >= 1.33,
    }

    return ok_flags, qualitaets_stats


def berechne_maschinenlaufzeit(
    start_zeit: float, end_zeit: float, pausen: list[tuple[float, float]]
) -> dict:
    """
    🎯 Aufgabe 4: Komplexe Zeitberechnungen

    Berechnen Sie effektive Maschinenlaufzeiten unter Berücksichtigung von Pausen.

    Args:
        start_zeit: Startzeit in Stunden (z.B. 8.0 für 08:00)
        end_zeit: Endzeit in Stunden
        pausen: Liste von (start, end) Pausenzeiten

    Returns:
        Dictionary mit Zeitstatistiken
    """
    # TODO: Grundlegende Zeitberechnung
    gesamtzeit = end_zeit - start_zeit

    # TODO: Pausenzeiten berechnen
    pausenzeit_gesamt = 0.0
    for pause_start, pause_end in pausen:
        if pause_start >= start_zeit and pause_end <= end_zeit:
            pausenzeit_gesamt += pause_end - pause_start

    # TODO: Effektive Laufzeit
    effektive_laufzeit = gesamtzeit - pausenzeit_gesamt

    # TODO: Zeitformatierung (Stunden:Minuten)
    def stunden_zu_zeit(stunden: float) -> str:
        h = int(stunden)
        m = int((stunden - h) * 60)
        return f"{h:02d}:{m:02d}"

    return {
        "start_zeit": stunden_zu_zeit(start_zeit),
        "end_zeit": stunden_zu_zeit(end_zeit),
        "gesamtzeit_stunden": gesamtzeit,
        "pausenzeit_stunden": pausenzeit_gesamt,
        "effektive_laufzeit_stunden": effektive_laufzeit,
        "effektive_laufzeit_formatiert": stunden_zu_zeit(effektive_laufzeit),
        "auslastung_prozent": (
            (effektive_laufzeit / gesamtzeit) * 100 if gesamtzeit > 0 else 0
        ),
    }


def main():
    """🚀 Hauptprogramm - Interaktive Demonstration"""
    print("🟡 INTERMEDIATE: Erweiterte Zahlenoperationen")
    print("=" * 60)
    print("🏭 Professionelle Berechnungen für SmartFactory-Produktionsdaten")
    print()

    try:
        # Aufgabe 1: Eingabevalidierung testen
        print("📝 AUFGABE 1: Eingabevalidierung")
        print("-" * 30)

        while True:
            try:
                eingabe = input("Geben Sie eine Stückzahl ein (1-10000): ")
                stueckzahl = validiere_eingabe(eingabe, "int", 1, 10000)
                print(f"✅ Gültige Stückzahl: {stueckzahl}")
                break
            except ValueError as e:
                print(f"❌ Fehler: {e}")

        # Aufgabe 2: Produktionsstatistiken
        print("\n📊 AUFGABE 2: Produktionsstatistiken")
        print("-" * 30)

        beispiel_produktion = [120, 135, 98, 142, 156, 89, 167]
        stats = berechne_produktionsstatistiken(beispiel_produktion)

        print(f"Produktionsdaten: {beispiel_produktion}")
        print(f"Durchschnitt: {stats['durchschnitt']:.1f} Teile/Tag")
        print(f"Standardabweichung: {stats['standardabweichung']:.1f}")
        print(f"Variationskoeffizient: {stats['variationskoeffizient']:.1f}%")

        # Aufgabe 3: Qualitätskontrolle
        print("\n🔍 AUFGABE 3: Qualitätskontrolle")
        print("-" * 30)

        messungen = [2.48, 2.52, 2.49, 2.51, 2.47, 2.53, 2.50]
        ok_flags, qual_stats = qualitaetskontrolle_komplex(messungen, 2.50, 0.05)

        print(f"Messungen: {messungen}")
        print(f"Ausschussquote: {qual_stats['ausschussquote_prozent']:.1f}%")
        print(f"Cp-Wert: {qual_stats['cp_wert']:.2f}")
        print(f"Prozess fähig: {'✅' if qual_stats['prozess_faehig'] else '❌'}")

        # Aufgabe 4: Maschinenlaufzeit
        print("\n⏰ AUFGABE 4: Maschinenlaufzeit")
        print("-" * 30)

        pausen = [(10.0, 10.25), (12.0, 13.0), (15.0, 15.25)]  # Pausen
        zeit_stats = berechne_maschinenlaufzeit(8.0, 17.0, pausen)

        print(f"Schicht: {zeit_stats['start_zeit']} - {zeit_stats['end_zeit']}")
        print(f"Effektive Laufzeit: {zeit_stats['effektive_laufzeit_formatiert']}")
        print(f"Auslastung: {zeit_stats['auslastung_prozent']:.1f}%")

        print("\n🎉 Alle Intermediate-Aufgaben erfolgreich abgeschlossen!")
        print("📈 Nächster Schritt: Advanced-Level oder String-Übungen")

    except Exception as e:
        print(f"\n❌ Unerwarteter Fehler: {e}")
        print("💡 Überprüfen Sie Ihre Implementierung")


if __name__ == "__main__":
    main()
