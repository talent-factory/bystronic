#!/usr/bin/env python3
"""
📊 MICRO-ASSESSMENT: Dashboard für Kapitel 01
=============================================

ZWECK:
Zentrales Dashboard für alle Micro-Assessment-Tools mit Übersicht
über Lernfortschritt, Empfehlungen und nächste Schritte.

FEATURES:
- Übersicht aller Assessment-Ergebnisse
- Fortschrittsverfolgung über Zeit
- Integrierte Empfehlungen
- Direkter Zugang zu allen Tools
- Exportfunktionen

ZEIT: 5-10 Minuten
"""

import json
import os
import subprocess
import sys
from datetime import datetime
from typing import Any


class MicroAssessmentDashboard:
    """Zentrales Dashboard für alle Micro-Assessment-Tools."""

    def __init__(self):
        self.assessment_dateien = {
            "learning_path": "learning_path_results.json",
            "quiz": "quiz_verlauf.json",
            "challenges": "challenges_verlauf.json",
            "reflexion": "reflexions_verlauf.json",
        }

    def zeige_dashboard(self) -> None:
        """Zeigt das Haupt-Dashboard an."""
        print("📊 MICRO-ASSESSMENT DASHBOARD - KAPITEL 01")
        print("=" * 55)
        print("Ihr zentraler Überblick über den Lernfortschritt")
        print("=" * 55)

        # Lade alle verfügbaren Daten
        daten = self._lade_alle_assessment_daten()

        # Zeige Übersicht
        self._zeige_fortschritts_uebersicht(daten)

        # Zeige letzte Aktivitäten
        self._zeige_letzte_aktivitaeten(daten)

        # Zeige Empfehlungen
        self._zeige_empfehlungen(daten)

        # Interaktives Menü
        self._zeige_interaktives_menu()

    def _lade_alle_assessment_daten(self) -> dict[str, Any]:
        """Lädt alle verfügbaren Assessment-Daten."""
        daten = {}

        for tool, dateiname in self.assessment_dateien.items():
            try:
                if os.path.exists(dateiname):
                    with open(dateiname, encoding="utf-8") as f:
                        daten[tool] = json.load(f)
                else:
                    daten[tool] = []
            except Exception as e:
                print(f"⚠️ Konnte {dateiname} nicht laden: {e}")
                daten[tool] = []

        return daten

    def _zeige_fortschritts_uebersicht(self, daten: dict[str, Any]) -> None:
        """Zeigt eine Übersicht des Lernfortschritts."""
        print("\n🎯 LERNFORTSCHRITT-ÜBERSICHT")
        print("-" * 35)

        # Learning Path Assessment
        if daten["learning_path"]:
            letztes_assessment = (
                daten["learning_path"][-1]
                if isinstance(daten["learning_path"], list)
                else daten["learning_path"]
            )
            empfohlener_pfad = letztes_assessment.get("empfohlener_pfad", "Unbekannt")
            gesamtscore = letztes_assessment.get("gesamtscore", 0)
            print(
                f"📋 Eingangsassessment: {empfohlener_pfad} (Score: {gesamtscore:.1f})"
            )
        else:
            print("📋 Eingangsassessment: ❌ Noch nicht durchgeführt")

        # Quiz-Ergebnisse
        if daten["quiz"]:
            letztes_quiz = daten["quiz"][-1]
            quiz_prozent = letztes_quiz.get("prozent", 0)
            print(
                f"🧠 Letztes Quiz: {quiz_prozent:.1f}% ({len(daten['quiz'])} Durchgänge)"
            )
        else:
            print("🧠 Wissensquiz: ❌ Noch nicht durchgeführt")

        # Challenge-Ergebnisse (simuliert, da nicht in challenges.py implementiert)
        print("🚀 Code-Challenges: ⏳ Verfügbar (noch nicht durchgeführt)")

        # Reflexions-Ergebnisse
        if daten["reflexion"]:
            letzte_reflexion = daten["reflexion"][-1]
            kompetenzen = letzte_reflexion.get("kompetenzen", {})
            if kompetenzen:
                durchschnitt = sum(
                    k["durchschnitt"] for k in kompetenzen.values()
                ) / len(kompetenzen)
                print(
                    f"🤔 Letzte Reflexion: {durchschnitt:.1f}/5 ({len(daten['reflexion'])} Reflexionen)"
                )
            else:
                print("🤔 Selbstreflexion: ✅ Durchgeführt")
        else:
            print("🤔 Selbstreflexion: ❌ Noch nicht durchgeführt")

        # Gesamtbewertung
        self._berechne_gesamtbewertung(daten)

    def _berechne_gesamtbewertung(self, daten: dict[str, Any]) -> None:
        """Berechnet eine Gesamtbewertung des Lernfortschritts."""
        print("\n⭐ GESAMTBEWERTUNG:")
        print("-" * 20)

        bewertungen = []

        # Quiz-Bewertung
        if daten["quiz"]:
            letztes_quiz = daten["quiz"][-1]
            quiz_score = letztes_quiz.get("prozent", 0) / 100
            bewertungen.append(("Quiz", quiz_score))

        # Reflexions-Bewertung
        if daten["reflexion"]:
            letzte_reflexion = daten["reflexion"][-1]
            kompetenzen = letzte_reflexion.get("kompetenzen", {})
            if kompetenzen:
                reflexion_score = (
                    sum(k["durchschnitt"] for k in kompetenzen.values())
                    / len(kompetenzen)
                    / 5
                )
                bewertungen.append(("Reflexion", reflexion_score))

        if bewertungen:
            gesamtscore = sum(score for _, score in bewertungen) / len(bewertungen)

            # Visualisierung
            balken = "█" * int(gesamtscore * 10) + "░" * (10 - int(gesamtscore * 10))
            print(f"Fortschritt: {balken} {gesamtscore * 100:.1f}%")

            # Bewertung
            if gesamtscore >= 0.8:
                status = "🌟 Ausgezeichnet!"
            elif gesamtscore >= 0.6:
                status = "✅ Gut!"
            elif gesamtscore >= 0.4:
                status = "⚠️ Entwicklungsbedarf"
            else:
                status = "❌ Mehr Übung nötig"

            print(f"Status: {status}")
        else:
            print("Noch keine Bewertung möglich - führen Sie Assessments durch!")

    def _zeige_letzte_aktivitaeten(self, daten: dict[str, Any]) -> None:
        """Zeigt die letzten Assessment-Aktivitäten."""
        print("\n📅 LETZTE AKTIVITÄTEN")
        print("-" * 25)

        aktivitaeten = []

        # Sammle alle Aktivitäten mit Datum
        for tool, tool_daten in daten.items():
            if tool_daten:
                if isinstance(tool_daten, list):
                    for eintrag in tool_daten[-3:]:  # Letzte 3 Einträge
                        datum_str = eintrag.get("datum", "Unbekannt")
                        aktivitaeten.append((datum_str, tool, eintrag))
                else:
                    datum_str = tool_daten.get("datum", "Unbekannt")
                    aktivitaeten.append((datum_str, tool, tool_daten))

        # Sortiere nach Datum (neueste zuerst)
        try:
            aktivitaeten.sort(
                key=lambda x: datetime.fromisoformat(x[0].replace("Z", "+00:00")),
                reverse=True,
            )
        except:
            pass  # Falls Datum-Parsing fehlschlägt

        # Zeige letzte 5 Aktivitäten
        for i, (datum_str, tool, eintrag) in enumerate(aktivitaeten[:5]):
            try:
                datum = datetime.fromisoformat(datum_str.replace("Z", "+00:00"))
                datum_formatiert = datum.strftime("%d.%m.%Y %H:%M")
            except:
                datum_formatiert = datum_str

            tool_namen = {
                "learning_path": "📋 Eingangsassessment",
                "quiz": "🧠 Wissensquiz",
                "challenges": "🚀 Code-Challenges",
                "reflexion": "🤔 Selbstreflexion",
            }

            tool_name = tool_namen.get(tool, tool)

            if tool == "quiz":
                prozent = eintrag.get("prozent", 0)
                print(f"{datum_formatiert} - {tool_name} ({prozent:.1f}%)")
            elif tool == "reflexion":
                kompetenzen = eintrag.get("kompetenzen", {})
                if kompetenzen:
                    durchschnitt = sum(
                        k["durchschnitt"] for k in kompetenzen.values()
                    ) / len(kompetenzen)
                    print(f"{datum_formatiert} - {tool_name} ({durchschnitt:.1f}/5)")
                else:
                    print(f"{datum_formatiert} - {tool_name}")
            else:
                print(f"{datum_formatiert} - {tool_name}")

        if not aktivitaeten:
            print("Noch keine Aktivitäten - starten Sie mit einem Assessment!")

    def _zeige_empfehlungen(self, daten: dict[str, Any]) -> None:
        """Zeigt personalisierte Empfehlungen basierend auf den Daten."""
        print("\n💡 PERSONALISIERTE EMPFEHLUNGEN")
        print("-" * 35)

        empfehlungen = []

        # Prüfe fehlende Assessments
        if not daten["learning_path"]:
            empfehlungen.append(
                "🎯 Starten Sie mit dem Eingangsassessment für optimale Lernpfad-Empfehlung"
            )

        if not daten["quiz"]:
            empfehlungen.append("🧠 Testen Sie Ihr Wissen mit dem interaktiven Quiz")

        if not daten["reflexion"]:
            empfehlungen.append(
                "🤔 Reflektieren Sie Ihren Lernprozess mit dem Selbstreflexions-Tool"
            )

        # Analysiere Quiz-Performance
        if daten["quiz"]:
            letztes_quiz = daten["quiz"][-1]
            quiz_prozent = letztes_quiz.get("prozent", 0)

            if quiz_prozent < 60:
                empfehlungen.append(
                    "📚 Quiz-Score unter 60% - wiederholen Sie die Grundlagen"
                )
                empfehlungen.append("💡 Nutzen Sie die hints.md Dateien für Konzepte")
            elif quiz_prozent < 80:
                empfehlungen.append(
                    "🚀 Gute Quiz-Performance - probieren Sie die Intermediate-Übungen"
                )
            else:
                empfehlungen.append(
                    "🌟 Exzellente Quiz-Performance - versuchen Sie die Advanced-Übungen"
                )

        # Analysiere Reflexions-Daten
        if daten["reflexion"]:
            letzte_reflexion = daten["reflexion"][-1]
            kompetenzen = letzte_reflexion.get("kompetenzen", {})

            # Finde schwächste Bereiche
            if kompetenzen:
                schwache_bereiche = [
                    titel
                    for bereich_id, bereich in kompetenzen.items()
                    if bereich["durchschnitt"] < 3.0
                    for titel in [bereich["titel"]]
                ]

                if schwache_bereiche:
                    empfehlungen.append(f"🎯 Fokus auf: {', '.join(schwache_bereiche)}")

        # Zeitbasierte Empfehlungen
        heute = datetime.now()

        if daten["quiz"]:
            letztes_quiz_datum = datetime.fromisoformat(daten["quiz"][-1]["datum"])
            tage_seit_quiz = (heute - letztes_quiz_datum).days

            if tage_seit_quiz > 7:
                empfehlungen.append(
                    "🔄 Letztes Quiz ist über eine Woche her - Zeit für Wiederholung!"
                )

        # Zeige Empfehlungen
        if empfehlungen:
            for i, empfehlung in enumerate(empfehlungen[:5], 1):
                print(f"{i}. {empfehlung}")
        else:
            print("🎉 Alle Assessments durchgeführt - weiter so!")
            print("💡 Wiederholen Sie regelmässig zur Festigung des Wissens")

    def _zeige_interaktives_menu(self) -> None:
        """Zeigt das interaktive Menü für weitere Aktionen."""
        print("\n🛠️ AKTIONEN")
        print("-" * 15)
        print("1. 📋 Eingangsassessment starten")
        print("2. 🧠 Wissensquiz durchführen")
        print("3. 🚀 Code-Challenges lösen")
        print("4. 🤔 Selbstreflexion starten")
        print("5. 📊 Detaillierte Statistiken")
        print("6. 📄 Fortschrittsbericht exportieren")
        print("0. ❌ Dashboard beenden")

        while True:
            try:
                wahl = int(input("\nIhre Wahl (0-6): "))
                if 0 <= wahl <= 6:
                    self._fuehre_aktion_aus(wahl)
                    break
                else:
                    print("❌ Bitte wählen Sie 0-6!")
            except ValueError:
                print("❌ Bitte geben Sie eine Zahl ein!")

    def _fuehre_aktion_aus(self, wahl: int) -> None:
        """Führt die gewählte Aktion aus."""
        if wahl == 0:
            print("\n👋 Dashboard beendet. Viel Erfolg beim Lernen!")
            return

        elif wahl == 1:
            print("\n🚀 Starte Eingangsassessment...")
            self._starte_tool("learning_path_assessment.py")

        elif wahl == 2:
            print("\n🧠 Starte Wissensquiz...")
            self._starte_tool("micro_assessment_quiz.py")

        elif wahl == 3:
            print("\n🚀 Starte Code-Challenges...")
            self._starte_tool("micro_assessment_challenges.py")

        elif wahl == 4:
            print("\n🤔 Starte Selbstreflexion...")
            self._starte_tool("micro_assessment_reflection.py")

        elif wahl == 5:
            self._zeige_detaillierte_statistiken()

        elif wahl == 6:
            self._exportiere_fortschrittsbericht()

    def _starte_tool(self, tool_datei: str) -> None:
        """Startet ein Assessment-Tool."""
        try:
            if os.path.exists(tool_datei):
                subprocess.run([sys.executable, tool_datei])
                print(f"\n✅ {tool_datei} beendet. Kehre zum Dashboard zurück...")
                input("Drücken Sie Enter um fortzufahren...")
                self.zeige_dashboard()  # Dashboard neu laden
            else:
                print(f"❌ {tool_datei} nicht gefunden!")
        except Exception as e:
            print(f"❌ Fehler beim Starten von {tool_datei}: {e}")

    def _zeige_detaillierte_statistiken(self) -> None:
        """Zeigt detaillierte Statistiken aller Assessments."""
        print("\n📊 DETAILLIERTE STATISTIKEN")
        print("=" * 30)

        daten = self._lade_alle_assessment_daten()

        # Quiz-Statistiken
        if daten["quiz"]:
            print("\n🧠 QUIZ-STATISTIKEN:")
            print("-" * 20)

            quiz_scores = [q["prozent"] for q in daten["quiz"]]
            print(f"Durchgänge: {len(quiz_scores)}")
            print(f"Bester Score: {max(quiz_scores):.1f}%")
            print(f"Durchschnitt: {sum(quiz_scores) / len(quiz_scores):.1f}%")
            print(f"Letzter Score: {quiz_scores[-1]:.1f}%")

            # Fortschritt über Zeit
            if len(quiz_scores) > 1:
                verbesserung = quiz_scores[-1] - quiz_scores[0]
                print(f"Verbesserung: {verbesserung:+.1f}%")

        # Reflexions-Statistiken
        if daten["reflexion"]:
            print("\n🤔 REFLEXIONS-STATISTIKEN:")
            print("-" * 25)

            letzte_reflexion = daten["reflexion"][-1]
            kompetenzen = letzte_reflexion.get("kompetenzen", {})

            if kompetenzen:
                print("Kompetenz-Durchschnitte:")
                for bereich_id, bereich in kompetenzen.items():
                    print(f"  {bereich['titel']}: {bereich['durchschnitt']:.1f}/5")

        input("\nDrücken Sie Enter um zurückzukehren...")

    def _exportiere_fortschrittsbericht(self) -> None:
        """Exportiert einen umfassenden Fortschrittsbericht."""
        print("\n📄 FORTSCHRITTSBERICHT EXPORTIEREN")
        print("-" * 35)

        daten = self._lade_alle_assessment_daten()

        bericht = {
            "erstellt_am": datetime.now().isoformat(),
            "kapitel": "01 - Python Grundlagen",
            "assessment_daten": daten,
            "zusammenfassung": self._erstelle_zusammenfassung(daten),
        }

        dateiname = (
            f"fortschrittsbericht_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        )

        try:
            with open(dateiname, "w", encoding="utf-8") as f:
                json.dump(bericht, f, indent=2, ensure_ascii=False)

            print(f"✅ Fortschrittsbericht exportiert: {dateiname}")
            print("📊 Der Bericht enthält alle Assessment-Daten und Statistiken")

        except Exception as e:
            print(f"❌ Fehler beim Export: {e}")

        input("\nDrücken Sie Enter um zurückzukehren...")

    def _erstelle_zusammenfassung(self, daten: dict[str, Any]) -> dict[str, Any]:
        """Erstellt eine Zusammenfassung der Assessment-Daten."""
        zusammenfassung = {
            "assessments_durchgefuehrt": [],
            "gesamtaktivitaet": 0,
            "empfohlene_naechste_schritte": [],
        }

        for tool, tool_daten in daten.items():
            if tool_daten:
                zusammenfassung["assessments_durchgefuehrt"].append(tool)
                if isinstance(tool_daten, list):
                    zusammenfassung["gesamtaktivitaet"] += len(tool_daten)
                else:
                    zusammenfassung["gesamtaktivitaet"] += 1

        return zusammenfassung


def main():
    """Hauptfunktion für das Assessment-Dashboard."""
    print("🎓 BYSTRONIC PYTHON GRUNDKURS")
    print("Micro-Assessment Dashboard für Kapitel 01")
    print("=" * 45)

    dashboard = MicroAssessmentDashboard()
    dashboard.zeige_dashboard()


if __name__ == "__main__":
    main()

"""
VERWENDUNG:
===========
python micro_assessment_dashboard.py

FEATURES:
=========
✅ Zentraler Überblick über alle Assessments
✅ Fortschrittsverfolgung über Zeit
✅ Personalisierte Empfehlungen
✅ Direkter Zugang zu allen Tools
✅ Detaillierte Statistiken
✅ Export-Funktionen
✅ Interaktive Navigation

DASHBOARD-BEREICHE:
===================
📊 Lernfortschritt-Übersicht
📅 Letzte Aktivitäten
💡 Personalisierte Empfehlungen
🛠️ Direkte Tool-Starts
📊 Detaillierte Statistiken
📄 Fortschrittsbericht-Export

INTEGRATION:
============
□ Eingangsassessment (learning_path_assessment.py)
□ Wissensquiz (micro_assessment_quiz.py)
□ Code-Challenges (micro_assessment_challenges.py)
□ Selbstreflexion (micro_assessment_reflection.py)
"""
