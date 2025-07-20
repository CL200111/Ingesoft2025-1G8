import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from use_cases.CU01_register_book_screen import RegisterBookScreen

app = QApplication([])


class TestRegisterBookScreen(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()
        self.mock_user.id = 1

        patcher = patch("use_cases.CU01_register_book_screen.Database")
        self.addCleanup(patcher.stop)
        self.mock_db_class = patcher.start()

        self.mock_session = MagicMock()
        self.mock_db_instance = MagicMock()
        self.mock_db_instance.get_session.return_value = self.mock_session
        self.mock_db_class.return_value = self.mock_db_instance

        self.window = RegisterBookScreen(user=self.mock_user)

        self.window.ui.tituloInput.text = MagicMock(return_value="Libro Test")
        self.window.ui.autorInput.text = MagicMock(return_value="Autor Test")
        self.window.ui.paginasInput.text = MagicMock(return_value="100")
        self.window.ui.estanteriaInput.text = MagicMock(return_value="A1")
        self.window.ui.espacioInput.text = MagicMock(return_value="10")
        self.window.ui.fechaInput.date().toPyDate = MagicMock(return_value="2025-01-01")
        self.window._clear_form = MagicMock()
        self.window._show_error = MagicMock()
        self.window.ui.errorLabel.setText = MagicMock()

    @patch("use_cases.CU01_register_book_screen.write_to_historial")
    @patch("use_cases.CU01_register_book_screen.lookup")
    @patch("use_cases.CU01_register_book_screen.QMessageBox.information")
    def test_registrar_libro_success(
        self, mock_info, mock_lookup, mock_write_historial
    ):
        mock_estado = MagicMock()
        mock_estado.id = 5
        self.mock_session.query.return_value.filter_by.return_value.first.return_value = mock_estado

        mock_libro = MagicMock()
        mock_libro.id = 42
        self.mock_session.query.return_value.filter_by.return_value.first.return_value = mock_libro

        mock_lookup.accion_crear.id = 1
        mock_lookup.tt_libro.id = 2

        self.window.registrar_libro()

        self.mock_session.add.assert_called()
        self.mock_session.commit.assert_called()
        mock_write_historial.assert_called_with(
            inserted_usuario_id=1,
            inserted_accion_id=1,
            inserted_target_type_id=2,
            inserted_target_id=42,
        )
        mock_info.assert_called()

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
