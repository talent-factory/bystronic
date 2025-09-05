#!/usr/bin/env python3
"""
🟢 PARTIAL: Übung 1 - Persönliche Informationen (Beginner)
==========================================================

ANLEITUNG:
Diese Version ist fast vollständig implementiert. Nur wenige Lücken müssen
noch gefüllt werden. Perfekt, wenn Sie fast fertig sind!

HILFE:
- Die meiste Arbeit ist bereits getan
- Nur noch 3-4 kleine Ergänzungen nötig
- Schauen Sie nach den # ERGÄNZEN Kommentaren
"""

# Begrüssung ausgeben
print("=" * 40)
print("WILLKOMMEN BEI BYSTRONIC!")
print("=" * 40)
print("Erzählen Sie uns etwas über sich...")

# Nach persönlichen Informationen fragen
name = input("Wie heissen Sie? ")
alter = input("Wie alt sind Sie? ")
wohnort = input("Wo wohnen Sie? ")
beruf = input("Was ist Ihr Beruf? ")

# Zusätzliche Frage (optional)
# TODO: Ergänzen Sie hier eine weitere interessante Frage
hobby = input("# ERGÄNZEN: Frage nach einem Hobby")

# Zusammenfassung ausgeben
print("\n" + "=" * 40)
print("IHRE ANGABEN:")
print("=" * 40)

print(f"Name:     {name}")
print(f"Alter:    {alter}")
print(f"Wohnort:  {wohnort}")
print(f"Beruf:    {beruf}")
# TODO: Geben Sie auch das Hobby aus
print("Hobby:    # ERGÄNZEN")

# Persönliche Nachricht erstellen
print("\n" + "-" * 40)
print(f"Hallo {name}! Schön, dass Sie aus {wohnort} zu uns gefunden haben!")

# TODO: Ergänzen Sie eine weitere persönliche Zeile mit Alter oder Beruf
print(f"# ERGÄNZEN: Weitere persönliche Nachricht mit {alter} oder {beruf}")

# Spezielle Nachricht basierend auf Beruf
if beruf.lower() in ["ingenieur", "techniker", "entwickler", "programmierer"]:
    print("Als technische Fachkraft werden Sie Python sicher schnell meistern!")
elif beruf.lower() in ["manager", "leiter", "chef"]:
    print(
        "Als Führungskraft können Sie Python für Datenanalyse und Automatisierung nutzen!"
    )
else:
    # TODO: Ergänzen Sie eine allgemeine Nachricht für andere Berufe
    print("# ERGÄNZEN: Allgemeine motivierende Nachricht")

# Verabschiedung
print("-" * 40)
print("Vielen Dank für Ihre Angaben!")
print("Willkommen im Bystronic Python-Kurs! 🐍")

# BONUS: Statistik anzeigen
print(f"\nStatistik: Sie haben {len(name.split())} Wörter in Ihrem Namen.")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
========================================
WILLKOMMEN BEI BYSTRONIC!
========================================
Erzählen Sie uns etwas über sich...
Wie heissen Sie? Anna Müller
Wie alt sind Sie? 32
Wo wohnen Sie? Basel
Was ist Ihr Beruf? Ingenieurin
Was ist Ihr Lieblingshobby? Wandern

========================================
IHRE ANGABEN:
========================================
Name:     Anna Müller
Alter:    32
Wohnort:  Basel
Beruf:    Ingenieurin
Hobby:    Wandern

----------------------------------------
Hallo Anna Müller! Schön, dass Sie aus Basel zu uns gefunden haben!
Mit 32 Jahren haben Sie sicher schon viel Berufserfahrung gesammelt!
Als technische Fachkraft werden Sie Python sicher schnell meistern!
----------------------------------------
Vielen Dank für Ihre Angaben!
Willkommen im Bystronic Python-Kurs! 🐍

Statistik: Sie haben 2 Wörter in Ihrem Namen.

WAS FEHLT NOCH:
===============
□ Hobby-Frage formulieren
□ Hobby in der Ausgabe anzeigen
□ Weitere persönliche Nachricht mit Alter/Beruf
□ Allgemeine Nachricht für andere Berufe

LÖSUNGSHILFEN:
==============
1. hints.md     - Konzeptuelle Tipps
2. skeleton.py  - Code-Grundgerüst
3. partial.py   - Teilweise implementiert (Sie sind hier!)
4. complete.py  - Vollständige Lösung
"""
