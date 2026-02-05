# Database functions for Architect's Log analytics

import sqlite3

def phase_duration_by_project(project_id: int, 
	cur: sqlite3.Cursor) -> list[tuple[int, int]]:
	"""Retrieve the summation of a project's phase duration,
	returns a list of tuples containing (phase_id, sum duration_minutes)"""
	sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2) FROM time_entries\
		WHERE project_id = ? \
		GROUP BY phase_id \
		ORDER BY phase_id ASC"
	cur.execute(sql, (project_id,))
	return cur.fetchall()

def phase_time_entries_by_project(project_id: int, 
	cur: sqlite3.Cursor) -> list[tuple[int, int, int]]:
	"""Retrieve all of a project_id's time_entries duration_minutes with each 
	corresponding phase_id and start_times. 
	Returns a list of tuples containing (phase_id, duration_minutes, start_time)"""
	sql = "SELECT phase_id, duration_minutes, start_time \
		FROM time_entries \
		WHERE project_id = ? \
		ORDER BY start_time ASC"
	cur.execute(sql, (project_id,))
	return cur.fetchall()