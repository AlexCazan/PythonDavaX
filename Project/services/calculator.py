from __future__ import annotations
from functools import lru_cache
from math import factorial as _factorial


class Calculator:
    """Pure maths. Static methods = easy to unit‑test and reuse."""
    @staticmethod
    def pow(base: float, exp: float) -> float:
        # For negative bases, only integer exponents are allowed in real numbers;
        # fractional exponents would result in complex numbers, which we disallow here.
        if base < 0 and not float(exp).is_integer():
            raise ValueError(
                "Negative base with fractional exponent is undefined in ℝ")
        return base ** exp

    @staticmethod
    @lru_cache(maxsize=2048)
    def fib(n: int) -> int:
        if n < 0:
            raise ValueError("Fibonacci is undefined for negative integers")
        if n < 2:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    @staticmethod
    def factorial(n: int) -> int:
        if n < 0:
            raise ValueError("Factorial is undefined for negative integers")
        if n > 100_000:            # Arbitrary limit to prevent excessive computation
            raise ValueError("Input too large")
        return _factorial(n)
