# Proyecto/db/crear_usuario_admin.py

import bcrypt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pathlib import Path

from db_init import Base, Usuario, Rol

# Configuración de conexión
db_path = Path(__file__).resolve().parent / "books.db"
engine = create_engine(f"sqlite:///{db_path}", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# Verifica si ya existe el rol 'Administrador'
rol_admin = session.query(Rol).filter_by(nombre="Administrador").first()
if not rol_admin:
    rol_admin = Rol(nombre="Administrador", descripcion="Acceso completo al sistema")
    session.add(rol_admin)
    session.commit()
    print("✔️ Rol 'Administrador' creado.")

# Verifica si ya existe el usuario
usuario_existente = session.query(Usuario).filter_by(correo_electronico="admin@archibox.com").first()
if usuario_existente:
    print("⚠️ El usuario ya existe.")
else:
    contraseña_plana = "admin123"
    hash_pw = bcrypt.hashpw(contraseña_plana.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    nuevo_usuario = Usuario(
        nombres="Admin",
        apellidos="General",
        correo_electronico="admin@archibox.com",
        hash_contraseña=hash_pw,
        rol_id=rol_admin.id,
        estado=True
    )

    session.add(nuevo_usuario)
    session.commit()
    print("✅ Usuario administrador creado exitosamente.")