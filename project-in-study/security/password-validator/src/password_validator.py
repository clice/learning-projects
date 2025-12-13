import re


def is_strong(password: str) -> bool:
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[^A-Za-z0-9]", password):
        return False
    return True


def main():
    print("=== Validador de Senhas ===")
    pwd = input("Digite a senha: ")
    if is_strong(pwd):
        print("Senha forte!")
    else:
        print("Senha fraca. Use letras maiúsculas, minúsculas, números e símbolos, com pelo menos 8 caracteres.")


if __name__ == "__main__":
    main()
