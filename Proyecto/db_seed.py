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

 # --- SEED CATEGORIES ---
    categories_data = [
        ("Novela", "Obras de ficción narrativa de cierta extensión"),
        ("Poesía", "Composiciones literarias en verso"),
        ("Ensayo", "Escritos breves que analizan un tema específico"),
        ("Biografía", "Relatos de la vida de personas reales"),
        ("Historia", "Obras sobre eventos históricos"),
        ("Ciencia Ficción", "Literatura basada en supuestos científicos"),
        ("Fantasía", "Obras con elementos mágicos o sobrenaturales"),
        ("Infantil", "Literatura dirigida a niños"),
        ("Terror", "Obras diseñadas para causar miedo"),
        ("Aventura", "Narrativas de viajes y acciones emocionantes")
    ]

    for nombre, descripcion in categories_data:
            nueva_categoria = Categoria(
                nombre=nombre,
                descripcion=descripcion
            )
            session.add(nueva_categoria)
            session.commit()

    #--- SEED BOOKS ---
    reviser = session.query(Usuario).filter_by(correo_electronico="suzana.revisor@example.com", estado=True).first()

    books_data = [
        ("La Eneida", "Virgilio", 290, "A1", "01"),
        ("Cien Años de Soledad", "Gabriel García Márquez", 417, "A1", "02"),
        ("Don Quijote de la Mancha", "Miguel de Cervantes", 863, "A1", "03"),
        ("Rayuela", "Julio Cortázar", 560, "A1", "04"),
        ("Pedro Páramo", "Juan Rulfo", 144, "A1", "05"),
        ("El Aleph", "Jorge Luis Borges", 157, "A1", "06"),
        ("La Ciudad y los Perros", "Mario Vargas Llosa", 376, "A1", "07"),
        ("El amor en los tiempos del cólera", "Gabriel García Márquez", 348, "A1", "08"),
        ("Ficciones", "Jorge Luis Borges", 200, "A1", "09"),
        ("Sobre héroes y tumbas", "Ernesto Sabato", 460, "A1", "10"),
        ("La tregua", "Mario Benedetti", 180, "A1", "11"),
        ("La casa de los espíritus", "Isabel Allende", 490, "A1", "12"),
    ]

    for titulo, autor, paginas, estanteria, espacio in books_data:
        nuevo_libro = Libro(
            titulo=titulo,
            autor=autor,
            fecha=datetime.now(),  # or a historical publication date
            numero_paginas=paginas,
            estanteria=estanteria,
            espacio=espacio,
            estado_id=lookup.estado_registrado.id
        )

        session.add(nuevo_libro)
        session.commit()

        new_book = session.query(Libro).filter_by(titulo=titulo).first()
        write_to_historial(
            inserted_usuario_id=reviser.id,
            inserted_accion_id=lookup.accion_crear.id,
            inserted_target_type_id=lookup.tt_libro.id,
            inserted_target_id=new_book.id
        )

    print("✅ Test data inserted successfully.")
