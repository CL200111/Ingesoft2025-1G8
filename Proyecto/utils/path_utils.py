import os
from pathlib import Path

def get_project_root() -> Path:
    """
    Devuelve la ruta absoluta a la carpeta raíz del proyecto ('Proyecto').
    """
    return Path(__file__).resolve().parent.parent

def get_asset_path(filename):
    """
    Devuelve la ruta absoluta a un archivo dentro de la carpeta 'assets'.
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_dir, "..", "assets", filename)

def get_books_path(filename):
    """
    Devuelve la ruta absoluta a un archivo dentro de la carpeta 'books'.
    """
    project_root = get_project_root()
    return os.path.join(project_root, "books", filename)
