# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewArchitects.ui'
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
    QLayout, QSizePolicy, QTableView, QVBoxLayout,
    QWidget)

class Ui_ViewArchitectsWindow(object):
    def setupUi(self, ViewArchitectsWindow):
        if not ViewArchitectsWindow.objectName():
            ViewArchitectsWindow.setObjectName(u"ViewArchitectsWindow")
        ViewArchitectsWindow.resize(874, 450)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ViewArchitectsWindow.sizePolicy().hasHeightForWidth())
        ViewArchitectsWindow.setSizePolicy(sizePolicy)
        ViewArchitectsWindow.setMinimumSize(QSize(830, 450))
        ViewArchitectsWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color: #1E2E34;\n"
"    border: 1px solid black;\n"
"}\n"
"QLineEdit{\n"
"	color: #89D5D2;\n"
"}\n"
"QComboBox{\n"
"	color: #89D5D2;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"	color: #89D5D2;\n"
"}")
        self.verticalLayout = QVBoxLayout(ViewArchitectsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.architectsLabel = QLabel(ViewArchitectsWindow)
        self.architectsLabel.setObjectName(u"architectsLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.architectsLabel.sizePolicy().hasHeightForWidth())
        self.architectsLabel.setSizePolicy(sizePolicy1)
        self.architectsLabel.setMinimumSize(QSize(550, 60))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.architectsLabel.setFont(font)
        self.architectsLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")
        self.architectsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.architectsLabel)

        self.showArchitectCheckBox = QCheckBox(ViewArchitectsWindow)
        self.showArchitectCheckBox.setObjectName(u"showArchitectCheckBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.showArchitectCheckBox.sizePolicy().hasHeightForWidth())
        self.showArchitectCheckBox.setSizePolicy(sizePolicy2)
        self.showArchitectCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
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
"")

        self.verticalLayout.addWidget(self.showArchitectCheckBox, 0, Qt.AlignmentFlag.AlignRight)

        self.architectsTableView = QTableView(ViewArchitectsWindow)
        self.architectsTableView.setObjectName(u"architectsTableView")
        self.architectsTableView.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.architectsTableView.sizePolicy().hasHeightForWidth())
        self.architectsTableView.setSizePolicy(sizePolicy3)
        self.architectsTableView.setMinimumSize(QSize(850, 0))
        self.architectsTableView.setStyleSheet(u"QTableView{\n"
"	color: #89D5D2;\n"
"	alternate-background-color:  #25383F;\n"
"	gridline-color: black;\n"
"}\n"
"QHeaderView::section {\n"
"    color: white;\n"
"    background-color: #1E2E34;\n"
"    border: 1px solid black;\n"
"}")
        self.architectsTableView.setDragEnabled(False)
        self.architectsTableView.setAlternatingRowColors(True)
        self.architectsTableView.horizontalHeader().setCascadingSectionResizes(False)
        self.architectsTableView.horizontalHeader().setStretchLastSection(True)
        self.architectsTableView.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.architectsTableView)

        self.verticalLayout.setStretch(2, 1)

        self.retranslateUi(ViewArchitectsWindow)

        QMetaObject.connectSlotsByName(ViewArchitectsWindow)
    # setupUi

    def retranslateUi(self, ViewArchitectsWindow):
        ViewArchitectsWindow.setWindowTitle(QCoreApplication.translate("ViewArchitectsWindow", u"Form", None))
        self.architectsLabel.setText(QCoreApplication.translate("ViewArchitectsWindow", u"Architects", None))
        self.showArchitectCheckBox.setText(QCoreApplication.translate("ViewArchitectsWindow", u"Show Inactive / Change Status", None))
    # retranslateUi

