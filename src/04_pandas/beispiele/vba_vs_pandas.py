#!/usr/bin/env python3
"""
VBA vs Pandas Vergleich - Tutorial für Bystronic

Dieses Beispiel zeigt direkte Vergleiche zwischen VBA/Excel und Pandas/Python:
- Datenmanipulation
- Pivot-Tabellen
- Formeln und Berechnungen
- Automatisierung
- Performance-Unterschiede

Für Bystronic-Entwickler: Migration von VBA zu Python/Pandas
"""

import time

import numpy as np
import pandas as pd

print("=" * 70)
print("⚔️  VBA/EXCEL vs PANDAS/PYTHON VERGLEICH")
print("=" * 70)


# Beispieldaten erstellen (repräsentativ für Bystronic-Daten)
def create_comparison_data():
    """Erstelle Daten, die typisch für VBA-Automatisierungen sind"""
    np.random.seed(42)

    # Produktionsdaten wie sie oft in Excel-Sheets zu finden sind
    dates = pd.date_range("2024-01-01", periods=1000, freq="H")  # Stündliche Daten

    data = []
    maschinen = ["LASER_001", "LASER_002", "PRESSE_001", "PRESSE_002", "STANZE_001"]

    for _i, date in enumerate(dates):
        maschine = np.random.choice(maschinen)

        data.append(
            {
                "Zeitstempel": date,
                "Maschine": maschine,
                "Stueckzahl": np.random.randint(10, 100),
                "Zykluszeit_Sek": np.random.uniform(30, 120),
                "Temperatur_C": np.random.uniform(18, 35),
                "Druck_Bar": np.random.uniform(5, 15),
                "Qualitaet_OK": np.random.choice([True, False], p=[0.92, 0.08]),
                "Schicht": np.random.choice(["Früh", "Spät", "Nacht"]),
                "Bediener_ID": f"BY{np.random.randint(100, 999)}",
            }
        )

    return pd.DataFrame(data)


df = create_comparison_data()
print(f"📊 Testdaten: {len(df)} Datensätze erstellt")
print(f"Zeitraum: {df['Zeitstempel'].min()} bis {df['Zeitstempel'].max()}")
print(df.head())

print("\n" + "=" * 70)
print("1️⃣  DATENFILTERUNG")
print("=" * 70)

print("\n🔴 VBA/EXCEL Ansatz:")
print(
    """
' VBA Code für Filterung
Sub FilterData()
    Dim ws As Worksheet
    Dim lastRow As Long
    Dim i As Long

    Set ws = ActiveSheet
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    ' Filter: Nur Laser-Maschinen mit guter Qualität
    For i = 2 To lastRow
        If InStr(ws.Cells(i, 2).Value, "LASER") > 0 And _
           ws.Cells(i, 7).Value = True Then
            ws.Rows(i).Hidden = False
        Else
            ws.Rows(i).Hidden = True
        End If
    Next i
End Sub
"""
)

print("Probleme mit VBA:")
print("❌ Langsam bei grossen Datenmengen")
print("❌ Keine Wiederverwendbarkeit")
print("❌ Schwer zu testen und debuggen")
print("❌ Excel muss geöffnet sein")

print("\n🟢 PANDAS/PYTHON Ansatz:")
start_time = time.time()

# Einfache, lesbare Filterung
laser_quality = df[(df["Maschine"].str.contains("LASER")) & (df["Qualitaet_OK"])]

pandas_time = time.time() - start_time

print("# Python Code für Filterung")
print("laser_quality = df[")
print("    (df['Maschine'].str.contains('LASER')) & ")
print("    (df['Qualitaet_OK'] == True)")
print("]")

print(f"\n✅ Gefilterte Datensätze: {len(laser_quality)}")
print(f"✅ Ausführungszeit: {pandas_time:.4f} Sekunden")
print("✅ Lesbar und wiederverwendbar")
print("✅ Keine Excel-Abhängigkeit")

print("\n" + "=" * 70)
print("2️⃣  AGGREGATION UND GRUPPIERUNG")
print("=" * 70)

print("\n🔴 VBA/EXCEL Ansatz:")
print(
    """
' VBA Code für Aggregation (sehr umständlich!)
Sub CreateSummary()
    Dim ws As Worksheet, summaryWs As Worksheet
    Dim dict As Object
    Dim i As Long, lastRow As Long

    Set dict = CreateObject("Scripting.Dictionary")
    Set ws = Worksheets("Daten")
    Set summaryWs = Worksheets("Zusammenfassung")

    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    ' Durchlaufe alle Zeilen und sammle Daten
    For i = 2 To lastRow
        maschine = ws.Cells(i, 2).Value
        stueckzahl = ws.Cells(i, 3).Value

        If dict.Exists(maschine) Then
            dict(maschine) = dict(maschine) + stueckzahl
        Else
            dict.Add maschine, stueckzahl
        End If
    Next i

    ' Ergebnisse in Summary-Sheet schreiben
    ' ... noch mehr Code ...
End Sub
"""
)

print("\n🟢 PANDAS/PYTHON Ansatz:")
start_time = time.time()

# Elegante Aggregation
maschinen_summary = (
    df.groupby("Maschine")
    .agg(
        {
            "Stueckzahl": "sum",
            "Zykluszeit_Sek": "mean",
            "Qualitaet_OK": "mean",
            "Temperatur_C": ["mean", "max"],
        }
    )
    .round(2)
)

pandas_agg_time = time.time() - start_time

print("# Python Code für Aggregation")
print("maschinen_summary = df.groupby('Maschine').agg({")
print("    'Stueckzahl': 'sum',")
print("    'Zykluszeit_Sek': 'mean',")
print("    'Qualitaet_OK': 'mean',")
print("    'Temperatur_C': ['mean', 'max']")
print("}).round(2)")

print("\n📊 Zusammenfassung nach Maschinen:")
print(maschinen_summary)
print(f"✅ Ausführungszeit: {pandas_agg_time:.4f} Sekunden")

print("\n" + "=" * 70)
print("3️⃣  PIVOT-TABELLEN")
print("=" * 70)

print("\n🔴 VBA/EXCEL Ansatz:")
print(
    """
' VBA Code für Pivot-Tabelle (sehr komplex!)
Sub CreatePivotTable()
    Dim ws As Worksheet, ptWs As Worksheet
    Dim pt As PivotTable
    Dim pc As PivotCache
    Dim dataRange As Range

    Set ws = Worksheets("Daten")
    Set dataRange = ws.UsedRange

    ' PivotCache erstellen
    Set pc = ActiveWorkbook.PivotCaches.Create(_
        SourceType:=xlDatabase, _
        SourceData:=dataRange)

    ' Pivot-Tabelle erstellen
    Set ptWs = Worksheets.Add
    Set pt = pc.CreatePivotTable(_
        TableDestination:=ptWs.Range("A1"))

    ' Felder konfigurieren
    pt.PivotFields("Maschine").Orientation = xlRowField
    pt.PivotFields("Schicht").Orientation = xlColumnField
    pt.PivotFields("Stueckzahl").Orientation = xlDataField
    ' ... weitere Konfiguration ...
End Sub
"""
)

print("🟢 PANDAS/PYTHON Ansatz:")
start_time = time.time()

# Einfache Pivot-Tabelle
pivot_table = df.pivot_table(
    values="Stueckzahl",
    index="Maschine",
    columns="Schicht",
    aggfunc="sum",
    fill_value=0,
)

pandas_pivot_time = time.time() - start_time

print("# Python Code für Pivot-Tabelle")
print("pivot_table = df.pivot_table(")
print("    values='Stueckzahl',")
print("    index='Maschine',")
print("    columns='Schicht',")
print("    aggfunc='sum',")
print("    fill_value=0")
print(")")

print("\n📋 Pivot-Tabelle: Stückzahl nach Maschine und Schicht:")
print(pivot_table)
print(f"✅ Ausführungszeit: {pandas_pivot_time:.4f} Sekunden")

print("\n" + "=" * 70)
print("4️⃣  BEDINGTE FORMATIERUNG UND BERECHNUNGEN")
print("=" * 70)

print("\n🔴 VBA/EXCEL Ansatz:")
print(
    """
' VBA Code für bedingte Berechnungen
Sub CalculateEfficiency()
    Dim ws As Worksheet
    Dim i As Long, lastRow As Long

    Set ws = ActiveSheet
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow
        stueckzahl = ws.Cells(i, 3).Value
        zykluszeit = ws.Cells(i, 4).Value

        ' Effizienz berechnen
        If zykluszeit > 0 Then
            effizienz = stueckzahl / (zykluszeit / 60) ' Stück pro Minute
            ws.Cells(i, 10).Value = effizienz

            ' Kategorisierung
            If effizienz > 1.5 Then
                ws.Cells(i, 11).Value = "Hoch"
                ws.Cells(i, 11).Interior.Color = RGB(0, 255, 0)
            ElseIf effizienz > 1.0 Then
                ws.Cells(i, 11).Value = "Mittel"
                ws.Cells(i, 11).Interior.Color = RGB(255, 255, 0)
            Else
                ws.Cells(i, 11).Value = "Niedrig"
                ws.Cells(i, 11).Interior.Color = RGB(255, 0, 0)
            End If
        End If
    Next i
End Sub
"""
)

print("\n🟢 PANDAS/PYTHON Ansatz:")
start_time = time.time()

# Elegante vektorisierte Berechnungen
df_enhanced = df.copy()

# Effizienz berechnen (Stück pro Minute)
df_enhanced["Effizienz_Stueck_pro_Min"] = (
    df_enhanced["Stueckzahl"] / (df_enhanced["Zykluszeit_Sek"] / 60)
).round(2)

# Kategorisierung mit np.where (vektorisiert!)
df_enhanced["Effizienz_Kategorie"] = np.where(
    df_enhanced["Effizienz_Stueck_pro_Min"] > 1.5,
    "Hoch",
    np.where(df_enhanced["Effizienz_Stueck_pro_Min"] > 1.0, "Mittel", "Niedrig"),
)

# OEE-Berechnung (Overall Equipment Effectiveness)
df_enhanced["OEE_Faktor"] = (
    df_enhanced["Qualitaet_OK"].astype(int)
    * np.where(
        df_enhanced["Effizienz_Stueck_pro_Min"] > 1.0,
        1.0,
        df_enhanced["Effizienz_Stueck_pro_Min"],
    )
).round(3)

pandas_calc_time = time.time() - start_time

print("# Python Code für Berechnungen")
print("# Effizienz berechnen")
print("df['Effizienz'] = df['Stueckzahl'] / (df['Zykluszeit_Sek'] / 60)")
print("")
print("# Kategorisierung")
print("df['Kategorie'] = np.where(df['Effizienz'] > 1.5, 'Hoch',")
print("                  np.where(df['Effizienz'] > 1.0, 'Mittel', 'Niedrig'))")

print("\n📈 Effizienz-Analyse:")
effizienz_stats = (
    df_enhanced.groupby("Effizienz_Kategorie")
    .agg({"Effizienz_Stueck_pro_Min": ["count", "mean"], "OEE_Faktor": "mean"})
    .round(3)
)
print(effizienz_stats)
print(f"✅ Ausführungszeit: {pandas_calc_time:.4f} Sekunden")

print("\n" + "=" * 70)
print("5️⃣  DATENVALIDIERUNG UND FEHLERBEHANDLUNG")
print("=" * 70)

print("\n🔴 VBA/EXCEL Ansatz:")
print(
    """
' VBA Code für Datenvalidierung (fehleranfällig)
Sub ValidateData()
    Dim ws As Worksheet
    Dim i As Long, lastRow As Long, errorCount As Long

    Set ws = ActiveSheet
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    For i = 2 To lastRow
        ' Temperatur-Validierung
        If IsNumeric(ws.Cells(i, 5).Value) Then
            temp = CDbl(ws.Cells(i, 5).Value)
            If temp < 10 Or temp > 50 Then
                ws.Cells(i, 12).Value = "Temperatur ungültig"
                errorCount = errorCount + 1
            End If
        Else
            ws.Cells(i, 12).Value = "Temperatur kein Zahlenwert"
            errorCount = errorCount + 1
        End If

        ' Weitere Validierungen...
    Next i

    MsgBox "Validierung abgeschlossen. Fehler: " & errorCount
End Sub
"""
)

print("\n🟢 PANDAS/PYTHON Ansatz:")
start_time = time.time()


def validate_production_data(df):
    """Umfassende Datenvalidierung mit Pandas"""
    validation_report = {"total_records": len(df), "errors": [], "warnings": []}

    # Temperatur-Validierung
    temp_invalid = (df["Temperatur_C"] < 10) | (df["Temperatur_C"] > 50)
    if temp_invalid.any():
        validation_report["errors"].append(
            f"Ungültige Temperaturen: {temp_invalid.sum()} Datensätze"
        )

    # Zykluszeit-Validierung
    cycle_invalid = (df["Zykluszeit_Sek"] <= 0) | (df["Zykluszeit_Sek"] > 300)
    if cycle_invalid.any():
        validation_report["errors"].append(
            f"Ungültige Zykluszeiten: {cycle_invalid.sum()} Datensätze"
        )

    # Stückzahl-Plausibilität
    pieces_suspicious = df["Stueckzahl"] > 200  # Sehr hohe Stückzahl
    if pieces_suspicious.any():
        validation_report["warnings"].append(
            f"Verdächtig hohe Stückzahlen: {pieces_suspicious.sum()} Datensätze"
        )

    # Qualitätsrate nach Maschine
    quality_by_machine = df.groupby("Maschine")["Qualitaet_OK"].mean()
    low_quality_machines = quality_by_machine[quality_by_machine < 0.85]
    if not low_quality_machines.empty:
        validation_report["warnings"].append(
            f"Maschinen mit niedriger Qualitätsrate: {list(low_quality_machines.index)}"
        )

    return validation_report


validation_result = validate_production_data(df_enhanced)
pandas_validation_time = time.time() - start_time

print("# Python Code für Validierung")
print("def validate_production_data(df):")
print("    # Temperatur-Validierung")
print("    temp_invalid = (df['Temperatur_C'] < 10) | (df['Temperatur_C'] > 50)")
print("    # Weitere Validierungen...")
print("    return validation_report")

print("\n🔍 Validierungsergebnis:")
print(f"Gesamtdatensätze: {validation_result['total_records']}")
print(f"Fehler: {len(validation_result['errors'])}")
for error in validation_result["errors"]:
    print(f"  ❌ {error}")
print(f"Warnungen: {len(validation_result['warnings'])}")
for warning in validation_result["warnings"]:
    print(f"  ⚠️ {warning}")
print(f"✅ Ausführungszeit: {pandas_validation_time:.4f} Sekunden")

print("\n" + "=" * 70)
print("6️⃣  PERFORMANCE-VERGLEICH")
print("=" * 70)

# Größeres Dataset für Performance-Test
print("\n📊 Performance-Test mit 100.000 Datensätzen...")

# Großes Dataset erstellen
large_dates = pd.date_range("2023-01-01", periods=100000, freq="15min")
large_data = {
    "Zeitstempel": large_dates,
    "Maschine": np.random.choice(["LASER_001", "LASER_002", "PRESSE_001"], 100000),
    "Wert": np.random.uniform(1, 100, 100000),
    "Status": np.random.choice(["OK", "NOK"], 100000),
}
large_df = pd.DataFrame(large_data)

print(f"Test-Dataset: {len(large_df):,} Datensätze")

# Test 1: Filterung
print("\n1. Filterung Performance:")
start_time = time.time()
filtered_large = large_df[
    (large_df["Maschine"] == "LASER_001") & (large_df["Status"] == "OK")
]
filter_time = time.time() - start_time
print(f"   Pandas Filterung: {filter_time:.4f} Sekunden")
print(f"   Ergebnis: {len(filtered_large):,} Datensätze")
print("   VBA würde bei dieser Menge mehrere Minuten benötigen!")

# Test 2: Aggregation
print("\n2. Aggregation Performance:")
start_time = time.time()
agg_result = large_df.groupby(["Maschine", "Status"])["Wert"].agg(
    ["sum", "mean", "count"]
)
agg_time = time.time() - start_time
print(f"   Pandas Aggregation: {agg_time:.4f} Sekunden")
print("   VBA würde hier oft zum Absturz führen!")

# Test 3: Berechnungen
print("\n3. Berechnungen Performance:")
start_time = time.time()
large_df["Berechnet"] = (large_df["Wert"] * 1.19).round(2)  # MwSt.
large_df["Kategorie"] = np.where(large_df["Wert"] > 50, "Hoch", "Niedrig")
calc_time = time.time() - start_time
print(f"   Pandas Berechnungen: {calc_time:.4f} Sekunden")
print("   100.000 Berechnungen vektorisiert!")

print("\n" + "=" * 70)
print("7️⃣  AUTOMATISIERUNG UND INTEGRATION")
print("=" * 70)

print("\n🔴 VBA/EXCEL Limitations:")
print("❌ Nur in Excel-Umgebung lauffähig")
print("❌ Schwierige Integration in andere Systeme")
print("❌ Keine Web-APIs oder Datenbankverbindungen ohne Zusatztools")
print("❌ Begrenzte Bibliotheken und Funktionen")
print("❌ Schwer testbar und debuggbar")

print("\n🟢 PANDAS/PYTHON Vorteile:")
print("✅ Läuft überall (Server, Cloud, Desktop)")
print("✅ Einfache Integration in Webservices")
print("✅ Direkter Zugriff auf Datenbanken, APIs, Cloud-Services")
print("✅ Riesiges Ökosystem an Bibliotheken")
print("✅ Professionelle Entwicklungstools")
print("✅ Automatisierung via Cron/Task Scheduler")
print("✅ Version Control mit Git")
print("✅ CI/CD Pipeline Integration")

# Beispiel: Automatisierter Report
print("\n📈 Beispiel: Automatisierte Berichtserstellung")
print("# Python Code für automatisierten Report")
print(
    """
def generate_daily_report(data_source):
    # Daten laden (CSV, Datenbank, API...)
    df = pd.read_csv(data_source)

    # Analysen durchführen
    summary = df.groupby('Maschine').agg({
        'Produktion': 'sum',
        'Qualitaet': 'mean'
    })

    # Report erstellen
    report = f'''
    Tagesreport {datetime.now().strftime('%Y-%m-%d')}

    Gesamtproduktion: {df['Produktion'].sum():,} Stück
    Durchschnittsqualität: {df['Qualitaet'].mean():.2%}

    Details:
    {summary.to_string()}
    '''

    # Report versenden (E-Mail, Slack, etc.)
    send_report(report)

    return summary

# Automatisch jeden Tag um 7:00 ausführen
"""
)

print("\n" + "=" * 70)
print("8️⃣  MIGRATION ROADMAP: VON VBA ZU PANDAS")
print("=" * 70)

migration_steps = [
    {
        "Phase": "1. Assessment",
        "VBA_Tasks": "Inventory aller VBA-Skripte erstellen",
        "Python_Equivalent": "Funktionalitäten in Python/Pandas nachbauen",
        "Effort": "1-2 Wochen",
    },
    {
        "Phase": "2. Pilot Projekt",
        "VBA_Tasks": "Ein einfaches VBA-Skript auswählen",
        "Python_Equivalent": "In Python/Pandas reimplementieren",
        "Effort": "1 Woche",
    },
    {
        "Phase": "3. Team Training",
        "VBA_Tasks": "VBA-Kenntnisse dokumentieren",
        "Python_Equivalent": "Python/Pandas Schulungen",
        "Effort": "2-3 Wochen",
    },
    {
        "Phase": "4. Parallel Development",
        "VBA_Tasks": "VBA-Skripte weiter nutzen",
        "Python_Equivalent": "Python-Äquivalente entwickeln",
        "Effort": "4-6 Wochen",
    },
    {
        "Phase": "5. Production Migration",
        "VBA_Tasks": "VBA-Skripte schrittweise abschalten",
        "Python_Equivalent": "Python-Lösungen in Produktion",
        "Effort": "2-4 Wochen",
    },
]

print("\n🚀 Migration Roadmap:")
migration_df = pd.DataFrame(migration_steps)
print(migration_df.to_string(index=False))

print("\n" + "=" * 70)
print("9️⃣  FAZIT UND EMPFEHLUNGEN")
print("=" * 70)

comparison_summary = pd.DataFrame(
    {
        "Kriterium": [
            "Entwicklungszeit",
            "Performance",
            "Wartbarkeit",
            "Testbarkeit",
            "Skalierbarkeit",
            "Integration",
            "Fehlerbehandlung",
            "Wiederverwendung",
        ],
        "VBA/Excel": [
            "Langsam",
            "Schlecht",
            "Schwierig",
            "Minimal",
            "Begrenzt",
            "Schwierig",
            "Umständlich",
            "Niedrig",
        ],
        "Python/Pandas": [
            "Schnell",
            "Exzellent",
            "Einfach",
            "Ausgezeichnet",
            "Unbegrenzt",
            "Nahtlos",
            "Robust",
            "Hoch",
        ],
        "Faktor_Verbesserung": [
            "5-10x",
            "50-100x",
            "10x",
            "∞",
            "∞",
            "20x",
            "10x",
            "20x",
        ],
    }
)

print("\n📊 Vergleichstabelle:")
print(comparison_summary.to_string(index=False))

print("\n✅ EMPFEHLUNGEN FÜR BYSTRONIC:")
recommendations = [
    "Sofortiger Stopp neuer VBA-Entwicklungen",
    "Beginne mit einfachen, häufig genutzten Reports",
    "Investiere in Python/Pandas Training für das Team",
    "Etabliere Python als Standard für Datenanalyse",
    "Nutze Jupyter Notebooks für interaktive Analysen",
    "Implementiere automatisierte Tests für alle Skripte",
    "Verwende Git für Versionskontrolle",
    "Plane Migration über 6-12 Monate",
]

for i, rec in enumerate(recommendations, 1):
    print(f"{i:2d}. {rec}")

print("\n💰 ROI-Schätzung:")
print("   • Entwicklungszeit: 70% Reduktion")
print("   • Wartungsaufwand: 80% Reduktion")
print("   • Fehlerrate: 90% Reduktion")
print("   • Performance: 50-100x Verbesserung")
print("   • Gesamtkosten: 60% Reduktion nach 12 Monaten")

print("\n" + "=" * 70)
print("🎯 ZUSAMMENFASSUNG: VBA vs PANDAS")
print("=" * 70)
print("✅ Pandas ist VBA in allen Bereichen überlegen")
print("✅ 10-100x bessere Performance bei grossen Datenmengen")
print("✅ Einfachere Syntax für komplexe Operationen")
print("✅ Professionelle Entwicklungsumgebung")
print("✅ Unlimitierte Integrationsmöglichkeiten")
print("✅ Bessere Fehlerbehandlung und Testing")
print("✅ Zukunftssicher und industrieller Standard")
print("\n💡 Fazit: Die Migration von VBA zu Python/Pandas ist")
print("   nicht nur empfohlen, sondern essentiell für")
print("   moderne Datenverarbeitung bei Bystronic!")
