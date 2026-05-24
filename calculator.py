"""Simple calculator functions for demonstration."""

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
