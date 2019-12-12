# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\FacepalmProject\Library\Addbook.ui',
# licensing of 'd:\FacepalmProject\Library\Addbook.ui' applies.
#
# Created: Fri Oct 11 12:35:46 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Addbook(object):
    def setupUi(self, Addbook):
        Addbook.setObjectName("Addbook")
        Addbook.resize(500, 500)
        Addbook.setMinimumSize(QtCore.QSize(500, 500))
        Addbook.setMaximumSize(QtCore.QSize(500, 500))
        self.gridLayout = QtWidgets.QGridLayout(Addbook)
        self.gridLayout.setObjectName("gridLayout")
        self.Exit = QtWidgets.QPushButton(Addbook)
        self.Exit.setObjectName("Exit")
        self.gridLayout.addWidget(self.Exit, 3, 2, 1, 1)
        self.Save = QtWidgets.QPushButton(Addbook)
        self.Save.setObjectName("Save")
        self.gridLayout.addWidget(self.Save, 3, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.add_description_name = QtWidgets.QTextEdit(Addbook)
        self.add_description_name.setObjectName("add_description_name")
        self.gridLayout.addWidget(self.add_description_name, 2, 0, 1, 3)
        self.add_author_name = QtWidgets.QLineEdit(Addbook)
        self.add_author_name.setObjectName("add_author_name")
        self.gridLayout.addWidget(self.add_author_name, 1, 0, 1, 3)
        self.add_book_name = QtWidgets.QLineEdit(Addbook)
        self.add_book_name.setObjectName("add_book_name")
        self.gridLayout.addWidget(self.add_book_name, 0, 0, 1, 3)

        self.retranslateUi(Addbook)
        QtCore.QMetaObject.connectSlotsByName(Addbook)

    def retranslateUi(self, Addbook):
        Addbook.setWindowTitle(QtWidgets.QApplication.translate("Addbook", "Добавить книгу", None, -1))
        self.Exit.setText(QtWidgets.QApplication.translate("Addbook", "Выход", None, -1))
        self.Save.setText(QtWidgets.QApplication.translate("Addbook", "Сохранить", None, -1))
        self.add_description_name.setPlaceholderText(QtWidgets.QApplication.translate("Addbook", "Описание книги", None, -1))
        self.add_author_name.setPlaceholderText(QtWidgets.QApplication.translate("Addbook", "Автор книги", None, -1))
        self.add_book_name.setPlaceholderText(QtWidgets.QApplication.translate("Addbook", "Название книги", None, -1))

