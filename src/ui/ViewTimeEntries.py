# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewTimeEntries.ui'
##
## Created by: Qt User Interface Compiler version 6.9.3
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHeaderView, QLabel,
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_ViewTimeEntriesWindow(object):
    def setupUi(self, ViewTimeEntriesWindow):
        if not ViewTimeEntriesWindow.objectName():
            ViewTimeEntriesWindow.setObjectName(u"ViewTimeEntriesWindow")
        ViewTimeEntriesWindow.resize(1124, 461)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewTimeEntriesWindow.sizePolicy().hasHeightForWidth())
        ViewTimeEntriesWindow.setSizePolicy(sizePolicy)
        ViewTimeEntriesWindow.setMinimumSize(QSize(1000, 450))
        ViewTimeEntriesWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ViewTimeEntriesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainTitle = QLabel(ViewTimeEntriesWindow)
        self.MainTitle.setObjectName(u"MainTitle")
        self.MainTitle.setMinimumSize(QSize(550, 60))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.MainTitle.setFont(font)
        self.MainTitle.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")
        self.MainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.MainTitle)

        self.hideInvoicedCheckBox = QCheckBox(ViewTimeEntriesWindow)
        self.hideInvoicedCheckBox.setObjectName(u"hideInvoicedCheckBox")
        self.hideInvoicedCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.hideInvoicedCheckBox, 0, Qt.AlignmentFlag.AlignRight)

        self.timeEntriesTableView = QTableView(ViewTimeEntriesWindow)
        self.timeEntriesTableView.setObjectName(u"timeEntriesTableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeEntriesTableView.sizePolicy().hasHeightForWidth())
        self.timeEntriesTableView.setSizePolicy(sizePolicy1)
        self.timeEntriesTableView.setMinimumSize(QSize(1100, 0))
        self.timeEntriesTableView.setStyleSheet(u"QTableView{\n"
"	color: #89D5D2;\n"
"}")
        self.timeEntriesTableView.setAlternatingRowColors(False)

        self.verticalLayout.addWidget(self.timeEntriesTableView)


        self.retranslateUi(ViewTimeEntriesWindow)

        QMetaObject.connectSlotsByName(ViewTimeEntriesWindow)
    # setupUi

    def retranslateUi(self, ViewTimeEntriesWindow):
        ViewTimeEntriesWindow.setWindowTitle(QCoreApplication.translate("ViewTimeEntriesWindow", u"Form", None))
        self.MainTitle.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Time Logs", None))
        self.hideInvoicedCheckBox.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Hide Invoiced", None))
    # retranslateUi

