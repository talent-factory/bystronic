#!/bin/bash

# Bystronic Jupyter Development Environment Starter
# Autor: Daniel Senften

set -e

echo "🚀 Starte Bystronic Jupyter Development Environment..."

# Umgebungsvariablen für Development setzen
export ENVIRONMENT=dev
export JUPYTER_PORT=8888
export JUPYTER_TOKEN=dev-token-bystronic

# Docker-Compose für Development starten
docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d

echo "✅ Development Environment gestartet!"
echo "📊 Jupyter Lab: http://localhost:8888"
echo "🔑 Token: $JUPYTER_TOKEN"
echo ""
echo "Zum Stoppen: ./stop-dev.sh"
