# tests/test_history_logger.py
import unittest
from unittest.mock import patch, MagicMock
from utils.history_logger import write_to_historial

class TestHistoryLogger(unittest.TestCase):

    @patch("utils.history_logger.session")
    def test_write_to_historial_success(self, mock_session):
        # Preparar mocks
        mock_add = MagicMock()
        mock_commit = MagicMock()
        mock_session.add = mock_add
        mock_session.commit = mock_commit

        # Ejecutar
        write_to_historial(
            inserted_usuario_id=1,
            inserted_accion_id=2,
            inserted_target_type_id=3,
            inserted_target_id=10
        )

        # Verificar que se llamó a add() y commit()
        self.assertTrue(mock_session.add.called)
        self.assertTrue(mock_session.commit.called)
        added_entry = mock_session.add.call_args[0][0]

        # Verificar contenido de la entrada agregada
        self.assertEqual(added_entry.usuario_id, 1)
        self.assertEqual(added_entry.accion_id, 2)
        self.assertEqual(added_entry.target_type_id, 3)
        self.assertEqual(added_entry.target_id, 10)

    @patch("utils.history_logger.session")
    def test_write_to_historial_db_failure(self, mock_session):
        # Simular error en commit
        mock_session.commit.side_effect = Exception("DB error")

        with self.assertRaises(Exception) as context:
            write_to_historial(
                inserted_usuario_id=1,
                inserted_accion_id=2,
                inserted_target_type_id=3,
                inserted_target_id=10
            )

        self.assertIn("DB error", str(context.exception))

if __name__ == '__main__':
    unittest.main()