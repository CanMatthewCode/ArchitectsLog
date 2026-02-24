# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoadDatabaseWarning.ui'
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

class Ui_LoadDatabaseDialog(object):
    def setupUi(self, LoadDatabaseDialog):
        if not LoadDatabaseDialog.objectName():
            LoadDatabaseDialog.setObjectName(u"LoadDatabaseDialog")
        LoadDatabaseDialog.resize(570, 217)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadDatabaseDialog.sizePolicy().hasHeightForWidth())
        LoadDatabaseDialog.setSizePolicy(sizePolicy)
        LoadDatabaseDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(LoadDatabaseDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadDatabaseLabel = QLabel(LoadDatabaseDialog)
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

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.loadDatabaseWarning = QTextBrowser(LoadDatabaseDialog)
        self.loadDatabaseWarning.setObjectName(u"loadDatabaseWarning")
        self.loadDatabaseWarning.setStyleSheet(u"QTextBrowser{\n"
"	color: #89D5D2;\n"
"}")

        self.verticalLayout.addWidget(self.loadDatabaseWarning)

        self.loadDatabaseButtonBox = QDialogButtonBox(LoadDatabaseDialog)
        self.loadDatabaseButtonBox.setObjectName(u"loadDatabaseButtonBox")
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
        self.loadDatabaseButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)

        self.verticalLayout.addWidget(self.loadDatabaseButtonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(LoadDatabaseDialog)
        self.loadDatabaseButtonBox.accepted.connect(LoadDatabaseDialog.accept)
        self.loadDatabaseButtonBox.rejected.connect(LoadDatabaseDialog.reject)

        QMetaObject.connectSlotsByName(LoadDatabaseDialog)
    # setupUi

    def retranslateUi(self, LoadDatabaseDialog):
        LoadDatabaseDialog.setWindowTitle(QCoreApplication.translate("LoadDatabaseDialog", u"Dialog", None))
        self.loadDatabaseLabel.setText(QCoreApplication.translate("LoadDatabaseDialog", u"LOAD ARCHIVED DATABASE?", None))
        self.loadDatabaseWarning.setHtml(QCoreApplication.translate("LoadDatabaseDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'.AppleSystemUIFont'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This will revert your Architects, Projects, Time Entries, and Invoices to a previous version.  </p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">	      "
                        " Your current work will be archived.  Proceed?</p></body></html>", None))
    # retranslateUi

