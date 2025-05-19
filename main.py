from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine, Base

# Crear tablas
Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/libros/", response_model=schemas.Libro)
def crear_libro(libro: schemas.LibroCreate, db: Session = Depends(get_db)):
    return crud.create_libro(db, libro)


@app.get("/libros/", response_model=list[schemas.Libro])
def leer_libros(db: Session = Depends(get_db)):
    return crud.get_libros(db)


@app.get("/libros/{libro_id}", response_model=schemas.Libro)
def leer_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.get_libro(db, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro


@app.put("/libros/{libro_id}", response_model=schemas.Libro)
def actualizar_libro(
    libro_id: int, libro: schemas.LibroCreate, db: Session = Depends(get_db)
):
    libro_actualizado = crud.update_libro(db, libro_id, libro)
    if libro_actualizado is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return libro_actualizado


@app.delete("/libros/{libro_id}")
def borrar_libro(libro_id: int, db: Session = Depends(get_db)):
    libro = crud.delete_libro(db, libro_id)
    if libro is None:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"mensaje": "Libro eliminado"}
