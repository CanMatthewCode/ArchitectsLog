from architectsLog_classes import Architect, Project, Invoice, TimeEntry
import time
from datetime import datetime

#	~CLASS CREATION AND INITIALIZATION TESTS~~~

#test if the Architect class instance is initialized correctly
def test_architect_initialization():
	"""Test if the Architect class instance is created and __init__() initializes correctly"""
	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")

	assert testArchitect.name ==  "Name"
	assert testArchitect.license_number == "LicenseNumber01"
	assert testArchitect.phone_number == "123-456-7890"
	assert testArchitect.email =="email@domain.com"
	assert testArchitect.company_name == "MyCompany"
	assert testArchitect.is_active == 1
	assert testArchitect.architect_id == None

#test if the Project class instance is initialized correctly
def test_project_initialization():
	"""Test if the Project class instance is created and __init__() initializes correctly"""
	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025", testArchitect)

	assert testProject.project_name == "NewProject"
	assert testProject.client_name == "NewClient"
	assert testProject.client_address == "123ClientStreet"
	assert testProject.start_date == "01-01-2025"
	assert testProject.architect == testArchitect
	assert testProject.current_phase_id == 1
	assert testProject.status == "active"
	assert testProject.project_id == None

#test if the Invoice class instance is initialized correctly
def test_invoice_initialization():
	"""Test if the Invoice class is created and __init__() initializes correctly"""
	testInvoice = Invoice(1, "01-01-2025")

	assert testInvoice.invoice_number == 1
	assert testInvoice.created_date == "01-01-2025"
	assert testInvoice.invoice_id == None
	assert testInvoice.project_id == None

#test if the TimeEntry class instance is initialized correctly
def test_time_entry_initialization():
	"""Test if the TimeEntry class is created and __init__() initializes correctly"""
	start_time = "01-01-2025 12:00:00"
	end_time = "01-01-2025 12:30:00"
	duration = 30

	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025", testArchitect)
	testTimeEntry = TimeEntry(start_time, end_time, duration, testProject, testArchitect)

	assert testTimeEntry.start_time == start_time
	assert testTimeEntry.end_time == end_time
	assert testTimeEntry.duration_minutes == duration
	assert testTimeEntry.project == testProject
	assert testTimeEntry.architect == testArchitect
	assert testTimeEntry.time_entry_id == None
	assert testTimeEntry.phase_id == 1
	assert testTimeEntry.invoice_id == None
	assert testTimeEntry.notes == None