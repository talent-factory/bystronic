#!/usr/bin/env python3
"""
🟢 COMPLETE: Übung 1 - Persönliche Informationen (Beginner)
===========================================================

MUSTERLÖSUNG:
Dies ist eine vollständige, professionelle Lösung der Übung.
Verwenden Sie diese nur, wenn Sie wirklich nicht weiterkommen!

LERNZIELE ERFÜLLT:
✅ input() für Benutzereingaben
✅ Variablen zum Speichern von Daten
✅ f-strings für formatierte Ausgaben
✅ print() für strukturierte Ausgaben
✅ Einfache Bedingungen (if/else)
"""

# Begrüssung ausgeben
print("=" * 40)
print("WILLKOMMEN BEI BYSTRONIC!")
print("=" * 40)
print("Erzählen Sie uns etwas über sich...")
print("Wir freuen uns, Sie kennenzulernen! 😊")

# Nach persönlichen Informationen fragen
name = input("\nWie heissen Sie? ")
alter = input("Wie alt sind Sie? ")
wohnort = input("Wo wohnen Sie? ")
beruf = input("Was ist Ihr Beruf? ")
hobby = input("Was ist Ihr Lieblingshobby? ")

# Zusätzliche interessante Frage
erfahrung = input("Haben Sie schon mal programmiert? (ja/nein) ")

# Zusammenfassung ausgeben
print("\n" + "=" * 40)
print("IHRE ANGABEN:")
print("=" * 40)

print(f"Name:           {name}")
print(f"Alter:          {alter} Jahre")
print(f"Wohnort:        {wohnort}")
print(f"Beruf:          {beruf}")
print(f"Hobby:          {hobby}")
print(f"Programmiererfahrung: {erfahrung}")

# Persönliche Nachricht erstellen
print("\n" + "-" * 40)
print("PERSÖNLICHE NACHRICHT:")
print("-" * 40)

print(f"Hallo {name}! Schön, dass Sie aus {wohnort} zu uns gefunden haben!")

# Altersbasierte Nachricht
try:
    alter_zahl = int(alter)
    if alter_zahl < 25:
        print("Als junge Person haben Sie beste Voraussetzungen für das Programmieren!")
    elif alter_zahl < 40:
        print(
            f"Mit {alter} Jahren haben Sie die perfekte Balance aus Erfahrung und Lernbereitschaft!"
        )
    else:
        print("Ihre Lebenserfahrung wird Ihnen beim strukturierten Denken sehr helfen!")
except ValueError:
    print("Egal in welchem Alter - es ist nie zu spät zum Programmieren lernen!")

# Berufsbasierte Nachricht
if beruf.lower() in [
    "ingenieur",
    "ingenieurin",
    "techniker",
    "technikerin",
    "entwickler",
    "entwicklerin",
    "programmierer",
    "programmiererin",
]:
    print("Als technische Fachkraft werden Sie Python sicher schnell meistern!")
elif beruf.lower() in [
    "manager",
    "managerin",
    "leiter",
    "leiterin",
    "chef",
    "chefin",
    "direktor",
    "direktorin",
]:
    print(
        "Als Führungskraft können Sie Python für Datenanalyse und Automatisierung nutzen!"
    )
elif beruf.lower() in ["student", "studentin", "schüler", "schülerin"]:
    print("Als Lernende/r haben Sie den perfekten Zeitpunkt gewählt, Python zu lernen!")
else:
    print(
        f"In Ihrem Beruf als {beruf} gibt es sicher viele Möglichkeiten für Automatisierung!"
    )

# Hobby-basierte Nachricht
if hobby.lower() in ["lesen", "bücher", "lernen", "studieren"]:
    print(
        f"Ihr Hobby '{hobby}' zeigt, dass Sie gerne Neues lernen - perfekt für Python!"
    )
elif hobby.lower() in ["sport", "fitness", "laufen", "wandern", "radfahren"]:
    print(f"Wie beim {hobby} braucht auch Programmieren Ausdauer und Übung!")
elif hobby.lower() in ["musik", "instrument", "klavier", "gitarre"]:
    print(
        f"Programmieren ist wie {hobby} - es braucht Übung, aber macht dann richtig Spass!"
    )
else:
    print(f"Ihr Hobby '{hobby}' zeigt Ihre vielseitigen Interessen!")

# Erfahrungsbasierte Nachricht
if erfahrung.lower() in ["ja", "yes", "j", "y"]:
    print("Prima! Ihre Vorerfahrung wird Ihnen helfen, schneller voranzukommen.")
else:
    print("Kein Problem! Jeder Experte hat mal als Anfänger begonnen.")

# Motivierende Abschlussnachricht
print(f"\nWir sind gespannt auf Ihre Fortschritte im Kurs, {name}!")

# Verabschiedung
print("-" * 40)
print("Vielen Dank für Ihre Angaben!")
print("Willkommen im SmartFactory Python-Kurs! 🐍")

# BONUS: Interessante Statistiken
print("\n📊 KLEINE STATISTIKEN:")
print(f"• Ihr Name hat {len(name)} Zeichen")
print(f"• Ihr Name hat {len(name.split())} Wörter")
print(f"• Ihr Wohnort hat {len(wohnort)} Zeichen")
print(
    f"• Sie haben insgesamt {len(name + alter + wohnort + beruf + hobby)} Zeichen eingegeben"
)

# Zusätzliche Motivation
print("\n🎯 IHR LERNZIEL:")
print("Am Ende dieses Kurses können Sie eigene Python-Programme schreiben!")
print("Viel Erfolg und Spass beim Lernen! 🚀")

"""
ERWARTETE AUSGABE (Beispiel):
=============================
========================================
WILLKOMMEN BEI BYSTRONIC!
========================================
Erzählen Sie uns etwas über sich...
Wir freuen uns, Sie kennenzulernen! 😊

Wie heissen Sie? Max Mustermann
Wie alt sind Sie? 28
Wo wohnen Sie? Zürich
Was ist Ihr Beruf? Ingenieur
Was ist Ihr Lieblingshobby? Wandern
Haben Sie schon mal programmiert? (ja/nein) nein

========================================
IHRE ANGABEN:
========================================
Name:           Max Mustermann
Alter:          28 Jahre
Wohnort:        Zürich
Beruf:          Ingenieur
Hobby:          Wandern
Programmiererfahrung: nein

----------------------------------------
PERSÖNLICHE NACHRICHT:
----------------------------------------
Hallo Max Mustermann! Schön, dass Sie aus Zürich zu uns gefunden haben!
Mit 28 Jahren haben Sie die perfekte Balance aus Erfahrung und Lernbereitschaft!
Als technische Fachkraft werden Sie Python sicher schnell meistern!
Wie beim Wandern braucht auch Programmieren Ausdauer und Übung!
Kein Problem! Jeder Experte hat mal als Anfänger begonnen.

Wir sind gespannt auf Ihre Fortschritte im Kurs, Max Mustermann!
----------------------------------------
Vielen Dank für Ihre Angaben!
Willkommen im SmartFactory Python-Kurs! 🐍

📊 KLEINE STATISTIKEN:
• Ihr Name hat 14 Zeichen
• Ihr Name hat 2 Wörter
• Ihr Wohnort hat 6 Zeichen
• Sie haben insgesamt 39 Zeichen eingegeben

🎯 IHR LERNZIEL:
Am Ende dieses Kurses können Sie eigene Python-Programme schreiben!
Viel Erfolg und Spass beim Lernen! 🚀

VERWENDETE KONZEPTE:
====================
✅ input() - Benutzereingaben
✅ Variablen - Datenspeicherung
✅ f-strings - Formatierte Ausgaben
✅ print() - Strukturierte Ausgaben
✅ if/elif/else - Bedingte Ausführung
✅ try/except - Fehlerbehandlung
✅ String-Methoden - .lower(), .split(), len()
✅ Datentyp-Konvertierung - int()

NÄCHSTE SCHRITTE:
=================
🎯 Verstehen Sie alle Konzepte? Probieren Sie Übung 2!
🚀 Zu einfach? Versuchen Sie die Intermediate-Version!
💡 Eigene Ideen? Erweitern Sie das Programm!
"""
