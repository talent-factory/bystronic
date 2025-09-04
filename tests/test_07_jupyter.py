#!/usr/bin/env python3
"""
Tests für 07_jupyter/beispiele

Diese Tests validieren die Funktionalität der Jupyter-Beispiele
und demonstrieren Test-Patterns für Notebook-Code.
"""

import json
import subprocess
import sys
from pathlib import Path
from unittest.mock import patch

import pandas as pd
import pytest

# Pfad zu den Beispielen hinzufügen
beispiele_path = Path(__file__).parent.parent / "src" / "07_jupyter" / "beispiele"
sys.path.insert(0, str(beispiele_path))

import jupyter_extensions_demo
import jupyter_widgets_demo


class TestJupyterWidgetsDemo:
    """Tests für jupyter_widgets_demo.py"""

    def test_module_imports_successfully(self):
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert jupyter_widgets_demo is not None

    def test_create_sample_machine_data(self):
        """Testet die Erstellung von Beispiel-Maschinendaten"""
        # Standard-Datensatz
        data = jupyter_widgets_demo.create_sample_machine_data(100)

        assert isinstance(data, pd.DataFrame)
        assert len(data) == 100
        assert list(data.columns) == [
            "Maschine",
            "Temperatur",
            "Effizienz",
            "Produktionszeit",
            "Status",
        ]

        # Datentypen prüfen
        assert data["Maschine"].dtype == "object"
        assert pd.api.types.is_numeric_dtype(data["Temperatur"])
        assert pd.api.types.is_numeric_dtype(data["Effizienz"])
        assert pd.api.types.is_numeric_dtype(data["Produktionszeit"])
        assert data["Status"].dtype == "object"

        # Wertebereiche prüfen
        assert data["Temperatur"].min() >= 40
        assert data["Temperatur"].max() <= 90
        assert data["Effizienz"].min() >= 50
        assert data["Effizienz"].max() <= 100
        assert data["Produktionszeit"].min() >= 0.1
        assert data["Produktionszeit"].max() <= 10

    def test_create_sample_machine_data_different_sizes(self):
        """Testet verschiedene Datensatzgrößen"""
        for size in [10, 50, 200]:
            data = jupyter_widgets_demo.create_sample_machine_data(size)
            assert len(data) == size
            assert not data.empty

    def test_create_sample_machine_data_reproducibility(self):
        """Testet die Reproduzierbarkeit der Daten (durch Seed)"""
        data1 = jupyter_widgets_demo.create_sample_machine_data(50)
        data2 = jupyter_widgets_demo.create_sample_machine_data(50)

        # Sollten identisch sein aufgrund des Seeds
        pd.testing.assert_frame_equal(data1, data2)

    def test_create_interactive_dashboard_without_widgets(self):
        """Testet Dashboard-Erstellung ohne ipywidgets"""
        data = jupyter_widgets_demo.create_sample_machine_data(50)

        # Mock ipywidgets als nicht verfügbar
        with patch.object(jupyter_widgets_demo, "WIDGETS_AVAILABLE", False):
            dashboard = jupyter_widgets_demo.create_interactive_dashboard(data)
            assert dashboard is None

    @pytest.mark.skipif(
        not jupyter_widgets_demo.WIDGETS_AVAILABLE, reason="ipywidgets nicht verfügbar"
    )
    def test_create_interactive_dashboard_with_widgets(self):
        """Testet Dashboard-Erstellung mit ipywidgets"""
        data = jupyter_widgets_demo.create_sample_machine_data(30)
        dashboard = jupyter_widgets_demo.create_interactive_dashboard(data)

        assert dashboard is not None
        # Widget sollte ein Container sein
        assert hasattr(dashboard, "children")

    def test_create_simple_widgets_without_widgets(self):
        """Testet einfache Widgets ohne ipywidgets"""
        with patch.object(jupyter_widgets_demo, "WIDGETS_AVAILABLE", False):
            widgets = jupyter_widgets_demo.create_simple_widgets()
            assert widgets == {}

    @pytest.mark.skipif(
        not jupyter_widgets_demo.WIDGETS_AVAILABLE, reason="ipywidgets nicht verfügbar"
    )
    def test_create_simple_widgets_with_widgets(self):
        """Testet einfache Widgets mit ipywidgets"""
        widgets = jupyter_widgets_demo.create_simple_widgets()

        expected_types = ["slider", "text", "button", "checkbox", "dropdown"]
        assert all(widget_type in widgets for widget_type in expected_types)
        assert len(widgets) == len(expected_types)

    def test_demonstrate_magic_commands(self):
        """Testet Magic Commands Demonstration"""
        magic_commands = jupyter_widgets_demo.demonstrate_magic_commands()

        assert isinstance(magic_commands, list)
        assert len(magic_commands) > 0

        # Prüfe bekannte Magic Commands
        command_text = " ".join(magic_commands)
        assert "%time" in command_text
        assert "%matplotlib" in command_text
        assert "%%time" in command_text
        assert "%%bash" in command_text

    def test_validate_notebook_security_safe_content(self):
        """Testet Sicherheitsvalidierung mit sicherem Inhalt"""
        safe_content = """
        import pandas as pd
        import numpy as np

        data = pd.DataFrame({'A': [1, 2, 3]})
        result = data.sum()
        print(result)
        """

        validation = jupyter_widgets_demo.validate_notebook_security(safe_content)

        assert validation["safe"] is True
        assert len(validation["warnings"]) == 0
        assert len(validation["blocked_patterns"]) == 0

    def test_validate_notebook_security_dangerous_content(self):
        """Testet Sicherheitsvalidierung mit gefährlichem Inhalt"""
        dangerous_content = """
        import os
        import subprocess

        os.system('rm -rf /')
        subprocess.call(['sudo', 'rm', '-rf', '/'])
        eval('malicious_code')
        """

        validation = jupyter_widgets_demo.validate_notebook_security(dangerous_content)

        assert validation["safe"] is False
        assert len(validation["warnings"]) > 0
        assert len(validation["blocked_patterns"]) > 0

        # Prüfe spezifische gefährliche Patterns
        blocked = validation["blocked_patterns"]
        assert "import os" in blocked
        assert "subprocess" in blocked
        assert "eval(" in blocked

    def test_performance_test_function(self):
        """Testet Performance-Test-Funktion"""
        # Kleine Anzahl für schnellen Test
        execution_time = jupyter_widgets_demo.performance_test_function(1000)

        assert isinstance(execution_time, float)
        assert execution_time >= 0
        assert execution_time < 1.0  # Sollte unter 1 Sekunde sein

    def test_performance_test_function_scaling(self):
        """Testet Performance-Skalierung"""
        time_small = jupyter_widgets_demo.performance_test_function(100)
        time_large = jupyter_widgets_demo.performance_test_function(1000)

        # Größere Berechnung sollte länger dauern
        assert time_large >= time_small


class TestJupyterExtensionsDemo:
    """Tests für jupyter_extensions_demo.py"""

    def test_module_imports_successfully(self):
        """Testet, ob das Modul erfolgreich importiert wird"""
        assert jupyter_extensions_demo is not None

    def test_extension_manager_initialization(self):
        """Testet Initialisierung des Extension Managers"""
        manager = jupyter_extensions_demo.JupyterExtensionManager()

        assert hasattr(manager, "lab_extensions")
        assert hasattr(manager, "notebook_extensions")
        assert isinstance(manager.lab_extensions, list)
        assert isinstance(manager.notebook_extensions, list)
        assert len(manager.lab_extensions) > 0
        assert len(manager.notebook_extensions) > 0

    def test_get_lab_extension_commands(self):
        """Testet Lab Extension Commands"""
        manager = jupyter_extensions_demo.JupyterExtensionManager()
        commands = manager.get_lab_extension_commands()

        assert isinstance(commands, list)
        assert len(commands) > 0

        # Prüfe bekannte Commands
        command_text = " ".join(commands)
        assert "jupyter labextension install" in command_text
        assert "@jupyter-widgets/jupyterlab-manager" in command_text
        assert "jupyter lab build" in command_text

    def test_get_notebook_extension_commands(self):
        """Testet Notebook Extension Commands"""
        manager = jupyter_extensions_demo.JupyterExtensionManager()
        commands = manager.get_notebook_extension_commands()

        assert isinstance(commands, list)
        assert len(commands) > 0

        # Prüfe bekannte Commands
        command_text = " ".join(commands)
        assert "pip install" in command_text
        assert "jupyter_contrib_nbextensions" in command_text
        assert "jupyter nbextension enable" in command_text

    @patch("subprocess.run")
    def test_check_extension_availability_success(self, mock_run):
        """Testet Extension-Verfügbarkeit bei erfolgreicher Prüfung"""
        # Mock erfolgreiche subprocess calls
        mock_run.return_value.returncode = 0

        manager = jupyter_extensions_demo.JupyterExtensionManager()
        status = manager.check_extension_availability()

        assert isinstance(status, dict)
        assert "jupyterlab_available" in status
        assert "notebook_available" in status
        assert "extensions_installed" in status

    @patch("subprocess.run")
    def test_check_extension_availability_failure(self, mock_run):
        """Testet Extension-Verfügbarkeit bei fehlgeschlagener Prüfung"""
        # Mock fehlgeschlagene subprocess calls
        mock_run.side_effect = FileNotFoundError()

        manager = jupyter_extensions_demo.JupyterExtensionManager()
        status = manager.check_extension_availability()

        assert status["jupyterlab_available"] is False
        assert status["notebook_available"] is False

    def test_create_jupyter_config(self):
        """Testet Jupyter-Konfigurationserstellung"""
        config = jupyter_extensions_demo.create_jupyter_config()

        assert isinstance(config, str)
        assert len(config) > 0

        # Prüfe wichtige Konfigurationsoptionen
        assert "c = get_config()" in config
        assert "NotebookApp.ip" in config
        assert "NotebookApp.port" in config
        assert "bystronic" in config.lower()
        assert "MappingKernelManager" in config

    def test_create_jupyterlab_settings(self):
        """Testet JupyterLab Settings Erstellung"""
        settings = jupyter_extensions_demo.create_jupyterlab_settings()

        assert isinstance(settings, dict)
        assert len(settings) > 0

        # Prüfe bekannte Settings-Kategorien
        expected_keys = [
            "@jupyterlab/apputils-extension:themes",
            "@jupyterlab/notebook-extension:tracker",
            "@jupyterlab/shortcuts-extension:shortcuts",
            "@jupyterlab/terminal-extension:plugin",
        ]

        for key in expected_keys:
            assert key in settings

    def test_create_extension_test_notebook(self):
        """Testet Test-Notebook Erstellung"""
        notebook = jupyter_extensions_demo.create_extension_test_notebook()

        assert isinstance(notebook, dict)
        assert "cells" in notebook
        assert "metadata" in notebook
        assert "nbformat" in notebook
        assert "nbformat_minor" in notebook

        # Prüfe Notebook-Struktur
        assert notebook["nbformat"] == 4
        assert isinstance(notebook["cells"], list)
        assert len(notebook["cells"]) > 0

        # Prüfe Zell-Typen
        cell_types = [cell["cell_type"] for cell in notebook["cells"]]
        assert "markdown" in cell_types
        assert "code" in cell_types

    def test_create_extension_test_notebook_content(self):
        """Testet Inhalt des Test-Notebooks"""
        notebook = jupyter_extensions_demo.create_extension_test_notebook()

        # Sammle allen Zellinhalt
        all_content = []
        for cell in notebook["cells"]:
            if "source" in cell:
                if isinstance(cell["source"], list):
                    all_content.extend(cell["source"])
                else:
                    all_content.append(cell["source"])

        content_text = " ".join(all_content)

        # Prüfe auf Extension-spezifische Inhalte
        assert "Variable Inspector" in content_text
        assert "Table of Contents" in content_text
        assert "Git Integration" in content_text
        assert "Debugger" in content_text

    @patch("subprocess.run")
    def test_validate_extension_installation_success(self, mock_run):
        """Testet erfolgreiche Extension-Validierung"""
        # Mock erfolgreiche Extension-Liste
        mock_output = """
        JupyterLab v3.4.0
        @jupyter-widgets/jupyterlab-manager v5.0.0 enabled OK
        @jupyterlab/toc v6.0.0 enabled OK
        @jupyterlab/git v0.37.0 enabled OK
        """

        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = mock_output

        validation = jupyter_extensions_demo.validate_extension_installation()

        assert validation["status"] == "success"
        assert (
            "alle empfohlenen extensions installiert" in validation["message"].lower()
        )
        assert len(validation["recommendations"]) == 0

    @patch("subprocess.run")
    def test_validate_extension_installation_partial(self, mock_run):
        """Testet teilweise Extension-Installation"""
        # Mock teilweise Extension-Liste
        mock_output = """
        JupyterLab v3.4.0
        @jupyter-widgets/jupyterlab-manager v5.0.0 enabled OK
        """

        mock_run.return_value.returncode = 0
        mock_run.return_value.stdout = mock_output

        validation = jupyter_extensions_demo.validate_extension_installation()

        assert validation["status"] == "partial"
        assert len(validation["recommendations"]) > 0

    @patch("subprocess.run")
    def test_validate_extension_installation_error(self, mock_run):
        """Testet fehlerhafte Extension-Validierung"""
        # Mock fehlgeschlagener subprocess call
        mock_run.return_value.returncode = 1

        validation = jupyter_extensions_demo.validate_extension_installation()

        assert validation["status"] == "error"
        assert len(validation["message"]) > 0

    @patch("subprocess.run")
    def test_validate_extension_installation_timeout(self, mock_run):
        """Testet Timeout bei Extension-Validierung"""
        # Mock Timeout
        mock_run.side_effect = subprocess.TimeoutExpired("jupyter", 15)

        validation = jupyter_extensions_demo.validate_extension_installation()

        assert validation["status"] == "error"
        assert (
            "timeout" in validation["message"].lower()
            or "fehler" in validation["message"].lower()
        )


class TestJupyterNotebookHandling:
    """Tests für Notebook-spezifische Funktionalität"""

    def test_notebook_json_structure(self):
        """Testet JSON-Struktur von Notebooks"""
        notebook = jupyter_extensions_demo.create_extension_test_notebook()

        # Validiere als JSON
        json_str = json.dumps(notebook)
        parsed = json.loads(json_str)

        assert parsed == notebook

    def test_notebook_cell_validation(self):
        """Testet Validierung von Notebook-Zellen"""
        notebook = jupyter_extensions_demo.create_extension_test_notebook()

        for i, cell in enumerate(notebook["cells"]):
            # Jede Zelle muss cell_type haben
            assert "cell_type" in cell, f"Zelle {i} hat keinen cell_type"
            assert cell["cell_type"] in [
                "markdown",
                "code",
            ], f"Ungültiger cell_type in Zelle {i}"

            # Jede Zelle muss metadata haben
            assert "metadata" in cell, f"Zelle {i} hat keine metadata"

            # Code-Zellen müssen zusätzliche Felder haben
            if cell["cell_type"] == "code":
                assert (
                    "execution_count" in cell
                ), f"Code-Zelle {i} hat keine execution_count"
                assert "outputs" in cell, f"Code-Zelle {i} hat keine outputs"

    def test_notebook_security_validation_integration(self):
        """Testet Integration der Sicherheitsvalidierung mit Notebooks"""
        notebook = jupyter_extensions_demo.create_extension_test_notebook()

        # Extrahiere Code aus allen Code-Zellen
        code_content = []
        for cell in notebook["cells"]:
            if cell["cell_type"] == "code" and "source" in cell:
                if isinstance(cell["source"], list):
                    code_content.extend(cell["source"])
                else:
                    code_content.append(cell["source"])

        combined_code = "\n".join(code_content)

        # Validiere Sicherheit
        validation = jupyter_widgets_demo.validate_notebook_security(combined_code)

        # Test-Notebook sollte sicher sein
        assert validation["safe"] is True


class TestJupyterDeploymentIntegration:
    """Tests für Deployment-Integration"""

    def test_deployment_files_exist(self):
        """Testet Existenz der Deployment-Dateien"""
        deployment_path = (
            Path(__file__).parent.parent / "src" / "07_jupyter" / "deployment"
        )

        assert deployment_path.exists()
        assert (deployment_path / "Dockerfile").exists()
        assert (deployment_path / "docker-compose.yml").exists()

    def test_dockerfile_content(self):
        """Testet Dockerfile-Inhalt"""
        dockerfile_path = (
            Path(__file__).parent.parent
            / "src"
            / "07_jupyter"
            / "deployment"
            / "Dockerfile"
        )

        with open(dockerfile_path) as f:
            content = f.read()

        # Prüfe wichtige Dockerfile-Komponenten
        assert "FROM jupyter/scipy-notebook" in content
        assert "EXPOSE 8888" in content
        assert "pip install" in content
        assert "jupyter labextension install" in content

    def test_docker_compose_content(self):
        """Testet docker-compose.yml Inhalt"""
        compose_path = (
            Path(__file__).parent.parent
            / "src"
            / "07_jupyter"
            / "deployment"
            / "docker-compose.yml"
        )

        with open(compose_path) as f:
            content = f.read()

        # Prüfe wichtige Compose-Komponenten
        assert "version:" in content
        assert "services:" in content
        assert "jupyter:" in content
        assert "8888:8888" in content
        assert "volumes:" in content


@pytest.mark.integration
class TestJupyterIntegration:
    """Integrationstests für Jupyter-Komponenten"""

    def test_full_workflow_simulation(self):
        """Simuliert einen vollständigen Jupyter-Workflow"""
        # 1. Daten erstellen
        data = jupyter_widgets_demo.create_sample_machine_data(50)
        assert not data.empty

        # 2. Sicherheitsvalidierung
        test_code = "import pandas as pd\ndata.head()"
        validation = jupyter_widgets_demo.validate_notebook_security(test_code)
        assert validation["safe"]

        # 3. Extension Manager
        manager = jupyter_extensions_demo.JupyterExtensionManager()
        commands = manager.get_lab_extension_commands()
        assert len(commands) > 0

        # 4. Konfiguration
        config = jupyter_extensions_demo.create_jupyter_config()
        assert "bystronic" in config.lower()

        # 5. Test-Notebook
        notebook = jupyter_extensions_demo.create_extension_test_notebook()
        assert len(notebook["cells"]) > 0

    def test_error_handling_robustness(self):
        """Testet Robustheit der Fehlerbehandlung"""
        # Test mit leeren/ungültigen Eingaben
        empty_data = pd.DataFrame()

        # Sollte nicht crashen
        try:
            dashboard = jupyter_widgets_demo.create_interactive_dashboard(empty_data)
            # Dashboard kann None sein oder ein leeres Widget
            assert dashboard is None or hasattr(dashboard, "children")
        except Exception as e:
            pytest.fail(f"Dashboard-Erstellung sollte nicht crashen: {e}")

        # Test mit ungültigen Sicherheitsinhalten
        invalid_content = None
        try:
            validation = jupyter_widgets_demo.validate_notebook_security("")
            assert isinstance(validation, dict)
        except Exception as e:
            pytest.fail(f"Sicherheitsvalidierung sollte nicht crashen: {e}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
