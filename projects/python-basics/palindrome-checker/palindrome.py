# import re

# def is_palindrome(text: str) -> bool:
#     cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
#     return cleaned == cleaned[::-1]

# def main():
#     print("=== Verificador de Palíndromos ===")
#     text = input("Digite uma palavra ou frase: ")
#     if is_palindrome(text):
#         print("É um palíndromo!")
#     else:
#         print("Não é um palíndromo.")

# if __name__ == "__main__":
#     main()
