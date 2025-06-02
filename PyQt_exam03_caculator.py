import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("calculator.ui")[0]

class ExampleApp(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_numbers = [self.btn_0, self.btn_1]
        btn_0.clicked.connect(self.btn_number_slot())

    def btn_number_slot(self):
        btn = self.sender()

        print(f"{btn_0.text()} 버튼이 클릭 됨")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ExampleApp()
    main_window.show()
    sys.exit(app.exec_())