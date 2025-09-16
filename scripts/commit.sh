#!/bin/bash
# Einfaches Shell-Script für Git-Commits mit dem Python-Tool
# Alternative zum direkten Aufruf von commit.py

set -e

# Farben für Output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Prüfe ob Python-Script existiert
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/commit.py"

if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo -e "${RED}Fehler: commit.py nicht gefunden in $SCRIPT_DIR${NC}"
    exit 1
fi

# Prüfe ob wir in einem Git-Repository sind
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo -e "${RED}Fehler: Nicht in einem Git-Repository${NC}"
    exit 1
fi

# Prüfe ob uv verfügbar ist
if ! command -v uv &> /dev/null; then
    echo -e "${RED}Fehler: uv ist nicht installiert${NC}"
    echo -e "${YELLOW}Installiere uv mit: curl -LsSf https://astral.sh/uv/install.sh | sh${NC}"
    exit 1
fi

# Führe Python-Script aus mit allen übergebenen Argumenten
echo -e "${BLUE}Starte professionellen Git-Commit...${NC}"
python "$PYTHON_SCRIPT" "$@"
