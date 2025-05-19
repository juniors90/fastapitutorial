[![codecov](https://codecov.io/gh/juniors90/fastapitutorial/graph/badge.svg?token=FYn0fBOBP9)](https://codecov.io/gh/juniors90/fastapitutorial)

# Tutorial FastAPI

## Estructura de carpetas

fastapi_libros/
│
├── main.py               # Punto de entrada
├── models.py             # Modelos SQLAlchemy
├── schemas.py            # Modelos Pydantic
├── database.py           # Conexión a la base de datos
├── crud.py               # Lógica de acceso a datos

## POST

```cmd
curl -X POST "http://127.0.0.1:8000/libros/" \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Rayuela", "autor": "Julio Cortázar"}'
```

```
curl -X POST "http://127.0.0.1:8000/libros/" \
     -H "Content-Type: application/json" \
     -d '{"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez"}'
```

```
curl -X POST "http://127.0.0.1:8000/libros/" \
     -H "Content-Type: application/json" \
     -d '{"titulo": "El Aleph", "autor": "Jorge Luis Borges"}'
```

```
echo "# fastapitutorial" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/juniors90/fastapitutorial.git
git push -u origin main
```