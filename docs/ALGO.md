# Algorithmes – Fraction Exacte

> Document technique – L1 Informatique  
> Version 1.0 – Dernière mise à jour : 2026

---

## 📐 Sommaire

1. [Simplification de fraction (PGCD)](#1-simplification-de-fraction-pgcd)
2. [Addition de fractions](#2-addition-de-fractions)
3. [Comparaison de fractions](#3-comparaison-de-fractions)
4. [Fractions continues](#4-fractions-continues)
5. [Complexités algorithmiques](#5-complexités-algorithmiques)

---

## 1. Simplification de fraction (PGCD)

### Principe

Une fraction est simplifiée lorsque son numérateur et son dénominateur sont premiers entre eux (PGCD = 1).

### Algorithme d'Euclide

```python
def pgcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)