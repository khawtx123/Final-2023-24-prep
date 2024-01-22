from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import re

class Ui_Dialog(object):

	def setupUi(self, Dialog):
		Dialog.setObjectName("Dialog")
		Dialog.resize(194, 250)

		self.lblPwd = QtWidgets.QLabel(Dialog)
		self.lblPwd.setGeometry(QtCore.QRect(10, 10, 171, 21))
		self.lblPwd.setObjectName("lblPwd")

		self.lnePwd = QtWidgets.QLineEdit(Dialog)
		self.lnePwd.setGeometry(QtCore.QRect(10, 30, 171, 31))
		font = QtGui.QFont()
		font.setFamily("Menlo")
		self.lnePwd.setFont(font)
		self.lnePwd.setObjectName("lnePwd")
		#RETRIEVE INPUT STRING
		self.input_str = self.lnePwd.text()

		self.lblRulSufLen = QtWidgets.QLabel(Dialog)
		self.lblRulSufLen.setGeometry(QtCore.QRect(10, 70, 171, 21))
		self.lblRulSufLen.setFrameShape(QtWidgets.QFrame.Box)
		self.lblRulSufLen.setFrameShadow(QtWidgets.QFrame.Plain)
		self.lblRulSufLen.setObjectName("lblrulSuflen")

		self.lblRulMixCase = QtWidgets.QLabel(Dialog)
		self.lblRulMixCase.setGeometry(QtCore.QRect(10, 100, 171, 21))
		self.lblRulMixCase.setFrameShape(QtWidgets.QFrame.Box)
		self.lblRulMixCase.setFrameShadow(QtWidgets.QFrame.Plain)
		self.lblRulMixCase.setObjectName("lblRulMixCase")

		self.lblRulNumLtr = QtWidgets.QLabel(Dialog)
		self.lblRulNumLtr.setGeometry(QtCore.QRect(10, 130, 171, 21))
		self.lblRulNumLtr.setFrameShape(QtWidgets.QFrame.Box)
		self.lblRulNumLtr.setFrameShadow(QtWidgets.QFrame.Plain)
		self.lblRulNumLtr.setObjectName("lblRulNumLtr")

		self.lblRulSpcChr = QtWidgets.QLabel(Dialog)
		self.lblRulSpcChr.setGeometry(QtCore.QRect(10, 160, 171, 21))
		self.lblRulSpcChr.setFrameShape(QtWidgets.QFrame.Box)
		self.lblRulSpcChr.setFrameShadow(QtWidgets.QFrame.Plain)
		self.lblRulSpcChr.setObjectName("lblRulSpcChr")

		self.resetBut = QtWidgets.QPushButton(Dialog)
		self.resetBut.setGeometry(QtCore.QRect(10, 190, 75, 21))
		self.resetBut.setObjectName("resetBut")
		# ADD EVENT LISTENER
		self.resetBut.clicked.connect(self.onResetBut)

		self.setBut = QtWidgets.QPushButton(Dialog)
		self.setBut.setGeometry(QtCore.QRect(106, 190, 75, 21))
		self.setBut.setEnabled(False)
		self.setBut.setObjectName("setBut")

		self.retranslateUi(Dialog)
		QtCore.QMetaObject.connectSlotsByName(Dialog)

	def onResetBut(self):
		print("hi")

	def retranslateUi(self, Dialog):
		_translate = QtCore.QCoreApplication.translate 
		Dialog.setWindowTitle(_translate("Dialog", "Password Setup"))
		self.lblPwd.setText(_translate("Dialog", "Enter New Password"))
		self.lblRulSufLen.setText(_translate("Dialog", "Sufficient Length: NG"))
		self.lblRulMixCase.setText(_translate("Dialog", "Mix Case: NG"))
		self.lblRulNumLtr.setText(_translate("Dialog", "Numbers + Letters: NG"))
		self.lblRulSpcChr.setText(_translate("Dialog", "Special Characters: NG"))
		self.resetBut.setText(_translate("Dialog", "Reset"))
		self.setBut.setText(_translate("Dialog", "Set"))


class MyForm(QtWidgets.QDialog):
	def __init__(self, parent=None):
		QtWidgets.QWidget.__init__(self, parent)
		self.ui = Ui_Dialog()
		self.ui.setupUi(self)
		self.input_str = ""
		# Continue with your code here
		self.ui.lnePwd.textChanged.connect(self.on_text_changed)
		self.ui.resetBut.clicked.connect(self.on_resetBut)

	def on_resetBut(self):
		self.ui.lnePwd.clear()

	def on_text_changed(self):
		self.input_str = self.ui.lnePwd.text()
		rule_len = self.check_len()
		rule_mix_case =self.mix_case()
		rule_special =self.mix_special()
		rule_mix_numchar =self.mix_num_char()

		if rule_len:
			if rule_special+ rule_mix_numchar +rule_mix_case >=2:
				self.ui.setBut.setEnabled(True)
			else:
				self.ui.setBut.setEnabled(False)

	def check_len(self):
		if len(self.input_str) > 9:
			self.ui.lblRulSufLen.setText("Sufficient Length: Good")
			return True
		else:
			self.ui.lblRulSufLen.setText("Sufficient Length: NG")
			return False

	def mix_case(self):
		upper = 0
		lower = 0
		for char in self.input_str:
			if char.isupper(): upper += 1
			else: lower+= 1

		if upper*lower > 0:
			self.ui.lblRulMixCase.setText("Mix Case: Good")
			return True
		else:
			self.ui.lblRulMixCase.setText("Mix Case: NG")
			return False

	def mix_special(self):
		special_characters_regex = re.compile(r'[@_!#$%^&*()<>?/\|}{~:]')
		match_search = re.search(special_characters_regex, self.input_str)
		if match_search is not None:
			self.ui.lblRulSpcChr.setText("Special Characters: Good")
			return True
		else:
			self.ui.lblRulSpcChr.setText("Special Characters: NG")
			return False

	def mix_num_char(self):
		has_digits = bool(re.search(r'\d', self.input_str))
		has_chars = bool(re.search(r'\w', self.input_str))
		if has_chars and has_digits:
			self.ui.lblRulNumLtr.setText("Numbers + Letters: Good")
			return True
		else:
			self.ui.lblRulNumLtr.setText("Numbers + Letters: NG")
			return False


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
