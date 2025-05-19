[![codecov](https://codecov.io/gh/juniors90/fastapitutorial/graph/badge.svg?token=FYn0fBOBP9)](https://codecov.io/gh/juniors90/fastapitutorial)

# Tutorial FastAPI

## Estructura de carpetas

´´´
fastapi_libros/
│
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   └── database.py
│
├── tests/
│   └── test_main.py
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── requirements.txt
└── pytest.ini
´´´

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