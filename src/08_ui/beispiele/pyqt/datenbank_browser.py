#!/usr/bin/env python3
"""
Datenbank-Browser für Maschinendaten
====================================

Dieses Beispiel zeigt eine vollständige CRUD-Anwendung mit PyQt:
- SQLite-Datenbank-Integration
- Daten anzeigen, erstellen, bearbeiten, löschen
- Suchen und Filtern
- Datenvalidierung
- Export-Funktionen

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import sqlite3
import sys
from datetime import datetime, timedelta

import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QDateTimeEdit,
    QDialog,
    QDialogButtonBox,
    QDoubleSpinBox,
    QFileDialog,
    QFormLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
    QWidget,
)


class DatabaseManager:
    """Manager für Datenbankoperationen."""

    def __init__(self, db_path=':memory:'):
        self.db_path = db_path
        self.init_database()

    def init_database(self):
        """Initialisiert die Datenbank mit Beispieltabellen."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Maschinen-Tabelle
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS machines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    type TEXT NOT NULL,
                    location TEXT,
                    install_date DATE,
                    status TEXT DEFAULT 'Active'
                )
            ''')

            # Produktionsdaten-Tabelle
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS production_data (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    machine_id INTEGER,
                    timestamp DATETIME,
                    temperature REAL,
                    pressure REAL,
                    cutting_speed REAL,
                    parts_produced INTEGER,
                    quality_index REAL,
                    operator TEXT,
                    FOREIGN KEY (machine_id) REFERENCES machines (id)
                )
            ''')

            # Wartungsdaten-Tabelle
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS maintenance (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    machine_id INTEGER,
                    maintenance_date DATETIME,
                    type TEXT,
                    description TEXT,
                    cost REAL,
                    technician TEXT,
                    duration_hours INTEGER,
                    FOREIGN KEY (machine_id) REFERENCES machines (id)
                )
            ''')

            # Qualitätsdaten-Tabelle
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS quality_control (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    production_id INTEGER,
                    check_time DATETIME,
                    dimension_x REAL,
                    dimension_y REAL,
                    surface_quality TEXT,
                    pass_fail TEXT,
                    inspector TEXT,
                    FOREIGN KEY (production_id) REFERENCES production_data (id)
                )
            ''')

            conn.commit()

            # Beispieldaten einfügen, falls Tabellen leer sind
            self.insert_sample_data(conn)

            conn.close()

        except sqlite3.Error as e:
            print(f"Datenbankfehler: {e}")

    def insert_sample_data(self, conn):
        """Fügt Beispieldaten ein."""
        cursor = conn.cursor()

        # Prüfen ob Daten bereits existieren
        cursor.execute("SELECT COUNT(*) FROM machines")
        if cursor.fetchone()[0] > 0:
            return

        # Beispiel-Maschinen
        machines_data = [
            ('Laser 1', 'Laser Cutter', 'Halle A', '2022-01-15', 'Active'),
            ('Laser 2', 'Laser Cutter', 'Halle A', '2022-03-20', 'Active'),
            ('Stanze 1', 'Punching Machine', 'Halle B', '2021-11-10', 'Active'),
            ('Biegemaschine', 'Bending Machine', 'Halle C', '2023-02-05', 'Maintenance')
        ]

        cursor.executemany('''
            INSERT INTO machines (name, type, location, install_date, status)
            VALUES (?, ?, ?, ?, ?)
        ''', machines_data)

        # Beispiel-Produktionsdaten
        import numpy as np
        np.random.seed(42)

        production_data = []
        for _i in range(100):
            machine_id = np.random.randint(1, 5)
            timestamp = datetime.now() - timedelta(hours=np.random.randint(1, 168))
            temp = np.random.normal(65, 5)
            pressure = np.random.normal(8.2, 0.8)
            speed = np.random.normal(2.5, 0.3)
            parts = np.random.randint(200, 300)
            quality = np.random.uniform(95, 99.5)
            operators = ['Schmidt', 'Müller', 'Weber', 'Meyer', 'Wagner']
            operator = np.random.choice(operators)

            production_data.append((
                machine_id, timestamp, temp, pressure, speed, parts, quality, operator
            ))

        cursor.executemany('''
            INSERT INTO production_data
            (machine_id, timestamp, temperature, pressure, cutting_speed,
             parts_produced, quality_index, operator)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', production_data)

        # Beispiel-Wartungsdaten
        maintenance_data = [
            (1, '2024-09-01 10:00', 'Routine', 'Routinewartung und Reinigung', 250.0, 'Tech1', 2),
            (2, '2024-08-28 14:00', 'Repair', 'Optik-Justierung', 450.0, 'Tech2', 4),
            (3, '2024-08-25 09:00', 'Calibration', 'Präzisionskalibrierung', 180.0, 'Tech1', 1),
            (4, '2024-09-03 08:00', 'Upgrade', 'Software-Update', 120.0, 'Tech3', 3)
        ]

        cursor.executemany('''
            INSERT INTO maintenance
            (machine_id, maintenance_date, type, description, cost, technician, duration_hours)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', maintenance_data)

        conn.commit()

    def execute_query(self, query, params=None):
        """Führt eine SQL-Abfrage aus."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                columns = [description[0] for description in cursor.description]
                conn.close()
                return results, columns
            else:
                conn.commit()
                conn.close()
                return cursor.rowcount, []

        except sqlite3.Error as e:
            print(f"Datenbankfehler: {e}")
            return None, []


class EditRecordDialog(QDialog):
    """Dialog zum Bearbeiten von Datensätzen."""

    def __init__(self, table_name, record_data=None, columns=None, parent=None):
        super().__init__(parent)
        self.table_name = table_name
        self.record_data = record_data or {}
        self.columns = columns or []
        self.input_widgets = {}

        self.setWindowTitle(f"Datensatz {'bearbeiten' if record_data else 'erstellen'} - {table_name}")
        self.setModal(True)
        self.resize(500, 400)

        self.setup_ui()

    def setup_ui(self):
        """Erstellt die Dialog-UI."""
        layout = QVBoxLayout(self)

        # Formular
        form_widget = QWidget()
        form_layout = QFormLayout(form_widget)

        # Eingabefelder basierend auf Tabelle erstellen
        self.create_input_fields(form_layout)

        layout.addWidget(form_widget)

        # Buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)

    def create_input_fields(self, layout):
        """Erstellt Eingabefelder basierend auf der Tabelle."""
        if self.table_name == 'machines':
            self.create_machine_fields(layout)
        elif self.table_name == 'production_data':
            self.create_production_fields(layout)
        elif self.table_name == 'maintenance':
            self.create_maintenance_fields(layout)
        elif self.table_name == 'quality_control':
            self.create_quality_fields(layout)

    def create_machine_fields(self, layout):
        """Erstellt Felder für Maschinen-Tabelle."""
        # Name
        self.input_widgets['name'] = QLineEdit()
        self.input_widgets['name'].setText(str(self.record_data.get('name', '')))
        layout.addRow("Name:", self.input_widgets['name'])

        # Typ
        self.input_widgets['type'] = QComboBox()
        self.input_widgets['type'].addItems([
            'Laser Cutter', 'Punching Machine', 'Bending Machine',
            'Welding Machine', 'Other'
        ])
        current_type = self.record_data.get('type', '')
        if current_type:
            index = self.input_widgets['type'].findText(current_type)
            if index >= 0:
                self.input_widgets['type'].setCurrentIndex(index)
        layout.addRow("Typ:", self.input_widgets['type'])

        # Standort
        self.input_widgets['location'] = QLineEdit()
        self.input_widgets['location'].setText(str(self.record_data.get('location', '')))
        layout.addRow("Standort:", self.input_widgets['location'])

        # Installationsdatum
        self.input_widgets['install_date'] = QDateTimeEdit()
        self.input_widgets['install_date'].setCalendarPopup(True)
        if self.record_data.get('install_date'):
            try:
                date = datetime.fromisoformat(str(self.record_data['install_date']))
                self.input_widgets['install_date'].setDateTime(date)
            except:
                self.input_widgets['install_date'].setDateTime(datetime.now())
        else:
            self.input_widgets['install_date'].setDateTime(datetime.now())
        layout.addRow("Installationsdatum:", self.input_widgets['install_date'])

        # Status
        self.input_widgets['status'] = QComboBox()
        self.input_widgets['status'].addItems(['Active', 'Maintenance', 'Inactive'])
        current_status = self.record_data.get('status', 'Active')
        index = self.input_widgets['status'].findText(current_status)
        if index >= 0:
            self.input_widgets['status'].setCurrentIndex(index)
        layout.addRow("Status:", self.input_widgets['status'])

    def create_production_fields(self, layout):
        """Erstellt Felder für Produktionsdaten."""
        # Maschinen-ID (vereinfacht)
        self.input_widgets['machine_id'] = QSpinBox()
        self.input_widgets['machine_id'].setRange(1, 10)
        self.input_widgets['machine_id'].setValue(int(self.record_data.get('machine_id', 1)))
        layout.addRow("Maschinen-ID:", self.input_widgets['machine_id'])

        # Zeitstempel
        self.input_widgets['timestamp'] = QDateTimeEdit()
        self.input_widgets['timestamp'].setCalendarPopup(True)
        if self.record_data.get('timestamp'):
            try:
                timestamp = datetime.fromisoformat(str(self.record_data['timestamp']))
                self.input_widgets['timestamp'].setDateTime(timestamp)
            except:
                self.input_widgets['timestamp'].setDateTime(datetime.now())
        else:
            self.input_widgets['timestamp'].setDateTime(datetime.now())
        layout.addRow("Zeitstempel:", self.input_widgets['timestamp'])

        # Temperatur
        self.input_widgets['temperature'] = QDoubleSpinBox()
        self.input_widgets['temperature'].setRange(0, 150)
        self.input_widgets['temperature'].setValue(float(self.record_data.get('temperature', 65.0)))
        self.input_widgets['temperature'].setSuffix(" °C")
        layout.addRow("Temperatur:", self.input_widgets['temperature'])

        # Druck
        self.input_widgets['pressure'] = QDoubleSpinBox()
        self.input_widgets['pressure'].setRange(0, 20)
        self.input_widgets['pressure'].setValue(float(self.record_data.get('pressure', 8.2)))
        self.input_widgets['pressure'].setSuffix(" bar")
        layout.addRow("Druck:", self.input_widgets['pressure'])

        # Schnittgeschwindigkeit
        self.input_widgets['cutting_speed'] = QDoubleSpinBox()
        self.input_widgets['cutting_speed'].setRange(0, 10)
        self.input_widgets['cutting_speed'].setValue(float(self.record_data.get('cutting_speed', 2.5)))
        self.input_widgets['cutting_speed'].setSuffix(" m/min")
        layout.addRow("Geschwindigkeit:", self.input_widgets['cutting_speed'])

        # Teile produziert
        self.input_widgets['parts_produced'] = QSpinBox()
        self.input_widgets['parts_produced'].setRange(0, 1000)
        self.input_widgets['parts_produced'].setValue(int(self.record_data.get('parts_produced', 250)))
        layout.addRow("Teile produziert:", self.input_widgets['parts_produced'])

        # Qualitätsindex
        self.input_widgets['quality_index'] = QDoubleSpinBox()
        self.input_widgets['quality_index'].setRange(0, 100)
        self.input_widgets['quality_index'].setValue(float(self.record_data.get('quality_index', 98.0)))
        self.input_widgets['quality_index'].setSuffix(" %")
        layout.addRow("Qualitätsindex:", self.input_widgets['quality_index'])

        # Operator
        self.input_widgets['operator'] = QLineEdit()
        self.input_widgets['operator'].setText(str(self.record_data.get('operator', '')))
        layout.addRow("Operator:", self.input_widgets['operator'])

    def create_maintenance_fields(self, layout):
        """Erstellt Felder für Wartungsdaten."""
        # Ähnliche Implementierung wie bei production_fields
        # Hier vereinfacht dargestellt
        pass

    def create_quality_fields(self, layout):
        """Erstellt Felder für Qualitätsdaten."""
        # Ähnliche Implementierung
        pass

    def get_data(self):
        """Gibt die eingegebenen Daten zurück."""
        data = {}
        for field, widget in self.input_widgets.items():
            if isinstance(widget, QLineEdit):
                data[field] = widget.text()
            elif isinstance(widget, QComboBox):
                data[field] = widget.currentText()
            elif isinstance(widget, QSpinBox | QDoubleSpinBox):
                data[field] = widget.value()
            elif isinstance(widget, QDateTimeEdit):
                data[field] = widget.dateTime().toPython().isoformat()

        return data


class DatenbankBrowser(QMainWindow):
    """Hauptanwendung für den Datenbank-Browser."""

    def __init__(self, db_path=None):
        super().__init__()
        self.setWindowTitle("Bystronic Datenbank-Browser")
        self.setGeometry(100, 100, 1200, 800)

        # Datenbankmanager
        self.db_path = db_path or ':memory:'
        self.db_manager = DatabaseManager(self.db_path)

        # Aktuelle Tabelle und Daten
        self.current_table = 'machines'
        self.current_data = []
        self.current_columns = []

        self.setup_ui()
        self.load_table_data()

    def setup_ui(self):
        """Erstellt die Benutzeroberfläche."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Hauptlayout
        main_layout = QHBoxLayout(central_widget)

        # Linke Seite - Tabellen-Navigation
        self.create_navigation_panel(main_layout)

        # Rechte Seite - Daten-Ansicht
        self.create_data_panel(main_layout)

        # Statusbar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Bereit")

    def create_navigation_panel(self, parent_layout):
        """Erstellt das Navigation-Panel."""
        nav_widget = QWidget()
        nav_layout = QVBoxLayout(nav_widget)

        # Tabellen-Liste
        tables_group = QGroupBox("Tabellen")
        tables_layout = QVBoxLayout(tables_group)

        self.table_tree = QTreeWidget()
        self.table_tree.setHeaderLabel("Datenbank-Struktur")

        # Tabellen-Knoten erstellen
        self.setup_table_tree()

        self.table_tree.itemClicked.connect(self.on_table_selected)
        tables_layout.addWidget(self.table_tree)

        nav_layout.addWidget(tables_group)

        # Aktionen
        actions_group = QGroupBox("Aktionen")
        actions_layout = QVBoxLayout(actions_group)

        # CRUD-Buttons
        self.add_button = QPushButton("Neuen Datensatz hinzufügen")
        self.add_button.clicked.connect(self.add_record)
        actions_layout.addWidget(self.add_button)

        self.edit_button = QPushButton("Datensatz bearbeiten")
        self.edit_button.clicked.connect(self.edit_record)
        actions_layout.addWidget(self.edit_button)

        self.delete_button = QPushButton("Datensatz löschen")
        self.delete_button.clicked.connect(self.delete_record)
        actions_layout.addWidget(self.delete_button)

        actions_layout.addWidget(QLabel())  # Spacer

        # Weitere Aktionen
        self.refresh_button = QPushButton("Aktualisieren")
        self.refresh_button.clicked.connect(self.refresh_data)
        actions_layout.addWidget(self.refresh_button)

        self.export_button = QPushButton("Daten exportieren")
        self.export_button.clicked.connect(self.export_data)
        actions_layout.addWidget(self.export_button)

        self.import_button = QPushButton("Daten importieren")
        self.import_button.clicked.connect(self.import_data)
        actions_layout.addWidget(self.import_button)

        nav_layout.addWidget(actions_group)
        nav_layout.addStretch()

        parent_layout.addWidget(nav_widget, 1)

    def create_data_panel(self, parent_layout):
        """Erstellt das Daten-Panel."""
        data_widget = QWidget()
        data_layout = QVBoxLayout(data_widget)

        # Such- und Filter-Bereich
        search_group = QGroupBox("Suchen und Filtern")
        search_layout = QHBoxLayout(search_group)

        search_layout.addWidget(QLabel("Suchen:"))
        self.search_edit = QLineEdit()
        self.search_edit.setPlaceholderText("Suchbegriff eingeben...")
        self.search_edit.textChanged.connect(self.filter_data)
        search_layout.addWidget(self.search_edit)

        search_layout.addWidget(QLabel("Spalte:"))
        self.column_filter = QComboBox()
        self.column_filter.addItem("Alle Spalten")
        search_layout.addWidget(self.column_filter)

        search_button = QPushButton("Suchen")
        search_button.clicked.connect(self.search_data)
        search_layout.addWidget(search_button)

        clear_button = QPushButton("Zurücksetzen")
        clear_button.clicked.connect(self.clear_search)
        search_layout.addWidget(clear_button)

        data_layout.addWidget(search_group)

        # Daten-Tabelle
        self.data_table = QTableWidget()
        self.data_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.data_table.setAlternatingRowColors(True)
        self.data_table.horizontalHeader().setStretchLastSection(True)
        self.data_table.itemDoubleClicked.connect(self.edit_record)

        data_layout.addWidget(self.data_table)

        # Info-Bereich
        info_layout = QHBoxLayout()

        self.record_count_label = QLabel("Datensätze: 0")
        info_layout.addWidget(self.record_count_label)

        info_layout.addStretch()

        self.table_info_label = QLabel("Tabelle: machines")
        info_layout.addWidget(self.table_info_label)

        data_layout.addLayout(info_layout)

        parent_layout.addWidget(data_widget, 3)

    def setup_table_tree(self):
        """Erstellt den Tabellen-Baum."""
        # Hauptknoten für Tabellen
        tables_root = QTreeWidgetItem(["Tabellen"])
        self.table_tree.addTopLevelItem(tables_root)

        # Einzelne Tabellen
        tables = [
            ("machines", "Maschinen"),
            ("production_data", "Produktionsdaten"),
            ("maintenance", "Wartung"),
            ("quality_control", "Qualitätskontrolle")
        ]

        for table_name, display_name in tables:
            table_item = QTreeWidgetItem([display_name])
            table_item.setData(0, Qt.UserRole, table_name)
            tables_root.addChild(table_item)

        # Baum expandieren
        self.table_tree.expandAll()

        # Erste Tabelle auswählen
        first_table = tables_root.child(0)
        self.table_tree.setCurrentItem(first_table)

    def on_table_selected(self, item):
        """Wird aufgerufen, wenn eine Tabelle ausgewählt wird."""
        table_name = item.data(0, Qt.UserRole)
        if table_name:
            self.current_table = table_name
            self.table_info_label.setText(f"Tabelle: {table_name}")
            self.load_table_data()

    def load_table_data(self):
        """Lädt die Daten der aktuellen Tabelle."""
        if not self.current_table:
            return

        query = f"SELECT * FROM {self.current_table}"
        data, columns = self.db_manager.execute_query(query)

        if data is not None:
            self.current_data = data
            self.current_columns = columns
            self.update_table_display()
            self.update_column_filter()

            self.status_bar.showMessage(f"Tabelle {self.current_table} geladen: {len(data)} Datensätze")
        else:
            QMessageBox.warning(self, "Fehler", "Fehler beim Laden der Tabellendaten")

    def update_table_display(self):
        """Aktualisiert die Tabellenanzeige."""
        if not self.current_data or not self.current_columns:
            self.data_table.setRowCount(0)
            self.data_table.setColumnCount(0)
            self.record_count_label.setText("Datensätze: 0")
            return

        # Tabelle konfigurieren
        self.data_table.setRowCount(len(self.current_data))
        self.data_table.setColumnCount(len(self.current_columns))
        self.data_table.setHorizontalHeaderLabels(self.current_columns)

        # Daten einfügen
        for row, record in enumerate(self.current_data):
            for col, value in enumerate(record):
                item = QTableWidgetItem(str(value) if value is not None else "")
                self.data_table.setItem(row, col, item)

        # Spaltenbreite anpassen
        self.data_table.resizeColumnsToContents()

        # Info aktualisieren
        self.record_count_label.setText(f"Datensätze: {len(self.current_data)}")

    def update_column_filter(self):
        """Aktualisiert die Spalten-Filter Dropdown."""
        self.column_filter.clear()
        self.column_filter.addItem("Alle Spalten")
        self.column_filter.addItems(self.current_columns)

    def filter_data(self):
        """Filtert die Daten basierend auf dem Suchtext."""
        search_text = self.search_edit.text().lower()

        if not search_text:
            # Alle Zeilen anzeigen
            for row in range(self.data_table.rowCount()):
                self.data_table.setRowHidden(row, False)
            return

        # Zeilen filtern
        for row in range(self.data_table.rowCount()):
            match_found = False

            # In allen Spalten suchen
            for col in range(self.data_table.columnCount()):
                item = self.data_table.item(row, col)
                if item and search_text in item.text().lower():
                    match_found = True
                    break

            self.data_table.setRowHidden(row, not match_found)

    def search_data(self):
        """Führt eine erweiterte Suche durch."""
        search_text = self.search_edit.text()
        if not search_text:
            return

        column_name = self.column_filter.currentText()

        if column_name == "Alle Spalten":
            # In allen Spalten suchen
            where_clause = " OR ".join([f"{col} LIKE ?" for col in self.current_columns])
            params = [f"%{search_text}%"] * len(self.current_columns)
        else:
            # In spezifischer Spalte suchen
            where_clause = f"{column_name} LIKE ?"
            params = [f"%{search_text}%"]

        query = f"SELECT * FROM {self.current_table} WHERE {where_clause}"
        data, columns = self.db_manager.execute_query(query, params)

        if data is not None:
            self.current_data = data
            self.update_table_display()
            self.status_bar.showMessage(f"Suche abgeschlossen: {len(data)} Treffer")

    def clear_search(self):
        """Setzt die Suche zurück."""
        self.search_edit.clear()
        self.column_filter.setCurrentIndex(0)
        self.load_table_data()

    def add_record(self):
        """Fügt einen neuen Datensatz hinzu."""
        dialog = EditRecordDialog(self.current_table, parent=self)

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            # SQL INSERT erstellen
            columns = list(data.keys())
            placeholders = ", ".join(["?"] * len(columns))
            query = f"INSERT INTO {self.current_table} ({', '.join(columns)}) VALUES ({placeholders})"

            rowcount, _ = self.db_manager.execute_query(query, list(data.values()))

            if rowcount and rowcount > 0:
                self.load_table_data()
                self.status_bar.showMessage("Datensatz hinzugefügt", 3000)
            else:
                QMessageBox.warning(self, "Fehler", "Fehler beim Hinzufügen des Datensatzes")

    def edit_record(self):
        """Bearbeitet den ausgewählten Datensatz."""
        current_row = self.data_table.currentRow()
        if current_row < 0:
            QMessageBox.information(self, "Info", "Bitte wählen Sie einen Datensatz aus.")
            return

        # Aktuelle Daten des Datensatzes abrufen
        record_data = {}
        for col in range(len(self.current_columns)):
            column_name = self.current_columns[col]
            item = self.data_table.item(current_row, col)
            record_data[column_name] = item.text() if item else ""

        dialog = EditRecordDialog(self.current_table, record_data, self.current_columns, self)

        if dialog.exec() == QDialog.Accepted:
            data = dialog.get_data()

            # SQL UPDATE erstellen
            set_clause = ", ".join([f"{col} = ?" for col in data.keys() if col != 'id'])
            values = [value for col, value in data.items() if col != 'id']
            record_id = record_data.get('id')

            if record_id:
                query = f"UPDATE {self.current_table} SET {set_clause} WHERE id = ?"
                values.append(record_id)

                rowcount, _ = self.db_manager.execute_query(query, values)

                if rowcount and rowcount > 0:
                    self.load_table_data()
                    self.status_bar.showMessage("Datensatz aktualisiert", 3000)
                else:
                    QMessageBox.warning(self, "Fehler", "Fehler beim Aktualisieren des Datensatzes")

    def delete_record(self):
        """Löscht den ausgewählten Datensatz."""
        current_row = self.data_table.currentRow()
        if current_row < 0:
            QMessageBox.information(self, "Info", "Bitte wählen Sie einen Datensatz aus.")
            return

        # Bestätigung
        reply = QMessageBox.question(
            self, "Datensatz löschen",
            "Möchten Sie den ausgewählten Datensatz wirklich löschen?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply != QMessageBox.Yes:
            return

        # ID des Datensatzes ermitteln
        id_item = self.data_table.item(current_row, 0)  # Annahme: ID ist in der ersten Spalte
        if not id_item:
            QMessageBox.warning(self, "Fehler", "Datensatz-ID nicht gefunden")
            return

        record_id = id_item.text()
        query = f"DELETE FROM {self.current_table} WHERE id = ?"

        rowcount, _ = self.db_manager.execute_query(query, [record_id])

        if rowcount and rowcount > 0:
            self.load_table_data()
            self.status_bar.showMessage("Datensatz gelöscht", 3000)
        else:
            QMessageBox.warning(self, "Fehler", "Fehler beim Löschen des Datensatzes")

    def refresh_data(self):
        """Aktualisiert die Daten."""
        self.load_table_data()
        self.status_bar.showMessage("Daten aktualisiert", 2000)

    def export_data(self):
        """Exportiert die aktuellen Daten."""
        if not self.current_data:
            QMessageBox.information(self, "Info", "Keine Daten zum Exportieren vorhanden.")
            return

        filename, _ = QFileDialog.getSaveFileName(
            self, "Daten exportieren", f"{self.current_table}_export.csv",
            "CSV Files (*.csv);;JSON Files (*.json);;Excel Files (*.xlsx)"
        )

        if filename:
            try:
                # DataFrame erstellen
                df = pd.DataFrame(self.current_data, columns=self.current_columns)

                # Export basierend auf Dateierweiterung
                if filename.endswith('.csv'):
                    df.to_csv(filename, index=False)
                elif filename.endswith('.json'):
                    df.to_json(filename, orient='records', indent=2)
                elif filename.endswith('.xlsx'):
                    df.to_excel(filename, index=False)

                QMessageBox.information(self, "Export", f"Daten erfolgreich exportiert nach: {filename}")
                self.status_bar.showMessage("Export abgeschlossen", 3000)

            except Exception as e:
                QMessageBox.warning(self, "Export-Fehler", f"Fehler beim Exportieren: {e}")

    def import_data(self):
        """Importiert Daten aus einer Datei."""
        filename, _ = QFileDialog.getOpenFileName(
            self, "Daten importieren", "",
            "CSV Files (*.csv);;JSON Files (*.json);;Excel Files (*.xlsx)"
        )

        if filename:
            try:
                # DataFrame basierend auf Dateierweiterung laden
                if filename.endswith('.csv'):
                    df = pd.read_csv(filename)
                elif filename.endswith('.json'):
                    df = pd.read_json(filename)
                elif filename.endswith('.xlsx'):
                    df = pd.read_excel(filename)
                else:
                    QMessageBox.warning(self, "Fehler", "Nicht unterstütztes Dateiformat")
                    return

                # Import-Dialog zeigen
                reply = QMessageBox.question(
                    self, "Daten importieren",
                    f"Möchten Sie {len(df)} Datensätze in die Tabelle {self.current_table} importieren?",
                    QMessageBox.Yes | QMessageBox.No
                )

                if reply == QMessageBox.Yes:
                    # Hier würde der tatsächliche Import stattfinden
                    QMessageBox.information(self, "Import",
                        f"Import-Simulation:\n{len(df)} Datensätze würden importiert werden.\n"
                        f"Spalten: {', '.join(df.columns.tolist())}")

            except Exception as e:
                QMessageBox.warning(self, "Import-Fehler", f"Fehler beim Importieren: {e}")


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # Hauptfenster erstellen
    window = DatenbankBrowser()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
