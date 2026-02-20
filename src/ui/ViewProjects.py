# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewProjects.ui'
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

class Ui_ViewProjectsWindow(object):
    def setupUi(self, ViewProjectsWindow):
        if not ViewProjectsWindow.objectName():
            ViewProjectsWindow.setObjectName(u"ViewProjectsWindow")
        ViewProjectsWindow.resize(1100, 550)
        ViewProjectsWindow.setMinimumSize(QSize(1100, 450))
        ViewProjectsWindow.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ViewProjectsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.projectsLabel = QLabel(ViewProjectsWindow)
        self.projectsLabel.setObjectName(u"projectsLabel")
        self.projectsLabel.setMinimumSize(QSize(550, 60))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.projectsLabel.setFont(font)
        self.projectsLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")
        self.projectsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.projectsLabel)

        self.showProjectCheckBox = QCheckBox(ViewProjectsWindow)
        self.showProjectCheckBox.setObjectName(u"showProjectCheckBox")
        self.showProjectCheckBox.setStyleSheet(u"QCheckBox{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.showProjectCheckBox, 0, Qt.AlignmentFlag.AlignRight)

        self.projectsTableView = QTableView(ViewProjectsWindow)
        self.projectsTableView.setObjectName(u"projectsTableView")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projectsTableView.sizePolicy().hasHeightForWidth())
        self.projectsTableView.setSizePolicy(sizePolicy)
        self.projectsTableView.setMinimumSize(QSize(1050, 0))
        self.projectsTableView.setStyleSheet(u"QTableView{\n"
"	color: #89D5D2;\n"
"}")
        self.projectsTableView.setAlternatingRowColors(True)
        self.projectsTableView.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.projectsTableView)


        self.retranslateUi(ViewProjectsWindow)

        QMetaObject.connectSlotsByName(ViewProjectsWindow)
    # setupUi

    def retranslateUi(self, ViewProjectsWindow):
        ViewProjectsWindow.setWindowTitle(QCoreApplication.translate("ViewProjectsWindow", u"Form", None))
        self.projectsLabel.setText(QCoreApplication.translate("ViewProjectsWindow", u"Projects", None))
        self.showProjectCheckBox.setText(QCoreApplication.translate("ViewProjectsWindow", u"Show Completed / Change Status", None))
    # retranslateUi

