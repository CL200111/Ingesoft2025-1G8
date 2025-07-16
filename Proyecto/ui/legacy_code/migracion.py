from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QTabWidget, QTableWidget, QTableWidgetItem, QPushButton,
    QLabel, QLineEdit, QSplitter, QGroupBox, QTextEdit,
    QListWidget, QListWidgetItem, QHeaderView, QStatusBar,
    QGraphicsView, QGraphicsScene
)
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QColor, QBrush, QPen, QPainterPath
import sys

class MigracionWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ArchiBox - Migración de Libros")
        self.setGeometry(100, 100, 1200, 800)
        self.init_ui()

    def init_ui(self):
        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Listo para la migración de libros.")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)

        # Panel lateral izquierdo
        left_panel = QWidget()
        left_panel_layout = QVBoxLayout(left_panel)
        left_panel.setFixedWidth(250)
        left_panel.setStyleSheet("border-right: 1px solid #d0d0d0;")

        self.nav_list = QListWidget()
        self.nav_list.addItem(QListWidgetItem("Vista General"))
        self.nav_list.addItem(QListWidgetItem("Libros Pendientes"))
        self.nav_list.addItem(QListWidgetItem("Libros Migrados"))
        self.nav_list.addItem(QListWidgetItem("Con Conflictos"))
        self.nav_list.currentRowChanged.connect(self.change_tab)
        left_panel_layout.addWidget(self.nav_list)

        filter_group = QGroupBox("Filtros")
        filter_layout = QVBoxLayout(filter_group)
        filter_layout.addWidget(QLabel("Búsqueda:"))
        filter_layout.addWidget(QLineEdit())
        left_panel_layout.addWidget(filter_group)
        left_panel_layout.addStretch()

        main_layout.addWidget(left_panel)

        # Área central
        self.central_splitter = QSplitter(Qt.Orientation.Vertical)
        main_layout.addWidget(self.central_splitter)

        self.tab_widget = QTabWidget()
        self.central_splitter.addWidget(self.tab_widget)

        # Pestaña: Vista General
        overview_page = QWidget()
        overview_layout = QVBoxLayout(overview_page)
        overview_layout.addWidget(QLabel("<h1>Vista General de la Migración</h1>"))
        self.graphics_view = QGraphicsView()
        scene = QGraphicsScene()
        self.draw_progress_chart(scene, 70, 20, 10)
        self.graphics_view.setScene(scene)
        self.graphics_view.setFixedSize(400, 200)
        overview_layout.addWidget(self.graphics_view, alignment=Qt.AlignmentFlag.AlignCenter)
        self.tab_widget.addTab(overview_page, "Vista General")

        # Pestaña: Detalle Libros
        self.books_table = QTableWidget()
        self.books_table.setColumnCount(8)
        self.books_table.setHorizontalHeaderLabels([
            "ID Antiguo", "Título", "Autor", "ISBN",
            "Estado", "ID Nuevo", "Última Acción", "Notas"
        ])
        self.books_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.books_table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        self.books_table.itemSelectionChanged.connect(self.display_book_details)
        self.tab_widget.addTab(self.books_table, "Detalle de Libros")

        # Panel de detalles inferior
        self.detail_panel = QWidget()
        detail_layout = QVBoxLayout(self.detail_panel)
        detail_group = QGroupBox("Detalles del Libro Seleccionado")
        group_layout = QHBoxLayout(detail_group)

        self.old_title_edit = QLineEdit(); self.old_title_edit.setReadOnly(True)
        self.old_author_edit = QLineEdit(); self.old_author_edit.setReadOnly(True)
        self.old_isbn_edit = QLineEdit(); self.old_isbn_edit.setReadOnly(True)

        old_layout = QVBoxLayout()
        old_layout.addWidget(QLabel("Título:")); old_layout.addWidget(self.old_title_edit)
        old_layout.addWidget(QLabel("Autor:")); old_layout.addWidget(self.old_author_edit)
        old_layout.addWidget(QLabel("ISBN:")); old_layout.addWidget(self.old_isbn_edit)

        self.new_title_edit = QLineEdit()
        self.new_author_edit = QLineEdit()
        self.new_isbn_edit = QLineEdit()

        new_layout = QVBoxLayout()
        new_layout.addWidget(QLabel("Título:")); new_layout.addWidget(self.new_title_edit)
        new_layout.addWidget(QLabel("Autor:")); new_layout.addWidget(self.new_author_edit)
        new_layout.addWidget(QLabel("ISBN:")); new_layout.addWidget(self.new_isbn_edit)

        self.book_notes_edit = QTextEdit()

        action_layout = QVBoxLayout()
        action_layout.addWidget(QLabel("Notas:"))
        action_layout.addWidget(self.book_notes_edit)
        action_layout.addStretch()

        group_layout.addLayout(old_layout)
        group_layout.addLayout(new_layout)
        group_layout.addLayout(action_layout)
        detail_layout.addWidget(detail_group)
        self.central_splitter.addWidget(self.detail_panel)

        self.populate_sample_data()

    def draw_progress_chart(self, scene, mig, pen, err):
        total = 360 * 16
        mig_angle = int(mig / 100 * total)
        pen_angle = int(pen / 100 * total)
        err_angle = int(err / 100 * total)
        rect = QRectF(0, 0, 150, 150)

        path = QPainterPath(); path.moveTo(rect.center())
        path.arcTo(rect, 0, -mig_angle / 16); path.closeSubpath()
        scene.addPath(path, QPen(Qt.GlobalColor.transparent), QBrush(QColor("#4CAF50")))

        path = QPainterPath(); path.moveTo(rect.center())
        path.arcTo(rect, -mig_angle / 16, -pen_angle / 16); path.closeSubpath()
        scene.addPath(path, QPen(Qt.GlobalColor.transparent), QBrush(QColor("#2196F3")))

        path = QPainterPath(); path.moveTo(rect.center())
        path.arcTo(rect, -(mig_angle + pen_angle) / 16, -err_angle / 16); path.closeSubpath()
        scene.addPath(path, QPen(Qt.GlobalColor.transparent), QBrush(QColor("#F44336")))

        scene.addText(f"Migrados: {mig}%").setPos(160, 0)
        scene.addText(f"Pendientes: {pen}%").setPos(160, 20)
        scene.addText(f"Errores: {err}%").setPos(160, 40)

    def populate_sample_data(self):
        data = [
            ["OLD001", "Cien Años de Soledad", "Gabo", "978-123", "Migrado", "NEW001", "2024-01-01", ""],
            ["OLD002", "Rayuela", "Cortázar", "978-456", "Pendiente", "", "", "Falta info"],
            ["OLD003", "1984", "Orwell", "978-789", "Error", "", "2024-02-20", "Conflicto"]
        ]
        self.books_table.setRowCount(len(data))
        for r, row in enumerate(data):
            for c, val in enumerate(row):
                self.books_table.setItem(r, c, QTableWidgetItem(str(val)))

    def display_book_details(self):
        items = self.books_table.selectedItems()
        if not items:
            self.statusBar().showMessage("Ningún libro seleccionado")
            return
        row = items[0].row()
        self.old_title_edit.setText(self.books_table.item(row, 1).text())
        self.old_author_edit.setText(self.books_table.item(row, 2).text())
        self.old_isbn_edit.setText(self.books_table.item(row, 3).text())
        self.new_title_edit.setText(self.books_table.item(row, 1).text())
        self.new_author_edit.setText(self.books_table.item(row, 2).text())
        self.new_isbn_edit.setText(self.books_table.item(row, 3).text())
        self.book_notes_edit.setText(self.books_table.item(row, 7).text())
        self.statusBar().showMessage(f"Libro seleccionado: {self.books_table.item(row, 1).text()}")

    def change_tab(self, index):
        self.tab_widget.setCurrentIndex(index)