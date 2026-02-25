# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ProgramStartupWelcome.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_ProgramStartupDialog(object):
    def setupUi(self, ProgramStartupDialog):
        if not ProgramStartupDialog.objectName():
            ProgramStartupDialog.setObjectName(u"ProgramStartupDialog")
        ProgramStartupDialog.resize(915, 712)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProgramStartupDialog.sizePolicy().hasHeightForWidth())
        ProgramStartupDialog.setSizePolicy(sizePolicy)
        ProgramStartupDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(ProgramStartupDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadDatabaseLabel = QLabel(ProgramStartupDialog)
        self.loadDatabaseLabel.setObjectName(u"loadDatabaseLabel")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        self.loadDatabaseLabel.setFont(font)
        self.loadDatabaseLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.loadDatabaseLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(10, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.loadDatabaseWarning = QTextBrowser(ProgramStartupDialog)
        self.loadDatabaseWarning.setObjectName(u"loadDatabaseWarning")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.loadDatabaseWarning.sizePolicy().hasHeightForWidth())
        self.loadDatabaseWarning.setSizePolicy(sizePolicy1)
        self.loadDatabaseWarning.setMinimumSize(QSize(891, 561))
        self.loadDatabaseWarning.setStyleSheet(u"QTextBrowser{\n"
"	color: #89D5D2;\n"
"}")

        self.verticalLayout.addWidget(self.loadDatabaseWarning)

        self.loadDatabaseButtonBox = QDialogButtonBox(ProgramStartupDialog)
        self.loadDatabaseButtonBox.setObjectName(u"loadDatabaseButtonBox")
        sizePolicy1.setHeightForWidth(self.loadDatabaseButtonBox.sizePolicy().hasHeightForWidth())
        self.loadDatabaseButtonBox.setSizePolicy(sizePolicy1)
        self.loadDatabaseButtonBox.setMinimumSize(QSize(87, 40))
        font1 = QFont()
        font1.setPointSize(18)
        self.loadDatabaseButtonBox.setFont(font1)
        self.loadDatabaseButtonBox.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	border-style: solid;\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	padding: 5px 10px;\n"
"	margin-left: 5px;\n"
"	margin-right: 10px;\n"
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
        self.loadDatabaseButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.loadDatabaseButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Ok)

        self.verticalLayout.addWidget(self.loadDatabaseButtonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(ProgramStartupDialog)
        self.loadDatabaseButtonBox.accepted.connect(ProgramStartupDialog.accept)
        self.loadDatabaseButtonBox.rejected.connect(ProgramStartupDialog.reject)

        QMetaObject.connectSlotsByName(ProgramStartupDialog)
    # setupUi

    def retranslateUi(self, ProgramStartupDialog):
        ProgramStartupDialog.setWindowTitle(QCoreApplication.translate("ProgramStartupDialog", u"Dialog", None))
        self.loadDatabaseLabel.setText(QCoreApplication.translate("ProgramStartupDialog", u"The Architect's Log", None))
        self.loadDatabaseWarning.setHtml(QCoreApplication.translate("ProgramStartupDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Welcome to the Architect's Log, a time logging and analytics program designed around an architect's workflow.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-r"
                        "ight:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt;Upon program startup you will see a demo file populated with temporary information for architect, projects, time logs, and invoices.  Look around to see how the program will eventually appear once you have spent a considerable time logging your work. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">-&gt;Check out the Analytics section to view how your graphs will be drawn, including: your Projects by Phase, a single project's Worked Timeline, your Phase Averages across all your projects, up to three Project's Phases vs their Phase Averages, and Total Time Logged by Project, color coded "
                        "by phase, over a chosen time range. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Then, when you are ready, simply go to File-&gt;Create New Database to get a clean, empty database from which to log  your own work.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-rig"
                        "ht:0px; -qt-block-indent:0; text-indent:0px;\">Once in your new personal database, add an Architect, add some Projects, and either log your times with the help of an on-screen timer (LOG TIME) or by manually inputting your past times (ADD TIME). </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To create an invoice enter the View Time Logs section and click 'Create Invoice', at which point you can select which logs from the same project and phase you would like to group together. Hit 'Generate Invoice', enter an invoice number, and have it saved to the View Invoices section of the program. </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margi"
                        "n-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">You can view all your invoices from View Invoices or see the time logs associated with any one Invoice by clicking the View Invoice button, at which point you can click  Save to PDF to get a clean printout of that invoice's logged times and total duration.</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Over time your logs will fill the Analytics section giving you a better understanding of your work history - the time spent per phase and per project.  <br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-to"
                        "p:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Enjoy</p></body></html>", None))
    # retranslateUi

