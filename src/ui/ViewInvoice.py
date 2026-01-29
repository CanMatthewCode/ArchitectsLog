# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewInvoice.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_ViewInvoiceWindow(object):
    def setupUi(self, ViewInvoiceWindow):
        if not ViewInvoiceWindow.objectName():
            ViewInvoiceWindow.setObjectName(u"ViewInvoiceWindow")
        ViewInvoiceWindow.resize(1020, 466)
        ViewInvoiceWindow.setMinimumSize(QSize(900, 400))
        ViewInvoiceWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(ViewInvoiceWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.invoiceNumberLayout = QHBoxLayout()
        self.invoiceNumberLayout.setObjectName(u"invoiceNumberLayout")
        self.horizontalSpacer_2 = QSpacerItem(270, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.invoiceNumberLayout.addItem(self.horizontalSpacer_2)

        self.invoiceNumberLabel = QLabel(ViewInvoiceWindow)
        self.invoiceNumberLabel.setObjectName(u"invoiceNumberLabel")
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(False)
        self.invoiceNumberLabel.setFont(font)
        self.invoiceNumberLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")

        self.invoiceNumberLayout.addWidget(self.invoiceNumberLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.addInvoiceNumberLabel = QLabel(ViewInvoiceWindow)
        self.addInvoiceNumberLabel.setObjectName(u"addInvoiceNumberLabel")
        font1 = QFont()
        font1.setPointSize(48)
        font1.setBold(True)
        self.addInvoiceNumberLabel.setFont(font1)
        self.addInvoiceNumberLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")

        self.invoiceNumberLayout.addWidget(self.addInvoiceNumberLabel)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.invoiceNumberLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.invoiceNumberLayout)

        self.projectNameLabel = QLabel(ViewInvoiceWindow)
        self.projectNameLabel.setObjectName(u"projectNameLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(150)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectNameLabel.sizePolicy().hasHeightForWidth())
        self.projectNameLabel.setSizePolicy(sizePolicy)
        self.projectNameLabel.setMinimumSize(QSize(350, 0))
        font2 = QFont()
        font2.setPointSize(24)
        self.projectNameLabel.setFont(font2)
        self.projectNameLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.projectNameLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(10, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.invoiceTableView = QTableView(ViewInvoiceWindow)
        self.invoiceTableView.setObjectName(u"invoiceTableView")
        self.invoiceTableView.setAlternatingRowColors(True)

        self.verticalLayout.addWidget(self.invoiceTableView)

        self.invoiceTotalLayout = QHBoxLayout()
        self.invoiceTotalLayout.setObjectName(u"invoiceTotalLayout")
        self.horizontalSpacer_3 = QSpacerItem(1000, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.invoiceTotalLayout.addItem(self.horizontalSpacer_3)

        self.totalHoursLabel = QLabel(ViewInvoiceWindow)
        self.totalHoursLabel.setObjectName(u"totalHoursLabel")
        self.totalHoursLabel.setFont(font2)
        self.totalHoursLabel.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.totalHoursLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")
        self.totalHoursLabel.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.invoiceTotalLayout.addWidget(self.totalHoursLabel, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.addTotalHoursLabel = QLabel(ViewInvoiceWindow)
        self.addTotalHoursLabel.setObjectName(u"addTotalHoursLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(100)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.addTotalHoursLabel.sizePolicy().hasHeightForWidth())
        self.addTotalHoursLabel.setSizePolicy(sizePolicy1)
        self.addTotalHoursLabel.setMinimumSize(QSize(100, 0))
        self.addTotalHoursLabel.setFont(font2)
        self.addTotalHoursLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.invoiceTotalLayout.addWidget(self.addTotalHoursLabel)


        self.verticalLayout.addLayout(self.invoiceTotalLayout)


        self.retranslateUi(ViewInvoiceWindow)

        QMetaObject.connectSlotsByName(ViewInvoiceWindow)
    # setupUi

    def retranslateUi(self, ViewInvoiceWindow):
        ViewInvoiceWindow.setWindowTitle(QCoreApplication.translate("ViewInvoiceWindow", u"Form", None))
        self.invoiceNumberLabel.setText(QCoreApplication.translate("ViewInvoiceWindow", u"Invoice Number", None))
        self.addInvoiceNumberLabel.setText("")
        self.projectNameLabel.setText("")
        self.totalHoursLabel.setText(QCoreApplication.translate("ViewInvoiceWindow", u"Total Time: ", None))
        self.addTotalHoursLabel.setText("")
    # retranslateUi

