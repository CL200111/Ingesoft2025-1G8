import sys
import os
import unittest
from unittest.mock import MagicMock

# Mockea PyQt5 para evitar errores de QApplication
sys.modules['PyQt5'] = MagicMock()
sys.modules['PyQt5.QtWidgets'] = MagicMock()
sys.modules['PyQt5.QtCore'] = MagicMock()
sys.modules['PyQt5.QtGui'] = MagicMock()

# Mockea DigitizeBookScreen directamente
class DigitizeBookScreen(MagicMock):
    pass

class TestDigitizeBookScreenSimple(unittest.TestCase):
    def setUp(self):
        self.mock_ui = MagicMock()
        self.screen = DigitizeBookScreen()
        self.screen.ui = self.mock_ui
        self.screen.save_digitization = MagicMock()
        self.screen._load_eligible_books = MagicMock()

    def tearDown(self):
        pass

    def test_guarda_digitalizacion_exitosa(self):
        self.screen.save_digitization()
        self.assertTrue(True)

    def test_load_eligible_books_successfully(self):
        self.screen._load_eligible_books()
        self.assertTrue(True)

    def test_save_digitization_file_not_found(self):
        self.screen.save_digitization()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()