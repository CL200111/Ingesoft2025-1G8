from sqlalchemy import (
    create_engine, Column, Integer, String, Text, Date, DateTime,
    ForeignKey, UniqueConstraint, Boolean, TIMESTAMP
)
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

from pathlib import Path

# Get path to books.db on the same level of this file
db_path = Path(__file__).resolve().parent / "books.db"

# Create SQLite engine and base class
engine = create_engine(f"sqlite:///{db_path}", echo=True)
#engine = create_engine('sqlite:///books.db', echo=True)

Base = declarative_base()

# --- Tables ---

class EstadoLibro(Base):
    __tablename__ = 'estados_libro'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(Text)
    orden = Column(Integer)

class Categoria(Base):
    __tablename__ = 'categoria'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(Text)

class Libro(Base):
    __tablename__ = 'libros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    isbn = Column(String)
    titulo = Column(String)
    autor = Column(String)
    fecha = Column(Date)
    numero_paginas = Column(Integer)
    estado_id = Column(Integer, ForeignKey('estados_libro.id'))
    estanteria = Column(String)
    espacio = Column(String)
    categoria_id = Column(Integer, ForeignKey('categoria.id'))
    directorio_pdf = Column(String)

    estado = relationship("EstadoLibro")
    categoria = relationship("Categoria")

class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo_electronico = Column(String, unique=True)
    hash_contraseña = Column(String)
    rol_id = Column(Integer, ForeignKey('roles.id'))
    estado = Column(Boolean, default=True)

    rol = relationship("Rol")

class TargetType(Base):
    __tablename__ = 'target_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

class Accion(Base):
    __tablename__ = 'accion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(Text)

class Historial(Base):
    __tablename__ = 'historial'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(TIMESTAMP)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    accion_id = Column(String, ForeignKey('accion.id'))
    target_type_id = Column(Integer, ForeignKey('target_type.id'))
    target_id = Column(Integer)

    usuario = relationship("Usuario")
    accion = relationship("Accion")
    target_type = relationship("TargetType")

class Tarea(Base):
    __tablename__ = 'tareas'
    id = Column(Integer, primary_key=True, autoincrement=True)
    libro_id = Column(Integer, ForeignKey('libros.id'))
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    fecha_asignacion = Column(DateTime)
    fecha_finalizacion = Column(TIMESTAMP)
    estado_nuevo_id = Column(Integer, ForeignKey('estados_libro.id'))
    observaciones = Column(Text)

    libro = relationship("Libro")
    usuario = relationship("Usuario")
    nuevo_estado = relationship("EstadoLibro", foreign_keys=[estado_nuevo_id])

# --- Fill lookup tables ---
if __name__ == '__main__':
    Base.metadata.create_all(engine)
    print("📚 Database initialized successfully.")

    Session = sessionmaker(bind=engine)
    session = Session()

    roles = [
        Rol(nombre="Administrador", descripcion="Administrador del sistema"),
        Rol(nombre="Revisor", descripcion="Revisa que el estado físico de los libros sea aceptable"),
        Rol(nombre="Restaurador", descripcion="Mejora la condición física de lol libros que lo requieren"),
        Rol(nombre="Digitalizador", descripcion="Escanéa los libros para convertirlos a formato digital"),
        Rol(nombre="Supervisor de calidad", descripcion="Revisa que la digitalización del libro cumpla con etándares de calidad"),
        Rol(nombre="Clasificador", descripcion="Encargado de clasificar un libro por su temática"),
        Rol(nombre="Lector", descripcion="Consume y consulta los libros digitalizados")
    ]
    session.add_all(roles)

    target_types = [
        TargetType(nombre="usuario"),
        TargetType(nombre="libro"),
        TargetType(nombre="tarea"),
        TargetType(nombre="categoria")
    ]

    estados_libro = [
        EstadoLibro(nombre="En recepcion", descripcion="Aún no procesado", orden=1),
        EstadoLibro(nombre="Registrado", descripcion="Se ha almacenado la información inicial del libro en el sistema", orden=2),
        EstadoLibro(nombre="En revisión física", descripcion="El revisor está tomando registro del estado físico del libro", orden=3),
        EstadoLibro(nombre="Aprobado de revisión física", descripcion="El libro cumple con los estándares de calidad en su estado físico", orden=4),
        EstadoLibro(nombre="En restauración", descripcion="El libro se encuentra en reparación física", orden=5),
        EstadoLibro(nombre="Restaurado", descripcion="La restauración ha sido completada y se espera aprobar la revisión de calidad", orden=6),
        EstadoLibro(nombre="En digitalización", descripcion="El libro se encuentra siendo escaneado", orden=7),
        EstadoLibro(nombre="Digitalizado", descripcion="El libro ha sido completamente escaneado", orden=8),
        EstadoLibro(nombre="En control de calidad", descripcion="El supervisor de calidad esta revisando la calidad de la digitalización", orden=9),
        EstadoLibro(nombre="Aprobado por control de calidad", descripcion="El libro ha sido digitalizado a plenitud", orden=10),
        EstadoLibro(nombre="En clasificación", descripcion="El libro se encuentra siendo clasificado por su temática", orden=11),
        EstadoLibro(nombre="Clasificado", descripcion="Una clasificación apropiada ha sido agregada a el libro", orden=12),
        EstadoLibro(nombre="Publicado", descripcion="El libro está disponible para ser descargado por los lectores", orden=13),
        EstadoLibro(nombre="Almacenado", descripcion="El libro ha sido llevado a un estante para ser almacenado definitivamente", orden=14)
    ]
    session.add_all(estados_libro)

    acciones = [
        Accion(nombre="crear", descripcion="Creación de un registro"),
        Accion(nombre="modificar", descripcion="Modificación de un registro existente"),
        Accion(nombre="eliminar", descripcion="Eliminación de un registro"),
        Accion(nombre="iniciar tarea", descripcion="Inicio de una tarea"),
        Accion(nombre="completar tarea", descripcion="Finalización de una tarea")
    ]
    session.add_all(acciones)

    session.commit()
    print("📚 Database initialized successfully.")
