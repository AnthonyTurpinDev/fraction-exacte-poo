#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Fractions continues – Module de génération
===========================================

Ce module fournit des outils pour générer et manipuler
des fractions continues sous forme de fractions exactes.

Auteur : Étudiant L1 Informatique
Date : 2026
"""

from typing import List, Tuple
from .fraction import Fraction
from .exceptions import InvalidOperationError


# -------------------------------------------------------------------
# Fonction principale
# -------------------------------------------------------------------

def fraction_continue(valeur: int, profondeur: int) -> Fraction:
    """
    Génère une fraction continue imbriquée.
    
    La fraction est construite selon le schéma suivant :
        
        total = 0
        frac = 1/1
        pour i de 1 à profondeur:
            total += valeur
            frac = Fraction(total, frac)
    
    Paramètres
    ----------
    valeur : int
        Valeur entière répétée à chaque étage de la fraction continue.
        Doit être un entier (positif ou négatif).
    
    profondeur : int
        Nombre d'étages de la fraction continue.
        Doit être ≥ 1.
    
    Retourne
    -------
    Fraction
        La fraction continue calculée, exprimée sous forme irréductible.
    
    Lève
    ----
    InvalidOperationError
        Si profondeur < 1.
    
    Exemples
    --------
    >>> from fraction import fraction_continue
    >>> fraction_continue(7, 1)
    Fraction(7, 1)
    
    >>> fraction_continue(7, 2)
    Fraction(2, 1)
    
    >>> fraction_continue(7, 8)
    Fraction(128, 35)
    
    >>> fraction_continue(5, 8)
    Fraction(128, 35)  # Même résultat qu'avec 7, 8 !
    
    Notes
    -----
    Cette fonction implémente un cas particulier de fraction continue
    où la même valeur est répétée à chaque étage.
    """
    
    if profondeur < 1:
        raise InvalidOperationError(
            f"La profondeur doit être ≥ 1, reçu : {profondeur}"
        )
    
    total = 0
    frac = Fraction(1, 1)
    
    for _ in range(profondeur):
        total += valeur
        frac = Fraction(total, frac)
    
    return frac


# -------------------------------------------------------------------
# Fonctions avancées
# -------------------------------------------------------------------

def fraction_continue_generique(coefficients: List[int]) -> Fraction:
    """
    Génère une fraction continue à partir d'une liste de coefficients.
    
    Forme générale :
        a0 + 1/(a1 + 1/(a2 + 1/(a3 + ...)))
    
    Paramètres
    ----------
    coefficients : List[int]
        Liste des coefficients [a0, a1, a2, ..., an]
        Tous les éléments doivent être des entiers.
    
    Retourne
    -------
    Fraction
        La fraction continue correspondante.
    
    Exemples
    --------
    >>> fraction_continue_generique([1, 2, 2])
    Fraction(7, 5)  # 1 + 1/(2 + 1/2) = 7/5
    
    >>> fraction_continue_generique([3, 7, 15, 1])
    Fraction(355, 113)  # Approximation de π
    """
    
    if not coefficients:
        raise InvalidOperationError("La liste des coefficients ne peut être vide")
    
    # On part de la fin : 1 / an
    frac = Fraction(coefficients[-1], 1)
    
    # On remonte vers le début
    for coef in reversed(coefficients[:-1]):
        frac = Fraction(coef, 1) + Fraction(1, frac)
    
    return frac


def convergence(valeur: int, profondeur_max: int) -> List[Fraction]:
    """
    Calcule les valeurs successives d'une fraction continue.
    
    Utile pour étudier la convergence vers une limite éventuelle.
    
    Paramètres
    ----------
    valeur : int
        Valeur de base répétée à chaque étage.
    
    profondeur_max : int
        Profondeur maximale (nombre d'étapes).
    
    Retourne
    -------
    List[Fraction]
        Liste des fractions pour p = 1 à profondeur_max.
    
    Exemple
    -------
    >>> conv = convergence(7, 5)
    >>> [str(f) for f in conv]
    ['7', '2', '21/2', '5/2', '77/10']
    """
    
    resultats = []
    total = 0
    frac = Fraction(1, 1)
    
    for _ in range(profondeur_max):
        total += valeur
        frac = Fraction(total, frac)
        resultats.append(frac)
    
    return resultats


def est_periodique(valeur: int, profondeur: int, seuil: int = 10) -> bool:
    """
    Vérifie si une fraction continue devient périodique.
    
    Paramètres
    ----------
    valeur : int
        Valeur de base.
    
    profondeur : int
        Profondeur à vérifier.
    
    seuil : int
        Nombre de répétitions nécessaires pour valider la périodicité.
    
    Retourne
    -------
    bool
        True si la fraction devient périodique (se stabilise).
    
    Note
    ----
    Pour certaines valeurs (comme 7), la fraction se stabilise
    rapidement. Pour d'autres, elle peut osciller indéfiniment.
    """
    
    valeurs = convergence(valeur, profondeur)
    
    if len(valeurs) < 2 * seuil:
        return False
    
    # Vérifier la périodicité sur les dernières valeurs
    fin = valeurs[-seuil:]
    for i in range(len(valeurs) - 2 * seuil, len(valeurs) - seuil):
        if valeurs[i:i + seuil] != fin:
            return False
    
    return True


def limite_approximative(valeur: int, profondeur: int = 100) -> float:
    """
    Calcule une approximation de la limite d'une fraction continue.
    
    Pour certaines valeurs, la fraction continue converge vers
    une limite réelle. Cette fonction estime cette limite.
    
    Paramètres
    ----------
    valeur : int
        Valeur de base.
    
    profondeur : int
        Profondeur pour l'approximation (plus grand = plus précis).
    
    Retourne
    -------
    float
        Approximation de la limite.
    
    Exemple
    -------
    >>> limite_approximative(1, 100)  # Nombre d'or
    1.618033988749895
    """
    
    f = fraction_continue(valeur, profondeur)
    return f.to_float()


# -------------------------------------------------------------------
# Constantes mathématiques via fractions continues
# -------------------------------------------------------------------

def nombre_dor(profondeur: int = 20) -> Fraction:
    """
    Approximation du nombre d'or (φ = (1 + √5)/2 ≈ 1.618...)
    
    La fraction continue du nombre d'or est [1; 1, 1, 1, ...]
    
    Paramètres
    ----------
    profondeur : int
        Nombre d'étages de la fraction continue.
    
    Retourne
    -------
    Fraction
        Approximation rationnelle du nombre d'or.
    """
    return fraction_continue_generique([1] * (profondeur + 1))


def racine_deux(profondeur: int = 20) -> Fraction:
    """
    Approximation de √2 ≈ 1.41421356...
    
    La fraction continue de √2 est [1; 2, 2, 2, ...]
    
    Paramètres
    ----------
    profondeur : int
        Nombre d'étages de la fraction continue.
    
    Retourne
    -------
    Fraction
        Approximation rationnelle de √2.
    """
    coefs = [1] + [2] * profondeur
    return fraction_continue_generique(coefs)


# -------------------------------------------------------------------
# Documentation et helpers
# -------------------------------------------------------------------

def _demo():
    """Démonstration rapide des fonctionnalités du module."""
    
    print("=" * 50)
    print("Démonstration : Fractions continues")
    print("=" * 50)
    
    print("\n1. fraction_continue(7, 8)")
    print(f"   → {fraction_continue(7, 8)}")
    
    print("\n2. fraction_continue_generique([1, 2, 2])")
    print(f"   → {fraction_continue_generique([1, 2, 2])}")
    
    print("\n3. convergence(7, 5)")
    for i, f in enumerate(convergence(7, 5), 1):
        print(f"   p={i} → {f}")
    
    print("\n4. nombre_dor(5)")
    print(f"   → {nombre_dor(5)} ≈ {nombre_dor(5).to_float()}")
    
    print("\n5. racine_deux(5)")
    print(f"   → {racine_deux(5)} ≈ {racine_deux(5).to_float()}")


if __name__ == "__main__":
    _demo()