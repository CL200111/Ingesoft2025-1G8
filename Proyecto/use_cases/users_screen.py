from PyQt5.QtWidgets import QWidget
from ui.screens.ui_users_screen import Ui_UsersScreen

class UsersScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_UsersScreen()
        self.ui.setupUi(self)

        self.ui.addUserButton.clicked.connect(self.add_user)

    def add_user(self):
        email = self.ui.emailInput.text()
        print(f"👤 Adding user with email: {email}")
