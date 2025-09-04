#!/usr/bin/env python3
"""
Diagramm-Viewer mit Matplotlib-Integration
==========================================

Dieses Beispiel zeigt, wie Matplotlib-Plots in PyQt-Anwendungen
integriert werden können:
- Matplotlib-Canvas in PyQt
- Interaktive Plots
- Datenvisualisierung in Echtzeit
- Plot-Konfiguration und Export
- Navigation und Zoom

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import sys
from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
from PySide6.QtCore import Qt, QTimer
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDoubleSpinBox,
    QFileDialog,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)


class MaschinendatenPlot(FigureCanvas):
    """Custom Matplotlib-Canvas für Maschinendaten."""

    def __init__(self, parent=None, width=8, height=6, dpi=100):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        super().__init__(self.figure)
        self.setParent(parent)

        # Datenstrukturen
        self.timestamps = []
        self.temperature_data = []
        self.pressure_data = []
        self.speed_data = []
        self.power_data = []

        # Plot-Konfiguration
        self.show_temperature = True
        self.show_pressure = True
        self.show_speed = True
        self.show_power = False

        # Plots erstellen
        self.setup_plots()

    def setup_plots(self):
        """Erstellt die Subplot-Struktur."""
        self.figure.clear()

        # 2x2 Subplot-Layout
        self.ax1 = self.figure.add_subplot(2, 2, 1)  # Temperatur
        self.ax2 = self.figure.add_subplot(2, 2, 2)  # Druck
        self.ax3 = self.figure.add_subplot(2, 2, 3)  # Geschwindigkeit
        self.ax4 = self.figure.add_subplot(2, 2, 4)  # Leistung

        # Plot-Titel und Labels
        self.ax1.set_title('Temperatur [°C]', fontweight='bold')
        self.ax1.set_ylabel('Temperatur [°C]')
        self.ax1.grid(True, alpha=0.3)

        self.ax2.set_title('Druck [bar]', fontweight='bold')
        self.ax2.set_ylabel('Druck [bar]')
        self.ax2.grid(True, alpha=0.3)

        self.ax3.set_title('Schnittgeschwindigkeit [m/min]', fontweight='bold')
        self.ax3.set_ylabel('Geschwindigkeit [m/min]')
        self.ax3.set_xlabel('Zeit')
        self.ax3.grid(True, alpha=0.3)

        self.ax4.set_title('Leistungsaufnahme [kW]', fontweight='bold')
        self.ax4.set_ylabel('Leistung [kW]')
        self.ax4.set_xlabel('Zeit')
        self.ax4.grid(True, alpha=0.3)

        # Layout optimieren
        self.figure.tight_layout(pad=2.0)

    def add_data_point(self, timestamp, temperature, pressure, speed, power):
        """Fügt einen neuen Datenpunkt hinzu."""
        self.timestamps.append(timestamp)
        self.temperature_data.append(temperature)
        self.pressure_data.append(pressure)
        self.speed_data.append(speed)
        self.power_data.append(power)

        # Nur die letzten 50 Datenpunkte behalten
        max_points = 50
        if len(self.timestamps) > max_points:
            self.timestamps = self.timestamps[-max_points:]
            self.temperature_data = self.temperature_data[-max_points:]
            self.pressure_data = self.pressure_data[-max_points:]
            self.speed_data = self.speed_data[-max_points:]
            self.power_data = self.power_data[-max_points:]

        self.update_plots()

    def update_plots(self):
        """Aktualisiert alle Plots."""
        if not self.timestamps:
            return

        # Plots löschen
        self.ax1.clear()
        self.ax2.clear()
        self.ax3.clear()
        self.ax4.clear()

        # Temperatur-Plot
        self.ax1.plot(self.timestamps, self.temperature_data, 'r-', linewidth=2, label='Temperatur')
        self.ax1.axhline(y=70, color='orange', linestyle='--', alpha=0.7, label='Warnung')
        self.ax1.axhline(y=80, color='red', linestyle='--', alpha=0.7, label='Kritisch')
        self.ax1.set_title('Temperatur [°C]', fontweight='bold')
        self.ax1.set_ylabel('Temperatur [°C]')
        self.ax1.grid(True, alpha=0.3)
        self.ax1.legend()

        # Y-Achse für bessere Lesbarkeit anpassen
        if self.temperature_data:
            temp_min, temp_max = min(self.temperature_data), max(self.temperature_data)
            padding = (temp_max - temp_min) * 0.1 or 5
            self.ax1.set_ylim(temp_min - padding, temp_max + padding)

        # Druck-Plot
        self.ax2.plot(self.timestamps, self.pressure_data, 'b-', linewidth=2, label='Druck')
        self.ax2.axhline(y=6, color='red', linestyle='--', alpha=0.7, label='Min. Druck')
        self.ax2.axhline(y=10, color='red', linestyle='--', alpha=0.7, label='Max. Druck')
        self.ax2.set_title('Druck [bar]', fontweight='bold')
        self.ax2.set_ylabel('Druck [bar]')
        self.ax2.grid(True, alpha=0.3)
        self.ax2.legend()

        if self.pressure_data:
            press_min, press_max = min(self.pressure_data), max(self.pressure_data)
            padding = (press_max - press_min) * 0.1 or 1
            self.ax2.set_ylim(max(0, press_min - padding), press_max + padding)

        # Geschwindigkeits-Plot
        self.ax3.plot(self.timestamps, self.speed_data, 'g-', linewidth=2, label='Geschwindigkeit')
        self.ax3.axhline(y=2.0, color='orange', linestyle='--', alpha=0.7, label='Optimal')
        self.ax3.set_title('Schnittgeschwindigkeit [m/min]', fontweight='bold')
        self.ax3.set_ylabel('Geschwindigkeit [m/min]')
        self.ax3.set_xlabel('Zeit')
        self.ax3.grid(True, alpha=0.3)
        self.ax3.legend()

        # Leistungs-Plot
        self.ax4.plot(self.timestamps, self.power_data, 'm-', linewidth=2, label='Leistung')
        self.ax4.set_title('Leistungsaufnahme [kW]', fontweight='bold')
        self.ax4.set_ylabel('Leistung [kW]')
        self.ax4.set_xlabel('Zeit')
        self.ax4.grid(True, alpha=0.3)
        self.ax4.legend()

        # X-Achsen formatieren (nur Zeit anzeigen)
        for ax in [self.ax1, self.ax2, self.ax3, self.ax4]:
            ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
            ax.tick_params(axis='x', rotation=45)

        # Layout aktualisieren
        self.figure.tight_layout(pad=2.0)
        self.draw()

    def clear_data(self):
        """Löscht alle Daten."""
        self.timestamps.clear()
        self.temperature_data.clear()
        self.pressure_data.clear()
        self.speed_data.clear()
        self.power_data.clear()
        self.setup_plots()
        self.draw()


class StatistikPlot(FigureCanvas):
    """Canvas für statistische Auswertungen."""

    def __init__(self, parent=None):
        self.figure = Figure(figsize=(10, 6))
        super().__init__(self.figure)
        self.setParent(parent)

        self.create_sample_statistics()

    def create_sample_statistics(self):
        """Erstellt Beispiel-Statistiken."""
        self.figure.clear()

        # Daten generieren
        np.random.seed(42)

        # Subplot 1: Produktionsverteilung
        ax1 = self.figure.add_subplot(2, 2, 1)
        hours = ['06:00', '08:00', '10:00', '12:00', '14:00', '16:00', '18:00']
        production = [20, 45, 52, 48, 55, 43, 25]
        ax1.bar(hours, production, color='skyblue', alpha=0.7)
        ax1.set_title('Stündliche Produktion')
        ax1.set_ylabel('Teile pro Stunde')
        ax1.tick_params(axis='x', rotation=45)

        # Subplot 2: Qualitätsverteilung
        ax2 = self.figure.add_subplot(2, 2, 2)
        quality_data = np.random.normal(98.5, 1.2, 100)
        ax2.hist(quality_data, bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
        ax2.axvline(x=95, color='red', linestyle='--', label='Min. Qualität')
        ax2.set_title('Qualitätsverteilung')
        ax2.set_xlabel('Qualitätsindex [%]')
        ax2.set_ylabel('Häufigkeit')
        ax2.legend()

        # Subplot 3: Temperatur vs. Qualität
        ax3 = self.figure.add_subplot(2, 2, 3)
        temp_data = np.random.normal(65, 5, 50)
        quality_corr = 100 - (temp_data - 65)**2 * 0.1 + np.random.normal(0, 0.5, 50)
        ax3.scatter(temp_data, quality_corr, alpha=0.6, color='orange')
        ax3.set_title('Temperatur vs. Qualität')
        ax3.set_xlabel('Temperatur [°C]')
        ax3.set_ylabel('Qualität [%]')

        # Trendlinie
        z = np.polyfit(temp_data, quality_corr, 2)
        p = np.poly1d(z)
        temp_sorted = np.sort(temp_data)
        ax3.plot(temp_sorted, p(temp_sorted), "r--", alpha=0.8, label='Trend')
        ax3.legend()

        # Subplot 4: Maschinenauslastung
        ax4 = self.figure.add_subplot(2, 2, 4)
        machines = ['Laser 1', 'Laser 2', 'Stanze 1', 'Biege-\nmaschine']
        utilization = [87, 92, 78, 65]
        colors = ['red' if u < 70 else 'orange' if u < 85 else 'green' for u in utilization]

        bars = ax4.bar(machines, utilization, color=colors, alpha=0.7)
        ax4.set_title('Maschinenauslastung')
        ax4.set_ylabel('Auslastung [%]')
        ax4.set_ylim(0, 100)

        # Werte auf Balken anzeigen
        for bar, value in zip(bars, utilization, strict=False):
            ax4.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                    f'{value}%', ha='center', va='bottom', fontweight='bold')

        ax4.tick_params(axis='x', rotation=45)

        self.figure.tight_layout(pad=2.0)
        self.draw()


class DiagrammViewer(QMainWindow):
    """Hauptanwendung für Diagramm-Visualisierung."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bystronic Diagramm-Viewer")
        self.setGeometry(50, 50, 1400, 800)

        # Timer für Live-Daten
        self.data_timer = QTimer()
        self.data_timer.timeout.connect(self.generate_live_data)
        self.data_interval = 2000  # 2 Sekunden

        self.setup_ui()

    def setup_ui(self):
        """Erstellt die Benutzeroberfläche."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Hauptlayout
        main_layout = QVBoxLayout(central_widget)

        # Tab-Widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Tabs erstellen
        self.create_realtime_tab()
        self.create_statistics_tab()
        self.create_comparison_tab()
        self.create_export_tab()

    def create_realtime_tab(self):
        """Erstellt den Echtzeit-Tab."""
        tab = QWidget()
        layout = QHBoxLayout(tab)

        # Linke Seite - Plot
        plot_widget = QWidget()
        plot_layout = QVBoxLayout(plot_widget)

        # Matplotlib-Canvas
        self.realtime_plot = MaschinendatenPlot()
        plot_layout.addWidget(self.realtime_plot)

        # Navigation-Toolbar
        self.nav_toolbar = NavigationToolbar(self.realtime_plot, self)
        plot_layout.addWidget(self.nav_toolbar)

        layout.addWidget(plot_widget, 3)

        # Rechte Seite - Steuerung
        control_widget = QWidget()
        control_layout = QVBoxLayout(control_widget)

        # Live-Daten Steuerung
        live_group = QGroupBox("Live-Daten")
        live_layout = QVBoxLayout(live_group)

        self.start_button = QPushButton("Live-Daten starten")
        self.start_button.clicked.connect(self.start_live_data)
        live_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Live-Daten stoppen")
        self.stop_button.clicked.connect(self.stop_live_data)
        self.stop_button.setEnabled(False)
        live_layout.addWidget(self.stop_button)

        self.clear_button = QPushButton("Daten löschen")
        self.clear_button.clicked.connect(self.clear_data)
        live_layout.addWidget(self.clear_button)

        # Update-Intervall
        interval_layout = QHBoxLayout()
        interval_layout.addWidget(QLabel("Update-Intervall:"))
        self.interval_spin = QSpinBox()
        self.interval_spin.setRange(500, 10000)
        self.interval_spin.setValue(2000)
        self.interval_spin.setSuffix(" ms")
        self.interval_spin.valueChanged.connect(self.change_interval)
        interval_layout.addWidget(self.interval_spin)
        live_layout.addLayout(interval_layout)

        control_layout.addWidget(live_group)

        # Plot-Konfiguration
        config_group = QGroupBox("Plot-Konfiguration")
        config_layout = QVBoxLayout(config_group)

        self.temp_checkbox = QCheckBox("Temperatur anzeigen")
        self.temp_checkbox.setChecked(True)
        config_layout.addWidget(self.temp_checkbox)

        self.pressure_checkbox = QCheckBox("Druck anzeigen")
        self.pressure_checkbox.setChecked(True)
        config_layout.addWidget(self.pressure_checkbox)

        self.speed_checkbox = QCheckBox("Geschwindigkeit anzeigen")
        self.speed_checkbox.setChecked(True)
        config_layout.addWidget(self.speed_checkbox)

        self.power_checkbox = QCheckBox("Leistung anzeigen")
        self.power_checkbox.setChecked(False)
        config_layout.addWidget(self.power_checkbox)

        control_layout.addWidget(config_group)

        # Manueller Datenpunkt
        manual_group = QGroupBox("Manueller Datenpunkt")
        manual_layout = QVBoxLayout(manual_group)

        # Temperatur
        temp_layout = QHBoxLayout()
        temp_layout.addWidget(QLabel("Temperatur:"))
        self.temp_spin = QDoubleSpinBox()
        self.temp_spin.setRange(0, 100)
        self.temp_spin.setValue(65)
        self.temp_spin.setSuffix(" °C")
        temp_layout.addWidget(self.temp_spin)
        manual_layout.addLayout(temp_layout)

        # Druck
        press_layout = QHBoxLayout()
        press_layout.addWidget(QLabel("Druck:"))
        self.pressure_spin = QDoubleSpinBox()
        self.pressure_spin.setRange(0, 15)
        self.pressure_spin.setValue(8.2)
        self.pressure_spin.setSuffix(" bar")
        press_layout.addWidget(self.pressure_spin)
        manual_layout.addLayout(press_layout)

        # Geschwindigkeit
        speed_layout = QHBoxLayout()
        speed_layout.addWidget(QLabel("Geschwindigkeit:"))
        self.speed_spin = QDoubleSpinBox()
        self.speed_spin.setRange(0, 5)
        self.speed_spin.setValue(2.5)
        self.speed_spin.setSuffix(" m/min")
        speed_layout.addWidget(self.speed_spin)
        manual_layout.addLayout(speed_layout)

        # Leistung
        power_layout = QHBoxLayout()
        power_layout.addWidget(QLabel("Leistung:"))
        self.power_spin = QDoubleSpinBox()
        self.power_spin.setRange(0, 100)
        self.power_spin.setValue(50)
        self.power_spin.setSuffix(" kW")
        power_layout.addWidget(self.power_spin)
        manual_layout.addLayout(power_layout)

        add_point_button = QPushButton("Datenpunkt hinzufügen")
        add_point_button.clicked.connect(self.add_manual_point)
        manual_layout.addWidget(add_point_button)

        control_layout.addWidget(manual_group)

        # Export-Buttons
        export_group = QGroupBox("Export")
        export_layout = QVBoxLayout(export_group)

        save_plot_button = QPushButton("Plot als Bild speichern")
        save_plot_button.clicked.connect(self.save_plot)
        export_layout.addWidget(save_plot_button)

        save_data_button = QPushButton("Daten als CSV speichern")
        save_data_button.clicked.connect(self.save_data)
        export_layout.addWidget(save_data_button)

        control_layout.addWidget(export_group)

        # Stretch hinzufügen
        control_layout.addStretch()

        layout.addWidget(control_widget, 1)

        self.tab_widget.addTab(tab, "Echtzeit-Daten")

    def create_statistics_tab(self):
        """Erstellt den Statistik-Tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Titel
        title = QLabel("Produktionsstatistiken und Trends")
        title.setStyleSheet("font-size: 16px; font-weight: bold; margin: 10px;")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Statistik-Plot
        self.statistics_plot = StatistikPlot()
        layout.addWidget(self.statistics_plot)

        # Steuerungsbuttons
        button_layout = QHBoxLayout()

        refresh_button = QPushButton("Statistiken aktualisieren")
        refresh_button.clicked.connect(self.refresh_statistics)
        button_layout.addWidget(refresh_button)

        export_stats_button = QPushButton("Statistiken exportieren")
        export_stats_button.clicked.connect(self.export_statistics)
        button_layout.addWidget(export_stats_button)

        layout.addLayout(button_layout)

        self.tab_widget.addTab(tab, "Statistiken")

    def create_comparison_tab(self):
        """Erstellt den Vergleichs-Tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Info-Label
        info_label = QLabel("""
        Maschinenvergleich und Trend-Analyse

        Hier könnten verschiedene Maschinen verglichen werden:
        • Performance-Vergleich zwischen Maschinen
        • Historische Trends
        • Effizienz-Analyse
        • Wartungskorrelationen

        Diese Funktionalität würde in einer vollständigen Anwendung
        weitere Matplotlib-Plots mit komplexeren Datenquellen beinhalten.
        """)
        info_label.setStyleSheet("""
            border: 2px solid #ccc;
            padding: 20px;
            background-color: #f9f9f9;
            font-size: 14px;
        """)
        layout.addWidget(info_label)

        # Beispiel-Konfiguration
        config_group = QGroupBox("Vergleichskonfiguration")
        config_layout = QGridLayout(config_group)

        config_layout.addWidget(QLabel("Maschine 1:"), 0, 0)
        machine1_combo = QComboBox()
        machine1_combo.addItems(["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"])
        config_layout.addWidget(machine1_combo, 0, 1)

        config_layout.addWidget(QLabel("Maschine 2:"), 1, 0)
        machine2_combo = QComboBox()
        machine2_combo.addItems(["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"])
        machine2_combo.setCurrentIndex(1)
        config_layout.addWidget(machine2_combo, 1, 1)

        config_layout.addWidget(QLabel("Zeitraum:"), 2, 0)
        period_combo = QComboBox()
        period_combo.addItems(["Letzte Stunde", "Heute", "Diese Woche", "Dieser Monat"])
        config_layout.addWidget(period_combo, 2, 1)

        compare_button = QPushButton("Vergleich erstellen")
        compare_button.clicked.connect(self.create_comparison)
        config_layout.addWidget(compare_button, 3, 0, 1, 2)

        layout.addWidget(config_group)
        layout.addStretch()

        self.tab_widget.addTab(tab, "Vergleich")

    def create_export_tab(self):
        """Erstellt den Export-Tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Export-Optionen
        export_group = QGroupBox("Export-Optionen")
        export_layout = QVBoxLayout(export_group)

        # Dateiformat
        format_layout = QHBoxLayout()
        format_layout.addWidget(QLabel("Bildformat:"))
        self.format_combo = QComboBox()
        self.format_combo.addItems(["PNG", "PDF", "SVG", "JPG"])
        format_layout.addWidget(self.format_combo)
        layout.addWidget(export_group)
        export_layout.addLayout(format_layout)

        # Auflösung
        resolution_layout = QHBoxLayout()
        resolution_layout.addWidget(QLabel("DPI:"))
        self.dpi_spin = QSpinBox()
        self.dpi_spin.setRange(72, 600)
        self.dpi_spin.setValue(300)
        resolution_layout.addWidget(self.dpi_spin)
        export_layout.addLayout(resolution_layout)

        # Größe
        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Breite:"))
        self.width_spin = QSpinBox()
        self.width_spin.setRange(400, 2000)
        self.width_spin.setValue(1200)
        self.width_spin.setSuffix(" px")
        size_layout.addWidget(self.width_spin)

        size_layout.addWidget(QLabel("Höhe:"))
        self.height_spin = QSpinBox()
        self.height_spin.setRange(300, 1500)
        self.height_spin.setValue(800)
        self.height_spin.setSuffix(" px")
        size_layout.addWidget(self.height_spin)
        export_layout.addLayout(size_layout)

        # Export-Buttons
        export_button_layout = QHBoxLayout()

        export_current_button = QPushButton("Aktuellen Plot exportieren")
        export_current_button.clicked.connect(self.export_current_plot)
        export_button_layout.addWidget(export_current_button)

        export_all_button = QPushButton("Alle Plots exportieren")
        export_all_button.clicked.connect(self.export_all_plots)
        export_button_layout.addWidget(export_all_button)

        export_layout.addLayout(export_button_layout)

        layout.addWidget(export_group)

        # Report-Generation
        report_group = QGroupBox("Bericht erstellen")
        report_layout = QVBoxLayout(report_group)

        report_info = QLabel("""
        Automatische Berichtsgenerierung mit allen Diagrammen,
        Statistiken und Maschinendaten für Management-Präsentationen.
        """)
        report_layout.addWidget(report_info)

        generate_report_button = QPushButton("PDF-Bericht erstellen")
        generate_report_button.clicked.connect(self.generate_pdf_report)
        report_layout.addWidget(generate_report_button)

        layout.addWidget(report_group)
        layout.addStretch()

        self.tab_widget.addTab(tab, "Export")

    def start_live_data(self):
        """Startet die Live-Daten Generierung."""
        self.data_timer.start(self.data_interval)
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.statusBar().showMessage("Live-Daten gestartet", 3000)

    def stop_live_data(self):
        """Stoppt die Live-Daten Generierung."""
        self.data_timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.statusBar().showMessage("Live-Daten gestoppt", 3000)

    def clear_data(self):
        """Löscht alle Daten aus dem Plot."""
        self.realtime_plot.clear_data()
        self.statusBar().showMessage("Daten gelöscht", 3000)

    def change_interval(self, value):
        """Ändert das Update-Intervall."""
        self.data_interval = value
        if self.data_timer.isActive():
            self.data_timer.stop()
            self.data_timer.start(self.data_interval)

    def generate_live_data(self):
        """Generiert simulierte Live-Daten."""
        # Simulierte Maschinendaten
        base_temp = 65
        base_pressure = 8.2
        base_speed = 2.5
        base_power = 50

        # Leichte Schwankungen
        temp = max(0, base_temp + np.random.normal(0, 3))
        pressure = max(0, base_pressure + np.random.normal(0, 0.5))
        speed = max(0, base_speed + np.random.normal(0, 0.2))
        power = max(0, base_power + np.random.normal(0, 5))

        self.realtime_plot.add_data_point(
            datetime.now(), temp, pressure, speed, power
        )

    def add_manual_point(self):
        """Fügt einen manuellen Datenpunkt hinzu."""
        temp = self.temp_spin.value()
        pressure = self.pressure_spin.value()
        speed = self.speed_spin.value()
        power = self.power_spin.value()

        self.realtime_plot.add_data_point(
            datetime.now(), temp, pressure, speed, power
        )

        self.statusBar().showMessage("Manueller Datenpunkt hinzugefügt", 2000)

    def save_plot(self):
        """Speichert den aktuellen Plot als Bild."""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Plot speichern", "maschinendaten_plot.png",
            "PNG Files (*.png);;PDF Files (*.pdf);;SVG Files (*.svg)"
        )

        if filename:
            try:
                self.realtime_plot.figure.savefig(filename, dpi=300, bbox_inches='tight')
                QMessageBox.information(self, "Export", f"Plot gespeichert als: {filename}")
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"Fehler beim Speichern: {e}")

    def save_data(self):
        """Speichert die aktuellen Daten als CSV."""
        if not self.realtime_plot.timestamps:
            QMessageBox.information(self, "Info", "Keine Daten zum Speichern vorhanden.")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, "Daten speichern", "maschinendaten.csv",
            "CSV Files (*.csv)"
        )

        if filename:
            try:
                # Simulierter CSV-Export
                QMessageBox.information(self, "Export",
                    f"Daten würden gespeichert werden in: {filename}\n"
                    f"Datenpunkte: {len(self.realtime_plot.timestamps)}")
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"Fehler beim Speichern: {e}")

    def refresh_statistics(self):
        """Aktualisiert die Statistiken."""
        self.statistics_plot.create_sample_statistics()
        self.statusBar().showMessage("Statistiken aktualisiert", 3000)

    def export_statistics(self):
        """Exportiert die Statistiken."""
        filename, _ = QFileDialog.getSaveFileName(
            self, "Statistiken speichern", "statistiken.png",
            "PNG Files (*.png);;PDF Files (*.pdf)"
        )

        if filename:
            try:
                self.statistics_plot.figure.savefig(filename, dpi=300, bbox_inches='tight')
                QMessageBox.information(self, "Export", f"Statistiken gespeichert als: {filename}")
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"Fehler beim Exportieren: {e}")

    def create_comparison(self):
        """Erstellt einen Maschinenvergleich."""
        QMessageBox.information(self, "Vergleich",
            "Maschinenvergleich würde hier erstellt werden.\n"
            "In einer vollständigen Anwendung würde hier ein neuer\n"
            "Plot mit den Vergleichsdaten generiert werden.")

    def export_current_plot(self):
        """Exportiert den aktuell angezeigten Plot."""
        current_tab = self.tab_widget.currentIndex()

        filename, _ = QFileDialog.getSaveFileName(
            self, "Plot exportieren", f"plot_tab_{current_tab}.png",
            f"{self.format_combo.currentText()} Files (*.{self.format_combo.currentText().lower()})"
        )

        if filename:
            try:
                if current_tab == 0:  # Echtzeit-Tab
                    plot_widget = self.realtime_plot
                elif current_tab == 1:  # Statistik-Tab
                    plot_widget = self.statistics_plot
                else:
                    QMessageBox.information(self, "Info", "Dieser Tab enthält keinen exportierbaren Plot.")
                    return

                # DPI und Größe aus den Einstellungen verwenden
                dpi = self.dpi_spin.value()
                plot_widget.figure.savefig(filename, dpi=dpi, bbox_inches='tight')

                QMessageBox.information(self, "Export", f"Plot exportiert als: {filename}")
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"Fehler beim Export: {e}")

    def export_all_plots(self):
        """Exportiert alle verfügbaren Plots."""
        folder = QFileDialog.getExistingDirectory(self, "Ordner für Export wählen")

        if folder:
            try:
                # Echtzeit-Plot
                self.realtime_plot.figure.savefig(
                    f"{folder}/echtzeit_daten.{self.format_combo.currentText().lower()}",
                    dpi=self.dpi_spin.value(), bbox_inches='tight'
                )

                # Statistik-Plot
                self.statistics_plot.figure.savefig(
                    f"{folder}/statistiken.{self.format_combo.currentText().lower()}",
                    dpi=self.dpi_spin.value(), bbox_inches='tight'
                )

                QMessageBox.information(self, "Export", f"Alle Plots exportiert nach: {folder}")
            except Exception as e:
                QMessageBox.warning(self, "Fehler", f"Fehler beim Export: {e}")

    def generate_pdf_report(self):
        """Generiert einen PDF-Bericht."""
        filename, _ = QFileDialog.getSaveFileName(
            self, "PDF-Bericht speichern", "maschinendaten_bericht.pdf",
            "PDF Files (*.pdf)"
        )

        if filename:
            QMessageBox.information(self, "Bericht",
                f"PDF-Bericht würde erstellt werden: {filename}\n\n"
                "Der Bericht würde enthalten:\n"
                "• Alle aktuellen Diagramme\n"
                "• Produktionsstatistiken\n"
                "• Qualitätsmetriken\n"
                "• Maschinenstatus\n"
                "• Wartungsempfehlungen")


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Matplotlib-Style setzen
    plt.style.use('default')

    # Hauptfenster erstellen
    window = DiagrammViewer()
    window.statusBar().showMessage("Diagramm-Viewer bereit")
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
