# Classe simples para realizar operações matemáticas básicas
class Calculadora:
    # Método que soma dois números   
    def somar(self, num_1, num_2):
        return num_1 + num_2
    
    # Método que subtrai dois números
    def subtrair(self, num_1, num_2):
        return num_1 - num_2    
    
    # Método que multiplica dois números 
    def multiplicar(self, num_1, num_2):
        return num_1 * num_2    
    
    # Método que divide dois números
    def dividir(self, num_1, num_2):
        # Verifica se o divisor é zero para evitar erro
        if num_2 == 0:
            raise ZeroDivisionError("Erro: divisão por zero!")
            return None  # Usa None para indicar que não há resultado válido
        return num_1 / num_2
    
    
# Função que lê um número do usuário, garantindo que a entrada seja válida
def ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            # Se o usuário não digitar um número
            print("Valor inválido. Tente novamente.")
            

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
    calculadora = Calculadora()
    
    # Loop principal: mantém o programa rodando até o usuário escolher sair
    while True:
        mostrar_menu()  # Exibe o menu sempre no início do loop
        opcao = input("\nEscolha uma opção: ")
        
        # Se a opção for 5, o usuário quer sair
        if opcao == "5":
            print("\nSaindo... Até mais!")
            break  # Encerra o loop e, consequentemente, o programa 
        
        # Se a opção não estiver entre 1, 2, 3 ou 4, é inválida
        if opcao not in ("1", "2", "3", "4"):
            print("\nOpção inválida. Tente novamente.")
            continue    
        
        # Se chegou aqui, a opção é válida. Agora, lê os dois números
        num_1 = ler_numero("Digite o primeiro número: ")
        num_2 = ler_numero("Digite o segundo número: ") 
        
        # Dicionário com as operações disponíveis
        operacoes = {
            "1": (calculadora.somar, "+"),
            "2": (calculadora.subtrair, "-"),
            "3": (calculadora.multiplicar, "*"),
            "4": (calculadora.dividir, "/"),
        }
        
        funcao, operacao = operacoes[opcao]
        resultado = funcao(num_1, num_2)
        
        # Mostra o resultado da operação se for válida
        if resultado is not None:
            print(f"\nResultado: {num_1} {operacao} {num_2} é: {resultado}")
            
            
# Garante que main() só será executada se esse arquivo for rodado diretamente
if __name__ == "__main__":
    main()
