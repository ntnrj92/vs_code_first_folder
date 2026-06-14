"""Simple calculator functions for demonstration."""
import math


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return the quotient of a and b.

    If b is zero, return None to avoid a crash.
    """
    if b == 0:
        return None
    return a / b


def sqrt(x):
    """Return the square root of x.

    Returns None for negative inputs to avoid complex results.
    """
    if x < 0:
        return None
    return math.sqrt(x)


def cbrt(x):
    """Return the real cube root of x (handles negative inputs)."""
    return math.copysign(abs(x) ** (1.0 / 3.0), x)
