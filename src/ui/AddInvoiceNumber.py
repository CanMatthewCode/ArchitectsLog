# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddInvoiceNumber.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddInvoiceDialog(object):
    def setupUi(self, AddInvoiceDialog):
        if not AddInvoiceDialog.objectName():
            AddInvoiceDialog.setObjectName(u"AddInvoiceDialog")
        AddInvoiceDialog.resize(308, 149)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddInvoiceDialog.sizePolicy().hasHeightForWidth())
        AddInvoiceDialog.setSizePolicy(sizePolicy)
        AddInvoiceDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}\n"
"QLineEdit{\n"
"	color: #89D5D2;\n"
"}")
        self.verticalLayout = QVBoxLayout(AddInvoiceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.addInvoiceLabel = QLabel(AddInvoiceDialog)
        self.addInvoiceLabel.setObjectName(u"addInvoiceLabel")
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        self.addInvoiceLabel.setFont(font)
        self.addInvoiceLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")

        self.verticalLayout.addWidget(self.addInvoiceLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.addInvoiceLineEdit = QLineEdit(AddInvoiceDialog)
        self.addInvoiceLineEdit.setObjectName(u"addInvoiceLineEdit")

        self.verticalLayout.addWidget(self.addInvoiceLineEdit)

        self.addinvoiceButtonBox = QDialogButtonBox(AddInvoiceDialog)
        self.addinvoiceButtonBox.setObjectName(u"addinvoiceButtonBox")
        self.addinvoiceButtonBox.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	border-style: solid;\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
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
        self.addinvoiceButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.addinvoiceButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.addinvoiceButtonBox)


        self.retranslateUi(AddInvoiceDialog)
        self.addinvoiceButtonBox.accepted.connect(AddInvoiceDialog.accept)
        self.addinvoiceButtonBox.rejected.connect(AddInvoiceDialog.reject)

        QMetaObject.connectSlotsByName(AddInvoiceDialog)
    # setupUi

    def retranslateUi(self, AddInvoiceDialog):
        AddInvoiceDialog.setWindowTitle(QCoreApplication.translate("AddInvoiceDialog", u"Dialog", None))
        self.addInvoiceLabel.setText(QCoreApplication.translate("AddInvoiceDialog", u"Add Invoice Number", None))
    # retranslateUi

