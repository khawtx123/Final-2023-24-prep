from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# QRect(x, y, width, height)

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(273, 184)

		# Generate the text in the middle showing our BMI result.
		self.lblResult = QtWidgets.QLabel(Dialog)
		self.lblResult.setGeometry(QtCore.QRect(50, 90, 171, 41))
		self.lblResult.setAlignment(QtCore.Qt.AlignCenter)
		self.lblResult.setWordWrap(True)
		self.lblResult.setObjectName("lblResult")

		# Generate a box for us to input our height.
		self.lneHeight = QtWidgets.QLineEdit(Dialog)
		self.lneHeight.setGeometry(QtCore.QRect(150, 10, 71, 31))
		self.lneHeight.setAlignment(QtCore.Qt.AlignCenter)
		self.lneHeight.setObjectName("lneHeight")

		# Generate a box for us to input our weight.
		self.lneWeight = QtWidgets.QLineEdit(Dialog)
		self.lneWeight.setGeometry(QtCore.QRect(150, 50, 71, 31))
		self.lneWeight.setAlignment(QtCore.Qt.AlignCenter)
		self.lneWeight.setObjectName("lneWeight")

		# To generate the Push Button labeled "Convert"
		self.pbtCalculate = QtWidgets.QPushButton(Dialog)
		self.pbtCalculate.setGeometry(QtCore.QRect(10, 140, 251, 41))
		self.pbtCalculate.setObjectName("pbtCalculate")

		# To label - Height (cm)
		self.lblHeight = QtWidgets.QLabel(Dialog)
		self.lblHeight.setGeometry(QtCore.QRect(20, 10, 101,31))
		self.lblHeight.setAlignment(QtCore.Qt.AlignCenter)
		self.lblHeight.setWordWrap(True)
		self.lblHeight.setObjectName("lblHeight")

		# To label - Weight (kg)
		self.lblWeight = QtWidgets.QLabel(Dialog)
		self.lblWeight.setGeometry(QtCore.QRect(20, 50, 101, 31))
		self.lblWeight.setAlignment(QtCore.Qt.AlignCenter)
		self.lblWeight.setWordWrap(True)
		self.lblWeight.setObjectName("lblWeight")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate
		Dialog.setWindowTitle(_translate("Dialog", "EMI Calculator"))
		self.lblResult.setText(_translate("Dialog", "BMI is 22.06. Your weight is normal."))
		self.lneHeight.setText(_translate("Dialog", "155"))
		self.pbtCalculate.setText(_translate("Dialog", "Convert"))
		self.lblHeight.setText(_translate("Dialog", "Height (cm)"))
		self.lneWeight.setText(_translate("Dialog", "53"))
		self.lblWeight.setText(_translate("Dialog", "Weight (kg)"))


class MyForm(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)

		# Continue with your code here.


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())