"""
Arquivo de testes: test_tkinter_calculator.py

Aqui usamos pytest para garantir que as funções 
do módulo: tkinter_calculator.py
estão funcionando corretamente.
"""

import pytest
from tkinter_calculator import Calculadora

calculadora = Calculadora()


# Função de teste para o método somar()
def test_somar():
    assert calculadora.somar(2, 3) == 5
    assert calculadora.somar(-1, 1) == 0
    assert calculadora.somar(0, 0) == 0


# Função de teste para o método subtrair()
def test_subtrair():
    assert calculadora.subtrair(5, 3) == 2
    assert calculadora.subtrair(0, 5) == -5
    assert calculadora.subtrair(-20, 6) == -26


# Função de teste para o método multiplicar()
def test_multiplicar():
	assert calculadora.multiplicar(2, 3) == 6
	assert calculadora.multiplicar(-1, 3) == -3
	assert calculadora.multiplicar(6, 0) == 0


# Função de teste para o método dividir()
def test_dividir():
	assert calculadora.dividir(6, 3) == 2
	assert calculadora.dividir(5, 2) == 2.5
	assert calculadora.dividir(2.5, 2) == 1.25


# Função para testar a função dividir() em casos de divisão por zero
# Espera um erro específico levando a ZeroDivisionError
def test_dividir_por_zero():
	with pytest.raises(ZeroDivisionError):
		calculadora.dividir(10, 0)
		calculadora.dividir(-2.5, 0)
		calculadora.dividir(-20, 0)