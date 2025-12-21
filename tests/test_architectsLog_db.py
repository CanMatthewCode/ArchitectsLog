#testing for acrchitectsLog_db.py

import pytest
import os
import sqlite3

from architectsLog_db import get_connection, create_architect_table, create_project_table, \
 create_phases_table, create_invoices_table, create_time_entries_table, add_architect, \
 initialize_phases, add_project, add_invoice, add_time_entry, load_all_active_architects, \
 load_all_architects, load_architect, load_all_active_projects, load_all_projects, \
 load_project, load_invoice, load_project_invoices, load_status_invoices, load_all_invoices, \
 load_time_entry, load_all_project_time_entries, load_all_architect_time_entries, \
 load_invoice_time_entries, load_all_time_entries, load_nonproject_phases_time_entries, \
 update_architect, update_project, update_invoice, update_time_entry, \
 delete_invoice, delete_time_entry


from architectsLog_classes import Architect, Project, Invoice, TimeEntry

TEST_DB = 'test_architectsLog.db'

#	~~~PYTEST.FIXTURES AND DATABASE CONNECTIONS~~~

#create a database auto cleanup before and after each test
@pytest.fixture(autouse=True)
def cleanup_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

#create a connection for the databases then closes them before each test
@pytest.fixture
def test_conn():
    """Fixture that provides a test connection and cleans up after"""
    conn = get_connection(TEST_DB)
    yield conn
    conn.close()

#create all tables and populate or initialize them 
@pytest.fixture
def table_initialize(test_conn):
	#create cursor, create architects table, create projects table, create invoices table and
	#commit them to the database
	cur = test_conn.cursor()
	create_architect_table(cur)
	create_phases_table(cur)
	create_project_table(cur)
	create_invoices_table(cur)
	create_time_entries_table(cur)
	test_conn.commit()

	#add an architect to Architect table to get architect_id assigned
	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")
	architect_id = add_architect(testArchitect, cur)

	#initialize the phases table
	initialize_phases(cur)

	#create a test project with testArchitect and add it to the project table
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025")
	project_id = add_project(testProject, cur)

	#create a test invoice with testProject and add it to the invoice table
	testInvoice = Invoice(1, "01-01-2025", testProject)
	invoice_id = add_invoice(testInvoice, cur)

	#create a test time entry with testProject and testArchitect and add it to the time_entries table
	testTimeEntry = TimeEntry("01-01-2025 12:00:00", 30, testProject, testArchitect.architect_id,
		notes= "Note", invoice_id= 1)
	time_entry_id = add_time_entry(testTimeEntry, cur)

	#commit and return the created objects as a dictionary 
	test_conn.commit()

	return {
		'architect' : testArchitect,
		'architect_id' : architect_id,
		'project' : testProject,
		'project_id' : project_id,
		'invoice' : testInvoice,
		'invoice_id' : invoice_id,
		'time_entry' : testTimeEntry,
		'time_entry_id' : time_entry_id
	}


#tests if the database connection works
def test_get_connection_creates_connection(test_conn):
    """Test that get_connection returns a valid connection"""
    assert test_conn is not None
    assert isinstance(test_conn, sqlite3.Connection)

#tests if foreign keys are actually enabled 
def test_foreign_keys_enabled(test_conn):
    """Test that foreign keys are enabled on connection"""
    cursor = test_conn.cursor()
    cursor.execute("PRAGMA foreign_keys")
    result = cursor.fetchone()[0]
    assert result == 1, "Foreign keys should be enabled"



#	~~~TABLE CREATION TESTS~~~

#test if architects table was created
def test_architect_table_creation(test_conn):
	"""Test that the architects table is created"""
	cursor = test_conn.cursor()
	create_architect_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' \
		AND name='architects'")
	result = cursor.fetchone()

	assert result is not None, "architects table should exist"
	assert result[0] == 'architects'


#test if projects table was created
def test_project_table_creation(test_conn):
	"""Test that the projects table is created"""
	cursor = test_conn.cursor()
	create_project_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' \
		AND name='projects'")
	result = cursor.fetchone()

	assert result is not None, "projects table should exist"
	assert result[0] == 'projects'


#test if phases table was created
def test_phase_table_creation(test_conn):
	"""Test that the phases table is created"""
	cursor = test_conn.cursor()
	create_phases_table(cursor)

	#query sqlite_master to check if the table exits
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' \
		AND name='phases'")
	result = cursor.fetchone()

	assert result is not None, "phases table should exist"
	assert result[0] == 'phases'


#test if invoices table was created
def test_create_invoices_table(test_conn):
	"""Test that the invoices table is created"""
	cursor = test_conn.cursor()
	create_invoices_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' \
		AND name='invoices'")
	result = cursor.fetchone()

	assert result is not None, "invoices table should exist"
	assert result[0] == 'invoices'


#test if time_entries table was created
def test_create_time_entries_table(test_conn):
	"""Test that the time_entries table is created"""
	cursor = test_conn.cursor()
	create_time_entries_table(cursor)

	#query sqlite_master to check if time_entries table is created
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' \
		AND name='time_entries'")
	result = cursor.fetchone()

	assert result is not None, "time_entries table should exist"
	assert result[0] == 'time_entries'	



#	~~FIXTURE FOR GETTING TABLE INFORMATION~~

#create a generic fixture so I can get table information for all table tests
@pytest.fixture
def table_info(test_conn):
	"""Generic fixture that returns table info for a given table"""
	def _get_table_info(table_name, create_func):
		"""
		Create a table and return its column info

		Args:
			table_name: Name of the table to query
			create_func: Function that creates the table
		"""
		cursor = test_conn.cursor()
		create_func(cursor)
		test_conn.commit()
		cursor.execute(f"PRAGMA table_info({table_name})")
		return cursor.fetchall()

	return _get_table_info



#	~~~TABLE COLUMN NAME AND COLUMN TYPE TESTS~~~

#test if architects table has correct column names
def test_architect_table_column_names(table_info):
	"""Test that the architects table has correct column names"""
	column_names = [col[1] for col in table_info('architects', create_architect_table)]

	assert 'architect_id' in column_names
	assert 'name' in column_names
	assert 'license_number' in column_names
	assert 'phone_number' in column_names
	assert 'email' in column_names
	assert 'company_name' in column_names
	assert 'status' in column_names

#test if architects table has correct column types
def test_architect_table_column_types(table_info):
	"""Test that the architects table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('architects', create_architect_table)}

	assert column_types['architect_id'] == 'INTEGER'
	assert column_types['name'] == 'TEXT'
	assert column_types['license_number'] == 'TEXT'
	assert column_types['phone_number'] == 'TEXT'
	assert column_types['email'] == 'TEXT'
	assert column_types['company_name'] == 'TEXT'
	assert column_types['status'] == 'TEXT'


#test if projects table has correct column names
def test_project_table_column_names(table_info):
	"""Test that the projects table has correct column names"""
	column_names = [col[1] for col in table_info('projects', create_project_table)]

	assert 'project_id' in column_names
	assert 'project_name' in column_names
	assert 'client_name' in column_names
	assert 'client_address' in column_names
	assert 'start_date' in column_names
	assert 'current_phase_id' in column_names
	assert 'status' in column_names

#test if projects table has correct column types
def test_project_table_column_types(table_info):
	"""Test that the projects table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('projects', create_project_table)}

	assert column_types['project_id'] == 'INTEGER'
	assert column_types['project_name'] == 'TEXT'
	assert column_types['client_name'] == 'TEXT'
	assert column_types['client_address'] == 'TEXT'
	assert column_types['start_date'] == 'TEXT'
	assert column_types['current_phase_id'] == 'INTEGER'
	assert column_types['status'] == 'TEXT'


#test if phases table has correct column names
def test_phases_table_column_names(table_info):
	"""Test that the phases table has correct column names"""
	column_names = [col[1] for col in table_info('phases', create_phases_table)]

	assert 'phase_id' in column_names
	assert 'project_phase' in column_names

#test if phases table has correct column types
def test_phase_table_column_types(table_info):
	"""Test that the phases table has the correct column types"""
	column_types = {col[1] : col[2] for col in table_info('phases', create_phases_table)}

	assert column_types['phase_id'] == 'INTEGER'
	assert column_types['project_phase'] == 'TEXT'


#test if the invoices table has correct column names
def test_create_invoices_table_column_names(table_info):
	"""Test that the invoices table has correct column names"""
	column_names = [col[1] for col in table_info('invoices', create_invoices_table)]

	assert 'invoice_id' in column_names
	assert 'project_id' in column_names
	assert 'created_date' in column_names
	assert 'invoice_number' in column_names
	assert 'status' in column_names

#test if the invoices table has correct column types
def test_create_invoices_table_column_types(table_info):
	"""Test that the invoices table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('invoices', create_invoices_table)}

	assert column_types['invoice_id'] == 'INTEGER'
	assert column_types['project_id'] == 'INTEGER'
	assert column_types['created_date'] == 'TEXT'
	assert column_types['invoice_number'] == 'INTEGER'
	assert column_types['status'] == 'TEXT'


#test if the time_entries table has correct column names
def test_create_time_entries_table_names(table_info):
	"""Test that the time_entries table has correct column names"""
	column_names = [col[1] for col in table_info('time_entries', create_time_entries_table)]

	assert 'time_entry_id' in column_names
	assert 'project_id' in column_names
	assert 'architect_id' in column_names
	assert 'phase_id' in column_names
	assert 'start_time' in column_names
	assert 'duration_minutes' in column_names
	assert 'notes' in column_names
	assert 'invoice_id' in column_names

#test if the time_entries table has correct column types
def test_create_time_entries_table_types(table_info):
	"""Test that the time_entries table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('time_entries', create_time_entries_table)}

	assert column_types['time_entry_id'] == 'INTEGER'
	assert column_types['project_id'] == 'INTEGER'
	assert column_types['architect_id'] == 'INTEGER'
	assert column_types['phase_id'] == 'INTEGER'
	assert column_types['start_time'] == 'TEXT'
	assert column_types['duration_minutes'] == 'INTEGER'
	assert column_types['notes'] == 'TEXT'
	assert column_types['invoice_id'] == 'INTEGER'



#	~~~INSERT FUNCTIONS TESTS~~~

#test if the add_architect function adds an architect to the architects table
def test_add_architect(test_conn, table_initialize):
	"""Test that the architects table has correctly added a new architect"""
	#create cursor, create architect table, and commit it to the database
	cur = test_conn.cursor()

	#query information from newly added architect to ensure insertion
	sql = "SELECT * FROM architects WHERE architect_id = ?"
	cur.execute(sql, (table_initialize['architect_id'],))
	row = cur.fetchone()

	#test if row was created - if so, it validates the add_architect function's return value
	assert row is not None

	#unpack row for readability
	arch_id, name, license, phone, email, company, status = row

	#test table columns for correct insertion 
	assert arch_id == 1
	assert name == "Name"
	assert license == "LicenseNumber01"
	assert phone == "123-456-7890"
	assert email == "email@domain.com"
	assert company == "MyCompany"
	assert status == "active"

	#test if architect object was updated with architect_id
	assert table_initialize['architect'].architect_id == 1


#test if the phases table is correctly initialized with the PHASES dictionary
def test_initialize_phases(test_conn, table_initialize):
	"""Test that the phases table is correctly populated by the PHASES dictionary"""
	cur = test_conn.cursor()

	#initialize the phases table a 2nd time to check for duplicate insertion
	initialize_phases(cur)

	#query all information from the initialized phases table
	sql = "SELECT * FROM phases"
	cur.execute(sql)
	rows = cur.fetchall()

	#test if number of items in phases table equals number of items in PHASES dictionary
	#and test that table is only initialized once
	assert len(rows) == 9

	#test all rows for correct insertion 
	assert rows[0] == (1, "Schematic Design")
	assert rows[1] == (2, "Design Development")
	assert rows[2] == (3, "Construction Documents")
	assert rows[3] == (4, "Bidding Negotiation" )
	assert rows[4] == (5, "Construction Administration")
	assert rows[5] == (6, "Interior Design")
	assert rows[6] == (7, "Add Service")
	assert rows[7] == (8, "Business Development")
	assert rows[8] == (9, "Administration")


#test if the add_project function adds a project to the projects table
def test_add_project(test_conn, table_initialize):
	"""Test that the projects table has correctly added a new project"""
	cur = test_conn.cursor()
	
	#query information from newly added project to ensure insertion
	sql = "SELECT * FROM projects WHERE project_id = ?"
	cur.execute(sql, (table_initialize['project_id'],))
	row = cur.fetchone()

	#test if row was created - if so, it validates the add_project function's return value
	assert row is not None

	#unpack row for readability 
	project_id, project_name, client_name, client_address, start_date, current_phase_id, status = row

	#test table columns for correct insertion
	assert project_id == 1
	assert project_name == "NewProject"
	assert client_name == "NewClient"
	assert client_address == "123ClientStreet"
	assert start_date == "01-01-2025"
	assert current_phase_id == 1
	assert status == "active"

	#test if project object was updated with project_id
	assert table_initialize['project'].project_id == 1


#test if the add_invoice function adds an invoice to the projects table
def test_add_invoice(test_conn, table_initialize):
	"""Test that the invoices table has correctly added a new invoice"""
	cur = test_conn.cursor()

	#query information from newly added project to ensure insertion
	sql = "SELECT * FROM invoices WHERE invoice_id = ?"
	cur.execute(sql, (table_initialize['invoice_id'],))
	row = cur.fetchone()

	#test if row was created - if so, it validates the add_invoice function's return value
	assert row is not None

	#unpack row for readability
	invoice_id, project_id, created_date, invoice_number, status = row

	#test table columns for correct insertion 
	assert invoice_id == 1
	assert project_id == table_initialize['project'].project_id
	assert created_date == "01-01-2025"
	assert invoice_number == 1
	assert status == "draft"

	#test if invoice object was updated with invoice_id
	assert table_initialize['invoice'].invoice_id == 1


#test if the add_time_entry function adds a time_entry to the time_entries table
def test_add_time_entries(test_conn, table_initialize):
	"""Test that the time_entries table has correctly added a new time_entry"""
	cur = test_conn.cursor()

	#query information from newly added time_entry to unsure insertion
	sql = "SELECT * FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (table_initialize['time_entry_id'],))
	row = cur.fetchone()

	time_entry_id, project_id, architect_id, phase_id, start_time, end_time, duration_minutes, notes, invoice_id = row

	#test if row was created - if so, it validates the add_time_entry function's return value
	assert row is not None

	#test table columns for correct insertion
	assert time_entry_id == 1
	assert project_id == table_initialize['project'].project_id
	assert architect_id == table_initialize['architect'].architect_id
	assert phase_id == table_initialize['project'].current_phase_id
	assert start_time == "01-01-2025 12:00:00"
	assert duration_minutes == 30
	assert notes == "Note"
	assert invoice_id == 1

	#test if time_entry object was updated with time_entry_id
	assert table_initialize['time_entry'].time_entry_id == 1



#	~~~LOAD OBJECT FROM DATABASE FUNCTIONS TESTS~~~

#Test if the load_architect function correctly loads an architect object from the architects table
def test_load_architect(test_conn, table_initialize):
	"""Test that an Architect object successfully loads and returns from the architects table"""
	cur = test_conn.cursor()
	testArchitect = load_architect(1, cur)

	#test if all columns were correctly loaded into Architect object
	assert testArchitect.name ==  "Name"
	assert testArchitect.license_number == "LicenseNumber01"
	assert testArchitect.phone_number == "123-456-7890"
	assert testArchitect.email =="email@domain.com"
	assert testArchitect.company_name == "MyCompany"
	assert testArchitect.status == "active"
	assert testArchitect.architect_id == 1

#Test if the load_all_active_architects function correctly loads and returns all the architect names and ids
def test_load_all_active_architects(test_conn, table_initialize):
	"""Test that all architect names and ids successfully load from the architects table and return as 
	a list of tuples"""
	cur = test_conn.cursor()
	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", "email2@domain.com",
		"Company 2")
	third_architect = Architect("Name 3", "LicenseNumber03", "987-654-3211", "email3@domain.com",
		"Company 3", status = 'inactive')
	add_architect(second_architect, cur)
	add_architect(third_architect, cur)
	test_conn.commit()
	testArchitectList = load_all_active_architects(cur)

	#test if the returned number of active architects matches the number in the table
	assert len(testArchitectList) == 2

	#test if all architects in the architect table were returned
	assert testArchitectList[0][0] == 1
	assert testArchitectList[0][1] == "Name"
	assert testArchitectList[1][0] == 2
	assert testArchitectList[1][1] == "Name 2"

#Test if the load_all_architects function correctly loads and returns all the architect names, ids, and statuses
def test_load_all_architects(test_conn, table_initialize):
	"""Test that all architect names, ids, and statuses successfully load from the projects table and 
	return as a list of tuples"""
	cur = test_conn.cursor()
	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", "email2@domain.com",
		"Company 2")
	third_architect = Architect("Name 3", "LicenseNumber03", "987-654-3211", "email3@domain.com",
		"Company 3", status = 'inactive')
	add_architect(second_architect, cur)
	add_architect(third_architect, cur)
	test_conn.commit()
	testArchitectList = load_all_architects(cur)

	#test if the returned number of total architects matches the total number in the table
	assert len(testArchitectList) == 3

	#test if all architects in the architect table were returned
	assert testArchitectList[0][0] == 1
	assert testArchitectList[0][1] == "Name"
	assert testArchitectList[0][2] == "active"
	assert testArchitectList[1][0] == 2
	assert testArchitectList[1][1] == "Name 2"
	assert testArchitectList[1][2] == "active"
	assert testArchitectList[2][0] == 3
	assert testArchitectList[2][1] == "Name 3"
	assert testArchitectList[2][2] == "inactive"


#Test if the load_projects function correctly loads a project object from the project table"""
def test_load_project(test_conn, table_initialize):
	"""Test that a Project object successfully loads and returns from the projects table"""
	cur = test_conn.cursor()
	testProject = load_project(1, cur)

	#test if all columns were correctly loaded into Project object
	assert testProject.project_name == "NewProject"
	assert testProject.client_name == "NewClient"
	assert testProject.client_address == "123ClientStreet"
	assert testProject.start_date == "01-01-2025"
	assert testProject.current_phase_id == 1
	assert testProject.status == "active"
	assert testProject.project_id == 1

#Test if the load_all_active_projects function correctly loads and returns all the project names and ids"
def test_load_all_active_projects(test_conn, table_initialize):
	"""Test that all project names and ids successfully load from the projects table and return as
	a list of tuples"""
	cur = test_conn.cursor()
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	third_project = Project("NewProject3", "NewClient3", "678ClientStreet", "03-03-2025",
		status = 'completed')
	add_project(second_project, cur)
	add_project(third_project, cur)
	test_conn.commit()
	testProjectList = load_all_active_projects(cur)

	#test if the returned number of active projects matches the number in the table
	assert len(testProjectList) == 2

	#test if all the projects in the project table were returned
	assert testProjectList[0][0] == 1
	assert testProjectList[0][1] == "NewProject"
	assert testProjectList[1][0] == 2
	assert testProjectList[1][1] == "NewProject2"

#Test if the load_all_projects function correctly loads and returns all the project names, ids, and statuses"
def test_load_all_projects(test_conn, table_initialize):
	"""Test that all project names, ids, and statuses successfully load from the projects table and
	return as a list of tuples"""
	cur = test_conn.cursor()
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	third_project = Project("NewProject3", "NewClient3", "678ClientStreet", "03-03-2025",
		status = 'completed')
	add_project(second_project, cur)
	add_project(third_project, cur)
	test_conn.commit()
	testProjectList = load_all_projects(cur)

	#test if the returned number of total projects matches the number in the table
	assert len(testProjectList) == 3

	#test if all the projects in the project table were returned
	assert testProjectList[0][0] == 1
	assert testProjectList[0][1] == "NewProject"
	assert testProjectList[0][2] == "active"
	assert testProjectList[1][0] == 2
	assert testProjectList[1][1] == "NewProject2"
	assert testProjectList[1][2] == "active"
	assert testProjectList[2][0] == 3
	assert testProjectList[2][1] == "NewProject3"
	assert testProjectList[2][2] == "completed"


#Test if the load_invoice function correctly loads an Invoice object from the invoices table
def test_load_invoice(test_conn, table_initialize):
	"""Test that an Invoice object successfully loads and returns from the invoices table"""
	cur = test_conn.cursor()

	testInvoice = load_invoice(1, cur)

	#test if all columns were correctly loaded into Invoice object
	assert testInvoice.invoice_number == 1
	assert testInvoice.created_date == "01-01-2025"
	assert testInvoice.project.project_id == 1
	assert testInvoice.status == "draft"
	assert testInvoice.invoice_id == 1

#Test if the load_project_invoices correctly loads all project invoices rows
def test_load_project_invoices(test_conn, table_initialize):
	"""Test that all invoices associated with a project_id are returned as a
	list of tuples containing invoice_id, invoice_number, created_date, status"""
	cur = test_conn.cursor()
	project = table_initialize['project']
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_project(second_project, cur)
	testInvoice2 = Invoice(2, "02-02-2025", project)
	testInvoice3 = Invoice(3, "03-03-2025", project, status = "billed")
	testInvoice4 = Invoice(4, "04-04-2025", second_project)
	add_invoice(testInvoice2, cur)
	add_invoice(testInvoice3, cur)
	add_invoice(testInvoice4, cur)
	test_conn.commit()
	testInvoices = load_project_invoices(1, cur)

	#test if the returned number of invoices matches the number in the table
	assert len(testInvoices) == 3

	#test if all the columns were correctly loaded into the tuples in the correct order
	assert testInvoices[0][0] == 3
	assert testInvoices[0][1] == 3
	assert testInvoices[0][2] == "03-03-2025"
	assert testInvoices[0][3] == "billed"
	assert testInvoices[1][0] == 1
	assert testInvoices[1][1] == 1
	assert testInvoices[1][2] == "01-01-2025"
	assert testInvoices[1][3] == "draft"
	assert testInvoices[2][0] == 2
	assert testInvoices[2][1] == 2
	assert testInvoices[2][2] == "02-02-2025"
	assert testInvoices[2][3] == "draft"

def test_load_status_invoices(test_conn, table_initialize):
	"""Test that all invoices associated with a status are returned as a list of tuples 
	containing invoice_id, invoice_number, created_date, project_name"""
	cur = test_conn.cursor()
	project = table_initialize['project']
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_project(second_project, cur)
	testInvoice2 = Invoice(2, "02-02-2025", project)
	testInvoice3 = Invoice(3, "03-03-2025", project, status = "billed")
	testInvoice4 = Invoice(4, "04-04-2025", second_project, status = "billed")
	add_invoice(testInvoice2, cur)
	add_invoice(testInvoice3, cur)
	add_invoice(testInvoice4, cur)
	test_conn.commit()
	testDraftInvoices = load_status_invoices("draft", cur)
	testBilledInvoices = load_status_invoices("billed", cur)

	#test if the returned number of invoices matches the number in the invoices table
	assert len(testDraftInvoices) == 2
	assert len(testBilledInvoices) == 2

	#test if all columns were correctly loaded into the tuples in the correct order
	assert testDraftInvoices[0][0] == 1
	assert testDraftInvoices[0][1] == 1
	assert testDraftInvoices[0][2] == "01-01-2025"
	assert testDraftInvoices[0][3] == "NewProject"
	assert testBilledInvoices[0][0] == 3
	assert testBilledInvoices[0][1] == 3
	assert testBilledInvoices[0][2] == "03-03-2025"
	assert testBilledInvoices[0][3] == "NewProject"
	assert testBilledInvoices[1][0] == 4
	assert testBilledInvoices[1][1] == 4
	assert testBilledInvoices[1][2] == "04-04-2025"
	assert testBilledInvoices[1][3] == "NewProject2"

def test_load_status_invoices_invalid_column(test_conn, table_initialize):
	"""Test to see if inputting an invalid invoice status throws an exception"""
	cur = test_conn.cursor()

	with pytest.raises(ValueError, match='Invalid status'):
		load_status_invoices("invalid", cur)

def test_load_all_invoices(test_conn, table_initialize):
	"""Test that all invoices were loaded into a list of tuples containing invoice_id, 
	project name, created date, invoice number, status and ordered by project name, 
	invoice status, then creation date"""
	cur = test_conn.cursor()
	project = table_initialize['project']
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_project(second_project, cur)
	testInvoice2 = Invoice(2, "02-02-2025", project, status = "paid")
	testInvoice3 = Invoice(3, "03-03-2025", second_project, status = "billed")
	testInvoice4 = Invoice(4, "04-04-2025", second_project, status = "paid")
	add_invoice(testInvoice2, cur)
	add_invoice(testInvoice3, cur)
	add_invoice(testInvoice4, cur)
	test_conn.commit()
	testInvoices = load_all_invoices(cur)

	#test if the returned number of invoices match the number in the invoices table
	assert len(testInvoices) == 4

	#test if all columns were correctly loaded into the tuples in the correct order
	assert testInvoices[0][0] == 1
	assert testInvoices[0][1] == "NewProject"
	assert testInvoices[0][2] == "01-01-2025"
	assert testInvoices[0][3] == 1
	assert testInvoices[0][4] == "draft"
	assert testInvoices[3][0] == 4
	assert testInvoices[3][1] == "NewProject2"
	assert testInvoices[3][2] == "04-04-2025"
	assert testInvoices[3][3] == 4
	assert testInvoices[3][4] == "paid"


#Test if the load_time_entry function correctly loads a TimeEntry object from the time_entry table
def test_load_time_entry(test_conn, table_initialize):
	"""Test that a TimeEntry object successfully loads and returns from the time_entry table"""
	cur = test_conn.cursor()
	testTimeEntry = load_time_entry(1, cur)

	#test if all columns were correctly loaded into TimeEntry object
	assert testTimeEntry.start_time == "01-01-2025 12:00:00"
	assert testTimeEntry.duration_minutes == 30
	assert testTimeEntry.project_id == table_initialize['project'].project_id
	assert testTimeEntry.architect_id == table_initialize['architect'].architect_id
	assert testTimeEntry.phase_id == 1
	assert testTimeEntry.notes == "Note"
	assert testTimeEntry.invoice_id == 1
	assert testTimeEntry.time_entry_id == 1

#Test if the load_all_project_time_entries function correctly loads all project time_enties rows
def test_load_all_project_time_entries(test_conn, table_initialize):
	"""Test that all time_entry rows for a project are returned as a list of tuples
	containing time_entry_id, start_time, duration_minutes, architect.name"""
	cur = test_conn.cursor()
	project = table_initialize['project']
	architect = table_initialize['architect']
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_project(second_project, cur)
	test_conn.commit()
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, project.project_id, 
		architect.architect_id)
	testTimeEntry3 = TimeEntry("02-02-2025 12:00:00", 60, second_project.project_id, 
		architect.architect_id)
	add_time_entry(testTimeEntry2, cur)
	add_time_entry(testTimeEntry3, cur)
	test_conn.commit()

	testTimeEntries = load_all_project_time_entries(project.project_id, cur)

	#test if the returned number of tuples matches the number of TimeEntry rows in time_entries
	#table that corresponds to the same project
	assert len(testTimeEntries) == 2

	#test if all the columns were correctly loaded into the tuples
	assert testTimeEntries[0][0] == 1
	assert testTimeEntries[0][1] == "01-01-2025 12:00:00"
	assert testTimeEntries[0][2] == 30
	assert testTimeEntries[0][3] == "Name"
	assert testTimeEntries[1][0] == 2
	assert testTimeEntries[1][1] == "01-01-2025 1:00:00"
	assert testTimeEntries[1][2] == 45
	assert testTimeEntries[1][3] == "Name"

#Test if the load_all_architect_time_entries function correctly loads all architect time_entries rows
def test_load_all_architect_time_entries(test_conn, table_initialize):
	"""Test that all time_entry rows for an architect are returned as a list of tuples
	containing time_entry_id, start_time, duration_minutes, project_name"""
	cur = test_conn.cursor()
	project = table_initialize['project']
	architect = table_initialize['architect']
	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", "email2@domain.com",
		"Company 2")
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_architect(second_architect, cur)
	add_project(second_project, cur)
	test_conn.commit()
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, second_project.project_id, 
		architect.architect_id)
	testTimeEntry3 = TimeEntry("02-02-2025 12:00:00", 60, project.project_id, 
		second_architect.architect_id)
	add_time_entry(testTimeEntry2, cur)
	add_time_entry(testTimeEntry3, cur)
	test_conn.commit()

	testTimeEntries = load_all_architect_time_entries(architect.architect_id, cur)
	#test if the returned number of tuples matches the number of TimeEntry objects
	#in the database that correspond to the same architect
	assert len(testTimeEntries) == 2

	#test if all the columns were correctly loaded into the tuples
	assert testTimeEntries[0][0] == 1
	assert testTimeEntries[0][1] == "01-01-2025 12:00:00"
	assert testTimeEntries[0][2] == 30
	assert testTimeEntries[0][3] == "NewProject"
	assert testTimeEntries[1][0] == 2
	assert testTimeEntries[1][1] == "01-01-2025 1:00:00"
	assert testTimeEntries[1][2] == 45
	assert testTimeEntries[1][3] == "NewProject2"

#Test if the load_invoice_time_entries function correctly loads all invoice time_entries rows
def test_load_invoice_time_entries(test_conn, table_initialize):
	"""Test that all time_entries rows for an invoice are returned as a list of tuples
	containing time_entry_id, start_time, duration_minutes, project_id, notes. 
	Test if passing in None returns all non-invoice affiliated time_entries rows"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']
	project = table_initialize['project']
	testInvoice2 = Invoice(2, "02-02-2025", project)
	add_invoice(testInvoice2, cur)
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, project.project_id, 
		architect.architect_id, invoice_id=1)
	testTimeEntry3 = TimeEntry("02-02-2025 12:00:00", 60, project.project_id, 
		architect.architect_id, invoice_id=2)
	testTimeEntry4 = TimeEntry("03-03-2025 3:00:00", 120, project.project_id, 
		architect.architect_id, invoice_id=None)
	add_time_entry(testTimeEntry2, cur)
	add_time_entry(testTimeEntry3, cur)
	add_time_entry(testTimeEntry4, cur)
	test_conn.commit()

	testTimeEntries = load_invoice_time_entries(1, cur)
	testTimeEntries2 = load_invoice_time_entries(None, cur)
	#test if the returned number of tuples matches the number of TimeEntry objects with the same invoice_id
	assert len(testTimeEntries) == 2
	assert len(testTimeEntries2) == 1

	#test if all the columns were correctly loaded into the tuples in the correct order
	assert testTimeEntries[0][0] == 1
	assert testTimeEntries[0][1] == "01-01-2025 12:00:00"
	assert testTimeEntries[0][2] == 30
	assert testTimeEntries[0][3] == 1
	assert testTimeEntries[0][4] == "Note"
	assert testTimeEntries[1][0] == 2
	assert testTimeEntries[1][1] == "01-01-2025 1:00:00"
	assert testTimeEntries[1][2] == 45
	assert testTimeEntries[1][3] == 1
	assert testTimeEntries[1][4] == None

#Test if the load_all_time_entries function correctly loads all time entries from the table
def test_load_all_time_entries(test_conn, table_initialize):
	"""Test that all time_entry rows in the table are returned as a list of tuples
	containing time_entry_id, start_time, duration_minutes, project_name, architect_name"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']
	project = table_initialize['project']
	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", 
		"email2@domain.com","Company 2")
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", 
		"02-02-2025")
	add_architect(second_architect, cur)
	add_project(second_project, cur)
	test_conn.commit()
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, second_project.project_id,
		architect.architect_id)
	testTimeEntry3 = TimeEntry("02-02-2025 12:00:00", 60, project.project_id, 
		second_architect.architect_id)
	testTimeEntry4 = TimeEntry("03-03-2025 3:00:00", 120, None, 
		second_architect.architect_id)
	add_time_entry(testTimeEntry2, cur)
	add_time_entry(testTimeEntry3, cur)
	add_time_entry(testTimeEntry4, cur)
	test_conn.commit()

	testTimeEntries = load_all_time_entries(cur)
	#test if the returned number of tuples matches the number of TimeEntry objects in the table
	assert len(testTimeEntries) == 4

	#test if all the columns were correctly loaded into the tuples
	assert testTimeEntries[0][0] == 1
	assert testTimeEntries[0][1] == "01-01-2025 12:00:00"
	assert testTimeEntries[0][2] == 30
	assert testTimeEntries[0][3] == "NewProject"
	assert testTimeEntries[0][4] == "Name"
	assert testTimeEntries[1][0] == 3
	assert testTimeEntries[1][1] == "02-02-2025 12:00:00"
	assert testTimeEntries[1][2] == 60
	assert testTimeEntries[1][3] == "NewProject"
	assert testTimeEntries[1][4] == "Name 2"
	assert testTimeEntries[2][0] == 2
	assert testTimeEntries[2][1] == "01-01-2025 1:00:00"
	assert testTimeEntries[2][2] == 45
	assert testTimeEntries[2][3] == "NewProject2"
	assert testTimeEntries[2][4] == "Name"
	assert testTimeEntries[3][0] == 4
	assert testTimeEntries[3][1] == "03-03-2025 3:00:00"
	assert testTimeEntries[3][2] == 120
	assert testTimeEntries[3][3] == None
	assert testTimeEntries[3][4] == "Name 2"

#Test if the load_nonproject_phases_time_entries correctly loads time_entries from phases 8 & 9 only
def test_load_nonproject_phases_time_entries(test_conn, table_initialize):
	"""Test that all time_entry rows for phases 8 and 9 are loaded and returned 
	as a list of tuples containing time_entry_id, start time, duration_mionutes,
	architect_name, phase_id"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, None, architect.architect_id,
		phase_id = 8)
	testTimeEntry3 = TimeEntry("02-02-2025 12:00:00", 60, None, architect.architect_id, 
		phase_id = 8)
	testTimeEntry4 = TimeEntry("03-03-2025 3:00:00", 120, None, architect.architect_id, 
		phase_id = 9)
	add_time_entry(testTimeEntry2, cur)
	add_time_entry(testTimeEntry3, cur)
	add_time_entry(testTimeEntry4, cur)
	test_conn.commit()

	testTimeEntries = load_nonproject_phases_time_entries(cur)
	#test if the returned number of tuples matches the number of TimeEntry objects 
	#with phases 8 and 9 in the table, ordered by phase_id
	assert len(testTimeEntries) == 3

	#test if all the columns were correctly loaded into the tuples
	assert testTimeEntries[0][0] == 2
	assert testTimeEntries[0][1] == "01-01-2025 1:00:00"
	assert testTimeEntries[0][2] == 45
	assert testTimeEntries[0][3] == "Name"
	assert testTimeEntries[0][4] == 8
	assert testTimeEntries[2][0] == 4
	assert testTimeEntries[2][1] == "03-03-2025 3:00:00"
	assert testTimeEntries[2][2] == 120
	assert testTimeEntries[2][3] == "Name"
	assert testTimeEntries[2][4] == 9



#	~~~UPDATE FUNCTIONS TESTS~~~

#test if the update_architect function updates the architect table
def test_update_architect(test_conn, table_initialize):
	"""Test that the architects table has been correctly updated with the new input values"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']
	
	#update all columns in the architects table with new values
	architect = update_architect('name', architect, 'New_Name', cur)
	architect = update_architect('license_number', architect, 'LicenseNumber02', cur)
	architect = update_architect('phone_number', architect, '987-654-3210', cur)
	architect = update_architect('email', architect, 'new_email@domain.com', cur)
	architect = update_architect('company_name', architect, 'MyNewCompany', cur)
	architect = update_architect('status', architect, 'inactive', cur)
	test_conn.commit()

	#test if all column values were correctly updated
	sql = "SELECT * FROM architects WHERE architect_id = ?"
	cur.execute(sql, (architect.architect_id,))
	row = cur.fetchone()

	#unpack row for readability
	arch_id, name, license_number, phone_number, email, company_name, status = row

	assert name == "New_Name"
	assert license_number == "LicenseNumber02"
	assert phone_number == "987-654-3210"
	assert email == "new_email@domain.com"
	assert company_name == "MyNewCompany"
	assert status == "inactive"

	#test if all object attributes were correctly updated
	assert architect.name == "New_Name"
	assert architect.license_number == "LicenseNumber02"
	assert architect.phone_number == "987-654-3210"
	assert architect.email == "new_email@domain.com"
	assert architect.company_name == "MyNewCompany"
	assert architect.status == "inactive"

#Test if the update_architect function raises an exception to an incorrect column name
def test_update_architect_invalid_column(test_conn, table_initialize):
	"""Test to see if trying to change an invalid column in the architects table throws an exception"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']

	with pytest.raises(ValueError, match="Invalid column"):
		update_architect('invalid_column', architect, 'value', cur)


#Test if the update_project function updates the project table
def test_update_project(test_conn, table_initialize):
	"""Test that the projects table has been correctly updated with the new input values"""
	cur = test_conn.cursor()
	project = table_initialize['project']

	#update all columns in the projects table with new values
	project = update_project('project_name', project, "NewProject2", cur)
	project = update_project('client_name', project, "NewClient2", cur)
	project = update_project('client_address', project, "345ClientStreet", cur)
	project = update_project('start_date', project, "02-02-2025", cur)
	project = update_project('current_phase_id', project, 2, cur)
	project = update_project('status', project, 'completed', cur)
	test_conn.commit()

	#test if all column values were correctly updated
	sql = "SELECT * FROM projects WHERE project_id = ?"
	cur.execute(sql, (project.project_id,))
	row = cur.fetchone()

	#unpack row for readability 
	project_id, project_name, client_name, client_address, start_date, current_phase_id, status = row

	assert project_name == "NewProject2"
	assert client_name == "NewClient2"
	assert client_address == "345ClientStreet"
	assert start_date == "02-02-2025"
	assert current_phase_id == 2
	assert status == 'completed'

	#test if all object attributes where correctly updated
	assert project.project_name == "NewProject2"
	assert project.client_name == "NewClient2"
	assert project.client_address == "345ClientStreet"
	assert project.start_date == "02-02-2025"
	assert project.current_phase_id == 2
	assert project.status == 'completed'

#Test if the update_project function raises an exception to an incorrect column name
def test_update_project_invalid_column(test_conn, table_initialize):
	"""Test to see if trying to change an invalid column in the projects table throws an exception"""
	cur = test_conn.cursor()
	project = table_initialize['project']

	with pytest.raises(ValueError, match='Invalid column'):
		update_project('invalid_column', project, 'value', cur)


#Test if the update_invoice function updates the invoices table
def test_update_invoice(test_conn, table_initialize):
	"""Test that the invoices table has been correctly updated with the new input values"""
	cur = test_conn.cursor()
	invoice = table_initialize['invoice']
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_project(second_project, cur)
	test_conn.commit()

	#update all columns in the invoices table with new values
	invoice = update_invoice('project_id', invoice, 2, cur)
	invoice = update_invoice('created_date', invoice, "02-02-2025", cur)
	invoice = update_invoice('invoice_number', invoice, 2, cur)
	invoice = update_invoice('status', invoice, "billed", cur)
	test_conn.commit()

	#test if all column values were correctly updated
	sql = "SELECT * FROM invoices WHERE invoice_id = ?"
	cur.execute(sql, (invoice.invoice_id,))
	row = cur.fetchone()

	#unpack row for readability
	invoice_id, project_id, created_date, invoice_number, status = row

	assert project_id == 2
	assert created_date == "02-02-2025"
	assert invoice_number == 2
	assert status == "billed"

	#test if all object attributes were correctly updated
	assert invoice.project.project_id == 2
	assert invoice.created_date == "02-02-2025"
	assert invoice.invoice_number == 2
	assert invoice.status == "billed"

#Test if the update_invoice function raises an exception to an incorrect column name
def test_update_invoice_invalid_column(test_conn, table_initialize):
	"""Test to see if trying to change an invalid column in the invoices table throws an exception"""
	cur = test_conn.cursor()
	invoice = table_initialize['invoice']

	with pytest.raises(ValueError, match='Invalid column'):
		update_invoice('invalid_column', invoice, 'value', cur)


#Test if the update_time_entry function updates the time_entries table
def test_update_time_entry(test_conn, table_initialize):
	"""Test that the time_entries table has been correctly updated with the new input values"""
	cur = test_conn.cursor()
	time_entry = table_initialize['time_entry']
	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", "email2@domain.com",
		"Company 2")
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", "02-02-2025")
	add_architect(second_architect, cur)
	add_project(second_project, cur)
	test_conn.commit()

	#update all columns in the time_entries table with new values
	time_entry = update_time_entry('project_id', time_entry, 2, cur)
	time_entry = update_time_entry('architect_id', time_entry, 2, cur)
	time_entry = update_time_entry('phase_id', time_entry, 2, cur)
	time_entry = update_time_entry('start_time', time_entry, '02-02-2025 1:00:00', cur)
	time_entry = update_time_entry('duration_minutes', time_entry, 60, cur)
	time_entry = update_time_entry('notes', time_entry, 'New Note', cur)
	time_entry = update_time_entry('invoice_id', time_entry, 1, cur)
	test_conn.commit()

	#test if all column values were correctly updated
	sql = "SELECT * FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (time_entry.time_entry_id,))
	row = cur.fetchone()

	#unpack row for readability
	time_entry_id, project_id, architect_id, phase_id, start_time, end_time, \
		duration_minutes, notes, invoice_id = row

	assert project_id == 2
	assert architect_id == 2
	assert phase_id == 2
	assert start_time == "02-02-2025 1:00:00"
	assert duration_minutes == 60
	assert notes == "New Note"
	assert invoice_id == 1

	#test if all object attributes where correctly updated
	assert time_entry.start_time == "02-02-2025 1:00:00"
	assert time_entry.duration_minutes == 60
	assert time_entry.project.project_id == 2
	assert time_entry.architect.architect_id == 2
	assert time_entry.phase_id == 2
	assert time_entry.notes == "New Note"
	assert time_entry.invoice_id == 1

#Test if the update_time_entry function raises an exception to an incorrect column name
def test_update_time_entry_invalid_column(test_conn, table_initialize):
	"""Test to see if trying to change an invalid column in the time_entry table throws an exception"""
	cur = test_conn.cursor()
	time_entry = table_initialize['time_entry']

	with pytest.raises(ValueError, match='Invalid column'):
		update_time_entry('invalid_column', time_entry, 'value', cur)



#	~~~DELETE FUNCTIONS TESTS~~~

#Test if the delete_invoice function deletes the correct row from the invoices table
def test_delete_invoice(test_conn, table_initialize):
	"""Test to see if the delete_invoice function deletes the correct row"""
	cur = test_conn.cursor()
	project = table_initialize['project']
	testInvoice2 = Invoice(2, "02-02-2025", project, status = "paid")
	add_invoice(testInvoice2, cur)
	test_conn.commit()
	pre_delete_invoices = load_all_invoices(cur)

	#test to see if there are 2 invoices to start
	assert len(pre_delete_invoices) == 2

	#test delete_invoice function
	delete_invoice(1, cur)
	test_conn.commit()
	post_delete_invoices = load_all_invoices(cur)
	assert len(post_delete_invoices) == 1

	#test the correct invoice was deleted
	assert post_delete_invoices[0][0] == 2
	assert post_delete_invoices[0][1] == "NewProject"
	assert post_delete_invoices[0][2] == "02-02-2025"
	assert post_delete_invoices[0][3] == 2
	assert post_delete_invoices[0][4] == "paid"


#Test if the delete_time_entry function deletes the correct row from the time_entry table
def test_delete_time_entry(test_conn, table_initialize):
	"""Test to see if the delete_time_entry function deletes the correct row"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']
	project = table_initialize['project']
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, project.project_id, 
		architect.architect_id, phase_id = 8)
	add_time_entry(testTimeEntry2, cur)
	test_conn.commit()
	pre_delete_time_entries = load_all_time_entries(cur)

	#test to see if there are 2 time_entries to start
	assert len(pre_delete_time_entries) == 2

	#test delete_time_entries function
	delete_time_entry(1, cur)
	test_conn.commit()
	post_delete_time_entries = load_all_time_entries(cur)
	assert len(post_delete_time_entries) == 1

	#test the correct time_entry was deleted
	assert post_delete_time_entries[0][0] == 2
	assert post_delete_time_entries[0][1] == "01-01-2025 1:00:00"
	assert post_delete_time_entries[0][2] == 45
	assert post_delete_time_entries[0][3] == "NewProject"
	assert post_delete_time_entries[0][4] == "Name"