# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Analytics.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from architectsLog_analytics import AnalyticsChartDesigner

class Ui_AnalyticsWindow(object):
    def setupUi(self, AnalyticsWindow):
        if not AnalyticsWindow.objectName():
            AnalyticsWindow.setObjectName(u"AnalyticsWindow")
        AnalyticsWindow.resize(2000, 1200)
        AnalyticsWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(AnalyticsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.analyticsLabel = QLabel(AnalyticsWindow)
        self.analyticsLabel.setObjectName(u"analyticsLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.analyticsLabel.sizePolicy().hasHeightForWidth())
        self.analyticsLabel.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(84)
        font.setBold(True)
        font.setUnderline(True)
        self.analyticsLabel.setFont(font)
        self.analyticsLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.analyticsLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.analyticsQuadWidgets = QWidget(AnalyticsWindow)
        self.analyticsQuadWidgets.setObjectName(u"analyticsQuadWidgets")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.analyticsQuadWidgets.sizePolicy().hasHeightForWidth())
        self.analyticsQuadWidgets.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.analyticsQuadWidgets)
        self.gridLayout.setObjectName(u"gridLayout")
        self.analyticsWidget1 = QWidget(self.analyticsQuadWidgets)
        self.analyticsWidget1.setObjectName(u"analyticsWidget1")
        self.verticalLayout_2 = QVBoxLayout(self.analyticsWidget1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.projectByPhaseFrame = QFrame(self.analyticsWidget1)
        self.projectByPhaseFrame.setObjectName(u"projectByPhaseFrame")
        self.projectByPhaseFrame.setStyleSheet(u"QFrame{\n"
"	background: #1E2E34;\n"
"}")
        self.projectByPhaseFrame.setFrameShape(QFrame.Shape.Panel)
        self.projectByPhaseFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.projectByPhaseFrame.setLineWidth(2)
        self.projectByPhaseFrame.setMidLineWidth(1)
        self.gridLayout_2 = QGridLayout(self.projectByPhaseFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.projectByPhaseWidget = AnalyticsChartDesigner(self.projectByPhaseFrame)
        self.projectByPhaseWidget.setObjectName(u"projectByPhaseWidget")

        self.gridLayout_2.addWidget(self.projectByPhaseWidget, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.projectByPhaseFrame)

        self.ProjectByPhaseBtn = QPushButton(self.analyticsWidget1)
        self.ProjectByPhaseBtn.setObjectName(u"ProjectByPhaseBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ProjectByPhaseBtn.sizePolicy().hasHeightForWidth())
        self.ProjectByPhaseBtn.setSizePolicy(sizePolicy2)
        self.ProjectByPhaseBtn.setMinimumSize(QSize(200, 40))
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(False)
        self.ProjectByPhaseBtn.setFont(font1)
        self.ProjectByPhaseBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_2.addWidget(self.ProjectByPhaseBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.analyticsWidget1, 0, 1, 1, 1)

        self.analyticsWidget2 = QWidget(self.analyticsQuadWidgets)
        self.analyticsWidget2.setObjectName(u"analyticsWidget2")
        self.verticalLayout_3 = QVBoxLayout(self.analyticsWidget2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.projectOverTimeFrame = QFrame(self.analyticsWidget2)
        self.projectOverTimeFrame.setObjectName(u"projectOverTimeFrame")
        self.projectOverTimeFrame.setStyleSheet(u"QFrame{\n"
"	background: #1E2E34;\n"
"}")
        self.projectOverTimeFrame.setFrameShape(QFrame.Shape.Panel)
        self.projectOverTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.projectOverTimeFrame.setLineWidth(2)
        self.projectOverTimeFrame.setMidLineWidth(1)
        self.gridLayout_3 = QGridLayout(self.projectOverTimeFrame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.projectOverTimeWidget = AnalyticsChartDesigner(self.projectOverTimeFrame)
        self.projectOverTimeWidget.setObjectName(u"projectOverTimeWidget")
        self.projectOverTimeWidget.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.projectOverTimeWidget, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.projectOverTimeFrame)

        self.ProjectOverTimeBtn = QPushButton(self.analyticsWidget2)
        self.ProjectOverTimeBtn.setObjectName(u"ProjectOverTimeBtn")
        sizePolicy2.setHeightForWidth(self.ProjectOverTimeBtn.sizePolicy().hasHeightForWidth())
        self.ProjectOverTimeBtn.setSizePolicy(sizePolicy2)
        self.ProjectOverTimeBtn.setMinimumSize(QSize(200, 40))
        font2 = QFont()
        font2.setPointSize(18)
        self.ProjectOverTimeBtn.setFont(font2)
        self.ProjectOverTimeBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_3.addWidget(self.ProjectOverTimeBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.analyticsWidget2, 0, 2, 1, 1)

        self.analyticsWidget4 = QWidget(self.analyticsQuadWidgets)
        self.analyticsWidget4.setObjectName(u"analyticsWidget4")
        self.verticalLayout_5 = QVBoxLayout(self.analyticsWidget4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.projectsOverTimeFrame = QFrame(self.analyticsWidget4)
        self.projectsOverTimeFrame.setObjectName(u"projectsOverTimeFrame")
        self.projectsOverTimeFrame.setStyleSheet(u"QFrame{\n"
"	background: #1E2E34;\n"
"}")
        self.projectsOverTimeFrame.setFrameShape(QFrame.Shape.Panel)
        self.projectsOverTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.projectsOverTimeFrame.setLineWidth(2)
        self.projectsOverTimeFrame.setMidLineWidth(1)
        self.gridLayout_5 = QGridLayout(self.projectsOverTimeFrame)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.projectsOverTimeWidget = AnalyticsChartDesigner(self.projectsOverTimeFrame)
        self.projectsOverTimeWidget.setObjectName(u"projectsOverTimeWidget")

        self.gridLayout_5.addWidget(self.projectsOverTimeWidget, 0, 0, 1, 1)


        self.verticalLayout_5.addWidget(self.projectsOverTimeFrame)

        self.ProjectsOverTimeBtn = QPushButton(self.analyticsWidget4)
        self.ProjectsOverTimeBtn.setObjectName(u"ProjectsOverTimeBtn")
        self.ProjectsOverTimeBtn.setMinimumSize(QSize(200, 40))
        self.ProjectsOverTimeBtn.setFont(font2)
        self.ProjectsOverTimeBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_5.addWidget(self.ProjectsOverTimeBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.analyticsWidget4, 1, 2, 1, 1)

        self.analyticsWidget3 = QWidget(self.analyticsQuadWidgets)
        self.analyticsWidget3.setObjectName(u"analyticsWidget3")
        self.verticalLayout_4 = QVBoxLayout(self.analyticsWidget3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.phaseAveragesFrame = QFrame(self.analyticsWidget3)
        self.phaseAveragesFrame.setObjectName(u"phaseAveragesFrame")
        self.phaseAveragesFrame.setStyleSheet(u"QFrame{\n"
"	background: #1E2E34;\n"
"}")
        self.phaseAveragesFrame.setFrameShape(QFrame.Shape.Panel)
        self.phaseAveragesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.phaseAveragesFrame.setLineWidth(2)
        self.phaseAveragesFrame.setMidLineWidth(1)
        self.gridLayout_4 = QGridLayout(self.phaseAveragesFrame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.phaseAveragesWidget = AnalyticsChartDesigner(self.phaseAveragesFrame)
        self.phaseAveragesWidget.setObjectName(u"phaseAveragesWidget")

        self.gridLayout_4.addWidget(self.phaseAveragesWidget, 0, 0, 1, 1)


        self.verticalLayout_4.addWidget(self.phaseAveragesFrame)

        self.PhaseAveragesBtn = QPushButton(self.analyticsWidget3)
        self.PhaseAveragesBtn.setObjectName(u"PhaseAveragesBtn")
        sizePolicy2.setHeightForWidth(self.PhaseAveragesBtn.sizePolicy().hasHeightForWidth())
        self.PhaseAveragesBtn.setSizePolicy(sizePolicy2)
        self.PhaseAveragesBtn.setMinimumSize(QSize(200, 40))
        self.PhaseAveragesBtn.setFont(font2)
        self.PhaseAveragesBtn.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout_4.addWidget(self.PhaseAveragesBtn, 0, Qt.AlignmentFlag.AlignHCenter)


        self.gridLayout.addWidget(self.analyticsWidget3, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.analyticsQuadWidgets)


        self.retranslateUi(AnalyticsWindow)

        QMetaObject.connectSlotsByName(AnalyticsWindow)
    # setupUi

    def retranslateUi(self, AnalyticsWindow):
        AnalyticsWindow.setWindowTitle(QCoreApplication.translate("AnalyticsWindow", u"Form", None))
        self.analyticsLabel.setText(QCoreApplication.translate("AnalyticsWindow", u"Analytics", None))
        self.ProjectByPhaseBtn.setText(QCoreApplication.translate("AnalyticsWindow", u"Project By Phase", None))
        self.ProjectOverTimeBtn.setText(QCoreApplication.translate("AnalyticsWindow", u"Project Timeline", None))
        self.ProjectsOverTimeBtn.setText(QCoreApplication.translate("AnalyticsWindow", u"Projects Over Time", None))
        self.PhaseAveragesBtn.setText(QCoreApplication.translate("AnalyticsWindow", u"Phase Averages ", None))
    # retranslateUi

