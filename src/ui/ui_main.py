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
from PySide6.QtWidgets import (QApplication, QDateEdit, QFrame, QGraphicsView,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1499, 903)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
" \n"
"qconicalgradient(cx:0.486, cy:0.505682, angle:0, stop:0.86758 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
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
        self.a_title_label.setGeometry(QRect(10, 10, 731, 70))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(22)
        font.setBold(False)
        font.setItalic(False)
        self.a_title_label.setFont(font)
        self.a_title_label.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"background-color: qlineargradient(spread:pad, x1:0.242342, y1:0.699, x2:1, y2:1, stop:0.155251 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));")
        self.a_title_label.setFrameShape(QFrame.Shape.StyledPanel)
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
        self.data_tb_wgt.setGeometry(QRect(20, 440, 1061, 321))
        self.data_tb_wgt.setStyleSheet(u"gridline-color: rgb(85, 0, 127);")
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(290, 100, 461, 281))
        self.graphicsView.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.graphicsView_2 = QGraphicsView(self.centralwidget)
        self.graphicsView_2.setObjectName(u"graphicsView_2")
        self.graphicsView_2.setGeometry(QRect(760, 100, 571, 281))
        self.graphicsView_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 100, 271, 281))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.costs_lb = QLabel(self.layoutWidget)
        self.costs_lb.setObjectName(u"costs_lb")

        self.gridLayout.addWidget(self.costs_lb, 4, 0, 1, 1)

        self.fil_name_lb = QLabel(self.layoutWidget)
        self.fil_name_lb.setObjectName(u"fil_name_lb")

        self.gridLayout.addWidget(self.fil_name_lb, 0, 0, 1, 1)

        self.country_lb = QLabel(self.layoutWidget)
        self.country_lb.setObjectName(u"country_lb")

        self.gridLayout.addWidget(self.country_lb, 1, 0, 1, 1)

        self.new_client_nr_lb = QLabel(self.layoutWidget)
        self.new_client_nr_lb.setObjectName(u"new_client_nr_lb")

        self.gridLayout.addWidget(self.new_client_nr_lb, 6, 0, 1, 1)

        self.satisfaction_le = QLineEdit(self.layoutWidget)
        self.satisfaction_le.setObjectName(u"satisfaction_le")

        self.gridLayout.addWidget(self.satisfaction_le, 7, 1, 1, 1)

        self.new_client_nr_le = QLineEdit(self.layoutWidget)
        self.new_client_nr_le.setObjectName(u"new_client_nr_le")

        self.gridLayout.addWidget(self.new_client_nr_le, 6, 1, 1, 1)

        self.vol_le = QLineEdit(self.layoutWidget)
        self.vol_le.setObjectName(u"vol_le")

        self.gridLayout.addWidget(self.vol_le, 5, 1, 1, 1)

        self.vol_lb = QLabel(self.layoutWidget)
        self.vol_lb.setObjectName(u"vol_lb")

        self.gridLayout.addWidget(self.vol_lb, 5, 0, 1, 1)

        self.satisfaction_lb = QLabel(self.layoutWidget)
        self.satisfaction_lb.setObjectName(u"satisfaction_lb")

        self.gridLayout.addWidget(self.satisfaction_lb, 7, 0, 1, 1)

        self.country_le = QLineEdit(self.layoutWidget)
        self.country_le.setObjectName(u"country_le")

        self.gridLayout.addWidget(self.country_le, 1, 1, 1, 1)

        self.fil_name_le = QLineEdit(self.layoutWidget)
        self.fil_name_le.setObjectName(u"fil_name_le")

        self.gridLayout.addWidget(self.fil_name_le, 0, 1, 1, 1)

        self.revenue_lb = QLabel(self.layoutWidget)
        self.revenue_lb.setObjectName(u"revenue_lb")

        self.gridLayout.addWidget(self.revenue_lb, 3, 0, 1, 1)

        self.date_lb = QLabel(self.layoutWidget)
        self.date_lb.setObjectName(u"date_lb")

        self.gridLayout.addWidget(self.date_lb, 2, 0, 1, 1)

        self.depense_pub_lb = QLabel(self.layoutWidget)
        self.depense_pub_lb.setObjectName(u"depense_pub_lb")

        self.gridLayout.addWidget(self.depense_pub_lb, 8, 0, 1, 1)

        self.dateEdit = QDateEdit(self.layoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 2, 1, 1, 1)

        self.depense_pub_le = QLineEdit(self.layoutWidget)
        self.depense_pub_le.setObjectName(u"depense_pub_le")

        self.gridLayout.addWidget(self.depense_pub_le, 8, 1, 1, 1)

        self.costs_le = QLineEdit(self.layoutWidget)
        self.costs_le.setObjectName(u"costs_le")

        self.gridLayout.addWidget(self.costs_le, 4, 1, 1, 1)

        self.revenue_le = QLineEdit(self.layoutWidget)
        self.revenue_le.setObjectName(u"revenue_le")

        self.gridLayout.addWidget(self.revenue_le, 3, 1, 1, 1)

        self.add_btn = QPushButton(self.layoutWidget)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.add_btn, 9, 1, 1, 1)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(1100, 470, 221, 291))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
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

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.gen_repport_btn = QPushButton(self.layoutWidget1)
        self.gen_repport_btn.setObjectName(u"gen_repport_btn")
        sizePolicy.setHeightForWidth(self.gen_repport_btn.sizePolicy().hasHeightForWidth())
        self.gen_repport_btn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.gen_repport_btn)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.image_upload_btn = QPushButton(self.layoutWidget1)
        self.image_upload_btn.setObjectName(u"image_upload_btn")
        sizePolicy.setHeightForWidth(self.image_upload_btn.sizePolicy().hasHeightForWidth())
        self.image_upload_btn.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.image_upload_btn)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(760, 10, 571, 74))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"border:none;")

        self.verticalLayout_4.addWidget(self.label_5)

        self.revenue_lb_2 = QLabel(self.layoutWidget2)
        self.revenue_lb_2.setObjectName(u"revenue_lb_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.revenue_lb_2.sizePolicy().hasHeightForWidth())
        self.revenue_lb_2.setSizePolicy(sizePolicy1)
        self.revenue_lb_2.setStyleSheet(u"background-color: rgb(100, 255, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border: none;")

        self.verticalLayout_4.addWidget(self.revenue_lb_2)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.horizontalSpacer = QSpacerItem(15, 20, QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.layoutWidget2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"border:none;")

        self.verticalLayout_3.addWidget(self.label_3)

        self.costs_lb_2 = QLabel(self.layoutWidget2)
        self.costs_lb_2.setObjectName(u"costs_lb_2")
        sizePolicy1.setHeightForWidth(self.costs_lb_2.sizePolicy().hasHeightForWidth())
        self.costs_lb_2.setSizePolicy(sizePolicy1)
        self.costs_lb_2.setStyleSheet(u"background-color: rgb(200, 255, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border: none;")

        self.verticalLayout_3.addWidget(self.costs_lb_2)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.layoutWidget2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"border:none;")

        self.verticalLayout_2.addWidget(self.label)

        self.income_lb = QLabel(self.layoutWidget2)
        self.income_lb.setObjectName(u"income_lb")
        sizePolicy1.setHeightForWidth(self.income_lb.sizePolicy().hasHeightForWidth())
        self.income_lb.setSizePolicy(sizePolicy1)
        self.income_lb.setStyleSheet(u"background-color: rgb(255, 85, 0);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.income_lb)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.kpi_btn = QPushButton(self.centralwidget)
        self.kpi_btn.setObjectName(u"kpi_btn")
        self.kpi_btn.setGeometry(QRect(1220, 390, 111, 36))
        sizePolicy.setHeightForWidth(self.kpi_btn.sizePolicy().hasHeightForWidth())
        self.kpi_btn.setSizePolicy(sizePolicy)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1499, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.a_title_label.setText(QCoreApplication.translate("MainWindow", u"Global Sales Dashboard - HAPPY PEOPLE Corp", None))
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
        self.costs_lb.setText(QCoreApplication.translate("MainWindow", u"Co\u00fbts mensuels", None))
        self.fil_name_lb.setText(QCoreApplication.translate("MainWindow", u"Nom de filiale", None))
        self.country_lb.setText(QCoreApplication.translate("MainWindow", u"Pays ", None))
        self.new_client_nr_lb.setText(QCoreApplication.translate("MainWindow", u"Nouv. clients", None))
        self.vol_lb.setText(QCoreApplication.translate("MainWindow", u"Volume ventes ", None))
        self.satisfaction_lb.setText(QCoreApplication.translate("MainWindow", u"Satisfaction % ", None))
        self.revenue_lb.setText(QCoreApplication.translate("MainWindow", u"Revenus mens.", None))
        self.date_lb.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.depense_pub_lb.setText(QCoreApplication.translate("MainWindow", u"D\u00e9p. publicit\u00e9", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Sauvgarder", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Supprimer la ligne", None))
        self.gen_repport_btn.setText(QCoreApplication.translate("MainWindow", u"Generer les rapports", None))
        self.image_upload_btn.setText(QCoreApplication.translate("MainWindow", u"Charger images", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Revenue in K\u20ac", None))
        self.revenue_lb_2.setText(QCoreApplication.translate("MainWindow", u"Lorem", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Costs in k\u20ac\u00a9", None))
        self.costs_lb_2.setText(QCoreApplication.translate("MainWindow", u"Lorem", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Income in K\u20ac", None))
        self.income_lb.setText(QCoreApplication.translate("MainWindow", u"Lorem", None))
        self.kpi_btn.setText(QCoreApplication.translate("MainWindow", u"KPI ->", None))
    # retranslateUi

