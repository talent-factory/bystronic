#!/usr/bin/env python3
"""
Übung 2: Einfacher Taschenrechner

Aufgabe:
1. Erstellen Sie Funktionen für die Grundrechenarten (+, -, *, /)
2. Implementieren Sie ein Menü zur Auswahl der Operation
3. Fragen Sie nach zwei Zahlen
4. Führen Sie die Berechnung durch und zeigen Sie das Ergebnis an
5. BONUS: Behandeln Sie Division durch Null
6. BONUS: Erweitern Sie um weitere Operationen (%, **, sqrt)

TIPP: Verwenden Sie try/except für Fehlerbehandlung
"""

import math

def addition(a: float, b: float) -> float:
    """
    TODO: Implementieren Sie die Addition
    
    Args:
        a: Erste Zahl
        b: Zweite Zahl
        
    Returns:
        Summe von a und b
    """
    # Ihre Implementierung hier:
    pass

def subtraktion(a: float, b: float) -> float:
    """TODO: Implementieren Sie die Subtraktion"""
    # Ihre Implementierung hier:
    pass

def multiplikation(a: float, b: float) -> float:
    """TODO: Implementieren Sie die Multiplikation"""
    # Ihre Implementierung hier:
    pass

def division(a: float, b: float) -> float:
    """
    TODO: Implementieren Sie die Division mit Fehlerbehandlung
    
    WICHTIG: Behandeln Sie Division durch Null!
    """
    # Ihre Implementierung hier:
    pass

# BONUS-Funktionen
def modulo(a: float, b: float) -> float:
    """TODO: Implementieren Sie den Modulo-Operator (Rest der Division)"""
    pass

def potenz(a: float, b: float) -> float:
    """TODO: Implementieren Sie die Potenzierung (a hoch b)"""
    pass

def quadratwurzel(a: float) -> float:
    """
    TODO: Implementieren Sie die Quadratwurzel
    TIPP: Verwenden Sie math.sqrt() oder a ** 0.5
    Behandeln Sie negative Zahlen!
    """
    pass

def zeige_menu() -> None:
    """
    TODO: Zeigen Sie ein übersichtliches Menü mit allen verfügbaren Operationen
    
    Beispiel:
    ========================================
    🧮 BYSTRONIC TASCHENRECHNER
    ========================================
    1. Addition (+)
    2. Subtraktion (-)
    ...
    """
    # Ihre Implementierung hier:
    pass

def hole_zahl(prompt: str) -> float:
    """
    TODO: Sicher eine Zahl vom Benutzer einlesen
    
    Behandeln Sie ungültige Eingaben mit try/except!
    
    Args:
        prompt: Text für die Eingabeaufforderung
        
    Returns:
        Die eingegebene Zahl als float
    """
    # Ihre Implementierung hier:
    pass

def waehle_operation() -> str:
    """
    TODO: Lassen Sie den Benutzer eine Operation wählen
    
    Returns:
        Die gewählte Operation als String ('1', '2', etc.)
    """
    # Ihre Implementierung hier:
    pass

def fuehre_berechnung_aus(operation: str, a: float, b: float = None) -> None:
    """
    TODO: Führen Sie die gewählte Berechnung aus und zeigen Sie das Ergebnis
    
    Args:
        operation: Die gewählte Operation ('1', '2', etc.)
        a: Erste Zahl
        b: Zweite Zahl (optional für einstellige Operationen wie sqrt)
    """
    # Ihre Implementierung hier:
    pass

def main():
    """
    Hauptfunktion - Implementiert die Taschenrechner-Logik
    """
    print("Willkommen beim Bystronic Taschenrechner! 🧮")
    print()
    
    while True:
        # TODO: Implementieren Sie die Hauptschleife:
        # 1. Menü anzeigen
        # 2. Operation wählen
        # 3. Zahlen eingeben
        # 4. Berechnung durchführen
        # 5. Fragen ob weiter gemacht werden soll
        
        # Ihre Implementierung hier:
        
        # Zum Testen können Sie diese Zeile verwenden:
        break  # Entfernen Sie diese Zeile in Ihrer Implementierung
    
    print("Auf Wiedersehen! 👋")

# Lösungsvorschläge (auskommentiert):
"""
def addition(a: float, b: float) -> float:
    return a + b

def subtraktion(a: float, b: float) -> float:
    return a - b

def multiplikation(a: float, b: float) -> float:
    return a * b

def division(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division durch Null ist nicht erlaubt!")
    return a / b

def modulo(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Modulo durch Null ist nicht erlaubt!")
    return a % b

def potenz(a: float, b: float) -> float:
    return a ** b

def quadratwurzel(a: float) -> float:
    if a < 0:
        raise ValueError("Quadratwurzel aus negativer Zahl ist nicht erlaubt!")
    return math.sqrt(a)

def zeige_menu() -> None:
    print("\\n" + "="*50)
    print("🧮 BYSTRONIC TASCHENRECHNER")
    print("="*50)
    print("1. Addition (+)")
    print("2. Subtraktion (-)")
    print("3. Multiplikation (×)")
    print("4. Division (÷)")
    print("5. Modulo (%)")
    print("6. Potenz (^)")
    print("7. Quadratwurzel (√)")
    print("0. Beenden")
    print("="*50)

def hole_zahl(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ Ungültige Eingabe! Bitte geben Sie eine Zahl ein.")

def waehle_operation() -> str:
    while True:
        wahl = input("Wählen Sie eine Operation (0-7): ")
        if wahl in ['0', '1', '2', '3', '4', '5', '6', '7']:
            return wahl
        print("❌ Ungültige Auswahl! Bitte wählen Sie 0-7.")

def fuehre_berechnung_aus(operation: str, a: float, b: float = None) -> None:
    try:
        if operation == '1':
            resultat = addition(a, b)
            print(f"➡️  {a} + {b} = {resultat}")
        elif operation == '2':
            resultat = subtraktion(a, b)
            print(f"➡️  {a} - {b} = {resultat}")
        elif operation == '3':
            resultat = multiplikation(a, b)
            print(f"➡️  {a} × {b} = {resultat}")
        elif operation == '4':
            resultat = division(a, b)
            print(f"➡️  {a} ÷ {b} = {resultat}")
        elif operation == '5':
            resultat = modulo(a, b)
            print(f"➡️  {a} % {b} = {resultat}")
        elif operation == '6':
            resultat = potenz(a, b)
            print(f"➡️  {a}^{b} = {resultat}")
        elif operation == '7':
            resultat = quadratwurzel(a)
            print(f"➡️  √{a} = {resultat}")
    except ValueError as e:
        print(f"❌ Fehler: {e}")
    except Exception as e:
        print(f"❌ Unerwarteter Fehler: {e}")
"""

if __name__ == "__main__":
    main()