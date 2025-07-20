import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from ui.screens.ui_CU09_create_user_screen import Ui_create_user_screen
from use_cases.CU09_create_user_screen import CreateUserScreen

app = QApplication([])  # Necesario para iniciar widgets PyQt


class TestCreateUserScreen(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()
        self.mock_user.id = 1
        self.window = CreateUserScreen(user=self.mock_user)

        # Mock UI elements
        self.window.ui = Ui_create_user_screen()
        try:
            self.window.ui.setupUi(self.window)
        except RuntimeError:
            pass  # prevenir error de layout duplicado en test

        self.window.ui.nombresInput.text = MagicMock(return_value="Juan")
        self.window.ui.apellidosInput.text = MagicMock(return_value="Pérez")
        self.window.ui.emailInput.text = MagicMock(return_value="juan@example.com")
        self.window.ui.passwordInput.text = MagicMock(return_value="Segura123!")
        self.window.ui.rolComboBox.currentIndex = MagicMock(return_value=0)
        self.window.ui.rolComboBox.itemData = MagicMock(return_value=1)
        self.window.ui.errorLabel.setText = MagicMock()

    @patch("use_cases.CU09_create_user_screen.lookup")
    @patch("use_cases.CU09_create_user_screen.QMessageBox.information")
    @patch("use_cases.CU09_create_user_screen.write_to_historial")
    @patch("use_cases.CU09_create_user_screen.hash_password", return_value="hash")
    @patch("use_cases.CU09_create_user_screen.session")
    def test_create_user_success(
        self, mock_session, mock_hash, mock_log, mock_msgbox, mock_lookup
    ):
        # Simular que el usuario no existe en primera llamada, y devolver el nuevo usuario en la segunda
        mock_session.query.return_value.filter_by.return_value.first.side_effect = [
            None,  # No existe antes de crear
            MagicMock(id=123),  # Devuelto tras commit
        ]

        # Mock lookup
        mock_lookup.accion_crear.id = 2
        mock_lookup.tt_usuario.id = 3

        # Ejecutar
        self.window.create_user()

        # Validaciones
        mock_session.add.assert_called()
        mock_session.commit.assert_called()
        mock_log.assert_called_with(
            inserted_usuario_id=self.mock_user.id,
            inserted_accion_id=2,
            inserted_target_type_id=3,
            inserted_target_id=123,
        )
        mock_msgbox.assert_called_with(
            self.window, "Éxito", "Usuario creado exitosamente"
        )

    @patch("use_cases.CU09_create_user_screen.lookup")
    @patch("use_cases.CU09_create_user_screen.QMessageBox.warning")
    @patch("use_cases.CU09_create_user_screen.session")
    def test_create_user_duplicate_email(self, mock_session, mock_warning, mock_lookup):
        mock_existing_user = MagicMock(id=999)
        mock_session.query.return_value.filter_by.return_value.first.return_value = (
            mock_existing_user
        )

        # Ejecutar
        self.window.create_user()

        # Validar que no se hizo commit ni se añadió usuario
        mock_session.add.assert_not_called()
        mock_session.commit.assert_not_called()

        # Validar que el mensaje de error fue mostrado
        self.window.ui.errorLabel.setText.assert_called_with(
            "Ya existe un usuario con ese correo electrónico."
        )

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
