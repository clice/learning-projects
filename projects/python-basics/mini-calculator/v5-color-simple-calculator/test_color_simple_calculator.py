"""
Arquivo de testes: test_color_simple_calculator.py

Aqui usamos pytest para garantir que as funções 
do módulo: color_simple_calculator.py
estão funcionando corretamente.
"""

import pytest
from color_simple_calculator import somar, subtrair, multiplicar, dividir


# Função para testar a função somar() 
def test_somar():
	assert somar(2, 3) == 5
	assert somar (-1, 1) == 0
	assert somar(0, 0) == 0


# Função para testar a função subtrair()
def test_subtrair():
	assert subtrair(5, 3) == 2
	assert subtrair(0, 5) == -5
	assert subtrair(-20, 6) == -26


# Função para testar a função multiplicar()
def test_multiplicar():
	assert multiplicar(2, 3) == 6
	assert multiplicar(-1, 3) == -3
	assert multiplicar(6, 0) == 0


# Função para testar a função dividir()
def test_dividir():
	assert dividir(6, 3) == 2
	assert dividir(5, 2) == 2.5
	assert dividir(2.5, 2) == 1.25


# Função para testar a função dividir() em casos de divisão por zero
# Espera um erro específico levando a ZeroDivisionError
def test_dividir_por_zero():
	with pytest.raises(ZeroDivisionError):
		dividir(10, 0)
		dividir(-2.5, 0)
		dividir(-20, 0)