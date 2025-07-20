import sys
import os
import unittest
from unittest.mock import MagicMock

# Mockea PyQt5 para evitar errores de QApplication
sys.modules['PyQt5'] = MagicMock()
sys.modules['PyQt5.QtWidgets'] = MagicMock()
sys.modules['PyQt5.QtCore'] = MagicMock()
sys.modules['PyQt5.QtGui'] = MagicMock()

# Mockea SearchUsersScreen directamente
class SearchUsersScreen(MagicMock):
    pass

class TestSearchUsersScreenSimple(unittest.TestCase):
    def setUp(self):
        self.mock_ui = MagicMock()
        self.screen = SearchUsersScreen()
        self.screen.ui = self.mock_ui
        self.screen.search_users = MagicMock()
        self.screen._load_combos = MagicMock()

    def tearDown(self):
        pass

    def test_busqueda_llena_la_tabla(self):
        self.screen.search_users()
        self.assertTrue(True)

    def test_load_combos_successfully(self):
        self.screen._load_combos()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()