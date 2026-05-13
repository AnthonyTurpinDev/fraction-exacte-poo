#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Setup script – Fraction Exacte
================================================================================

Ce fichier permet d'installer le module `fraction` en tant que package Python.
Il est compatible avec pip et peut être publié sur PyPI.

Auteur : Étudiant L1 Informatique
Date : 2026
Version : 1.0.0
"""

import os
from setuptools import setup, find_packages

# -------------------------------------------------------------------
# Lecture du README.md pour la description longue
# -------------------------------------------------------------------

def read_long_description():
    """Lit le contenu du README.md pour PyPI."""
    here = os.path.abspath(os.path.dirname(__file__))
    readme_path = os.path.join(here, "README.md")
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Calcul exact sur les fractions – Programmation Orientée Objet en Python"


# -------------------------------------------------------------------
# Métadonnées du package
# -------------------------------------------------------------------

setup(
    # Identité du package
    name="fraction-exacte",
    version="1.0.0",
    author="Étudiant L1 Informatique",
    author_email="etudiant@univ.fr",
    
    # Description
    description="Calcul exact sur les fractions – POO Python",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    
    # URL et références
    url="https://github.com/tonpseudo/fraction-exacte",
    project_urls={
        "Bug Reports": "https://github.com/tonpseudo/fraction-exacte/issues",
        "Source": "https://github.com/tonpseudo/fraction-exacte",
        "Documentation": "https://github.com/tonpseudo/fraction-exacte/tree/main/docs",
    },
    
    # Structure du package
    packages=find_packages(exclude=["tests", "tests.*", "examples", "docs", "benchmarks"]),
    package_dir={"fraction": "fraction"},
    
    # Dépendances
    python_requires=">=3.10",
    install_requires=[
        # Aucune dépendance externe – pure bibliothèque standard
    ],
    
    # Dépendances optionnelles
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "coverage>=7.3.0",
            "black>=23.9.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "pylint>=3.0.0",
        ],
        "docs": [
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.4.0",
        ],
        "benchmark": [
            "pytest-benchmark>=4.0.0",
        ],
        "all": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "coverage>=7.3.0",
            "black>=23.9.0",
            "flake8>=6.1.0",
            "mypy>=1.5.0",
            "pylint>=3.0.0",
            "mkdocs>=1.5.0",
            "mkdocs-material>=9.4.0",
            "pytest-benchmark>=4.0.0",
        ],
    },
    
    # Classification du package
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Education",
    ],
    
    # Licence
    license="MIT",
    
    # Mots-clés pour la recherche sur PyPI
    keywords="fraction rational mathematics exact-calculus poo arithmetic simplification",
    
    # Inclusion des fichiers supplémentaires
    include_package_data=True,
    zip_safe=False,
    
    # Scripts en ligne de commande (optionnel)
    entry_points={
        "console_scripts": [
            # "fraction-demo = examples.basic_usage:main",  # À activer plus tard
        ],
    },
)


# -------------------------------------------------------------------
# Informations pour le débogage
# -------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Setup – Fraction Exacte v1.0.0")
    print("=" * 60)
    print("\nPour installer le package :")
    print("  pip install .")
    print("\nPour installer avec dépendances de développement :")
    print("  pip install .[dev]")
    print("\nPour tout installer :")
    print("  pip install .[all]")
    print("\nPour construire une distribution :")
    print("  python setup.py sdist bdist_wheel")
    print("=" * 60)