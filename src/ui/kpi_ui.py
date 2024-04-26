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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_kpi_window(object):
    def setupUi(self, kpi_window):
        if not kpi_window.objectName():
            kpi_window.setObjectName(u"kpi_window")
        kpi_window.resize(844, 869)
        self.centralwidget = QWidget(kpi_window)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 20, 75, 24))
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
    # retranslateUi

