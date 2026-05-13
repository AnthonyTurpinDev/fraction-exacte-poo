# ============================================================
# Makefile – Projet Fraction Exacte
# ============================================================
# Auteur : Étudiant L1 Informatique
# Date : 2026
# Description : Commandes pour installation, tests, benchmarks
# ============================================================

# --------------------------------------------
# Variables
# --------------------------------------------

# Python interpreter
PYTHON = python3
PYTEST = pytest
COVERAGE = coverage

# Project name
PROJECT_NAME = fraction_exacte
VERSION = 1.0.0

# Directories
SRC_DIR = fraction
TEST_DIR = tests
EXAMPLES_DIR = examples
BENCH_DIR = benchmarks
DOCS_DIR = docs

# Colors for pretty output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[0;33m
BLUE = \033[0;34m
NC = \033[0m # No Color

# --------------------------------------------
# Default target
# --------------------------------------------

.DEFAULT_GOAL = help

# --------------------------------------------
# Help
# --------------------------------------------

.PHONY: help
help:
	@echo "$(BLUE)============================================================$(NC)"
	@echo "$(BLUE)Fraction Exacte – Makefile Commands$(NC)"
	@echo "$(BLUE)============================================================$(NC)"
	@echo ""
	@echo "$(GREEN)Installation:$(NC)"
	@echo "  make install      Installer les dépendances"
	@echo "  make dev          Installer avec dépendances de développement"
	@echo "  make clean        Nettoyer les fichiers temporaires"
	@echo "  make clean-all    Nettoyage complet (y compris venv)"
	@echo ""
	@echo "$(GREEN)Tests:$(NC)"
	@echo "  make test         Exécuter tous les tests unitaires"
	@echo "  make test-verbose Tests unitaires (mode verbeux)"
	@echo "  make test-core    Tests du module core"
	@echo "  make test-fraction Tests de la classe Fraction"
	@echo "  make test-continued Tests des fractions continues"
	@echo "  make coverage     Générer le rapport de couverture"
	@echo ""
	@echo "$(GREEN)Qualité:$(NC)"
	@echo "  make lint         Vérifier le code avec pylint/flake8"
	@echo "  make format       Formater le code avec black"
	@echo "  make type-check   Vérification des types avec mypy"
	@echo ""
	@echo "$(GREEN)Exécution:$(NC)"
	@echo "  make run          Exécuter la démo basique"
	@echo "  make run-advanced Exécuter la démo avancée"
	@echo "  make run-compare  Comparer fractions vs flottants"
	@echo "  make bench        Exécuter les benchmarks"
	@echo ""
	@echo "$(GREEN)Documentation:$(NC)"
	@echo "  make docs         Générer la documentation"
	@echo "  make serve-docs   Servir la documentation localement"
	@echo ""
	@echo "$(GREEN)Distribution:$(NC)"
	@echo "  make build        Construire le package"
	@echo "  make package      Créer l'archive de distribution"
	@echo ""
	@echo "$(GREEN)CI/CD:$(NC)"
	@echo "  make ci           Exécuter tous les checks CI"
	@echo "  make validate     Valider le projet complet"

# --------------------------------------------
# Installation
# --------------------------------------------

.PHONY: install
install:
	@echo "$(GREEN)📦 Installation des dépendances...$(NC)"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -r requirements.txt
	@echo "$(GREEN)✅ Installation terminée$(NC)"

.PHONY: dev
dev:
	@echo "$(GREEN)🔧 Installation avec dépendances de développement...$(NC)"
	$(PYTHON) -m pip install --upgrade pip
	$(PYTHON) -m pip install -e .
	$(PYTHON) -m pip install pytest pytest-cov coverage black flake8 mypy pylint
	@echo "$(GREEN)✅ Installation développement terminée$(NC)"

.PHONY: clean
clean:
	@echo "$(YELLOW)🧹 Nettoyage des fichiers temporaires...$(NC)"
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".mypy_cache" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name "htmlcov" -exec rm -rf {} + 2>/dev/null || true
	rm -rf build/ dist/ 2>/dev/null || true
	@echo "$(GREEN)✅ Nettoyage terminé$(NC)"

.PHONY: clean-all
clean-all: clean
	@echo "$(YELLOW)🗑️  Nettoyage complet (y compris venv)...$(NC)"
	rm -rf venv/ .venv/ env/ 2>/dev/null || true
	rm -rf .coverage coverage.xml .pytest_cache/ 2>/dev/null || true
	rm -rf .mypy_cache/ .ruff_cache/ 2>/dev/null || true
	@echo "$(GREEN)✅ Nettoyage complet terminé$(NC)"

# --------------------------------------------
# Tests
# --------------------------------------------

.PHONY: test
test:
	@echo "$(BLUE)🧪 Exécution des tests unitaires...$(NC)"
	$(PYTHON) -m unittest discover $(TEST_DIR) -q
	@echo "$(GREEN)✅ Tous les tests sont passés$(NC)"

.PHONY: test-verbose
test-verbose:
	@echo "$(BLUE)🧪 Exécution des tests unitaires (mode verbeux)...$(NC)"
	$(PYTHON) -m unittest discover $(TEST_DIR) -v
	@echo "$(GREEN)✅ Tous les tests sont passés$(NC)"

.PHONY: test-core
test-core:
	@echo "$(BLUE)🧪 Tests du module core...$(NC)"
	$(PYTHON) -m unittest $(TEST_DIR).test_core -v

.PHONY: test-fraction
test-fraction:
	@echo "$(BLUE)🧪 Tests de la classe Fraction...$(NC)"
	$(PYTHON) -m unittest $(TEST_DIR).test_fraction -v

.PHONY: test-continued
test-continued:
	@echo "$(BLUE)🧪 Tests des fractions continues...$(NC)"
	$(PYTHON) -m unittest $(TEST_DIR).test_continued -v

.PHONY: coverage
coverage:
	@echo "$(BLUE)📊 Génération du rapport de couverture...$(NC)"
	$(COVERAGE) run -m unittest discover $(TEST_DIR)
	$(COVERAGE) report -m
	$(COVERAGE) html
	@echo "$(GREEN)✅ Rapport HTML généré dans htmlcov/$(NC)"

# --------------------------------------------
# Qualité du code
# --------------------------------------------

.PHONY: lint
lint:
	@echo "$(BLUE)🔍 Vérification du code avec flake8...$(NC)"
	flake8 $(SRC_DIR) $(TEST_DIR) $(EXAMPLES_DIR) --max-line-length=100 --ignore=E203,W503
	@echo "$(GREEN)✅ Linting terminé$(NC)"

.PHONY: format
format:
	@echo "$(BLUE)🎨 Formatage du code avec black...$(NC)"
	black $(SRC_DIR) $(TEST_DIR) $(EXAMPLES_DIR) --line-length=100
	@echo "$(GREEN)✅ Formatage terminé$(NC)"

.PHONY: type-check
type-check:
	@echo "$(BLUE)🔍 Vérification des types avec mypy...$(NC)"
	mypy $(SRC_DIR) --ignore-missing-imports --allow-untyped-decorators
	@echo "$(GREEN)✅ Vérification des types terminée$(NC)"

# --------------------------------------------
# Exécution des exemples
# --------------------------------------------

.PHONY: run
run:
	@echo "$(BLUE)🚀 Exécution de la démo basique...$(NC)"
	$(PYTHON) $(EXAMPLES_DIR)/basic_usage.py --auto

.PHONY: run-advanced
run-advanced:
	@echo "$(BLUE)🚀 Exécution de la démo avancée...$(NC)"
	$(PYTHON) $(EXAMPLES_DIR)/advanced_continued.py --auto

.PHONY: run-compare
run-compare:
	@echo "$(BLUE)🚀 Comparaison Fractions vs Flottants...$(NC)"
	$(PYTHON) $(EXAMPLES_DIR)/compare_with_float.py --auto

# --------------------------------------------
# Benchmarks
# --------------------------------------------

.PHONY: bench
bench:
	@echo "$(BLUE)⚡ Exécution des benchmarks...$(NC)"
	$(PYTHON) $(BENCH_DIR)/perf_test.py
	@echo "$(GREEN)✅ Benchmarks terminés$(NC)"

# --------------------------------------------
# Documentation
# --------------------------------------------

.PHONY: docs
docs:
	@echo "$(BLUE)📚 Génération de la documentation...$(NC)"
	@echo "  Voir docs/API.md et docs/ALGO.md"
	@echo "$(GREEN)✅ Documentation prête$(NC)"

.PHONY: serve-docs
serve-docs:
	@echo "$(BLUE)🌐 Service de la documentation...$(NC)"
	cd $(DOCS_DIR) && $(PYTHON) -m http.server 8000
	@echo "$(GREEN)✅ Documentation disponible sur http://localhost:8000$(NC)"

# --------------------------------------------
# Distribution
# --------------------------------------------

.PHONY: build
build:
	@echo "$(BLUE)📦 Construction du package...$(NC)"
	$(PYTHON) setup.py sdist bdist_wheel
	@echo "$(GREEN)✅ Package construit dans dist/$(NC)"

.PHONY: package
package: clean build
	@echo "$(GREEN)✅ Archive créée : dist/$(PROJECT_NAME)-$(VERSION).tar.gz$(NC)"

# --------------------------------------------
# CI/CD
# --------------------------------------------

.PHONY: ci
ci: clean test lint type-check
	@echo "$(GREEN)✅ CI : tous les checks sont passés$(NC)"

.PHONY: validate
validate: ci coverage bench
	@echo "$(GREEN)✅ Projet validé avec succès$(NC)"

# --------------------------------------------
# Quick commands (pour un usage rapide)
# --------------------------------------------

.PHONY: all
all: install test run bench
	@echo "$(GREEN)✅ Projet prêt et testé$(NC)"

.PHONY: quick
quick: test run
	@echo "$(GREEN)✅ Tests et démo exécutés$(NC)"

# --------------------------------------------
# Développement
# --------------------------------------------

.PHONY: venv
venv:
	@echo "$(BLUE)🐍 Création de l'environnement virtuel...$(NC)"
	$(PYTHON) -m venv venv
	@echo "$(GREEN)✅ Environnement créé. Activez-le avec : source venv/bin/activate$(NC)"

# --------------------------------------------
# Nettoyage final des sorties
# --------------------------------------------

.PHONY: clean-output
clean-output:
	@echo "$(YELLOW)🗑️  Nettoyage des fichiers de sortie...$(NC)"
	rm -rf output/ results/ 2>/dev/null || true
	rm -f *.log *.out 2>/dev/null || true
	@echo "$(GREEN)✅ Sorties nettoyées$(NC)"