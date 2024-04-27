# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kpi.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QWidget)

class Ui_kpi_window(object):
    def setupUi(self, kpi_window):
        if not kpi_window.objectName():
            kpi_window.setObjectName(u"kpi_window")
        kpi_window.resize(844, 869)
        self.centralwidget = QWidget(kpi_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 75, 24))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 70, 741, 51))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.revenue_label = QLabel(self.layoutWidget)
        self.revenue_label.setObjectName(u"revenue_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.revenue_label.sizePolicy().hasHeightForWidth())
        self.revenue_label.setSizePolicy(sizePolicy)
        self.revenue_label.setStyleSheet(u"background-color: rgb(255, 101, 209);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.revenue_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.costs_label = QLabel(self.layoutWidget)
        self.costs_label.setObjectName(u"costs_label")
        sizePolicy.setHeightForWidth(self.costs_label.sizePolicy().hasHeightForWidth())
        self.costs_label.setSizePolicy(sizePolicy)
        self.costs_label.setStyleSheet(u"background-color: rgb(0, 255, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.costs_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setStyleSheet(u"background-color: rgb(0, 85, 255);\n"
"font: 700 12pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")

        self.horizontalLayout.addWidget(self.label_3)

        self.country_wdg = QWidget(self.centralwidget)
        self.country_wdg.setObjectName(u"country_wdg")
        self.country_wdg.setGeometry(QRect(40, 190, 341, 611))
        self.date_wdg = QWidget(self.centralwidget)
        self.date_wdg.setObjectName(u"date_wdg")
        self.date_wdg.setGeometry(QRect(400, 190, 441, 611))
        kpi_window.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(kpi_window)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 33))
        kpi_window.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(kpi_window)
        self.statusbar.setObjectName(u"statusbar")
        kpi_window.setStatusBar(self.statusbar)

        self.retranslateUi(kpi_window)

        QMetaObject.connectSlotsByName(kpi_window)
    # setupUi

    def retranslateUi(self, kpi_window):
        kpi_window.setWindowTitle(QCoreApplication.translate("kpi_window", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("kpi_window", u"PDF", None))
        self.revenue_label.setText(QCoreApplication.translate("kpi_window", u"TextLabel", None))
        self.costs_label.setText(QCoreApplication.translate("kpi_window", u"costs_label", None))
        self.label_3.setText(QCoreApplication.translate("kpi_window", u"TextLabel", None))
    # retranslateUi

