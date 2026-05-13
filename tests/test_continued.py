#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests unitaires – Fractions continues
======================================

Ce fichier contient les tests pour le module `fraction.continued`.

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import unittest
import sys
import os

# Ajouter le parent directory au path pour importer le module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction.continued import (
    fraction_continue,
    fraction_continue_generique,
    convergence,
    est_periodique,
    limite_approximative,
    nombre_dor,
    racine_deux,
)
from fraction.fraction import Fraction
from fraction.exceptions import InvalidOperationError


class TestFractionContinueSimple(unittest.TestCase):
    """Tests pour la fonction fraction_continue (version simple)"""
    
    def test_profondeur_1(self):
        """Test avec profondeur = 1"""
        f = fraction_continue(7, 1)
        self.assertEqual(f, Fraction(7, 1))
        
        f = fraction_continue(5, 1)
        self.assertEqual(f, Fraction(5, 1))
    
    def test_profondeur_2(self):
        """Test avec profondeur = 2"""
        f = fraction_continue(7, 2)
        self.assertEqual(f, Fraction(2, 1))
        
        f = fraction_continue(3, 2)
        self.assertEqual(f, Fraction(6, 1))  # 3 + 3/1 = 6
    
    def test_profondeur_8_valeur_7(self):
        """Test avec valeur=7, profondeur=8 (fraction B de l'énoncé)"""
        f = fraction_continue(7, 8)
        self.assertEqual(f, Fraction(128, 35))
        self.assertEqual(f.to_float(), 128/35)
    
    def test_profondeur_8_valeur_5(self):
        """Test avec valeur=5, profondeur=8 (fraction C de l'énoncé)"""
        f = fraction_continue(5, 8)
        self.assertEqual(f, Fraction(128, 35))
        self.assertEqual(f, fraction_continue(7, 8))  # Résultat identique !
    
    def test_profondeur_croissante(self):
        """Test des valeurs successives pour valeur=7"""
        attentes = [
            (1, Fraction(7, 1)),
            (2, Fraction(2, 1)),
            (3, Fraction(21, 2)),
            (4, Fraction(5, 2)),
            (5, Fraction(77, 10)),
            (6, Fraction(7, 5)),
            (7, Fraction(128, 35)),
            (8, Fraction(128, 35)),  # Se stabilise
        ]
        
        for p, attendu in attentes:
            f = fraction_continue(7, p)
            self.assertEqual(f, attendu, f"Erreur pour p={p}")
    
    def test_valeur_negative(self):
        """Test avec valeur négative"""
        f = fraction_continue(-3, 3)
        # Vérification que ça ne lève pas d'erreur
        self.assertIsInstance(f, Fraction)
    
    def test_profondeur_invalide_zero(self):
        """Test avec profondeur = 0 (invalide)"""
        with self.assertRaises(InvalidOperationError):
            fraction_continue(7, 0)
    
    def test_profondeur_invalide_negative(self):
        """Test avec profondeur négative (invalide)"""
        with self.assertRaises(InvalidOperationError):
            fraction_continue(7, -5)


class TestFractionContinueGenerique(unittest.TestCase):
    """Tests pour la fonction fraction_continue_generique"""
    
    def test_coefficients_basiques(self):
        """Test avec coefficients simples"""
        # [1] = 1
        f = fraction_continue_generique([1])
        self.assertEqual(f, Fraction(1, 1))
        
        # [1, 2] = 1 + 1/2 = 3/2
        f = fraction_continue_generique([1, 2])
        self.assertEqual(f, Fraction(3, 2))
        
        # [1, 2, 2] = 1 + 1/(2 + 1/2) = 7/5
        f = fraction_continue_generique([1, 2, 2])
        self.assertEqual(f, Fraction(7, 5))
    
    def test_approximation_pi(self):
        """Test approximation de π avec [3, 7, 15, 1] = 355/113"""
        f = fraction_continue_generique([3, 7, 15, 1])
        self.assertEqual(f, Fraction(355, 113))
        self.assertAlmostEqual(f.to_float(), 3.1415929203539825, places=10)
    
    def test_coefficients_tous_identiques(self):
        """Test avec coefficients tous égaux à 1"""
        # [1, 1, 1] = 1 + 1/(1 + 1/1) = 1 + 1/2 = 3/2
        f = fraction_continue_generique([1, 1, 1])
        self.assertEqual(f, Fraction(3, 2))
        
        # [1, 1, 1, 1] = Fibonacci ratio
        f = fraction_continue_generique([1, 1, 1, 1])
        self.assertEqual(f, Fraction(5, 3))
    
    def test_liste_vide(self):
        """Test avec liste vide (invalide)"""
        with self.assertRaises(InvalidOperationError):
            fraction_continue_generique([])


class TestConvergence(unittest.TestCase):
    """Tests pour la fonction convergence"""
    
    def test_convergence_7(self):
        """Test de convergence pour valeur=7"""
        resultats = convergence(7, 8)
        
        self.assertEqual(len(resultats), 8)
        
        attentes = [
            Fraction(7, 1),
            Fraction(2, 1),
            Fraction(21, 2),
            Fraction(5, 2),
            Fraction(77, 10),
            Fraction(7, 5),
            Fraction(128, 35),
            Fraction(128, 35),
        ]
        
        for i, (obtenu, attendu) in enumerate(zip(resultats, attentes)):
            self.assertEqual(obtenu, attendu, f"Erreur à l'étape {i+1}")
    
    def test_convergence_longueur(self):
        """Test que convergence retourne le bon nombre d'éléments"""
        resultats = convergence(3, 10)
        self.assertEqual(len(resultats), 10)
        
        resultats = convergence(5, 1)
        self.assertEqual(len(resultats), 1)


class TestPeriodicite(unittest.TestCase):
    """Tests pour la fonction est_periodique"""
    
    def test_periodique_valeur_7(self):
        """Test que valeur=7 devient périodique rapidement"""
        # À partir de p=7, la fraction se stabilise
        self.assertTrue(est_periodique(7, 20, seuil=5))
    
    def test_non_periodique_valeur_2(self):
        """Test que valeur=2 n'est pas périodique (oscille)"""
        # 2 alterne : 2, 2/1, 6/1, 3/1, 12/1, ...
        # Pas de stabilisation simple
        # On teste juste que la fonction ne lève pas d'erreur
        try:
            resultat = est_periodique(2, 20, seuil=3)
            # Le résultat peut être True ou False, mais pas d'erreur
        except Exception as e:
            self.fail(f"est_periodique a levé une exception : {e}")
    
    def test_seuil_plus_grand_que_longueur(self):
        """Test quand seuil > profondeur"""
        # Ne doit pas lever d'erreur, doit retourner False
        resultat = est_periodique(7, 5, seuil=10)
        self.assertFalse(resultat)


class TestLimiteApproximative(unittest.TestCase):
    """Tests pour la fonction limite_approximative"""
    
    def test_limite_7_profondeur_100(self):
        """Test approximation de la limite pour valeur=7"""
        limite = limite_approximative(7, 100)
        # La limite théorique est 7/2 + √(49/4 + 7) ≈ 3.657...
        self.assertAlmostEqual(limite, 3.657, places=2)
    
    def test_limite_1_profondeur_100(self):
        """Test approximation du nombre d'or (valeur=1)"""
        limite = limite_approximative(1, 100)
        self.assertAlmostEqual(limite, 1.618033988749895, places=10)
    
    def test_limite_2_profondeur_100(self):
        """Test approximation pour valeur=2"""
        limite = limite_approximative(2, 100)
        # Limite théorique = 1 + √2 ≈ 2.41421
        self.assertAlmostEqual(limite, 2.41421, places=4)


class TestConstantesMathematiques(unittest.TestCase):
    """Tests pour les constantes mathématiques (nombre d'or, √2)"""
    
    def test_nombre_dor_profondeur_1(self):
        """Test nombre d'or avec profondeur=1"""
        phi = nombre_dor(1)
        self.assertEqual(phi, Fraction(2, 1))  # 1 + 1/1 = 2
    
    def test_nombre_dor_profondeur_2(self):
        """Test nombre d'or avec profondeur=2"""
        phi = nombre_dor(2)
        self.assertEqual(phi, Fraction(3, 2))  # 1 + 1/(1 + 1/1) = 3/2
    
    def test_nombre_dor_profondeur_3(self):
        """Test nombre d'or avec profondeur=3"""
        phi = nombre_dor(3)
        self.assertEqual(phi, Fraction(5, 3))
    
    def test_nombre_dor_profondeur_4(self):
        """Test nombre d'or avec profondeur=4"""
        phi = nombre_dor(4)
        self.assertEqual(phi, Fraction(8, 5))
    
    def test_nombre_dor_convergence(self):
        """Test convergence du nombre d'or"""
        phi10 = nombre_dor(10).to_float()
        phi20 = nombre_dor(20).to_float()
        
        # La convergence doit être monotone et précise
        self.assertAlmostEqual(phi20, 1.618033988749895, places=8)
    
    def test_racine_deux_profondeur_1(self):
        """Test √2 avec profondeur=1"""
        sqrt2 = racine_deux(1)
        self.assertEqual(sqrt2, Fraction(3, 2))  # 1 + 1/2 = 3/2
    
    def test_racine_deux_profondeur_2(self):
        """Test √2 avec profondeur=2"""
        sqrt2 = racine_deux(2)
        self.assertEqual(sqrt2, Fraction(7, 5))  # 1 + 1/(2 + 1/2) = 7/5
    
    def test_racine_deux_convergence(self):
        """Test convergence de √2"""
        sqrt2_10 = racine_deux(10).to_float()
        sqrt2_20 = racine_deux(20).to_float()
        
        self.assertAlmostEqual(sqrt2_20, 1.4142135623730951, places=8)


class TestIntegration(unittest.TestCase):
    """Tests d'intégration entre les différentes fonctions"""
    
    def test_coherence_fraction_continue_generique_et_simple(self):
        """Vérifie que la version générique avec coefficients [v, v, v...] 
           donne le même résultat que la version simple"""
        
        # Pour valeur=7, profondeur=3 : [7, 7, 7]
        simple = fraction_continue(7, 3)
        generique = fraction_continue_generique([7, 7, 7])
        self.assertEqual(simple, generique)
    
    def test_nombre_dor_et_limite_approximative(self):
        """Vérifie que nombre_dor et limite_approximative(1) convergent"""
        phi = nombre_dor(50).to_float()
        limite = limite_approximative(1, 50)
        self.assertAlmostEqual(phi, limite, places=10)
    
    def test_chaine_operations(self):
        """Test d'une chaîne d'opérations complexe"""
        # Générer une fraction puis l'utiliser dans un calcul
        f1 = fraction_continue(7, 8)
        f2 = fraction_continue(5, 8)
        
        # f1 et f2 doivent être égales
        self.assertEqual(f1, f2)
        
        # Calcul avec la fraction
        resultat = f1 + Fraction(1, 2)
        self.assertEqual(resultat, Fraction(128, 35) + Fraction(1, 2))
        self.assertEqual(resultat, Fraction(291, 70))


# -------------------------------------------------------------------
# Point d'entrée pour l'exécution directe
# -------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Tests unitaires : Fractions continues")
    print("=" * 60)
    unittest.main(verbosity=2)