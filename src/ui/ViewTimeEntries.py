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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHBoxLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QTableView, QVBoxLayout, QWidget)

class Ui_ViewTimeEntriesWindow(object):
    def setupUi(self, ViewTimeEntriesWindow):
        if not ViewTimeEntriesWindow.objectName():
            ViewTimeEntriesWindow.setObjectName(u"ViewTimeEntriesWindow")
        ViewTimeEntriesWindow.resize(1424, 650)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewTimeEntriesWindow.sizePolicy().hasHeightForWidth())
        ViewTimeEntriesWindow.setSizePolicy(sizePolicy)
        ViewTimeEntriesWindow.setMinimumSize(QSize(920, 450))
        ViewTimeEntriesWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ViewTimeEntriesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeLogsLabel = QLabel(ViewTimeEntriesWindow)
        self.timeLogsLabel.setObjectName(u"timeLogsLabel")
        self.timeLogsLabel.setMinimumSize(QSize(550, 60))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.timeLogsLabel.setFont(font)
        self.timeLogsLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")
        self.timeLogsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.timeLogsLabel)

        self.timeEntriesTableView = QTableView(ViewTimeEntriesWindow)
        self.timeEntriesTableView.setObjectName(u"timeEntriesTableView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.timeEntriesTableView.sizePolicy().hasHeightForWidth())
        self.timeEntriesTableView.setSizePolicy(sizePolicy1)
        self.timeEntriesTableView.setMinimumSize(QSize(1200, 0))
        self.timeEntriesTableView.setStyleSheet(u"QTableView{\n"
"	color: #89D5D2;\n"
"}")
        self.timeEntriesTableView.setAlternatingRowColors(True)
        self.timeEntriesTableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.timeEntriesTableView)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.showInternalsCheckBox = QCheckBox(ViewTimeEntriesWindow)
        self.showInternalsCheckBox.setObjectName(u"showInternalsCheckBox")
        self.showInternalsCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.horizontalLayout_2.addWidget(self.showInternalsCheckBox, 0, Qt.AlignmentFlag.AlignRight)

        self.showInvoicedCheckBox = QCheckBox(ViewTimeEntriesWindow)
        self.showInvoicedCheckBox.setObjectName(u"showInvoicedCheckBox")
        self.showInvoicedCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.horizontalLayout_2.addWidget(self.showInvoicedCheckBox, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.showByProjectCheckBox = QCheckBox(ViewTimeEntriesWindow)
        self.showByProjectCheckBox.setObjectName(u"showByProjectCheckBox")
        self.showByProjectCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.horizontalLayout.addWidget(self.showByProjectCheckBox)

        self.ProjectComboBox = QComboBox(ViewTimeEntriesWindow)
        self.ProjectComboBox.setObjectName(u"ProjectComboBox")
        self.ProjectComboBox.setMinimumSize(QSize(200, 0))

        self.horizontalLayout.addWidget(self.ProjectComboBox)

        self.showCompletedProjectsCheckBox = QCheckBox(ViewTimeEntriesWindow)
        self.showCompletedProjectsCheckBox.setObjectName(u"showCompletedProjectsCheckBox")
        self.showCompletedProjectsCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.horizontalLayout.addWidget(self.showCompletedProjectsCheckBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.cancelInvoiceBtn = QPushButton(ViewTimeEntriesWindow)
        self.cancelInvoiceBtn.setObjectName(u"cancelInvoiceBtn")
        font1 = QFont()
        font1.setPointSize(18)
        self.cancelInvoiceBtn.setFont(font1)
        self.cancelInvoiceBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.cancelInvoiceBtn)

        self.createInvoiceBtn = QPushButton(ViewTimeEntriesWindow)
        self.createInvoiceBtn.setObjectName(u"createInvoiceBtn")
        self.createInvoiceBtn.setFont(font1)
        self.createInvoiceBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.createInvoiceBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ViewTimeEntriesWindow)

        QMetaObject.connectSlotsByName(ViewTimeEntriesWindow)
    # setupUi

    def retranslateUi(self, ViewTimeEntriesWindow):
        ViewTimeEntriesWindow.setWindowTitle(QCoreApplication.translate("ViewTimeEntriesWindow", u"Form", None))
        self.timeLogsLabel.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Time Logs", None))
        self.showInternalsCheckBox.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Show Internal Time Logs", None))
        self.showInvoicedCheckBox.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Show Invoiced Logs", None))
        self.showByProjectCheckBox.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Display By Project", None))
        self.showCompletedProjectsCheckBox.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Show Completed Projects", None))
        self.cancelInvoiceBtn.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Cancel", None))
        self.createInvoiceBtn.setText(QCoreApplication.translate("ViewTimeEntriesWindow", u"Create Invoice", None))
    # retranslateUi

