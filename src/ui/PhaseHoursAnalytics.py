# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PhaseHoursAnalytics.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from architectsLog_analytics import AnalyticsChartDesigner

class Ui_PhaseHoursWindow(object):
    def setupUi(self, PhaseHoursWindow):
        if not PhaseHoursWindow.objectName():
            PhaseHoursWindow.setObjectName(u"PhaseHoursWindow")
        PhaseHoursWindow.resize(1390, 983)
        PhaseHoursWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(PhaseHoursWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.phaseHoursFrame = QFrame(PhaseHoursWindow)
        self.phaseHoursFrame.setObjectName(u"phaseHoursFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.phaseHoursFrame.sizePolicy().hasHeightForWidth())
        self.phaseHoursFrame.setSizePolicy(sizePolicy)
        self.phaseHoursFrame.setFrameShape(QFrame.Shape.Panel)
        self.phaseHoursFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.phaseHoursFrame.setLineWidth(2)
        self.phaseHoursFrame.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.phaseHoursFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.PhaseHoursWidget = AnalyticsChartDesigner(self.phaseHoursFrame)
        self.PhaseHoursWidget.setObjectName(u"PhaseHoursWidget")

        self.gridLayout.addWidget(self.PhaseHoursWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.phaseHoursFrame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(600, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.ProjectComboBox = QComboBox(PhaseHoursWindow)
        self.ProjectComboBox.setObjectName(u"ProjectComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.ProjectComboBox.sizePolicy().hasHeightForWidth())
        self.ProjectComboBox.setSizePolicy(sizePolicy1)
        self.ProjectComboBox.setMinimumSize(QSize(300, 30))

        self.horizontalLayout.addWidget(self.ProjectComboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.showAllProjectsChkBx = QCheckBox(PhaseHoursWindow)
        self.showAllProjectsChkBx.setObjectName(u"showAllProjectsChkBx")
        self.showAllProjectsChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout.addWidget(self.showAllProjectsChkBx, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_2 = QSpacerItem(450, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.barsStemToPieStepBtn = QPushButton(PhaseHoursWindow)
        self.barsStemToPieStepBtn.setObjectName(u"barsStemToPieStepBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.barsStemToPieStepBtn.sizePolicy().hasHeightForWidth())
        self.barsStemToPieStepBtn.setSizePolicy(sizePolicy2)
        self.barsStemToPieStepBtn.setMinimumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(18)
        self.barsStemToPieStepBtn.setFont(font)
        self.barsStemToPieStepBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
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

        self.verticalLayout.addWidget(self.barsStemToPieStepBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.retranslateUi(PhaseHoursWindow)

        QMetaObject.connectSlotsByName(PhaseHoursWindow)
    # setupUi

    def retranslateUi(self, PhaseHoursWindow):
        PhaseHoursWindow.setWindowTitle(QCoreApplication.translate("PhaseHoursWindow", u"Form", None))
        self.showAllProjectsChkBx.setText(QCoreApplication.translate("PhaseHoursWindow", u"Show All Projects", None))
        self.barsStemToPieStepBtn.setText(QCoreApplication.translate("PhaseHoursWindow", u"Pie Chart", None))
    # retranslateUi

