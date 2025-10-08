# Database functions for the Architect's Log

import sqlite3
import os

DB_FILE = 'architectsLog.db'

def get_connection():
	"""Get database connection with foreign keys enabled"""
	conn = sqlite3.connect(DB_FILE)
	conn.execute('PRAGMA foreign_keys = ON;')
	return conn

