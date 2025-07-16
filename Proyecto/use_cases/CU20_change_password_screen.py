from PyQt5.QtWidgets import QWidget
from ui.screens.ui_CU20_change_password_screen import Ui_change_password_screen

class ChangePasswordScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_change_password_screen()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save_entry)

    def save_entry(self):
        value = self.ui.titleInput.text()
        print(f"✅ Saving change password screen: {value}")
