from pydantic import BaseModel, ConfigDict


class LibroBase(BaseModel):
    titulo: str
    autor: str


class LibroCreate(LibroBase):
    pass


class Libro(LibroBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
