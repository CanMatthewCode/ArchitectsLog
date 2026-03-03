# PySide6 functions for the Architect's Log

import re
from datetime import datetime, timedelta
import random
from typing import Optional

from PySide6.QtWidgets import (QMainWindow, QApplication, QDialog, QMessageBox,
	QStyledItemDelegate, QLineEdit, QDateTimeEdit, QDateEdit, QComboBox, QWidget,
	QLCDNumber, QStyleOptionButton, QStyle, QAbstractItemView, QHeaderView)
from PySide6.QtSql import (QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, 
	QSqlRelation, QSqlRelationalDelegate, QSqlQuery)
from PySide6.QtCore import (Qt, QDate, QDateTime, QModelIndex, QTimer, QTime, 
	QRegularExpression, QEvent, QRect)
from PySide6.QtGui import QRegularExpressionValidator, QAction, QKeySequence

from ui.MainWindow import Ui_MainWindow
from ui.AddArchitect import Ui_AddArchitectDialog
from ui.AddProject import Ui_AddProjectDialog
from ui.ViewArchitects import Ui_ViewArchitectsWindow
from ui.ViewProjects import Ui_ViewProjectsWindow
from ui.ViewTimeEntries import Ui_ViewTimeEntriesWindow
from ui.TimeNotes import Ui_TimeNotesDialog
from ui.AddTimeEntry import Ui_AddTimeDialog
from ui.ViewInvoices import Ui_ViewInvoicesWindow
from ui.AddInvoiceNumber import Ui_AddInvoiceDialog
from ui.DeleteInvoiceWarning import Ui_DeleteInvoiceDialog
from ui.DeleteTimeEntryWarning import Ui_DeleteTimeEntryDialog
from ui.CreateDatabaseWarning import Ui_CreateDatabaseDialog
from ui.LoadDatabaseWarning import Ui_LoadDatabaseDialog
from ui.ViewInvoice import Ui_ViewInvoiceWindow
from ui.Analytics import Ui_AnalyticsWindow
from ui.PhaseHoursAnalytics import Ui_PhaseHoursWindow
from ui.PhaseAveragesAnalytics import Ui_PhaseAveragesWindow
from ui.ProjectsOverTime import Ui_ProjectsOverTimeWindow

from architectsLog_classes import Architect, Project, TimeEntry 
from architectsLog_constants import (PHASES, ARCHITECT_STATUSES, PROJECT_STATUSES,
	INVOICE_STATUSES, ADMIN, BUSDEV)
from architectsLog_db import (get_db_connection, add_architect, add_project,
	add_time_entry, get_most_recent_archid_and_projid,
	get_most_recent_project_phase, load_invoice_ids_no_time_entries, 
	update_project, delete_invoice)
from architectsLog_utils import new_database, load_database, WelcomeSign
from architectsLog_pdf import generate_invoice_pdf

from architectsLog_analytics_db import (phase_duration_by_project, 
	phase_time_entries_by_project, phase_duration_all_projects, 
	phase_duration_by_project_with_name, total_number_of_projects_by_phase,
	project_ids_over_time_period, earliest_start_date)

def initialize_database(db_file: str) -> None:
	"""Open the persistent global Qt connection to the database"""
	db = QSqlDatabase.addDatabase("QSQLITE")
	db.setDatabaseName(db_file)
	if not db.open():
		raise Exception("Failed to open database")

class MainWindow(QMainWindow, Ui_MainWindow):
	def __init__(self) -> None:
		super(MainWindow, self).__init__()
		self.setupUi(self) 
		self.setFixedSize(self.size())

		self.setWindowTitle("The Architect's Log")

		self.view_arch_window = None
		self.view_proj_window = None
		self.view_time_entries_window = None
		self.view_invoices_window = None
		self.analytics_window = None

		self.architect_model = QSqlTableModel()
		self.architect_model.setTable("architects")
		self.architect_model.select()
		self.ArchitectsComboBox.setModel(self.architect_model)
		self.ArchitectsComboBox.setModelColumn(1)				# Index 1 is arch name

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter("status = 'Active'")
		self.project_model.select()
		self.ProjectsComboBox.setModel(self.project_model)
		self.ProjectsComboBox.setModelColumn(1)					# Index 1 is proj name
		
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.select()
		self.PhasesComboBox.setModel(self.phase_model)
		self.PhasesComboBox.setModelColumn(1)					# Index 1 is phase name

		setCrossComboBox(self.ProjectsComboBox, self.PhasesComboBox, 5)
		self.ProjectsComboBox.currentIndexChanged.connect(self.projectChanged)
		self.PhasesComboBox.currentIndexChanged.connect(self.phaseChanged)

		# Set architect and project combo boxes on most recently added time entry
		with get_db_connection() as conn:
			cur = conn.cursor()
			arch_proj_ids = get_most_recent_archid_and_projid(cur)
		if arch_proj_ids:
			arch_id, proj_id = arch_proj_ids
			arch_match = self.architect_model.match(self.architect_model.index(0,0), 
				Qt.EditRole, arch_id, 1, Qt.MatchFlags(Qt.MatchExactly))
			if arch_match:
				row = arch_match[0].row()
				self.ArchitectsComboBox.setCurrentIndex(row)
			proj_match = self.project_model.match(self.project_model.index(0,0),
				Qt.EditRole, proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
			if proj_match:
				row = proj_match[0].row()
				self.ProjectsComboBox.setCurrentIndex(row)
		else:
			self.ProjectsComboBox.setCurrentIndex(1)

		new_architect_action = QAction("Add Architect", self)
		new_architect_action.triggered.connect(self.addArchitect)
		new_architect_action.setShortcut(QKeySequence("Ctrl+A"))
		new_project_action = QAction("Add Project", self)
		new_project_action.triggered.connect(self.addProject)
		new_project_action.setShortcut(QKeySequence("Ctrl+P"))
		log_time_action = QAction("Log Time", self)
		log_time_action.triggered.connect(self.logTime)
		log_time_action.setShortcut(QKeySequence("Ctrl+L"))
		add_time_action = QAction("Add Time", self)
		add_time_action.triggered.connect(self.addTime)
		add_time_action.setShortcut(QKeySequence("Ctrl+T"))

		view_architects_action = QAction("View Architects", self)
		view_architects_action.triggered.connect(self.viewArchitects)
		view_architects_action.setShortcut(QKeySequence("Ctrl+Shift+A"))
		view_projects_action = QAction("View Projects", self)
		view_projects_action.triggered.connect(self.viewProjects)
		view_projects_action.setShortcut(QKeySequence("Ctrl+Shift+P"))
		view_time_entries_action = QAction("View Time Logs", self)
		view_time_entries_action.triggered.connect(self.viewTimeEntries)
		view_time_entries_action.setShortcut(QKeySequence("Ctrl+Shift+L"))
		view_invoices_action = QAction("View Invoices", self)
		view_invoices_action.triggered.connect(self.viewInvoices)
		view_invoices_action.setShortcut(QKeySequence("Ctrl+Shift+I"))
		view_analytics_action = QAction("Analytics", self)
		view_analytics_action.triggered.connect(self.viewAnalytics)
		view_analytics_action.setShortcut(QKeySequence("Ctrl+Shift+N"))
		view_welcome_sign = QAction("Read Welcome Information", self)
		view_welcome_sign.triggered.connect(self.viewWelcome)

		new_database_action = QAction("Create New Database", self)
		new_database_action.triggered.connect(self.newDatabase)
		load_database_action = QAction("Load Existing Database", self)
		load_database_action.triggered.connect(self.loadDatabase)


		close_window_action = QAction("Close Window", self)
		close_window_action.triggered.connect(self.closeActiveWindow)
		close_window_action.setShortcut(QKeySequence.StandardKey.Close)
		close_window_action.setShortcutContext(Qt.ShortcutContext.ApplicationShortcut)
		self.addAction(close_window_action)

		menu = self.menuBar()
		file_menu = menu.addMenu("File")
		file_menu.addAction(new_architect_action)
		file_menu.addAction(new_project_action)
		file_menu.addAction(log_time_action)
		file_menu.addAction(add_time_action)
		file_menu.addSeparator()
		file_menu.addAction(new_database_action)
		file_menu.addAction(load_database_action)
		view_menu = menu.addMenu("Views")
		view_menu.addAction(view_architects_action)
		view_menu.addAction(view_projects_action)
		view_menu.addAction(view_time_entries_action)
		view_menu.addAction(view_invoices_action)
		view_menu.addSeparator()
		view_menu.addAction(view_analytics_action)
		view_menu.addSeparator()
		view_menu.addAction(view_welcome_sign)

		# enable button clicks
		self.AddArchitectBtn.clicked.connect(new_architect_action.trigger)
		self.AddProjectBtn.clicked.connect(new_project_action.trigger)
		self.LogTimeBtn.clicked.connect(log_time_action.trigger)
		self.AddTimeBtn.clicked.connect(add_time_action.trigger)

		self.ViewArchitectsBtn.clicked.connect(view_architects_action.trigger)
		self.ViewProjectsBtn.clicked.connect(view_projects_action.trigger)
		self.ViewTimeLogsBtn.clicked.connect(view_time_entries_action.trigger)
		self.ViewInvoicesBtn.clicked.connect(view_invoices_action.trigger)

		self.AnalyticsBtn.clicked.connect(view_analytics_action.trigger)

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
		if phase_id in (ADMIN, BUSDEV):
			self.PhasesComboBox.setEnabled(False)
			if phase_id == ADMIN:
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

	# Button methods
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
			phase_index = proj_window.phaseComboBox.currentIndex()
			model = proj_window.phaseComboBox.model()
			phase_id = model.data(model.index(phase_index, 0))
			# Turn the QDate object into a string
			start_date = proj_window.projectStartDate.date()
			start_date_str = start_date.toString("MM/dd/yyyy")
			project_date = datetime.strptime(start_date_str, "%m/%d/%Y")
			int_date = int(project_date.timestamp())
			new_project = Project(project_name = proj_window.projectNameInput.text(),
				client_name = proj_window.clientInput.text(),
				client_address = proj_window.projectAddressInput.text(),
				start_date = int_date,
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
		self.view_time_entries_window = ViewTimeEntries(self)

	def viewInvoices(self) -> None:
		"""Method to view all invoices from the database table"""
		self.view_invoices_window = ViewInvoices()

	def viewAnalytics(self) -> None:
		"""Method to access the analytics window"""
		self.analytics_window = ViewAnalytics()

	def viewWelcome(self) -> None:
		"""Method to access the intoructory text"""
		self.view_welcome_sign = WelcomeSign()
		self.view_welcome_sign.exec()

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

			if phase_id == ADMIN:
				proj_id = -1
			elif phase_id == BUSDEV:
				proj_id = -2
			else:
				proj_index = manual_log_time.ProjectComboBox.currentIndex()
				proj_model = manual_log_time.ProjectComboBox.model()
				proj_id = proj_model.data(proj_model.index(proj_index, 0))

			# Get start date and time and turn into a timestamp int for database
			#start_date = manual_log_time.timeStartDate.date()
			start_time = manual_log_time.timeStartEdit.dateTime()
			end_time = manual_log_time.timeEndEdit.dateTime()
			
			qDatetimeStart = QDateTime(start_time)
			pyDatetimeStart = qDatetimeStart.toPython()
			time_log_start_time = int(pyDatetimeStart.timestamp())

			qDatetimeEnd = QDateTime(end_time)
			pyDateTimeEnd = qDatetimeEnd.toPython()
			time_log_end_time = int(pyDatetimeEnd.timestamp())

			# Get duration input and validate it with validation function
			duration = pyDateTimeEnd - pyDatetimeStart
			duration = duration.total_seconds() / 60
			total_duration = validateDuration(duration)

			new_time_entry = TimeEntry(start_time = time_log_start_time,
				end_time = time_log_end_time, duration_minutes = total_duration,
				project_id = proj_id, architect_id = arch_id, phase_id = phase_id,
				notes = manual_log_time.notesTextEdit.toPlainText(), invoice_id = 0)
			with get_db_connection() as conn:
				cur = conn.cursor()
				add_time_entry(new_time_entry, cur)

			if self.view_time_entries_window is not None:
				self.view_time_entries_window.model.select()

	def closeActiveWindow(self) -> None:
		window = QApplication.activeWindow()
		if window:
			window.close()

	def newDatabase(self) -> None:
		create_new_database = CreateNewDatabase()
		result = create_new_database.exec()
		if result == QDialog.Accepted:
			new_database()

	def loadDatabase(self) -> None:
		load_old_database = LoadOldDatabase()
		result = load_old_database.exec()
		if result == QDialog.Accepted:
			load_database()

class ArchitectWindow(QDialog, Ui_AddArchitectDialog):
	def __init__(self) -> None:
		super(ArchitectWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Add Architect")

		# Set validators on phone and email patterns to sanitize user input
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
		 
		# Modify phone number to fix (xxx) xxx.xxxx style
		original_text = self.phoneInput.text()
		result = phone_pattern.sub(r"(\g<1>) \g<3>-\g<5>", original_text)
		self.phoneInput.setText(result)

		super().accept()


class ProjectWindow(QDialog, Ui_AddProjectDialog):
	def __init__(self) -> None:
		super(ProjectWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Add Project")

		self.projectStartDate.setDate(QDate.currentDate())

		# Set first phase to the Phase QComboBox
		self.phase_model = QSqlTableModel()
		self.phase_model.setTable("phases")
		self.phase_model.setFilter("phase_id < 8")
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


#		~~~Table View Windows~~~

class ViewArchitects(QWidget, Ui_ViewArchitectsWindow):
	def __init__(self) -> None:
		super(ViewArchitects, self).__init__()
		self.setupUi(self)
		self.setMinimumSize(self.size())
		header = self.architectsTableView.horizontalHeader()
		header.setSectionResizeMode(QHeaderView.Interactive)
		self.setWindowTitle("Architects")

		# Create no-delete table model and set it on window's TableView
		self.model = ArchitectsTableModel()
		self.model.setTable("architects")

		self.architectsTableView.setModel(self.model)

		# Allow editing of architect information
		self.model.setEditStrategy(QSqlTableModel.OnFieldChange)

		# Create and set column headers
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

		self.architectsTableView.setColumnHidden(
			self.model.fieldIndex("architect_id"), True)

		self.model.setFilter("status != 'Inactive'")
		self.model.select()
		self.architectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
			True)
		self.architectsTableView.setColumnWidth(1, 165)
		self.architectsTableView.setColumnWidth(2, 115)
		self.architectsTableView.setColumnWidth(3, 135)
		self.architectsTableView.setColumnWidth(4, 215)
		self.architectsTableView.setColumnWidth(5, 170)

		# Move license number to after company name
		header = self.architectsTableView.horizontalHeader()
		header.moveSection(5, 2) 			# move company name to 2nd column
		#self.model.select()

		# Set original sort by architect name
		index = self.model.fieldIndex("name")
		self.architectsTableView.sortByColumn(index, Qt.AscendingOrder)

		# Allow table to be sorted by clicking top header tabs
		self.architectsTableView.setSortingEnabled(True)

		# Only allow chosen options for status column - create a combo box and set
		# it on the column for status to allow only acceptable status options
		status_delegate = StatusDelegate(ARCHITECT_STATUSES, self.architectsTableView)
		status_column = self.model.fieldIndex("status")
		self.architectsTableView.setItemDelegateForColumn(status_column, 
			status_delegate)
		
		# Set checkbox button to hide inactive architects
		self.showArchitectCheckBox.stateChanged.connect(self.showInactiveArchitects)
		
		self.show()

	def showInactiveArchitects(self, state) -> None:
		"""Create filter to hide inactive architects and status column"""
		if state == 2:
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
	
		else:
			self.model.setFilter("status != 'Inactive'")
			self.model.select()
			self.architectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				True)
			self.architectsTableView.setColumnWidth(1, 165)
			self.architectsTableView.setColumnWidth(2, 115)
			self.architectsTableView.setColumnWidth(3, 135)
			self.architectsTableView.setColumnWidth(4, 215)
			self.architectsTableView.setColumnWidth(5, 170)


class ViewProjects(QWidget, Ui_ViewProjectsWindow):
	def __init__(self, main_window) -> None:
		super(ViewProjects, self).__init__()
		self.main_window = main_window
		self.setupUi(self)
		self.setMinimumSize(self.size())
		header = self.projectsTableView.horizontalHeader()
		header.setSectionResizeMode(QHeaderView.Interactive)
		self.setWindowTitle("Projects")

		# Create a relational table model and set its relation to the phases table
		self.model = ProjectsRelationalTableModel()

		self.projectsTableView.setModel(self.model)

		self.model.setTable("projects")
		
		# Create a relation between 'projects' table and 'phases' with drop-down menu
		relation = QSqlRelation("phases", "phase_id", "project_phase")
		self.model.setRelation(self.model.fieldIndex("current_phase_id"), relation)

		self.projectsTableView.setItemDelegate(QSqlRelationalDelegate(
			self.projectsTableView))

		# Set start date delegate
		start_date_column_index = self.model.fieldIndex("start_date")
		self.projectsTableView.setItemDelegateForColumn(
			start_date_column_index, CreatedDateDelegate(
				self.projectsTableView))

		self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)

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

		self.projectsTableView.setColumnHidden(
			self.model.fieldIndex("project_id"), True)

		self.model.setFilter("status != 'Completed' and project_id > 0")
		self.model.select()
		self.projectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
			True)
		self.projectsTableView.setColumnWidth(1, 200)
		self.projectsTableView.setColumnWidth(2, 180)
		self.projectsTableView.setColumnWidth(3, 340)
		self.projectsTableView.setColumnWidth(4, 90)
		self.projectsTableView.setColumnWidth(5, 202)

		index = self.model.fieldIndex("project_name")
		self.projectsTableView.sortByColumn(index, Qt.AscendingOrder)

		self.projectsTableView.setSortingEnabled(True)

		# Allow only chosen options for status column combo box
		status_delegate = StatusDelegate(PROJECT_STATUSES, self.projectsTableView)
		status_column = self.model.fieldIndex("status")
		self.projectsTableView.setItemDelegateForColumn(status_column, 
			status_delegate)

		self.showProjectCheckBox.stateChanged.connect(self.showCompletedProjects)

		# Set the main window phases combo box when user changes project phase
		self.model.dataChanged.connect(self.dataChanged)

		self.show()

	def dataChanged(self, topLeft: QModelIndex, bottomRight: QModelIndex, 
		roles: list = None) -> None:
		"""Change the phase combo box on the main window when user updates
		it in the view projects table"""
		# topLeft.column() will read 5 & 0 instead of just 5 because .dataChanged 
		# fires twice -> once for the RelationalTableModel and once for the relation 
		# table. The if only picks up the 2nd which is 0 due to the combo box display 
		if topLeft.column() != 0:
			return

		proj_index = self.main_window.ProjectsComboBox.currentIndex()
		proj_id = self.main_window.project_model.data(
			self.main_window.project_model.index(proj_index, 0))

		self.main_window.ProjectsComboBox.model().select()

		# block and reset the correct project after .select() so it doesn't reset to 0
		self.main_window.ProjectsComboBox.blockSignals(True)
		self.main_window.ProjectsComboBox.setCurrentIndex(proj_index)
		self.main_window.ProjectsComboBox.blockSignals(False)

		with get_db_connection() as conn:
			cur = conn.cursor()
			cur.execute("SELECT current_phase_id FROM projects WHERE project_id = ?",
				(proj_id,))
			result = cur.fetchone()
		if not result:
			return

		new_phase_id = result[0]
		phase_matches = self.main_window.phase_model.match(
			self.main_window.phase_model.index(0,0),
			Qt.EditRole, new_phase_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if phase_matches:
			self.main_window.PhasesComboBox.blockSignals(True)
			self.main_window.PhasesComboBox.setCurrentIndex(phase_matches[0].row())
			self.main_window.PhasesComboBox.blockSignals(False)
		self.main_window.PhasesComboBox.setEnabled(True)

	def showCompletedProjects(self, signal) -> None:
		"""Create filter to hide completed projects and status column"""
		if signal == 2:
			self.model.setFilter("project_id > 0")
			self.model.select()
			self.projectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				False)
			self.projectsTableView.setColumnWidth(1, 200)
			self.projectsTableView.setColumnWidth(2, 160)
			self.projectsTableView.setColumnWidth(3, 320)
			self.projectsTableView.setColumnWidth(4, 90)
			self.projectsTableView.setColumnWidth(5, 180)
			self.projectsTableView.setColumnWidth(6, 80)

		else:
			self.model.setFilter("status != 'Completed' and project_id > 0")
			self.model.select()
			self.projectsTableView.setColumnHidden(self.model.fieldIndex("status"), 
				True)
			self.projectsTableView.setColumnWidth(1, 200)
			self.projectsTableView.setColumnWidth(2, 180)
			self.projectsTableView.setColumnWidth(3, 340)
			self.projectsTableView.setColumnWidth(4, 90)
			self.projectsTableView.setColumnWidth(5, 202)

		self.model.select()


class ViewTimeEntries(QWidget, Ui_ViewTimeEntriesWindow):
	def __init__(self, main_window) -> None:
		super(ViewTimeEntries, self).__init__()
		self.main_window = main_window
		self.setupUi(self)
		self.setMinimumSize(self.size())
		header = self.timeEntriesTableView.horizontalHeader()
		header.setSectionResizeMode(QHeaderView.Interactive)
		self.setWindowTitle("Time Logs")

		self.model = TimeEntriesRelationalTableModel()
		self.timeEntriesTableView.setModel(self.model)
		self.model.setTable("time_entries")

		self.timeEntriesTableView.setSortingEnabled(True)

		self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)

		phase_relation = QSqlRelation("phases", "phase_id", "project_phase")
		self.model.setRelation(self.model.fieldIndex("phase_id"), phase_relation)

		arch_relation = QSqlRelation("architects", "architect_id", "name")
		self.model.setRelation(self.model.fieldIndex("architect_id"), arch_relation)

		project_relation = QSqlRelation("projects", "project_id", "project_name")
		self.model.setRelation(self.model.fieldIndex("project_id"), project_relation)

		invoice_relation = QSqlRelation("invoices", "invoice_id", "invoice_number")
		self.model.setRelation(self.model.fieldIndex("invoice_id"), invoice_relation)

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter("status = 'Active'")
		self.project_model.select()
		self.ProjectComboBox.setModel(self.project_model)
		self.ProjectComboBox.setModelColumn(1)
		self.original_row = 0

		self.timeEntriesTableView.setItemDelegate(QSqlRelationalDelegate(
			self.timeEntriesTableView))

		# Set start  and end time delegates
		start_time_column_index = self.model.fieldIndex("start_time")
		self.timeEntriesTableView.setItemDelegateForColumn(
			start_time_column_index, TimeDelegate(
				self.timeEntriesTableView))

		end_time_column_index = self.model.fieldIndex("end_time")
		self.timeEntriesTableView.setItemDelegateForColumn(
			end_time_column_index, TimeDelegate(
				self.timeEntriesTableView))

		# Set checkbox delegate
		self.invoice_checkbox_delegate = InvoiceCheckboxDelegate(self.model, self)
		invoice_col = self.model.fieldIndex("invoice_id")
		self.timeEntriesTableView.setItemDelegateForColumn(invoice_col, 
			self.invoice_checkbox_delegate)

		column_titles = {
			"project_id" : "Project Name",
			"architect_id" : "Architect's Name",
			"phase_id" : "Project Phase",
			"start_time" : "Start Time",
			"end_time" : "End Time",
			"duration_minutes" : "Duration",
			"notes" : "Notes",
			"invoice_id" : "Invoice Number",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		self.model.select()

		self.timeEntriesTableView.setColumnHidden(
			self.model.fieldIndex("time_entry_id"), True)

		header = self.timeEntriesTableView.horizontalHeader()
		header.moveSection(1, 2)
		header.moveSection(8, 7)

		self.updateFilter()

		index = self.model.fieldIndex("start_time")
		self.timeEntriesTableView.sortByColumn(index, Qt.DescendingOrder)

		#self.model.setFilter("invoice_number = 'Not Invoiced' AND \
		#	project_phase NOT IN ('Administration', 'Business Development')")
		self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
			"invoice_number"), True)
		self.expandColumns()

		# Create an event filter so the table view sees delete key presses
		self.timeEntriesTableView.installEventFilter(self)

		self.cancelInvoiceBtn.hide()

		self.ProjectComboBox.hide()
		self.showCompletedProjectsCheckBox.hide()

		# Click box activation
		self.showInvoicedCheckBox.stateChanged.connect(self.showInvoicedTimes)
		self.showInternalsCheckBox.stateChanged.connect(self.updateFilter)

		self.showByProjectCheckBox.stateChanged.connect(self.showProjectCombo)
		self.ProjectComboBox.currentIndexChanged.connect(self.updateFilter)
		self.showCompletedProjectsCheckBox.stateChanged.connect(
			self.showCompletedProjects)

		self.createInvoiceBtn.clicked.connect(self.createInvoice)

		self.cancelInvoiceBtn.clicked.connect(self.cancelInvoice)

		self.show()

	def showInvoicedTimes(self, signal) -> None:
		"""Filter out time log entries attached to an invoice"""
		if signal == 2:
			self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
				"invoice_number"), False)
			self.contractColumns()

		else:
			self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
				"invoice_number"), True)
			self.expandColumns()	

		self.updateFilter()

	def showProjectCombo(self, signal) -> None:
		"""Show or hide Project ComboBox"""
		if signal == 2:
			self.ProjectComboBox.show()
			self.showCompletedProjectsCheckBox.show()
			with get_db_connection() as conn:
				cur = conn.cursor()
				arch_proj_ids = get_most_recent_archid_and_projid(cur)
			if arch_proj_ids:
				arch_id, proj_id = arch_proj_ids
			proj_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
			if proj_match:
				self.original_row = proj_match[0].row()
				self.ProjectComboBox.setCurrentIndex(self.original_row)

			self.updateFilter()

		else:
			self.ProjectComboBox.hide()
			self.showCompletedProjectsCheckBox.hide()
			self.updateFilter()

	def showCompletedProjects(self, signal) -> None:
		current_row = self.ProjectComboBox.currentIndex()
		current_proj_id = self.project_model.data(
			self.project_model.index(current_row, 0))
		if signal == 2:
			self.project_model.setFilter("")
		else:
			self.project_model.setFilter("status = 'Active'")
		proj_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, current_proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if proj_match:
			row = proj_match[0].row()
			self.ProjectComboBox.setCurrentIndex(row)
		else:
			self.ProjectComboBox.setCurrentIndex(self.original_row)

	def updateFilter(self) -> None:
		"""Filter table depending on state of showInvoicedCheckBox and 
		showByProjectCheckBox"""
		filters = []

		# Add 'Not Invoiced' filter
		if not self.showInvoicedCheckBox.isChecked():
			filters.append("invoice_number = 'Not Invoiced'")

		if self.showByProjectCheckBox.isChecked():
			proj_index = self.ProjectComboBox.currentIndex()
			proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
			with get_db_connection() as conn:
				cur = conn.cursor()
				sql = "SELECT * FROM projects WHERE project_id = ?"
				cur.execute(sql, (proj_id,))
				proj_row = cur.fetchone()
			proj_name = proj_row[1]
			filters.append(f"project_name = '{proj_name}'")
		else:
			if not self.showInternalsCheckBox.isChecked():
				filters.append(
					"project_phase NOT IN ('Administration', 'Business Development')")

		# Combine filters from both check-boxes
		if filters:
			self.model.setFilter(" AND ".join(filters))
		else:
			self.model.setFilter("")
		self.model.select()

	def createInvoice(self) -> None:
		if self.invoice_checkbox_delegate.selection_mode is False:
			self.invoice_checkbox_delegate.selection_mode = True
			self.createInvoiceBtn.setText("Generate Invoice")
			self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
				"invoice_number"), False)
			self.contractColumns()
			index = self.model.fieldIndex("invoice_number")
			self.model.setHeaderData(index, Qt.Horizontal, "Select Entries")
			self.timeEntriesTableView.horizontalHeader().headerDataChanged(
				Qt.Horizontal, index, index)
			self.cancelInvoiceBtn.show()
			self.showInvoicedCheckBox.setEnabled(False)
		else:
			self.invoice_checkbox_delegate.selection_mode = False
			self.createInvoiceBtn.setText("Create Invoice")

			# Add time_entry_ids and proj_ids to list
			checked_invoice_time_entry_ids = []
			checked_invoice_proj_names = set()
			for row in self.invoice_checkbox_delegate.checked_rows:
				time_entry_id = self.model.data(self.model.index(row, 
					self.model.fieldIndex("time_entry_id")), Qt.EditRole)
				proj_id = self.model.data(self.model.index(
					row, self.model.fieldIndex("project_name")), Qt.EditRole)
				checked_invoice_time_entry_ids.append(time_entry_id)
				checked_invoice_proj_names.add(proj_id)
			
			if len(checked_invoice_proj_names) == 0:
				self.cancelInvoice()
				return
			elif len(checked_invoice_proj_names) != 1:
				# Pop up warning on ids
				QMessageBox.warning(self, "Invalid Project",
			 		"All Time Entries Must Be From The Same Project")
				self.cancelInvoice()
				return
			else:
				project_name = checked_invoice_proj_names.pop()
				# Check to make sure project is real
				if (project_name == "Administration" or 
					project_name == "Business Development"):
					QMessageBox.warning(self, "Invalid Project",
			 		f"{project_name} Cannot Be Invoiced")
					self.cancelInvoice()
					return
				# Pop up invoice number dialog
				add_invoice_number = AddInvoiceNumber()
				add_invoice_number.exec()
				invoice_number = None
				while not invoice_number:
					invoice_number = add_invoice_number.addInvoiceLineEdit.text().strip()
					if not invoice_number:
						QMessageBox.warning(self, "Invalid Invoice Number",
			 				"Must Add An Invoice Number")
						add_invoice_number = AddInvoiceNumber()
						add_invoice_number.exec()
				date = datetime.now()
				start_date = int(date.timestamp())

				db = QSqlDatabase.database()
				db.transaction()

				try:
					query = QSqlQuery()
					query.prepare("SELECT project_id FROM projects WHERE project_name = ?")
					query.addBindValue(project_name)
					query.exec()
					if query.next():
						proj_id = query.value(0)
				        
				        # Create invoice
						query2 = QSqlQuery()
						query2.prepare("INSERT INTO invoices (project_id, created_date, invoice_number, status) VALUES (?, ?, ?, ?)")
						query2.addBindValue(proj_id)
						query2.addBindValue(start_date)
						query2.addBindValue(invoice_number)
						query2.addBindValue("Draft")
						query2.exec()
						invoice_id = query2.lastInsertId()
				        
				        # Update time entries
						for time_entry in checked_invoice_time_entry_ids:
							query3 = QSqlQuery()
							query3.prepare("UPDATE time_entries SET invoice_id = ? WHERE time_entry_id = ?")
							query3.addBindValue(invoice_id)
							query3.addBindValue(time_entry)
							query3.exec()
				    
					db.commit()
				except Exception:
					db.rollback()
					raise

				self.model.select()

				# Refresh the invoice_number model's drop down menu
				invoice_column_index = self.model.fieldIndex("invoice_number")
				relation_model = self.model.relationModel(invoice_column_index)
				if relation_model:
					relation_model.select()

				# Refresh ViewInvoices window
				if self.main_window.view_invoices_window:
					self.main_window.view_invoices_window.model.select()

			if not self.showInvoicedCheckBox.isChecked():
				self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
					"invoice_number"), True)
				self.expandColumns()
			index = self.model.fieldIndex("invoice_number")
			self.model.setHeaderData(index, Qt.Horizontal, "Invoice Number")
			self.cancelInvoiceBtn.hide()
			self.invoice_checkbox_delegate.checked_rows.clear()
			self.showInvoicedCheckBox.setEnabled(True)

		self.timeEntriesTableView.viewport().update()

	def cancelInvoice(self) -> None:
		self.invoice_checkbox_delegate.selection_mode = False
		self.createInvoiceBtn.setText("Create Invoice")
		if not self.showInvoicedCheckBox.isChecked():
			self.timeEntriesTableView.setColumnHidden(self.model.fieldIndex(
				"invoice_number"), True)
			self.expandColumns()
		index = self.model.fieldIndex("invoice_number")
		self.model.setHeaderData(index, Qt.Horizontal, "Invoice Number")
		self.cancelInvoiceBtn.hide()
		self.invoice_checkbox_delegate.checked_rows.clear()
		self.showInvoicedCheckBox.setEnabled(True)
		self.timeEntriesTableView.viewport().update()

	def expandColumns(self) -> None:
		self.timeEntriesTableView.setColumnWidth(1, 200)
		self.timeEntriesTableView.setColumnWidth(2, 155)
		self.timeEntriesTableView.setColumnWidth(3, 180)
		self.timeEntriesTableView.setColumnWidth(4, 170)
		self.timeEntriesTableView.setColumnWidth(5, 170)
		self.timeEntriesTableView.setColumnWidth(6, 100)
		self.timeEntriesTableView.setColumnWidth(7, 380)

	def contractColumns(self) -> None:	
		self.timeEntriesTableView.setColumnWidth(1, 200)
		self.timeEntriesTableView.setColumnWidth(2, 140)
		self.timeEntriesTableView.setColumnWidth(3, 180)
		self.timeEntriesTableView.setColumnWidth(4, 152)
		self.timeEntriesTableView.setColumnWidth(5, 152)
		self.timeEntriesTableView.setColumnWidth(6, 80)
		self.timeEntriesTableView.setColumnWidth(7, 360)
		self.timeEntriesTableView.setColumnWidth(8, 100)

	def eventFilter(self, obj, event) -> bool:
		"""Method to allow row deletions"""
		if obj == self.timeEntriesTableView and event.type() == QEvent.KeyPress:
			if event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
				selected_indexes = self.timeEntriesTableView.selectionModel().selectedIndexes()
				if selected_indexes:
					selected_rows = set(index.row() for index in selected_indexes)
					if selected_rows:
						self.delete_time_entry = DeleteTimeEntryWarning()
						result = self.delete_time_entry.exec()
						if result == QDialog.Accepted:
							for row in selected_rows:
								time_entry_id = self.model.data(self.model.index(row, 0))
								query = QSqlQuery()
								query.prepare(
									"DELETE FROM time_entries WHERE time_entry_id = ?")
								query.addBindValue(time_entry_id)
								if not query.exec():
									print(f"Delete failed: {query.lastError().text()}")

							self.model.select()
						else:
							return False
				return True
		return super().eventFilter(obj, event)

	def closeEvent(self, event) -> None:
		deleteEmptyInvoices()
		if self.main_window.view_invoices_window:
			self.main_window.view_invoices_window.model.select()
		event.accept()


class ViewInvoices(QWidget, Ui_ViewInvoicesWindow):
	def __init__(self) -> None:
		super(ViewInvoices, self).__init__()
		self.setupUi(self)
		self.setMinimumSize(self.size())
		header = self.invoicesTableView.horizontalHeader()
		header.setSectionResizeMode(QHeaderView.Interactive)
		self.setWindowTitle("Invoices")

		self.model = InvoiceRelationalTableModel()
		self.invoicesTableView.setModel(self.model)
		self.model.setTable("invoices")
		self.model.setFilter('invoice_id > 0')

		self.invoicesTableView.setSortingEnabled(True)

		self.model.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)

		project_relation = QSqlRelation("projects", "project_id", "project_name")
		self.model.setRelation(self.model.fieldIndex("project_id"), project_relation)

		column_titles = {
			"project_id" : "Project Name",
			"created_date" : "Invoice Created",
			"invoice_number" : "Invoice Number",
			"status" : "Status",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		self.model.select()

		# Create an event filter so the table view sees delete key presses
		self.invoicesTableView.installEventFilter(self)

		self.invoicesTableView.setColumnHidden(
			self.model.fieldIndex("invoice_id"), True)

		# Set created date delegate
		created_date_column_index = self.model.fieldIndex("created_date")
		self.invoicesTableView.setItemDelegateForColumn(
			created_date_column_index, CreatedDateDelegate(
				self.invoicesTableView))

		header = self.invoicesTableView.horizontalHeader()
		header.moveSection(3, 1)

		index = self.model.fieldIndex("created_date")
		self.invoicesTableView.sortByColumn(index, Qt.DescendingOrder)

		self.invoicesTableView.setColumnWidth(1, 200)
		self.invoicesTableView.setColumnWidth(2, 150)
		self.invoicesTableView.setColumnWidth(3, 150)
		self.invoicesTableView.setColumnWidth(4, 100)

		status_delegate = StatusDelegate(INVOICE_STATUSES, self.invoicesTableView)
		status_column = self.model.fieldIndex("status")
		self.invoicesTableView.setItemDelegateForColumn(status_column, 
			status_delegate)

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter("status = 'Active' AND project_id > 0")
		self.project_model.select()
		self.ProjectComboBox.setModel(self.project_model)
		self.ProjectComboBox.setModelColumn(1)
		
		project_relation = QSqlRelation("projects", "project_id", "project_name")
		self.model.setRelation(self.model.fieldIndex("project_id"), project_relation)
		
		self.ProjectComboBox.hide()
		self.showCompletedProjectsCheckBox.hide()

		self.showByProjectCheckBox.stateChanged.connect(self.showProjectCombo)
		self.ProjectComboBox.currentIndexChanged.connect(self.updateFilter)
		self.showCompletedProjectsCheckBox.stateChanged.connect(
			self.showCompletedProjects)

		self.viewInvoicePushButton.clicked.connect(self.viewInvoice)
		self.invoice_windows = []
		
		self.show()

	def showProjectCombo(self, signal) -> None:
		"""Show or hide Project ComboBox"""
		if signal == 2:
			self.ProjectComboBox.show()
			self.showCompletedProjectsCheckBox.show()
			with get_db_connection() as conn:
				cur = conn.cursor()
				arch_proj_ids = get_most_recent_archid_and_projid(cur)
			if arch_proj_ids:
				arch_id, proj_id = arch_proj_ids
			proj_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
			if proj_match:
				row = proj_match[0].row()
				self.ProjectComboBox.setCurrentIndex(row)
			self.updateFilter()

		else:
			self.ProjectComboBox.hide()
			self.showCompletedProjectsCheckBox.hide()
			self.model.setFilter("invoice_id > 0")

	def updateFilter(self) -> None:
		proj_index = self.ProjectComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		with get_db_connection() as conn:
			cur = conn.cursor()
			sql = "SELECT * FROM projects WHERE project_id = ?"
			cur.execute(sql, (proj_id,))
			proj_row = cur.fetchone()
		proj_name = proj_row[1]
		self.model.setFilter(f"project_name = '{proj_name}'")

	def showCompletedProjects(self, signal) -> None:
		proj_index = self.ProjectComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		if signal == 2:
			self.project_model.setFilter("project_id > 0")
		else:
			self.project_model.setFilter("status = 'Active' AND project_id > 0")
		proj_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if proj_match:
			row = proj_match[0].row()
			self.ProjectComboBox.setCurrentIndex(row)

	def viewInvoice(self) -> None:
		self.invoice_ids = []
		selected_indexes = self.invoicesTableView.selectionModel().selectedIndexes()
		if selected_indexes:
			selected_rows = set(index.row() for index in selected_indexes)
			if selected_rows:
				for row in selected_rows:
					invoice_id = self.model.data(self.model.index(row, 0))
					self.invoice_ids.append(invoice_id)
		if self.invoice_ids:
			for invoice_id in self.invoice_ids:
				self.invoice_windows.append(ViewInvoice(invoice_id))

	def eventFilter(self, obj, event) -> bool:
		"""Method to allow row deletions"""
		if obj == self.invoicesTableView and event.type() == QEvent.KeyPress:
			if event.key() in (Qt.Key_Delete, Qt.Key_Backspace):
				selected_indexes = self.invoicesTableView.selectionModel().selectedIndexes()
				if selected_indexes:
					selected_rows = set(index.row() for index in selected_indexes)
					if selected_rows:
						self.delete_invoices = DeleteInvoiceWarning()
						result = self.delete_invoices.exec()
						if result == QDialog.Accepted:
							for row in selected_rows:
								invoice_id = self.model.data(self.model.index(row, 0))
								query = QSqlQuery()
								query.prepare("DELETE FROM invoices \
									WHERE invoice_id = ?")
								query.addBindValue(invoice_id)
								if not query.exec():
									print(f"Delete failed: {query.lastError().text()}")
							self.model.select()
						else:
							return False

				return True
		return super().eventFilter(obj, event)

class ViewInvoice(Ui_ViewInvoiceWindow, QWidget):
	def __init__(self, invoice_number: int) -> None:
		super(ViewInvoice, self).__init__()
		self.setupUi(self)
		self.setMinimumSize(self.size())
		header = self.invoiceTableView.horizontalHeader()
		header.setSectionResizeMode(QHeaderView.Interactive)

		self.invoice_number = invoice_number
		
		self.model = TimeEntriesRelationalTableModel()
		self.invoiceTableView.setModel(self.model)
		self.model.setTable("time_entries")
		filter_string = f"invoice_id = {self.invoice_number}"
		self.model.setFilter(filter_string)
		self.invoiceTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)

		project_relation = QSqlRelation("projects", "project_id", "project_name")
		self.model.setRelation(self.model.fieldIndex("project_id"), project_relation)

		phase_relation = QSqlRelation("phases", "phase_id", "project_phase")
		self.model.setRelation(self.model.fieldIndex("phase_id"), phase_relation)

		with get_db_connection() as conn:
			cur = conn.cursor()
			sql = "SELECT invoice_number FROM invoices WHERE invoice_id = ?"
			cur.execute(sql, (invoice_number,))
			invoice_name = cur.fetchone()[0]

		self.invoiceTableView.setSortingEnabled(True)
		
		self.addInvoiceNumberLabel.setText(invoice_name)
		self.setWindowTitle(f"Invoice #{invoice_name}")

		column_titles = {
			"project_phase" : "Project Phase",
			"start_time" : "Start Time",
			"end_time" : "End Time",
			"duration_minutes" : "Duration",
			"notes" : "Notes",
		}
		for name, title in column_titles.items():
			index = self.model.fieldIndex(name)
			self.model.setHeaderData(index, Qt.Horizontal, title)

		self.invoiceTableView.setColumnWidth(1, 155)
		self.invoiceTableView.setColumnWidth(2, 140)
		self.invoiceTableView.setColumnWidth(3, 180)
		self.invoiceTableView.setColumnWidth(4, 152)
		self.invoiceTableView.setColumnWidth(5, 152)
		self.invoiceTableView.setColumnWidth(6, 100)
		self.invoiceTableView.setColumnWidth(7, 200)

		# Hide unused columns
		self.invoiceTableView.setColumnHidden(
			self.model.fieldIndex("time_entry_id"), True)
		self.invoiceTableView.setColumnHidden(
			self.model.fieldIndex("invoice_id"), True)
		self.invoiceTableView.setColumnHidden(
			self.model.fieldIndex("architect_id"), True)
		self.invoiceTableView.setColumnHidden(
			self.model.fieldIndex("project_name"), True)

		self.model.select()

		# Sum total time in invoice
		with get_db_connection() as conn:
			cur = conn.cursor()
			sql = "SELECT SUM(duration_minutes) FROM time_entries \
				WHERE invoice_id = ?"
			cur.execute(sql, (invoice_number,))
			self.total_time = cur.fetchone()

		hours = self.total_time[0] // 60
		minutes = self.total_time[0] % 60
		total_time_hours_mins = f"{hours}:{minutes:02d}"

		self.addTotalHoursLabel.setText(total_time_hours_mins)

		self.project_name = self.model.data(self.model.index(0, 1))
		self.projectNameLabel.setText(self.project_name)

		self.saveToPDFBtn.clicked.connect(self.makePDF)

		self.show()

	def makePDF(self):
		with get_db_connection() as conn:
			cur = conn.cursor()
			generate_invoice_pdf(self.invoice_number, cur)


#	~~ANALYTICS~~

class ViewAnalytics(QWidget, Ui_AnalyticsWindow):
	def __init__(self) -> None:
		super(ViewAnalytics, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Analytics")

		with get_db_connection() as conn:
			cur = conn.cursor()
			cur.execute("SELECT project_id FROM projects \
				WHERE current_phase_id > 3 AND current_phase_id < 8")
			proj_ids = cur.fetchall()
			cur.execute("SELECT project_id FROM projects")
			low_proj_ids = cur.fetchall()
		if proj_ids:
			all_proj_ids = [pid[0] for pid in proj_ids]
			rand_id = random.choice(all_proj_ids)
		elif low_proj_ids:
			all_proj_ids = [pid[0] for pid in low_proj_ids]
			rand_id = random.choice(all_proj_ids)
		else:
			rand_id = -1

		end_date = datetime.now()
		end_date_int = int(end_date.timestamp())
		start_date = end_date - timedelta(weeks=104)
		start_date_int = int(start_date.timestamp())

		with get_db_connection() as conn:
			cur = conn.cursor()
			phase_data = phase_duration_by_project(rand_id, cur)
			phase_time_data = phase_time_entries_by_project(rand_id, cur)
			total_hours = phase_duration_all_projects(cur)
			projs_over_time = project_ids_over_time_period(start_date_int, end_date_int, cur)
			projs_over_time_ids = [proj[0] for proj in projs_over_time]
			projs_over_time_names = [proj[1] for proj in projs_over_time]
			projs_over_time_list = []
			for proj_id in projs_over_time_ids:
				projs_over_time_list.append(phase_duration_by_project(proj_id, cur))

		self.projectByPhaseWidget.bars_by_phase(
			phase_data)
		self.projectOverTimeWidget.step_plot_phases(
			phase_time_data)
		self.phaseAveragesWidget.pie_by_phase(
			total_hours, "Total Time Breakdown")

		if ("Administration" in projs_over_time_names and 
			"Business Development" in projs_over_time_names):
			shifted_projs_over_time = (projs_over_time_list[2:] 
				+ projs_over_time_list[1:2] + projs_over_time_list[0:1])
			shifted_names_over_time = (projs_over_time_names[2:] 
				+ projs_over_time_names[1:2] + projs_over_time_names[0:1])
		elif ("Administration" in projs_over_time_names or
			"Business Development" in projs_over_time_names):
			shifted_projs_over_time = (projs_over_time_list[1:] 
				+ projs_over_time_list[0:1])
			shifted_names_over_time = (projs_over_time_names[1:] 
				+ projs_over_time_names[0:1])
		else:
			shifted_projs_over_time = projs_over_time_list
			shifted_names_over_time = projs_over_time_names

		self.projectsOverTimeWidget.bars_projects_by_phase(
			shifted_projs_over_time, shifted_names_over_time)

		self.ProjectByPhaseBtn.clicked.connect(self.projectByPhase)
		self.ProjectOverTimeBtn.clicked.connect(self.projectOverTime)
		self.PhaseAveragesBtn.clicked.connect(self.averageProjectTime)
		self.ProjectsOverTimeBtn.clicked.connect(self.projectsOverTime)

		self.show()

	def projectByPhase(self) -> None:
		self.phases_bar_or_pie = ViewProjectPhases("bar_pie")

	def projectOverTime(self) -> None:
		self.phases_stem_or_step = ViewProjectPhases("stem_step")

	def averageProjectTime(self) -> None:
		self.phases_averages = ViewProjectAverages()

	def projectsOverTime(self) -> None:
		self.projects_by_phase = ViewProjectsOverTime()


class ViewProjectPhases(QWidget, Ui_PhaseHoursWindow):
	"""Class to utilize either bar/pie charts or stem/step charts.
	Must pass in either 'bar_pie' or 'stem_step' as the 2nd parameter"""
	def __init__(self, chart_type: str) -> None:
		super(ViewProjectPhases, self).__init__()
		self.setupUi(self)
		self.setMinimumSize(self.size())
		self.setWindowTitle("Projects By Phase")

		self.chart_type = chart_type
		self.barStem_or_pieStep = 0
		self.phase_data = []
		self.original_row = 0

		end_date = datetime.now()
		start_date = end_date - timedelta(weeks=102)
		self.start_date_int = int(start_date.timestamp())

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter(
			f"project_id > 0 AND start_date > {self.start_date_int}")
		self.project_model.select()
		self.ProjectComboBox.setModel(self.project_model)
		self.ProjectComboBox.setModelColumn(1)

		with get_db_connection() as conn:
			cur = conn.cursor()
			arch_proj_ids = get_most_recent_archid_and_projid(cur)
		if arch_proj_ids:
			arch_id, proj_id = arch_proj_ids
			proj_match = self.project_model.match(self.project_model.index(0,0),
				Qt.EditRole, proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
			if proj_match:
				self.original_row = proj_match[0].row()
				self.ProjectComboBox.setCurrentIndex(self.original_row)
		else:
			self.ProjectComboBox.setCurrentIndex(0)

		with get_db_connection() as conn:
			cur = conn.cursor()
			if self.chart_type == "bar_pie":
				self.bar_phase_data = phase_duration_by_project(proj_id, cur)
			else:
				self.stem_phase_data = phase_time_entries_by_project(proj_id, cur)

		if self.chart_type == 'bar_pie':
			self.PhaseHoursWidget.bars_by_phase(self.bar_phase_data, 
				phase_names_length = 1)
		else:
			self.BarsStemToPieStepBtn.setText("Stem Chart")
			self.PhaseHoursWidget.step_plot_phases(self.stem_phase_data)

		self.ProjectComboBox.currentIndexChanged.connect(self.projectChanged)
		self.BarsStemToPieStepBtn.clicked.connect(self.barStemToPieStep)
		self.ShowAllProjectsChkBx.stateChanged.connect(self.projectFilter)

		self.show()

	def projectChanged(self) -> None:
		proj_index = self.ProjectComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		with get_db_connection() as conn:
			cur = conn.cursor()
			if self.chart_type == "bar_pie":
				self.bar_phase_data = phase_duration_by_project(proj_id, cur)
			else:
				self.stem_phase_data = phase_time_entries_by_project(proj_id, cur)
		if self.chart_type == "bar_pie":
			self.barsOrPie()
		else:
			self.stemOrStep()

	def barsOrPie(self) -> None:
		if self.barStem_or_pieStep == 0:
			self.PhaseHoursWidget.bars_by_phase(self.bar_phase_data, 
				phase_names_length = 1)
			self.BarsStemToPieStepBtn.setText("Pie Chart")
		else:
			self.PhaseHoursWidget.pie_by_phase(self.bar_phase_data)
			self.BarsStemToPieStepBtn.setText("Bar Chart")

	def stemOrStep(self) -> None:
		if self.barStem_or_pieStep == 0:
			self.PhaseHoursWidget.step_plot_phases(self.stem_phase_data)
			self.BarsStemToPieStepBtn.setText("Stem Chart")
		else:
			self.PhaseHoursWidget.stem_plot_phases(self.stem_phase_data)
			self.BarsStemToPieStepBtn.setText("Step Chart")

	def barStemToPieStep(self) -> None:
		if self.barStem_or_pieStep == 0:
			self.barStem_or_pieStep = 1
		else:
			self.barStem_or_pieStep = 0
		if self.chart_type == "bar_pie":
			self.barsOrPie()
		else:
			self.stemOrStep()

	def projectFilter(self, signal):
		proj_index = self.ProjectComboBox.currentIndex()
		proj_model = self.ProjectComboBox.model()
		current_proj_id = proj_model.data(proj_model.index(proj_index, 0))
		if signal == 2:
			self.project_model.setFilter("project_id > 0")
		else:
			self.project_model.setFilter(
				f"project_id > 0 AND start_date > {self.start_date_int}")
		proj_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, current_proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if proj_match:
			row = proj_match[0].row()
			self.ProjectComboBox.setCurrentIndex(row)
		else:
			self.ProjectComboBox.setCurrentIndex(self.original_row)
		
class ViewProjectAverages(QWidget, Ui_PhaseAveragesWindow):
	def __init__(self) -> None:
		super(ViewProjectAverages, self).__init__()
		self.setupUi(self)
		self.setMinimumSize(self.size())
		self.setWindowTitle("Phase Time Averages")
		self.bar_or_pie = 0
		self.project_vs_average = 0

		self.total_hours = []
		self.shifted_total_hours = []
		self.avg_data_tuple = ()
		self.original_project_row = 0

		self.proj_data = 0
		self.proj_data2 = 0
		self.proj_data3 = 0

		self.current_start_date = None
		self.current_end_date = None

		self.ShowAllProjectsChkBx.hide()
		self.ProjectComboBox.hide()
		self.Project2ComboBox.hide()
		self.Project3ComboBox.hide()
		self.Show2ndProjectChkBx.hide()
		self.Show3rdProjectChkBx.hide()
		self.NonBillableTimesChkBx.hide()
		self.StartDateEdit.hide()
		self.EndDateEdit.hide()

		# ComboBoxes Model setup
		end_date = datetime.now()
		start_date = end_date - timedelta(weeks=102)
		self.start_date_int = int(start_date.timestamp())
		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter(
			f"project_id > 0 AND start_date > {self.start_date_int}")
		self.project_model.select()
		self.ProjectComboBox.setModel(self.project_model)
		self.ProjectComboBox.setModelColumn(1)
		self.Project2ComboBox.setModel(self.project_model)
		self.Project2ComboBox.setModelColumn(1)
		self.Project3ComboBox.setModel(self.project_model)
		self.Project3ComboBox.setModelColumn(1)

		self.getData()

		self.original_total_hours = self.total_hours
		self.original_shifted_total_hours = self.shifted_total_hours
		self.original_avg_tuple = self.avg_data_tuple

		self.current_date = QDate.currentDate()
		self.EndDateEdit.setDate(self.current_date)
		start_date_datetime = datetime.fromtimestamp(self.first_proj_start_date[0])
		self.start_date = QDate(start_date_datetime.year, start_date_datetime.month,
			start_date_datetime.day)
		self.StartDateEdit.setDate(self.start_date)

		self.ProjectComboBox.setCurrentIndex(self.original_project_row)
		self.Project2ComboBox.setCurrentIndex(self.original_project_row)
		self.Project3ComboBox.setCurrentIndex(self.original_project_row)

		self.PhaseAverageWidget.bars_by_phase(self.avg_data_tuple, 
			"Average Hours Per Phase", phase_names_length = 1)

		self.PieToBarBtn.clicked.connect(self.barsToPie)
		self.AvgTotalTimeChkBx.stateChanged.connect(self.showHideTotalTimes)
		self.NonBillableTimesChkBx.stateChanged.connect(self.showHideNonbillable)
		self.ChoseDateChkBx.stateChanged.connect(self.showDateRange)
		self.StartDateEdit.userDateChanged.connect(self.selectDateRange)
		self.EndDateEdit.userDateChanged.connect(self.selectDateRange)

		self.ProjectVsAveragesBtn.clicked.connect(self.projectVsAverages)
		self.ShowAllProjectsChkBx.stateChanged.connect(self.projectFilter)
		self.Show2ndProjectChkBx.stateChanged.connect(self.projectVsAverages2ndProject)
		self.Show3rdProjectChkBx.stateChanged.connect(self.projectVsAverages3rdProject)

		self.ProjectComboBox.currentIndexChanged.connect(self.getAveragesData)
		self.Project2ComboBox.currentIndexChanged.connect(self.getAveragesData)
		self.Project3ComboBox.currentIndexChanged.connect(self.getAveragesData)

		self.show()

	def getData(self, start_date: Optional[int] = None, 
		end_date: Optional[int] = None) -> None:
		"""Method to fetch all needed information from database"""
		with get_db_connection() as conn:
			cur = conn.cursor()
			self.total_hours = phase_duration_all_projects(cur, start_date, end_date)
			self.first_proj_start_date = earliest_start_date(cur)
			num_proj_by_phase_tuple = total_number_of_projects_by_phase(cur, start_date,
				end_date)
			arch_proj_ids = get_most_recent_archid_and_projid(cur)

		num_projects_by_phase = [projects[1] for projects in num_proj_by_phase_tuple]
		avg_data = [round(data[1] / projects, 1) 
			for data, projects in zip(self.total_hours, num_projects_by_phase)]
		avg_phases = [data[0] for data in self.total_hours]

		if ADMIN in avg_phases and BUSDEV in avg_phases:
			shifted_avg_phases = avg_phases[:-2]
			shifted_avg_data = avg_data[:-2]
			self.shifted_total_hours = self.total_hours[:-2]
		elif ADMIN in avg_phases or BUSDEV in avg_phases:
			shifted_avg_phases = avg_phases[:-1]
			shifted_avg_data = avg_data[:-1]
			self.shifted_total_hours = self.total_hours[:-1]
		else:
			shifted_avg_phases = avg_phases
			shifted_avg_data = avg_data
			self.shifted_total_hours = self.total_hours
		self.avg_data_tuple = list(zip(shifted_avg_phases, shifted_avg_data))

		if arch_proj_ids:
			arch_id, proj_id = arch_proj_ids
			proj_match = self.project_model.match(self.project_model.index(0,0),
				Qt.EditRole, proj_id, 1, Qt.MatchFlags(Qt.MatchExactly))
			if proj_match:
				self.original_project_row = proj_match[0].row()
			else:
				self.original_project_row = 1

	def getAveragesData(self) -> None:
		proj_index = self.ProjectComboBox.currentIndex()
		proj_index2 = self.Project2ComboBox.currentIndex()
		proj_index3 = self.Project3ComboBox.currentIndex()
		proj_id = self.project_model.data(self.project_model.index(proj_index, 0))
		proj_id2 = self.project_model.data(self.project_model.index(proj_index2, 0))
		proj_id3 = self.project_model.data(self.project_model.index(proj_index3, 0))
		with get_db_connection() as conn:
			cur = conn.cursor()
			self.proj_data = phase_duration_by_project_with_name(proj_id, cur, 
				self.current_start_date, self.current_end_date)
			self.proj_data2 = phase_duration_by_project_with_name(proj_id2, cur, 
				self.current_start_date, self.current_end_date)
			self.proj_data3 = phase_duration_by_project_with_name(proj_id3, cur, 
				self.current_start_date, self.current_end_date)
		if self.project_vs_average == 1:
			self.projectPhasesVsAverages()

	def barsToPie(self) -> None:
		if self.project_vs_average == 1:
			self.project_vs_average = 0
			self.ShowAllProjectsChkBx.hide()
			self.ProjectComboBox.hide()
			self.ProjectVsAveragesBtn.show()
			self.Show2ndProjectChkBx.setChecked(False)
			self.Show2ndProjectChkBx.hide()
			self.Project2ComboBox.hide()
			self.Show3rdProjectChkBx.setChecked(False)
			self.Show3rdProjectChkBx.hide()
			self.Project3ComboBox.hide()
			self.ChoseDateChkBx.setChecked(False)
			self.ProjectComboBox.setCurrentIndex(self.original_project_row)
			self.Project2ComboBox.setCurrentIndex(self.original_project_row)
			self.Project3ComboBox.setCurrentIndex(self.original_project_row)
		if self.bar_or_pie == 0:
			self.bar_or_pie = 1
			self.PieToBarBtn.setText("Bar Chart")
		else:
			self.bar_or_pie = 0
			self.PieToBarBtn.setText("Pie Chart")
		self.barsOrPie()

	def barsOrPie(self) -> None:
		if self.bar_or_pie == 1:
			self.PhaseAverageWidget.pie_by_phase(self.total_hours, 
				"Total Time Breakdown")
			self.NonBillableTimesChkBx.show()
			self.AvgTotalTimeChkBx.setChecked(False)
			self.AvgTotalTimeChkBx.hide()
		else:
			self.PhaseAverageWidget.bars_by_phase(self.avg_data_tuple, 
				"Average Hours Per Phase", phase_names_length = 1)
			self.AvgTotalTimeChkBx.show()
			self.NonBillableTimesChkBx.setChecked(False)
			self.NonBillableTimesChkBx.hide()

	def projectPhasesVsAverages(self) -> None:
		if self.Show3rdProjectChkBx.checkState().value == 2:
			if len(self.proj_data) == 0:
				self.proj_data = self.proj_data2
				self.proj_data2 = self.proj_data3
				self.proj_data3 = []
				if len(self.proj_data) == 0:
					self.proj_data = self.proj_data2
					self.proj_data2 = []
			self.PhaseAverageWidget.bars_projects_vs_average(self.avg_data_tuple, 
				self.proj_data, self.proj_data2, self.proj_data3)
		elif self.Show2ndProjectChkBx.checkState().value == 2:
			if len(self.proj_data) == 0:
				self.proj_data = self.proj_data2
				self.proj_data2 = []
			self.PhaseAverageWidget.bars_projects_vs_average(self.avg_data_tuple, 
				self.proj_data, self.proj_data2)
		else:
			self.PhaseAverageWidget.bars_projects_vs_average(self.avg_data_tuple, 
				self.proj_data)

	def showHideTotalTimes(self, signal) -> None:
		if signal == 2 and self.bar_or_pie == 0:
			self.PhaseAverageWidget.bars_by_phase(self.total_hours, 
				"Total Time By Phase", phase_names_length = 1)
		elif signal == 0 and self.bar_or_pie == 0:
			self.PhaseAverageWidget.bars_by_phase(self.avg_data_tuple, 
				"Average Hours Per Phase", phase_names_length = 1)

	def showHideNonbillable(self, signal) -> None:
		if signal == 2 and self.bar_or_pie == 1:
			self.PhaseAverageWidget.pie_by_phase(self.shifted_total_hours,
				"Total Billable Time Breakdown")
		elif signal == 0 and self.bar_or_pie == 1:
			self.PhaseAverageWidget.pie_by_phase(self.total_hours,
				"Total Time Breakdown")

	def showDateRange(self, signal) -> None:
		if signal == 2:
			self.StartDateEdit.show()
			self.EndDateEdit.show()
		else:
			self.StartDateEdit.hide()
			self.EndDateEdit.hide()
			self.total_hours = self.original_total_hours
			self.shifted_total_hours = self.original_shifted_total_hours
			self.avg_data_tuple = self.original_avg_tuple
			self.current_start_date = None
			self.current_end_date = None
			self.StartDateEdit.setDate(self.start_date)
			self.EndDateEdit.setDate(self.current_date)

	def selectDateRange(self) -> None:
		start_date = self.StartDateEdit.date()
		end_date = self.EndDateEdit.date()
		pyDatetime_start = start_date.toPython()
		pyDatetime_end = end_date.toPython()
		int_start_time = int(datetime(pyDatetime_start.year, pyDatetime_start.month,
			pyDatetime_start.day).timestamp())
		int_end_time = int(datetime(pyDatetime_end.year, pyDatetime_end.month, 
			pyDatetime_end.day).timestamp())
		self.current_start_date = int_start_time
		self.current_end_date = int_end_time
		self.getData(int_start_time, int_end_time)
		self.getAveragesData()
		if self.project_vs_average == 0:
			if self.bar_or_pie == 0:
				self.showHideTotalTimes(self.AvgTotalTimeChkBx.checkState().value)
			else:
				self.showHideNonbillable(self.NonBillableTimesChkBx.checkState().value)
		else:
			self.projectPhasesVsAverages()

	def projectVsAverages(self) -> None:
		self.project_vs_average = 1
		self.ShowAllProjectsChkBx.show()
		self.ProjectComboBox.show()
		self.Show2ndProjectChkBx.show()
		self.ProjectVsAveragesBtn.hide()
		self.AvgTotalTimeChkBx.hide()
		self.NonBillableTimesChkBx.hide()
		self.getAveragesData()
		self.projectPhasesVsAverages()

	def projectVsAverages2ndProject(self, signal) -> None:
		if signal == 2:
			self.Project2ComboBox.show()
			self.Show3rdProjectChkBx.show()
			self.projectPhasesVsAverages()
		else:
			self.Project2ComboBox.hide()
			self.Show3rdProjectChkBx.setChecked(False)
			self.Show3rdProjectChkBx.hide()
			self.getAveragesData()
			self.projectPhasesVsAverages()

	def projectVsAverages3rdProject(self, signal) -> None:
		if signal == 2:
			self.Project3ComboBox.show()
			self.projectPhasesVsAverages()
		else:
			self.Project3ComboBox.hide()
			self.getAveragesData()
			self.projectPhasesVsAverages()

	def projectFilter(self, signal):
		proj_index1 = self.ProjectComboBox.currentIndex()
		proj_index2 = self.Project2ComboBox.currentIndex()
		proj_index3 = self.Project3ComboBox.currentIndex()
		proj_model = self.ProjectComboBox.model()
		current_proj1_id = proj_model.data(proj_model.index(proj_index1, 0))
		current_proj2_id = proj_model.data(proj_model.index(proj_index2, 0))
		current_proj3_id = proj_model.data(proj_model.index(proj_index3, 0))
		
		if signal == 2:
			self.project_model.setFilter("project_id > 0")
		else:
			self.project_model.setFilter(
				f"project_id > 0 AND start_date > {self.start_date_int}")
		
		proj1_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, current_proj1_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if proj1_match:
			row1 = proj1_match[0].row()
			self.ProjectComboBox.setCurrentIndex(row1)
		else:
			self.ProjectComboBox.setCurrentIndex(self.original_project_row)
		
		proj2_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, current_proj2_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if proj2_match:
			row2 = proj2_match[0].row()
			self.Project2ComboBox.setCurrentIndex(row2)
		else:
			self.Project2ComboBox.setCurrentIndex(self.original_project_row)
		
		proj3_match = self.project_model.match(self.project_model.index(0,0),
			Qt.EditRole, current_proj3_id, 1, Qt.MatchFlags(Qt.MatchExactly))
		if proj3_match:
			row3 = proj3_match[0].row()
			self.Project3ComboBox.setCurrentIndex(row3)
		else:
			self.Project3ComboBox.setCurrentIndex(self.original_project_row)

class ViewProjectsOverTime(QWidget, Ui_ProjectsOverTimeWindow):
	def __init__(self) -> None:
		super(ViewProjectsOverTime, self).__init__()
		self.setupUi(self)
		self.setMinimumSize(self.size())
		self.setWindowTitle("Projects By Phase Over Time")

		with get_db_connection() as conn:
			cur = conn.cursor()
			first_proj_start_date = earliest_start_date(cur)
			self.earliest_start_date = first_proj_start_date[0]

		end_time = datetime.now()
		self.latest_end_date = int(end_time.timestamp())
		self.current_start_date = self.earliest_start_date
		self.current_end_date = self.latest_end_date
		self.projs_over_time = []
		self.projs_over_time_ids = []
		self.projs_over_time_names = []
		self.projs_over_time_list = []
		self.shifted_projs_over_time = []
		self.shifted_names_over_time = []

		self.getData()

		self.EndDateEdit.setDate(QDate.currentDate())
		start_date_datetime = datetime.fromtimestamp(self.earliest_start_date)
		self.start_date = QDate(start_date_datetime.year, start_date_datetime.month,
			start_date_datetime.day)
		self.StartDateEdit.setDate(self.start_date)

		self.ProjectsOverTimeWidget.bars_projects_by_phase(
			self.shifted_projs_over_time, self.shifted_names_over_time, "legend")

		self.StartDateEdit.userDateChanged.connect(self.selectDateRange)
		self.EndDateEdit.userDateChanged.connect(self.selectDateRange)

		self.show()

	def getData(self) -> None:
		self.projs_over_time_list = []
		with get_db_connection() as conn:
			cur = conn.cursor()
			self.projs_over_time = project_ids_over_time_period(
				self.current_start_date, self.current_end_date, cur)
			self.projs_over_time_ids = [proj[0] for proj in self.projs_over_time]
			self.projs_over_time_names = [proj[1] for proj in self.projs_over_time]
			for proj_id in self.projs_over_time_ids:
				self.projs_over_time_list.append(
					phase_duration_by_project(proj_id, cur, 
						self.current_start_date, self.current_end_date))

		if ("Administration" in self.projs_over_time_names and 
			"Business Development" in self.projs_over_time_names):
			self.shifted_projs_over_time = (self.projs_over_time_list[2:] 
				+ self.projs_over_time_list[1:2] + self.projs_over_time_list[0:1])
			self.shifted_names_over_time = (self.projs_over_time_names[2:] 
				+ self.projs_over_time_names[1:2] + self.projs_over_time_names[0:1])
		elif ("Administration" in self.projs_over_time_names or 
			"Business Development" in self.projs_over_time_names):
			self.shifted_projs_over_time = (self.projs_over_time_list[1:] 
				+ self.projs_over_time_list[0:1])
			self.shifted_names_over_time = (self.projs_over_time_names[1:] 
				+ self.projs_over_time_names[0:1])
		else:
			self.shifted_projs_over_time = self.projs_over_time_list
			self.shifted_names_over_time = self.projs_over_time_names

	def selectDateRange(self) -> None:
		start_date = self.StartDateEdit.date()
		end_date = self.EndDateEdit.date()
		pyDatetime_start = start_date.toPython()
		pyDatetime_end = end_date.toPython()
		int_start_time = int(datetime(pyDatetime_start.year, pyDatetime_start.month,
			pyDatetime_start.day).timestamp())
		int_end_time = int(datetime(pyDatetime_end.year, pyDatetime_end.month, 
			pyDatetime_end.day).timestamp())
		self.current_start_date = int_start_time
		self.current_end_date = int_end_time

		self.getData()
		self.ProjectsOverTimeWidget.bars_projects_by_phase(
			self.shifted_projs_over_time, self.shifted_names_over_time, "legend")


#		~~~TIME LOGGERS~~~

class TimerDisplay(QLCDNumber):
	def __init__(self, parent = None) -> None:
		super().__init__(parent)
		self.setWindowTitle("Timer")

		QTimer.singleShot(0, lambda: self.display("   00:00"))
		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.timeout.connect(self.update_lcd)
		self.timer.start()

	def update_lcd(self) -> None:
		elapsed_time = self.parent().time_log.elapsedTime()
		qt_time = QTime(0, 0, 0).addSecs(int(elapsed_time))
		self.display(qt_time.toString("   hh:mm"))


# Import ui.TimeLogger after TimerDisplay to stop circular import
from ui.TimeLogger import Ui_TimeLoggerWindow	  # noqa: E402

class TimeLogger(QWidget, Ui_TimeLoggerWindow):
	def __init__(self, main_window) -> None:
		super(TimeLogger, self).__init__()
		self.main_window = main_window
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Timer")

		self.architect_model = QSqlTableModel()
		self.architect_model.setTable("architects")
		self.architect_model.select()
		self.ArchitectComboBox.setModel(self.architect_model)
		self.ArchitectComboBox.setModelColumn(1)				
		setLinkedComboBox(self.main_window.ArchitectsComboBox,
			self.ArchitectComboBox)

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter("status = 'Active'")
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

	def phaseChanged(self) -> None:
		# Get current index and phase_id from phases combo box
		phase_index = self.PhaseComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))

		# Set project ComboBox and disable phase ComboBox if phase is 
		# 	Business Development or Administration
		if phase_id in (ADMIN, BUSDEV):
			self.PhaseComboBox.setEnabled(False)
			if phase_id == ADMIN:
				self.ProjectComboBox.setCurrentIndex(1)
			else:
				self.ProjectComboBox.setCurrentIndex(0)
			return
		else:
			self.PhaseComboBox.setEnabled(True)

	def startPauseTime(self) -> None:
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

	def stopTime(self) -> None:
		if self.time_log.start_time == 0:
			self.main_window.showNormal()
			self.close()
			return
		self.timer.timer.stop()
		self.time_log.end_time = datetime.now()
		total_time = 0
		if self.time_log.timer_state == "running":
			self.time_log.timer_state = "paused"
		total_time = ((self.time_log.end_time - 
			self.time_log.start_time).total_seconds() - 
			self.time_log.total_pause_duration)
		start_time = int(self.time_log.start_time.timestamp())
		end_time = int(self.time_log.end_time.timestamp())
		
		total_minutes = total_time // 60
		quarter_hours = total_minutes // 15
		if total_minutes % 15 > 0:
			quarter_hours += 1
		total_time_logged = quarter_hours * 15

		if total_time_logged == 0:
			self.main_window.showNormal()
			self.close()
			return

		self.timeNotes = TimeEntriesNotesWindow()
		self.timeNotes.exec()

		arch_index = self.ArchitectComboBox.currentIndex()
		arch_id = self.architect_model.data(self.architect_model.index(arch_index, 0))

		phase_index = self.PhaseComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))

		if phase_id == ADMIN:
			proj_id = -1
		elif phase_id == BUSDEV:
			proj_id = -2
		else:
			proj_index = self.ProjectComboBox.currentIndex()
			proj_id = self.project_model.data(self.project_model.index(proj_index, 0))

		time_notes = self.timeNotes.notesTextEdit.toPlainText()

		query = QSqlQuery()
		query.prepare("""INSERT INTO time_entries\
			(project_id, architect_id, phase_id, start_time, end_time, \
			duration_minutes, notes) \
			VALUES (?, ?, ?, ?, ?, ?, ?)""")
		query.addBindValue(proj_id)
		query.addBindValue(arch_id)
		query.addBindValue(phase_id)
		query.addBindValue(start_time)
		query.addBindValue(end_time)
		query.addBindValue(total_time_logged)
		query.addBindValue(time_notes)

		if not query.exec():
			print(f"Insert failed: {query.lastError().text()}")
		else:
			if self.main_window.view_time_entries_window is not None:
				self.main_window.view_time_entries_window.model.select()

		self.main_window.showNormal()
		self.close()

	def closeEvent(self, event) -> None:
		self.main_window.showNormal()

class TimeLog():
	def __init__(self) -> None:
		self.timer_state = "inactive"
		self.total_time = 0
		self.start_time = 0
		self.end_time = 0
		self.pause_start_time = 0
		self.total_pause_duration = 0

	def elapsedTime(self) -> int:
		if self.timer_state == "running":
			self.total_time = ((datetime.now() - self.start_time).total_seconds()
				- self.total_pause_duration)
		elif self.timer_state == "paused":
			self.total_time = ((self.pause_start_time - self.start_time).total_seconds()
				- self.total_pause_duration)
		return self.total_time

class TimeEntriesNotesWindow(QDialog, Ui_TimeNotesDialog):
	def __init__(self) -> None:
		super(TimeEntriesNotesWindow, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Notes")


class ManualTimeLogger(QDialog, Ui_AddTimeDialog):
	"""Class for a user to manually input a time entry with duration validation"""
	def __init__(self, main_window) -> None:
		super(ManualTimeLogger, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.main_window = main_window
		self.setWindowTitle("Add Time")
		
		self.architect_model = QSqlTableModel()
		self.architect_model.setTable("architects")
		self.architect_model.select()
		self.ArchitectComboBox.setModel(self.architect_model)
		self.ArchitectComboBox.setModelColumn(1)				
		setLinkedComboBox(self.main_window.ArchitectsComboBox,
			self.ArchitectComboBox)

		self.project_model = QSqlTableModel()
		self.project_model.setTable("projects")
		self.project_model.setFilter("status = 'Active'")
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

		# Set current time onto the time edit drop downs
		self.timeStartEdit.setDateTime(QDateTime.currentDateTime())
		self.timeEndEdit.setDateTime(QDateTime.currentDateTime())
		#self.timeEndEdit.setDate(QTime.currentTime())

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

	def phaseChanged(self) -> None:
		# Get current index and phase_id from phases combo box
		phase_index = self.PhaseComboBox.currentIndex()
		phase_id = self.phase_model.data(self.phase_model.index(phase_index, 0))

		# Set project ComboBox and disable phase ComboBox if phase is 
		# 	Business Development or Administration
		if phase_id in (ADMIN, BUSDEV):
			self.PhaseComboBox.setEnabled(False)
			if phase_id == ADMIN:
				self.ProjectComboBox.setCurrentIndex(1)
			else:
				self.ProjectComboBox.setCurrentIndex(0)
			return
		else:
			self.PhaseComboBox.setEnabled(True)

	def accept(self) -> None:
		"""Method to verify all forms were entered with correct syntax"""
		time_start = self.timeStartEdit.dateTime()
		end_time = self.timeEndEdit.dateTime()
		
		if end_time <= time_start:
			QMessageBox.warning(self, "Invalid Duration", 
				"Please ensure End Time is later than Start Time")
			return

		super().accept()

class AddInvoiceNumber(QDialog, Ui_AddInvoiceDialog):
	def __init__(self) -> None:
		super(AddInvoiceNumber, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Invoice Number")

class DeleteInvoiceWarning(QDialog, Ui_DeleteInvoiceDialog):
	def __init__(self) -> None:
		super(DeleteInvoiceWarning, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("DELETE Invoice")

class DeleteTimeEntryWarning(QDialog, Ui_DeleteTimeEntryDialog):
	def __init__(self) -> None:
		super(DeleteTimeEntryWarning, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("DELETE Time Log")

class CreateNewDatabase(QDialog, Ui_CreateDatabaseDialog):
	def __init__(self) -> None:
		super(CreateNewDatabase, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Create New Database")

class LoadOldDatabase(QDialog, Ui_LoadDatabaseDialog):
	def __init__(self) -> None:
		super(LoadOldDatabase, self).__init__()
		self.setupUi(self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Load Archived Database")


#		~~~TABLE MODELS~~~

class ArchitectsTableModel(QSqlTableModel):
	"""Class to disallow deletions of entire rows in table views and to 
	check for valid email address and phone number on user edit"""
	def removeRows(self, row, count, parent=None) -> bool:
		return False

	def setData(self, index, value, role = Qt.EditRole) -> bool:
		# Get column database names to safety desired column entries by user
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


class ProjectsRelationalTableModel(QSqlRelationalTableModel):
	"""Class to disallow deletions of entire rows in relational table views 
	and to check and reformat date on user edit"""
	def removeRows(self, row, count, parent=None) -> bool:
		return False

	def data(self, index, role = Qt.DisplayRole) -> any:
		field_name = self.record().fieldName(index.column())
		value = super().data(index, role)

		if (field_name == "start_date" and value is not None 
			and role == Qt.DisplayRole):
			date_time = datetime.fromtimestamp(value)
			value = date_time.strftime("%m/%d/%Y")
			return value

		return super().data(index, role)

	def setData(self, index, value, role = Qt.EditRole) -> bool:
		field_name = self.record().fieldName(index.column())

		if field_name == "project_phase":
			if isinstance(value, str):
				return super().setData(index, value, role)
			if value > 7:
				return False

		return super().setData(index, value, role)

class TimeEntriesRelationalTableModel(QSqlRelationalTableModel):
	"""Class to ensure proper formatting and display of ViewTimeEntries model"""
	def data(self, index, role = Qt.DisplayRole) -> any:
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
			value = date_time.strftime("%m/%d/%Y   %I:%M %p")

		if field_name == "end_time" and value is not None:
			date_time = datetime.fromtimestamp(value)
			value = date_time.strftime("%m/%d/%Y   %I:%M %p")

		# Display a blank string if invoice_number == 0
		if field_name == "invoice_number" and value == "Not Invoiced":
			value = ""

		return value

	def setData(self, index, value, role = Qt.EditRole) -> bool:
		field_name = self.record().fieldName(index.column())

		# Reset a user's entered start date and time to an int
		if field_name in ("start_time", "end_time"):
			row = index.row()
			start_time_column = self.fieldIndex("start_time")
			start_time_index = self.index(row, start_time_column)

			end_time_column = self.fieldIndex("end_time")
			end_time_index = self.index(row, end_time_column)

			time_entry_id_column = self.fieldIndex("time_entry_id")
			time_entry_index = self.index(row, time_entry_id_column)
			time_entry_id = self.data(time_entry_index)

			start_time = 0
			end_time = 0

			if field_name == "start_time":
				end_time = self.data(end_time_index, Qt.EditRole)
				start_time = value
			elif field_name == "end_time":
				start_time = self.data(start_time_index, Qt.EditRole)
				end_time = value
			if start_time >= end_time:
				return False

			duration_column = self.fieldIndex("duration_minutes")
			duration_index = self.index(row, duration_column)

			new_duration_seconds = end_time - start_time
			new_duration_minutes = new_duration_seconds / 60
			new_duration = validateDuration(new_duration_minutes)

			query = QSqlQuery()
			query.prepare("""UPDATE time_entries SET duration_minutes = ?\
				WHERE time_entry_id = ?""")
			query.addBindValue(new_duration)
			query.addBindValue(time_entry_id)
			if not query.exec():
				print(f"Update failed: {query.lastError().text()}")

			super().setData(duration_index, new_duration, role)

		# Safety a Business Dev or Admin project from having an incorrect status
		if field_name == "project_name":
			# On project name change setData fires twice, 
			# 	ignore first one where value is str, only use 2nd where value is int
			if isinstance(value, str):
				return super().setData(index, value, role)

			old_proj = self.data(index, role)
			new_proj_id = value
			
			phase_id = None
			if new_proj_id < 0:
				phase_id = BUSDEV if new_proj_id == -2 else ADMIN

			# if the phase id is currently 8 or 9, then change it to whatever 
			#	the last phase was for the project in the database
			elif old_proj == "Administration" or old_proj == "Business Development":
				with get_db_connection() as conn:
					cur = conn.cursor()
					phase_id = get_most_recent_project_phase(new_proj_id, cur)
				# If project has no previous time entries
				if not phase_id:
					phase_id = 1
			else:
				phase_id = None
			if phase_id is not None:
				phase_column = self.fieldIndex("project_phase")
				phase_index = self.index(index.row(), phase_column)
				super().setData(phase_index, phase_id, role)

		# Safety a project's status to being changed to Administration or 
		#	Business Development
		if field_name == "project_phase":
			if isinstance(value, str):
				return super().setData(index, value, role)
			old_phase = self.data(index, role)
			new_phase = value
			if old_phase == "Administration" or old_phase == "Business Development":
				return False
			elif new_phase > len(PHASES) - 2:
				return False

		if field_name == "invoice_number":
			# Ignore firing twice issue
			if isinstance(value, str):
				return super().setData(index, value, role)

			project_column = self.fieldIndex("project_name")
			row = index.row()
			project_index = self.index(row, project_column)
			project_name = self.data(project_index)

			# Get project_id from invoice and from project to make sure they are equal
			with get_db_connection() as conn:
				cur = conn.cursor()
				invoice_sql = "SELECT project_id FROM invoices WHERE invoice_id = ?"
				cur.execute(invoice_sql, (value,))
				invoice_result = cur.fetchone()
				invoice_proj_id = invoice_result[0]

				project_sql = "SELECT project_id FROM projects WHERE project_name = ?"
				cur.execute(project_sql, (project_name,))
				project_result = cur.fetchone()
				proj_project_id = project_result[0]
			# Allow time entries to be set to 'Not Invoiced'
			if value == 0:
				return super().setData(index, value, role)
			if invoice_proj_id != proj_project_id:
				return False

		return super().setData(index, value, role)

	def flags(self, index):
		flags = super().flags(index)
		if self.record().fieldName(index.column()) == "duration_minutes":
			flags &= ~Qt.ItemIsEditable
		return flags

class InvoiceRelationalTableModel(QSqlRelationalTableModel):
	"""Class to reformat created date for invoices"""
	def data(self, index, role = Qt.DisplayRole) -> any:
		field_name = self.record().fieldName(index.column())
		value = super().data(index, role)

		if (field_name == "created_date" and value is not None 
			and role == Qt.DisplayRole):
			date_time = datetime.fromtimestamp(value)
			value = date_time.strftime("%m/%d/%Y")
			return value

		if (field_name == "invoice_number" and role == Qt.TextAlignmentRole):
			return Qt.AlignCenter

		return super().data(index, role)

	def setData(self, index, value, role = Qt.EditRole) -> bool:
		field_name = self.record().fieldName(index.column())

		if field_name == "invoice_number":
			value = value.strip()
			if not value:
				return False

		return super().setData(index, value, role)


#		~~~DELEGATES~~~

class StatusDelegate(QStyledItemDelegate):
	"""Class to allow drop down ComboBoxes for table cells where only a specific
	selection of values is allowed"""
	def __init__(self, options, parent=None) -> None:
		super().__init__(parent)
		self.options = options

	def createEditor(self, parent, options, index) -> QComboBox:
		# Create and return a combo box as the editor
		combo = QComboBox(parent)
		combo.addItems(self.options)
		return combo

	def setEditorData(self, editor, index) -> None:
		# Set the current value on the combo box
		current_value = index.data()
		current_index = editor.findText(current_value)
		if current_index >= 0:
			editor.setCurrentIndex(current_index)

	def setModelData(self, editor, model, index) -> None:
		# Save the value back to the model
		value = editor.currentText()
		model.setData(index, value)

class TimeDelegate(QStyledItemDelegate):
	"""Class to validate manual date/time input by user"""
	def createEditor(self, parent, options, index) -> QDateTimeEdit:
		editor = QDateTimeEdit(parent)
		editor.setCalendarPopup(True)
		editor.setDisplayFormat("M/d/yy H:mm Ap")
		return editor

	def setEditorData(self, editor, index) -> None:
		value = index.model().data(index, Qt.EditRole)
		if isinstance(value, int):
			date_datetime = datetime.fromtimestamp(value)
			date_time = QDateTime(date_datetime.year, date_datetime.month, 
				date_datetime.day, date_datetime.hour, date_datetime.minute,
				date_datetime.second)
			editor.setDateTime(date_time)

	def setModelData(self, editor, model, index) -> None:
		dateTime = editor.dateTime()
		# set this on db as int 
		pyDatetime = dateTime.toPython()
		time_log_int = int(pyDatetime.timestamp())
		model.setData(index, time_log_int, Qt.EditRole)

class CreatedDateDelegate(QStyledItemDelegate):
	"""Class to validate manual date input by user"""
	def createEditor(self, parent, options, index) -> QDateEdit:
		editor = QDateEdit(parent)
		editor.setCalendarPopup(True)
		editor.setDisplayFormat("M/d/yy")
		return editor

	def setEditorData(self, editor, index) -> None:
		value = index.model().data(index, Qt.EditRole)
		if isinstance(value, int):
			date_datetime = datetime.fromtimestamp(value)
			date = QDate(date_datetime.year, date_datetime.month,
				date_datetime.day)
			editor.setDate(date)

	def setModelData(self, editor, model, index) -> None:
		date = editor.date()
		pyDate = date.toPython()
		pyDate_datetime = datetime(pyDate.year, pyDate.month, pyDate.day)
		start_time_int = int(pyDate_datetime.timestamp())
		model.setData(index, start_time_int, Qt.EditRole)


class InvoiceCheckboxDelegate(QStyledItemDelegate):
	"""Delegate to show check-boxes in selection mode or drop-down in normal mode"""
	def __init__(self, model, parent=None) -> None:
		super().__init__(parent)
		self.selection_mode = False
		self.checked_rows = set()
		self.model = model
		self.relational_delegate = QSqlRelationalDelegate(parent)
	
	def paint(self, painter, option, index) -> None:
		# If in selection mode and row is not invoiced, draw checkbox
		if self.selection_mode:
			invoice_id = index.data(Qt.EditRole)
			if invoice_id == "Not Invoiced":
				# Draw checkbox
				checkbox_rect = self.getCheckboxRect(option.rect)
				check_state = Qt.Checked if index.row() in self.checked_rows else Qt.Unchecked
				
				checkbox = QStyleOptionButton()
				checkbox.rect = checkbox_rect
				checkbox.state = QStyle.State_Enabled
				if check_state == Qt.Checked:
					checkbox.state |= QStyle.State_On
				else:
					checkbox.state |= QStyle.State_Off
				
				QApplication.style().drawControl(QStyle.CE_CheckBox, checkbox, painter)
				return
		
		# Otherwise, use relational delegate for drop-down display
		self.relational_delegate.paint(painter, option, index)
	
	def createEditor(self, parent, option, index) -> QWidget | None:
		# If in selection mode, no editor needed for check-boxes
		if self.selection_mode:
			return None
		
		# Otherwise, use relational delegate to create drop-down
		return self.relational_delegate.createEditor(parent, option, index)
	
	def setEditorData(self, editor, index) -> None:
		# Not in selection mode, use relational delegate
		if not self.selection_mode:
			self.relational_delegate.setEditorData(editor, index)
	
	def setModelData(self, editor, model, index) -> None:
		# Not in selection mode, use relational delegate
		if not self.selection_mode:
			self.relational_delegate.setModelData(editor, model, index)
	
	def editorEvent(self, event, model, option, index) -> None:
		# Handle checkbox clicks in selection mode
		if self.selection_mode:
			invoice_id = index.data(Qt.EditRole)
			if invoice_id == "Not Invoiced":
				if event.type() == QEvent.MouseButtonRelease:
					if index.row() in self.checked_rows:
						self.checked_rows.discard(index.row())
					else:
						self.checked_rows.add(index.row())
					# Trigger repaint
					model.dataChanged.emit(index, index)
					return True
		
		# Otherwise use relational delegate
		return self.relational_delegate.editorEvent(event, model, option, index)
	
	def getCheckboxRect(self, rect) -> QRect:
		# Center the checkbox in the cell
		checkbox_size = 20
		x = rect.x() + (rect.width() - checkbox_size) // 2
		y = rect.y() + (rect.height() - checkbox_size) // 2
		return QRect(x, y, checkbox_size, checkbox_size)


#		~~~FUNCTIONS~~~		

def setCrossComboBox(source_combo: QComboBox, target_combo: QComboBox, 
	column: int = 1) -> None:
	"""Function to pull the information from one combo box and populate 
	it on a combo box elsewhere in the program; column parameter is the column
	on the source_combo table you want to match to your target_combo's table"""
	row = source_combo.currentIndex()
	model = source_combo.model()
	item_id = model.data(model.index(row, column))

	matches = target_combo.model().match(target_combo.model().index(0,0),
		Qt.EditRole, item_id, 1, Qt.MatchFlags(Qt.MatchExactly))
	if matches:
		row = matches[0].row()
		target_combo.setCurrentIndex(row)

def setLinkedComboBox(source_combo: QComboBox, target_combo: QComboBox) -> None:
	"""Function to set a target ComboBox to the chosen value in the target,
	both combo boxes must hold the same table and column"""
	target_combo.setCurrentIndex(source_combo.currentIndex())


def validateDuration(duration: str) -> int:
	"""Function to parse duration input and return it as a total minutes int
	rounded up to the next 15 minute increment"""
	if not duration:
		return
	minutes = 0
	hours = 0
	if isinstance(duration, str) and ":" in duration:
		if duration.count(":") != 1:
			raise ValueError
		if duration[0] == ":":
			minutes = int(duration[1:])
		else:
			hours, minutes = duration.split(":")
			hours = int(hours)
			minutes = int(minutes)
	elif isinstance(duration, str) and "." in duration:
		if duration.count(".") != 1:
			raise ValueError
		if duration[0] == ".":
			minutes = 60 * float(duration)
		else:
			hours, percent_minutes = duration.split(".")
			if len(percent_minutes) == 1:
				percent_minutes += "0"
			hours = int(hours)
			minutes = 60 * (int(percent_minutes) / 100)

	else:
		minutes = int(duration)
	quarter_hours = minutes // 15
	if minutes % 15:
		quarter_hours += 1
	minutes = quarter_hours * 15

	return hours * 60 + minutes

def deleteEmptyInvoices() -> None:
	"""Delete invoices with no time_entry logs attached"""
	with get_db_connection() as conn:
		cur = conn.cursor()
		no_times_invoices_tuples = load_invoice_ids_no_time_entries(cur)
		no_times_invoices = [items[0] for items in no_times_invoices_tuples]
		for invoice_id in no_times_invoices:
			delete_invoice(invoice_id, cur)
