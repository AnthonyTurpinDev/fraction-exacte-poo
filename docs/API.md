# API Reference – Fraction Exacte

> Documentation technique – L1 Informatique  
> Version 1.0 – Dernière mise à jour : 2026

---

## 📑 Sommaire

1. [Classe Fraction](#classe-fraction)
2. [Fonctions utilitaires](#fonctions-utilitaires)
3. [Exceptions](#exceptions)
4. [Exemples complets](#exemples-complets)

---

## Classe Fraction

### `Fraction(num: int, den: int = 1)`

Crée une fraction à partir d'un numérateur et d'un dénominateur.

**Paramètres :**

| Nom | Type | Description |
|-----|------|-------------|
| `num` | `int` | Numérateur (peut être négatif) |
| `den` | `int` | Dénominateur (doit être ≠ 0, défaut = 1) |

**Lève :**
- `DivisionByZeroError` – si `den == 0`

**Exemple :**

```python
from fraction import Fraction

a = Fraction(3, 4)      # 3/4
b = Fraction(5)         # 5/1
c = Fraction(-6, 8)     # -3/4 (simplifié automatiquement)