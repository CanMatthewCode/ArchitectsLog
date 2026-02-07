# Database functions for Architect's Log analytics

import sqlite3
from typing import Optional

def phase_duration_by_project(project_id: int, cur: sqlite3.Cursor, 
	start_date: Optional[int] = None, 
	end_date: Optional[int] = None) -> list[tuple[int, int]]:
	"""Retrieve the summation of all of a project's per phase duration,
	returns a list of tuples containing (phase_id, sum duration_minutes) per phase"""
	if start_date and end_date:
		sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2) FROM time_entries \
			WHERE project_id = ? AND start_time >= ? AND start_time <= ?\
			GROUP BY phase_id \
			ORDER BY phase_id ASC"
		cur.execute(sql, (project_id,start_date, end_date))
	else:
		sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2) FROM time_entries \
			WHERE project_id = ? \
			GROUP BY phase_id \
			ORDER BY phase_id ASC"
		cur.execute(sql, (project_id,))
	return cur.fetchall()

def phase_duration_by_project_with_name(project_id: int, 
	cur: sqlite3.Cursor) -> list[tuple[int, int, str]]:
	"""Retrieve the summation of all of a project's per phase duration,
	returns a list of tuples containing (phase_id, sum duration_minutes, project_name) 
	per phase"""
	sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2), projects.project_name \
		FROM time_entries\
		INNER JOIN projects ON time_entries.project_id = projects.project_id\
		WHERE time_entries.project_id = ? \
		GROUP BY phase_id \
		ORDER BY phase_id ASC"
	cur.execute(sql, (project_id,))
	return cur.fetchall()

def phase_time_entries_by_project(project_id: int, 
	cur: sqlite3.Cursor) -> list[tuple[int, int, int]]:
	"""Retrieve all of a project_id's time_entries duration_minutes with each 
	corresponding phase_id and start_times. Returns a list of tuples 
	containing (phase_id, duration_minutes, start_time) per phase"""
	sql = "SELECT phase_id, duration_minutes, start_time \
		FROM time_entries \
		WHERE project_id = ? \
		ORDER BY start_time ASC"
	cur.execute(sql, (project_id,))
	return cur.fetchall()

def phase_duration_all_projects( cur: sqlite3.Cursor, start_date: Optional[int] = None,
	end_date: Optional[int] = None) -> list[tuple[int, int]]:
	"""Retrieve a summation of all your projects' phase duration + business dev & admin,
	within a passed in time constraint (as integers), returns a list of tuples containing 
	(phase_id, sum duration_minutes) per phase"""
	if start_date and end_date: 
		sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2) FROM time_entries \
		WHERE start_time >= ? AND start_time <= ? \
		GROUP BY phase_id ORDER BY phase_id ASC"
		cur.execute(sql, (start_date, end_date))
	else:
		sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2) FROM time_entries \
		GROUP BY phase_id ORDER BY phase_id ASC"
		cur.execute(sql)
	return cur.fetchall()

def total_number_of_projects_by_phase(cur:sqlite3.Cursor) -> list[tuple[int, int]]:
	"""Retrieve the total number of project_ids per phase in the time_entries table"""
	cur.execute("SELECT phase_id, COUNT(DISTINCT project_id) FROM time_entries\
		GROUP BY phase_id ORDER BY phase_id ASC")
	return cur.fetchall()

def project_start_date(project_id: int, cur:sqlite3.Cursor) -> int:
	"""Retrieve a project_id's start_date as an integer"""
	sql = "SELECT start_time FROM projects WHERE project_id = ?"
	cur.execute(sql, (project_id,))
	return cur.fetchone()

def project_ids_over_time_period(start_date: int, end_date: int, 
	cur:sqlite3.Cursor) -> list[int]:
	"""Retrieve all project_ids within a time frame"""
	sql = "SELECT DISTINCT project_id FROM time_entries \
		WHERE start_time >= ? AND start_time <= ? \
		ORDER BY project_id ASC"
	cur.execute(sql, (start_date, end_date))
	return cur.fetchall()
	