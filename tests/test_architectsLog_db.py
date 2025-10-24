#testing for acrchitectsLog_db.py

import pytest
import os
import sqlite3

from architectsLog_db import get_connection, create_architect_table, create_project_table
from architectsLog_db import create_phases_table, create_invoices_table, create_time_entries_table
from architectsLog_db import add_architect, initialize_phases, add_project, add_invoice, add_time_entry

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
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025", testArchitect)
	project_id = add_project(testProject, cur)

	#create a test invoice with testProject and add it to the invoice table
	testInvoice = Invoice(1, "01-01-2025", testProject)
	invoice_id = add_invoice(testInvoice, cur)

	#create a test time entry with testProject and testArchitect and add it to the time_entries table
	testTimeEntry = TimeEntry("01-01-2025 12:00:00", "01-01-2025 12:30:00", 30, testProject, testArchitect)
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
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='architects'")
	result = cursor.fetchone()

	assert result is not None, "architects table should exist"
	assert result[0] == 'architects'


#test if projects table was created
def test_project_table_creation(test_conn):
	"""Test that the projects table is created"""
	cursor = test_conn.cursor()
	create_project_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='projects'")
	result = cursor.fetchone()

	assert result is not None, "projects table should exist"
	assert result[0] == 'projects'


#test if phases table was created
def test_phase_table_creation(test_conn):
	"""Test that the phases table is created"""
	cursor = test_conn.cursor()
	create_phases_table(cursor)

	#query sqlite_master to check if the table exits
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='phases'")
	result = cursor.fetchone()

	assert result is not None, "phases table should exist"
	assert result[0] == 'phases'


#test if invoices table was created
def test_create_invoices_table(test_conn):
	"""Test that the invoices table is created"""
	cursor = test_conn.cursor()
	create_invoices_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='invoices'")
	result = cursor.fetchone()

	assert result is not None, "invoices table should exist"
	assert result[0] == 'invoices'


#test if time_entries table was created
def test_create_time_entries_table(test_conn):
	"""Test that the time_entries table is created"""
	cursor = test_conn.cursor()
	create_time_entries_table(cursor)

	#query sqlite_master to check if time_entries table is created
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='time_entries'")
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
	assert 'is_active' in column_names

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
	assert column_types['is_active'] == 'INTEGER'


#test if projects table has correct column names
def test_project_table_column_names(table_info):
	"""Test that the projects table has correct column names"""
	column_names = [col[1] for col in table_info('projects', create_project_table)]

	assert 'project_id' in column_names
	assert 'project_name' in column_names
	assert 'client_name' in column_names
	assert 'client_address' in column_names
	assert 'architect_id' in column_names
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
	assert column_types['architect_id'] == 'INTEGER'
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
	assert 'end_time' in column_names
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
	assert column_types['end_time'] == 'TEXT'
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
	arch_id, name, license, phone, email, company, is_active = row

	#test table columns for correct insertion 
	assert arch_id == 1
	assert name == "Name"
	assert license == "LicenseNumber01"
	assert phone == "123-456-7890"
	assert email == "email@domain.com"
	assert company == "MyCompany"
	assert is_active == 1

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
	assert len(rows) == 8

	#test all rows for correct insertion 
	assert rows[0] == (1, "Schematic Design")
	assert rows[1] == (2, "Design Development")
	assert rows[2] == (3, "Construction Documents")
	assert rows[3] == (4, "Bidding Negotiation" )
	assert rows[4] == (5, "Construction Administration")
	assert rows[5] == (6, "Interior Design")
	assert rows[6] == (7, "Business Development")
	assert rows[7] == (8, "Administration")


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
	project_id, project_name, client_name, client_address, architect_id, start_date, current_phase_id, status = row

	#test table columns for correct insertion
	assert project_id == 1
	assert project_name == "NewProject"
	assert client_name == "NewClient"
	assert client_address == "123ClientStreet"
	assert architect_id == table_initialize['project'].architect.architect_id
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
	assert end_time == "01-01-2025 12:30:00"
	assert duration_minutes == 30
	assert notes == None
	assert invoice_id == None

	#test if time_entry object was updated with time_entry_id
	assert table_initialize['time_entry'].time_entry_id == 1