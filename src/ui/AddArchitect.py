# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddArchitect.ui'
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
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_AddArchitectDialog(object):
    def setupUi(self, AddArchitectDialog):
        if not AddArchitectDialog.objectName():
            AddArchitectDialog.setObjectName(u"AddArchitectDialog")
        AddArchitectDialog.resize(576, 450)
        AddArchitectDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(AddArchitectDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.MainTitle = QLabel(AddArchitectDialog)
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
        self.name_layout = QVBoxLayout()
        self.name_layout.setSpacing(1)
        self.name_layout.setObjectName(u"name_layout")
        self.architectName = QLabel(AddArchitectDialog)
        self.architectName.setObjectName(u"architectName")
        self.architectName.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.name_layout.addWidget(self.architectName)

        self.architectNameInput = QLineEdit(AddArchitectDialog)
        self.architectNameInput.setObjectName(u"architectNameInput")

        self.name_layout.addWidget(self.architectNameInput)


        self.input_layout.addLayout(self.name_layout)

        self.license_layout = QVBoxLayout()
        self.license_layout.setSpacing(1)
        self.license_layout.setObjectName(u"license_layout")
        self.license = QLabel(AddArchitectDialog)
        self.license.setObjectName(u"license")
        self.license.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.license_layout.addWidget(self.license)

        self.licenseInput = QLineEdit(AddArchitectDialog)
        self.licenseInput.setObjectName(u"licenseInput")

        self.license_layout.addWidget(self.licenseInput)


        self.input_layout.addLayout(self.license_layout)

        self.company_layout = QVBoxLayout()
        self.company_layout.setSpacing(1)
        self.company_layout.setObjectName(u"company_layout")
        self.companyName = QLabel(AddArchitectDialog)
        self.companyName.setObjectName(u"companyName")
        self.companyName.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.company_layout.addWidget(self.companyName)

        self.companyInput = QLineEdit(AddArchitectDialog)
        self.companyInput.setObjectName(u"companyInput")

        self.company_layout.addWidget(self.companyInput)


        self.input_layout.addLayout(self.company_layout)

        self.phone_layout = QVBoxLayout()
        self.phone_layout.setSpacing(1)
        self.phone_layout.setObjectName(u"phone_layout")
        self.phone = QLabel(AddArchitectDialog)
        self.phone.setObjectName(u"phone")
        self.phone.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.phone_layout.addWidget(self.phone)

        self.phoneInput = QLineEdit(AddArchitectDialog)
        self.phoneInput.setObjectName(u"phoneInput")

        self.phone_layout.addWidget(self.phoneInput)


        self.input_layout.addLayout(self.phone_layout)

        self.email_layout = QVBoxLayout()
        self.email_layout.setSpacing(1)
        self.email_layout.setObjectName(u"email_layout")
        self.email = QLabel(AddArchitectDialog)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"QLabel{\n"
"	color: #89D5D2;\n"
"}")

        self.email_layout.addWidget(self.email)

        self.emailInput = QLineEdit(AddArchitectDialog)
        self.emailInput.setObjectName(u"emailInput")

        self.email_layout.addWidget(self.emailInput)


        self.input_layout.addLayout(self.email_layout)


        self.verticalLayout_3.addLayout(self.input_layout)

        self.addArchitectButtonBox = QDialogButtonBox(AddArchitectDialog)
        self.addArchitectButtonBox.setObjectName(u"addArchitectButtonBox")
        self.addArchitectButtonBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addArchitectButtonBox.sizePolicy().hasHeightForWidth())
        self.addArchitectButtonBox.setSizePolicy(sizePolicy)
        self.addArchitectButtonBox.setMinimumSize(QSize(150, 30))
        self.addArchitectButtonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.addArchitectButtonBox.setStyleSheet(u"QDialogButtonBox QPushButton{\n"
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
        self.addArchitectButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.addArchitectButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.addArchitectButtonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.addArchitectButtonBox, 0, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignVCenter)


        self.retranslateUi(AddArchitectDialog)
        self.addArchitectButtonBox.accepted.connect(AddArchitectDialog.accept)
        self.addArchitectButtonBox.rejected.connect(AddArchitectDialog.reject)

        QMetaObject.connectSlotsByName(AddArchitectDialog)
    # setupUi

    def retranslateUi(self, AddArchitectDialog):
        AddArchitectDialog.setWindowTitle(QCoreApplication.translate("AddArchitectDialog", u"Dialog", None))
        self.MainTitle.setText(QCoreApplication.translate("AddArchitectDialog", u"Add Architect", None))
        self.architectName.setText(QCoreApplication.translate("AddArchitectDialog", u"Architect Name:", None))
        self.license.setText(QCoreApplication.translate("AddArchitectDialog", u"License Number:", None))
        self.companyName.setText(QCoreApplication.translate("AddArchitectDialog", u"Company Name:", None))
        self.phone.setText(QCoreApplication.translate("AddArchitectDialog", u"Phone Number:", None))
        self.email.setText(QCoreApplication.translate("AddArchitectDialog", u"Email:", None))
    # retranslateUi

