#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Beispiel: VBA vs NumPy Vergleich

Dieses Skript zeigt den direkten Vergleich zwischen VBA-Code
und NumPy-Code für typische numerische Berechnungen.
"""

import time

import numpy as np


def main() -> None:
    print("=" * 70)
    print("BYSTRONIC - VBA vs NUMPY VERGLEICH")
    print("=" * 70)

    # 1. Arrays erstellen und mit Werten füllen
    print("\n1️⃣ Arrays erstellen und füllen")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: Array deklarieren und füllen
    Dim zahlen(1 To 1000) As Double
    Dim i As Integer

    For i = 1 To 1000
        zahlen(i) = i * 0.5
    Next i
    """
    )

    print("NumPy-Code:")
    print("zahlen = np.arange(1, 1001) * 0.5")

    # NumPy-Implementierung
    zahlen = np.arange(1, 1001) * 0.5
    print(f"Ergebnis: {zahlen[:5]}... (erste 5 von {len(zahlen)})")

    # 2. Summe berechnen
    print("\n2️⃣ Summe aller Werte berechnen")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: Summe mit Schleife
    Dim summe As Double
    summe = 0

    For i = 1 To 1000
        summe = summe + zahlen(i)
    Next i
    """
    )

    print("NumPy-Code:")
    print("summe = np.sum(zahlen)")

    summe = np.sum(zahlen)
    print(f"Ergebnis: {summe}")

    # 3. Durchschnitt und Standardabweichung
    print("\n3️⃣ Statistische Berechnungen")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: Durchschnitt berechnen
    Dim durchschnitt As Double
    durchschnitt = summe / 1000

    ' VBA: Standardabweichung (sehr aufwendig!)
    Dim varianz As Double, stdAbw As Double
    varianz = 0

    For i = 1 To 1000
        varianz = varianz + (zahlen(i) - durchschnitt) ^ 2
    Next i

    varianz = varianz / 999  ' (n-1) für Stichprobe
    stdAbw = Sqr(varianz)
    """
    )

    print("NumPy-Code:")
    print(
        """
    durchschnitt = np.mean(zahlen)
    std_abweichung = np.std(zahlen, ddof=1)  # ddof=1 für Stichprobe
    """
    )

    durchschnitt = np.mean(zahlen)
    std_abweichung = np.std(zahlen, ddof=1)

    print(f"Durchschnitt: {durchschnitt}")
    print(f"Std.abweichung: {std_abweichung}")

    # 4. Konditionelle Operationen
    print("\n4️⃣ Konditionelle Operationen")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: Werte über 200 finden und zählen
    Dim anzahlGroß As Integer
    Dim großeWerte() As Double
    ReDim großeWerte(1 To 1000)  ' Maximal groß dimensionieren

    anzahlGroß = 0
    For i = 1 To 1000
        If zahlen(i) > 200 Then
            anzahlGroß = anzahlGroß + 1
            großeWerte(anzahlGroß) = zahlen(i)
        End If
    Next i

    ' Array auf tatsächliche Größe redimensionieren
    ReDim Preserve großeWerte(1 To anzahlGroß)
    """
    )

    print("NumPy-Code:")
    print(
        """
    große_werte = zahlen[zahlen > 200]
    anzahl_groß = len(große_werte)
    """
    )

    große_werte = zahlen[zahlen > 200]
    anzahl_groß = len(große_werte)

    print(f"Anzahl Werte > 200: {anzahl_groß}")
    print(f"Erste große Werte: {große_werte[:5]}")

    # 5. Matrix-Operationen
    print("\n5️⃣ Matrix-Operationen")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: 3x3 Matrix-Multiplikation (sehr aufwendig!)
    Dim matrix1(1 To 3, 1 To 3) As Double
    Dim matrix2(1 To 3, 1 To 3) As Double
    Dim result(1 To 3, 1 To 3) As Double
    Dim i As Integer, j As Integer, k As Integer

    ' Matrizen füllen...
    For i = 1 To 3
        For j = 1 To 3
            matrix1(i, j) = i + j
            matrix2(i, j) = i * j
        Next j
    Next i

    ' Matrix-Multiplikation
    For i = 1 To 3
        For j = 1 To 3
            result(i, j) = 0
            For k = 1 To 3
                result(i, j) = result(i, j) + matrix1(i, k) * matrix2(k, j)
            Next k
        Next j
    Next i
    """
    )

    print("NumPy-Code:")
    print(
        """
    matrix1 = np.array([[i+j for j in range(1, 4)] for i in range(1, 4)])
    matrix2 = np.array([[i*j for j in range(1, 4)] for i in range(1, 4)])
    result = matrix1 @ matrix2  # oder np.dot(matrix1, matrix2)
    """
    )

    matrix1 = np.array([[i + j for j in range(1, 4)] for i in range(1, 4)])
    matrix2 = np.array([[i * j for j in range(1, 4)] for i in range(1, 4)])
    result = matrix1 @ matrix2

    print("Matrix 1:")
    print(matrix1)
    print("Matrix 2:")
    print(matrix2)
    print("Produkt:")
    print(result)

    # 6. Trigonometrische Berechnungen
    print("\n6️⃣ Trigonometrische Berechnungen")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: Sinus-Werte für Array berechnen
    Dim winkel(1 To 360) As Double
    Dim sinusWerte(1 To 360) As Double
    Dim i As Integer

    For i = 1 To 360
        winkel(i) = i * (3.14159265 / 180)  ' Grad zu Radiant
        sinusWerte(i) = Sin(winkel(i))
    Next i
    """
    )

    print("NumPy-Code:")
    print(
        """
    winkel_grad = np.arange(1, 361)
    winkel_rad = np.radians(winkel_grad)
    sinus_werte = np.sin(winkel_rad)
    """
    )

    winkel_grad = np.arange(1, 361)
    winkel_rad = np.radians(winkel_grad)
    sinus_werte = np.sin(winkel_rad)

    print(f"Sinus-Werte berechnet für {len(sinus_werte)} Winkel")
    print(f"Sinus(30°) = {sinus_werte[29]:.3f}")  # Index 29 für 30°
    print(f"Sinus(90°) = {sinus_werte[89]:.3f}")  # Index 89 für 90°

    # 7. Produktionsdaten-Analyse
    print("\n7️⃣ Produktionsdaten-Analyse")
    print("-" * 50)

    print("VBA-Code:")
    print(
        """
    ' VBA: Maschinenlaufzeiten analysieren
    Dim laufzeiten(1 To 5) As Double
    Dim i As Integer
    Dim summe As Double, mittel As Double
    Dim maxWert As Double, minWert As Double

    laufzeiten(1) = 8.5: laufzeiten(2) = 7.2: laufzeiten(3) = 9.1
    laufzeiten(4) = 8.8: laufzeiten(5) = 7.9

    ' Summe und Mittelwert
    summe = 0
    For i = 1 To 5
        summe = summe + laufzeiten(i)
    Next i
    mittel = summe / 5

    ' Maximum und Minimum finden
    maxWert = laufzeiten(1)
    minWert = laufzeiten(1)
    For i = 2 To 5
        If laufzeiten(i) > maxWert Then maxWert = laufzeiten(i)
        If laufzeiten(i) < minWert Then minWert = laufzeiten(i)
    Next i
    """
    )

    print("NumPy-Code:")
    print(
        """
    laufzeiten = np.array([8.5, 7.2, 9.1, 8.8, 7.9])
    summe = np.sum(laufzeiten)
    mittel = np.mean(laufzeiten)
    max_wert = np.max(laufzeiten)
    min_wert = np.min(laufzeiten)
    """
    )

    laufzeiten = np.array([8.5, 7.2, 9.1, 8.8, 7.9])

    print(f"Laufzeiten: {laufzeiten}")
    print(f"Summe: {np.sum(laufzeiten)}")
    print(f"Mittelwert: {np.mean(laufzeiten):.2f}")
    print(f"Maximum: {np.max(laufzeiten)}")
    print(f"Minimum: {np.min(laufzeiten)}")

    # 8. Performance-Vergleich
    print("\n8️⃣ Performance-Vergleich")
    print("-" * 50)

    print("Simulierter Performance-Test (1000 Elemente):")
    print("(Zeiten sind approximiert basierend auf typischen VBA vs NumPy Performance)")

    test_daten = np.random.random(1000)

    # NumPy-Performance messen
    start_time = time.time()
    numpy_summe = np.sum(test_daten**2)
    numpy_mittel = np.mean(test_daten)
    numpy_std = np.std(test_daten)
    numpy_time = time.time() - start_time

    # VBA-äquivalente Performance simulieren (normalerweise 50-100x langsamer)
    vba_time_estimated = numpy_time * 75  # Geschätzter Faktor

    print(f"NumPy-Zeit:       {numpy_time:.6f} Sekunden")
    print(f"VBA-Zeit (est.):  {vba_time_estimated:.6f} Sekunden")
    print(f"Speedup-Faktor:   ~{vba_time_estimated / numpy_time:.0f}x schneller")

    print(
        f"Ergebnisse - Summe: {numpy_summe:.2f}, Mittel: {numpy_mittel:.3f}, Std: {numpy_std:.3f}"
    )

    # 9. Speicherverbrauch
    print("\n9️⃣ Speicherverbrauch und Effizienz")
    print("-" * 50)

    print("VBA:")
    print("- Jede Variable einzeln im Speicher")
    print("- Overhead durch Variant-Datentyp")
    print("- Keine Vektorisierung")
    print("- Speicher-Layout nicht optimiert")

    print("\nNumPy:")
    print("- Zusammenhängender Speicherblock")
    print("- Optimierte Datentypen (float64, int32, etc.)")
    print("- Vektorisierte Operationen")
    print("- Cache-freundliches Memory Layout")

    # Speicherverbrauch demonstrieren
    big_array = np.zeros(100000, dtype=np.float64)
    print(f"\nNumPy Array (100.000 float64): {big_array.nbytes / 1024:.1f} KB")
    print("VBA Array (100.000 Double): ~781 KB + Overhead")

    # 10. Code-Komplexität Vergleich
    print("\n🔟 Code-Komplexität Vergleich")
    print("-" * 50)

    print(
        "Aufgabe: Finde alle Werte zwischen 100 und 300, quadriere sie und berechne den Durchschnitt"
    )

    print("\nVBA-Code (~15 Zeilen):")
    print(
        """
    Dim i As Integer, count As Integer
    Dim tempArray() As Double
    Dim summe As Double, durchschnitt As Double

    ReDim tempArray(1 To UBound(zahlen))
    count = 0

    For i = 1 To UBound(zahlen)
        If zahlen(i) >= 100 And zahlen(i) <= 300 Then
            count = count + 1
            tempArray(count) = zahlen(i) * zahlen(i)
        End If
    Next i

    summe = 0
    For i = 1 To count
        summe = summe + tempArray(i)
    Next i
    durchschnitt = summe / count
    """
    )

    print("NumPy-Code (1 Zeile!):")
    print("durchschnitt = np.mean(zahlen[(zahlen >= 100) & (zahlen <= 300)] ** 2)")

    # NumPy-Implementierung
    gefilterte_werte = zahlen[(zahlen >= 100) & (zahlen <= 300)] ** 2
    durchschnitt_numpy = np.mean(gefilterte_werte)

    print(f"Ergebnis: {durchschnitt_numpy:.2f}")
    print(f"Anzahl gefilterte Werte: {len(gefilterte_werte)}")

    # 11. Fazit
    print("\n🎯 FAZIT: Warum NumPy besser ist")
    print("-" * 50)

    print("✅ Vorteile von NumPy gegenüber VBA:")
    print("   • 50-100x schneller bei numerischen Berechnungen")
    print("   • Deutlich weniger Code (kompakter und lesbarer)")
    print("   • Weniger fehleranfällig (keine manuellen Schleifen)")
    print("   • Speicher-effizienter")
    print("   • Viele vorgefertigte mathematische Funktionen")
    print("   • Bessere Integration mit anderen Python-Libraries")
    print("   • Vektorisierte Operationen (moderne CPU-Features)")

    print("\n⚠️  VBA ist noch sinnvoll für:")
    print("   • Excel-Integration und Automatisierung")
    print("   • Einfache Office-Makros")
    print("   • Bestehende VBA-Infrastruktur")

    print("\n🚀 NumPy ist optimal für:")
    print("   • Numerische Berechnungen und Simulationen")
    print("   • Datenanalyse und -verarbeitung")
    print("   • Wissenschaftliche Berechnungen")
    print("   • Machine Learning und KI")
    print("   • Große Datenmengen")

    print(f"\n{'=' * 70}")
    print("✅ VBA vs NumPy Vergleich abgeschlossen!")
    print("💡 NumPy ist die moderne Alternative für numerische Berechnungen")
    print("🔄 Migration von VBA zu Python/NumPy lohnt sich langfristig")


if __name__ == "__main__":
    main()
