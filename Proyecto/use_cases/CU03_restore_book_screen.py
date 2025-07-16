from PyQt5.QtWidgets import QWidget
from ui.screens.ui_CU03_restore_book_screen import Ui_restore_book_screen

class RestoreBookScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_restore_book_screen()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save_entry)

    def save_entry(self):
        value = self.ui.titleInput.text()
        print(f"✅ Saving restore book screen: {value}")
