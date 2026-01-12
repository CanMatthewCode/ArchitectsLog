# PySide6 functions for the Architect's Log

import sys
import os
import re
from datetime import datetime

from PySide6.QtWidgets import (QMainWindow, QApplication, QDialog, QMessageBox,
	QStyledItemDelegate, QLineEdit, QComboBox, QWidget, QLCDNumber)
from PySide6.QtSql import (QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, 
	QSqlRelation, QSqlRelationalDelegate)
from PySide6.QtCore import (Qt, QDate, QDateTime, QModelIndex, QTimer, QTime, 
	QRegularExpression)
from PySide6.QtGui import QRegularExpressionValidator

from ui.MainWindow import Ui_MainWindow
from ui.AddArchitect import Ui_AddArchitectDialog
from ui.AddProject import Ui_AddProjectDialog
from ui.ViewArchitects import Ui_ViewArchitectsWindow
from ui.ViewProjects import Ui_ViewProjectsWindow
from ui.ViewTimeEntries import Ui_ViewTimeEntriesWindow
from ui.TimeNotes import Ui_TimeNotesDialog
from ui.AddTimeEntry import Ui_AddTimeDialog

from architectsLog_classes import Architect, Project, Invoice, TimeEntry 
from architectsLog_constants import	(PHASES, ARCHITECT_STATUSES, PROJECT_STATUSES, 
	INVOICE_STATUSES)
from architectsLog_db import (DB_FILE, get_db_connection, add_architect, add_project,
	add_time_entry, add_invoice, update_project)


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
		self.ArchitectsComboBox.setModelColumn(1)				# Index 1 is arch name

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
		# set the phases combo box to be the project's current phase - 
		# 5 is phase_id column number in projects table
		setCrossComboBox(self.ProjectsComboBox, self.PhasesComboBox, 5)
		self.ProjectsComboBox.currentIndexChanged.connect(self.projectChanged)
		self.PhasesComboBox.currentIndexChanged.connect(self.phaseChanged)

		# enable button clicks
		self.AddArchitectBtn.clicked.connect(self.addArchitect)
		self.AddProjectBtn.clicked.connect(self.addProject)
		self.LogTimeBtn.clicked.connect(self.logTime)
		self.AddTimeBtn.clicked.connect(self.addTime)
		
		self.view_arch_window = None
		self.view_proj_window = None
		self.view_time_entries_window = None

		self.ViewArchitectsBtn.clicked.connect(self.viewArchitects)
		self.ViewProjectsBtn.clicked.connect(self.viewProjects)
		self.ViewTimeLogsBtn.clicked.connect(self.viewTimeEntries)

		self.show()

	def projectChanged(self) -> None:
		"""Method to set phase combo box to phase attached to project"""
		self.PhasesComboBox.blockSignals(True)
		setCrossComboBox(self.ProjectsComboBox, self.PhasesComboBox, 5)
		
		# Block phases combo box if proj_id is for administrative work
		proj_index = self.ProjectsComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		if proj_id < 0:
			self.PhasesComboBox.setEnabled(False)
		else:
			self.PhasesComboBox.setEnabled(True)

		self.PhasesComboBox.blockSignals(False)

	def phaseChanged(self) -> None:
		"""Method to set a newly chosen phase as the project's updated current_phase"""
		phase_index = self.PhasesComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))
		
		# Get current index of project combo box and phases column from projects table
		proj_index = self.ProjectsComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		
		# Disable PhasesComboBox if phase is Business Development or Administration
		if phase_id in (8, 9):
			self.PhasesComboBox.setEnabled(False)
			if phase_id == 8:
				self.ProjectsComboBox.setCurrentIndex(1)
			else:
				self.ProjectsComboBox.setCurrentIndex(0)
			return
		else:
			self.PhasesComboBox.setEnabled(True)

		# Update project with new phase in project table
		with get_db_connection() as conn:
			cur = conn.cursor()
			update_project("current_phase_id", proj_id, phase_id, cur)

		# Reset the model and set the current index back on Projects ComboBox
		self.project_model.select()
		self.ProjectsComboBox.setCurrentIndex(proj_index)
		# Refresh the view_proj_window's model to display new information
		if self.view_proj_window is not None:
			self.view_proj_window.model.select()

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
			# Turn the QDate object into a string
			start_date = proj_window.projectStartDate.date()
			start_date_str = start_date.toString("MM/dd/yyyy")
			new_project = Project(project_name = proj_window.projectNameInput.text(),
				client_name = proj_window.clientInput.text(),
				client_address = proj_window.projectAddressInput.text(),
				start_date = start_date_str,
				current_phase_id = phase_id)
			with get_db_connection() as conn:
				cur = conn.cursor()
				add_project(new_project, cur)
			self.project_model.select()

	def viewArchitects(self) -> None:
		"""Method to view all architects in database table, click button to
		hide inactive architects"""
		self.view_arch_window = ViewArchitects()

	def viewProjects(self) -> None:
		"""Method to view all projects in database table, click button to
		hide completed projects"""
		self.view_proj_window = ViewProjects(self)

	def viewTimeEntries(self) -> None:
		"""Method to view all time_entries in database table, click button 
		to hide entries already associated with an invoice"""
		self.view_time_entries_window = ViewTimeEntries()

	def logTime(self) -> None:
		"""Method to activate TimeLogger window and store resulting 
		TimeEntry object in time_entries database"""
		self.log_time = TimeLogger(self)
		self.showMinimized()

	def addTime(self) -> None:
		"""Method to activate ManualTimeLogger window and input
		manual information into the time_entries database"""
		manual_log_time = ManualTimeLogger(self)
		result = manual_log_time.exec()
		if result == QDialog.Accepted:
			# Get id's for architect, project, phase
			arch_index = manual_log_time.ArchitectComboBox.currentIndex()
			arch_model = manual_log_time.ArchitectComboBox.model()
			arch_id = arch_model.data(arch_model.index(arch_index, 0))

			phase_index = manual_log_time.PhaseComboBox.currentIndex()
			phase_model = manual_log_time.PhaseComboBox.model()
			phase_id = phase_model.data(phase_model.index(phase_index, 0))

			if phase_id == 8:
				proj_id = -1
			elif phase_id == 9:
				proj_id = -2
			else:
				proj_index = manual_log_time.ProjectComboBox.currentIndex()
				proj_model = manual_log_time.ProjectComboBox.model()
				proj_id = proj_model.data(proj_model.index(proj_index, 0))

			# Get start date and time and turn into a timestamp int for database
			start_date = manual_log_time.timeStartDate.date()
			start_time = manual_log_time.timeEdit.time()
			qDatetime = QDateTime(start_date, start_time)
			pyDatetime = qDatetime.toPython()
			time_log_start_time = int(pyDatetime.timestamp())

			# Get duration input and validate it with validation function
			duration = manual_log_time.durationLineEdit.text()
			if not duration:
				return
			total_duration = validate_duration(duration)

			new_time_entry = TimeEntry(start_time = time_log_start_time,
				duration_minutes = total_duration,
				project_id = proj_id, architect_id = arch_id, phase_id = phase_id,
				notes = manual_log_time.notesTextEdit.toPlainText())
			with get_db_connection() as conn:
				cur = conn.cursor()
				add_time_entry(new_time_entry, cur)

			self.model.select()


class ArchitectWindow(QDialog, Ui_AddArchitectDialog):
	def __init__(self) -> None:
		super(ArchitectWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())

		# set validators on phone and email patterns to sanitize user input
		phone_regex = QRegularExpression(r'\(*(\d{3})\)*(\s|.)?(\d{3})(\s|.)?(\d{4})')
		phone_validator = QRegularExpressionValidator(phone_regex, self.phoneInput)
		self.phoneInput.setValidator(phone_validator)

		email_regex = QRegularExpression(
			r'^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$')
		email_validator = QRegularExpressionValidator(email_regex, self.emailInput)
		self.emailInput.setValidator(email_validator)

	def accept(self) -> None:
		"""Method to verify all forms were entered with correct syntax; 
		set phone to chosen (xxx) xxx-xxxx style"""
		architect_name = self.architectNameInput.text()
		license_number = self.licenseInput.text()

		phone_pattern = re.compile(r'\(*(\d{3})\)*(\s|.)?(\d{3})(\s|.)?(\d{4})')
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
		result = phone_pattern.sub(r"(\g<1>) \g<3>-\g<5>", original_text)
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

		# create no-delete table model and set it on window's TableView
		self.model = NoDeleteTableModel()
		self.model.setTable("architects")

		# set my view state reset function onto the model
		self.model.modelReset.connect(self.applyViewState)
		self.model.layoutChanged.connect(self.applyViewState)

		# set my model on my view
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
			"status" : "Status",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		self.model.select()

		# hide architect_id column
		self.architectsTableView.setColumnHidden(
			self.model.fieldIndex("architect_id"), True)

		# set column widths
		self.architectsTableView.setColumnWidth(1, 150)
		self.architectsTableView.setColumnWidth(2, 100)
		self.architectsTableView.setColumnWidth(3, 120)
		self.architectsTableView.setColumnWidth(4, 200)
		self.architectsTableView.setColumnWidth(5, 150)
		self.architectsTableView.setColumnWidth(6, 80)

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
		
		# set checkbox button to hide inactive architects
		self.hideArchitectCheckBox.stateChanged.connect(self.hideInactiveArchitects)
		
		self.show()

	def hideInactiveArchitects(self, state) -> None:
		# create filter to hide inactive architects and status column
		if state == 2:
			self.model.setFilter("status != 'Inactive'")
			self.model.select()
			self.architectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				True)
			self.architectsTableView.setColumnWidth(1, 165)
			self.architectsTableView.setColumnWidth(2, 115)
			self.architectsTableView.setColumnWidth(3, 135)
			self.architectsTableView.setColumnWidth(4, 215)
			self.architectsTableView.setColumnWidth(5, 170)
	
		else:
			self.model.setFilter("")
			self.model.select()
			self.architectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				False)
			self.architectsTableView.setColumnWidth(1, 150)
			self.architectsTableView.setColumnWidth(2, 100)
			self.architectsTableView.setColumnWidth(3, 120)
			self.architectsTableView.setColumnWidth(4, 200)
			self.architectsTableView.setColumnWidth(5, 150)
			self.architectsTableView.setColumnWidth(6, 80)

	def applyViewState(self) -> None:
		# conditionally hide/show status column based on checkbox
		status_column = self.model.fieldIndex("status")
		if status_column != -1:
			hide_status = self.hideArchitectCheckBox.isChecked()
			self.architectsTableView.setColumnHidden(status_column, hide_status)


class ViewProjects(QWidget, Ui_ViewProjectsWindow):
	def __init__(self, main_window) -> None:
		super(ViewProjects, self).__init__()
		self.main_window = main_window
		self.setupUi(self)
		self.setFixedSize(self.size())

		# create a relational table model and set its relation to the phases table
		self.model = NonDeletableRelationalTableModel()

		self.projectsTableView.setModel(self.model)

		self.model.setTable("projects")
		
		# create a relation between 'projects' table and 'phases' with dropdown menu
		relation = QSqlRelation("phases", "phase_id", "project_phase")
		self.model.setRelation(self.model.fieldIndex("current_phase_id"), relation)

		self.projectsTableView.setItemDelegate(QSqlRelationalDelegate(
			self.projectsTableView))


		# set my view state reset function onto the model
		self.model.modelReset.connect(self.applyViewState)
		self.model.layoutChanged.connect(self.applyViewState)

		# allow editing of project information
		self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)

		# create and set column headers
		column_titles = {
			"project_name" : "Project Name",
			"client_name" : "Client Name",
			"client_address" : "Project Address",
			"start_date" : "Start Date",
			"current_phase_id" : "Current Phase",
			"status" : "Status",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		self.model.select()

		# hide project_id column
		self.projectsTableView.setColumnHidden(
			self.model.fieldIndex("project_id"), True)

		self.model.setFilter("project_id > 0")

		# set column widths
		self.projectsTableView.setColumnWidth(1, 150)
		self.projectsTableView.setColumnWidth(2, 160)
		self.projectsTableView.setColumnWidth(3, 320)
		self.projectsTableView.setColumnWidth(4, 90)
		self.projectsTableView.setColumnWidth(5, 180)
		self.projectsTableView.setColumnWidth(6, 80)

		# set original sort by project name
		index = self.model.fieldIndex("project_name")
		self.projectsTableView.sortByColumn(index, Qt.AscendingOrder)

		# allow table to be sorted by clicking top header tabs
		self.projectsTableView.setSortingEnabled(True)

		# allow only chosen options for status column combo box
		status_delegate = StatusDelegate(PROJECT_STATUSES, self.projectsTableView)
		status_column = self.model.fieldIndex("status")
		self.projectsTableView.setItemDelegateForColumn(status_column, 
			status_delegate)

		# set checkbox button to show completed projects
		self.hideProjectCheckBox.stateChanged.connect(self.hideCompletedProjects)

		# set the main window phases combo box when user changes project phase
		self.model.dataChanged.connect(self.dataChanged)

		self.show()

	def dataChanged(self, topLeft: QModelIndex, bottomRight: QModelIndex, 
		roles: list = None) -> None:
		"""Change the phase combo box on the main window when user updates
		it in the view projects table"""
		# topLeft.column() will read 5 & 0 instead of just 5 because .dataChanged 
		# fires twice -> once for the RelationalTableModel and once for the relation 
		# table. The if only picks up the 2nd which is 0 due to th combo box display 
		if topLeft.column() == 0:
			self.main_window.ProjectsComboBox.model().select()
			setCrossComboBox(self.main_window.ProjectsComboBox, 
				self.main_window.PhasesComboBox, 5)

	def hideCompletedProjects(self, signal) -> None:
		"""create filter to hide completed projects and status column"""
		if signal == 2:
			self.model.setFilter("status != 'Completed'")
			self.model.select()
			self.projectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				True)
			self.projectsTableView.setColumnWidth(1, 170)
			self.projectsTableView.setColumnWidth(2, 180)
			self.projectsTableView.setColumnWidth(3, 340)
			self.projectsTableView.setColumnWidth(4, 90)
			self.projectsTableView.setColumnWidth(5, 202)

		else:
			self.model.setFilter("")
			self.model.select()
			self.projectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				False)
			self.projectsTableView.setColumnWidth(1, 150)
			self.projectsTableView.setColumnWidth(2, 160)
			self.projectsTableView.setColumnWidth(3, 320)
			self.projectsTableView.setColumnWidth(4, 90)
			self.projectsTableView.setColumnWidth(5, 180)
			self.projectsTableView.setColumnWidth(6, 80)

		self.model.select()

	def applyViewState(self) -> None:
		# conditionally hide/show status column based on checkbox
		status_column = self.model.fieldIndex("status")
		if status_column != -1:
			hide_status = self.hideProjectCheckBox.isChecked()
			self.projectsTableView.setColumnHidden(status_column, hide_status)


class ViewTimeEntries(QWidget, Ui_ViewTimeEntriesWindow):
	def __init__(self) -> None:
		super(ViewTimeEntries, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())

		# create a relational table model and set its relation to the phases table
		self.model = TimeEntriesRelationalTableModel()
		self.timeEntriesTableView.setModel(self.model)
		self.model.setTable("time_entries")

		# allow table to be sorted by clicking top header tabs
		self.timeEntriesTableView.setSortingEnabled(True)

		# allow editing of time_entries information
		self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)

		# add a relation between 'time_entries' table and 'phases' with dropdown menu
		phase_relation = QSqlRelation("phases", "phase_id", "project_phase")
		self.model.setRelation(self.model.fieldIndex("phase_id"), phase_relation)

		# add relation between 'time_entries' table and 'architects' with dropdown menu
		arch_relation = QSqlRelation("architects", "architect_id", "name")
		self.model.setRelation(self.model.fieldIndex("architect_id"), arch_relation)

		# add relation between 'time_entries' table and 'projects' with dropdown menu
		project_relation = QSqlRelation("projects", "project_id", "project_name")
		self.model.setRelation(self.model.fieldIndex("project_id"), project_relation)

		self.timeEntriesTableView.setItemDelegate(QSqlRelationalDelegate(
			self.timeEntriesTableView))

		# set duration delegate
		duration_column_index = self.model.fieldIndex("duration_minutes")
		self.timeEntriesTableView.setItemDelegateForColumn(
			duration_column_index, DurationDelegate(
				self.timeEntriesTableView))

		# set start time delegate
		start_time_column_index = self.model.fieldIndex("start_time")
		self.timeEntriesTableView.setItemDelegateForColumn(
			start_time_column_index, TimeStartDelegate(
				self.timeEntriesTableView))

		# create and set column headers
		column_titles = {
			"project_id" : "Project Name",
			"architect_id" : "Architect's Name",
			"phase_id" : "Project Phase",
			"start_time" : "Start Time",
			"duration_minutes" : "Duration",
			"notes" : "Notes",
			"invoice_id" : "Invoice Number",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		self.model.select()

		# hide time_entry_id column
		self.timeEntriesTableView.setColumnHidden(
			self.model.fieldIndex("time_entry_id"), True)

		header = self.timeEntriesTableView.horizontalHeader()
		header.moveSection(1, 2)
		header.moveSection(7, 6)

		# set original sort by start time
		index = self.model.fieldIndex("start_time")
		self.timeEntriesTableView.sortByColumn(index, Qt.DescendingOrder)

		# set column widths
		self.timeEntriesTableView.setColumnWidth(1, 140)
		self.timeEntriesTableView.setColumnWidth(2, 140)
		self.timeEntriesTableView.setColumnWidth(3, 180)
		self.timeEntriesTableView.setColumnWidth(4, 152)
		self.timeEntriesTableView.setColumnWidth(5, 80)
		self.timeEntriesTableView.setColumnWidth(6, 565)
		self.timeEntriesTableView.setColumnWidth(7, 100)

		# click box activation
		self.hideInvoicedCheckBox.stateChanged.connect(self.hideInvoicedTimes)

		self.show()

	def hideInvoicedTimes(self, signal):
		"""Filter out time log entries attached to an invoice"""
		if signal == 2:
			self.model.setFilter("invoice_id IS NULL")
			self.model.select()
			self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
				"invoice_id"), True)
			self.timeEntriesTableView.setColumnWidth(1, 155)
			self.timeEntriesTableView.setColumnWidth(2, 155)
			self.timeEntriesTableView.setColumnWidth(3, 180)
			self.timeEntriesTableView.setColumnWidth(4, 170)
			self.timeEntriesTableView.setColumnWidth(5, 100)
			self.timeEntriesTableView.setColumnWidth(6, 597)

		else:
			self.model.setFilter("")
			self.model.select()
			self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
				"invoice_id"), False)
			self.timeEntriesTableView.setColumnWidth(1, 140)
			self.timeEntriesTableView.setColumnWidth(2, 140)
			self.timeEntriesTableView.setColumnWidth(3, 180)
			self.timeEntriesTableView.setColumnWidth(4, 152)
			self.timeEntriesTableView.setColumnWidth(5, 80)
			self.timeEntriesTableView.setColumnWidth(6, 565)
			self.timeEntriesTableView.setColumnWidth(7, 100)

		self.model.select()


class TimerDisplay(QLCDNumber):
	def __init__(self, parent = None):
		super().__init__(parent)

		QTimer.singleShot(0, lambda: self.display("   00:00"))
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.update_lcd)
		self.timer.start()

	def update_lcd(self):
		elapsed_time = self.parent().time_log.elapsedTime()
		qt_time = QTime(0, 0, 0).addSecs(int(elapsed_time))
		self.display(qt_time.toString("   hh:mm"))

# Import ui.TimeLogger after TimerDisplay to stop circular import
from ui.TimeLogger import Ui_TimeLoggerWindow


class TimeLogger(QWidget, Ui_TimeLoggerWindow):
	def __init__(self, main_window) -> None:
		super(TimeLogger, self).__init__()
		self.main_window = main_window
		self.setupUi(self)
		self.setFixedSize(self.size())

		self.architect_model = QSqlTableModel()
		self.architect_model.setTable("architects")
		self.architect_model.select()
		self.ArchitectComboBox.setModel(self.architect_model)
		self.ArchitectComboBox.setModelColumn(1)				
		setLinkedComboBox(self.main_window.ArchitectsComboBox,
			self.ArchitectComboBox)

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.select()
		self.ProjectComboBox.setModel(self.project_model)
		self.ProjectComboBox.setModelColumn(1)					
		setLinkedComboBox(self.main_window.ProjectsComboBox,
			self.ProjectComboBox)
		
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.select()
		self.PhaseComboBox.setModel(self.phase_model)
		self.PhaseComboBox.setModelColumn(1)
		setLinkedComboBox(self.main_window.PhasesComboBox, 
			self.PhaseComboBox)

		self.PhaseComboBox.currentIndexChanged.connect(self.phaseChanged)
		self.ProjectComboBox.currentIndexChanged.connect(self.projectChanged)

		# link buttons
		self.startPauseTimer.clicked.connect(self.startPauseTime)
		self.stopTimer.clicked.connect(self.stopTime)

		self.time_log = TimeLog()

		self.show()

	def projectChanged(self) -> None:
		"""Method to set phase combo box to phase attached to project"""
		self.PhaseComboBox.blockSignals(True)
		setCrossComboBox(self.ProjectComboBox, self.PhaseComboBox, 5)
		
		# Block phases combo box if proj_id is for administrative work
		proj_index = self.ProjectComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		if proj_id < 0:
			self.PhaseComboBox.setEnabled(False)
		else:
			self.PhaseComboBox.setEnabled(True)

		self.PhaseComboBox.blockSignals(False)

	def phaseChanged(self):
		# Get current index and phase_id from phases combo box
		phase_index = self.PhaseComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))

		# Set project ComboBox and disable phase ComboBox if phase is 
		# 	Business Development or Administration
		if phase_id in (8, 9):
			self.PhaseComboBox.setEnabled(False)
			if phase_id == 8:
				self.ProjectComboBox.setCurrentIndex(1)
			else:
				self.ProjectComboBox.setCurrentIndex(0)
			return
		else:
			self.PhaseComboBox.setEnabled(True)

	def startPauseTime(self):
		if self.time_log.timer_state == "inactive":
			self.time_log.timer_state = "running"
			self.time_log.start_time = datetime.now()
			self.startPauseTimer.setText("PAUSE")
			self.timer.setStyleSheet("QLCDNumber {color : #35B5AC;}")
		elif self.time_log.timer_state == "running":
			self.time_log.timer_state = "paused"
			self.startPauseTimer.setText("RESUME")
			self.time_log.pause_start_time = datetime.now()
			self.timer.setStyleSheet("QLCDNumber {color : #008080;}")
		else:
			self.time_log.total_pause_duration += (datetime.now() - 
				self.time_log.pause_start_time).total_seconds()
			self.time_log.timer_state = "running"
			self.startPauseTimer.setText("PAUSE")
			self.time_log.pause_start_time = 0
			self.timer.setStyleSheet("QLCDNumber {color : #35B5AC;}")

	def stopTime(self):
		if self.time_log.start_time == 0:
			self.main_window.showNormal()
			self.close()
			return
		self.timer.timer.stop()
		end_time = datetime.now()
		total_time = 0
		if self.time_log.timer_state == "running":
			self.time_log.timer_state = "paused"
		total_time = ((end_time - self.time_log.start_time).total_seconds() - 
			self.time_log.total_pause_duration)
		# Convert to int to store in database
		start_time = int(self.time_log.start_time.timestamp())
		
		total_minutes = total_time // 60
		quarter_hours = total_minutes // 15
		if total_minutes % 15 > 0:
			quarter_hours += 1
		total_time_logged = quarter_hours * 15

		if total_time_logged == 0:
			self.main_window.showNormal()
			self.close()
			return

		# Pop up notes dialog
		self.timeNotes = TimeEntriesNotesWindow()
		self.timeNotes.exec()

		arch_index = self.ArchitectComboBox.currentIndex()
		arch_id = self.architect_model.data(self.architect_model.index(arch_index, 0))

		phase_index = self.PhaseComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))

		if phase_id == 8:
			proj_id = -1
		elif phase_id == 9:
			proj_id = -2
		else:
			proj_index = self.ProjectComboBox.currentIndex()
			proj_id = self.project_model.data(self.project_model.index(proj_index, 0))

		time_notes = self.timeNotes.notesTextEdit.toPlainText()

		# Create TimeEntry object with created data
		new_time_entry = TimeEntry(start_time = start_time, 
			duration_minutes = total_time_logged, project_id = proj_id, 
			architect_id = arch_id, phase_id = phase_id, notes = time_notes)

		with get_db_connection() as conn:
			cur = conn.cursor()
			add_time_entry(new_time_entry, cur)

		self.main_window.showNormal()
		self.close()

class TimeLog():
	def __init__(self):
		self.timer_state = "inactive"
		self.total_time = 0
		self.start_time = 0
		self.pause_start_time = 0
		self.total_pause_duration = 0

	def elapsedTime(self):
		if self.timer_state == "running":
			self.total_time = ((datetime.now() - self.start_time).total_seconds()
				- self.total_pause_duration)
		elif self.timer_state == "paused":
			self.total_time = ((self.pause_start_time - self.start_time).total_seconds()
				- self.total_pause_duration)
		return self.total_time

class TimeEntriesNotesWindow(QDialog, Ui_TimeNotesDialog):
	def __init__(self):
		super(TimeEntriesNotesWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())


class ManualTimeLogger(QDialog, Ui_AddTimeDialog):
	"""Class for a user to manually input a time entry with duration validation"""
	def __init__(self, main_window) -> None:
		super(ManualTimeLogger, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.main_window = main_window
		
		# Set models
		self.architect_model = QSqlTableModel()
		self.architect_model.setTable("architects")
		self.architect_model.select()
		self.ArchitectComboBox.setModel(self.architect_model)
		self.ArchitectComboBox.setModelColumn(1)				
		setLinkedComboBox(self.main_window.ArchitectsComboBox,
			self.ArchitectComboBox)

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.select()
		self.ProjectComboBox.setModel(self.project_model)
		self.ProjectComboBox.setModelColumn(1)					
		setLinkedComboBox(self.main_window.ProjectsComboBox,
			self.ProjectComboBox)
		
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.select()
		self.PhaseComboBox.setModel(self.phase_model)
		self.PhaseComboBox.setModelColumn(1)
		setLinkedComboBox(self.main_window.PhasesComboBox, 
			self.PhaseComboBox)

		self.ProjectComboBox.currentIndexChanged.connect(self.projectChanged)
		self.PhaseComboBox.currentIndexChanged.connect(self.phaseChanged)

		# Set current date onto the calendar drop down
		self.timeStartDate.setDate(QDate.currentDate())

		# Set current time onto the time edit drop down
		self.timeEdit.setTime(QTime.currentTime())

		# Set validator on duration input
		duration_regex = QRegularExpression(r"^(\d+)?(:\d{0,2})?$")
		validator = QRegularExpressionValidator(duration_regex, self.durationLineEdit)
		self.durationLineEdit.setValidator(validator)

	def projectChanged(self) -> None:
		"""Method to set phase combo box to phase attached to project"""
		self.PhaseComboBox.blockSignals(True)
		setCrossComboBox(self.ProjectComboBox, self.PhaseComboBox, 5)
		
		# Block phases combo box if proj_id is for administrative work
		proj_index = self.ProjectComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		if proj_id < 0:
			self.PhaseComboBox.setEnabled(False)
		else:
			self.PhaseComboBox.setEnabled(True)

		self.PhaseComboBox.blockSignals(False)

	def phaseChanged(self):
		# Get current index and phase_id from phases combo box
		phase_index = self.PhaseComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))

		# Set project ComboBox and disable phase ComboBox if phase is 
		# 	Business Development or Administration
		if phase_id in (8, 9):
			self.PhaseComboBox.setEnabled(False)
			if phase_id == 8:
				self.ProjectComboBox.setCurrentIndex(1)
			else:
				self.ProjectComboBox.setCurrentIndex(0)
			return
		else:
			self.PhaseComboBox.setEnabled(True)

	def accept(self) -> None:
		"""Method to verify all forms were entered with correct syntax"""
		duration_patter = re.compile(r"^(\d+)?(:\d{0,2})?$")
		duration_result = duration_patter.search(self.durationLineEdit.text())
		
		if not duration_result:
			QMessageBox.warning(self, "Invalid Time Duration", 
				"Please Add Event Duration")
			return

		super().accept()

class NoDeleteTableModel(QSqlTableModel):
	"""Class to dissalow deletions of entire rows in table views and to 
	check for valid email address and phone number on user edit"""
	def removeRows(self, row, count, parent=None) -> bool:
		return False

	def setData(self, index, value, role = Qt.EditRole):
		# Get column database names to safetey desired column entries by user
		field_name = self.record().fieldName(index.column())

		# Check Phone Number and Email to make sure they are valid, re-format phone
		if field_name == "phone_number":
			if value:
				phone_pattern = re.compile(
					r'\(*(\d{3})\)*(\s|.)?(\d{3})(\s|.)?(\d{4})$')
				phone_result = phone_pattern.search(value)
				if not phone_result: 
					QMessageBox.warning(None, "Invalid Phone Number", 
						"Invalid Phone Number, Please Correct")
					return False
				else:
					value = phone_pattern.sub(r"(\g<1>) \g<3>-\g<5>", value)

		if field_name == "email":
			if value:
				email_pattern = re.compile(
					r'^[a-zA-Z0-9_.+-]+@[a-zA-z0-9-]+\.[a-zA-Z0-9-.]+$')
				email_result = email_pattern.search(value)
				if not email_result:
					QMessageBox.warning(None, "Invalid Email", "Invalid Email, \
						Please Correct")
					return False

		return super().setData(index, value, role)


class NonDeletableRelationalTableModel(QSqlRelationalTableModel):
	"""Class to dissalow deletions of entire rows in relational table views 
	and to check and reformat date on user edit"""
	def removeRows(self, row, count, parent=None):
		return False

	def setData(self, index, value, role = Qt.EditRole):
		# Get column database names to safetey desired column entries by user
		field_name = self.record().fieldName(index.column())

		# Check start date is a valid date and reformat to chosen syntax
		if field_name == "start_date":
			if value:
				try:
					for fmt in ['%m-%d-%Y', '%m/%d/%Y', '%d-%m-%Y', '%d/%m/%Y']:
						try:
							date_obj = datetime.strptime(value, fmt)
							formatted_date = date_obj.strftime('%m/%d/%Y')
							value = formatted_date
							break
						except ValueError:
							continue
					else:
						QMessageBox.warning(None, "Invalid Date", 
							"Invalid Date, Please Correct")
						return False
				except Exception:
					QMessageBox.warning(None, "Invalid Date", 
							"Invalid Date, Please Correct")
					return False

		return super().setData(index, value, role)

class TimeEntriesRelationalTableModel(QSqlRelationalTableModel):
	"""Class to make invoice_id column read only in ViewTimeEntries window,
	display duration time in hour:minute format instead of total minutes, 
	display start_time as mm/dd/yyyy hh:mm am/pm,
	reformat user duration input from hour:min to total minutes,
	reformat user start_time input from mm/dd/yyyy hh:mm am/pm to total ints"""
	def flags(self, index):
		# Get the default flags
		default_flag = super().flags(index)
		# If its invoice_id column remove the editable flag
		if self.record().fieldName(index.column()) == "invoice_id":
			return default_flag & ~Qt.ItemIsEditable

		return default_flag

	def data(self, index, role = Qt.DisplayRole):
		# Get column database names to change display of time duration
		if role != Qt.DisplayRole:
			return super().data(index, role)

		field_name = self.record().fieldName(index.column())
		value = super().data(index, role)

		# Display duration in hours:minutes
		if field_name == "duration_minutes" and value is not None:
			hour = value // 60
			minute = value % 60
			value = f"{hour:02d}:{minute:02d}"

		# Display start time in month/day/year hour:minute AM/PM
		if field_name == "start_time" and value is not None:
			date_time = datetime.fromtimestamp(value)
			value = date_time.strftime("%m/%d/%Y %I:%M %p")

		return value

	def setData(self, index, value, role = Qt.EditRole):
		field_name = self.record().fieldName(index.column())

		# Reset a user's entered duration from xx:xx to just minutes
		if field_name == "duration_minutes":
			try:
				value = validate_duration(value)
			except ValueError:
				return False

		# Reset a user's entered start date and time to an int
		if field_name == "start_time":
			value = value.replace("-", "/")
			try: 
				date_time = datetime.strptime(value, "%m/%d/%Y %I:%M %p")
			except ValueError:
				try:
					date_time = datetime.strptime(value, "%m/%d/%y %I:%M %p")
				except ValueError:
					QMessageBox.warning(self.parent(), "Invalid Start Date/Time",
						"Invalid Start Date/Time \
						Must Be In Month/Day/Year Hour:Minute AM/PM Format")
					return False
			value = int(date_time.timestamp())

		return super().setData(index, value, role)


class StatusDelegate(QStyledItemDelegate):
	"""Class to allow drop down ComboBoxes for table cells where only a specific
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

class DurationDelegate(QStyledItemDelegate):
	"""Class to validate manual time duration input by user to allow
	total minutes or hour:minutes input"""
	def createEditor(self, parent, options, index):
		editor = QLineEdit(parent)
		regex = QRegularExpression(r"^(\d+)?(:\d{2})?$")
		validator = QRegularExpressionValidator(regex, editor)
		editor.setValidator(validator)

		return editor

class TimeStartDelegate(QStyledItemDelegate):
	"""Class to validate manual date/time input by user"""
	def createEditor(self, parent, options, index):
		editor = QLineEdit(parent)
		regex = QRegularExpression(
			r"^\d{1,2}(-|\/)\d{1,2}(-|\/)(\d{2}|\d{4})\s+(([0]?[1-9])|([1][0-2]))\
			:[0-5]\d\s(AM|PM|am|pm])$")
		validator = QRegularExpressionValidator(regex, editor)
		editor.setValidator(validator)

		return editor


def setCrossComboBox(source_combo: QComboBox, target_combo: QComboBox, 
	column: int = 1) -> None:
	"""Function to pull the information from one combo box and populate 
	it on a combo box elsewhere in the program; column parameter is the column
	on the source_combo table you want to match to your target_combo's table"""
	row = source_combo.currentIndex()
	model = source_combo.model()
	item_id = model.data(model.index(row, column))

	matches = target_combo.model().match(target_combo.model().index(0,0),
		Qt.EditRole, item_id)
	if matches:
		row = matches[0].row()
		target_combo.setCurrentIndex(row)

def setLinkedComboBox(source_combo: QComboBox, target_combo: QComboBox) -> None:
	"""Function to set a target ComboBox to the chosen value in the target,
	both combo boxes must hold the same table and column"""
	target_combo.setCurrentIndex(source_combo.currentIndex())


def validate_duration(duration: str) -> int:
	"""Function to parse duration input and return it as a total minutes int
	rounded up to the next 15 minute increment"""
	if not duration:
		return
	minutes = 0
	hours = 0
	if isinstance (duration, str) and ":" in duration:
		if duration.count(":") != 1:
			raise ValueError
		if duration[0] == ":":
			minutes = int(duration[1:])
		else:
			hours, minutes = duration.split(":")
			hours = int(hours)
			minutes = int(minutes)
	else:
		minutes = int(duration)
	quarter_hours = minutes // 15
	if minutes % 15:
		quarter_hours += 1
	minutes = quarter_hours * 15

	return hours * 60 + minutes