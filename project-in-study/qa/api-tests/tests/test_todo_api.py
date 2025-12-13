import requests


BASE_URL = "http://localhost:5000"


def test_create_and_list_task():
    # cria tarefa
    resp = requests.post(f"{BASE_URL}/tasks", json={"title": "teste"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "teste"
    task_id = data["id"]

    # lista tarefas
    resp_list = requests.get(f"{BASE_URL}/tasks")
    assert resp_list.status_code == 200
    tasks = resp_list.json()
    assert any(t["id"] == task_id for t in tasks)
