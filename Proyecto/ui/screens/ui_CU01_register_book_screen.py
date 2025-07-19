# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_CU01_register_book_screen.ui'
#
# Created by: PyQt5 UI code generator
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is run again.

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_register_book_screen(object):
    def setupUi(self, register_book_screen):
        register_book_screen.setObjectName("register_book_screen")
        register_book_screen.resize(400, 450)
        self.verticalLayout = QtWidgets.QVBoxLayout(register_book_screen)
        self.verticalLayout.setObjectName("verticalLayout")

        self.labelTitulo = QtWidgets.QLabel(register_book_screen)
        self.labelTitulo.setText("Título:")
        self.verticalLayout.addWidget(self.labelTitulo)
        self.tituloInput = QtWidgets.QLineEdit(register_book_screen)
        self.tituloInput.setPlaceholderText("Título")
        self.tituloInput.setObjectName("tituloInput")
        self.verticalLayout.addWidget(self.tituloInput)

        self.labelAutor = QtWidgets.QLabel(register_book_screen)
        self.labelAutor.setText("Autor:")
        self.verticalLayout.addWidget(self.labelAutor)
        self.autorInput = QtWidgets.QLineEdit(register_book_screen)
        self.autorInput.setPlaceholderText("Autor")
        self.autorInput.setObjectName("autorInput")
        self.verticalLayout.addWidget(self.autorInput)

        self.labelFecha = QtWidgets.QLabel(register_book_screen)
        self.labelFecha.setText("Fecha:")
        self.verticalLayout.addWidget(self.labelFecha)
        self.fechaInput = QtWidgets.QDateEdit(register_book_screen)
        self.fechaInput.setCalendarPopup(True)
        self.fechaInput.setObjectName("fechaInput")
        self.verticalLayout.addWidget(self.fechaInput)

        self.labelPaginas = QtWidgets.QLabel(register_book_screen)
        self.labelPaginas.setText("Número de páginas:")
        self.verticalLayout.addWidget(self.labelPaginas)
        self.paginasInput = QtWidgets.QLineEdit(register_book_screen)
        self.paginasInput.setPlaceholderText("Número de páginas")
        self.paginasInput.setObjectName("paginasInput")
        self.verticalLayout.addWidget(self.paginasInput)

        self.labelEstanteria = QtWidgets.QLabel(register_book_screen)
        self.labelEstanteria.setText("Estantería:")
        self.verticalLayout.addWidget(self.labelEstanteria)
        self.estanteriaInput = QtWidgets.QLineEdit(register_book_screen)
        self.estanteriaInput.setPlaceholderText("Estantería")
        self.estanteriaInput.setObjectName("estanteriaInput")
        self.verticalLayout.addWidget(self.estanteriaInput)

        self.labelEspacio = QtWidgets.QLabel(register_book_screen)
        self.labelEspacio.setText("Espacio:")
        self.verticalLayout.addWidget(self.labelEspacio)
        self.espacioInput = QtWidgets.QLineEdit(register_book_screen)
        self.espacioInput.setPlaceholderText("Espacio")
        self.espacioInput.setObjectName("espacioInput")
        self.verticalLayout.addWidget(self.espacioInput)

        self.errorLabel = QtWidgets.QLabel(register_book_screen)
        self.errorLabel.setText("")
        self.errorLabel.setObjectName("errorLabel")
        self.verticalLayout.addWidget(self.errorLabel)

        self.saveButton = QtWidgets.QPushButton(register_book_screen)
        self.saveButton.setText("Registrar Libro")
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)

        self.retranslateUi(register_book_screen)
        QtCore.QMetaObject.connectSlotsByName(register_book_screen)

    def retranslateUi(self, register_book_screen):
        _translate = QtCore.QCoreApplication.translate
        register_book_screen.setWindowTitle(_translate("register_book_screen", "Registrar Libro"))
