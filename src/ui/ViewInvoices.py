# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewInvoices.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_ViewInvoicesWindow(object):
    def setupUi(self, ViewInvoicesWindow):
        if not ViewInvoicesWindow.objectName():
            ViewInvoicesWindow.setObjectName(u"ViewInvoicesWindow")
        ViewInvoicesWindow.resize(634, 450)
        ViewInvoicesWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ViewInvoicesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.invoicesLabel = QLabel(ViewInvoicesWindow)
        self.invoicesLabel.setObjectName(u"invoicesLabel")
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        self.invoicesLabel.setFont(font)
        self.invoicesLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")

        self.verticalLayout.addWidget(self.invoicesLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(10, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.invoicesTableView = QTableView(ViewInvoicesWindow)
        self.invoicesTableView.setObjectName(u"invoicesTableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoicesTableView.sizePolicy().hasHeightForWidth())
        self.invoicesTableView.setSizePolicy(sizePolicy)
        self.invoicesTableView.setMinimumSize(QSize(610, 0))
        self.invoicesTableView.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.invoicesTableView)

        self.viewInvoicePushButton = QPushButton(ViewInvoicesWindow)
        self.viewInvoicePushButton.setObjectName(u"viewInvoicePushButton")
        font1 = QFont()
        font1.setPointSize(18)
        self.viewInvoicePushButton.setFont(font1)
        self.viewInvoicePushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	border-style: solid;\n"
"	min-width: 60px;\n"
"	min-height: 30px;\n"
"	padding: 5px 10px;\n"
"	margin-left: 5px;\n"
"	margin-right: 10px;\n"
"	background-color: #008080;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #006666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #004D4D;\n"
"}")

        self.verticalLayout.addWidget(self.viewInvoicePushButton, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(ViewInvoicesWindow)

        QMetaObject.connectSlotsByName(ViewInvoicesWindow)
    # setupUi

    def retranslateUi(self, ViewInvoicesWindow):
        ViewInvoicesWindow.setWindowTitle(QCoreApplication.translate("ViewInvoicesWindow", u"Form", None))
        self.invoicesLabel.setText(QCoreApplication.translate("ViewInvoicesWindow", u"Invoices", None))
        self.viewInvoicePushButton.setText(QCoreApplication.translate("ViewInvoicesWindow", u"View Invoice", None))
    # retranslateUi

