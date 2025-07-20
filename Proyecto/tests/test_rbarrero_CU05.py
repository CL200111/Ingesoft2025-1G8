# tests/test_classify_book.py
import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from use_cases.CU05_classify_book_screen import ClassifyBookScreen

app = QApplication([])  # Necesario para iniciar widgets PyQt


class TestClassifyBookScreen(unittest.TestCase):
    def setUp(self):
        self.mock_user = MagicMock()
        self.mock_user.id = 1

        # Parchar Database antes de crear la ventana
        patcher = patch("use_cases.CU05_classify_book_screen.Database")
        self.addCleanup(patcher.stop)
        self.mock_database_class = patcher.start()

        # Simular instancia de base de datos y sesión
        self.mock_session = MagicMock()
        mock_db_instance = MagicMock()
        mock_db_instance.get_session.return_value = self.mock_session
        self.mock_database_class.return_value = mock_db_instance

        # Instanciar pantalla con mocks
        self.window = ClassifyBookScreen(user=self.mock_user)

        # Mock UI components
        self.window.ui.book_combo.currentData = MagicMock(return_value=10)
        self.window.ui.category_combo.currentData = MagicMock(return_value=5)
        self.window.ui.title_display.setText = MagicMock()
        self.window.ui.author_display.setText = MagicMock()
        self.window.ui.current_category_display.setText = MagicMock()

    @patch("use_cases.CU05_classify_book_screen.QMessageBox.information")
    @patch("use_cases.CU05_classify_book_screen.write_to_historial")
    @patch("use_cases.CU05_classify_book_screen.lookup")
    def test_save_classification_success(
        self, mock_lookup, mock_write_historial, mock_info
    ):
        # Simular libro existente
        mock_estado = MagicMock(nombre="Pendiente")
        mock_book = MagicMock(id=10, titulo="Libro de prueba", estado=mock_estado)
        self.mock_session.query.return_value.get.return_value = mock_book

        # Simular estado "Clasificado"
        mock_estado_clasificado = MagicMock(id=99)
        self.mock_session.query.return_value.filter_by.return_value.first.return_value = mock_estado_clasificado

        # Simular lookup
        mock_lookup.accion_modificar.id = 2
        mock_lookup.tt_libro.id = 3

        # Ejecutar método
        self.window.save_classification()

        # Verificar interacciones clave
        self.assertEqual(mock_book.categoria_id, 5)
        self.assertEqual(mock_book.estado_id, 99)
        self.mock_session.commit.assert_called()
        mock_write_historial.assert_called_with(
            inserted_usuario_id=self.mock_user.id,
            inserted_accion_id=2,
            inserted_target_type_id=3,
            inserted_target_id=10,
        )
        mock_info.assert_called()

    def tearDown(self):
        self.window.close()


if __name__ == "__main__":
    unittest.main()
