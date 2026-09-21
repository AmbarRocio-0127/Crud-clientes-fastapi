from fastapi import FastAPI, HTTPException #httpexception: clase de fastapi que permite gestionar errores
from pydantic import BaseModel #pydantic aplica tipado, validacion (por BaseModel) y lo correspondiente a un tipo de seguridad
from typing import List #List corresponde a la estructura de datos importada de python y tiene tipado fuerte

app = FastAPI()

class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    
clientes_db : List[Cliente] = []
contador_id = 1

#CREACION DE CRUD BASICO

# Endpoint de inicio
@app.get("/")
async def inicio():
    return{ "mensaje": "Backend Practice"}

# Crear un cliente
@app.post("/clientes", response_model=Cliente)
async def crear_cliente(cliente: Cliente):
    global contador_id
    cliente.id = contador_id
    clientes_db.append(cliente)
    contador_id += 1
    return cliente

# Listado de todos los elementos de la persistencia
@app.get("/clientes", response_model=List[Cliente])
async def listar_clientes():
    return clientes_db

# Listar un registro
@app.get("/clientes/{cliente_id}", response_model=Cliente)
async def obtener_cliente(cliente_id: int):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# Actualizar un registro
@app.put("/clientes/{cliente_id}", response_model=Cliente)
async def actualizar_cliente(cliente_id : int, cliente_actualizado : Cliente):
    for cliente in clientes_db:
        if cliente.id == cliente_id:
            cliente.nombre = cliente_actualizado.nombre
            cliente.edad = cliente_actualizado.edad
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")
        
#Eliminar un registro
@app.delete("/clientes/{cliente_id}")    
async def eliminar_cliente(cliente_id: int):
        for cliente in clientes_db:
            if cliente.id == cliente_id:
                clientes_db.remove(cliente)
                return {"mensaje":f"Cliente con ID {cliente_id} Eliminado con éxito!"}
        raise HTTPException(status_code=404, detail="Cliente no encontrado")