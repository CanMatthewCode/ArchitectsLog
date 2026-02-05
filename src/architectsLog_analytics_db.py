# Database functions for Architect's Log analytics

import sqlite3

def phase_duration_by_project(project_id: int, cur: sqlite3.Cursor) -> list[tuple[int]]:
	"""Method to retrieve the summation of a project's phase duration,
	returns a list of tuples containing (phase_id ints, sum duration ints)"""
	sql = "SELECT phase_id, ROUND(SUM(duration_minutes)/60.0, 2) FROM time_entries\
		WHERE project_id = ? \
		GROUP BY phase_id \
		ORDER BY phase_id ASC"
	cur.execute(sql, (project_id,))
	return cur.fetchall()