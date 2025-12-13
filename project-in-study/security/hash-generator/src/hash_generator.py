import hashlib

def generate_sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def main():
    print("=== Gerador de Hash SHA-256 ===")
    text = input("Digite o texto: ")
    print(generate_sha256(text))

if __name__ == "__main__":
    main()
