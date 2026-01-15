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
from PySide6.QtWidgets import (QApplication, QHeaderView, QLabel, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

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

        self.invoicesTableView = QTableView(ViewInvoicesWindow)
        self.invoicesTableView.setObjectName(u"invoicesTableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.invoicesTableView.sizePolicy().hasHeightForWidth())
        self.invoicesTableView.setSizePolicy(sizePolicy)
        self.invoicesTableView.setMinimumSize(QSize(610, 0))

        self.verticalLayout.addWidget(self.invoicesTableView)


        self.retranslateUi(ViewInvoicesWindow)

        QMetaObject.connectSlotsByName(ViewInvoicesWindow)
    # setupUi

    def retranslateUi(self, ViewInvoicesWindow):
        ViewInvoicesWindow.setWindowTitle(QCoreApplication.translate("ViewInvoicesWindow", u"Form", None))
        self.invoicesLabel.setText(QCoreApplication.translate("ViewInvoicesWindow", u"Invoices", None))
    # retranslateUi

