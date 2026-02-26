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

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.selectDateRangeLabel = QLabel(ProjectsOverTimeWindow)
        self.selectDateRangeLabel.setObjectName(u"selectDateRangeLabel")
        self.selectDateRangeLabel.setMinimumSize(QSize(120, 0))
        self.selectDateRangeLabel.setStyleSheet(u"QLabel{\n"
"	color : #89D5D2;\n"
"}")

        self.horizontalLayout.addWidget(self.selectDateRangeLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

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

        self.horizontalLayout.addWidget(self.StartDateEdit)

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
        self.EndDateEdit.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.EndDateEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ProjectsOverTimeWindow)

        QMetaObject.connectSlotsByName(ProjectsOverTimeWindow)
    # setupUi

    def retranslateUi(self, ProjectsOverTimeWindow):
        ProjectsOverTimeWindow.setWindowTitle(QCoreApplication.translate("ProjectsOverTimeWindow", u"Form", None))
        self.selectDateRangeLabel.setText(QCoreApplication.translate("ProjectsOverTimeWindow", u"Select Date Range", None))
    # retranslateUi

