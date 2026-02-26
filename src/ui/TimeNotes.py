# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TimeNotes.ui'
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
    QLabel, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_TimeNotesDialog(object):
    def setupUi(self, TimeNotesDialog):
        if not TimeNotesDialog.objectName():
            TimeNotesDialog.setObjectName(u"TimeNotesDialog")
        TimeNotesDialog.resize(424, 197)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(TimeNotesDialog.sizePolicy().hasHeightForWidth())
        TimeNotesDialog.setSizePolicy(sizePolicy)
        TimeNotesDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}\n"
"QTextEdit{\n"
"	color: #89D5D2;\n"
"}")
        self.verticalLayout = QVBoxLayout(TimeNotesDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.notesLabel = QLabel(TimeNotesDialog)
        self.notesLabel.setObjectName(u"notesLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.notesLabel.sizePolicy().hasHeightForWidth())
        self.notesLabel.setSizePolicy(sizePolicy1)
        self.notesLabel.setMinimumSize(QSize(400, 40))
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(True)
        self.notesLabel.setFont(font)
        self.notesLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")
        self.notesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.notesLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.notesTextEdit = QTextEdit(TimeNotesDialog)
        self.notesTextEdit.setObjectName(u"notesTextEdit")

        self.verticalLayout.addWidget(self.notesTextEdit)

        self.notesButtonBox = QDialogButtonBox(TimeNotesDialog)
        self.notesButtonBox.setObjectName(u"notesButtonBox")
        self.notesButtonBox.setStyleSheet(u"QPushButton{\n"
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
        self.notesButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Save)

        self.verticalLayout.addWidget(self.notesButtonBox)


        self.retranslateUi(TimeNotesDialog)
        self.notesButtonBox.accepted.connect(TimeNotesDialog.accept)

        QMetaObject.connectSlotsByName(TimeNotesDialog)
    # setupUi

    def retranslateUi(self, TimeNotesDialog):
        TimeNotesDialog.setWindowTitle(QCoreApplication.translate("TimeNotesDialog", u"Dialog", None))
        self.notesLabel.setText(QCoreApplication.translate("TimeNotesDialog", u"Notes", None))
    # retranslateUi

