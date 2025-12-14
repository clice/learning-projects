"""
Funções utilitárias para entrada de dados do usuário.
"""


def ler_numero(mensagem):
    """
    Lê um número digitado pelo usuário de forma segura.

    Continua solicitando até que um valor válido seja informado.
    """
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Valor inválido. Digite um número válido.")