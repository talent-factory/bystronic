#!/usr/bin/env python3
"""
PyQt/PySide Grundlagen - Widgets und Layouts
============================================

Dieses Beispiel demonstriert die grundlegenden PyQt/PySide-Konzepte:
- Fenster und Widgets erstellen
- Verschiedene Layout-Manager verwenden
- Event-Handling und Signals/Slots
- Grundlegende Widget-Typen

Autor: Daniel Senften
"""

import sys

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QAction, QFont
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QSplitter,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class GrundlagenWidget(QMainWindow):
    """Hauptfenster zur Demonstration grundlegender PyQt-Widgets."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt Grundlagen - Bystronic UI-Entwicklung")
        self.setGeometry(100, 100, 1000, 700)

        # Statusbar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Bereit - PyQt Grundlagen", 5000)

        # Timer für Demos
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)

        self.setup_menubar()
        self.setup_ui()

        # Variablen für Demo
        self.progress_value = 0

    def setup_menubar(self):
        """Erstellt die Menüleiste."""
        menubar = self.menuBar()

        # Datei-Menü
        datei_menu = menubar.addMenu("&Datei")

        neue_aktion = QAction("&Neu", self)
        neue_aktion.setShortcut("Ctrl+N")
        neue_aktion.triggered.connect(lambda: self.show_message("Neue Datei"))
        datei_menu.addAction(neue_aktion)

        oeffnen_aktion = QAction("&Öffnen", self)
        oeffnen_aktion.setShortcut("Ctrl+O")
        oeffnen_aktion.triggered.connect(lambda: self.show_message("Datei öffnen"))
        datei_menu.addAction(oeffnen_aktion)

        datei_menu.addSeparator()

        beenden_aktion = QAction("&Beenden", self)
        beenden_aktion.setShortcut("Ctrl+Q")
        beenden_aktion.triggered.connect(self.close)
        datei_menu.addAction(beenden_aktion)

        # Hilfe-Menü
        hilfe_menu = menubar.addMenu("&Hilfe")
        info_aktion = QAction("&Info", self)
        info_aktion.triggered.connect(self.show_info)
        hilfe_menu.addAction(info_aktion)

    def setup_ui(self):
        """Erstellt die Benutzeroberfläche."""
        # Zentrales Widget mit Tabs
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Hauptlayout
        main_layout = QVBoxLayout(central_widget)

        # Titel
        title_label = QLabel("PyQt/PySide Grundlagen für Bystronic-Entwickler")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(title_label)

        # Tab-Widget
        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        # Verschiedene Tabs erstellen
        self.create_basic_widgets_tab()
        self.create_layout_demo_tab()
        self.create_input_widgets_tab()
        self.create_display_widgets_tab()

    def create_basic_widgets_tab(self):
        """Erstellt Tab mit grundlegenden Widgets."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Gruppenbox für Buttons
        button_group = QGroupBox("Schaltflächen")
        button_layout = QHBoxLayout(button_group)

        # Einfacher Button
        simple_button = QPushButton("Einfacher Button")
        simple_button.clicked.connect(
            lambda: self.show_message("Einfacher Button geklickt!")
        )
        button_layout.addWidget(simple_button)

        # Button mit Icon (simuliert)
        icon_button = QPushButton("Button mit 'Icon'")
        icon_button.setStyleSheet(
            "background-color: #4CAF50; color: white; font-weight: bold;"
        )
        icon_button.clicked.connect(lambda: self.show_message("Icon-Button geklickt!"))
        button_layout.addWidget(icon_button)

        # Deaktivierter Button
        disabled_button = QPushButton("Deaktiviert")
        disabled_button.setEnabled(False)
        button_layout.addWidget(disabled_button)

        layout.addWidget(button_group)

        # Gruppenbox für Labels
        label_group = QGroupBox("Labels und Text")
        label_layout = QVBoxLayout(label_group)

        normal_label = QLabel("Dies ist ein normales Label")
        label_layout.addWidget(normal_label)

        styled_label = QLabel("Dies ist ein gestyltes Label")
        styled_label.setStyleSheet("color: blue; font-size: 14px; font-weight: bold;")
        label_layout.addWidget(styled_label)

        html_label = QLabel(
            "<b>HTML-formatiertes</b> <i>Label</i> mit <font color='red'>Farbe</font>"
        )
        label_layout.addWidget(html_label)

        layout.addWidget(label_group)

        # Gruppenbox für Checkboxen und Radio Buttons
        selection_group = QGroupBox("Auswahl-Widgets")
        selection_layout = QVBoxLayout(selection_group)

        # Checkboxen
        checkbox1 = QCheckBox("Option 1 aktivieren")
        checkbox1.stateChanged.connect(
            lambda state: self.status_bar.showMessage(
                f"Checkbox 1: {'aktiviert' if state == Qt.Checked else 'deaktiviert'}",
                3000,
            )
        )
        selection_layout.addWidget(checkbox1)

        checkbox2 = QCheckBox("Option 2 aktivieren")
        checkbox2.setChecked(True)  # Standardmäßig aktiviert
        selection_layout.addWidget(checkbox2)

        # Radio Buttons
        radio1 = QRadioButton("Laser-Schnitt")
        radio1.setChecked(True)  # Standardauswahl
        selection_layout.addWidget(radio1)

        radio2 = QRadioButton("Plasma-Schnitt")
        selection_layout.addWidget(radio2)

        radio3 = QRadioButton("Wasser-Schnitt")
        selection_layout.addWidget(radio3)

        layout.addWidget(selection_group)

        self.tab_widget.addTab(tab, "Basis-Widgets")

    def create_layout_demo_tab(self):
        """Demonstriert verschiedene Layout-Manager."""
        tab = QWidget()
        main_layout = QVBoxLayout(tab)

        # Splitter für verschiedene Layout-Bereiche
        splitter = QSplitter(Qt.Horizontal)

        # VBox Layout Demo
        vbox_widget = QGroupBox("VBox Layout (Vertikal)")
        vbox_layout = QVBoxLayout(vbox_widget)
        for i in range(1, 4):
            btn = QPushButton(f"VBox Button {i}")
            vbox_layout.addWidget(btn)
        splitter.addWidget(vbox_widget)

        # HBox Layout Demo
        hbox_widget = QGroupBox("HBox Layout (Horizontal)")
        hbox_layout = QHBoxLayout(hbox_widget)
        for i in range(1, 4):
            btn = QPushButton(f"HBox {i}")
            hbox_layout.addWidget(btn)
        splitter.addWidget(hbox_widget)

        # Grid Layout Demo
        grid_widget = QGroupBox("Grid Layout (Raster)")
        grid_layout = QGridLayout(grid_widget)

        # Grid mit Buttons füllen
        positions = [(i, j) for i in range(3) for j in range(3)]
        for position in positions:
            button = QPushButton(f"({position[0]},{position[1]})")
            grid_layout.addWidget(button, *position)

        splitter.addWidget(grid_widget)

        main_layout.addWidget(splitter)

        # Layout-Kontrollen
        control_group = QGroupBox("Layout-Kontrollen")
        control_layout = QHBoxLayout(control_group)

        stretch_button = QPushButton("Stretch hinzufügen")
        stretch_button.clicked.connect(
            lambda: self.show_message("Stretch würde Platz hinzufügen")
        )
        control_layout.addWidget(stretch_button)

        spacing_button = QPushButton("Spacing ändern")
        spacing_button.clicked.connect(
            lambda: self.show_message("Spacing würde Abstände ändern")
        )
        control_layout.addWidget(spacing_button)

        main_layout.addWidget(control_group)

        self.tab_widget.addTab(tab, "Layouts")

    def create_input_widgets_tab(self):
        """Erstellt Tab mit Eingabe-Widgets."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Textfelder
        text_group = QGroupBox("Text-Eingabe")
        text_layout = QVBoxLayout(text_group)

        # Einzelzeile
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Geben Sie hier Text ein...")
        self.line_edit.textChanged.connect(
            lambda text: self.status_bar.showMessage(f"Text: {text}", 1000)
        )
        text_layout.addWidget(QLabel("Einzeiliges Textfeld:"))
        text_layout.addWidget(self.line_edit)

        # Mehrzeilig
        self.text_edit = QTextEdit()
        self.text_edit.setPlaceholderText("Mehrzeiliger Text...")
        self.text_edit.setMaximumHeight(100)
        text_layout.addWidget(QLabel("Mehrzeiliges Textfeld:"))
        text_layout.addWidget(self.text_edit)

        layout.addWidget(text_group)

        # Numerische Eingabe
        numeric_group = QGroupBox("Numerische Eingabe")
        numeric_layout = QHBoxLayout(numeric_group)

        # Spinbox
        spin_label = QLabel("Anzahl Teile:")
        self.spin_box = QSpinBox()
        self.spin_box.setRange(0, 1000)
        self.spin_box.setValue(100)
        self.spin_box.setSuffix(" Stk")
        numeric_layout.addWidget(spin_label)
        numeric_layout.addWidget(self.spin_box)

        # Slider
        slider_label = QLabel("Temperatur:")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 200)
        self.slider.setValue(65)
        self.temp_label = QLabel("65°C")
        self.slider.valueChanged.connect(
            lambda value: self.temp_label.setText(f"{value}°C")
        )
        numeric_layout.addWidget(slider_label)
        numeric_layout.addWidget(self.slider)
        numeric_layout.addWidget(self.temp_label)

        layout.addWidget(numeric_group)

        # Auswahl-Widgets
        selection_group = QGroupBox("Auswahl-Listen")
        selection_layout = QVBoxLayout(selection_group)

        # Combobox
        combo_label = QLabel("Maschinentyp auswählen:")
        self.combo_box = QComboBox()
        self.combo_box.addItems(
            [
                "Laser-Schneidmaschine",
                "Plasma-Schneidmaschine",
                "Wasser-Schneidmaschine",
                "Stanzmaschine",
                "Biegemaschine",
            ]
        )
        self.combo_box.currentTextChanged.connect(
            lambda text: self.status_bar.showMessage(f"Ausgewählt: {text}", 3000)
        )
        selection_layout.addWidget(combo_label)
        selection_layout.addWidget(self.combo_box)

        layout.addWidget(selection_group)

        # Buttons für Aktionen
        action_layout = QHBoxLayout()

        clear_button = QPushButton("Alles löschen")
        clear_button.clicked.connect(self.clear_all_inputs)
        action_layout.addWidget(clear_button)

        get_values_button = QPushButton("Werte anzeigen")
        get_values_button.clicked.connect(self.show_input_values)
        action_layout.addWidget(get_values_button)

        layout.addLayout(action_layout)

        self.tab_widget.addTab(tab, "Eingabe-Widgets")

    def create_display_widgets_tab(self):
        """Erstellt Tab mit Anzeige-Widgets."""
        tab = QWidget()
        layout = QVBoxLayout(tab)

        # Progress Bar
        progress_group = QGroupBox("Fortschrittsanzeige")
        progress_layout = QVBoxLayout(progress_group)

        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 100)
        self.progress_bar.setValue(0)
        progress_layout.addWidget(self.progress_bar)

        progress_controls = QHBoxLayout()
        start_progress = QPushButton("Progress starten")
        start_progress.clicked.connect(self.start_progress_demo)
        progress_controls.addWidget(start_progress)

        stop_progress = QPushButton("Progress stoppen")
        stop_progress.clicked.connect(self.stop_progress_demo)
        progress_controls.addWidget(stop_progress)

        reset_progress = QPushButton("Reset")
        reset_progress.clicked.connect(
            lambda: (self.progress_bar.setValue(0), setattr(self, "progress_value", 0))
        )
        progress_controls.addWidget(reset_progress)

        progress_layout.addLayout(progress_controls)
        layout.addWidget(progress_group)

        # Status-Anzeigen
        status_group = QGroupBox("Status-Anzeigen")
        status_layout = QVBoxLayout(status_group)

        # Verschiedene Status-Labels
        self.machine_status = QLabel("Maschinen-Status: Bereit")
        self.machine_status.setStyleSheet(
            "padding: 10px; border: 2px solid green; background-color: lightgreen;"
        )
        status_layout.addWidget(self.machine_status)

        self.temp_status = QLabel("Temperatur: Normal (65°C)")
        self.temp_status.setStyleSheet(
            "padding: 10px; border: 2px solid blue; background-color: lightblue;"
        )
        status_layout.addWidget(self.temp_status)

        self.production_status = QLabel("Produktion: 245 Teile/Stunde")
        self.production_status.setStyleSheet(
            "padding: 10px; border: 2px solid orange; background-color: lightyellow;"
        )
        status_layout.addWidget(self.production_status)

        # Buttons zum Status ändern
        status_buttons = QHBoxLayout()

        ready_btn = QPushButton("Bereit")
        ready_btn.clicked.connect(
            lambda: self.update_machine_status("Bereit", "green", "lightgreen")
        )
        status_buttons.addWidget(ready_btn)

        running_btn = QPushButton("Läuft")
        running_btn.clicked.connect(
            lambda: self.update_machine_status("Läuft", "blue", "lightblue")
        )
        status_buttons.addWidget(running_btn)

        warning_btn = QPushButton("Warnung")
        warning_btn.clicked.connect(
            lambda: self.update_machine_status("Warnung", "orange", "lightyellow")
        )
        status_buttons.addWidget(warning_btn)

        error_btn = QPushButton("Fehler")
        error_btn.clicked.connect(
            lambda: self.update_machine_status("Fehler", "red", "lightcoral")
        )
        status_buttons.addWidget(error_btn)

        status_layout.addLayout(status_buttons)
        layout.addWidget(status_group)

        self.tab_widget.addTab(tab, "Anzeige-Widgets")

    def show_message(self, message):
        """Zeigt eine Nachricht in einem MessageBox an."""
        QMessageBox.information(self, "Information", message)

    def show_info(self):
        """Zeigt Informationen über die Anwendung."""
        QMessageBox.about(
            self,
            "Über diese Anwendung",
            "PyQt Grundlagen Demo\n\n"
            "Diese Anwendung demonstriert grundlegende PyQt/PySide-Konzepte "
            "für Bystronic-Entwickler.\n\n"
            "Erstellt für den Python Grundkurs.",
        )

    def clear_all_inputs(self):
        """Löscht alle Eingabefelder."""
        self.line_edit.clear()
        self.text_edit.clear()
        self.spin_box.setValue(0)
        self.slider.setValue(0)
        self.combo_box.setCurrentIndex(0)
        self.status_bar.showMessage("Alle Eingaben gelöscht", 3000)

    def show_input_values(self):
        """Zeigt alle aktuellen Eingabewerte an."""
        values = f"""Aktuelle Eingabewerte:

Textfeld: {self.line_edit.text()}
Textbereich: {self.text_edit.toPlainText()[:50]}...
Anzahl: {self.spin_box.value()}
Temperatur: {self.slider.value()}°C
Maschinentyp: {self.combo_box.currentText()}"""

        QMessageBox.information(self, "Eingabewerte", values)

    def start_progress_demo(self):
        """Startet die Progress-Bar-Demo."""
        self.progress_value = 0
        self.timer.start(100)  # Alle 100ms

    def stop_progress_demo(self):
        """Stoppt die Progress-Bar-Demo."""
        self.timer.stop()

    def update_progress(self):
        """Aktualisiert die Progress-Bar."""
        self.progress_value += 2
        if self.progress_value > 100:
            self.progress_value = 0

        self.progress_bar.setValue(self.progress_value)
        self.status_bar.showMessage(f"Progress: {self.progress_value}%", 1000)

    def update_machine_status(self, status, border_color, bg_color):
        """Aktualisiert den Maschinen-Status."""
        self.machine_status.setText(f"Maschinen-Status: {status}")
        self.machine_status.setStyleSheet(
            f"padding: 10px; border: 2px solid {border_color}; "
            f"background-color: {bg_color}; font-weight: bold;"
        )
        self.status_bar.showMessage(f"Status geändert zu: {status}", 3000)

    def closeEvent(self, event):
        """Wird beim Schließen des Fensters aufgerufen."""
        self.timer.stop()
        event.accept()


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    app = QApplication(sys.argv)

    # Anwendungs-Stil setzen
    app.setStyle("Fusion")

    # Hauptfenster erstellen und anzeigen
    window = GrundlagenWidget()
    window.show()

    # Event-Loop starten
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
