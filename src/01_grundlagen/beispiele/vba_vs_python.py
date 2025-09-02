#!/usr/bin/env python3
"""
vba_vs_python.py - Vergleich zwischen VBA und Python

Dieses Programm demonstriert praktische Unterschiede zwischen VBA und Python
mit Fokus auf Datenverarbeitung und moderne Programmierkonzepte.
"""

import datetime
from typing import List, Dict, Any

def demonstriere_listen():
    """Zeigt erweiterte Listenoperationen in Python"""
    print("=== Listen in Python (vs. VBA Arrays) ===")
    
    # Einfache Liste erstellen
    zahlen = [1, 2, 3, 4, 5]
    print(f"Original Liste: {zahlen}")
    
    # Dynamisch erweitern (in VBA kompliziert mit ReDim Preserve)
    zahlen.append(6)
    zahlen.extend([7, 8, 9])
    print(f"Nach Erweiterung: {zahlen}")
    
    # List Comprehensions (in VBA nicht möglich)
    quadrate = [x**2 for x in zahlen]
    print(f"Quadrate: {quadrate}")
    
    # Filtern mit Bedingungen
    gerade = [x for x in zahlen if x % 2 == 0]
    ungerade = [x for x in zahlen if x % 2 == 1]
    print(f"Gerade Zahlen: {gerade}")
    print(f"Ungerade Zahlen: {ungerade}")
    
    # Mathematische Operationen
    summe = sum(zahlen)
    durchschnitt = sum(zahlen) / len(zahlen)
    maximum = max(zahlen)
    minimum = min(zahlen)
    
    print(f"Summe: {summe}, Ø: {durchschnitt:.2f}, Max: {maximum}, Min: {minimum}")

def demonstriere_dictionaries():
    """Zeigt Dictionary-Operationen (bessere Alternative zu VBA Collections)"""
    print("\n=== Dictionaries in Python (vs. VBA Collections) ===")
    
    # Mitarbeiterdaten (strukturierter als VBA Collections)
    mitarbeiter = {
        "M001": {
            "name": "Max Mustermann",
            "abteilung": "IT",
            "gehalt": 60000,
            "einstellungsdatum": "2020-01-15",
            "skills": ["Python", "VBA", "SQL"]
        },
        "M002": {
            "name": "Anna Schmidt",
            "abteilung": "Sales", 
            "gehalt": 55000,
            "einstellungsdatum": "2019-03-10",
            "skills": ["Excel", "PowerPoint", "CRM"]
        },
        "M003": {
            "name": "Tom Weber",
            "abteilung": "IT",
            "gehalt": 65000,
            "einstellungsdatum": "2018-09-01",
            "skills": ["Python", "JavaScript", "Docker"]
        }
    }
    
    print(f"Anzahl Mitarbeiter: {len(mitarbeiter)}")
    
    # IT-Mitarbeiter filtern (in VBA sehr umständlich)
    it_mitarbeiter = {
        emp_id: daten for emp_id, daten in mitarbeiter.items() 
        if daten["abteilung"] == "IT"
    }
    print(f"IT-Mitarbeiter: {len(it_mitarbeiter)} von {len(mitarbeiter)}")
    
    # Durchschnittsgehalt berechnen
    gehaelter = [daten["gehalt"] for daten in mitarbeiter.values()]
    durchschnittsgehalt = sum(gehaelter) / len(gehaelter)
    print(f"Durchschnittsgehalt: €{durchschnittsgehalt:,.2f}")
    
    # Python-Skills zählen
    python_entwickler = [
        daten["name"] for daten in mitarbeiter.values()
        if "Python" in daten["skills"]
    ]
    print(f"Python-Entwickler: {python_entwickler}")

def demonstriere_funktionen():
    """Zeigt moderne Funktionsdefinitionen mit Type Hints"""
    print("\n=== Funktionen mit Type Hints ===")
    
    def berechne_nettogehalt(bruttogehalt: float, steuersatz: float = 0.3) -> float:
        """
        Berechnet das Nettogehalt nach Steuerabzug
        
        Args:
            bruttogehalt: Bruttogehalt in Euro
            steuersatz: Steuersatz als Dezimalzahl (default: 0.3 = 30%)
            
        Returns:
            Nettogehalt nach Steuerabzug
        """
        return bruttogehalt * (1 - steuersatz)
    
    def analysiere_gehaltsstruktur(mitarbeiter_daten: Dict[str, Dict[str, Any]]) -> Dict[str, float]:
        """Analysiert die Gehaltsstruktur einer Mitarbeitergruppe"""
        gehaelter = [daten["gehalt"] for daten in mitarbeiter_daten.values()]
        
        return {
            "minimum": min(gehaelter),
            "maximum": max(gehaelter),
            "durchschnitt": sum(gehaelter) / len(gehaelter),
            "median": sorted(gehaelter)[len(gehaelter) // 2]
        }
    
    # Beispielverwendung
    beispiel_gehalt = 60000
    netto = berechne_nettogehalt(beispiel_gehalt)
    print(f"Brutto: €{beispiel_gehalt:,} → Netto: €{netto:,.2f}")

def demonstriere_fehlerbehandlung():
    """Zeigt professionelle Fehlerbehandlung"""
    print("\n=== Fehlerbehandlung (Try/Except) ===")
    
    def sichere_division(a: float, b: float) -> float:
        """Führt eine Division mit Fehlerbehandlung durch"""
        try:
            result = a / b
            return result
        except ZeroDivisionError:
            print(f"Fehler: Division durch Null! ({a} / {b})")
            return float('inf')
        except TypeError as e:
            print(f"Fehler: Ungültige Datentypen! {e}")
            return 0.0
    
    # Beispiele
    print(f"10 / 2 = {sichere_division(10, 2)}")
    print(f"10 / 0 = {sichere_division(10, 0)}")
    
def demonstriere_datetime():
    """Zeigt Datum/Zeit-Handling (besser als VBA)"""
    print("\n=== Datum und Zeit ===")
    
    heute = datetime.date.today()
    jetzt = datetime.datetime.now()
    
    print(f"Heute: {heute}")
    print(f"Jetzt: {jetzt.strftime('%d.%m.%Y %H:%M:%S')}")
    
    # Berechnung von Zeiträumen
    einstellungsdatum = datetime.date(2020, 1, 15)
    dienstzeit = heute - einstellungsdatum
    
    print(f"Dienstzeit seit {einstellungsdatum}: {dienstzeit.days} Tage")
    print(f"Das sind ca. {dienstzeit.days / 365:.1f} Jahre")

def vba_vs_python_vergleich():
    """Direkter Vergleich häufiger Aufgaben"""
    print("\n" + "="*60)
    print("VBA vs Python - Direkte Vergleiche")
    print("="*60)
    
    vergleiche = [
        {
            "aufgabe": "Array/Liste erstellen",
            "vba": "Dim arr(1 to 5) As Integer\narr(1) = 1: arr(2) = 2 ...",
            "python": "zahlen = [1, 2, 3, 4, 5]"
        },
        {
            "aufgabe": "Element hinzufügen", 
            "vba": "ReDim Preserve arr(1 to 6)\narr(6) = 6",
            "python": "zahlen.append(6)"
        },
        {
            "aufgabe": "Filtern",
            "vba": "For i = 1 to UBound(arr)\n  If arr(i) Mod 2 = 0 Then...",
            "python": "gerade = [x for x in zahlen if x % 2 == 0]"
        },
        {
            "aufgabe": "Dateien lesen",
            "vba": "Open \"file.txt\" For Input As #1\nLine Input #1, zeile",
            "python": "with open('file.txt') as f:\n    zeilen = f.readlines()"
        }
    ]
    
    for i, vergleich in enumerate(vergleiche, 1):
        print(f"\n{i}. {vergleich['aufgabe']}:")
        print(f"   VBA:    {vergleich['vba']}")
        print(f"   Python: {vergleich['python']}")

def main():
    """Hauptfunktion - führt alle Demonstrationen aus"""
    print("VBA vs Python - Praktische Vergleiche für Bystronic-Entwickler")
    print("=" * 70)
    
    demonstriere_listen()
    demonstriere_dictionaries()
    demonstriere_funktionen()
    demonstriere_fehlerbehandlung()
    demonstriere_datetime()
    vba_vs_python_vergleich()
    
    print("\n" + "="*70)
    print("FAZIT: Python bietet...")
    print("✅ Elegantere Syntax")
    print("✅ Mächtigere Datenstrukturen") 
    print("✅ Bessere Fehlerbehandlung")
    print("✅ Riesiges Ökosystem von Libraries")
    print("✅ Plattformunabhängigkeit")
    print("✅ Moderne Entwicklungstools")
    print("="*70)

if __name__ == "__main__":
    main()