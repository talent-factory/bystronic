#!/usr/bin/env python3
"""
🤔 MICRO-ASSESSMENT: Selbstreflexions-Tool für Kapitel 01
=========================================================

ZWECK:
Strukturierte Selbsteinschätzung und Reflexion des Lernfortschritts.
Hilft Lernenden, ihre Stärken und Schwächen zu identifizieren.

FEATURES:
- Strukturierte Selbsteinschätzung
- Reflexionsfragen zu Lernprozess
- Zielsetzung für weiteres Lernen
- Fortschrittsverfolgung
- Personalisierte Empfehlungen

ZEIT: 10-15 Minuten
"""

import json
from datetime import datetime
from typing import Any


class SelbstreflexionsTool:
    """Tool für strukturierte Selbstreflexion des Lernfortschritts."""

    def __init__(self):
        self.reflexion_daten = {}
        self.kompetenzbereiche = self._definiere_kompetenzbereiche()

    def _definiere_kompetenzbereiche(self) -> dict[str, dict[str, Any]]:
        """Definiert die zu bewertenden Kompetenzbereiche."""
        return {
            "grundlagen": {
                "titel": "Python Grundlagen",
                "beschreibung": "Variablen, Datentypen, Ein-/Ausgabe",
                "fragen": [
                    "Ich kann Variablen erstellen und verwenden",
                    "Ich verstehe verschiedene Datentypen (str, int, float)",
                    "Ich kann input() und print() sicher verwenden",
                    "Ich verstehe f-strings für formatierte Ausgaben",
                ],
            },
            "datenstrukturen": {
                "titel": "Datenstrukturen",
                "beschreibung": "Listen, Dictionaries, Operationen",
                "fragen": [
                    "Ich kann Listen erstellen und manipulieren",
                    "Ich verstehe Listen-Methoden (append, sort, etc.)",
                    "Ich kann mit dem 'in' Operator arbeiten",
                    "Ich verstehe Dictionaries und deren Verwendung",
                ],
            },
            "kontrollstrukturen": {
                "titel": "Kontrollstrukturen",
                "beschreibung": "Schleifen, Bedingungen, Logik",
                "fragen": [
                    "Ich kann if/elif/else Bedingungen schreiben",
                    "Ich verstehe for-Schleifen für Listen",
                    "Ich kann enumerate() für nummerierte Ausgaben nutzen",
                    "Ich verstehe logische Operatoren (and, or, not)",
                ],
            },
            "funktionen": {
                "titel": "Funktionen",
                "beschreibung": "Modulare Programmierung",
                "fragen": [
                    "Ich kann einfache Funktionen definieren",
                    "Ich verstehe Parameter und Rückgabewerte",
                    "Ich kann Funktionen sinnvoll einsetzen",
                    "Ich verstehe den Unterschied zwischen lokalen und globalen Variablen",
                ],
            },
            "fehlerbehandlung": {
                "titel": "Fehlerbehandlung",
                "beschreibung": "Debugging und Problemlösung",
                "fragen": [
                    "Ich kann häufige Fehlermeldungen verstehen",
                    "Ich kann try/except für Fehlerbehandlung nutzen",
                    "Ich kann systematisch nach Fehlern suchen",
                    "Ich kann Code Schritt für Schritt debuggen",
                ],
            },
            "praxis": {
                "titel": "Praktische Anwendung",
                "beschreibung": "Problemlösung und Projektarbeit",
                "fragen": [
                    "Ich kann kleine Programme selbstständig schreiben",
                    "Ich kann Probleme in Teilschritte zerlegen",
                    "Ich kann bestehenden Code verstehen und anpassen",
                    "Ich kann eigene Ideen in Code umsetzen",
                ],
            },
        }

    def starte_reflexion(self) -> None:
        """Startet den strukturierten Reflexionsprozess."""
        print("🤔 SELBSTREFLEXIONS-TOOL: Python Grundlagen")
        print("=" * 50)
        print("Reflektieren Sie Ihren Lernfortschritt ehrlich und strukturiert.")
        print("Diese Selbsteinschätzung hilft Ihnen, gezielt zu lernen.")
        print("=" * 50)

        self.reflexion_daten["datum"] = datetime.now().isoformat()
        self.reflexion_daten["kompetenzen"] = {}

        # 1. Kompetenz-Selbsteinschätzung
        self._kompetenz_selbsteinschaetzung()

        # 2. Lernprozess-Reflexion
        self._lernprozess_reflexion()

        # 3. Herausforderungen und Erfolge
        self._herausforderungen_erfolge()

        # 4. Zielsetzung
        self._zielsetzung()

        # 5. Auswertung und Empfehlungen
        self._auswertung_und_empfehlungen()

        # 6. Speichern
        self._speichere_reflexion()

    def _kompetenz_selbsteinschaetzung(self) -> None:
        """Führt durch die Kompetenz-Selbsteinschätzung."""
        print("\n📊 TEIL 1: KOMPETENZ-SELBSTEINSCHÄTZUNG")
        print("=" * 45)
        print("Bewerten Sie Ihre Fähigkeiten auf einer Skala von 1-5:")
        print("1 = Gar nicht | 2 = Wenig | 3 = Teilweise | 4 = Gut | 5 = Sehr gut")

        for bereich_id, bereich in self.kompetenzbereiche.items():
            print(f"\n🎯 {bereich['titel']}")
            print(f"   {bereich['beschreibung']}")
            print("-" * 40)

            bereich_bewertungen = []

            for i, frage in enumerate(bereich["fragen"], 1):
                while True:
                    try:
                        bewertung = int(
                            input(f"   {i}. {frage}\n      Bewertung (1-5): ")
                        )
                        if 1 <= bewertung <= 5:
                            bereich_bewertungen.append(bewertung)
                            break
                        else:
                            print(
                                "      ❌ Bitte geben Sie eine Zahl zwischen 1 und 5 ein!"
                            )
                    except ValueError:
                        print("      ❌ Bitte geben Sie eine gültige Zahl ein!")

            # Durchschnitt für Bereich berechnen
            durchschnitt = sum(bereich_bewertungen) / len(bereich_bewertungen)

            self.reflexion_daten["kompetenzen"][bereich_id] = {
                "titel": bereich["titel"],
                "bewertungen": bereich_bewertungen,
                "durchschnitt": durchschnitt,
            }

            print(f"   ➡️ Durchschnitt für {bereich['titel']}: {durchschnitt:.1f}/5")

    def _lernprozess_reflexion(self) -> None:
        """Reflexion über den Lernprozess."""
        print("\n🔄 TEIL 2: LERNPROZESS-REFLEXION")
        print("=" * 40)

        fragen = [
            {
                "key": "lernzeit",
                "frage": "Wie viele Stunden haben Sie bisher für Python gelernt?",
                "typ": "zahl",
            },
            {
                "key": "lernmethoden",
                "frage": "Welche Lernmethoden haben Sie verwendet? (z.B. Übungen, Videos, Bücher)",
                "typ": "text",
            },
            {
                "key": "motivation",
                "frage": "Wie motiviert sind Sie aktuell? (1-5)",
                "typ": "skala",
            },
            {
                "key": "schwierigkeitsgrad",
                "frage": "Wie empfinden Sie den Schwierigkeitsgrad? (1=zu leicht, 3=genau richtig, 5=zu schwer)",
                "typ": "skala",
            },
            {
                "key": "tempo",
                "frage": "Wie empfinden Sie das Lerntempo? (1=zu langsam, 3=genau richtig, 5=zu schnell)",
                "typ": "skala",
            },
        ]

        lernprozess = {}

        for frage_data in fragen:
            print(f"\n❓ {frage_data['frage']}")

            if frage_data["typ"] == "zahl":
                while True:
                    try:
                        antwort = float(input("   Antwort: "))
                        lernprozess[frage_data["key"]] = antwort
                        break
                    except ValueError:
                        print("   ❌ Bitte geben Sie eine Zahl ein!")

            elif frage_data["typ"] == "skala":
                while True:
                    try:
                        antwort = int(input("   Antwort (1-5): "))
                        if 1 <= antwort <= 5:
                            lernprozess[frage_data["key"]] = antwort
                            break
                        else:
                            print(
                                "   ❌ Bitte geben Sie eine Zahl zwischen 1 und 5 ein!"
                            )
                    except ValueError:
                        print("   ❌ Bitte geben Sie eine gültige Zahl ein!")

            else:  # text
                antwort = input("   Antwort: ").strip()
                lernprozess[frage_data["key"]] = antwort

        self.reflexion_daten["lernprozess"] = lernprozess

    def _herausforderungen_erfolge(self) -> None:
        """Reflexion über Herausforderungen und Erfolge."""
        print("\n🎯 TEIL 3: HERAUSFORDERUNGEN UND ERFOLGE")
        print("=" * 45)

        print("\n💪 Was waren Ihre grössten Lernerfolge bisher?")
        print("   (Beschreiben Sie 2-3 konkrete Erfolge)")
        erfolge = []
        for i in range(3):
            erfolg = input(f"   Erfolg {i + 1}: ").strip()
            if erfolg:
                erfolge.append(erfolg)

        print("\n⚠️ Was waren Ihre grössten Herausforderungen?")
        print("   (Beschreiben Sie 2-3 konkrete Schwierigkeiten)")
        herausforderungen = []
        for i in range(3):
            herausforderung = input(f"   Herausforderung {i + 1}: ").strip()
            if herausforderung:
                herausforderungen.append(herausforderung)

        print("\n🤝 Welche Unterstützung würden Sie sich wünschen?")
        unterstuetzung = input("   Antwort: ").strip()

        self.reflexion_daten["erfolge_herausforderungen"] = {
            "erfolge": erfolge,
            "herausforderungen": herausforderungen,
            "gewuenschte_unterstuetzung": unterstuetzung,
        }

    def _zielsetzung(self) -> None:
        """Zielsetzung für weiteres Lernen."""
        print("\n🎯 TEIL 4: ZIELSETZUNG")
        print("=" * 25)

        print("\n🚀 Was möchten Sie als nächstes lernen?")
        naechste_ziele = input("   Antwort: ").strip()

        print("\n⏰ Bis wann möchten Sie diese Ziele erreichen?")
        zeitrahmen = input("   Antwort: ").strip()

        print("\n📅 Wie viel Zeit können Sie pro Woche für Python aufwenden?")
        wochenzeit = input("   Antwort (Stunden): ").strip()

        print("\n🎯 Was ist Ihr langfristiges Ziel mit Python?")
        langfristig = input("   Antwort: ").strip()

        self.reflexion_daten["zielsetzung"] = {
            "naechste_ziele": naechste_ziele,
            "zeitrahmen": zeitrahmen,
            "wochenzeit": wochenzeit,
            "langfristige_ziele": langfristig,
        }

    def _auswertung_und_empfehlungen(self) -> None:
        """Zeigt Auswertung und gibt Empfehlungen."""
        print("\n📊 AUSWERTUNG UND EMPFEHLUNGEN")
        print("=" * 40)

        # Kompetenz-Übersicht
        print("\n🎯 IHRE KOMPETENZ-ÜBERSICHT:")
        print("-" * 30)

        gesamtdurchschnitt = 0
        anzahl_bereiche = len(self.reflexion_daten["kompetenzen"])

        staerkste_bereiche = []
        schwache_bereiche = []

        for bereich_id, daten in self.reflexion_daten["kompetenzen"].items():
            durchschnitt = daten["durchschnitt"]
            gesamtdurchschnitt += durchschnitt

            # Balken-Visualisierung
            balken = "█" * int(durchschnitt) + "░" * (5 - int(durchschnitt))
            print(f"{daten['titel']:<20} {balken} {durchschnitt:.1f}/5")

            if durchschnitt >= 4.0:
                staerkste_bereiche.append(daten["titel"])
            elif durchschnitt < 3.0:
                schwache_bereiche.append(daten["titel"])

        gesamtdurchschnitt /= anzahl_bereiche

        print(f"\n🎯 Gesamtdurchschnitt: {gesamtdurchschnitt:.1f}/5")

        # Bewertung
        if gesamtdurchschnitt >= 4.0:
            bewertung = "🌟 Ausgezeichnet!"
            kommentar = "Sie haben sehr gute Grundkenntnisse entwickelt!"
        elif gesamtdurchschnitt >= 3.0:
            bewertung = "✅ Gut!"
            kommentar = "Solide Grundlagen, gezieltes Üben für Verbesserung."
        elif gesamtdurchschnitt >= 2.0:
            bewertung = "⚠️ Entwicklungsbedarf"
            kommentar = "Grundlagen vorhanden, aber mehr Übung nötig."
        else:
            bewertung = "❌ Anfänger"
            kommentar = "Konzentrieren Sie sich auf die Grundlagen."

        print(f"\n{bewertung}")
        print(f"💬 {kommentar}")

        # Personalisierte Empfehlungen
        print("\n💡 PERSONALISIERTE EMPFEHLUNGEN:")
        print("-" * 35)

        if staerkste_bereiche:
            print(f"🌟 Ihre Stärken: {', '.join(staerkste_bereiche)}")
            print("   → Nutzen Sie diese Stärken für komplexere Projekte!")

        if schwache_bereiche:
            print(f"🎯 Fokus-Bereiche: {', '.join(schwache_bereiche)}")
            print("   → Konzentrieren Sie sich auf diese Bereiche!")

            for bereich in schwache_bereiche:
                if "Grundlagen" in bereich:
                    print("     • Wiederholen Sie Variablen und Datentypen")
                    print("     • Übung: uebung_01_personal_info_beginner.py")
                elif "Datenstrukturen" in bereich:
                    print("     • Üben Sie Listen-Operationen intensiv")
                    print("     • Übung: uebung_03_programmiersprachen_beginner.py")
                elif "Kontrollstrukturen" in bereich:
                    print("     • Fokus auf if/else und for-Schleifen")
                    print("     • Übung: uebung_02_taschenrechner_beginner.py")
                elif "Funktionen" in bereich:
                    print("     • Beginnen Sie mit einfachen Funktionen")
                    print("     • Übung: Intermediate-Übungen anschauen")

        # Lernprozess-Empfehlungen
        lernprozess = self.reflexion_daten["lernprozess"]

        if lernprozess["motivation"] < 3:
            print("\n🔥 Motivation steigern:")
            print("   • Setzen Sie sich kleine, erreichbare Ziele")
            print("   • Feiern Sie jeden kleinen Erfolg")
            print("   • Suchen Sie sich einen Lernpartner")

        if lernprozess["schwierigkeitsgrad"] > 3:
            print("\n📚 Schwierigkeit anpassen:")
            print("   • Beginnen Sie mit einfacheren Übungen")
            print("   • Nutzen Sie die hints.md Dateien intensiv")
            print("   • Arbeiten Sie mit skeleton.py Dateien")

        if lernprozess["tempo"] > 3:
            print("\n⏰ Tempo anpassen:")
            print("   • Nehmen Sie sich mehr Zeit für jede Übung")
            print("   • Wiederholen Sie Konzepte mehrfach")
            print("   • Machen Sie regelmässige Pausen")

    def _speichere_reflexion(self) -> None:
        """Speichert die Reflexionsdaten."""
        try:
            # Versuche vorherige Reflexionen zu laden
            try:
                with open("reflexions_verlauf.json", encoding="utf-8") as f:
                    verlauf = json.load(f)
            except FileNotFoundError:
                verlauf = []

            # Neue Reflexion hinzufügen
            verlauf.append(self.reflexion_daten)

            # Speichern
            with open("reflexions_verlauf.json", "w", encoding="utf-8") as f:
                json.dump(verlauf, f, indent=2, ensure_ascii=False)

            print("\n💾 Reflexion gespeichert in reflexions_verlauf.json")
            print("📈 Sie können Ihren Fortschritt über Zeit verfolgen!")

        except Exception as e:
            print(f"\n⚠️ Konnte Reflexion nicht speichern: {e}")


def main():
    """Hauptfunktion für das Selbstreflexions-Tool."""
    print("🎓 BYSTRONIC PYTHON GRUNDKURS")
    print("Selbstreflexions-Tool für Kapitel 01")
    print("=" * 40)

    tool = SelbstreflexionsTool()

    print("Dieses Tool hilft Ihnen dabei:")
    print("• Ihren Lernfortschritt zu reflektieren")
    print("• Stärken und Schwächen zu identifizieren")
    print("• Ziele für weiteres Lernen zu setzen")
    print("• Personalisierte Empfehlungen zu erhalten")

    bereit = input("\nSind Sie bereit für die Reflexion? (j/n): ").strip().lower()
    if bereit == "j":
        tool.starte_reflexion()
        print("\n🎉 Reflexion abgeschlossen!")
        print("💡 Nutzen Sie die Empfehlungen für Ihr weiteres Lernen.")
    else:
        print("Kommen Sie gerne später zurück! 👋")


if __name__ == "__main__":
    main()

"""
VERWENDUNG:
===========
python micro_assessment_reflection.py

FEATURES:
=========
✅ Strukturierte Kompetenz-Selbsteinschätzung
✅ Reflexion über Lernprozess
✅ Identifikation von Erfolgen und Herausforderungen
✅ Zielsetzung für weiteres Lernen
✅ Personalisierte Empfehlungen
✅ Fortschrittsverfolgung über Zeit
✅ JSON-Export für Verlaufsanalyse

KOMPETENZBEREICHE:
==================
🎯 Python Grundlagen
🎯 Datenstrukturen
🎯 Kontrollstrukturen
🎯 Funktionen
🎯 Fehlerbehandlung
🎯 Praktische Anwendung

REFLEXIONSFRAGEN:
=================
□ Wie schätze ich meine Fähigkeiten ein?
□ Wie läuft mein Lernprozess?
□ Was sind meine Erfolge und Herausforderungen?
□ Was sind meine nächsten Ziele?
□ Welche Unterstützung brauche ich?
"""
