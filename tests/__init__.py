#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests unitaires – Module Fraction
==================================

Ce package contient l'ensemble des tests unitaires pour le module `fraction`.

Exécution des tests :
---------------------
Depuis la racine du projet :

    # Exécuter tous les tests
    python -m unittest discover tests/
    
    # Exécuter avec verbosité
    python -m unittest discover tests/ -v
    
    # Exécuter un fichier de test spécifique
    python -m unittest tests.test_fraction
    
    # Exécuter une classe de test spécifique
    python -m unittest tests.test_fraction.TestFraction

Avec coverage :
---------------
    pip install coverage
    coverage run -m unittest discover tests/
    coverage report -m

Auteur : Étudiant L1 Informatique
Date : 2026
"""

# -------------------------------------------------------------------
# Métadonnées du package de test
# -------------------------------------------------------------------

__all__ = [
    'test_core',
    'test_fraction',
    'test_continued',
]

# -------------------------------------------------------------------
# Version et auteur (cohérence avec le module principal)
# -------------------------------------------------------------------

__version__ = "1.0.0"
__author__ = "Étudiant L1 Informatique"

# -------------------------------------------------------------------
# Fonction utilitaire pour exécuter tous les tests
# -------------------------------------------------------------------

def run_all():
    """
    Exécute tous les tests unitaires du module fraction.
    
    Cette fonction est pratique pour une exécution programmatique
    depuis un script ou un notebook.
    
    Utilisation
    -----------
    >>> from tests import run_all
    >>> run_all()
    
    Returns
    -------
    unittest.TestResult
        Résultat de l'exécution des tests
    """
    import unittest
    
    # Découverte automatique de tous les tests
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir='.', pattern='test_*.py')
    
    # Exécution
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


def run_module(module_name: str):
    """
    Exécute les tests d'un module spécifique.
    
    Paramètres
    ----------
    module_name : str
        Nom du module à tester (ex: 'core', 'fraction', 'continued')
    
    Utilisation
    -----------
    >>> from tests import run_module
    >>> run_module('fraction')
    """
    import unittest
    
    test_file = f"test_{module_name}.py"
    suite = unittest.defaultTestLoader.discover(
        start_dir='.',
        pattern=test_file
    )
    
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


# -------------------------------------------------------------------
# Informations pour le debugging
# -------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Tests unitaires – Fraction Exacte")
    print("=" * 60)
    print(f"Version : {__version__}")
    print(f"Auteur  : {__author__}")
    print("-" * 60)
    print("\nPour exécuter les tests :")
    print("  python -m unittest discover tests/ -v")
    print("\nOu depuis Python :")
    print("  from tests import run_all")
    print("  run_all()")
    print("=" * 60)