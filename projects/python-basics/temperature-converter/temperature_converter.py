# fU
def ler_temperatura(mensagem):
	while True:  # Loop infinito até o usuário digitar um valor válido
		try:
			# Tenta converter o que o usuário digitou para float
			temperatura = float(input(mensagem))
			return temperatura
		except ValueError:
			# Se o usuário não digitar um número
			print("Temperatura inválida. Tente novamente.")


# Função que converte Celsius em Fahrenheit
def celsius_fahrenheit(temperatura):
	return 9 * temperatura / 5 + 32


# Função que converte Celsius em Kelvin
def celsius_kelvin(temperatura):
	return temperatura + 273


# Função que converte Fahrenheit em Celsius
def fahrenheit_celsius(temperatura):
	return 5 * (temperatura - 32) / 9


# Função que converte Fahrenheit em Kelvin
def fahrenheit_kelvin(temperatura):
	return 5 * (temperatura - 32) / 9 + 273


# Função que converte Kelvin em Celsius
def kelvin_celsius(temperatura):
	return temperatura - 273


# Função que converte Kelvin em Fahrenheit
def kelvin_fahrenheit(temperatura):
	return 9 * (temperatura - 273) / 5 + 32


# Função que mostra o menu de opções
def mostrar_menu():
	print("\n=== CONVERSOR DE TEMPERATURAS ===")
	print("1) Celsius para Fahrenheit")
	print("2) Celsius para Kelvin")
	print("3) Fahrenheit para Celsius")
	print("4) Fahrenheit para Kelvin")
	print("5) Kelvin para Celsius")
	print("6) Kelvin para Fahrenheit")
	print("7) Sair")


# Função principal do programa
def main():
	# Loop principal: mantém o programa rodando até o usuário escolher sair
	while True:
		mostrar_menu()  # Exibe o menu sempre no início do loop
		opcao = input("\nEscolha uma opção: ")

		# Se a opção for 7, o usuário quer sair
		if opcao == "7":
			print("Saindo... Até mais!")
			break

		# Se a opção não estiver entre as válidas
		if opcao not in ("1", "2", "3", "4", "5", "6"):
			print("\nOpção inválida. Tente de novo.")
			continue  # Volte para o início do loop

		# Se chegou aqui, a opção é válida. Agora, lê a temperatura
		temperatura = ler_temperatura("Digite a temperatura: ")

		# Verifica qual das opções foi escolhida e chama a função correspondente
		if opcao == "1":
			resultado = celsius_fahrenheit(temperatura)
			original_escala = "C"
			nova_escala = "F"
		if opcao == "2":
			resultado = celsius_kelvin(temperatura)
			original_escala = "C"
			nova_escala = "K"
		if opcao == "3":
			resultado = fahrenheit_celsius(temperatura)
			original_escala = "F"
			nova_escala = "C"
		if opcao == "4":
			resultado = fahrenheit_kelvin(temperatura)
			original_escala = "F"
			nova_escala = "K"
		if opcao == "5":
			resultado = kelvin_celsius(temperatura)
			original_escala = "K"
			nova_escala = "C"
		if opcao == "6":
			resultado = kelvin_fahrenheit(temperatura)
			original_escala = "K"
			nova_escala = "F"

		# Só mostra o resultado se não for None
		if resultado is not None:
			print(f"{temperatura} {original_escala} = {resultado} {nova_escala}")


# Garante que main() só será executado se esse arquivo for rodado diretamente
if __name__ == "__main__":
	main()