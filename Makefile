.PHONY: help format lint test clean install dev-install

help: ## Zeige verfügbare Kommandos
	@echo "Verfügbare Kommandos:"
	@echo ""
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Installiere Basis-Dependencies
	uv sync

dev-install: ## Installiere alle Dependencies inklusive Development-Tools
	uv sync --extra dev

format: ## Formatiere Code mit Black
	uv run black src/
	uv run ruff format src/

lint: ## Prüfe Code mit Ruff
	uv run ruff check src/
	uv run mypy src/ || true

lint-fix: ## Behebe automatisch behebbare Linting-Probleme
	uv run ruff check --fix src/

test: ## Führe Tests aus
	uv run pytest

test-coverage: ## Führe Tests mit Coverage-Report aus
	uv run pytest --cov=src --cov-report=html --cov-report=term

notebook: ## Starte Jupyter Notebook Server
	uv run jupyter notebook

lab: ## Starte Jupyter Lab
	uv run jupyter lab

pre-commit-install: ## Installiere Pre-Commit Hooks
	uv run pre-commit install

pre-commit: ## Führe Pre-Commit Checks manuell aus
	uv run pre-commit run --all-files

clean: ## Räume Build-Artefakte auf
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .mypy_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete

all: clean dev-install lint test ## Führe alle Checks aus

ci: lint test ## Continuous Integration Checks