import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from PyQt5.QtWidgets import QApplication
from main_window import MainWindow  # Adjust import path if needed


# Minimal mock classes for the role and user
class MockRol:
    def __init__(self, nombre):
        self.nombre = nombre


class MockUser:
    def __init__(self, rol_nombre):
        self.rol = MockRol(rol_nombre)


class TestMainWindowPermissions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])  # Needed for QWidget tests

        # Must match role_permissions from MainWindow
        cls.expected_permissions = {
            "Administrador": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Crear Usuario",
                "Editar Usuario",
                "Desactivar Usuario",
                "Buscar Usuarios",
                "Modificar Libro",
                "Generar Reporte",
                "Restaurar Contraseña",
                "Consultar Historial de Libro",
                "Asignar Tarea",
                "Crear Categoría",
                "Desactivar Libro",
            ],
            "Revisor": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Registrar Libro",
                "Registrar Condición",
            ],
            "Restaurador": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Restaurar Libro",
            ],
            "Digitalizador": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Digitalizar Libro",
            ],
            "Supervisor de calidad": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Calidad Digital",
                "Calidad Física",
            ],
            "Clasificador": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Clasificar Libro",
            ],
            "Lector": [
                "Notificaciones",
                "Cambiar Contraseña",
                "Buscar Libros",
                "Consultar Libro",
                "Descargar Libro",
            ],
        }

    def test_permissions_by_role(self):
        for role, expected_features in self.expected_permissions.items():
            with self.subTest(role=role):
                user = MockUser(role)
                window = MainWindow(user=user)
                self.assertCountEqual(
                    window.available_features,
                    expected_features,
                    f"Permissions mismatch for role: {role}",
                )

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()
