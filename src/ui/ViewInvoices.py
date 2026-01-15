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

class Ui_viewInvicesWinow(object):
    def setupUi(self, viewInvicesWinow):
        if not viewInvicesWinow.objectName():
            viewInvicesWinow.setObjectName(u"viewInvicesWinow")
        viewInvicesWinow.resize(1034, 450)
        viewInvicesWinow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(viewInvicesWinow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.invoicesLabel = QLabel(viewInvicesWinow)
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

        self.invoicesTableView = QTableView(viewInvicesWinow)
        self.invoicesTableView.setObjectName(u"invoicesTableView")

        self.verticalLayout.addWidget(self.invoicesTableView)


        self.retranslateUi(viewInvicesWinow)

        QMetaObject.connectSlotsByName(viewInvicesWinow)
    # setupUi

    def retranslateUi(self, viewInvicesWinow):
        viewInvicesWinow.setWindowTitle(QCoreApplication.translate("viewInvicesWinow", u"Form", None))
        self.invoicesLabel.setText(QCoreApplication.translate("viewInvicesWinow", u"Invoices", None))
    # retranslateUi

