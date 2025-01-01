import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

task_data = {
    "titulo":"Projeto com FastAPI",
    "descricao": "Criar API de to-do list com FastAPI",
    "estado": "pendente",
}

def test_create_task():
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    response_data = response.json()
    assert response_data["titulo"] == task_data["titulo"]
    assert response_data["estado"] == task_data["estado"]

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    tasks = response.json()
    assert isinstance(tasks, list)
    if tasks:
        assert "titulo" in tasks[0]
        assert "estado" in tasks[0]

# def test_get_task_by_id():
#     response = client.post("/tasks/", json=task_data)
#     assert response.status_code == 201
#     task_id = response.json()["id"]

#     response = client.post(f"tasks/{task_id}", json=task_data)

def test_update_task():
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    task_id = response.json()["id"]

    updated_data = {"estado": "concluida"}
    response = client.put(f"tasks/{task_id}", json=updated_data)
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["estado"] == "concluida"

def test_delete_task():
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 201
    task_id = response.json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204 

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
