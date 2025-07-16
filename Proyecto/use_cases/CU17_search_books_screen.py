from PyQt5.QtWidgets import QWidget
from ui.screens.ui_CU17_search_books_screen import Ui_search_books_screen

class SearchBooksScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_search_books_screen()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save_entry)

    def save_entry(self):
        value = self.ui.titleInput.text()
        print(f"✅ Saving search books screen: {value}")
