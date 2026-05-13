#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests unitaires – Core mathématique
=====================================

Ce fichier contient les tests pour le module `fraction.core`
qui regroupe les fonctions mathématiques de base :
- PGCD (algorithme d'Euclide)
- Euclide étendu
- Simplification de fractions
- Validations et transformations
- Comparaisons exactes
- Arrondis

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import unittest
import sys
import os

# Ajouter le parent directory au path pour importer le module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction.core import (
    pgcd,
    pgcd_etendu,
    simplifier,
    est_entier,
    est_unitaire,
    valeur_absolue,
    oppose,
    inverse,
    comparer,
    arrondir,
)
from fraction.exceptions import DivisionByZeroError


class TestPGCD(unittest.TestCase):
    """Tests pour la fonction pgcd (algorithme d'Euclide)"""
    
    def test_pgcd_nombres_positifs(self):
        """Test PGCD avec nombres positifs"""
        self.assertEqual(pgcd(12, 8), 4)
        self.assertEqual(pgcd(17, 19), 1)
        self.assertEqual(pgcd(100, 25), 25)
        self.assertEqual(pgcd(48, 18), 6)
    
    def test_pgcd_avec_zero(self):
        """Test PGCD avec zéro"""
        self.assertEqual(pgcd(0, 5), 5)
        self.assertEqual(pgcd(5, 0), 5)
        self.assertEqual(pgcd(0, 0), 0)
    
    def test_pgcd_nombres_negatifs(self):
        """Test PGCD avec nombres négatifs (doit retourner positif)"""
        self.assertEqual(pgcd(-12, 8), 4)
        self.assertEqual(pgcd(12, -8), 4)
        self.assertEqual(pgcd(-12, -8), 4)
    
    def test_pgcd_nombres_premiers_entre_eux(self):
        """Test PGCD avec nombres premiers entre eux"""
        self.assertEqual(pgcd(13, 17), 1)
        self.assertEqual(pgcd(21, 22), 1)
        self.assertEqual(pgcd(35, 36), 1)
    
    def test_pgcd_grands_nombres(self):
        """Test PGCD avec grands nombres"""
        self.assertEqual(pgcd(12345678, 87654321), 3)
        self.assertEqual(pgcd(10**6, 10**5), 10**5)


class TestPGCDEtendu(unittest.TestCase):
    """Tests pour la fonction pgcd_etendu (coefficients de Bézout)"""
    
    def test_etendu_cas_simple(self):
        """Test Euclide étendu avec cas simple"""
        g, x, y = pgcd_etendu(12, 8)
        self.assertEqual(g, 4)
        self.assertEqual(12 * x + 8 * y, g)
    
    def test_etendu_nombres_premiers(self):
        """Test Euclide étendu avec nombres premiers entre eux"""
        g, x, y = pgcd_etendu(17, 19)
        self.assertEqual(g, 1)
        self.assertEqual(17 * x + 19 * y, g)
    
    def test_etendu_avec_zero(self):
        """Test Euclide étendu avec zéro"""
        g, x, y = pgcd_etendu(5, 0)
        self.assertEqual(g, 5)
        self.assertEqual(5 * x + 0 * y, g)
        
        g, x, y = pgcd_etendu(0, 5)
        self.assertEqual(g, 5)
    
    def test_etendu_nombres_negatifs(self):
        """Test Euclide étendu avec nombres négatifs"""
        g, x, y = pgcd_etendu(-12, 8)
        self.assertEqual(g, 4)
        self.assertEqual((-12) * x + 8 * y, g)
        
        g, x, y = pgcd_etendu(12, -8)
        self.assertEqual(g, 4)
    
    def test_etendu_identite_bezout(self):
        """Vérifie l'identité de Bézout : a*x + b*y = pgcd(a,b)"""
        test_cases = [(15, 6), (21, 14), (100, 35), (7, 13)]
        for a, b in test_cases:
            g, x, y = pgcd_etendu(a, b)
            self.assertEqual(a * x + b * y, g,
                           f"Échec pour a={a}, b={b}: {a}*{x} + {b}*{y} = {a*x+b*y} != {g}")


class TestSimplifier(unittest.TestCase):
    """Tests pour la fonction simplifier"""
    
    def test_simplifier_fraction_classique(self):
        """Test simplification de fractions classiques"""
        self.assertEqual(simplifier(4, 8), (1, 2))
        self.assertEqual(simplifier(6, 9), (2, 3))
        self.assertEqual(simplifier(12, 18), (2, 3))
        self.assertEqual(simplifier(25, 100), (1, 4))
    
    def test_simplifier_fraction_deja_simplifiee(self):
        """Test fraction déjà simplifiée"""
        self.assertEqual(simplifier(3, 4), (3, 4))
        self.assertEqual(simplifier(17, 19), (17, 19))
    
    def test_simplifier_avec_negatif(self):
        """Test simplification avec signes négatifs (normalisation)"""
        # Le dénominateur doit devenir positif
        self.assertEqual(simplifier(6, -8), (-3, 4))
        self.assertEqual(simplifier(-6, 8), (-3, 4))
        self.assertEqual(simplifier(-6, -8), (3, 4))
    
    def test_simplifier_numerateur_nul(self):
        """Test simplification avec numérateur nul"""
        self.assertEqual(simplifier(0, 5), (0, 1))
        self.assertEqual(simplifier(0, -5), (0, 1))
        self.assertEqual(simplifier(0, 1), (0, 1))
    
    def test_simplifier_denominateur_un(self):
        """Test avec dénominateur = 1"""
        self.assertEqual(simplifier(5, 1), (5, 1))
        self.assertEqual(simplifier(-5, 1), (-5, 1))
    
    def test_simplifier_denominateur_negatif_un(self):
        """Test avec dénominateur = -1"""
        self.assertEqual(simplifier(5, -1), (-5, 1))
    
    def test_simplifier_denominateur_zero(self):
        """Test erreur avec dénominateur nul"""
        with self.assertRaises(DivisionByZeroError):
            simplifier(1, 0)


class TestValidations(unittest.TestCase):
    """Tests pour les fonctions de validation (est_entier, est_unitaire)"""
    
    def test_est_entier(self):
        """Test est_entier"""
        self.assertTrue(est_entier(4, 2))
        self.assertTrue(est_entier(6, 3))
        self.assertTrue(est_entier(0, 5))
        self.assertTrue(est_entier(-4, 2))
        
        self.assertFalse(est_entier(3, 2))
        self.assertFalse(est_entier(1, 3))
    
    def test_est_entier_denominateur_zero(self):
        """Test est_entier avec dénominateur nul (doit retourner False)"""
        self.assertFalse(est_entier(1, 0))
    
    def test_est_unitaire(self):
        """Test est_unitaire (numérateur = ±1)"""
        self.assertTrue(est_unitaire(1, 2))
        self.assertTrue(est_unitaire(1, 5))
        self.assertTrue(est_unitaire(-1, 3))
        self.assertTrue(est_unitaire(1, 1))
        
        self.assertFalse(est_unitaire(2, 3))
        self.assertFalse(est_unitaire(0, 1))
        self.assertFalse(est_unitaire(-2, 5))


class TestTransformations(unittest.TestCase):
    """Tests pour les transformations : valeur_absolue, oppose, inverse"""
    
    def test_valeur_absolue(self):
        """Test valeur absolue d'une fraction"""
        self.assertEqual(valeur_absolue(3, 4), (3, 4))
        self.assertEqual(valeur_absolue(-3, 4), (3, 4))
        self.assertEqual(valeur_absolue(-6, -8), (3, 4))
        self.assertEqual(valeur_absolue(0, 5), (0, 1))
    
    def test_oppose(self):
        """Test opposé d'une fraction"""
        self.assertEqual(oppose(3, 4), (-3, 4))
        self.assertEqual(oppose(-3, 4), (3, 4))
        self.assertEqual(oppose(0, 5), (0, 1))
    
    def test_inverse(self):
        """Test inverse d'une fraction"""
        self.assertEqual(inverse(3, 4), (4, 3))
        self.assertEqual(inverse(-2, 5), (-5, 2))
        self.assertEqual(inverse(1, 3), (3, 1))
        self.assertEqual(inverse(5, 1), (1, 5))
    
    def test_inverse_fraction_nulle(self):
        """Test inverse d'une fraction nulle (doit lever une erreur)"""
        with self.assertRaises(DivisionByZeroError):
            inverse(0, 1)
        with self.assertRaises(DivisionByZeroError):
            inverse(0, 5)
    
    def test_inverse_apres_simplification(self):
        """Test que l'inverse est correctement simplifié"""
        num, den = inverse(4, 6)
        self.assertEqual((num, den), (3, 2))  # 4/6 = 2/3 → inverse = 3/2


class TestComparateur(unittest.TestCase):
    """Tests pour la fonction comparer (comparaison exacte)"""
    
    def test_comparer_positif(self):
        """Test comparaison de fractions positives"""
        # 1/2 > 1/3
        self.assertEqual(comparer(1, 2, 1, 3), 1)
        # 1/3 < 2/5
        self.assertEqual(comparer(1, 3, 2, 5), -1)
        # 1/2 == 2/4
        self.assertEqual(comparer(1, 2, 2, 4), 0)
    
    def test_comparer_negatif(self):
        """Test comparaison avec fractions négatives"""
        # -1/2 < -1/3
        self.assertEqual(comparer(-1, 2, -1, 3), -1)
        # -1/3 > -1/2
        self.assertEqual(comparer(-1, 3, -1, 2), 1)
    
    def test_comparer_melange_signe(self):
        """Test comparaison avec signes mélangés"""
        # Négatif vs Positif
        self.assertEqual(comparer(-1, 2, 1, 3), -1)
        self.assertEqual(comparer(1, 2, -1, 3), 1)
    
    def test_comparer_egalite_apres_simplification(self):
        """Test égalité après simplification"""
        self.assertEqual(comparer(2, 4, 3, 6), 0)
        self.assertEqual(comparer(-2, 4, 1, -2), 0)
    
    def test_comparer_avec_zero(self):
        """Test comparaison avec zéro"""
        # 0 vs 1/2
        self.assertEqual(comparer(0, 1, 1, 2), -1)
        self.assertEqual(comparer(1, 2, 0, 1), 1)
        # 0 vs 0
        self.assertEqual(comparer(0, 1, 0, 1), 0)
        self.assertEqual(comparer(0, 1, 0, 5), 0)


class TestArrondi(unittest.TestCase):
    """Tests pour la fonction arrondir"""
    
    def test_arrondi_base(self):
        """Test arrondi de base"""
        self.assertEqual(arrondir(1, 2, 0), 1.0)
        self.assertEqual(arrondir(1, 3, 2), 0.33)
        self.assertEqual(arrondir(2, 3, 2), 0.67)
    
    def test_arrondi_sans_decimales(self):
        """Test arrondi avec n=0 (défaut)"""
        self.assertEqual(arrondir(1, 2), 1.0)
        self.assertEqual(arrondir(4, 3), 1.0)
    
    def test_arrondi_negatif(self):
        """Test arrondi avec fractions négatives"""
        self.assertEqual(arrondir(-1, 2, 1), -0.5)
        self.assertEqual(arrondir(-1, 3, 2), -0.33)
    
    def test_arrondi_grandes_decimales(self):
        """Test arrondi avec beaucoup de décimales"""
        resultat = arrondir(1, 7, 10)
        self.assertAlmostEqual(resultat, 0.1428571429, places=10)


class TestIntegrationCore(unittest.TestCase):
    """Tests d'intégration entre les fonctions du module core"""
    
    def test_chaine_simplifier_comparer(self):
        """Test chaînage simplifier puis comparer"""
        num1, den1 = simplifier(6, 9)      # 2/3
        num2, den2 = simplifier(8, 12)     # 2/3
        
        # Doivent être égales
        self.assertEqual(comparer(num1, den1, num2, den2), 0)
    
    def test_chaine_oppose_inverse(self):
        """Test chaînage oppose puis inverse"""
        num, den = oppose(3, 4)  # -3/4
        num, den = inverse(num, den)  # -4/3
        
        self.assertEqual((num, den), (-4, 3))
    
    def test_valeur_absolue_est_unitaire(self):
        """Test combinaison valeur_absolue et est_unitaire"""
        num, den = valeur_absolue(-1, 3)
        self.assertTrue(est_unitaire(num, den))
        
        num, den = valeur_absolue(-2, 5)
        self.assertFalse(est_unitaire(num, den))


# -------------------------------------------------------------------
# Point d'entrée pour l'exécution directe
# -------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Tests unitaires : Core mathématique")
    print("=" * 60)
    unittest.main(verbosity=2)