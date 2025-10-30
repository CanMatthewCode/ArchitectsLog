# Database functions for the Architect's Log

import sqlite3
import os
from contextlib import contextmanager
from architectsLog_classes import Architect, Project, Invoice, TimeEntry
from architectsLog_constants import PHASES, UPDATABLE_ARCHITECTS_COLUMNS, \
	UPDATABLE_PROJECTS_COLUMNS, UPDATABLE_INVOICES_COLUMNS, UPDATABLE_TIME_ENTRIES_COLUMNS

DB_FILE = 'architectsLog.db'

#database connection function for testing
def get_connection(db_file: str | None = None) -> sqlite3.Connection:
	"""Get database connection with foreign keys enabled"""
	if db_file is None:
		db_file = DB_FILE

	conn = sqlite3.connect(db_file)
	conn.execute('PRAGMA foreign_keys = ON;')
	return conn

#database connection function for production code
@contextmanager
def get_db_connection(db_file: str | None = None) -> sqlite3.Connection:
    """Context manager for database connections"""
    if db_file is None:
        db_file = DB_FILE
    conn = sqlite3.connect(db_file)
    conn.execute('PRAGMA foreign_keys = ON;')
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


#	~~~TABLE CREATION FUNCTIONS~~~

def create_architect_table(cur: sqlite3.Cursor) -> None:
	"""Create Architect's Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS architects (
			architect_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL UNIQUE,
			license_number TEXT NOT NULL UNIQUE,
			phone_number TEXT NOT NULL,
			email TEXT NOT NULL UNIQUE,
			company_name TEXT,
			is_active INTEGER DEFAULT 1
		)
	''')

def create_project_table(cur: sqlite3.Cursor) -> None:
	"""Create Project's Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS projects (
			project_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_name TEXT NOT NULL,
			client_name TEXT NOT NULL,
			client_address TEXT NOT NULL UNIQUE,
			start_date TEXT NOT NULL,
			current_phase_id INTEGER NOT NULL,
			status TEXT DEFAULT 'active',
			FOREIGN KEY (current_phase_id) REFERENCES phases (phase_id)
		)
	''')

def create_phases_table(cur: sqlite3.Cursor) -> None:
	"""Create Phases Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS phases (
			phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_phase TEXT NOT NULL
		)
	''')

def create_invoices_table(cur: sqlite3.Cursor) -> None:
	"""Create Invoices Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS invoices (
			invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_id INTEGER NOT NULL,
			created_date TEXT NOT NULL,
			invoice_number INTEGER,
			status TEXT DEFAULT 'draft',
			FOREIGN KEY (project_id) REFERENCES projects (project_id)
		)
	''')

def create_time_entries_table(cur: sqlite3.Cursor) -> None:
	"""Create Time_Entries Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS time_entries (
			time_entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_id INTEGER,
			architect_id INTEGER NOT NULL,
			phase_id INTEGER NOT NULL,
			start_time TEXT NOT NULL,
			end_time TEXT NOT NULL,
			duration_minutes INTEGER NOT NULL,
			notes TEXT,
			invoice_id INTEGER,
			FOREIGN KEY (project_id) REFERENCES projects (project_id),
			FOREIGN KEY (architect_id) REFERENCES architects (architect_id),
			FOREIGN KEY (phase_id) REFERENCES phases (phase_id),
			FOREIGN KEY (invoice_id) REFERENCES invoices (invoice_id)
		)
	''')


#	~~~TABLE INSERTION FUNCTIONS~~~

def add_architect(architect: Architect, cur: sqlite3.Cursor) -> int:
	"""Add an Architect object to the architects table"""
	sql = "INSERT INTO architects (name, license_number, phone_number, email, \
		company_name, is_active) VALUES(?, ?, ?, ?, ?, ?)"

	architect_values = (architect.name, architect.license_number, architect.phone_number, 
		architect.email, architect.company_name, architect.is_active)

	cur.execute(sql, architect_values)
	architect_id = cur.lastrowid
	architect.architect_id = architect_id

	return architect_id


def initialize_phases(cur: sqlite3.Cursor) -> None:
	"""Initialize the phases table with the PHASES dictionary if not done so already"""
	query = "SELECT COUNT(*) FROM phases"
	cur.execute(query)
	#check if the PHASES are already in the phases table - fetchone() returns tuple
	number_of_phases = cur.fetchone()[0]
	if number_of_phases > 0:
		return
	#if not, loop through PHASES dictionary and add values to match PHASES order
	else:
		sql = "INSERT INTO phases (project_phase) VALUES (?)"
		for phase_id, phase_name in PHASES.items():
			cur.execute(sql, (phase_name,))


def add_project(project: Project, cur: sqlite3.Cursor) -> int:
	"""Add a Project object to the projects table"""
	sql = "INSERT INTO projects (project_name, client_name, client_address, \
		start_date, current_phase_id, status) VALUES (?, ?, ?, ?, ?, ?)"

	project_values = (project.project_name, project.client_name, project.client_address, 
		project.start_date, project.current_phase_id, project.status)

	cur.execute(sql, project_values)
	project_id = cur.lastrowid
	project.project_id = project_id

	return project_id


def add_invoice(invoice: Invoice, cur: sqlite3.Cursor) -> int:
	"""Add an Invoice object to the invoices table"""
	sql = "INSERT INTO invoices (project_id, created_date, invoice_number, status) \
		VALUES (?, ?, ?, ?)"

	invoice_values = (invoice.project.project_id, invoice.created_date, 
		invoice.invoice_number, invoice.status)

	cur.execute(sql, invoice_values)
	invoice_id = cur.lastrowid
	invoice.invoice_id = invoice_id

	return invoice_id


def add_time_entry(time_entry: TimeEntry, cur: sqlite3.Cursor) -> int:
	"""Add a TimeEntry object to the time_entries table"""
	sql = "INSERT INTO time_entries (project_id, architect_id, phase_id, start_time, \
		end_time, duration_minutes, invoice_id, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"

	time_entry_values = (time_entry.project.project_id, time_entry.architect.architect_id,
		time_entry.project.current_phase_id, time_entry.start_time, time_entry.end_time,
		time_entry.duration_minutes, time_entry.notes, time_entry.invoice_id)

	cur.execute(sql, time_entry_values)
	time_entry_id = cur.lastrowid
	time_entry.time_entry_id = time_entry_id

	return time_entry_id



#	~~~TABLE UPDATE FUNCTIONS~~~

def update_architect(column_name: str, architect: Architect, value: int | str, cur: sqlite3.Cursor) -> int:
	"""Update one column for a row which already exists in the architects table"""
	if column_name not in UPDATABLE_ARCHITECTS_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE architects SET {column_name} = ? WHERE architect_id = ?"
	update_values = (value, architect.architect_id)

	rows_updated = cur.execute(sql, update_values)

	if rows_updated.rowcount > 0:
		setattr(architect, column_name, value)
		return architect
	else:
		return None