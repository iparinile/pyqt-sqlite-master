import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel

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
        self.model.setTable(db.tables()[0])
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.tableView.setModel(self.model)
        self.model.select()
        self.tableView.setSortingEnabled(True)
        self.add_row.clicked.connect(self.addRow)
        self.del_row.clicked.connect(self.delRow)

        self.select_table.addItems(db.tables())
        self.select_table.currentTextChanged.connect(self.update_current_table)

    def update_current_table(self):
        print(self.select_table.currentText())
        self.model.setTable(self.select_table.currentText())
        self.model.select()

    def addRow(self):
        self.model.insertRow(self.model.rowCount())

    def delRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.select()


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
