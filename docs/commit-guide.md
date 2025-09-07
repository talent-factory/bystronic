# Git-Commit-Guide für Bystronic Python-Projekt

## Übersicht

Das Bystronic Python-Projekt verfügt über ein professionelles Git-Commit-System
mit automatischen Qualitätschecks und konventionellen Commit-Nachrichten auf
Deutsch.

## Schnellstart

### Mit Makefile (empfohlen)

```bash
# Standard-Commit mit allen Checks
make commit

# Commit ohne Pre-Commit-Checks
make commit-no-verify

# Commit ohne Tests (für schnelle Fixes)
make commit-skip-tests

# Commit mit automatischem Force-Push (Vorsicht!)
make commit-force
```

### Direkt mit Python

```bash
# Standard-Commit
python scripts/commit.py

# Mit Optionen
python scripts/commit.py --no-verify
python scripts/commit.py --skip-tests
python scripts/commit.py --force-push
```

### Mit Shell-Script

```bash
# Standard-Commit
./scripts/commit.sh

# Mit Optionen
./scripts/commit.sh --no-verify
```

## Funktionalität

### 1. Automatische Pre-Commit-Checks

Das System führt folgende Checks automatisch aus:

- **Ruff Linting**: Prüft Code-Qualität und Style
- **Black Formatierung**: Formatiert Code automatisch
- **MyPy Type Checking**: Prüft Typen (Warnungen sind nicht kritisch)
- **Pytest Tests**: Führt alle Tests aus

### 2. Intelligente Staging-Verwaltung

- Prüft `git status` auf gestakte Dateien
- Fügt automatisch alle Änderungen hinzu, falls nichts gestakt ist
- Zeigt Übersicht der zu committenden Dateien

### 3. Diff-Analyse und Commit-Optimierung

- Analysiert `git diff --cached` um Änderungstyp zu bestimmen
- Erkennt automatisch den passenden Commit-Typ
- Erstellt aussagekräftige Commit-Nachrichten

### 4. Konventionelle Commit-Nachrichten

Das System verwendet Emoji Conventional Commits auf Deutsch:

| Typ        | Emoji | Beschreibung                        |
| ---------- | ----- | ----------------------------------- |
| `feat`     | ✨    | Neue Funktionalität                 |
| `fix`      | 🐛    | Fehlerbehebung                      |
| `docs`     | 📚    | Dokumentationsänderungen            |
| `style`    | 💎    | Code-Formatierung                   |
| `refactor` | ♻️    | Code-Umstrukturierung               |
| `perf`     | ⚡    | Performance-Verbesserungen          |
| `test`     | 🧪    | Tests hinzufügen oder korrigieren   |
| `chore`    | 🔧    | Build-Prozess, Tools, Konfiguration |
| `ci`       | 🚀    | Continuous Integration Änderungen   |
| `security` | 🔒    | Sicherheitsverbesserungen           |
| `deps`     | 📦    | Dependency-Updates                  |

## Beispiel-Workflow

1. **Änderungen machen**: Bearbeite Dateien in `src/`, `tests/`, etc.
1. **Commit starten**: `make commit`
1. **Automatische Checks**: System führt Linting, Formatierung und Tests aus
1. **Commit-Nachricht**: System generiert professionelle Nachricht
1. **Bestätigung**: Du bestätigst die Commit-Nachricht
1. **Push-Option**: Optional Push zum Remote-Repository

## Beispiel-Commit-Nachrichten

```
✨ feat: Füge neue Datenanalyse-Funktionen hinzu

Typ: Neue Funktionalität
Geänderte Dateien: 3

Dateien:
- src/04_pandas/datenanalyse.py
- tests/test_04_pandas.py
- docs/pandas-guide.md
```

```
🐛 fix: Behebe Import-Fehler in Visualisierung

Typ: Fehlerbehebung
Geänderte Dateien: 1

Dateien:
- src/05_visualisierung/matplotlib_beispiele.py
```

```
📦 deps: Aktualisiere Python-Dependencies

Typ: Dependency-Updates
Geänderte Dateien: 2

Dateien:
- pyproject.toml
- uv.lock
```

## Optionen

### `--no-verify`

Überspringt alle Pre-Commit-Checks. Nützlich für:

- Schnelle Fixes
- Work-in-Progress Commits
- Notfall-Commits

### `--skip-tests`

Überspringt nur die Testausführung, führt aber Linting und Formatierung aus.
Nützlich für:

- Dokumentationsänderungen
- Konfigurationsänderungen
- Wenn Tests lange dauern

### `--force-push`

Führt automatisch einen Force-Push aus. **Vorsicht!** Nur verwenden wenn:

- Du allein am Branch arbeitest
- Du weißt was du tust
- Es sich um einen Feature-Branch handelt

## Fehlerbehebung

### Ruff-Linting-Fehler

Das System versucht automatische Fixes:

```bash
# Manuelle Fixes
uv run ruff check --fix src/
```

### Black-Formatierung

Wird automatisch angewendet:

```bash
# Manuell formatieren
uv run black src/
```

### Test-Fehler

Tests müssen manuell behoben werden:

```bash
# Tests einzeln ausführen
uv run pytest tests/test_specific.py -v
```

### MyPy-Warnungen

Sind nicht kritisch, aber sollten behoben werden:

```bash
# MyPy manuell ausführen
uv run mypy src/
```

## Integration mit IDE

### VS Code

Füge zu `.vscode/tasks.json` hinzu:

```json
{
    "label": "Git Commit",
    "type": "shell",
    "command": "make commit",
    "group": "build",
    "presentation": {
        "echo": true,
        "reveal": "always",
        "focus": false,
        "panel": "shared"
    }
}
```

### Terminal-Alias

Füge zu `.bashrc` oder `.zshrc` hinzu:

```bash
alias gcommit='make commit'
alias gcommit-fast='make commit-skip-tests'
```

## Best Practices

1. **Kleine, atomare Commits**: Jeder Commit sollte eine logische Einheit sein
1. **Aussagekräftige Nachrichten**: Das System hilft dabei, aber prüfe die
   Nachricht
1. **Tests vor Commit**: Lass die Tests laufen, außer bei Dokumentation
1. **Regelmäßige Commits**: Committe oft, aber nur funktionierende Zustände
1. **Branch-Strategie**: Verwende Feature-Branches für größere Änderungen

## Anpassungen

Das System kann in `scripts/commit.py` angepasst werden:

- Neue Commit-Typen hinzufügen
- Andere Linting-Tools integrieren
- Commit-Nachricht-Format ändern
- Zusätzliche Checks hinzufügen
