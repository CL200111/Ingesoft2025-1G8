from database import Database
from models import Rol, EstadoLibro, TargetType, Accion

# Start DB session
session = Database().get_session()

# After session.commit()

# Roles
admin_role = session.query(Rol).filter_by(nombre="Administrador").first()
revisor_role = session.query(Rol).filter_by(nombre="Revisor").first()
restaurador_role = session.query(Rol).filter_by(nombre="Restaurador").first()
digitalizador_role = session.query(Rol).filter_by(nombre="Digitalizador").first()
supervisor_role = session.query(Rol).filter_by(nombre="Supervisor de calidad").first()
clasificador_role = session.query(Rol).filter_by(nombre="Clasificador").first()
lector_role = session.query(Rol).filter_by(nombre="Lector").first()

# Target Types
tt_usuario = session.query(TargetType).filter_by(nombre="usuario").first()
tt_libro = session.query(TargetType).filter_by(nombre="libro").first()
tt_tarea = session.query(TargetType).filter_by(nombre="tarea").first()
tt_categoria = session.query(TargetType).filter_by(nombre="categoria").first()

# Estados del libro
estado_recepcion = session.query(EstadoLibro).filter_by(nombre="En recepcion").first()
estado_registrado = session.query(EstadoLibro).filter_by(nombre="Registrado").first()
estado_revision = session.query(EstadoLibro).filter_by(nombre="En revisión física").first()
estado_revision_aprobada = session.query(EstadoLibro).filter_by(nombre="Aprobado de revisión física").first()
estado_restauracion = session.query(EstadoLibro).filter_by(nombre="En restauración").first()
estado_restaurado = session.query(EstadoLibro).filter_by(nombre="Restaurado").first()
estado_digitalizacion = session.query(EstadoLibro).filter_by(nombre="En digitalización").first()
estado_digitalizado = session.query(EstadoLibro).filter_by(nombre="Digitalizado").first()
estado_calidad = session.query(EstadoLibro).filter_by(nombre="En control de calidad").first()
estado_calidad_aprobado = session.query(EstadoLibro).filter_by(nombre="Aprobado por control de calidad").first()
estado_clasificacion = session.query(EstadoLibro).filter_by(nombre="En clasificación").first()
estado_clasificado = session.query(EstadoLibro).filter_by(nombre="Clasificado").first()
estado_publicado = session.query(EstadoLibro).filter_by(nombre="Publicado").first()
estado_almacenado = session.query(EstadoLibro).filter_by(nombre="Almacenado").first()

# Acciones
accion_crear = session.query(Accion).filter_by(nombre="crear").first()
accion_modificar = session.query(Accion).filter_by(nombre="modificar").first()
accion_eliminar = session.query(Accion).filter_by(nombre="eliminar").first()
accion_iniciar = session.query(Accion).filter_by(nombre="iniciar tarea").first()
accion_completar = session.query(Accion).filter_by(nombre="completar tarea").first()

