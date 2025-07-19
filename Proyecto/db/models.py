from sqlalchemy import (
    Column, Integer, String, Text, Date, DateTime, TIMESTAMP,
    ForeignKey, Boolean, create_engine
)
from sqlalchemy.orm import declarative_base, relationship
import bcrypt

Base = declarative_base()

# --- Lookup Tables ---

class Rol(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(String)

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

class TargetType(Base):
    __tablename__ = 'target_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)

class Accion(Base):
    __tablename__ = 'accion'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String)
    descripcion = Column(Text)

# --- Main Tables ---

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo_electronico = Column(String, unique=True)
    hash_contraseña = Column(String)
    rol_id = Column(Integer, ForeignKey('roles.id'))
    estado = Column(Boolean, default=True)  # active/inactive user

    rol = relationship("Rol")

    def verify_password(self, plain_password: str) -> bool:
        return bcrypt.checkpw(plain_password.encode('utf-8'), self.hash_contraseña.encode('utf-8'))

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

class Historial(Base):
    __tablename__ = 'historial'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fecha = Column(TIMESTAMP)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'))
    accion_id = Column(Integer, ForeignKey('accion.id'))
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
