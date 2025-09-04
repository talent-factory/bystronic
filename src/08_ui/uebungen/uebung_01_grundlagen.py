#!/usr/bin/env python3
"""
Übung 1: GUI-Grundlagen mit PyQt/PySide
======================================

Lernziele:
- Erste PyQt-Anwendung erstellen
- Widgets und Layouts verwenden
- Event-Handling implementieren
- Einfache Benutzerinteraktionen

Schwierigkeitsgrad: ⭐⭐☆☆☆ (Anfänger)

Autor: Daniel Senften
"""

import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


# TODO: Aufgabe 1 - Vervollständigen Sie die KlassenDefinition
class MeineErsteGUI(QMainWindow):
    """Meine erste PyQt-Anwendung."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Übung 1: Meine erste GUI")
        self.setGeometry(100, 100, 600, 400)

        # TODO: Rufen Sie hier die setup_ui Methode auf
        # self.setup_ui()

    def setup_ui(self):
        """Erstellt die Benutzeroberfläche."""
        # Zentrales Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # TODO: Aufgabe 2 - Erstellen Sie ein Haupt-Layout (VBoxLayout)
        # main_layout = QVBoxLayout(central_widget)

        # TODO: Aufgabe 3 - Erstellen Sie einen Titel-Label
        # title_label = QLabel("Willkommen zu meiner ersten GUI!")
        # title_label.setAlignment(Qt.AlignCenter)
        # main_layout.addWidget(title_label)

        # TODO: Aufgabe 4 - Erstellen Sie ein Eingabefeld mit Label
        # input_layout = QHBoxLayout()
        # input_label = QLabel("Ihr Name:")
        # self.name_input = QLineEdit()
        # input_layout.addWidget(input_label)
        # input_layout.addWidget(self.name_input)
        # main_layout.addLayout(input_layout)

        # TODO: Aufgabe 5 - Erstellen Sie einen Button
        # self.greet_button = QPushButton("Begrüßen")
        # self.greet_button.clicked.connect(self.show_greeting)
        # main_layout.addWidget(self.greet_button)

        # TODO: Aufgabe 6 - Erstellen Sie ein Textfeld für Ausgabe
        # self.output_text = QTextEdit()
        # self.output_text.setMaximumHeight(100)
        # main_layout.addWidget(self.output_text)

        pass  # Entfernen Sie diese Zeile, wenn Sie die Aufgaben lösen

    # TODO: Aufgabe 7 - Implementieren Sie die show_greeting Methode
    def show_greeting(self):
        """Zeigt eine Begrüßung an."""
        # name = self.name_input.text()
        # if name:
        #     greeting = f"Hallo {name}! Willkommen bei Bystronic!"
        #     self.output_text.append(greeting)
        # else:
        #     QMessageBox.warning(self, "Warnung", "Bitte geben Sie Ihren Namen ein!")
        pass


# BONUS-AUFGABEN für Fortgeschrittene
class ErweiterteGUI(QMainWindow):
    """Erweiterte GUI mit mehr Funktionen."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bonus: Erweiterte GUI")
        self.setGeometry(150, 150, 700, 500)

        self.setup_ui()

    def setup_ui(self):
        """Erstellt eine erweiterte Benutzeroberfläche."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        # Titel
        title = QLabel("🏭 Bystronic Steuerung")
        title.setStyleSheet("font-size: 18px; font-weight: bold; color: #1f4e79;")
        title.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title)

        # TODO: BONUS 1 - Maschinenauswahl
        # machine_layout = QHBoxLayout()
        # machine_layout.addWidget(QLabel("Maschine:"))
        # self.machine_combo = QComboBox()
        # self.machine_combo.addItems(["Laser 1", "Laser 2", "Stanze 1", "Biegemaschine"])
        # machine_layout.addWidget(self.machine_combo)
        # main_layout.addLayout(machine_layout)

        # TODO: BONUS 2 - Temperatur-Slider
        # temp_layout = QVBoxLayout()
        # temp_layout.addWidget(QLabel("Temperatur-Einstellung:"))
        # self.temp_slider = QSlider(Qt.Horizontal)
        # self.temp_slider.setRange(50, 100)
        # self.temp_slider.setValue(65)
        # self.temp_label = QLabel("65°C")
        # self.temp_slider.valueChanged.connect(self.update_temp_label)
        # temp_layout.addWidget(self.temp_slider)
        # temp_layout.addWidget(self.temp_label)
        # main_layout.addLayout(temp_layout)

        # TODO: BONUS 3 - Produktionsanzahl
        # production_layout = QHBoxLayout()
        # production_layout.addWidget(QLabel("Stückzahl:"))
        # self.production_spinbox = QSpinBox()
        # self.production_spinbox.setRange(1, 1000)
        # self.production_spinbox.setValue(100)
        # production_layout.addWidget(self.production_spinbox)
        # main_layout.addLayout(production_layout)

        # TODO: BONUS 4 - Fortschrittsbalken
        # self.progress_bar = QProgressBar()
        # self.progress_bar.setRange(0, 100)
        # self.progress_bar.setValue(0)
        # main_layout.addWidget(self.progress_bar)

        # TODO: BONUS 5 - Steuerungsbuttons
        # button_layout = QHBoxLayout()
        # self.start_button = QPushButton("▶️ Start")
        # self.stop_button = QPushButton("⏹️ Stopp")
        # self.reset_button = QPushButton("🔄 Reset")
        #
        # self.start_button.clicked.connect(self.start_production)
        # self.stop_button.clicked.connect(self.stop_production)
        # self.reset_button.clicked.connect(self.reset_production)
        #
        # button_layout.addWidget(self.start_button)
        # button_layout.addWidget(self.stop_button)
        # button_layout.addWidget(self.reset_button)
        # main_layout.addLayout(button_layout)

        pass  # Entfernen Sie diese Zeile für die Bonus-Aufgaben

    # TODO: BONUS 6 - Implementieren Sie die Event-Handler
    def update_temp_label(self, value):
        """Aktualisiert das Temperatur-Label."""
        # self.temp_label.setText(f"{value}°C")
        pass

    def start_production(self):
        """Startet die Produktion."""
        # machine = self.machine_combo.currentText()
        # temp = self.temp_slider.value()
        # quantity = self.production_spinbox.value()
        #
        # QMessageBox.information(
        #     self,
        #     "Produktion gestartet",
        #     f"Maschine: {machine}\nTemperatur: {temp}°C\nStückzahl: {quantity}"
        # )
        pass

    def stop_production(self):
        """Stoppt die Produktion."""
        # QMessageBox.warning(self, "Stopp", "Produktion wurde gestoppt!")
        pass

    def reset_production(self):
        """Setzt alle Werte zurück."""
        # self.temp_slider.setValue(65)
        # self.production_spinbox.setValue(100)
        # self.progress_bar.setValue(0)
        # self.machine_combo.setCurrentIndex(0)
        pass


def main():
    """Hauptfunktion zum Testen der Übungen."""
    app = QApplication(sys.argv)

    # Wählen Sie hier welche GUI Sie testen möchten:

    # Grundübung
    window = MeineErsteGUI()

    # Für Bonus-Aufgaben, kommentieren Sie die obige Zeile aus und verwenden Sie diese:
    # window = ErweiterteGUI()

    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()


"""
LÖSUNGSHINWEISE:
===============

Grundlagen-Aufgaben:
1. Rufen Sie self.setup_ui() im __init__ auf
2. Erstellen Sie QVBoxLayout(central_widget)
3. Erstellen Sie QLabel mit Text und setAlignment(Qt.AlignCenter)
4. Erstellen Sie QHBoxLayout, QLabel und QLineEdit
5. Erstellen Sie QPushButton und verbinden Sie clicked.connect()
6. Erstellen Sie QTextEdit und setzen Sie setMaximumHeight()
7. Holen Sie Text mit .text(), prüfen Sie auf leer, verwenden Sie .append()

Bonus-Aufgaben:
- Verwenden Sie QComboBox.addItems() für Dropdown
- QSlider mit setRange(), setValue() und valueChanged Signal
- QSpinBox für numerische Eingabe
- QProgressBar mit setRange() und setValue()
- Verbinden Sie Buttons mit entsprechenden Methoden
- Implementieren Sie Event-Handler für Benutzerinteraktionen

ERWARTETE FUNKTIONEN:
====================

Grundversion:
✅ Fenster öffnet sich
✅ Titel wird angezeigt
✅ Eingabefeld für Namen
✅ Button zeigt Begrüßung an
✅ Warnung bei leerem Namen
✅ Ausgabe im Textfeld

Bonus-Version:
✅ Maschinenauswahl funktioniert
✅ Temperatur-Slider aktualisiert Label
✅ Produktionsparameter einstellbar
✅ Buttons zeigen entsprechende Meldungen
✅ Reset setzt alle Werte zurück
"""
