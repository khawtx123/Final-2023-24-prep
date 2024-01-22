from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from random import shuffle

# in QRect, I changed 60 to 75. Just design error.

class Ui_Dialog(object):
	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(140, 140)
		self.lbDisplay = QtWidgets.QLabel(Dialog)
		self.lbDisplay.setGeometry(QtCore.QRect(20, 10, 111, 31))
		self.lbDisplay.setAcceptDrops(False)
		self.lbDisplay.setAutoFillBackground(False)
		self.lbDisplay.setFrameShape(QtWidgets.QFrame.Box)
		self.lbDisplay.setFrameShadow(QtWidgets.QFrame.Plain)
		self.lbDisplay.setLineWidth(2)
		self.lbDisplay.setAlignment(QtCore.Qt.AlignCenter)
		self.lbDisplay.setObjectName("lbDisplay")

		# Displaying number 3
		self.pbKey04 = QtWidgets.QPushButton(Dialog)
		self.pbKey04.setGeometry(QtCore.QRect(75, 70, 71, 31))
		self.pbKey04.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pbKey04.setFlat(False)
		self.pbKey04.setObjectName("pbKey04")

		# Displaying number 1
		self.pbKey03 = QtWidgets.QPushButton(Dialog)
		self.pbKey03.setGeometry(QtCore.QRect(0, 70, 71, 31))
		self.pbKey03.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pbKey03.setFlat(False)
		self.pbKey03.setObjectName("pbKey03")

		# Displaying number 4
		self.pbKey01 = QtWidgets.QPushButton(Dialog)
		self.pbKey01.setGeometry(QtCore.QRect(0, 40, 71, 31))
		self.pbKey01.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pbKey01.setFlat(False)
		self.pbKey01.setObjectName("pbKey01")

		# Displaying CLR
		self.pbClear = QtWidgets.QPushButton(Dialog)
		self.pbClear.setGeometry(QtCore.QRect(0, 100, 71, 31))
		self.pbClear.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pbClear.setFlat(False)
		self.pbClear.setObjectName("pbClear")

		# Displaying OK
		self.pbOkay = QtWidgets.QPushButton(Dialog)
		self.pbOkay.setGeometry(QtCore.QRect(75, 100, 71, 31))
		self.pbOkay.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pbOkay.setFlat(False)
		self.pbOkay.setObjectName("pbOkay")

		# Displaying number 2
		self.pbKey02 = QtWidgets.QPushButton(Dialog)
		self.pbKey02.setGeometry(QtCore.QRect(75, 40, 71, 31))
		self.pbKey02.setFocusPolicy(QtCore.Qt.NoFocus)
		self.pbKey02.setFlat(False)
		self.pbKey02.setObjectName("pbKey02")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate 
		Dialog.setWindowTitle(_translate("Dialog", "PIN"))
		self.lbDisplay.setText(_translate("Dialog", "Enter PIN"))
		self.pbKey04.setText(_translate("Dialog", "4"))
		self.pbKey03.setText(_translate("Dialog", "3"))
		self.pbKey01.setText(_translate("Dialog", "1"))
		self.pbClear.setText(_translate("Dialog", "CLR"))
		self.pbOkay.setText(_translate("Dialog", "OK"))
		self.pbKey02.setText(_translate("Dialog", "2"))

class MyForm(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.display_text = ""
		self.pw = ""
		self.tries = 1
		self.correct_pw = "123"
		self.nums = [(75, 70, 71, 31), (75, 40, 71, 31), (0, 40, 71, 31), (0, 70, 71, 31)]
		shuffle(self.nums)
		self.ui.pbKey04.setGeometry(QtCore.QRect(self.nums[0][0], self.nums[0][1], self.nums[0][2], self.nums[0][3]))
		self.ui.pbKey03.setGeometry(QtCore.QRect(self.nums[1][0], self.nums[1][1], self.nums[1][2], self.nums[1][3]))
		self.ui.pbKey02.setGeometry(QtCore.QRect(self.nums[2][0], self.nums[2][1], self.nums[2][2], self.nums[2][3]))
		self.ui.pbKey01.setGeometry(QtCore.QRect(self.nums[3][0], self.nums[3][1], self.nums[3][2], self.nums[3][3]))

		# Continue with your code here
		self.ui.lbDisplay.setText(f"Try #{self.tries}")
		self.ui.pbKey01.clicked.connect(self.onPb1Clicked)
		self.ui.pbKey02.clicked.connect(self.onPb2Clicked)
		self.ui.pbKey03.clicked.connect(self.onPb3Clicked)
		self.ui.pbKey04.clicked.connect(self.onPb4Clicked)
		self.ui.pbClear.clicked.connect(self.onClrClicked)
		self.ui.pbOkay.clicked.connect(self.onOkClicked)

	def onPb1Clicked(self):
		self.display_text += "*"
		self.pw += self.ui.pbKey01.objectName()[-1]
		self.ui.lbDisplay.setText(self.display_text)

	def onPb2Clicked(self):
		self.display_text += "*"
		self.pw += self.ui.pbKey02.objectName()[-1]
		self.ui.lbDisplay.setText(self.display_text)

	def onPb3Clicked(self):
		self.display_text += "*"
		self.pw += self.ui.pbKey03.objectName()[-1]
		self.ui.lbDisplay.setText(self.display_text)

	def onPb4Clicked(self):
		self.display_text += "*"
		self.pw += self.ui.pbKey04.objectName()[-1]
		self.ui.lbDisplay.setText(self.display_text)

	def onClrClicked(self):
		self.pw = ""
		self.display_text = ""
		self.ui.lbDisplay.setText(self.display_text)

	def onOkClicked(self):
		if self.pw == self.correct_pw:
			self.ui.lbDisplay.setText("Correct!")
			self.pw = ""
			self.display_text = ""
		else:
			self.tries += 1
			self.ui.lbDisplay.setText(f"Try #{self.tries}")
			self.pw = ""
			self.display_text = ""
			if self.tries>3:
				self.ui.lbDisplay.setText("FUCK OFF BITCH ! Account Locked")
				self.pw = ""
				self.display_text = ""
				self.ui.pbOkay.setEnabled(False)

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())