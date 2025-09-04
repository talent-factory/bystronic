#!/usr/bin/env python3
"""
Übung 2: Maschinendaten-Interface
================================

Lernziele:
- Tabellen-Widgets verwenden
- Daten dynamisch anzeigen
- Timer für Echtzeit-Updates
- Status-Anzeigen implementieren
- Datenvalidierung

Schwierigkeitsgrad: ⭐⭐⭐☆☆ (Fortgeschrittene)

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


class MaschinendatenInterface(QMainWindow):
    """Interface für Maschinendaten-Überwachung."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Übung 2: Maschinendaten-Interface")
        self.setGeometry(100, 100, 1000, 700)

        # TODO: Aufgabe 1 - Initialisieren Sie die Maschinendaten-Liste
        # self.machine_data = []

        # TODO: Aufgabe 2 - Erstellen Sie einen QTimer für Updates
        # self.update_timer = QTimer()
        # self.update_timer.timeout.connect(self.update_machine_data)

        self.setup_ui()

        # TODO: Aufgabe 3 - Starten Sie den Timer (alle 2 Sekunden)
        # self.update_timer.start(2000)

    def setup_ui(self):
        """Erstellt die Benutzeroberfläche."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Titel
        title = QLabel("🏭 Bystronic Maschinendaten-Monitor")
        title.setStyleSheet(
            "font-size: 20px; font-weight: bold; color: #1f4e79; margin: 10px;"
        )
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # TODO: Aufgabe 4 - Erstellen Sie das Steuerungs-Panel
        self.create_control_panel(main_layout)

        # TODO: Aufgabe 5 - Erstellen Sie die Maschinendaten-Tabelle
        self.create_data_table(main_layout)

        # TODO: Aufgabe 6 - Erstellen Sie das Status-Panel
        self.create_status_panel(main_layout)

    def create_control_panel(self, parent_layout):
        """Erstellt das Steuerungs-Panel."""
        control_group = QGroupBox("Steuerung")
        QHBoxLayout(control_group)

        # TODO: Aufgabe 4a - Maschine hinzufügen
        # add_machine_layout = QVBoxLayout()
        # add_machine_layout.addWidget(QLabel("Neue Maschine:"))
        #
        # self.machine_name_combo = QComboBox()
        # self.machine_name_combo.addItems(["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine", "Schweißroboter"])
        # add_machine_layout.addWidget(self.machine_name_combo)
        #
        # self.add_machine_button = QPushButton("Maschine hinzufügen")
        # self.add_machine_button.clicked.connect(self.add_machine)
        # add_machine_layout.addWidget(self.add_machine_button)
        #
        # control_layout.addLayout(add_machine_layout)

        # TODO: Aufgabe 4b - Simulation starten/stoppen
        # simulation_layout = QVBoxLayout()
        # simulation_layout.addWidget(QLabel("Simulation:"))
        #
        # self.start_button = QPushButton("▶️ Start")
        # self.stop_button = QPushButton("⏹️ Stopp")
        # self.start_button.clicked.connect(self.start_simulation)
        # self.stop_button.clicked.connect(self.stop_simulation)
        #
        # sim_button_layout = QHBoxLayout()
        # sim_button_layout.addWidget(self.start_button)
        # sim_button_layout.addWidget(self.stop_button)
        # simulation_layout.addLayout(sim_button_layout)
        #
        # control_layout.addLayout(simulation_layout)

        # TODO: Aufgabe 4c - Daten löschen
        # clear_layout = QVBoxLayout()
        # clear_layout.addWidget(QLabel("Aktionen:"))
        #
        # self.clear_button = QPushButton("🗑️ Alle Daten löschen")
        # self.clear_button.clicked.connect(self.clear_all_data)
        # clear_layout.addWidget(self.clear_button)
        #
        # control_layout.addLayout(clear_layout)

        parent_layout.addWidget(control_group)

    def create_data_table(self, parent_layout):
        """Erstellt die Maschinendaten-Tabelle."""
        table_group = QGroupBox("Maschinendaten")
        QVBoxLayout(table_group)

        # TODO: Aufgabe 5a - Erstellen Sie die Tabelle
        # self.data_table = QTableWidget()
        # self.data_table.setColumnCount(7)
        # self.data_table.setHorizontalHeaderLabels([
        #     "Maschine", "Temperatur [°C]", "Druck [bar]",
        #     "Leistung [%]", "Stückzahl/h", "Status", "Letztes Update"
        # ])

        # TODO: Aufgabe 5b - Tabellen-Konfiguration
        # header = self.data_table.horizontalHeader()
        # header.setStretchLastSection(True)
        # self.data_table.setAlternatingRowColors(True)
        # self.data_table.setSelectionBehavior(QTableWidget.SelectRows)

        # table_layout.addWidget(self.data_table)

        parent_layout.addWidget(table_group)

    def create_status_panel(self, parent_layout):
        """Erstellt das Status-Panel."""
        status_group = QGroupBox("System-Status")
        QGridLayout(status_group)

        # TODO: Aufgabe 6a - Erstellen Sie Status-Labels
        # self.total_machines_label = QLabel("Maschinen: 0")
        # self.running_machines_label = QLabel("Läuft: 0")
        # self.avg_temperature_label = QLabel("Ø Temperatur: 0°C")
        # self.total_production_label = QLabel("Gesamt/h: 0")

        # TODO: Aufgabe 6b - Fügen Sie Labels zum Grid hinzu
        # status_layout.addWidget(QLabel("📊"), 0, 0)
        # status_layout.addWidget(self.total_machines_label, 0, 1)
        # status_layout.addWidget(QLabel("▶️"), 0, 2)
        # status_layout.addWidget(self.running_machines_label, 0, 3)
        # status_layout.addWidget(QLabel("🌡️"), 1, 0)
        # status_layout.addWidget(self.avg_temperature_label, 1, 1)
        # status_layout.addWidget(QLabel("📦"), 1, 2)
        # status_layout.addWidget(self.total_production_label, 1, 3)

        # TODO: Aufgabe 6c - Erstellen Sie eine Fortschrittsanzeige
        # status_layout.addWidget(QLabel("Gesamteffizienz:"), 2, 0)
        # self.efficiency_progress = QProgressBar()
        # self.efficiency_progress.setRange(0, 100)
        # status_layout.addWidget(self.efficiency_progress, 2, 1, 1, 3)

        parent_layout.addWidget(status_group)

    # TODO: Aufgabe 7 - Implementieren Sie die Event-Handler
    def add_machine(self):
        """Fügt eine neue Maschine hinzu."""
        # machine_name = self.machine_name_combo.currentText()
        #
        # # Prüfen ob Maschine bereits existiert
        # for machine in self.machine_data:
        #     if machine['name'] == machine_name:
        #         QMessageBox.warning(self, "Warnung", f"Maschine '{machine_name}' existiert bereits!")
        #         return
        #
        # # Neue Maschine hinzufügen
        # new_machine = {
        #     'name': machine_name,
        #     'temperature': 65.0,
        #     'pressure': 8.2,
        #     'power': 75.0,
        #     'production': 250,
        #     'status': 'Bereit',
        #     'last_update': datetime.now().strftime('%H:%M:%S')
        # }
        #
        # self.machine_data.append(new_machine)
        # self.update_table_display()
        #
        # QMessageBox.information(self, "Erfolg", f"Maschine '{machine_name}' hinzugefügt!")
        pass

    def start_simulation(self):
        """Startet die Datensimulation."""
        # if not self.machine_data:
        #     QMessageBox.warning(self, "Warnung", "Keine Maschinen vorhanden! Bitte fügen Sie zuerst Maschinen hinzu.")
        #     return
        #
        # self.update_timer.start(2000)
        # self.start_button.setEnabled(False)
        # self.stop_button.setEnabled(True)
        pass

    def stop_simulation(self):
        """Stoppt die Datensimulation."""
        # self.update_timer.stop()
        # self.start_button.setEnabled(True)
        # self.stop_button.setEnabled(False)
        pass

    def clear_all_data(self):
        """Löscht alle Maschinendaten."""
        # reply = QMessageBox.question(
        #     self, "Daten löschen",
        #     "Möchten Sie wirklich alle Maschinendaten löschen?",
        #     QMessageBox.Yes | QMessageBox.No
        # )
        #
        # if reply == QMessageBox.Yes:
        #     self.machine_data.clear()
        #     self.update_table_display()
        #     self.update_status_display()
        pass

    # TODO: Aufgabe 8 - Implementieren Sie die Update-Methoden
    def update_machine_data(self):
        """Aktualisiert die Maschinendaten (Simulation)."""
        # for machine in self.machine_data:
        #     if machine['status'] == 'Läuft':
        #         # Realistische Schwankungen simulieren
        #         machine['temperature'] += random.uniform(-2, 3)
        #         machine['temperature'] = max(50, min(100, machine['temperature']))
        #
        #         machine['pressure'] += random.uniform(-0.3, 0.3)
        #         machine['pressure'] = max(5, min(12, machine['pressure']))
        #
        #         machine['power'] += random.uniform(-5, 5)
        #         machine['power'] = max(30, min(100, machine['power']))
        #
        #         machine['production'] = random.randint(200, 300)
        #
        #         # Gelegentliche Status-Änderungen
        #         if random.random() < 0.05:  # 5% Chance
        #             machine['status'] = random.choice(['Bereit', 'Wartung', 'Fehler'])
        #
        #         machine['last_update'] = datetime.now().strftime('%H:%M:%S')
        #
        # self.update_table_display()
        # self.update_status_display()
        pass

    def update_table_display(self):
        """Aktualisiert die Tabellendarstellung."""
        # self.data_table.setRowCount(len(self.machine_data))
        #
        # for row, machine in enumerate(self.machine_data):
        #     # Maschinennamen
        #     self.data_table.setItem(row, 0, QTableWidgetItem(machine['name']))
        #
        #     # Temperatur
        #     temp_item = QTableWidgetItem(f"{machine['temperature']:.1f}")
        #     if machine['temperature'] > 80:
        #         temp_item.setBackground(QColor(255, 200, 200))  # Rot bei hoher Temp
        #     self.data_table.setItem(row, 1, temp_item)
        #
        #     # Druck
        #     self.data_table.setItem(row, 2, QTableWidgetItem(f"{machine['pressure']:.1f}"))
        #
        #     # Leistung
        #     power_item = QTableWidgetItem(f"{machine['power']:.0f}")
        #     if machine['power'] < 50:
        #         power_item.setBackground(QColor(255, 255, 200))  # Gelb bei niedriger Leistung
        #     self.data_table.setItem(row, 3, power_item)
        #
        #     # Produktion
        #     self.data_table.setItem(row, 4, QTableWidgetItem(str(machine['production'])))
        #
        #     # Status mit Farben
        #     status_item = QTableWidgetItem(machine['status'])
        #     if machine['status'] == 'Läuft':
        #         status_item.setBackground(QColor(200, 255, 200))  # Grün
        #     elif machine['status'] == 'Wartung':
        #         status_item.setBackground(QColor(255, 255, 200))  # Gelb
        #     elif machine['status'] == 'Fehler':
        #         status_item.setBackground(QColor(255, 200, 200))  # Rot
        #     self.data_table.setItem(row, 5, status_item)
        #
        #     # Letztes Update
        #     self.data_table.setItem(row, 6, QTableWidgetItem(machine['last_update']))
        pass

    def update_status_display(self):
        """Aktualisiert die Status-Anzeige."""
        # if not self.machine_data:
        #     self.total_machines_label.setText("Maschinen: 0")
        #     self.running_machines_label.setText("Läuft: 0")
        #     self.avg_temperature_label.setText("Ø Temperatur: 0°C")
        #     self.total_production_label.setText("Gesamt/h: 0")
        #     self.efficiency_progress.setValue(0)
        #     return
        #
        # total_machines = len(self.machine_data)
        # running_machines = sum(1 for m in self.machine_data if m['status'] == 'Läuft')
        # avg_temp = sum(m['temperature'] for m in self.machine_data) / total_machines
        # total_production = sum(m['production'] for m in self.machine_data if m['status'] == 'Läuft')
        # efficiency = (running_machines / total_machines) * 100 if total_machines > 0 else 0
        #
        # self.total_machines_label.setText(f"Maschinen: {total_machines}")
        # self.running_machines_label.setText(f"Läuft: {running_machines}")
        # self.avg_temperature_label.setText(f"Ø Temperatur: {avg_temp:.1f}°C")
        # self.total_production_label.setText(f"Gesamt/h: {total_production}")
        # self.efficiency_progress.setValue(int(efficiency))
        pass


# BONUS-AUFGABE: Erweiterte Funktionen
class ErweitertesMaschinendatenInterface(MaschinendatenInterface):
    """Erweiterte Version mit zusätzlichen Funktionen."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("BONUS: Erweiterte Maschinendaten-Interface")

    def setup_ui(self):
        """Erweiterte UI mit zusätzlichen Funktionen."""
        super().setup_ui()

        # TODO: BONUS - Erweitern Sie das Control Panel
        # Fügen Sie hinzu:
        # - Export-Button für CSV
        # - Filter nach Status
        # - Manueller Alarm-Test
        # - Wartungs-Planer

    # TODO: BONUS - Implementieren Sie erweiterte Methoden
    def export_to_csv(self):
        """Exportiert Daten als CSV."""
        pass

    def trigger_maintenance_alert(self):
        """Löst einen Wartungsalarm aus."""
        pass

    def filter_by_status(self, status):
        """Filtert Anzeige nach Status."""
        pass


def main():
    """Hauptfunktion zum Testen der Übung."""
    app = QApplication(sys.argv)

    # Wählen Sie hier welche Version Sie testen möchten:

    # Standard-Übung
    window = MaschinendatenInterface()

    # Für Bonus-Aufgaben:
    # window = ErweitertesMaschinendatenInterface()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()


"""
LÖSUNGSHINWEISE:
===============

Grundaufgaben:
1. Erstellen Sie eine Liste: self.machine_data = []
2. Erstellen Sie QTimer: self.update_timer = QTimer()
3. Starten Sie Timer: self.update_timer.start(2000)
4. Implementieren Sie create_control_panel mit Layouts und Buttons
5. Erstellen Sie QTableWidget mit 7 Spalten
6. Erstellen Sie Status-Labels und ProgressBar
7. Implementieren Sie Event-Handler für Buttons
8. Implementieren Sie Update-Methoden für Daten und UI

Wichtige Konzepte:
- QTimer für periodische Updates
- QTableWidget für strukturierte Datenanzeige
- QTableWidgetItem für Zellen-Inhalte
- QColor für Hintergrund-Farben
- Datenvalidierung vor Aktionen
- Status-Updates mit Berechnungen

ERWARTETE FUNKTIONEN:
====================

✅ Maschinen können hinzugefügt werden
✅ Simulation startet/stoppt Datenupdates
✅ Tabelle zeigt alle Maschinendaten
✅ Farb-Coding für kritische Werte
✅ Status-Panel zeigt Übersichtsdaten
✅ Timer aktualisiert Daten automatisch
✅ Daten können komplett gelöscht werden
✅ Benutzer-Feedback durch MessageBoxes

BONUS-FEATURES:
==============
✅ CSV-Export Funktionalität
✅ Status-Filter für Tabelle
✅ Wartungsalarm-System
✅ Erweiterte Validierung
✅ Historische Daten-Speicherung
"""
