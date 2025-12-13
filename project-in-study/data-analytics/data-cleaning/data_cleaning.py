import pandas as pd


def main():
    data = {
        "nome": ["Ana", "Bruno", "Carlos", "Ana"],
        "idade": [25, None, 30, 25],
        "cidade": ["SP", "RJ", None, "SP"],
    }
    df = pd.DataFrame(data)
    print("Original:")
    print(df)

    # remove duplicatas
    df = df.drop_duplicates()

    # preenche valores ausentes
    df["idade"] = df["idade"].fillna(df["idade"].mean())
    df["cidade"] = df["cidade"].fillna("Desconhecida")

    print("\nLimpo:")
    print(df)


if __name__ == "__main__":
    main()
