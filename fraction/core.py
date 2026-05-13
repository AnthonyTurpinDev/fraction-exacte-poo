#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Cœur mathématique – Fonctions de base pour les fractions
=========================================================

Ce module contient les fonctions mathématiques fondamentales
utilisées par la classe Fraction : PGCD, simplification,
et validations.

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import math
from typing import Tuple
from .exceptions import DivisionByZeroError


# -------------------------------------------------------------------
# Fonctions mathématiques fondamentales
# -------------------------------------------------------------------

def pgcd(a: int, b: int) -> int:
    """
    Calcule le Plus Grand Commun Diviseur (PGCD) de deux entiers.
    
    Utilise l'algorithme d'Euclide (version itérative optimisée).
    
    Paramètres
    ----------
    a : int
        Premier entier (peut être négatif)
    b : int
        Second entier (peut être nul)
    
    Retourne
    -------
    int
        PGCD de a et b (toujours positif ou nul)
    
    Complexité
    ----------
    O(log(min(|a|, |b|))) dans le pire cas
    
    Exemples
    --------
    >>> pgcd(12, 8)
    4
    >>> pgcd(17, 19)
    1
    >>> pgcd(-12, 8)
    4
    >>> pgcd(0, 5)
    5
    >>> pgcd(0, 0)
    0
    """
    a = abs(a)
    b = abs(b)
    
    # Cas particuliers
    if a == 0 and b == 0:
        return 0
    if a == 0:
        return b
    if b == 0:
        return a
    
    # Algorithme d'Euclide itératif
    while b:
        a, b = b, a % b
    
    return a


def pgcd_etendu(a: int, b: int) -> Tuple[int, int, int]:
    """
    Algorithme d'Euclide étendu.
    
    Retourne (g, x, y) tels que : a*x + b*y = g = pgcd(a, b)
    
    Paramètres
    ----------
    a : int
        Premier entier
    b : int
        Second entier
    
    Retourne
    -------
    Tuple[int, int, int]
        (pgcd, coefficient_x, coefficient_y)
    
    Exemple
    -------
    >>> pgcd_etendu(12, 8)
    (4, 1, -1)  # 12*1 + 8*(-1) = 4
    
    Notes
    -----
    Utile pour calculer l'inverse modulaire et résoudre
    des équations diophantiennes.
    """
    if b == 0:
        return (abs(a), 1 if a > 0 else -1, 0)
    
    # Algorithme récursif
    g, x1, y1 = pgcd_etendu(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    
    # Normalisation du signe
    if g < 0:
        g, x, y = -g, -x, -y
    
    return (g, x, y)


def simplifier(num: int, den: int) -> Tuple[int, int]:
    """
    Simplifie une fraction et normalise le signe.
    
    La normalisation garantit que :
    - Le dénominateur est toujours positif
    - La fraction est irréductible (PGCD = 1)
    
    Paramètres
    ----------
    num : int
        Numérateur (peut être négatif)
    den : int
        Dénominateur (≠ 0)
    
    Retourne
    -------
    Tuple[int, int]
        (numérateur simplifié, dénominateur positif)
    
    Lève
    ----
    DivisionByZeroError
        Si den == 0
    
    Exemples
    --------
    >>> simplifier(4, 8)
    (1, 2)
    >>> simplifier(6, -4)
    (-3, 2)
    >>> simplifier(0, 5)
    (0, 1)
    >>> simplifier(-12, -18)
    (2, 3)
    """
    if den == 0:
        raise DivisionByZeroError("Dénominateur nul")
    
    # Gestion du signe
    if den < 0:
        num = -num
        den = -den
    
    # Cas particulier : numérateur nul
    if num == 0:
        return (0, 1)
    
    # Simplification par le PGCD
    d = pgcd(num, den)
    if d > 1:
        num //= d
        den //= d
    
    return (num, den)


# -------------------------------------------------------------------
# Validations et utilitaires
# -------------------------------------------------------------------

def est_entier(num: int, den: int) -> bool:
    """
    Vérifie si une fraction représente un entier.
    
    Paramètres
    ----------
    num : int
        Numérateur
    den : int
        Dénominateur (≠ 0)
    
    Retourne
    -------
    bool
        True si den divise num exactement
    
    Exemples
    --------
    >>> est_entier(4, 2)
    True
    >>> est_entier(3, 2)
    False
    >>> est_entier(0, 5)
    True
    """
    if den == 0:
        return False
    return num % den == 0


def est_unitaire(num: int, den: int) -> bool:
    """
    Vérifie si une fraction est unitaire (numérateur = 1).
    
    Paramètres
    ----------
    num : int
        Numérateur
    den : int
        Dénominateur (≠ 0)
    
    Retourne
    -------
    bool
        True si |num| = 1
    
    Exemples
    --------
    >>> est_unitaire(1, 2)
    True
    >>> est_unitaire(-1, 3)
    True
    >>> est_unitaire(2, 3)
    False
    """
    return abs(num) == 1


def valeur_absolue(num: int, den: int) -> Tuple[int, int]:
    """
    Retourne la valeur absolue d'une fraction.
    
    Paramètres
    ----------
    num : int
        Numérateur
    den : int
        Dénominateur (≠ 0)
    
    Retourne
    -------
    Tuple[int, int]
        (|num|, den) après simplification
    
    Exemple
    -------
    >>> valeur_absolue(-3, 4)
    (3, 4)
    """
    return simplifier(abs(num), den)


def oppose(num: int, den: int) -> Tuple[int, int]:
    """
    Retourne l'opposé d'une fraction.
    
    Paramètres
    ----------
    num : int
        Numérateur
    den : int
        Dénominateur (≠ 0)
    
    Retourne
    -------
    Tuple[int, int]
        (-num, den) après simplification
    
    Exemple
    -------
    >>> oppose(3, 4)
    (-3, 4)
    """
    return simplifier(-num, den)


def inverse(num: int, den: int) -> Tuple[int, int]:
    """
    Retourne l'inverse d'une fraction (non nulle).
    
    Paramètres
    ----------
    num : int
        Numérateur (≠ 0)
    den : int
        Dénominateur (≠ 0)
    
    Retourne
    -------
    Tuple[int, int]
        (den, num) après simplification
    
    Lève
    ----
    DivisionByZeroError
        Si num == 0 (inverse impossible)
    
    Exemple
    -------
    >>> inverse(3, 4)
    (4, 3)
    >>> inverse(-2, 5)
    (-5, 2)
    """
    if num == 0:
        raise DivisionByZeroError("Impossible de prendre l'inverse d'une fraction nulle")
    return simplifier(den, num)


# -------------------------------------------------------------------
# Fonctions de comparaison (bas niveau)
# -------------------------------------------------------------------

def comparer(num1: int, den1: int, num2: int, den2: int) -> int:
    """
    Compare deux fractions sans conversion en flottant.
    
    Paramètres
    ----------
    num1, den1 : int
        Première fraction (den1 ≠ 0)
    num2, den2 : int
        Deuxième fraction (den2 ≠ 0)
    
    Retourne
    -------
    int
        -1 si f1 < f2
         0 si f1 == f2
         1 si f1 > f2
    
    Complexité
    ----------
    O(1) – utilise la multiplication croisée
    
    Exemples
    --------
    >>> comparer(1, 2, 1, 3)
    1  # 1/2 > 1/3
    >>> comparer(1, 3, 2, 5)
    -1  # 1/3 < 2/5
    >>> comparer(1, 2, 2, 4)
    0  # 1/2 == 2/4
    """
    # Multiplication croisée
    gauche = num1 * den2
    droite = num2 * den1
    
    if gauche < droite:
        return -1
    if gauche > droite:
        return 1
    return 0


# -------------------------------------------------------------------
# Fonctions d'arrondi et conversion
# -------------------------------------------------------------------

def arrondir(num: int, den: int, decimales: int = 0) -> float:
    """
    Arrondit une fraction à un nombre donné de décimales.
    
    Paramètres
    ----------
    num : int
        Numérateur
    den : int
        Dénominateur (≠ 0)
    decimales : int
        Nombre de décimales (défaut : 0)
    
    Retourne
    -------
    float
        Valeur arrondie
    
    Exemple
    -------
    >>> arrondir(1, 3, 2)
    0.33
    """
    return round(num / den, decimales)


# -------------------------------------------------------------------
# Constantes utiles
# -------------------------------------------------------------------

# Quelques constantes mathématiques sous forme de fractions exactes
# (à utiliser avec la classe Fraction, pas directement avec ce module)

_PRECOMPUTED = {
    "ZERO": (0, 1),
    "UN": (1, 1),
    "MOINS_UN": (-1, 1),
    "DEMI": (1, 2),
    "TIERS": (1, 3),
    "QUART": (1, 4),
    "DEUX_TIERS": (2, 3),
    "TROIS_QUARTS": (3, 4),
}


# -------------------------------------------------------------------
# Tests et démonstration
# -------------------------------------------------------------------

def _demo():
    """Démonstration rapide des fonctions du module core."""
    
    print("=" * 50)
    print("Démonstration : Core mathématique")
    print("=" * 50)
    
    print("\n1. PGCD")
    print(f"   pgcd(12, 8) = {pgcd(12, 8)}")
    print(f"   pgcd(17, 19) = {pgcd(17, 19)}")
    print(f"   pgcd(0, 5) = {pgcd(0, 5)}")
    
    print("\n2. Euclide étendu")
    g, x, y = pgcd_etendu(12, 8)
    print(f"   pgcd_etendu(12, 8) = ({g}, {x}, {y})")
    print(f"   Vérification : 12*{x} + 8*{y} = {12*x + 8*y}")
    
    print("\n3. Simplification")
    print(f"   simplifier(4, 8) = {simplifier(4, 8)}")
    print(f"   simplifier(6, -4) = {simplifier(6, -4)}")
    print(f"   simplifier(0, 5) = {simplifier(0, 5)}")
    
    print("\n4. Utilitaires")
    print(f"   est_entier(4, 2) = {est_entier(4, 2)}")
    print(f"   est_unitaire(1, 3) = {est_unitaire(1, 3)}")
    print(f"   valeur_absolue(-3, 4) = {valeur_absolue(-3, 4)}")
    print(f"   oppose(3, 4) = {oppose(3, 4)}")
    print(f"   inverse(3, 4) = {inverse(3, 4)}")
    
    print("\n5. Comparaison")
    print(f"   comparer(1, 2, 1, 3) = {comparer(1, 2, 1, 3)} (1/2 > 1/3)")
    print(f"   comparer(1, 3, 2, 5) = {comparer(1, 3, 2, 5)} (1/3 < 2/5)")
    
    print("\n6. Arrondi")
    print(f"   arrondir(1, 3, 2) = {arrondir(1, 3, 2)}")


if __name__ == "__main__":
    _demo()