# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\leejoonho\Desktop\joon_code\web_blog_crawling\test\spinbox\spinboxTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(284, 133)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 262, 103))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinbox_Test = QtWidgets.QSpinBox(self.widget)
        self.spinbox_Test.setObjectName("spinbox_Test")
        self.verticalLayout.addWidget(self.spinbox_Test)
        self.btn_showInfo = QtWidgets.QPushButton(self.widget)
        self.btn_showInfo.setObjectName("btn_showInfo")
        self.verticalLayout.addWidget(self.btn_showInfo)
        self.btn_changeRangeStep = QtWidgets.QPushButton(self.widget)
        self.btn_changeRangeStep.setObjectName("btn_changeRangeStep")
        self.verticalLayout.addWidget(self.btn_changeRangeStep)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.doublespinbox_Test = QtWidgets.QDoubleSpinBox(self.widget)
        self.doublespinbox_Test.setObjectName("doublespinbox_Test")
        self.verticalLayout_2.addWidget(self.doublespinbox_Test)
        self.btn_doubleShowInfo = QtWidgets.QPushButton(self.widget)
        self.btn_doubleShowInfo.setObjectName("btn_doubleShowInfo")
        self.verticalLayout_2.addWidget(self.btn_doubleShowInfo)
        self.btn_doubleChangeRangeStep = QtWidgets.QPushButton(self.widget)
        self.btn_doubleChangeRangeStep.setObjectName("btn_doubleChangeRangeStep")
        self.verticalLayout_2.addWidget(self.btn_doubleChangeRangeStep)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_showInfo.setText(_translate("Dialog", "ShowInfo"))
        self.btn_changeRangeStep.setText(_translate("Dialog", "Change"))
        self.btn_doubleShowInfo.setText(_translate("Dialog", "ShowInfo"))
        self.btn_doubleChangeRangeStep.setText(_translate("Dialog", "Change"))
