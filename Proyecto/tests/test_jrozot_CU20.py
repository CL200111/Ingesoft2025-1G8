import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from unittest.mock import MagicMock, patch, ANY
from PyQt5.QtWidgets import QApplication
from use_cases.CU20_change_password_screen import ChangePasswordScreen

app = QApplication([])  # Required for QWidget

class TestChangePasswordScreen(unittest.TestCase):
    def setUp(self):
        # Mock user
        self.mock_user = MagicMock()
        self.mock_user.id = 1
        self.mock_user.verify_password.return_value = True

        # Patch QMessageBox
        self.messagebox_info = patch("use_cases.CU20_change_password_screen.QMessageBox.information").start()
        self.addCleanup(patch.stopall)

        # Instantiate screen
        self.screen = ChangePasswordScreen(user=self.mock_user)

        # Shortcuts for setting UI inputs
        self.ui = self.screen.ui
        self.ui.currentPasswordInput.setText("Current123!")
        self.ui.newPasswordInput.setText("NewPass123!")
        self.ui.confirmPasswordInput.setText("NewPass123!")

    def test_empty_fields(self):
        self.ui.currentPasswordInput.setText("")
        self.ui.newPasswordInput.setText("")
        self.ui.confirmPasswordInput.setText("")
        self.screen._handle_password_change()
        self.assertEqual(self.ui.errorLabel.text(), "Todos los campos son obligatorios.")

    def test_invalid_current_password(self):
        self.mock_user.verify_password.return_value = False
        self.screen._handle_password_change()
        self.assertEqual(self.ui.errorLabel.text(), "La contraseña actual es incorrecta.")

    def test_passwords_do_not_match(self):
        self.ui.confirmPasswordInput.setText("Different123!")
        self.screen._handle_password_change()
        self.assertEqual(self.ui.errorLabel.text(), "Las nuevas contraseñas no coinciden.")

    def test_invalid_new_password(self):
        self.ui.newPasswordInput.setText("weak")  # too short, no number, etc.
        self.ui.confirmPasswordInput.setText("weak")
        self.screen._handle_password_change()
        self.assertEqual(self.ui.errorLabel.text(), "La nueva contraseña no cumple con los requisitos.")

    @patch("use_cases.CU20_change_password_screen.session")
    @patch("use_cases.CU20_change_password_screen.hash_password", return_value="hashed123")
    @patch("use_cases.CU20_change_password_screen.write_to_historial")
    def test_successful_password_change(self, mock_write_historial, mock_hash, mock_session):
        # Mock DB user result
        mock_user_db = MagicMock()
        mock_session.query().filter_by().first.return_value = mock_user_db

        self.screen._handle_password_change()

        # Assertions
        self.assertEqual(mock_user_db.hash_contraseña, "hashed123")
        mock_session.commit.assert_called_once()
        mock_write_historial.assert_called_once_with(
            inserted_usuario_id=1,

            inserted_accion_id=ANY,
            inserted_target_type_id=ANY,

            #inserted_accion_id=patch.ANY,  # Assuming lookup is not mocked here
            #inserted_target_type_id=patch.ANY,
            inserted_target_id=1
        )
        self.messagebox_info.assert_called_once_with(self.screen, "Éxito", "Contraseña actualizada correctamente.")
        self.assertEqual(self.ui.currentPasswordInput.text(), "")
        self.assertEqual(self.ui.newPasswordInput.text(), "")
        self.assertEqual(self.ui.confirmPasswordInput.text(), "")
        self.assertEqual(self.ui.errorLabel.text(), "")

#if __name__ == "__main__":
#    unittest.main()
