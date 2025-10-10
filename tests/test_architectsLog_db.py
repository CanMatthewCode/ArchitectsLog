#testing for acrchitectsLog_db.py

import pytest
import os
import sqlite3
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from architectsLog_db import get_connection, create_architect_table, create_project_table, create_phases_table, create_room_types_table, create_project_rooms_table

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

#test if rooms_type table was created
def test_room_types_table_creation(test_conn):
	"""Test that the rooms_type table is created"""
	cursor = test_conn.cursor()
	create_room_types_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='room_types'")
	result = cursor.fetchone()

	assert result is not None, "room_types table should exist"
	assert result[0] == 'room_types'

#test if project_rooms table was created
def test_project_rooms_table_creation(test_conn):
	"""Test that the project_rooms table is created"""
	cursor = test_conn.cursor()
	create_project_rooms_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='project_rooms'")
	result = cursor.fetchone()

	assert result is not None, "project_rooms table should exist"
	assert result[0] == 'project_rooms' 



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

#test if the room_types table has correct column names
def test_room_types_table_column_names(table_info):
	"""Test that the room_types table has correct column names"""
	column_names = [col[1] for col in table_info('room_types', create_room_types_table)]

	assert 'room_type_id' in column_names
	assert 'room_name' in column_names

#test if the room_types table has correct column types
def test_room_types_table_column_types(table_info):
	"""Test that the room_types table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('room_types', create_room_types_table)}

	assert column_types['room_type_id'] == 'INTEGER'
	assert column_types['room_name'] == 'TEXT'

#test if the project_rooms table has correct column names
def test_project_rooms_table_column_names(table_info):
	"""Test that the project_rooms table has correct column names"""
	column_names = [col[1] for col in table_info('project_rooms', create_project_rooms_table)]

	assert 'project_room_id' in column_names
	assert 'room_type_id' in column_names
	assert 'project_id' in column_names

#test if the project_rooms table has correct column types
def test_project_rooms_table_column_types(table_info):
	"""Test that the project_rooms table has correct column types"""
	column_types = {col[1] : col[2] for col in table_info('project_rooms', create_project_rooms_table)}

	assert column_types['project_room_id'] == 'INTEGER'
	assert column_types['room_type_id'] == 'INTEGER'
	assert column_types['project_id'] == 'INTEGER'