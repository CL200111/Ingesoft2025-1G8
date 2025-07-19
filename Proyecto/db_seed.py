from datetime import datetime
from sqlalchemy.orm import sessionmaker
from db.database import Database
from db.models import Usuario, Libro, Tarea
from db.models import Rol, EstadoLibro, Categoria
from utils.password_hashing import hash_password
from utils.history_logger import write_to_historial
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

    admin = session.query(Usuario).filter_by(correo_electronico="root", estado=True).first()

    users = [
        Usuario(
            nombres="Suzana",
            apellidos="Horia",
            correo_electronico="suzana.revisor@example.com",
            hash_contraseña=hash_password("Abcd#1234"),
            rol_id=lookup.revisor_role.id,
            estado=True
        )
    ]

    session.add_all(users)
    session.commit()

    new_user = session.query(Usuario).filter_by(correo_electronico="suzana.revisor@example.com", estado=True).first()
    write_to_historial(
        inserted_usuario_id=admin.id,
        inserted_accion_id=lookup.accion_crear.id,
        inserted_target_type_id=lookup.tt_usuario.id,
        inserted_target_id=new_user.id
        )

    restaurador_user = Usuario(
        nombres="Camilo",
        apellidos="Restrepo",
        correo_electronico="camilo.restaurador@example.com",
        hash_contraseña=hash_password("Abcd#1234"),
        rol_id=lookup.restaurador_role.id,
        estado=True
    )

    session.add(restaurador_user)
    session.commit()

    restaurador_user = session.query(Usuario).filter_by(correo_electronico="camilo.restaurador@example.com").first()
    write_to_historial(
        inserted_usuario_id=admin.id,
        inserted_accion_id=lookup.accion_crear.id,
        inserted_target_type_id=lookup.tt_usuario.id,
        inserted_target_id=restaurador_user.id
    )

    digitalizador_user = Usuario(
        nombres="Laura",
        apellidos="Digitalez",
        correo_electronico="laura.digitalizadora@example.com",
        hash_contraseña=hash_password("Abcd#1234"),
        rol_id=lookup.digitalizador_role.id,
        estado=True
    )

    session.add(digitalizador_user)
    session.commit()

    digitalizador_user = session.query(Usuario).filter_by(correo_electronico="laura.digitalizadora@example.com").first()
    write_to_historial(
        inserted_usuario_id=admin.id,
        inserted_accion_id=lookup.accion_crear.id,
        inserted_target_type_id=lookup.tt_usuario.id,
        inserted_target_id=digitalizador_user.id
    )

    supervisor_user = Usuario(
        nombres="Carlos",
        apellidos="Calidad",
        correo_electronico="carlos.supervisor@example.com",
        hash_contraseña=hash_password("Abcd#1234"),
        rol_id=lookup.supervisor_role.id,
        estado=True
    )

    session.add(supervisor_user)
    session.commit()

    supervisor_user = session.query(Usuario).filter_by(correo_electronico="carlos.supervisor@example.com").first()
    write_to_historial(
        inserted_usuario_id=admin.id,
        inserted_accion_id=lookup.accion_crear.id,
        inserted_target_type_id=lookup.tt_usuario.id,
        inserted_target_id=supervisor_user.id
    )

    clasificador_user = Usuario(
        nombres="Valentina",
        apellidos="Clasifica",
        correo_electronico="valentina.clasificador@example.com",
        hash_contraseña=hash_password("Abcd#1234"),
        rol_id=lookup.clasificador_role.id,
        estado=True
    )

    session.add(clasificador_user)
    session.commit()

    clasificador_user = session.query(Usuario).filter_by(correo_electronico="valentina.clasificador@example.com").first()
    write_to_historial(
        inserted_usuario_id=admin.id,
        inserted_accion_id=lookup.accion_crear.id,
        inserted_target_type_id=lookup.tt_usuario.id,
        inserted_target_id=clasificador_user.id
    )

    lector_user = Usuario(
        nombres="Mateo",
        apellidos="Lector",
        correo_electronico="mateo.lector@example.com",
        hash_contraseña=hash_password("Abcd#1234"),
        rol_id=lookup.lector_role.id,
        estado=True
    )

    session.add(lector_user)
    session.commit()

    lector_user = session.query(Usuario).filter_by(correo_electronico="mateo.lector@example.com").first()
    write_to_historial(
        inserted_usuario_id=admin.id,
        inserted_accion_id=lookup.accion_crear.id,
        inserted_target_type_id=lookup.tt_usuario.id,
        inserted_target_id=lector_user.id
    )
    print("✅ Test data inserted successfully.")
