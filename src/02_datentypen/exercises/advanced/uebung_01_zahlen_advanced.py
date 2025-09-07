#!/usr/bin/env python3
"""
🔴 ADVANCED - Bystronic Python Grundkurs - Kapitel 2
Übung 1: Professionelle Zahlenverarbeitung mit OOP

🎯 LERNZIELE (45-60 Minuten):
- Objektorientierte Datenmodellierung
- Design Patterns für numerische Berechnungen
- Erweiterte mathematische Operationen
- Performance-Optimierung
- Professionelle Fehlerbehandlung und Logging
- Unit Testing und Dokumentation

📚 HILFSMITTEL:
- Hints: solutions/advanced/uebung_01_hints.md
- Skeleton: solutions/advanced/uebung_01_skeleton.py
- Partial: solutions/advanced/uebung_01_partial.py
- Complete: solutions/advanced/uebung_01_complete.py

🏭 BYSTRONIC-KONTEXT:
Entwickeln Sie ein professionelles Produktionsdaten-Analysesystem
mit objektorientierten Design Patterns und Enterprise-Standards.
"""

import math
import statistics
import logging
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Dict, Optional, Union, Callable, Any
from datetime import datetime, timedelta
from enum import Enum
import json


# Konfiguration des Logging-Systems
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class QualitaetsStatus(Enum):
    """Enumeration für Qualitätsstatus"""
    OK = "OK"
    NOK = "NOK"
    NACHARBEIT = "NACHARBEIT"
    AUSSCHUSS = "AUSSCHUSS"


@dataclass
class Messwert:
    """
    🎯 Aufgabe 1: Datenklasse für Messwerte
    
    Erweitern Sie diese Datenklasse um:
    - Automatische Qualitätsbewertung
    - Zeitstempel-Verwaltung
    - Serialisierung/Deserialisierung
    """
    wert: float
    sollwert: float
    toleranz: float
    zeitstempel: datetime = field(default_factory=datetime.now)
    operator: str = "System"
    maschine_id: str = "UNKNOWN"
    
    def __post_init__(self):
        """Automatische Qualitätsbewertung nach Initialisierung"""
        self._berechne_qualitaetsstatus()
    
    def _berechne_qualitaetsstatus(self) -> None:
        """Berechnet den Qualitätsstatus basierend auf Toleranzen"""
        abweichung = abs(self.wert - self.sollwert)
        
        if abweichung <= self.toleranz:
            self.status = QualitaetsStatus.OK
        elif abweichung <= self.toleranz * 1.5:
            self.status = QualitaetsStatus.NACHARBEIT
        else:
            self.status = QualitaetsStatus.AUSSCHUSS
    
    @property
    def abweichung_prozent(self) -> float:
        """Berechnet die prozentuale Abweichung vom Sollwert"""
        if self.sollwert == 0:
            return float('inf') if self.wert != 0 else 0
        return ((self.wert - self.sollwert) / self.sollwert) * 100
    
    def to_dict(self) -> Dict[str, Any]:
        """Konvertiert den Messwert zu einem Dictionary für JSON-Serialisierung"""
        return {
            'wert': self.wert,
            'sollwert': self.sollwert,
            'toleranz': self.toleranz,
            'zeitstempel': self.zeitstempel.isoformat(),
            'operator': self.operator,
            'maschine_id': self.maschine_id,
            'status': self.status.value,
            'abweichung_prozent': self.abweichung_prozent
        }


class StatistikCalculator(ABC):
    """
    🎯 Aufgabe 2: Abstract Base Class für Statistik-Berechnungen
    
    Implementieren Sie das Strategy Pattern für verschiedene Statistik-Algorithmen
    """
    
    @abstractmethod
    def berechne_statistiken(self, werte: List[float]) -> Dict[str, float]:
        """Abstrakte Methode für Statistik-Berechnungen"""
        pass


class StandardStatistik(StatistikCalculator):
    """Standard-Statistiken (Mittelwert, Median, Standardabweichung)"""
    
    def berechne_statistiken(self, werte: List[float]) -> Dict[str, float]:
        if not werte:
            return {}
        
        return {
            'anzahl': len(werte),
            'mittelwert': statistics.mean(werte),
            'median': statistics.median(werte),
            'standardabweichung': statistics.stdev(werte) if len(werte) > 1 else 0.0,
            'minimum': min(werte),
            'maximum': max(werte),
            'spannweite': max(werte) - min(werte)
        }


class ErweiterteStatistik(StatistikCalculator):
    """Erweiterte Statistiken mit Prozessfähigkeitsindizes"""
    
    def berechne_statistiken(self, werte: List[float]) -> Dict[str, float]:
        if not werte:
            return {}
        
        basis_stats = StandardStatistik().berechne_statistiken(werte)
        
        # Erweiterte Statistiken
        basis_stats.update({
            'varianz': statistics.variance(werte) if len(werte) > 1 else 0.0,
            'schiefe': self._berechne_schiefe(werte),
            'kurtosis': self._berechne_kurtosis(werte),
            'variationskoeffizient': (basis_stats['standardabweichung'] / basis_stats['mittelwert']) * 100 if basis_stats['mittelwert'] != 0 else 0
        })
        
        return basis_stats
    
    def _berechne_schiefe(self, werte: List[float]) -> float:
        """Berechnet die Schiefe der Verteilung"""
        if len(werte) < 3:
            return 0.0
        
        mittelwert = statistics.mean(werte)
        std_abw = statistics.stdev(werte)
        
        if std_abw == 0:
            return 0.0
        
        n = len(werte)
        schiefe = sum(((x - mittelwert) / std_abw) ** 3 for x in werte) * n / ((n - 1) * (n - 2))
        return schiefe
    
    def _berechne_kurtosis(self, werte: List[float]) -> float:
        """Berechnet die Kurtosis der Verteilung"""
        if len(werte) < 4:
            return 0.0
        
        mittelwert = statistics.mean(werte)
        std_abw = statistics.stdev(werte)
        
        if std_abw == 0:
            return 0.0
        
        n = len(werte)
        kurtosis = sum(((x - mittelwert) / std_abw) ** 4 for x in werte) * n * (n + 1) / ((n - 1) * (n - 2) * (n - 3)) - 3 * (n - 1) ** 2 / ((n - 2) * (n - 3))
        return kurtosis


class ProduktionsdatenAnalyzer:
    """
    🎯 Aufgabe 3: Hauptklasse für Produktionsdaten-Analyse
    
    Implementieren Sie ein umfassendes Analysesystem mit:
    - Observer Pattern für Ereignisse
    - Decorator Pattern für Caching
    - Factory Pattern für Statistik-Algorithmen
    """
    
    def __init__(self, statistik_typ: str = "standard"):
        self.messwerte: List[Messwert] = []
        self.statistik_calculator = self._create_statistik_calculator(statistik_typ)
        self._observers: List[Callable] = []
        self._cache: Dict[str, Any] = {}
        
        logger.info(f"ProduktionsdatenAnalyzer initialisiert mit {statistik_typ} Statistik")
    
    def _create_statistik_calculator(self, typ: str) -> StatistikCalculator:
        """Factory Method für Statistik-Calculator"""
        calculators = {
            "standard": StandardStatistik,
            "erweitert": ErweiterteStatistik
        }
        
        if typ not in calculators:
            raise ValueError(f"Unbekannter Statistik-Typ: {typ}")
        
        return calculators[typ]()
    
    def add_observer(self, observer: Callable) -> None:
        """Fügt einen Observer hinzu (Observer Pattern)"""
        self._observers.append(observer)
    
    def _notify_observers(self, event: str, data: Any) -> None:
        """Benachrichtigt alle Observer über ein Ereignis"""
        for observer in self._observers:
            try:
                observer(event, data)
            except Exception as e:
                logger.error(f"Fehler beim Benachrichtigen des Observers: {e}")
    
    def add_messwert(self, messwert: Messwert) -> None:
        """Fügt einen neuen Messwert hinzu"""
        self.messwerte.append(messwert)
        self._cache.clear()  # Cache invalidieren
        
        logger.info(f"Messwert hinzugefügt: {messwert.wert} (Status: {messwert.status.value})")
        self._notify_observers("messwert_hinzugefuegt", messwert)
        
        # Qualitätsalarm bei NOK-Teilen
        if messwert.status != QualitaetsStatus.OK:
            self._notify_observers("qualitaetsalarm", messwert)
    
    def berechne_gesamtstatistiken(self) -> Dict[str, Any]:
        """Berechnet umfassende Statistiken mit Caching"""
        cache_key = "gesamtstatistiken"
        
        if cache_key in self._cache:
            logger.debug("Statistiken aus Cache geladen")
            return self._cache[cache_key]
        
        if not self.messwerte:
            return {}
        
        # Werte extrahieren
        alle_werte = [m.wert for m in self.messwerte]
        
        # Basis-Statistiken
        statistiken = self.statistik_calculator.berechne_statistiken(alle_werte)
        
        # Qualitäts-Statistiken
        status_counts = {}
        for status in QualitaetsStatus:
            status_counts[status.value] = sum(1 for m in self.messwerte if m.status == status)
        
        statistiken['qualitaets_verteilung'] = status_counts
        statistiken['ausschussquote_prozent'] = (status_counts.get('AUSSCHUSS', 0) / len(self.messwerte)) * 100
        statistiken['nacharbeitsquote_prozent'] = (status_counts.get('NACHARBEIT', 0) / len(self.messwerte)) * 100
        
        # Zeitbasierte Analyse
        if len(self.messwerte) > 1:
            zeitspanne = self.messwerte[-1].zeitstempel - self.messwerte[0].zeitstempel
            statistiken['zeitspanne_stunden'] = zeitspanne.total_seconds() / 3600
            statistiken['messrate_pro_stunde'] = len(self.messwerte) / max(statistiken['zeitspanne_stunden'], 0.001)
        
        self._cache[cache_key] = statistiken
        logger.info("Gesamtstatistiken berechnet und gecacht")
        
        return statistiken
    
    def exportiere_daten(self, dateiname: str) -> None:
        """Exportiert alle Daten als JSON"""
        export_data = {
            'export_zeitstempel': datetime.now().isoformat(),
            'anzahl_messwerte': len(self.messwerte),
            'messwerte': [m.to_dict() for m in self.messwerte],
            'statistiken': self.berechne_gesamtstatistiken()
        }
        
        with open(dateiname, 'w', encoding='utf-8') as f:
            json.dump(export_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Daten exportiert nach: {dateiname}")


def qualitaets_observer(event: str, data: Any) -> None:
    """Observer-Funktion für Qualitätsereignisse"""
    if event == "qualitaetsalarm":
        messwert = data
        print(f"🚨 QUALITÄTSALARM: {messwert.status.value} - Wert: {messwert.wert}, "
              f"Abweichung: {messwert.abweichung_prozent:.2f}%")


def main():
    """🚀 Hauptprogramm - Demonstration des Advanced-Systems"""
    print("🔴 ADVANCED: Professionelle Zahlenverarbeitung mit OOP")
    print("=" * 70)
    print("🏭 Enterprise-Level Produktionsdaten-Analysesystem")
    print()
    
    try:
        # System initialisieren
        analyzer = ProduktionsdatenAnalyzer("erweitert")
        analyzer.add_observer(qualitaets_observer)
        
        # Beispiel-Messwerte hinzufügen
        print("📊 Füge Beispiel-Messwerte hinzu...")
        beispiel_werte = [
            (2.48, "LASER_001", "Operator_A"),
            (2.52, "LASER_001", "Operator_A"),
            (2.49, "LASER_001", "Operator_B"),
            (2.51, "LASER_001", "Operator_B"),
            (2.47, "LASER_001", "Operator_A"),
            (2.58, "LASER_001", "Operator_C"),  # Ausschuss
            (2.50, "LASER_001", "Operator_A"),
        ]
        
        for wert, maschine, operator in beispiel_werte:
            messwert = Messwert(
                wert=wert,
                sollwert=2.50,
                toleranz=0.05,
                maschine_id=maschine,
                operator=operator
            )
            analyzer.add_messwert(messwert)
        
        # Statistiken berechnen und anzeigen
        print(f"\n📈 GESAMTSTATISTIKEN:")
        print("-" * 40)
        
        stats = analyzer.berechne_gesamtstatistiken()
        
        print(f"Anzahl Messungen: {stats['anzahl']}")
        print(f"Mittelwert: {stats['mittelwert']:.4f}")
        print(f"Standardabweichung: {stats['standardabweichung']:.4f}")
        print(f"Variationskoeffizient: {stats['variationskoeffizient']:.2f}%")
        print(f"Ausschussquote: {stats['ausschussquote_prozent']:.1f}%")
        print(f"Schiefe: {stats['schiefe']:.3f}")
        print(f"Kurtosis: {stats['kurtosis']:.3f}")
        
        # Daten exportieren
        export_datei = f"produktionsdaten_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        analyzer.exportiere_daten(export_datei)
        
        print(f"\n✅ Daten exportiert nach: {export_datei}")
        print("\n🎉 Advanced-Übung erfolgreich abgeschlossen!")
        print("🏆 Sie beherrschen jetzt professionelle OOP-Datenverarbeitung!")
        
    except Exception as e:
        logger.error(f"Fehler im Hauptprogramm: {e}")
        print(f"❌ Fehler: {e}")


if __name__ == "__main__":
    main()
