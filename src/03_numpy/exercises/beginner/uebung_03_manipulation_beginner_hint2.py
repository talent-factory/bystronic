#!/usr/bin/env python3
"""
🟢 BEGINNER - NumPy Array-Manipulation - HINT 2 (Konkrete Ansätze)
Übung 3: Array-Manipulation für Bystronic Produktionsdaten

🎯 KONKRETE STRATEGIEN mit Pseudo-Code:

📋 AUFGABE 1 - Reshape und Transpose:
🔧 Lösungsansatz:
```python
# Pseudo-Code:
original_array = np.arange(1, 73)  # 72 Elemente
# Umformen zu 3×24:
reshaped = original_array.reshape(neue_zeilen, neue_spalten)
# Transponieren:
transposed = reshaped.T  # oder .transpose()
```

📋 AUFGABE 2 - Arrays kombinieren:
🔧 Lösungsansatz:
```python
# Pseudo-Code:
array1 = [Tag 1 Daten]
array2 = [Tag 2 Daten]
# Horizontal kombinieren:
combined_horizontal = np.concatenate([array1, array2], axis=1)
# Vertikal kombinieren:
combined_vertical = np.concatenate([array1, array2], axis=0)
```

📋 AUFGABE 3 - Boolean Indexing:
🔧 Lösungsansatz:
```python
# Pseudo-Code:
daten = [Produktionswerte]
# Bedingung erstellen:
bedingung = daten > schwellwert
# Filtern:
gefilterte_daten = daten[bedingung]
# Mehrere Bedingungen:
mehrfach_bedingung = (daten > min_wert) & (daten < max_wert)
```

📋 AUFGABE 4 - Erweiterte Manipulation:
🔧 Lösungsansatz:
```python
# Pseudo-Code:
# Aufteilen:
teile = np.split(array, anzahl_teile)
# Sortieren:
sortiert = np.sort(array)
# Eindeutige Werte:
eindeutig = np.unique(array)
# Statistiken pro Achse:
mittelwert_pro_spalte = np.mean(array, axis=0)
```

🎯 IMPLEMENTIERUNGSSTRATEGIE:
1. Beginne mit der einfachsten Teilaufgabe
2. Teste jeden Schritt einzeln
3. Verwende aussagekräftige Variablennamen
4. Überprüfe Shapes nach jeder Operation

🏭 PRAXISBEISPIELE:
- Stündliche → Tägliche Produktionsdaten umformen
- Maschinendaten verschiedener Schichten zusammenfassen
- Ausreißer in Qualitätsmessungen identifizieren
- Produktionsberichte für verschiedene Zeiträume erstellen
"""


def konkrete_ansaetze():
    """Konkrete Lösungsansätze mit Pseudo-Code"""
    print("=" * 60)
    print("🟢 HINT 2: Konkrete Lösungsstrategien")
    print("=" * 60)

    print("🔧 RESHAPE-STRATEGIE:")
    print("• Zielform berechnen: Gesamtelemente / neue_dimension")
    print("• Beispiel: 72 Elemente → 3×24 oder 24×3")
    print("• reshape(neue_zeilen, neue_spalten)")
    print("• oder reshape(-1, neue_spalten) für automatische Berechnung")
    print()

    print("🔧 CONCATENATE-STRATEGIE:")
    print("• axis=0: Untereinander stapeln (mehr Zeilen)")
    print("• axis=1: Nebeneinander fügen (mehr Spalten)")
    print("• Arrays müssen kompatible Dimensionen haben")
    print("• Alternative: np.vstack(), np.hstack()")
    print()

    print("🔧 BOOLEAN-INDEXING-STRATEGIE:")
    print("• Schritt 1: Bedingung formulieren (array > wert)")
    print("• Schritt 2: Boolean-Mask erhalten (True/False Array)")
    print("• Schritt 3: Mask zum Filtern verwenden (array[mask])")
    print("• Mehrere Bedingungen: & (und), | (oder), ~ (nicht)")
    print()

    print("🔧 PRAKTISCHE TIPPS:")
    print("• Verwende aussagekräftige Variablennamen")
    print("• Teste mit kleinen Arrays zuerst")
    print("• Nutze .shape für Größenkontrollen")
    print("• Dokumentiere deine Datenstruktur")


def beispiel_datenfluss():
    """Zeigt den typischen Datenfluss bei Array-Manipulation"""
    print("\n🔄 TYPISCHER DATENFLUSS:")
    print("1. Rohdaten laden/generieren")
    print("2. Form überprüfen (.shape)")
    print("3. Umformen (reshape/transpose)")
    print("4. Kombinieren/Aufteilen")
    print("5. Filtern (boolean indexing)")
    print("6. Analysieren/Statistiken")
    print("7. Ergebnis validieren")


if __name__ == "__main__":
    konkrete_ansaetze()
    beispiel_datenfluss()
