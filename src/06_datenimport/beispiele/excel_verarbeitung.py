#!/usr/bin/env python3
"""
Excel Verarbeitung

Umfassende Excel-Import/Export-Funktionen für Bystronic-Anwendungen.
Behandelt mehrere Arbeitsblätter, Formatierung und komplexe Strukturen.

Autor: Python Grundkurs Bystronic
"""

import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import warnings

warnings.filterwarnings('ignore')


def get_data_path(*args):
    """
    Hilfsfunktion zum korrekten Konstruieren der Datenpfade
    """
    project_root = Path(__file__).parent.parent.parent.parent
    data_path = project_root / "data"
    for arg in args:
        data_path = data_path / arg
    return data_path


class BystronicExcelHandler:
    """
    Klasse für die Verarbeitung von Excel-Dateien in Bystronic-Umgebung
    """
    
    def __init__(self):
        self.loaded_data = {}
        self.processing_log = []
    
    def log_action(self, message):
        """Protokolliert Aktionen"""
        timestamp = datetime.now().strftime('%H:%M:%S')
        log_entry = f"[{timestamp}] {message}"
        self.processing_log.append(log_entry)
        print(log_entry)
    
    def create_sample_workbook(self, file_path: str):
        """
        Erstellt eine umfassende Excel-Arbeitsmappe als Beispiel
        """
        self.log_action(f"Erstelle Beispiel-Arbeitsmappe: {file_path}")
        
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        
        with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
            
            # Arbeitsblatt 1: Tagesproduktion
            self.log_action("Generiere Tagesproduktionsdaten")
            dates = pd.date_range('2024-01-01', '2024-03-31', freq='D')
            production_data = pd.DataFrame({
                'Datum': dates,
                'Maschine_A': np.random.randint(800, 1200, len(dates)),
                'Maschine_B': np.random.randint(600, 1000, len(dates)),
                'Maschine_C': np.random.randint(900, 1300, len(dates)),
                'Schicht_1': np.random.randint(300, 500, len(dates)),
                'Schicht_2': np.random.randint(350, 550, len(dates)),
                'Schicht_3': np.random.randint(200, 400, len(dates)),
                'Wochentag': dates.day_name(),
                'Monat': dates.month_name(),
                'Gesamt': lambda x: x['Maschine_A'] + x['Maschine_B'] + x['Maschine_C']
            })
            production_data['Gesamt'] = (production_data['Maschine_A'] + 
                                       production_data['Maschine_B'] + 
                                       production_data['Maschine_C'])
            production_data.to_excel(writer, sheet_name='Tagesproduktion', index=False)
            
            # Arbeitsblatt 2: Qualitätsdaten
            self.log_action("Generiere Qualitätsdaten")
            quality_data = pd.DataFrame({
                'Monat': pd.date_range('2024-01-01', '2024-12-01', freq='M'),
                'Gesamtproduktion': np.random.randint(25000, 35000, 12),
                'Ausschuss_Anzahl': np.random.randint(100, 800, 12),
                'Ausschuss_Rate_%': np.random.uniform(0.5, 2.5, 12),
                'Nacharbeit_Anzahl': np.random.randint(50, 300, 12),
                'Nacharbeit_Rate_%': np.random.uniform(0.2, 1.2, 12),
                'Kundenbeschwerden': np.random.poisson(3, 12),
                'Kundenzufriedenheit': np.random.uniform(3.5, 4.8, 12),
                'Qualitätsscore': np.random.uniform(85, 98, 12)
            })
            quality_data.to_excel(writer, sheet_name='Qualität', index=False)
            
            # Arbeitsblatt 3: Wartungsplan
            self.log_action("Generiere Wartungsdaten")
            machines = ['Laser_A', 'Laser_B', 'Press_C', 'Press_D', 'Robot_E']
            maintenance_data = []
            
            for machine in machines:
                for month in range(1, 13):
                    maintenance_data.append({
                        'Maschine': machine,
                        'Monat': month,
                        'Präventive_Wartungen': np.random.randint(2, 6),
                        'Korrektive_Wartungen': np.random.randint(0, 3),
                        'Wartungszeit_h': np.random.uniform(4, 24),
                        'Wartungskosten_EUR': np.random.uniform(500, 5000),
                        'Ausfallzeit_h': np.random.uniform(0, 8),
                        'Ersatzteile_EUR': np.random.uniform(100, 2000)
                    })
            
            maintenance_df = pd.DataFrame(maintenance_data)
            maintenance_df.to_excel(writer, sheet_name='Wartung', index=False)
            
            # Arbeitsblatt 4: Maschinenparameter
            self.log_action("Generiere Maschinenparameter")
            parameters = [
                'Laser_Leistung_W', 'Schnittgeschwindigkeit_mm/min', 'Vorschub_mm/min',
                'Arbeitsdruck_bar', 'Kühlmitteltemperatur_C', 'Positionsgenauigkeit_mm',
                'Wiederholgenauigkeit_mm', 'Max_Materialdicke_mm'
            ]
            
            machine_params = pd.DataFrame({
                'Parameter': parameters,
                'Laser_A': [6000, 2500, 8000, 12, 20, 0.05, 0.02, 25],
                'Laser_B': [5500, 2200, 7500, 11, 22, 0.08, 0.03, 20],
                'Press_C': [0, 800, 0, 200, 25, 0.1, 0.05, 50],
                'Press_D': [0, 900, 0, 180, 23, 0.12, 0.04, 40],
                'Robot_E': [0, 1200, 500, 6, 18, 0.5, 0.2, 0],
                'Einheit': ['W', 'mm/min', 'mm/min', 'bar', '°C', 'mm', 'mm', 'mm'],
                'Toleranz_%': [5, 10, 15, 8, 10, 20, 25, 0]
            })
            machine_params.to_excel(writer, sheet_name='Parameter', index=False)
            
            # Arbeitsblatt 5: Energieverbrauch
            self.log_action("Generiere Energieverbrauchsdaten")
            hours = pd.date_range('2024-01-01', '2024-01-07 23:00:00', freq='H')
            energy_data = pd.DataFrame({
                'Timestamp': hours,
                'Gesamt_kW': np.random.uniform(50, 200, len(hours)),
                'Laser_A_kW': np.random.uniform(15, 60, len(hours)),
                'Laser_B_kW': np.random.uniform(12, 55, len(hours)),
                'Press_C_kW': np.random.uniform(10, 40, len(hours)),
                'Press_D_kW': np.random.uniform(8, 35, len(hours)),
                'Robot_E_kW': np.random.uniform(3, 15, len(hours)),
                'Beleuchtung_kW': np.random.uniform(5, 12, len(hours)),
                'Klimaanlage_kW': np.random.uniform(8, 25, len(hours)),
                'Stundentarif_EUR/kWh': np.random.uniform(0.15, 0.35, len(hours))
            })
            energy_data.to_excel(writer, sheet_name='Energie', index=False)
        
        file_size = Path(file_path).stat().st_size / 1024
        self.log_action(f"Arbeitsmappe erstellt: {file_size:.1f} KB")
        return file_path
    
    def load_excel_comprehensive(self, file_path: str):
        """
        Lädt eine Excel-Datei mit allen Arbeitsblättern
        """
        self.log_action(f"Lade Excel-Datei: {file_path}")
        
        try:
            # Alle Arbeitsblätter laden
            excel_data = pd.read_excel(file_path, sheet_name=None)
            
            self.log_action(f"Arbeitsblätter gefunden: {list(excel_data.keys())}")
            
            # Daten speichern und analysieren
            for sheet_name, df in excel_data.items():
                self.loaded_data[sheet_name] = df
                
                # Basis-Analyse
                numeric_cols = len(df.select_dtypes(include=[np.number]).columns)
                date_cols = len(df.select_dtypes(include=['datetime64']).columns)
                
                self.log_action(f"  {sheet_name}: {df.shape[0]} Zeilen × {df.shape[1]} Spalten "
                              f"({numeric_cols} numerisch, {date_cols} Datum)")
            
            return excel_data
            
        except Exception as e:
            self.log_action(f"Fehler beim Excel-Import: {e}")
            return None
    
    def analyze_workbook_structure(self, excel_data):
        """
        Analysiert die Struktur der geladenen Arbeitsmappe
        """
        self.log_action("Analysiere Arbeitsmappe-Struktur")
        
        structure_info = {
            'total_sheets': len(excel_data),
            'total_rows': sum(len(df) for df in excel_data.values()),
            'total_columns': sum(len(df.columns) for df in excel_data.values()),
            'sheets_info': {}
        }
        
        for sheet_name, df in excel_data.items():
            # Datentyp-Analyse
            dtypes_summary = df.dtypes.value_counts().to_dict()
            
            # Fehlende Werte
            missing_values = df.isnull().sum().sum()
            
            # Speicher-Verbrauch
            memory_usage = df.memory_usage(deep=True).sum() / 1024  # KB
            
            sheet_info = {
                'rows': len(df),
                'columns': len(df.columns),
                'dtypes': dtypes_summary,
                'missing_values': missing_values,
                'memory_kb': round(memory_usage, 1),
                'sample_columns': list(df.columns[:5])
            }
            
            structure_info['sheets_info'][sheet_name] = sheet_info
        
        # Zusammenfassung ausgeben
        print(f"\n📊 Arbeitsmappe-Analyse:")
        print(f"  Arbeitsblätter: {structure_info['total_sheets']}")
        print(f"  Gesamt Zeilen: {structure_info['total_rows']:,}")
        print(f"  Gesamt Spalten: {structure_info['total_columns']}")
        
        for sheet_name, info in structure_info['sheets_info'].items():
            print(f"  📋 {sheet_name}:")
            print(f"    - Dimension: {info['rows']} × {info['columns']}")
            print(f"    - Fehlende Werte: {info['missing_values']}")
            print(f"    - Speicher: {info['memory_kb']} KB")
            print(f"    - Beispiel-Spalten: {', '.join(info['sample_columns'])}")
        
        return structure_info
    
    def create_pivot_analysis(self, data_dict):
        """
        Erstellt Pivot-Analysen aus den geladenen Daten
        """
        self.log_action("Erstelle Pivot-Analysen")
        
        pivot_results = {}
        
        # Analyse 1: Tagesproduktion nach Wochentag
        if 'Tagesproduktion' in data_dict:
            df_prod = data_dict['Tagesproduktion'].copy()
            
            # Monatsproduktion nach Maschine
            monthly_pivot = pd.pivot_table(
                df_prod,
                values=['Maschine_A', 'Maschine_B', 'Maschine_C'],
                index=df_prod['Datum'].dt.month,
                aggfunc='sum'
            )
            monthly_pivot.index.name = 'Monat'
            pivot_results['Monatsproduktion'] = monthly_pivot
            
            # Wochentagsanalyse
            weekday_pivot = pd.pivot_table(
                df_prod,
                values='Gesamt',
                index='Wochentag',
                aggfunc=['mean', 'sum', 'count']
            )
            pivot_results['Wochentag_Analyse'] = weekday_pivot
        
        # Analyse 2: Qualitäts-Trends
        if 'Qualität' in data_dict:
            df_quality = data_dict['Qualität'].copy()
            df_quality['Quartal'] = df_quality['Monat'].dt.quarter
            
            quality_pivot = pd.pivot_table(
                df_quality,
                values=['Ausschuss_Rate_%', 'Nacharbeit_Rate_%', 'Qualitätsscore'],
                index='Quartal',
                aggfunc='mean'
            )
            pivot_results['Qualitäts_Quartale'] = quality_pivot
        
        # Analyse 3: Wartungskosten nach Maschine
        if 'Wartung' in data_dict:
            df_maint = data_dict['Wartung'].copy()
            
            maintenance_pivot = pd.pivot_table(
                df_maint,
                values=['Wartungskosten_EUR', 'Ausfallzeit_h', 'Wartungszeit_h'],
                index='Maschine',
                aggfunc=['sum', 'mean']
            )
            pivot_results['Wartungsanalyse'] = maintenance_pivot
        
        # Ergebnisse anzeigen
        for analysis_name, pivot_df in pivot_results.items():
            print(f"\n📊 {analysis_name}:")
            print(pivot_df.round(2))
        
        return pivot_results
    
    def export_enhanced_workbook(self, output_path: str, include_charts: bool = True):
        """
        Exportiert eine erweiterte Arbeitsmappe mit Analysen
        """
        self.log_action(f"Exportiere erweiterte Arbeitsmappe: {output_path}")
        
        if not self.loaded_data:
            self.log_action("Keine Daten zum Exportieren verfügbar")
            return False
        
        try:
            with pd.ExcelWriter(output_path, engine='openpyxl') as writer:
                
                # Originaldaten exportieren
                for sheet_name, df in self.loaded_data.items():
                    df.to_excel(writer, sheet_name=f"Original_{sheet_name}", index=False)
                
                # Zusammenfassungen erstellen
                if 'Tagesproduktion' in self.loaded_data:
                    df_prod = self.loaded_data['Tagesproduktion']
                    
                    # Monatszusammenfassung
                    monthly_summary = df_prod.groupby(df_prod['Datum'].dt.month).agg({
                        'Maschine_A': ['sum', 'mean'],
                        'Maschine_B': ['sum', 'mean'],
                        'Maschine_C': ['sum', 'mean'],
                        'Gesamt': ['sum', 'mean', 'max', 'min']
                    }).round(2)
                    monthly_summary.to_excel(writer, sheet_name='Monatszusammenfassung')
                    
                    # Top/Flop Tage
                    top_days = df_prod.nlargest(10, 'Gesamt')[['Datum', 'Gesamt', 'Wochentag']]
                    flop_days = df_prod.nsmallest(10, 'Gesamt')[['Datum', 'Gesamt', 'Wochentag']]
                    
                    performance_df = pd.DataFrame({
                        'Kategorie': ['Top Tage'] * 10 + ['Flop Tage'] * 10,
                        'Datum': list(top_days['Datum']) + list(flop_days['Datum']),
                        'Produktion': list(top_days['Gesamt']) + list(flop_days['Gesamt']),
                        'Wochentag': list(top_days['Wochentag']) + list(flop_days['Wochentag'])
                    })
                    performance_df.to_excel(writer, sheet_name='Performance_Ranking', index=False)
                
                # KPIs und Metriken
                kpis = self.calculate_kpis()
                if kpis:
                    kpi_df = pd.DataFrame(list(kpis.items()), columns=['KPI', 'Wert'])
                    kpi_df.to_excel(writer, sheet_name='KPIs', index=False)
                
                # Verarbeitungsprotokoll
                log_df = pd.DataFrame(self.processing_log, columns=['Log_Eintrag'])
                log_df.to_excel(writer, sheet_name='Verarbeitungsprotokoll', index=False)
            
            file_size = Path(output_path).stat().st_size / 1024
            self.log_action(f"Export erfolgreich: {file_size:.1f} KB")
            return True
            
        except Exception as e:
            self.log_action(f"Export-Fehler: {e}")
            return False
    
    def calculate_kpis(self):
        """
        Berechnet wichtige KPIs aus den geladenen Daten
        """
        kpis = {}
        
        if 'Tagesproduktion' in self.loaded_data:
            df_prod = self.loaded_data['Tagesproduktion']
            
            kpis['Gesamtproduktion'] = f"{df_prod['Gesamt'].sum():,}"
            kpis['Ø_Tagesproduktion'] = f"{df_prod['Gesamt'].mean():.0f}"
            kpis['Beste_Tagesleistung'] = f"{df_prod['Gesamt'].max():,}"
            kpis['Produktivster_Wochentag'] = df_prod.groupby('Wochentag')['Gesamt'].mean().idxmax()
        
        if 'Qualität' in self.loaded_data:
            df_qual = self.loaded_data['Qualität']
            
            kpis['Ø_Ausschussrate'] = f"{df_qual['Ausschuss_Rate_%'].mean():.2f}%"
            kpis['Ø_Nacharbeitrate'] = f"{df_qual['Nacharbeit_Rate_%'].mean():.2f}%"
            kpis['Ø_Kundenzufriedenheit'] = f"{df_qual['Kundenzufriedenheit'].mean():.2f}"
        
        if 'Wartung' in self.loaded_data:
            df_maint = self.loaded_data['Wartung']
            
            kpis['Gesamt_Wartungskosten'] = f"{df_maint['Wartungskosten_EUR'].sum():,.0f} €"
            kpis['Ø_Ausfallzeit_pro_Wartung'] = f"{df_maint['Ausfallzeit_h'].mean():.1f}h"
            kpis['Wartungsintensivste_Maschine'] = df_maint.groupby('Maschine')['Wartungskosten_EUR'].sum().idxmax()
        
        return kpis
    
    def visualize_excel_data(self):
        """
        Erstellt Visualisierungen der Excel-Daten
        """
        if not self.loaded_data:
            print("Keine Daten für Visualisierung verfügbar")
            return
        
        fig, axes = plt.subplots(2, 3, figsize=(20, 12))
        fig.suptitle('Excel Datenanalyse - Bystronic Dashboard', fontsize=16)
        
        # Plot 1: Monatsproduktion
        if 'Tagesproduktion' in self.loaded_data:
            df_prod = self.loaded_data['Tagesproduktion']
            monthly_prod = df_prod.groupby(df_prod['Datum'].dt.month)[['Maschine_A', 'Maschine_B', 'Maschine_C']].sum()
            
            monthly_prod.plot(kind='bar', ax=axes[0,0], width=0.8)
            axes[0,0].set_title('Monatsproduktion pro Maschine')
            axes[0,0].set_ylabel('Stück')
            axes[0,0].legend()
            axes[0,0].tick_params(axis='x', rotation=0)
        
        # Plot 2: Qualitätstrend
        if 'Qualität' in self.loaded_data:
            df_qual = self.loaded_data['Qualität']
            axes[0,1].plot(df_qual['Monat'], df_qual['Ausschuss_Rate_%'], 'o-', label='Ausschuss %')
            axes[0,1].plot(df_qual['Monat'], df_qual['Nacharbeit_Rate_%'], 's-', label='Nacharbeit %')
            axes[0,1].set_title('Qualitätstrends')
            axes[0,1].set_ylabel('Prozent')
            axes[0,1].legend()
            axes[0,1].tick_params(axis='x', rotation=45)
        
        # Plot 3: Wartungskosten
        if 'Wartung' in self.loaded_data:
            df_maint = self.loaded_data['Wartung']
            maint_by_machine = df_maint.groupby('Maschine')['Wartungskosten_EUR'].sum()
            
            axes[0,2].pie(maint_by_machine.values, labels=maint_by_machine.index, autopct='%1.1f%%')
            axes[0,2].set_title('Wartungskosten pro Maschine')
        
        # Plot 4: Wochentagsanalyse
        if 'Tagesproduktion' in self.loaded_data:
            weekday_avg = df_prod.groupby('Wochentag')['Gesamt'].mean()
            # Richtige Reihenfolge der Wochentage
            weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            weekday_avg = weekday_avg.reindex(weekday_order)
            
            axes[1,0].bar(range(len(weekday_avg)), weekday_avg.values, 
                         color=['lightblue' if day in ['Saturday', 'Sunday'] else 'steelblue' 
                               for day in weekday_avg.index])
            axes[1,0].set_title('Durchschnittliche Tagesproduktion nach Wochentag')
            axes[1,0].set_ylabel('Stück')
            axes[1,0].set_xticks(range(len(weekday_avg)))
            axes[1,0].set_xticklabels([day[:3] for day in weekday_avg.index])
        
        # Plot 5: Energieverbrauch (falls verfügbar)
        if 'Energie' in self.loaded_data:
            df_energy = self.loaded_data['Energie']
            daily_energy = df_energy.groupby(df_energy['Timestamp'].dt.date)['Gesamt_kW'].sum()
            
            axes[1,1].plot(daily_energy.index, daily_energy.values, 'g-', alpha=0.7)
            axes[1,1].set_title('Täglicher Energieverbrauch')
            axes[1,1].set_ylabel('kWh')
            axes[1,1].tick_params(axis='x', rotation=45)
        
        # Plot 6: Parameter-Heatmap
        if 'Parameter' in self.loaded_data:
            df_params = self.loaded_data['Parameter'].set_index('Parameter')
            numeric_params = df_params.select_dtypes(include=[np.number]).iloc[:, :5]  # Erste 5 numerische Spalten
            
            im = axes[1,2].imshow(numeric_params.values, cmap='viridis', aspect='auto')
            axes[1,2].set_title('Maschinenparameter Heatmap')
            axes[1,2].set_xticks(range(len(numeric_params.columns)))
            axes[1,2].set_xticklabels(numeric_params.columns, rotation=45)
            axes[1,2].set_yticks(range(len(numeric_params.index)))
            axes[1,2].set_yticklabels(numeric_params.index)
            
            # Colorbar
            plt.colorbar(im, ax=axes[1,2])
        
        plt.tight_layout()
        plt.show()


def main():
    """
    Hauptfunktion - demonstriert Excel-Verarbeitung
    """
    print("📊 Excel Verarbeitung - Comprehensive Demo")
    print("=" * 50)
    
    # Excel Handler initialisieren
    excel_handler = BystronicExcelHandler()
    
    # Beispiel-Arbeitsmappe erstellen
    sample_file = get_data_path("examples", "bystronic_comprehensive.xlsx")
    excel_handler.create_sample_workbook(sample_file)
    
    # Excel-Datei laden
    excel_data = excel_handler.load_excel_comprehensive(sample_file)
    
    if excel_data:
        # Struktur analysieren
        structure = excel_handler.analyze_workbook_structure(excel_data)
        
        # Pivot-Analysen erstellen
        pivot_analyses = excel_handler.create_pivot_analysis(excel_data)
        
        # KPIs berechnen
        kpis = excel_handler.calculate_kpis()
        
        print(f"\n📊 Wichtige KPIs:")
        for kpi, value in kpis.items():
            print(f"  {kpi}: {value}")
        
        # Erweiterte Arbeitsmappe exportieren
        enhanced_file = get_data_path("examples", "bystronic_enhanced.xlsx")
        success = excel_handler.export_enhanced_workbook(enhanced_file)
        
        if success:
            print(f"\n✅ Erweiterte Arbeitsmappe exportiert: {enhanced_file}")
        
        # Visualisierung
        excel_handler.visualize_excel_data()
        
        print("\n🎉 Excel-Verarbeitung abgeschlossen!")
        print("\n💡 Wichtige Erkenntnisse:")
        print("  • Excel eignet sich hervorragend für strukturierte Daten")
        print("  • Mehrere Arbeitsblätter ermöglichen thematische Trennung")
        print("  • Pivot-Tabellen bieten mächtige Analyse-Möglichkeiten")
        print("  • KPIs lassen sich automatisch berechnen und aktualisieren")
        print("  • Visualisierungen helfen bei der Dateninterpretation")
    
    else:
        print("❌ Excel-Verarbeitung fehlgeschlagen")


if __name__ == "__main__":
    main()