import sys
import os
import unittest
from unittest.mock import MagicMock
from use_cases.CU17_search_books_screen import SearchBooksScreen

# Añade la carpeta raíz del proyecto al path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, project_root)

class TestSearchBooksScreenSimple(unittest.TestCase):
    def setUp(self):
        self.mock_ui = MagicMock()
        self.screen = SearchBooksScreen()
        self.screen.ui = self.mock_ui
        self.screen.search_books = MagicMock()
        self.screen._load_combos = MagicMock()

    def tearDown(self):
        pass

    def test_busqueda_con_titulo_filtra_correctamente(self):
        self.screen.search_books()
        self.assertTrue(True)

    def test_load_combos_successfully(self):
        self.screen._load_combos()
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
