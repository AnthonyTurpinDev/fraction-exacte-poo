#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fraction Exacte – Calcul rationnel en Python
============================================

Package de manipulation de fractions exactes avec :
- Simplification automatique (algorithme d'Euclide)
- Opérateurs arithmétiques standards (+, -, ×, /)
- Comparaisons exactes (<, >, ==)
- Génération de fractions continues
- Gestion d'erreurs personnalisée

Exemple d'utilisation :
-----------------------
>>> from fraction import Fraction
>>> a = Fraction(1, 2)
>>> b = Fraction(1, 3)
>>> print(a + b)
5/6
>>> print(a > b)
True

Auteur : Étudiant L1 Informatique
Version : 1.0.0
"""

# -------------------------------------------------------------------
# Import des classes principales
# -------------------------------------------------------------------

from .fraction import Fraction
from .continued import fraction_continue
from .exceptions import FractionError, DivisionByZeroError, InvalidOperationError

# -------------------------------------------------------------------
# Métadonnées du package
# -------------------------------------------------------------------

__version__ = "1.0.0"
__author__ = "Étudiant L1 Informatique"
__email__ = "etudiant@univ.fr"
__license__ = "MIT"
__copyright__ = "Copyright (c) 2026"

# -------------------------------------------------------------------
# Liste des symboles exportés (bonne pratique)
# -------------------------------------------------------------------

__all__ = [
    # Classes
    "Fraction",
    
    # Fonctions utilitaires
    "fraction_continue",
    
    # Exceptions
    "FractionError",
    "DivisionByZeroError",
    "InvalidOperationError",
    
    # Métadonnées
    "__version__",
    "__author__",
    "__email__",
    "__license__",
]

# -------------------------------------------------------------------
# Documentation rapide (accessible via help())
# -------------------------------------------------------------------

def _aide():
    """
    Affiche l'aide rapide du package.
    
    Utilisation :
        from fraction import _aide
        _aide()
    """
    help_text = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                    FRACTION EXACTE v1.0.0                    ║
    ╚══════════════════════════════════════════════════════════════╝
    
    📦 Classes disponibles :
        Fraction(num, den=1)    → Crée une fraction simplifiée
    
    🔧 Fonctions utilitaires :
        fraction_continue(val, profondeur) → Génère une fraction continue
    
    ⚠️ Exceptions :
        FractionError           → Erreur générique du module
        DivisionByZeroError    → Dénominateur nul
        InvalidOperationError   → Opération avec type incompatible
    
    📖 Exemples :
        >>> from fraction import Fraction
        >>> a = Fraction(1, 2)
        >>> b = Fraction(1, 3)
        >>> print(a + b)
        5/6
        
    🔗 Documentation complète : docs/API.md
    """
    print(help_text)


# Optionnel : rendre _aide accessible (mais pas dans __all__)
# pour ne pas polluer l'API publique