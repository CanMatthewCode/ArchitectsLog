# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimeLogger.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLCDNumber, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_TimeLoggerWindow(object):
    def setupUi(self, TimeLoggerWindow):
        if not TimeLoggerWindow.objectName():
            TimeLoggerWindow.setObjectName(u"TimeLoggerWindow")
        TimeLoggerWindow.resize(424, 211)
        TimeLoggerWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(TimeLoggerWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timer = QLCDNumber(TimeLoggerWindow)
        self.timer.setObjectName(u"timer")
        self.timer.setMinimumSize(QSize(400, 90))
        self.timer.setStyleSheet(u"QLCDNumber{\n"
"	color: #35B5AC;\n"
"}")
        self.timer.setFrameShape(QFrame.Shape.Box)
        self.timer.setSmallDecimalPoint(False)
        self.timer.setDigitCount(8)
        self.timer.setSegmentStyle(QLCDNumber.SegmentStyle.Flat)
        self.timer.setProperty(u"intValue", 0)

        self.verticalLayout.addWidget(self.timer)

        self.input_values_layout = QHBoxLayout()
        self.input_values_layout.setObjectName(u"input_values_layout")
        self.ArchitectComboBox = QComboBox(TimeLoggerWindow)
        self.ArchitectComboBox.setObjectName(u"ArchitectComboBox")
        font = QFont()
        font.setPointSize(10)
        self.ArchitectComboBox.setFont(font)

        self.input_values_layout.addWidget(self.ArchitectComboBox)

        self.ProjectComboBox = QComboBox(TimeLoggerWindow)
        self.ProjectComboBox.setObjectName(u"ProjectComboBox")
        self.ProjectComboBox.setFont(font)

        self.input_values_layout.addWidget(self.ProjectComboBox)

        self.PhaseComboBox = QComboBox(TimeLoggerWindow)
        self.PhaseComboBox.setObjectName(u"PhaseComboBox")
        self.PhaseComboBox.setFont(font)

        self.input_values_layout.addWidget(self.PhaseComboBox)


        self.verticalLayout.addLayout(self.input_values_layout)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.setObjectName(u"buttons_layout")
        self.horizontalSpacer = QSpacerItem(180, 10, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.buttons_layout.addItem(self.horizontalSpacer)

        self.pushButton_3 = QPushButton(TimeLoggerWindow)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(80, 25))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"	background-color: #35B5AC;\n"
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

        self.buttons_layout.addWidget(self.pushButton_3, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.pushButton = QPushButton(TimeLoggerWindow)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 25))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border-radius: 4px;\n"
"	border: 1px solid black;\n"
"	background-color: #35B5AC;\n"
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

        self.buttons_layout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.buttons_layout)


        self.retranslateUi(TimeLoggerWindow)

        QMetaObject.connectSlotsByName(TimeLoggerWindow)
    # setupUi

    def retranslateUi(self, TimeLoggerWindow):
        TimeLoggerWindow.setWindowTitle(QCoreApplication.translate("TimeLoggerWindow", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("TimeLoggerWindow", u"START", None))
        self.pushButton.setText(QCoreApplication.translate("TimeLoggerWindow", u"STOP", None))
    # retranslateUi

