# Test for architectsLog_classes.py

from architectsLog_classes import Architect, Project, Invoice, TimeEntry
from datetime import datetime

#	~CLASS CREATION AND INITIALIZATION TESTS~~~

#test if the Architect class instance is initialized correctly
def test_architect_initialization():
	"""Test if the Architect class instance is created and __init__() initializes correctly"""
	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")

	assert testArchitect.name == "Name"
	assert testArchitect.license_number == "LicenseNumber01"
	assert testArchitect.phone_number == "123-456-7890"
	assert testArchitect.email == "email@domain.com"
	assert testArchitect.company_name == "MyCompany"
	assert testArchitect.status == "Active"
	assert testArchitect.architect_id is None

#test if the Project class instance is initialized correctly
def test_project_initialization():
	"""Test if the Project class instance is created and __init__() initializes correctly"""
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025")

	assert testProject.project_name == "NewProject"
	assert testProject.client_name == "NewClient"
	assert testProject.client_address == "123ClientStreet"
	assert testProject.start_date == "01-01-2025"
	assert testProject.current_phase_id == 1
	assert testProject.status == "Active"
	assert testProject.project_id is None

#test if the Invoice class instance is initialized correctly
def test_invoice_initialization():
	"""Test if the Invoice class is created and __init__() initializes correctly"""
	test_project_id = 1
	date = "01-01-2025"
	invoice_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(invoice_date.timestamp())
	testInvoice = Invoice(1, int_date, test_project_id)

	assert testInvoice.invoice_number == 1
	assert testInvoice.created_date == int_date
	assert testInvoice.project_id == test_project_id
	assert testInvoice.status == "Draft"
	assert testInvoice.invoice_id is None

#test if the TimeEntry class instance is initialized correctly
def test_time_entry_initialization():
	"""Test if the TimeEntry class is created and __init__() initializes correctly"""
	start_time = "01-01-2025 12:00:00"
	duration = 30

	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025")
	testTimeEntry = TimeEntry(start_time, duration, testProject.project_id, testArchitect.architect_id, 
		notes = "Note", invoice_id = 1)

	assert testTimeEntry.start_time == start_time
	assert testTimeEntry.duration_minutes == duration
	assert testTimeEntry.project_id == testProject.project_id
	assert testTimeEntry.architect_id == testArchitect.architect_id
	assert testTimeEntry.phase_id == 1
	assert testTimeEntry.notes == "Note"
	assert testTimeEntry.invoice_id == 1
	assert testTimeEntry.time_entry_id is None
