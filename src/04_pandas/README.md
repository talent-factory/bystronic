# Kapitel 4: Pandas für Datenanalyse

Willkommen zum vierten Kapitel des Python Grundkurses für
SmartFactory-Entwickler! 🐼📊

## 📚 Inhalte dieses Kapitels

### Hauptdokumentation

- **[04_pandas.ipynb](04_pandas.ipynb)** - Interaktives Jupyter Notebook mit
  Pandas-Grundlagen

### 💡 Beispiele

- **[dataframe_basics.py](beispiele/dataframe_basics.py)** -
  DataFrame-Erstellung und grundlegende Operationen
- **[data_import_export.py](beispiele/data_import_export.py)** - Daten aus CSV,
  Excel und anderen Quellen laden
- **[data_cleaning.py](beispiele/data_cleaning.py)** - Datenbereinigung und
  -validierung
- **[data_analysis.py](beispiele/data_analysis.py)** - Statistische Analysen und
  Gruppierungen
- **[vba_vs_pandas.py](beispiele/vba_vs_pandas.py)** - Vergleich Excel/VBA zu
  Pandas

### 🎯 Übungen

- **[Übung 1: DataFrame-Grundlagen](uebungen/uebung_01_dataframe_basics.py)** -
  Erstellen und Manipulieren von DataFrames
- **[Übung 2: Datenimport](uebungen/uebung_02_data_import.py)** - Laden
  verschiedener Datenformate
- **[Übung 3: Datenbereinigung](uebungen/uebung_03_data_cleaning.py)** - Umgang
  mit fehlenden und fehlerhaften Daten
- **[Übung 4: Datenanalyse](uebungen/uebung_04_data_analysis.py)** -
  Statistische Auswertungen und Visualisierungen

## 🚀 Schnellstart

### 1. Umgebung einrichten

```bash
# Im Projektverzeichnis
uv sync
uv shell
```

### 2. Jupyter Notebook starten

```bash
# Haupttutorial öffnen
uv run jupyter notebook src/04_pandas/04_pandas.ipynb
```

### 3. Beispiele ausführen

```bash
# DataFrame-Grundlagen
uv run python src/04_pandas/beispiele/dataframe_basics.py

# Datenimport
uv run python src/04_pandas/beispiele/data_import_export.py

# Datenbereinigung
uv run python src/04_pandas/beispiele/data_cleaning.py

# Datenanalyse
uv run python src/04_pandas/beispiele/data_analysis.py

# VBA-Vergleich
uv run python src/04_pandas/beispiele/vba_vs_pandas.py
```

### 4. Übungen bearbeiten

```bash
# Übung 1 - DataFrame-Grundlagen
uv run python src/04_pandas/uebungen/uebung_01_dataframe_basics.py

# Übung 2 - Datenimport
uv run python src/04_pandas/uebungen/uebung_02_data_import.py

# Übung 3 - Datenbereinigung
uv run python src/04_pandas/uebungen/uebung_03_data_cleaning.py

# Übung 4 - Datenanalyse
uv run python src/04_pandas/uebungen/uebung_04_data_analysis.py
```

## 📖 Lernziele

Nach diesem Kapitel können Sie:

✅ **DataFrames**: Erstellen, manipulieren und durchsuchen von tabellarischen
Daten ✅ **Datenimport**: CSV, Excel, JSON und andere Formate laden und speichern
✅ **Datenbereinigung**: Fehlende Werte, Duplikate und inkonsistente Daten
behandeln ✅ **Indexing**: Zeilen und Spalten effizient auswählen und filtern ✅
**Aggregation**: Daten gruppieren und statistische Kennzahlen berechnen ✅
**Zeitreihen**: Datum und Zeit-basierte Daten analysieren ✅ **Joins**: Mehrere
DataFrames zusammenführen ✅ **Visualisierung**: Grundlegende Diagramme direkt
aus Pandas erstellen

## 🔧 Pandas-Kernkonzepte

### Series vs DataFrame

```python
import pandas as pd

# Series: Ein-dimensionale Datenstruktur
temperaturen = pd.Series([20.5, 21.2, 19.8, 22.1],
                        index=['Mo', 'Di', 'Mi', 'Do'])

# DataFrame: Zwei-dimensionale Tabellenstruktur
maschinendaten = pd.DataFrame({
    'Maschine': ['Laser_01', 'Presse_02', 'Stanze_03'],
    'Produktionszeit': [8.5, 7.2, 9.1],
    'Ausschuss': [0.02, 0.05, 0.03],
    'Wartung_fällig': [True, False, True]
})
```

### Wichtige Pandas-Operationen

```python
# Daten laden
df = pd.read_csv('produktionsdaten.csv')
df = pd.read_excel('qualitaet.xlsx')

# Daten inspizieren
df.head()          # Erste 5 Zeilen
df.info()          # Datentypen und Speicher
df.describe()      # Statistische Kennzahlen

# Daten filtern
df[df['Ausschuss'] < 0.05]              # Filterkriterium
df.loc[df['Maschine'] == 'Laser_01']    # Label-basiert
df.iloc[0:3, 1:4]                       # Index-basiert

# Daten aggregieren
df.groupby('Maschine').mean()           # Gruppierung
df['Produktionszeit'].sum()             # Summierung
df.pivot_table(values='Ausschuss',      # Pivot-Tabelle
               index='Maschine')
```

## 💡 Tipps für Excel/VBA-Entwickler

### Excel-Arbeitsblätter vs DataFrames

```vba
' VBA: Arbeiten mit Worksheets
Dim ws As Worksheet
Set ws = ActiveSheet
Dim lastRow As Long
lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

For i = 2 To lastRow
    If ws.Cells(i, 3).Value > 0.05 Then  ' Spalte C > 0.05
        ws.Cells(i, 4).Value = "Hoch"    ' Spalte D = "Hoch"
    End If
Next i

' Python/Pandas: Vektorisierte Operationen
import pandas as pd
df = pd.read_excel('daten.xlsx')
df.loc[df['Ausschuss'] > 0.05, 'Kategorie'] = 'Hoch'
```

### VLOOKUP vs Merge/Join

```vba
' VBA: VLOOKUP-Formel
ws.Range("E2:E" & lastRow).Formula = _
    "=VLOOKUP(A2,Maschinen!A:C,3,FALSE)"

' Python/Pandas: JOIN-Operationen
maschinen_info = pd.read_excel('maschinen.xlsx')
produktionsdaten = pd.read_excel('produktion.xlsx')

# Left Join
result = produktionsdaten.merge(
    maschinen_info,
    on='Maschine',
    how='left'
)
```

### Pivot-Tabellen

```vba
' VBA: Pivot-Tabelle erstellen (sehr umständlich!)
Dim pt As PivotTable
' ... viele Zeilen Code ...

' Python/Pandas: Einfache Pivot-Tabellen
pivot = df.pivot_table(
    values='Produktionszeit',
    index='Abteilung',
    columns='Schicht',
    aggfunc='mean'
)
```

## 📊 Praktische Anwendungen für SmartFactory

### Produktionsdaten analysieren

```python
# Typische Maschinendaten-Analyse
produktionsdaten = pd.DataFrame({
    'Datum': pd.date_range('2024-01-01', periods=100, freq='D'),
    'Maschine': ['Laser_01', 'Presse_02', 'Stanze_03'] * 34,
    'Schicht': ['Früh', 'Spät', 'Nacht'] * 34,
    'Produktionszeit': np.random.uniform(6.0, 10.0, 100),
    'Ausschussmenge': np.random.uniform(0.01, 0.08, 100),
    'Energieverbrauch': np.random.uniform(150, 300, 100)
})

# Monatliche Auswertung
monatlich = produktionsdaten.set_index('Datum').resample('M').agg({
    'Produktionszeit': 'sum',
    'Ausschussmenge': 'mean',
    'Energieverbrauch': 'mean'
})

# Maschinenverfügbarkeit
verfügbarkeit = produktionsdaten.groupby('Maschine').agg({
    'Produktionszeit': ['mean', 'std'],
    'Ausschussmenge': 'mean'
})
```

### Qualitätskontrolle

```python
# Messdaten analysieren
qualitätsdaten = pd.read_csv('messwerte.csv')

# Statistische Prozesskontrolle
spc_grenzen = qualitätsdaten.groupby('Teil_Nr').agg({
    'Abmessung': ['mean', 'std']
})
spc_grenzen['UCL'] = (spc_grenzen[('Abmessung', 'mean')] +
                      3 * spc_grenzen[('Abmessung', 'std')])
spc_grenzen['LCL'] = (spc_grenzen[('Abmessung', 'mean')] -
                      3 * spc_grenzen[('Abmessung', 'std')])

# Ausreisser identifizieren
ausreisser = qualitätsdaten.merge(spc_grenzen, on='Teil_Nr')
ausreisser = ausreisser[
    (ausreisser['Abmessung'] > ausreisser['UCL']) |
    (ausreisser['Abmessung'] < ausreisser['LCL'])
]
```

### Wartungsplanung

```python
# Wartungsdaten verwalten
wartung = pd.DataFrame({
    'Maschine': ['Laser_01', 'Laser_02', 'Presse_01'],
    'Letzte_Wartung': ['2024-01-15', '2024-02-01', '2024-01-20'],
    'Wartungsintervall_Tage': [90, 90, 120],
    'Betriebsstunden': [2450, 1890, 3200]
})

# Datum-konvertierung
wartung['Letzte_Wartung'] = pd.to_datetime(wartung['Letzte_Wartung'])
wartung['Nächste_Wartung'] = (wartung['Letzte_Wartung'] +
                             pd.to_timedelta(wartung['Wartungsintervall_Tage'],
                                           unit='D'))

# Wartungen in den nächsten 30 Tagen
heute = pd.Timestamp.now()
bald_fällig = wartung[
    wartung['Nächste_Wartung'] <= heute + pd.Timedelta(days=30)
]
```

## 🎓 Überprüfen Sie Ihr Verständnis

Bevor Sie zum nächsten Kapitel wechseln:

- [ ] Können Sie DataFrames erstellen und grundlegende Operationen durchführen?
- [ ] Verstehen Sie Indexing, Filtering und Selection?
- [ ] Können Sie Daten aus verschiedenen Quellen importieren?
- [ ] Beherrschen Sie grundlegende Datenbereinigungstechniken?
- [ ] Können Sie Daten gruppieren und aggregieren?
- [ ] Verstehen Sie Join- und Merge-Operationen?
- [ ] Haben Sie alle vier Übungen erfolgreich gelöst?

## 📈 Performance-Tipps

### Effiziente Pandas-Nutzung

```python
# ❌ Langsam: Schleifen über Zeilen
for index, row in df.iterrows():
    df.at[index, 'new_col'] = row['col1'] * row['col2']

# ✅ Schnell: Vektorisierte Operationen
df['new_col'] = df['col1'] * df['col2']

# ❌ Langsam: Einzelne append()-Aufrufe
df_result = pd.DataFrame()
for chunk in data_chunks:
    df_result = df_result.append(chunk)

# ✅ Schnell: pd.concat() mit Liste
df_result = pd.concat(data_chunks, ignore_index=True)
```

## 📝 Zusätzliche Ressourcen

- **Pandas Documentation**: <https://pandas.pydata.org/docs/>
- **10 Minutes to Pandas**:
  <https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html>
- **Pandas Cookbook**:
  <https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html>
- **Real Python Pandas Tutorials**:
  <https://realpython.com/learning-paths/pandas-data-science/>

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels: **→
[Kapitel 5: Datenvisualisierung mit Matplotlib](../05_visualisierung/README.md)**

______________________________________________________________________

*Dieses Kapitel ist Teil des Python Grundkurses für SmartFactory-Entwickler*
