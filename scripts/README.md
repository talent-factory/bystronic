# Scripts für Bystronic Python-Projekt

Dieses Verzeichnis enthält Hilfsskripte für das Bystronic Python-Projekt.

## Verfügbare Scripts

### `commit.py` - Professioneller Git-Commit

Ein umfassendes Python-Script für professionelle Git-Commits mit automatischen
Qualitätschecks.

**Verwendung:**

```bash
# Standard-Commit
python scripts/commit.py

# Mit Optionen
python scripts/commit.py --no-verify    # Ohne Pre-Commit-Checks
python scripts/commit.py --skip-tests   # Ohne Tests
python scripts/commit.py --force-push   # Mit automatischem Force-Push
```

**Features:**

- Automatische Pre-Commit-Checks (Ruff, Black, MyPy, pytest)
- Intelligente Staging-Verwaltung
- Konventionelle Commit-Nachrichten mit Emojis (auf Deutsch)
- Diff-Analyse und automatische Commit-Typ-Erkennung
- Optional: Automatischer Push zum Remote-Repository

### `commit.sh` - Shell-Wrapper

Ein einfaches Shell-Script als Alternative zum direkten Python-Aufruf.

**Verwendung:**

```bash
# Standard-Commit
./scripts/commit.sh

# Mit Optionen (werden an commit.py weitergegeben)
./scripts/commit.sh --no-verify
```

## Integration mit Makefile

Die Scripts sind in das Makefile integriert:

```bash
make commit              # Standard-Commit
make commit-no-verify    # Ohne Pre-Commit-Checks
make commit-skip-tests   # Ohne Tests
make commit-force        # Mit automatischem Force-Push
```

## Dokumentation

Siehe `docs/commit-guide.md` für eine ausführliche Anleitung.

## Voraussetzungen

- Python 3.13+
- uv Package Manager
- Git Repository
- Alle Projekt-Dependencies installiert (`uv sync --extra dev`)

## Anpassungen

Die Scripts können nach Bedarf angepasst werden:

- Neue Commit-Typen in `commit.py` hinzufügen
- Andere Linting-Tools integrieren
- Commit-Nachricht-Format ändern
- Zusätzliche Checks hinzufügen
