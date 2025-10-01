#!/usr/bin/env python3
"""
🟢 BEGINNER - SmartFactory Python Grundkurs - Kapitel 2
Übung 1: Zahlenoperationen (Einsteigerfreundlich)

🎯 LERNZIELE (15-20 Minuten):
- Grundlegende Zahlentypen verstehen (int, float, bool)
- Einfache mathematische Operationen durchführen
- Variablen erstellen und verwenden
- Erste Schritte mit type() und print()

📚 HILFSMITTEL:
- Hints: solutions/beginner/uebung_01_hints.md
- Skeleton: solutions/beginner/uebung_01_skeleton.py
- Partial: solutions/beginner/uebung_01_partial.py
- Complete: solutions/beginner/uebung_01_complete.py

🏭 BYSTRONIC-KONTEXT:
Lernen Sie Zahlen zu verwenden, wie sie in der Produktion vorkommen:
Stückzahlen, Materialdicken, Geschwindigkeiten, Qualitätswerte.
"""


def aufgabe_1_grundlagen():
    """🎯 Aufgabe 1: Erste Schritte mit Zahlen"""
    print("=" * 50)
    print("🟢 AUFGABE 1: Zahlentypen kennenlernen")
    print("=" * 50)

    # TODO 1: Erstellen Sie diese Variablen für eine SmartFactory-Maschine
    print("📊 Maschinendaten eingeben:")

    # Ganze Zahlen (Integer)
    teile_heute = 150  # Anzahl produzierte Teile heute

    # Kommazahlen (Float)
    materialdicke = 2.5  # Dicke des Materials in mm

    # Wahrheitswerte (Boolean)
    maschine_laeuft = True  # Ist die Maschine in Betrieb?

    # TODO 2: Geben Sie die Werte und ihre Typen aus
    print(f"Teile heute: {teile_heute} (Typ: {type(teile_heute).__name__})")
    print(f"Materialdicke: {materialdicke} mm (Typ: {type(materialdicke).__name__})")
    print(f"Maschine läuft: {maschine_laeuft} (Typ: {type(maschine_laeuft).__name__})")

    print("\n✅ Aufgabe 1 abgeschlossen!")


def aufgabe_2_berechnungen():
    """🎯 Aufgabe 2: Einfache Berechnungen"""
    print("\n" + "=" * 50)
    print("🟢 AUFGABE 2: Einfache Berechnungen")
    print("=" * 50)

    # TODO 1: Grundrechenarten mit Produktionsdaten
    teile_montag = 120
    teile_dienstag = 135
    teile_mittwoch = 98

    # Addition
    teile_gesamt = teile_montag + teile_dienstag + teile_mittwoch
    print(f"📈 Teile gesamt (3 Tage): {teile_gesamt}")

    # Division für Durchschnitt
    durchschnitt = teile_gesamt / 3
    print(f"📊 Durchschnitt pro Tag: {durchschnitt:.1f}")

    # TODO 2: Materialberechnungen
    laenge_pro_teil = 0.85  # Meter pro Teil
    material_gesamt = teile_gesamt * laenge_pro_teil
    print(f"📏 Material benötigt: {material_gesamt:.2f} Meter")

    # TODO 3: Prozentrechnung
    soll_teile = 400  # Soll-Produktion für 3 Tage
    prozent_erreicht = (teile_gesamt / soll_teile) * 100
    print(f"🎯 Ziel erreicht: {prozent_erreicht:.1f}%")

    print("\n✅ Aufgabe 2 abgeschlossen!")


def aufgabe_3_vergleiche():
    """🎯 Aufgabe 3: Werte vergleichen"""
    print("\n" + "=" * 50)
    print("🟢 AUFGABE 3: Werte vergleichen")
    print("=" * 50)

    # TODO 1: Qualitätskontrolle mit Vergleichen
    gemessene_dicke = 2.48  # mm
    soll_dicke = 2.50  # mm
    toleranz = 0.05  # mm

    # Prüfungen
    zu_duenn = gemessene_dicke < (soll_dicke - toleranz)
    zu_dick = gemessene_dicke > (soll_dicke + toleranz)
    in_toleranz = not (zu_duenn or zu_dick)

    print(f"🔍 Gemessene Dicke: {gemessene_dicke} mm")
    print(f"📏 Soll-Dicke: {soll_dicke} mm (±{toleranz} mm)")
    print(f"❌ Zu dünn: {zu_duenn}")
    print(f"❌ Zu dick: {zu_dick}")
    print(f"✅ In Toleranz: {in_toleranz}")

    # TODO 2: Produktionsziele prüfen
    aktuelle_stueckzahl = 1250
    tagesziel = 1200
    wochenziel = 6000

    tagesziel_erreicht = aktuelle_stueckzahl >= tagesziel
    wochenziel_moeglich = aktuelle_stueckzahl * 5 >= wochenziel

    print(f"\n📊 Aktuelle Stückzahl: {aktuelle_stueckzahl}")
    print(f"🎯 Tagesziel erreicht: {tagesziel_erreicht}")
    print(f"📅 Wochenziel möglich: {wochenziel_moeglich}")

    print("\n✅ Aufgabe 3 abgeschlossen!")


def aufgabe_4_eingabe():
    """🎯 Aufgabe 4: Benutzereingaben verarbeiten"""
    print("\n" + "=" * 50)
    print("🟢 AUFGABE 4: Benutzereingaben")
    print("=" * 50)

    # TODO 1: Einfache Eingaben
    print("📝 Geben Sie Produktionsdaten ein:")

    # Eingabe als Text, dann zu Zahl konvertieren
    eingabe_teile = input("Anzahl produzierte Teile: ")
    anzahl_teile = int(eingabe_teile)  # String zu Integer

    eingabe_zeit = input("Produktionszeit in Stunden: ")
    produktionszeit = float(eingabe_zeit)  # String zu Float

    # TODO 2: Berechnungen mit Eingaben
    teile_pro_stunde = anzahl_teile / produktionszeit

    print("\n📊 AUSWERTUNG:")
    print(f"Teile produziert: {anzahl_teile}")
    print(f"Produktionszeit: {produktionszeit} Stunden")
    print(f"Teile pro Stunde: {teile_pro_stunde:.1f}")

    # TODO 3: Bewertung
    if teile_pro_stunde >= 50:
        bewertung = "Sehr gut! 🌟"
    elif teile_pro_stunde >= 30:
        bewertung = "Gut 👍"
    else:
        bewertung = "Verbesserung möglich 📈"

    print(f"Bewertung: {bewertung}")

    print("\n✅ Aufgabe 4 abgeschlossen!")


def main():
    """🚀 Hauptprogramm - Alle Aufgaben ausführen"""
    print("🟢 BEGINNER: Zahlenoperationen für SmartFactory")
    print("=" * 60)
    print("📚 Lernen Sie die Grundlagen von Zahlen in Python!")
    print("🏭 Mit praktischen Beispielen aus der Produktion")
    print()

    try:
        aufgabe_1_grundlagen()
        aufgabe_2_berechnungen()
        aufgabe_3_vergleiche()
        aufgabe_4_eingabe()

        print("\n" + "🎉" * 20)
        print("🎉 HERZLICHEN GLÜCKWUNSCH! 🎉")
        print("🎉" * 20)
        print("✅ Sie haben alle Beginner-Aufgaben zu Zahlen gemeistert!")
        print("📈 Nächster Schritt: Intermediate-Level oder String-Übungen")
        print("🏆 Sie können jetzt:")
        print("   • Zahlentypen unterscheiden und verwenden")
        print("   • Grundrechenarten durchführen")
        print("   • Werte vergleichen und bewerten")
        print("   • Benutzereingaben verarbeiten")

    except Exception as e:
        print(f"\n❌ Fehler aufgetreten: {e}")
        print("💡 Tipp: Überprüfen Sie Ihre Eingaben und versuchen Sie es erneut")


if __name__ == "__main__":
    main()
