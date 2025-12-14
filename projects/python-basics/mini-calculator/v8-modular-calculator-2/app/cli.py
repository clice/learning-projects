"""
Interface de linha de comando da calculadora.
"""

from app.input_utils import ler_numero
from app.operations import somar, subtrair, multiplicar, dividir


def mostrar_menu():
    """Exibe o menu de opções."""
    print("\n=== CALCULADORA ===")
    print("1) Somar")
    print("2) Subtrair")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Sair")


def main():
    """Controla o fluxo principal da aplicação."""
    while True:
        mostrar_menu()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "5":
            print("\nSaindo... Até mais!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("\nOpção inválida.")
            continue

        num_1 = ler_numero("Digite o primeiro número: ")
        num_2 = ler_numero("Digite o segundo número: ")

        try:
            if opcao == "1":
                resultado = somar(num_1, num_2)
                operador = "+"
            elif opcao == "2":
                resultado = subtrair(num_1, num_2)
                operador = "-"
            elif opcao == "3":
                resultado = multiplicar(num_1, num_2)
                operador = "*"
            else:
                resultado = dividir(num_1, num_2)
                operador = "/"

            print(f"\n{num_1} {operador} {num_2} = {resultado:.2f}")

        except ZeroDivisionError as erro:
            print(f"\nErro: {erro}")


if __name__ == "__main__":
    main()