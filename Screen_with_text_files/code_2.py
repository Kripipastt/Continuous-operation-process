import sys
import os

import sqlite3
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QWidget
from Screen_with_text_files.interface_2 import Ui_Form
from Screen_read_file.code_read import ReadScreen
from Screen_with_audio_files import code_3
from Other_function.synthesizer import transform_string_to_audio
from Other_function.collection_in_one_line import collection
from Other_function.recoder import coder
from Screen_with_add_files import code_add_files


class IdFileError(Exception):
    pass


class AccessLevelError(Exception):
    pass


class SecondScreen(QWidget, Ui_Form):
    def __init__(self, account_info):
        super().__init__()
        self.setupUi(self)
        self.account_info = account_info
        self.set_info()
        self.database_display()
        self.connection = sqlite3.connect(r"Database/db.sqlite")
        self.pushButton.clicked.connect(self.open_file_to_read)
        self.pushButton_2.clicked.connect(self.convert)
        self.pushButton_3.clicked.connect(self.select_to_screen_3)
        self.pushButton_4.clicked.connect(self.select_screen_with_add_files)

    def set_info(self):
        self.access_level = self.account_info[2]
        self.label_name.setText(self.account_info[0])
        self.label_surname.setText(self.account_info[1])
        self.label_access_level.setText(f"{self.access_level}")

    def database_display(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(r"Database/db.sqlite")
        db.open()
        model = QSqlTableModel(self, db)
        model.setTable('Text_files')
        model.select()
        self.tableView.setModel(model)

    def open_file_to_read(self):
        result = self.get_file()
        if result:
            self.window_read = ReadScreen(result)
            self.window_read.show()
            self.label_error.setText("")

    def convert(self):
        result = self.get_file()
        if result:
            try:
                if f"{coder(result[1])}.mp3" in os.listdir(fr'Audio_files'):
                    raise sqlite3.IntegrityError(f"Ошибка! Файл с ID {result[0]} уже преобразован!")
                transform_string_to_audio(collection(fr"Text_files/{result[1]}.{result[2]}", result[2]), result[3],
                                          f"{coder(result[1])}.mp3")
                cursor_2 = self.connection.cursor()
                cursor_2.execute(f'''INSERT INTO Audio_files (id, File_name, Access_level)
                VALUES ({max(list(map(lambda x: x[0], cursor_2.execute("SELECT id FROM Audio_files").fetchall())) + [0]) + 1}, 
                "{coder(result[1])}.mp3", {result[4]})''')
                self.connection.commit()
                self.label_convert.setText(F"Файл с ID {result[0]} успешно преобразован :3")
            except sqlite3.IntegrityError as error:
                self.label_convert.setText("")
                self.label_error.setText(f"{error}")

    def get_file(self):
        cursor = self.connection.cursor()
        result = cursor.execute(f'''SELECT * FROM Text_files
        WHERE id = {self.spinBox.text()}''').fetchone()
        try:
            if result is None:
                raise IdFileError(f"Ошибка! Нет файла с ID: {self.spinBox.text()}")
            elif self.access_level < result[4]:
                raise AccessLevelError("Вам НЕ СЛЕДУЕТ читать/конвертировать данный файл")
            result = list(result)
            result[2] = cursor.execute(f'''SELECT expansion FROM expansions
WHERE id = "{result[2]}"''').fetchone()[0]
            self.label_error.setText("")
            return result
        except (IdFileError, AccessLevelError) as error:
            self.label_error.setText(f"{error}")
            self.label_convert.setText("")
            return ""

    def select_to_screen_3(self):
        self.window_3 = code_3.ThirdScreen(self.account_info)
        self.window_3.show()
        self.close()

    def select_screen_with_add_files(self):
        try:
            if self.access_level < 5:
                raise AccessLevelError("Файлы можно добавлять только пользователям с 5 уровнем доступа")
            self.window_add_files = code_add_files.ScreenAddFile(self.account_info)
            self.window_add_files.show()
            self.close()
        except AccessLevelError as error:
            self.label_error.setText(f"{error}")
            self.label_convert.setText("")

    def closeEvent(self, event):
        self.connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = SecondScreen(("Тест_имя", "тест_фамилия", 5))
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
