#testing for acrchitectsLog_db.py

import pytest
import os
import sqlite3
import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from architectsLog_db import get_connection, create_architect_table

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

#test if architect table was created
def test_architect_table_creation(test_conn):
	"""Test that the architect table is created"""
	cursor = test_conn.cursor()
	create_architect_table(cursor)

	#query sqlite_master to check if the table exists
	cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='architects'")
	result = cursor.fetchone()

	assert result is not None, "architects table should exist"
	assert result[0] == 'architects'

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


#test if architect table has correct column names
def test_architect_table_column_names(table_info):
	'''Test that the architect table has correct column names'''
	column_names = [col[1] for col in table_info('architects', create_architect_table)]

	assert 'architect_id' in column_names
	assert 'name' in column_names
	assert 'license_number' in column_names
	assert 'phone_number' in column_names
	assert 'email' in column_names
	assert 'company_name' in column_names
	assert 'is_active' in column_names

#test if architect table has correct column types
def test_architect_table_column_types(table_info):
	'''Test that the architect table has correct column types'''
	column_types = {col[1] : col[2] for col in table_info('architects', create_architect_table)}

	assert column_types['architect_id'] == 'INTEGER'
	assert column_types['name'] == 'TEXT'
	assert column_types['license_number'] == 'TEXT'
	assert column_types['phone_number'] == 'TEXT'
	assert column_types['email'] == 'TEXT'
	assert column_types['company_name'] == 'TEXT'
	assert column_types['is_active'] == 'INTEGER'