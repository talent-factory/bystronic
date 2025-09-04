#!/usr/bin/env python3
"""
Maschinendaten-GUI für industrielle Anwendungen
==============================================

Dieses Beispiel zeigt eine realistische industrielle GUI für die
Überwachung und Steuerung von Bystronic-Maschinen:
- Echtzeitdaten-Anzeige
- Maschinensteuerung
- Datenprotokollierung
- Alarm-Management
- Wartungsplanung

Autor: Daniel Senften
"""

import sqlite3
import sys
from datetime import datetime

import numpy as np
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtGui import QAction, QColor
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateTimeEdit,
    QDialog,
    QDialogButtonBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class MaschinendatenWorker(QThread):
    """Worker-Thread für das Laden von Maschinendaten."""

    data_updated = Signal(dict)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        """Simuliert das kontinuierliche Laden von Maschinendaten."""
        self.running = True
        while self.running:
            # Simulierte Maschinendaten generieren
            data = self.generate_machine_data()
            self.data_updated.emit(data)
            self.msleep(1000)  # 1 Sekunde warten

    def stop(self):
        """Stoppt den Worker-Thread."""
        self.running = False

    def generate_machine_data(self):
        """Generiert simulierte Maschinendaten."""
        base_temp = 65
        base_pressure = 8.2
        base_speed = 2.5

        # Leichte Schwankungen simulieren
        temp_variation = np.random.normal(0, 2)
        pressure_variation = np.random.normal(0, 0.3)
        speed_variation = np.random.normal(0, 0.1)

        return {
            "timestamp": datetime.now(),
            "temperature": max(0, base_temp + temp_variation),
            "pressure": max(0, base_pressure + pressure_variation),
            "cutting_speed": max(0, base_speed + speed_variation),
            "parts_produced": np.random.randint(240, 260),
            "quality_index": np.random.uniform(95, 99.5),
            "power_consumption": np.random.uniform(45, 55),
            "status": np.random.choice(
                ["Normal", "Normal", "Normal", "Warnung"], p=[0.85, 0.1, 0.04, 0.01]
            ),
        }


class AlarmDialog(QDialog):
    """Dialog für Alarm-Details."""

    def __init__(self, alarm_data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Alarm-Details")
        self.setModal(True)
        self.resize(400, 300)

        layout = QVBoxLayout(self)

        # Alarm-Informationen
        info_label = QLabel(
            f"<b>Alarm:</b> {alarm_data['type']}<br>"
            f"<b>Zeit:</b> {alarm_data['timestamp']}<br>"
            f"<b>Maschine:</b> {alarm_data['machine']}<br>"
            f"<b>Schweregrad:</b> {alarm_data['severity']}"
        )
        layout.addWidget(info_label)

        # Beschreibung
        desc_label = QLabel("Beschreibung:")
        layout.addWidget(desc_label)

        self.description = QTextEdit()
        self.description.setPlainText(alarm_data["description"])
        layout.addWidget(self.description)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)


class WartungsDialog(QDialog):
    """Dialog für Wartungsplanung."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Wartung planen")
        self.setModal(True)
        self.resize(450, 350)

        layout = QVBoxLayout(self)

        # Maschinenwahl
        machine_layout = QHBoxLayout()
        machine_layout.addWidget(QLabel("Maschine:"))
        self.machine_combo = QComboBox()
        self.machine_combo.addItems(["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"])
        machine_layout.addWidget(self.machine_combo)
        layout.addLayout(machine_layout)

        # Wartungstyp
        type_layout = QHBoxLayout()
        type_layout.addWidget(QLabel("Wartungstyp:"))
        self.type_combo = QComboBox()
        self.type_combo.addItems(
            ["Routinewartung", "Präventivwartung", "Reparatur", "Kalibrierung"]
        )
        type_layout.addWidget(self.type_combo)
        layout.addLayout(type_layout)

        # Geplantes Datum
        date_layout = QHBoxLayout()
        date_layout.addWidget(QLabel("Geplant für:"))
        self.date_edit = QDateTimeEdit(datetime.now())
        date_layout.addWidget(self.date_edit)
        layout.addLayout(date_layout)

        # Beschreibung
        layout.addWidget(QLabel("Beschreibung:"))
        self.description = QTextEdit()
        self.description.setPlaceholderText("Wartungsdetails eingeben...")
        layout.addWidget(self.description)

        # Geschätzte Dauer
        duration_layout = QHBoxLayout()
        duration_layout.addWidget(QLabel("Geschätzte Dauer (Stunden):"))
        self.duration_spin = QSpinBox()
        self.duration_spin.setRange(1, 24)
        self.duration_spin.setValue(2)
        duration_layout.addWidget(self.duration_spin)
        layout.addLayout(duration_layout)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def get_wartung_data(self):
        """Gibt die eingegebenen Wartungsdaten zurück."""
        return {
            "machine": self.machine_combo.currentText(),
            "type": self.type_combo.currentText(),
            "planned_date": self.date_edit.dateTime().toPython(),
            "description": self.description.toPlainText(),
            "estimated_duration": self.duration_spin.value(),
        }


class MaschinendatenGUI(QMainWindow):
    """Hauptanwendung für Maschinendaten-Management."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bystronic Maschinendaten-Zentrale")
        self.setGeometry(50, 50, 1400, 900)

        # Datenstrukturen
        self.machine_data_history = []
        self.alarms = []
        self.maintenance_schedule = []

        # Worker-Thread für Daten
        self.data_worker = MaschinendatenWorker()
        self.data_worker.data_updated.connect(self.update_machine_data)

        self.setup_ui()
        self.setup_menubar()
        self.setup_statusbar()

        # Datenbank initialisieren
        self.init_database()

        # Worker starten
        self.data_worker.start()

    def setup_menubar(self):
        """Erstellt die Menüleiste."""
        menubar = self.menuBar()

        # Datei-Menü
        file_menu = menubar.addMenu("&Datei")

        export_action = QAction("Daten &exportieren", self)
        export_action.triggered.connect(self.export_data)
        file_menu.addAction(export_action)

        file_menu.addSeparator()

        exit_action = QAction("&Beenden", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)

        # Maschinen-Menü
        machine_menu = menubar.addMenu("&Maschinen")

        start_action = QAction("&Starten", self)
        start_action.triggered.connect(self.start_machine)
        machine_menu.addAction(start_action)

        stop_action = QAction("&Stoppen", self)
        stop_action.triggered.connect(self.stop_machine)
        machine_menu.addAction(stop_action)

        # Wartung-Menü
        maintenance_menu = menubar.addMenu("&Wartung")

        schedule_action = QAction("Wartung &planen", self)
        schedule_action.triggered.connect(self.schedule_maintenance)
        maintenance_menu.addAction(schedule_action)

    def setup_statusbar(self):
        """Erstellt die Statusleiste."""
        self.status_bar = self.statusBar()

        # Status-Labels
        self.connection_status = QLabel("Verbunden")
        self.connection_status.setStyleSheet("color: green; font-weight: bold;")
        self.status_bar.addPermanentWidget(self.connection_status)

        self.data_status = QLabel("Daten: Aktuell")
        self.status_bar.addPermanentWidget(self.data_status)

        self.status_bar.showMessage("System bereit")

    def setup_ui(self):
        """Erstellt die Hauptbenutzeroberfläche."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Hauptlayout
        main_layout = QVBoxLayout(central_widget)

        # Oberer Bereich - Schnellübersicht
        self.create_overview_section(main_layout)

        # Hauptbereich mit Tabs
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Verschiedene Tabs erstellen
        self.create_realtime_tab()
        self.create_production_tab()
        self.create_maintenance_tab()
        self.create_alarms_tab()
        self.create_reports_tab()

    def create_overview_section(self, parent_layout):
        """Erstellt den Übersichtsbereich."""
        overview_group = QGroupBox("Schnellübersicht")
        overview_layout = QGridLayout(overview_group)

        # KPI-Karten
        self.create_kpi_card(
            overview_layout, "Maschinenauslastung", "87%", 0, 0, "green"
        )
        self.create_kpi_card(overview_layout, "Stückzahl/Stunde", "245", 0, 1, "blue")
        self.create_kpi_card(overview_layout, "Qualitätsindex", "98.5%", 0, 2, "orange")
        self.create_kpi_card(overview_layout, "Aktive Alarme", "2", 0, 3, "red")

        parent_layout.addWidget(overview_group)

    def create_kpi_card(self, layout, title, value, row, col, color):
        """Erstellt eine KPI-Karte."""
        card = QGroupBox()
        card_layout = QVBoxLayout(card)

        title_label = QLabel(title)
        title_label.setAlignment(Qt.AlignCenter)
        card_layout.addWidget(title_label)

        value_label = QLabel(value)
        value_label.setAlignment(Qt.AlignCenter)
        value_label.setStyleSheet(
            f"font-size: 24px; font-weight: bold; color: {color};"
        )
        card_layout.addWidget(value_label)

        # Referenz speichern für Updates
        setattr(
            self,
            f"kpi_{title.lower().replace(' ', '_').replace('/', '_')}",
            value_label,
        )

        layout.addWidget(card, row, col)

    def create_realtime_tab(self):
        """Erstellt den Echtzeit-Daten Tab."""
        tab = QWidget()
        layout = QHBoxLayout(tab)

        # Linke Seite - Aktuelle Werte
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)

        # Maschinenstatus
        status_group = QGroupBox("Maschinenstatus")
        status_layout = QVBoxLayout(status_group)

        self.machine_status_label = QLabel("Status: Bereit")
        self.machine_status_label.setStyleSheet(
            "padding: 10px; background-color: lightgreen; "
            "border: 2px solid green; font-weight: bold;"
        )
        status_layout.addWidget(self.machine_status_label)

        left_layout.addWidget(status_group)

        # Aktuelle Messwerte
        values_group = QGroupBox("Aktuelle Messwerte")
        values_layout = QVBoxLayout(values_group)

        self.temp_label = QLabel("Temperatur: 65°C")
        self.pressure_label = QLabel("Druck: 8.2 bar")
        self.speed_label = QLabel("Schnittgeschwindigkeit: 2.5 m/min")
        self.power_label = QLabel("Leistungsaufnahme: 50 kW")

        for label in [
            self.temp_label,
            self.pressure_label,
            self.speed_label,
            self.power_label,
        ]:
            label.setStyleSheet("padding: 8px; border: 1px solid gray; margin: 2px;")
            values_layout.addWidget(label)

        left_layout.addWidget(values_group)

        # Steuerung
        control_group = QGroupBox("Maschinensteuerung")
        control_layout = QVBoxLayout(control_group)

        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.setStyleSheet(
            "background-color: green; color: white; font-weight: bold;"
        )
        self.start_button.clicked.connect(self.start_machine)

        self.stop_button = QPushButton("Stopp")
        self.stop_button.setStyleSheet(
            "background-color: red; color: white; font-weight: bold;"
        )
        self.stop_button.clicked.connect(self.stop_machine)

        self.pause_button = QPushButton("Pause")
        self.pause_button.setStyleSheet(
            "background-color: orange; color: white; font-weight: bold;"
        )
        self.pause_button.clicked.connect(self.pause_machine)

        button_layout.addWidget(self.start_button)
        button_layout.addWidget(self.pause_button)
        button_layout.addWidget(self.stop_button)
        control_layout.addLayout(button_layout)

        left_layout.addWidget(control_group)

        layout.addWidget(left_widget, 1)

        # Rechte Seite - Diagramme (Platzhalter)
        right_widget = QGroupBox("Verlaufsdiagramme")
        right_layout = QVBoxLayout(right_widget)

        # Matplotlib-Canvas würde hier eingefügt
        chart_placeholder = QLabel(
            "Hier würden Matplotlib-Diagramme angezeigt:\n\n"
            "• Temperaturverlauf\n"
            "• Druckverlauf\n"
            "• Geschwindigkeitsprofil\n"
            "• Leistungsaufnahme"
        )
        chart_placeholder.setAlignment(Qt.AlignCenter)
        chart_placeholder.setStyleSheet("border: 2px dashed gray; padding: 20px;")
        right_layout.addWidget(chart_placeholder)

        layout.addWidget(right_widget, 2)

        self.tab_widget.addTab(tab, "Echtzeit-Daten")

    def create_production_tab(self):
        """Erstellt den Produktions-Tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Produktionsübersicht
        production_group = QGroupBox("Tagesproduktion")
        production_layout = QHBoxLayout(production_group)

        # Produktions-Metriken
        metrics_layout = QVBoxLayout()

        self.production_target = QLabel("Tagesziel: 2000 Teile")
        self.production_current = QLabel("Aktuell: 1450 Teile")
        self.production_rate = QLabel("Rate: 245 Teile/Stunde")
        self.production_efficiency = QLabel("Effizienz: 87%")

        for label in [
            self.production_target,
            self.production_current,
            self.production_rate,
            self.production_efficiency,
        ]:
            label.setStyleSheet("padding: 8px; border: 1px solid blue; margin: 2px;")
            metrics_layout.addWidget(label)

        production_layout.addLayout(metrics_layout)

        # Fortschrittsbalken
        progress_layout = QVBoxLayout()

        progress_layout.addWidget(QLabel("Tagesfortschritt:"))
        self.daily_progress = QProgressBar()
        self.daily_progress.setValue(72)  # 72% des Tagesziels
        progress_layout.addWidget(self.daily_progress)

        progress_layout.addWidget(QLabel("Qualitätsindex:"))
        self.quality_progress = QProgressBar()
        self.quality_progress.setValue(98)
        progress_layout.addWidget(self.quality_progress)

        production_layout.addLayout(progress_layout)

        layout.addWidget(production_group)

        # Produktionsliste
        production_list_group = QGroupBox("Produktionsaufträge")
        list_layout = QVBoxLayout(production_list_group)

        self.production_table = QTableWidget(10, 6)
        self.production_table.setHorizontalHeaderLabels(
            ["Auftragsnr", "Teil", "Menge", "Status", "Start", "Ende"]
        )

        # Beispieldaten
        sample_orders = [
            ["PO-001", "Flansch 150mm", "50", "Läuft", "08:00", "10:30"],
            ["PO-002", "Gehäuse Typ A", "25", "Wartend", "10:30", "12:00"],
            ["PO-003", "Blech 5mm", "100", "Wartend", "13:00", "16:00"],
            ["PO-004", "Halterung", "75", "Geplant", "16:00", "18:30"],
        ]

        for row, order in enumerate(sample_orders):
            for col, value in enumerate(order):
                item = QTableWidgetItem(value)
                if col == 3:  # Status-Spalte
                    if value == "Läuft":
                        item.setBackground(QColor("lightgreen"))
                    elif value == "Wartend":
                        item.setBackground(QColor("lightyellow"))
                    elif value == "Geplant":
                        item.setBackground(QColor("lightblue"))
                self.production_table.setItem(row, col, item)

        self.production_table.resizeColumnsToContents()
        list_layout.addWidget(self.production_table)

        layout.addWidget(production_list_group)

        self.tab_widget.addTab(tab, "Produktion")

    def create_maintenance_tab(self):
        """Erstellt den Wartungs-Tab."""
        tab = QWidget()
        layout = QHBoxLayout(tab)

        # Linke Seite - Wartungsplanung
        left_widget = QGroupBox("Wartungsplanung")
        left_layout = QVBoxLayout(left_widget)

        # Neue Wartung planen
        plan_button = QPushButton("Neue Wartung planen")
        plan_button.clicked.connect(self.schedule_maintenance)
        left_layout.addWidget(plan_button)

        # Wartungsliste
        self.maintenance_list = QListWidget()
        self.maintenance_list.addItems(
            [
                "Laser 1: Routinewartung - 05.09.2024",
                "Stanze 1: Kalibrierung - 07.09.2024",
                "Biegemaschine: Reparatur - 10.09.2024",
            ]
        )
        left_layout.addWidget(self.maintenance_list)

        layout.addWidget(left_widget)

        # Rechte Seite - Wartungshistorie
        right_widget = QGroupBox("Wartungshistorie")
        right_layout = QVBoxLayout(right_widget)

        self.maintenance_history = QTableWidget(8, 5)
        self.maintenance_history.setHorizontalHeaderLabels(
            ["Datum", "Maschine", "Typ", "Dauer", "Status"]
        )

        # Beispiel-Wartungshistorie
        history_data = [
            ["02.09.2024", "Laser 1", "Routinewartung", "2h", "Abgeschlossen"],
            ["30.08.2024", "Laser 2", "Reparatur", "4h", "Abgeschlossen"],
            ["28.08.2024", "Stanze 1", "Kalibrierung", "1h", "Abgeschlossen"],
            ["25.08.2024", "Biegemaschine", "Präventiv", "3h", "Abgeschlossen"],
        ]

        for row, entry in enumerate(history_data):
            for col, value in enumerate(entry):
                item = QTableWidgetItem(value)
                if col == 4 and value == "Abgeschlossen":
                    item.setBackground(QColor("lightgreen"))
                self.maintenance_history.setItem(row, col, item)

        self.maintenance_history.resizeColumnsToContents()
        right_layout.addWidget(self.maintenance_history)

        layout.addWidget(right_widget)

        self.tab_widget.addTab(tab, "Wartung")

    def create_alarms_tab(self):
        """Erstellt den Alarm-Tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Alarm-Übersicht
        alarm_overview = QGroupBox("Aktive Alarme")
        overview_layout = QHBoxLayout(alarm_overview)

        # Alarm-Zähler
        self.critical_alarms = QLabel("Kritisch: 0")
        self.critical_alarms.setStyleSheet(
            "color: red; font-weight: bold; font-size: 16px;"
        )

        self.warning_alarms = QLabel("Warnung: 2")
        self.warning_alarms.setStyleSheet(
            "color: orange; font-weight: bold; font-size: 16px;"
        )

        self.info_alarms = QLabel("Info: 1")
        self.info_alarms.setStyleSheet(
            "color: blue; font-weight: bold; font-size: 16px;"
        )

        overview_layout.addWidget(self.critical_alarms)
        overview_layout.addWidget(self.warning_alarms)
        overview_layout.addWidget(self.info_alarms)

        layout.addWidget(alarm_overview)

        # Alarm-Liste
        alarm_list_group = QGroupBox("Alarm-Details")
        list_layout = QVBoxLayout(alarm_list_group)

        self.alarm_table = QTableWidget(10, 6)
        self.alarm_table.setHorizontalHeaderLabels(
            ["Zeit", "Maschine", "Typ", "Schweregrad", "Beschreibung", "Status"]
        )

        # Beispiel-Alarme
        alarm_data = [
            ["14:32", "Laser 1", "Temperatur", "Warnung", "Temperatur erhöht", "Aktiv"],
            ["14:15", "Stanze 1", "Wartung", "Info", "Wartung fällig", "Bestätigt"],
            ["13:45", "Laser 2", "Druck", "Warnung", "Druckabfall", "Aktiv"],
        ]

        for row, alarm in enumerate(alarm_data):
            for col, value in enumerate(alarm):
                item = QTableWidgetItem(value)
                if col == 3:  # Schweregrad
                    if value == "Kritisch":
                        item.setBackground(QColor("lightcoral"))
                    elif value == "Warnung":
                        item.setBackground(QColor("lightyellow"))
                    elif value == "Info":
                        item.setBackground(QColor("lightblue"))
                self.alarm_table.setItem(row, col, item)

        # Doppelklick für Details
        self.alarm_table.itemDoubleClicked.connect(self.show_alarm_details)

        self.alarm_table.resizeColumnsToContents()
        list_layout.addWidget(self.alarm_table)

        # Alarm-Aktionen
        action_layout = QHBoxLayout()

        acknowledge_button = QPushButton("Bestätigen")
        acknowledge_button.clicked.connect(self.acknowledge_alarm)
        action_layout.addWidget(acknowledge_button)

        clear_button = QPushButton("Löschen")
        clear_button.clicked.connect(self.clear_alarm)
        action_layout.addWidget(clear_button)

        list_layout.addLayout(action_layout)
        layout.addWidget(alarm_list_group)

        self.tab_widget.addTab(tab, "Alarme")

    def create_reports_tab(self):
        """Erstellt den Berichte-Tab."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Berichtsgenerierung
        report_group = QGroupBox("Berichte generieren")
        report_layout = QHBoxLayout(report_group)

        # Berichtstyp
        type_layout = QVBoxLayout()
        type_layout.addWidget(QLabel("Berichtstyp:"))

        self.report_type = QComboBox()
        self.report_type.addItems(
            [
                "Tagesproduktion",
                "Wochenübersicht",
                "Qualitätsbericht",
                "Wartungsbericht",
                "Effizienz-Analyse",
            ]
        )
        type_layout.addWidget(self.report_type)

        # Zeitraum
        type_layout.addWidget(QLabel("Zeitraum:"))
        self.report_period = QComboBox()
        self.report_period.addItems(
            ["Heute", "Gestern", "Diese Woche", "Letzte Woche", "Dieser Monat"]
        )
        type_layout.addWidget(self.report_period)

        generate_button = QPushButton("Bericht erstellen")
        generate_button.clicked.connect(self.generate_report)
        type_layout.addWidget(generate_button)

        report_layout.addLayout(type_layout)

        # Bericht-Vorschau
        preview_layout = QVBoxLayout()
        preview_layout.addWidget(QLabel("Vorschau:"))

        self.report_preview = QTextEdit()
        self.report_preview.setReadOnly(True)
        self.report_preview.setText("Hier wird der generierte Bericht angezeigt...")
        preview_layout.addWidget(self.report_preview)

        report_layout.addLayout(preview_layout, 1)

        layout.addWidget(report_group)

        self.tab_widget.addTab(tab, "Berichte")

    def init_database(self):
        """Initialisiert die SQLite-Datenbank."""
        try:
            self.db_connection = sqlite3.connect(":memory:")  # In-Memory DB für Demo
            cursor = self.db_connection.cursor()

            # Tabelle für Maschinendaten
            cursor.execute(
                """
                CREATE TABLE machine_data (
                    id INTEGER PRIMARY KEY,
                    timestamp DATETIME,
                    temperature REAL,
                    pressure REAL,
                    cutting_speed REAL,
                    parts_produced INTEGER,
                    quality_index REAL,
                    power_consumption REAL,
                    status TEXT
                )
            """
            )

            self.db_connection.commit()
            self.status_bar.showMessage("Datenbank initialisiert", 3000)
        except Exception as e:
            QMessageBox.warning(
                self, "Datenbankfehler", f"Fehler beim Initialisieren: {e}"
            )

    def update_machine_data(self, data):
        """Aktualisiert die Anzeige mit neuen Maschinendaten."""
        try:
            # Labels aktualisieren
            self.temp_label.setText(f"Temperatur: {data['temperature']:.1f}°C")
            self.pressure_label.setText(f"Druck: {data['pressure']:.1f} bar")
            self.speed_label.setText(
                f"Schnittgeschwindigkeit: {data['cutting_speed']:.1f} m/min"
            )
            self.power_label.setText(
                f"Leistungsaufnahme: {data['power_consumption']:.1f} kW"
            )

            # Status aktualisieren
            status_colors = {
                "Normal": ("lightgreen", "green"),
                "Warnung": ("lightyellow", "orange"),
                "Fehler": ("lightcoral", "red"),
            }
            bg_color, text_color = status_colors.get(
                data["status"], ("lightgray", "black")
            )

            self.machine_status_label.setText(f"Status: {data['status']}")
            self.machine_status_label.setStyleSheet(
                f"padding: 10px; background-color: {bg_color}; "
                f"border: 2px solid {text_color}; font-weight: bold;"
            )

            # KPIs aktualisieren
            if hasattr(self, "kpi_stückzahl_stunde"):
                self.kpi_stückzahl_stunde.setText(str(data["parts_produced"]))

            if hasattr(self, "kpi_qualitätsindex"):
                self.kpi_qualitätsindex.setText(f"{data['quality_index']:.1f}%")

            # Daten zur Historie hinzufügen
            self.machine_data_history.append(data)

            # Nur die letzten 100 Datenpunkte behalten
            if len(self.machine_data_history) > 100:
                self.machine_data_history.pop(0)

            # Datenbank aktualisieren
            self.save_to_database(data)

            self.data_status.setText(f"Daten: {data['timestamp'].strftime('%H:%M:%S')}")

        except Exception as e:
            print(f"Fehler beim Aktualisieren der Daten: {e}")

    def save_to_database(self, data):
        """Speichert Daten in die Datenbank."""
        try:
            cursor = self.db_connection.cursor()
            cursor.execute(
                """
                INSERT INTO machine_data
                (timestamp, temperature, pressure, cutting_speed, parts_produced,
                 quality_index, power_consumption, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    data["timestamp"],
                    data["temperature"],
                    data["pressure"],
                    data["cutting_speed"],
                    data["parts_produced"],
                    data["quality_index"],
                    data["power_consumption"],
                    data["status"],
                ),
            )
            self.db_connection.commit()
        except Exception as e:
            print(f"Datenbankfehler: {e}")

    def start_machine(self):
        """Startet die Maschine."""
        self.status_bar.showMessage("Maschine wird gestartet...", 3000)
        QMessageBox.information(self, "Maschine", "Maschine erfolgreich gestartet!")

    def stop_machine(self):
        """Stoppt die Maschine."""
        reply = QMessageBox.question(
            self,
            "Maschine stoppen",
            "Möchten Sie die Maschine wirklich stoppen?",
            QMessageBox.Yes | QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.status_bar.showMessage("Maschine wird gestoppt...", 3000)

    def pause_machine(self):
        """Pausiert die Maschine."""
        self.status_bar.showMessage("Maschine pausiert", 3000)

    def schedule_maintenance(self):
        """Öffnet Dialog zur Wartungsplanung."""
        dialog = WartungsDialog(self)
        if dialog.exec() == QDialog.Accepted:
            wartung = dialog.get_wartung_data()
            self.maintenance_schedule.append(wartung)

            # Liste aktualisieren
            item_text = f"{wartung['machine']}: {wartung['type']} - {wartung['planned_date'].strftime('%d.%m.%Y')}"
            self.maintenance_list.addItem(item_text)

            self.status_bar.showMessage("Wartung geplant", 3000)

    def show_alarm_details(self, item):
        """Zeigt Alarm-Details an."""
        row = item.row()
        alarm_data = {
            "type": self.alarm_table.item(row, 2).text(),
            "timestamp": self.alarm_table.item(row, 0).text(),
            "machine": self.alarm_table.item(row, 1).text(),
            "severity": self.alarm_table.item(row, 3).text(),
            "description": self.alarm_table.item(row, 4).text(),
        }

        dialog = AlarmDialog(alarm_data, self)
        dialog.exec()

    def acknowledge_alarm(self):
        """Bestätigt ausgewählten Alarm."""
        current_row = self.alarm_table.currentRow()
        if current_row >= 0:
            self.alarm_table.setItem(current_row, 5, QTableWidgetItem("Bestätigt"))
            self.status_bar.showMessage("Alarm bestätigt", 3000)

    def clear_alarm(self):
        """Löscht ausgewählten Alarm."""
        current_row = self.alarm_table.currentRow()
        if current_row >= 0:
            self.alarm_table.removeRow(current_row)
            self.status_bar.showMessage("Alarm gelöscht", 3000)

    def generate_report(self):
        """Generiert einen Bericht."""
        report_type = self.report_type.currentText()
        period = self.report_period.currentText()

        # Beispiel-Bericht
        report = f"""
BYSTRONIC PRODUKTIONSBERICHT
============================

Berichtstyp: {report_type}
Zeitraum: {period}
Erstellt am: {datetime.now().strftime("%d.%m.%Y %H:%M")}

ZUSAMMENFASSUNG:
- Gesamtproduktion: 1.450 Teile
- Durchschnittliche Rate: 245 Teile/Stunde
- Qualitätsindex: 98.5%
- Maschinenauslastung: 87%
- Ungeplante Stillstände: 2 (Total: 45 Minuten)

MASCHINENDETAILS:
Laser 1:
- Betriebszeit: 7h 30min
- Produzierte Teile: 650
- Durchschnittstemperatur: 65.2°C

Laser 2:
- Betriebszeit: 6h 45min
- Produzierte Teile: 580
- Durchschnittstemperatur: 63.8°C

WARTUNGSHINWEISE:
- Laser 1: Routinewartung fällig am 05.09.2024
- Stanze 1: Kalibrierung erforderlich

EMPFEHLUNGEN:
- Überprüfung der Kühlsysteme
- Wartungsintervalle einhalten
- Qualitätskontrolle verstärken bei Charge #2024-234
        """

        self.report_preview.setText(report.strip())
        self.status_bar.showMessage(f"Bericht '{report_type}' generiert", 3000)

    def export_data(self):
        """Exportiert Maschinendaten."""
        if self.machine_data_history:
            filename = f"maschinendaten_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            try:
                # Daten für JSON serialisierbar machen
                export_data = []
                for data in self.machine_data_history[-50:]:  # Letzte 50 Datenpunkte
                    export_entry = data.copy()
                    export_entry["timestamp"] = data["timestamp"].isoformat()
                    export_data.append(export_entry)

                # Simulierter Export (in echte Anwendung würde hier gespeichert)
                QMessageBox.information(
                    self,
                    "Export",
                    f"Daten würden in {filename} exportiert werden.\n"
                    f"Anzahl Datensätze: {len(export_data)}",
                )

            except Exception as e:
                QMessageBox.warning(self, "Export-Fehler", f"Fehler beim Export: {e}")
        else:
            QMessageBox.information(
                self, "Export", "Keine Daten zum Exportieren vorhanden."
            )

    def closeEvent(self, event):
        """Wird beim Schließen der Anwendung aufgerufen."""
        # Worker-Thread stoppen
        if hasattr(self, "data_worker") and self.data_worker.isRunning():
            self.data_worker.stop()
            self.data_worker.wait(5000)  # Max 5 Sekunden warten

        # Datenbankverbindung schließen
        if hasattr(self, "db_connection"):
            self.db_connection.close()

        event.accept()


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Anwendungsmetadaten
    app.setApplicationName("Bystronic Maschinendaten-GUI")
    app.setApplicationVersion("1.0")
    app.setOrganizationName("Bystronic")

    # Hauptfenster erstellen und anzeigen
    window = MaschinendatenGUI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
