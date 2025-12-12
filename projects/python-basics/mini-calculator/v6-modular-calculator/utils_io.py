"""
Módulo utils_io.py

Responsável por lidar com a interação com o usuário:
- Ler números do input
- Mostrar menus e mensagens na tela
"""

def ler_numero(mensagem):
    """
    Função para ler um número do usuário de forma segura.

    Continua pedindo até o usuário digitar um valor válido.
    """
    while True:  # Loop infinito até o usuário digitar um valor válido
        try:
            # Tenta converter o que o usuário digitou para float
            valor = float(input(mensagem))
            return valor  # Se der certo, retorna o valor e sai da função
        except ValueError:
            # Se o usuário não digitar um número
            print("Valor inválido. Tente novamente.")
            

def mostrar_menu():
    """
    Exibe o menu de opções da calculadora na tela.
    Não recebe nem retorna nada, apenas imprime.
    """
    print("\n=== CALCULADORA MODULAR ===")
    print("1) Somar")
    print("2) Subtrair")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Sair")