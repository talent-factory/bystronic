# Kapitel 5: Visualisierung mit Python

Willkommen zum fünften Kapitel des Python Grundkurses für Bystronic-Entwickler! 📊📈🎨

## 📚 Inhalte dieses Kapitels

### Hauptdokumentation
- **[05_visualisierung.ipynb](05_visualisierung.ipynb)** - Interaktives Jupyter Notebook mit Visualisierungs-Grundlagen

### 💡 Beispiele
- **[matplotlib_grundlagen.py](beispiele/matplotlib_grundlagen.py)** - Matplotlib-Grundlagen und 2D-Diagramme
- **[interaktive_plots.py](beispiele/interaktive_plots.py)** - Interaktive Visualisierungen mit Widgets
- **[3d_visualisierung.py](beispiele/3d_visualisierung.py)** - 3D-Plots und räumliche Darstellungen
- **[seaborn_statistik.py](beispiele/seaborn_statistik.py)** - Statistische Visualisierungen mit Seaborn
- **[plotly_dashboards.py](beispiele/plotly_dashboards.py)** - Moderne Web-Visualisierungen mit Plotly
- **[maschinendaten_viz.py](beispiele/maschinendaten_viz.py)** - Industrielle Datenvisualisierung

### 🎯 Übungen
- **[Übung 1: Grundlagen](uebungen/uebung_01_grundlagen.py)** - Erste Schritte mit Matplotlib
- **[Übung 2: Statistische Plots](uebungen/uebung_02_statistik.py)** - Histogramme, Boxplots, Scatterplots
- **[Übung 3: 3D und Animation](uebungen/uebung_03_3d_animation.py)** - 3D-Visualisierungen und Animationen
- **[Übung 4: Dashboard-Entwicklung](uebungen/uebung_04_dashboards.py)** - Interaktive Dashboards erstellen

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
uv run jupyter notebook src/05_visualisierung/05_visualisierung.ipynb
```

### 3. Beispiele ausführen
```bash
# Matplotlib-Grundlagen
uv run python src/05_visualisierung/beispiele/matplotlib_grundlagen.py

# Interaktive Plots
uv run python src/05_visualisierung/beispiele/interaktive_plots.py

# 3D-Visualisierung
uv run python src/05_visualisierung/beispiele/3d_visualisierung.py

# Seaborn Statistiken
uv run python src/05_visualisierung/beispiele/seaborn_statistik.py

# Plotly Dashboards
uv run python src/05_visualisierung/beispiele/plotly_dashboards.py

# Maschinendaten-Visualisierung
uv run python src/05_visualisierung/beispiele/maschinendaten_viz.py
```

### 4. Übungen bearbeiten
```bash
# Übung 1 - Grundlagen
uv run python src/05_visualisierung/uebungen/uebung_01_grundlagen.py

# Übung 2 - Statistische Plots
uv run python src/05_visualisierung/uebungen/uebung_02_statistik.py

# Übung 3 - 3D und Animation
uv run python src/05_visualisierung/uebungen/uebung_03_3d_animation.py

# Übung 4 - Dashboards
uv run python src/05_visualisierung/uebungen/uebung_04_dashboards.py
```

## 📖 Lernziele

Nach diesem Kapitel können Sie:

✅ **Matplotlib**: 2D-Diagramme, Subplots und Anpassungen erstellen
✅ **Seaborn**: Statistische Visualisierungen und moderne Plot-Stile
✅ **Plotly**: Interaktive Web-Visualisierungen und Dashboards
✅ **3D-Plots**: Räumliche Darstellungen und 3D-Animationen
✅ **Interaktivität**: Widgets, Zoom, Pan und dynamische Updates
✅ **Styling**: Professionelle Layouts, Farben und Themes
✅ **Export**: Grafiken in verschiedenen Formaten speichern
✅ **Performance**: Große Datensätze effizient visualisieren

## 🎨 Visualisierungs-Bibliotheken

### Matplotlib - Die Basis
```python
import matplotlib.pyplot as plt
import numpy as np

# Einfacher Plot
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, label='sin(x)')
plt.xlabel('X-Werte')
plt.ylabel('Y-Werte')
plt.title('Sinus-Funktion')
plt.legend()
plt.grid(True)
plt.show()
```

**📖 Matplotlib Ressourcen:**
- **Homepage**: [https://matplotlib.org/](https://matplotlib.org/)
- **Dokumentation**: [https://matplotlib.org/stable/contents.html](https://matplotlib.org/stable/contents.html)
- **Gallery**: [https://matplotlib.org/stable/gallery/index.html](https://matplotlib.org/stable/gallery/index.html)
- **Tutorials**: [https://matplotlib.org/stable/tutorials/index.html](https://matplotlib.org/stable/tutorials/index.html)

### Seaborn - Statistische Visualisierung
```python
import seaborn as sns
import pandas as pd

# Moderner Plot-Stil
sns.set_style("whitegrid")
tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip",
               hue="size", size="size")
plt.title('Rechnung vs. Trinkgeld')
plt.show()
```

**📖 Seaborn Ressourcen:**
- **Homepage**: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)
- **API Reference**: [https://seaborn.pydata.org/api.html](https://seaborn.pydata.org/api.html)
- **Gallery**: [https://seaborn.pydata.org/examples/index.html](https://seaborn.pydata.org/examples/index.html)
- **Tutorial**: [https://seaborn.pydata.org/tutorial.html](https://seaborn.pydata.org/tutorial.html)

### Plotly - Interaktive Visualisierungen
```python
import plotly.graph_objects as go
import plotly.express as px

# Interaktiver 3D-Plot
fig = px.scatter_3d(df, x='x', y='y', z='z',
                   color='category', size='values',
                   title='3D Scatter Plot')
fig.show()
```

**📖 Plotly Ressourcen:**
- **Homepage**: [https://plotly.com/python/](https://plotly.com/python/)
- **Dokumentation**: [https://plotly.com/python-api-reference/](https://plotly.com/python-api-reference/)
- **Gallery**: [https://plotly.com/python/](https://plotly.com/python/)
- **Dash Framework**: [https://dash.plotly.com/](https://dash.plotly.com/)

## 📊 Diagrammtypen im Überblick

### 2D-Grundlagen
- **Liniendiagramme**: Zeitreihen, Trends, Verläufe
- **Balkendiagramme**: Kategorische Daten, Vergleiche
- **Histogramme**: Verteilungen, Häufigkeiten
- **Scatterplots**: Korrelationen, Zusammenhänge
- **Boxplots**: Statistik, Quartile, Ausreißer

### Spezialisierte Plots
- **Heatmaps**: Korrelationsmatrizen, 2D-Daten
- **Violin Plots**: Verteilungsformen
- **Contour Plots**: Höhenlinien, Funktionen
- **Polar Plots**: Kreisdiagramme, Richtungsdaten
- **Sankey Diagramme**: Flüsse, Verbindungen

### 3D-Visualisierungen
- **3D Scatter**: Punktwolken im Raum
- **3D Surface**: Oberflächen, Funktionen
- **3D Mesh**: Drahtgitter-Modelle
- **Volumetric**: Voxel-Daten, MRT-ähnlich

## 🏭 Bystronic-Anwendungen

### Maschinendaten-Dashboard
```python
# Produktionsübersicht
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Durchsatz pro Stunde
axes[0,0].plot(stunden, durchsatz)
axes[0,0].set_title('Stündlicher Durchsatz')

# Temperaturverteilung
axes[0,1].hist(temperaturen, bins=30)
axes[0,1].set_title('Temperaturverteilung')

# Korrelation Geschwindigkeit vs. Qualität
axes[1,0].scatter(geschwindigkeit, qualitaet)
axes[1,0].set_title('Geschwindigkeit vs. Qualität')

# Auslastung der letzten 7 Tage
axes[1,1].bar(tage, auslastung)
axes[1,1].set_title('Wöchentliche Auslastung')

plt.tight_layout()
plt.show()
```

### 3D-Materialanalyse
```python
# 3D-Visualisierung von Materialspannungen
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Mesh für Werkstück
X, Y = np.meshgrid(x_coords, y_coords)
Z = spannungsfeld(X, Y)

surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
ax.set_xlabel('X-Position (mm)')
ax.set_ylabel('Y-Position (mm)')
ax.set_zlabel('Spannung (MPa)')
plt.colorbar(surface)
plt.title('Spannungsverteilung im Werkstück')
plt.show()
```

## 💡 Best Practices

### Professionelle Layouts
```python
# Bystronic Corporate Design
plt.style.use('seaborn-v0_8-whitegrid')
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(data, color=colors[0], linewidth=2.5)
ax.set_title('Maschinendaten Analyse', fontsize=16, fontweight='bold')
ax.grid(True, alpha=0.3)
plt.tight_layout()
```

### Performance-Optimierung
```python
# Für große Datensätze
plt.rcParams['agg.path.chunksize'] = 10000

# Weniger Datenpunkte bei interaktiven Plots
if len(data) > 10000:
    step = len(data) // 1000
    data_subset = data[::step]
```

## 🎯 Überprüfen Sie Ihr Verständnis

Bevor Sie zum nächsten Kapitel wechseln:

- [ ] Können Sie einfache 2D-Plots mit Matplotlib erstellen?
- [ ] Verstehen Sie Subplots und Layout-Management?
- [ ] Können Sie statistische Plots mit Seaborn erstellen?
- [ ] Beherrschen Sie 3D-Visualisierungen?
- [ ] Können Sie interaktive Plots mit Plotly erstellen?
- [ ] Verstehen Sie Plot-Styling und Themes?
- [ ] Können Sie Plots in verschiedenen Formaten exportieren?
- [ ] Haben Sie alle vier Übungen erfolgreich gelöst?

## 📝 Zusätzliche Ressourcen

### NumPy & Pandas Integration
- **NumPy Plotting**: [https://numpy.org/doc/stable/user/quickstart.html#plotting](https://numpy.org/doc/stable/user/quickstart.html#plotting)
- **Pandas Plotting**: [https://pandas.pydata.org/docs/user_guide/visualization.html](https://pandas.pydata.org/docs/user_guide/visualization.html)

### Erweiterte Bibliotheken
- **Bokeh**: [https://bokeh.org/](https://bokeh.org/) - Web-native interaktive Visualisierungen
- **Altair**: [https://altair-viz.github.io/](https://altair-viz.github.io/) - Grammar of Graphics für Python
- **Holoviews**: [https://holoviews.org/](https://holoviews.org/) - Hochdimensionale Datenvisualisierung

### Specialized Tools
- **Mayavi**: [https://docs.enthought.com/mayavi/mayavi/](https://docs.enthought.com/mayavi/mayavi/) - 3D wissenschaftliche Visualisierung
- **PyVista**: [https://pyvista.org/](https://pyvista.org/) - 3D Plotting und Mesh-Analyse

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels:
**→ [Kapitel 6: Datenimport und -export](../06_datenimport/README.md)**

---
*Dieses Kapitel ist Teil des Python Grundkurses für Bystronic-Entwickler*
