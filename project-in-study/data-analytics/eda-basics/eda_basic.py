import pandas as pd
import matplotlib.pyplot as plt


def main():
    print("Este é um exemplo simples de EDA.")
    data = {
        "categoria": ["A", "B", "C", "A", "B", "C"],
        "valor": [10, 15, 7, 12, 18, 5],
    }
    df = pd.DataFrame(data)
    print(df.describe())

    df.groupby("categoria")["valor"].mean().plot(kind="bar")
    plt.title("Média por categoria")
    plt.xlabel("Categoria")
    plt.ylabel("Valor médio")
    plt.tight_layout()
    plt.savefig("plot.png")
    print("Gráfico salvo como plot.png")


if __name__ == "__main__":
    main()
