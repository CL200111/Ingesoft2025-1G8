from PyQt5.QtWidgets import QMainWindow
from ui.ui_main_window import Ui_MainWindow
from use_cases.books_screen import BooksScreen
from use_cases.users_screen import UsersScreen

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create screens
        self.books_screen = BooksScreen()
        self.users_screen = UsersScreen()

        # Add to stackedWidget (indexes start at 0)
        self.ui.stackedWidget.addWidget(self.books_screen)   # index 1
        self.ui.stackedWidget.addWidget(self.users_screen)   # index 2

        # Connect side menu buttons to switch screens
        self.ui.btn_books.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.books_screen))
        self.ui.btn_users.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.users_screen))
        self.ui.btn_dashboard.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))  # page_dashboard
