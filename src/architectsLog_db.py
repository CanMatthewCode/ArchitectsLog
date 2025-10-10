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
			status TEXT DEFAULT 'active',
			FOREIGN KEY (architect_id) REFERENCES architects (architect_id)
		)
	''')

def create_phases_table(cur: sqlite3.Cursor) -> None:
	"""Create Phases Table"""
	cur.execute('''
		CREATE TABLE IF NOT EXISTS phases (
			phase_id INTEGER PRIMARY KEY AUTOINCREMENT,
			room_phase TEXT NOT NULL,
			phase_order INTEGER NOT NULL
		)
	''')