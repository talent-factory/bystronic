#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Beispiel: Lineare Algebra mit NumPy

Dieses Skript demonstriert Matrix-Operationen und lineare Algebra
für geometrische Berechnungen und technische Anwendungen.
"""

import numpy as np
import numpy.linalg as la


def main() -> None:
    print("=" * 60)
    print("BYSTRONIC - LINEARE ALGEBRA MIT NUMPY")
    print("=" * 60)

    # 1. Matrix-Grundlagen
    print("\n1️⃣ Matrix-Grundlagen")
    print("-" * 40)

    # Transformationsmatrix für 2D-Rotation
    winkel = np.radians(30)  # 30 Grad in Radiant
    rotation_matrix = np.array(
        [[np.cos(winkel), -np.sin(winkel)], [np.sin(winkel), np.cos(winkel)]]
    )

    print("Rotationsmatrix (30°):")
    print(rotation_matrix)
    print(f"Shape: {rotation_matrix.shape}")
    print(f"Determinante: {la.det(rotation_matrix):.6f}")

    # Punkt rotieren
    punkt = np.array([10, 5])  # Originalkoordinate
    rotierter_punkt = rotation_matrix @ punkt  # Matrix-Multiplikation

    print(f"\nOriginal-Punkt:   ({punkt[0]}, {punkt[1]})")
    print(f"Rotierter Punkt:  ({rotierter_punkt[0]:.2f}, {rotierter_punkt[1]:.2f})")

    # 2. Matrix-Operationen
    print("\n2️⃣ Matrix-Operationen")
    print("-" * 40)

    # Maschinenkonfiguration als Matrix
    A = np.array([[2.5, 1.8, 0.5], [1.2, 3.0, 2.1], [0.8, 1.5, 2.8]])

    B = np.array([[1.0, 0.5, 1.2], [2.0, 1.8, 0.9], [0.7, 2.2, 1.1]])

    print("Matrix A:")
    print(A)
    print("Matrix B:")
    print(B)

    # Verschiedene Matrix-Operationen
    summe = A + B
    produkt = A @ B  # Matrix-Multiplikation
    element_produkt = A * B  # Element-weise Multiplikation

    print(f"\nA + B:\n{summe}")
    print(f"\nA @ B (Matrix-Multiplikation):\n{produkt}")
    print(f"\nA * B (Element-weise):\n{element_produkt}")

    # 3. Matrix-Eigenschaften
    print("\n3️⃣ Matrix-Eigenschaften")
    print("-" * 40)

    # Symmetrische Matrix erstellen
    sym_matrix = np.array([[4, 2, 1], [2, 5, 3], [1, 3, 6]])

    print("Symmetrische Matrix:")
    print(sym_matrix)

    # Eigenschaften berechnen
    determinante = la.det(sym_matrix)
    spur = np.trace(sym_matrix)  # Summe der Diagonalelemente
    rang = la.matrix_rank(sym_matrix)

    print(f"\nDeterminante:     {determinante:.3f}")
    print(f"Spur (Trace):     {spur}")
    print(f"Rang:             {rang}")
    print(f"Ist invertierbar: {'Ja' if determinante != 0 else 'Nein'}")

    # 4. Eigenwerte und Eigenvektoren
    print("\n4️⃣ Eigenwerte und Eigenvektoren")
    print("-" * 40)

    # Für Schwingungsanalyse oder Hauptkomponentenanalyse
    eigenwerte, eigenvektoren = la.eig(sym_matrix)

    print("Eigenwerte:")
    for i, wert in enumerate(eigenwerte):
        print(f"  λ{i + 1} = {wert:.3f}")

    print("\nEigenvektoren:")
    print(eigenvektoren)

    # Überprüfung: A * v = λ * v
    print("\nVerifikation für ersten Eigenvektor:")
    v1 = eigenvektoren[:, 0]
    lambda1 = eigenwerte[0]
    links = sym_matrix @ v1
    rechts = lambda1 * v1
    print(f"A @ v1 = {links}")
    print(f"λ1 * v1 = {rechts}")
    print(f"Differenz: {np.allclose(links, rechts)}")

    # 5. Lineare Gleichungssysteme lösen
    print("\n5️⃣ Lineare Gleichungssysteme")
    print("-" * 40)

    # Beispiel: Materialbilanzen in der Produktion
    # 3 Materialien (Stahl, Aluminium, Kunststoff)
    # 3 Produkte mit verschiedenen Materialanteilen

    material_matrix = np.array(
        [
            [2, 1, 0.5],  # Produkt 1: 2kg Stahl, 1kg Alu, 0.5kg Kunststoff
            [1, 3, 1],  # Produkt 2: 1kg Stahl, 3kg Alu, 1kg Kunststoff
            [0, 2, 2],  # Produkt 3: 0kg Stahl, 2kg Alu, 2kg Kunststoff
        ]
    )

    verfuegbare_materialien = np.array([500, 800, 300])  # Verfügbare Mengen

    print("Materialmatrix (Produkte x Materialien):")
    print(material_matrix)
    print(f"Verfügbare Materialien: {verfuegbare_materialien}")

    # Gleichungssystem lösen: A * x = b
    try:
        produktion = la.solve(material_matrix, verfuegbare_materialien)
        print("\nOptimale Produktionsmengen:")
        for i, menge in enumerate(produktion):
            print(f"  Produkt {i + 1}: {menge:.1f} Einheiten")

        # Verifikation
        verbrauch = material_matrix @ produktion
        print(f"\nMaterialverbrauch: {verbrauch}")
        print(f"Verfügbar:         {verfuegbare_materialien}")
        print(f"Lösung korrekt:    {np.allclose(verbrauch, verfuegbare_materialien)}")

    except la.LinAlgError:
        print("Gleichungssystem nicht eindeutig lösbar!")

    # 6. Matrix-Inversion
    print("\n6️⃣ Matrix-Inversion")
    print("-" * 40)

    # Kalibrierungsmatrix für Sensoren
    kalibrier_matrix = np.array(
        [[1.05, 0.02, -0.01], [0.01, 1.03, 0.02], [-0.02, 0.01, 1.04]]
    )

    print("Kalibrierungsmatrix:")
    print(kalibrier_matrix)

    # Inverse berechnen
    try:
        inverse = la.inv(kalibrier_matrix)
        print("\nInverse Matrix:")
        print(inverse)

        # Verifikation: A * A^-1 = I (Einheitsmatrix)
        einheitsmatrix = kalibrier_matrix @ inverse
        print("\nA @ A^-1 (sollte Einheitsmatrix sein):")
        print(einheitsmatrix)

        # Numerische Präzision prüfen
        identitaet = np.eye(3)
        print(f"Ist Einheitsmatrix: {np.allclose(einheitsmatrix, identitaet)}")

    except la.LinAlgError:
        print("Matrix ist nicht invertierbar!")

    # 7. QR-Zerlegung
    print("\n7️⃣ QR-Zerlegung")
    print("-" * 40)

    # Für Least-Squares-Probleme
    messmatrix = np.array(
        [[1, 2, 1], [2, 1, 3], [3, 1, 2], [1, 3, 1]]
    )  # Überbestimmtes System (4 Gleichungen, 3 Unbekannte)

    Q, R = la.qr(messmatrix)

    print(f"Messmatrix Shape: {messmatrix.shape}")
    print(f"Q Shape: {Q.shape} (orthogonal)")
    print(f"R Shape: {R.shape} (obere Dreiecksmatrix)")

    print("\nQ (orthogonale Matrix):")
    print(Q)
    print("\nR (obere Dreiecksmatrix):")
    print(R)

    # Verifikation: Q @ R = A
    rekonstruiert = Q @ R
    print(f"\nRekonstruktion korrekt: {np.allclose(messmatrix, rekonstruiert)}")

    # 8. Singulärwertzerlegung (SVD)
    print("\n8️⃣ Singulärwertzerlegung (SVD)")
    print("-" * 40)

    # Datenmatrix für Dimensionsreduktion
    datenmatrix = np.array([[4, 2, 1, 0], [2, 4, 3, 1], [1, 3, 4, 2], [0, 1, 2, 4]])

    U, s, Vt = la.svd(datenmatrix)

    print(f"Datenmatrix Shape: {datenmatrix.shape}")
    print(f"U Shape: {U.shape}")
    print(f"Singulärwerte s: {s}")
    print(f"Vt Shape: {Vt.shape}")

    # Rang der Matrix
    toleranz = 1e-10
    rang_svd = np.sum(s > toleranz)
    print(f"Rang (via SVD): {rang_svd}")

    # Rekonstruktion
    S_matrix = np.diag(s)
    rekonstruiert_svd = U @ S_matrix @ Vt
    print(f"SVD-Rekonstruktion korrekt: {np.allclose(datenmatrix, rekonstruiert_svd)}")

    # 9. Geometrische Anwendungen
    print("\n9️⃣ Geometrische Anwendungen")
    print("-" * 40)

    # Koordinatentransformation für CNC-Programmierung
    # Originalpunkte
    punkte_2d = np.array([[0, 0], [10, 0], [10, 5], [5, 8], [0, 5]])

    print("Original-Koordinaten:")
    print(punkte_2d)

    # Transformation: Rotation + Translation
    rotationswinkel = np.radians(45)  # 45 Grad
    translation = np.array([20, 15])  # Verschiebung

    # Rotationsmatrix
    R = np.array(
        [
            [np.cos(rotationswinkel), -np.sin(rotationswinkel)],
            [np.sin(rotationswinkel), np.cos(rotationswinkel)],
        ]
    )

    # Transformation anwenden
    rotierte_punkte = (R @ punkte_2d.T).T  # Transponierung für korrekte Multiplikation
    transformierte_punkte = rotierte_punkte + translation

    print("\nNach 45° Rotation:")
    print(rotierte_punkte)
    print(f"Nach Translation (+{translation}):")
    print(transformierte_punkte)

    # Abstände berechnen
    ursprungsabstaende = la.norm(punkte_2d, axis=1)
    neue_abstaende = la.norm(transformierte_punkte, axis=1)

    print(f"\nUrsprungs-Abstände:     {ursprungsabstaende}")
    print(f"Neue Abstände:          {neue_abstaende}")

    # 10. Praktisches Beispiel: Kraftberechnung
    print("\n🔟 Praktisches Beispiel: Kraftverteilung")
    print("-" * 50)

    # 3 Stützpunkte mit verschiedenen Steifigkeiten
    steifigkeitsmatrix = np.array(
        [
            [1000, -200, 0],  # Stützpunkt 1
            [-200, 1500, -300],  # Stützpunkt 2 (gekoppelt)
            [0, -300, 800],  # Stützpunkt 3
        ]
    )

    externe_kraefte = np.array([500, 800, 300])  # N

    print("Steifigkeitsmatrix (N/mm):")
    print(steifigkeitsmatrix)
    print(f"Externe Kräfte (N): {externe_kraefte}")

    # Verformungen berechnen: K * x = F
    try:
        verformungen = la.solve(steifigkeitsmatrix, externe_kraefte)
        print(f"\nVerformungen (mm): {verformungen}")

        # Reaktionskräfte in den Stützpunkten
        reaktionskraefte = steifigkeitsmatrix @ verformungen
        print(f"Reaktionskräfte (N): {reaktionskraefte}")

        # Maximale Verformung
        max_verformung = np.max(np.abs(verformungen))
        max_position = np.argmax(np.abs(verformungen))
        print(
            f"Maximale Verformung: {max_verformung:.3f} mm an Position {max_position + 1}"
        )

    except la.LinAlgError:
        print("Steifigkeitsmatrix ist singulär!")

    print(f"\n{'=' * 60}")
    print("✅ Lineare Algebra erfolgreich demonstriert!")
    print("🔧 Matrix-Operationen sind essentiell für technische Berechnungen")
    print("📐 Geometrische Transformationen und Kraftberechnungen vereinfacht")


if __name__ == "__main__":
    main()
