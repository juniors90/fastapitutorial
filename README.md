
![Build Status](https://github.com/juniors90/fastapitutorial/actions/workflows/coverage.yml/badge.svg)
[![codecov](https://codecov.io/gh/juniors90/fastapitutorial/graph/badge.svg?token=FYn0fBOBP9)](https://codecov.io/gh/juniors90/fastapitutorial)
![GitHub Repo stars](https://img.shields.io/github/stars/juniors90/fastapitutorial)
![GitHub forks](https://img.shields.io/github/forks/juniors90/fastapitutorial)
[![issues](https://img.shields.io/github/issues/juniors90/fastapitutorial?color=teal)](https://github.com/juniors90/fastapitutorial/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/juniors90/fastapitutorial?color=green)](https://github.com/juniors90/fastapitutorial/graphs/contributors)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Tutorial FastAPI

## Estructura de carpetas

```
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
```

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