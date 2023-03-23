import sys

from Other_function.collection_in_one_line import collection
from PyQt5.QtWidgets import QApplication, QWidget
from Screen_read_file.interface import Ui_Form


class ReadScreen(QWidget, Ui_Form):
    def __init__(self, file_from_bd):
        super().__init__()
        self.setupUi(self)
        self.file_from_bd = list(file_from_bd)
        self.setWindowTitle(f"{self.file_from_bd[1]}.{self.file_from_bd[2]}")
        self.label_2.setText(f"{self.file_from_bd[1]}.{self.file_from_bd[2]}")
        self.textEdit.setText(collection(fr"text_files\{self.label_2.text()}", f"{self.file_from_bd[2]}"))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = ReadScreen((3, 'Города и годы', 'pdf', 'ru', 3))
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
