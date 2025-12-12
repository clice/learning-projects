from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
import pytest


from app.main import app
from app.database import Base, get_db


# URL do banco de dados de TESTE (arquivo separado do banco "real")
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"


# Cria um engine específico para os testes
engine = create_engine(
	SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)


# Session para testes, ligada ao engine de teste
TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def override_get_db():
    """
    Essa função substitui a dependência get_db original
    para usar o banco de testes (TestingSessionLocal).
    """
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


# Aqui informamos ao FastAPI que, sempre que for usar get_db,
# deve usar override_get_db no lugar (apenas durante os testes).
app.dependency_overrides[get_db] = override_get_db

# Cria o cliente de testes do FastAPI
client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    """
    Fixture que roda ANTES de cada teste.
    Ela recria as tabelas no banco de teste, garantindo
    que cada teste comece com o banco "limpo".
    """
    # Remove todas as tabelas (se existirem)
    Base.metadata.drop_all(bind=engine)
    # Cria todas as tabelas novamente
    Base.metadata.create_all(bind=engine)
    # Entrega o controle para o teste
    yield
    # Opcionalmente, poderia limpar depois também, se quisesse.


def test_create_task():
    """
    Deve criar uma nova tarefa com sucesso (HTTP 201)
    e retornar os dados corretos.
    """
    payload = {
        "title": "Estudar FastAPI",
        "description": "Seguir o projeto To-do API",
        "completed": False,
    }

    response = client.post("/tasks/", json=payload)

    assert response.status_code == 201
    data = response.json()

    # Verificações básicas
    assert data["id"] == 1
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["completed"] is False
    # created_at deve existir
    assert "created_at" in data


def test_list_tasks_returns_empty_list_initially():
    """
    Quando não há tarefas, a listagem deve retornar uma lista vazia.
    """
    response = client.get("/tasks/")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert data == []


def test_list_tasks_after_creating():
    """
    Após criar uma tarefa, ela deve aparecer na listagem.
    """
    # Cria uma tarefa
    client.post(
        "/tasks/",
        json={"title": "Tarefa 1", "description": "Desc", "completed": False},
    )

    # Lista tarefas
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()

    assert len(data) == 1
    assert data[0]["title"] == "Tarefa 1"


def test_get_task_by_id():
    """
    Deve retornar uma tarefa específica pelo ID.
    """
    # Cria uma tarefa
    create_resp = client.post(
        "/tasks/",
        json={"title": "Tarefa X", "description": "Teste get", "completed": False},
    )
    created = create_resp.json()
    task_id = created["id"]

    # Busca pelo ID
    response = client.get(f"/tasks/{task_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Tarefa X"


def test_get_task_not_found():
    """
    Deve retornar 404 quando a tarefa não existe.
    """
    response = client.get("/tasks/999")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Task not found"


def test_update_task():
    """
    Deve atualizar uma tarefa existente.
    """
    # Cria uma tarefa
    create_resp = client.post(
        "/tasks/",
        json={"title": "Antigo título", "description": "Desc", "completed": False},
    )
    task_id = create_resp.json()["id"]

    # Atualiza a tarefa
    update_payload = {"title": "Novo título", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_payload)

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == task_id
    assert data["title"] == "Novo título"
    assert data["completed"] is True


def test_delete_task():
    """
    Deve deletar uma tarefa e, depois disso,
    a tarefa não deve mais ser encontrada.
    """
    # Cria uma tarefa
    create_resp = client.post(
        "/tasks/",
        json={"title": "Apagar", "description": "Teste delete", "completed": False},
    )
    task_id = create_resp.json()["id"]

    # Deleta a tarefa
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 204  # No Content

    # Tenta buscar de novo → 404
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 404