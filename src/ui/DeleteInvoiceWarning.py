# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeleteInvoiceWarning.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_DeleteInvoiceDialog(object):
    def setupUi(self, DeleteInvoiceDialog):
        if not DeleteInvoiceDialog.objectName():
            DeleteInvoiceDialog.setObjectName(u"DeleteInvoiceDialog")
        DeleteInvoiceDialog.resize(400, 150)
        DeleteInvoiceDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(DeleteInvoiceDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.invoiceDeleteLabel = QLabel(DeleteInvoiceDialog)
        self.invoiceDeleteLabel.setObjectName(u"invoiceDeleteLabel")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        self.invoiceDeleteLabel.setFont(font)
        self.invoiceDeleteLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")

        self.verticalLayout.addWidget(self.invoiceDeleteLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.invoiceDeleteWarning = QLabel(DeleteInvoiceDialog)
        self.invoiceDeleteWarning.setObjectName(u"invoiceDeleteWarning")
        self.invoiceDeleteWarning.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.invoiceDeleteWarning)

        self.invoicDeleteButtonBox = QDialogButtonBox(DeleteInvoiceDialog)
        self.invoicDeleteButtonBox.setObjectName(u"invoicDeleteButtonBox")
        self.invoicDeleteButtonBox.setStyleSheet(u"QPushButton{\n"
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
"	background-color: #2A9089;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1F6B66;\n"
"}")
        self.invoicDeleteButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.invoicDeleteButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)

        self.verticalLayout.addWidget(self.invoicDeleteButtonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(DeleteInvoiceDialog)
        self.invoicDeleteButtonBox.accepted.connect(DeleteInvoiceDialog.accept)
        self.invoicDeleteButtonBox.rejected.connect(DeleteInvoiceDialog.reject)

        QMetaObject.connectSlotsByName(DeleteInvoiceDialog)
    # setupUi

    def retranslateUi(self, DeleteInvoiceDialog):
        DeleteInvoiceDialog.setWindowTitle(QCoreApplication.translate("DeleteInvoiceDialog", u"Dialog", None))
        self.invoiceDeleteLabel.setText(QCoreApplication.translate("DeleteInvoiceDialog", u"DELELETE INVOICE?", None))
        self.invoiceDeleteWarning.setText(QCoreApplication.translate("DeleteInvoiceDialog", u"DELETED Invoices Cannot Be Recovered. Confirm DELETE:", None))
    # retranslateUi

