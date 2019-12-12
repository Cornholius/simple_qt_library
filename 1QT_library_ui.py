# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'g:\FacepalmProject\library\untitled.ui',
# licensing of 'g:\FacepalmProject\library\untitled.ui' applies.
#
# Created: Fri Oct 11 00:30:40 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(824, 627)
        Dialog.setMinimumSize(QtCore.QSize(800, 600))
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 22, 302, 223))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.search_book_label = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_book_label.sizePolicy().hasHeightForWidth())
        self.search_book_label.setSizePolicy(sizePolicy)
        self.search_book_label.setObjectName("search_book_label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.search_book_label)
        self.book_name = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.book_name.setFont(font)
        self.book_name.setObjectName("book_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.book_name)
        self.enter_book_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.enter_book_name.setObjectName("enter_book_name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.enter_book_name)
        self.author_name = QtWidgets.QLabel(self.layoutWidget)
        self.author_name.setObjectName("author_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.author_name)
        self.enter_author_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.enter_author_name.setObjectName("enter_author_name")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.enter_author_name)
        self.bt_find_book = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_find_book.sizePolicy().hasHeightForWidth())
        self.bt_find_book.setSizePolicy(sizePolicy)
        self.bt_find_book.setMinimumSize(QtCore.QSize(300, 40))
        self.bt_find_book.setObjectName("bt_find_book")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.bt_find_book)
        self.bt_add_book = QtWidgets.QPushButton(self.layoutWidget)
        self.bt_add_book.setMinimumSize(QtCore.QSize(300, 40))
        self.bt_add_book.setObjectName("bt_add_book")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.SpanningRole, self.bt_add_book)
        self.bt_delete_book = QtWidgets.QPushButton(self.layoutWidget)
        self.bt_delete_book.setMinimumSize(QtCore.QSize(300, 40))
        self.bt_delete_book.setObjectName("bt_delete_book")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.bt_delete_book)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtWidgets.QApplication.translate("Dialog", "Dialog", None, -1))
        self.search_book_label.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p><span style=\" font-size:16pt;\">Поиск книги</span></p></body></html>", None, -1))
        self.book_name.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p align=\"right\">Название</p></body></html>", None, -1))
        self.author_name.setText(QtWidgets.QApplication.translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:14pt;\">Автор</span></p></body></html>", None, -1))
        self.bt_find_book.setText(QtWidgets.QApplication.translate("Dialog", "Найти", None, -1))
        self.bt_add_book.setText(QtWidgets.QApplication.translate("Dialog", "Добавить книгу", None, -1))
        self.bt_delete_book.setText(QtWidgets.QApplication.translate("Dialog", "Удалить книгу", None, -1))
