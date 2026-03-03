# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddTimeEntry.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QComboBox, QDateTimeEdit,
    QDialog, QDialogButtonBox, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_AddTimeDialog(object):
    def setupUi(self, AddTimeDialog):
        if not AddTimeDialog.objectName():
            AddTimeDialog.setObjectName(u"AddTimeDialog")
        AddTimeDialog.resize(606, 400)
        AddTimeDialog.setStyleSheet(u"QWidget{\n"
"	background-color: #1E2E34;\n"
"}\n"
"QComboBox{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QComboBox QAbstractItemView{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QLineEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QDateEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QTimeEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QDateTimeEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}\n"
"QTextEdit{\n"
"	color: #89D5D2;\n"
"	background-color: #1E2E34;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(AddTimeDialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.addTimeLabel = QLabel(AddTimeDialog)
        self.addTimeLabel.setObjectName(u"addTimeLabel")
        self.addTimeLabel.setMinimumSize(QSize(550, 60))
        font = QFont()
        font.setPointSize(48)
        font.setBold(True)
        font.setUnderline(True)
        self.addTimeLabel.setFont(font)
        self.addTimeLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")
        self.addTimeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.addTimeLabel)

        self.verticalSpacer = QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)

        self.arch_proj_phase_layout = QHBoxLayout()
        self.arch_proj_phase_layout.setObjectName(u"arch_proj_phase_layout")
        self.architectLabel = QLabel(AddTimeDialog)
        self.architectLabel.setObjectName(u"architectLabel")
        self.architectLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.arch_proj_phase_layout.addWidget(self.architectLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.projectLabel = QLabel(AddTimeDialog)
        self.projectLabel.setObjectName(u"projectLabel")
        self.projectLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.arch_proj_phase_layout.addWidget(self.projectLabel, 0, Qt.AlignmentFlag.AlignHCenter)

        self.phaseLabel = QLabel(AddTimeDialog)
        self.phaseLabel.setObjectName(u"phaseLabel")
        self.phaseLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.arch_proj_phase_layout.addWidget(self.phaseLabel, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_6.addLayout(self.arch_proj_phase_layout)

        self.presets_combobox_layout = QHBoxLayout()
        self.presets_combobox_layout.setObjectName(u"presets_combobox_layout")
        self.ArchitectComboBox = QComboBox(AddTimeDialog)
        self.ArchitectComboBox.setObjectName(u"ArchitectComboBox")

        self.presets_combobox_layout.addWidget(self.ArchitectComboBox)

        self.ProjectComboBox = QComboBox(AddTimeDialog)
        self.ProjectComboBox.setObjectName(u"ProjectComboBox")

        self.presets_combobox_layout.addWidget(self.ProjectComboBox)

        self.PhaseComboBox = QComboBox(AddTimeDialog)
        self.PhaseComboBox.setObjectName(u"PhaseComboBox")

        self.presets_combobox_layout.addWidget(self.PhaseComboBox)


        self.verticalLayout_6.addLayout(self.presets_combobox_layout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.timeLayoutLeftSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.timeLayoutLeftSpacer)

        self.start_times_layout = QVBoxLayout()
        self.start_times_layout.setObjectName(u"start_times_layout")
        self.startTimeLabel = QLabel(AddTimeDialog)
        self.startTimeLabel.setObjectName(u"startTimeLabel")
        self.startTimeLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.start_times_layout.addWidget(self.startTimeLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.timeStartEdit = QDateTimeEdit(AddTimeDialog)
        self.timeStartEdit.setObjectName(u"timeStartEdit")
        self.timeStartEdit.setCurrentSection(QDateTimeEdit.Section.HourSection)
        self.timeStartEdit.setCalendarPopup(True)

        self.start_times_layout.addWidget(self.timeStartEdit)


        self.horizontalLayout.addLayout(self.start_times_layout)

        self.end_times_layout = QVBoxLayout()
        self.end_times_layout.setObjectName(u"end_times_layout")
        self.endTimeLabel = QLabel(AddTimeDialog)
        self.endTimeLabel.setObjectName(u"endTimeLabel")
        self.endTimeLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.end_times_layout.addWidget(self.endTimeLabel, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.timeEndEdit = QDateTimeEdit(AddTimeDialog)
        self.timeEndEdit.setObjectName(u"timeEndEdit")
        self.timeEndEdit.setCurrentSection(QDateTimeEdit.Section.HourSection)
        self.timeEndEdit.setCalendarPopup(True)

        self.end_times_layout.addWidget(self.timeEndEdit)


        self.horizontalLayout.addLayout(self.end_times_layout)

        self.timeLayoutSpacer = QSpacerItem(150, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.timeLayoutSpacer)


        self.verticalLayout_6.addLayout(self.horizontalLayout)

        self.verticalSpacer_3 = QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_3)

        self.notes_layout = QVBoxLayout()
        self.notes_layout.setObjectName(u"notes_layout")
        self.notesLabel = QLabel(AddTimeDialog)
        self.notesLabel.setObjectName(u"notesLabel")
        self.notesLabel.setStyleSheet(u"QLabel{\n"
"	color: #35B5AC;\n"
"}")

        self.notes_layout.addWidget(self.notesLabel)

        self.notesTextEdit = QTextEdit(AddTimeDialog)
        self.notesTextEdit.setObjectName(u"notesTextEdit")

        self.notes_layout.addWidget(self.notesTextEdit)


        self.verticalLayout_6.addLayout(self.notes_layout)

        self.addTimeButtonBox = QDialogButtonBox(AddTimeDialog)
        self.addTimeButtonBox.setObjectName(u"addTimeButtonBox")
        self.addTimeButtonBox.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addTimeButtonBox.sizePolicy().hasHeightForWidth())
        self.addTimeButtonBox.setSizePolicy(sizePolicy)
        self.addTimeButtonBox.setMinimumSize(QSize(150, 40))
        self.addTimeButtonBox.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.addTimeButtonBox.setStyleSheet(u"QDialogButtonBox QPushButton {\n"
"	border-radius: 12px;\n"
"	border: 1px solid black;\n"
"	border-style: solid;\n"
"	background-color: #35B5AC;\n"
"	color: black;\n"
"	min-width: 50px;\n"
"	min-height: 10px;\n"
"	padding: 5px 10px;\n"
"	margin-left: 5px;\n"
"	margin-right: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #2A9089;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"	background-color: #1F6B66;\n"
"}")
        self.addTimeButtonBox.setOrientation(Qt.Orientation.Horizontal)
        self.addTimeButtonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Save)
        self.addTimeButtonBox.setCenterButtons(True)

        self.verticalLayout_6.addWidget(self.addTimeButtonBox, 0, Qt.AlignmentFlag.AlignRight)


        self.retranslateUi(AddTimeDialog)
        self.addTimeButtonBox.accepted.connect(AddTimeDialog.accept)
        self.addTimeButtonBox.rejected.connect(AddTimeDialog.reject)

        QMetaObject.connectSlotsByName(AddTimeDialog)
    # setupUi

    def retranslateUi(self, AddTimeDialog):
        AddTimeDialog.setWindowTitle(QCoreApplication.translate("AddTimeDialog", u"Dialog", None))
        self.addTimeLabel.setText(QCoreApplication.translate("AddTimeDialog", u"Add Time", None))
        self.architectLabel.setText(QCoreApplication.translate("AddTimeDialog", u"Architect", None))
        self.projectLabel.setText(QCoreApplication.translate("AddTimeDialog", u"Project", None))
        self.phaseLabel.setText(QCoreApplication.translate("AddTimeDialog", u"Phase", None))
        self.startTimeLabel.setText(QCoreApplication.translate("AddTimeDialog", u"Start Time:", None))
        self.endTimeLabel.setText(QCoreApplication.translate("AddTimeDialog", u"End Time", None))
        self.notesLabel.setText(QCoreApplication.translate("AddTimeDialog", u"Notes:", None))
    # retranslateUi

