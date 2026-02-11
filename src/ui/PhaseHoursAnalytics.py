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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

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

        self.phaseHoursComboBox = QComboBox(PhaseHoursWindow)
        self.phaseHoursComboBox.setObjectName(u"phaseHoursComboBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(200)
        sizePolicy1.setVerticalStretch(200)
        sizePolicy1.setHeightForWidth(self.phaseHoursComboBox.sizePolicy().hasHeightForWidth())
        self.phaseHoursComboBox.setSizePolicy(sizePolicy1)
        self.phaseHoursComboBox.setMinimumSize(QSize(300, 30))

        self.verticalLayout.addWidget(self.phaseHoursComboBox, 0, Qt.AlignmentFlag.AlignHCenter)

        self.barsPieBtn = QPushButton(PhaseHoursWindow)
        self.barsPieBtn.setObjectName(u"barsPieBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.barsPieBtn.sizePolicy().hasHeightForWidth())
        self.barsPieBtn.setSizePolicy(sizePolicy2)
        self.barsPieBtn.setMinimumSize(QSize(200, 40))
        font = QFont()
        font.setPointSize(18)
        self.barsPieBtn.setFont(font)

        self.verticalLayout.addWidget(self.barsPieBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(PhaseHoursWindow)

        QMetaObject.connectSlotsByName(PhaseHoursWindow)
    # setupUi

    def retranslateUi(self, PhaseHoursWindow):
        PhaseHoursWindow.setWindowTitle(QCoreApplication.translate("PhaseHoursWindow", u"Form", None))
        self.barsPieBtn.setText(QCoreApplication.translate("PhaseHoursWindow", u"Pie Chart", None))
    # retranslateUi

