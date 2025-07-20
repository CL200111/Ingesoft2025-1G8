# tests/test_register_condition.py
import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from use_cases.CU02_register_condition_screen import RegisterConditionScreen

app = QApplication([])


class TestRegisterConditionScreen(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()
        self.mock_user.id = 1

        patcher_db = patch("use_cases.CU02_register_condition_screen.Database")
        self.addCleanup(patcher_db.stop)
        self.mock_database_class = patcher_db.start()

        mock_db_instance = MagicMock()
        self.mock_session = MagicMock()
        mock_db_instance.get_session.return_value = self.mock_session
        self.mock_database_class.return_value = mock_db_instance

        self.window = RegisterConditionScreen(user=self.mock_user)

        self.patcher_msgbox = patch(
            "use_cases.CU02_register_condition_screen.QMessageBox.information"
        )
        self.mock_msgbox = self.patcher_msgbox.start()
        self.addCleanup(self.patcher_msgbox.stop)

        self.patcher_lookup = patch("use_cases.CU02_register_condition_screen.lookup")
        self.mock_lookup = self.patcher_lookup.start()
        self.addCleanup(self.patcher_lookup.stop)

        self.patcher_historial = patch(
            "use_cases.CU02_register_condition_screen.write_to_historial"
        )
        self.mock_historial = self.patcher_historial.start()
        self.addCleanup(self.patcher_historial.stop)

        self.window.ui.libroIdInput.setText("123")
        self.window.ui.condicionComboBox.currentData = MagicMock(return_value="bueno")
        self.window.ui.fechaInicioEdit.date = MagicMock()
        self.window.ui.fechaFinEdit.date = MagicMock()
        today = app.primaryScreen().availableGeometry().topLeft().toTuple()
        self.window.ui.fechaInicioEdit.date().toPyDate.return_value = self.window.ui.fechaFinEdit.date().toPyDate.return_value = today

    def test_registrar_revision_exito(self):
        mock_estado = MagicMock(nombre="Registrado")
        mock_libro = MagicMock(id=123, estado_id=1)
        self.mock_session.query.return_value.get.return_value = mock_libro
        self.mock_session.query.return_value.filter_by.return_value.first.side_effect = [
            mock_estado,
            MagicMock(id=999),
        ]

        self.mock_lookup.accion_modificar.id = 2
        self.mock_lookup.tt_libro.id = 3

        self.window.registrar_revision()

        self.assertEqual(mock_libro.estado_id, 999)
        self.mock_session.commit.assert_called()
        self.mock_historial.assert_called_with(
            inserted_usuario_id=self.mock_user.id,
            inserted_accion_id=2,
            inserted_target_type_id=3,
            inserted_target_id=123,
        )
        self.mock_msgbox.assert_called()

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
