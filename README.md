# Crud-clientes-fastapi

API REST básica para gestionar clientes (crear, listar, consultar, actualizar y eliminar), construida con **FastAPI**. Es un proyecto de práctica para aprender los fundamentos de backend con Python.

## Tecnologías

- Python 3.9 o superior
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/) (servidor ASGI)
- [Pydantic](https://docs.pydantic.dev/) (validación de datos)

## Estructura del proyecto

```
proyecto2/
├── main.py            # Aplicación FastAPI, modelo y endpoints
├── requirements.txt   # Dependencias
└── README.md
```

## Ejecución

Desde la carpeta que contiene `main.py`:

```bash
uvicorn main:app --reload
```

La API quedará disponible en `http://127.0.0.1:8000`.

## Documentación interactiva

FastAPI genera la documentación automáticamente. Con el servidor corriendo, abre:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

Desde Swagger puedes probar todos los endpoints sin necesidad de otras herramientas.

## Modelo de datos

**Cliente**

| Campo    | Tipo   | Descripción                    |
|----------|--------|--------------------------------|
| `id`     | int    | Identificador único del cliente|
| `nombre` | string | Nombre del cliente             |
| `edad`   | int    | edad                           |

## Endpoints

| Método   | Ruta             | Descripción                    |
|----------|------------------|--------------------------------|
| `POST`   | `/clientes`      | Crear un nuevo cliente         |
| `GET`    | `/clientes`      | Listar todos los clientes      |
| `GET`    | `/clientes/{id}` | Obtener un cliente por su id   |
| `PUT`    | `/clientes/{id}` | Actualizar un cliente existente |
| `DELETE` | `/clientes/{id}` | Eliminar un cliente            |

## Notas

- Los datos se guardan **en memoria** (en una lista de Python), por lo que se pierden cada vez que se reinicia el servidor. No se usa base de datos.
- Este proyecto tiene fines educativos y no incluye autenticación.

## Posibles mejoras

- Conectar una base de datos (SQLite o PostgreSQL con SQLAlchemy).
- Separar el código en módulos (modelos, rutas, servicios).
- Agregar pruebas automáticas con `pytest`.
- Agregar autenticación.

## Autora

Proyecto desarrollado como práctica de backend con FastAPI.
