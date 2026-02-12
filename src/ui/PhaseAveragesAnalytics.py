# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PhaseAveragesAnalytics.ui'
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

class Ui_PhaseAveragesWindow(object):
    def setupUi(self, PhaseAveragesWindow):
        if not PhaseAveragesWindow.objectName():
            PhaseAveragesWindow.setObjectName(u"PhaseAveragesWindow")
        PhaseAveragesWindow.resize(1390, 983)
        PhaseAveragesWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(PhaseAveragesWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.phaseHoursFrame = QFrame(PhaseAveragesWindow)
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
        self.PhaseAverageWidget = AnalyticsChartDesigner(self.phaseHoursFrame)
        self.PhaseAverageWidget.setObjectName(u"PhaseAverageWidget")

        self.gridLayout.addWidget(self.PhaseAverageWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.phaseHoursFrame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(250, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.showAllProjectsChkBx = QCheckBox(PhaseAveragesWindow)
        self.showAllProjectsChkBx.setObjectName(u"showAllProjectsChkBx")
        self.showAllProjectsChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout.addWidget(self.showAllProjectsChkBx)

        self.ProjectComboBox = QComboBox(PhaseAveragesWindow)
        self.ProjectComboBox.setObjectName(u"ProjectComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.ProjectComboBox.sizePolicy().hasHeightForWidth())
        self.ProjectComboBox.setSizePolicy(sizePolicy1)
        self.ProjectComboBox.setMinimumSize(QSize(300, 30))

        self.horizontalLayout.addWidget(self.ProjectComboBox)

        self.Project2ComboBox = QComboBox(PhaseAveragesWindow)
        self.Project2ComboBox.setObjectName(u"Project2ComboBox")
        sizePolicy1.setHeightForWidth(self.Project2ComboBox.sizePolicy().hasHeightForWidth())
        self.Project2ComboBox.setSizePolicy(sizePolicy1)
        self.Project2ComboBox.setMinimumSize(QSize(300, 30))

        self.horizontalLayout.addWidget(self.Project2ComboBox)

        self.Project3ComboBox = QComboBox(PhaseAveragesWindow)
        self.Project3ComboBox.setObjectName(u"Project3ComboBox")
        sizePolicy1.setHeightForWidth(self.Project3ComboBox.sizePolicy().hasHeightForWidth())
        self.Project3ComboBox.setSizePolicy(sizePolicy1)
        self.Project3ComboBox.setMinimumSize(QSize(300, 30))

        self.horizontalLayout.addWidget(self.Project3ComboBox)

        self.horizontalSpacer_2 = QSpacerItem(285, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.show2ndProjectChkBx = QCheckBox(PhaseAveragesWindow)
        self.show2ndProjectChkBx.setObjectName(u"show2ndProjectChkBx")
        self.show2ndProjectChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_2.addWidget(self.show2ndProjectChkBx)

        self.show3rdProjectChkBx = QCheckBox(PhaseAveragesWindow)
        self.show3rdProjectChkBx.setObjectName(u"show3rdProjectChkBx")
        self.show3rdProjectChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_2.addWidget(self.show3rdProjectChkBx)

        self.ProjectVsAveragesBtn = QPushButton(PhaseAveragesWindow)
        self.ProjectVsAveragesBtn.setObjectName(u"ProjectVsAveragesBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ProjectVsAveragesBtn.sizePolicy().hasHeightForWidth())
        self.ProjectVsAveragesBtn.setSizePolicy(sizePolicy2)
        self.ProjectVsAveragesBtn.setMinimumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(18)
        self.ProjectVsAveragesBtn.setFont(font)
        self.ProjectVsAveragesBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.ProjectVsAveragesBtn)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.BarToPieBtn = QPushButton(PhaseAveragesWindow)
        self.BarToPieBtn.setObjectName(u"BarToPieBtn")
        sizePolicy2.setHeightForWidth(self.BarToPieBtn.sizePolicy().hasHeightForWidth())
        self.BarToPieBtn.setSizePolicy(sizePolicy2)
        self.BarToPieBtn.setMinimumSize(QSize(200, 40))
        self.BarToPieBtn.setFont(font)
        self.BarToPieBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout_2.addWidget(self.BarToPieBtn)

        self.horizontalSpacer_4 = QSpacerItem(400, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(PhaseAveragesWindow)

        QMetaObject.connectSlotsByName(PhaseAveragesWindow)
    # setupUi

    def retranslateUi(self, PhaseAveragesWindow):
        PhaseAveragesWindow.setWindowTitle(QCoreApplication.translate("PhaseAveragesWindow", u"Form", None))
        self.showAllProjectsChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Show All Projects", None))
        self.show2ndProjectChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Add 2nd Project", None))
        self.show3rdProjectChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Add 3rd Project", None))
        self.ProjectVsAveragesBtn.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Project Vs Averages", None))
        self.BarToPieBtn.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Pie Chart", None))
    # retranslateUi

