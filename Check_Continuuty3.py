# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Check_Continuity.ui'
# This is a generated PyQt5 UI code for a simple dialog window with a text input, two buttons, and a plain text output area.
# The purpose of the dialog is not clear from the code alone, but it seems to be related to checking continuity in some data.

from PyQt5 import QtCore, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # Initialize the UI elements and layout
        Dialog.setObjectName("Dialog")
        Dialog.resize(494, 187)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")

        # Create a vertical layout to hold the input and buttons
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Create a horizontal layout to hold the input field and "Fold" button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.btn_sps_file = QtWidgets.QPushButton(Dialog)
        self.btn_sps_file.setObjectName("btn_sps_file")
        self.horizontalLayout.addWidget(self.btn_sps_file)
        self.verticalLayout.addLayout(self.horizontalLayout)

        # Create another horizontal layout to hold the "Run" button
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)

        self.btn_ok = QtWidgets.QPushButton(Dialog)
        self.btn_ok.setObjectName("btn_ok")
        self.horizontalLayout_3.addWidget(self.btn_ok)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        # Add the vertical layout to the main grid layout
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        # Create another horizontal layout to hold the output area
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.horizontalLayout_2.addWidget(self.plainTextEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        # Set the text labels for the UI elements
        self.retranslateUi(Dialog)
        # Connect signals to slots
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_sps_file.setText(_translate("Dialog", "Fold"))
        self.btn_ok.setText(_translate("Dialog", "Run"))
