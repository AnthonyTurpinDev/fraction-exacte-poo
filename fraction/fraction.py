#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Classe Fraction – Calcul exact de nombres rationnels
=====================================================

Cette classe implémente une fraction mathématique avec :
- Simplification automatique (algorithme d'Euclide)
- Opérateurs arithmétiques standards (+, -, *, /)
- Opérateurs de comparaison (<, >, ==)
- Conversion en flottant et arrondi
- Support des opérations avec entiers

Auteur : Étudiant L1 Informatique
Date : 2026
"""

from typing import Union, Any
from .core import simplifier, comparer, arrondir, inverse
from .exceptions import DivisionByZeroError, InvalidOperationError


class Fraction:
    """
    Fraction rationnelle simplifiée automatiquement.
    
    Attributes
    ----------
    _num : int
        Numérateur (stocké après simplification)
    _den : int
        Dénominateur (toujours positif après simplification)
    
    Examples
    --------
    >>> from fraction import Fraction
    >>> a = Fraction(1, 2)
    >>> b = Fraction(1, 3)
    >>> print(a + b)
    5/6
    >>> print(a > b)
    True
    >>> print(a == Fraction(2, 4))
    True
    """
    
    __slots__ = ('_num', '_den')
    
    def __init__(self, num: int, den: int = 1):
        """
        Initialise une fraction à partir d'un numérateur et d'un dénominateur.
        
        Paramètres
        ----------
        num : int
            Numérateur (peut être négatif)
        den : int
            Dénominateur (doit être ≠ 0, défaut = 1)
        
        Lève
        ----
        DivisionByZeroError
            Si den == 0
        
        Exemples
        --------
        >>> Fraction(3, 4)
        Fraction(3, 4)
        >>> Fraction(6, -8)
        Fraction(-3, 4)
        >>> Fraction(5)
        Fraction(5, 1)
        """
        if den == 0:
            raise DivisionByZeroError("Dénominateur nul")
        
        self._num, self._den = simplifier(num, den)
    
    # -------------------------------------------------------------------
    # Propriétés
    # -------------------------------------------------------------------
    
    @property
    def num(self) -> int:
        """
        Retourne le numérateur (après simplification).
        
        Returns
        -------
        int
            Numérateur simplifié
        
        Exemple
        -------
        >>> f = Fraction(4, 8)
        >>> f.num
        1
        """
        return self._num
    
    @property
    def den(self) -> int:
        """
        Retourne le dénominateur (toujours positif après simplification).
        
        Returns
        -------
        int
            Dénominateur simplifié et positif
        
        Exemple
        -------
        >>> f = Fraction(4, -8)
        >>> f.den
        2
        """
        return self._den
    
    # -------------------------------------------------------------------
    # Opérateurs arithmétiques
    # -------------------------------------------------------------------
    
    def __add__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Additionne deux fractions ou une fraction avec un entier.
        
        Paramètres
        ----------
        other : Fraction ou int
            Opérande à ajouter
        
        Retourne
        -------
        Fraction
            Résultat de l'addition
        
        Exemples
        --------
        >>> Fraction(1, 2) + Fraction(1, 3)
        Fraction(5, 6)
        >>> Fraction(1, 2) + 2
        Fraction(5, 2)
        """
        if isinstance(other, int):
            return Fraction(self._num + other * self._den, self._den)
        
        if isinstance(other, Fraction):
            return Fraction(
                self._num * other._den + other._num * self._den,
                self._den * other._den
            )
        
        raise InvalidOperationError(
            f"Addition impossible entre Fraction et {type(other).__name__}"
        )
    
    def __radd__(self, other: int) -> 'Fraction':
        """
        Addition à droite (entier + Fraction).
        
        Paramètres
        ----------
        other : int
            Entier à ajouter
        
        Retourne
        -------
        Fraction
            Résultat de l'addition
        
        Exemple
        -------
        >>> 2 + Fraction(1, 2)
        Fraction(5, 2)
        """
        return self + other
    
    def __sub__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Soustrait deux fractions ou une fraction avec un entier.
        
        Paramètres
        ----------
        other : Fraction ou int
            Opérande à soustraire
        
        Retourne
        -------
        Fraction
            Résultat de la soustraction
        
        Exemples
        --------
        >>> Fraction(3, 4) - Fraction(1, 4)
        Fraction(1, 2)
        >>> Fraction(5, 2) - 1
        Fraction(3, 2)
        """
        if isinstance(other, int):
            return Fraction(self._num - other * self._den, self._den)
        
        if isinstance(other, Fraction):
            return Fraction(
                self._num * other._den - other._num * self._den,
                self._den * other._den
            )
        
        raise InvalidOperationError(
            f"Soustraction impossible entre Fraction et {type(other).__name__}"
        )
    
    def __rsub__(self, other: int) -> 'Fraction':
        """
        Soustraction à droite (entier - Fraction).
        
        Paramètres
        ----------
        other : int
            Entier dont on soustrait la fraction
        
        Retourne
        -------
        Fraction
            Résultat de la soustraction
        
        Exemple
        -------
        >>> 1 - Fraction(1, 2)
        Fraction(1, 2)
        """
        return Fraction(other * self._den - self._num, self._den)
    
    def __mul__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Multiplie deux fractions ou une fraction avec un entier.
        
        Paramètres
        ----------
        other : Fraction ou int
            Opérande à multiplier
        
        Retourne
        -------
        Fraction
            Résultat de la multiplication
        
        Exemples
        --------
        >>> Fraction(2, 3) * Fraction(3, 5)
        Fraction(2, 5)
        >>> Fraction(1, 4) * 8
        Fraction(2, 1)
        """
        if isinstance(other, int):
            return Fraction(self._num * other, self._den)
        
        if isinstance(other, Fraction):
            return Fraction(self._num * other._num, self._den * other._den)
        
        raise InvalidOperationError(
            f"Multiplication impossible entre Fraction et {type(other).__name__}"
        )
    
    def __rmul__(self, other: int) -> 'Fraction':
        """
        Multiplication à droite (entier × Fraction).
        
        Paramètres
        ----------
        other : int
            Entier à multiplier
        
        Retourne
        -------
        Fraction
            Résultat de la multiplication
        
        Exemple
        -------
        >>> 4 * Fraction(1, 2)
        Fraction(2, 1)
        """
        return self * other
    
    def __truediv__(self, other: Union['Fraction', int]) -> 'Fraction':
        """
        Divise deux fractions ou une fraction par un entier.
        
        Paramètres
        ----------
        other : Fraction ou int
            Opérande diviseur (≠ 0)
        
        Retourne
        -------
        Fraction
            Résultat de la division
        
        Lève
        ----
        DivisionByZeroError
            Si other == 0
        
        Exemples
        --------
        >>> Fraction(1, 2) / Fraction(1, 3)
        Fraction(3, 2)
        >>> Fraction(3, 4) / 2
        Fraction(3, 8)
        """
        if isinstance(other, int):
            if other == 0:
                raise DivisionByZeroError("Division par zéro")
            return Fraction(self._num, self._den * other)
        
        if isinstance(other, Fraction):
            if other._num == 0:
                raise DivisionByZeroError("Division par une fraction nulle")
            return Fraction(self._num * other._den, self._den * other._num)
        
        raise InvalidOperationError(
            f"Division impossible entre Fraction et {type(other).__name__}"
        )
    
    def __rtruediv__(self, other: int) -> 'Fraction':
        """
        Division à droite (entier ÷ Fraction).
        
        Paramètres
        ----------
        other : int
            Entier à diviser par la fraction
        
        Retourne
        -------
        Fraction
            Résultat de la division
        
        Exemple
        -------
        >>> 2 / Fraction(1, 2)
        Fraction(4, 1)
        """
        if other == 0:
            raise DivisionByZeroError("Division par zéro")
        
        return Fraction(other * self._den, self._num)
    
    # -------------------------------------------------------------------
    # Opérateurs de comparaison
    # -------------------------------------------------------------------
    
    def __eq__(self, other: Any) -> bool:
        """
        Teste l'égalité exacte entre deux fractions ou avec un entier.
        
        Paramètres
        ----------
        other : Fraction, int ou autre
            Opérande à comparer
        
        Retourne
        -------
        bool
            True si les fractions sont égales, False sinon
        
        Exemples
        --------
        >>> Fraction(1, 2) == Fraction(2, 4)
        True
        >>> Fraction(1, 2) == 0.5
        False  # Comparaison avec float non supportée
        """
        if isinstance(other, int):
            return self._num == other * self._den
        
        if isinstance(other, Fraction):
            return self._num * other._den == other._num * self._den
        
        return False
    
    def __lt__(self, other: Union['Fraction', int]) -> bool:
        """
        Teste si self < other.
        
        Paramètres
        ----------
        other : Fraction ou int
            Opérande à comparer
        
        Retourne
        -------
        bool
            True si self < other, False sinon
        
        Exemples
        --------
        >>> Fraction(1, 3) < Fraction(1, 2)
        True
        >>> Fraction(2, 3) < 1
        True
        """
        if isinstance(other, int):
            return self._num < other * self._den
        
        if isinstance(other, Fraction):
            return self._num * other._den < other._num * self._den
        
        raise InvalidOperationError(
            f"Comparaison impossible entre Fraction et {type(other).__name__}"
        )
    
    def __gt__(self, other: Union['Fraction', int]) -> bool:
        """
        Teste si self > other.
        
        Paramètres
        ----------
        other : Fraction ou int
            Opérande à comparer
        
        Retourne
        -------
        bool
            True si self > other, False sinon
        
        Exemples
        --------
        >>> Fraction(2, 3) > Fraction(1, 2)
        True
        >>> Fraction(3, 4) > 0
        True
        """
        return not self < other and not self == other
    
    # -------------------------------------------------------------------
    # Méthodes de conversion
    # -------------------------------------------------------------------
    
    def __repr__(self) -> str:
        """
        Représentation technique (pour débogage).
        
        Returns
        -------
        str
            Représentation sous forme "Fraction(num, den)"
        
        Exemple
        -------
        >>> repr(Fraction(3, 4))
        'Fraction(3, 4)'
        """
        return f"Fraction({self._num}, {self._den})"
    
    def __str__(self) -> str:
        """
        Représentation lisible par un humain.
        
        Returns
        -------
        str
            "num/den" ou "num" si den == 1
        
        Exemples
        --------
        >>> str(Fraction(3, 4))
        '3/4'
        >>> str(Fraction(4, 2))
        '2'
        """
        if self._den == 1:
            return str(self._num)
        return f"{self._num}/{self._den}"
    
    def to_float(self) -> float:
        """
        Convertit la fraction en nombre flottant.
        
        Returns
        -------
        float
            Valeur décimale approchée
        
        Exemple
        -------
        >>> Fraction(1, 3).to_float()
        0.3333333333333333
        """
        return self._num / self._den
    
    def round(self, n: int = 0) -> float:
        """
        Arrondit la fraction à n décimales.
        
        Paramètres
        ----------
        n : int
            Nombre de décimales (défaut : 0)
        
        Returns
        -------
        float
            Valeur arrondie
        
        Exemple
        -------
        >>> Fraction(1, 3).round(2)
        0.33
        """
        return arrondir(self._num, self._den, n)
    
    # -------------------------------------------------------------------
    # Méthodes utilitaires supplémentaires
    # -------------------------------------------------------------------
    
    def inverse(self) -> 'Fraction':
        """
        Retourne l'inverse de la fraction.
        
        Returns
        -------
        Fraction
            Inverse de la fraction (den / num)
        
        Lève
        ----
        DivisionByZeroError
            Si la fraction est nulle
        
        Exemple
        -------
        >>> Fraction(3, 4).inverse()
        Fraction(4, 3)
        """
        if self._num == 0:
            raise DivisionByZeroError("Impossible de prendre l'inverse d'une fraction nulle")
        
        num, den = inverse(self._num, self._den)
        return Fraction(num, den)
    
    def est_entier(self) -> bool:
        """
        Vérifie si la fraction représente un entier.
        
        Returns
        -------
        bool
            True si den divise num exactement
        
        Exemple
        -------
        >>> Fraction(4, 2).est_entier()
        True
        >>> Fraction(3, 2).est_entier()
        False
        """
        return self._num % self._den == 0
    
    def est_unitaire(self) -> bool:
        """
        Vérifie si la fraction est unitaire (numérateur = ±1).
        
        Returns
        -------
        bool
            True si |num| == 1
        
        Exemple
        -------
        >>> Fraction(1, 2).est_unitaire()
        True
        >>> Fraction(2, 3).est_unitaire()
        False
        """
        return abs(self._num) == 1
    
    def valeur_absolue(self) -> 'Fraction':
        """
        Retourne la valeur absolue de la fraction.
        
        Returns
        -------
        Fraction
            Fraction avec numérateur positif
        
        Exemple
        -------
        >>> Fraction(-3, 4).valeur_absolue()
        Fraction(3, 4)
        """
        return Fraction(abs(self._num), self._den)
    
    # -------------------------------------------------------------------
    # Hash (pour utilisation dans sets/dictionnaires)
    # -------------------------------------------------------------------
    
    def __hash__(self) -> int:
        """
        Calcule le hash de la fraction (basé sur le couple num/den).
        
        Returns
        -------
        int
            Hash de la fraction
        
        Notes
        -----
        Permet d'utiliser Fraction comme clé de dictionnaire.
        """
        return hash((self._num, self._den))


# -------------------------------------------------------------------
# Tests et démonstration
# -------------------------------------------------------------------

def _demo():
    """Démonstration rapide de la classe Fraction."""
    
    print("=" * 50)
    print("Démonstration : Classe Fraction")
    print("=" * 50)
    
    print("\n1. Création")
    print(f"   Fraction(3, 4) = {Fraction(3, 4)}")
    print(f"   Fraction(6, -8) = {Fraction(6, -8)}")
    print(f"   Fraction(5) = {Fraction(5)}")
    
    print("\n2. Opérations")
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    print(f"   {a} + {b} = {a + b}")
    print(f"   {a} - {b} = {a - b}")
    print(f"   {a} × {b} = {a * b}")
    print(f"   {a} ÷ {b} = {a / b}")
    
    print("\n3. Comparaisons")
    print(f"   {a} > {b} ? {a > b}")
    print(f"   {a} < {b} ? {a < b}")
    print(f"   {a} == {Fraction(2, 4)} ? {a == Fraction(2, 4)}")
    
    print("\n4. Conversions")
    print(f"   {a}.to_float() = {a.to_float()}")
    print(f"   {a}.round(2) = {a.round(2)}")
    
    print("\n5. Méthodes utilitaires")
    print(f"   {a}.inverse() = {a.inverse()}")
    print(f"   {a}.est_entier() = {a.est_entier()}")
    print(f"   {a}.est_unitaire() = {a.est_unitaire()}")
    print(f"   {a}.valeur_absolue() = {a.valeur_absolue()}")


if __name__ == "__main__":
    _demo()