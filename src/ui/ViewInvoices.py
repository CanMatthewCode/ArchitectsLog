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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QLayout, QPushButton,
    QSizePolicy, QSpacerItem, QTableView, QVBoxLayout,
    QWidget)

class Ui_ViewInvoicesWindow(object):
    def setupUi(self, ViewInvoicesWindow):
        if not ViewInvoicesWindow.objectName():
            ViewInvoicesWindow.setObjectName(u"ViewInvoicesWindow")
        ViewInvoicesWindow.resize(683, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewInvoicesWindow.sizePolicy().hasHeightForWidth())
        ViewInvoicesWindow.setSizePolicy(sizePolicy)
        ViewInvoicesWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}\n"
"QComboBox{\n"
"	color: #89D5D2;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"	color: #89D5D2;\n"
"}\n"
"QHeaderView::section {\n"
"	color: white;\n"
"	background-color: #1E2E34;\n"
"	border: 1px solid black;\n"
"}\n"
"QCheckBox::indicator {\n"
"	background-color: #4F5E63;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"	width: 14px;\n"
"	height: 14px;\n"
"}\n"
"QCheckBox::indicator::checked{\n"
"	background-color: #008080;\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"	width: 14px;\n"
"	height: 14px;\n"
"}\n"
"QLineEdit{\n"
"	color: #89D5D2;\n"
"}\n"
"QDateEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QCalendarWidget QToolButton{\n"
"	color: #89D5D2;\n"
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
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.invoicesTableView.sizePolicy().hasHeightForWidth())
        self.invoicesTableView.setSizePolicy(sizePolicy1)
        self.invoicesTableView.setMinimumSize(QSize(620, 0))
        self.invoicesTableView.setStyleSheet(u"QTableView{\n"
"	color: #89D5D2;\n"
"	alternate-background-color:  #25383F;\n"
"	gridline-color: black;\n"
"}\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color: #1E2E34;\n"
"    border: 1px solid black;\n"
"}")
        self.invoicesTableView.setAlternatingRowColors(True)
        self.invoicesTableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.invoicesTableView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.showByProjectCheckBox = QCheckBox(ViewInvoicesWindow)
        self.showByProjectCheckBox.setObjectName(u"showByProjectCheckBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showByProjectCheckBox.sizePolicy().hasHeightForWidth())
        self.showByProjectCheckBox.setSizePolicy(sizePolicy2)
        self.showByProjectCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.horizontalLayout.addWidget(self.showByProjectCheckBox, 0, Qt.AlignmentFlag.AlignLeft)

        self.ProjectComboBox = QComboBox(ViewInvoicesWindow)
        self.ProjectComboBox.setObjectName(u"ProjectComboBox")
        sizePolicy2.setHeightForWidth(self.ProjectComboBox.sizePolicy().hasHeightForWidth())
        self.ProjectComboBox.setSizePolicy(sizePolicy2)
        self.ProjectComboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.ProjectComboBox)

        self.showCompletedProjectsCheckBox = QCheckBox(ViewInvoicesWindow)
        self.showCompletedProjectsCheckBox.setObjectName(u"showCompletedProjectsCheckBox")
        sizePolicy2.setHeightForWidth(self.showCompletedProjectsCheckBox.sizePolicy().hasHeightForWidth())
        self.showCompletedProjectsCheckBox.setSizePolicy(sizePolicy2)
        self.showCompletedProjectsCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.horizontalLayout.addWidget(self.showCompletedProjectsCheckBox)

        self.viewInvoicePushButton = QPushButton(ViewInvoicesWindow)
        self.viewInvoicePushButton.setObjectName(u"viewInvoicePushButton")
        sizePolicy2.setHeightForWidth(self.viewInvoicePushButton.sizePolicy().hasHeightForWidth())
        self.viewInvoicePushButton.setSizePolicy(sizePolicy2)
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

        self.horizontalLayout.addWidget(self.viewInvoicePushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ViewInvoicesWindow)

        QMetaObject.connectSlotsByName(ViewInvoicesWindow)
    # setupUi

    def retranslateUi(self, ViewInvoicesWindow):
        ViewInvoicesWindow.setWindowTitle(QCoreApplication.translate("ViewInvoicesWindow", u"Form", None))
        self.invoicesLabel.setText(QCoreApplication.translate("ViewInvoicesWindow", u"Invoices", None))
        self.showByProjectCheckBox.setText(QCoreApplication.translate("ViewInvoicesWindow", u"Display By Project", None))
        self.showCompletedProjectsCheckBox.setText(QCoreApplication.translate("ViewInvoicesWindow", u"Show Comleted Projects", None))
        self.viewInvoicePushButton.setText(QCoreApplication.translate("ViewInvoicesWindow", u"View Invoice", None))
    # retranslateUi

