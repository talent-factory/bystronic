#!/usr/bin/env python3
"""
Übung 4: Datenanalyse - Pandas Tutorial für Bystronic

AUFGABENSTELLUNG:
In dieser Übung führen Sie umfassende Datenanalysen durch.
Sie lernen Aggregationen, Pivot-Tabellen, Zeitreihenanalyse,
statistische Auswertungen und JOIN-Operationen.

SCHWIERIGKEITSGRAD: Intermediate bis Advanced
ZEITAUFWAND: 75-90 Minuten

LERNZIELE:
- Multi-dimensionale Gruppierungen und Aggregationen
- Pivot-Tabellen für komplexe Analysen
- Zeitreihenanalyse und Resampling
- Statistische Kennzahlen berechnen
- JOIN-Operationen mit Stammdaten
- Performance-Benchmarking implementieren
- Umfassende Analysereports erstellen
"""

import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

print("=" * 60)
print("📊 ÜBUNG 4: DATENANALYSE")
print("=" * 60)

# =============================================================================
# VORBEREITUNG: Realistische Produktionsdaten erstellen
# =============================================================================

print("\n🔧 Vorbereitung: Erstelle umfassende Produktionsdaten...")


def create_comprehensive_production_data():
    """Erstelle realistische Produktionsdaten für 3 Monate"""
    np.random.seed(42)

    # Setup
    start_date = pd.Timestamp("2024-01-01")
    end_date = pd.Timestamp("2024-03-31")
    date_range = pd.date_range(start_date, end_date, freq="H")

    maschinen_config = [
        {
            "name": "Laser_01",
            "typ": "ByStar",
            "halle": "A",
            "baujahr": 2019,
            "kapazitaet": 10,
        },
        {
            "name": "Laser_02",
            "typ": "ByStar",
            "halle": "A",
            "baujahr": 2020,
            "kapazitaet": 10,
        },
        {
            "name": "Laser_03",
            "typ": "ByStar",
            "halle": "A",
            "baujahr": 2021,
            "kapazitaet": 12,
        },
        {
            "name": "Presse_01",
            "typ": "Xpert",
            "halle": "B",
            "baujahr": 2018,
            "kapazitaet": 8,
        },
        {
            "name": "Presse_02",
            "typ": "Xpert",
            "halle": "B",
            "baujahr": 2021,
            "kapazitaet": 8,
        },
        {
            "name": "Stanze_01",
            "typ": "ByTrans",
            "halle": "C",
            "baujahr": 2017,
            "kapazitaet": 6,
        },
    ]

    produkte = ["Teil_A", "Teil_B", "Teil_C", "Teil_D", "Teil_E"]

    # Produktkomplexität definieren
    produkt_faktoren = {
        "Teil_A": {"komplexitaet": 1.2, "ausschuss_basis": 0.02},
        "Teil_B": {"komplexitaet": 1.0, "ausschuss_basis": 0.03},
        "Teil_C": {"komplexitaet": 0.8, "ausschuss_basis": 0.05},
        "Teil_D": {"komplexitaet": 1.1, "ausschuss_basis": 0.025},
        "Teil_E": {"komplexitaet": 1.3, "ausschuss_basis": 0.02},
    }

    data = []
    for timestamp in date_range:
        for maschine in maschinen_config:
            # 85% Wahrscheinlichkeit für Produktionsdaten pro Stunde
            if np.random.random() < 0.85:
                # Wochenende: reduzierte Produktion
                if timestamp.weekday() >= 5:  # Samstag/Sonntag
                    if np.random.random() < 0.7:  # 70% weniger Produktion
                        continue

                # Nachtschicht: etwas weniger Produktion
                stunde = timestamp.hour
                if 22 <= stunde or stunde < 6:  # Nachtschicht
                    if np.random.random() < 0.1:  # 10% weniger
                        continue

                # Schicht bestimmen
                if 6 <= stunde < 14:
                    schicht = "Früh"
                elif 14 <= stunde < 22:
                    schicht = "Spät"
                else:
                    schicht = "Nacht"

                # Produkt wählen (gewichtet nach Häufigkeit)
                produkt = np.random.choice(
                    produkte,
                    p=[0.3, 0.25, 0.2, 0.15, 0.1],  # Teil_A am häufigsten
                )

                # Basis-Produktionszeit mit Maschinen- und Schicht-Faktoren
                basis_prod = np.random.uniform(
                    maschine["kapazitaet"] * 0.6, maschine["kapazitaet"] * 0.95
                )

                # Schicht-Faktoren
                schicht_faktoren = {"Früh": 1.0, "Spät": 0.95, "Nacht": 0.85}
                produktionszeit = basis_prod * schicht_faktoren[schicht]

                # Produkt-Komplexität berücksichtigen
                produktionszeit *= produkt_faktoren[produkt]["komplexitaet"]

                # Maschinen-Alter berücksichtigen
                alter = 2024 - maschine["baujahr"]
                effizienz_faktor = max(0.8, 1 - (alter * 0.02))  # 2% pro Jahr
                produktionszeit *= effizienz_faktor

                # Stückzahl berechnen
                stueck_pro_stunde = np.random.uniform(15, 25) / produktionszeit
                stueckzahl = int(stueck_pro_stunde * produktionszeit)

                # Qualitäts-Parameter
                basis_ausschuss = produkt_faktoren[produkt]["ausschuss_basis"]
                # Nachtschicht: etwas höherer Ausschuss
                if schicht == "Nacht":
                    basis_ausschuss *= 1.2
                ausschuss_rate = np.random.normal(
                    basis_ausschuss, basis_ausschuss * 0.3
                )
                ausschuss_rate = max(0.001, min(0.15, ausschuss_rate))  # Grenzen

                # Temperatur (abhängig von Maschinentyp und Auslastung)
                basis_temp = {"ByStar": 24, "Xpert": 22, "ByTrans": 20}[maschine["typ"]]
                temp_variation = (
                    produktionszeit / maschine["kapazitaet"]
                ) * 3  # Höhere Last = höhere Temp
                temperatur = basis_temp + temp_variation + np.random.normal(0, 1.5)

                # Energie (abhängig von Typ und Last)
                energie_basis = {"ByStar": 200, "Xpert": 150, "ByTrans": 100}[
                    maschine["typ"]
                ]
                energieverbrauch = energie_basis * (
                    produktionszeit / maschine["kapazitaet"]
                ) + np.random.normal(0, 20)

                # Wartungsindikatoren
                wartung_score = np.random.uniform(0.8, 1.0)
                if alter > 5:  # Ältere Maschinen
                    wartung_score -= 0.1

                data.append(
                    {
                        "Timestamp": timestamp,
                        "Maschine": maschine["name"],
                        "Typ": maschine["typ"],
                        "Halle": maschine["halle"],
                        "Baujahr": maschine["baujahr"],
                        "Schicht": schicht,
                        "Produkt": produkt,
                        "Produktionszeit_h": round(produktionszeit, 2),
                        "Stückzahl": stueckzahl,
                        "Ausschuss_Rate": round(ausschuss_rate, 4),
                        "Temperatur_C": round(temperatur, 1),
                        "Energieverbrauch_kWh": round(energieverbrauch, 1),
                        "Wartung_Score": round(wartung_score, 3),
                        "Wochentag": timestamp.strftime("%A"),
                        "KW": timestamp.isocalendar()[1],
                        "Monat": timestamp.month,
                        "Quartal": timestamp.quarter,
                    }
                )

    return pd.DataFrame(data)


def create_master_data():
    """Erstelle Stammdaten für JOIN-Operationen"""

    # Maschinenstamm
    maschinen_stamm = pd.DataFrame(
        {
            "Maschine": [
                "Laser_01",
                "Laser_02",
                "Laser_03",
                "Presse_01",
                "Presse_02",
                "Stanze_01",
            ],
            "Anschaffungswert_Euro": [450000, 480000, 520000, 320000, 360000, 280000],
            "Wartungsintervall_Tage": [90, 90, 90, 120, 120, 180],
            "Max_Stueck_pro_h": [180, 180, 200, 120, 120, 80],
            "Energiekosten_pro_kWh": [0.12, 0.12, 0.12, 0.10, 0.10, 0.08],
            "Letzte_Wartung": [
                "2024-01-15",
                "2024-02-01",
                "2024-01-20",
                "2024-01-10",
                "2024-02-20",
                "2023-12-15",
            ],
        }
    )
    maschinen_stamm["Letzte_Wartung"] = pd.to_datetime(
        maschinen_stamm["Letzte_Wartung"]
    )

    # Produktstamm
    produkt_stamm = pd.DataFrame(
        {
            "Produkt": ["Teil_A", "Teil_B", "Teil_C", "Teil_D", "Teil_E"],
            "Material": ["Stahl", "Aluminium", "Edelstahl", "Stahl", "Titan"],
            "Verkaufspreis_Euro": [15.80, 12.50, 8.75, 18.20, 45.60],
            "Materialkosten_Euro": [8.20, 6.80, 4.50, 9.50, 28.40],
            "Zielausschuss_max": [0.02, 0.03, 0.05, 0.025, 0.015],
            "Gewicht_kg": [2.5, 1.8, 1.2, 3.1, 0.8],
            "Produktkategorie": [
                "Standard",
                "Standard",
                "Einfach",
                "Premium",
                "Speziell",
            ],
        }
    )

    # Kostenstellen
    kostenstellen = pd.DataFrame(
        {
            "Halle": ["A", "B", "C"],
            "Kostenstelle": ["KST_4100", "KST_4200", "KST_4300"],
            "Hallenleiter": ["Müller", "Schmidt", "Weber"],
            "Fläche_qm": [1200, 800, 600],
            "Overhead_Faktor": [1.2, 1.15, 1.1],
        }
    )

    return maschinen_stamm, produkt_stamm, kostenstellen


# Daten erstellen
print("Erstelle Produktionsdaten...")
df_produktion = create_comprehensive_production_data()
print(f"✅ {len(df_produktion):,} Produktionsdatensätze erstellt")

print("Erstelle Stammdaten...")
df_maschinen, df_produkte, df_kostenstellen = create_master_data()
print(
    f"✅ Stammdaten erstellt: {len(df_maschinen)} Maschinen, {len(df_produkte)} Produkte, {len(df_kostenstellen)} Kostenstellen"
)

print(
    f"\\nZeitraum: {df_produktion['Timestamp'].min()} bis {df_produktion['Timestamp'].max()}"
)
print(f"Maschinen: {df_produktion['Maschine'].nunique()}")
print(f"Produkte: {df_produktion['Produkt'].nunique()}")
print("Erste 5 Datensätze:")
print(df_produktion.head())

# =============================================================================
# AUFGABE 1: Grundlegende Aggregationen (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 1: Grundlegende Aggregationen")
print("-" * 40)

print(
    """
TODO: Führen Sie grundlegende Aggregationen durch:

a) Berechnen Sie Gesamtstatistiken über alle Daten
b) Analysieren Sie Produktionsleistung nach Maschinen
c) Bewerten Sie Qualitätsmetriken nach Produkten
d) Erstellen Sie einen Schichtvergleich
"""
)

print("a) Gesamtstatistiken berechnen:")
# IHRE LÖSUNG HIER:
gesamt_stats = {
    "Zeitraum_Tage": (
        df_produktion["Timestamp"].max() - df_produktion["Timestamp"].min()
    ).days,
    "Produktionsstunden_Total": df_produktion["Produktionszeit_h"].sum(),
    "Stückzahl_Total": df_produktion["Stückzahl"].sum(),
    "Durchschnitt_Ausschuss": df_produktion["Ausschuss_Rate"].mean(),
    "Energieverbrauch_Total": df_produktion["Energieverbrauch_kWh"].sum(),
    "Durchschnitt_Temperatur": df_produktion["Temperatur_C"].mean(),
    "Produktionsstunden_pro_Tag": df_produktion["Produktionszeit_h"].sum()
    / ((df_produktion["Timestamp"].max() - df_produktion["Timestamp"].min()).days or 1),
}

print("📈 GESAMTSTATISTIKEN:")
for key, value in gesamt_stats.items():
    if "Durchschnitt" in key or "Rate" in key:
        print(f"{key}: {value:.4f}")
    elif "pro_Tag" in key:
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value:,.2f}")

print("\\nb) Produktionsleistung nach Maschinen:")
# IHRE LÖSUNG HIER:
maschinen_performance = (
    df_produktion.groupby("Maschine")
    .agg(
        {
            "Produktionszeit_h": ["sum", "mean", "count"],
            "Stückzahl": ["sum", "mean"],
            "Ausschuss_Rate": ["mean", "std"],
            "Energieverbrauch_kWh": "sum",
            "Temperatur_C": "mean",
            "Wartung_Score": "mean",
        }
    )
    .round(3)
)

# Spalten-Namen vereinfachen
maschinen_performance.columns = ["_".join(col) for col in maschinen_performance.columns]

# Effizienz-Kennzahlen hinzufügen
maschinen_performance["Stück_pro_Stunde"] = (
    maschinen_performance["Stückzahl_sum"]
    / maschinen_performance["Produktionszeit_h_sum"]
).round(2)

maschinen_performance["Energie_pro_Stück"] = (
    maschinen_performance["Energieverbrauch_kWh_sum"]
    / maschinen_performance["Stückzahl_sum"]
).round(3)

print("🏭 MASCHINEN-PERFORMANCE:")
print(maschinen_performance)

print("\\nc) Qualitätsmetriken nach Produkten:")
# IHRE LÖSUNG HIER:
produkt_qualitaet = (
    df_produktion.groupby("Produkt")
    .agg(
        {
            "Ausschuss_Rate": ["count", "mean", "std", "min", "max"],
            "Stückzahl": "sum",
            "Produktionszeit_h": "sum",
        }
    )
    .round(4)
)

produkt_qualitaet.columns = ["_".join(col) for col in produkt_qualitaet.columns]

# Zusätzliche Qualitäts-Metriken
produkt_qualitaet["Qualitaets_Konsistenz"] = (
    1
    - (
        produkt_qualitaet["Ausschuss_Rate_std"]
        / produkt_qualitaet["Ausschuss_Rate_mean"]
    )
).round(3)

print("🎯 PRODUKT-QUALITÄTSMETRIKEN:")
print(produkt_qualitaet)

print("\\nd) Schichtvergleich:")
# IHRE LÖSUNG HIER:
schicht_vergleich = (
    df_produktion.groupby("Schicht")
    .agg(
        {
            "Produktionszeit_h": ["sum", "mean"],
            "Stückzahl": ["sum", "mean"],
            "Ausschuss_Rate": ["mean", "std"],
            "Energieverbrauch_kWh": "mean",
            "Wartung_Score": "mean",
        }
    )
    .round(3)
)

schicht_vergleich.columns = ["_".join(col) for col in schicht_vergleich.columns]

# Schichten logisch sortieren
schicht_reihenfolge = ["Früh", "Spät", "Nacht"]
schicht_vergleich = schicht_vergleich.reindex(schicht_reihenfolge)

print("⏰ SCHICHT-VERGLEICH:")
print(schicht_vergleich)

# Beste/schlechteste Schicht identifizieren
beste_schicht_prod = schicht_vergleich["Produktionszeit_h_sum"].idxmax()
beste_schicht_qual = schicht_vergleich["Ausschuss_Rate_mean"].idxmin()
print(f"\\n🥇 Beste Schicht (Produktion): {beste_schicht_prod}")
print(f"🥇 Beste Schicht (Qualität): {beste_schicht_qual}")

# Validierung
try:
    assert (
        gesamt_stats["Produktionsstunden_Total"] > 0
    ), "Sollte Produktionsstunden haben"
    assert len(maschinen_performance) == 6, "Sollte 6 Maschinen analysiert haben"
    assert len(produkt_qualitaet) == 5, "Sollte 5 Produkte analysiert haben"
    print("\\n✅ Aufgabe 1 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 1: {e}")

# =============================================================================
# AUFGABE 2: Pivot-Tabellen für komplexe Analysen (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 2: Pivot-Tabellen für komplexe Analysen")
print("-" * 40)

print(
    """
TODO: Erstellen Sie verschiedene Pivot-Tabellen:

a) Produktionszeit nach Maschine × Schicht
b) Ausschussrate nach Halle × Produkt
c) Energieverbrauch nach Typ × Monat
d) Stückzahl nach Produkt × KW (Kalenderwoche)
"""
)

print("a) Produktionszeit nach Maschine × Schicht:")
# IHRE LÖSUNG HIER:
pivot_prod_maschine_schicht = df_produktion.pivot_table(
    values="Produktionszeit_h",
    index="Maschine",
    columns="Schicht",
    aggfunc="sum",
    fill_value=0,
    margins=True,  # Gesamtsummen
    margins_name="Total",
).round(2)

print("📋 PIVOT: Produktionszeit (Stunden) - Maschine × Schicht")
print(pivot_prod_maschine_schicht)

# Zusätzliche Analyse: Prozentuale Verteilung
pivot_prod_prozent = df_produktion.pivot_table(
    values="Produktionszeit_h",
    index="Maschine",
    columns="Schicht",
    aggfunc="sum",
    fill_value=0,
    normalize="index",  # Prozent pro Zeile (Maschine)
).round(3)

print("\\n📊 PIVOT: Produktionszeit-Verteilung (%) - Maschine × Schicht")
print(pivot_prod_prozent)

print("\\nb) Ausschussrate nach Halle × Produkt:")
# IHRE LÖSUNG HIER:
pivot_ausschuss_halle_produkt = df_produktion.pivot_table(
    values="Ausschuss_Rate",
    index="Halle",
    columns="Produkt",
    aggfunc="mean",
    fill_value=0,
).round(4)

print("📋 PIVOT: Durchschnittliche Ausschussrate - Halle × Produkt")
print(pivot_ausschuss_halle_produkt)

# Heatmap-ähnliche Analyse: Problembereiche identifizieren
print("\\n🚨 Problembereiche (Ausschuss > 0.04):")
problem_combinations = pivot_ausschuss_halle_produkt > 0.04
for halle in problem_combinations.index:
    for produkt in problem_combinations.columns:
        if problem_combinations.loc[halle, produkt]:
            rate = pivot_ausschuss_halle_produkt.loc[halle, produkt]
            print(f"  Halle {halle} - {produkt}: {rate:.4f}")

print("\\nc) Energieverbrauch nach Typ × Monat:")
# IHRE LÖSUNG HIER:
pivot_energie_typ_monat = df_produktion.pivot_table(
    values="Energieverbrauch_kWh",
    index="Typ",
    columns="Monat",
    aggfunc="sum",
    fill_value=0,
    margins=True,
).round(1)

print("📋 PIVOT: Energieverbrauch (kWh) - Typ × Monat")
print(pivot_energie_typ_monat)

# Energieeffizienz pro Stück
pivot_energie_effizienz = (
    df_produktion.groupby(["Typ", "Monat"])
    .agg({"Energieverbrauch_kWh": "sum", "Stückzahl": "sum"})
    .reset_index()
)
pivot_energie_effizienz["Energie_pro_Stück"] = (
    pivot_energie_effizienz["Energieverbrauch_kWh"]
    / pivot_energie_effizienz["Stückzahl"]
).round(3)

pivot_effizienz = pivot_energie_effizienz.pivot_table(
    values="Energie_pro_Stück", index="Typ", columns="Monat", fill_value=0
)

print("\\n⚡ PIVOT: Energieeffizienz (kWh/Stück) - Typ × Monat")
print(pivot_effizienz)

print("\\nd) Stückzahl nach Produkt × KW:")
# IHRE LÖSUNG HIER:
# Nur erste 8 Kalenderwochen für bessere Lesbarkeit
kw_filter = df_produktion["KW"] <= 8
pivot_stueck_produkt_kw = df_produktion[kw_filter].pivot_table(
    values="Stückzahl",
    index="Produkt",
    columns="KW",
    aggfunc="sum",
    fill_value=0,
    margins=True,
)

print("📋 PIVOT: Stückzahl - Produkt × KW (erste 8 Wochen)")
print(pivot_stueck_produkt_kw)

# Trend-Analyse: Wachstum pro Produkt
if len(pivot_stueck_produkt_kw.columns) > 2:  # Mindestens 2 KW + Total
    erste_kw = pivot_stueck_produkt_kw.columns[0]
    letzte_kw = pivot_stueck_produkt_kw.columns[-2]  # Vor 'Total'

    trend_analyse = pd.DataFrame(
        {
            "KW_" + str(erste_kw): pivot_stueck_produkt_kw[erste_kw],
            "KW_" + str(letzte_kw): pivot_stueck_produkt_kw[letzte_kw],
        }
    ).dropna()

    trend_analyse["Trend_%"] = (
        (trend_analyse["KW_" + str(letzte_kw)] - trend_analyse["KW_" + str(erste_kw)])
        / trend_analyse["KW_" + str(erste_kw)]
        * 100
    ).round(2)

    print("\\n📈 TREND-ANALYSE (Stückzahl-Entwicklung):")
    print(trend_analyse)

# Validierung
try:
    assert pivot_prod_maschine_schicht.shape[0] > 0, "Pivot-Tabelle sollte Daten haben"
    assert "Total" in pivot_prod_maschine_schicht.index, "Sollte Gesamtsummen haben"
    assert len(pivot_ausschuss_halle_produkt.index) == 3, "Sollte 3 Hallen haben"
    print("\\n✅ Aufgabe 2 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 2: {e}")

# =============================================================================
# AUFGABE 3: Zeitreihenanalyse (25 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 3: Zeitreihenanalyse")
print("-" * 40)

print(
    """
TODO: Führen Sie Zeitreihenanalysen durch:

a) Erstellen Sie tägliche Produktions-Aggregate
b) Implementieren Sie wöchentliches Resampling
c) Berechnen Sie gleitende Durchschnitte
d) Analysieren Sie saisonale Muster und Trends
"""
)

# DataFrame für Zeitreihenanalyse vorbereiten
df_time = df_produktion.copy()
df_time = df_time.set_index("Timestamp")

print("a) Tägliche Produktions-Aggregate:")
# IHRE LÖSUNG HIER:
daily_production = (
    df_time.groupby(df_time.index.date)
    .agg(
        {
            "Produktionszeit_h": "sum",
            "Stückzahl": "sum",
            "Ausschuss_Rate": "mean",
            "Energieverbrauch_kWh": "sum",
            "Temperatur_C": "mean",
        }
    )
    .round(2)
)

daily_production.index = pd.to_datetime(daily_production.index)
daily_production["Produktivitaet"] = (
    daily_production["Stückzahl"] / daily_production["Produktionszeit_h"]
).round(2)

print("📅 TÄGLICHE PRODUKTION (erste 10 Tage):")
print(daily_production.head(10))

print(
    f"\\nZeitraum: {daily_production.index.min().date()} bis {daily_production.index.max().date()}"
)
print(
    f"Durchschnittliche tägliche Produktion: {daily_production['Stückzahl'].mean():.0f} Stück"
)

print("\\nb) Wöchentliches Resampling:")
# IHRE LÖSUNG HIER:
weekly_production = (
    df_time.resample("W")
    .agg(
        {
            "Produktionszeit_h": "sum",
            "Stückzahl": "sum",
            "Ausschuss_Rate": "mean",
            "Energieverbrauch_kWh": "sum",
            "Temperatur_C": "mean",
            "Wartung_Score": "mean",
        }
    )
    .round(2)
)

# Zusätzliche wöchentliche KPIs
weekly_production["Produktivitaet"] = (
    weekly_production["Stückzahl"] / weekly_production["Produktionszeit_h"]
).round(2)

weekly_production["Energie_Effizienz"] = (
    weekly_production["Energieverbrauch_kWh"] / weekly_production["Stückzahl"]
).round(3)

print("📊 WÖCHENTLICHE AGGREGATE:")
print(weekly_production)

# Wöchentliche Trends
print("\\n📈 Wöchentliche Entwicklung:")
for col in ["Stückzahl", "Ausschuss_Rate", "Produktivitaet"]:
    if col in weekly_production.columns:
        first_week = weekly_production[col].iloc[0]
        last_week = weekly_production[col].iloc[-1]
        if first_week != 0:
            trend = (last_week - first_week) / first_week * 100
            print(f"  {col}: {trend:+.2f}%")

print("\\nc) Gleitende Durchschnitte berechnen:")
# IHRE LÖSUNG HIER:
# 7-Tage gleitender Durchschnitt
daily_production["Stückzahl_MA7"] = (
    daily_production["Stückzahl"].rolling(window=7, center=True).mean().round(2)
)

# 14-Tage gleitender Durchschnitt
daily_production["Stückzahl_MA14"] = (
    daily_production["Stückzahl"].rolling(window=14, center=True).mean().round(2)
)

# Exponentieller gleitender Durchschnitt
daily_production["Stückzahl_EMA"] = (
    daily_production["Stückzahl"].ewm(span=7).mean().round(2)
)

print("📈 GLEITENDE DURCHSCHNITTE (erste 20 Tage):")
ma_columns = ["Stückzahl", "Stückzahl_MA7", "Stückzahl_MA14", "Stückzahl_EMA"]
print(daily_production[ma_columns].head(20))

# Trend-Erkennung mit gleitenden Durchschnitten
recent_trend = (
    daily_production["Stückzahl_MA7"].iloc[-5:].mean()
    - daily_production["Stückzahl_MA7"].iloc[-10:-5].mean()
)
print(
    f"\\n🔍 Kurzfristiger Trend (letzte 5 vs. vorherige 5 Tage): {recent_trend:+.2f} Stück/Tag"
)

print("\\nd) Saisonale Muster und Trends:")
# IHRE LÖSUNG HIER:
# Wochentags-Analyse
df_time["Wochentag_Num"] = df_time.index.dayofweek  # 0=Montag, 6=Sonntag
wochentag_pattern = (
    df_time.groupby("Wochentag_Num")
    .agg({"Produktionszeit_h": "mean", "Stückzahl": "mean", "Ausschuss_Rate": "mean"})
    .round(2)
)

# Wochentags-Namen hinzufügen
wochentag_namen = [
    "Montag",
    "Dienstag",
    "Mittwoch",
    "Donnerstag",
    "Freitag",
    "Samstag",
    "Sonntag",
]
wochentag_pattern["Wochentag"] = [wochentag_namen[i] for i in wochentag_pattern.index]
wochentag_pattern = wochentag_pattern.set_index("Wochentag")

print("📅 WOCHENTAGS-MUSTER:")
print(wochentag_pattern)

# Stunden-Analyse (Produktionsverteilung über den Tag)
stunden_pattern = (
    df_time.groupby(df_time.index.hour)
    .agg({"Produktionszeit_h": "mean", "Stückzahl": "mean", "Ausschuss_Rate": "mean"})
    .round(2)
)

print("\\n🕐 STUNDEN-MUSTER (Auswahl: 6-22 Uhr):")
print(stunden_pattern.loc[6:22])

# Spitzenstunden identifizieren
beste_stunde_prod = stunden_pattern["Stückzahl"].idxmax()
schlechteste_stunde_qual = stunden_pattern["Ausschuss_Rate"].idxmax()
print(f"\\n🏆 Produktivste Stunde: {beste_stunde_prod:02d}:00 Uhr")
print(f"⚠️ Schlechteste Qualität: {schlechteste_stunde_qual:02d}:00 Uhr")

# Monatliche Trends
monthly_comparison = (
    df_time.groupby(df_time.index.month)
    .agg({"Produktionszeit_h": "sum", "Stückzahl": "sum", "Ausschuss_Rate": "mean"})
    .round(2)
)

monthly_comparison.index = ["Januar", "Februar", "März"][: len(monthly_comparison)]
print("\\n📆 MONATLICHE ENTWICKLUNG:")
print(monthly_comparison)

# Validierung
try:
    assert len(daily_production) > 10, "Sollte mindestens 10 Tage Daten haben"
    assert (
        "Stückzahl_MA7" in daily_production.columns
    ), "Sollte gleitenden Durchschnitt haben"
    assert len(wochentag_pattern) == 7, "Sollte alle 7 Wochentage haben"
    print("\\n✅ Aufgabe 3 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 3: {e}")

# =============================================================================
# AUFGABE 4: JOIN-Operationen mit Stammdaten (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 4: JOIN-Operationen mit Stammdaten")
print("-" * 40)

print(
    """
TODO: Führen Sie verschiedene JOIN-Operationen durch:

a) Verknüpfen Sie Produktionsdaten mit Maschinenstamm
b) Joinen Sie Produktdaten für Kosten-Analyse
c) Ergänzen Sie Kostenstellen-Informationen
d) Erstellen Sie einen vollständig angereicherten Datensatz
"""
)

print("a) Produktionsdaten mit Maschinenstamm verknüpfen:")
# IHRE LÖSUNG HIER:
df_enriched = df_produktion.merge(df_maschinen, on="Maschine", how="left")

print(f"✅ Maschinenstamm-JOIN: {len(df_enriched)} Datensätze")
print("Neue Spalten durch JOIN:")
neue_spalten_maschinen = [
    col for col in df_enriched.columns if col not in df_produktion.columns
]
print(f"  {neue_spalten_maschinen}")

# Erweiterte Berechnungen mit Maschinendaten
df_enriched["Auslastung_Prozent"] = (
    df_enriched["Stückzahl"] / df_enriched["Max_Stueck_pro_h"] * 100
).round(2)

df_enriched["Energiekosten_Euro"] = (
    df_enriched["Energieverbrauch_kWh"] * df_enriched["Energiekosten_pro_kWh"]
).round(2)

print("\\n💡 Erweiterte Kennzahlen (erste 5 Zeilen):")
print(
    df_enriched[
        [
            "Maschine",
            "Stückzahl",
            "Max_Stueck_pro_h",
            "Auslastung_Prozent",
            "Energiekosten_Euro",
        ]
    ].head()
)

print("\\nb) Produktdaten für Kosten-Analyse joinen:")
# IHRE LÖSUNG HIER:
df_enriched = df_enriched.merge(df_produkte, on="Produkt", how="left")

print(f"✅ Produktstamm-JOIN: {len(df_enriched)} Datensätze")
print("Neue Spalten durch Produkt-JOIN:")
neue_spalten_produkte = [
    col
    for col in df_enriched.columns
    if col not in df_produktion.columns and col not in df_maschinen.columns
]
print(f"  {neue_spalten_produkte}")

# Kosten- und Erlös-Berechnungen
df_enriched["Umsatz_Euro"] = (
    df_enriched["Stückzahl"] * df_enriched["Verkaufspreis_Euro"]
).round(2)

df_enriched["Materialkosten_Total"] = (
    df_enriched["Stückzahl"] * df_enriched["Materialkosten_Euro"]
).round(2)

df_enriched["Deckungsbeitrag_Euro"] = (
    df_enriched["Umsatz_Euro"]
    - df_enriched["Materialkosten_Total"]
    - df_enriched["Energiekosten_Euro"]
).round(2)

# Qualitäts-Compliance prüfen
df_enriched["Qualitaet_OK"] = (
    df_enriched["Ausschuss_Rate"] <= df_enriched["Zielausschuss_max"]
)

print("\\n💰 Kosten-Analyse (erste 5 Zeilen):")
cost_columns = [
    "Produkt",
    "Stückzahl",
    "Umsatz_Euro",
    "Materialkosten_Total",
    "Energiekosten_Euro",
    "Deckungsbeitrag_Euro",
]
print(df_enriched[cost_columns].head())

print("\\nc) Kostenstellen-Informationen ergänzen:")
# IHRE LÖSUNG HIER:
df_enriched = df_enriched.merge(df_kostenstellen, on="Halle", how="left")

print(f"✅ Kostenstellen-JOIN: {len(df_enriched)} Datensätze")

# Overhead-Kosten berechnen
df_enriched["Overhead_Kosten"] = (
    df_enriched["Energiekosten_Euro"] * df_enriched["Overhead_Faktor"]
).round(2)

df_enriched["Deckungsbeitrag_nach_Overhead"] = (
    df_enriched["Deckungsbeitrag_Euro"] - df_enriched["Overhead_Kosten"]
).round(2)

print("\\n🏢 Kostenstellen-Analyse:")
kostenstellen_summary = (
    df_enriched.groupby(["Halle", "Kostenstelle", "Hallenleiter"])
    .agg(
        {
            "Umsatz_Euro": "sum",
            "Deckungsbeitrag_Euro": "sum",
            "Overhead_Kosten": "sum",
            "Deckungsbeitrag_nach_Overhead": "sum",
        }
    )
    .round(2)
)
print(kostenstellen_summary)

print("\\nd) Vollständig angereicherter Datensatz:")
# IHRE LÖSUNG HIER:
print("📊 FINALER DATENSATZ:")
print(f"Zeilen: {len(df_enriched):,}")
print(f"Spalten: {len(df_enriched.columns)}")

# ROI-Analyse pro Maschine
roi_analyse = (
    df_enriched.groupby(["Maschine", "Anschaffungswert_Euro"])
    .agg(
        {
            "Deckungsbeitrag_nach_Overhead": "sum",
            "Produktionszeit_h": "sum",
            "Stückzahl": "sum",
        }
    )
    .round(2)
)

roi_analyse["ROI_Prozent"] = (
    roi_analyse["Deckungsbeitrag_nach_Overhead"]
    / roi_analyse.index.get_level_values("Anschaffungswert_Euro")
    * 100
).round(2)

roi_analyse["DB_pro_Stunde"] = (
    roi_analyse["Deckungsbeitrag_nach_Overhead"] / roi_analyse["Produktionszeit_h"]
).round(2)

print("\\n💹 ROI-ANALYSE PRO MASCHINE:")
print(roi_analyse)

# Top-Performer identifizieren
beste_maschine_roi = roi_analyse["ROI_Prozent"].idxmax()
beste_maschine_db_stunde = roi_analyse["DB_pro_Stunde"].idxmax()
print(f"\\n🏆 Beste Maschine (ROI): {beste_maschine_roi[0]}")
print(f"🏆 Beste Maschine (DB/Stunde): {beste_maschine_db_stunde[0]}")

# Data Quality Check nach JOINs
missing_after_joins = df_enriched.isnull().sum()
kritische_fehlende = missing_after_joins[missing_after_joins > 0]

if len(kritische_fehlende) > 0:
    print("\\n⚠️ Fehlende Werte nach JOINs:")
    print(kritische_fehlende)
else:
    print("\\n✅ Keine fehlenden Werte nach JOINs")

# Validierung
try:
    assert (
        "Anschaffungswert_Euro" in df_enriched.columns
    ), "Sollte Maschinenstamm-Daten haben"
    assert (
        "Verkaufspreis_Euro" in df_enriched.columns
    ), "Sollte Produktstamm-Daten haben"
    assert "Kostenstelle" in df_enriched.columns, "Sollte Kostenstellen-Daten haben"
    assert len(df_enriched) == len(df_produktion), "JOIN sollte keine Zeilen verlieren"
    print("\\n✅ Aufgabe 4 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 4: {e}")

# =============================================================================
# AUFGABE 5: Statistische Analysen und Korrelationen (10 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 5: Statistische Analysen und Korrelationen")
print("-" * 40)

print(
    """
TODO: Führen Sie statistische Analysen durch:

a) Berechnen Sie Korrelationsmatrix für numerische Variablen
b) Identifizieren Sie starke Korrelationen
c) Führen Sie Ausreisser-Analyse durch
d) Erstellen Sie deskriptive Statistiken nach Kategorien
"""
)

print("a) Korrelationsmatrix berechnen:")
# IHRE LÖSUNG HIER:
# Numerische Spalten auswählen
numeric_columns = df_enriched.select_dtypes(include=[np.number]).columns.tolist()
# Irrelevante Spalten entfernen
exclude_cols = ["Timestamp", "KW", "Monat", "Quartal", "Baujahr"]
numeric_columns = [col for col in numeric_columns if col not in exclude_cols]

correlation_matrix = df_enriched[numeric_columns].corr().round(3)

print("📊 KORRELATIONSMATRIX (Auswahl wichtiger Variablen):")
# Nur wichtigste Variablen anzeigen
wichtige_vars = [
    "Produktionszeit_h",
    "Stückzahl",
    "Ausschuss_Rate",
    "Temperatur_C",
    "Energieverbrauch_kWh",
    "Umsatz_Euro",
    "Deckungsbeitrag_Euro",
]
wichtige_vars = [var for var in wichtige_vars if var in correlation_matrix.columns]

print(correlation_matrix.loc[wichtige_vars, wichtige_vars])

print("\\nb) Starke Korrelationen identifizieren:")
# IHRE LÖSUNG HIER:
starke_korrelationen = []

for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > 0.5:  # Starke Korrelation
            starke_korrelationen.append(
                {
                    "Variable_1": correlation_matrix.columns[i],
                    "Variable_2": correlation_matrix.columns[j],
                    "Korrelation": corr_value,
                    "Stärke": "Stark" if abs(corr_value) > 0.7 else "Mittel",
                }
            )

if starke_korrelationen:
    korr_df = pd.DataFrame(starke_korrelationen)
    korr_df = korr_df.sort_values("Korrelation", key=abs, ascending=False)
    print("🔍 STARKE KORRELATIONEN (|r| > 0.5):")
    print(korr_df.head(10))

    print("\\n📈 Interpretation wichtiger Korrelationen:")
    for _, row in korr_df.head(5).iterrows():
        richtung = "positiv" if row["Korrelation"] > 0 else "negativ"
        print(
            f"  • {row['Variable_1']} ↔ {row['Variable_2']}: {richtung} ({row['Korrelation']:.3f})"
        )
else:
    print("Keine starken Korrelationen gefunden")

print("\\nc) Ausreisser-Analyse:")


# IHRE LÖSUNG HIER:
def identify_outliers_iqr(series, column_name):
    """Identifiziert Ausreisser mit IQR-Methode"""
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers_mask = (series < lower_bound) | (series > upper_bound)
    outliers_count = outliers_mask.sum()

    return {
        "column": column_name,
        "outliers_count": outliers_count,
        "outliers_percent": (outliers_count / len(series) * 100),
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "outliers_mask": outliers_mask,
    }


print("🚨 AUSREISSER-ANALYSE:")
outlier_results = {}
analyse_vars = [
    "Produktionszeit_h",
    "Stückzahl",
    "Ausschuss_Rate",
    "Temperatur_C",
    "Deckungsbeitrag_Euro",
]

for var in analyse_vars:
    if var in df_enriched.columns:
        result = identify_outliers_iqr(df_enriched[var].dropna(), var)
        outlier_results[var] = result

        if result["outliers_count"] > 0:
            print(f"\\n{var}:")
            print(
                f"  Ausreisser: {result['outliers_count']:,} ({result['outliers_percent']:.2f}%)"
            )
            print(
                f"  Normale Bandbreite: {result['lower_bound']:.2f} bis {result['upper_bound']:.2f}"
            )

            # Top Ausreisser zeigen
            outliers_data = df_enriched.loc[
                result["outliers_mask"], ["Maschine", "Produkt", var]
            ].nlargest(3, var)
            if not outliers_data.empty:
                print("  Top Ausreisser:")
                for _, row in outliers_data.iterrows():
                    print(f"    {row['Maschine']} - {row['Produkt']}: {row[var]}")

print("\\nd) Deskriptive Statistiken nach Kategorien:")
# IHRE LÖSUNG HIER:
print("📊 STATISTIKEN NACH MASCHINENTYP:")
stats_by_typ = (
    df_enriched.groupby("Typ")
    .agg(
        {
            "Produktionszeit_h": ["count", "mean", "std"],
            "Stückzahl": ["mean", "std"],
            "Ausschuss_Rate": ["mean", "min", "max"],
            "Deckungsbeitrag_Euro": ["mean", "sum"],
            "Auslastung_Prozent": "mean",
        }
    )
    .round(3)
)

stats_by_typ.columns = ["_".join(col) for col in stats_by_typ.columns]
print(stats_by_typ)

print("\\n📊 STATISTIKEN NACH PRODUKTKATEGORIE:")
stats_by_kategorie = (
    df_enriched.groupby("Produktkategorie")
    .agg(
        {
            "Stückzahl": ["count", "mean"],
            "Ausschuss_Rate": ["mean", "std"],
            "Umsatz_Euro": ["mean", "sum"],
            "Deckungsbeitrag_Euro": ["mean", "sum"],
        }
    )
    .round(3)
)

stats_by_kategorie.columns = ["_".join(col) for col in stats_by_kategorie.columns]
print(stats_by_kategorie)

# Statistische Tests (einfache Varianzanalyse)
print("\\n🔬 VARIANZANALYSE:")
kategorien = ["Typ", "Halle", "Schicht"]
zielvar = "Deckungsbeitrag_Euro"

for kategorie in kategorien:
    if kategorie in df_enriched.columns:
        gruppen_mittel = df_enriched.groupby(kategorie)[zielvar].mean()
        gesamt_mittel = df_enriched[zielvar].mean()

        # Einfache Varianz zwischen Gruppen
        zwischen_varianz = sum(
            [(mittel - gesamt_mittel) ** 2 for mittel in gruppen_mittel]
        ) / len(gruppen_mittel)

        print(f"{kategorie}:")
        print(f"  Varianz zwischen Gruppen: {zwischen_varianz:.2f}")
        print(
            f"  Spannweite der Mittelwerte: {gruppen_mittel.max() - gruppen_mittel.min():.2f}"
        )

# Validierung
try:
    assert len(correlation_matrix) > 5, "Sollte mehrere Variablen korreliert haben"
    assert len(outlier_results) > 0, "Sollte Ausreisser-Analyse durchgeführt haben"
    assert len(stats_by_typ) > 0, "Sollte Statistiken nach Typ haben"
    print("\\n✅ Aufgabe 5 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 5: {e}")

# =============================================================================
# AUFGABE 6: Comprehensive Business Intelligence Report (10 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 6: Comprehensive Business Intelligence Report")
print("-" * 40)

print(
    """
TODO: Erstellen Sie einen umfassenden BI-Report:

a) Management Summary mit KPIs
b) Produktionseffizienz-Analyse
c) Kosten- und Rentabilitätsanalyse
d) Handlungsempfehlungen ableiten
"""
)

print("a) Management Summary mit KPIs:")


# IHRE LÖSUNG HIER:
def create_management_summary(df):
    """Erstellt Management Summary mit wichtigsten KPIs"""

    # Zeitraum
    zeitraum_tage = (df["Timestamp"].max() - df["Timestamp"].min()).days

    # Produktions-KPIs
    kpis = {
        "Berichtszeitraum_Tage": zeitraum_tage,
        "Gesamtumsatz_Euro": df["Umsatz_Euro"].sum(),
        "Gesamtdeckungsbeitrag_Euro": df["Deckungsbeitrag_nach_Overhead"].sum(),
        "DB_Marge_Prozent": (
            df["Deckungsbeitrag_nach_Overhead"].sum() / df["Umsatz_Euro"].sum() * 100
        ),
        "Produktionsstunden_Total": df["Produktionszeit_h"].sum(),
        "Stückzahl_Total": df["Stückzahl"].sum(),
        "Durchschnitt_Ausschuss_Prozent": (df["Ausschuss_Rate"].mean() * 100),
        "Energiekosten_Total_Euro": df["Energiekosten_Euro"].sum(),
        "Durchschnitt_Auslastung_Prozent": df["Auslastung_Prozent"].mean(),
        "Anzahl_Maschinen": df["Maschine"].nunique(),
        "Anzahl_Produkte": df["Produkt"].nunique(),
        "Produktivitaet_Stueck_pro_h": (
            df["Stückzahl"].sum() / df["Produktionszeit_h"].sum()
        ),
    }

    return kpis


management_kpis = create_management_summary(df_enriched)

print("🎯 MANAGEMENT SUMMARY - KEY PERFORMANCE INDICATORS:")
print("=" * 55)
print(f"📅 Berichtszeitraum: {management_kpis['Berichtszeitraum_Tage']} Tage")
print(f"💰 Gesamtumsatz: €{management_kpis['Gesamtumsatz_Euro']:,.2f}")
print(f"📊 Deckungsbeitrag: €{management_kpis['Gesamtdeckungsbeitrag_Euro']:,.2f}")
print(f"📈 DB-Marge: {management_kpis['DB_Marge_Prozent']:.2f}%")
print(f"⏱️ Produktionsstunden: {management_kpis['Produktionsstunden_Total']:,.1f}h")
print(f"🔢 Produzierte Stücke: {management_kpis['Stückzahl_Total']:,}")
print(f"⚡ Produktivität: {management_kpis['Produktivitaet_Stueck_pro_h']:.1f} Stück/h")
print(f"🎯 Ausschussrate: {management_kpis['Durchschnitt_Ausschuss_Prozent']:.3f}%")
print(f"🔌 Energiekosten: €{management_kpis['Energiekosten_Total_Euro']:,.2f}")
print(f"📊 Auslastung: {management_kpis['Durchschnitt_Auslastung_Prozent']:.1f}%")

print("\\nb) Produktionseffizienz-Analyse:")
# IHRE LÖSUNG HIER:
# Effizienz-Ranking nach Maschinen
effizienz_ranking = (
    df_enriched.groupby("Maschine")
    .agg(
        {
            "Produktionszeit_h": "sum",
            "Stückzahl": "sum",
            "Deckungsbeitrag_nach_Overhead": "sum",
            "Ausschuss_Rate": "mean",
            "Auslastung_Prozent": "mean",
            "Energiekosten_Euro": "sum",
        }
    )
    .round(2)
)

effizienz_ranking["DB_pro_Stunde"] = (
    effizienz_ranking["Deckungsbeitrag_nach_Overhead"]
    / effizienz_ranking["Produktionszeit_h"]
).round(2)

effizienz_ranking["Stück_pro_Stunde"] = (
    effizienz_ranking["Stückzahl"] / effizienz_ranking["Produktionszeit_h"]
).round(2)

effizienz_ranking["Energiekosten_pro_Stück"] = (
    effizienz_ranking["Energiekosten_Euro"] / effizienz_ranking["Stückzahl"]
).round(3)

# Effizienz-Score berechnen (gewichteter Index)
effizienz_ranking["Effizienz_Score"] = (
    effizienz_ranking["DB_pro_Stunde"] / effizienz_ranking["DB_pro_Stunde"].max() * 0.4
    + effizienz_ranking["Stück_pro_Stunde"]
    / effizienz_ranking["Stück_pro_Stunde"].max()
    * 0.3
    + (
        1
        - effizienz_ranking["Ausschuss_Rate"]
        / effizienz_ranking["Ausschuss_Rate"].max()
    )
    * 0.3
).round(3)

effizienz_ranking_sorted = effizienz_ranking.sort_values(
    "Effizienz_Score", ascending=False
)

print("🏭 PRODUKTIONSEFFIZIENZ-RANKING:")
print(
    effizienz_ranking_sorted[
        ["DB_pro_Stunde", "Stück_pro_Stunde", "Ausschuss_Rate", "Effizienz_Score"]
    ]
)

# Top und Bottom Performer
top_performer = effizienz_ranking_sorted.index[0]
bottom_performer = effizienz_ranking_sorted.index[-1]
print(
    f"\\n🥇 Top Performer: {top_performer} (Score: {effizienz_ranking_sorted.iloc[0]['Effizienz_Score']:.3f})"
)
print(
    f"🔴 Bottom Performer: {bottom_performer} (Score: {effizienz_ranking_sorted.iloc[-1]['Effizienz_Score']:.3f})"
)

print("\\nc) Kosten- und Rentabilitätsanalyse:")
# IHRE LÖSUNG HIER:
# Rentabilität nach Produkten
produkt_rentabilitaet = (
    df_enriched.groupby(["Produkt", "Produktkategorie"])
    .agg(
        {
            "Stückzahl": "sum",
            "Umsatz_Euro": "sum",
            "Materialkosten_Total": "sum",
            "Energiekosten_Euro": "sum",
            "Overhead_Kosten": "sum",
            "Deckungsbeitrag_nach_Overhead": "sum",
        }
    )
    .round(2)
)

produkt_rentabilitaet["DB_Marge_Prozent"] = (
    produkt_rentabilitaet["Deckungsbeitrag_nach_Overhead"]
    / produkt_rentabilitaet["Umsatz_Euro"]
    * 100
).round(2)

produkt_rentabilitaet["DB_pro_Stück"] = (
    produkt_rentabilitaet["Deckungsbeitrag_nach_Overhead"]
    / produkt_rentabilitaet["Stückzahl"]
).round(2)

produkt_rentabilitaet_sorted = produkt_rentabilitaet.sort_values(
    "DB_Marge_Prozent", ascending=False
)

print("💰 PRODUKT-RENTABILITÄTSANALYSE:")
print(
    produkt_rentabilitaet_sorted[
        [
            "Stückzahl",
            "Umsatz_Euro",
            "Deckungsbeitrag_nach_Overhead",
            "DB_Marge_Prozent",
            "DB_pro_Stück",
        ]
    ]
)

# Kosten-Hotspots identifizieren
print("\\n🔥 KOSTEN-HOTSPOTS:")
gesamt_energiekosten = df_enriched["Energiekosten_Euro"].sum()
gesamt_materialkosten = df_enriched["Materialkosten_Total"].sum()
gesamt_overhead = df_enriched["Overhead_Kosten"].sum()

print(
    f"Materialkosten: €{gesamt_materialkosten:,.2f} ({gesamt_materialkosten / (gesamt_materialkosten + gesamt_energiekosten + gesamt_overhead) * 100:.1f}%)"
)
print(
    f"Energiekosten: €{gesamt_energiekosten:,.2f} ({gesamt_energiekosten / (gesamt_materialkosten + gesamt_energiekosten + gesamt_overhead) * 100:.1f}%)"
)
print(
    f"Overhead-Kosten: €{gesamt_overhead:,.2f} ({gesamt_overhead / (gesamt_materialkosten + gesamt_energiekosten + gesamt_overhead) * 100:.1f}%)"
)

print("\\nd) Handlungsempfehlungen ableiten:")


# IHRE LÖSUNG HIER:
def generate_recommendations(df, effizienz_ranking, produkt_rentabilitaet):
    """Generiert datenbasierte Handlungsempfehlungen"""

    empfehlungen = []

    # 1. Effizienz-basierte Empfehlungen
    ineffiziente_maschinen = effizienz_ranking[
        effizienz_ranking["Effizienz_Score"] < 0.6
    ]
    if not ineffiziente_maschinen.empty:
        for maschine in ineffiziente_maschinen.index:
            score = ineffiziente_maschinen.loc[maschine, "Effizienz_Score"]
            empfehlungen.append(
                {
                    "Kategorie": "Effizienz",
                    "Priorität": "Hoch",
                    "Empfehlung": f"Wartung/Optimierung für {maschine} (Effizienz-Score: {score:.3f})",
                    "Erwarteter_Nutzen": "Produktivitätssteigerung 10-20%",
                }
            )

    # 2. Qualitäts-basierte Empfehlungen
    hoher_ausschuss = df.groupby("Produkt")["Ausschuss_Rate"].mean()
    kritische_produkte = hoher_ausschuss[hoher_ausschuss > 0.04]  # > 4%
    for produkt in kritische_produkte.index:
        rate = kritische_produkte[produkt]
        empfehlungen.append(
            {
                "Kategorie": "Qualität",
                "Priorität": "Hoch",
                "Empfehlung": f"Qualitätsverbesserung für {produkt} (Ausschuss: {rate:.3%})",
                "Erwarteter_Nutzen": "Kostenreduktion durch weniger Ausschuss",
            }
        )

    # 3. Rentabilitäts-basierte Empfehlungen
    niedrige_marge = produkt_rentabilitaet[
        produkt_rentabilitaet["DB_Marge_Prozent"] < 20
    ]
    if not niedrige_marge.empty:
        for produkt in niedrige_marge.index:
            marge = niedrige_marge.loc[produkt, "DB_Marge_Prozent"]
            empfehlungen.append(
                {
                    "Kategorie": "Rentabilität",
                    "Priorität": "Mittel",
                    "Empfehlung": f"Preisanpassung oder Kostensenkung für {produkt[0]} (DB-Marge: {marge:.1f}%)",
                    "Erwarteter_Nutzen": "Verbesserung der Gesamtrentabilität",
                }
            )

    # 4. Energie-Effizienz Empfehlungen
    hohe_energiekosten = effizienz_ranking["Energiekosten_pro_Stück"].quantile(0.8)
    energie_ineffizient = effizienz_ranking[
        effizienz_ranking["Energiekosten_pro_Stück"] > hohe_energiekosten
    ]

    for maschine in energie_ineffizient.index:
        kosten = energie_ineffizient.loc[maschine, "Energiekosten_pro_Stück"]
        empfehlungen.append(
            {
                "Kategorie": "Energie",
                "Priorität": "Mittel",
                "Empfehlung": f"Energieeffizienz-Optimierung für {maschine} (€{kosten:.3f}/Stück)",
                "Erwarteter_Nutzen": "Reduzierung Energiekosten um 5-15%",
            }
        )

    return pd.DataFrame(empfehlungen)


empfehlungen_df = generate_recommendations(
    df_enriched, effizienz_ranking, produkt_rentabilitaet
)

print("🎯 HANDLUNGSEMPFEHLUNGEN:")
print("=" * 50)

if not empfehlungen_df.empty:
    for prioritaet in ["Hoch", "Mittel", "Niedrig"]:
        prio_empfehlungen = empfehlungen_df[empfehlungen_df["Priorität"] == prioritaet]
        if not prio_empfehlungen.empty:
            print(f"\\n{prioritaet} Priorität:")
            for _, emp in prio_empfehlungen.iterrows():
                print(f"  📋 {emp['Kategorie']}: {emp['Empfehlung']}")
                print(f"     💡 {emp['Erwarteter_Nutzen']}")

# Business Impact Schätzung
print("\\n💼 GESCHÄFTS-IMPACT SCHÄTZUNG:")
verbesserungs_potenzial = {
    "Effizienz_Steigerung": management_kpis["Gesamtdeckungsbeitrag_Euro"]
    * 0.15,  # 15% durch Effizienz
    "Qualitaets_Verbesserung": management_kpis["Gesamtumsatz_Euro"]
    * 0.02,  # 2% durch weniger Ausschuss
    "Energie_Einsparung": management_kpis["Energiekosten_Total_Euro"]
    * 0.10,  # 10% Energie-Einsparung
}

gesamt_potenzial = sum(verbesserungs_potenzial.values())
print(f"Geschätztes Verbesserungspotenzial: €{gesamt_potenzial:,.2f} pro Quartal")
print(
    f"Das entspricht {gesamt_potenzial / management_kpis['Gesamtumsatz_Euro'] * 100:.1f}% des Quartalsumsatzes"
)

# Validierung
try:
    assert management_kpis["Gesamtumsatz_Euro"] > 0, "Sollte Umsatz-KPIs haben"
    assert len(effizienz_ranking) > 0, "Sollte Effizienz-Ranking haben"
    assert not empfehlungen_df.empty, "Sollte Handlungsempfehlungen haben"
    print("\\n✅ Aufgabe 6 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\\n❌ Fehler in Aufgabe 6: {e}")

# =============================================================================
# ZUSAMMENFASSUNG UND EXPORT
# =============================================================================

print("\n" + "=" * 60)
print("🎯 ÜBUNG 4 ABGESCHLOSSEN")
print("=" * 60)

print("\\n📊 FINALE ANALYSE-ZUSAMMENFASSUNG:")
print(f"• Datensätze analysiert: {len(df_enriched):,}")
print(f"• Zeitraum: {management_kpis['Berichtszeitraum_Tage']} Tage")
print(f"• Gesamtumsatz: €{management_kpis['Gesamtumsatz_Euro']:,.2f}")
print(f"• Deckungsbeitrag: €{management_kpis['Gesamtdeckungsbeitrag_Euro']:,.2f}")
print(f"• Produktivität: {management_kpis['Produktivitaet_Stueck_pro_h']:.1f} Stück/h")
print(
    f"• Durchschnittliche Auslastung: {management_kpis['Durchschnitt_Auslastung_Prozent']:.1f}%"
)

print("\\n✅ LERNZIELE ERREICHT:")
print("• Multi-dimensionale Gruppierungen und Aggregationen")
print("• Komplexe Pivot-Tabellen für verschiedene Analysen")
print("• Zeitreihenanalyse mit Resampling und gleitenden Durchschnitten")
print("• Statistische Analysen und Korrelationsuntersuchungen")
print("• JOIN-Operationen mit mehreren Stammdaten-Tabellen")
print("• Umfassendes Business Intelligence Reporting")
print("• Datenbasierte Handlungsempfehlungen")

# Export der Analyse-Ergebnisse
print("\\n💾 EXPORT DER ANALYSE-ERGEBNISSE:")

# 1. Management Summary
management_summary_df = pd.DataFrame([management_kpis]).T
management_summary_df.columns = ["Wert"]
management_summary_df.to_csv("data/generated/management_summary.csv", encoding="utf-8")
print("✅ management_summary.csv")

# 2. Effizienz-Ranking
effizienz_ranking_sorted.to_csv(
    "data/generated/effizienz_ranking.csv", encoding="utf-8"
)
print("✅ effizienz_ranking.csv")

# 3. Produkt-Rentabilität
produkt_rentabilitaet_sorted.to_csv(
    "data/generated/produkt_rentabilitaet.csv", encoding="utf-8"
)
print("✅ produkt_rentabilitaet.csv")

# 4. Handlungsempfehlungen
empfehlungen_df.to_csv(
    "data/generated/handlungsempfehlungen.csv", index=False, encoding="utf-8"
)
print("✅ handlungsempfehlungen.csv")

# 5. Vollständiger angereicherter Datensatz (Stichprobe)
df_enriched.sample(1000).to_csv(
    "data/generated/angereicherte_produktionsdaten_stichprobe.csv",
    index=False,
    encoding="utf-8",
)
print("✅ angereicherte_produktionsdaten_stichprobe.csv")

print("\\n🎓 NÄCHSTE SCHRITTE:")
print("• Dashboard-Entwicklung mit Streamlit oder Dash")
print("• Machine Learning für Predictive Analytics")
print("• Real-time Analytics mit Apache Kafka")
print("• Advanced Visualization mit Plotly/Matplotlib")

print("\\n💡 Als Bystronic-Entwickler beherrschen Sie jetzt")
print("   professionelle Datenanalyse und Business Intelligence!")
print("   Sie können umfassende Produktionsdaten-Analysen")
print("   durchführen und strategische Entscheidungen datenbasiert unterstützen.")
