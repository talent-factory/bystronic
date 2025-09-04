# Kapitel 8: Benutzeroberflächen mit Python

Willkommen zum achten Kapitel des Python Grundkurses für Bystronic-Entwickler!
🖥️🎨🔧

## 📚 Inhalte dieses Kapitels

### Hauptdokumentation

- **[08_ui.ipynb](08_ui.ipynb)** - Interaktives Jupyter Notebook mit
  UI-Entwicklungs-Grundlagen

### 💡 Beispiele

#### PyQt/PySide (Desktop GUI)

- **[grundlagen_widget.py](beispiele/pyqt/grundlagen_widget.py)** - Erste
  Widgets und Layouts
- **[maschinendaten_gui.py](beispiele/pyqt/maschinendaten_gui.py)** -
  Industrielle Datenerfassung GUI
- **[diagramm_viewer.py](beispiele/pyqt/diagramm_viewer.py)** -
  Matplotlib-Integration in GUI
- **[datenbank_browser.py](beispiele/pyqt/datenbank_browser.py)** -
  Datenbank-CRUD-Interface
- **[moderne_ui.py](beispiele/pyqt/moderne_ui.py)** - Moderne UI-Elemente und
  Styling

#### Streamlit (Web-Dashboards)

- **[erste_webapp.py](beispiele/streamlit/erste_webapp.py)** - Grundlagen von
  Streamlit
- **[produktions_dashboard.py](beispiele/streamlit/produktions_dashboard.py)** -
  Produktionsübersicht-Dashboard
- **[qualitaets_monitor.py](beispiele/streamlit/qualitaets_monitor.py)** -
  Echtzeit-Qualitätskontrolle
- **[daten_upload.py](beispiele/streamlit/daten_upload.py)** - Datei-Upload und
  -verarbeitung
- **[interaktive_charts.py](beispiele/streamlit/interaktive_charts.py)** -
  Dynamische Diagramme

### 🎯 Übungen

- **[Übung 1: GUI-Grundlagen](uebungen/uebung_01_grundlagen.py)** - Erste
  PyQt-Anwendung erstellen
- **[Übung 2: Maschinendaten-Interface](uebungen/uebung_02_maschinen_ui.py)** -
  Industrielle Benutzeroberfläche
- **[Übung 3: Streamlit-Dashboard](uebungen/uebung_03_dashboard.py)** -
  Web-Dashboard entwickeln
- **[Übung 4: Vollständige Anwendung](uebungen/uebung_04_vollstaendige_app.py)**
  \- Komplette UI-Anwendung

## 🚀 Schnellstart

### 1. Umgebung einrichten

```bash
# Im Projektverzeichnis
uv sync
uv shell

# UI-Abhängigkeiten installieren
uv add PySide6 streamlit plotly-express
```

### 2. Jupyter Notebook starten

```bash
# Haupttutorial öffnen
uv run jupyter notebook src/08_ui/08_ui.ipynb
```

### 3. PyQt-Beispiele ausführen

```bash
# Grundlagen-Widget
uv run python src/08_ui/beispiele/pyqt/grundlagen_widget.py

# Maschinendaten-GUI
uv run python src/08_ui/beispiele/pyqt/maschinendaten_gui.py

# Diagramm-Viewer
uv run python src/08_ui/beispiele/pyqt/diagramm_viewer.py

# Datenbank-Browser
uv run python src/08_ui/beispiele/pyqt/datenbank_browser.py

# Moderne UI
uv run python src/08_ui/beispiele/pyqt/moderne_ui.py
```

### 4. Streamlit-Beispiele ausführen

```bash
# Erste Web-App
uv run streamlit run src/08_ui/beispiele/streamlit/erste_webapp.py

# Produktions-Dashboard
uv run streamlit run src/08_ui/beispiele/streamlit/produktions_dashboard.py

# Qualitäts-Monitor
uv run streamlit run src/08_ui/beispiele/streamlit/qualitaets_monitor.py

# Daten-Upload
uv run streamlit run src/08_ui/beispiele/streamlit/daten_upload.py

# Interaktive Charts
uv run streamlit run src/08_ui/beispiele/streamlit/interaktive_charts.py
```

### 5. Übungen bearbeiten

```bash
# Übung 1 - GUI-Grundlagen
uv run python src/08_ui/uebungen/uebung_01_grundlagen.py

# Übung 2 - Maschinendaten-Interface
uv run python src/08_ui/uebungen/uebung_02_maschinen_ui.py

# Übung 3 - Streamlit-Dashboard
uv run streamlit run src/08_ui/uebungen/uebung_03_dashboard.py

# Übung 4 - Vollständige Anwendung
uv run python src/08_ui/uebungen/uebung_04_vollstaendige_app.py
```

## 📖 Lernziele

Nach diesem Kapitel können Sie:

✅ **PyQt/PySide**: Desktop-GUI-Anwendungen mit modernen Widgets entwickeln ✅
**Layouts**: Flexible und responsive Benutzeroberflächen gestalten ✅ **Events**:
Benutzerinteraktionen verarbeiten und auf Ereignisse reagieren ✅ **Streamlit**:
Schnell Web-Dashboards für Datenvisualisierung erstellen ✅ **Integration**:
Matplotlib, Plotly und Pandas in UIs einbinden ✅ **Styling**: Professionelle und
ansprechende Benutzeroberflächen designen ✅ **Datenverarbeitung**: Echtzeitdaten
in UIs anzeigen und aktualisieren ✅ **Deployment**: UI-Anwendungen verteilen und
bereitstellen

## 🖥️ PyQt/PySide - Desktop-GUIs

### Grundlagen-Setup

```python
import sys
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QWidget, QPushButton, QLabel
)

class MeineApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bystronic Maschinendaten")
        self.setGeometry(100, 100, 800, 600)

        # Zentrales Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Layout
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Widgets hinzufügen
        label = QLabel("Willkommen zur Maschinendatenerfassung")
        button = QPushButton("Daten laden")
        button.clicked.connect(self.daten_laden)

        layout.addWidget(label)
        layout.addWidget(button)

    def daten_laden(self):
        print("Lade Maschinendaten...")

# App ausführen
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MeineApp()
    window.show()
    app.exec()
```

**📖 PyQt Ressourcen:**

- **PySide6 Dokumentation**:
  [https://doc.qt.io/qtforpython/](https://doc.qt.io/qtforpython/)
- **Qt Widgets**:
  [https://doc.qt.io/qt-6/qtwidgets-module.html](https://doc.qt.io/qt-6/qtwidgets-module.html)
- **Qt Designer**:
  [https://doc.qt.io/qt-6/qtdesigner-manual.html](https://doc.qt.io/qt-6/qtdesigner-manual.html)

### Moderne UI-Komponenten

```python
from PySide6.QtWidgets import (
    QProgressBar, QTableWidget, QTabWidget,
    QSlider, QSpinBox, QDateTimeEdit
)
from PySide6.QtCore import Qt

# Fortschrittsbalken für Maschinenauslastung
progress = QProgressBar()
progress.setValue(75)  # 75% Auslastung
progress.setFormat("Auslastung: %p%")

# Tabelle für Maschinendaten
table = QTableWidget(10, 5)
table.setHorizontalHeaderLabels([
    "Zeit", "Temperatur", "Druck", "Geschwindigkeit", "Status"
])

# Tabs für verschiedene Ansichten
tabs = QTabWidget()
tabs.addTab(produktions_widget, "Produktion")
tabs.addTab(qualitaets_widget, "Qualität")
tabs.addTab(wartungs_widget, "Wartung")
```

## 🌐 Streamlit - Web-Dashboards

### Einfaches Dashboard

```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Seitenkonfiguration
st.set_page_config(
    page_title="Bystronic Dashboard",
    page_icon="🏭",
    layout="wide"
)

# Titel und Beschreibung
st.title("🏭 Bystronic Produktions-Dashboard")
st.markdown("**Echtzeitübersicht der Maschinendaten**")

# Sidebar für Einstellungen
st.sidebar.header("Einstellungen")
maschine = st.sidebar.selectbox(
    "Maschine auswählen",
    ["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"]
)

# Metriken anzeigen
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Auslastung",
        value="87%",
        delta="5%"
    )

with col2:
    st.metric(
        label="Stückzahl/Std",
        value="245",
        delta="-12"
    )

with col3:
    st.metric(
        label="Temperatur",
        value="65°C",
        delta="2°C"
    )

with col4:
    st.metric(
        label="Qualitätsindex",
        value="98.5%",
        delta="0.3%"
    )

# Daten generieren und visualisieren
data = np.random.randn(100, 3)
df = pd.DataFrame(data, columns=['Temperatur', 'Druck', 'Geschwindigkeit'])

# Interaktive Diagramme
fig = px.line(df, title="Maschinendaten über Zeit")
st.plotly_chart(fig, use_container_width=True)
```

**📖 Streamlit Ressourcen:**

- **Homepage**: [https://streamlit.io/](https://streamlit.io/)
- **Dokumentation**: [https://docs.streamlit.io/](https://docs.streamlit.io/)
- **Gallery**: [https://streamlit.io/gallery](https://streamlit.io/gallery)
- **Components**:
  [https://streamlit.io/components](https://streamlit.io/components)

### Erweiterte Features

```python
# File Upload
uploaded_file = st.file_uploader(
    "Maschinendaten hochladen",
    type=['csv', 'xlsx'],
    help="Laden Sie Ihre Produktionsdaten hoch"
)

# Caching für Performance
@st.cache_data
def load_machine_data(file):
    return pd.read_csv(file)

# Session State für Datenerhaltung
if 'production_data' not in st.session_state:
    st.session_state.production_data = generate_sample_data()

# Echtzeitdaten mit Auto-Refresh
placeholder = st.empty()
with placeholder.container():
    # Wird automatisch aktualisiert
    current_data = get_live_data()
    st.dataframe(current_data)
```

## 🏭 Bystronic-Anwendungsfälle

### 1. Produktionsüberwachung

```python
class ProduktionsMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Produktionsüberwachung")

        # Timer für Echtzeitdaten
        self.timer = QTimer()
        self.timer.timeout.connect(self.aktualisiere_daten)
        self.timer.start(1000)  # Jede Sekunde

        self.setup_ui()

    def setup_ui(self):
        # Hauptlayout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Status-Panel
        self.status_label = QLabel("System bereit")
        layout.addWidget(self.status_label)

        # Maschinendaten-Tabelle
        self.data_table = QTableWidget()
        layout.addWidget(self.data_table)

        # Steuerungsbuttons
        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.stop_button = QPushButton("Stop")
        self.reset_button = QPushButton("Reset")

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.stop_button)
        button_layout.addWidget(self.reset_button)
        layout.addLayout(button_layout)

    def aktualisiere_daten(self):
        # Neue Daten von Maschinen abrufen
        neue_daten = self.hole_maschinendaten()
        self.update_table(neue_daten)
```

### 2. Qualitätskontroll-Dashboard

```python
def qualitaets_dashboard():
    st.title("🔍 Qualitätskontrolle")

    # Live-Qualitätsmetriken
    col1, col2, col3 = st.columns(3)

    with col1:
        # Ausschussrate
        ausschuss_rate = get_current_defect_rate()
        st.metric("Ausschussrate", f"{ausschuss_rate:.2f}%",
                 delta=f"{ausschuss_rate - 2.1:.2f}%")

    with col2:
        # Toleranzüberschreitungen
        toleranz_fehler = get_tolerance_violations()
        st.metric("Toleranzfehler", toleranz_fehler,
                 delta=f"{toleranz_fehler - 5}")

    with col3:
        # Prüfgeschwindigkeit
        pruef_geschwindigkeit = get_inspection_speed()
        st.metric("Prüfungen/Min", pruef_geschwindigkeit,
                 delta="15")

    # Echtzeit-Qualitätsverteilung
    quality_data = generate_quality_distribution()
    fig = px.histogram(quality_data, x='toleranz_abweichung',
                      title="Toleranzabweichungen")
    st.plotly_chart(fig, use_container_width=True)

    # Warnungen und Alerts
    if ausschuss_rate > 3.0:
        st.error("⚠️ Ausschussrate zu hoch! Sofortige Kontrolle erforderlich.")
    elif ausschuss_rate > 2.5:
        st.warning("⚡ Ausschussrate erhöht. Überwachung verstärken.")
    else:
        st.success("✅ Qualitätsparameter im Normbereich.")
```

### 3. Wartungsplaner

```python
class WartungsPlaner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wartungsplaner")
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Kalender für Wartungstermine
        self.kalender = QCalendarWidget()
        layout.addWidget(self.kalender)

        # Wartungsaufgaben-Liste
        self.aufgaben_liste = QListWidget()
        layout.addWidget(self.aufgaben_liste)

        # Neue Wartung hinzufügen
        self.neue_wartung_button = QPushButton("Neue Wartung planen")
        self.neue_wartung_button.clicked.connect(self.neue_wartung_dialog)
        layout.addWidget(self.neue_wartung_button)

    def neue_wartung_dialog(self):
        dialog = WartungsDialog(self)
        if dialog.exec() == QDialog.Accepted:
            wartung = dialog.get_wartung_data()
            self.add_wartung(wartung)
```

## 🎨 UI-Design Best Practices

### Professionelles Styling

```python
# PyQt Styling mit QSS (Qt Style Sheets)
app.setStyleSheet("""
QMainWindow {
    background-color: #f0f0f0;
}

QPushButton {
    background-color: #0066cc;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    font-weight: bold;
}

QPushButton:hover {
    background-color: #0052a3;
}

QPushButton:pressed {
    background-color: #003d7a;
}

QLabel {
    color: #333333;
    font-size: 12px;
}

QTableWidget {
    gridline-color: #d0d0d0;
    background-color: white;
    alternate-background-color: #f8f8f8;
}
""")

# Streamlit Custom CSS
st.markdown("""
<style>
.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.main-header {
    color: #0066cc;
    font-size: 2.5rem;
    font-weight: bold;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)
```

### Responsive Layouts

```python
# PyQt: Splitter für anpassbare Bereiche
splitter = QSplitter(Qt.Horizontal)
splitter.addWidget(linkes_panel)
splitter.addWidget(rechtes_panel)
splitter.setSizes([200, 600])

# Streamlit: Columns für responsive Layouts
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    # Hauptinhalt in der Mitte
    st.plotly_chart(fig)
```

## 💡 Performance-Optimierung

### Datenhandling

```python
# PyQt: Model/View für große Datenmengen
class MaschinendatenModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return len(self._data.columns)

    def data(self, index, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

# Streamlit: Caching für teure Operationen
@st.cache_data
def load_large_dataset():
    return pd.read_csv("large_machine_data.csv")

@st.cache_resource
def create_ml_model():
    return joblib.load("quality_prediction_model.pkl")
```

### Memory Management

```python
# PyQt: Explizite Cleanup
def closeEvent(self, event):
    # Timer stoppen
    if hasattr(self, 'timer'):
        self.timer.stop()

    # Datenverbindungen schließen
    if hasattr(self, 'db_connection'):
        self.db_connection.close()

    event.accept()

# Streamlit: Session State optimieren
if len(st.session_state.data_buffer) > 1000:
    # Alte Daten entfernen
    st.session_state.data_buffer = st.session_state.data_buffer[-500:]
```

## 🔧 Integration mit anderen Systemen

### Datenbank-Anbindung

```python
import sqlite3
from PySide6.QtCore import QThread, pyqtSignal

class DatabaseWorker(QThread):
    data_loaded = pyqtSignal(pd.DataFrame)

    def run(self):
        conn = sqlite3.connect('production.db')
        query = """
        SELECT timestamp, machine_id, temperature, pressure, status
        FROM machine_data
        WHERE timestamp >= datetime('now', '-1 hour')
        ORDER BY timestamp DESC
        """
        data = pd.read_sql_query(query, conn)
        conn.close()
        self.data_loaded.emit(data)
```

### API-Integration

```python
import requests
import streamlit as st

@st.cache_data(ttl=60)  # Cache für 1 Minute
def get_machine_status():
    try:
        response = requests.get("http://machine-api/status")
        return response.json()
    except requests.RequestException:
        return {"error": "API nicht erreichbar"}

# Verwendung in Streamlit
machine_data = get_machine_status()
if "error" in machine_data:
    st.error(machine_data["error"])
else:
    st.success("✅ Alle Maschinen online")
```

## 📱 Deployment und Distribution

### PyQt Application Packaging

```bash
# PyInstaller für Desktop-Apps
pip install pyinstaller
pyinstaller --onefile --windowed maschinendaten_gui.py

# Oder mit spezifischen Icons
pyinstaller --onefile --windowed --icon=bystronic.ico maschinendaten_gui.py
```

### Streamlit Deployment

```bash
# Lokales Deployment
streamlit run dashboard.py --server.port 8080

# Requirements für Cloud-Deployment
# requirements.txt:
# streamlit>=1.20.0
# pandas>=1.5.0
# plotly>=5.15.0
```

## 🎯 Überprüfen Sie Ihr Verständnis

Bevor Sie zum nächsten Kapitel wechseln:

- [ ] Können Sie einfache PyQt-Anwendungen mit Widgets erstellen?
- [ ] Verstehen Sie Layouts und Event-Handling in Desktop-GUIs?
- [ ] Können Sie Streamlit-Dashboards für Datenvisualisierung entwickeln?
- [ ] Beherrschen Sie die Integration von Matplotlib/Plotly in UIs?
- [ ] Können Sie Echtzeitdaten in UIs darstellen und aktualisieren?
- [ ] Verstehen Sie Performance-Optimierung für UI-Anwendungen?
- [ ] Können Sie professionelle UI-Designs umsetzen?
- [ ] Haben Sie alle vier Übungen erfolgreich gelöst?

## 📝 Zusätzliche Ressourcen

### PyQt/PySide Erweitert

- **Qt Documentation**: [https://doc.qt.io/](https://doc.qt.io/)
- **Qt Designer Tutorial**:
  [https://realpython.com/qt-designer-python/](https://realpython.com/qt-designer-python/)
- **Advanced PyQt**: [https://www.pythonguis.com/](https://www.pythonguis.com/)

### Streamlit Ecosystem

- **Streamlit Components**:
  [https://streamlit.io/components](https://streamlit.io/components)
- **Streamlit Cloud**: [https://streamlit.io/cloud](https://streamlit.io/cloud)
- **Advanced Streamlit**:
  [https://streamlit-tutorial.readthedocs.io/](https://streamlit-tutorial.readthedocs.io/)

### Alternative UI-Frameworks

- **Dash by Plotly**: [https://dash.plotly.com/](https://dash.plotly.com/) -
  Web-Apps für Datenvisualisierung
- **Flask + Bootstrap**: Klassische Web-Entwicklung
- **FastAPI + React**: Moderne API + Frontend-Kombination
- **Kivy**: Mobile und Desktop-Apps mit Python

## ➡️ Nächste Schritte

Nach erfolgreichem Abschluss dieses Kapitels: **→
[Kapitel 9: Praxisprojekte](../09_projekte/README.md)**

______________________________________________________________________

*Dieses Kapitel ist Teil des Python Grundkurses für Bystronic-Entwickler*
