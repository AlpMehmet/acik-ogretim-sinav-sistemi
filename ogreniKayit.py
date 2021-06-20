# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogrenciKayit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
ders1=""
ders2=""
ders3=""
sehir=""
dersId=[]
class Ui_ogrenciKayit(object):
    def setupUi(self, ogrenciKayit):
        ogrenciKayit.setObjectName("ogrenciKayit")
        ogrenciKayit.resize(297, 600)
        self.centralwidget = QtWidgets.QWidget(ogrenciKayit)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_7.setGeometry(QtCore.QRect(30, 50, 231, 411))
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_3.addWidget(self.comboBox)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_4.addWidget(self.comboBox_2)
        self.verticalLayout_7.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_5.addWidget(self.comboBox_3)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_7)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.comboBox_4 = QtWidgets.QComboBox(self.verticalLayoutWidget_7)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_6.addWidget(self.comboBox_4)
        self.verticalLayout_5.addLayout(self.verticalLayout_6)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        ogrenciKayit.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ogrenciKayit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 297, 23))
        self.menubar.setObjectName("menubar")
        ogrenciKayit.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ogrenciKayit)
        self.statusbar.setObjectName("statusbar")
        ogrenciKayit.setStatusBar(self.statusbar)
       
        self.pushEklee = QtWidgets.QPushButton(self.verticalLayoutWidget_7)
        self.pushEklee.setObjectName("pushEklee")
        self.verticalLayout_7.addWidget(self.pushEklee)
        
        self.comboBox_2.activated[str].connect(self.ders2)
        self.comboBox_3.activated[str].connect(self.ders3)
        self.comboBox.activated[str].connect(self.ders1)
        self.comboBox_4.activated[str].connect(self.sehir)
        self.pushEklee.clicked.connect(self.ogrenciEkle)        
        
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM dersler""") 
        for i in im:         
            self.comboBox_2.addItem(str(i[1]))
            self.comboBox_3.addItem(str(i[1]))
            self.comboBox.addItem(str(i[1]))
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM il""") 
        for i in im2:         
            self.comboBox_4.addItem(str(i[1]))

        vt.close()
        
        self.retranslateUi(ogrenciKayit)
        QtCore.QMetaObject.connectSlotsByName(ogrenciKayit)
        
    def ders2(self,text):
        self.ders2=str(text)
    def ders3(self,text):
        self.ders3=str(text)    
    def ders1(self,text):
        self.ders1=str(text)    
    def sehir(self,text):
        self.sehir=str(text)    
    def ogrenciEkle(self):

        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        deger1=self.lineEdit.text()
        deger2=self.lineEdit_2.text()
        
        im11 = vt.cursor()
        im11.execute("""SELECT * FROM il WHERE  ilAd='"""+str(self.sehir)+"""'""")  
        for i in im11:
            sehirId=str(i[0])
            
        im.execute("""INSERT INTO  ogrenci (no, isim,aldigiDersler, ili) VALUES ('"""+str(deger1)+"""', '"""+str(deger2)+"""', '"""+str("0")+"""' , '"""+str(sehirId)+"""')""")   
        
        im6 = vt.cursor()
        im6.execute("""SELECT * FROM ogrenci WHERE  no='"""+str(deger1)+"""'""")  
        for i in im6:
            ogrenciId=i[0]
        
        im3 = vt.cursor()
        im3.execute("""SELECT * FROM dersler WHERE  dersAd='"""+str(self.ders1)+"""'""")  
        for i in im3:
            dersId.append(i[0])
       
        im5 = vt.cursor()
        im5.execute("""SELECT * FROM dersler WHERE  dersAd='"""+str(self.ders2)+"""'""")  
        for i in im5:
            dersId.append(i[0])
        
        im4 = vt.cursor()
        im4.execute("""SELECT * FROM dersler WHERE  dersAd='"""+str(self.ders3)+"""'""")  
        for i in im4:
            dersId.append(i[0])
            
        im2 = vt.cursor()



        for i in dersId:
            im2.execute("""INSERT INTO  alinanDersler (dersId, ogrenciId) VALUES ('"""+str(i)+"""' , '"""+str(ogrenciId)+"""')""")   

        vt.commit()
        vt.close()           
    def retranslateUi(self, ogrenciKayit):
        _translate = QtCore.QCoreApplication.translate
        ogrenciKayit.setWindowTitle(_translate("ogrenciKayit", "Öğrenci Ekle"))
        self.label.setText(_translate("ogrenciKayit", "No:"))
        self.label_2.setText(_translate("ogrenciKayit", "İsim:"))
        self.label_3.setText(_translate("ogrenciKayit", "Almak İstediğiniz Birinci Dersi Seçiniz."))
        self.label_4.setText(_translate("ogrenciKayit", "Almak İstediğiniz İkinci Dersi Seçiniz."))
        self.label_5.setText(_translate("ogrenciKayit", "Almak İstediğiniz Üçüncü Dersi Seçiniz."))
        self.label_6.setText(_translate("ogrenciKayit", "Şehir:"))
       
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)

        self.pushEklee.setText(_translate("ogrenciKayit", "Ekle"))
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ogrenciKayit = QtWidgets.QMainWindow()
    ui = Ui_ogrenciKayit()
    ui.setupUi(ogrenciKayit)
    ogrenciKayit.show()
    sys.exit(app.exec_())

