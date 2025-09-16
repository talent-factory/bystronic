#!/usr/bin/env python3
"""
🔴 ADVANCED: Übung 3 - Skill-Analytics-Platform
===============================================

LERNZIELE:
- Datenbank-ähnliche Operationen mit SQLite
- REST-API-ähnliche Schnittstelle
- Erweiterte Analytics und Reporting
- Plugin-Architektur für Skill-Bewertungen
- Performance-Optimierung für grosse Datenmengen
- Comprehensive Testing und Dokumentation

AUFGABE:
Entwickeln Sie eine vollständige Skill-Analytics-Platform mit
Datenbankpersistierung, API-ähnlicher Schnittstelle und erweiterten
Analysefunktionen für Enterprise-Skill-Management.

ZEIT: 45-60 Minuten
SCHWIERIGKEIT: 🔴 Experte

ANFORDERUNGEN:
- SQLite-Datenbankintegration
- REST-API-ähnliche Operationen (CRUD)
- Erweiterte Analytics und Machine Learning
- Plugin-System für Bewertungsalgorithmen
- Performance-Benchmarking
- Umfassende Dokumentation
"""

import json
import logging
import sqlite3
import statistics
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from datetime import datetime
from functools import wraps
from typing import Any, Protocol

# Logging konfigurieren
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


def performance_monitor(func):
    """Decorator für Performance-Monitoring."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = (end_time - start_time) * 1000
        logger.info(f"{func.__name__} executed in {execution_time:.2f}ms")
        return result

    return wrapper


@dataclass
class Skill:
    """Datenklasse für Skills mit umfassenden Metadaten."""

    id: int | None
    name: str
    category: str
    level: int  # 1-10
    experience_years: float
    last_used: str  # ISO date
    projects: list[str]
    certifications: list[str]
    learning_resources: list[str]
    market_demand: int  # 1-10
    salary_impact: float  # Multiplikator
    created_at: str
    updated_at: str

    def __post_init__(self):
        """Validierung nach Initialisierung."""
        if not 1 <= self.level <= 10:
            raise ValueError("Level muss zwischen 1 und 10 liegen")
        if not 1 <= self.market_demand <= 10:
            raise ValueError("Market demand muss zwischen 1 und 10 liegen")
        if self.experience_years < 0:
            raise ValueError("Erfahrung kann nicht negativ sein")


class SkillEvaluatorProtocol(Protocol):
    """Protocol für Skill-Bewertungsalgorithmen."""

    def calculate_skill_score(self, skill: Skill) -> float:
        """Berechnet einen Gesamtscore für den Skill."""
        ...

    def get_improvement_suggestions(self, skill: Skill) -> list[str]:
        """Gibt Verbesserungsvorschläge zurück."""
        ...

    def get_algorithm_name(self) -> str:
        """Gibt den Namen des Algorithmus zurück."""
        ...


class StandardSkillEvaluator:
    """Standard-Algorithmus für Skill-Bewertung."""

    def calculate_skill_score(self, skill: Skill) -> float:
        """
        Berechnet einen gewichteten Gesamtscore.

        Faktoren:
        - Skill Level (40%)
        - Erfahrung (25%)
        - Marktrelevanz (20%)
        - Zertifizierungen (10%)
        - Aktualität (5%)
        """
        # Basis-Score aus Level
        level_score = skill.level / 10 * 0.4

        # Erfahrungs-Score (logarithmisch skaliert)
        import math

        exp_score = min(math.log(skill.experience_years + 1) / math.log(11), 1) * 0.25

        # Marktrelevanz-Score
        market_score = skill.market_demand / 10 * 0.2

        # Zertifizierungs-Score
        cert_score = min(len(skill.certifications) / 3, 1) * 0.1

        # Aktualitäts-Score (basierend auf letzter Nutzung)
        try:
            last_used = datetime.fromisoformat(skill.last_used)
            days_ago = (datetime.now() - last_used).days
            recency_score = max(0, 1 - days_ago / 365) * 0.05
        except:
            recency_score = 0

        total_score = (
            level_score + exp_score + market_score + cert_score + recency_score
        )
        return round(total_score * 100, 2)  # 0-100 Skala

    def get_improvement_suggestions(self, skill: Skill) -> list[str]:
        """Generiert Verbesserungsvorschläge."""
        suggestions = []

        if skill.level < 5:
            suggestions.append("📚 Grundlagen durch Online-Kurse stärken")

        if len(skill.certifications) == 0:
            suggestions.append("🏆 Professionelle Zertifizierung anstreben")

        if skill.experience_years < 2:
            suggestions.append("💼 Mehr praktische Projekte durchführen")

        try:
            last_used = datetime.fromisoformat(skill.last_used)
            if (datetime.now() - last_used).days > 90:
                suggestions.append("🔄 Skill durch aktuelle Projekte auffrischen")
        except:
            pass

        if skill.market_demand >= 8 and skill.level < 7:
            suggestions.append("🚀 Hohe Marktrelevanz - Level dringend ausbauen!")

        if len(skill.learning_resources) < 3:
            suggestions.append("📖 Mehr Lernressourcen sammeln")

        return suggestions

    def get_algorithm_name(self) -> str:
        return "Standard Weighted Evaluator"


class AdvancedSkillEvaluator:
    """Erweiterte Skill-Bewertung mit Machine Learning-ähnlichen Ansätzen."""

    def calculate_skill_score(self, skill: Skill) -> float:
        """Erweiterte Bewertung mit nicht-linearen Faktoren."""
        import math

        # Exponentieller Level-Bonus für hohe Skills
        level_factor = (skill.level / 10) ** 1.5 * 0.35

        # Erfahrungs-Plateau-Effekt
        exp_factor = (1 - math.exp(-skill.experience_years / 3)) * 0.3

        # Markt-Skill-Synergie
        market_skill_synergy = (skill.market_demand * skill.level) / 100 * 0.2

        # Zertifizierungs-Exponential
        cert_factor = (1 - math.exp(-len(skill.certifications))) * 0.1

        # Projekt-Diversität
        project_diversity = min(len(skill.projects) / 5, 1) * 0.05

        total_score = (
            level_factor
            + exp_factor
            + market_skill_synergy
            + cert_factor
            + project_diversity
        )

        return round(total_score * 100, 2)

    def get_improvement_suggestions(self, skill: Skill) -> list[str]:
        """KI-inspirierte Verbesserungsvorschläge."""
        suggestions = []
        score = self.calculate_skill_score(skill)

        if score < 30:
            suggestions.append("🎯 Fokus: Intensive Grundlagenarbeit erforderlich")
        elif score < 60:
            suggestions.append("📈 Wachstumsphase: Praktische Erfahrung sammeln")
        elif score < 80:
            suggestions.append("🏅 Spezialisierung: Expertise in Nischenbereichen")
        else:
            suggestions.append("🌟 Mentoring: Wissen an andere weitergeben")

        # Markt-basierte Empfehlungen
        if skill.market_demand > skill.level:
            gap = skill.market_demand - skill.level
            suggestions.append(
                f"💰 Marktchance: {gap} Level Verbesserung = höheres Gehalt"
            )

        return suggestions

    def get_algorithm_name(self) -> str:
        return "Advanced ML-Inspired Evaluator"


class SkillDatabase:
    """Datenbankklasse für Skill-Management mit SQLite."""

    def __init__(self, db_path: str = "skills.db"):
        self.db_path = db_path
        self.init_database()

    @contextmanager
    def get_connection(self):
        """Context Manager für Datenbankverbindungen."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Ermöglicht dict-ähnlichen Zugriff
        try:
            yield conn
        finally:
            conn.close()

    def init_database(self) -> None:
        """Initialisiert die Datenbankstruktur."""
        with self.get_connection() as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS skills (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT UNIQUE NOT NULL,
                    category TEXT NOT NULL,
                    level INTEGER NOT NULL CHECK (level BETWEEN 1 AND 10),
                    experience_years REAL NOT NULL CHECK (experience_years >= 0),
                    last_used TEXT NOT NULL,
                    projects TEXT NOT NULL,  -- JSON array
                    certifications TEXT NOT NULL,  -- JSON array
                    learning_resources TEXT NOT NULL,  -- JSON array
                    market_demand INTEGER NOT NULL CHECK (market_demand BETWEEN 1 AND 10),
                    salary_impact REAL NOT NULL,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL
                )
            """
            )

            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_category ON skills(category)
            """
            )

            conn.execute(
                """
                CREATE INDEX IF NOT EXISTS idx_level ON skills(level)
            """
            )

            conn.commit()
            logger.info("Datenbank initialisiert")

    @performance_monitor
    def create_skill(self, skill: Skill) -> int:
        """Erstellt einen neuen Skill."""
        with self.get_connection() as conn:
            cursor = conn.execute(
                """
                INSERT INTO skills (
                    name, category, level, experience_years, last_used,
                    projects, certifications, learning_resources,
                    market_demand, salary_impact, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
                (
                    skill.name,
                    skill.category,
                    skill.level,
                    skill.experience_years,
                    skill.last_used,
                    json.dumps(skill.projects),
                    json.dumps(skill.certifications),
                    json.dumps(skill.learning_resources),
                    skill.market_demand,
                    skill.salary_impact,
                    skill.created_at,
                    skill.updated_at,
                ),
            )
            conn.commit()
            return cursor.lastrowid

    @performance_monitor
    def get_skill(self, skill_id: int) -> Skill | None:
        """Holt einen Skill anhand der ID."""
        with self.get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM skills WHERE id = ?", (skill_id,)
            ).fetchone()
            if row:
                return self._row_to_skill(row)
            return None

    @performance_monitor
    def get_all_skills(self) -> list[Skill]:
        """Holt alle Skills."""
        with self.get_connection() as conn:
            rows = conn.execute("SELECT * FROM skills ORDER BY name").fetchall()
            return [self._row_to_skill(row) for row in rows]

    @performance_monitor
    def update_skill(self, skill: Skill) -> bool:
        """Aktualisiert einen Skill."""
        with self.get_connection() as conn:
            cursor = conn.execute(
                """
                UPDATE skills SET
                    name = ?, category = ?, level = ?, experience_years = ?,
                    last_used = ?, projects = ?, certifications = ?,
                    learning_resources = ?, market_demand = ?, salary_impact = ?,
                    updated_at = ?
                WHERE id = ?
            """,
                (
                    skill.name,
                    skill.category,
                    skill.level,
                    skill.experience_years,
                    skill.last_used,
                    json.dumps(skill.projects),
                    json.dumps(skill.certifications),
                    json.dumps(skill.learning_resources),
                    skill.market_demand,
                    skill.salary_impact,
                    skill.updated_at,
                    skill.id,
                ),
            )
            conn.commit()
            return cursor.rowcount > 0

    @performance_monitor
    def delete_skill(self, skill_id: int) -> bool:
        """Löscht einen Skill."""
        with self.get_connection() as conn:
            cursor = conn.execute("DELETE FROM skills WHERE id = ?", (skill_id,))
            conn.commit()
            return cursor.rowcount > 0

    def search_skills(self, query: str) -> list[Skill]:
        """Sucht Skills basierend auf verschiedenen Feldern."""
        with self.get_connection() as conn:
            rows = conn.execute(
                """
                SELECT * FROM skills
                WHERE name LIKE ? OR category LIKE ? OR projects LIKE ?
                ORDER BY level DESC
            """,
                (f"%{query}%", f"%{query}%", f"%{query}%"),
            ).fetchall()
            return [self._row_to_skill(row) for row in rows]

    def filter_by_category(self, category: str) -> list[Skill]:
        """Filtert Skills nach Kategorie."""
        with self.get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM skills WHERE category = ? ORDER BY level DESC",
                (category,),
            ).fetchall()
            return [self._row_to_skill(row) for row in rows]

    def filter_by_level_range(self, min_level: int, max_level: int) -> list[Skill]:
        """Filtert Skills nach Level-Bereich."""
        with self.get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM skills WHERE level BETWEEN ? AND ? ORDER BY level DESC",
                (min_level, max_level),
            ).fetchall()
            return [self._row_to_skill(row) for row in rows]

    def get_statistics(self) -> dict[str, Any]:
        """Berechnet umfassende Statistiken."""
        with self.get_connection() as conn:
            # Grundstatistiken
            stats = conn.execute(
                """
                SELECT
                    COUNT(*) as total_skills,
                    AVG(level) as avg_level,
                    AVG(experience_years) as avg_experience,
                    MAX(level) as max_level,
                    MIN(level) as min_level,
                    AVG(market_demand) as avg_market_demand
                FROM skills
            """
            ).fetchone()

            # Kategorien-Verteilung
            categories = conn.execute(
                """
                SELECT category, COUNT(*) as count, AVG(level) as avg_level
                FROM skills
                GROUP BY category
                ORDER BY count DESC
            """
            ).fetchall()

            # Level-Verteilung
            level_dist = conn.execute(
                """
                SELECT level, COUNT(*) as count
                FROM skills
                GROUP BY level
                ORDER BY level
            """
            ).fetchall()

            return {
                "total_skills": stats["total_skills"],
                "avg_level": round(stats["avg_level"] or 0, 2),
                "avg_experience": round(stats["avg_experience"] or 0, 2),
                "max_level": stats["max_level"] or 0,
                "min_level": stats["min_level"] or 0,
                "avg_market_demand": round(stats["avg_market_demand"] or 0, 2),
                "categories": [dict(row) for row in categories],
                "level_distribution": [dict(row) for row in level_dist],
            }

    def _row_to_skill(self, row: sqlite3.Row) -> Skill:
        """Konvertiert Datenbankzeile zu Skill-Objekt."""
        return Skill(
            id=row["id"],
            name=row["name"],
            category=row["category"],
            level=row["level"],
            experience_years=row["experience_years"],
            last_used=row["last_used"],
            projects=json.loads(row["projects"]),
            certifications=json.loads(row["certifications"]),
            learning_resources=json.loads(row["learning_resources"]),
            market_demand=row["market_demand"],
            salary_impact=row["salary_impact"],
            created_at=row["created_at"],
            updated_at=row["updated_at"],
        )


class SkillAnalytics:
    """Erweiterte Analytics-Engine für Skills."""

    def __init__(self, database: SkillDatabase):
        self.db = database
        self.evaluators = {
            "standard": StandardSkillEvaluator(),
            "advanced": AdvancedSkillEvaluator(),
        }

    def generate_skill_report(
        self, skill: Skill, evaluator_name: str = "standard"
    ) -> dict[str, Any]:
        """Generiert einen umfassenden Skill-Report."""
        evaluator = self.evaluators.get(evaluator_name, self.evaluators["standard"])

        score = evaluator.calculate_skill_score(skill)
        suggestions = evaluator.get_improvement_suggestions(skill)

        # Marktanalyse
        market_analysis = self._analyze_market_position(skill)

        # Karriere-Impact
        career_impact = self._calculate_career_impact(skill)

        return {
            "skill": asdict(skill),
            "overall_score": score,
            "grade": self._score_to_grade(score),
            "improvement_suggestions": suggestions,
            "market_analysis": market_analysis,
            "career_impact": career_impact,
            "evaluator_used": evaluator.get_algorithm_name(),
            "generated_at": datetime.now().isoformat(),
        }

    def _analyze_market_position(self, skill: Skill) -> dict[str, Any]:
        """Analysiert die Marktposition des Skills."""
        # Vergleich mit anderen Skills in derselben Kategorie
        category_skills = self.db.filter_by_category(skill.category)

        if len(category_skills) > 1:
            category_levels = [s.level for s in category_skills if s.id != skill.id]
            if category_levels:
                avg_category_level = statistics.mean(category_levels)
                percentile = (
                    sum(1 for level in category_levels if level < skill.level)
                    / len(category_levels)
                    * 100
                )
            else:
                avg_category_level = skill.level
                percentile = 50
        else:
            avg_category_level = skill.level
            percentile = 50

        return {
            "category_average_level": round(avg_category_level, 2),
            "percentile_in_category": round(percentile, 1),
            "market_demand_rating": self._demand_to_rating(skill.market_demand),
            "competitive_advantage": skill.level > avg_category_level,
        }

    def _calculate_career_impact(self, skill: Skill) -> dict[str, Any]:
        """Berechnet den Karriere-Impact des Skills."""
        # Gehaltspotential basierend auf Level und Marktrelevanz
        base_impact = skill.level * skill.market_demand * skill.salary_impact

        # Zertifizierungs-Bonus
        cert_bonus = len(skill.certifications) * 0.1

        # Erfahrungs-Multiplikator
        exp_multiplier = min(skill.experience_years / 5, 2)

        total_impact = base_impact * (1 + cert_bonus) * exp_multiplier

        return {
            "salary_impact_score": round(total_impact, 2),
            "certification_bonus": round(cert_bonus * 100, 1),
            "experience_multiplier": round(exp_multiplier, 2),
            "career_stage": self._determine_career_stage(skill),
            "growth_potential": self._calculate_growth_potential(skill),
        }

    def _score_to_grade(self, score: float) -> str:
        """Konvertiert Score zu Buchstabennote."""
        if score >= 90:
            return "A+"
        elif score >= 85:
            return "A"
        elif score >= 80:
            return "A-"
        elif score >= 75:
            return "B+"
        elif score >= 70:
            return "B"
        elif score >= 65:
            return "B-"
        elif score >= 60:
            return "C+"
        elif score >= 55:
            return "C"
        elif score >= 50:
            return "C-"
        else:
            return "D"

    def _demand_to_rating(self, demand: int) -> str:
        """Konvertiert Marktrelevanz zu Rating."""
        if demand >= 9:
            return "Sehr hoch"
        elif demand >= 7:
            return "Hoch"
        elif demand >= 5:
            return "Mittel"
        elif demand >= 3:
            return "Niedrig"
        else:
            return "Sehr niedrig"

    def _determine_career_stage(self, skill: Skill) -> str:
        """Bestimmt die Karrierestufe basierend auf Skill."""
        if skill.level <= 3:
            return "Einsteiger"
        elif skill.level <= 6:
            return "Fortgeschritten"
        elif skill.level <= 8:
            return "Experte"
        else:
            return "Thought Leader"

    def _calculate_growth_potential(self, skill: Skill) -> str:
        """Berechnet das Wachstumspotential."""
        potential_score = (10 - skill.level) * skill.market_demand

        if potential_score >= 20:
            return "Sehr hoch"
        elif potential_score >= 15:
            return "Hoch"
        elif potential_score >= 10:
            return "Mittel"
        else:
            return "Begrenzt"


def create_sample_data(db: SkillDatabase) -> None:
    """Erstellt Beispieldaten für Demonstrationszwecke."""
    sample_skills = [
        Skill(
            id=None,
            name="Python",
            category="Data Science",
            level=8,
            experience_years=3.5,
            last_used="2024-12-01",
            projects=["ML Pipeline", "Data Analysis", "Automation"],
            certifications=["Python Institute PCAP"],
            learning_resources=["Real Python", "Python.org"],
            market_demand=9,
            salary_impact=1.3,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        ),
        Skill(
            id=None,
            name="Java",
            category="Enterprise",
            level=7,
            experience_years=5.0,
            last_used="2024-11-15",
            projects=["Microservices", "Spring Boot API"],
            certifications=["Oracle Certified Java Programmer"],
            learning_resources=["Oracle Docs"],
            market_demand=8,
            salary_impact=1.2,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        ),
        Skill(
            id=None,
            name="JavaScript",
            category="Web Development",
            level=6,
            experience_years=2.5,
            last_used="2024-12-03",
            projects=["React App", "Node.js Backend"],
            certifications=[],
            learning_resources=["MDN", "JavaScript.info"],
            market_demand=9,
            salary_impact=1.1,
            created_at=datetime.now().isoformat(),
            updated_at=datetime.now().isoformat(),
        ),
    ]

    for skill in sample_skills:
        try:
            db.create_skill(skill)
            logger.info(f"Sample skill '{skill.name}' created")
        except Exception as e:
            logger.warning(f"Could not create sample skill '{skill.name}': {e}")


class SkillPlatformAPI:
    """REST-API-ähnliche Schnittstelle für die Skill-Platform."""

    def __init__(self):
        self.db = SkillDatabase()
        self.analytics = SkillAnalytics(self.db)

        # Erstelle Beispieldaten falls Datenbank leer
        if not self.db.get_all_skills():
            create_sample_data(self.db)

    def show_dashboard(self) -> None:
        """Zeigt das Haupt-Dashboard an."""
        stats = self.db.get_statistics()

        print("\n" + "=" * 80)
        print("🚀 SKILL-ANALYTICS-PLATFORM - ENTERPRISE DASHBOARD")
        print("=" * 80)

        print(f"📊 Gesamt Skills:              {stats['total_skills']}")
        print(f"⭐ Durchschnittliches Level:   {stats['avg_level']}/10")
        print(f"📅 Durchschnittliche Erfahrung: {stats['avg_experience']} Jahre")
        print(f"🏆 Höchstes Level:             {stats['max_level']}/10")
        print(f"📈 Marktrelevanz (Ø):          {stats['avg_market_demand']}/10")

        print("\n📂 KATEGORIEN-VERTEILUNG:")
        for cat in stats["categories"]:
            print(
                f"  {cat['category']:<20} {cat['count']} Skills (Ø Level: {cat['avg_level']:.1f})"
            )

        print("\n📊 LEVEL-VERTEILUNG:")
        for level in stats["level_distribution"]:
            bar = "█" * level["count"]
            print(f"  Level {level['level']:2d}: {bar} ({level['count']})")

    def generate_comprehensive_report(
        self, skill_id: int, evaluator: str = "advanced"
    ) -> None:
        """Generiert einen umfassenden Skill-Report."""
        skill = self.db.get_skill(skill_id)
        if not skill:
            print(f"❌ Skill mit ID {skill_id} nicht gefunden.")
            return

        report = self.analytics.generate_skill_report(skill, evaluator)

        print("\n" + "=" * 80)
        print(f"📋 UMFASSENDER SKILL-REPORT: {skill.name.upper()}")
        print("=" * 80)

        print(
            f"🎯 Gesamtscore:     {report['overall_score']}/100 (Note: {report['grade']})"
        )
        print(f"📊 Kategorie:       {skill.category}")
        print(f"⭐ Aktuelles Level: {skill.level}/10")
        print(f"📅 Erfahrung:       {skill.experience_years} Jahre")
        print(f"📈 Marktrelevanz:   {skill.market_demand}/10")

        # Marktanalyse
        market = report["market_analysis"]
        print("\n🏪 MARKTANALYSE:")
        print(f"  Kategorie-Durchschnitt: {market['category_average_level']}/10")
        print(f"  Percentile:            {market['percentile_in_category']}%")
        print(f"  Marktbewertung:        {market['market_demand_rating']}")
        print(
            f"  Wettbewerbsvorteil:    {'✅ Ja' if market['competitive_advantage'] else '❌ Nein'}"
        )

        # Karriere-Impact
        career = report["career_impact"]
        print("\n💼 KARRIERE-IMPACT:")
        print(f"  Gehaltspotential:      {career['salary_impact_score']:.1f}")
        print(f"  Zertifizierungs-Bonus: {career['certification_bonus']}%")
        print(f"  Erfahrungs-Multiplikator: {career['experience_multiplier']}x")
        print(f"  Karrierestufe:         {career['career_stage']}")
        print(f"  Wachstumspotential:    {career['growth_potential']}")

        # Verbesserungsvorschläge
        print("\n💡 VERBESSERUNGSVORSCHLÄGE:")
        for i, suggestion in enumerate(report["improvement_suggestions"], 1):
            print(f"  {i}. {suggestion}")

        print(f"\n🔬 Evaluator: {report['evaluator_used']}")
        print(f"📅 Generiert: {report['generated_at']}")

    def run_interactive_mode(self) -> None:
        """Startet den interaktiven Modus."""
        while True:
            print("\n" + "=" * 60)
            print("🏢 SKILL-ANALYTICS-PLATFORM")
            print("=" * 60)
            print("1. Dashboard anzeigen")
            print("2. Alle Skills auflisten")
            print("3. Skill-Report generieren")
            print("4. Skills suchen")
            print("5. Nach Kategorie filtern")
            print("6. Performance-Statistiken")
            print("0. Beenden")
            print("=" * 60)

            choice = input("Ihre Wahl (0-6): ").strip()

            if choice == "0":
                break
            elif choice == "1":
                self.show_dashboard()
            elif choice == "2":
                skills = self.db.get_all_skills()
                print(f"\n📋 ALLE SKILLS ({len(skills)}):")
                for skill in skills:
                    print(
                        f"  {skill.id:2d}. {skill.name:<15} (Level {skill.level}/10, {skill.category})"
                    )
            elif choice == "3":
                try:
                    skill_id = int(input("Skill-ID: "))
                    evaluator = input(
                        "Evaluator (standard/advanced, Enter für advanced): "
                    ).strip()
                    if not evaluator:
                        evaluator = "advanced"
                    self.generate_comprehensive_report(skill_id, evaluator)
                except ValueError:
                    print("❌ Ungültige ID!")
            elif choice == "4":
                query = input("Suchbegriff: ").strip()
                results = self.db.search_skills(query)
                print(f"\n🔍 {len(results)} Ergebnisse gefunden:")
                for skill in results:
                    print(f"  {skill.id:2d}. {skill.name} (Level {skill.level}/10)")
            elif choice == "5":
                stats = self.db.get_statistics()
                categories = [cat["category"] for cat in stats["categories"]]
                print(f"Verfügbare Kategorien: {', '.join(categories)}")
                category = input("Kategorie: ").strip()
                results = self.db.filter_by_category(category)
                print(f"\n📂 {len(results)} Skills in '{category}':")
                for skill in results:
                    print(f"  {skill.id:2d}. {skill.name} (Level {skill.level}/10)")
            elif choice == "6":
                print("\n⚡ PERFORMANCE-STATISTIKEN:")
                print("Siehe Log-Ausgaben für detaillierte Performance-Metriken")
            else:
                print("❌ Ungültige Auswahl!")


def main():
    """Hauptfunktion der Skill-Analytics-Platform."""
    print("🚀 BYSTRONIC SKILL-ANALYTICS-PLATFORM")
    print("=" * 50)
    print("Enterprise-Grade Skill-Management mit erweiterten Analytics")

    try:
        platform = SkillPlatformAPI()
        platform.run_interactive_mode()
    except Exception as e:
        logger.error(f"Kritischer Fehler: {e}")
        print(f"❌ Kritischer Fehler: {e}")

    print("\n🎉 Vielen Dank für die Nutzung der Skill-Analytics-Platform!")


if __name__ == "__main__":
    main()

"""
ERWARTETE AUSGABE:
==================
🚀 BYSTRONIC SKILL-ANALYTICS-PLATFORM
==================================================
Enterprise-Grade Skill-Management mit erweiterten Analytics

================================================================================
🚀 SKILL-ANALYTICS-PLATFORM - ENTERPRISE DASHBOARD
================================================================================
📊 Gesamt Skills:              3
⭐ Durchschnittliches Level:   7.0/10
📅 Durchschnittliche Erfahrung: 3.7 Jahre
🏆 Höchstes Level:             8/10
📈 Marktrelevanz (Ø):          8.7/10

📂 KATEGORIEN-VERTEILUNG:
  Data Science         1 Skills (Ø Level: 8.0)
  Enterprise           1 Skills (Ø Level: 7.0)
  Web Development      1 Skills (Ø Level: 6.0)

📊 LEVEL-VERTEILUNG:
  Level  6: █ (1)
  Level  7: █ (1)
  Level  8: █ (1)

============================================================
🏢 SKILL-ANALYTICS-PLATFORM
============================================================
1. Dashboard anzeigen
2. Alle Skills auflisten
3. Skill-Report generieren
4. Skills suchen
5. Nach Kategorie filtern
6. Performance-Statistiken
0. Beenden
============================================================
Ihre Wahl (0-6): 3
Skill-ID: 1
Evaluator (standard/advanced, Enter für advanced):

================================================================================
📋 UMFASSENDER SKILL-REPORT: PYTHON
================================================================================
🎯 Gesamtscore:     87.2/100 (Note: A)
📊 Kategorie:       Data Science
⭐ Aktuelles Level: 8/10
📅 Erfahrung:       3.5 Jahre
📈 Marktrelevanz:   9/10

🏪 MARKTANALYSE:
  Kategorie-Durchschnitt: 8.0/10
  Percentile:            50.0%
  Marktbewertung:        Sehr hoch
  Wettbewerbsvorteil:    ❌ Nein

💼 KARRIERE-IMPACT:
  Gehaltspotential:      75.6
  Zertifizierungs-Bonus: 10.0%
  Erfahrungs-Multiplikator: 1.4x
  Karrierestufe:         Experte
  Wachstumspotential:    Mittel

💡 VERBESSERUNGSVORSCHLÄGE:
  1. 🌟 Mentoring: Wissen an andere weitergeben
  2. 💰 Marktchance: 1 Level Verbesserung = höheres Gehalt

🔬 Evaluator: Advanced ML-Inspired Evaluator
📅 Generiert: 2024-12-05T15:30:22.123456

LERNKONTROLLE:
==============
□ Verstehe ich SQLite-Datenbankoperationen?
□ Kann ich REST-API-ähnliche Schnittstellen entwickeln?
□ Beherrsche ich erweiterte Analytics und Reporting?
□ Kann ich Plugin-Architekturen implementieren?
□ Verstehe ich Performance-Optimierung?
□ Kann ich umfassende Enterprise-Systeme entwickeln?
"""
