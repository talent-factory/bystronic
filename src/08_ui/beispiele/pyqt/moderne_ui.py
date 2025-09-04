#!/usr/bin/env python3
"""
Moderne UI mit PyQt/PySide - Dark Theme & Glassmorphism
======================================================

Dieses Beispiel zeigt moderne UI-Design-Konzepte:
- Dark Theme Implementation
- Glassmorphism-Effekte
- Animationen und Übergänge
- Custom Widgets und Styling
- Responsive Design
- Modern Material Design Elemente

Autor: Python Grundkurs für Bystronic-Entwickler
"""

import sys

from PySide6.QtCore import QEasingCurve, QPropertyAnimation, Qt, QTimer, Signal
from PySide6.QtGui import (
    QColor,
)
from PySide6.QtWidgets import (
    QApplication,
    QComboBox,
    QFrame,
    QGraphicsDropShadowEffect,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)


class ModernButton(QPushButton):
    """Moderne Button-Komponente mit Hover-Effekten."""

    def __init__(self, text, color="primary", parent=None):
        super().__init__(text, parent)
        self.color_scheme = color
        self.setup_style()

    def setup_style(self):
        """Setzt das moderne Button-Styling."""
        colors = {
            "primary": {
                "bg": "#3498db",
                "hover": "#2980b9",
                "pressed": "#1f5582",
                "text": "#ffffff"
            },
            "success": {
                "bg": "#2ecc71",
                "hover": "#27ae60",
                "pressed": "#1e7e34",
                "text": "#ffffff"
            },
            "danger": {
                "bg": "#e74c3c",
                "hover": "#c0392b",
                "pressed": "#a93226",
                "text": "#ffffff"
            },
            "dark": {
                "bg": "#34495e",
                "hover": "#2c3e50",
                "pressed": "#1a252f",
                "text": "#ffffff"
            }
        }

        color = colors.get(self.color_scheme, colors["primary"])

        style = f"""
        QPushButton {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {color['bg']}, stop:1 {self.darken_color(color['bg'])});
            color: {color['text']};
            border: none;
            border-radius: 8px;
            padding: 12px 24px;
            font-weight: bold;
            font-size: 14px;
        }}

        QPushButton:hover {{
            background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                stop:0 {color['hover']}, stop:1 {self.darken_color(color['hover'])});
        }}

        QPushButton:pressed {{
            background: {color['pressed']};
        }}

        QPushButton:disabled {{
            background: #95a5a6;
            color: #bdc3c7;
        }}
        """

        self.setStyleSheet(style)

        # Drop Shadow Effekt
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 3)
        self.setGraphicsEffect(shadow)

    def darken_color(self, color_hex):
        """Verdunkelt eine Hex-Farbe um 20%."""
        color = QColor(color_hex)
        return color.darker(120).name()


class ModernCard(QFrame):
    """Moderne Karten-Komponente im Glassmorphism-Stil."""

    def __init__(self, title="", content="", parent=None):
        super().__init__(parent)
        self.setup_style()
        self.setup_content(title, content)

    def setup_style(self):
        """Setzt das Karten-Styling."""
        self.setFrameStyle(QFrame.Box)

        style = """
        QFrame {
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 16px;
            backdrop-filter: blur(20px);
        }
        """

        self.setStyleSheet(style)

        # Drop Shadow
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 60))
        shadow.setOffset(0, 5)
        self.setGraphicsEffect(shadow)

    def setup_content(self, title, content):
        """Setzt den Inhalt der Karte."""
        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        if title:
            title_label = QLabel(title)
            title_label.setStyleSheet("""
                QLabel {
                    color: #ffffff;
                    font-size: 18px;
                    font-weight: bold;
                    margin-bottom: 10px;
                }
            """)
            layout.addWidget(title_label)

        if content:
            content_label = QLabel(content)
            content_label.setWordWrap(True)
            content_label.setStyleSheet("""
                QLabel {
                    color: rgba(255, 255, 255, 0.9);
                    font-size: 14px;
                    line-height: 1.4;
                }
            """)
            layout.addWidget(content_label)


class ModernProgressBar(QWidget):
    """Moderne Fortschrittsanzeige mit Animationen."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.value = 0
        self.max_value = 100
        self.setup_ui()

    def setup_ui(self):
        """Erstellt die UI."""
        layout = QVBoxLayout(self)

        # Label für Wert
        self.value_label = QLabel("0%")
        self.value_label.setAlignment(Qt.AlignCenter)
        self.value_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(self.value_label)

        # Fortschrittsbalken
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, self.max_value)
        self.progress_bar.setValue(self.value)

        # Modernes Styling
        self.progress_bar.setStyleSheet("""
            QProgressBar {
                border: none;
                border-radius: 10px;
                background: rgba(255, 255, 255, 0.2);
                height: 20px;
                text-align: center;
            }

            QProgressBar::chunk {
                border-radius: 10px;
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 #3498db, stop:0.5 #2ecc71, stop:1 #f39c12);
            }
        """)

        layout.addWidget(self.progress_bar)

    def set_value(self, value):
        """Setzt den Fortschrittswert mit Animation."""
        self.value = max(0, min(value, self.max_value))

        # Animation erstellen
        self.animation = QPropertyAnimation(self.progress_bar, b"value")
        self.animation.setDuration(500)
        self.animation.setStartValue(self.progress_bar.value())
        self.animation.setEndValue(self.value)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

        # Label während Animation aktualisieren
        self.animation.valueChanged.connect(
            lambda v: self.value_label.setText(f"{v}%")
        )

        self.animation.start()


class ModernSidebar(QWidget):
    """Moderne Sidebar mit Navigation."""

    page_changed = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """Erstellt die Sidebar UI."""
        self.setFixedWidth(250)

        layout = QVBoxLayout(self)
        layout.setSpacing(0)
        layout.setContentsMargins(0, 0, 0, 0)

        # Header
        header = QLabel("Bystronic Dashboard")
        header.setStyleSheet("""
            QLabel {
                background: rgba(52, 73, 94, 0.9);
                color: #ffffff;
                padding: 20px;
                font-size: 18px;
                font-weight: bold;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)
        layout.addWidget(header)

        # Navigation Items
        nav_items = [
            ("🏠", "Dashboard", "dashboard"),
            ("📊", "Produktion", "production"),
            ("🔧", "Wartung", "maintenance"),
            ("📈", "Statistiken", "statistics"),
            ("⚙️", "Einstellungen", "settings")
        ]

        for icon, text, page_id in nav_items:
            nav_button = self.create_nav_button(icon, text, page_id)
            layout.addWidget(nav_button)

        layout.addStretch()

        # User Info
        user_info = QLabel("👤 Benutzer: Admin")
        user_info.setStyleSheet("""
            QLabel {
                background: rgba(52, 73, 94, 0.7);
                color: rgba(255, 255, 255, 0.8);
                padding: 15px;
                border-top: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)
        layout.addWidget(user_info)

        # Sidebar-Hintergrund
        self.setStyleSheet("""
            QWidget {
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 rgba(44, 62, 80, 0.95),
                    stop:1 rgba(52, 73, 94, 0.95));
                border-right: 1px solid rgba(255, 255, 255, 0.1);
            }
        """)

    def create_nav_button(self, icon, text, page_id):
        """Erstellt einen Navigations-Button."""
        button = QPushButton(f"{icon}  {text}")
        button.setStyleSheet("""
            QPushButton {
                background: transparent;
                color: rgba(255, 255, 255, 0.9);
                border: none;
                padding: 15px 20px;
                text-align: left;
                font-size: 14px;
            }

            QPushButton:hover {
                background: rgba(255, 255, 255, 0.1);
                color: #ffffff;
            }

            QPushButton:pressed {
                background: rgba(255, 255, 255, 0.2);
            }
        """)

        button.clicked.connect(lambda: self.page_changed.emit(page_id))
        return button


class ModernDashboard(QMainWindow):
    """Moderne Dashboard-Anwendung."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bystronic Modern Dashboard")
        self.setGeometry(100, 100, 1400, 900)

        self.setup_dark_theme()
        self.setup_ui()
        self.setup_animations()

    def setup_dark_theme(self):
        """Setzt das dunkle Theme."""
        self.setStyleSheet("""
            QMainWindow {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                    stop:0 #2c3e50, stop:0.5 #34495e, stop:1 #2c3e50);
            }

            QWidget {
                background: transparent;
                color: #ffffff;
            }

            QScrollArea {
                border: none;
                background: transparent;
            }

            QScrollBar:vertical {
                background: rgba(255, 255, 255, 0.1);
                width: 12px;
                border-radius: 6px;
            }

            QScrollBar::handle:vertical {
                background: rgba(255, 255, 255, 0.3);
                border-radius: 6px;
            }

            QScrollBar::handle:vertical:hover {
                background: rgba(255, 255, 255, 0.5);
            }
        """)

    def setup_ui(self):
        """Erstellt die Benutzeroberfläche."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Sidebar
        self.sidebar = ModernSidebar()
        self.sidebar.page_changed.connect(self.change_page)
        main_layout.addWidget(self.sidebar)

        # Content Area
        self.content_area = QScrollArea()
        self.content_area.setWidgetResizable(True)
        self.content_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Initial Dashboard laden
        self.load_dashboard_page()

        main_layout.addWidget(self.content_area)

    def setup_animations(self):
        """Erstellt Animationen und Timer."""
        # Timer für Live-Updates
        self.update_timer = QTimer()
        self.update_timer.timeout.connect(self.update_live_data)
        self.update_timer.start(2000)  # Alle 2 Sekunden

        # Animation-Counter
        self.animation_counter = 0

    def change_page(self, page_id):
        """Wechselt zur angegebenen Seite."""
        if page_id == "dashboard":
            self.load_dashboard_page()
        elif page_id == "production":
            self.load_production_page()
        elif page_id == "maintenance":
            self.load_maintenance_page()
        elif page_id == "statistics":
            self.load_statistics_page()
        elif page_id == "settings":
            self.load_settings_page()

    def load_dashboard_page(self):
        """Lädt die Dashboard-Seite."""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Titel
        title = QLabel("🏠 Dashboard Übersicht")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title)

        # KPI-Karten Grid
        kpi_grid = QGridLayout()
        kpi_grid.setSpacing(20)

        # KPI-Daten
        kpi_data = [
            ("Maschinenauslastung", "87%", "success"),
            ("Stückzahl/Stunde", "245", "primary"),
            ("Qualitätsindex", "98.5%", "success"),
            ("Aktive Alarme", "2", "danger")
        ]

        self.kpi_cards = []
        for i, (title, value, color) in enumerate(kpi_data):
            card = self.create_kpi_card(title, value, color)
            kpi_grid.addWidget(card, 0, i)
            self.kpi_cards.append(card)

        layout.addLayout(kpi_grid)

        # Maschinenübersicht
        machines_card = ModernCard(
            "🏭 Maschinenübersicht",
            "Aktuelle Status der Produktionsmaschinen:"
        )

        machines_layout = QVBoxLayout()

        # Beispiel-Maschinen
        machines = [
            ("Laser 1", 92, "Läuft"),
            ("Laser 2", 87, "Läuft"),
            ("Stanze 1", 0, "Wartung"),
            ("Biegemaschine", 78, "Läuft")
        ]

        for name, utilization, status in machines:
            machine_widget = self.create_machine_widget(name, utilization, status)
            machines_layout.addWidget(machine_widget)

        machines_card.layout().addLayout(machines_layout)
        layout.addWidget(machines_card)

        # Scroll-Widget setzen
        self.content_area.setWidget(content)

    def create_kpi_card(self, title, value, color_scheme):
        """Erstellt eine KPI-Karte."""
        card = ModernCard()

        # Layout
        layout = QVBoxLayout()

        # Titel
        title_label = QLabel(title)
        title_label.setStyleSheet("""
            QLabel {
                color: rgba(255, 255, 255, 0.8);
                font-size: 14px;
                margin-bottom: 10px;
            }
        """)
        layout.addWidget(title_label)

        # Wert
        value_label = QLabel(value)
        colors = {
            "primary": "#3498db",
            "success": "#2ecc71",
            "danger": "#e74c3c",
            "warning": "#f39c12"
        }

        value_label.setStyleSheet(f"""
            QLabel {{
                color: {colors.get(color_scheme, colors['primary'])};
                font-size: 36px;
                font-weight: bold;
            }}
        """)
        layout.addWidget(value_label)

        # Trend-Indikator (Simulation)
        trend = QLabel("↗ +5.2%")
        trend.setStyleSheet("""
            QLabel {
                color: #2ecc71;
                font-size: 12px;
                font-weight: bold;
            }
        """)
        layout.addWidget(trend)

        card.setLayout(layout)
        return card

    def create_machine_widget(self, name, utilization, status):
        """Erstellt ein Maschinen-Widget."""
        widget = QWidget()
        layout = QHBoxLayout(widget)

        # Name
        name_label = QLabel(name)
        name_label.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-weight: bold;
                font-size: 14px;
            }
        """)
        name_label.setFixedWidth(120)
        layout.addWidget(name_label)

        # Auslastungsbalken
        progress = ModernProgressBar()
        progress.set_value(utilization)
        layout.addWidget(progress)

        # Status
        status_label = QLabel(status)
        status_colors = {
            "Läuft": "#2ecc71",
            "Wartung": "#f39c12",
            "Fehler": "#e74c3c",
            "Offline": "#95a5a6"
        }

        status_label.setStyleSheet(f"""
            QLabel {{
                color: {status_colors.get(status, '#ffffff')};
                font-weight: bold;
                font-size: 14px;
                padding: 5px 10px;
                border-radius: 5px;
                background: rgba(255, 255, 255, 0.1);
            }}
        """)
        status_label.setFixedWidth(80)
        layout.addWidget(status_label)

        return widget

    def load_production_page(self):
        """Lädt die Produktions-Seite."""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        # Titel
        title = QLabel("📊 Produktionsübersicht")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title)

        # Produktions-Controls
        controls_card = ModernCard("Produktionssteuerung", "")
        controls_layout = QHBoxLayout()

        start_btn = ModernButton("Produktion starten", "success")
        pause_btn = ModernButton("Pause", "warning")
        stop_btn = ModernButton("Stopp", "danger")

        controls_layout.addWidget(start_btn)
        controls_layout.addWidget(pause_btn)
        controls_layout.addWidget(stop_btn)
        controls_layout.addStretch()

        controls_card.layout().addLayout(controls_layout)
        layout.addWidget(controls_card)

        # Placeholder für weitere Inhalte
        placeholder = ModernCard(
            "Produktionsdaten",
            "Hier würden detaillierte Produktionsdaten, Diagramme und "
            "Echtzeitmetriken angezeigt werden."
        )
        layout.addWidget(placeholder)

        layout.addStretch()
        self.content_area.setWidget(content)

    def load_maintenance_page(self):
        """Lädt die Wartungs-Seite."""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("🔧 Wartungsplaner")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title)

        # Wartungsübersicht
        maintenance_card = ModernCard(
            "Anstehende Wartungen",
            "Laser 1: Routinewartung - 05.09.2024\n"
            "Stanze 1: Kalibrierung - 07.09.2024\n"
            "Biegemaschine: Reparatur - 10.09.2024"
        )
        layout.addWidget(maintenance_card)

        # Neue Wartung planen
        plan_button = ModernButton("Neue Wartung planen", "primary")
        layout.addWidget(plan_button)

        layout.addStretch()
        self.content_area.setWidget(content)

    def load_statistics_page(self):
        """Lädt die Statistik-Seite."""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("📈 Statistiken & Trends")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title)

        stats_card = ModernCard(
            "Produktionsstatistiken",
            "Hier würden detaillierte Charts und Grafiken zur\n"
            "Produktionsleistung, Qualitätsmetriken und Trends angezeigt."
        )
        layout.addWidget(stats_card)

        layout.addStretch()
        self.content_area.setWidget(content)

    def load_settings_page(self):
        """Lädt die Einstellungs-Seite."""
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setSpacing(20)
        layout.setContentsMargins(30, 30, 30, 30)

        title = QLabel("⚙️ Systemeinstellungen")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 28px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        """)
        layout.addWidget(title)

        # Theme-Auswahl
        theme_card = ModernCard("Anzeigeeinstellungen", "")
        theme_layout = QVBoxLayout()

        theme_combo = QComboBox()
        theme_combo.addItems(["Dunkles Theme", "Helles Theme", "Auto"])
        theme_combo.setStyleSheet("""
            QComboBox {
                background: rgba(255, 255, 255, 0.1);
                border: 1px solid rgba(255, 255, 255, 0.3);
                border-radius: 5px;
                padding: 8px;
                color: #ffffff;
            }
        """)
        theme_layout.addWidget(QLabel("Theme:"))
        theme_layout.addWidget(theme_combo)

        theme_card.layout().addLayout(theme_layout)
        layout.addWidget(theme_card)

        # System-Einstellungen
        system_card = ModernCard(
            "Systemkonfiguration",
            "Automatische Updates: ✓ Aktiviert\n"
            "Datenbank-Backup: Täglich um 02:00\n"
            "Session-Timeout: 60 Minuten"
        )
        layout.addWidget(system_card)

        layout.addStretch()
        self.content_area.setWidget(content)

    def update_live_data(self):
        """Aktualisiert Live-Daten (Simulation)."""
        import random

        # Animation-Counter erhöhen
        self.animation_counter += 1

        # KPI-Werte leicht variieren (nur auf Dashboard-Seite)
        if hasattr(self, 'kpi_cards') and self.kpi_cards:
            # Simulierte Schwankungen
            [random.randint(-2, 3) for _ in range(4)]

            # Hier könnten die KPI-Werte aktualisiert werden
            # Das ist eine vereinfachte Simulation
            pass


def main():
    """Hauptfunktion zum Starten der Anwendung."""
    app = QApplication(sys.argv)

    # Anwendungs-Metadaten
    app.setApplicationName("Bystronic Modern Dashboard")
    app.setApplicationVersion("2.0")

    # Hauptfenster erstellen
    window = ModernDashboard()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
