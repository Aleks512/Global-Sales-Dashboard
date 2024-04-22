# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDateEdit, QGraphicsView, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QSplitter, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1508, 911)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: rgb(89, 97, 255);\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"	font: 9pt \"Arial Rounded MT Bold\";\n"
"	\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(56, 182, 240);\n"
"font: 9pt \"Arial Rounded MT Bold\";\n"
"}\n"
"")
        self.a_title_label = QLabel(self.centralwidget)
        self.a_title_label.setObjectName(u"a_title_label")
        self.a_title_label.setGeometry(QRect(580, 0, 281, 70))
        font = QFont()
        font.setFamilies([u"Arial Rounded MT Bold"])
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        self.a_title_label.setFont(font)
        self.data_tb_wgt = QTableWidget(self.centralwidget)
        if (self.data_tb_wgt.columnCount() < 9):
            self.data_tb_wgt.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.data_tb_wgt.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.data_tb_wgt.setObjectName(u"data_tb_wgt")
        self.data_tb_wgt.setGeometry(QRect(20, 440, 1161, 291))
        self.data_tb_wgt.setStyleSheet(u"gridline-color: rgb(85, 0, 127);")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(300, 140, 461, 281))
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(770, 140, 571, 281))
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gen_repport_btn = QPushButton(self.centralwidget)
        self.gen_repport_btn.setObjectName(u"gen_repport_btn")
        self.gen_repport_btn.setGeometry(QRect(770, 100, 181, 31))
        self.image_upload_btn = QPushButton(self.centralwidget)
        self.image_upload_btn.setObjectName(u"image_upload_btn")
        self.image_upload_btn.setGeometry(QRect(960, 100, 181, 31))
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(300, 110, 401, 23))
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.search_le = QLineEdit(self.splitter)
        self.search_le.setObjectName(u"search_le")
        self.splitter.addWidget(self.search_le)
        self.research_btn = QPushButton(self.splitter)
        self.research_btn.setObjectName(u"research_btn")
        self.splitter.addWidget(self.research_btn)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 140, 271, 281))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.fil_name_lb = QLabel(self.layoutWidget)
        self.fil_name_lb.setObjectName(u"fil_name_lb")

        self.gridLayout.addWidget(self.fil_name_lb, 0, 0, 1, 1)

        self.fil_name_le = QLineEdit(self.layoutWidget)
        self.fil_name_le.setObjectName(u"fil_name_le")

        self.gridLayout.addWidget(self.fil_name_le, 0, 1, 1, 1)

        self.country_lb = QLabel(self.layoutWidget)
        self.country_lb.setObjectName(u"country_lb")

        self.gridLayout.addWidget(self.country_lb, 1, 0, 1, 1)

        self.country_le = QLineEdit(self.layoutWidget)
        self.country_le.setObjectName(u"country_le")

        self.gridLayout.addWidget(self.country_le, 1, 1, 1, 1)

        self.date_lb = QLabel(self.layoutWidget)
        self.date_lb.setObjectName(u"date_lb")

        self.gridLayout.addWidget(self.date_lb, 2, 0, 1, 1)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.revenue_lb = QLabel(self.layoutWidget)
        self.revenue_lb.setObjectName(u"revenue_lb")

        self.gridLayout.addWidget(self.revenue_lb, 3, 0, 1, 1)

        self.revenue_le = QLineEdit(self.layoutWidget)
        self.revenue_le.setObjectName(u"revenue_le")

        self.gridLayout.addWidget(self.revenue_le, 3, 1, 1, 1)

        self.costs_lb = QLabel(self.layoutWidget)
        self.costs_lb.setObjectName(u"costs_lb")

        self.gridLayout.addWidget(self.costs_lb, 4, 0, 1, 1)

        self.costs_le = QLineEdit(self.layoutWidget)
        self.costs_le.setObjectName(u"costs_le")

        self.gridLayout.addWidget(self.costs_le, 4, 1, 1, 1)

        self.vol_lb = QLabel(self.layoutWidget)
        self.vol_lb.setObjectName(u"vol_lb")

        self.gridLayout.addWidget(self.vol_lb, 5, 0, 1, 1)

        self.vol_le = QLineEdit(self.layoutWidget)
        self.vol_le.setObjectName(u"vol_le")

        self.gridLayout.addWidget(self.vol_le, 5, 1, 1, 1)

        self.new_client_nr_lb = QLabel(self.layoutWidget)
        self.new_client_nr_lb.setObjectName(u"new_client_nr_lb")

        self.gridLayout.addWidget(self.new_client_nr_lb, 6, 0, 1, 1)

        self.new_client_nr_le = QLineEdit(self.layoutWidget)
        self.new_client_nr_le.setObjectName(u"new_client_nr_le")

        self.gridLayout.addWidget(self.new_client_nr_le, 6, 1, 1, 1)

        self.satisfaction_lb = QLabel(self.layoutWidget)
        self.satisfaction_lb.setObjectName(u"satisfaction_lb")

        self.gridLayout.addWidget(self.satisfaction_lb, 7, 0, 1, 1)

        self.satisfaction_le = QLineEdit(self.layoutWidget)
        self.satisfaction_le.setObjectName(u"satisfaction_le")

        self.gridLayout.addWidget(self.satisfaction_le, 7, 1, 1, 1)

        self.depense_pub_lb = QLabel(self.layoutWidget)
        self.depense_pub_lb.setObjectName(u"depense_pub_lb")

        self.gridLayout.addWidget(self.depense_pub_lb, 8, 0, 1, 1)

        self.depense_pub_le = QLineEdit(self.layoutWidget)
        self.depense_pub_le.setObjectName(u"depense_pub_le")

        self.gridLayout.addWidget(self.depense_pub_le, 8, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1210, 440, 131, 291))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.add_btn = QPushButton(self.layoutWidget1)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.add_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.update_btn = QPushButton(self.layoutWidget1)
        self.update_btn.setObjectName(u"update_btn")
        sizePolicy.setHeightForWidth(self.update_btn.sizePolicy().hasHeightForWidth())
        self.update_btn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.update_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.save_btn = QPushButton(self.layoutWidget1)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.save_btn)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.delete_btn = QPushButton(self.layoutWidget1)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.delete_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1508, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.a_title_label.setText(QCoreApplication.translate("MainWindow", u"Global Sales Dashboard - Super Entreprise", None))
        ___qtablewidgetitem = self.data_tb_wgt.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nom de la Filiale", None));
        ___qtablewidgetitem1 = self.data_tb_wgt.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Pays", None));
        ___qtablewidgetitem2 = self.data_tb_wgt.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem3 = self.data_tb_wgt.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Revenus Mensuels (\u20ac)", None));
        ___qtablewidgetitem4 = self.data_tb_wgt.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Co\u00fbts Mensuels (\u20ac)", None));
        ___qtablewidgetitem5 = self.data_tb_wgt.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Volume des Ventes", None));
        ___qtablewidgetitem6 = self.data_tb_wgt.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Nouveaux Clients", None));
        ___qtablewidgetitem7 = self.data_tb_wgt.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Taux de Satisfaction (%)", None));
        ___qtablewidgetitem8 = self.data_tb_wgt.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"D\u00e9penses Publicitaires (\u20ac)", None));
        self.gen_repport_btn.setText(QCoreApplication.translate("MainWindow", u"Generer les rapports", None))
        self.image_upload_btn.setText(QCoreApplication.translate("MainWindow", u"Charger images", None))
        self.research_btn.setText(QCoreApplication.translate("MainWindow", u"Rechercher", None))
        self.fil_name_lb.setText(QCoreApplication.translate("MainWindow", u"Nom de filiale", None))
        self.country_lb.setText(QCoreApplication.translate("MainWindow", u"Pays ", None))
        self.date_lb.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.revenue_lb.setText(QCoreApplication.translate("MainWindow", u"Revenus mens.", None))
        self.costs_lb.setText(QCoreApplication.translate("MainWindow", u"Co\u00fbts mensuels", None))
        self.vol_lb.setText(QCoreApplication.translate("MainWindow", u"Volume ventes ", None))
        self.new_client_nr_lb.setText(QCoreApplication.translate("MainWindow", u"Nouv. clients", None))
        self.satisfaction_lb.setText(QCoreApplication.translate("MainWindow", u"Satisfaction % ", None))
        self.depense_pub_lb.setText(QCoreApplication.translate("MainWindow", u"D\u00e9p. publicit\u00e9", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.update_btn.setText(QCoreApplication.translate("MainWindow", u"Modifier la ligne", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Sauvgarder", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer la ligne", None))
    # retranslateUi

