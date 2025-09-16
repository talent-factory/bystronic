#!/usr/bin/env python3
"""
Bystronic Python Grundkurs - Kapitel 3
Übung 4: Lineare Algebra mit NumPy

Diese Übung behandelt lineare Algebra für technische Anwendungen:
- Matrix-Operationen und Eigenschaften
- Lineare Gleichungssysteme
- Geometrische Transformationen
- Eigenwerte und Eigenvektoren
- Least-Squares-Probleme
"""

import numpy as np
import numpy.linalg as la


def uebung_4_1() -> None:
    """Übung 4.1: Matrix-Grundoperationen"""
    print("=" * 60)
    print("ÜBUNG 4.1: Matrix-Grundoperationen")
    print("=" * 60)

    # Materialbedarfsmatrizen für verschiedene Produkte
    # Zeilen: Materialien (Stahl, Alu, Kunststoff)
    # Spalten: Produkte (A, B, C)
    material_pro_stueck = np.array(
        [
            [2.5, 1.8, 0.0],  # Stahl kg/Stück
            [0.0, 3.2, 2.1],  # Aluminium kg/Stück
            [0.5, 0.7, 1.8],  # Kunststoff kg/Stück
        ]
    )

    # Materialkosten pro kg
    materialkosten = np.array(
        [
            [3.20],  # Euro/kg Stahl
            [5.80],  # Euro/kg Aluminium
            [2.40],  # Euro/kg Kunststoff
        ]
    )

    print("Material pro Stück (kg):")
    print("        Prod.A  Prod.B  Prod.C")
    print(
        f"Stahl    {material_pro_stueck[0, 0]:5.1f}   {material_pro_stueck[0, 1]:5.1f}   {material_pro_stueck[0, 2]:5.1f}"
    )
    print(
        f"Alu      {material_pro_stueck[1, 0]:5.1f}   {material_pro_stueck[1, 1]:5.1f}   {material_pro_stueck[1, 2]:5.1f}"
    )
    print(
        f"Kunst.   {material_pro_stueck[2, 0]:5.1f}   {material_pro_stueck[2, 1]:5.1f}   {material_pro_stueck[2, 2]:5.1f}"
    )

    print(f"\nMaterialkosten: {materialkosten.flatten()}")

    # TODO: Führen Sie Matrix-Operationen durch

    # a) Berechnen Sie die Materialkosten pro Stück (Matrix-Multiplikation)
    kosten_pro_stueck = materialkosten.T @ material_pro_stueck
    print("\na) Materialkosten pro Stück:")
    print(f"   Produkt A: {kosten_pro_stueck[0, 0]:.2f} €")
    print(f"   Produkt B: {kosten_pro_stueck[0, 1]:.2f} €")
    print(f"   Produkt C: {kosten_pro_stueck[0, 2]:.2f} €")

    # b) Transponieren Sie die Materialmatrix
    material_transponiert = material_pro_stueck.T
    print("\nb) Transponierte Matrix (Produkte x Materialien):")
    print("         Stahl   Alu   Kunst.")
    for i, prod in enumerate(["Prod.A", "Prod.B", "Prod.C"]):
        print(
            f"{prod}    {material_transponiert[i, 0]:5.1f}  {material_transponiert[i, 1]:5.1f}   {material_transponiert[i, 2]:5.1f}"
        )

    # c) Produktionsplan: 100, 150, 80 Stück von A, B, C
    produktionsplan = np.array([100, 150, 80])
    gesamter_materialbedarf = material_pro_stueck @ produktionsplan

    print(f"\nc) Gesamter Materialbedarf bei Produktion {produktionsplan}:")
    print(f"   Stahl: {gesamter_materialbedarf[0]:.1f} kg")
    print(f"   Aluminium: {gesamter_materialbedarf[1]:.1f} kg")
    print(f"   Kunststoff: {gesamter_materialbedarf[2]:.1f} kg")

    # d) Gesamte Materialkosten
    gesamtkosten = materialkosten.T @ gesamter_materialbedarf
    print(f"\nd) Gesamte Materialkosten: {gesamtkosten[0]:.2f} €")

    # e) Element-weise Operationen: 10% Kostensteigerung
    neue_kosten = materialkosten * 1.1
    neue_kosten_pro_stueck = neue_kosten.T @ material_pro_stueck

    print("\ne) Nach 10% Kostensteigerung:")
    print(
        f"   Produkt A: {neue_kosten_pro_stueck[0, 0]:.2f} € ({neue_kosten_pro_stueck[0, 0] / kosten_pro_stueck[0, 0] * 100 - 100:+.1f}%)"
    )
    print(
        f"   Produkt B: {neue_kosten_pro_stueck[0, 1]:.2f} € ({neue_kosten_pro_stueck[0, 1] / kosten_pro_stueck[0, 1] * 100 - 100:+.1f}%)"
    )
    print(
        f"   Produkt C: {neue_kosten_pro_stueck[0, 2]:.2f} € ({neue_kosten_pro_stueck[0, 2] / kosten_pro_stueck[0, 2] * 100 - 100:+.1f}%)"
    )


def uebung_4_2() -> None:
    """Übung 4.2: Lineare Gleichungssysteme"""
    print("\n" + "=" * 60)
    print("ÜBUNG 4.2: Lineare Gleichungssysteme")
    print("=" * 60)

    # Problemstellung: Ressourcenverteilung
    # 3 Maschinen, 3 Ressourcen (Strom, Druckluft, Kühlwasser)
    # Jede Maschine benötigt verschiedene Mengen der Ressourcen

    verbrauchsmatrix = np.array(
        [
            [
                12,
                8,
                15,
            ],  # Maschine 1: 12 kW Strom, 8 L/min Druckluft, 15 L/min Kühlwasser
            [18, 12, 10],  # Maschine 2: 18 kW, 12 L/min, 10 L/min
            [9, 15, 20],  # Maschine 3: 9 kW, 15 L/min, 20 L/min
        ]
    )

    # Verfügbare Gesamtressourcen
    verfuegbare_ressourcen = np.array([150, 120, 180])  # kW, L/min, L/min

    print("Ressourcenverbrauch pro Betriebsstunde:")
    print("         Strom  Druckluft  Kühlwasser")
    print(
        f"Masch.1   {verbrauchsmatrix[0, 0]:3d}       {verbrauchsmatrix[0, 1]:3d}        {verbrauchsmatrix[0, 2]:3d}"
    )
    print(
        f"Masch.2   {verbrauchsmatrix[1, 0]:3d}       {verbrauchsmatrix[1, 1]:3d}        {verbrauchsmatrix[1, 2]:3d}"
    )
    print(
        f"Masch.3   {verbrauchsmatrix[2, 0]:3d}       {verbrauchsmatrix[2, 1]:3d}        {verbrauchsmatrix[2, 2]:3d}"
    )

    print(f"\nVerfügbare Ressourcen: {verfuegbare_ressourcen}")

    # TODO: Lösen Sie das lineare Gleichungssystem

    # a) Direkte Lösung mit numpy.linalg.solve
    try:
        laufzeiten = la.solve(verbrauchsmatrix, verfuegbare_ressourcen)
        print("\na) Optimale Laufzeiten:")
        for i, zeit in enumerate(laufzeiten):
            print(f"   Maschine {i + 1}: {zeit:.2f} Stunden")

        # Verifikation
        tatsaechlicher_verbrauch = verbrauchsmatrix @ laufzeiten
        print("\nVerifikation:")
        ressourcen = ["Strom", "Druckluft", "Kühlwasser"]
        for i, ressource in enumerate(ressourcen):
            print(
                f"   {ressource}: {tatsaechlicher_verbrauch[i]:.1f} von {verfuegbare_ressourcen[i]} "
                f"({'✓' if abs(tatsaechlicher_verbrauch[i] - verfuegbare_ressourcen[i]) < 0.001 else '✗'})"
            )

    except la.LinAlgError:
        print("Das Gleichungssystem ist nicht eindeutig lösbar!")

    # b) Determinante und Eigenschaften der Matrix
    det = la.det(verbrauchsmatrix)
    rang = la.matrix_rank(verbrauchsmatrix)

    print("\nb) Matrix-Eigenschaften:")
    print(f"   Determinante: {det:.2f}")
    print(f"   Rang: {rang}")
    print(f"   Invertierbar: {'Ja' if abs(det) > 1e-10 else 'Nein'}")

    # c) Condition Number (Konditionszahl)
    cond_num = la.cond(verbrauchsmatrix)
    print(f"   Konditionszahl: {cond_num:.1f}")
    if cond_num > 1000:
        print("   ⚠️  Matrix ist schlecht konditioniert!")
    elif cond_num > 100:
        print("   ⚠️  Matrix ist mäßig konditioniert")
    else:
        print("   ✓ Matrix ist gut konditioniert")

    # d) Alternative Lösung mit Matrix-Inversion
    try:
        inverse_matrix = la.inv(verbrauchsmatrix)
        laufzeiten_inv = inverse_matrix @ verfuegbare_ressourcen

        print("\nd) Lösung via Matrix-Inversion:")
        print(f"   Laufzeiten: {laufzeiten_inv}")
        print(
            f"   Identisch mit direkter Lösung: {np.allclose(laufzeiten, laufzeiten_inv)}"
        )

    except la.LinAlgError:
        print("Matrix ist nicht invertierbar!")

    # e) Was passiert bei geänderten Ressourcen?
    neue_ressourcen = verfuegbare_ressourcen * np.array(
        [1.2, 0.8, 1.1]
    )  # +20%, -20%, +10%
    neue_laufzeiten = la.solve(verbrauchsmatrix, neue_ressourcen)

    print("\ne) Szenario mit geänderten Ressourcen:")
    print(f"   Neue Ressourcen: {neue_ressourcen}")
    print("   Neue Laufzeiten:")
    for i, (alt, neu) in enumerate(zip(laufzeiten, neue_laufzeiten, strict=False)):
        aenderung = (neu - alt) / alt * 100
        print(f"   Maschine {i + 1}: {neu:.2f}h ({aenderung:+.1f}%)")


def uebung_4_3() -> None:
    """Übung 4.3: Geometrische Transformationen"""
    print("\n" + "=" * 60)
    print("ÜBUNG 4.3: Geometrische Transformationen")
    print("=" * 60)

    # Koordinaten eines Werkstücks (rechteckiges Profil)
    original_punkte = np.array(
        [
            [0, 0],  # Punkt 1
            [50, 0],  # Punkt 2
            [50, 30],  # Punkt 3
            [30, 30],  # Punkt 4
            [30, 15],  # Punkt 5
            [0, 15],  # Punkt 6
            [0, 0],  # Zurück zum Start
        ]
    )

    print("Original-Koordinaten (mm):")
    for i, punkt in enumerate(original_punkte[:-1]):  # Letzter Punkt ist Wiederholung
        print(f"   P{i + 1}: ({punkt[0]:3.0f}, {punkt[1]:3.0f})")

    # TODO: Führen Sie geometrische Transformationen durch

    # a) Translation (Verschiebung)
    verschiebung = np.array([25, 40])
    verschobene_punkte = original_punkte + verschiebung

    print(f"\na) Translation um {verschiebung}:")
    print("Original → Verschoben")
    for i, (orig, neu) in enumerate(
        zip(original_punkte[:-1], verschobene_punkte[:-1], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({neu[0]:3.0f},{neu[1]:2.0f})"
        )

    # b) Rotation um den Ursprung
    winkel = np.radians(45)  # 45 Grad
    rotationsmatrix = np.array(
        [[np.cos(winkel), -np.sin(winkel)], [np.sin(winkel), np.cos(winkel)]]
    )

    # Rotation anwenden (Punkte als Spalten)
    rotierte_punkte = (rotationsmatrix @ original_punkte.T).T

    print(f"\nb) Rotation um {np.degrees(winkel):.0f}° um Ursprung:")
    print("Original → Rotiert")
    for i, (orig, rot) in enumerate(
        zip(original_punkte[:-1], rotierte_punkte[:-1], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({rot[0]:5.1f},{rot[1]:5.1f})"
        )

    # c) Skalierung (Vergrößerung/Verkleinerung)
    skalierung = np.array([1.5, 0.8])  # 150% in X, 80% in Y
    skalierte_punkte = original_punkte * skalierung

    print(f"\nc) Skalierung um Faktoren {skalierung}:")
    print("Original → Skaliert")
    for i, (orig, skal) in enumerate(
        zip(original_punkte[:-1], skalierte_punkte[:-1], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({skal[0]:5.1f},{skal[1]:4.1f})"
        )

    # d) Kombination: Erst rotieren, dann verschieben
    erst_rotiert = (rotationsmatrix @ original_punkte.T).T
    dann_verschoben = erst_rotiert + verschiebung

    print(f"\nd) Kombination: 45° Rotation + Translation {verschiebung}:")
    print("Original → Kombiniert")
    for i, (orig, komb) in enumerate(
        zip(original_punkte[:-1], dann_verschoben[:-1], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({komb[0]:5.1f},{komb[1]:5.1f})"
        )

    # e) Homogene Koordinaten (3D-Transformation in 2D)
    def homogene_transformation(
        punkte_2d: np.ndarray, rotation_grad: float, translation: np.ndarray
    ) -> np.ndarray:
        """Kombinierte Transformation mit homogenen Koordinaten"""
        # Punkte zu homogenen Koordinaten erweitern
        n_punkte = len(punkte_2d)
        homogene_punkte = np.column_stack([punkte_2d, np.ones(n_punkte)])

        # Transformationsmatrix erstellen
        winkel = np.radians(rotation_grad)
        T = np.array(
            [
                [np.cos(winkel), -np.sin(winkel), translation[0]],
                [np.sin(winkel), np.cos(winkel), translation[1]],
                [0, 0, 1],
            ]
        )

        # Transformation anwenden
        transformiert_homogen = (T @ homogene_punkte.T).T

        # Zurück zu kartesischen Koordinaten
        return np.asarray(transformiert_homogen[:, :2])

    homogen_transformiert = homogene_transformation(
        original_punkte, 30, np.array([20, 30])
    )

    print("\ne) Homogene Transformation (30° + Translation [20, 30]):")
    print("Original → Homogen transformiert")
    for i, (orig, homo) in enumerate(
        zip(original_punkte[:-1], homogen_transformiert[:-1], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({homo[0]:5.1f},{homo[1]:5.1f})"
        )

    # f) Reflexion (Spiegelung)
    # Spiegelung an der x-Achse
    reflexion_x = np.array([[1, 0], [0, -1]])
    gespiegelt_x = (reflexion_x @ original_punkte.T).T

    # Spiegelung an der Geraden y = x
    reflexion_diagonal = np.array([[0, 1], [1, 0]])
    gespiegelt_diagonal = (reflexion_diagonal @ original_punkte.T).T

    print("\nf) Reflexionen:")
    print("Spiegelung an x-Achse:")
    for i, (orig, spiegel) in enumerate(
        zip(original_punkte[:3], gespiegelt_x[:3], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({spiegel[0]:3.0f},{spiegel[1]:3.0f})"
        )

    print("Spiegelung an y=x:")
    for i, (orig, spiegel) in enumerate(
        zip(original_punkte[:3], gespiegelt_diagonal[:3], strict=False)
    ):
        print(
            f"P{i + 1}: ({orig[0]:3.0f},{orig[1]:2.0f}) → ({spiegel[0]:3.0f},{spiegel[1]:3.0f})"
        )


def uebung_4_4() -> None:
    """Übung 4.4: Eigenwerte und Eigenvektoren"""
    print("\n" + "=" * 60)
    print("ÜBUNG 4.4: Eigenwerte und Eigenvektoren")
    print("=" * 60)

    # Steifigkeitsmatrix eines mechanischen Systems
    # Symmetrische Matrix (typisch für mechanische Systeme)
    steifigkeitsmatrix = np.array([[200, -100, 0], [-100, 300, -50], [0, -50, 150]])

    print("Steifigkeitsmatrix (N/mm):")
    print(steifigkeitsmatrix)

    # TODO: Eigenwertanalyse durchführen

    # a) Eigenwerte und Eigenvektoren berechnen
    eigenwerte, eigenvektoren = la.eig(steifigkeitsmatrix)

    # Sortieren nach Eigenwerten (aufsteigend)
    sort_indices = np.argsort(eigenwerte)
    eigenwerte = eigenwerte[sort_indices]
    eigenvektoren = eigenvektoren[:, sort_indices]

    print("\na) Eigenwerte und Eigenvektoren:")
    for i, (wert, vektor) in enumerate(zip(eigenwerte, eigenvektoren.T, strict=False)):
        print(f"   λ{i + 1} = {wert:8.2f} N/mm")
        print(f"   v{i + 1} = [{vektor[0]:6.3f}, {vektor[1]:6.3f}, {vektor[2]:6.3f}]")

        # Normalisierung prüfen
        norm = la.norm(vektor)
        print(f"        ||v{i + 1}|| = {norm:.3f}")
        print()

    # b) Eigenfrequenzen berechnen (für mechanische Systeme)
    # ω = sqrt(λ/m), angenommen m = 1 kg pro Freiheitsgrad
    masse = 1.0  # kg
    eigenfrequenzen = np.sqrt(eigenwerte / masse) / (2 * np.pi)  # Hz

    print(f"b) Eigenfrequenzen (bei m = {masse} kg):")
    for i, freq in enumerate(eigenfrequenzen):
        print(f"   f{i + 1} = {freq:.2f} Hz")

    # c) Verifikation: A @ v = λ @ v
    print("\nc) Verifikation (A @ v = λ @ v):")
    for i in range(len(eigenwerte)):
        v = eigenvektoren[:, i]
        links = steifigkeitsmatrix @ v
        rechts = eigenwerte[i] * v
        fehler = la.norm(links - rechts)
        print(
            f"   Eigenvektor {i + 1}: Fehler = {fehler:.2e} {'✓' if fehler < 1e-10 else '✗'}"
        )

    # d) Hauptachsentransformation
    # P^T @ A @ P = D (Diagonalmatrix)
    P = eigenvektoren
    D = P.T @ steifigkeitsmatrix @ P

    print("\nd) Hauptachsentransformation (P^T @ A @ P):")
    print("Diagonalmatrix D:")
    for i in range(3):
        print(f"   [{D[i, 0]:8.2f} {D[i, 1]:8.2f} {D[i, 2]:8.2f}]")

    # Prüfen, ob wirklich diagonal
    off_diagonal = D - np.diag(np.diag(D))
    max_off_diag = np.max(np.abs(off_diagonal))
    print(f"Maximaler Off-Diagonal-Eintrag: {max_off_diag:.2e}")

    # e) Konditionszahl über Eigenwerte
    cond_eigenvalue = np.max(eigenwerte) / np.min(eigenwerte)
    cond_numpy = la.cond(steifigkeitsmatrix)

    print("\ne) Konditionszahl:")
    print(f"   Über Eigenwerte: {cond_eigenvalue:.1f}")
    print(f"   NumPy cond(): {cond_numpy:.1f}")
    print(
        f"   Übereinstimmung: {'Ja' if abs(cond_eigenvalue - cond_numpy) < 0.1 else 'Nein'}"
    )

    # f) Quadratische Form und Definitheit
    # Matrix ist positiv definit wenn alle Eigenwerte > 0
    definitheit = (
        "positiv definit"
        if np.all(eigenwerte > 0)
        else "negativ definit" if np.all(eigenwerte < 0) else "indefinit"
    )

    print("\nf) Definitheit der Matrix:")
    print(f"   Alle Eigenwerte > 0? {np.all(eigenwerte > 0)}")
    print(f"   Matrix ist: {definitheit}")

    if definitheit == "positiv definit":
        print("   ✓ Steifigkeitsmatrix ist physikalisch sinnvoll")


def uebung_4_5() -> None:
    """Übung 4.5: Least-Squares-Probleme"""
    print("\n" + "=" * 60)
    print("ÜBUNG 4.5: Least-Squares-Probleme")
    print("=" * 60)

    # Messdaten: Kraft-Deformations-Beziehung
    # Mehr Messpunkte als unbekannte Parameter (überbestimmtes System)
    kraft = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])  # N
    deformation = np.array(
        [0.02, 1.98, 4.05, 5.97, 8.12, 9.89, 12.15, 13.92, 16.08, 18.01, 19.95]
    )  # mm

    print("Kraft-Deformations-Messdaten:")
    print("Kraft (N)    Deformation (mm)")
    print("-" * 28)
    for f, d in zip(kraft, deformation, strict=False):
        print(f"{f:6.0f}        {d:8.2f}")

    # TODO: Least-Squares-Analyse durchführen

    # a) Linearer Fit: d = a * F + b
    # Designmatrix A für lineares Modell
    A_linear = np.column_stack([kraft, np.ones(len(kraft))])

    # Normalgleichungen lösen: A^T @ A @ x = A^T @ b
    koeff_linear = la.solve(A_linear.T @ A_linear, A_linear.T @ deformation)

    steigung = koeff_linear[0]
    achsenabschnitt = koeff_linear[1]

    print("\na) Linearer Fit (d = a*F + b):")
    print(f"   Steigung a = {steigung:.6f} mm/N")
    print(f"   Y-Achsenabschnitt b = {achsenabschnitt:.4f} mm")
    print(f"   Gleichung: d = {steigung:.6f} * F + {achsenabschnitt:.4f}")

    # Vorhersagen und Residuen
    vorhersage_linear = A_linear @ koeff_linear
    residuen_linear = deformation - vorhersage_linear

    print(f"\n   Erste 5 Residuen: {residuen_linear[:5]}")
    print(f"   RMS-Fehler: {np.sqrt(np.mean(residuen_linear**2)):.4f} mm")

    # b) Quadratischer Fit: d = a*F² + b*F + c
    A_quadratisch = np.column_stack([kraft**2, kraft, np.ones(len(kraft))])
    koeff_quadratisch = la.lstsq(A_quadratisch, deformation, rcond=None)[0]

    a_quad, b_quad, c_quad = koeff_quadratisch

    print("\nb) Quadratischer Fit (d = a*F² + b*F + c):")
    print(f"   a = {a_quad:.8f} mm/N²")
    print(f"   b = {b_quad:.6f} mm/N")
    print(f"   c = {c_quad:.4f} mm")

    vorhersage_quadratisch = A_quadratisch @ koeff_quadratisch
    residuen_quadratisch = deformation - vorhersage_quadratisch

    print(f"   RMS-Fehler: {np.sqrt(np.mean(residuen_quadratisch**2)):.4f} mm")

    # c) Modellvergleich
    # R-squared (Bestimmtheitsmaß)
    ss_tot = np.sum((deformation - np.mean(deformation)) ** 2)
    ss_res_linear = np.sum(residuen_linear**2)
    ss_res_quadratisch = np.sum(residuen_quadratisch**2)

    r2_linear = 1 - ss_res_linear / ss_tot
    r2_quadratisch = 1 - ss_res_quadratisch / ss_tot

    print("\nc) Modellvergleich:")
    print("   Lineares Modell:")
    print(f"     R² = {r2_linear:.6f}")
    print(
        f"     AIC approx = {len(kraft) * np.log(ss_res_linear / len(kraft)) + 4:.2f}"
    )

    print("   Quadratisches Modell:")
    print(f"     R² = {r2_quadratisch:.6f}")
    print(
        f"     AIC approx = {len(kraft) * np.log(ss_res_quadratisch / len(kraft)) + 6:.2f}"
    )

    besseres_modell = "quadratisch" if r2_quadratisch > r2_linear else "linear"
    print(f"   Besseres Modell: {besseres_modell}")

    # d) QR-Zerlegung für Least-Squares
    Q, R = la.qr(A_linear)
    koeff_qr = la.solve(R, Q.T @ deformation)

    print("\nd) QR-Zerlegung Lösung:")
    print(f"   Koeffizienten: {koeff_qr}")
    print(f"   Identisch mit Normalgleichungen: {np.allclose(koeff_linear, koeff_qr)}")

    # e) Konfidenzintervalle (vereinfacht)
    # Kovarianzmatrix der Parameter
    sigma2 = np.sum(residuen_linear**2) / (len(kraft) - 2)  # Residualvarianz
    kovarianz_matrix = sigma2 * la.inv(A_linear.T @ A_linear)

    std_fehler = np.sqrt(np.diag(kovarianz_matrix))

    print("\ne) Unsicherheiten (95% Konfidenz, t ≈ 2):")
    print(f"   Steigung: {steigung:.6f} ± {2 * std_fehler[0]:.6f} mm/N")
    print(f"   Y-Achsenabschnitt: {achsenabschnitt:.4f} ± {2 * std_fehler[1]:.4f} mm")

    # f) Extrapolation
    neue_kraft = np.array([110, 120, 150])
    A_extrapol = np.column_stack([neue_kraft, np.ones(len(neue_kraft))])
    deformation_extrapol = A_extrapol @ koeff_linear

    print("\nf) Extrapolation:")
    for f, d in zip(neue_kraft, deformation_extrapol, strict=False):
        print(f"   Bei {f:3.0f} N: {d:.2f} mm Deformation")


def uebung_4_6() -> None:
    """Übung 4.6: Praktisches Beispiel - Finite-Elemente-Vereinfachung"""
    print("\n" + "=" * 60)
    print("ÜBUNG 4.6: Praktisches Beispiel - FE-Vereinfachung")
    print("=" * 60)

    # Vereinfachtes 2D-Fachwerk mit 4 Knoten
    # Steifigkeitsmatrix eines einfachen Fachwerks
    # 6 Freiheitsgrade (2 pro Knoten für 2D: x, y)

    # Globale Steifigkeitsmatrix (vereinfacht)
    K_global = np.array(
        [
            [100, 0, -50, 0, -50, 0],  # Knoten 1, x-Richtung
            [0, 80, 0, -40, 0, -40],  # Knoten 1, y-Richtung
            [-50, 0, 150, -30, -50, 0],  # Knoten 2, x-Richtung
            [0, -40, -30, 120, 0, -40],  # Knoten 2, y-Richtung
            [-50, 0, -50, 0, 120, -20],  # Knoten 3, x-Richtung
            [0, -40, 0, -40, -20, 100],  # Knoten 3, y-Richtung
        ]
    )

    # Lasten [Fx1, Fy1, Fx2, Fy2, Fx3, Fy3]
    lasten = np.array([100, -200, 0, -300, -50, 0])  # N

    print("Globale Steifigkeitsmatrix (N/mm):")
    for _, zeile in enumerate(K_global):
        print(f"[{' '.join(f'{x:6.0f}' for x in zeile)}]")

    print(f"\nLastvektor: {lasten}")

    # TODO: FE-Analyse durchführen

    # a) Verformungen berechnen: K @ u = F
    verformungen = la.solve(K_global, lasten)

    print("\na) Verformungen (mm):")
    knoten_names = ["Knoten 1", "Knoten 2", "Knoten 3"]
    for i in range(3):
        ux = verformungen[2 * i]
        uy = verformungen[2 * i + 1]
        betrag = np.sqrt(ux**2 + uy**2)
        print(f"   {knoten_names[i]}: ux={ux:7.3f}, uy={uy:7.3f}, |u|={betrag:7.3f}")

    # b) Reaktionskräfte berechnen
    reaktionen = K_global @ verformungen

    print("\nb) Verifikation - Reaktionskräfte sollten Lasten entsprechen:")
    for i, (last, reakt) in enumerate(zip(lasten, reaktionen, strict=False)):
        print(
            f"   DOF {i + 1}: Last={last:6.1f}N, Reaktion={reakt:6.1f}N, "
            f"Diff={abs(last - reakt):.2e}"
        )

    # c) Konditionierung der Steifigkeitsmatrix
    cond_num = la.cond(K_global)
    det = la.det(K_global)

    print("\nc) Matrix-Eigenschaften:")
    print(f"   Konditionszahl: {cond_num:.1f}")
    print(f"   Determinante: {det:.2e}")

    if cond_num > 1e6:
        print("   ⚠️  System ist sehr schlecht konditioniert!")
    elif cond_num > 1e4:
        print("   ⚠️  System ist schlecht konditioniert")
    else:
        print("   ✓ System ist gut konditioniert")

    # d) Eigenmoden des Systems (freie Schwingungen)
    eigenwerte, eigenmoden = la.eig(K_global)

    # Sortieren nach Eigenwerten
    sort_idx = np.argsort(eigenwerte)
    eigenwerte = eigenwerte[sort_idx]
    eigenmoden = eigenmoden[:, sort_idx]

    print("\nd) Erste 3 Eigenfrequenzen (freie Schwingungen):")
    # ω = sqrt(λ/m), angenommen einheitliche Masse
    masse_pro_knoten = 1.0  # kg

    for i in range(3):
        if eigenwerte[i] > 0:
            freq = np.sqrt(eigenwerte[i] / masse_pro_knoten) / (2 * np.pi)
            print(f"   Mode {i + 1}: f = {freq:.2f} Hz")

            # Eigenmode anzeigen (normalisiert)
            mode = eigenmoden[:, i]
            mode_norm = mode / np.max(np.abs(mode))
            print(f"             Eigenmode: {mode_norm}")
        else:
            print(f"   Mode {i + 1}: Starrkörpermodus (λ ≈ 0)")

    # e) Energiebetrachtung
    # Verformungsenergie: U = 0.5 * u^T * K * u
    verformungsenergie = 0.5 * verformungen.T @ K_global @ verformungen

    # Arbeit der äußeren Kräfte: W = F^T * u
    arbeit_aussenkraefte = lasten.T @ verformungen

    print("\ne) Energiebilanz:")
    print(f"   Verformungsenergie: {verformungsenergie:.2f} N⋅mm")
    print(f"   Arbeit äußere Kräfte: {arbeit_aussenkraefte:.2f} N⋅mm")
    print(
        f"   Verhältnis (sollte ≈ 2 sein): {arbeit_aussenkraefte / verformungsenergie:.2f}"
    )

    # f) Spannungen (vereinfacht für ein Element)
    # Angenommen: lineares Element zwischen Knoten 1 und 2
    # σ = E * ε = E * (Δu/L)
    E = 200000  # N/mm² (Stahl)
    L = 100  # mm Elementlänge

    delta_u = verformungen[2] - verformungen[0]  # Δux zwischen Knoten 1 und 2
    dehnung = delta_u / L
    spannung = E * dehnung

    print("\nf) Spannung in Element 1-2 (vereinfacht):")
    print(f"   Längung: {delta_u:.4f} mm")
    print(f"   Dehnung: {dehnung:.6f}")
    print(f"   Spannung: {spannung:.1f} N/mm²")


def hauptprogramm() -> None:
    """Hauptprogramm - alle Übungen ausführen"""
    print("🔧 NUMPY LINEARE ALGEBRA - ÜBUNGEN")

    try:
        uebung_4_1()
        uebung_4_2()
        uebung_4_3()
        uebung_4_4()
        uebung_4_5()
        uebung_4_6()

        print("\n" + "=" * 60)
        print("✅ ALLE ÜBUNGEN ERFOLGREICH ABGESCHLOSSEN!")
        print("=" * 60)
        print("\n📝 Was Sie gelernt haben:")
        print("• Matrix-Operationen für technische Probleme")
        print("• Lösung linearer Gleichungssysteme")
        print("• Geometrische Transformationen und Koordinatensysteme")
        print("• Eigenwertanalyse für Schwingungsprobleme")
        print("• Least-Squares-Methoden für Datenanalyse")
        print("• Grundlagen der Finite-Elemente-Methode")

        print("\n🎯 Nächste Schritte:")
        print("• Kapitel 4: Pandas für Datenanalyse")
        print("• Vertiefung: Numerische Methoden und Optimierung")

    except Exception as e:
        print(f"\n❌ Fehler in den Übungen: {e}")
        print("Überprüfen Sie Ihren Code und versuchen Sie es erneut.")


if __name__ == "__main__":
    hauptprogramm()
