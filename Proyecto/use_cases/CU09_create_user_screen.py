from PyQt5.QtWidgets import QWidget
from ui.screens.ui_CU09_create_user_screen import Ui_create_user_screen

class CreateUserScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_create_user_screen()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save_entry)

    def save_entry(self):
        value = self.ui.titleInput.text()
        print(f"✅ Saving create user screen: {value}")
