#!/usr/bin/env python3
"""
Datenanalyse - Pandas Tutorial für Bystronic

Dieses Beispiel demonstriert fortgeschrittene Datenanalysemethoden:
- Gruppierungen und Aggregationen
- Pivot-Tabellen
- Zeitreihenanalyse
- Statistische Auswertungen
- Join-Operationen

Für Bystronic-Entwickler: Produktionsdaten analysieren und Insights gewinnen
"""

import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")

print("=" * 60)
print("📊 PANDAS DATENANALYSE")
print("=" * 60)


# Umfassende Beispieldaten für Analysen erstellen
def create_analysis_data():
    """Erstelle realistische Produktionsdaten für Analysen"""
    np.random.seed(42)

    # Basis-Setup
    start_date = pd.Timestamp("2024-01-01")
    end_date = pd.Timestamp("2024-03-31")
    date_range = pd.date_range(start_date, end_date, freq="D")

    maschinen = [
        {"name": "Laser_01", "typ": "ByStar", "halle": "A", "kapazitaet": 10},
        {"name": "Laser_02", "typ": "ByStar", "halle": "A", "kapazitaet": 10},
        {"name": "Presse_01", "typ": "Xpert", "halle": "B", "kapazitaet": 8},
        {"name": "Presse_02", "typ": "Xpert", "halle": "B", "kapazitaet": 8},
        {"name": "Stanze_01", "typ": "ByTrans", "halle": "C", "kapazitaet": 6},
    ]

    schichten = ["Früh", "Spät", "Nacht"]
    produkte = ["Teil_A", "Teil_B", "Teil_C", "Teil_D"]

    # Produktionsdaten generieren
    produktionsdaten = []
    for date in date_range:
        for maschine in maschinen:
            for schicht in schichten:
                # Nicht jede Schicht läuft (90% Wahrscheinlichkeit)
                if np.random.random() < 0.9:
                    # Basis-Produktionszeit mit Maschinen-spezifischen Faktoren
                    basis_zeit = np.random.uniform(
                        maschine["kapazitaet"] * 0.6, maschine["kapazitaet"] * 0.95
                    )

                    # Schicht-spezifische Faktoren
                    schicht_faktoren = {"Früh": 1.0, "Spät": 0.9, "Nacht": 0.8}
                    produktionszeit = basis_zeit * schicht_faktoren[schicht]

                    # Wochentag-Effekte
                    if date.weekday() >= 5:  # Wochenende
                        produktionszeit *= 0.7

                    # Zufälliges Produkt
                    produkt = np.random.choice(produkte)

                    # Produkt-spezifische Faktoren
                    produkt_faktoren = {
                        "Teil_A": 1.2,
                        "Teil_B": 1.0,
                        "Teil_C": 0.8,
                        "Teil_D": 1.1,
                    }
                    stückzahl = int(produktionszeit * 15 * produkt_faktoren[produkt])

                    # Qualitäts-Parameter
                    ausschuss = np.random.uniform(0.01, 0.06)
                    temperatur = np.random.uniform(18.0, 25.0)

                    # Energie-Parameter (abhängig von Maschinentyp)
                    energie_basis = {"ByStar": 200, "Xpert": 150, "ByTrans": 100}
                    energieverbrauch = energie_basis[maschine["typ"]] * (
                        produktionszeit / maschine["kapazitaet"]
                    ) + np.random.uniform(-20, 20)

                    produktionsdaten.append(
                        {
                            "Datum": date.date(),
                            "Maschine": maschine["name"],
                            "Typ": maschine["typ"],
                            "Halle": maschine["halle"],
                            "Schicht": schicht,
                            "Produkt": produkt,
                            "Produktionszeit": round(produktionszeit, 2),
                            "Stückzahl": stückzahl,
                            "Ausschuss_Rate": round(ausschuss, 4),
                            "Temperatur": round(temperatur, 1),
                            "Energieverbrauch": round(energieverbrauch, 1),
                            "Wochentag": date.strftime("%A"),
                            "KW": date.isocalendar()[1],
                            "Monat": date.month,
                        }
                    )

    return pd.DataFrame(produktionsdaten)


# Zusätzliche Stammdaten
def create_master_data():
    """Erstelle Stammdaten für Joins"""
    maschinen_stamm = pd.DataFrame(
        {
            "Maschine": ["Laser_01", "Laser_02", "Presse_01", "Presse_02", "Stanze_01"],
            "Baujahr": [2019, 2020, 2018, 2021, 2017],
            "Anschaffungswert": [450000, 480000, 320000, 360000, 280000],
            "Wartungsintervall_Tage": [90, 90, 120, 120, 180],
            "Letzte_Wartung": [
                "2024-01-15",
                "2024-02-01",
                "2024-01-10",
                "2024-02-20",
                "2023-12-15",
            ],
        }
    )
    maschinen_stamm["Letzte_Wartung"] = pd.to_datetime(
        maschinen_stamm["Letzte_Wartung"]
    )

    produkt_stamm = pd.DataFrame(
        {
            "Produkt": ["Teil_A", "Teil_B", "Teil_C", "Teil_D"],
            "Material": ["Stahl", "Aluminium", "Edelstahl", "Stahl"],
            "Komplexitaet": ["Hoch", "Mittel", "Niedrig", "Hoch"],
            "Zielpreis_Euro": [12.50, 8.75, 6.20, 15.80],
            "Mindestqualitaet": [0.02, 0.03, 0.05, 0.02],  # Max erlaubte Ausschussrate
        }
    )

    return maschinen_stamm, produkt_stamm


# 1. Daten laden und vorbereiten
print("\n1️⃣ Daten laden und vorbereiten")
print("-" * 40)

df_produktion = create_analysis_data()
df_maschinen, df_produkte = create_master_data()

print(f"Produktionsdaten: {len(df_produktion)} Datensätze")
print(f"Zeitraum: {df_produktion['Datum'].min()} bis {df_produktion['Datum'].max()}")
print(f"Maschinen: {df_produktion['Maschine'].nunique()}")
print(f"Produkte: {df_produktion['Produkt'].nunique()}")

print("\nErste 5 Datensätze:")
print(df_produktion.head())

# Datum als Index setzen für Zeitreihenanalyse
df_time_series = df_produktion.copy()
df_time_series["Datum"] = pd.to_datetime(df_time_series["Datum"])
df_time_series = df_time_series.set_index("Datum")

# 2. Grundlegende Aggregationen
print("\n2️⃣ Grundlegende Aggregationen")
print("-" * 40)

print("📈 Gesamtübersicht:")
gesamt_stats = {
    "Produktionszeit_Gesamt": df_produktion["Produktionszeit"].sum(),
    "Stückzahl_Gesamt": df_produktion["Stückzahl"].sum(),
    "Durchschnitt_Ausschuss": df_produktion["Ausschuss_Rate"].mean(),
    "Energieverbrauch_Gesamt": df_produktion["Energieverbrauch"].sum(),
}

for key, value in gesamt_stats.items():
    if "Rate" in key or "Durchschnitt" in key:
        print(f"{key}: {value:.4f}")
    else:
        print(f"{key}: {value:,.2f}")

print("\n📊 Statistische Kennzahlen:")
print(df_produktion[["Produktionszeit", "Stückzahl", "Ausschuss_Rate"]].describe())

# 3. Gruppierungen nach verschiedenen Dimensionen
print("\n3️⃣ Gruppierungen nach verschiedenen Dimensionen")
print("-" * 40)

print("🏭 Analyse nach Maschinen:")
maschinen_analyse = (
    df_produktion.groupby("Maschine")
    .agg(
        {
            "Produktionszeit": ["sum", "mean", "count"],
            "Stückzahl": "sum",
            "Ausschuss_Rate": ["mean", "std"],
            "Energieverbrauch": "sum",
        }
    )
    .round(2)
)

# Spalten-Namen vereinfachen
maschinen_analyse.columns = ["_".join(col) for col in maschinen_analyse.columns]
print(maschinen_analyse)

print("\n🏢 Analyse nach Hallen:")
hallen_analyse = (
    df_produktion.groupby("Halle")
    .agg({"Produktionszeit": "sum", "Stückzahl": "sum", "Energieverbrauch": "mean"})
    .round(2)
)
print(hallen_analyse)

print("\n⏰ Analyse nach Schichten:")
schicht_analyse = (
    df_produktion.groupby("Schicht")
    .agg({"Produktionszeit": "mean", "Ausschuss_Rate": "mean", "Stückzahl": "mean"})
    .round(2)
)

# Schichten logisch sortieren
schicht_reihenfolge = ["Früh", "Spät", "Nacht"]
schicht_analyse = schicht_analyse.reindex(schicht_reihenfolge)
print(schicht_analyse)

# 4. Mehr-dimensionale Gruppierungen
print("\n4️⃣ Mehr-dimensionale Gruppierungen")
print("-" * 40)

print("🔄 Maschine × Schicht Analyse:")
maschine_schicht = (
    df_produktion.groupby(["Maschine", "Schicht"])["Produktionszeit"]
    .agg(["sum", "count", "mean"])
    .round(2)
)
print(maschine_schicht.head(10))

print("\n📅 Wöchentliche Trends:")
weekly_trends = (
    df_produktion.groupby(["KW", "Typ"])
    .agg({"Produktionszeit": "sum", "Stückzahl": "sum"})
    .round(2)
)
print(weekly_trends.head(10))

# 5. Pivot-Tabellen für komplexe Analysen
print("\n5️⃣ Pivot-Tabellen für komplexe Analysen")
print("-" * 40)

print("📋 Produktionszeit: Maschine × Schicht:")
pivot_prod = df_produktion.pivot_table(
    values="Produktionszeit",
    index="Maschine",
    columns="Schicht",
    aggfunc="sum",
    fill_value=0,
).round(2)
print(pivot_prod)

print("\n📋 Ausschussrate: Halle × Produkt:")
pivot_ausschuss = df_produktion.pivot_table(
    values="Ausschuss_Rate", index="Halle", columns="Produkt", aggfunc="mean"
).round(4)
print(pivot_ausschuss)

print("\n📋 Energieeffizienz (kWh pro Stück):")
df_produktion["Energie_pro_Stück"] = (
    df_produktion["Energieverbrauch"] / df_produktion["Stückzahl"]
)
pivot_effizienz = df_produktion.pivot_table(
    values="Energie_pro_Stück", index="Typ", columns="Produkt", aggfunc="mean"
).round(3)
print(pivot_effizienz)

# 6. Zeitreihenanalyse
print("\n6️⃣ Zeitreihenanalyse")
print("-" * 40)

print("📈 Tägliche Produktionstrends:")
daily_production = (
    df_time_series.groupby(df_time_series.index.date)
    .agg({"Produktionszeit": "sum", "Stückzahl": "sum", "Ausschuss_Rate": "mean"})
    .round(2)
)
print(daily_production.head(10))

print("\n📊 Wöchentliche Aggregate (Resampling):")
weekly_resample = (
    df_time_series.resample("W")
    .agg(
        {
            "Produktionszeit": "sum",
            "Stückzahl": "sum",
            "Ausschuss_Rate": "mean",
            "Energieverbrauch": "sum",
        }
    )
    .round(2)
)
print(weekly_resample.head())

print("\n📅 Monatliche Trends:")
monthly_trends = (
    df_time_series.resample("M")
    .agg({"Produktionszeit": "sum", "Stückzahl": "sum", "Ausschuss_Rate": "mean"})
    .round(2)
)
print(monthly_trends)

# Rolling Windows für gleitende Durchschnitte
print("\n📈 Gleitender 7-Tage Durchschnitt:")
daily_agg = df_time_series.groupby(df_time_series.index.date)["Produktionszeit"].sum()
daily_agg.index = pd.to_datetime(daily_agg.index)
rolling_avg = daily_agg.rolling(window=7, center=True).mean().round(2)
print(rolling_avg.head(10))

# 7. Join-Operationen mit Stammdaten
print("\n7️⃣ Join-Operationen mit Stammdaten")
print("-" * 40)

print("🔗 Join mit Maschinendaten:")
df_enhanced = df_produktion.merge(df_maschinen, on="Maschine", how="left")
print(
    "Zusätzliche Spalten nach Join:",
    [col for col in df_enhanced.columns if col not in df_produktion.columns],
)

print("\n💰 Analyse mit Anschaffungswerten:")
value_analysis = (
    df_enhanced.groupby("Maschine")
    .agg({"Produktionszeit": "sum", "Stückzahl": "sum", "Anschaffungswert": "first"})
    .round(2)
)

# ROI-Berechnung (vereinfacht)
angenommener_stundensatz = 150  # Euro pro Produktionsstunde
value_analysis["Umsatz_YTD"] = (
    value_analysis["Produktionszeit"] * angenommener_stundensatz
)
value_analysis["ROI_Prozent"] = (
    value_analysis["Umsatz_YTD"] / value_analysis["Anschaffungswert"] * 100
).round(2)
print(value_analysis)

print("\n🔗 Join mit Produktdaten:")
df_full = df_enhanced.merge(df_produkte, on="Produkt", how="left")

print("\n✅ Qualitätsanalyse gegen Sollwerte:")
qualitaets_analyse = (
    df_full.groupby("Produkt")
    .agg({"Ausschuss_Rate": ["mean", "std", "min", "max"], "Mindestqualitaet": "first"})
    .round(4)
)

qualitaets_analyse.columns = [
    "_".join(col) if col[1] else col[0] for col in qualitaets_analyse.columns
]

# Qualitätsbewertung
qualitaets_analyse["Qualitaet_OK"] = (
    qualitaets_analyse["Ausschuss_Rate_mean"]
    <= qualitaets_analyse["Mindestqualitaet_first"]
)
print(qualitaets_analyse)

# 8. Erweiterte statistische Analysen
print("\n8️⃣ Erweiterte statistische Analysen")
print("-" * 40)

print("📊 Korrelationsanalyse:")
numeric_cols = [
    "Produktionszeit",
    "Stückzahl",
    "Ausschuss_Rate",
    "Temperatur",
    "Energieverbrauch",
]
correlation_matrix = df_produktion[numeric_cols].corr().round(3)
print(correlation_matrix)

# Starke Korrelationen finden
print("\n🔍 Starke Korrelationen (|r| > 0.5):")
strong_corr = []
for i in range(len(correlation_matrix.columns)):
    for j in range(i + 1, len(correlation_matrix.columns)):
        corr_value = correlation_matrix.iloc[i, j]
        if abs(corr_value) > 0.5:
            strong_corr.append(
                {
                    "Variable_1": correlation_matrix.columns[i],
                    "Variable_2": correlation_matrix.columns[j],
                    "Korrelation": corr_value,
                }
            )

if strong_corr:
    df_strong_corr = pd.DataFrame(strong_corr)
    print(df_strong_corr)
else:
    print("Keine starken Korrelationen gefunden")

# 9. Outlier-Analyse
print("\n9️⃣ Outlier-Analyse")
print("-" * 40)


def find_outliers_iqr(df, column):
    """Findet Outliers mit der IQR-Methode"""
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    return outliers, lower_bound, upper_bound


print("🚨 Ausreisser-Analyse für Produktionszeit:")
outliers_prod, lower_prod, upper_prod = find_outliers_iqr(
    df_produktion, "Produktionszeit"
)
print(f"Normale Bandbreite: {lower_prod:.2f} - {upper_prod:.2f} Stunden")
print(f"Gefundene Ausreisser: {len(outliers_prod)}")

if not outliers_prod.empty:
    print("Top 5 Ausreisser:")
    top_outliers = outliers_prod.nlargest(5, "Produktionszeit")[
        ["Maschine", "Datum", "Schicht", "Produktionszeit"]
    ]
    print(top_outliers)

# 10. Performance-Benchmarking
print("\n🔟 Performance-Benchmarking")
print("-" * 40)

print("🏆 Top-Performer Analyse:")

# Beste Maschinen nach verschiedenen Kriterien
top_performers = {}

# Höchste Produktionszeit
top_prod = (
    df_produktion.groupby("Maschine")["Produktionszeit"]
    .sum()
    .sort_values(ascending=False)
)
top_performers["Produktionszeit"] = top_prod.head(3)

# Niedrigste Ausschussrate
top_quality = df_produktion.groupby("Maschine")["Ausschuss_Rate"].mean().sort_values()
top_performers["Qualitaet"] = top_quality.head(3)

# Höchste Stückzahl
top_volume = (
    df_produktion.groupby("Maschine")["Stückzahl"].sum().sort_values(ascending=False)
)
top_performers["Stueckzahl"] = top_volume.head(3)

for metric, data in top_performers.items():
    print(f"\n🏅 Top 3 bei {metric}:")
    for i, (maschine, wert) in enumerate(data.items(), 1):
        if metric == "Qualitaet":
            print(f"  {i}. {maschine}: {wert:.4f}")
        else:
            print(f"  {i}. {maschine}: {wert:,.2f}")

# 11. Trendanalyse und Forecasting-Vorbereitung
print("\n1️⃣1️⃣ Trendanalyse")
print("-" * 40)

print("📈 Monatliche Entwicklung:")
monthly_dev = (
    df_time_series.groupby(df_time_series.index.to_period("M"))
    .agg({"Produktionszeit": "sum", "Ausschuss_Rate": "mean"})
    .round(2)
)

# Prozentuale Veränderung berechnen
monthly_dev["Prod_Change_%"] = monthly_dev["Produktionszeit"].pct_change() * 100
monthly_dev["Quality_Change_%"] = monthly_dev["Ausschuss_Rate"].pct_change() * 100

print(monthly_dev)

# 12. Zusammenfassender Analysebericht
print("\n1️⃣2️⃣ Zusammenfassender Analysebericht")
print("-" * 40)


def generate_analysis_summary(df):
    """Generiert einen umfassenden Analysebericht"""
    report = {
        "Zeitraum": f"{df['Datum'].min()} bis {df['Datum'].max()}",
        "Datenpunkte": len(df),
        "Produktionszeit_Gesamt_h": df["Produktionszeit"].sum(),
        "Stueckzahl_Gesamt": df["Stückzahl"].sum(),
        "Durchschnitt_Ausschuss_%": (df["Ausschuss_Rate"].mean() * 100),
        "Beste_Maschine_Produktion": df.groupby("Maschine")["Produktionszeit"]
        .sum()
        .idxmax(),
        "Beste_Maschine_Qualitaet": df.groupby("Maschine")["Ausschuss_Rate"]
        .mean()
        .idxmin(),
        "Produktivste_Schicht": df.groupby("Schicht")["Produktionszeit"].sum().idxmax(),
        "Energieeffizienz_kWh_pro_Stueck": (
            df["Energieverbrauch"].sum() / df["Stückzahl"].sum()
        ),
    }
    return report


summary = generate_analysis_summary(df_produktion)
print("📋 Analysebericht:")
for key, value in summary.items():
    if isinstance(value, float):
        print(f"{key}: {value:.2f}")
    else:
        print(f"{key}: {value}")

# Export für weitere Analysen
print("\n💾 Daten für weitere Analysen exportieren:")
export_files = [
    ("produktionsanalyse_zusammenfassung.csv", maschinen_analyse),
    ("pivot_produktionszeit.csv", pivot_prod),
    ("monatliche_trends.csv", monthly_trends),
    ("qualitaetsanalyse.csv", qualitaets_analyse),
]

for filename, dataframe in export_files:
    dataframe.to_csv(filename, encoding="utf-8")
    print(f"✅ {filename}")

print("\n" + "=" * 60)
print("🎯 ZUSAMMENFASSUNG: DATENANALYSE")
print("=" * 60)
print("✅ Grundlegende und erweiterte Aggregationen")
print("✅ Multi-dimensionale Gruppierungen")
print("✅ Pivot-Tabellen für komplexe Analysen")
print("✅ Zeitreihenanalyse mit Resampling")
print("✅ Join-Operationen mit Stammdaten")
print("✅ Statistische Analysen und Korrelationen")
print("✅ Outlier-Erkennung und Behandlung")
print("✅ Performance-Benchmarking")
print("✅ Trendanalyse und Forecasting-Vorbereitung")
print("✅ Umfassende Analysereports")
print("\n💡 Als Bystronic-Entwickler beherrschen Sie jetzt")
print("   professionelle Datenanalyse mit Pandas!")
print("   Nächster Schritt: Integration mit Visualisierungen")
