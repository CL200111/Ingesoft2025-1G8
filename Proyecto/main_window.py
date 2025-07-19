from PyQt5.QtWidgets import QMainWindow, QPushButton
from ui.ui_main_window import Ui_MainWindow
from PyQt5.QtGui import QIcon

from utils.path_utils import get_asset_path

# Import all CU screens (except CU06_login_screen)
from use_cases.CU01_register_book_screen import RegisterBookScreen
from use_cases.CU02_register_condition_screen import RegisterConditionScreen
from use_cases.CU03_restore_book_screen import RestoreBookScreen
from use_cases.CU04_digitize_book_screen import DigitizeBookScreen
from use_cases.CU05_classify_book_screen import ClassifyBookScreen
from use_cases.CU07_query_book_history_screen import QueryBookHistoryScreen
from use_cases.CU08_generate_report_screen import GenerateReportScreen
from use_cases.CU09_create_user_screen import CreateUserScreen
from use_cases.CU10_edit_user_screen import EditUserScreen
from use_cases.CU11_deactivate_user_screen import DeactivateUserScreen
from use_cases.CU12_modify_book_screen import ModifyBookScreen
from use_cases.CU13_deactivate_book_screen import DeactivateBookScreen
from use_cases.CU14_notification_screen import NotificationScreen
from use_cases.CU15_physical_qa_screen import PhysicalQaScreen
from use_cases.CU16_filter_books_by_state_screen import FilterBooksByStateScreen
from use_cases.CU17_search_books_screen import SearchBooksScreen
from use_cases.CU18_search_users_screen import SearchUsersScreen
from use_cases.CU19_assign_task_screen import AssignTaskScreen
from use_cases.CU20_change_password_screen import ChangePasswordScreen
from use_cases.CU21_restore_password_screen import RestorePasswordScreen
from use_cases.CU22_query_book_screen import QueryBookScreen
from use_cases.CU23_download_book_screen import DownloadBookScreen
from use_cases.CU24_digital_qa_screen import DigitalQaScreen
from use_cases.CU25_create_category_screen import CreateCategoryScreen


class MainWindow(QMainWindow):
    def __init__(self, user=None):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QIcon(get_asset_path("ArchiBox_alpha_icon.png")))  # or "app_icon.ico"

        self.user = user  # Could be passed from login window

        self.routes = {
            "Tablero": 0,
            "Registrar Libro": RegisterBookScreen(self.user),
            "Registrar Condición": RegisterConditionScreen(self.user),
            "Restaurar Libro": RestoreBookScreen(self.user),
            "Digitalizar Libro": DigitizeBookScreen(self.user),
            "Clasificar Libro": ClassifyBookScreen(),
            "Consultar Historial de Libro": QueryBookHistoryScreen(),
            "Generar Reporte": GenerateReportScreen(),
            "Crear Usuario": CreateUserScreen(self.user),
            "Editar Usuario": EditUserScreen(),
            "Desactivar Usuario": DeactivateUserScreen(),
            "Modificar Libro": ModifyBookScreen(),
            "Desactivar Libro": DeactivateBookScreen(),
            "Notificaciones": NotificationScreen(),
            "Calidad Física": PhysicalQaScreen(),
            "Filtrar Libros por Estado": FilterBooksByStateScreen(),
            "Buscar Libros": SearchBooksScreen(),
            "Buscar Usuarios": SearchUsersScreen(),
            "Asignar Tarea": AssignTaskScreen(),
            "Cambiar Contraseña": ChangePasswordScreen(),
            "Restaurar Contraseña": RestorePasswordScreen(),
            "Consultar Libro": QueryBookScreen(),
            "Descargar Libro": DownloadBookScreen(),
            "Calidad Digital": DigitalQaScreen(),
            "Crear Categoría": CreateCategoryScreen(self.user),
        }

        # Mapeo de roles a características disponibles
        role_permissions = {
            "Administrador": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Crear Usuario", "Editar Usuario", "Desactivar Usuario", "Buscar Usuarios",
                "Modificar Libro", "Generar Reporte", "Restaurar Contraseña",
                "Consultar Historial de Libro", "Asignar Tarea", "Crear Categoría",
                "Desactivar Libro"
            ],
            "Revisor": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Registrar Libro", "Registrar Condición"
            ],
            "Restaurador": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Restaurar Libro"
            ],
            "Digitalizador": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Digitalizar Libro"
            ],
            "Supervisor de calidad": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Calidad Digital", "Calidad Física"
            ],
            "Clasificador": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Clasificar Libro"
            ],
            "Lector": [
                "Filtrar Libros por Estado", "Notificaciones", "Cambiar Contraseña", "Buscar Libros",
                "Consultar Libro", "Descargar Libro"
            ]
        }

        # Obtener nombre de rol del usuario
        user_role = getattr(getattr(self.user, "rol", None), "nombre", "Lector")
        print("Usuario leido:",user)

        # Obtener nombre de rol del usuario (si existe)
        #user_role = self.user.rol.nombre if self.user and self.user.rol else "Lector"

        print("Rol identificado: ", user_role)

        # Obtener funciones disponibles según el rol
        self.available_features = role_permissions.get(user_role, [])

        # Asegurarse de que siempre se incluya el tablero
        if "Tablero" not in self.available_features:
            self.available_features.insert(0, "Tablero")

        # Agregar pantallas al stackedWidget solo si están permitidas
        for feature in self.available_features:
            screen = self.routes.get(feature)
            if isinstance(screen, int):
                continue
            self.ui.stackedWidget.addWidget(screen)

        # Poblar el panel lateral con botones correspondientes
        self._populate_sidebar()

    def _populate_sidebar(self):
        layout = self.ui.dynamicButtonLayout

        for feature in self.available_features:
            button = QPushButton(feature)
            button.setObjectName(f"btn_{feature.lower().replace(' ', '_')}")

            # Assign screen switch logic
            if isinstance(self.routes[feature], int):
                button.clicked.connect(lambda checked, idx=self.routes[feature]: self.ui.stackedWidget.setCurrentIndex(idx))
            else:
                button.clicked.connect(lambda checked, widget=self.routes[feature]: self.ui.stackedWidget.setCurrentWidget(widget))

            layout.addWidget(button)

    def center_on_screen(self):
        screen = self.screen().availableGeometry()
        size = self.geometry()
        self.move(
            screen.center().x() - size.width() // 2,
            screen.center().y() - size.height() // 2
        )
