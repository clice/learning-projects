# Função para ler um número do usuário de forma segura
def ler_numero(mensagem):
	while True:  # Loop infinito até o usuário digitar um valor válido
		try: 
			# Tenta converter o que o usuário digitou para float
			valor = float(input(mensagem))
			return valor  # Se der certo, retorna o valor e sai da função
		except ValueError:
			# Se o usuário não digitar um número
			print("Valor inválido. Tente novamente.")


# Função que soma dois números
def somar(num_1, num_2):
	return num_1 + num_2


# Função que subtrai dois números
def subtrair(num_1, num_2):
	return num_1 - num_2


# Função que multiplica dois números 
def multiplicar(num_1, num_2):
	return num_1 * num_2


# Função que divide dois números
def dividir(num_1, num_2):
	# Verifica se o divisor é zero para evitar erro
	if num_2 == 0:
		raise ZeroDivisionError("Erro: divisão por zero!")
		return None  # Usa None para indicar que não há resultado válido
	return num_1 / num_2


# Função que mostra o menu de opções da calculadora
def mostrar_menu():
	print("\n=== CALCULADORA ===")
	print("1) Somar")
	print("2) Subtrair")
	print("3) Multiplicar")
	print("4) Dividir")
	print("5) Sair")


# Função principal do programa
def main():
	# Loop principal: mantém o programa rodando até o usuário escolher sair
	while True:
		mostrar_menu()  # Exibe o menu sempre no início do loop
		opcao = input("Escolha uma opção: ")

		# Se a opção for 5, o usuário quer sair
		if opcao == "5":
			print("Saindo... Até mais!")
			break  # Encerra o loop e, consequentemente, o programa

		# Se a opção não estiver entre 1, 2, 3 ou 4, é inválida
		if opcao not in ("1", "2", "3", "4"):
			print("Opção inválida. Tente de novo.")
			continue  # Volte para o início do loop

		# Se chegou aqui, a opção é válida. Agora, lê os dois números
		num_1 = ler_numero("Digite o primeiro número: ")
		num_2 = ler_numero("Digite o segundo número: ")

		# Verifica qual operação foi escolhisa e chama a função correspondente
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
			print(f"\n{num_1} {operacao} {num_2} = {resultado}")


# Garante que main() só será executada se esse arquivo for rodado diretamente
if __name__ == "__main__":
    main()