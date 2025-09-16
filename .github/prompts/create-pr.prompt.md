______________________________________________________________________

## description: Erstelle einen neuen Branch, committe Änderungen und erstelle einen Pull Request mit automatischer Commit-Aufteilung category: version-control-git allowed-tools: Bash(git \*), Bash(gh \*), Bash(biome \*), Read, Glob

# Claude Command: Pull Request erstellen

Dieser Befehl erstellt automatisch einen neuen Branch, analysiert Änderungen,
teilt sie in logische Commits auf und erstellt einen professionellen Pull
Request.

Bitte darauf achten, dass alle Commit-Nachrichten und PR-Beschreibungen in
Deutsch verfasst werden.

## Verwendung

Für einen Standard-Pull-Request:

```bash
/create-pr
```

Mit Optionen:

```bash
/create-pr --draft          # Erstellt Draft-PR
/create-pr --no-format      # Überspringt Code-Formatierung
/create-pr --single-commit  # Alle Änderungen in einem Commit
/create-pr --target main    # Ziel-Branch angeben (Standard: main)
```

## Funktionalität

1. **Automatische Branch-Erstellung**:

   - Generiert aussagekräftigen Branch-Namen basierend auf Änderungen
   - Prüft auf bestehende Branches mit ähnlichen Namen
   - Erstellt Branch vom aktuellen HEAD

1. **Code-Formatierung** (ausser mit `--no-format`):

   - **JavaScript/TypeScript**: Biome Formatierung
   - **Python**: Black, isort, Ruff
   - **Java**: Google Java Format
   - **Markdown**: markdownlint, mdformat

1. **Integration mit /commit Command**:

   - Verwendet bestehende Commits oder ruft `/commit` auf
   - Respektiert bereits erstellte Commit-Struktur
   - Keine eigenständige Commit-Erstellung
   - Arbeitet mit vorhandenen Git-Commits

1. **Pull Request Erstellung**:

   - Generiert aussagekräftige PR-Titel und -Beschreibung
   - Fügt automatisch Test-Plan hinzu
   - Verlinkt relevante Issues (falls erkannt)
   - Setzt passende Labels basierend auf Änderungstyp

## Commit-Workflow Integration

### Voraussetzungen

- **Commits bereits vorhanden**: Arbeitet mit bestehenden Commits
- **Oder Aufruf von /commit**: Verwendet `/commit` für Commit-Erstellung
- **Keine doppelte Commit-Logik**: Vermeidet Konflikte mit `/commit` Command
- **Respektiert Commit-Historie**: Behält bestehende Commit-Struktur bei

### Workflow-Integration

- **Schritt 1**: Prüfe auf uncommitted Changes
- **Schritt 2**: Falls Changes vorhanden → Rufe `/commit` auf
- **Schritt 3**: Falls Commits vorhanden → Verwende diese für PR
- **Schritt 4**: Erstelle Branch und PR basierend auf Commits

## Pull Request Template

```markdown
## Beschreibung
[Kurze Beschreibung der Änderungen]

## Änderungen
- Änderung 1
- Änderung 2
- ...

## Test-Plan
- [ ] Manuelle Tests durchgeführt
- [ ] Automatische Tests laufen durch
- [ ] Code-Review bereit

## Breaking Changes
[Falls vorhanden, Breaking Changes auflisten]

## Zusätzliche Informationen
[Weitere relevante Informationen]
```

## Sicherheitshinweise

### Branch-Management

- **Eindeutige Namen**: Verhindert Konflikte mit bestehenden Branches
- **Clean Working Directory**: Stellt sicher, dass keine uncommitted Changes
  verloren gehen
- **Remote Sync**: Prüft auf neueste Änderungen im Ziel-Branch

### Code-Qualität

- **Pre-Commit-Checks**: Automatische Linting und Formatierung
- **Test-Validierung**: Stellt sicher, dass Tests vor PR-Erstellung laufen
- **Dependency-Checks**: Validiert Package-Updates und Kompatibilität

## Beispiel-Workflow

1. **Änderungen prüfen**: Erkennt uncommitted oder bereits committete Änderungen
1. **Commit-Status validieren**:
   - Falls uncommitted Changes → Rufe `/commit` auf
   - Falls Commits vorhanden → Verwende diese
1. **Branch erstellen**: `feature/neue-jupyter-widgets-2024-01-15`
1. **Code formatieren**: Biome/Black/etc. je nach Projekttyp (optional)
1. **PR erstellen**: Basierend auf vorhandenen Commits mit aussagekräftigem
   Titel und Test-Plan

## Fehlerbehebung

### Häufige Probleme

**Branch existiert bereits**:

```bash
# Automatische Lösung: Suffix wird hinzugefügt
feature/neue-widgets -> feature/neue-widgets-v2
```

**Formatierung schlägt fehl**:

```bash
# Option: --no-format verwenden
/create-pr --no-format
```

**Keine Änderungen erkannt**:

```bash
# Prüfung auf staged/unstaged changes
git status
git add .
```

**GitHub CLI nicht konfiguriert**:

```bash
# Setup erforderlich
gh auth login
```

### Troubleshooting-Befehle

```bash
# Status prüfen
git status
git branch -a

# Remote-Verbindung testen
gh auth status
gh repo view

# Letzte Commits anzeigen
git log --oneline -5
```

## Integration mit anderen Commands

### Commit-Integration

- **Automatischer `/commit` Aufruf**: Falls uncommitted Changes vorhanden
- **Respektiert `/commit` Logik**: Keine eigenständige Commit-Erstellung
- **Arbeitet mit bestehenden Commits**: Verwendet vorhandene Commit-Historie

### Command-Workflow

- **Nach `/commit`**: Verwende `/create-pr` für PR-Erstellung
- **Nach `/create-pr`**: Verwende GitHub Web-Interface für Review
- **Bei Konflikten**: Löse lokal auf, verwende `/commit`, dann `/create-pr`
  erneut

## Best Practices

### PR-Qualität

- **Aussagekräftige Titel**: Beschreibe das "Was" in 50 Zeichen
- **Detaillierte Beschreibung**: Erkläre das "Warum" und "Wie"
- **Test-Abdeckung**: Stelle sicher, dass neue Features getestet sind
- **Dokumentation**: Aktualisiere README und Docs bei Bedbedarf

### Code-Review-Vorbereitung

- **Self-Review**: Prüfe eigene Änderungen vor Submission
- **Kleine PRs**: Halte PRs fokussiert und reviewbar
- **Klare Commits**: Jeder Commit sollte eigenständig verständlich sein
