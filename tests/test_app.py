"""Unit test untuk aplikasi To-Do."""
import pytest

from app.app import TASKS, app


@pytest.fixture(name="client")
def client_fixture():
    """Membuat test client dengan data bersih."""
    TASKS.clear()
    app.config["TESTING"] = True
    with app.test_client() as test_client:
        yield test_client


def test_index(client):
    """Halaman utama mengembalikan status running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["status"] == "running"


def test_health(client):
    """Health check mengembalikan ok."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_add_and_list_task(client):
    """Tugas yang ditambah muncul di daftar."""
    created = client.post("/tasks", json={"title": "Belajar CI/CD"})
    assert created.status_code == 201
    listed = client.get("/tasks")
    assert len(listed.get_json()) == 1


def test_add_task_without_title(client):
    """Tugas tanpa judul ditolak."""
    response = client.post("/tasks", json={})
    assert response.status_code == 400
