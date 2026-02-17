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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

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

        self.ShowAllProjectsChkBx = QCheckBox(PhaseAveragesWindow)
        self.ShowAllProjectsChkBx.setObjectName(u"ShowAllProjectsChkBx")
        self.ShowAllProjectsChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout.addWidget(self.ShowAllProjectsChkBx)

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
        self.horizontalSpacer_3 = QSpacerItem(230, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.Show2ndProjectChkBx = QCheckBox(PhaseAveragesWindow)
        self.Show2ndProjectChkBx.setObjectName(u"Show2ndProjectChkBx")
        self.Show2ndProjectChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_2.addWidget(self.Show2ndProjectChkBx)

        self.Show3rdProjectChkBx = QCheckBox(PhaseAveragesWindow)
        self.Show3rdProjectChkBx.setObjectName(u"Show3rdProjectChkBx")
        self.Show3rdProjectChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_2.addWidget(self.Show3rdProjectChkBx)

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
"	background-color: #89D5D2;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #6FB5B2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #5A9695\n"
"}")

        self.horizontalLayout_2.addWidget(self.ProjectVsAveragesBtn)

        self.horizontalSpacer_5 = QSpacerItem(60, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.PieToBarBtn = QPushButton(PhaseAveragesWindow)
        self.PieToBarBtn.setObjectName(u"PieToBarBtn")
        sizePolicy2.setHeightForWidth(self.PieToBarBtn.sizePolicy().hasHeightForWidth())
        self.PieToBarBtn.setSizePolicy(sizePolicy2)
        self.PieToBarBtn.setMinimumSize(QSize(200, 40))
        self.PieToBarBtn.setFont(font)
        self.PieToBarBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	background-color: #89D5D2;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color: #6FB5B2;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #5A9695\n"
"}")

        self.horizontalLayout_2.addWidget(self.PieToBarBtn)

        self.horizontalSpacer_4 = QSpacerItem(370, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_6 = QSpacerItem(400, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)

        self.ChoseDateChkBx = QCheckBox(PhaseAveragesWindow)
        self.ChoseDateChkBx.setObjectName(u"ChoseDateChkBx")
        self.ChoseDateChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_3.addWidget(self.ChoseDateChkBx)

        self.StartDateEdit = QDateEdit(PhaseAveragesWindow)
        self.StartDateEdit.setObjectName(u"StartDateEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(30)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.StartDateEdit.sizePolicy().hasHeightForWidth())
        self.StartDateEdit.setSizePolicy(sizePolicy3)
        self.StartDateEdit.setStyleSheet(u"QDateEdit{\n"
"	color : #89D5D2;\n"
"}")
        self.StartDateEdit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.StartDateEdit)

        self.EndDateEdit = QDateEdit(PhaseAveragesWindow)
        self.EndDateEdit.setObjectName(u"EndDateEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(20)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.EndDateEdit.sizePolicy().hasHeightForWidth())
        self.EndDateEdit.setSizePolicy(sizePolicy4)
        self.EndDateEdit.setStyleSheet(u"QDateEdit{\n"
"	color : #89D5D2;\n"
"}")
        self.EndDateEdit.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.EndDateEdit)

        self.AvgTotalTimeChkBx = QCheckBox(PhaseAveragesWindow)
        self.AvgTotalTimeChkBx.setObjectName(u"AvgTotalTimeChkBx")
        self.AvgTotalTimeChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_3.addWidget(self.AvgTotalTimeChkBx)

        self.NonBillableTimesChkBx = QCheckBox(PhaseAveragesWindow)
        self.NonBillableTimesChkBx.setObjectName(u"NonBillableTimesChkBx")
        self.NonBillableTimesChkBx.setStyleSheet(u"QCheckBox{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout_3.addWidget(self.NonBillableTimesChkBx)

        self.horizontalSpacer_7 = QSpacerItem(550, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(PhaseAveragesWindow)

        QMetaObject.connectSlotsByName(PhaseAveragesWindow)
    # setupUi

    def retranslateUi(self, PhaseAveragesWindow):
        PhaseAveragesWindow.setWindowTitle(QCoreApplication.translate("PhaseAveragesWindow", u"Form", None))
        self.ShowAllProjectsChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Show All Projects", None))
        self.Show2ndProjectChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Add 2nd Project", None))
        self.Show3rdProjectChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Add 3rd Project", None))
        self.ProjectVsAveragesBtn.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Project Vs Averages", None))
        self.PieToBarBtn.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Pie Chart", None))
        self.ChoseDateChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Choose Date Range", None))
        self.AvgTotalTimeChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Show Total Times", None))
        self.NonBillableTimesChkBx.setText(QCoreApplication.translate("PhaseAveragesWindow", u"Hide Non-Billable Times", None))
    # retranslateUi

