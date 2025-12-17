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
    QSizePolicy, QTableView, QVBoxLayout, QWidget)

class Ui_ViewArchitectsWindow(object):
    def setupUi(self, ViewArchitectsWindow):
        if not ViewArchitectsWindow.objectName():
            ViewArchitectsWindow.setObjectName(u"ViewArchitectsWindow")
        ViewArchitectsWindow.resize(850, 450)
        ViewArchitectsWindow.setMinimumSize(QSize(830, 450))
        ViewArchitectsWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ViewArchitectsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainTitle = QLabel(ViewArchitectsWindow)
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

        self.hideArchitectCheckBox = QCheckBox(ViewArchitectsWindow)
        self.hideArchitectCheckBox.setObjectName(u"hideArchitectCheckBox")
        self.hideArchitectCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.hideArchitectCheckBox, 0, Qt.AlignmentFlag.AlignRight)

        self.architectsTableView = QTableView(ViewArchitectsWindow)
        self.architectsTableView.setObjectName(u"architectsTableView")
        self.architectsTableView.setMinimumSize(QSize(850, 0))
        self.architectsTableView.setStyleSheet(u"QTableView{\n"
"	color: #89D5D2;\n"
"}")
        self.architectsTableView.setAlternatingRowColors(False)

        self.verticalLayout.addWidget(self.architectsTableView)


        self.retranslateUi(ViewArchitectsWindow)

        QMetaObject.connectSlotsByName(ViewArchitectsWindow)
    # setupUi

    def retranslateUi(self, ViewArchitectsWindow):
        ViewArchitectsWindow.setWindowTitle(QCoreApplication.translate("ViewArchitectsWindow", u"Form", None))
        self.MainTitle.setText(QCoreApplication.translate("ViewArchitectsWindow", u"Architects", None))
        self.hideArchitectCheckBox.setText(QCoreApplication.translate("ViewArchitectsWindow", u"Hide Inactive", None))
    # retranslateUi

