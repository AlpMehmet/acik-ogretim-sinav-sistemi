# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Bilgiler.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Bilgiler(object):
    def setupUi(self, Bilgiler):
        Bilgiler.setObjectName("Bilgiler")
        Bilgiler.resize(278, 404)
        self.centralwidget = QtWidgets.QWidget(Bilgiler)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setGeometry(QtCore.QRect(40, 20, 191, 321))
        self.verticalLayoutWidget_6.setObjectName("verticalLayoutWidget_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.labelPuan = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.labelPuan.setObjectName("labelPuan")
        self.verticalLayout_2.addWidget(self.labelPuan)
        self.verticalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbMail = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.lbMail.setObjectName("lbMail")
        self.verticalLayout.addWidget(self.lbMail)
        self.verticalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBoxGAlY = QtWidgets.QComboBox(self.verticalLayoutWidget_6)
        self.comboBoxGAlY.setObjectName("comboBoxGAlY")
        self.verticalLayout_4.addWidget(self.comboBoxGAlY)
        self.verticalLayout_6.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.labelTSS = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.labelTSS.setObjectName("labelTSS")
        self.verticalLayout_5.addWidget(self.labelTSS)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelIli = QtWidgets.QLabel(self.verticalLayoutWidget_6)
        self.labelIli.setObjectName("labelIli")
        self.verticalLayout_3.addWidget(self.labelIli)
        self.verticalLayout_6.addLayout(self.verticalLayout_3)
        Bilgiler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Bilgiler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 278, 23))
        self.menubar.setObjectName("menubar")
        Bilgiler.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Bilgiler)
        self.statusbar.setObjectName("statusbar")
        Bilgiler.setStatusBar(self.statusbar)

        self.retranslateUi(Bilgiler)
        QtCore.QMetaObject.connectSlotsByName(Bilgiler)

    def retranslateUi(self, Bilgiler):
        _translate = QtCore.QCoreApplication.translate
        Bilgiler.setWindowTitle(_translate("Bilgiler", "MainWindow"))
        self.labelPuan.setText(_translate("Bilgiler", "Puan"))
        self.lbMail.setText(_translate("Bilgiler", "TextLabel"))
        self.labelTSS.setText(_translate("Bilgiler", "TextLabel"))
        self.labelIli.setText(_translate("Bilgiler", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Bilgiler = QtWidgets.QMainWindow()
    ui = Ui_Bilgiler()
    ui.setupUi(Bilgiler)
    Bilgiler.show()
    sys.exit(app.exec_())

