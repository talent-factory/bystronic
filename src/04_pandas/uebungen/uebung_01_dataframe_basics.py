#!/usr/bin/env python3
"""
Übung 1: DataFrame-Grundlagen - Pandas Tutorial für SmartFactory

AUFGABENSTELLUNG:
In dieser Übung lernen Sie die fundamentalen DataFrame-Operationen.
Sie arbeiten mit Maschinendaten und lernen DataFrame-Erstellung,
Indexing, Filtering und grundlegende Manipulationen.

SCHWIERIGKEITSGRAD: Beginner
ZEITAUFWAND: 30-45 Minuten

LERNZIELE:
- DataFrame aus verschiedenen Quellen erstellen
- Zeilen und Spalten auswählen (.loc, .iloc)
- Daten filtern mit Boolean Indexing
- Neue Spalten berechnen
- Grundlegende Aggregationen durchführen
"""

import numpy as np
import pandas as pd

print("=" * 60)
print("🐼 ÜBUNG 1: DATAFRAME-GRUNDLAGEN")
print("=" * 60)

# =============================================================================
# AUFGABE 1: DataFrame-Erstellung (10 Punkte)
# =============================================================================

print("\n📋 AUFGABE 1: DataFrame-Erstellung")
print("-" * 40)

print(
    """
Sie arbeiten als Datenanalyst bei SmartFactory und haben folgende Maschinendaten erhalten:

Maschinendaten:
- Laser_01: ByStar, Baujahr 2019, 2450.5h Laufzeit, Wartung fällig
- Laser_02: ByStar, Baujahr 2020, 1890.2h Laufzeit, keine Wartung
- Presse_01: Xpert, Baujahr 2018, 3200.8h Laufzeit, Wartung fällig
- Presse_02: Xpert, Baujahr 2021, 1250.4h Laufzeit, keine Wartung
- Stanze_01: ByTrans, Baujahr 2017, 2890.1h Laufzeit, Wartung fällig

TODO: Erstellen Sie einen DataFrame 'df_maschinen' mit folgenden Spalten:
- Maschine (String)
- Typ (String)
- Baujahr (Integer)
- Laufzeit_h (Float)
- Wartung_fällig (Boolean)
"""
)

# IHRE LÖSUNG HIER:
# df_maschinen = pd.DataFrame({
#     'Maschine': [...],
#     'Typ': [...],
#     # ... weitere Spalten
# })

# LÖSUNG (auskommentieren zum Testen):
df_maschinen = pd.DataFrame(
    {
        "Maschine": ["Laser_01", "Laser_02", "Presse_01", "Presse_02", "Stanze_01"],
        "Typ": ["ByStar", "ByStar", "Xpert", "Xpert", "ByTrans"],
        "Baujahr": [2019, 2020, 2018, 2021, 2017],
        "Laufzeit_h": [2450.5, 1890.2, 3200.8, 1250.4, 2890.1],
        "Wartung_fällig": [True, False, True, False, True],
    }
)

# Validierung
try:
    assert len(df_maschinen) == 5, "DataFrame sollte 5 Zeilen haben"
    assert list(df_maschinen.columns) == [
        "Maschine",
        "Typ",
        "Baujahr",
        "Laufzeit_h",
        "Wartung_fällig",
    ], "Spalten stimmen nicht"
    assert df_maschinen["Baujahr"].dtype == "int64", "Baujahr sollte Integer sein"
    assert (
        df_maschinen["Wartung_fällig"].dtype == "bool"
    ), "Wartung_fällig sollte Boolean sein"
    print("✅ Aufgabe 1 korrekt gelöst!")
    print(
        f"DataFrame erstellt mit {df_maschinen.shape[0]} Zeilen und {df_maschinen.shape[1]} Spalten"
    )
    print(df_maschinen)
except AssertionError as e:
    print(f"❌ Fehler: {e}")
except NameError:
    print("❌ Bitte implementieren Sie df_maschinen")

# =============================================================================
# AUFGABE 2: Zeilen und Spalten auswählen (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 2: Zeilen und Spalten auswählen")
print("-" * 40)

print(
    """
TODO: Führen Sie folgende Selections durch:

a) Wählen Sie die erste und letzte Zeile des DataFrames aus (verwenden Sie .iloc)
b) Wählen Sie nur die Spalten 'Maschine' und 'Laufzeit_h' aus
c) Wählen Sie die Zeilen 1-3 und Spalten 'Typ' bis 'Laufzeit_h' aus (verwenden Sie .loc)
d) Wählen Sie die Maschine mit der höchsten Laufzeit aus
"""
)

print("a) Erste und letzte Zeile:")
# IHRE LÖSUNG HIER:
erste_letzte = df_maschinen.iloc[[0, -1]]
print(erste_letzte)

print("\nb) Nur Maschine und Laufzeit_h:")
# IHRE LÖSUNG HIER:
maschine_laufzeit = df_maschinen[["Maschine", "Laufzeit_h"]]
print(maschine_laufzeit)

print("\nc) Zeilen 1-3, Spalten 'Typ' bis 'Laufzeit_h':")
# IHRE LÖSUNG HIER:
selection_loc = df_maschinen.loc[1:3, "Typ":"Laufzeit_h"]
print(selection_loc)

print("\nd) Maschine mit höchster Laufzeit:")
# IHRE LÖSUNG HIER:
max_laufzeit_idx = df_maschinen["Laufzeit_h"].idxmax()
hoechste_laufzeit = df_maschinen.loc[max_laufzeit_idx]
print(hoechste_laufzeit)

# Validierung
try:
    assert len(erste_letzte) == 2, "Erste/letzte Zeile: Sollte 2 Zeilen haben"
    assert len(maschine_laufzeit.columns) == 2, "Sollte 2 Spalten haben"
    assert "Presse_01" in str(
        hoechste_laufzeit.values
    ), "Presse_01 hat die höchste Laufzeit"
    print("\n✅ Aufgabe 2 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 2: {e}")

# =============================================================================
# AUFGABE 3: Daten filtern (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 3: Daten filtern")
print("-" * 40)

print(
    """
TODO: Erstellen Sie folgende Filter:

a) Alle Maschinen, bei denen Wartung fällig ist
b) Alle Maschinen mit Baujahr >= 2019
c) Alle Laser-Maschinen (Typ == 'ByStar')
d) Alle Maschinen mit Wartung fällig UND Laufzeit > 2500h
e) Alle Maschinen, deren Name 'Laser' enthält
"""
)

print("a) Wartung fällig:")
# IHRE LÖSUNG HIER:
wartung_fällig = df_maschinen[df_maschinen["Wartung_fällig"]]
print(f"Anzahl: {len(wartung_fällig)}")
print(wartung_fällig[["Maschine", "Wartung_fällig"]])

print("\nb) Baujahr >= 2019:")
# IHRE LÖSUNG HIER:
neue_maschinen = df_maschinen[df_maschinen["Baujahr"] >= 2019]
print(f"Anzahl: {len(neue_maschinen)}")
print(neue_maschinen[["Maschine", "Baujahr"]])

print("\nc) Laser-Maschinen (ByStar):")
# IHRE LÖSUNG HIER:
laser_maschinen = df_maschinen[df_maschinen["Typ"] == "ByStar"]
print(f"Anzahl: {len(laser_maschinen)}")
print(laser_maschinen[["Maschine", "Typ"]])

print("\nd) Wartung fällig UND Laufzeit > 2500h:")
# IHRE LÖSUNG HIER:
wartung_hohe_laufzeit = df_maschinen[
    (df_maschinen["Wartung_fällig"]) & (df_maschinen["Laufzeit_h"] > 2500)
]
print(f"Anzahl: {len(wartung_hohe_laufzeit)}")
print(wartung_hohe_laufzeit[["Maschine", "Laufzeit_h", "Wartung_fällig"]])

print("\ne) Name enthält 'Laser':")
# IHRE LÖSUNG HIER:
name_laser = df_maschinen[df_maschinen["Maschine"].str.contains("Laser")]
print(f"Anzahl: {len(name_laser)}")
print(name_laser[["Maschine"]])

# Validierung
try:
    assert len(wartung_fällig) == 3, "3 Maschinen brauchen Wartung"
    assert len(neue_maschinen) == 3, "3 Maschinen sind >= 2019"
    assert len(laser_maschinen) == 2, "2 Laser-Maschinen"
    assert len(wartung_hohe_laufzeit) == 2, "2 Maschinen: Wartung + hohe Laufzeit"
    assert len(name_laser) == 2, "2 Maschinen mit 'Laser' im Namen"
    print("\n✅ Aufgabe 3 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 3: {e}")

# =============================================================================
# AUFGABE 4: Neue Spalten berechnen (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 4: Neue Spalten berechnen")
print("-" * 40)

print(
    """
TODO: Berechnen Sie folgende neue Spalten:

a) 'Alter': Aktuelles Jahr (2024) - Baujahr
b) 'Laufzeit_Kategorie': 'Hoch' wenn > 2500h, 'Mittel' wenn 1500-2500h, sonst 'Niedrig'
c) 'Wartung_Status': 'Dringend' wenn Wartung fällig UND > 2500h, 'Normal' wenn nur Wartung fällig, sonst 'Keine'
d) 'Effizienz_Score': Laufzeit_h / Alter (gerundet auf 2 Stellen)
"""
)

# Kopie für Berechnungen erstellen
df_berechnet = df_maschinen.copy()

print("a) Alter berechnen:")
# IHRE LÖSUNG HIER:
df_berechnet["Alter"] = 2024 - df_berechnet["Baujahr"]
print(df_berechnet[["Maschine", "Baujahr", "Alter"]])

print("\nb) Laufzeit-Kategorie:")
# IHRE LÖSUNG HIER:
df_berechnet["Laufzeit_Kategorie"] = np.where(
    df_berechnet["Laufzeit_h"] > 2500,
    "Hoch",
    np.where(df_berechnet["Laufzeit_h"] >= 1500, "Mittel", "Niedrig"),
)
print(df_berechnet[["Maschine", "Laufzeit_h", "Laufzeit_Kategorie"]])

print("\nc) Wartung-Status:")
# IHRE LÖSUNG HIER:
df_berechnet["Wartung_Status"] = np.where(
    (df_berechnet["Wartung_fällig"]) & (df_berechnet["Laufzeit_h"] > 2500),
    "Dringend",
    np.where(df_berechnet["Wartung_fällig"], "Normal", "Keine"),
)
print(df_berechnet[["Maschine", "Wartung_fällig", "Laufzeit_h", "Wartung_Status"]])

print("\nd) Effizienz-Score:")
# IHRE LÖSUNG HIER:
df_berechnet["Effizienz_Score"] = (
    df_berechnet["Laufzeit_h"] / df_berechnet["Alter"]
).round(2)
print(df_berechnet[["Maschine", "Laufzeit_h", "Alter", "Effizienz_Score"]])

# Validierung
try:
    assert "Alter" in df_berechnet.columns, "Spalte 'Alter' fehlt"
    assert df_berechnet["Alter"].max() == 7, "Älteste Maschine sollte 7 Jahre alt sein"
    assert "Hoch" in df_berechnet["Laufzeit_Kategorie"].values, "Kategorie 'Hoch' fehlt"
    assert (
        "Dringend" in df_berechnet["Wartung_Status"].values
    ), "Status 'Dringend' fehlt"
    assert (
        df_berechnet["Effizienz_Score"].dtype == "float64"
    ), "Effizienz_Score sollte float sein"
    print("\n✅ Aufgabe 4 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 4: {e}")

# =============================================================================
# AUFGABE 5: Sortieren und Aggregieren (15 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 5: Sortieren und Aggregieren")
print("-" * 40)

print(
    """
TODO: Führen Sie folgende Operationen durch:

a) Sortieren Sie den DataFrame nach Laufzeit_h (absteigend)
b) Berechnen Sie die durchschnittliche Laufzeit aller Maschinen
c) Berechnen Sie Statistiken nach Typ (groupby)
d) Zählen Sie, wie viele Maschinen Wartung brauchen
e) Finden Sie die Maschine mit der niedrigsten Effizienz
"""
)

print("a) Nach Laufzeit sortiert (absteigend):")
# IHRE LÖSUNG HIER:
df_sortiert = df_berechnet.sort_values("Laufzeit_h", ascending=False)
print(df_sortiert[["Maschine", "Laufzeit_h"]])

print("\nb) Durchschnittliche Laufzeit:")
# IHRE LÖSUNG HIER:
avg_laufzeit = df_berechnet["Laufzeit_h"].mean()
print(f"Durchschnitt: {avg_laufzeit:.2f} Stunden")

print("\nc) Statistiken nach Typ:")
# IHRE LÖSUNG HIER:
stats_typ = (
    df_berechnet.groupby("Typ")
    .agg(
        {
            "Laufzeit_h": ["count", "mean", "sum"],
            "Alter": "mean",
            "Wartung_fällig": "sum",
        }
    )
    .round(2)
)
print(stats_typ)

print("\nd) Anzahl Maschinen mit Wartung:")
# IHRE LÖSUNG HIER:
wartung_anzahl = df_berechnet["Wartung_fällig"].sum()
print(f"Maschinen mit Wartung: {wartung_anzahl}")

print("\ne) Maschine mit niedrigster Effizienz:")
# IHRE LÖSUNG HIER:
min_effizienz_idx = df_berechnet["Effizienz_Score"].idxmin()
niedrigste_effizienz = df_berechnet.loc[
    min_effizienz_idx, ["Maschine", "Effizienz_Score"]
]
print(niedrigste_effizienz)

# Validierung
try:
    assert (
        df_sortiert.iloc[0]["Maschine"] == "Presse_01"
    ), "Presse_01 sollte höchste Laufzeit haben"
    assert 2100 < avg_laufzeit < 2400, "Durchschnitt sollte ~2336h sein"
    assert wartung_anzahl == 3, "3 Maschinen brauchen Wartung"
    print("\n✅ Aufgabe 5 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 5: {e}")

# =============================================================================
# AUFGABE 6: Praktische Anwendung (20 Punkte)
# =============================================================================

print("\n\n📋 AUFGABE 6: Praktische Anwendung")
print("-" * 40)

print(
    """
SZENARIO: Als Produktionsleiter müssen Sie einen Wartungsplan erstellen.

TODO: Analysieren Sie die Daten und beantworten Sie folgende Fragen:

a) Welche Maschinen haben die höchste Priorität für Wartung? (Wartung fällig + hohe Laufzeit)
b) Berechnen Sie die Wartungskosten (Annahme: 500€ + 50€ pro 100h Laufzeit)
c) Erstellen Sie eine Effizienz-Rangliste
d) Identifizieren Sie Maschinen für Ersatz (Alter > 5 Jahre UND niedrige Effizienz < 300)
"""
)

print("a) Wartungspriorität (Wartung + Laufzeit > 2500h):")
# IHRE LÖSUNG HIER:
hohe_prioritaet = df_berechnet[
    (df_berechnet["Wartung_fällig"]) & (df_berechnet["Laufzeit_h"] > 2500)
].sort_values("Laufzeit_h", ascending=False)
print(f"Anzahl mit hoher Priorität: {len(hohe_prioritaet)}")
print(hohe_prioritaet[["Maschine", "Typ", "Laufzeit_h", "Wartung_Status"]])

print("\nb) Wartungskosten berechnen:")
# IHRE LÖSUNG HIER:
df_berechnet["Wartungskosten_Euro"] = np.where(
    df_berechnet["Wartung_fällig"], 500 + (df_berechnet["Laufzeit_h"] / 100 * 50), 0
).round(2)

wartungskosten_total = df_berechnet["Wartungskosten_Euro"].sum()
print(f"Gesamte Wartungskosten: {wartungskosten_total:,.2f} €")
print(
    df_berechnet[df_berechnet["Wartung_fällig"]][
        ["Maschine", "Laufzeit_h", "Wartungskosten_Euro"]
    ]
)

print("\nc) Effizienz-Rangliste:")
# IHRE LÖSUNG HIER:
effizienz_ranking = df_berechnet.sort_values("Effizienz_Score", ascending=False)
effizienz_ranking["Rang"] = range(1, len(effizienz_ranking) + 1)
print(effizienz_ranking[["Rang", "Maschine", "Effizienz_Score", "Laufzeit_Kategorie"]])

print("\nd) Ersatz-Kandidaten (Alter > 5 UND Effizienz < 300):")
# IHRE LÖSUNG HIER:
ersatz_kandidaten = df_berechnet[
    (df_berechnet["Alter"] > 5) & (df_berechnet["Effizienz_Score"] < 300)
]
print(f"Anzahl Ersatz-Kandidaten: {len(ersatz_kandidaten)}")
if len(ersatz_kandidaten) > 0:
    print(
        ersatz_kandidaten[
            ["Maschine", "Alter", "Effizienz_Score", "Wartungskosten_Euro"]
        ]
    )
else:
    print("Keine Ersatz-Kandidaten gefunden")

# Validierung und Zusammenfassung
try:
    assert len(hohe_prioritaet) == 2, "2 Maschinen haben hohe Wartungspriorität"
    assert wartungskosten_total > 2000, "Wartungskosten sollten über 2000€ liegen"
    assert effizienz_ranking.iloc[0]["Rang"] == 1, "Ranking sollte bei 1 beginnen"
    print("\n✅ Aufgabe 6 korrekt gelöst!")
except (AssertionError, NameError) as e:
    print(f"\n❌ Fehler in Aufgabe 6: {e}")

# =============================================================================
# ZUSAMMENFASSUNG UND BEWERTUNG
# =============================================================================

print("\n" + "=" * 60)
print("🎯 ÜBUNG 1 ABGESCHLOSSEN")
print("=" * 60)

# Finales DataFrame anzeigen
print("\n📊 Finales DataFrame mit allen Berechnungen:")
print(df_berechnet.head())

# Zusammenfassung der wichtigsten Erkenntnisse
print("\n📈 WICHTIGSTE ERKENNTNISSE:")
print(f"• {len(df_berechnet)} Maschinen analysiert")
print(f"• {df_berechnet['Wartung_fällig'].sum()} Maschinen brauchen Wartung")
print(f"• Gesamte Laufzeit: {df_berechnet['Laufzeit_h'].sum():,.1f} Stunden")
print(f"• Durchschnittliches Alter: {df_berechnet['Alter'].mean():.1f} Jahre")
print(f"• Wartungskosten: {df_berechnet['Wartungskosten_Euro'].sum():,.2f} €")
print(
    f"• Beste Effizienz: {df_berechnet['Effizienz_Score'].max():.2f} (Maschine: {df_berechnet.loc[df_berechnet['Effizienz_Score'].idxmax(), 'Maschine']})"
)

print("\n✅ LERNZIELE ERREICHT:")
print("• DataFrame-Erstellung und -Struktur verstehen")
print("• Indexing und Selection (.loc, .iloc) beherrschen")
print("• Filterung mit Boolean Indexing anwenden")
print("• Neue Spalten berechnen und Datentypen handhaben")
print("• Sortierung und Aggregation durchführen")
print("• Praktische Geschäftsanalysen implementieren")

print("\n🎓 NÄCHSTE SCHRITTE:")
print("• Übung 2: Datenimport aus verschiedenen Quellen")
print("• Jupyter Notebook für interaktive Analysen erkunden")
print("• Eigene Maschinendaten mit Pandas analysieren")

print("\n💡 Als SmartFactory-Entwickler können Sie jetzt DataFrame-Grundlagen")
print("   professionell einsetzen für Produktionsdaten-Analysen!")

# Export der Ergebnisse (optional)
df_berechnet.to_csv("data/generated/uebung_01_ergebnisse.csv", index=False)
print("\n💾 Ergebnisse gespeichert als: data/generated/uebung_01_ergebnisse.csv")
