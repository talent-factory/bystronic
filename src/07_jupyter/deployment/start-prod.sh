# SmartFactory Jupyter Production Environment Starter
# Autor: Daniel Senften

set -e

echo "🏭 Starte SmartFactory Jupyter Production Environment..."

# Umgebungsvariablen für Production setzen
export ENVIRONMENT=prod
export JUPYTER_PORT=8888
export NGINX_PORT=80
export NGINX_SSL_PORT=443
export SSL_CERT_PATH=./ssl/certs

# SSL-Zertifikate prüfen
if [ ! -f "$SSL_CERT_PATH/jupyter.pem" ]; then
    echo "⚠️  SSL-Zertifikat nicht gefunden. Erstelle selbstsigniertes Zertifikat..."
    mkdir -p $SSL_CERT_PATH
    openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
        -keyout $SSL_CERT_PATH/jupyter.key \
        -out $SSL_CERT_PATH/jupyter.pem \
        -subj "/C=CH/ST=Bern/L=Niederönz/O=SmartFactory/CN=jupyter.smartfactory.local"
    echo "✅ SSL-Zertifikat erstellt"
fi

# Docker-Compose für Production starten
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

echo "✅ Production Environment gestartet!"
echo "🔒 Jupyter Lab (HTTPS): https://localhost:443"
echo "📊 Jupyter Lab (HTTP): http://localhost:80"
echo "🏢 JupyterHub: http://localhost:8000"
echo ""
echo "Zum Stoppen: ./stop-prod.sh"
