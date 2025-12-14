import pytest
from app.operations import somar, subtrair, multiplicar, dividir


def test_somar():
    assert somar(2, 3) == 5


def test_subtrair():
    assert subtrair(5, 3) == 2


def test_multiplicar():
    assert multiplicar(2, 4) == 8


def test_dividir():
    assert dividir(10, 2) == 5


def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)