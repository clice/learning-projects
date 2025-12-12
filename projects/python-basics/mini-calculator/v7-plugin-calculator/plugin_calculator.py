"""
plugin_calculator.py

Exemplo de "sistema de plugins" para uma calculadora em linha de comando.

A ideia é:
- Ter um dicionário OPERACOES que mapeia um símbolo (por exemplo, "+")
  para uma funćão (por exemplo, somar)
- Para adicionar uma nova operação, basta criar uma função 
  e registrá-la no dicionário

Isso imita um sistema de plugins de forma simples.
"""


# =========================
# Funções de operações
# =========================
def somar(num_1, num_2):
    """
    Retorna a soma de dois números.
    """
    return num_1 + num_2


def subtrair(num_1, num_2):
    """
    Retorna a subtração de dois números.
    """
    return num_1 - num_2


def multiplicar(num_1, num_2):
    """
    Retorna o produto (multiplicação) de dois números.
    """
    return num_1 * num_2


def dividir(num_1, num_2):
    """
    Retorna a divisão de dois números.

    Se num_2 for zero, mostra uma mensagem de erro e retorna None,
    indicando que a operação falhou.
    """
    if num_2 == 0:
        raise ZeroDivisionError("Erro: divisão por zero!")
        return None  # Usa None para indicar que não há resultado válido
    return num_1 / num_2


# Exemplo de uma nova operação ("plugin"): potência
def potencia(num_1, num_2):
    """
    Eleva num_1 à potência num_2 (num_1 ** num_2).
    """
    return num_1 ** num_2


def modulo(num_1, num_2):
    """
    Retorna o resto da divisão de num_1 por num_2.
    """
    if num_2 == 0:
        raise ZeroDivisionError("Erro: divisão por zero!")
        return None  # Usa None para indicar que não há resultado válido
    return num_1 % num_2



# =========================
# Registro de operações
# =========================

# Este dicionário funciona como um "registro" de plugins:
# - a chave é o símbolo que o usuário digita
# - o valor é a função que será chamada
OPERACOES = {
    "+": somar,
    "-": subtrair,
    "*": multiplicar,
    "/": dividir,
    "^": potencia,  # registramos a operação de potência
    "%": modulo,    # nova operação plugin
}


# =========================
# Funções auxiliares de I/O
# =========================

def ler_numero(mensagem):
    """
    Lê um número do usuário com validação.

    Fica em loop até o usuário digitar um valor numérico válido.
    """
    while True:
        try:
            texto = input(mensagem)
            valor = float(texto)
            return valor
        except ValueError:
            print("Valor inválido. Digite um número.")


def mostrar_operacoes():
    """
    Mostra as operações disponíveis com base nas chaves do dicionário OPERACOES.
    """
    simbolos = " ".join(OPERACOES.keys())
    print(f"Operações disponíveis: {simbolos}")


# =========================
# Função principal
# =========================

def main():
    """
    Função principal da calculadora.

    - Mostra as operações disponíveis
    - Pede ao usuário para escolher uma operação
    - Lê dois números
    - Executa a função correspondente
    """
    print("=== CALCULADORA COM PLUGINS SIMPLES ===")
    print("Digite 'sair' para encerrar.\n")

    while True:
        mostrar_operacoes()
        op = input("Escolha a operação (+, -, *, /, ^, %): ")

        # Permite encerrar o programa digitando 'sair' (maiúsculo ou minúsculo)
        if op.lower() == "sair":
            print("Saindo... Até mais!")
            break

        # Verifica se a operação digitada existe no dicionário
        if op not in OPERACOES:
            print("Operação desconhecida. Tente novamente.\n")
            continue

        # Lê os dois números a serem usados na operação
        num_1 = ler_numero("Digite o primeiro número: ")
        num_2 = ler_numero("Digite o segundo número: ")

        # Pega a função correspondente à operação escolhida
        funcao = OPERACOES[op]

        # Chama a função passando a e b
        resultado = funcao(num_1, num_2)

        # Se a operação não retornou None, mostramos o resultado
        if resultado is not None:
            print(f"\n{num_1} {op} {num_2} = {resultado}\n")


# Este bloco garante que main() só será executada
# se o arquivo for rodado diretamente (python plugins_calculadora.py)
if __name__ == "__main__":
    main()
