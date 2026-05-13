#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Tests unitaires – Classe Fraction
==================================

Ce fichier contient les tests pour la classe `fraction.Fraction` :
- Création et simplification automatique
- Opérateurs arithmétiques (+, -, *, /)
- Opérateurs de comparaison (<, >, ==)
- Conversions (__str__, __repr__, to_float, round)
- Méthodes utilitaires (inverse, est_entier, etc.)
- Gestion des erreurs et exceptions

Auteur : Étudiant L1 Informatique
Date : 2026
"""

import unittest
import sys
import os

# Ajouter le parent directory au path pour importer le module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fraction.fraction import Fraction
from fraction.exceptions import DivisionByZeroError, InvalidOperationError


class TestFractionCreation(unittest.TestCase):
    """Tests pour la création et la simplification des fractions"""
    
    def test_creation_base(self):
        """Test création de fractions simples"""
        f = Fraction(1, 2)
        self.assertEqual(f.num, 1)
        self.assertEqual(f.den, 2)
        
        f = Fraction(3, 4)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)
    
    def test_creation_denominateur_defaut(self):
        """Test création avec dénominateur par défaut (=1)"""
        f = Fraction(5)
        self.assertEqual(f.num, 5)
        self.assertEqual(f.den, 1)
        
        f = Fraction(-3)
        self.assertEqual(f.num, -3)
        self.assertEqual(f.den, 1)
    
    def test_simplification_automatique(self):
        """Test simplification automatique à la création"""
        f = Fraction(4, 8)
        self.assertEqual(f.num, 1)
        self.assertEqual(f.den, 2)
        
        f = Fraction(6, 9)
        self.assertEqual(f.num, 2)
        self.assertEqual(f.den, 3)
        
        f = Fraction(12, 18)
        self.assertEqual(f.num, 2)
        self.assertEqual(f.den, 3)
    
    def test_simplification_avec_negatifs(self):
        """Test simplification avec signes négatifs"""
        f = Fraction(6, -8)
        self.assertEqual(f.num, -3)
        self.assertEqual(f.den, 4)
        
        f = Fraction(-6, 8)
        self.assertEqual(f.num, -3)
        self.assertEqual(f.den, 4)
        
        f = Fraction(-6, -8)
        self.assertEqual(f.num, 3)
        self.assertEqual(f.den, 4)
    
    def test_fraction_nulle(self):
        """Test fraction avec numérateur nul"""
        f = Fraction(0, 5)
        self.assertEqual(f.num, 0)
        self.assertEqual(f.den, 1)
        
        f = Fraction(0, -3)
        self.assertEqual(f.num, 0)
        self.assertEqual(f.den, 1)
    
    def test_creation_erreur_denominateur_nul(self):
        """Test erreur avec dénominateur nul"""
        with self.assertRaises(DivisionByZeroError):
            Fraction(1, 0)


class TestFractionOperations(unittest.TestCase):
    """Tests pour les opérations arithmétiques"""
    
    def setUp(self):
        """Préparation des fractions pour les tests"""
        self.a = Fraction(1, 2)
        self.b = Fraction(1, 3)
    
    def test_addition_fractions(self):
        """Test addition de deux fractions"""
        resultat = self.a + self.b
        self.assertEqual(resultat, Fraction(5, 6))
    
    def test_addition_avec_entier(self):
        """Test addition fraction + entier"""
        resultat = self.a + 2
        self.assertEqual(resultat, Fraction(5, 2))
        
        resultat = 2 + self.a  # __radd__
        self.assertEqual(resultat, Fraction(5, 2))
    
    def test_soustraction_fractions(self):
        """Test soustraction de deux fractions"""
        resultat = self.a - self.b
        self.assertEqual(resultat, Fraction(1, 6))
        
        resultat = self.b - self.a
        self.assertEqual(resultat, Fraction(-1, 6))
    
    def test_soustraction_avec_entier(self):
        """Test soustraction fraction - entier"""
        resultat = self.a - 1
        self.assertEqual(resultat, Fraction(-1, 2))
        
        resultat = 1 - self.a  # __rsub__
        self.assertEqual(resultat, Fraction(1, 2))
    
    def test_multiplication_fractions(self):
        """Test multiplication de deux fractions"""
        resultat = self.a * self.b
        self.assertEqual(resultat, Fraction(1, 6))
        
        resultat = Fraction(2, 3) * Fraction(3, 4)
        self.assertEqual(resultat, Fraction(1, 2))
    
    def test_multiplication_avec_entier(self):
        """Test multiplication fraction × entier"""
        resultat = self.a * 4
        self.assertEqual(resultat, Fraction(2, 1))
        
        resultat = 4 * self.a  # __rmul__
        self.assertEqual(resultat, Fraction(2, 1))
    
    def test_division_fractions(self):
        """Test division de deux fractions"""
        resultat = self.a / self.b
        self.assertEqual(resultat, Fraction(3, 2))
        
        resultat = Fraction(2, 3) / Fraction(4, 5)
        self.assertEqual(resultat, Fraction(10, 12))
        self.assertEqual(resultat, Fraction(5, 6))  # Simplifiée
    
    def test_division_avec_entier(self):
        """Test division fraction ÷ entier"""
        resultat = self.a / 2
        self.assertEqual(resultat, Fraction(1, 4))
        
        resultat = 2 / self.a  # __rtruediv__
        self.assertEqual(resultat, Fraction(4, 1))
    
    def test_division_par_zero(self):
        """Test division par zéro"""
        with self.assertRaises(DivisionByZeroError):
            self.a / 0
        
        with self.assertRaises(DivisionByZeroError):
            self.a / Fraction(0, 1)
    
    def test_chaine_operations(self):
        """Test chaîne d'opérations"""
        resultat = (self.a + self.b) * Fraction(2, 1) - self.a
        # (1/2 + 1/3) = 5/6
        # 5/6 × 2 = 10/6 = 5/3
        # 5/3 - 1/2 = 10/6 - 3/6 = 7/6
        self.assertEqual(resultat, Fraction(7, 6))


class TestFractionComparaisons(unittest.TestCase):
    """Tests pour les opérateurs de comparaison"""
    
    def test_egalite(self):
        """Test égalité entre fractions"""
        self.assertEqual(Fraction(1, 2), Fraction(2, 4))
        self.assertEqual(Fraction(-3, 4), Fraction(3, -4))
        self.assertEqual(Fraction(0, 1), Fraction(0, 5))
        self.assertEqual(Fraction(1, 2) == Fraction(1, 3), False)
    
    def test_egalite_avec_entier(self):
        """Test égalité fraction == entier"""
        self.assertEqual(Fraction(2, 1), 2)
        self.assertEqual(Fraction(4, 2), 2)
        self.assertEqual(Fraction(3, 2) == 1, False)
    
    def test_egalite_avec_float_retourne_false(self):
        """Test égalité avec float (non supportée, retourne False)"""
        # Par conception, Fraction(1,2) == 0.5 retourne False
        # car la comparaison directe avec float n'est pas implémentée
        self.assertNotEqual(Fraction(1, 2), 0.5)
    
    def test_inferieur(self):
        """Test opérateur <"""
        self.assertTrue(Fraction(1, 3) < Fraction(1, 2))
        self.assertTrue(Fraction(1, 2) < Fraction(3, 4))
        self.assertFalse(Fraction(3, 4) < Fraction(1, 2))
    
    def test_inferieur_avec_entier(self):
        """Test inférieur avec entier"""
        self.assertTrue(Fraction(1, 2) < 1)
        self.assertTrue(Fraction(3, 2) < 2)
        self.assertFalse(Fraction(3, 2) < 1)
    
    def test_superieur(self):
        """Test opérateur >"""
        self.assertTrue(Fraction(1, 2) > Fraction(1, 3))
        self.assertTrue(Fraction(3, 4) > Fraction(1, 2))
        self.assertFalse(Fraction(1, 3) > Fraction(1, 2))
    
    def test_superieur_avec_entier(self):
        """Test supérieur avec entier"""
        self.assertTrue(Fraction(3, 2) > 1)
        self.assertTrue(Fraction(5, 4) > 1)
        self.assertFalse(Fraction(1, 2) > 1)
    
    def test_comparaison_fractions_negatives(self):
        """Test comparaison avec fractions négatives"""
        self.assertTrue(Fraction(-1, 2) < Fraction(1, 3))
        self.assertTrue(Fraction(-1, 2) < Fraction(-1, 3))
        self.assertTrue(Fraction(-1, 3) > Fraction(-1, 2))
    
    def test_type_invalide_comparaison(self):
        """Test comparaison avec type invalide (doit lever une exception)"""
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) < "3"


class TestFractionConversions(unittest.TestCase):
    """Tests pour les conversions (__str__, __repr__, to_float, round)"""
    
    def test_str_representation(self):
        """Test représentation string"""
        self.assertEqual(str(Fraction(1, 2)), "1/2")
        self.assertEqual(str(Fraction(3, 1)), "3")
        self.assertEqual(str(Fraction(-2, 3)), "-2/3")
        self.assertEqual(str(Fraction(4, 8)), "1/2")  # Simplifiée
    
    def test_repr_representation(self):
        """Test représentation technique"""
        self.assertEqual(repr(Fraction(1, 2)), "Fraction(1, 2)")
        self.assertEqual(repr(Fraction(4, 8)), "Fraction(1, 2)")
        self.assertEqual(repr(Fraction(-3, 4)), "Fraction(-3, 4)")
    
    def test_to_float(self):
        """Test conversion en flottant"""
        self.assertEqual(Fraction(1, 2).to_float(), 0.5)
        self.assertEqual(Fraction(1, 3).to_float(), 1/3)
        self.assertAlmostEqual(Fraction(1, 7).to_float(), 0.142857142857, places=10)
    
    def test_round(self):
        """Test arrondi"""
        self.assertEqual(Fraction(1, 3).round(2), 0.33)
        self.assertEqual(Fraction(2, 3).round(2), 0.67)
        self.assertEqual(Fraction(1, 2).round(0), 1.0)
    
    def test_round_sans_parametre(self):
        """Test arrondi sans paramètre (n=0 par défaut)"""
        self.assertEqual(Fraction(1, 2).round(), 1.0)
        self.assertEqual(Fraction(1, 3).round(), 0.0)


class TestFractionMethodesUtilitaires(unittest.TestCase):
    """Tests pour les méthodes utilitaires"""
    
    def test_inverse(self):
        """Test inverse de fraction"""
        f = Fraction(3, 4).inverse()
        self.assertEqual(f, Fraction(4, 3))
        
        f = Fraction(2, 1).inverse()
        self.assertEqual(f, Fraction(1, 2))
        
        f = Fraction(-5, 3).inverse()
        self.assertEqual(f, Fraction(-3, 5))
    
    def test_inverse_fraction_nulle(self):
        """Test inverse de fraction nulle (doit lever une erreur)"""
        with self.assertRaises(DivisionByZeroError):
            Fraction(0, 1).inverse()
    
    def test_est_entier(self):
        """Test est_entier"""
        self.assertTrue(Fraction(4, 2).est_entier())
        self.assertTrue(Fraction(6, 3).est_entier())
        self.assertTrue(Fraction(0, 1).est_entier())
        self.assertFalse(Fraction(3, 2).est_entier())
        self.assertFalse(Fraction(1, 3).est_entier())
    
    def test_est_unitaire(self):
        """Test est_unitaire"""
        self.assertTrue(Fraction(1, 2).est_unitaire())
        self.assertTrue(Fraction(1, 5).est_unitaire())
        self.assertTrue(Fraction(-1, 3).est_unitaire())
        self.assertFalse(Fraction(2, 3).est_unitaire())
        self.assertFalse(Fraction(0, 1).est_unitaire())
    
    def test_valeur_absolue(self):
        """Test valeur absolue"""
        f = Fraction(-3, 4).valeur_absolue()
        self.assertEqual(f, Fraction(3, 4))
        
        f = Fraction(3, 4).valeur_absolue()
        self.assertEqual(f, Fraction(3, 4))
        
        f = Fraction(0, 1).valeur_absolue()
        self.assertEqual(f, Fraction(0, 1))


class TestFractionHash(unittest.TestCase):
    """Tests pour le hash (utilisation dans sets/dictionnaires)"""
    
    def test_hash_egalite(self):
        """Test que deux fractions égales ont le même hash"""
        f1 = Fraction(1, 2)
        f2 = Fraction(2, 4)
        f3 = Fraction(1, 3)
        
        self.assertEqual(hash(f1), hash(f2))
        self.assertNotEqual(hash(f1), hash(f3))
    
    def test_utilisation_dans_set(self):
        """Test utilisation de Fraction dans un set"""
        s = {Fraction(1, 2), Fraction(2, 4), Fraction(1, 3)}
        # Fraction(1,2) et Fraction(2,4) sont considérées identiques
        self.assertEqual(len(s), 2)
        self.assertIn(Fraction(1, 2), s)
        self.assertIn(Fraction(1, 3), s)
    
    def test_utilisation_dans_dict(self):
        """Test utilisation de Fraction comme clé de dictionnaire"""
        d = {
            Fraction(1, 2): "moitié",
            Fraction(1, 3): "tiers",
            Fraction(2, 4): "un demi",  # Même clé que Fraction(1,2)
        }
        # Les deux premières clés sont distinctes, la troisième écrase la première
        self.assertEqual(len(d), 2)
        self.assertEqual(d[Fraction(1, 2)], "un demi")
        self.assertEqual(d[Fraction(1, 3)], "tiers")


class TestFractionIntegration(unittest.TestCase):
    """Tests d'intégration avec les autres modules"""
    
    def test_avec_fraction_continue(self):
        """Test intégration avec fraction_continue"""
        from fraction.continued import fraction_continue
        
        f = fraction_continue(7, 8)
        self.assertIsInstance(f, Fraction)
        self.assertEqual(f, Fraction(128, 35))
    
    def test_operations_avec_grands_nombres(self):
        """Test opérations avec de grands nombres"""
        f1 = Fraction(10**6, 10**5)  # = 10/1
        f2 = Fraction(10**5, 10**6)  # = 1/10
        
        self.assertEqual(f1, Fraction(10, 1))
        self.assertEqual(f1 * f2, Fraction(1, 1))
        self.assertEqual(f1 / f2, Fraction(100, 1))
    
    def test_comparaisons_en_serie(self):
        """Test comparaisons en série"""
        # Vérifier la transitivité
        a = Fraction(1, 3)
        b = Fraction(1, 2)
        c = Fraction(2, 3)
        
        self.assertTrue(a < b < c)
        self.assertTrue(a < c)
    
    def test_fractions_remarquables(self):
        """Test fractions mathématiquement remarquables"""
        # Fraction A de l'énoncé
        f1 = Fraction(1, 1 + Fraction(1, 2 - Fraction(1, 3 + Fraction(1, 4 - Fraction(1, 5 + Fraction(1, 6))))))
        f2 = Fraction(1, 1 - Fraction(1, 2 + Fraction(1, 3 - Fraction(1, 4 + Fraction(1, 5 - Fraction(1, 6))))))
        A = f1 + f2
        self.assertEqual(A, Fraction(66160, 27999))
        
        # Fraction D
        D = Fraction(10 + 20, Fraction(15 + 30, Fraction(20 + 40, Fraction(25 + 50, 45 + 90))))
        self.assertEqual(D, Fraction(72, 1))
        
        # Fraction Z
        Z = (326 + Fraction(12, 13)) / (164 - Fraction(7, 13))
        self.assertEqual(Z, Fraction(2, 1))


class TestFractionTypeErrors(unittest.TestCase):
    """Tests pour la gestion des types invalides"""
    
    def test_addition_type_invalide(self):
        """Test addition avec type invalide"""
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) + "string"
        
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) + 3.14  # float non supporté
    
    def test_soustraction_type_invalide(self):
        """Test soustraction avec type invalide"""
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) - "string"
    
    def test_multiplication_type_invalide(self):
        """Test multiplication avec type invalide"""
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) * "string"
    
    def test_division_type_invalide(self):
        """Test division avec type invalide"""
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) / "string"
    
    def test_comparaison_type_invalide(self):
        """Test comparaison avec type invalide"""
        with self.assertRaises(InvalidOperationError):
            Fraction(1, 2) < "string"


# -------------------------------------------------------------------
# Point d'entrée pour l'exécution directe
# -------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 60)
    print("Tests unitaires : Classe Fraction")
    print("=" * 60)
    unittest.main(verbosity=2)