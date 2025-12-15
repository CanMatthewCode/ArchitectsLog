# PySide6 functions for the Architect's Log

import sys
import os
import re

from PySide6.QtWidgets import (QMainWindow, QApplication, QDialog, QMessageBox,
	QStyledItemDelegate, QComboBox, QWidget)
from PySide6.QtSql import (QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, 
	QSqlRelation)
from PySide6.QtCore import Qt, QDate

from ui.MainWindow import Ui_MainWindow
from ui.AddArchitect import Ui_AddArchitectDialog
from ui.AddProject import Ui_AddProjectDialog
from ui.ViewArchitects import Ui_ViewArchitectsWindow

from architectsLog_classes import Architect, Project, Invoice, TimeEntry 
from architectsLog_constants import	(PHASES, ARCHITECT_STATUSES, PROJECT_STATUSES, 
	INVOICE_STATUSES)
from architectsLog_db import DB_FILE, get_db_connection, add_architect, add_project


def initialize_database(DB_FILE: str) -> None:
	"""Open the persistant global Qt connection to the database"""
	db = QSqlDatabase.addDatabase("QSQLITE")
	db.setDatabaseName(DB_FILE)
	if not db.open():
		raise Exception("Failed to open database")

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self) -> None:
		super(MainWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())

		# create architect, project, phase models and set them on their combo box
		self.architect_model = QSqlTableModel()
		self.architect_model.setTable("architects")
		self.architect_model.select()
		self.ArchitectsComboBox.setModel(self.architect_model)
		self.ArchitectsComboBox.setModelColumn(1)				# Index 1 is arch. name

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.select()
		self.ProjectsComboBox.setModel(self.project_model)
		self.ProjectsComboBox.setModelColumn(1)					# Index 1 is proj name
		
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.select()
		self.PhasesComboBox.setModel(self.phase_model)
		self.PhasesComboBox.setModelColumn(1)					# Index 1 is phase name

		# enable button clicks
		self.AddArchitectBtn.clicked.connect(self.addArchitect)
		self.AddProjectBtn.clicked.connect(self.addProject)
		self.ViewArchitectsBtn.clicked.connect(self.viewArchitects)


		self.show()


	# button methods
	def addArchitect(self) -> None:
		"""Method to open new architect dialog, store results as a new Architect
		object, then store that object in the architects table of the database"""
		arch_window = ArchitectWindow()
		result = arch_window.exec()
		if result == QDialog.Accepted:
			new_architect = Architect(name = arch_window.architectNameInput.text(), 
				license_number = arch_window.licenseInput.text(), 
				phone_number = arch_window.phoneInput.text(),
				email = arch_window.emailInput.text(), 
				company_name = arch_window.companyInput.text())
			with get_db_connection() as conn:
				cur = conn.cursor()
				add_architect(new_architect, cur)
			self.architect_model.select()

	def addProject(self) -> None:
		"""Method to open new projects dialog, store results as a new Project
		object, then store that object in the projects table of the database"""
		proj_window = ProjectWindow()
		result = proj_window.exec()
		if result == QDialog.Accepted:
			# Get the current index from the combo box
			phase_index = proj_window.phaseComboBox.currentIndex()
			# Get the phase_id from the phases table through the QComboBox model
			model = proj_window.phaseComboBox.model()
			phase_id = model.data(model.index(phase_index, 0))
			new_project = Project(project_name = proj_window.projectNameInput.text(),
				client_name = proj_window.clientInput.text(),
				client_address = proj_window.projectAddressInput.text(),
				start_date = proj_window.projectStartDate.date(),
				current_phase_id = phase_id)
			with get_db_connection() as conn:
				cur = conn.cursor()
				add_project(new_project, cur)
			self.project_model.select()

	def viewArchitects(self) -> None:
		"""Method to view all architects in database table, click button to
		include inactive architects"""
		self.view_arch_window = ViewArchitects()


		

class ArchitectWindow(QDialog, Ui_AddArchitectDialog):
	def __init__(self) -> None:
		super(ArchitectWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())

	def accept(self) -> None:
		"""Method to verify all forms were entered with correct syntax; 
		set phone to chosen (xxx) xxx.xxxx style"""
		architect_name = self.architectNameInput.text()
		license_number = self.licenseInput.text()

		phone_pattern = re.compile(r'\(*(\d{3})\)*(\s|.)(\d{3})(\s|.)(\d{4})')
		phone_result = phone_pattern.search(self.phoneInput.text())

		email_pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$')
		email_result = email_pattern.search(self.emailInput.text())

		# Checks to ensure valid input for architect table
		if not architect_name:
			QMessageBox.warning(self, "Invalid Name", "Please Enter Architect's Name")
			return

		if not license_number:
			QMessageBox.warning(self, "Invalid License", 
				"Please Add Architect's License Number")
			return

		if not email_result and not phone_result:
			QMessageBox.warning(self, "Invalid Phone Number and Email", 
				"Invalid Phone Number and Email, Please Correct")
			return

		if not email_result:
			QMessageBox.warning(self, "Invalid Email", "Invalid Email, Please Correct")
			return

		if not phone_result:
			QMessageBox.warning(self, "Invalid Phone Number", 
				"Invalid Phone Number, Please Correct")
			return
		 
		# modify phone number to fix (xxx) xxx.xxxx style
		original_text = self.phoneInput.text()
		result = phone_pattern.sub(r"(\g<1>) \g<3>.\g<5>", original_text)
		self.phoneInput.setText(result)

		super().accept()


class ProjectWindow(QDialog, Ui_AddProjectDialog):
	def __init__(self) -> None:
		super(ProjectWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())

		# set current date onto the calendar drop down
		self.projectStartDate.setDate(QDate.currentDate())

		# set first phase to the Phase QComboBox
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.select()
		self.phaseComboBox.setModel(self.phase_model)
		self.phaseComboBox.setModelColumn(1)				# Index 1 is phase names
		self.phaseComboBox.setCurrentIndex(0)				# Row 0 is first phase

	def accept(self) -> None:
		"""Method to verify all needed forms contain information"""
		project_name = self.projectNameInput.text()
		client_name = self.clientInput.text()
		client_address = self.projectAddressInput.text()

		# Checks to ensure valid input for projects table
		if not project_name:
			QMessageBox.warning(self, "Invalid Name", "Please Enter a Project Name")
			return

		if not client_name: 
			QMessageBox.warning(self, "Invalid Client Name",
			 "Please Enter Client's Name")
			return

		if not client_address:
			QMessageBox.warning(self, "Invalid Address", 
				"Please Enter Client's Address")
			return

		super().accept()


class ViewArchitects(QWidget, Ui_ViewArchitectsWindow):
	def __init__(self) -> None:
		super(ViewArchitects, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())

		# create query table model and set it on window's TableView
		self.model = NoDeleteTableModel()
		self.model.setTable("architects")
		self.architectsTableView.setModel(self.model)

		# allow editing of architect information
		self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

		# create and set column headers
		column_titles = {
			"name" : "Name",
			"license_number" : "License Number",
			"phone_number" : "Phone Number",
			"email" : "Email Address",
			"company_name" : "Firm Name",
			"status" : "Architect Status",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		# hide architect_id and status columns
		self.architectsTableView.setColumnHidden(
			self.model.fieldIndex("architect_id"), True)

		# move license number to after company name
		header = self.architectsTableView.horizontalHeader()
		header.moveSection(5, 2) 			# move company name to 2nd column

		# set original sort by architect name
		index = self.model.fieldIndex("name")
		self.architectsTableView.sortByColumn(index, Qt.AscendingOrder)

		# allow table to be sorted by clicking top header tabs
		self.architectsTableView.setSortingEnabled(True)

		# only allow chosen options for status column - create a combo box and set
		# it on the column for status to allow only acceptable status options
		status_delegate = StatusDelegate(ARCHITECT_STATUSES, self.architectsTableView)
		status_column = self.model.fieldIndex("status")
		self.architectsTableView.setItemDelegateForColumn(status_column, 
			status_delegate)

		self.model.select()
		
		# set checkbox button to show inactive architects
		self.hideArchitectCheckBox.stateChanged.connect(self.hideInactiveArchitects)
		
		self.show()

	def hideInactiveArchitects(self, signal) -> None:
		if signal == Qt.Checked:
			self.model.setFilter("status = 'active'")
			self.architectsTableView.setColumnHidden(
				self.model.fieldIndex("status"), True)
			self.model.select()
		else:
			self.model.setFilter("")
			self.architectsTableView.setColumnHidden(
				self.model.fieldIndex("status"), False)
			self.model.select()


class NoDeleteTableModel(QSqlTableModel):
	"""New Class to dissalow deletions of entire rows in my table views"""
	def removeRows(self, row, count, parent=None) -> bool:
		return False


class StatusDelegate(QStyledItemDelegate):
	"""Class to allow drop down ComboBoxes for areas where only a specific
	selection of values is allowed"""
	def __init__(self, options, parent=None) -> None:
		super().__init__(parent)
		self.options = options

	def createEditor(self, parent, options, index) -> QComboBox:
		# create and return a combo box as the editor
		combo = QComboBox(parent)
		combo.addItems(self.options)
		return combo

	def setEditorData(self, editor, index) -> None:
		# set the current value on the combo box
		current_value = index.data()
		current_index = editor.findText(current_value)
		if current_index >= 0:
			editor.setCurrentIndex(current_index)

	def setModelData(self, editor, model, index) -> None:
		# save the value back to the model
		value = editor.currentText()
		model.setData(index, value)



app = QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())