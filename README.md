# 🧮 Fraction Exacte – Calcul rationnel haute précision

[![Python 3.12](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-130%20passed-brightgreen.svg)]()
[![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen.svg)]()
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)]()

---

## 📌 À propos

**Fraction Exacte** est une implémentation professionnelle en **Programmation Orientée Objet** d'une classe de fractions rationnelles. Ce projet a été réalisé dans le cadre de ma **L1 Informatique** pour démontrer ma maîtrise des concepts fondamentaux de la POO en Python.

### 🎯 Objectifs pédagogiques

- Implémenter une classe **robuste** avec encapsulation et validation
- Utiliser les **opérateurs magiques** (`__add__`, `__eq__`, etc.)
- Assurer la **simplification automatique** via l'algorithme d'Euclide
- Garantir des **comparaisons exactes** sans conversion flottante
- Structurer un projet **maintenable** (séparation src/tests/docs)
- Rédiger une **documentation technique** complète

---

## ✨ Fonctionnalités

| Fonctionnalité | Description |
|----------------|-------------|
| **Création** | `Fraction(num, den=1)` – construction avec simplification auto |
| **Opérations** | `+`, `-`, `*`, `/` – avec fractions ou entiers |
| **Comparaisons** | `==`, `<`, `>` – comparaisons exactes sans flottants |
| **Conversions** | `to_float()`, `round(n)` – conversion et arrondi |
| **Utilitaires** | `inverse()`, `est_entier()`, `est_unitaire()`, `valeur_absolue()` |
| **Fractions continues** | Génération de fractions continues imbriquées |
| **Hash** | Utilisable comme clé de dictionnaire / set |

---

## 📦 Installation

```bash
# Cloner le dépôt
git clone https://github.com/tonpseudo/fraction_exacte.git
cd fraction_exacte

# Installer les dépendances
make install

# Ou manuellement
pip install -r requirements.txt