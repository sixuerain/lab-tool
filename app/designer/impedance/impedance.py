# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'impedance.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(534, 466)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.ok = QtWidgets.QPushButton(Dialog)
        self.ok.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok.sizePolicy().hasHeightForWidth())
        self.ok.setSizePolicy(sizePolicy)
        self.ok.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ok.setFont(font)
        self.ok.setObjectName("ok")
        self.horizontalLayout_6.addWidget(self.ok, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/image/measure.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalWidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgba(0,20,0,255);")
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.label_2 = QtWidgets.QLabel(self.verticalWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(3, 0))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.generator_channel = QtWidgets.QComboBox(self.verticalWidget)
        self.generator_channel.setObjectName("generator_channel")
        self.generator_channel.addItem("")
        self.generator_channel.addItem("")
        self.generator_channel.addItem("")
        self.generator_channel.addItem("")
        self.generator_channel.addItem("")
        self.generator_channel.addItem("")
        self.generator_channel.addItem("")
        self.verticalLayout_2.addWidget(self.generator_channel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.verticalWidget)
        self.verticalWidget_2 = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setObjectName("verticalWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.verticalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgba(0,20,0,255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.verticalWidget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMinimumSize(QtCore.QSize(3, 0))
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter)
        self.input_channel = QtWidgets.QComboBox(self.verticalWidget_2)
        self.input_channel.setObjectName("input_channel")
        self.input_channel.addItem("")
        self.input_channel.addItem("")
        self.input_channel.addItem("")
        self.input_channel.addItem("")
        self.input_channel.addItem("")
        self.input_channel.addItem("")
        self.input_channel.addItem("")
        self.verticalLayout_3.addWidget(self.input_channel, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.verticalWidget_2)
        self.verticalWidget_5 = QtWidgets.QWidget(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_5.sizePolicy().hasHeightForWidth())
        self.verticalWidget_5.setSizePolicy(sizePolicy)
        self.verticalWidget_5.setObjectName("verticalWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalWidget_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(self.verticalWidget_5)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgba(0,20,0,255);")
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11, 0, QtCore.Qt.AlignHCenter)
        self.resistance = QtWidgets.QSpinBox(self.verticalWidget_5)
        self.resistance.setAlignment(QtCore.Qt.AlignCenter)
        self.resistance.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.resistance.setMinimum(1)
        self.resistance.setMaximum(1000000)
        self.resistance.setObjectName("resistance")
        self.verticalLayout_6.addWidget(self.resistance)
        self.horizontalLayout.addWidget(self.verticalWidget_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.input_channel.setCurrentIndex(1)
        self.generator_channel.currentTextChanged['QString'].connect(self.label_2.setText)
        self.input_channel.currentTextChanged['QString'].connect(self.label_5.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Input Impedance Requirements"))
        self.ok.setText(_translate("Dialog", "OK!"))
        self.label_3.setText(_translate("Dialog", "Generator Channel"))
        self.label_2.setText(_translate("Dialog", "1"))
        self.generator_channel.setItemText(0, _translate("Dialog", "1"))
        self.generator_channel.setItemText(1, _translate("Dialog", "2"))
        self.generator_channel.setItemText(2, _translate("Dialog", "3"))
        self.generator_channel.setItemText(3, _translate("Dialog", "4"))
        self.generator_channel.setItemText(4, _translate("Dialog", "5"))
        self.generator_channel.setItemText(5, _translate("Dialog", "6"))
        self.generator_channel.setItemText(6, _translate("Dialog", "MATH"))
        self.label_4.setText(_translate("Dialog", "Input Channel"))
        self.label_5.setText(_translate("Dialog", "2"))
        self.input_channel.setCurrentText(_translate("Dialog", "2"))
        self.input_channel.setItemText(0, _translate("Dialog", "1"))
        self.input_channel.setItemText(1, _translate("Dialog", "2"))
        self.input_channel.setItemText(2, _translate("Dialog", "3"))
        self.input_channel.setItemText(3, _translate("Dialog", "4"))
        self.input_channel.setItemText(4, _translate("Dialog", "5"))
        self.input_channel.setItemText(5, _translate("Dialog", "6"))
        self.input_channel.setItemText(6, _translate("Dialog", "MATH"))
        self.label_11.setText(_translate("Dialog", "Resistor"))

from app.designer.impedance import impedance_resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

