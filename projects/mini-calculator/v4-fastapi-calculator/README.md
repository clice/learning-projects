# 🧮 Mini Calculadora — Python com FastAPI

Projeto simples para treinar lógica, funções, entrada de dados e organização de código, utilizando o FastAPI para construir uma calculadora.

---

## 🚀 Funcionalidades

- Adição
- Subtração
- Multiplicação
- Divisão com verificação de zero
- Loop para repetir operações

---

## 📁 Estrutura

mini-calculator/

└── v3-tkinter-calculator/

    ├── .gitignore
    ├── main.py
    ├── README.md
    ├── requirements.txt
    └── test_main.py

---

## ▶️ Como executar o projeto

```bash
python3 -m venv .venv                  # Instalar o ambiente de execução
source .venv/bin/activate              # Ativar o ambiente de execução
pip install -r requirements.txt        # Instalar os módulos necessários para a execução
pip install fastapi uvicorn[standard]  # Instalar o Tkinter no Python (precisa instalar globalmente)
uvicorn main:app --reload              # Executar o projeto
deactivate                             # Desativar o ambiente de execução
```

---

## ▶️ Como executar os testes

```bash
source .venv/bin/activate   # Ativar o ambiente de execução
uvicorn main:app --reload   # Executar o projeto
# No navegador acessar:
http://127.0.0.1:8000/docs  # Testar individualmente as rotas

deactivate                  # Desativar o ambiente de execução
```

---

## 📚 O que aprendi

- Criar funções em Python
- Validar entradas
- Estruturar pequenos projetos
- Tratar erros simples

---

## 🔮 Próximos passos

- Adicionar operações avançadas
- Criar testes unitários (pytest) ✅
- Criar uma versão com interface em terminal ✅