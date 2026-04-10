# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProjectsOverTime.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from architectsLog_analytics import AnalyticsChartDesigner

class Ui_ProjectsOverTimeWindow(object):
    def setupUi(self, ProjectsOverTimeWindow):
        if not ProjectsOverTimeWindow.objectName():
            ProjectsOverTimeWindow.setObjectName(u"ProjectsOverTimeWindow")
        ProjectsOverTimeWindow.resize(1390, 983)
        ProjectsOverTimeWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ProjectsOverTimeWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectsOverTimeFrame = QFrame(ProjectsOverTimeWindow)
        self.projectsOverTimeFrame.setObjectName(u"projectsOverTimeFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectsOverTimeFrame.sizePolicy().hasHeightForWidth())
        self.projectsOverTimeFrame.setSizePolicy(sizePolicy)
        self.projectsOverTimeFrame.setFrameShape(QFrame.Shape.Panel)
        self.projectsOverTimeFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.projectsOverTimeFrame.setLineWidth(2)
        self.projectsOverTimeFrame.setMidLineWidth(1)
        self.gridLayout = QGridLayout(self.projectsOverTimeFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ProjectsOverTimeWidget = AnalyticsChartDesigner(self.projectsOverTimeFrame)
        self.ProjectsOverTimeWidget.setObjectName(u"ProjectsOverTimeWidget")

        self.gridLayout.addWidget(self.ProjectsOverTimeWidget, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.projectsOverTimeFrame)

        self.totalTimeLayout = QHBoxLayout()
        self.totalTimeLayout.setObjectName(u"totalTimeLayout")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.totalTimeLayout.addItem(self.horizontalSpacer_3)

        self.totalTimeLabel = QLabel(ProjectsOverTimeWindow)
        self.totalTimeLabel.setObjectName(u"totalTimeLabel")
        font = QFont()
        font.setPointSize(18)
        self.totalTimeLabel.setFont(font)
        self.totalTimeLabel.setStyleSheet(u"QLabel{\n"
"	color : #89D5D2;\n"
"}")

        self.totalTimeLayout.addWidget(self.totalTimeLabel, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)

        self.totalTimeValueLabel = QLabel(ProjectsOverTimeWindow)
        self.totalTimeValueLabel.setObjectName(u"totalTimeValueLabel")
        self.totalTimeValueLabel.setFont(font)
        self.totalTimeValueLabel.setStyleSheet(u"QLabel{\n"
"	color : #89D5D2;\n"
"}")

        self.totalTimeLayout.addWidget(self.totalTimeValueLabel, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.totalTimeLayout.addItem(self.horizontalSpacer_4)


        self.verticalLayout.addLayout(self.totalTimeLayout)

        self.dateRangeLayout = QHBoxLayout()
        self.dateRangeLayout.setObjectName(u"dateRangeLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.dateRangeLayout.addItem(self.horizontalSpacer)

        self.selectDateRangeLabel = QLabel(ProjectsOverTimeWindow)
        self.selectDateRangeLabel.setObjectName(u"selectDateRangeLabel")
        self.selectDateRangeLabel.setMinimumSize(QSize(120, 0))
        self.selectDateRangeLabel.setStyleSheet(u"QLabel{\n"
"	color : #89D5D2;\n"
"}")

        self.dateRangeLayout.addWidget(self.selectDateRangeLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.StartDateEdit = QDateEdit(ProjectsOverTimeWindow)
        self.StartDateEdit.setObjectName(u"StartDateEdit")
        self.StartDateEdit.setStyleSheet(u"QDateEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #1E2E34;\n"
"    color: #89D5D2;\n"
"}\n"
"QCalendarWidget QWidget {\n"
"    background-color: #1E2E34;\n"
"    color: #89D5D2;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"    selection-background-color: #4F5E63;\n"
"    selection-color: #89D5D2;\n"
"}\n"
"QCalendarWidget QHeaderView {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"}\n"
"\n"
"QCalendarWidget qt_calendar_calendarview QHeaderView::section {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"}")
        self.StartDateEdit.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.StartDateEdit.setCalendarPopup(True)

        self.dateRangeLayout.addWidget(self.StartDateEdit)

        self.EndDateEdit = QDateEdit(ProjectsOverTimeWindow)
        self.EndDateEdit.setObjectName(u"EndDateEdit")
        self.EndDateEdit.setStyleSheet(u"QDateEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QCalendarWidget QAbstractItemView {\n"
"    background-color: #1E2E34;\n"
"    color: #89D5D2;\n"
"}\n"
"QCalendarWidget QWidget {\n"
"    background-color: #1E2E34;\n"
"    color: #89D5D2;\n"
"}\n"
"\n"
"QCalendarWidget QToolButton {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"    selection-background-color: #4F5E63;\n"
"    selection-color: #89D5D2;\n"
"}\n"
"QCalendarWidget QHeaderView {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"}\n"
"\n"
"QCalendarWidget qt_calendar_calendarview QHeaderView::section {\n"
"    color: #89D5D2;\n"
"    background-color: #1E2E34;\n"
"}")
        self.EndDateEdit.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.EndDateEdit.setCalendarPopup(True)

        self.dateRangeLayout.addWidget(self.EndDateEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.dateRangeLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.dateRangeLayout)


        self.retranslateUi(ProjectsOverTimeWindow)

        QMetaObject.connectSlotsByName(ProjectsOverTimeWindow)
    # setupUi

    def retranslateUi(self, ProjectsOverTimeWindow):
        ProjectsOverTimeWindow.setWindowTitle(QCoreApplication.translate("ProjectsOverTimeWindow", u"Form", None))
        self.totalTimeLabel.setText(QCoreApplication.translate("ProjectsOverTimeWindow", u"Total Time: ", None))
        self.totalTimeValueLabel.setText("")
        self.selectDateRangeLabel.setText(QCoreApplication.translate("ProjectsOverTimeWindow", u"Select Date Range", None))
    # retranslateUi

