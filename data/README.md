# Testdaten-Verzeichnis

Dieses Verzeichnis enthält alle Testdaten für die Python-Grundkurs-Module.

## Struktur

```
data/
├── samples/           # Kleine Beispieldateien (< 10MB)
│   ├── produktionsdaten.csv
│   ├── schmutzige_daten.csv
│   └── maschinendaten_klein.csv
├── large/            # Große Dateien mit Git LFS (> 10MB)
│   └── V084_Scope.csv
└── generated/        # Automatisch generierte Dateien (ignoriert)
    ├── bereinigte_*.csv
    ├── export_*.csv
    └── *.json
```

## Git LFS Konfiguration

Große Dateien (> 10MB) werden automatisch mit Git LFS verwaltet:

- `*.csv` Dateien > 10MB
- `*.xlsx` Dateien > 5MB
- `*.json` Dateien > 5MB

## Verwendung

### Kleine Testdaten (samples/)

- Direkt in Git versioniert
- Für Lernmodule und Tests
- Schneller Zugriff ohne LFS

### Große Dateien (large/)

- Mit Git LFS verwaltet
- Für realistische Datenanalyse-Projekte
- Automatischer Download bei Bedarf

### Generierte Dateien (generated/)

- Werden durch Skripte erstellt
- In .gitignore ausgeschlossen
- Können jederzeit neu generiert werden
