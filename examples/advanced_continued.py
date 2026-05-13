#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Démonstrateur avancé : Fractions continues
------------------------------------------
Ce script explore les propriétés des fractions continues générées
par la fonction fraction_continue(valeur, profondeur).

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import sys
import os

# Ajouter le parent directory au path pour importer le module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction.fraction import Fraction
from fraction.continued import fraction_continue


def analyse_convergence(valeur: int, profondeur_max: int = 10):
    """
    Analyse la convergence d'une fraction continue.
    Affiche les valeurs successives et leur différence avec la limite théorique.
    """
    print(f"\n{'='*60}")
    print(f"Analyse de convergence pour valeur = {valeur}")
    print(f"{'='*60}")
    
    valeurs = []
    for p in range(1, profondeur_max + 1):
        f = fraction_continue(valeur, p)
        valeurs.append(f)
        print(f"p={p:2d} : {f} ≈ {f.to_float():.10f}")
    
    # Calcul des différences entre étapes consécutives
    print(f"\n--- Différences entre étapes consécutives ---")
    for i in range(1, len(valeurs)):
        diff = valeurs[i] - valeurs[i-1]
        print(f"Δ({i}→{i+1}) = {diff} ≈ {diff.to_float():.10f}")
    
    return valeurs


def comparaison_valeurs():
    """
    Compare les fractions continues pour différentes valeurs de base.
    """
    print(f"\n{'='*60}")
    print("Comparaison pour différentes valeurs de base (profondeur = 8)")
    print(f"{'='*60}")
    
    for v in [2, 3, 5, 7, 10]:
        f = fraction_continue(v, 8)
        print(f"valeur={v:2d} : {f} ≈ {f.to_float():.10f}")


def recherche_seuil(valeur: int, cible: float, max_depth: int = 20):
    """
    Trouve la profondeur minimale pour approcher une cible avec une précision donnée.
    """
    print(f"\n{'='*60}")
    print(f"Recherche de seuil pour valeur={valeur}, cible={cible}")
    print(f"{'='*60}")
    
    for p in range(1, max_depth + 1):
        f = fraction_continue(valeur, p)
        erreur = abs(f.to_float() - cible)
        print(f"p={p:2d} : {f} ≈ {f.to_float():.10f} | erreur = {erreur:.10f}")
        if erreur < 1e-6:
            print(f"\n✅ Seuil atteint à p={p} (erreur < 1e-6)")
            return p
    
    print(f"\n⚠️  Seuil non atteint après {max_depth} étapes")
    return None


def analyse_rationnels(valeur: int, profondeur: int):
    """
    Analyse détaillée d'une fraction continue spécifique.
    Décompose la fraction en étapes intermédiaires.
    """
    print(f"\n{'='*60}")
    print(f"Analyse détaillée : valeur={valeur}, profondeur={profondeur}")
    print(f"{'='*60}")
    
    # Reconstruire étape par étape manuellement
    total = 0
    frac = Fraction(1, 1)
    
    print(f"\n--- Construction pas à pas ---")
    for i in range(1, profondeur + 1):
        total += valeur
        frac = Fraction(total, frac)
        print(f"Étape {i:2d} : total={total:3d} | frac={frac} ≈ {frac.to_float():.10f}")
    
    print(f"\n--- Vérification par fonction dédiée ---")
    f = fraction_continue(valeur, profondeur)
    print(f"Résultat : {f} ≈ {f.to_float():.10f}")
    print(f"Égalité avec reconstruction manuelle : {f == frac}")


def proprietes_mathematiques(valeur: int, profondeur: int):
    """
    Met en évidence certaines propriétés mathématiques des fractions continues.
    """
    f = fraction_continue(valeur, profondeur)
    
    print(f"\n{'='*60}")
    print(f"Propriétés mathématiques")
    print(f"{'='*60}")
    
    # Valeur exacte
    print(f"Fraction exacte : {f}")
    
    # Valeur approximative
    print(f"Valeur décimale : {f.to_float():.15f}")
    
    # Simplification
    print(f"Numérateur  : {f.num:,}")
    print(f"Dénominateur: {f.den:,}")
    
    # Facteurs premiers (simplification)
    if f.num > 1 and f.den > 1:
        print(f"PGCD(num, den) = 1 → fraction irréductible")


def benchmark_performance():
    """
    Benchmark simple des performances de fraction_continue.
    """
    import time
    
    print(f"\n{'='*60}")
    print("Benchmark des performances")
    print(f"{'='*60}")
    
    profondeurs = [10, 50, 100, 200]
    
    for p in profondeurs:
        start = time.time()
        for _ in range(100):
            _ = fraction_continue(7, p)
        end = time.time()
        print(f"Profondeur={p:3d} : {100} générations en {(end-start)*1000:.2f} ms")
        print(f"  → {(end-start)/100*1000:.4f} ms par fraction")


def menu():
    """
    Menu interactif pour explorer les différentes fonctionnalités.
    """
    print("\n" + "="*60)
    print(" EXPLORATEUR DE FRACTIONS CONTINUES")
    print("="*60)
    print("1. Analyser la convergence")
    print("2. Comparer différentes valeurs")
    print("3. Rechercher un seuil de précision")
    print("4. Analyser une fraction spécifique")
    print("5. Propriétés mathématiques")
    print("6. Benchmark performance")
    print("7. Tout exécuter")
    print("0. Quitter")
    print("-"*60)
    
    choix = input("Votre choix : ").strip()
    
    if choix == "1":
        v = int(input("Valeur de base (ex: 7) : ") or "7")
        p = int(input("Profondeur max (ex: 10) : ") or "10")
        analyse_convergence(v, p)
    elif choix == "2":
        comparaison_valeurs()
    elif choix == "3":
        v = int(input("Valeur de base (ex: 7) : ") or "7")
        c = float(input("Cible (ex: 3.657) : ") or "3.657")
        recherche_seuil(v, c)
    elif choix == "4":
        v = int(input("Valeur de base : ") or "7")
        p = int(input("Profondeur : ") or "8")
        analyse_rationnels(v, p)
    elif choix == "5":
        v = int(input("Valeur de base : ") or "7")
        p = int(input("Profondeur : ") or "8")
        proprietes_mathematiques(v, p)
    elif choix == "6":
        benchmark_performance()
    elif choix == "7":
        analyse_convergence(7, 8)
        comparaison_valeurs()
        recherche_seuil(7, 3.657)
        analyse_rationnels(7, 8)
        proprietes_mathematiques(7, 8)
        benchmark_performance()
    elif choix == "0":
        print("Au revoir !")
        sys.exit(0)
    else:
        print("Choix invalide")


if __name__ == "__main__":
    # Mode interactif ou exécution automatique
    if len(sys.argv) > 1 and sys.argv[1] == "--auto":
        print("Mode automatique : exécution de tous les tests")
        analyse_convergence(7, 8)
        comparaison_valeurs()
        recherche_seuil(7, 3.657)
        analyse_rationnels(7, 8)
        proprietes_mathematiques(7, 8)
        benchmark_performance()
    else:
        while True:
            menu()
            input("\nAppuyez sur Entrée pour continuer...")