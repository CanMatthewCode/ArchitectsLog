# Database functions for the Architect's Log

import sqlite3
from datetime import datetime
from contextlib import contextmanager
from architectsLog_classes import Architect, Project, Invoice, TimeEntry
from architectsLog_constants import (PHASES, UPDATABLE_PROJECTS_COLUMNS,
	UPDATABLE_TIME_ENTRIES_COLUMNS)

DB_FILE = ""

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
	"""Create Architects Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS architects (
			architect_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL UNIQUE,
			license_number TEXT NOT NULL UNIQUE,
			phone_number TEXT NOT NULL,
			email TEXT NOT NULL UNIQUE,
			company_name TEXT,
			status TEXT DEFAULT 'Active'
		)
	''')

def create_project_table(cur: sqlite3.Cursor) -> None:
	"""Create Projects Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS projects (
			project_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_name TEXT NOT NULL,
			client_name TEXT NOT NULL,
			client_address TEXT NOT NULL UNIQUE,
			start_date INTEGER NOT NULL,
			current_phase_id INTEGER NOT NULL,
			status TEXT DEFAULT 'Active',
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
			created_date INTEGER NOT NULL,
			invoice_number TEXT,
			status TEXT DEFAULT 'Draft',
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
			start_time INTEGER NOT NULL,
			duration_minutes INTEGER NOT NULL,
			notes TEXT,
			invoice_id INTEGER DEFAULT 0,
			FOREIGN KEY (project_id) REFERENCES projects (project_id),
			FOREIGN KEY (architect_id) REFERENCES architects (architect_id),
			FOREIGN KEY (phase_id) REFERENCES phases (phase_id),
			FOREIGN KEY (invoice_id) REFERENCES invoices (invoice_id) 
				ON DELETE SET DEFAULT
		)
	''')



#	~~~TABLE INITIALIZE FUNCTION~~~

def sqltable_initialize() -> None:
	"""Creates all needed tables for architects database on initial program boot up
	initializes phases table to store possible project phases"""
	with get_db_connection() as conn:
		cur = conn.cursor()
		create_architect_table(cur)
		create_project_table(cur)
		create_phases_table(cur)
		create_invoices_table(cur)
		create_time_entries_table(cur)
		initialize_phases(cur)
		initialize_projects(cur)
		initialize_invoices(cur)

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

def initialize_projects(cur: sqlite3.Cursor) -> None:
	"""Initialize projects table with non-project based work flows: 
	Business Development (id = -1) and Administration (id = -2)"""
	cur.execute("SELECT COUNT(*) FROM projects WHERE project_id IN (-1, -2)")
	#return if these already exist in database table
	if cur.fetchone()[0] > 0:
		return
	# add Business Development as id -1
	start_date_str = "01-01-1900"
	project_date = datetime.strptime(start_date_str, "%m-%d-%Y")
	int_date = int(project_date.timestamp())
	cur.execute("""INSERT INTO projects (project_id, project_name, client_name,
		client_address, start_date, current_phase_id)
		VALUES(-1, ?, ?, ?, ?, 8)""", ("Administration", "Internal", "N/A", int_date,))
	# add Administration as id -2
	cur.execute("""INSERT INTO projects (project_id, project_name, client_name,
		client_address, start_date, current_phase_id)
		VALUES(-2, ?, ?, ?, ?, 9)""", ("Business Development", "Internal", "N/A2", int_date,))

def initialize_invoices(cur: sqlite3.Cursor) -> None:
	"""Initialize the invoices table with a 0 id, None named invoice for default
	time entries"""
	cur.execute("SELECT COUNT(*) FROM invoices WHERE invoice_id IS 0")
	if cur.fetchone()[0] > 0:
		return
	cur.execute("""INSERT INTO invoices (invoice_id, project_id, 
		created_date, invoice_number)
		VALUES (?, ?, ?, ?)""", (0, -1, 0,'Not Invoiced',))



#	~~~TABLE INSERTION FUNCTIONS~~~

def add_architect(architect: Architect, cur: sqlite3.Cursor) -> int:
	"""Add an Architect object to the architects table, add architect_id to architect object, 
	return newly added architect_id"""
	sql = "INSERT INTO architects (name, license_number, phone_number, email, \
		company_name, status) VALUES(?, ?, ?, ?, ?, ?)"

	architect_values = (architect.name, architect.license_number, architect.phone_number, 
		architect.email, architect.company_name, architect.status)

	cur.execute(sql, architect_values)
	architect_id = cur.lastrowid
	architect.architect_id = architect_id

	return architect_id

def add_project(project: Project, cur: sqlite3.Cursor) -> int:
	"""Add a Project object to the projects table, add project_id to the Project object,
	return newly added project_id"""
	sql = "INSERT INTO projects (project_name, client_name, client_address, \
		start_date, current_phase_id, status) VALUES (?, ?, ?, ?, ?, ?)"

	project_values = (project.project_name, project.client_name, project.client_address, 
		project.start_date, project.current_phase_id, project.status)

	cur.execute(sql, project_values)
	project_id = cur.lastrowid
	project.project_id = project_id

	return project_id

def add_time_entry(time_entry: TimeEntry, cur: sqlite3.Cursor) -> int:
	"""Add a TimeEntry object to the time_entries table, return newly added time_entry_id"""
	sql = "INSERT INTO time_entries (project_id, architect_id, phase_id, start_time, \
		duration_minutes, notes, invoice_id) VALUES (?, ?, ?, ?, ?, ?, ?)"
	project_id = time_entry.project_id if time_entry.project_id else None
	time_entry_values = (project_id, time_entry.architect_id,
		time_entry.phase_id, time_entry.start_time, time_entry.duration_minutes, 
		time_entry.notes, time_entry.invoice_id)

	cur.execute(sql, time_entry_values)
	time_entry_id = cur.lastrowid
	time_entry.time_entry_id = time_entry_id

	return time_entry_id

def add_invoice(invoice: Invoice, cur: sqlite3.Cursor) -> int:
	"""Add an Invoice object to the invoices table, add invoice_id to the Invoice object, 
	return newly added invoice_id.  Function was refactored out, but kept for testing
	SQL validity"""
	sql = "INSERT INTO invoices (project_id, created_date, invoice_number, status) \
		VALUES (?, ?, ?, ?)"

	invoice_values = (invoice.project_id, invoice.created_date, 
		invoice.invoice_number, invoice.status)

	cur.execute(sql, invoice_values)
	invoice_id = cur.lastrowid
	invoice.invoice_id = invoice_id

	return invoice_id



#	~~~LOAD EXISTING VALUES FROM TABLE FUNCTIONS~~~

def load_architect(architect_id: int, cur: sqlite3.Cursor) -> Architect:
	"""Load Architect object from the architects table and return it"""
	sql = "SELECT * FROM architects WHERE architect_id = ?"
	cur.execute(sql, (architect_id,))
	arch_info = cur.fetchone()
	loaded_architect = Architect(arch_info[1], arch_info[2], arch_info[3],
		arch_info[4], arch_info[5], arch_info[6], arch_info[0])

	return loaded_architect

def load_project(project_id: int, cur: sqlite3.Cursor) -> Project:
	"""Load Project object from the projects table and return it"""
	sql = "SELECT * FROM projects WHERE project_id = ?"
	cur.execute(sql, (project_id,))
	proj_info = cur.fetchone()
	loaded_project = Project(proj_info[1], proj_info[2], proj_info[3], proj_info[4],
		proj_info[5], proj_info[6], proj_info[0])

	return loaded_project

def get_most_recent_archid_and_projid(cur: sqlite3.Cursor) -> list[tuple[int, int]]:
	"""Function to retrieve the most recent architect and project from the
	time_entries table in the database"""
	query = "SELECT architect_id, project_id FROM time_entries\
		ORDER BY start_time DESC LIMIT 1"
	cur.execute(query)
	return cur.fetchone()

def get_most_recent_project_phase(project_id: int, cur: sqlite3.Cursor) -> int:
	"""Get a projects most recently used phase from the time_entries table
	using a project_id"""
	query = "SELECT phase_id FROM time_entries WHERE project_id = ?\
		ORDER BY start_time DESC LIMIT 1"
	cur.execute(query, (project_id,))
	value = cur.fetchone()
	if value:
		return value[0]
	else:
		return None

def load_invoice_ids_no_time_entries(cur:sqlite3.Cursor) -> list[tuple[int]]:
	"""Load all invoice_id's which have no time_entry objects attached to them"""
	sql = "SELECT invoices.invoice_id FROM invoices LEFT JOIN time_entries \
		ON invoices.invoice_id = time_entries.invoice_id \
		WHERE time_entries.invoice_id IS NULL AND invoices.invoice_id != 0"

	cur.execute(sql)
	no_time_entries_invoices = cur.fetchall()

	return no_time_entries_invoices



#	~~~TABLE UPDATE FUNCTIONS~~~

def update_project(column_name: str, project_id: int, value: int | str,
	cur: sqlite3.Cursor) -> None:
	"""Update one column for a row which exists in the projects table"""
	if column_name not in UPDATABLE_PROJECTS_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE projects SET {column_name} = ? WHERE project_id = ?"
	update_values = (value, project_id)

	cur.execute(sql, update_values)

def update_time_entry(column_name: str, time_entry_id: int, value: int | str,
	cur: sqlite3.Cursor) -> None:
	"""Update one column for a row which exists in the time_entries table"""
	if column_name not in UPDATABLE_TIME_ENTRIES_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE time_entries SET {column_name} = ? WHERE time_entry_id = ?"
	update_values = (value, time_entry_id)

	cur.execute(sql, update_values)



#	~~~TABLE DELETE FUNCTIONS~~~

def delete_invoice(invoice_id: int, cur: sqlite3.Cursor) -> None:
	"""Permenently delete an invoice row from the invoices table"""
	sql = "DELETE FROM invoices WHERE invoice_id = ?"
	cur.execute(sql, (invoice_id,))

def delete_time_entry(time_entry_id: int, cur: sqlite3.Cursor) -> None:
	"""Permenently delete a time_entry row from the time_entries table"""
	sql = "DELETE FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (time_entry_id,))
