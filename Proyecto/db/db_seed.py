from datetime import datetime
from sqlalchemy.orm import sessionmaker
from database import Database
from models import Usuario, Libro, Tarea
from models import Rol, EstadoLibro, Categoria
import hashlib

# Start DB session
session = Database().get_session()

# --- Helper: simple password hashing ---
def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

# --- Seed example users ---
admin_role = session.query(Rol).filter_by(nombre="admin").first()
restaurador_role = session.query(Rol).filter_by(nombre="restaurador").first()

test_users = [
    Usuario(
        nombres="Ana",
        apellidos="Gómez",
        correo_electronico="ana@example.com",
        hash_contraseña=hash_password("1234"),
        rol_id=admin_role.id,
        estado=True
    ),
    Usuario(
        nombres="Carlos",
        apellidos="Ríos",
        correo_electronico="carlos@example.com",
        hash_contraseña=hash_password("5678"),
        rol_id=restaurador_role.id,
        estado=True
    )
]

session.add_all(test_users)
session.commit()

# --- Seed example books ---
pending_state = session.query(EstadoLibro).filter_by(nombre="pendiente").first()
history_cat = session.query(Categoria).filter_by(nombre="historia").first()

libros = [
    Libro(
        isbn="123-456-789",
        titulo="Historia de Colombia",
        autor="Juan Pérez",
        fecha=datetime(1950, 1, 1),
        numero_paginas=350,
        estado_id=pending_state.id,
        estanteria="A",
        espacio="3",
        categoria_id=history_cat.id,
        directorio_pdf="/pdfs/colombia.pdf"
    ),
    Libro(
        isbn="987-654-321",
        titulo="Los secretos del arte",
        autor="María Ruiz",
        fecha=datetime(1975, 5, 20),
        numero_paginas=220,
        estado_id=pending_state.id,
        estanteria="B",
        espacio="1",
        categoria_id=None,
        directorio_pdf="/pdfs/arte.pdf"
    )
]

session.add_all(libros)
session.commit()

# --- Seed a test task ---
usuario = session.query(Usuario).filter_by(correo_electronico="carlos@example.com").first()
libro = session.query(Libro).filter_by(titulo="Historia de Colombia").first()

nueva_tarea = Tarea(
    libro_id=libro.id,
    usuario_id=usuario.id,
    fecha_asignacion=datetime.now(),
    fecha_finalizacion=None,
    estado_nuevo_id=pending_state.id,
    observaciones="Primera revisión en curso."
)

session.add(nueva_tarea)
session.commit()

print("✅ Test data inserted successfully.")
