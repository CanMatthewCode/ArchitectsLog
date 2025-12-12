# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QSpacerItem, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(907, 479)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(900, 475))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 901, 421))
        self.main_layout = QVBoxLayout(self.layoutWidget)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.MainTitle = QLabel(self.layoutWidget)
        self.MainTitle.setObjectName(u"MainTitle")
        self.MainTitle.setMinimumSize(QSize(501, 61))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.MainTitle.setFont(font)
        self.MainTitle.setStyleSheet(u"QLabel{\n"
"	color: teal;\n"
"}")
        self.MainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addWidget(self.MainTitle)

        self.project_button_layout = QHBoxLayout()
        self.project_button_layout.setObjectName(u"project_button_layout")
        self.architects_layout = QVBoxLayout()
        self.architects_layout.setObjectName(u"architects_layout")
        self.Architects = QLabel(self.layoutWidget)
        self.Architects.setObjectName(u"Architects")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.Architects.setFont(font1)
        self.Architects.setStyleSheet(u"QLabel{\n"
"\n"
"	color: #89D5D2;\n"
"}")
        self.Architects.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.architects_layout.addWidget(self.Architects)

        self.ArchitectsComboBox = QComboBox(self.layoutWidget)
        self.ArchitectsComboBox.setObjectName(u"ArchitectsComboBox")
        sizePolicy.setHeightForWidth(self.ArchitectsComboBox.sizePolicy().hasHeightForWidth())
        self.ArchitectsComboBox.setSizePolicy(sizePolicy)
        self.ArchitectsComboBox.setMinimumSize(QSize(0, 20))
        self.ArchitectsComboBox.setStyleSheet(u"QLabel{\n"
"	background-color: #89D5D2;\n"
"}")

        self.architects_layout.addWidget(self.ArchitectsComboBox, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AddArchitectBtn = QPushButton(self.layoutWidget)
        self.AddArchitectBtn.setObjectName(u"AddArchitectBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AddArchitectBtn.sizePolicy().hasHeightForWidth())
        self.AddArchitectBtn.setSizePolicy(sizePolicy1)
        self.AddArchitectBtn.setMinimumSize(QSize(200, 40))
        self.AddArchitectBtn.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(18)
        self.AddArchitectBtn.setFont(font2)
        self.AddArchitectBtn.setStyleSheet(u"QPushButton{\n"
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
        self.AddArchitectBtn.setIconSize(QSize(10, 16))

        self.architects_layout.addWidget(self.AddArchitectBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.project_button_layout.addLayout(self.architects_layout)

        self.projects_layout = QVBoxLayout()
        self.projects_layout.setObjectName(u"projects_layout")
        self.Projects = QLabel(self.layoutWidget)
        self.Projects.setObjectName(u"Projects")
        self.Projects.setFont(font1)
        self.Projects.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")
        self.Projects.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.projects_layout.addWidget(self.Projects, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ProjectsComboBox = QComboBox(self.layoutWidget)
        self.ProjectsComboBox.setObjectName(u"ProjectsComboBox")
        sizePolicy.setHeightForWidth(self.ProjectsComboBox.sizePolicy().hasHeightForWidth())
        self.ProjectsComboBox.setSizePolicy(sizePolicy)
        self.ProjectsComboBox.setMinimumSize(QSize(0, 20))

        self.projects_layout.addWidget(self.ProjectsComboBox, 0, Qt.AlignmentFlag.AlignVCenter)

        self.AddProjectBtn = QPushButton(self.layoutWidget)
        self.AddProjectBtn.setObjectName(u"AddProjectBtn")
        sizePolicy1.setHeightForWidth(self.AddProjectBtn.sizePolicy().hasHeightForWidth())
        self.AddProjectBtn.setSizePolicy(sizePolicy1)
        self.AddProjectBtn.setMinimumSize(QSize(200, 40))
        self.AddProjectBtn.setMaximumSize(QSize(16777215, 16777215))
        self.AddProjectBtn.setFont(font2)
        self.AddProjectBtn.setStyleSheet(u"QPushButton{\n"
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
        self.AddProjectBtn.setIconSize(QSize(10, 16))

        self.projects_layout.addWidget(self.AddProjectBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.project_button_layout.addLayout(self.projects_layout)

        self.phases_layout = QVBoxLayout()
        self.phases_layout.setObjectName(u"phases_layout")
        self.phases_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.ProjectPhases = QLabel(self.layoutWidget)
        self.ProjectPhases.setObjectName(u"ProjectPhases")
        self.ProjectPhases.setMaximumSize(QSize(16777215, 16777215))
        self.ProjectPhases.setFont(font1)
        self.ProjectPhases.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")
        self.ProjectPhases.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.phases_layout.addWidget(self.ProjectPhases, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.PhasesComboBox = QComboBox(self.layoutWidget)
        self.PhasesComboBox.setObjectName(u"PhasesComboBox")
        sizePolicy.setHeightForWidth(self.PhasesComboBox.sizePolicy().hasHeightForWidth())
        self.PhasesComboBox.setSizePolicy(sizePolicy)
        self.PhasesComboBox.setMinimumSize(QSize(0, 20))
        self.PhasesComboBox.setStyleSheet(u"QLabel{\n"
"	background-color: #89D5D2;\n"
"}")

        self.phases_layout.addWidget(self.PhasesComboBox)

        self.phases_vertical_spacer = QSpacerItem(200, 48, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.phases_layout.addItem(self.phases_vertical_spacer)


        self.project_button_layout.addLayout(self.phases_layout)


        self.main_layout.addLayout(self.project_button_layout)

        self.main_layout_spacer = QSpacerItem(10, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.main_layout.addItem(self.main_layout_spacer)

        self.time_button_layout = QHBoxLayout()
        self.time_button_layout.setObjectName(u"time_button_layout")
        self.left_time_spacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.time_button_layout.addItem(self.left_time_spacer)

        self.LogTimeBtn = QPushButton(self.layoutWidget)
        self.LogTimeBtn.setObjectName(u"LogTimeBtn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(20)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.LogTimeBtn.sizePolicy().hasHeightForWidth())
        self.LogTimeBtn.setSizePolicy(sizePolicy2)
        self.LogTimeBtn.setMinimumSize(QSize(200, 50))
        self.LogTimeBtn.setMaximumSize(QSize(16777215, 16777215))
        font3 = QFont()
        font3.setPointSize(24)
        self.LogTimeBtn.setFont(font3)
        self.LogTimeBtn.setStyleSheet(u"QPushButton{\n"
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
        self.LogTimeBtn.setIconSize(QSize(10, 16))

        self.time_button_layout.addWidget(self.LogTimeBtn)

        self.AddTimeBtn = QPushButton(self.layoutWidget)
        self.AddTimeBtn.setObjectName(u"AddTimeBtn")
        sizePolicy2.setHeightForWidth(self.AddTimeBtn.sizePolicy().hasHeightForWidth())
        self.AddTimeBtn.setSizePolicy(sizePolicy2)
        self.AddTimeBtn.setMinimumSize(QSize(200, 50))
        self.AddTimeBtn.setMaximumSize(QSize(16777215, 16777215))
        self.AddTimeBtn.setFont(font3)
        self.AddTimeBtn.setStyleSheet(u"QPushButton{\n"
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
        self.AddTimeBtn.setIconSize(QSize(10, 16))

        self.time_button_layout.addWidget(self.AddTimeBtn)

        self.right_time_spacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.time_button_layout.addItem(self.right_time_spacer)


        self.main_layout.addLayout(self.time_button_layout)

        self.logs_layout = QHBoxLayout()
        self.logs_layout.setObjectName(u"logs_layout")
        self.ArchitectLogsBtn = QPushButton(self.layoutWidget)
        self.ArchitectLogsBtn.setObjectName(u"ArchitectLogsBtn")
        sizePolicy.setHeightForWidth(self.ArchitectLogsBtn.sizePolicy().hasHeightForWidth())
        self.ArchitectLogsBtn.setSizePolicy(sizePolicy)
        self.ArchitectLogsBtn.setMinimumSize(QSize(150, 50))
        self.ArchitectLogsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.ArchitectLogsBtn.setFont(font2)
        self.ArchitectLogsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ArchitectLogsBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	background-color: #008080;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #006666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #004D4D;\n"
"}")
        self.ArchitectLogsBtn.setIconSize(QSize(10, 16))
        self.ArchitectLogsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.ArchitectLogsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ProjectLogsBtn = QPushButton(self.layoutWidget)
        self.ProjectLogsBtn.setObjectName(u"ProjectLogsBtn")
        sizePolicy.setHeightForWidth(self.ProjectLogsBtn.sizePolicy().hasHeightForWidth())
        self.ProjectLogsBtn.setSizePolicy(sizePolicy)
        self.ProjectLogsBtn.setMinimumSize(QSize(150, 50))
        self.ProjectLogsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.ProjectLogsBtn.setFont(font2)
        self.ProjectLogsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ProjectLogsBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	background-color: #008080;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #006666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #004D4D;\n"
"}")
        self.ProjectLogsBtn.setIconSize(QSize(10, 16))
        self.ProjectLogsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.ProjectLogsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.TimeLogsBtn = QPushButton(self.layoutWidget)
        self.TimeLogsBtn.setObjectName(u"TimeLogsBtn")
        sizePolicy.setHeightForWidth(self.TimeLogsBtn.sizePolicy().hasHeightForWidth())
        self.TimeLogsBtn.setSizePolicy(sizePolicy)
        self.TimeLogsBtn.setMinimumSize(QSize(150, 50))
        self.TimeLogsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.TimeLogsBtn.setFont(font2)
        self.TimeLogsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.TimeLogsBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	background-color: #008080;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #006666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #004D4D;\n"
"}")
        self.TimeLogsBtn.setIconSize(QSize(10, 16))
        self.TimeLogsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.TimeLogsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.InvoiceLogsBtn = QPushButton(self.layoutWidget)
        self.InvoiceLogsBtn.setObjectName(u"InvoiceLogsBtn")
        sizePolicy.setHeightForWidth(self.InvoiceLogsBtn.sizePolicy().hasHeightForWidth())
        self.InvoiceLogsBtn.setSizePolicy(sizePolicy)
        self.InvoiceLogsBtn.setMinimumSize(QSize(150, 50))
        self.InvoiceLogsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.InvoiceLogsBtn.setFont(font2)
        self.InvoiceLogsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.InvoiceLogsBtn.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	background-color: #008080;\n"
"	color: black;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #006666;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #004D4D;\n"
"}")
        self.InvoiceLogsBtn.setIconSize(QSize(10, 16))
        self.InvoiceLogsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.InvoiceLogsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.main_layout.addLayout(self.logs_layout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 907, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.MainTitle.setText(QCoreApplication.translate("MainWindow", u"The Architects Log", None))
        self.Architects.setText(QCoreApplication.translate("MainWindow", u"Architect", None))
        self.AddArchitectBtn.setText(QCoreApplication.translate("MainWindow", u"Add New Architect", None))
        self.Projects.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.AddProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Add New Project", None))
        self.ProjectPhases.setText(QCoreApplication.translate("MainWindow", u"Project Phase", None))
        self.LogTimeBtn.setText(QCoreApplication.translate("MainWindow", u"LOG TIME", None))
        self.AddTimeBtn.setText(QCoreApplication.translate("MainWindow", u"ADD TIME", None))
        self.ArchitectLogsBtn.setText(QCoreApplication.translate("MainWindow", u"View Architects", None))
        self.ProjectLogsBtn.setText(QCoreApplication.translate("MainWindow", u"View Projects", None))
        self.TimeLogsBtn.setText(QCoreApplication.translate("MainWindow", u"View Time Logs", None))
        self.InvoiceLogsBtn.setText(QCoreApplication.translate("MainWindow", u"View Invoices", None))
    # retranslateUi

