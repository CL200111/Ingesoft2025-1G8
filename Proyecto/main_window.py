from PyQt5.QtWidgets import QMainWindow, QPushButton
from ui.ui_main_window import Ui_MainWindow

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

        self.user = user  # Could be passed from login window

        # Create instances of each screen
        self.routes = {
            "Dashboard": 0,
            "Register Book": RegisterBookScreen(),
            "Register Condition": RegisterConditionScreen(),
            "Restore Book": RestoreBookScreen(),
            "Digitize Book": DigitizeBookScreen(),
            "Classify Book": ClassifyBookScreen(),
            "Query Book History": QueryBookHistoryScreen(),
            "Generate Report": GenerateReportScreen(),
            "Create User": CreateUserScreen(),
            "Edit User": EditUserScreen(),
            "Deactivate User": DeactivateUserScreen(),
            "Modify Book": ModifyBookScreen(),
            "Deactivate Book": DeactivateBookScreen(),
            "Notifications": NotificationScreen(),
            "Physical QA": PhysicalQaScreen(),
            "Filter Books by State": FilterBooksByStateScreen(),
            "Search Books": SearchBooksScreen(),
            "Search Users": SearchUsersScreen(),
            "Assign Task": AssignTaskScreen(),
            "Change Password": ChangePasswordScreen(),
            "Restore Password": RestorePasswordScreen(),
            "Query Book": QueryBookScreen(),
            "Download Book": DownloadBookScreen(),
            "Digital QA": DigitalQaScreen(),
            "Create Category": CreateCategoryScreen(),
        }

        # Add screens to stacked widget
        for screen in self.routes.values():
            if isinstance(screen, int):
                continue
            self.ui.stackedWidget.addWidget(screen)

        # Available buttons (simulate full access for now)
        self.available_features = list(self.routes.keys())

        # Populate sidebar dynamically
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
