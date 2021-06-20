dogruMu=0
ogretmenId=0
seciliIl=''
seciliTarih=''
istekTarihId=0
istekSalonId=0
istekSaat=0
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Ogretmen(object):
    def giris(self,a,b):
        sifreGir=self.lineEditOSifre.text()
        adgir=self.lineEditOAd.text()
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogretmen""")        
        for veri in im:
            if(veri[4]==sifreGir and veri[3]==adgir):
                sehri=veri[1]
                self.ogretmenId=veri[0]
                if(a==1):
                    self.groupBox3ayKala_2.setVisible(True)
                    self.groupBoxGiris.setVisible(False)
                elif(b==1):
                    self.groupBoxGiris.setVisible(False)
                    self.groupBoxKabulMu.setVisible(True)
                elif(b!=1 and a!=1):
                    self.groupBoxGiris.setVisible(False)
                    self.pushButtonBilgilerim.setVisible(True)
                    
       
        im3 = vt.cursor()
        print(str(sehri))
        im3.execute("""SELECT distinct * FROM salon WHERE salon.ilId='"""+str(sehri)+"""'""") 
        for i in im3:
            self.comboBox3AySalon_2.addItem(str(i[2]))       
        im2 = vt.cursor()
        im2.execute("""SELECT distinct * FROM salon WHERE salon.gorevli1='"""+str(self.ogretmenId)+"""' AND salon.ilId='"""+str(sehri)+"""'""") 
        for i in im2:
            self.labelKabulMuTarih.setText(str(i[5])+" "+str(i[6]))
        vt.close()
    def setupUi(self, Ogretmen):       
        Ogretmen.setObjectName("Ogretmen")
        Ogretmen.resize(628, 377)
        self.centralwidget = QtWidgets.QWidget(Ogretmen)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxKabulMu = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxKabulMu.setEnabled(True)
        self.groupBoxKabulMu.setGeometry(QtCore.QRect(80, 50, 411, 211))
        self.groupBoxKabulMu.setTitle("")
        self.groupBoxKabulMu.setObjectName("groupBoxKabulMu")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBoxKabulMu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(30, 10, 351, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.labelKabulMuTarih = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelKabulMuTarih.sizePolicy().hasHeightForWidth())
        self.labelKabulMuTarih.setSizePolicy(sizePolicy)
        self.labelKabulMuTarih.setObjectName("labelKabulMuTarih")
        self.verticalLayout.addWidget(self.labelKabulMuTarih)
        self.radioButtonRed = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonRed.setObjectName("radioButtonRed")
        self.verticalLayout.addWidget(self.radioButtonRed)
        self.radioButtonKabul = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButtonKabul.setObjectName("radioButtonKabul")
        self.verticalLayout.addWidget(self.radioButtonKabul)
        self.kabul = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.kabul.setObjectName("kabul")
        self.verticalLayout.addWidget(self.kabul)
        self.groupBox3ayKala_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox3ayKala_2.setEnabled(True)
        self.groupBox3ayKala_2.setGeometry(QtCore.QRect(10, 20, 611, 311))
        self.groupBox3ayKala_2.setTitle("")
        self.groupBox3ayKala_2.setObjectName("groupBox3ayKala_2")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox3ayKala_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(30, 40, 562, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox3AyTarih_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox3AyTarih_2.setObjectName("comboBox3AyTarih_2")
        self.horizontalLayout_2.addWidget(self.comboBox3AyTarih_2)
        self.comboBox3AySaat_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox3AySaat_2.setObjectName("comboBox3AySaat_2")
        self.horizontalLayout_2.addWidget(self.comboBox3AySaat_2)
        self.comboBox3AySalon_2 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox3AySalon_2.setObjectName("comboBox3AySalon_2")
        self.horizontalLayout_2.addWidget(self.comboBox3AySalon_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.pushButton3AyOnay_2 = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButton3AyOnay_2.setObjectName("pushButton3AyOnay_2")
        self.verticalLayout_2.addWidget(self.pushButton3AyOnay_2)
        self.groupBoxGiris = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGiris.setEnabled(True)
        self.groupBoxGiris.setGeometry(QtCore.QRect(80, 50, 421, 211))
        self.groupBoxGiris.setTitle("")
        self.groupBoxGiris.setObjectName("groupBoxGiris")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBoxGiris)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(20, 30, 376, 161))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.lineEditOAd = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditOAd.setObjectName("lineEditOAd")
        self.horizontalLayout_3.addWidget(self.lineEditOAd)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.lineEditOSifre = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditOSifre.setObjectName("lineEditOSifre")
        self.horizontalLayout_4.addWidget(self.lineEditOSifre)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.pushButtonOGiris = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButtonOGiris.setObjectName("pushButtonOGiris")
        self.verticalLayout_4.addWidget(self.pushButtonOGiris)
        self.pushButtonBilgilerim = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonBilgilerim.setGeometry(QtCore.QRect(90, 100, 311, 161))
        self.pushButtonBilgilerim.setObjectName("pushButtonBilgilerim")
        Ogretmen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ogretmen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 23))
        self.menubar.setObjectName("menubar")
        Ogretmen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ogretmen)
        self.statusbar.setObjectName("statusbar")
        Ogretmen.setStatusBar(self.statusbar)
        vt = sqlite3.connect('ogrenci.db')
        vt2 = sqlite3.connect('ogrenci.db')
        im2 = vt2.cursor()
        im2.execute("""SELECT distinct * FROM sinavTarih""")   
        for i in im2:
            self.comboBox3AyTarih_2.addItem(str(i[1]))
            self.comboBox3AySaat_2.addItem(str(i[2]))
        vt2.close()   
        vt3 = sqlite3.connect('ogrenci.db')
        im3 = vt3.cursor()
        im3.execute("""SELECT distinct * FROM yonetici""")   
        a=0
        b=0
        for i in im3:
            if(str(i[3])=="1"):
                a=1
                
            elif(str(i[4])=="1"):
                b=1
        vt.close()
        self.pushButtonOGiris.clicked.connect(lambda:self.giris(a,b))
        
        self.comboBox3AySalon_2.activated[str].connect(self.onChanged1Ay_01)
        self.comboBox3AyTarih_2.activated[str].connect(self.onChanged1Ay_02)
        self.comboBox3AySaat_2.activated[str].connect(self.onChanged1Ay_03)
        self.pushButton3AyOnay_2.clicked.connect(self.isteklerKayit)
        self.kabul.clicked.connect(self.kabulveyaRed)
        self.retranslateUi(Ogretmen)
        QtCore.QMetaObject.connectSlotsByName(Ogretmen)
    def isteklerKayit(self):
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        deger1=self.istekSalonId
        deger2=self.istekTarihId
        deger3=self.istekSaat
        im.execute("""UPDATE ogretmen SET salonNoI='"""+deger1+"""', tarihI='"""+deger2+"""', tarihSaatI='"""+deger3+"""' WHERE id='"""+str(self.ogretmenId)+"""""")
        vt.close()
    def kabulveyaRed(self):
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        deger1=self.secili
        im.execute("""UPDATE ogretmen SET kabulRed='"""+deger1+"""' WHERE id='"""+str(self.ogretmenId)+"""""")
        vt.close()
    def onChanged1Ay_01(self,text):
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM salon WHERE  salon.id='"""+str(text)+"""'""")  
        for i in im:
            self.istekSalonId=i[0]
        im()
        vt.close()
        
    def onChanged1Ay_02(self,text):
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM sinavTarih WHERE  tarih='"""+str(text)+"""'""")  
        for i in im:
            self.istekTarihId=i[0]
        im()
        vt.close()
    def onChanged1Ay_03(self,text):
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM sinavTarih WHERE  saat='"""+str(text)+"""'""")  
        for i in im:
            self.istekSaat=i[0]
        im()
        vt.close()
    def toggleRadio(self,b):
        
        if b.text() == "Reddet":
            if b.isChecked() == True:
                self.secili="0"
            else:
                print (b.text()+" is deselected")
				
        if b.text() == "Kabul Et":
            if b.isChecked() == True:
                self.secili="1"
            else:
                print (b.text()+" is deselected")
    def retranslateUi(self, Ogretmen):
        _translate = QtCore.QCoreApplication.translate
        Ogretmen.setWindowTitle(_translate("Ogretmen", "Ogretmen"))
        self.label.setText(_translate("Ogretmen", "Aşağıda yer alan tarihteki görevi kabul ediyor musunuz?"))
        self.radioButtonRed.setText(_translate("Ogretmen", "Reddet"))
        self.radioButtonKabul.setText(_translate("Ogretmen", "Kabul Et"))
        self.label_2.setText(_translate("Ogretmen", "Aşağıdan görev almak istediğiniz tarih, saat ve salonu seçiniz."))
        self.pushButton3AyOnay_2.setText(_translate("Ogretmen", "Onayla"))
        self.label_4.setText(_translate("Ogretmen", "Öğretmen Girişi Yapmaktasınız"))
        self.label_5.setText(_translate("Ogretmen", "Mail Adresiniz: "))
        self.label_6.setText(_translate("Ogretmen", "Şifreniz:         "))
        self.pushButtonOGiris.setText(_translate("Ogretmen", "Giris"))
        self.pushButtonBilgilerim.setText(_translate("Ogretmen", "Bilgileriim"))
        self.kabul.setText(_translate("Ogretmen", "Tamam"))
        self.radioButtonKabul.toggled.connect(lambda:self.toggleRadio(self.radioButtonKabul))
        self.radioButtonRed.toggled.connect(lambda:self.toggleRadio(self.radioButtonRed))
        self.groupBox3ayKala_2.setVisible(False)
        self.groupBoxGiris.setVisible(True)
        self.groupBoxKabulMu.setVisible(False)
        self.pushButtonBilgilerim.setVisible(False)
        self.lineEditOSifre.setEchoMode(QtWidgets.QLineEdit.Password)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ogretmen = QtWidgets.QOgretmen()
    ui = Ui_Ogretmen()
    ui.setupUi(Ogretmen)
    Ogretmen.show()
    sys.exit(app.exec_())

