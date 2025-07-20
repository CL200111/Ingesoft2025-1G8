import unittest
from unittest.mock import MagicMock, patch
from PyQt5.QtWidgets import QApplication
from use_cases.CU25_create_category_screen import CreateCategoryScreen

# Necesario para pruebas de PyQt
app = QApplication([])


class TestCreateCategoryScreen(unittest.TestCase):
    def setUp(self):
        # Configuración inicial para cada test
        self.mock_session = MagicMock()
        self.mock_user = MagicMock()
        self.mock_user.id = 1

        # Parchear la sesión de la base de datos
        self.patcher_session = patch(
            "CU25_create_category_screen.session", self.mock_session
        )
        self.patcher_session.start()

        # Crear instancia de la pantalla
        self.screen = CreateCategoryScreen(user=self.mock_user)

        # Configurar mocks para los inputs
        self.screen.ui.nombreInput = MagicMock()
        self.screen.ui.descripcionInput = MagicMock()
        self.screen.ui.errorLabel = MagicMock()

        # Mock para QMessageBox
        self.patcher_msgbox = patch("CU25_create_category_screen.QMessageBox")
        self.mock_msgbox = self.patcher_msgbox.start()
        self.mock_msgbox_instance = MagicMock()
        self.mock_msgbox.return_value = self.mock_msgbox_instance

    def tearDown(self):
        # Limpiar los patches después de cada test
        self.patcher_session.stop()
        self.patcher_msgbox.stop()

    def test_crear_categoria_campos_vacios(self):
        """Test cuando el nombre está vacío"""
        self.screen.ui.nombreInput.text.return_value = ""

        self.screen.crear_categoria()

        # Verificar que se mostró el error correcto
        self.screen.ui.errorLabel.setText.assert_called_with(
            "El nombre de la categoría es obligatorio."
        )
        # Verificar que no se intentó guardar en la base de datos
        self.mock_session.add.assert_not_called()

    def test_crear_categoria_nombre_largo(self):
        """Test cuando el nombre excede el límite de caracteres"""
        long_name = "a" * 101
        self.screen.ui.nombreInput.text.return_value = long_name

        self.screen.crear_categoria()

        self.screen.ui.errorLabel.setText.assert_called_with(
            "El nombre no puede exceder los 100 caracteres."
        )
        self.mock_session.add.assert_not_called()

    def test_crear_categoria_existente(self):
        """Test cuando la categoría ya existe"""
        existing_name = "Categoría Existente"
        self.screen.ui.nombreInput.text.return_value = existing_name

        # Configurar mock para simular que la categoría ya existe
        mock_existing = MagicMock()
        self.mock_session.query.return_value.filter_by.return_value.first.return_value = mock_existing

        self.screen.crear_categoria()

        self.screen.ui.errorLabel.setText.assert_called_with(
            f"Ya existe una categoría con el nombre '{existing_name}'."
        )
        self.mock_session.add.assert_not_called()

    @patch("CU25_create_category_screen.write_to_historial")
    def test_crear_categoria_exito(self, mock_write_historial):
        """Test creación exitosa de categoría"""
        test_name = "Nueva Categoría"
        test_desc = "Descripción de prueba"

        self.screen.ui.nombreInput.text.return_value = test_name
        self.screen.ui.descripcionInput.toPlainText.return_value = test_desc

        # Configurar mock para nueva categoría
        mock_new_category = MagicMock()
        mock_new_category.id = 123
        mock_new_category.nombre = test_name
        self.mock_session.query.return_value.filter_by.return_value.first.return_value = mock_new_category

        self.screen.crear_categoria()

        # Verificar que se agregó a la sesión
        self.mock_session.add.assert_called_once()
        self.mock_session.commit.assert_called_once()

        # Verificar que se mostró mensaje de éxito
        self.mock_msgbox.information.assert_called_once()

        # Verificar que se registró en el historial
        mock_write_historial.assert_called_once_with(
            inserted_usuario_id=self.mock_user.id,
            inserted_accion_id=MagicMock().id,  # No podemos mockear el lookup directamente
            inserted_target_type_id=MagicMock().id,
            inserted_target_id=mock_new_category.id,
        )

        # Verificar que se limpió el formulario
        self.screen.ui.nombreInput.clear.assert_called_once()
        self.screen.ui.descripcionInput.clear.assert_called_once()
        self.screen.ui.errorLabel.setText.assert_called_with("")

    def test_crear_categoria_error_db(self):
        """Test cuando hay un error en la base de datos"""
        test_name = "Categoría con Error"
        self.screen.ui.nombreInput.text.return_value = test_name

        # Configurar mock para lanzar excepción al hacer commit
        self.mock_session.commit.side_effect = Exception("Error de DB")

        self.screen.crear_categoria()

        # Verificar que se hizo rollback
        self.mock_session.rollback.assert_called_once()

        # Verificar que se mostró el error
        self.screen.ui.errorLabel.setText.assert_called_with(
            "Error al crear la categoría: Error de DB"
        )


if __name__ == "__main__":
    unittest.main()
