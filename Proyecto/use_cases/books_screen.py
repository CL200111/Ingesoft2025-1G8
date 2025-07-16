from PyQt5.QtWidgets import QWidget
from ui.screens.ui_books_screen import Ui_BooksScreen

class BooksScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BooksScreen()
        self.ui.setupUi(self)

        self.ui.saveButton.clicked.connect(self.save_book)

    def save_book(self):
        title = self.ui.titleInput.text()
        print(f"📘 Saving book: {title}")
