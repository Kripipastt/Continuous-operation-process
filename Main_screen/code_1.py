import sys
import os
import sqlite3
import random
import webbrowser
os.chdir("..")
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog
from interface_1 import Ui_MainWindow
from Screen_with_text_files.code_2 import SecondScreen


class WrongLoginOrPassword(Exception):
    pass


class WrongCaptcha(Exception):
    pass


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.start_x_secret = 511
        self.start_y_secret = 351
        self.secret = ""
        self.label_secter.hide()
        self.connection = sqlite3.connect(r"Database/db.sqlite")
        self.pushButton.clicked.connect(self.enter_the_npr)
        self.commandLinkButton.clicked.connect(self.show_time)

    def show_time(self):
        webbrowser.open("https://yandex.ru/time")

    def enter_the_npr(self):
        correct_captcha = self.captcha_generate()
        self.setStyleSheet('''QPushButton {background-color: rgb(189, 230, 255)}
QInputDialog {background-color: #ffe7ee;}''')
        captcha, ok_pressed = QInputDialog.getText(self, "Введите капчу",
                                                   f"{correct_captcha}")
        cur = self.connection.cursor()
        result = cur.execute(f'''SELECT * FROM logins_and_passwords
    WHERE login = "{self.lineEdit.text()}" AND password = "{self.lineEdit_2.text()}"''').fetchone()
        try:
            if ok_pressed:
                # print(result)
                if correct_captcha != captcha:
                    raise WrongCaptcha("Ошибка! Неверная капча!")
                elif not result:
                    raise WrongLoginOrPassword("Ошибка! Неверный логин или пароль!")
                else:
                    self.window_2 = SecondScreen((result[1].split()[0], result[1].split()[1], result[-1]))
                    self.window_2.show()
                    self.close()
        except (WrongLoginOrPassword, WrongCaptcha) as error:
            self.label_5.setText(f"{error}")

    def captcha_generate(self):
        return "".join([chr(random.randint(1040, 1103)) for _ in range(5)])

    def closeEvent(self, event):
        self.connection.close()

    def keyPressEvent(self, event):
        self.secret += str(event.key())
        if len(self.secret) > 30:
            self.secret = ""
        if "806583676576" in self.secret:
            self.label_secter.show()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
