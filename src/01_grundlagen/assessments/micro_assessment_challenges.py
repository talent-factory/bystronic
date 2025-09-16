#!/usr/bin/env python3
"""
🚀 MICRO-ASSESSMENT: Praktische Code-Challenges für Kapitel 01
==============================================================

ZWECK:
Hands-on Programmieraufgaben zur Überprüfung praktischer Fähigkeiten.
Teilnehmer lösen kleine Coding-Challenges mit automatischer Bewertung.

FEATURES:
- Interaktive Programmieraufgaben
- Automatische Code-Ausführung und -Bewertung
- Schritt-für-Schritt Feedback
- Verschiedene Schwierigkeitsgrade
- Realistische Mini-Projekte

ZEIT: 15-25 Minuten
"""

import io


class CodeChallenge:
    """Einzelne Code-Challenge mit automatischer Bewertung."""

    def __init__(
        self,
        challenge_id: str,
        titel: str,
        beschreibung: str,
        schwierigkeit: str,
        punkte: int,
        test_cases: list[dict],
        loesung_template: str = "",
        hinweise: list[str] = None,
    ):
        self.challenge_id = challenge_id
        self.titel = titel
        self.beschreibung = beschreibung
        self.schwierigkeit = schwierigkeit
        self.punkte = punkte
        self.test_cases = test_cases
        self.loesung_template = loesung_template
        self.hinweise = hinweise or []


class MicroAssessmentChallenges:
    """System für praktische Code-Challenges."""

    def __init__(self):
        self.challenges = self._lade_challenges()
        self.ergebnisse = []
        self.gesamt_punkte = 0
        self.max_punkte = 0

    def _lade_challenges(self) -> list[CodeChallenge]:
        """Lädt alle verfügbaren Code-Challenges."""
        return [
            # CHALLENGE 1: Variablen und Ausgabe
            CodeChallenge(
                challenge_id="var_output",
                titel="Persönliche Begrüssung",
                beschreibung="""
Erstellen Sie ein Programm, das:
1. Nach Ihrem Namen fragt
2. Nach Ihrem Alter fragt
3. Eine personalisierte Begrüssung ausgibt

Erwartete Ausgabe (Beispiel):
Hallo Max! Du bist 25 Jahre alt.
                """,
                schwierigkeit="leicht",
                punkte=3,
                test_cases=[
                    {
                        "inputs": ["Max", "25"],
                        "expected_output": "Hallo Max! Du bist 25 Jahre alt.",
                        "beschreibung": "Standard-Test mit Name und Alter",
                    },
                    {
                        "inputs": ["Anna", "30"],
                        "expected_output": "Hallo Anna! Du bist 30 Jahre alt.",
                        "beschreibung": "Test mit anderem Namen und Alter",
                    },
                ],
                loesung_template="""
# Ihr Code hier:
name = input("Wie heissen Sie? ")
alter = input("Wie alt sind Sie? ")
print(f"Hallo {name}! Du bist {alter} Jahre alt.")
                """,
                hinweise=[
                    "Verwenden Sie input() für Eingaben",
                    "Verwenden Sie f-strings für die Ausgabe",
                    "Die Ausgabe muss exakt dem Format entsprechen",
                ],
            ),
            # CHALLENGE 2: Listen-Operationen
            CodeChallenge(
                challenge_id="list_ops",
                titel="Lieblings-Hobbys verwalten",
                beschreibung="""
Erstellen Sie ein Programm, das:
1. Eine Liste mit 3 Hobbys erstellt: ["Lesen", "Sport", "Musik"]
2. "Programmieren" zur Liste hinzufügt
3. Die Liste alphabetisch sortiert
4. Alle Hobbys nummeriert ausgibt (1. Hobby, 2. Hobby, ...)

Erwartete Ausgabe:
1. Lesen
2. Musik
3. Programmieren
4. Sport
                """,
                schwierigkeit="mittel",
                punkte=4,
                test_cases=[
                    {
                        "inputs": [],
                        "expected_output": "1. Lesen\n2. Musik\n3. Programmieren\n4. Sport",
                        "beschreibung": "Standard-Test mit vorgegebenen Hobbys",
                    }
                ],
                loesung_template="""
# Ihr Code hier:
hobbys = ["Lesen", "Sport", "Musik"]
hobbys.append("Programmieren")
hobbys.sort()
for i, hobby in enumerate(hobbys, 1):
    print(f"{i}. {hobby}")
                """,
                hinweise=[
                    "Verwenden Sie append() zum Hinzufügen",
                    "Verwenden Sie sort() zum Sortieren",
                    "Verwenden Sie enumerate(liste, 1) für Nummerierung ab 1",
                ],
            ),
            # CHALLENGE 3: Bedingungen und Berechnungen
            CodeChallenge(
                challenge_id="calc_grade",
                titel="Noten-Rechner",
                beschreibung="""
Erstellen Sie einen Noten-Rechner, der:
1. Nach einer Punktzahl fragt (0-100)
2. Die entsprechende Note berechnet:
   - 90-100: Note 6
   - 80-89: Note 5
   - 70-79: Note 4
   - 60-69: Note 3
   - 50-59: Note 2
   - 0-49: Note 1
3. Das Ergebnis ausgibt

Erwartete Ausgabe (bei 85 Punkten):
85 Punkte entsprechen der Note 5.
                """,
                schwierigkeit="mittel",
                punkte=5,
                test_cases=[
                    {
                        "inputs": ["85"],
                        "expected_output": "85 Punkte entsprechen der Note 5.",
                        "beschreibung": "Test mit 85 Punkten (Note 5)",
                    },
                    {
                        "inputs": ["95"],
                        "expected_output": "95 Punkte entsprechen der Note 6.",
                        "beschreibung": "Test mit 95 Punkten (Note 6)",
                    },
                    {
                        "inputs": ["45"],
                        "expected_output": "45 Punkte entsprechen der Note 1.",
                        "beschreibung": "Test mit 45 Punkten (Note 1)",
                    },
                ],
                loesung_template="""
# Ihr Code hier:
punkte = int(input("Punktzahl (0-100): "))

if punkte >= 90:
    note = 6
elif punkte >= 80:
    note = 5
elif punkte >= 70:
    note = 4
elif punkte >= 60:
    note = 3
elif punkte >= 50:
    note = 2
else:
    note = 1

print(f"{punkte} Punkte entsprechen der Note {note}.")
                """,
                hinweise=[
                    "Verwenden Sie int() um String zu Zahl zu konvertieren",
                    "Verwenden Sie if/elif/else für die Bedingungen",
                    "Beginnen Sie mit der höchsten Punktzahl",
                ],
            ),
            # CHALLENGE 4: Schleifen und Berechnungen
            CodeChallenge(
                challenge_id="sum_calc",
                titel="Summen-Rechner",
                beschreibung="""
Erstellen Sie ein Programm, das:
1. Nach 5 Zahlen fragt
2. Die Summe aller Zahlen berechnet
3. Den Durchschnitt berechnet
4. Das Ergebnis ausgibt

Erwartete Ausgabe (bei Zahlen 10, 20, 30, 40, 50):
Summe: 150
Durchschnitt: 30.0
                """,
                schwierigkeit="mittel",
                punkte=4,
                test_cases=[
                    {
                        "inputs": ["10", "20", "30", "40", "50"],
                        "expected_output": "Summe: 150\nDurchschnitt: 30.0",
                        "beschreibung": "Test mit Zahlen 10-50",
                    },
                    {
                        "inputs": ["5", "15", "25", "35", "45"],
                        "expected_output": "Summe: 125\nDurchschnitt: 25.0",
                        "beschreibung": "Test mit anderen Zahlen",
                    },
                ],
                loesung_template="""
# Ihr Code hier:
zahlen = []
for i in range(5):
    zahl = float(input(f"Zahl {i+1}: "))
    zahlen.append(zahl)

summe = sum(zahlen)
durchschnitt = summe / len(zahlen)

print(f"Summe: {int(summe)}")
print(f"Durchschnitt: {durchschnitt}")
                """,
                hinweise=[
                    "Verwenden Sie eine Schleife für 5 Eingaben",
                    "Sammeln Sie die Zahlen in einer Liste",
                    "Verwenden Sie sum() für die Summe",
                ],
            ),
            # CHALLENGE 5: Erweiterte Listen-Verarbeitung
            CodeChallenge(
                challenge_id="list_analysis",
                titel="Listen-Analyse",
                beschreibung="""
Erstellen Sie ein Programm, das eine Liste von Zahlen analysiert:
Liste: [12, 45, 7, 23, 56, 89, 34, 67, 8, 90]

Das Programm soll ausgeben:
1. Anzahl der Zahlen
2. Grösste Zahl
3. Kleinste Zahl
4. Zahlen grösser als 50

Erwartete Ausgabe:
Anzahl: 10
Grösste Zahl: 90
Kleinste Zahl: 7
Zahlen > 50: [56, 89, 67, 90]
                """,
                schwierigkeit="schwer",
                punkte=6,
                test_cases=[
                    {
                        "inputs": [],
                        "expected_output": "Anzahl: 10\nGrösste Zahl: 90\nKleinste Zahl: 7\nZahlen > 50: [56, 89, 67, 90]",
                        "beschreibung": "Analyse der vorgegebenen Liste",
                    }
                ],
                loesung_template="""
# Ihr Code hier:
zahlen = [12, 45, 7, 23, 56, 89, 34, 67, 8, 90]

anzahl = len(zahlen)
groesste = max(zahlen)
kleinste = min(zahlen)
grosse_zahlen = [z for z in zahlen if z > 50]

print(f"Anzahl: {anzahl}")
print(f"Grösste Zahl: {groesste}")
print(f"Kleinste Zahl: {kleinste}")
print(f"Zahlen > 50: {grosse_zahlen}")
                """,
                hinweise=[
                    "Verwenden Sie len(), max(), min() für Statistiken",
                    "Verwenden Sie List Comprehension oder eine Schleife für Filterung",
                    "Die Liste ist bereits vorgegeben",
                ],
            ),
        ]

    def starte_challenges(self, schwierigkeit: str = "alle") -> None:
        """
        Startet die Code-Challenges.

        Args:
            schwierigkeit: "leicht", "mittel", "schwer", "alle"
        """
        print("🚀 MICRO-ASSESSMENT: Praktische Code-Challenges")
        print("=" * 55)
        print("Lösen Sie praktische Programmieraufgaben!")
        print("Ihr Code wird automatisch getestet und bewertet.")
        print("=" * 55)

        # Challenges nach Schwierigkeit filtern
        if schwierigkeit == "alle":
            ausgewaehlte_challenges = self.challenges
        else:
            ausgewaehlte_challenges = [
                c for c in self.challenges if c.schwierigkeit == schwierigkeit
            ]

        if not ausgewaehlte_challenges:
            print(f"❌ Keine Challenges für Schwierigkeit '{schwierigkeit}' gefunden!")
            return

        print(f"📝 {len(ausgewaehlte_challenges)} Challenges ausgewählt")
        print(f"🎯 Schwierigkeit: {schwierigkeit}")

        # Challenges durchführen
        for i, challenge in enumerate(ausgewaehlte_challenges, 1):
            print(f"\n{'=' * 60}")
            print(f"🎯 CHALLENGE {i}/{len(ausgewaehlte_challenges)}: {challenge.titel}")
            print(
                f"Schwierigkeit: {challenge.schwierigkeit} | Punkte: {challenge.punkte}"
            )
            print(f"{'=' * 60}")

            punkte = self._fuehre_challenge_durch(challenge)
            self.gesamt_punkte += punkte
            self.max_punkte += challenge.punkte

            self.ergebnisse.append(
                {
                    "challenge_id": challenge.challenge_id,
                    "titel": challenge.titel,
                    "punkte_erhalten": punkte,
                    "punkte_max": challenge.punkte,
                    "bestanden": punkte > 0,
                }
            )

        # Gesamtauswertung
        self._zeige_gesamtauswertung()

    def _fuehre_challenge_durch(self, challenge: CodeChallenge) -> int:
        """Führt eine einzelne Challenge durch."""
        print(challenge.beschreibung)

        if challenge.hinweise:
            print("\n💡 HINWEISE:")
            for i, hinweis in enumerate(challenge.hinweise, 1):
                print(f"   {i}. {hinweis}")

        print("\n📝 Schreiben Sie Ihren Code:")
        print("(Beenden Sie mit einer leeren Zeile)")

        # Code-Eingabe sammeln
        code_zeilen = []
        while True:
            try:
                zeile = input(">>> " if not code_zeilen else "... ")
                if not zeile.strip() and code_zeilen:
                    break
                code_zeilen.append(zeile)
            except KeyboardInterrupt:
                print("\n⚠️ Challenge abgebrochen.")
                return 0

        user_code = "\n".join(code_zeilen)

        if not user_code.strip():
            print("❌ Kein Code eingegeben!")
            return 0

        # Code testen
        return self._teste_code(challenge, user_code)

    def _teste_code(self, challenge: CodeChallenge, user_code: str) -> int:
        """Testet den Benutzer-Code gegen die Test-Cases."""
        print("\n🧪 TESTE IHREN CODE...")
        print("-" * 30)

        erfolgreiche_tests = 0

        for i, test_case in enumerate(challenge.test_cases, 1):
            print(f"Test {i}: {test_case['beschreibung']}")

            try:
                # Code in isolierter Umgebung ausführen
                erfolg, ausgabe, fehler = self._fuehre_code_aus(
                    user_code, test_case.get("inputs", [])
                )

                if not erfolg:
                    print(f"❌ Laufzeitfehler: {fehler}")
                    continue

                # Ausgabe vergleichen
                erwartete_ausgabe = test_case["expected_output"].strip()
                tatsaechliche_ausgabe = ausgabe.strip()

                if tatsaechliche_ausgabe == erwartete_ausgabe:
                    print("✅ Test bestanden!")
                    erfolgreiche_tests += 1
                else:
                    print("❌ Test fehlgeschlagen!")
                    print(f"   Erwartet: {erwartete_ausgabe}")
                    print(f"   Erhalten: {tatsaechliche_ausgabe}")

            except Exception as e:
                print(f"❌ Unerwarteter Fehler: {e}")

        # Punkte berechnen
        if erfolgreiche_tests == len(challenge.test_cases):
            punkte = challenge.punkte
            print(f"\n🎉 Alle Tests bestanden! {punkte}/{challenge.punkte} Punkte")
        elif erfolgreiche_tests > 0:
            punkte = int(
                challenge.punkte * (erfolgreiche_tests / len(challenge.test_cases))
            )
            print(f"\n⚠️ Teilweise korrekt: {punkte}/{challenge.punkte} Punkte")
        else:
            punkte = 0
            print(f"\n❌ Keine Tests bestanden: 0/{challenge.punkte} Punkte")

        # Lösungsvorschlag anbieten
        if punkte < challenge.punkte:
            zeige_loesung = (
                input("\n💡 Möchten Sie die Musterlösung sehen? (j/n): ")
                .strip()
                .lower()
            )
            if zeige_loesung == "j":
                print("\n📋 MUSTERLÖSUNG:")
                print(challenge.loesung_template.strip())

        return punkte

    def _fuehre_code_aus(self, code: str, inputs: list[str]) -> tuple[bool, str, str]:
        """
        Führt Code in isolierter Umgebung aus.

        Returns:
            (erfolg, ausgabe, fehler)
        """
        # Input-Iterator für input() Simulation
        input_iter = iter(inputs)

        def mock_input(prompt=""):
            try:
                return next(input_iter)
            except StopIteration:
                return ""

        # Ausgabe und Fehler abfangen
        stdout_capture = io.StringIO()
        stderr_capture = io.StringIO()

        try:
            # Globale Umgebung für Code-Ausführung
            code_globals = {
                "__builtins__": __builtins__,
                "input": mock_input,
                "print": lambda *args, **kwargs: print(
                    *args, **kwargs, file=stdout_capture
                ),
            }

            # Code ausführen
            exec(code, code_globals)

            return True, stdout_capture.getvalue(), ""

        except Exception as e:
            return False, stdout_capture.getvalue(), str(e)

    def _zeige_gesamtauswertung(self) -> None:
        """Zeigt die Gesamtauswertung aller Challenges."""
        print(f"\n{'=' * 60}")
        print("📊 GESAMTAUSWERTUNG - CODE-CHALLENGES")
        print(f"{'=' * 60}")

        # Gesamtergebnis
        prozent = (
            (self.gesamt_punkte / self.max_punkte) * 100 if self.max_punkte > 0 else 0
        )
        print(
            f"🎯 Gesamtergebnis: {self.gesamt_punkte}/{self.max_punkte} Punkte ({prozent:.1f}%)"
        )

        # Einzelergebnisse
        print("\n📋 EINZELERGEBNISSE:")
        print("-" * 50)
        for ergebnis in self.ergebnisse:
            status = "✅" if ergebnis["bestanden"] else "❌"
            print(
                f"{status} {ergebnis['titel']:<25} {ergebnis['punkte_erhalten']}/{ergebnis['punkte_max']} Punkte"
            )

        # Bewertung
        if prozent >= 90:
            bewertung = "🌟 Ausgezeichnet!"
            kommentar = "Sie beherrschen praktisches Programmieren perfekt!"
        elif prozent >= 75:
            bewertung = "✅ Sehr gut!"
            kommentar = "Starke praktische Fähigkeiten, kleine Optimierungen möglich."
        elif prozent >= 60:
            bewertung = "👍 Gut!"
            kommentar = "Solide Grundlagen, mehr Übung für Perfektion."
        elif prozent >= 40:
            bewertung = "⚠️ Verbesserungsbedarf"
            kommentar = "Grundlagen vorhanden, aber mehr Praxis nötig."
        else:
            bewertung = "❌ Ungenügend"
            kommentar = "Arbeiten Sie die Grundlagen nochmals durch und üben Sie mehr."

        print(f"\n{bewertung}")
        print(f"💬 {kommentar}")

        # Empfehlungen
        print("\n💡 EMPFEHLUNGEN:")
        if prozent < 60:
            print("   • Wiederholen Sie die Beginner-Übungen")
            print("   • Nutzen Sie die skeleton.py Dateien als Hilfe")
            print("   • Üben Sie täglich kleine Programmieraufgaben")
        elif prozent < 80:
            print("   • Probieren Sie die Intermediate-Übungen")
            print("   • Fokus auf schwächere Bereiche")
            print("   • Experimentieren Sie mit Variationen")
        else:
            print("   • Versuchen Sie die Advanced-Übungen")
            print("   • Entwickeln Sie eigene Projekte")
            print("   • Helfen Sie anderen beim Lernen")


def main():
    """Hauptfunktion für die Code-Challenges."""
    print("🎓 BYSTRONIC PYTHON GRUNDKURS")
    print("Praktische Code-Challenges für Kapitel 01")
    print("=" * 45)

    challenges = MicroAssessmentChallenges()

    # Benutzer-Optionen
    print("Wählen Sie Ihren Challenge-Modus:")
    print("1. Alle Challenges (5 Aufgaben)")
    print("2. Nur leichte Challenges")
    print("3. Nur mittlere Challenges")
    print("4. Nur schwere Challenges")

    while True:
        try:
            wahl = int(input("\nIhre Wahl (1-4): "))
            if 1 <= wahl <= 4:
                break
            print("❌ Bitte wählen Sie 1-4!")
        except ValueError:
            print("❌ Bitte geben Sie eine Zahl ein!")

    # Challenges starten
    if wahl == 1:
        challenges.starte_challenges("alle")
    elif wahl == 2:
        challenges.starte_challenges("leicht")
    elif wahl == 3:
        challenges.starte_challenges("mittel")
    elif wahl == 4:
        challenges.starte_challenges("schwer")

    print("\n🎉 Challenges beendet! Vielen Dank für Ihre Teilnahme!")
    print("💡 Nutzen Sie die Empfehlungen für gezieltes Üben.")


if __name__ == "__main__":
    main()

"""
VERWENDUNG:
===========
python micro_assessment_challenges.py

FEATURES:
=========
✅ 5 praktische Programmieraufgaben
✅ Automatische Code-Ausführung und -Bewertung
✅ Verschiedene Schwierigkeitsgrade
✅ Realistische Test-Cases
✅ Sofortiges Feedback
✅ Musterlösungen verfügbar
✅ Detaillierte Auswertung

CHALLENGE-TYPEN:
================
🟢 Leicht: Variablen, Ein-/Ausgabe
🟡 Mittel: Listen, Bedingungen, Schleifen
🔴 Schwer: Erweiterte Listen-Verarbeitung

LERNKONTROLLE:
==============
□ Kann ich einfache Programme schreiben?
□ Verstehe ich Listen-Operationen praktisch?
□ Kann ich Bedingungen korrekt implementieren?
□ Beherrsche ich Schleifen und Berechnungen?
□ Kann ich komplexere Datenverarbeitung?
"""
