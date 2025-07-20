from datetime import datetime
from db.database import Database
from db.models import Historial

session = Database().get_session()


def write_to_historial(
    inserted_usuario_id: int,
    inserted_accion_id: int,
    inserted_target_type_id: int,
    inserted_target_id: int,
):
    """
    Records an action in the historial table.
    Args:
        user_id (int): ID of the user performing the action.
        action_name (str): Name of the action (e.g., "crear usuario").
        target_type_name (str): Name of the target type (e.g., "usuario").
        target_id (int): ID of the target object.
    """
    # accion = session.query(Accion).filter_by(nombre=action_name).first()
    # target_type = session.query(TargetType).filter_by(nombre=target_type_name).first()

    # if not accion or not target_type:
    #    print(f"⚠️ Acción o TargetType no encontrado: '{action_name}', '{target_type_name}'")
    #    return

    historial_entry = Historial(
        fecha=datetime.now(),
        usuario_id=inserted_usuario_id,
        accion_id=inserted_accion_id,
        target_type_id=inserted_target_type_id,
        target_id=inserted_target_id,
    )

    session.add(historial_entry)
    session.commit()
    print(
        f"✅ Historial registrado: Usuario {inserted_usuario_id} hizo '{inserted_accion_id}' sobre {inserted_target_type_id}({inserted_target_id})"
    )
