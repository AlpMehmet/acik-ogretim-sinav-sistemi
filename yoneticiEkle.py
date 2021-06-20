# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yoneticiEkle.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class Ui_YoneticiEkle(object):
    def setupUi(self, YoneticiEkle):
        YoneticiEkle.setObjectName("YoneticiEkle")
        YoneticiEkle.resize(299, 281)
        self.centralwidget = QtWidgets.QWidget(YoneticiEkle)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(20, 20, 241, 191))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_8.addWidget(self.lineEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_10.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_10.addWidget(self.lineEdit_2)
        self.verticalLayout_9.addLayout(self.verticalLayout_10)
        self.verticalLayout_7.addLayout(self.verticalLayout_9)
        YoneticiEkle.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(YoneticiEkle)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 299, 23))
        self.menubar.setObjectName("menubar")
        YoneticiEkle.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(YoneticiEkle)
        self.statusbar.setObjectName("statusbar")
        YoneticiEkle.setStatusBar(self.statusbar)
        self.pushEklee = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushEklee.setObjectName("pushEklee")
        self.verticalLayout_7.addWidget(self.pushEklee)
        
        self.retranslateUi(YoneticiEkle)
        QtCore.QMetaObject.connectSlotsByName(YoneticiEkle)
          
        self.pushEklee.clicked.connect(self.yoneticiEkle)             

    def yoneticiEkle(self):
        vt = sqlite3.connect('ogrenci.db')
        
        deger1=self.lineEdit.text()
        deger2=self.lineEdit_2.text()
        im = vt.cursor()
        im.execute("""INSERT INTO  yonetici (sifre, kullaniciAd) VALUES ('"""+str(deger1)+"""', '"""+str(deger2)+"""')""")   
        vt.commit()
        vt.close() 
        
    def retranslateUi(self, YoneticiEkle):
        _translate = QtCore.QCoreApplication.translate
        YoneticiEkle.setWindowTitle(_translate("YoneticiEkle", "Yönetici Ekle"))
        self.label.setText(_translate("YoneticiEkle", "Kullanıcı Adı:"))
        self.label_2.setText(_translate("YoneticiEkle", "Şifre:"))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushEklee.setText(_translate("ogrenciKayit", "Ekle"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    YoneticiEkle = QtWidgets.QMainWindow()
    ui = Ui_YoneticiEkle()
    ui.setupUi(YoneticiEkle)
    YoneticiEkle.show()
    sys.exit(app.exec_())

