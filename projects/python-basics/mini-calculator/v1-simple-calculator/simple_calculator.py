"""
Calculadora simples em modo CLI (linha de comando).

Este módulo implementa uma calculadora básica com as operações
de soma, subtração, multiplicação e divisão, incluindo validação
de entrada do usuário e tratamento de erros comuns.

Projeto voltado para estudos de Python e boas práticas.
"""

def ler_numero(mensagem):
	"""
    Lê um número digitado pelo usuário de forma segura.

    Continua solicitando a entrada até que o usuário informe
    um valor numérico válido.

    Args:
        mensagem (str): Texto exibido para solicitar a entrada.

    Returns:
        float: Número digitado pelo usuário.
    """
	while True:
		try: 
			valor = float(input(mensagem))
			return valor
		except ValueError:
			# Evita que o programa quebre caso o usuário digite texto inválido
			print("Valor inválido. Tente novamente.")


def somar(num_1, num_2):
	"""Retorna a soma de dois números."""
	return num_1 + num_2


def subtrair(num_1, num_2):
	"""Retorna a subtração de dois números."""
	return num_1 - num_2


def multiplicar(num_1, num_2):
	"""Retorna a multiplicação de dois números."""
	return num_1 * num_2


def dividir(num_1, num_2):
	"""
    Retorna a divisão entre dois números.

    Raises:
        ZeroDivisionError: Se o divisor for zero.
    """
	if num_2 == 0:
		# Falha explícita: divisão por zero não é permitida
		raise ZeroDivisionError("Erro: divisão por zero!")
		return None
	return num_1 / num_2


def mostrar_menu():
	"""Exibe o menu de opções da calculadora."""
	print("\n=== CALCULADORA ===")
	print("1) Somar")
	print("2) Subtrair")
	print("3) Multiplicar")
	print("4) Dividir")
	print("5) Sair")


def main():
	"""
    Função principal da aplicação.

    Controla o fluxo do programa, exibindo o menu,
    lendo as entradas do usuário e chamando as operações.
    """
	while True:
		mostrar_menu()
		opcao = input("\nEscolha uma opção: ")

		# Se a opção for 5, o usuário quer sair
		if opcao == "5":
			print("\nSaindo... Até mais!")
			break  # Encerra o loop e, consequentemente, o programa

		# Se a opção não estiver entre 1, 2, 3 ou 4, é inválida
		if opcao not in ("1", "2", "3", "4"):
			print("\nOpção inválida. Tente de novo.")
			continue  # Volte para o início do loop

		# Se chegou aqui, a opção é válida. Agora, lê os dois números
		num_1 = ler_numero("Digite o primeiro número: ")
		num_2 = ler_numero("Digite o segundo número: ")

		# Verifica qual operação foi escolhida e chama a função correspondente
		if opcao == "1":
			resultado = somar(num_1, num_2)
			operacao = "+"
		elif opcao == "2":
			resultado = subtrair(num_1, num_2)
			operacao = "-"
		elif opcao == "3":
			resultado = multiplicar(num_1, num_2)
			operacao = "*"
		else:  # opcao == "4"
			resultado = dividir(num_1, num_2)
			operacao = "/"

		# Só mostra o resultado se não for None (por exemplo, na divisão por zero)
		if resultado is not None:
			print(f"\n{num_1} {operacao} {num_2} = {resultado:.2f}")


if __name__ == "__main__":
    main()