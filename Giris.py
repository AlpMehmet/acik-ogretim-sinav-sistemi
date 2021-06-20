
from PyQt5 import QtCore, QtGui, QtWidgets
from Ogretmen import Ui_Ogretmen
from Yonetici import Ui_Yonetici
from ogrenciGiris import Ui_og
class Ui_MainWindow(object):
    def openWindowO(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Ogretmen()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()      
    def openWindowY  (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Yonetici()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()    
    def openWindowOg  (self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_og()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 251)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 50, 211, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonYonetici = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonYonetici.setObjectName("pushButtonYonetici")
        self.verticalLayout.addWidget(self.pushButtonYonetici)
        self.pushButtonOgretmen = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonOgretmen.setObjectName("pushButtonOgretmen")
        self.verticalLayout.addWidget(self.pushButtonOgretmen)
        self.pushButtonOgrenci = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButtonOgrenci.setObjectName("pushButtonOgrenci")
        self.verticalLayout.addWidget(self.pushButtonOgrenci)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 429, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButtonOgretmen.clicked.connect(self.openWindowO)
        self.pushButtonYonetici.clicked.connect(self.openWindowY)
        self.pushButtonOgrenci.clicked.connect(self.openWindowOg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonYonetici.setText(_translate("MainWindow", "Yönetici Girişi Yap"))
        self.pushButtonOgretmen.setText(_translate("MainWindow", "Öğretmen Girişi Yap"))
        self.pushButtonOgrenci.setText(_translate("MainWindow", "Öğrenci Girişi Yap"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

