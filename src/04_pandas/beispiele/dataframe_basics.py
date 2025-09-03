#!/usr/bin/env python3
"""
DataFrame-Grundlagen - Pandas Tutorial für Bystronic

Dieses Beispiel demonstriert die wichtigsten DataFrame-Operationen:
- Erstellung von DataFrames
- Grundlegende Eigenschaften und Methoden
- Indexing und Selection
- Einfache Datenmanipulation

Für Bystronic-Entwickler: Vergleichbare Funktionalität zu Excel-Arbeitsblättern
"""

import numpy as np
import pandas as pd

print("=" * 60)
print("🐼 PANDAS DATAFRAME-GRUNDLAGEN")
print("=" * 60)

# 1. DataFrame aus Dictionary erstellen
print("\n1️⃣ DataFrame aus Dictionary erstellen")
print("-" * 40)

maschinendaten = {
    "Maschine": ["Laser_01", "Laser_02", "Presse_01", "Presse_02", "Stanze_01"],
    "Typ": ["ByStar", "ByStar", "Xpert", "Xpert", "ByTrans"],
    "Baujahr": [2019, 2020, 2018, 2021, 2017],
    "Produktionszeit_h": [2450.5, 1890.2, 3200.8, 1250.4, 2890.1],
    "Wartung_fällig": [True, False, True, False, True],
}

df_maschinen = pd.DataFrame(maschinendaten)
print("Maschinendaten DataFrame:")
print(df_maschinen)
print(
    f"\nShape: {df_maschinen.shape} (Zeilen: {df_maschinen.shape[0]}, Spalten: {df_maschinen.shape[1]})"
)

# 2. DataFrame-Eigenschaften erkunden
print("\n2️⃣ DataFrame-Eigenschaften erkunden")
print("-" * 40)

print("Spalten-Namen:")
print(df_maschinen.columns.tolist())

print("\nDatentypen:")
print(df_maschinen.dtypes)

print("\nGrundlegende Informationen:")
print(df_maschinen.info())

print("\nStatistische Übersicht:")
print(df_maschinen.describe())

# 3. Zeilen und Spalten auswählen
print("\n3️⃣ Zeilen und Spalten auswählen")
print("-" * 40)

print("Erste 3 Zeilen:")
print(df_maschinen.head(3))

print("\nLetzte 2 Zeilen:")
print(df_maschinen.tail(2))

print("\nEine Spalte auswählen:")
print(df_maschinen["Maschine"])

print("\nMehrere Spalten auswählen:")
print(df_maschinen[["Maschine", "Produktionszeit_h"]])

# 4. Label-basierte Auswahl mit .loc
print("\n4️⃣ Label-basierte Auswahl mit .loc")
print("-" * 40)

print("Erste Zeile, alle Spalten:")
print(df_maschinen.loc[0])

print("\nBestimmte Zeilen und Spalten:")
print(df_maschinen.loc[1:3, ["Maschine", "Typ"]])

print("\nAlle Zeilen, bestimmte Spalten:")
print(df_maschinen.loc[:, "Typ":"Produktionszeit_h"])

# 5. Index-basierte Auswahl mit .iloc
print("\n5️⃣ Index-basierte Auswahl mit .iloc")
print("-" * 40)

print("Erste 2 Zeilen, erste 3 Spalten:")
print(df_maschinen.iloc[0:2, 0:3])

print("\nLetzte Zeile, alle Spalten:")
print(df_maschinen.iloc[-1, :])

# 6. Daten filtern
print("\n6️⃣ Daten filtern")
print("-" * 40)

# Boolean Indexing
wartung_fällig = df_maschinen[df_maschinen["Wartung_fällig"] == True]
print("Maschinen mit fälliger Wartung:")
print(wartung_fällig)

# Mehrere Bedingungen
neue_maschinen = df_maschinen[
    (df_maschinen["Baujahr"] >= 2020) & (df_maschinen["Produktionszeit_h"] > 1500)
]
print("\nNeue Maschinen mit hoher Produktionszeit:")
print(neue_maschinen)

# String-Filterung
laser_maschinen = df_maschinen[df_maschinen["Maschine"].str.contains("Laser")]
print("\nAlle Laser-Maschinen:")
print(laser_maschinen)

# 7. Neue Spalten hinzufügen
print("\n7️⃣ Neue Spalten hinzufügen")
print("-" * 40)

# Einfache Berechnung
df_maschinen["Alter"] = 2024 - df_maschinen["Baujahr"]

# Bedingte Spalte
df_maschinen["Produktions_Kategorie"] = np.where(
    df_maschinen["Produktionszeit_h"] > 2000, "Hoch", "Normal"
)

# Komplexere Berechnung
df_maschinen["Effizienz_Score"] = (
    df_maschinen["Produktionszeit_h"] / df_maschinen["Alter"]
).round(2)

print("DataFrame mit neuen Spalten:")
print(df_maschinen)

# 8. Daten sortieren
print("\n8️⃣ Daten sortieren")
print("-" * 40)

print("Nach Produktionszeit sortiert (aufsteigend):")
print(df_maschinen.sort_values("Produktionszeit_h"))

print("\nNach Baujahr sortiert (absteigend):")
print(df_maschinen.sort_values("Baujahr", ascending=False))

print("\nNach mehreren Spalten sortiert:")
print(df_maschinen.sort_values(["Typ", "Produktionszeit_h"], ascending=[True, False]))

# 9. Grundlegende Aggregationen
print("\n9️⃣ Grundlegende Aggregationen")
print("-" * 40)

print("Durchschnittliche Produktionszeit:")
print(f"{df_maschinen['Produktionszeit_h'].mean():.2f} Stunden")

print("\nSumme aller Produktionszeiten:")
print(f"{df_maschinen['Produktionszeit_h'].sum():.2f} Stunden")

print("\nMaschine mit höchster Produktionszeit:")
max_idx = df_maschinen["Produktionszeit_h"].idxmax()
print(df_maschinen.loc[max_idx, ["Maschine", "Produktionszeit_h"]])

print("\nAnzahl Maschinen pro Typ:")
print(df_maschinen["Typ"].value_counts())

# 10. Gruppenoperationen
print("\n🔟 Gruppenoperationen")
print("-" * 40)

print("Durchschnittswerte pro Maschinentyp:")
grouped = (
    df_maschinen.groupby("Typ")
    .agg({"Produktionszeit_h": ["mean", "sum", "count"], "Alter": "mean"})
    .round(2)
)
print(grouped)

print("\nAnzahl Maschinen mit fälliger Wartung pro Typ:")
wartung_stats = df_maschinen.groupby("Typ")["Wartung_fällig"].sum()
print(wartung_stats)

# 11. Praktisches Beispiel: Produktionsplanung
print("\n1️⃣1️⃣ Praktisches Beispiel: Produktionsplanung")
print("-" * 40)

# Simuliere wöchentliche Produktionsdaten
np.random.seed(42)  # Für reproduzierbare Ergebnisse

wochen_daten = []
for woche in range(1, 5):  # 4 Wochen
    for _, maschine in df_maschinen.iterrows():
        # Simuliere unterschiedliche Produktionszeiten
        basis_zeit = maschine["Produktionszeit_h"] / 52  # Pro Woche
        variation = np.random.normal(0, basis_zeit * 0.1)  # 10% Variation
        tatsächliche_zeit = max(0, basis_zeit + variation)

        wochen_daten.append(
            {
                "Woche": woche,
                "Maschine": maschine["Maschine"],
                "Typ": maschine["Typ"],
                "Geplante_Zeit": basis_zeit,
                "Tatsächliche_Zeit": tatsächliche_zeit,
                "Abweichung": tatsächliche_zeit - basis_zeit,
            }
        )

df_produktion = pd.DataFrame(wochen_daten)
print("Wöchentliche Produktionsdaten:")
print(df_produktion.head(10))

print("\nDurchschnittliche Abweichung pro Maschine:")
abweichungen = df_produktion.groupby("Maschine")["Abweichung"].mean().round(2)
print(abweichungen)

print("\nGesamtproduktion pro Woche:")
wochen_summen = df_produktion.groupby("Woche")["Tatsächliche_Zeit"].sum().round(2)
print(wochen_summen)

# 12. Daten exportieren
print("\n1️⃣2️⃣ Daten exportieren")
print("-" * 40)

# CSV exportieren (wird in .gitignore ignoriert)
df_maschinen.to_csv("data/generated/maschinendaten.csv", index=False, encoding="utf-8")
print("✅ Daten als CSV exportiert: data/generated/maschinendaten.csv")

# Excel exportieren (wird in .gitignore ignoriert)
try:
    df_maschinen.to_excel("maschinendaten.xlsx", index=False)
    print("✅ Daten als Excel exportiert: maschinendaten.xlsx")
except ImportError:
    print("ℹ️ Für Excel-Export: pip install openpyxl")

print("\n" + "=" * 60)
print("🎯 ZUSAMMENFASSUNG: DATAFRAME-GRUNDLAGEN")
print("=" * 60)
print("✅ DataFrame erstellen und erkunden")
print("✅ Zeilen und Spalten auswählen (.loc, .iloc)")
print("✅ Daten filtern mit Boolean Indexing")
print("✅ Neue Spalten berechnen")
print("✅ Sortieren und Aggregieren")
print("✅ Gruppierungen für Analysen")
print("✅ Praktisches Beispiel: Produktionsdaten")
print("✅ Export in verschiedene Formate")
print("\n💡 Als Bystronic-Entwickler kennen Sie jetzt die Pandas-Grundlagen!")
print("   Nächster Schritt: Datenimport aus verschiedenen Quellen")
