# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DeleteTimeEntryWarning.ui'
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
    QLabel, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_DeleteTimeEntryDialog(object):
    def setupUi(self, DeleteTimeEntryDialog):
        if not DeleteTimeEntryDialog.objectName():
            DeleteTimeEntryDialog.setObjectName(u"DeleteTimeEntryDialog")
        DeleteTimeEntryDialog.resize(410, 150)
        DeleteTimeEntryDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout = QVBoxLayout(DeleteTimeEntryDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.timeEntryDeleteLabel = QLabel(DeleteTimeEntryDialog)
        self.timeEntryDeleteLabel.setObjectName(u"timeEntryDeleteLabel")
        font = QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        self.timeEntryDeleteLabel.setFont(font)
        self.timeEntryDeleteLabel.setStyleSheet(u"QLabel{\n"
"	color: #008080;\n"
"}")

        self.verticalLayout.addWidget(self.timeEntryDeleteLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(10, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.timeEntryDeleteWarning = QLabel(DeleteTimeEntryDialog)
        self.timeEntryDeleteWarning.setObjectName(u"timeEntryDeleteWarning")
        self.timeEntryDeleteWarning.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.verticalLayout.addWidget(self.timeEntryDeleteWarning)

        self.timeEntryDeleteButtonBox = QDialogButtonBox(DeleteTimeEntryDialog)
        self.timeEntryDeleteButtonBox.setObjectName(u"timeEntryDeleteButtonBox")
        self.timeEntryDeleteButtonBox.setStyleSheet(u"QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	border-style: solid;\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	padding: 5px 10px;\n"
"	margin-left: 5px;\n"
"	margin-right: 10px;\n"
"	background-color: #008080;\n"
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
        self.timeEntryDeleteButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.timeEntryDeleteButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Yes)

        self.verticalLayout.addWidget(self.timeEntryDeleteButtonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignBottom)


        self.retranslateUi(DeleteTimeEntryDialog)
        self.timeEntryDeleteButtonBox.accepted.connect(DeleteTimeEntryDialog.accept)
        self.timeEntryDeleteButtonBox.rejected.connect(DeleteTimeEntryDialog.reject)

        QMetaObject.connectSlotsByName(DeleteTimeEntryDialog)
    # setupUi

    def retranslateUi(self, DeleteTimeEntryDialog):
        DeleteTimeEntryDialog.setWindowTitle(QCoreApplication.translate("DeleteTimeEntryDialog", u"Dialog", None))
        self.timeEntryDeleteLabel.setText(QCoreApplication.translate("DeleteTimeEntryDialog", u"DELELETE TIME LOG?", None))
        self.timeEntryDeleteWarning.setText(QCoreApplication.translate("DeleteTimeEntryDialog", u"DELETED Time Logs Cannot Be Recovered. Confirm DELETE:", None))
    # retranslateUi

