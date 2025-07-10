from PyQt6.QtWidgets import (
    QWidget, QLineEdit, QLabel, QPushButton,
    QVBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from pathlib import Path
import bcrypt

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from dashboard import DashboardWindow

# Ruta hacia la base de datos (sube un nivel, entra a db/)
db_path = Path(__file__).resolve().parent.parent /"db"/ "books.db"
engine = create_engine(f"sqlite:///{db_path}", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# Importar modelos
from db.db_init import Usuario

# Clase para la ventana de inicio de sesión
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArchiBox - Iniciar sesión")
        self.setGeometry(100, 100, 300, 150)

        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Correo electrónico")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setPlaceholderText("Contraseña")

        self.login_button = QPushButton("Iniciar sesión")
        self.login_button.clicked.connect(self.login)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Correo electrónico:"))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel("Contraseña:"))
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        self.setLayout(layout)

    def login(self):
        correo = self.email_input.text().strip()
        contraseña = self.password_input.text().strip()

        usuario = session.query(Usuario).filter_by(correo_electronico=correo, estado=True).first()
        if usuario and bcrypt.checkpw(contraseña.encode('utf-8'), usuario.hash_contraseña.encode('utf-8')):
            self.accept_login(usuario)
        else:
            QMessageBox.warning(self, "Error", "Credenciales incorrectas o usuario inactivo.")

    def accept_login(self, usuario):
        self.main_window = DashboardWindow(usuario)
        self.main_window.show()
        self.close()