from sqlalchemy.orm import Session
import models, schemas


def get_libros(db: Session):
    return db.query(models.Libro).all()


def get_libro(db: Session, libro_id: int):
    return db.query(models.Libro).filter(models.Libro.id == libro_id).first()


def create_libro(db: Session, libro: schemas.LibroCreate):
    db_libro = models.Libro(**libro.dict())
    db.add(db_libro)
    db.commit()
    db.refresh(db_libro)
    return db_libro


def delete_libro(db: Session, libro_id: int):
    libro = get_libro(db, libro_id)
    if libro:
        db.delete(libro)
        db.commit()
    return libro


def update_libro(db: Session, libro_id: int, libro_data: schemas.LibroCreate):
    libro = get_libro(db, libro_id)
    if libro:
        libro.titulo = libro_data.titulo
        libro.autor = libro_data.autor
        db.commit()
        db.refresh(libro)
    return libro
