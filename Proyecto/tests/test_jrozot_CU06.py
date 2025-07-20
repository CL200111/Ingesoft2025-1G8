import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from unittest.mock import MagicMock, patch

from PyQt5.QtWidgets import QApplication
from use_cases.CU06_login_screen import LoginScreen
from db.models import Usuario

app = QApplication([])  # Required for QWidget-based tests


class TestLoginScreen(unittest.TestCase):
    def setUp(self):
        # Create a dummy user and callback
        self.mock_user = MagicMock(spec=Usuario)
        self.mock_user.verify_password.return_value = True

        self.login_success_callback = MagicMock()
        self.screen = LoginScreen(on_login_success=self.login_success_callback)

        # Patch UI inputs
        self.screen.ui.email_in.setText("")
        self.screen.ui.password_in.setText("")
        self.screen.ui.err_display.setText("")

    @patch("use_cases.CU06_login_screen.Database")
    def test_successful_login(self, mock_db):
        # Arrange
        self.screen.ui.email_in.setText("test@example.com")
        self.screen.ui.password_in.setText("secure123")

        session_mock = MagicMock()
        session_mock.query().filter_by().first.return_value = self.mock_user
        mock_db.return_value.get_session.return_value = session_mock

        # Act
        self.screen.handle_login()

        # Assert
        self.mock_user.verify_password.assert_called_once_with("secure123")
        self.login_success_callback.assert_called_once_with(self.mock_user)
        self.assertEqual(self.screen.ui.err_display.text(), "")

    @patch("use_cases.CU06_login_screen.Database")
    def test_invalid_credentials(self, mock_db):
        # Arrange
        self.screen.ui.email_in.setText("wrong@example.com")
        self.screen.ui.password_in.setText("wrongpass")

        session_mock = MagicMock()
        session_mock.query().filter_by().first.return_value = None
        mock_db.return_value.get_session.return_value = session_mock

        # Act
        self.screen.handle_login()

        # Assert
        self.assertEqual(
            self.screen.ui.err_display.text(),
            "❌ Credenciales inválidas o usuario inactivo",
        )
        self.login_success_callback.assert_not_called()

    def test_missing_fields(self):
        # Case: email and password empty
        self.screen.handle_login()
        self.assertEqual(
            self.screen.ui.err_display.text(), "⚠️ Todos los campos son obligatorios"
        )

        # Case: email only
        self.screen.ui.email_in.setText("only@example.com")
        self.screen.ui.password_in.setText("")
        self.screen.handle_login()
        self.assertEqual(
            self.screen.ui.err_display.text(), "⚠️ Todos los campos son obligatorios"
        )

        # Case: password only
        self.screen.ui.email_in.setText("")
        self.screen.ui.password_in.setText("onlypass")
        self.screen.handle_login()
        self.assertEqual(
            self.screen.ui.err_display.text(), "⚠️ Todos los campos son obligatorios"
        )
