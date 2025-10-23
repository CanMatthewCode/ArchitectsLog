#testing for acrchitectsLog_db.py

import pytest
import os
import sqlite3

from architectsLog_db import get_connection, create_architect_table, create_project_table, create_phases_table
from architectsLog_db import create_invoices_table, create_time_entries_table
from architectsLog_db import add_architect

from architectsLog_classes import Architect, Project, Invoice, TimeEntry

TEST_DB = 'test_architectsLog.db'

#createa database auto cleanup before and after each test
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
	assert 'phase_order' in column_names

#test if phases table has correct column types
def test_phase_table_column_types(table_info):
	"""Test that the phases table has the correct column types"""
	column_types = {col[1] : col[2] for col in table_info('phases', create_phases_table)}

	assert column_types['phase_id'] == 'INTEGER'
	assert column_types['project_phase'] == 'TEXT'
	assert column_types['phase_order'] == 'INTEGER'


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
	assert column_types['invoice_number'] == 'TEXT'
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
	assert 'invoice_id' in column_names
	assert 'notes' in column_names

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
	assert column_types['invoice_id'] == 'INTEGER'
	assert column_types['notes'] == 'TEXT'


#	~~~INSERT FUNCTIONS TESTS~~~

#test if the add_architect function adds an architect to the architects table
def test_add_architect(test_conn):
	"""Test that the architects table has correctly added architect"""
	#create cursor, create architect table, and commit it to the database
	cur = test_conn.cursor()
	create_architect_table(cur)
	test_conn.commit()

	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")
	architect_id = add_architect(testArchitect, cur)
	test_conn.commit()

	#quiery information from newly added architect to ensure insertion
	sql = "SELECT * FROM architects WHERE architect_id = ?"
	cur.execute(sql, (architect_id,))
	row = cur.fetchone()

	assert row[0] == 1
	assert row[1] == "Name"
	assert row[2] == "LicenseNumber01"
	assert row[3] == "123-456-7890"
	assert row[4] == "email@domain.com"
	assert row[5] == "MyCompany"
	assert row[6] == 1