import sys
import sqlite3
import os

from pygame import mixer
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog
from Screen_with_audio_files.interface_3 import Ui_Form
from Screen_with_text_files import code_2


class IdAudioFileError(Exception):
    pass


class AccessLevelError(Exception):
    pass


class ThirdScreen(QWidget, Ui_Form):
    def __init__(self, account_info):
        super().__init__()
        mixer.init()
        self.account_info = account_info
        self.setupUi(self)
        self.connection = sqlite3.connect(r"Database/db.sqlite")
        self.set_info()
        self.database_display()
        self.pushButton_2.clicked.connect(self.select_to_screen_2)
        self.pushButton.clicked.connect(self.listen)
        self.pushButton_3.clicked.connect(self.delete_db)
        self.pushButton_4.clicked.connect(self.stop_audio_file)

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
        model.setTable('Audio_files')
        model.select()
        self.tableView.setModel(model)

    def select_to_screen_2(self):
        self.window_2 = code_2.SecondScreen(self.account_info)
        self.window_2.show()
        self.close()

    def listen(self):
        cursor = self.connection.cursor()
        result = cursor.execute(f'''SELECT * FROM Audio_files
        WHERE id = {self.spinBox.text()}''').fetchone()
        try:
            if result is None:
                raise IdAudioFileError(f"Ошибка! Не найден ID файла: {self.spinBox.text()}")
            elif self.access_level < result[2]:
                raise AccessLevelError("Вам НЕ СЛЕДУЕТ слушать данный файл")
            else:
                mixer.music.load(fr'Audio_files/{result[1]}')
                mixer.music.play()
                self.label_error.setText("")
        except (IdAudioFileError, AccessLevelError) as error:
            self.label_error.setText(f"{error}")

    def closeEvent(self, event):
        self.connection.close()
        self.stop_audio_file()

    def delete_db(self):
        self.stop_audio_file()
        confirmation, ok_pressed = QInputDialog.getText(self, "Вы уверены?", 'Введите "ДА", чтобы подтвердить')
        if confirmation == "ДА" and ok_pressed:
            cursor = self.connection.cursor()
            cursor.execute('''DELETE FROM Audio_files''')
            self.connection.commit()
            self.database_display()
            for i in os.listdir(r'Audio_files'):
                os.remove(fr'Audio_files/{i}')
            self.label_error.setText("Все аудиофайлы удалены :(")

    def stop_audio_file(self):
        mixer.music.unload()
        mixer.music.stop()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ThirdScreen(("Тест_имя", "тест_фамилия", 3))
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
