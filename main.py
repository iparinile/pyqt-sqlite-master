import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel, QSqlTableModel
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QStandardItemModel, QStandardItem

import design  # Это наш конвертированный файл дизайна


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('data.db')
        db.open()

        self.model = QSqlTableModel(self)
        self.model.setTable('Товары')
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.tableView.setModel(self.model)
        self.model.select()
        self.tableView.setSortingEnabled(True)
        self.pushButton.clicked.connect(self.delRow)

    def addRow(self):
        self.model.insertRow(self.model.rowCount())

    def delRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.select()
    #     self.model = QStandardItemModel()
    #     self.tableView = QTableView()
    #     self.tableView.setModel(self.model)
    #     self.pushButton.clicked.connect(self.load_data)
    #
    # def load_data(self):
    #     l = [[i + j for i in range(3)] for j in range(4)]
    #     self.model.setRowCount(4)
    #     self.model.setColumnCount(3)
    #     for i in range(4):
    #         for j in range(3):
    #             item = QStandardItem(str(l[i][j]))
    #             self.model.setItem(i, j, item)


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
