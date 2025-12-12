"""
Módulo operations.py

Aqui ficam as funções matemáticas da calculadora.
Este módulo NÃO interage com o usuário (não usa input nem print),
ele só recebe números e retorna resultados.
"""

def somar(num_1, num_2):
    """
    Função que soma dois números e retorna o resultado.
    """
    return num_1 + num_2

def subtrair(num_1, num_2):
    """
    Função que subtrai o segundo número do primeiro e retorna o resultado.
    """
    return num_1 - num_2

def multiplicar(num_1, num_2):
    """
    Função que multiplica dois números e retorna o resultado.
    """
    return num_1 * num_2

def dividir(num_1, num_2):
    """
    Função que divide o primeiro número pelo segundo e retorna o resultado.

    Levanta ZeroDivisionError se o segundo número for zero.
    """
    if num_2 == 0:
        raise ZeroDivisionError("Erro: divisão por zero!")
        return None  # Usa None para indicar que não há resultado válido
    return num_1 / num_2