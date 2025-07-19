from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot
from ui.screens.ui_CU25_create_category_screen import Ui_create_category_screen
from db.database import Database
from db.models import Categoria, Historial
from utils.history_logger import write_to_historial
import db.lookup_cache as lookup

session = Database().get_session()

class CreateCategoryScreen(QWidget):
    def __init__(self, user=None):
        super().__init__()
        self.ui = Ui_create_category_screen()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.crear_categoria)
        self.user = user

    @pyqtSlot()
    def crear_categoria(self):
        """Registra una nueva categoría en el sistema"""
        nombre = self.ui.nombreInput.text().strip()
        descripcion = self.ui.descripcionInput.toPlainText().strip()

        # Validación de campos vacíos
        if not nombre:
            self._show_error("El nombre de la categoría es obligatorio.")
            return

        # Validación de longitud máxima
        if len(nombre) > 100:
            self._show_error("El nombre no puede exceder los 100 caracteres.")
            return

        # Verificar si la categoría ya existe
        categoria_existente = session.query(Categoria).filter_by(nombre=nombre).first()
        if categoria_existente:
            self._show_error(f"Ya existe una categoría con el nombre '{nombre}'.")
            return

        try:
            # Crear categoría
            nueva_categoria = Categoria(
                nombre=nombre,
                descripcion=descripcion if descripcion else None
            )

            session.add(nueva_categoria)
            session.commit()


    

            QMessageBox.information(
                self,
                "✅ Éxito",
                f"Categoría '{nombre}' creada exitosamente."
            )
            self._clear_form()

        except Exception as e:
            session.rollback()
            self._show_error(f"Error al crear la categoría: {str(e)}")

    def _clear_form(self):
        """Limpia el formulario"""
        self.ui.nombreInput.clear()
        self.ui.descripcionInput.clear()
        self.ui.errorLabel.setText("")

    def _show_error(self, message):
        """Muestra un mensaje de error"""
        self.ui.errorLabel.setText(message)