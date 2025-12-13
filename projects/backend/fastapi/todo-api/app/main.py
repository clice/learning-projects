from fastapi import FastAPI

from .database import Base, engine
from .routers import todos


def create_app() -> FastAPI:
    """
    Função que cria e configura a instância da aplicação FastAPI.
    Isso é útil para testes e para separar configuração da variável global.
    """
    app = FastAPI(
        title="To-do API",  # Título que aparece na documentação
        description="API simples de tarefas construída com FastAPI para estudos.",
        version="1.0.0",
    )

    # Cria as tabelas no banco, se ainda não existirem.
    # Base contém a definição de todos os modelos (como Task).
    Base.metadata.create_all(bind=engine)

    # Inclui o router de tarefas na aplicação, com as rotas definidas em todos.py
    app.include_router(todos.router)

    return app


# Instância global da aplicação, usada pelo Uvicorn.
# Quando rodamos "uvicorn app.main:app", é essa variável que ele usa.
app = create_app()