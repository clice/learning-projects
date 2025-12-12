"""
Arquivo de testes: test_temperature_converter.py

Aqui usamos pytest para garantir que as funções 
do módulo: temperature_converter.py
estão funcionando corretamente.
"""

import pytest
from temperature_converter import celsius_fahrenheit, celsius_kelvin, fahrenheit_celsius, fahrenheit_kelvin, kelvin_celsius, kelvin_fahrenheit


# Função para testar a conversão de Celsius para Fahrenheit
def test_celsius_fahrenheit():
    assert celsius_fahrenheit(0) == 32
    assert celsius_fahrenheit(100) == 212
    assert celsius_fahrenheit(-40) == -40
    
    
# Função para testar a conversão de Celsius para Kelvin
def test_celsius_kelvin():
    assert celsius_kelvin(0) == 273
    assert celsius_kelvin(100) == 373
    assert celsius_kelvin(-273) == 0