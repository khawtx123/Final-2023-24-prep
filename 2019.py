# Given from Question

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(270, 183)
		## QRect(xcoordinate, ycoordinate, width, height)
		# Creates the label in the middle
		self.label = QtWidgets.QLabel(Dialog)
		self.label.setGeometry(QtCore.QRect(50, 80, 171, 41))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setWordWrap(True)
		self.label.setObjectName("label")
		# Creates the box for our input
		self.lineEdit = QtWidgets.QLineEdit(Dialog)
		self.lineEdit.setGeometry(QtCore.QRect(80, 10, 111, 51))
		self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
		self.lineEdit.setObjectName("lineEdit")
		# Creates a button for us to push "convert"
		self.pushButton = QtWidgets.QPushButton(Dialog)
		self.pushButton.setGeometry(QtCore.QRect(10, 140, 251, 41))
		self.pushButton.setObjectName("pushButton")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		# translate(x, y). Translate x text to y.
		Dialog.setWindowTitle(_translate("Dialog", "Fahrenheit to Celcius Converter"))
		self.label.setText(_translate("Dialog", "77 Fahrenheit is equivalent to 25 Celcius"))
		self.lineEdit.setText(_translate("Dialog", "77"))
		self.pushButton.setText(_translate("Dialog", "Convert"))

# Question
import sys

class MyForm(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		#Continue code here

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
