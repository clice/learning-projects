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
    
    
# Função para testar a conversão de Fahrenheit para Celsius
def test_fahrenheit_celsius():
    assert fahrenheit_celsius(32) == 0
    assert fahrenheit_celsius(212) == 100
    assert fahrenheit_celsius(-40) == -40
    
    
# Função para testar a conversão de Fahrenheit para Kelvin
def test_fahrenheit_kelvin():
    assert fahrenheit_kelvin(32) == 273
    assert fahrenheit_kelvin(212) == 373
    assert fahrenheit_kelvin(-40) == 233
    

# Função para testar a conversão de Kelvin para Celsius
def test_kelvin_celsius():
    assert kelvin_celsius(273) == 0
    assert kelvin_celsius(373) == 100
    assert kelvin_celsius(0) == -273
    
    
# Função para testar a conversão de Kelvin para Fahrenheit
def test_kelvin_fahrenheit():
    assert kelvin_fahrenheit(273) == 32
    assert kelvin_fahrenheit(373) == 212
    assert kelvin_fahrenheit(0) == -459.4
    