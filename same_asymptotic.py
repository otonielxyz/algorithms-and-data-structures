"""
same_asymptotic.py
Author: Otoniel Torres Bernal

Description:
    A small utility module for comparing the asymptotic growth rates of two
    mathematical expressions using SymPy. This program determines whether two
    functions f(n) and g(n) have the same Θ (theta) growth by evaluating:

        lim (n → ∞) | f(n) / g(n) | = L   where 0 < L < ∞

    If the limit exists and satisfies the condition above, the functions are
    considered asymptotically equivalent: Θ(f) = Θ(g).

    This file is part of a broader collection of algorithmic and mathematical
    tools for analyzing computational complexity.

Dependencies:
    - SymPy
"""

from sympy import symbols, log as _log, sympify, limit, Abs, oo, simplify
from sympy.core.expr import Expr
from sympy.core.symbol import Symbol

# Public symbol so users can write: same_asymptotic(n**2*_log(n), ...)
n: Symbol = symbols('n', positive=True)
log = _log


def _ensure_expr(x):
    """
    Convert `x` to a SymPy expression and verify that it depends only on the
    symbol n (or is constant).

    Raises
    ------
    TypeError:
        If x cannot be converted into a SymPy expression or is not an Expr.
    ValueError:
        If x contains symbols other than 'n'.
    """
    try:
        ex = sympify(x)
    except Exception as e:
        raise TypeError(
            "Inputs must be SymPy-expressible expressions or use the provided symbol n."
        ) from e

    if not isinstance(ex, Expr):
        raise TypeError("Inputs must be SymPy expressions.")

    # Only allow expressions involving n (or constants)
    other_syms = ex.free_symbols - {n}
    if other_syms:
        raise ValueError("Expressions may only depend on the symbol 'n'.")

    return ex


def _is_positive_finite(value):
    """
    Returns True iff `value` is a finite, positive SymPy object.

    Useful for verifying whether the asymptotic limit lies within (0, ∞).
    """
    if value is None:
        return False
    if value.is_real is False:
        return False
    if value.is_finite is False:
        return False

    # SymPy may already know positivity
    if getattr(value, "is_positive", None) is True:
        return True

    # Fallback: evaluate numerically if possible
    try:
        return bool(value.evalf() > 0)
    except Exception:
        return False


def same_asymptotic(left, right):
    """
    Determine whether two expressions have the same Θ (theta) asymptotic growth
    as n → ∞.

    Definition:
        f ~ Θ(g)  ⇔  lim (n → ∞) | f(n) / g(n) | = L  where 0 < L < ∞.

    Par
