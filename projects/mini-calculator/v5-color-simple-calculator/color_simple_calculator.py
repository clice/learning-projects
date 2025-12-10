# Função para ler um número do usuário de forma segura
def ler_numero(mensagem):
	while True:  # Loop infinito até o usuário digitar um valor válido
		try: 
			# Tenta converter o que o usuário digitou para float
			valor = float(input(mensagem))
			return valor  # Se der certo, retorna o valor e sai da função
		except ValueError:
			# Se o usuário não digitar um número
			print("\033[91mValor inválido. Tente novamente.\033[0m")


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
		raise ZeroDivisionError("\033[91mErro: divisão por zero!\033[0m")
		return None  # Usa None para indicar que não há resultado válido
	return num_1 / num_2


# Função que mostra o menu de opções da calculadora
def mostrar_menu():
	print("\n\033[96m=== CALCULADORA ===\033[0m")
	print("1) Somar")
	print("2) Subtrair")
	print("3) Multiplicar")
	print("4) Dividir")
	print("5) Ver Histórico")
	print("6) Sair")


# Função principal do programa
def main():
    historico = []  # Lista para armazenar o histórico de operações
    ultimo_resultado = None  # Variável para armazenar o último resultado
    
	# Loop principal: mantém o programa rodando até o usuário escolher sair
    while True:
        mostrar_menu()  # Exibe o menu sempre no início do loop
        opcao = input("\nEscolha uma opção: ")

		# Se a opção for 6, o usuário quer sair
        if opcao == "6":
            print("\nSaindo... Até mais!")
            break  # Encerra o loop e, consequentemente, o programa
        
        # Se a opção for 5, mostra o histórico
        if opcao == "5":
            print("\n\033[95m=== HISTÓRICO DE OPERAÇÕES ===\033[0m")
            if not historico:
                print("Nenhuma operação realizada ainda.")
            else:
                for item in historico:
                    print(item)
            continue  # Volta para o início do loop

		# Se a opção não estiver entre 1, 2, 3 ou 4, é inválida
        if opcao not in ("1", "2", "3", "4"):
            print("\033[91mOpção inválida. Tente de novo.\033[0m")
            continue  # Volte para o início do loop
        
        # Para usar o último resultado
        if ultimo_resultado is not None:
            print("\033[93m(Digite 'r' para usar o último resultado)\033[0m")
            entrada = input("Escolha: ")
        
            if entrada.lower() == 'r':
                num_1 = ultimo_resultado
        else:
            num_1 = ler_numero("\nDigite o primeiro número: ")    

		# Se chegou aqui, a opção é válida. Agora, lê os dois números
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
            print(f"\n\033[92m{num_1} {operacao} {num_2} = {resultado:.2f}\033[0m")
            historico.append(f"{num_1} {operacao} {num_2} = {resultado:.2f}")  # Adiciona ao histórico
            ultimo_resultado = resultado  # Atualiza o último resultado


# Garante que main() só será executada se esse arquivo for rodado diretamente
if __name__ == "__main__":
    main()