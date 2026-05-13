#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Exceptions personnalisées – Module Fraction
============================================

Ce module définit la hiérarchie des exceptions spécifiques
à la manipulation des fractions.

Hiérarchie :
    FractionError (base)
    ├── DivisionByZeroError
    └── InvalidOperationError

Auteur : Étudiant L1 Informatique
Date : 2026
"""


# -------------------------------------------------------------------
# Exception de base
# -------------------------------------------------------------------

class FractionError(Exception):
    """
    Exception de base pour tout le module `fraction`.
    
    Toutes les exceptions spécifiques au module héritent de cette classe.
    
    Utilisation
    -----------
    >>> from fraction import FractionError
    >>> try:
    ...     f = Fraction(1, 0)
    ... except FractionError as e:
    ...     print(f"Erreur : {e}")
    
    Notes
    -----
    Cette exception ne devrait jamais être levée directement.
    Utilisez ses sous-classes pour une gestion d'erreur plus fine.
    """
    
    def __init__(self, message: str = "Erreur générique du module fraction"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"[FractionError] {self.message}"


# -------------------------------------------------------------------
# Exception : Division par zéro
# -------------------------------------------------------------------

class DivisionByZeroError(FractionError):
    """
    Exception levée lorsqu'une opération implique une division par zéro.
    
    Cas concernés :
    - Création d'une fraction avec dénominateur = 0
    - Inverse d'une fraction nulle
    - Division par une fraction nulle
    
    Utilisation
    -----------
    >>> from fraction import DivisionByZeroError
    >>> try:
    ...     f = Fraction(1, 0)
    ... except DivisionByZeroError as e:
    ...     print(f"Erreur : {e}")
    Erreur : Dénominateur nul
    
    Exemples de levée
    -----------------
    Fraction(1, 0)              # Dénominateur nul
    Fraction(0, 1).inverse()    # Inverse de zéro
    Fraction(1, 2) / Fraction(0, 1)  # Division par zéro
    """
    
    def __init__(self, message: str = "Division par zéro interdite"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"[DivisionByZeroError] {self.message}"


# -------------------------------------------------------------------
# Exception : Opération invalide
# -------------------------------------------------------------------

class InvalidOperationError(FractionError):
    """
    Exception levée lorsqu'une opération est invalide.
    
    Cas concernés :
    - Type d'opérande non supporté (ex: Fraction + "texte")
    - Profondeur invalide dans une fraction continue
    - Liste vide pour fraction_continue_generique
    
    Utilisation
    -----------
    >>> from fraction import InvalidOperationError
    >>> try:
    ...     f = Fraction(1, 2) + "3"
    ... except InvalidOperationError as e:
    ...     print(f"Erreur : {e}")
    Erreur : Opération non supportée entre Fraction et str
    
    Exemples de levée
    -----------------
    Fraction(1, 2) + "3"        # Type incompatible
    fraction_continue(7, 0)     # Profondeur < 1
    fraction_continue_generique([])  # Liste vide
    """
    
    def __init__(self, message: str = "Opération invalide"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"[InvalidOperationError] {self.message}"


# -------------------------------------------------------------------
# Exceptions spécifiques (réservées pour extensions futures)
# -------------------------------------------------------------------

class OverflowFractionError(FractionError):
    """
    Exception levée en cas de dépassement de capacité.
    
    Réservée pour des extensions futures où les numérateurs/dénominateurs
    pourraient devenir trop grands (ex: factorielles, grands entiers).
    
    Notes
    -----
    Actuellement non utilisée car Python gère nativement les entiers
    de taille arbitraire.
    """
    
    def __init__(self, message: str = "Dépassement de capacité"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"[OverflowFractionError] {self.message}"


class NotReducibleError(FractionError):
    """
    Exception levée lorsqu'une fraction n'est pas simplifiable.
    
    Réservée pour des contextes où on s'attend à ce qu'une fraction
    ne soit pas déjà simplifiée.
    """
    
    def __init__(self, message: str = "La fraction est déjà irréductible"):
        self.message = message
        super().__init__(self.message)
    
    def __str__(self) -> str:
        return f"[NotReducibleError] {self.message}"


# -------------------------------------------------------------------
# Fonction utilitaire : vérification de type
# -------------------------------------------------------------------

def verifier_type(valeur, types_attendus, contexte: str = "") -> None:
    """
    Vérifie qu'une valeur est d'un type attendu.
    
    Paramètres
    ----------
    valeur : any
        Valeur à vérifier
    types_attendus : tuple
        Types acceptés (ex: (int, Fraction))
    contexte : str
        Message contextuel pour l'exception
    
    Lève
    ----
    InvalidOperationError
        Si le type n'est pas dans types_attendus
    
    Exemple
    -------
    >>> verifier_type(42, (int,), "addition")
    >>> verifier_type("42", (int,), "addition")
    [InvalidOperationError] addition : Type str non supporté
    """
    if not isinstance(valeur, types_attendus):
        types_str = " ou ".join(t.__name__ for t in types_attendus)
        message = f"{contexte} : Type {type(valeur).__name__} non supporté. Attendu : {types_str}"
        raise InvalidOperationError(message)


# -------------------------------------------------------------------
# Tests et démonstration
# -------------------------------------------------------------------

def _demo():
    """Démonstration rapide de la hiérarchie des exceptions."""
    
    print("=" * 50)
    print("Démonstration : Exceptions")
    print("=" * 50)
    
    print("\n1. DivisionByZeroError")
    try:
        raise DivisionByZeroError("Test de division par zéro")
    except DivisionByZeroError as e:
        print(f"   Attrapé : {e}")
    
    print("\n2. InvalidOperationError")
    try:
        raise InvalidOperationError("Test d'opération invalide")
    except InvalidOperationError as e:
        print(f"   Attrapé : {e}")
    
    print("\n3. Hiérarchie")
    try:
        raise DivisionByZeroError("Erreur spécifique")
    except FractionError as e:
        print(f"   Attrapé comme FractionError : {e}")
    
    print("\n4. Fonction verifier_type")
    try:
        verifier_type("abc", (int,), "addition")
    except InvalidOperationError as e:
        print(f"   Attrapé : {e}")


if __name__ == "__main__":
    _demo()