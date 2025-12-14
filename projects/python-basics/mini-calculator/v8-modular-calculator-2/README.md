# 🧮 Calculator CLI – Python

Calculadora simples em linha de comando desenvolvida em Python,
com foco em boas práticas, separação de responsabilidades e testes.

## 🚀 Funcionalidades

- Soma
- Subtração
- Multiplicação
- Divisão com tratamento de erro
- Validação de entrada do usuário

## 🧱 Estrutura

mini-calculator/

└── v8-modular-calculator-2/

    ├── app/
    │   ├── __init__.py
    │   ├── cli.py              # interface de linha de comando
    │   ├── operations.py       # regras de negócio (soma, divisão, etc.)
    │   └── input_utils.py      # leitura segura de números
    │
    ├── tests/
    │   ├── __init__.py
    │   ├── test_operations.py
    │   └── test_input_utils.py
    │
    ├── README.md
    ├── requirements.txt
    └── .gitignore


## ▶️ Como executar

```bash
python -m app.cli
```