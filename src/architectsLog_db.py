# Database functions for the Architect's Log

import sqlite3
import os
from contextlib import contextmanager

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
			architect_id INTEGER,
			start_date TEXT NOT NULL,
			current_phase_id INTEGER NOT NULL,
			status TEXT DEFAULT 'active',
			FOREIGN KEY (architect_id) REFERENCES architects (architect_id)
			FOREIGN KEY (current_phase_id) REFERENCES phases (phase_id)
		)
	''')

def create_phases_table(cur: sqlite3.Cursor) -> None:
	"""Create Phases Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS phases (
			phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_phase TEXT NOT NULL,
			phase_order INTEGER NOT NULL
		)
	''')

def create_room_types_table(cur: sqlite3.Cursor) -> None:
	"""Create Room_Types Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS room_types (
			room_type_id INTEGER PRIMARY KEY AUTOINCREMENT,
			room_name TEXT NOT NULL
		)
	''')

def create_project_rooms_table(cur: sqlite3.Cursor) -> None:
	"""Create Project_Rooms Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS project_rooms (
			project_room_id INTEGER PRIMARY KEY AUTOINCREMENT,
			room_type_id INTEGER NOT NULL,
			project_id INTEGER NOT NULL,
			FOREIGN KEY (room_type_id) REFERENCES room_types (room_type_id),
			FOREIGN KEY (project_id) REFERENCES projects (project_id)
		)
	''')

def create_invoices_table(cur: sqlite3.Cursor) -> None:
	"""Create Invoices Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS invoices (
			invoice_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_id INTEGER NOT NULL,
			created_date TEXT NOT NULL,
			invoice_number TEXT,
			status TEXT DEFAULT 'draft',
			FOREIGN KEY (project_id) REFERENCES projects (project_id)
		)
	''')

def create_time_entries_table(cur: sqlite3.Cursor) -> None:
	"""Create Time_Entries Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS time_entries (
			entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
			project_id INTEGER NOT NULL,
			architect_id INTEGER NOT NULL,
			phase_id INTEGER NOT NULL,
			project_room_id INTEGER NOT NULL,
			start_time TEXT NOT NULL,
			end_time TEXT NOT NULL,
			duration_minutes INTEGER NOT NULL,
			invoice_id INTEGER,
			notes TEXT,
			FOREIGN KEY (project_id) REFERENCES projects (project_id),
			FOREIGN KEY (architect_id) REFERENCES architects (architect_id),
			FOREIGN KEY (phase_id) REFERENCES phases (phase_id),
			FOREIGN KEY (project_room_id) REFERENCES project_rooms (project_room_id),
			FOREIGN KEY (invoice_id) REFERENCES invoices (invoice_id)
		)
	''')
