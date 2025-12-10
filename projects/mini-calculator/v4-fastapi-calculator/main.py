"""
Arquivo main.py

Aqui definimos uma API simples de calculadora usando FastAPI.
Ela terá endpoints (rotas) para somar, subtrair, multiplicar e dividir
"""

from fastapi import FastAPI
from pydantic import BaseModel


class Operacao(BaseModel):
	"""
	Classe que representa o corpo (JSON) da requisição

	Quando o cliente fizer um POST para /somar, por exemplo,
	ele deve enviar algo como:
		{
			"num_1": 10,
			"num_2": 5
		}

	O FastAPI usa essa classe para validar e converter os dados.
	"""
	num_1: float  # Primeiro número
	num_2: float  # Segundo número


# Cria a aplicação FastAPI
app = FastAPI(
	title="API Calculadora", 
	description="Uma API simples de calculadora para estudo",
	version="1.0.0"
)


@app.get("/")
def raiz():
	"""
	Rota GET básica para testar se a API está no ar

	Acessando http://localhost:8000/ você verá esse retorno.
	"""
	return {"mensagem": "API da Calculadora está funcionando!"}


@app.post("/somar")
def somar(op: Operacao):
	"""
	Rota POST para somar dois números

	Exemplo de requisiçao (JSON):
		{
			"num_1": 2,
			"num_2": 3
		}

	Resposta:
		{
			"resultado": 5
		}
	"""
	return {"resultado": op.num_1 + op.num_2}


@app.post("/subtrair")
def subtrair(op: Operacao):
	"""
	Rota POST para subtrair dois números

	Exemplo de requisiçao (JSON):
		{
			"num_1": 2,
			"num_2": 3
		}

	Resposta:
		{
			"resultado": -1
		}
	"""
	return {"resultado": op.num_1 - op.num_2}


@app.post("/multiplicar")
def multiplicar(op: Operacao):
	"""
	Rota POST para multiplicar dois números

	Exemplo de requisiçao (JSON):
		{
			"num_1": 2,
			"num_2": 3
		}

	Resposta:
		{
			"resultado": 6
		}
	"""
	return {"resultado": op.num_1 * op.num_2}


@app.post("/dividir")
def dividir(op: Operacao):
	"""
	Rota POST para dividir dois números

	Exemplo de requisiçao (JSON):
		{
			"num_1": 6,
			"num_2": 3
		}

	Resposta:
		{
			"resultado": 2
		}
	"""
	# Verifica se o divisor é zero para evitar erro
	if op.num_2 == 0:
		raise ZeroDivisionError("Erro: divisão para zero!")
		return None  # Usa None para indicar que não há resultado válido
	return {"resultado": op.num_1 / op.num_2}