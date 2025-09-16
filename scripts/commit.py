#!/usr/bin/env python3
"""
Professioneller Git-Commit-Befehl für Bystronic Python-Projekt
Führt automatische Qualitätschecks durch und erstellt konventionelle Commit-Nachrichten
"""

import argparse
import subprocess
import sys
from pathlib import Path


class Colors:
    """ANSI-Farbcodes für Terminal-Output"""

    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BOLD = "\033[1m"
    END = "\033[0m"


class GitCommitter:
    """Hauptklasse für professionelle Git-Commits"""

    def __init__(
        self,
        no_verify: bool = False,
        force_push: bool = False,
        skip_tests: bool = False,
    ):
        self.no_verify = no_verify
        self.force_push = force_push
        self.skip_tests = skip_tests
        self.project_root = Path.cwd()

        # Commit-Typen mit Emojis (auf Deutsch)
        self.commit_types = {
            "feat": {"emoji": "✨", "desc": "Neue Funktionalität"},
            "fix": {"emoji": "🐛", "desc": "Fehlerbehebung"},
            "docs": {"emoji": "📚", "desc": "Dokumentationsänderungen"},
            "style": {"emoji": "💎", "desc": "Code-Formatierung"},
            "refactor": {"emoji": "♻️", "desc": "Code-Umstrukturierung"},
            "perf": {"emoji": "⚡", "desc": "Performance-Verbesserungen"},
            "test": {"emoji": "🧪", "desc": "Tests hinzufügen oder korrigieren"},
            "chore": {"emoji": "🔧", "desc": "Build-Prozess, Tools, Konfiguration"},
            "ci": {"emoji": "🚀", "desc": "Continuous Integration Änderungen"},
            "security": {"emoji": "🔒", "desc": "Sicherheitsverbesserungen"},
            "deps": {"emoji": "📦", "desc": "Dependency-Updates"},
        }

    def print_status(self, message: str, color: str = Colors.BLUE) -> None:
        """Druckt Status-Nachricht mit Farbe"""
        print(f"{color}{Colors.BOLD}[COMMIT]{Colors.END} {message}")

    def print_error(self, message: str) -> None:
        """Druckt Fehlermeldung"""
        print(f"{Colors.RED}{Colors.BOLD}[FEHLER]{Colors.END} {message}")

    def print_success(self, message: str) -> None:
        """Druckt Erfolgsmeldung"""
        print(f"{Colors.GREEN}{Colors.BOLD}[ERFOLG]{Colors.END} {message}")

    def run_command(
        self, cmd: list[str], capture_output: bool = True
    ) -> tuple[bool, str]:
        """Führt Shell-Kommando aus und gibt Erfolg und Output zurück"""
        try:
            result = subprocess.run(
                cmd, capture_output=capture_output, text=True, cwd=self.project_root
            )
            return result.returncode == 0, result.stdout + result.stderr
        except Exception as e:
            return False, str(e)

    def check_git_status(self) -> tuple[list[str], list[str]]:
        """Prüft Git-Status und gibt gestakte und ungestakte Dateien zurück"""
        success, output = self.run_command(["git", "status", "--porcelain"])
        if not success:
            self.print_error("Fehler beim Abrufen des Git-Status")
            sys.exit(1)

        staged_files = []
        unstaged_files = []

        for line in output.strip().split("\n"):
            if not line:
                continue
            status = line[:2]
            filename = line[3:]

            if status[0] != " " and status[0] != "?":
                staged_files.append(filename)
            if status[1] != " ":
                unstaged_files.append(filename)

        return staged_files, unstaged_files

    def auto_stage_files(self) -> None:
        """Fügt automatisch alle Änderungen hinzu, falls nichts gestakt ist"""
        staged_files, unstaged_files = self.check_git_status()

        if not staged_files and unstaged_files:
            self.print_status("Keine Dateien gestakt. Füge alle Änderungen hinzu...")
            success, _ = self.run_command(["git", "add", "."])
            if not success:
                self.print_error("Fehler beim Hinzufügen der Dateien")
                sys.exit(1)
            self.print_success("Alle Änderungen hinzugefügt")

    def run_python_checks(self) -> bool:
        """Führt Python-spezifische Qualitätschecks aus"""
        if self.no_verify:
            self.print_status("Pre-Commit-Checks übersprungen (--no-verify)")
            return True

        self.print_status("Führe Python-Qualitätschecks aus...")

        # Ruff Linting
        self.print_status("Prüfe Code mit Ruff...")
        success, output = self.run_command(["uv", "run", "ruff", "check", "src/"])
        if not success:
            self.print_error("Ruff-Linting fehlgeschlagen:")
            print(output)

            # Versuche automatische Fixes
            self.print_status("Versuche automatische Ruff-Fixes...")
            fix_success, _ = self.run_command(
                ["uv", "run", "ruff", "check", "--fix", "src/"]
            )
            if fix_success:
                self.print_success("Automatische Fixes angewendet")
                # Erneut prüfen
                success, output = self.run_command(
                    ["uv", "run", "ruff", "check", "src/"]
                )
                if not success:
                    self.print_error(
                        "Ruff-Probleme konnten nicht automatisch behoben werden"
                    )
                    return False
            else:
                return False

        # Black Formatierung
        self.print_status("Prüfe Code-Formatierung mit Black...")
        success, output = self.run_command(["uv", "run", "black", "--check", "src/"])
        if not success:
            self.print_status("Formatiere Code mit Black...")
            success, _ = self.run_command(["uv", "run", "black", "src/"])
            if not success:
                self.print_error("Black-Formatierung fehlgeschlagen")
                return False
            self.print_success("Code formatiert")

        # MyPy Type Checking (optional, da es oft Warnungen gibt)
        self.print_status("Prüfe Typen mit MyPy...")
        success, output = self.run_command(["uv", "run", "mypy", "src/"])
        if not success:
            self.print_status(
                f"{Colors.YELLOW}MyPy-Warnungen gefunden (nicht kritisch):{Colors.END}"
            )
            print(output)

        # Tests ausführen
        if not self.skip_tests:
            self.print_status("Führe Tests aus...")
            success, output = self.run_command(["uv", "run", "pytest", "-v"])
            if not success:
                self.print_error("Tests fehlgeschlagen:")
                print(output)
                return False
            self.print_success("Alle Tests bestanden")
        else:
            self.print_status("Tests übersprungen (--skip-tests)")

        self.print_success("Alle Python-Qualitätschecks bestanden")
        return True

    def analyze_diff(self) -> dict[str, any]:
        """Analysiert git diff um Änderungstyp zu bestimmen"""
        success, diff_output = self.run_command(["git", "diff", "--cached", "--stat"])
        if not success:
            return {"type": "chore", "files": [], "stats": ""}

        # Analysiere geänderte Dateien
        files_changed = []
        for line in diff_output.split("\n"):
            if "|" in line:
                filename = line.split("|")[0].strip()
                files_changed.append(filename)

        # Bestimme Commit-Typ basierend auf Dateien
        commit_type = self.determine_commit_type(files_changed)

        return {"type": commit_type, "files": files_changed, "stats": diff_output}

    def determine_commit_type(self, files: list[str]) -> str:
        """Bestimmt Commit-Typ basierend auf geänderten Dateien"""
        # Prüfe auf verschiedene Dateitypen
        has_tests = any("test" in f.lower() for f in files)
        has_docs = any(f.endswith((".md", ".rst", ".txt", ".adoc")) for f in files)
        has_config = any(
            f in ["pyproject.toml", "Makefile", ".github/workflows/"]
            or f.startswith(".")
            for f in files
        )
        has_deps = any(f in ["pyproject.toml", "uv.lock"] for f in files)
        has_src = any(f.startswith("src/") for f in files)

        # Bestimme Typ nach Priorität
        if has_deps:
            return "deps"
        elif has_tests and not has_src:
            return "test"
        elif has_docs and not has_src:
            return "docs"
        elif has_config and not has_src:
            return "chore"
        elif has_src:
            return "feat"  # Default für Source-Code-Änderungen
        else:
            return "chore"

    def create_commit_message(self, diff_info: dict[str, any]) -> str:
        """Erstellt konventionelle Commit-Nachricht"""
        commit_type = diff_info["type"]
        files = diff_info["files"]

        # Emoji und Typ
        emoji = self.commit_types[commit_type]["emoji"]
        type_desc = self.commit_types[commit_type]["desc"]

        # Kurzbeschreibung basierend auf Dateien
        if len(files) == 1:
            filename = Path(files[0]).name
            short_desc = f"Aktualisiere {filename}"
        elif len(files) <= 3:
            short_desc = f"Aktualisiere {len(files)} Dateien"
        else:
            short_desc = f"Umfangreiche Änderungen ({len(files)} Dateien)"

        # Vollständige Commit-Nachricht
        commit_msg = f"{emoji} {commit_type}: {short_desc}\n\n"
        commit_msg += f"Typ: {type_desc}\n"
        commit_msg += f"Geänderte Dateien: {len(files)}\n\n"

        if files:
            commit_msg += "Dateien:\n"
            for file in files[:10]:  # Maximal 10 Dateien anzeigen
                commit_msg += f"- {file}\n"
            if len(files) > 10:
                commit_msg += f"... und {len(files) - 10} weitere\n"

        return commit_msg

    def commit_changes(self, message: str) -> bool:
        """Führt den Git-Commit aus"""
        self.print_status("Erstelle Commit...")
        success, output = self.run_command(["git", "commit", "-m", message])
        if not success:
            self.print_error("Commit fehlgeschlagen:")
            print(output)
            return False

        self.print_success("Commit erfolgreich erstellt")
        return True

    def push_changes(self) -> bool:
        """Pusht Änderungen zum Remote-Repository"""
        # Prüfe ob Remote existiert
        success, _ = self.run_command(["git", "remote"])
        if not success:
            self.print_status("Kein Remote-Repository konfiguriert")
            return True

        # Frage nach Push
        if not self.force_push:
            response = input(
                f"{Colors.CYAN}Änderungen zum Remote-Repository pushen? (j/N): {Colors.END}"
            )
            if response.lower() not in ["j", "ja", "y", "yes"]:
                return True

        self.print_status("Pushe Änderungen...")
        push_cmd = ["git", "push"]
        if self.force_push:
            push_cmd.append("--force")

        success, output = self.run_command(push_cmd)
        if not success:
            self.print_error("Push fehlgeschlagen:")
            print(output)
            return False

        self.print_success("Änderungen erfolgreich gepusht")
        return True

    def run(self) -> None:
        """Hauptmethode - führt den kompletten Commit-Prozess aus"""
        self.print_status("Starte professionellen Git-Commit-Prozess...")

        # 1. Prüfe Git-Status und stage Dateien
        self.auto_stage_files()

        # 2. Zeige Übersicht der Änderungen
        staged_files, _ = self.check_git_status()
        if not staged_files:
            self.print_error("Keine Änderungen zum Committen gefunden")
            sys.exit(1)

        self.print_status(f"Zu committende Dateien: {len(staged_files)}")
        for file in staged_files[:5]:  # Zeige erste 5 Dateien
            print(f"  - {file}")
        if len(staged_files) > 5:
            print(f"  ... und {len(staged_files) - 5} weitere")

        # 3. Führe Qualitätschecks aus
        if not self.run_python_checks():
            self.print_error("Qualitätschecks fehlgeschlagen. Commit abgebrochen.")
            sys.exit(1)

        # 4. Analysiere Diff und erstelle Commit-Nachricht
        diff_info = self.analyze_diff()
        commit_message = self.create_commit_message(diff_info)

        # 5. Zeige Commit-Nachricht zur Bestätigung
        print(f"\n{Colors.CYAN}{Colors.BOLD}Geplante Commit-Nachricht:{Colors.END}")
        print(f"{Colors.WHITE}{commit_message}{Colors.END}")

        response = input(
            f"{Colors.CYAN}Commit mit dieser Nachricht erstellen? (J/n): {Colors.END}"
        )
        if response.lower() in ["n", "no", "nein"]:
            self.print_status("Commit abgebrochen")
            sys.exit(0)

        # 6. Erstelle Commit
        if not self.commit_changes(commit_message):
            sys.exit(1)

        # 7. Optional: Push zum Remote
        self.push_changes()

        self.print_success("Git-Commit-Prozess erfolgreich abgeschlossen!")


def main():
    """Hauptfunktion mit Argument-Parsing"""
    parser = argparse.ArgumentParser(
        description="Professioneller Git-Commit mit automatischen Qualitätschecks",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Beispiele:
  python scripts/commit.py                    # Standard-Commit
  python scripts/commit.py --no-verify       # Ohne Pre-Commit-Checks
  python scripts/commit.py --skip-tests      # Ohne Tests
  python scripts/commit.py --force-push      # Mit automatischem Force-Push
        """,
    )

    parser.add_argument(
        "--no-verify", action="store_true", help="Überspringt Pre-Commit-Checks"
    )
    parser.add_argument(
        "--force-push",
        action="store_true",
        help="Führt automatischen Force-Push aus (Vorsicht!)",
    )
    parser.add_argument(
        "--skip-tests", action="store_true", help="Überspringt Testausführung"
    )

    args = parser.parse_args()

    # Erstelle und führe GitCommitter aus
    committer = GitCommitter(
        no_verify=args.no_verify, force_push=args.force_push, skip_tests=args.skip_tests
    )

    try:
        committer.run()
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Commit-Prozess abgebrochen{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"{Colors.RED}Unerwarteter Fehler: {e}{Colors.END}")
        sys.exit(1)


if __name__ == "__main__":
    main()
