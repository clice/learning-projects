import pytest
from src.calculator import add, sub, mul, div


def test_add():
    assert add(2, 3) == 5


def test_sub():
    assert sub(5, 3) == 2


def test_mul():
    assert mul(4, 3) == 12


def test_div():
    assert div(10, 2) == 5


def test_div_zero():
    with pytest.raises(ValueError):
        div(1, 0)
