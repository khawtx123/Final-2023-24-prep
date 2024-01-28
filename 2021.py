from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(202, 305)
        self.pbNo0 = QtWidgets.QPushButton(Dialog)
        self.pbNo0.setGeometry(QtCore.QRect(65, 235, 70, 70))
        self.pbNo0.setObjectName("pbNo0")
        self.pbNo1 = QtWidgets.QPushButton(Dialog)
        self.pbNo1.setGeometry(QtCore.QRect(0, 40, 70, 70))
        self.pbNo1.setObjectName("pbNo1")
        self.pbNo2 = QtWidgets.QPushButton(Dialog)
        self.pbNo2.setGeometry(QtCore.QRect(65, 40, 70, 70))
        self.pbNo2.setObjectName("pbNo2")
        self.pbNo3 = QtWidgets.QPushButton(Dialog)
        self.pbNo3.setGeometry(QtCore.QRect(130, 40, 70, 70))
        self.pbNo3.setObjectName("pbNo3")
        self.pbNo4 = QtWidgets.QPushButton(Dialog)
        self.pbNo4.setGeometry(QtCore.QRect(0, 105, 70, 70))
        self.pbNo4.setObjectName("pbNo4")
        self.pbNo5 = QtWidgets.QPushButton(Dialog)
        self.pbNo5.setGeometry(QtCore.QRect(65, 105, 70, 70))
        self.pbNo5.setObjectName("pbNo5")
        self.pbNo6 = QtWidgets.QPushButton(Dialog)
        self.pbNo6.setGeometry(QtCore.QRect(130, 105, 70, 70))
        self.pbNo6.setObjectName("pbNo6")
        self.pbNo7 = QtWidgets.QPushButton(Dialog)
        self.pbNo7.setGeometry(QtCore.QRect(0, 170, 70, 70))
        self.pbNo7.setObjectName("pbNo7")
        self.pbNo8 = QtWidgets.QPushButton(Dialog)
        self.pbNo8.setGeometry(QtCore.QRect(65, 170, 70, 70))
        self.pbNo8.setObjectName("pbNo8")
        self.pbNo9 = QtWidgets.QPushButton(Dialog)
        self.pbNo9.setGeometry(QtCore.QRect(130, 170, 70, 70))
        self.pbNo9.setObjectName("pbNo9")
        self.leDisplay = QtWidgets.QLineEdit(Dialog)
        self.leDisplay.setGeometry(QtCore.QRect(7, 5, 187, 35))
        self.leDisplay.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.leDisplay.setObjectName("leDisplay")
        self.pbClear = QtWidgets.QPushButton(Dialog)
        self.pbClear.setGeometry(QtCore.QRect(0, 235, 70, 70))
        self.pbClear.setObjectName("pbClear")
        self.pbOkay = QtWidgets.QPushButton(Dialog)
        self.pbOkay.setGeometry(QtCore.QRect(130, 235, 70, 70))
        self.pbOkay.setObjectName("pbOkay")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "PIN Entry"))
        self.pbNo1.setText(_translate("Dialog", "1"))
        self.pbNo2.setText(_translate("Dialog", "2"))
        self.pbNo3.setText(_translate("Dialog", "3"))
        self.pbNo6.setText(_translate("Dialog", "6"))
        self.pbNo4.setText(_translate("Dialog", "4"))
        self.pbNo5.setText(_translate("Dialog", "5"))
        self.pbNo7.setText(_translate("Dialog", "7"))
        self.pbNo8.setText(_translate("Dialog", "8"))
        self.pbNo9.setText(_translate("Dialog", "9"))
        self.pbNo0.setText(_translate("Dialog", "0"))
        self.leDisplay.setText(_translate("Dialog", "Please Enter PIN"))
        self.pbClear.setText(_translate("Dialog", "CLR"))


class MyForm(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # Continue with your code here.
        self.pw = "12345678"
        self.display_text = ""
        self.ui.pbNo1.clicked.connect(lambda: self.display(self.ui.pbNo1))
        self.ui.pbNo2.clicked.connect(lambda: self.display(self.ui.pbNo2))
        self.ui.pbNo3.clicked.connect(lambda: self.display(self.ui.pbNo3))
        self.ui.pbNo4.clicked.connect(lambda: self.display(self.ui.pbNo4))
        self.ui.pbNo5.clicked.connect(lambda: self.display(self.ui.pbNo5))
        self.ui.pbNo6.clicked.connect(lambda: self.display(self.ui.pbNo6))
        self.ui.pbNo7.clicked.connect(lambda: self.display(self.ui.pbNo7))
        self.ui.pbNo8.clicked.connect(lambda: self.display(self.ui.pbNo8))
        self.ui.pbNo9.clicked.connect(lambda: self.display(self.ui.pbNo9))
        self.ui.pbClear.clicked.connect(self.clear)
        self.ui.pbOkay.setEnabled(True)
        self.ui.pbOkay.clicked.connect(self.check_pw)

    def display(self, sender_button):
        digit = sender_button.text()
        self.display_text += digit
        self.ui.leDisplay.setText(self.display_text)
        if len(self.display_text) == len(self.pw):
            self.check_pw()

    def check_pw(self):
        if re.match(self.pw, self.display_text):
            self.ui.leDisplay.setText("Correct pw")
            return True
        else:
            self.ui.leDisplay.setText("Wrong pw")
            self.display_text = ""
            return False

    def clear(self):
        self.display_text = ""
        self.ui.leDisplay.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())