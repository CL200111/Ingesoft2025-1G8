from datetime import datetime
from sqlalchemy.orm import sessionmaker
from database import Database
from models import Usuario, Libro, Tarea
from models import Rol, EstadoLibro, Categoria
from utils.password_hashing import hash_password
import lookup_cache as lookup

# Start DB session
session = Database().get_session()

# --- Seed example users ---

admin = [
    Usuario(
        nombres="Elber",
        apellidos="Gón",
        correo_electronico="root",
        hash_contraseña=hash_password("1234"),
        rol_id=lookup.admin_role.id,
        estado=True
    )
]

session.add_all(admin)
session.commit()

print("✅ Test data inserted successfully.")
