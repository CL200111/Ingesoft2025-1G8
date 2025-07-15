from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QLabel, QVBoxLayout,
    QGridLayout, QPushButton, QMessageBox
)
from PyQt6.QtCore import Qt
from migracion import MigracionWindow



class DashboardWindow(QMainWindow):
    def __init__(self, usuario):
        super().__init__()
        self.usuario = usuario
        self.setWindowTitle("ArchiBox - Panel Principal")
        self.setGeometry(200, 150, 600, 400)
        self.initUI()

    def initUI(self):
        widget = QWidget()
        layout = QVBoxLayout()

        bienvenida = QLabel(f"👋 Bienvenido, {self.usuario.nombres} {self.usuario.apellidos}")
        bienvenida.setStyleSheet("font-size: 16px; font-weight: bold")
        bienvenida.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(bienvenida)
        layout.addSpacing(20)

        grid = QGridLayout()
        grid.setSpacing(15)

        botones = {
            "📚 Gestión de Libros": self.fake_action,
            "📈 Seguimiento de Proceso": self.open_migracion,
            "📝 Generar Reporte": self.fake_action,
            "🔒 Cerrar sesión": self.logout
        }

        for i, (texto, funcion) in enumerate(botones.items()):
            btn = QPushButton(texto)
            btn.clicked.connect(funcion)
            btn.setMinimumHeight(40)
            grid.addWidget(btn, i, 0)

        layout.addLayout(grid)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_migracion(self):
        self.migracion_window = MigracionWindow()
        self.migracion_window.show()


    def fake_action(self):
        QMessageBox.information(self, "Funcionalidad pendiente", "Esta funcionalidad aún no ha sido implementada.")

        
    def logout(self):
        self.close()