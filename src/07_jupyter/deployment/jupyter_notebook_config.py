# Bystronic Jupyter Notebook Configuration
# Autor: Daniel Senften

c = get_config()

# =============================================================================
# Sicherheitseinstellungen
# =============================================================================

# Token-basierte Authentifizierung
c.NotebookApp.token = "bystronic-secure-token-2024"

# Passwort-Hash (optional, zusätzlich zum Token)
# Generiert mit: from notebook.auth import passwd; passwd()
# c.NotebookApp.password = 'sha1:...'

# HTTPS-Konfiguration für Produktionsumgebung
# c.NotebookApp.certfile = '/etc/ssl/certs/jupyter.pem'
# c.NotebookApp.keyfile = '/etc/ssl/private/jupyter.key'

# =============================================================================
# Netzwerk-Konfiguration
# =============================================================================

# Alle Netzwerk-Interfaces binden
c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = 8888
c.NotebookApp.allow_remote_access = True

# CORS-Einstellungen für externe Zugriffe
c.NotebookApp.allow_origin = "*"
c.NotebookApp.allow_credentials = True

# =============================================================================
# Arbeitsverzeichnis und Dateizugriff
# =============================================================================

# Basis-Arbeitsverzeichnis
c.NotebookApp.notebook_dir = "/home/jovyan/work"

# Dateibrowser-Einstellungen
c.ContentsManager.allow_hidden = False
c.ContentsManager.hide_globs = ["__pycache__", "*.pyc", "*.pyo", ".DS_Store"]

# =============================================================================
# Kernel-Management
# =============================================================================

# Automatisches Beenden inaktiver Kernels (1 Stunde)
c.MappingKernelManager.cull_idle_timeout = 3600

# Überprüfungsintervall für inaktive Kernels (5 Minuten)
c.MappingKernelManager.cull_interval = 300

# Maximale Anzahl gleichzeitiger Kernels
c.MappingKernelManager.kernel_manager_class = (
    "notebook.services.kernels.kernelmanager.MappingKernelManager"
)

# =============================================================================
# Logging und Monitoring
# =============================================================================

# Log-Level
c.Application.log_level = "INFO"

# Log-Format
c.Application.log_format = "[%(name)s]%(highlevel)s %(message)s"

# =============================================================================
# Performance-Optimierungen
# =============================================================================

# WebSocket-Konfiguration
c.NotebookApp.tornado_settings = {
    "websocket_ping_interval": 30,
    "websocket_ping_timeout": 30,
}

# Session-Management
c.Session.key = b"bystronic-session-key-2024"

# =============================================================================
# Bystronic-spezifische Einstellungen
# =============================================================================


# Startup-Hooks für Bystronic-Umgebung
def bystronic_startup_hook():
    """Initialisierung für Bystronic-spezifische Funktionen"""
    import os
    import sys

    # Bystronic-Module zum Python-Pfad hinzufügen
    bystronic_path = "/home/jovyan/work/bystronic_modules"
    if os.path.exists(bystronic_path) and bystronic_path not in sys.path:
        sys.path.insert(0, bystronic_path)

    # Umgebungsvariablen setzen
    os.environ["BYSTRONIC_ENV"] = "production"
    os.environ["PYTHONPATH"] = os.pathsep.join(sys.path)


# Startup-Hook registrieren
c.NotebookApp.startup_hooks = [bystronic_startup_hook]

# =============================================================================
# JupyterLab-spezifische Konfiguration
# =============================================================================

# JupyterLab als Standard-Interface
c.NotebookApp.default_url = "/lab"

# JupyterLab Extensions
c.LabApp.collaborative = False
c.LabApp.news_url = None
