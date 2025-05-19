from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_crear_y_leer_libro():
    # Crear un nuevo libro
    response = client.post("/libros/", json={"titulo": "1984", "autor": "George Orwell"})
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "1984"
    assert data["autor"] == "George Orwell"
    libro_id = data["id"]

    # Leer el libro creado
    response = client.get(f"/libros/{libro_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["titulo"] == "1984"
    assert data["autor"] == "George Orwell"
