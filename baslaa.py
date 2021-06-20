# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'basla.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
tarih=""
saat=""
class Ui_Basla(object):
    def setupUi(self, Basla):
        Basla.setObjectName("Basla")
        Basla.resize(800, 638)
        self.centralwidget = QtWidgets.QWidget(Basla)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(170, 450, 371, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.comboBoxT = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBoxT.setObjectName("comboBoxT")
        self.comboBoxT.addItem("")
        self.comboBoxT.addItem("")
        self.horizontalLayout.addWidget(self.comboBoxT)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox_th = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_th.setObjectName("comboBox_th")
        self.horizontalLayout_2.addWidget(self.comboBox_th)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.comboBox_s = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_s.setObjectName("comboBox_s")
        self.horizontalLayout_3.addWidget(self.comboBox_s)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 10, 731, 201))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(50)
        self.tableWidget_2 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_2.setGeometry(QtCore.QRect(30, 220, 731, 201))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(5)
        self.tableWidget_2.setRowCount(50)
        Basla.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Basla)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Basla.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Basla)
        self.statusbar.setObjectName("statusbar")
        Basla.setStatusBar(self.statusbar)
        
        self.comboBoxT.activated[str].connect(self.comboBoxT1)
        self.comboBox_th.activated[str].connect(self.comboBox_th1)
        self.comboBox_s.activated[str].connect(self.comboBox_th2)
        self.pushButton.clicked.connect(self.baslat)
        vt = sqlite3.connect('ogrenci.db')
        im3 = vt.cursor()
        im3.execute("""SELECT DISTINCT tarih FROM sinavTarih""") 
        for i in im3:
            self.comboBox_th.addItem(str(i[0]))      
        im4= vt.cursor()
        im4.execute("""SELECT DISTINCT saat FROM sinavTarih""") 
        for i in im4:
            self.comboBox_s.addItem(str(i[0]))      
        self.retranslateUi(Basla)
        QtCore.QMetaObject.connectSlotsByName(Basla)
        
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM oYerles""") 
        sayac=0
        for i in im:
            im2=vt.cursor()
            im2.execute("""SELECT * FROM ogrenci WHERE id='"""+str(i[1])+"""'""")
            for j in im2:
                no=str(i[1])
                isim=str(i[2])
            im3=vt.cursor()
            im3.execute("""SELECT * FROM salon WHERE id='"""+str(i[2])+"""'""")
            for a in im3:
                salonNo=str(a[2]) 
            self.tableWidget.setItem(sayac,0, QtWidgets.QTableWidgetItem(str(no)))
            self.tableWidget.setItem(sayac,1, QtWidgets.QTableWidgetItem(str(isim)))
            self.tableWidget.setItem(sayac,2, QtWidgets.QTableWidgetItem(str(salonNo)))
            sayac=sayac+1
        sayac=0
        im2 = vt.cursor()
        im2.execute("""SELECT * FROM salon""") 
        for a in im2:
                self.tableWidget_2.setItem(sayac,0, QtWidgets.QTableWidgetItem(str(a[0])))
                self.tableWidget_2.setItem(sayac,1, QtWidgets.QTableWidgetItem(str(a[1])))
                self.tableWidget_2.setItem(sayac,2, QtWidgets.QTableWidgetItem(str(a[3])))
                self.tableWidget_2.setItem(sayac,3, QtWidgets.QTableWidgetItem(str(a[5])))
                self.tableWidget_2.setItem(sayac,4, QtWidgets.QTableWidgetItem(str(a[6]))) 
                sayac=sayac+1
        vt.close()           
    def baslat(self):
        print("girdi")
        vt2 = sqlite3.connect('ogrenci.db')
        im = vt2.cursor()
        d1=self.tarih
        d2=self.saat
        print(d1,d2)
        im.execute("""INSERT INTO baslayan (tarih, saat) VALUES (?,?)""",(d1,d2))   
        vt2.commit()
        vt2.close()  
    def comboBox_th1(self,text):
        self.tarih=str(text)
    def comboBox_th2(self,text):
        self.saat=str(text)
    def comboBoxT1(self,text):
        vt = sqlite3.connect('ogrenci.db')
        im2 = vt.cursor()
        if(str(text=="Final")):
            im2.execute("""UPDATE yonetici SET sınavbasla='"""+str("1")+"""' WHERE yonetici.id='"""+str("1")+"""'""") 
        elif(str(text=="Ara Sınav")):
            im2.execute("""UPDATE yonetici SET sınavbasla='"""+str("2")+"""' WHERE yonetici.id='"""+str("1")+"""'""") 
        vt.commit()
        vt.close()    
    def retranslateUi(self, Basla):
        _translate = QtCore.QCoreApplication.translate
        Basla.setWindowTitle(_translate("Basla", "Başlat"))
        self.label.setText(_translate("Basla", "Hangi Sınav Başlasın:                              "))
        self.comboBoxT.setItemText(0, _translate("Basla", "Ara Sınav"))
        self.comboBoxT.setItemText(1, _translate("Basla", "Final"))
        self.label_2.setText(_translate("Basla", "Hangi Tarihteki Sınavlar Başlasın:"))
        self.label_3.setText(_translate("Basla", "Hangi Saatteki Sınavlar Başlasın:"))
        self.pushButton.setText(_translate("Basla", "Başlat"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Basla = QtWidgets.QMainWindow()
    ui = Ui_Basla()
    ui.setupUi(Basla)
    Basla.show()
    sys.exit(app.exec_())

