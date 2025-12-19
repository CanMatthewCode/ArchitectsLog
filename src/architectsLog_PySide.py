# PySide6 functions for the Architect's Log

import sys
import os
import re
from datetime import datetime

from PySide6.QtWidgets import (QMainWindow, QApplication, QDialog, QMessageBox,
	QStyledItemDelegate, QComboBox, QWidget, QLCDNumber)
from PySide6.QtSql import (QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, 
	QSqlRelation, QSqlRelationalDelegate)
from PySide6.QtCore import Qt, QDate, QModelIndex, QTimer, QTime

from ui.MainWindow import Ui_MainWindow
from ui.AddArchitect import Ui_AddArchitectDialog
from ui.AddProject import Ui_AddProjectDialog
from ui.ViewArchitects import Ui_ViewArchitectsWindow
from ui.ViewProjects import Ui_ViewProjectsWindow
from ui.ViewTimeEntries import Ui_ViewTimeEntries

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

		# enable button clicks
		self.AddArchitectBtn.clicked.connect(self.addArchitect)
		self.AddProjectBtn.clicked.connect(self.addProject)
		self.ViewArchitectsBtn.clicked.connect(self.viewArchitects)
		self.ViewProjectsBtn.clicked.connect(self.viewProjects)
		self.LogTimeBtn.clicked.connect(self.logTime)

		self.show()

	def projectChanged(self) -> None:
		"""Method to set phase combo box to phase attached to project"""
		setCrossComboBox(self.ProjectsComboBox, self.PhasesComboBox, 1)
		self.phase_model.select()


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
				company_name = arch_window.companyNameInput.text())
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
			start_date_str = start_date.toString("MM-dd-yyyy")
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
		include inactive architects"""
		self.view_arch_window = ViewArchitects()

	def viewProjects(self) -> None:
		"""Method to view all projects in database table, click button to
		include completed projects"""
		self.view_proj_window = ViewProjects(self)

	def logTime(self) -> None:
		"""Method to activate TimeLogger window and store resulting 
		TimeEntry object in time_entries database"""
		self.log_time = TimeLogger(self)
		self.showMinimized()


		

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
			self.architectsTableView.setColumnWidth(1, 165)
			self.architectsTableView.setColumnWidth(2, 115)
			self.architectsTableView.setColumnWidth(3, 135)
			self.architectsTableView.setColumnWidth(4, 215)
			self.architectsTableView.setColumnWidth(5, 170)
	
		else:
			self.model.setFilter("")
			self.model.select()
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
		self.model = QSqlRelationalTableModel()

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
		self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

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

		# set column widths
		self.projectsTableView.setColumnWidth(1, 150)
		self.projectsTableView.setColumnWidth(2, 160)
		self.projectsTableView.setColumnWidth(3, 320)
		self.projectsTableView.setColumnWidth(4, 90)
		self.projectsTableView.setColumnWidth(5, 180)
		self.projectsTableView.setColumnWidth(6, 60)

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
			self.projectsTableView.setColumnWidth(1, 165)
			self.projectsTableView.setColumnWidth(2, 175)
			self.projectsTableView.setColumnWidth(3, 335)
			self.projectsTableView.setColumnWidth(4, 90)
			self.projectsTableView.setColumnWidth(5, 195)

		else:
			self.model.setFilter("")
			self.model.select()
			self.projectsTableView.setColumnWidth(1, 150)
			self.projectsTableView.setColumnWidth(2, 160)
			self.projectsTableView.setColumnWidth(3, 320)
			self.projectsTableView.setColumnWidth(4, 90)
			self.projectsTableView.setColumnWidth(5, 180)
			self.projectsTableView.setColumnWidth(6, 60)

		self.model.select()

	def applyViewState(self) -> None:
		# conditionally hide/show status column based on checkbox
		status_column = self.model.fieldIndex("status")
		if status_column != -1:
			hide_status = self.hideProjectCheckBox.isChecked()
			self.projectsTableView.setColumnHidden(status_column, hide_status)


class TimerDisplay(QLCDNumber):
	def __init__(self, parent = None):
		super().__init__(parent)

		QTimer.singleShot(0, lambda: self.display("   00:00"))
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.update_lcd)
		self.timer.start()

	def update_lcd(self):
		elapsed_time = self.parent().time_log.elapsed_time()
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
		setLinkedComboBox(self.main_window.ArchitectsComboBox,
			self.ArchitectComboBox)
		
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.select()
		self.PhaseComboBox.setModel(self.phase_model)
		self.PhaseComboBox.setModelColumn(1)
		setLinkedComboBox(self.main_window.PhasesComboBox, 
			self.PhaseComboBox)

		# link buttons
		self.startPauseTimer.clicked.connect(self.start_pause_time)
		self.stopTimer.clicked.connect(self.stop_time)

		self.time_log = TimeLog()

		self.show()

	def start_pause_time(self):
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

	def stop_time(self):
		self.main_window.showNormal()
		self.close()

class TimeLog():
	def __init__(self):
		self.timer_state = "inactive"
		self.total_time = 0
		self.start_time = 0
		self.end_time = 0
		self.pause_start_time = 0
		self.total_pause_duration = 0

	def elapsed_time(self):
		if self.timer_state == "running":
			self.total_time = ((datetime.now() - self.start_time).total_seconds()
				- self.total_pause_duration)
		elif self.timer_state == "paused":
			self.total_time = ((self.pause_start_time - self.start_time).total_seconds()
				- self.total_pause_duration)
		return self.total_time



class NoDeleteTableModel(QSqlTableModel):
	"""New Class to dissalow deletions of entire rows in my table views"""
	def removeRows(self, row, count, parent=None) -> bool:
		return False


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


def setCrossComboBox(source_combo: QComboBox, target_combo: QComboBox, 
	column: int = 1) -> None:
	"""Function to pull the information from one combo box and populate 
	it on a combo box elsewhere in the program; column parameter is the column
	on the source_combo table you want to match to your target_combo's table"""
	row = source_combo.currentIndex()
	model = source_combo.model()
	item_id = model.data(model.index(row, column))
	matches = target_combo.model().match(target_combo.model().index(0,0),
		Qt.DisplayRole, item_id)
	if matches:
		row = matches[0].row()
		target_combo.setCurrentIndex(row)

def setLinkedComboBox(source_combo: QComboBox, target_combo: QComboBox) -> None:
	"""Function to set a target ComboBox to the chosen value in the target"""
	target_combo.setCurrentIndex(source_combo.currentIndex())