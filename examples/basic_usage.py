#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstrateur basique : Fractions exactes
-----------------------------------------
Ce script présente les fonctionnalités essentielles de la classe Fraction.

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import sys
import os

# Ajouter le parent directory au path pour importer le module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction.fraction import Fraction
from fraction.continued import fraction_continue


def introduction():
    """Présentation des fractions de base"""
    print("\n" + "="*60)
    print(" 1. CRÉATION DE FRACTIONS")
    print("="*60)
    
    # Création simple
    a = Fraction(1, 2)
    b = Fraction(3, 4)
    c = Fraction(5)  # Dénominateur par défaut = 1
    d = Fraction(6, -8)  # Simplification automatique + normalisation du signe
    
    print(f"Fraction(1, 2)     → {a}")
    print(f"Fraction(3, 4)     → {b}")
    print(f"Fraction(5)        → {c}")
    print(f"Fraction(6, -8)    → {d} (simplifiée et signe normalisé)")
    
    # Affichage des valeurs décimales
    print(f"\nValeurs décimales :")
    print(f"  {a} = {a.to_float()}")
    print(f"  {b} = {b.to_float()}")
    print(f"  {c} = {c.to_float()}")
    print(f"  {d} = {d.to_float()}")


def operations_arithmetiques():
    """Démonstration des opérations de base"""
    print("\n" + "="*60)
    print(" 2. OPÉRATIONS ARITHMÉTIQUES")
    print("="*60)
    
    a = Fraction(1, 2)
    b = Fraction(1, 3)
    
    print(f"a = {a}  |  b = {b}")
    print(f"-"*40)
    print(f"a + b = {a} + {b} = {a + b}")
    print(f"a - b = {a} - {b} = {a - b}")
    print(f"a × b = {a} × {b} = {a * b}")
    print(f"a ÷ b = {a} ÷ {b} = {a / b}")
    
    # Opérations avec des entiers
    print(f"\nOpérations avec des entiers :")
    print(f"{a} + 2 = {a + 2}")
    print(f"2 + {a} = {2 + a}  (via __radd__)")
    print(f"{a} - 1 = {a - 1}")
    print(f"1 - {a} = {1 - a}  (via __rsub__)")
    print(f"{a} × 4 = {a * 4}")
    print(f"4 × {a} = {4 * a}  (via __rmul__)")
    print(f"{a} ÷ 2 = {a / 2}")
    print(f"2 ÷ {a} = {2 / a}  (via __rtruediv__)")


def comparaisons():
    """Démonstration des comparaisons exactes"""
    print("\n" + "="*60)
    print(" 3. COMPARAISONS EXACTES")
    print("="*60)
    
    a = Fraction(1, 3)
    b = Fraction(2, 5)
    c = Fraction(1, 2)
    d = Fraction(2, 4)  # Équivalent à 1/2
    
    print(f"a = {a} ≈ {a.to_float():.3f}")
    print(f"b = {b} ≈ {b.to_float():.3f}")
    print(f"c = {c} ≈ {c.to_float():.3f}")
    print(f"d = {d} ≈ {d.to_float():.3f}")
    
    print(f"\nComparaisons :")
    print(f"  {a} < {b} → {a < b}")
    print(f"  {b} > {a} → {b > a}")
    print(f"  {c} == {d} → {c == d}  (égalité exacte après simplification)")
    print(f"  {a} == {b} → {a == b}")
    
    # Comparaison avec des entiers
    print(f"\nComparaisons avec des entiers :")
    print(f"  {c} < 1 → {c < 1}")
    print(f"  {c} > 0 → {c > 0}")
    print(f"  {a} == 0 → {a == 0}")


def simplification():
    """Démonstration de la simplification automatique"""
    print("\n" + "="*60)
    print(" 4. SIMPLIFICATION AUTOMATIQUE")
    print("="*60)
    
    fractions = [
        (2, 4), (6, 9), (12, 18), (-8, 12), (15, -25), (100, 250)
    ]
    
    print("Fraction brute → Fraction simplifiée")
    print("-"*40)
    for num, den in fractions:
        f = Fraction(num, den)
        print(f"{num}/{den:3d}      → {f}")
    
    # Vérification de l'irréductibilité
    print(f"\nVérification :")
    f = Fraction(17, 19)
    print(f"{f} est déjà irréductible (PGCD = 1)")


def conversion_arrondi():
    """Démonstration des conversions et arrondis"""
    print("\n" + "="*60)
    print(" 5. CONVERSIONS ET ARRONDIS")
    print("="*60)
    
    f = Fraction(1, 3)
    print(f"Fraction : {f}")
    print(f"to_float()   → {f.to_float()}")
    print(f"round(2)     → {f.round(2)}")
    print(f"round(4)     → {f.round(4)}")
    print(f"round(10)    → {f.round(10)}")
    
    g = Fraction(22, 7)
    print(f"\nFraction : {g}")
    print(f"to_float()   → {g.to_float()}")
    print(f"round(5)     → {g.round(5)}")
    print(f"round(10)    → {g.round(10)}")
    print(f"(Valeur approchée de π = 3.1415926535...)")


def fractions_legendaires():
    """Démonstration de fractions mathématiquement remarquables"""
    print("\n" + "="*60)
    print(" 6. FRACTIONS REMARQUABLES")
    print("="*60)
    
    # Fractions A, B, C, D, Z de l'énoncé
    print("Fractions issues de l'exercice :")
    print("-"*40)
    
    # Fraction A
    f1 = Fraction(1, 1 + Fraction(1, 2 - Fraction(1, 3 + Fraction(1, 4 - Fraction(1, 5 + Fraction(1, 6))))))
    f2 = Fraction(1, 1 - Fraction(1, 2 + Fraction(1, 3 - Fraction(1, 4 + Fraction(1, 5 - Fraction(1, 6))))))
    A = f1 + f2
    print(f"Fraction A : {A} ≈ {A.to_float():.10f}")
    
    # Fraction B (via fraction continue)
    B = fraction_continue(7, 8)
    print(f"Fraction B : {B} ≈ {B.to_float():.10f}")
    
    # Fraction C
    C = fraction_continue(5, 8)
    print(f"Fraction C : {C} ≈ {C.to_float():.10f}")
    
    # Fraction D
    D = Fraction(10 + 20, Fraction(15 + 30, Fraction(20 + 40, Fraction(25 + 50, 45 + 90))))
    print(f"Fraction D : {D} = {D} (entier)")
    
    # Fraction Z
    Z = (326 + Fraction(12, 13)) / (164 - Fraction(7, 13))
    print(f"Fraction Z : {Z} = {Z} (entier)")


def erreurs():
    """Démonstration de la gestion des erreurs"""
    print("\n" + "="*60)
    print(" 7. GESTION DES ERREURS")
    print("="*60)
    
    try:
        f = Fraction(1, 0)
    except ZeroDivisionError as e:
        print(f"✅ Division par zéro interceptée : {e}")
    
    try:
        # Tentative d'opération avec un type invalide
        f = Fraction(1, 2) + "3"
    except TypeError as e:
        print(f"✅ Type invalide intercepté : {e}")


def menu():
    """Menu interactif simple"""
    print("\n" + "="*60)
    print(" DÉMONSTRATEUR DE FRACTIONS")
    print("="*60)
    print("1. Création de fractions")
    print("2. Opérations arithmétiques")
    print("3. Comparaisons exactes")
    print("4. Simplification automatique")
    print("5. Conversions et arrondis")
    print("6. Fractions remarquables")
    print("7. Gestion des erreurs")
    print("8. Tout exécuter")
    print("0. Quitter")
    print("-"*60)
    
    choix = input("Votre choix : ").strip()
    
    if choix == "1":
        introduction()
    elif choix == "2":
        operations_arithmetiques()
    elif choix == "3":
        comparaisons()
    elif choix == "4":
        simplification()
    elif choix == "5":
        conversion_arrondi()
    elif choix == "6":
        fractions_legendaires()
    elif choix == "7":
        erreurs()
    elif choix == "8":
        introduction()
        operations_arithmetiques()
        comparaisons()
        simplification()
        conversion_arrondi()
        fractions_legendaires()
        erreurs()
    elif choix == "0":
        print("\nAu revoir !")
        sys.exit(0)
    else:
        print("\nChoix invalide")


if __name__ == "__main__":
    # Mode automatique ou interactif
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        print("\n🔧 Mode automatique : exécution de tous les tests")
        introduction()
        operations_arithmetiques()
        comparaisons()
        simplification()
        conversion_arrondi()
        fractions_legendaires()
        erreurs()
        print("\n✅ Démonstration terminée.")
    else:
        while True:
            menu()
            input("\nAppuyez sur Entrée pour continuer...")