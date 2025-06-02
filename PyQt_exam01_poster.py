
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

#from keras.models import load_model

form_class = uic.loadUiType("./Poster.ui")[0]

class ExampleApp(QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # self.setupUi(self)
        # self.btn_con.clicked.connect(self.lbl_con.show)
        # self.btn_con.clicked.connect(self.lbl_order.hide)
        # self.btn_con.clicked.connect(self.lbl_return.hide)
        # self.btn_con.clicked.connect(self.lbl_y2k.hide)
        #
        # self.btn_order.clicked.connect(self.lbl_con.hide)
        # self.btn_order.clicked.connect(self.lbl_order.show)
        # self.btn_order.clicked.connect(self.lbl_return.hide)
        # self.btn_order.clicked.connect(self.lbl_y2k.hide)
        #
        # self.btn_return.clicked.connect(self.lbl_con.hide)
        # self.btn_return.clicked.connect(self.lbl_order.hide)
        # self.btn_return.clicked.connect(self.lbl_return.show)
        # self.btn_return.clicked.connect(self.lbl_y2k.hide)
        #
        # self.btn_y2k.clicked.connect(self.lbl_con.hide)
        # self.btn_y2k.clicked.connect(self.lbl_order.hide)
        # self.btnbtn_y2k.clicked.connect(self.lbl_return.hide)
        # self.btn_y2k.clicked.connect(self.lbl_y2k.show)


        self.label_list = [self.lbl_con, self.lbl_order, self.lbl_return, self.lbl_y2k]

        self.btn_con.clicked.connect(self.btn_slot)
        self.btn_order.clicked.connect(self.btn_slot)
        self.btn_return.clicked.connect(self.btn_slot)
        self.btn_y2k.clicked.connect(self.btn_slot)

    def btn_slot(self):
        btn = self.sender()
        # self.lbl_con.hide()
        # self.lbl_order.hide()
        # self.lbl_return.hide()
        # self.lbl_y2k.hide()
        for label in self.label_list:
            label.hide()

        if btn.objectName()[-3:] == 'con': self.lbl_con.show()
        elif btn.objectName()[-3:] == 'der': self.lbl_order.show()
        elif btn.objectName()[-3:] == 'urn': self.lbl_return.show()
        elif btn.objectName()[-3:] == 'y2k':
            self.lbl_y2k.show()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = ExampleApp()
    main_window.show()
    sys.exit(app.exec_())






















