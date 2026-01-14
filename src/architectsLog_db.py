# Database functions for the Architect's Log

import sqlite3
import os
from contextlib import contextmanager
from architectsLog_classes import Architect, Project, Invoice, TimeEntry
from architectsLog_constants import PHASES, UPDATABLE_ARCHITECTS_COLUMNS, \
	UPDATABLE_PROJECTS_COLUMNS, UPDATABLE_INVOICES_COLUMNS, UPDATABLE_TIME_ENTRIES_COLUMNS, \
	ARCHITECT_STATUSES, INVOICE_STATUSES, PROJECT_STATUSES

basedir = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(basedir, 'architectsLog.db')

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
			status TEXT DEFAULT 'Active'
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
			invoice_id INTEGER,
			FOREIGN KEY (project_id) REFERENCES projects (project_id),
			FOREIGN KEY (architect_id) REFERENCES architects (architect_id),
			FOREIGN KEY (phase_id) REFERENCES phases (phase_id),
			FOREIGN KEY (invoice_id) REFERENCES invoices (invoice_id) 
				ON DELETE SET NULL
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
	cur.execute("""INSERT INTO projects (project_id, project_name, client_name,
		client_address, start_date, current_phase_id)
		VALUES(-1, "Business Development", "Internal", "N/A", "01/01/1900", 8)
		""")
	# add Administration as id -2
	cur.execute("""INSERT INTO projects (project_id, project_name, client_name,
		client_address, start_date, current_phase_id)
		VALUES(-2, "Administration", "Internal", "N/A2", "01/01/1900", 9)
		""")

def initialize_invoices(cur: sqlite3.Cursor) -> None:
	"""Initialize the invoices table with a 0 id, None named invoice for default
	time entries"""
	cur.execute("SELECT COUNT(*) FROM invoices WHERE invoice_id IS 0")
	if cur.fetchone()[0] > 0:
		return
	cur.execute("""INSERT INTO invoices (invoice_id, project_id, 
		created_date, invoice_number)
		VALUES (0,0,0,'Not Invoiced')""")

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


def add_invoice(invoice: Invoice, cur: sqlite3.Cursor) -> int:
	"""Add an Invoice object to the invoices table, add invoice_id to the Invoice object, 
	return newly added invoice_id"""
	sql = "INSERT INTO invoices (project_id, created_date, invoice_number, status) \
		VALUES (?, ?, ?, ?)"

	invoice_values = (invoice.project.project_id, invoice.created_date, 
		invoice.invoice_number, invoice.status)

	cur.execute(sql, invoice_values)
	invoice_id = cur.lastrowid
	invoice.invoice_id = invoice_id

	return invoice_id


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



#	~~~LOAD EXISTING OBJECT FROM TABLE FUNCTIONS~~~

def load_architect(architect_id: int, cur: sqlite3.Cursor) -> Architect:
	"""Load Architect object from the architects table and return it"""
	sql = "SELECT * FROM architects WHERE architect_id = ?"
	cur.execute(sql, (architect_id,))
	arch_info = cur.fetchone()
	loaded_architect = Architect(arch_info[1], arch_info[2], arch_info[3],
		arch_info[4], arch_info[5], arch_info[6], arch_info[0])

	return loaded_architect

def load_all_active_architects(cur: sqlite3.Cursor) -> list[tuple[int, str]]:
	"""Load all active architect names and architect_ids from architects table, 
	return list of tuples containing both"""
	sql = """SELECT architect_id, name FROM architects WHERE status = 'Active' 
		ORDER BY name ASC"""
	cur.execute(sql)
	architect_list = cur.fetchall()

	return architect_list

def load_all_architects(cur: sqlite3.Cursor) -> list[tuple[int, str, str]]:
	"""Load all active and inactive architect names, architect_ids, and statuses
	from architects table, return list of tuples containing all three columns"""
	sql = """SELECT architect_id, name, status FROM architects 
		ORDER BY status ASC, name ASC"""
	cur.execute(sql)
	architect_list = cur.fetchall()

	return architect_list


def load_project(project_id: int, cur: sqlite3.Cursor) -> Project:
	"""Load Project object from the projects table and return it"""
	sql = "SELECT * FROM projects WHERE project_id = ?"
	cur.execute(sql, (project_id,))
	proj_info = cur.fetchone()
	loaded_project = Project(proj_info[1], proj_info[2], proj_info[3], proj_info[4],
		proj_info[5], proj_info[6], proj_info[0])

	return loaded_project

def load_all_active_projects(cur:sqlite3.Cursor) -> list[tuple[int, str]]:
	"""Load all the active project names and project_ids from the projects table,
	return list of tuples containing both"""
	sql = """SELECT project_id, project_name FROM projects WHERE status = 'Active' 
		ORDER BY project_name ASC"""
	cur.execute(sql)
	project_list = cur.fetchall()

	return project_list

def load_all_projects(cur:sqlite3.Cursor) -> list[tuple[int, str, str]]:
	"""Load all the project names, project_ids, and statuses from the projects table,
	return list of tuples containing all three columns"""
	sql = """SELECT project_id, project_name, status FROM projects
		ORDER BY project_name ASC, status ASC"""
	cur.execute(sql)
	project_list = cur.fetchall()

	return project_list


def load_invoice(invoice_id: int, cur: sqlite3.Cursor) -> Invoice:
	"""Load Invoice object from the invoices table and return it"""
	sql = "SELECT * FROM invoices WHERE invoice_id = ?"
	cur.execute(sql, (invoice_id,))
	inv_info = cur.fetchone()
	project = load_project(inv_info[1], cur)
	loaded_invoice = Invoice(inv_info[3], inv_info[2], project, inv_info[4], inv_info[0])

	return loaded_invoice

def load_project_invoices(project_id: int, 
	cur: sqlite3.Cursor) -> list[tuple[int, int, str, str]]:
	"""Load all rows in the invoices table associated with a project_id, return
	list of tuples containing invoice_id, invoice_number, created_date, status"""
	sql = "SELECT invoice_id, invoice_number, created_date, status FROM invoices \
		WHERE project_id = ? ORDER BY status ASC, created_date ASC"
	cur.execute(sql, (project_id,))
	loaded_invoices = cur.fetchall()

	return loaded_invoices

def load_status_invoices(invoice_status: str, 
	cur: sqlite3.Cursor) -> list[tuple[int, int, str, str]]:
	"""Load all rows in the invoices table associated with an invoice status, return
	list of tuples containing invoice_id, invoice_number, created_date, project_name"""
	if invoice_status not in INVOICE_STATUSES:
		raise ValueError(f"Invalid status: {invoice_status}")
	sql = "SELECT invoice_id, invoice_number, created_date, projects.project_name \
		FROM invoices INNER JOIN projects ON invoices.project_id = projects.project_id \
		WHERE invoices.status = ? ORDER BY project_name ASC, created_date ASC"
	cur.execute(sql, (invoice_status,))
	loaded_invoices = cur.fetchall()

	return loaded_invoices

def load_all_invoices(cur: sqlite3.Cursor) -> list[tuple[int, str, str, int, str]]:
	"""Load all invoice rows from the invoice table and return them as a list of 
	tuples containing invoice_id, project name, created date, invoice number, status"""
	sql = "SELECT invoice_id, projects.project_name, created_date, invoice_number, \
		invoices.status FROM invoices INNER JOIN projects \
		ON invoices.project_id = projects.project_id \
		ORDER BY project_name ASC, invoices.status ASC, created_date ASC"
	cur.execute(sql)
	loaded_invoices = cur.fetchall()

	return loaded_invoices


def load_time_entry(time_entry_id: int, cur: sqlite3.Cursor) -> TimeEntry:
	"""Load TimeEntry object from the time_entries table and return it"""
	sql = "SELECT * FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (time_entry_id,))
	t_e_info = cur.fetchone()
	loaded_time_entry = TimeEntry(t_e_info[4], t_e_info[5], t_e_info[1],
		t_e_info[2], t_e_info[3], t_e_info[6], t_e_info[7], t_e_info[0])

	return loaded_time_entry

def load_all_project_time_entries(project_id: int, 
	cur: sqlite3.Cursor) -> list[tuple[int, str, int, str]]:
	"""Load all time_entries from time_entries table with same project_id,
	returns a list of tuples containing time_entry_id, start_time, duration_minutes,
	architect.name"""
	sql = "SELECT time_entry_id, start_time, duration_minutes, architects.name \
		FROM time_entries INNER JOIN architects ON time_entries.architect_id \
		= architects.architect_id WHERE project_id = ? ORDER BY start_time ASC"
	cur.execute(sql, (project_id,))
	time_entries_list = cur.fetchall()

	return time_entries_list

def load_all_architect_time_entries(architect_id: int,
	cur: sqlite3.Cursor) -> list[tuple[int, str, int, str]]:
	"""Load all time_entries from time_entries table with same architect_id,
	returns a list of tuples containing time_entry_id, start_time, 
	duration_minutes, project_name"""
	sql = "SELECT time_entry_id, start_time, duration_minutes, projects.project_name \
		FROM time_entries LEFT JOIN projects ON time_entries.project_id = \
		projects.project_id WHERE architect_id = ? ORDER BY start_time ASC"
	cur.execute(sql, (architect_id,))
	time_entries_list = cur.fetchall()

	return time_entries_list

def load_invoice_time_entries(invoice_id: int | None, 
	cur: sqlite3.Cursor) -> list[tuple[int, str, int, int, str]]:
	"""Load all time_entries from time_entries table with same invoice_id, 
	returns a list of tuples containing time_entry_id, start_time, 
	duration_minutes, project_id, notes. Passing in None returns all 
	unaffiliated time_entries ordered by project_id"""
	if invoice_id is None:
		sql = "SELECT time_entry_id, start_time, duration_minutes, project_id, notes \
			FROM time_entries WHERE invoice_id is Null \
			ORDER BY project_id ASC, start_time ASC"
		cur.execute(sql)
	else:
		sql = "SELECT time_entry_id, start_time, duration_minutes, project_id, notes \
			FROM time_entries WHERE invoice_id = ? ORDER BY start_time ASC"
		cur.execute(sql, (invoice_id,))
	time_entries_list = cur.fetchall()

	return time_entries_list

def load_all_time_entries(cur: sqlite3.Cursor) -> list[tuple[int, str, int, str, str]]:
	"""Load all time_entries in time_entries table, returns a list of tuples
	containing time_entry_id, start_time, duration_minutes, project_name, architect_name"""
	sql = "SELECT time_entry_id, start_time, duration_minutes, projects.project_name, \
		architects.name FROM time_entries \
		LEFT JOIN projects ON time_entries.project_id = projects.project_id \
		INNER JOIN architects ON time_entries.architect_id = architects.architect_id \
		ORDER BY project_name IS NULL, project_name ASC, name ASC"
	cur.execute(sql)
	time_entries_list = cur.fetchall()

	return time_entries_list

def load_nonproject_phases_time_entries(
	cur:sqlite3.Cursor) -> list[tuple[int, str, int, str, int]]:
	"""Load all time_entries by phase in the time_entries table which do not 
	have an attached project: either Business Development (8) or Administration (9)
	Returns a list of tuples containing time_entry_id, start time, duration_mionutes,
	architect_name, phase_id"""
	sql = "SELECT time_entry_id, start_time, duration_minutes, architects.name, \
		phase_id FROM time_entries INNER JOIN architects ON time_entries.architect_id= \
		architects.architect_id WHERE phase_id IN (8,9) ORDER BY start_time ASC"

	cur.execute(sql)
	time_entries_list = cur.fetchall()

	return time_entries_list



#	~~~TABLE UPDATE FUNCTIONS~~~

def update_architect(column_name: str, architect: Architect, value: int | str, 
	cur: sqlite3.Cursor) -> Architect:
	"""Update one column for a row which exists in the architects table, set newly
	changed attribute value to the Architect object, return Architect object"""
	if column_name not in UPDATABLE_ARCHITECTS_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE architects SET {column_name} = ? WHERE architect_id = ?"
	update_values = (value, architect.architect_id)

	cur.execute(sql, update_values)
	setattr(architect, column_name, value)
	
	return architect


def update_project(column_name: str, project_id: int, value: int | str,
	cur: sqlite3.Cursor) -> None:
	"""Update one column for a row which exists in the projects table, set newly
	changed attribute value to the Project object, return Project object"""
	if column_name not in UPDATABLE_PROJECTS_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE projects SET {column_name} = ? WHERE project_id = ?"
	update_values = (value, project_id)

	cur.execute(sql, update_values)



def update_invoice(column_name: str, invoice: Invoice, value: int | str,
	cur: sqlite3.Cursor) -> Invoice:
	"""Update one column for a row which exists in the invoices table, set newly
	changed attribute value to the Invoice object, return Invoice object"""
	if column_name not in UPDATABLE_INVOICES_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE invoices SET {column_name} = ? WHERE invoice_id = ?"
	update_values = (value, invoice.invoice_id)

	cur.execute(sql, update_values)

	if column_name == "project_id":
		project = load_project(value, cur)
		column_name = "project"
		value = project

	setattr(invoice, column_name, value)

	return invoice


def update_time_entry(column_name: str, time_entry: TimeEntry, value: int | str,
	cur: sqlite3.Cursor) -> TimeEntry:
	"""Update one column for a row which exists in the time_entries table, set
	newly changed attribute value to the TimeEntry object, return TimeEntry object"""
	if column_name not in UPDATABLE_TIME_ENTRIES_COLUMNS:
		raise ValueError(f"Invalid column: {column_name}")
	sql = f"UPDATE time_entries SET {column_name} = ? WHERE time_entry_id = ?"
	update_values = (value, time_entry.time_entry_id)

	cur.execute(sql, update_values)

	if column_name == "architect_id":
		architect = load_architect(value, cur)
		column_name = "architect"
		value = architect
	elif column_name == "project_id":
		project = load_project(value, cur)
		column_name = "project"
		value = project

	setattr(time_entry, column_name, value)

	return time_entry


#	~~~TABLE DELETE FUNCTIONS~~~

def delete_invoice(invoice_id: int, cur: sqlite3.Cursor) -> None:
	"""Permenently delete an invoice row from the invoices table"""
	sql = "DELETE FROM invoices WHERE invoice_id = ?"
	cur.execute(sql, (invoice_id,))


def delete_time_entry(time_entry_id: int, cur: sqlite3.Cursor) -> None:
	"""Permenently delete a time_entry row from the time_entries table"""
	sql = "DELETE FROM time_entries WHERE time_entry_id = ?"
	cur.execute(sql, (time_entry_id,))