# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogretmenKayit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
sehir=""

class Ui_ogretmenKayit(object):
    def setupUi(self, ogretmenKayit):
        ogretmenKayit.setObjectName("ogretmenKayit")
        ogretmenKayit.resize(303, 297)
        self.centralwidget = QtWidgets.QWidget(ogretmenKayit)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(30, 20, 241, 191))
        self.verticalLayoutWidget_7.setObjectName("verticalLayoutWidget_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_7)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.verticalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget_7)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_6.addWidget(self.comboBox_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_3)
        ogretmenKayit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ogretmenKayit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 303, 23))
        self.menubar.setObjectName("menubar")
        ogretmenKayit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ogretmenKayit)
        self.statusbar.setObjectName("statusbar")
        ogretmenKayit.setStatusBar(self.statusbar)
 

        self.pushEklee = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushEklee.setObjectName("pushEklee")
        self.verticalLayout_7.addWidget(self.pushEklee)
        
        
        self.pushEklee.clicked.connect(self.ogretmenEkle)             
        self.comboBox_4.activated[str].connect(self.sehir)

        self.retranslateUi(ogretmenKayit)
        QtCore.QMetaObject.connectSlotsByName(ogretmenKayit)
              
        vt = sqlite3.connect('ogrenci.db')
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM il""") 
        for i in im2:         
            self.comboBox_4.addItem(str(i[1]))
        vt.close()
    def sehir(self,text):
        self.sehir=str(text)    
    def ogretmenEkle(self):
        vt = sqlite3.connect('ogrenci.db')
        
        deger1=self.lineEdit.text()
        deger2=self.lineEdit_2.text()
        im4 = vt.cursor()
        im4.execute("""SELECT * FROM il WHERE  ilAd='"""+str(self.sehir)+"""'""")  
        for i in im4:
            sehirId=str(i[0])
            
        im = vt.cursor()
        im.execute("""INSERT INTO  ogretmen (ili, mail, sifre) VALUES ('"""+str(sehirId)+"""', '"""+str(deger1)+"""', '"""+str(deger2)+"""')""")   
        vt.commit()
        vt.close()           
    def retranslateUi(self, ogretmenKayit):
        _translate = QtCore.QCoreApplication.translate
        ogretmenKayit.setWindowTitle(_translate("ogretmenKayit", "Öğretmen Ekle"))
        self.label.setText(_translate("ogretmenKayit", "Mail:"))
        self.label_2.setText(_translate("ogretmenKayit", "Şifre:"))
        self.label_6.setText(_translate("ogretmenKayit", "Şehir:"))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushEklee.setText(_translate("ogrenciKayit", "Ekle"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ogretmenKayit = QtWidgets.QMainWindow()
    ui = Ui_ogretmenKayit()
    ui.setupUi(ogretmenKayit)
    ogretmenKayit.show()
    sys.exit(app.exec_())

