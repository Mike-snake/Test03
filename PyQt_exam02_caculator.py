import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("calculator.ui")[0]

class ExampleApp(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.first_input_flag = True
        self.first_number = 0
        self.opcode = ''
        self.btn_numbers = [self.btn_0, self.btn_1, self.btn_2, self.btn_3, self.btn_4,
                            self.btn_5, self.btn_6, self.btn_7, self.btn_8, self.btn_9]
        for btn in self.btn_numbers:
            btn.clicked.connect(self.btn_numbers_slot)
        self.btn_opcodes = [self.btn_add, self.btn_sub, self.btn_mul, self.btn_div, self.btn_eql]
        for btn in self.btn_opcodes:
            btn.clicked.connect(self.btn_opcodes_slot)

        # self.btn_eql.clicked.connect(self.calculate)
        self.btn_eql.clicked.connect(self.btn_opcodes_slot)
        self.btn_clear.clicked.connect(self.clear_slot)

    def clear_slot(self):
        self.first_input_flag = True
        self.first_number = 0
        self.opcode = ''
        self.lbl_result.setText('0')


    def calculate(self):
        if self.opcode == 'add':
            result = self.first_number + int(self.lbl_result.text())
            self.lbl_result.setText(str(result))
        elif self.opcode == 'sub':
            result = self.first_number - int(self.lbl_result.text())
            self.lbl_result.setText(str(result))
        elif self.opcode == 'mul':
            result = self.first_number * int(self.lbl_result.text())
            self.lbl_result.setText(str(result))
        elif self.opcode == 'div':
            if self.lbl_result.text() == '0':
                result = 'inf'
            else:
                result = self.first_number / int(self.lbl_result.text())
            self.lbl_result.setText(str(result))
        self.first_input_flag = True

    def btn_opcodes_slot(self):
        btn = self.sender()

        if self.first_input_flag:
            self.opcode = btn.objectName()[-3:]

            self.first_number = float(self.lbl_result.text())
        else:
            self.calculate()
            self.opcode = btn.objectName()[-3:]
            # self.first_number = int(self.lbl_result.text())
            self.first_number = float(self.lbl_result.text())
            self.first_input_flag = True

    def btn_numbers_slot(self):
        btn = self.sender()
        if self.lbl_result.text() == '0' or self.first_input_flag:
            self.first_input_flag = False
            self.lbl_result.setText("")
        # if self.first_input_flag:
        #     self.first_input_flag = False
        #     self.lbl_result.setText("")

        result = self.lbl_result.text()
        self.lbl_result.setText(result + btn.objectName()[-1])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ExampleApp()
    main_window.show()
    sys.exit(app.exec_())