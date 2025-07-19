from datetime import datetime
from sqlalchemy.orm import sessionmaker
from db.database import Database
from db.models import Usuario, Libro, Tarea
from db.models import Rol, EstadoLibro, Categoria
from utils.password_hashing import hash_password
import db.lookup_cache as lookup

if __name__ == "__main__":
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
