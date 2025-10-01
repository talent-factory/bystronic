#!/usr/bin/env python3
"""
🔴 ADVANCED: Übung 1 - Enterprise Mitarbeiter-Management-System
==============================================================

LERNZIELE:
- Objektorientierte Programmierung (Klassen, Datenklassen)
- Type Hints und Dokumentation
- JSON-Persistierung
- Erweiterte Validierung mit regulären Ausdrücken
- Plugin-ähnliche Architektur
- Logging und Fehlerbehandlung
- Performance-Optimierung

AUFGABE:
Entwickeln Sie ein vollständiges Enterprise-Mitarbeiter-Management-System
mit Datenpersistierung, erweiterbarer Architektur und professioneller
Code-Qualität.

ZEIT: 45-60 Minuten
SCHWIERIGKEIT: 🔴 Experte

ANFORDERUNGEN:
- Objektorientiertes Design
- Datenklassen mit Validierung
- JSON-Import/Export
- Erweiterbare Plugin-Architektur
- Comprehensive Error Handling
- Type Hints überall
- Docstrings für alle Methoden
"""

import json
import logging
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Protocol

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class ValidationError(Exception):
    """Custom Exception für Validierungsfehler."""

    pass


class ValidatorProtocol(Protocol):
    """Protocol für Validatoren - ermöglicht Plugin-Architektur."""

    def validate(self, value: Any) -> bool:
        """Validiert einen Wert."""
        ...

    def get_error_message(self) -> str:
        """Gibt Fehlermeldung zurück."""
        ...


@dataclass
class Mitarbeiter:
    """
    Datenklasse für Mitarbeiterinformationen mit integrierter Validierung.

    Attributes:
        name: Vollständiger Name (min. 2 Wörter)
        alter: Alter zwischen 16-100 Jahren
        abteilung: Gültige Abteilung aus vordefinierter Liste
        email: Gültige E-Mail-Adresse
        berufserfahrung: Jahre Berufserfahrung (optional)
        skills: Liste von Fähigkeiten
        erstellt_am: Timestamp der Erstellung
    """

    name: str
    alter: int
    abteilung: str
    email: str
    berufserfahrung: int | None = None
    skills: list[str] = field(default_factory=list)
    erstellt_am: datetime = field(default_factory=datetime.now)

    def __post_init__(self):
        """Validierung nach Initialisierung."""
        self._validate_all()

    def _validate_all(self) -> None:
        """Führt alle Validierungen durch."""
        validators = [
            (self.name, NameValidator()),
            (self.alter, AgeValidator()),
            (self.abteilung, DepartmentValidator()),
            (self.email, EmailValidator()),
        ]

        if self.berufserfahrung is not None:
            validators.append((self.berufserfahrung, ExperienceValidator()))

        for value, validator in validators:
            if not validator.validate(value):
                raise ValidationError(validator.get_error_message())

    @property
    def geburtsjahr(self) -> int:
        """Berechnet das geschätzte Geburtsjahr."""
        return datetime.now().year - self.alter

    @property
    def erfahrungsgrad(self) -> str:
        """Bestimmt den Erfahrungsgrad basierend auf Alter und Berufserfahrung."""
        erfahrung = self.berufserfahrung or 0

        if self.alter < 25:
            return "Nachwuchstalent 🌱"
        elif self.alter <= 35:
            return (
                "Senior Professional 🎯" if erfahrung >= 5 else "Junior Professional 📈"
            )
        else:
            return "Expert 🏆" if erfahrung > 10 else "Senior Professional 🎯"

    def to_dict(self) -> dict[str, Any]:
        """Konvertiert zu Dictionary für JSON-Serialisierung."""
        return {
            "name": self.name,
            "alter": self.alter,
            "abteilung": self.abteilung,
            "email": self.email,
            "berufserfahrung": self.berufserfahrung,
            "skills": self.skills,
            "erstellt_am": self.erstellt_am.isoformat(),
            "geburtsjahr": self.geburtsjahr,
            "erfahrungsgrad": self.erfahrungsgrad,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Mitarbeiter":
        """Erstellt Mitarbeiter-Objekt aus Dictionary."""
        # Entferne berechnete Felder
        data = data.copy()
        data.pop("geburtsjahr", None)
        data.pop("erfahrungsgrad", None)

        # Konvertiere Timestamp
        if "erstellt_am" in data:
            data["erstellt_am"] = datetime.fromisoformat(data["erstellt_am"])

        return cls(**data)


# Validator-Implementierungen


class NameValidator:
    """Validiert Namen (mindestens 2 Wörter, nur Buchstaben und Leerzeichen)."""

    def validate(self, name: str) -> bool:
        if not isinstance(name, str) or not name.strip():
            return False

        # Mindestens 2 Wörter, nur Buchstaben, Leerzeichen und Bindestriche
        pattern = r"^[a-zA-ZäöüÄÖÜß\s\-]{2,}\s+[a-zA-ZäöüÄÖÜß\s\-]{2,}$"
        return bool(re.match(pattern, name.strip()))

    def get_error_message(self) -> str:
        return "Name muss mindestens Vor- und Nachname enthalten (nur Buchstaben)"


class AgeValidator:
    """Validiert Alter (16-100 Jahre)."""

    def validate(self, alter: int) -> bool:
        return isinstance(alter, int) and 16 <= alter <= 100

    def get_error_message(self) -> str:
        return "Alter muss zwischen 16 und 100 Jahren liegen"


class DepartmentValidator:
    """Validiert Abteilungen gegen vordefinierte Liste."""

    VALID_DEPARTMENTS = {
        "Engineering",
        "Production",
        "Sales",
        "HR",
        "IT",
        "Finance",
        "Marketing",
        "Quality",
        "Logistics",
        "R&D",
    }

    def validate(self, abteilung: str) -> bool:
        return abteilung in self.VALID_DEPARTMENTS

    def get_error_message(self) -> str:
        return f"Abteilung muss eine der folgenden sein: {', '.join(sorted(self.VALID_DEPARTMENTS))}"


class EmailValidator:
    """Validiert E-Mail-Adressen mit regulären Ausdrücken."""

    def validate(self, email: str) -> bool:
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return bool(re.match(pattern, email))

    def get_error_message(self) -> str:
        return "Ungültige E-Mail-Adresse"


class ExperienceValidator:
    """Validiert Berufserfahrung (0-50 Jahre)."""

    def validate(self, erfahrung: int) -> bool:
        return isinstance(erfahrung, int) and 0 <= erfahrung <= 50

    def get_error_message(self) -> str:
        return "Berufserfahrung muss zwischen 0 und 50 Jahren liegen"


class MitarbeiterManager:
    """
    Manager-Klasse für Mitarbeiter-CRUD-Operationen und Persistierung.
    """

    def __init__(self, storage_path: str = "mitarbeiter_data.json"):
        self.storage_path = Path(storage_path)
        self.mitarbeiter: list[Mitarbeiter] = []
        self.load_data()

    def add_mitarbeiter(self, mitarbeiter: Mitarbeiter) -> None:
        """Fügt einen neuen Mitarbeiter hinzu."""
        # Prüfe auf Duplikate (E-Mail)
        if any(m.email == mitarbeiter.email for m in self.mitarbeiter):
            raise ValidationError(
                f"Mitarbeiter mit E-Mail {mitarbeiter.email} existiert bereits"
            )

        self.mitarbeiter.append(mitarbeiter)
        logger.info(f"Mitarbeiter {mitarbeiter.name} hinzugefügt")
        self.save_data()

    def get_mitarbeiter_by_email(self, email: str) -> Mitarbeiter | None:
        """Findet Mitarbeiter anhand der E-Mail."""
        return next((m for m in self.mitarbeiter if m.email == email), None)

    def list_mitarbeiter(self) -> list[Mitarbeiter]:
        """Gibt alle Mitarbeiter zurück."""
        return self.mitarbeiter.copy()

    def save_data(self) -> None:
        """Speichert alle Mitarbeiter in JSON-Datei."""
        try:
            data = [m.to_dict() for m in self.mitarbeiter]
            with open(self.storage_path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            logger.info(f"Daten gespeichert in {self.storage_path}")
        except Exception as e:
            logger.error(f"Fehler beim Speichern: {e}")
            raise

    def load_data(self) -> None:
        """Lädt Mitarbeiter aus JSON-Datei."""
        if not self.storage_path.exists():
            logger.info("Keine bestehende Datendatei gefunden, starte mit leerer Liste")
            return

        try:
            with open(self.storage_path, encoding="utf-8") as f:
                data = json.load(f)

            self.mitarbeiter = [Mitarbeiter.from_dict(item) for item in data]
            logger.info(f"{len(self.mitarbeiter)} Mitarbeiter geladen")
        except Exception as e:
            logger.error(f"Fehler beim Laden: {e}")
            self.mitarbeiter = []


class MitarbeiterInterface:
    """
    Benutzeroberfläche für das Mitarbeiter-Management-System.
    """

    def __init__(self):
        self.manager = MitarbeiterManager()

    def sammle_mitarbeiterdaten(self) -> Mitarbeiter:
        """Sammelt Mitarbeiterdaten mit umfassender Validierung."""
        print("📝 NEUEN MITARBEITER ERFASSEN")
        print("-" * 40)

        while True:
            try:
                # Name
                name = input("Vollständiger Name: ").strip()

                # Alter
                alter = int(input("Alter: "))

                # E-Mail
                email = input("E-Mail-Adresse: ").strip()

                # Abteilung
                departments = sorted(DepartmentValidator.VALID_DEPARTMENTS)
                print("\nVerfügbare Abteilungen:")
                for i, dept in enumerate(departments, 1):
                    print(f"  {i}. {dept}")

                dept_choice = int(input("Abteilung (Nummer): ")) - 1
                abteilung = departments[dept_choice]

                # Berufserfahrung (optional)
                erfahrung_input = input(
                    "Jahre Berufserfahrung (Enter für überspringen): "
                ).strip()
                berufserfahrung = int(erfahrung_input) if erfahrung_input else None

                # Skills (optional)
                skills_input = input(
                    "Fähigkeiten (kommagetrennt, Enter für überspringen): "
                ).strip()
                skills = (
                    [s.strip() for s in skills_input.split(",")] if skills_input else []
                )

                # Mitarbeiter erstellen (Validierung erfolgt automatisch)
                mitarbeiter = Mitarbeiter(
                    name=name,
                    alter=alter,
                    abteilung=abteilung,
                    email=email,
                    berufserfahrung=berufserfahrung,
                    skills=skills,
                )

                return mitarbeiter

            except (ValueError, IndexError) as e:
                print(f"❌ Eingabefehler: {e}")
            except ValidationError as e:
                print(f"❌ Validierungsfehler: {e}")

            print("\nBitte versuchen Sie es erneut.\n")

    def zeige_mitarbeiterprofil(self, mitarbeiter: Mitarbeiter) -> None:
        """Zeigt ein detailliertes Mitarbeiterprofil an."""
        print("\n" + "=" * 70)
        print(f"📋 MITARBEITERPROFIL: {mitarbeiter.name.upper()}")
        print("=" * 70)

        print(f"👤 Name:              {mitarbeiter.name}")
        print(f"📧 E-Mail:            {mitarbeiter.email}")
        print(f"🎂 Alter:             {mitarbeiter.alter} Jahre")
        print(f"📅 Geburtsjahr:       ca. {mitarbeiter.geburtsjahr}")
        print(f"🏢 Abteilung:         {mitarbeiter.abteilung}")
        print(f"📊 Erfahrungsgrad:    {mitarbeiter.erfahrungsgrad}")

        if mitarbeiter.berufserfahrung is not None:
            print(f"💼 Berufserfahrung:   {mitarbeiter.berufserfahrung} Jahre")

        if mitarbeiter.skills:
            print(f"🛠️  Fähigkeiten:      {', '.join(mitarbeiter.skills)}")

        print(
            f"📅 Erstellt am:       {mitarbeiter.erstellt_am.strftime('%d.%m.%Y %H:%M')}"
        )
        print("=" * 70)

    def run(self) -> None:
        """Hauptschleife der Anwendung."""
        print("🏢 BYSTRONIC ENTERPRISE MITARBEITER-MANAGEMENT-SYSTEM")
        print("=" * 60)

        try:
            # Neuen Mitarbeiter erfassen
            mitarbeiter = self.sammle_mitarbeiterdaten()

            # Zu Manager hinzufügen
            self.manager.add_mitarbeiter(mitarbeiter)

            # Profil anzeigen
            self.zeige_mitarbeiterprofil(mitarbeiter)

            # Statistiken
            total = len(self.manager.list_mitarbeiter())
            print(f"\n📊 Gesamt {total} Mitarbeiter im System")
            print("✅ Mitarbeiter erfolgreich gespeichert!")

        except KeyboardInterrupt:
            print("\n\n⚠️ Vorgang abgebrochen.")
        except Exception as e:
            logger.error(f"Unerwarteter Fehler: {e}")
            print(f"\n❌ Ein unerwarteter Fehler ist aufgetreten: {e}")


def main():
    """Hauptfunktion."""
    interface = MitarbeiterInterface()
    interface.run()


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE:
==================
🏢 BYSTRONIC ENTERPRISE MITARBEITER-MANAGEMENT-SYSTEM
============================================================

📝 NEUEN MITARBEITER ERFASSEN
----------------------------------------
Vollständiger Name: Dr. Sarah Schmidt
Alter: 32
E-Mail-Adresse: sarah.schmidt@smartfactory.com

Verfügbare Abteilungen:
  1. Engineering
  2. Finance
  3. HR
  4. IT
  5. Logistics
  6. Marketing
  7. Production
  8. Quality
  9. R&D
  10. Sales
Abteilung (Nummer): 9
Jahre Berufserfahrung (Enter für überspringen): 8
Fähigkeiten (kommagetrennt, Enter für überspringen): Python, Machine Learning, Data Analysis

======================================================================
📋 MITARBEITERPROFIL: DR. SARAH SCHMIDT
======================================================================
👤 Name:              Dr. Sarah Schmidt
📧 E-Mail:            sarah.schmidt@smartfactory.com
🎂 Alter:             32 Jahre
📅 Geburtsjahr:       ca. 1993
🏢 Abteilung:         R&D
📊 Erfahrungsgrad:    Senior Professional 🎯
💼 Berufserfahrung:   8 Jahre
🛠️  Fähigkeiten:      Python, Machine Learning, Data Analysis
📅 Erstellt am:       05.12.2024 14:30
======================================================================

📊 Gesamt 1 Mitarbeiter im System
✅ Mitarbeiter erfolgreich gespeichert!

LERNKONTROLLE:
==============
□ Verstehe ich Datenklassen und @dataclass?
□ Kann ich Type Hints korrekt verwenden?
□ Beherrsche ich objektorientierte Programmierung?
□ Kann ich JSON-Persistierung implementieren?
□ Verstehe ich Protokolle und Plugin-Architektur?
□ Kann ich umfassende Validierung implementieren?
□ Beherrsche ich Logging und Error Handling?
"""
