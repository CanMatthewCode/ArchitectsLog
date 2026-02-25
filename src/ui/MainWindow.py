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
        MainWindow.resize(907, 590)
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
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 6, -1, -1)
        self.theArchitectsLogLabel = QLabel(self.centralwidget)
        self.theArchitectsLogLabel.setObjectName(u"theArchitectsLogLabel")
        self.theArchitectsLogLabel.setMinimumSize(QSize(501, 61))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.theArchitectsLogLabel.setFont(font)
        self.theArchitectsLogLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")
        self.theArchitectsLogLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.theArchitectsLogLabel)

        self.project_button_layout = QHBoxLayout()
        self.project_button_layout.setObjectName(u"project_button_layout")
        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.project_button_layout.addItem(self.horizontalSpacer)

        self.architects_layout = QVBoxLayout()
        self.architects_layout.setObjectName(u"architects_layout")
        self.Architects = QLabel(self.centralwidget)
        self.Architects.setObjectName(u"Architects")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setBold(True)
        self.Architects.setFont(font1)
        self.Architects.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")
        self.Architects.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.architects_layout.addWidget(self.Architects)

        self.ArchitectsComboBox = QComboBox(self.centralwidget)
        self.ArchitectsComboBox.setObjectName(u"ArchitectsComboBox")
        sizePolicy.setHeightForWidth(self.ArchitectsComboBox.sizePolicy().hasHeightForWidth())
        self.ArchitectsComboBox.setSizePolicy(sizePolicy)
        self.ArchitectsComboBox.setMinimumSize(QSize(0, 20))
        self.ArchitectsComboBox.setStyleSheet(u"QLabel{\n"
"	background-color: #89D5D2;\n"
"}")

        self.architects_layout.addWidget(self.ArchitectsComboBox, 0, Qt.AlignmentFlag.AlignVCenter)

        self.verticalSpacer = QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.architects_layout.addItem(self.verticalSpacer)

        self.AddArchitectBtn = QPushButton(self.centralwidget)
        self.AddArchitectBtn.setObjectName(u"AddArchitectBtn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(20)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.AddArchitectBtn.sizePolicy().hasHeightForWidth())
        self.AddArchitectBtn.setSizePolicy(sizePolicy1)
        self.AddArchitectBtn.setMinimumSize(QSize(180, 40))
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

        self.horizontalSpacer_3 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.project_button_layout.addItem(self.horizontalSpacer_3)

        self.projects_layout = QVBoxLayout()
        self.projects_layout.setObjectName(u"projects_layout")
        self.Projects = QLabel(self.centralwidget)
        self.Projects.setObjectName(u"Projects")
        self.Projects.setFont(font1)
        self.Projects.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")
        self.Projects.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.projects_layout.addWidget(self.Projects, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ProjectsComboBox = QComboBox(self.centralwidget)
        self.ProjectsComboBox.setObjectName(u"ProjectsComboBox")
        sizePolicy.setHeightForWidth(self.ProjectsComboBox.sizePolicy().hasHeightForWidth())
        self.ProjectsComboBox.setSizePolicy(sizePolicy)
        self.ProjectsComboBox.setMinimumSize(QSize(0, 20))

        self.projects_layout.addWidget(self.ProjectsComboBox, 0, Qt.AlignmentFlag.AlignVCenter)

        self.projects_vertical_spacer = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.projects_layout.addItem(self.projects_vertical_spacer)

        self.AddProjectBtn = QPushButton(self.centralwidget)
        self.AddProjectBtn.setObjectName(u"AddProjectBtn")
        sizePolicy1.setHeightForWidth(self.AddProjectBtn.sizePolicy().hasHeightForWidth())
        self.AddProjectBtn.setSizePolicy(sizePolicy1)
        self.AddProjectBtn.setMinimumSize(QSize(180, 40))
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

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.project_button_layout.addItem(self.horizontalSpacer_4)

        self.phases_layout = QVBoxLayout()
        self.phases_layout.setObjectName(u"phases_layout")
        self.phases_layout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.ProjectPhases = QLabel(self.centralwidget)
        self.ProjectPhases.setObjectName(u"ProjectPhases")
        self.ProjectPhases.setMaximumSize(QSize(16777215, 16777215))
        self.ProjectPhases.setFont(font1)
        self.ProjectPhases.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")
        self.ProjectPhases.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.phases_layout.addWidget(self.ProjectPhases, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.PhasesComboBox = QComboBox(self.centralwidget)
        self.PhasesComboBox.setObjectName(u"PhasesComboBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.PhasesComboBox.sizePolicy().hasHeightForWidth())
        self.PhasesComboBox.setSizePolicy(sizePolicy2)
        self.PhasesComboBox.setMinimumSize(QSize(0, 22))
        self.PhasesComboBox.setStyleSheet(u"QLabel{\n"
"	background-color: #89D5D2;\n"
"}")

        self.phases_layout.addWidget(self.PhasesComboBox)

        self.phases_vertical_spacer = QSpacerItem(200, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.phases_layout.addItem(self.phases_vertical_spacer)


        self.project_button_layout.addLayout(self.phases_layout)

        self.horizontalSpacer_2 = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.project_button_layout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.project_button_layout)

        self.main_layout_spacer = QSpacerItem(13, 25, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.main_layout_spacer)

        self.time_button_layout = QHBoxLayout()
        self.time_button_layout.setObjectName(u"time_button_layout")
        self.left_time_spacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.time_button_layout.addItem(self.left_time_spacer)

        self.LogTimeBtn = QPushButton(self.centralwidget)
        self.LogTimeBtn.setObjectName(u"LogTimeBtn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(20)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.LogTimeBtn.sizePolicy().hasHeightForWidth())
        self.LogTimeBtn.setSizePolicy(sizePolicy3)
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

        self.AddTimeBtn = QPushButton(self.centralwidget)
        self.AddTimeBtn.setObjectName(u"AddTimeBtn")
        self.AddTimeBtn.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.AddTimeBtn.sizePolicy().hasHeightForWidth())
        self.AddTimeBtn.setSizePolicy(sizePolicy3)
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


        self.verticalLayout.addLayout(self.time_button_layout)

        self.logs_layout = QHBoxLayout()
        self.logs_layout.setObjectName(u"logs_layout")
        self.ViewArchitectsBtn = QPushButton(self.centralwidget)
        self.ViewArchitectsBtn.setObjectName(u"ViewArchitectsBtn")
        sizePolicy.setHeightForWidth(self.ViewArchitectsBtn.sizePolicy().hasHeightForWidth())
        self.ViewArchitectsBtn.setSizePolicy(sizePolicy)
        self.ViewArchitectsBtn.setMinimumSize(QSize(150, 50))
        self.ViewArchitectsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.ViewArchitectsBtn.setFont(font2)
        self.ViewArchitectsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ViewArchitectsBtn.setStyleSheet(u"QPushButton{\n"
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
        self.ViewArchitectsBtn.setIconSize(QSize(10, 16))
        self.ViewArchitectsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.ViewArchitectsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ViewProjectsBtn = QPushButton(self.centralwidget)
        self.ViewProjectsBtn.setObjectName(u"ViewProjectsBtn")
        sizePolicy.setHeightForWidth(self.ViewProjectsBtn.sizePolicy().hasHeightForWidth())
        self.ViewProjectsBtn.setSizePolicy(sizePolicy)
        self.ViewProjectsBtn.setMinimumSize(QSize(150, 50))
        self.ViewProjectsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.ViewProjectsBtn.setFont(font2)
        self.ViewProjectsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ViewProjectsBtn.setStyleSheet(u"QPushButton{\n"
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
        self.ViewProjectsBtn.setIconSize(QSize(10, 16))
        self.ViewProjectsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.ViewProjectsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ViewTimeLogsBtn = QPushButton(self.centralwidget)
        self.ViewTimeLogsBtn.setObjectName(u"ViewTimeLogsBtn")
        sizePolicy.setHeightForWidth(self.ViewTimeLogsBtn.sizePolicy().hasHeightForWidth())
        self.ViewTimeLogsBtn.setSizePolicy(sizePolicy)
        self.ViewTimeLogsBtn.setMinimumSize(QSize(150, 50))
        self.ViewTimeLogsBtn.setMaximumSize(QSize(16777215, 16777215))
        self.ViewTimeLogsBtn.setFont(font2)
        self.ViewTimeLogsBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ViewTimeLogsBtn.setStyleSheet(u"QPushButton{\n"
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
        self.ViewTimeLogsBtn.setIconSize(QSize(10, 16))
        self.ViewTimeLogsBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.ViewTimeLogsBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.ViewInvoicesBtn = QPushButton(self.centralwidget)
        self.ViewInvoicesBtn.setObjectName(u"ViewInvoicesBtn")
        sizePolicy.setHeightForWidth(self.ViewInvoicesBtn.sizePolicy().hasHeightForWidth())
        self.ViewInvoicesBtn.setSizePolicy(sizePolicy)
        self.ViewInvoicesBtn.setMinimumSize(QSize(150, 50))
        self.ViewInvoicesBtn.setMaximumSize(QSize(16777215, 16777215))
        self.ViewInvoicesBtn.setFont(font2)
        self.ViewInvoicesBtn.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.ViewInvoicesBtn.setStyleSheet(u"QPushButton{\n"
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
        self.ViewInvoicesBtn.setIconSize(QSize(10, 16))
        self.ViewInvoicesBtn.setAutoDefault(True)

        self.logs_layout.addWidget(self.ViewInvoicesBtn, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout.addLayout(self.logs_layout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.AnalyticsBtn = QPushButton(self.centralwidget)
        self.AnalyticsBtn.setObjectName(u"AnalyticsBtn")
        sizePolicy3.setHeightForWidth(self.AnalyticsBtn.sizePolicy().hasHeightForWidth())
        self.AnalyticsBtn.setSizePolicy(sizePolicy3)
        self.AnalyticsBtn.setMinimumSize(QSize(200, 50))
        self.AnalyticsBtn.setFont(font3)
        self.AnalyticsBtn.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.AnalyticsBtn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 907, 30))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.theArchitectsLogLabel.setText(QCoreApplication.translate("MainWindow", u"The Architect's Log", None))
        self.Architects.setText(QCoreApplication.translate("MainWindow", u"Architect", None))
        self.AddArchitectBtn.setText(QCoreApplication.translate("MainWindow", u"Add New Architect", None))
        self.Projects.setText(QCoreApplication.translate("MainWindow", u"Project", None))
        self.AddProjectBtn.setText(QCoreApplication.translate("MainWindow", u"Add New Project", None))
        self.ProjectPhases.setText(QCoreApplication.translate("MainWindow", u"Project Phase", None))
        self.LogTimeBtn.setText(QCoreApplication.translate("MainWindow", u"LOG TIME", None))
        self.AddTimeBtn.setText(QCoreApplication.translate("MainWindow", u"ADD TIME", None))
        self.ViewArchitectsBtn.setText(QCoreApplication.translate("MainWindow", u"View Architects", None))
        self.ViewProjectsBtn.setText(QCoreApplication.translate("MainWindow", u"View Projects", None))
        self.ViewTimeLogsBtn.setText(QCoreApplication.translate("MainWindow", u"View Time Logs", None))
        self.ViewInvoicesBtn.setText(QCoreApplication.translate("MainWindow", u"View Invoices", None))
        self.AnalyticsBtn.setText(QCoreApplication.translate("MainWindow", u"Analytics", None))
    # retranslateUi

