______________________________________________________________________

## description: Automatische Markdown-Formatierung und Linting

# Automatische Markdown-Formatierung

Dieses Workflow stellt sicher, dass alle Markdown-Dateien automatisch korrekt
formatiert werden.

## 1. Pre-commit Hooks installieren

```bash
uv run pre-commit install
```

## 2. Markdown-Dateien automatisch formatieren

```bash
# Alle Markdown-Dateien formatieren
uv run pre-commit run markdownlint --all-files
uv run pre-commit run mdformat --all-files
```

## 3. Einzelne Datei formatieren

```bash
# Spezifische Datei
uv run pre-commit run markdownlint --files path/to/file.md
uv run pre-commit run mdformat --files path/to/file.md
```

## 4. Vor jedem Commit automatisch

Die pre-commit hooks laufen automatisch bei jedem `git commit` und:

- Korrigieren MD032 (Listen mit Leerzeilen umgeben)
- Korrigieren MD022 (Überschriften mit Leerzeilen umgeben)
- Korrigieren MD031 (Code-Blöcke mit Leerzeilen umgeben)
- Formatieren Zeilenlänge auf 80 Zeichen
- Standardisieren Tabellen-Formatierung

## 5. Manuelle Formatierung überspringen

```bash
# Commit ohne pre-commit hooks
git commit --no-verify -m "message"
```

## Konfiguration

- `.markdownlint.json` - Linting-Regeln
- `.pre-commit-config.yaml` - Hook-Konfiguration
- Automatische Formatierung bei jedem Commit
