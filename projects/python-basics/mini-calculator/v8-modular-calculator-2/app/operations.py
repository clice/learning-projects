"""
Módulo com as operações matemáticas da calculadora.
"""


def somar(a, b):
    """Retorna a soma de dois números."""
    return a + b


def subtrair(a, b):
    """Retorna a subtração de dois números."""
    return a - b


def multiplicar(a, b):
    """Retorna a multiplicação de dois números."""
    return a * b


def dividir(a, b):
    """
    Retorna a divisão entre dois números.

    Raises:
        ZeroDivisionError: Se b for zero.
    """
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")

    return a / b