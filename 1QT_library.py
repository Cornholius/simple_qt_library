import json
from PySide2 import QtCore, QtGui, QtWidgets
import sys
from QT_library_ui import Ui_Dialog
from QT_library_addbook import Ui_Addbook

app = QtWidgets.QApplication(sys.argv)
Dialog = QtWidgets.QDialog()
Add_book_window = QtWidgets.QDialog()
ui = Ui_Dialog()
ui.setupUi(Dialog)
addbook = Ui_Addbook()
addbook.setupUi(Add_book_window)
Dialog.show()


class Book:

    def __init__(self, name, author, description):
        self.name = name
        self.author = author
        self.description = description
        ui.enter_book_name.clear()
        ui.enter_author_name.clear()
        addbook.add_book_name.clear()
        addbook.add_author_name.clear()
        addbook.add_description_name.clear()

class Library:

    def __init__(self):
        file = open('books.json', 'r', encoding='utf-8')
        self.books = json.load(file)
        self.data = []
        self.data.extend(self.books)
        file.close()

    def add_books(self):
        book = Book(name=addbook.add_book_name.text(), author=addbook.add_author_name.text(), description=addbook.add_description_name.toPlainText())
        self.data.append({"name": book.name, "author": book.author, "description": book.description})
        with open('books.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.data, ensure_ascii=False))

    def delete_books(self):
        book = Book(name=ui.enter_book_name.text(), author=ui.enter_author_name.text(), description=None)
        for i in self.data:
            if i.get("name", "") == book.name and i.get("author", "") == book.author:
                self.data.remove(i)
                print("книга удалена")
        with open('books.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.data, ensure_ascii=False))
        print("!!!delete book")

    def find_books(self):
        book = Book(name=ui.enter_book_name.text(), author=ui.enter_author_name.text(), description=None)
        for i in self.data:
            if i.get("name", "") == book.name or i.get("author", "") == book.author:
                print("Название: ", i["name"],
                      "Автор: ", i["author"],
                      "Описание: ", i["description"])

    def test(self):
        book = Book(name=addbook.add_book_name.text(), author=addbook.add_author_name.text(), description=addbook.add_description_name.toPlainText())
        self.data.append({"name": book.name, "author": book.author, "description": book.description})
        with open('books.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(self.data, ensure_ascii=False))

lib = Library()
ui.bt_find_book.clicked.connect(lib.find_books)
ui.bt_add_book.clicked.connect(Add_book_window.show)
ui.bt_delete_book.clicked.connect(lib.delete_books)
addbook.Save.clicked.connect(lib.add_books)
addbook.Exit.clicked.connect(Add_book_window.close)
# while True:
#     a = input("\n"
#               "Выберите нужный пункт: \n"
#               "1 - добавить книгу \n"
#               "2 - удалить книгу\n"
#               "3 - найти книгу\n"
#               "0 - завершение программы\n"
#               "")
#
#     if a == "1":
#         print("Введите название книги, автора, и её описание")
#         book = Book(name=input("Название книги: "),
#                     author=input("Автор: "),
#                     description=input("Описание: "))
#         lib.add_books()
#         print("книга добавлена")
#
#     if a == "2":
#         print("Введите название книги и автора")
#         book = Book(name=input("Название книги: "),
#                     author=input("Автор: "),
#                     description=None)
#         lib.delete_books()
#         print("книга удалена")
#
#     if a == "3":
#         print("Введите название книги или автора")
#         book = Book(name=input("Название книги: "),
#                     author=input("Автор: "),
#                     description=None)
#         lib.find_books()
#
#     if a == "0":
#         exit()


sys.exit(app.exec_())
