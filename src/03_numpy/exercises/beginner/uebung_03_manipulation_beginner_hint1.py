#!/usr/bin/env python3
"""
🟢 BEGINNER - NumPy Array-Manipulation - HINT 1 (Subtile Hinweise)
Übung 3: Array-Manipulation für SmartFactory Produktionsdaten

🎯 KONZEPTUELLE HINWEISE (ohne Code-Beispiele):

📋 AUFGABE 1 - Reshape und Transpose:
💡 Hinweise:
- Arrays haben verschiedene "Formen" - denke an Tabellen mit Zeilen/Spalten
- reshape() verändert nur die Anzeige, nicht die Daten selbst
- Die Gesamtzahl der Elemente muss gleich bleiben (3×24 = 72)
- Transpose macht aus Zeilen Spalten und umgekehrt

📋 AUFGABE 2 - Arrays kombinieren:
💡 Hinweise:
- Arrays können horizontal oder vertikal "geklebt" werden
- Denke an das Zusammenfügen von Excel-Tabellen
- Die Dimensionen müssen kompatibel sein
- axis=0 bedeutet "entlang der Zeilen", axis=1 "entlang der Spalten"

📋 AUFGABE 3 - Boolean Indexing:
💡 Hinweise:
- Arrays können mit Bedingungen gefiltert werden
- Vergleiche erstellen "Masken" aus True/False Werten
- Diese Masken können direkt zum Indexieren verwendet werden
- Mehrere Bedingungen können mit & (und) oder | (oder) verknüpft werden

📋 AUFGABE 4 - Erweiterte Manipulation:
💡 Hinweise:
- Arrays können in gleichgroße Teile aufgesplit werden
- Daten können nach verschiedenen Kriterien sortiert werden
- Eindeutige Werte lassen sich einfach finden
- Statistische Operationen funktionieren entlang verschiedener Achsen

🎯 DENKANSÄTZE:
1. Überlege dir die gewünschte Zielform BEVOR du umformst
2. Visualisiere deine Daten als Tabelle oder Matrix
3. Teste mit kleinen Beispielen zuerst
4. Nutze print() um die Shapes zu überprüfen

🏭 BYSTRONIC-ANWENDUNG:
- Maschinendaten verschiedener Formate zusammenführen
- Produktionsdaten nach Kriterien filtern (Qualität, Zeit, etc.)
- Schichtdaten für Reports umstrukturieren
- Anomalien in Messdaten identifizieren
"""


def subtile_hinweise():
    """Subtile konzeptuelle Hinweise ohne direkten Code"""
    print("=" * 60)
    print("🟢 HINT 1: Konzeptuelle Denkansätze")
    print("=" * 60)

    print("🧠 DENKPROZESS für Array-Manipulation:")
    print("1. Was ist meine Ausgangsform?")
    print("2. Was ist meine gewünschte Zielform?")
    print("3. Welche Achse soll verändert werden?")
    print("4. Bleiben alle Daten erhalten?")
    print()

    print("💭 WICHTIGE KONZEPTE:")
    print("• Shape = die 'Form' deiner Daten (Zeilen × Spalten)")
    print("• Axis = die Richtung der Operation (0=Zeilen, 1=Spalten)")
    print("• Boolean Mask = Filter aus True/False Werten")
    print("• Broadcasting = automatische Größenanpassung")
    print()

    print("🎯 LÖSUNGSSTRATEGIEN:")
    print("• Kleine Testdaten verwenden")
    print("• Shapes vor und nach Operationen prüfen")
    print("• Eine Operation nach der anderen")
    print("• Visualisierung der Datenstruktur")


if __name__ == "__main__":
    subtile_hinweise()
