#!/usr/bin/env python3
"""
Jupyter Extensions Demo für Bystronic

Demonstriert die Verwendung und Konfiguration von Jupyter Extensions.
"""

import subprocess


class JupyterExtensionManager:
    """Manager für Jupyter Extensions"""

    def __init__(self):
        self.lab_extensions = [
            "@jupyter-widgets/jupyterlab-manager",
            "@jupyterlab/toc",
            "@jupyterlab/git",
            "@jupyterlab/debugger",
            "@jupyterlab/variable-inspector",
        ]

        self.notebook_extensions = [
            "jupyter_contrib_nbextensions",
            "nbextensions_configurator",
            "jupyter_nbextensions_configurator",
        ]

    def check_extension_availability(self) -> dict[str, bool]:
        """
        Prüft verfügbare Extensions.

        Returns:
            Dictionary mit Extension-Status
        """
        status = {
            "jupyterlab_available": False,
            "notebook_available": False,
            "extensions_installed": [],
        }

        try:
            # JupyterLab verfügbar?
            result = subprocess.run(
                ["jupyter", "lab", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            status["jupyterlab_available"] = result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        try:
            # Notebook verfügbar?
            result = subprocess.run(
                ["jupyter", "notebook", "--version"],
                capture_output=True,
                text=True,
                timeout=10,
            )
            status["notebook_available"] = result.returncode == 0
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        return status

    def get_lab_extension_commands(self) -> list[str]:
        """
        Gibt Installation-Commands für JupyterLab Extensions zurück.

        Returns:
            Liste von Installationsbefehlen
        """
        commands = []

        for extension in self.lab_extensions:
            commands.append(f"jupyter labextension install {extension}")

        # Zusätzliche Konfigurationsbefehle
        commands.extend(
            [
                "jupyter labextension enable @jupyter-widgets/jupyterlab-manager",
                "jupyter lab build",
            ]
        )

        return commands

    def get_notebook_extension_commands(self) -> list[str]:
        """
        Gibt Installation-Commands für Notebook Extensions zurück.

        Returns:
            Liste von Installationsbefehlen
        """
        commands = [
            "pip install jupyter_contrib_nbextensions",
            "pip install jupyter_nbextensions_configurator",
            "jupyter contrib nbextension install --user",
            "jupyter nbextensions_configurator enable --user",
            "jupyter nbextension enable --py widgetsnbextension",
        ]

        return commands


def create_jupyter_config() -> str:
    """
    Erstellt eine Beispiel-Jupyter-Konfiguration.

    Returns:
        Konfiguration als String
    """
    config = """# jupyter_notebook_config.py - Bystronic Konfiguration
c = get_config()

# === Basis-Konfiguration ===
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False
c.NotebookApp.allow_remote_access = True

# === Sicherheit ===
c.NotebookApp.token = 'bystronic-secure-token-2024'
c.NotebookApp.password = ''  # Wird durch Token ersetzt

# === Arbeitsverzeichnis ===
c.NotebookApp.notebook_dir = '/opt/bystronic/notebooks'

# === Extensions ===
c.NotebookApp.nbserver_extensions = {
    'jupyter_nbextensions_configurator': True,
}

# === Kernel Management ===
c.MappingKernelManager.cull_idle_timeout = 3600  # 1 Stunde
c.MappingKernelManager.cull_interval = 300       # 5 Minuten
c.MappingKernelManager.cull_connected = True

# === Logging ===
c.Application.log_level = 'INFO'
c.NotebookApp.log_format = '[%(name)s]%(highlevelname)s %(message)s'

# === Content Manager ===
c.FileContentsManager.delete_to_trash = False
c.ContentsManager.allow_hidden = False

# === Terminal ===
c.NotebookApp.terminals_enabled = True
"""

    return config


def create_jupyterlab_settings() -> dict[str, dict]:
    """
    Erstellt JupyterLab Settings.

    Returns:
        Dictionary mit Settings
    """
    settings = {
        "@jupyterlab/apputils-extension:themes": {"theme": "JupyterLab Dark"},
        "@jupyterlab/notebook-extension:tracker": {
            "codeCellConfig": {
                "lineNumbers": True,
                "lineWrap": "wordWrapColumn",
                "wordWrapColumn": 80,
            }
        },
        "@jupyterlab/shortcuts-extension:shortcuts": {
            "shortcuts": [
                {
                    "command": "notebook:run-cell-and-select-next",
                    "keys": ["Shift Enter"],
                    "selector": ".jp-Notebook:focus",
                }
            ]
        },
        "@jupyterlab/terminal-extension:plugin": {
            "fontFamily": 'Monaco, Consolas, "Lucida Console", monospace',
            "fontSize": 13,
            "theme": "dark",
        },
    }

    return settings


def create_extension_test_notebook() -> dict:
    """
    Erstellt ein Test-Notebook für Extensions.

    Returns:
        Notebook als Dictionary
    """
    notebook = {
        "cells": [
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "# Extension Test Notebook\n",
                    "\n",
                    "Dieses Notebook testet verschiedene Jupyter Extensions.",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Test für Variable Inspector Extension\n",
                    "import numpy as np\n",
                    "import pandas as pd\n",
                    "\n",
                    "# Variablen für Inspector\n",
                    "test_array = np.array([1, 2, 3, 4, 5])\n",
                    "test_df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})\n",
                    "test_string = 'Bystronic Test'\n",
                    "\n",
                    "print('✅ Variablen für Inspector erstellt')",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Test für Table of Contents Extension\n",
                    "# Diese Zelle sollte im TOC erscheinen\n",
                    "\n",
                    "def test_function():\n",
                    '    """Test-Funktion für TOC"""\n',
                    '    return "TOC Test erfolgreich"\n',
                    "\n",
                    "result = test_function()\n",
                    "print(result)",
                ],
            },
            {
                "cell_type": "markdown",
                "metadata": {},
                "source": [
                    "## Git Integration Test\n",
                    "\n",
                    "Die Git-Extension sollte Änderungen in diesem Notebook verfolgen.",
                ],
            },
            {
                "cell_type": "code",
                "execution_count": None,
                "metadata": {},
                "outputs": [],
                "source": [
                    "# Debugger Extension Test\n",
                    "def debug_test_function(x, y):\n",
                    '    """Funktion zum Testen des Debuggers"""\n',
                    "    intermediate = x * 2\n",
                    "    result = intermediate + y\n",
                    "    return result\n",
                    "\n",
                    "# Breakpoint hier setzen für Debugger-Test\n",
                    "debug_result = debug_test_function(5, 3)\n",
                    "print(f'Debug-Test Ergebnis: {debug_result}')",
                ],
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3",
            },
            "language_info": {
                "codemirror_mode": {"name": "ipython", "version": 3},
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": "3.11.0",
            },
        },
        "nbformat": 4,
        "nbformat_minor": 4,
    }

    return notebook


def validate_extension_installation() -> dict[str, str]:
    """
    Validiert die Installation von Extensions.

    Returns:
        Dictionary mit Validierungsergebnissen
    """
    validation_results = {"status": "unknown", "message": "", "recommendations": []}

    try:
        # Prüfe JupyterLab Extensions
        result = subprocess.run(
            ["jupyter", "labextension", "list"],
            capture_output=True,
            text=True,
            timeout=15,
        )

        if result.returncode == 0:
            output = result.stdout

            required_extensions = [
                "@jupyter-widgets/jupyterlab-manager",
                "@jupyterlab/toc",
                "@jupyterlab/git",
            ]

            installed_extensions = []
            missing_extensions = []

            for ext in required_extensions:
                if ext in output:
                    installed_extensions.append(ext)
                else:
                    missing_extensions.append(ext)

            if len(missing_extensions) == 0:
                validation_results["status"] = "success"
                validation_results["message"] = (
                    "Alle empfohlenen Extensions installiert"
                )
            else:
                validation_results["status"] = "partial"
                validation_results["message"] = (
                    f"{len(installed_extensions)}/{len(required_extensions)} Extensions installiert"
                )
                validation_results["recommendations"] = [
                    f"Installiere fehlende Extension: {ext}"
                    for ext in missing_extensions
                ]

        else:
            validation_results["status"] = "error"
            validation_results["message"] = (
                "JupyterLab nicht verfügbar oder Fehler beim Auflisten"
            )
            validation_results["recommendations"] = [
                "Installiere JupyterLab: pip install jupyterlab"
            ]

    except (subprocess.TimeoutExpired, FileNotFoundError) as e:
        validation_results["status"] = "error"
        validation_results["message"] = f"Fehler bei Extension-Validierung: {str(e)}"
        validation_results["recommendations"] = ["Prüfe Jupyter-Installation"]

    return validation_results


if __name__ == "__main__":
    print("🔧 Jupyter Extensions Demo für Bystronic")
    print("=" * 50)

    # Extension Manager initialisieren
    manager = JupyterExtensionManager()

    # Verfügbarkeit prüfen
    status = manager.check_extension_availability()
    print(
        f"📊 JupyterLab verfügbar: {'✅' if status['jupyterlab_available'] else '❌'}"
    )
    print(f"📊 Notebook verfügbar: {'✅' if status['notebook_available'] else '❌'}")

    # Installation-Commands anzeigen
    lab_commands = manager.get_lab_extension_commands()
    print(f"\n🚀 JupyterLab Extensions ({len(lab_commands)} Befehle):")
    for cmd in lab_commands[:3]:  # Erste 3 anzeigen
        print(f"  {cmd}")

    notebook_commands = manager.get_notebook_extension_commands()
    print(f"\n📓 Notebook Extensions ({len(notebook_commands)} Befehle):")
    for cmd in notebook_commands[:3]:  # Erste 3 anzeigen
        print(f"  {cmd}")

    # Konfiguration erstellen
    config = create_jupyter_config()
    print(f"\n⚙️ Jupyter-Konfiguration erstellt ({len(config.split('\\n'))} Zeilen)")

    # JupyterLab Settings
    settings = create_jupyterlab_settings()
    print(f"🎨 JupyterLab Settings erstellt ({len(settings)} Kategorien)")

    # Test-Notebook
    test_notebook = create_extension_test_notebook()
    print(f"📝 Test-Notebook erstellt ({len(test_notebook['cells'])} Zellen)")

    # Validierung
    validation = validate_extension_installation()
    print(f"\n🔍 Extension-Validierung: {validation['status']}")
    print(f"📋 {validation['message']}")

    if validation["recommendations"]:
        print("💡 Empfehlungen:")
        for rec in validation["recommendations"]:
            print(f"  - {rec}")

    print("\n🎯 Extensions Demo abgeschlossen!")
