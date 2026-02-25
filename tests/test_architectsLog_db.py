#testing for acrchitectsLog_db.py

import pytest
import os
import sqlite3

from datetime import datetime

from architectsLog_db import (get_connection, create_architect_table, 
	create_project_table, create_phases_table, create_invoices_table, 
	create_time_entries_table, initialize_phases, initialize_projects, 
	initialize_invoices, add_architect, add_project, add_invoice, add_time_entry,
 	load_architect, load_project, get_most_recent_archid_and_projid, 
 	get_most_recent_project_phase, load_invoice_ids_no_time_entries, update_project,
 	update_time_entry, delete_invoice, delete_time_entry)


from architectsLog_classes import Architect, Project, Invoice, TimeEntry


#	~~~PYTEST.FIXTURES AND DATABASE CONNECTIONS~~~

#create all tables and populate or initialize them 
@pytest.fixture
def table_initialize(test_conn):
	#create cursor, create architects table, create projects table, create invoices 
	#table and commit them to the database
	cur = test_conn.cursor()
	create_architect_table(cur)
	create_phases_table(cur)
	create_project_table(cur)
	create_invoices_table(cur)
	create_time_entries_table(cur)
	test_conn.commit()

	#add an architect to Architect table to get architect_id assigned
	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890",
		"email@domain.com", "MyCompany")
	architect_id = add_architect(testArchitect, cur)

	#initialize the phases table
	initialize_phases(cur)

	#create a test project with testArchitect and add it to the project table
	date = "01-01-2025"
	project_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(project_date.timestamp())
	testProject = Project("NewProject", "NewClient", "123ClientStreet", int_date)
	project_id = add_project(testProject, cur)

	#create a test invoice with testProject and add it to the invoice table
	date = "01-01-2025"
	invoice_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(invoice_date.timestamp())
	testInvoice = Invoice(1, int_date, project_id)
	invoice_id = add_invoice(testInvoice, cur)

	#create a test time entry with testProject and testArchitect and add it to the 
	#time_entries table
	date_time = "01-01-2025 12:00:00"
	time_entry_date_time = datetime.strptime(date_time, "%m-%d-%Y %I:%M:%S")
	int_date_time = int(time_entry_date_time.timestamp())
	testTimeEntry = TimeEntry(int_date_time, 30, testProject.project_id, 
		testArchitect.architect_id, notes= "Note", invoice_id= 1)
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


def test_get_connection_creates_connection(test_conn):
    """Test that get_connection returns a valid connection"""
    assert test_conn is not None
    assert isinstance(test_conn, sqlite3.Connection)

def test_foreign_keys_enabled(test_conn):
    """Test that foreign keys are enabled on connection"""
    cursor = test_conn.cursor()
    cursor.execute("PRAGMA foreign_keys")
    result = cursor.fetchone()[0]
    assert result == 1, "Foreign keys should be enabled"



#	~~~TABLE CREATION TESTS~~~

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

#create a generic fixture to can get table information for all table tests
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

def test_architect_table_column_names(table_info):
	"""Test that the architects table has correct column names"""
	column_names = [col[1] for col in table_info('architects', 
		create_architect_table)]

	assert 'architect_id' in column_names
	assert 'name' in column_names
	assert 'license_number' in column_names
	assert 'phone_number' in column_names
	assert 'email' in column_names
	assert 'company_name' in column_names
	assert 'status' in column_names

def test_architect_table_column_types(table_info):
	"""Test that the architects table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('architects', 
		create_architect_table)}

	assert column_types['architect_id'] == 'INTEGER'
	assert column_types['name'] == 'TEXT'
	assert column_types['license_number'] == 'TEXT'
	assert column_types['phone_number'] == 'TEXT'
	assert column_types['email'] == 'TEXT'
	assert column_types['company_name'] == 'TEXT'
	assert column_types['status'] == 'TEXT'


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

def test_project_table_column_types(table_info):
	"""Test that the projects table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('projects', 
		create_project_table)}

	assert column_types['project_id'] == 'INTEGER'
	assert column_types['project_name'] == 'TEXT'
	assert column_types['client_name'] == 'TEXT'
	assert column_types['client_address'] == 'TEXT'
	assert column_types['start_date'] == 'INTEGER'
	assert column_types['current_phase_id'] == 'INTEGER'
	assert column_types['status'] == 'TEXT'


def test_phases_table_column_names(table_info):
	"""Test that the phases table has correct column names"""
	column_names = [col[1] for col in table_info('phases', create_phases_table)]

	assert 'phase_id' in column_names
	assert 'project_phase' in column_names

def test_phase_table_column_types(table_info):
	"""Test that the phases table has the correct column types"""
	column_types = {col[1] : col[2] for col in table_info('phases', 
		create_phases_table)}

	assert column_types['phase_id'] == 'INTEGER'
	assert column_types['project_phase'] == 'TEXT'


def test_create_invoices_table_column_names(table_info):
	"""Test that the invoices table has correct column names"""
	column_names = [col[1] for col in table_info('invoices', create_invoices_table)]

	assert 'invoice_id' in column_names
	assert 'project_id' in column_names
	assert 'created_date' in column_names
	assert 'invoice_number' in column_names
	assert 'status' in column_names

def test_create_invoices_table_column_types(table_info):
	"""Test that the invoices table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('invoices', 
		create_invoices_table)}

	assert column_types['invoice_id'] == 'INTEGER'
	assert column_types['project_id'] == 'INTEGER'
	assert column_types['created_date'] == 'INTEGER'
	assert column_types['invoice_number'] == 'TEXT'
	assert column_types['status'] == 'TEXT'


def test_create_time_entries_table_names(table_info):
	"""Test that the time_entries table has correct column names"""
	column_names = [col[1] for col in table_info('time_entries', 
		create_time_entries_table)]

	assert 'time_entry_id' in column_names
	assert 'project_id' in column_names
	assert 'architect_id' in column_names
	assert 'phase_id' in column_names
	assert 'start_time' in column_names
	assert 'duration_minutes' in column_names
	assert 'notes' in column_names
	assert 'invoice_id' in column_names

def test_create_time_entries_table_types(table_info):
	"""Test that the time_entries table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('time_entries', 
		create_time_entries_table)}

	assert column_types['time_entry_id'] == 'INTEGER'
	assert column_types['project_id'] == 'INTEGER'
	assert column_types['architect_id'] == 'INTEGER'
	assert column_types['phase_id'] == 'INTEGER'
	assert column_types['start_time'] == 'INTEGER'
	assert column_types['duration_minutes'] == 'INTEGER'
	assert column_types['notes'] == 'TEXT'
	assert column_types['invoice_id'] == 'INTEGER'



#	~~~INSERT FUNCTIONS TESTS~~~

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
	assert rows[7] == (8, "Administration")
	assert rows[8] == (9, "Business Development")


def test_initialize_projects(test_conn, table_initialize):
	"""Test that the projects table is correctly populated with 2 internal projects"""
	cur = test_conn.cursor()

	initialize_projects(cur)

	sql = "SELECT * FROM projects"
	cur.execute(sql)
	rows = cur.fetchall()

	assert len(rows) == 3

	assert rows[0][0] == -2
	assert rows[0][1] == "Business Development"
	assert rows[0][2] == "Internal"
	assert rows[0][3] == "N/A2"
	assert rows[1][0] == -1
	assert rows[1][1] == "Administration"
	assert rows[1][2] == "Internal"
	assert rows[1][3] == "N/A"

def test_initialize_invoices(test_conn, table_initialize):
	"""Test that the invoices table is correctly populated with Not Invoiced invoice"""
	cur = test_conn.cursor()

	initialize_projects(cur)
	initialize_invoices(cur)

	sql = "SELECT * FROM invoices"
	cur.execute(sql)
	rows = cur.fetchall()

	assert len(rows) == 2

	assert rows[0][0] == 0
	assert rows[0][1] == -1
	assert rows[0][2] == 0
	assert rows[0][3] == "Not Invoiced"

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
	assert status == "Active"

	#test if architect object was updated with architect_id
	assert table_initialize['architect'].architect_id == 1


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
	(project_id, project_name, client_name, client_address, start_date, 
		current_phase_id, status) = row

	date = "01-01-2025"
	invoice_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(invoice_date.timestamp())

	#test table columns for correct insertion
	assert project_id == 1
	assert project_name == "NewProject"
	assert client_name == "NewClient"
	assert client_address == "123ClientStreet"
	assert start_date == int_date
	assert current_phase_id == 1
	assert status == "Active"

	#test if project object was updated with project_id
	assert table_initialize['project'].project_id == 1


def test_add_invoice(test_conn, table_initialize):
	"""Test that the invoices table has correctly added a new invoice"""
	cur = test_conn.cursor()

	#query information from newly added project to ensure insertion
	sql = "SELECT * FROM invoices WHERE invoice_id = ?"
	cur.execute(sql, (table_initialize['invoice_id'],))
	row = cur.fetchone()

	#test if row was created - validate the add_invoice function's return value
	assert row is not None

	#unpack row for readability
	invoice_id, project_id, created_date, invoice_number, status = row

	#turn date into a timestamp int
	date = "01-01-2025"
	invoice_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(invoice_date.timestamp())
	#test table columns for correct insertion 
	assert invoice_id == 1
	assert project_id == table_initialize['project'].project_id
	assert created_date == int_date
	assert invoice_number == '1'
	assert status == "Draft"

	#test if invoice object was updated with invoice_id
	assert table_initialize['invoice'].invoice_id == 1


def test_add_time_entries(test_conn, table_initialize):
	"""Test that the time_entries table has correctly added a new time_entry"""
	cur = test_conn.cursor()

	#query information from newly added time_entry to unsure insertion
	sql = "SELECT * FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (table_initialize['time_entry_id'],))
	row = cur.fetchone()

	(time_entry_id, project_id, architect_id, phase_id, start_time, duration_minutes,
		notes, invoice_id) = row

	date_time = "01-01-2025 12:00:00"
	time_entry_date_time = datetime.strptime(date_time, "%m-%d-%Y %I:%M:%S")
	int_date_time = int(time_entry_date_time.timestamp())
	#test if row was created - validate the add_time_entry function's return value
	assert row is not None

	#test table columns for correct insertion
	assert time_entry_id == 1
	assert project_id == table_initialize['project'].project_id
	assert architect_id == table_initialize['architect'].architect_id
	assert phase_id == table_initialize['project'].current_phase_id
	assert start_time == int_date_time
	assert duration_minutes == 30
	assert notes == "Note"
	assert invoice_id == 1

	#test if time_entry object was updated with time_entry_id
	assert table_initialize['time_entry'].time_entry_id == 1



#	~~~LOAD OBJECT FROM DATABASE FUNCTIONS TESTS~~~

def test_load_architect(test_conn, table_initialize):
	"""Test that an Architect object successfully loads and returns 
	from the architects table"""
	cur = test_conn.cursor()
	testArchitect = load_architect(1, cur)

	#test if all columns were correctly loaded into Architect object
	assert testArchitect.name ==  "Name"
	assert testArchitect.license_number == "LicenseNumber01"
	assert testArchitect.phone_number == "123-456-7890"
	assert testArchitect.email =="email@domain.com"
	assert testArchitect.company_name == "MyCompany"
	assert testArchitect.status == "Active"
	assert testArchitect.architect_id == 1

def test_load_project(test_conn, table_initialize):
	"""Test that a Project object successfully loads and returns from the 
	projects table"""
	cur = test_conn.cursor()
	testProject = load_project(1, cur)

	date = "01-01-2025"
	project_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(project_date.timestamp())

	#test if all columns were correctly loaded into Project object
	assert testProject.project_name == "NewProject"
	assert testProject.client_name == "NewClient"
	assert testProject.client_address == "123ClientStreet"
	assert testProject.start_date == int_date
	assert testProject.current_phase_id == 1
	assert testProject.status == "Active"
	assert testProject.project_id == 1


def test_get_most_recent_archid_and_projid(test_conn, table_initialize):
	"""Test to get the architect_id and project_id from the last 
	entered time_entry log"""
	cur = test_conn.cursor()

	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", 
		"email2@domain.com", "Company 2")
	add_architect(second_architect, cur)
	date = "02-02-2025"
	project_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(project_date.timestamp())
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", int_date)
	add_project(second_project, cur)
	date2 = "03-03-2025"
	time_entry_date2 = datetime.strptime(date2, "%m-%d-%Y")
	int_date2 = int(time_entry_date2.timestamp())
	testTimeEntry2 = TimeEntry(int_date2, 45, second_project.project_id, 
		second_architect.architect_id, 4)
	add_time_entry(testTimeEntry2, cur)
	test_conn.commit()

	arch_id_proj_id = get_most_recent_archid_and_projid(cur)

	assert arch_id_proj_id[0] == second_architect.architect_id
	assert arch_id_proj_id[1] == second_project.project_id

def test_get_most_recent_project_phase(test_conn, table_initialize):
	"""Test to get the most recent phase from a project_id in the time_entries table"""
	cur = test_conn.cursor()

	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210", 
		"email2@domain.com", "Company 2")
	add_architect(second_architect, cur)
	date = "02-02-2025"
	project_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(project_date.timestamp())
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet", int_date)
	add_project(second_project, cur)
	date2 = "03-03-2025"
	time_entry_date2 = datetime.strptime(date2, "%m-%d-%Y")
	int_date2 = int(time_entry_date2.timestamp())
	testTimeEntry2 = TimeEntry(int_date2, 45, second_project.project_id, 
		second_architect.architect_id, 4)
	add_time_entry(testTimeEntry2, cur)
	test_conn.commit()

	proj_id_phase_id = get_most_recent_project_phase(1, cur)
	proj_id_phase_id2 = get_most_recent_project_phase(2, cur)

	assert proj_id_phase_id2 == 4
	assert proj_id_phase_id == 1

def test_load_invoice_ids_no_time_entries(test_conn, table_initialize):
	"""Test to ensure invoices with no assigned time_entries are correctly returned"""
	cur = test_conn.cursor()

	project_id = table_initialize['project_id']
	date = "02-02-2025"
	invoice_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(invoice_date.timestamp())
	testInvoice2 = Invoice(1, int_date, project_id)
	invoice_id = add_invoice(testInvoice2, cur)

	no_time_entries_invoice = load_invoice_ids_no_time_entries(cur)

	assert no_time_entries_invoice[0][0] == 2



#	~~~UPDATE FUNCTIONS TESTS~~~

def test_update_project(test_conn, table_initialize):
	"""Test that the projects table has been correctly updated with the 
	new input values"""
	cur = test_conn.cursor()
	project_id = table_initialize['project_id']

	#update all columns in the projects table with new values
	project = update_project('project_name', project_id, "NewProject2", cur)
	project = update_project('client_name', project_id, "NewClient2", cur)
	project = update_project('client_address', project_id, "345ClientStreet", cur)
	project = update_project('start_date', project_id, "02-02-2025", cur)
	project = update_project('current_phase_id', project_id, 2, cur)
	project = update_project('status', project_id, 'Completed', cur)
	test_conn.commit()

	#test if all column values were correctly updated
	sql = "SELECT * FROM projects WHERE project_id = ?"
	cur.execute(sql, (project_id,))
	row = cur.fetchone()

	#unpack row for readability 
	(project_id, project_name, client_name, client_address, start_date, 
		current_phase_id, status) = row

	assert project_name == "NewProject2"
	assert client_name == "NewClient2"
	assert client_address == "345ClientStreet"
	assert start_date == "02-02-2025"
	assert current_phase_id == 2
	assert status == 'Completed'

def test_update_project_invalid_column(test_conn, table_initialize):
	"""Test to see if trying to change an invalid column in the projects table
	throws an exception"""
	cur = test_conn.cursor()
	project = table_initialize['project']

	with pytest.raises(ValueError, match='Invalid column'):
		update_project('invalid_column', project, 'value', cur)


def test_update_time_entry(test_conn, table_initialize):
	"""Test that the time_entries table has been correctly updated with the
	new input values"""
	cur = test_conn.cursor()
	time_entry_id = table_initialize['time_entry_id']
	second_architect = Architect("Name 2", "LicenseNumber02", "987-654-3210",
		"email2@domain.com", "Company 2")
	second_project = Project("NewProject2", "NewClient2", "345ClientStreet",
		"02-02-2025")
	add_architect(second_architect, cur)
	add_project(second_project, cur)
	test_conn.commit()

	#update all columns in the time_entries table with new values
	time_entry = update_time_entry('project_id', time_entry_id, 2, cur)
	time_entry = update_time_entry('architect_id', time_entry_id, 2, cur)
	time_entry = update_time_entry('phase_id', time_entry_id, 2, cur)
	time_entry = update_time_entry('start_time', time_entry_id, 
		'02-02-2025 1:00:00', cur)
	time_entry = update_time_entry('duration_minutes', time_entry_id, 60, cur)
	time_entry = update_time_entry('notes', time_entry_id, 'New Note', cur)
	time_entry = update_time_entry('invoice_id', time_entry_id, 1, cur)
	test_conn.commit()

	#test if all column values were correctly updated
	sql = "SELECT * FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (time_entry_id,))
	row = cur.fetchone()

	#unpack row for readability
	time_entry_id, project_id, architect_id, phase_id, start_time, \
		duration_minutes, notes, invoice_id = row

	assert project_id == 2
	assert architect_id == 2
	assert phase_id == 2
	assert start_time == "02-02-2025 1:00:00"
	assert duration_minutes == 60
	assert notes == "New Note"
	assert invoice_id == 1

def test_update_time_entry_invalid_column(test_conn, table_initialize):
	"""Test to see if trying to change an invalid column in the time_entry table 
	throws an exception"""
	cur = test_conn.cursor()
	time_entry = table_initialize['time_entry']

	with pytest.raises(ValueError, match='Invalid column'):
		update_time_entry('invalid_column', time_entry, 'value', cur)



#	~~~DELETE FUNCTIONS TESTS~~~

def test_delete_invoice(test_conn, table_initialize):
	"""Test to see if the delete_invoice function deletes the correct row"""
	cur = test_conn.cursor()
	project_id = table_initialize['project_id']
	testInvoice2 = Invoice(2, "02-02-2025", project_id, status = "paid")
	add_invoice(testInvoice2, cur)
	test_conn.commit()
	sql = "SELECT invoice_id, projects.project_name, created_date, invoice_number, \
		invoices.status FROM invoices INNER JOIN projects \
		ON invoices.project_id = projects.project_id \
		ORDER BY project_name ASC, invoices.status ASC, created_date ASC"
	cur.execute(sql)
	pre_delete_invoices = cur.fetchall()

	#test to see if there are 2 invoices to start
	assert len(pre_delete_invoices) == 2

	#test delete_invoice function
	delete_invoice(2, cur)
	test_conn.commit()
	cur.execute(sql)
	post_delete_invoices = cur.fetchall()
	assert len(post_delete_invoices) == 1

	date = "01-01-2025"
	invoice_date = datetime.strptime(date, "%m-%d-%Y")
	int_date = int(invoice_date.timestamp())

	#test the correct invoice was deleted
	assert post_delete_invoices[0][0] == 1
	assert post_delete_invoices[0][1] == "NewProject"
	assert post_delete_invoices[0][2] == int_date
	assert post_delete_invoices[0][3] == "1"
	assert post_delete_invoices[0][4] == "Draft"


def test_delete_time_entry(test_conn, table_initialize):
	"""Test to see if the delete_time_entry function deletes the correct row"""
	cur = test_conn.cursor()
	architect = table_initialize['architect']
	project = table_initialize['project']
	testTimeEntry2 = TimeEntry("01-01-2025 1:00:00", 45, project.project_id, 
		architect.architect_id, phase_id = 8)
	add_time_entry(testTimeEntry2, cur)
	test_conn.commit()
	sql = "SELECT time_entry_id, start_time, duration_minutes, projects.project_name, \
		architects.name FROM time_entries \
		LEFT JOIN projects ON time_entries.project_id = projects.project_id \
		INNER JOIN architects ON time_entries.architect_id = architects.architect_id \
		ORDER BY project_name IS NULL, project_name ASC, name ASC"
	cur.execute(sql)
	pre_delete_time_entries = cur.fetchall()

	#test to see if there are 2 time_entries to start
	assert len(pre_delete_time_entries) == 2

	#test delete_time_entries function
	delete_time_entry(1, cur)
	test_conn.commit()
	cur.execute(sql)
	post_delete_time_entries = cur.fetchall()
	assert len(post_delete_time_entries) == 1

	#test the correct time_entry was deleted
	assert post_delete_time_entries[0][0] == 2
	assert post_delete_time_entries[0][1] == "01-01-2025 1:00:00"
	assert post_delete_time_entries[0][2] == 45
	assert post_delete_time_entries[0][3] == "NewProject"
	assert post_delete_time_entries[0][4] == "Name"