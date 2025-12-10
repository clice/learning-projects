"""
Arquivo main.py

Este é o ponto de entrada do programa.
Aqui nós:

- Importamos os módulos que criamos (operacoes e utils_io)
- Controlamos o fluxo do programa (menu, leitura de opções)
- Chamamos as funções certas de acordo com a escolha do usuário
"""

# Importa o módulo inteiro com as funções matemáticas
import operations as operacoes

# Importa funções específicas do módulo utils_io
from utils_io import ler_numero, mostrar_menu


def main():
    """
    Função principal da calculadora.

    Fica em loop exibindo o menu, lendo a opção escolhida pelo usuário
    e executando a operação correspondente.
    """
    while True:
        # Mostra o menu para o usuário
        mostrar_menu()

        # Lê a opção escolhida (como string)
        opcao = input("Escolha uma opção: ")

        # Verifica se o usuário quer sair
        if opcao == "5":
            print("Saindo... Até mais!")
            break  # Encerra o loop e a função main()

        # Verifica se a opção é válida (1 a 4)
        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente novamente.")
            continue  # Volta para o início do loop

        # Lê os dois números usando a função do módulo utils_io
        x = ler_numero("Digite o primeiro número: ")
        y = ler_numero("Digite o segundo número: ")

        # Define uma variável para guardar o resultado
        resultado = None
        simbolo = "?"

        # Decide qual função chamar com base na opção
        if opcao == "1":
            resultado = operacoes.somar(x, y)  # Chama somar() do módulo operacoes
            simbolo = "+"
        elif opcao == "2":
            resultado = operacoes.subtrair(x, y)
            simbolo = "-"
        elif opcao == "3":
            resultado = operacoes.multiplicar(x, y)
            simbolo = "*"
        elif opcao == "4":
            resultado = operacoes.dividir(x, y)
            simbolo = "/"

        # Só mostra o resultado se não for None
        # (por exemplo, na tentativa de divisão por zero)
        if resultado is not None:
            print(f"\n{x} {simbolo} {y} = {resultado}")


# Este bloco garante que main() só será executada
# se o arquivo main.py for rodado diretamente (python main.py)
if __name__ == "__main__":
    main()
