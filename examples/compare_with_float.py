#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Comparaison : Fractions exactes vs Flottants
--------------------------------------------
Ce script démontre pourquoi les calculs exacts avec fractions
sont supérieurs aux flottants pour les calculs financiers,
scientifiques ou nécessitant une précision absolue.

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import sys
import os

# Ajouter le parent directory au path pour importer le module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction.fraction import Fraction


def exemple_1_erreur_arrondi_classique():
    """Le célèbre 0.1 + 0.2 != 0.3"""
    print("\n" + "="*60)
    print(" 1. L'ERREUR CLASSIQUE : 0.1 + 0.2")
    print("="*60)
    
    # Avec des flottants
    a_float = 0.1
    b_float = 0.2
    somme_float = a_float + b_float
    
    print(f"Flottants :")
    print(f"  0.1 + 0.2 = {somme_float}")
    print(f"  Test : 0.1 + 0.2 == 0.3 ? {somme_float == 0.3}")
    print(f"  Représentation interne : {somme_float:.20f}")
    
    # Avec des fractions
    a_frac = Fraction(1, 10)
    b_frac = Fraction(1, 5)
    somme_frac = a_frac + b_frac
    
    print(f"\nFractions exactes :")
    print(f"  1/10 + 1/5 = {somme_frac}")
    print(f"  Test : 1/10 + 1/5 == 3/10 ? {somme_frac == Fraction(3, 10)}")
    print(f"  Valeur décimale : {somme_frac.to_float():.20f}")


def exemple_2_accumulation_d_erreurs():
    """L'accumulation d'erreurs dans les boucles"""
    print("\n" + "="*60)
    print(" 2. ACCUMULATION D'ERREURS (100 additions de 0.1)")
    print("="*60)
    
    # Avec des flottants
    total_float = 0.0
    for i in range(100):
        total_float += 0.1
    
    print(f"Flottants :")
    print(f"  100 × 0.1 = {total_float}")
    print(f"  Devrait être 10.0 → erreur = {abs(total_float - 10.0):.20f}")
    
    # Avec des fractions
    total_frac = Fraction(0, 1)
    for i in range(100):
        total_frac += Fraction(1, 10)
    
    print(f"\nFractions exactes :")
    print(f"  100 × 1/10 = {total_frac}")
    print(f"  = {total_frac.to_float():.20f} (exact)")


def exemple_3_soustraction_de_nombres_proches():
    """Perte de précision catastrophique"""
    print("\n" + "="*60)
    print(" 3. PERTE DE PRÉCISION (soustraction de nombres proches)")
    print("="*60)
    
    # Avec des flottants
    a_float = 1.0000000001
    b_float = 1.0000000000
    diff_float = a_float - b_float
    
    print(f"Flottants :")
    print(f"  {a_float} - {b_float} = {diff_float}")
    print(f"  Erreur relative : {abs(diff_float - 1e-10)/1e-10 * 100:.2f}%")
    
    # Avec des fractions
    a_frac = Fraction(10000000001, 10000000000)
    b_frac = Fraction(1, 1)
    diff_frac = a_frac - b_frac
    
    print(f"\nFractions exactes :")
    print(f"  {a_frac} - {b_frac} = {diff_frac}")
    print(f"  = {diff_frac.to_float():.20f} (exact)")


def exemple_4_comparaisons_egales():
    """Pourquoi les flottants ne sont pas fiables pour les comparaisons"""
    print("\n" + "="*60)
    print(" 4. COMPARAISONS : 1/3 × 3")
    print("="*60)
    
    # Avec des flottants
    tiers_float = 1.0 / 3.0
    produit_float = tiers_float * 3.0
    
    print(f"Flottants :")
    print(f"  1/3 = {tiers_float:.20f}")
    print(f"  (1/3) × 3 = {produit_float:.20f}")
    print(f"  (1/3) × 3 == 1 ? {produit_float == 1.0}")
    
    # Avec des fractions
    tiers_frac = Fraction(1, 3)
    produit_frac = tiers_frac * 3
    
    print(f"\nFractions exactes :")
    print(f"  1/3 = {tiers_frac}")
    print(f"  (1/3) × 3 = {produit_frac}")
    print(f"  (1/3) × 3 == 1 ? {produit_frac == Fraction(1, 1)}")


def exemple_5_boucle_infinie_ou_pas():
    """Boucle infinie à cause des flottants"""
    print("\n" + "="*60)
    print(" 5. PIÈGE : Boucle qui ne se termine pas")
    print("="*60)
    
    print("Flottants :")
    print("  Objectif : Ajouter 0.1 jusqu'à atteindre exactement 1.0")
    i_float = 0.0
    iterations_float = 0
    max_iter = 100
    
    while i_float != 1.0 and iterations_float < max_iter:
        i_float += 0.1
        iterations_float += 1
    
    if iterations_float >= max_iter:
        print(f"  ⚠️  Boucle non terminée après {max_iter} itérations")
        print(f"  Dernière valeur : {i_float:.20f}")
    else:
        print(f"  ✅ Terminée en {iterations_float} itérations")
    
    print("\nFractions exactes :")
    i_frac = Fraction(0, 1)
    iterations_frac = 0
    
    while i_frac != Fraction(1, 1) and iterations_frac < max_iter:
        i_frac += Fraction(1, 10)
        iterations_frac += 1
    
    print(f"  ✅ Terminée en {iterations_frac} itérations (exactement)")


def exemple_6_operations_en_serie():
    """Calculs en série : (1/3 + 1/3 + 1/3)"""
    print("\n" + "="*60)
    print(" 6. CALCULS EN SÉRIE : (1/3 + 1/3 + 1/3)")
    print("="*60)
    
    # Avec des flottants
    total_float = 0.0
    for _ in range(3):
        total_float += 1.0 / 3.0
    
    print(f"Flottants :")
    print(f"  (1/3 + 1/3 + 1/3) = {total_float:.20f}")
    print(f"  Différence avec 1 : {abs(total_float - 1.0):.20f}")
    
    # Avec des fractions
    total_frac = Fraction(1, 3) + Fraction(1, 3) + Fraction(1, 3)
    
    print(f"\nFractions exactes :")
    print(f"  (1/3 + 1/3 + 1/3) = {total_frac}")
    print(f"  = {total_frac.to_float():.20f} (exact)")


def exemple_7_fractions_irreductibles():
    """Simplification automatique vs flottants"""
    print("\n" + "="*60)
    print(" 7. SIMPLIFICATION AUTOMATIQUE")
    print("="*60)
    
    # Avec des flottants
    print("Flottants :")
    print("  Aucune simplification possible")
    print("  0.6666666666666666 ≠ 2/3 (conceptuellement)")
    
    # Avec des fractions
    f = Fraction(2, 3)
    print(f"\nFractions exactes :")
    print(f"  {f} reste {f}")
    print(f"  2/3 + 2/3 = {f + f}")
    print(f"  (2/3) × 3 = {f * 3}")


def exemple_8_cas_concret_bancaire():
    """Cas concret : répartition d'argent"""
    print("\n" + "="*60)
    print(" 8. CAS CONCRET : Répartition d'une somme d'argent")
    print("="*60)
    
    somme = 1000  # 1000€ à répartir
    
    # Avec des flottants (problème)
    parts_float = somme / 3
    total_float = parts_float * 3
    perte_float = somme - total_float
    
    print(f"Flottants :")
    print(f"  1000€ ÷ 3 = {parts_float:.10f}€")
    print(f"  3 × {parts_float:.10f} = {total_float:.10f}€")
    print(f"  Perte = {perte_float:.20f}€ (argent disparu !)")
    
    # Avec des fractions (exact)
    parts_frac = Fraction(somme, 3)
    total_frac = parts_frac * 3
    
    print(f"\nFractions exactes :")
    print(f"  1000€ ÷ 3 = {parts_frac}€")
    print(f"  3 × {parts_frac} = {total_frac}€")
    print(f"  Perte = 0€ (comptes exacts)")


def tableau_recapitulatif():
    """Tableau récapitulatif des différences"""
    print("\n" + "="*60)
    print(" RÉCAPITULATIF : Fraction vs Float")
    print("="*60)
    
    print("""
    ┌─────────────────────────┬──────────────────────┬──────────────────────┐
    │        Critère          │      Fraction        │       Float          │
    ├─────────────────────────┼──────────────────────┼──────────────────────┤
    │ Précision               │ Exacte (rationnel)   │ Approximative (64-bit)│
    │ Comparaisons            │ Fiables              │ Risquées             │
    │ Erreur d'arrondi        │ Aucune               │ Cumulative           │
    │ Simplification          │ Automatique          │ Impossible           │
    │ Boucles avec incréments │ Prédictibles         │ Peuvent boucler ∞     │
    │ Calculs financiers      │ Recommandé           │ À éviter             │
    │ Performance             │ Plus lent            │ Rapide               │
    │ Mémoire                 │ 2 entiers            │ 8 octets             │
    └─────────────────────────┴──────────────────────┴──────────────────────┘
    """)


def menu():
    """Menu interactif"""
    print("\n" + "="*60)
    print(" COMPARAISON : FRACTIONS EXACTES vs FLOTTANTS")
    print("="*60)
    print("1.  Erreur classique (0.1 + 0.2)")
    print("2.  Accumulation d'erreurs")
    print("3.  Perte de précision (soustraction)")
    print("4.  Comparaisons piégeuses")
    print("5.  Boucle infinie")
    print("6.  Calculs en série")
    print("7.  Simplification")
    print("8.  Cas concret (répartition d'argent)")
    print("9.  Tableau récapitulatif")
    print("10. Tout exécuter")
    print("0.  Quitter")
    print("-"*60)
    
    choix = input("Votre choix : ").strip()
    
    if choix == "1":
        exemple_1_erreur_arrondi_classique()
    elif choix == "2":
        exemple_2_accumulation_d_erreurs()
    elif choix == "3":
        exemple_3_soustraction_de_nombres_proches()
    elif choix == "4":
        exemple_4_comparaisons_egales()
    elif choix == "5":
        exemple_5_boucle_infinie_ou_pas()
    elif choix == "6":
        exemple_6_operations_en_serie()
    elif choix == "7":
        exemple_7_fractions_irreductibles()
    elif choix == "8":
        exemple_8_cas_concret_bancaire()
    elif choix == "9":
        tableau_recapitulatif()
    elif choix == "10":
        exemple_1_erreur_arrondi_classique()
        exemple_2_accumulation_d_erreurs()
        exemple_3_soustraction_de_nombres_proches()
        exemple_4_comparaisons_egales()
        exemple_5_boucle_infinie_ou_pas()
        exemple_6_operations_en_serie()
        exemple_7_fractions_irreductibles()
        exemple_8_cas_concret_bancaire()
        tableau_recapitulatif()
    elif choix == "0":
        print("\nAu revoir !")
        sys.exit(0)
    else:
        print("\nChoix invalide")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        print("\n🔬 Mode automatique : démonstration des limites des flottants")
        exemple_1_erreur_arrondi_classique()
        exemple_2_accumulation_d_erreurs()
        exemple_3_soustraction_de_nombres_proches()
        exemple_4_comparaisons_egales()
        exemple_5_boucle_infinie_ou_pas()
        exemple_6_operations_en_serie()
        exemple_7_fractions_irreductibles()
        exemple_8_cas_concret_bancaire()
        tableau_recapitulatif()
        print("\n✅ Démonstration terminée.")
    else:
        while True:
            menu()
            input("\nAppuyez sur Entrée pour continuer...")