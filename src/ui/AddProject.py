# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddProject.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateEdit,
    QDateTimeEdit, QDialog, QDialogButtonBox, QLabel,
    QLineEdit, QSizePolicy, QVBoxLayout, QWidget)

class Ui_AddProjectDialog(object):
    def setupUi(self, AddProjectDialog):
        if not AddProjectDialog.objectName():
            AddProjectDialog.setObjectName(u"AddProjectDialog")
        AddProjectDialog.resize(576, 450)
        AddProjectDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(AddProjectDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.MainTitle = QLabel(AddProjectDialog)
        self.MainTitle.setObjectName(u"MainTitle")
        self.MainTitle.setMinimumSize(QSize(550, 60))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.MainTitle.setFont(font)
        self.MainTitle.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")
        self.MainTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.MainTitle)

        self.input_layout = QVBoxLayout()
        self.input_layout.setSpacing(15)
        self.input_layout.setObjectName(u"input_layout")
        self.input_layout.setContentsMargins(110, 30, 110, 10)
        self.project_name_layout = QVBoxLayout()
        self.project_name_layout.setSpacing(1)
        self.project_name_layout.setObjectName(u"project_name_layout")
        self.projectName = QLabel(AddProjectDialog)
        self.projectName.setObjectName(u"projectName")
        self.projectName.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.project_name_layout.addWidget(self.projectName)

        self.projectNameInput = QLineEdit(AddProjectDialog)
        self.projectNameInput.setObjectName(u"projectNameInput")

        self.project_name_layout.addWidget(self.projectNameInput)


        self.input_layout.addLayout(self.project_name_layout)

        self.client_layout = QVBoxLayout()
        self.client_layout.setSpacing(1)
        self.client_layout.setObjectName(u"client_layout")
        self.client = QLabel(AddProjectDialog)
        self.client.setObjectName(u"client")
        self.client.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.client_layout.addWidget(self.client)

        self.clientInput = QLineEdit(AddProjectDialog)
        self.clientInput.setObjectName(u"clientInput")

        self.client_layout.addWidget(self.clientInput)


        self.input_layout.addLayout(self.client_layout)

        self.project_address_layout = QVBoxLayout()
        self.project_address_layout.setSpacing(1)
        self.project_address_layout.setObjectName(u"project_address_layout")
        self.projectAddress = QLabel(AddProjectDialog)
        self.projectAddress.setObjectName(u"projectAddress")
        self.projectAddress.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.project_address_layout.addWidget(self.projectAddress)

        self.projectAddressInput = QLineEdit(AddProjectDialog)
        self.projectAddressInput.setObjectName(u"projectAddressInput")

        self.project_address_layout.addWidget(self.projectAddressInput)


        self.input_layout.addLayout(self.project_address_layout)

        self.start_date_layout = QVBoxLayout()
        self.start_date_layout.setSpacing(1)
        self.start_date_layout.setObjectName(u"start_date_layout")
        self.startDate = QLabel(AddProjectDialog)
        self.startDate.setObjectName(u"startDate")
        self.startDate.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.start_date_layout.addWidget(self.startDate)

        self.projectStartDate = QDateEdit(AddProjectDialog)
        self.projectStartDate.setObjectName(u"projectStartDate")
        self.projectStartDate.setMaximumDate(QDate(2100, 12, 31))
        self.projectStartDate.setMinimumDate(QDate(2025, 1, 1))
        self.projectStartDate.setCurrentSection(QDateTimeEdit.Section.MonthSection)
        self.projectStartDate.setCalendarPopup(True)
        self.projectStartDate.setTimeSpec(Qt.TimeSpec.LocalTime)

        self.start_date_layout.addWidget(self.projectStartDate)


        self.input_layout.addLayout(self.start_date_layout)

        self.phase_layout = QVBoxLayout()
        self.phase_layout.setSpacing(1)
        self.phase_layout.setObjectName(u"phase_layout")
        self.phase = QLabel(AddProjectDialog)
        self.phase.setObjectName(u"phase")
        self.phase.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.phase_layout.addWidget(self.phase)

        self.phaseComboBox = QComboBox(AddProjectDialog)
        self.phaseComboBox.setObjectName(u"phaseComboBox")

        self.phase_layout.addWidget(self.phaseComboBox)


        self.input_layout.addLayout(self.phase_layout)


        self.verticalLayout_3.addLayout(self.input_layout)

        self.addProjectButtonBox = QDialogButtonBox(AddProjectDialog)
        self.addProjectButtonBox.setObjectName(u"addProjectButtonBox")
        self.addProjectButtonBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addProjectButtonBox.sizePolicy().hasHeightForWidth())
        self.addProjectButtonBox.setSizePolicy(sizePolicy)
        self.addProjectButtonBox.setMinimumSize(QSize(150, 30))
        self.addProjectButtonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.addProjectButtonBox.setStyleSheet(u"QDialogButtonBox QPushButton{\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	border-style: solid;\n"
"	background-color: #89D5D2;\n"
"	color: black;\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	padding: 5px 10px;\n"
"	margin-left: 5px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"QDialogButtonBox  QPushButton:hover{\n"
"	background-color: #6FB5B2;\n"
"}\n"
"\n"
"QDialogButtonBox QPushButton:pressed {\n"
"	background-color: #5A9695\n"
"}")
        self.addProjectButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.addProjectButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.addProjectButtonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.addProjectButtonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(AddProjectDialog)
        self.addProjectButtonBox.accepted.connect(AddProjectDialog.accept)
        self.addProjectButtonBox.rejected.connect(AddProjectDialog.reject)

        QMetaObject.connectSlotsByName(AddProjectDialog)
    # setupUi

    def retranslateUi(self, AddProjectDialog):
        AddProjectDialog.setWindowTitle(QCoreApplication.translate("AddProjectDialog", u"Dialog", None))
        self.MainTitle.setText(QCoreApplication.translate("AddProjectDialog", u"Add Project", None))
        self.projectName.setText(QCoreApplication.translate("AddProjectDialog", u"Project Name:", None))
        self.client.setText(QCoreApplication.translate("AddProjectDialog", u"Client Name:", None))
        self.projectAddress.setText(QCoreApplication.translate("AddProjectDialog", u"Project Address:", None))
        self.startDate.setText(QCoreApplication.translate("AddProjectDialog", u"Start Date:", None))
        self.projectStartDate.setDisplayFormat(QCoreApplication.translate("AddProjectDialog", u"MM/dd/yy", None))
        self.phase.setText(QCoreApplication.translate("AddProjectDialog", u"Phase:", None))
    # retranslateUi

