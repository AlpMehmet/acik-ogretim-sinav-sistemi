# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Yonetici.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
yoneticiId=0   
seciliIl=''
seciliDers=''
seciliDersId=0
seciliIlId=0
seciliRadio=''
diziSaat=[]
AD=""
DC=""
diziTatih=[]
diziSehir=[]
diziSalon=[]
gecerliSaat=""
gecerliTarih=""
gecerliSehir=0
gecerliSalon=0
geciciIdBirOnce=-1
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from baslaa import Ui_Basla
from ogreniKayit import Ui_ogrenciKayit
from ogretmenKayit import Ui_ogretmenKayit
from yoneticiEkle import Ui_YoneticiEkle

from email import encoders
class Ui_Yonetici(object):
    def openWindowO(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Basla()
        self.ui.setupUi(self.window)
        self.window.show() 
    def openWindow2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ogrenciKayit()
        self.ui.setupUi(self.window)
        self.window.show() 
    def openWindow3(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ogretmenKayit()
        self.ui.setupUi(self.window)
        self.window.show() 
    def openWindow4(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_YoneticiEkle()
        self.ui.setupUi(self.window)
        self.window.show()
    def openWindow5(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Basla()
        self.ui.setupUi(self.window)
        self.window.show() 
    def setupUi(self, Yonetici):
        Yonetici.setObjectName("Yonetici")
        Yonetici.resize(746, 691)
        self.centralwidget = QtWidgets.QWidget(Yonetici)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxGiris = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxGiris.setEnabled(True)
        self.groupBoxGiris.setGeometry(QtCore.QRect(170, 190, 421, 221))
        self.groupBoxGiris.setTitle("")
        self.groupBoxGiris.setObjectName("groupBoxGiris")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBoxGiris)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 40, 376, 161))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditYoneticiAd = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditYoneticiAd.setObjectName("lineEditYoneticiAd")
        self.horizontalLayout_2.addWidget(self.lineEditYoneticiAd)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEditYoneticiSifre = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.lineEditYoneticiSifre.setObjectName("lineEditYoneticiSifre")
        self.horizontalLayout_3.addWidget(self.lineEditYoneticiSifre)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.pushButtonYGiris = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.pushButtonYGiris.setObjectName("pushButtonYGiris")
        self.verticalLayout_2.addWidget(self.pushButtonYGiris)
        self.groupBoxTercih = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxTercih.setEnabled(True)
        self.groupBoxTercih.setGeometry(QtCore.QRect(170, 60, 371, 441))
        self.groupBoxTercih.setTitle("")
        self.groupBoxTercih.setObjectName("groupBoxTercih")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBoxTercih)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 70, 297, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButtonYeniSoru = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonYeniSoru.sizePolicy().hasHeightForWidth())
        self.pushButtonYeniSoru.setSizePolicy(sizePolicy)
        self.pushButtonYeniSoru.setObjectName("pushButtonYeniSoru")
        self.verticalLayout.addWidget(self.pushButtonYeniSoru)
        self.pushButtonYeniSalon = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonYeniSalon.sizePolicy().hasHeightForWidth())
        self.pushButtonYeniSalon.setSizePolicy(sizePolicy)
        self.pushButtonYeniSalon.setObjectName("pushButtonYeniSalon")
        self.verticalLayout.addWidget(self.pushButtonYeniSalon)
        self.pushButtonKitapcikOlustur = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonKitapcikOlustur.sizePolicy().hasHeightForWidth())
        self.pushButtonKitapcikOlustur.setSizePolicy(sizePolicy)
        self.pushButtonKitapcikOlustur.setObjectName("pushButtonKitapcikOlustur")
        self.verticalLayout.addWidget(self.pushButtonKitapcikOlustur)
        self.pushButton1MailYolla = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton1MailYolla.sizePolicy().hasHeightForWidth())
        self.pushButton1MailYolla.setSizePolicy(sizePolicy)
        self.pushButton1MailYolla.setObjectName("pushButton1MailYolla")
        self.verticalLayout.addWidget(self.pushButton1MailYolla)
        self.pushButtonYerlestir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonYerlestir.sizePolicy().hasHeightForWidth())
        self.pushButtonYerlestir.setSizePolicy(sizePolicy)
        self.pushButtonYerlestir.setObjectName("pushButtonYerlestir")
        self.verticalLayout.addWidget(self.pushButtonYerlestir)
        self.pushButton3Gun = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton3Gun.sizePolicy().hasHeightForWidth())
        self.pushButton3Gun.setSizePolicy(sizePolicy)
        self.pushButton3Gun.setObjectName("pushButton3Gun")
        self.verticalLayout.addWidget(self.pushButton3Gun)
        
        self.pbogrenciekle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbogrenciekle.sizePolicy().hasHeightForWidth())
        self.pbogrenciekle.setSizePolicy(sizePolicy)
        self.pbogrenciekle.setObjectName("pbogrenciekle")
        self.verticalLayout.addWidget(self.pbogrenciekle)
        
        self.pbogretmenekle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbogretmenekle.sizePolicy().hasHeightForWidth())
        self.pbogretmenekle.setSizePolicy(sizePolicy)
        self.pbogretmenekle.setObjectName("pbogretmenekle")
        self.verticalLayout.addWidget(self.pbogretmenekle)
        
        self.pbyoneticiekle = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbyoneticiekle.sizePolicy().hasHeightForWidth())
        self.pbyoneticiekle.setSizePolicy(sizePolicy)
        self.pbyoneticiekle.setObjectName("pbyoneticiekle")
        self.verticalLayout.addWidget(self.pbyoneticiekle)
 
        self.pbogrenciyerlestir = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pbogrenciyerlestir.sizePolicy().hasHeightForWidth())
        self.pbogrenciyerlestir.setSizePolicy(sizePolicy)
        self.pbogrenciyerlestir.setObjectName("pbogrenciyerlestir")
        self.verticalLayout.addWidget(self.pbogrenciyerlestir)
       
        self.pushButtonBaslat = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBaslat.sizePolicy().hasHeightForWidth())
        self.pushButtonBaslat.setSizePolicy(sizePolicy)
        self.pushButtonBaslat.setObjectName("pushButtonBaslat")
        self.verticalLayout.addWidget(self.pushButtonBaslat)
        self.groupBoxSoruEkle = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSoruEkle.setGeometry(QtCore.QRect(30, 50, 671, 561))
        self.groupBoxSoruEkle.setTitle("")
        self.groupBoxSoruEkle.setObjectName("groupBoxSoruEkle")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBoxSoruEkle)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 60, 661, 452))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.textEditSoru = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditSoru.sizePolicy().hasHeightForWidth())
        self.textEditSoru.setSizePolicy(sizePolicy)
        self.textEditSoru.setObjectName("textEditSoru")
        self.horizontalLayout_11.addWidget(self.textEditSoru)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.textEditA = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditA.sizePolicy().hasHeightForWidth())
        self.textEditA.setSizePolicy(sizePolicy)
        self.textEditA.setObjectName("textEditA")
        self.horizontalLayout_4.addWidget(self.textEditA)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_5.addWidget(self.label_8)
        self.textEditB = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditB.sizePolicy().hasHeightForWidth())
        self.textEditB.setSizePolicy(sizePolicy)
        self.textEditB.setObjectName("textEditB")
        self.horizontalLayout_5.addWidget(self.textEditB)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_6.addWidget(self.label_10)
        self.textEditC = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditC.sizePolicy().hasHeightForWidth())
        self.textEditC.setSizePolicy(sizePolicy)
        self.textEditC.setObjectName("textEditC")
        self.horizontalLayout_6.addWidget(self.textEditC)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_8.addWidget(self.label_12)
        self.textEditD = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEditD.sizePolicy().hasHeightForWidth())
        self.textEditD.setSizePolicy(sizePolicy)
        self.textEditD.setObjectName("textEditD")
        self.horizontalLayout_8.addWidget(self.textEditD)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.labelKontrol = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelKontrol.sizePolicy().hasHeightForWidth())
        self.labelKontrol.setSizePolicy(sizePolicy)
        self.labelKontrol.setObjectName("labelKontrol")
        self.horizontalLayout_9.addWidget(self.labelKontrol)
        self.radioButtonA = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonA.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonA.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButtonA.setObjectName("radioButtonA")
        self.horizontalLayout_9.addWidget(self.radioButtonA)
        self.radioButtonB = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonB.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonB.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButtonB.setObjectName("radioButtonB")
        self.horizontalLayout_9.addWidget(self.radioButtonB)
        self.radioButtonC = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonC.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonC.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButtonC.setObjectName("radioButtonC")
        self.horizontalLayout_9.addWidget(self.radioButtonC)
        self.radioButtonD = QtWidgets.QRadioButton(self.verticalLayoutWidget_3)
        self.radioButtonD.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.radioButtonD.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.radioButtonD.setObjectName("radioButtonD")
        self.horizontalLayout_9.addWidget(self.radioButtonD)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.comboBoxDersler = QtWidgets.QComboBox(self.groupBoxSoruEkle)
        self.comboBoxDersler.setGeometry(QtCore.QRect(10, 20, 661, 22))
        self.comboBoxDersler.setObjectName("comboBoxDersler")
        self.horizontalLayoutWidget_9 = QtWidgets.QWidget(self.groupBoxSoruEkle)
        self.horizontalLayoutWidget_9.setGeometry(QtCore.QRect(10, 510, 661, 41))
        self.horizontalLayoutWidget_9.setObjectName("horizontalLayoutWidget_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButtonBitir = QtWidgets.QPushButton(self.horizontalLayoutWidget_9)
        self.pushButtonBitir.setObjectName("pushButtonBitir")
        self.horizontalLayout_10.addWidget(self.pushButtonBitir)
        self.groupBoxSalonEkle = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSalonEkle.setEnabled(True)
        self.groupBoxSalonEkle.setGeometry(QtCore.QRect(180, 200, 401, 181))
        self.groupBoxSalonEkle.setTitle("")
        self.groupBoxSalonEkle.setObjectName("groupBoxSalonEkle")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBoxSalonEkle)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(90, 30, 231, 131))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.lineEditSalonKisiSay = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditSalonKisiSay.setObjectName("lineEditSalonKisiSay")
        self.horizontalLayout_7.addWidget(self.lineEditSalonKisiSay)
    
        self.lineEditSalonNo = QtWidgets.QLineEdit(self.verticalLayoutWidget_4)
        self.lineEditSalonNo.setObjectName("lineEditSalonNo")
        self.horizontalLayout_7.addWidget(self.lineEditSalonNo)
        
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout.addWidget(self.label_6)
        self.comboBoxSalonili = QtWidgets.QComboBox(self.verticalLayoutWidget_4)
        self.comboBoxSalonili.setObjectName("comboBoxSalonili")
        self.horizontalLayout.addWidget(self.comboBoxSalonili)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.pushButtonSalonEkle = QtWidgets.QPushButton(self.verticalLayoutWidget_4)
        self.pushButtonSalonEkle.setObjectName("pushButtonSalonEkle")
        self.verticalLayout_4.addWidget(self.pushButtonSalonEkle)
        Yonetici.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Yonetici)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 746, 23))
        self.menubar.setObjectName("menubar")
        Yonetici.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Yonetici)
        self.statusbar.setObjectName("statusbar")
        Yonetici.setStatusBar(self.statusbar)

        self.pushButtonYerlestir.clicked.connect(self.yerlestir)
        self.pushButtonKitapcikOlustur.clicked.connect(self.kitapcikOlustur)
        self.pushButtonBitir.clicked.connect(self.yeniSoruEkle)
        self.pushButtonYeniSoru.clicked.connect(self.yeniSoru)
        self.pushButtonSalonEkle.clicked.connect(self.yeniSalonEkle)
        self.pushButtonYeniSalon.clicked.connect(self.yeniSalon)
        self.pushButton3Gun.clicked.connect(self.mailyolla3gun)
        self.pushButton1MailYolla.clicked.connect(self.mailyolla1ay)
        self.pushButtonYGiris.clicked.connect(self.giris)
        self.pbogrenciekle.clicked.connect(self.openWindow2)
        self.pbogretmenekle.clicked.connect(self.openWindow3)
        self.pbyoneticiekle.clicked.connect(self.openWindow4)
        self.pushButtonBaslat.clicked.connect(self.openWindow5)
        self.pbogrenciyerlestir.clicked.connect(self.ogrenciYerlestir)
        

        self.retranslateUi(Yonetici)
        QtCore.QMetaObject.connectSlotsByName(Yonetici)
    def ogrenciYerlestir(self):
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM salon""") 
        for i in im:
            kisisay=str(i[3])
            sehirId=str(i[1])
            for j in kisisay:
                im2 = vt.cursor()
                im2.execute("""SELECT * FROM ogrenci WHERE id='"""+str(j)+"""' and ili='"""+str(sehirId)+"""'""") 
                for a in im:
                    im3 = vt.cursor()
                    im3.execute("""INSERT INTO  oYerles (ogrenciId, salonId) VALUES ('"""+str(a[0])+"""', '"""+str(i[0])+"""')""")   

        vt.close()
    
    def yerlestir(self):
        deger2="0"
        deger="1"
        vt2 = sqlite3.connect('ogrenci.db')
        im2 = vt2.cursor()
        im2.execute("""UPDATE yonetici SET y1ay='"""+deger2+"""', y3gun='"""+deger+"""' WHERE yonetici.id='"""+str(self.yoneticiId)+"""'""")   
        vt2.commit()
        vt2.close()
        diziId=[]      
        diziId2=[] 
        diziPuan=[]
        diziKac=[] 
                   
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogretmen""") 
        say=0
        for i in im:
            diziPuan.append(i[6])
            diziId2.append(i[0])
            diziId.append(i[0])
        vt.close()
        diziPuan.sort(reverse=True)
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogretmen""")         
        
        for i in im:
            for j in range(0,len(diziPuan)-1):
                if(i[6]==diziPuan[j]):
                    diziKac.append(say)                   
                say=say+1
            say=0

        

        for j in range(0,len(diziPuan)-1):
            diziId[diziKac[j]]=diziId2[j]
        salonNo=[]

        var=0
        for j in range(0,len(diziPuan)):   
            im2 = vt.cursor()
            im2.execute("""SELECT * FROM ogretmen WHERE id='"""+str(diziId[j])+"""'""") 
            for i in im2:
                    for j in range(0,len(salonNo)):
                        if(salonNo[j]==i[5]):  
                            if(i[9]==0):
                                var=1
                                
                    if(var==0 and i[9]==0):                 
                       salonNo.append(i[5])
                       im3 = vt.cursor()
                       im3.execute("""UPDATE salon SET gorevli1='"""+str(i[0])+"""' WHERE salon.salonNo='"""+str(i[5])+"""' AND salon.tarih='"""+str(i[7])+"""' AND salon.saat='"""+str(i[8])+"""'""")       
                       vt.commit()
                    else:
                        var=0
        vt.close()
    def  kitapcikOlustur(self):
#        96 soru için 16 kitapçık soru 8 tür için 12 soru 
        var=0
        a=0
        seciliDers2=[]
        for i in range(0,16):
            
            gecici=random.randint(0,8)
            for i in range(0,len(seciliDers2)):
                while(str(seciliDers2[i])==str(gecici)):
                    a=0
                    gecici=random.randint(0,8)
            if(str(var)=="0"):
                seciliDers2.append(gecici)
                gecici2=random.randint(0,1000)
                dersKodu=str(gecici)+str(gecici2)
                vt2 = sqlite3.connect('ogrenci.db')
                im2 = vt2.cursor()
                im2.execute("""SELECT * FROM dersler WHERE id='"""+str(gecici)+"""'""")  
            else:
                gecici=random.randint(0,8)
                seciliDers2.append(gecici)
            say1=0
            for j in range(0,6):
                for a in im2:
                    im4 = vt2.cursor()
                    im4.execute("""SELECT COUNT(id) FROM sorular""") 
                    for i in im4:
                        gecici=random.randint(1,i[0])
#                    
                    im3 = vt2.cursor()
                    im3.execute("""SELECT * FROM sorular WHERE dersId='"""+str(a[0])+"""'""") 
                    for b in im3:
                        if(say1!=1):
                            geciciS1=random.randint(2,5)
                            geciciS2=random.randint(2,5)
                            geciciS3=random.randint(2,5)
                            geciciS4=random.randint(2,5)
                        while(geciciS1==geciciS2 or geciciS3==geciciS4 or geciciS1==geciciS4 or geciciS1==geciciS3 or geciciS2==geciciS4 or geciciS2==geciciS3):
                            geciciS1=random.randint(2,5)
                            geciciS2=random.randint(2,5)
                            geciciS3=random.randint(2,5)
                            geciciS4=random.randint(2,5)
                        CA=geciciS1
                        CB=geciciS2
                        CC=geciciS3
                        CD=geciciS4
                        if(str(b[7])=="2"):
                            self.DC=CA
                        if(str(b[7])=="3"):
                            self.DC=CB
                        if(str(b[7])=="4"):
                            self.DC=CC
                        if(str(b[7])=="5"):
                            self.DC=CD
                        if(str(self.DC)=="2"):
                            self.AD="A"
                        if(str(self.DC)=="3"):
                            self.AD="B"
                        if(str(self.DC)=="4"):
                            self.AD="C"
                        if(str(self.DC)=="5"):
                            self.AD="D"
                        im = vt2.cursor()
                        im.execute("""INSERT INTO  sorularK (soru, A, B, C, D, Dogru, dersId, derskKodu) VALUES ('"""+str(b[1])+"""', '"""+str(b[CA])+"""' , '"""+str(b[CB])+"""', '"""+str(b[CC])+"""', '"""+str(b[CD])+"""', '"""+str(self.AD)+"""', '"""+str(a[0])+"""', '"""+str(dersKodu)+"""')""")   
                        say1=say1+1
            im232 = vt2.cursor()
            im232.execute("""INSERT INTO  kitapcık (dersKodu , soruId) VALUES ('"""+str(a[0])+"""', '"""+str(dersKodu)+"""')""")   
                          
            vt2.commit()
            vt2.close()
    def yeniSoruEkle(self):
        vt2 = sqlite3.connect('ogrenci.db')
        im2 = vt2.cursor()
        im2.execute("""SELECT * FROM dersler WHERE dersAd='"""+self.seciliDers+"""'""") 
        for i in im2:         
            self.seciliDersId=i[0]
        vt2.close()
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        deger1=self.textEditSoru.toPlainText()
        deger2=self.textEditA.toPlainText()
        deger3=self.textEditB.toPlainText()
        deger4=self.textEditC.toPlainText()
        deger5=self.textEditD.toPlainText()
        deger6=self.seciliRadio
    
        im.execute("""INSERT INTO  sorular (soru, A, B, C, D, Dogru, dersId) VALUES ('"""+str(deger1)+"""', '"""+str(deger2)+"""' , '"""+str(deger3)+"""', '"""+str(deger4)+"""', '"""+str(deger5)+"""', '"""+str(deger6)+"""', '"""+str(self.seciliDersId)+"""')""")   
        vt.commit()
        vt.close()       
        self.radioButtonA.setChecked(False)
        self.radioButtonB.setChecked(False)
        self.radioButtonC.setChecked(False)
        self.radioButtonD.setChecked(False)
        self.groupBoxSoruEkle.setVisible(False)
        self.groupBoxTercih.setVisible(True)


    def yeniSoru(self):
        self.groupBoxTercih.setVisible(False)
        self.groupBoxSoruEkle.setVisible(True)
        self.comboBoxDersler.activated[str].connect(self.onChanged2)
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM dersler""") 
        for i in im:         
            self.comboBoxDersler.addItem(str(i[1]))
        vt.close()
    def yeniSalon(self):
        self.groupBoxTercih.setVisible(False)
        self.groupBoxSalonEkle.setVisible(True)
        self.comboBoxSalonili.activated[str].connect(self.onChanged)
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM il""") 
        for i in im:         
            self.comboBoxSalonili.addItem(str(i[1]))
        vt.close()
    
    def yeniSalonEkle(self):
        vt2 = sqlite3.connect('ogrenci.db')
        im2 = vt2.cursor()
        saatler=["11:00","15:00","13:00"]
        tarihler=["10.01.2020","20.01.2020","12.02.2020","13.02.2020"]
        im2.execute("""SELECT * FROM il WHERE ilAd='"""+self.seciliIl+"""'""") 
        for i in im2:         
            self.seciliIlId=i[0]
        vt2.close()
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        deger3=self.lineEditSalonKisiSay.text()
        deger2=self.lineEditSalonNo.text()
        for i in saatler:
            for j in tarihler:
                im.execute("""INSERT INTO  salon (ilId, salonNo, kisiS, tarih, saat) VALUES ('"""+str(self.seciliIlId)+"""', '"""+str(deger2)+"""' , '"""+str(deger3)+"""', '"""+str(j)+"""', '"""+str(i)+"""')""")   
                vt.commit()
        vt.close()       
        self.groupBoxTercih.setVisible(True)
        self.groupBoxSalonEkle.setVisible(False)
    def onChanged2(self, text):
        self.seciliDers = text
    def onChanged(self, text):
        self.seciliIl = text
    def mailyolla3gun(self):       
        email_user = 'manizha.rasouly@gmail.com'
        email_password = '122my122'       
        deger2="0"
        subject = 'subject'
        vt2 = sqlite3.connect('ogrenci.db')
        im2 = vt2.cursor()
        im2.execute("""UPDATE yonetici SET y1ay='"""+deger2+"""', y3gun='"""+deger2+"""' WHERE yonetici.id='"""+str(self.yoneticiId)+"""'""")   
        vt2.commit()
        vt2.close()
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogretmen""")   
        for veri in im:
            email_send = veri[3]
            print(email_send)
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['Subject'] = subject
            msg['To'] = email_send
            body = 'Kabul veya red etme süreniz dolmuştur.'
            msg.attach(MIMEText(body,'plain'))
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)          
            server.sendmail(email_user,email_send,text)                       
        server.quit()
        vt.close()
    def mailyolla1ay(self):  
        email_user = 'manizha.rasouly@gmail.com'
        email_password = '122my122'
        deger="1"
        deger0="0"
        subject = 'subject'
        vt2 = sqlite3.connect('ogrenci.db')
        im2 = vt2.cursor()
        im2.execute("""UPDATE yonetici SET y1ay="""+deger+""",y3gun="""+deger0+""" WHERE yonetici.id="""+str(self.yoneticiId)+"""""")   
        vt2.commit()
        vt2.close()
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM ogretmen""")   
        for veri in im:
            email_send = veri[3]
            print(email_send)
            msg = MIMEMultipart()
            msg['From'] = email_user
            msg['Subject'] = subject
            msg['To'] = email_send
            body = 'Lütfen sisteme girip görev almak istediğiniz tarihleri seçiniz'
            msg.attach(MIMEText(body,'plain'))
            text = msg.as_string()
            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(email_user,email_password)          
            server.sendmail(email_user,email_send,text)                       
        server.quit()
        vt.close()
    def giris(self):
        sifreGir=self.lineEditYoneticiSifre.text()
        adgir=self.lineEditYoneticiAd.text()
        vt = sqlite3.connect('ogrenci.db')
        im = vt.cursor()
        im.execute("""SELECT * FROM yonetici""")        
        for veri in im:
            if(veri[1]==sifreGir and veri[2]==adgir):
                print("dogru")
                self.yoneticiId=veri[0]
                self.groupBoxTercih.setVisible(True)
                self.groupBoxGiris.setVisible(False)
        vt.close()
    def toggleRadio(self,b):
        
        if b.text() == "A":
            if b.isChecked() == True:
                self.seciliRadio=b.text()
            else:
                print (b.text()+" is deselected")
				
        if b.text() == "B":
            if b.isChecked() == True:
                self.seciliRadio=b.text()
            else:
                print (b.text()+" is deselected")
        if b.text() == "C":
            if b.isChecked() == True:
                self.seciliRadio=b.text()
            else:
                print (b.text()+" is deselected")
        if b.text() == "D":
            if b.isChecked() == True:
                self.seciliRadio=b.text()
            else:
                print (b.text()+" is deselected") 

            
    def retranslateUi(self, Yonetici):
        _translate = QtCore.QCoreApplication.translate
        Yonetici.setWindowTitle(_translate("Yonetici", "Yonetici"))
        self.label_2.setText(_translate("Yonetici", "                  Yönetici Girişi Yapmaktasınız"))
        self.label.setText(_translate("Yonetici", "Kullanıcı Adınız:"))
        self.label_3.setText(_translate("Yonetici", "Şifreniz:         "))
        self.pushButtonYGiris.setText(_translate("Yonetici", "Giriş"))
        self.pushButtonYeniSoru.setText(_translate("Yonetici", "Soru Ekle"))
        self.pushButtonYeniSalon.setText(_translate("Yonetici", "Yeni Salon Ekle"))
        self.pushButtonKitapcikOlustur.setText(_translate("Yonetici", " Kitapçık Oluştur"))
        self.pushButton1MailYolla.setText(_translate("Yonetici", "Sınava 1 Ay Kaldıysa Tüm Öğretmenlere Mail Yolla"))
        self.pushButtonYerlestir.setText(_translate("Yonetici", "Öğretmenlerin Yerleştirmesini Yap"))
        self.pushButton3Gun.setText(_translate("Yonetici", "Öğretmenlere 3 günlük kabul sırası bitti mi?"))
        self.pushButtonBaslat.setText(_translate("Yonetici", "Sınav İşlemlerini Başlat"))
        self.label_9.setText(_translate("Yonetici", "Soru:"))
        self.label_7.setText(_translate("Yonetici", "A"))
        self.label_8.setText(_translate("Yonetici", "B"))
        self.label_10.setText(_translate("Yonetici", "C"))
        self.label_12.setText(_translate("Yonetici", "D"))
        self.labelKontrol.setText(_translate("Yonetici", "Duğru Cevap:"))
        self.radioButtonA.setText(_translate("Yonetici", "A"))
        self.radioButtonA.toggled.connect(lambda:self.toggleRadio(self.radioButtonA))
        self.radioButtonB.setText(_translate("Yonetici", "B"))
        self.radioButtonA.toggled.connect(lambda:self.toggleRadio(self.radioButtonB))
        self.radioButtonC.setText(_translate("Yonetici", "C"))
        self.radioButtonA.toggled.connect(lambda:self.toggleRadio(self.radioButtonC))
        self.radioButtonD.setText(_translate("Yonetici", "D"))
        self.radioButtonA.toggled.connect(lambda:self.toggleRadio(self.radioButtonD))
        self.pushButtonBitir.setText(_translate("Yonetici", "Soruyu Ekle"))
        self.label_4.setText(_translate("Yonetici", "Salon Ekle"))
        self.label_5.setText(_translate("Yonetici", "Salondaki Kİşi sayısı:"))
        self.label_6.setText(_translate("Yonetici", "Saloun İli"))
        self.pushButtonSalonEkle.setText(_translate("Yonetici", "Ekle"))
        self.pbogrenciekle.setText(_translate("Yonetici", "Öğrenci Ekle"))
        self.pbogretmenekle.setText(_translate("Yonetici", "Öğretmen Ekle"))
        self.pbyoneticiekle.setText(_translate("Yonetici", "Yönetici Ekle"))
        self.pbogrenciyerlestir.setText(_translate("Yonetici", "Öğrencileri Yerleştir"))
        self.groupBoxGiris.setVisible(True)
        self.groupBoxSalonEkle.setVisible(False)
        self.groupBoxSoruEkle.setVisible(False)
        self.groupBoxTercih.setVisible(False)
        self.lineEditYoneticiSifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.radioButtonA.setAutoExclusive(False)
        self.radioButtonB.setAutoExclusive(False)
        self.radioButtonC.setAutoExclusive(False)
        self.radioButtonD.setAutoExclusive(False)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Yonetici = QtWidgets.QYonetici()
    ui = Ui_Yonetici()
    ui.setupUi(Yonetici)
    Yonetici.show()
    sys.exit(app.exec_())

