# Importar Librería de fastAPI
from fastapi import FastAPI

# Se crea una instancia (objeto) de fastAPI llamada app
app = FastAPI()

# Empezar a crear Apis con la anotacion @app
@app.get("/") #cuando se pone el back-slash indica que se va a la raiz de la pagina web
def inicio():
    return {"mensaje": "¡Practica Backend!"}