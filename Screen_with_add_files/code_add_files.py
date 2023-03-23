import sqlite3
import sys
import shutil

from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from Screen_with_add_files.interface_add_files import Ui_Form
from Screen_with_text_files import code_2


class ScreenAddFile(QWidget, Ui_Form):
    def __init__(self, account_info):
        super().__init__()
        self.setupUi(self)
        self.account_info = account_info
        self.set_info()
        self.connection = sqlite3.connect(r"Database/db.sqlite")
        self.pushButton.clicked.connect(self.select_to_screen_2)
        self.pushButton_2.clicked.connect(self.add_file)

    def set_info(self):
        self.access_level = self.account_info[2]
        self.label_name.setText(self.account_info[0])
        self.label_surname.setText(self.account_info[1])
        self.label_access_level.setText(f"{self.access_level}")

    def select_to_screen_2(self):
        self.window_2 = code_2.SecondScreen(self.account_info)
        self.window_2.show()
        self.close()

    def add_file(self):
        fname = QFileDialog.getOpenFileName(
            self, 'Выбрать картинку', '',
            'Файл (*.docx);;Файл (*.pdf)')[0]
        cursor = self.connection.cursor()
        try:
            if fname.split("/")[-1].split(".")[0] in [i[0]
                                                      for i in cursor.execute(
                    '''SELECT File_name FROM text_files''').fetchall()]:
                raise sqlite3.IntegrityError(
                    f'''Ошибка! Файл с именем "{fname.split("/")[-1].split(".")[0]}" уже есть!''')
            if fname:
                shutil.copy2(fname, fr'''Text_files/{fname.split("/")[-1]}''', follow_symlinks=True)
                cursor.execute(fr'''INSERT INTO text_files(id, File_name, Expansion, File_language, Access_level) VALUES
({max([i[0] for i in cursor.execute(fr'SELECT id FROM text_files').fetchall()] + [0]) + 1}, 
'{fname.split("/")[-1].split(".")[0]}', {cursor.execute(fr"""SELECT id FROM expansions WHERE expansion = 
'{fname.split("/")[-1].split(".")[1]}'""").fetchone()[0]}, 
'{self.comboBox.currentText().replace(")", "").split("(")[-1]}', 
{self.spinBox.text()})''')
                self.connection.commit()
                self.label_error.setStyleSheet("color: rgb(0, 255, 0);")
                self.label_error.setText(f"Файл успешно добавлен :3")
        except sqlite3.IntegrityError as error:
            self.label_error.setStyleSheet("color: rgb(255, 0, 0);")
            self.label_error.setText(f"{error}")

    def closeEvent(self, event):
        self.connection.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ScreenAddFile(("Тест_имя", "тест_фамилия", 5))
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
