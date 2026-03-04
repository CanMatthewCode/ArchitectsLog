# Test for architectsLog_analytics_db.py

import pytest
from datetime import datetime

from architectsLog_classes import Architect, Project, TimeEntry

from architectsLog_db import (create_architect_table, create_project_table,
	create_phases_table, create_invoices_table, create_time_entries_table,
	initialize_phases, add_architect, add_project, add_time_entry,)

from architectsLog_analytics_db import (phase_duration_by_project, 
	phase_duration_by_project_with_name, phase_time_entries_by_project, 
	phase_duration_all_projects, total_number_of_projects_by_phase, project_start_date,
	earliest_start_date, project_ids_over_time_period)

@pytest.fixture
def analytics_table_initialize(test_conn):
	cur = test_conn.cursor()
	create_architect_table(cur)
	create_phases_table(cur)
	create_project_table(cur)
	create_invoices_table(cur)
	create_time_entries_table(cur)
	test_conn.commit()

	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890",
		"email@domain.com", "MyCompany")
	architect_id = add_architect(testArchitect, cur)

	initialize_phases(cur)

	#	~~~PROJECTS~~~~
	#project 1 - inside date range
	date1 = datetime.strptime("01-01-2025", "%m-%d-%Y")
	int_date1 = int(date1.timestamp())
	testProject = Project("NewProject", "NewClient", "123 ClientStreet", int_date1)
	project1_id = add_project(testProject, cur)

	#project 2 - inside date range
	date2 = datetime.strptime("02-01-2025", "%m-%d-%Y")
	int_date2 = int(date2.timestamp())
	testProject2 = Project("SecondProject", "SecondClient", "456 ClientStreet", int_date2)
	project2_id = add_project(testProject2, cur)

    #project 3 - outside date range
	date3 = datetime.strptime("01-01-2023", "%m-%d-%Y")
	int_date3 = int(date3.timestamp())
	testProject3 = Project("ThirdProject", "ThirdClient", "789 ClientStreet", int_date3)
	project3_id = add_project(testProject3, cur)

	#	~~~RANGES~~~
	range_start = int(datetime.strptime("01-01-2025", "%m-%d-%Y").timestamp())
	range_end = int(datetime.strptime("12-31-2025", "%m-%d-%Y").timestamp())

	#	~~~TIME ENTRIES~~~
	#project 1, phase 1
	time_entry1_start = int(datetime.strptime("01-15-2025 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry1_end = int(datetime.strptime("01-15-2025 10:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry1 = TimeEntry(time_entry1_start, time_entry1_end, 60, project1_id, 
		architect_id)
	add_time_entry(time_entry1, cur)

	#project 1, phase 1 - outside date range
	time_entry2_start = int(datetime.strptime("02-15-2024 09:00:00",
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry2_end = int(datetime.strptime("02-15-2024 11:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry2 = TimeEntry(time_entry2_start, time_entry2_end, 120,
		project1_id, architect_id)
	add_time_entry(time_entry2, cur)

	#project 1, phase 2
	time_entry3_start = int(datetime.strptime("03-15-2025 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry3_end = int(datetime.strptime("03-15-2025 10:30:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry3 = TimeEntry(time_entry3_start, time_entry3_end, 90, 
		project1_id, architect_id, phase_id=2)
	add_time_entry(time_entry3, cur)

	#project 2, phase 1
	time_entry4_start = int(datetime.strptime("04-15-2025 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry4_end = int(datetime.strptime("04-15-2025 10:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry4 = TimeEntry(time_entry4_start, time_entry4_end, 60, project2_id,
		architect_id)
	add_time_entry(time_entry4, cur)

	#project 2, phase 3 - outside date range
	time_entry5_start = int(datetime.strptime("05-15-2024 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry5_end = int(datetime.strptime("05-15-2024 09:45:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry5 = TimeEntry(time_entry5_start, time_entry5_end, 45, project2_id, 
		architect_id, phase_id=3)
	add_time_entry(time_entry5, cur)

	#project 3, phase 1 - outside date range
	time_entry6_start = int(datetime.strptime("06-15-2023 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry6_end = int(datetime.strptime("06-15-2023 11:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry6 = TimeEntry(time_entry6_start, time_entry6_end, 120, project3_id, 
		architect_id)
	add_time_entry(time_entry6, cur)

	test_conn.commit()

	return {
		'architect': testArchitect,
		'architect_id': architect_id,
		'project1': testProject,
		'project1_id': project1_id,
		'project2': testProject2,
		'project2_id': project2_id,
		'project3': testProject3,
		'project3_id': project3_id,
		'range_start': range_start,
		'range_end': range_end,
	}


def test_phase_duration_by_project_no_time(test_conn, 
	analytics_table_initialize):
	"""Test that all phases with durations are correctly returned"""
	cur = test_conn.cursor()

	project1_id = analytics_table_initialize['project1_id']
	project2_id = analytics_table_initialize['project2_id']
	phases_with_durations = phase_duration_by_project(project1_id, cur)
	phases_with_durations2 = phase_duration_by_project(project2_id, cur)

	assert phases_with_durations[0][0] == 1
	assert phases_with_durations[0][1] == 3.0
	assert phases_with_durations[1][0] == 2
	assert phases_with_durations[1][1] == 1.5
	assert phases_with_durations2[0][0] == 1
	assert phases_with_durations2[0][1] == 1.0
	assert phases_with_durations2[1][0] == 3
	assert phases_with_durations2[1][1] == 0.75

def test_phase_duration_by_project_with_times(test_conn,
	analytics_table_initialize):
	"""Test that only those phase times within range are correctly returned"""
	cur = test_conn.cursor()

	project1_id = analytics_table_initialize['project1_id']
	project2_id = analytics_table_initialize['project2_id']
	project3_id = analytics_table_initialize['project3_id']
	range_start = analytics_table_initialize['range_start']
	range_end = analytics_table_initialize['range_end']

	phases_with_durations = phase_duration_by_project(project1_id, cur, 
		range_start, range_end)
	phases_with_durations2 = phase_duration_by_project(project2_id, cur,
		range_start, range_end)
	phases_with_durations3 = phase_duration_by_project(project3_id, cur,
		range_start, range_end)

	assert phases_with_durations[0][0] == 1
	assert phases_with_durations[0][1] == 1.0
	assert phases_with_durations[1][0] == 2
	assert phases_with_durations[1][1] == 1.5
	assert phases_with_durations2[0][0] == 1
	assert phases_with_durations2[0][1] == 1.0
	assert phases_with_durations3 == []

	with pytest.raises(IndexError):
		phases_with_durations2[1][0]


def test_phase_duration_by_project_with_name_no_time(test_conn, 
	analytics_table_initialize):
	"""Test that only those phase times within range are correctly returned with name"""
	cur = test_conn.cursor()

	project1_id = analytics_table_initialize['project1_id']
	project2_id = analytics_table_initialize['project2_id']
	phases_with_durations = phase_duration_by_project_with_name(project1_id, cur)
	phases_with_durations2 = phase_duration_by_project_with_name(project2_id, cur)

	assert phases_with_durations[0][0] == 1
	assert phases_with_durations[0][1] == 3.0
	assert phases_with_durations[0][2] == 'NewProject'
	assert phases_with_durations[1][0] == 2
	assert phases_with_durations[1][1] == 1.5
	assert phases_with_durations[1][2] == 'NewProject'
	assert phases_with_durations2[0][0] == 1
	assert phases_with_durations2[0][1] == 1.0
	assert phases_with_durations2[0][2] == 'SecondProject'
	assert phases_with_durations2[1][0] == 3
	assert phases_with_durations2[1][1] == 0.75
	assert phases_with_durations2[1][2] == 'SecondProject'

def test_phase_duration_by_project_with_name_with_times(test_conn, 
	analytics_table_initialize):
	"""Test that only those phase times within range are correctly returned with name"""
	cur = test_conn.cursor()

	project1_id = analytics_table_initialize['project1_id']
	project2_id = analytics_table_initialize['project2_id']
	project3_id = analytics_table_initialize['project3_id']
	range_start = analytics_table_initialize['range_start']
	range_end = analytics_table_initialize['range_end']

	phases_with_durations = phase_duration_by_project_with_name(project1_id, cur, 
		range_start, range_end)
	phases_with_durations2 = phase_duration_by_project_with_name(project2_id, cur,
		range_start, range_end)
	phases_with_durations3 = phase_duration_by_project_with_name(project3_id, cur,
		range_start, range_end)

	assert phases_with_durations[0][0] == 1
	assert phases_with_durations[0][1] == 1.0
	assert phases_with_durations[0][2] == 'NewProject'
	assert phases_with_durations[1][0] == 2
	assert phases_with_durations[1][1] == 1.5
	assert phases_with_durations[1][2] == 'NewProject'
	assert phases_with_durations2[0][0] == 1
	assert phases_with_durations2[0][1] == 1.0
	assert phases_with_durations2[0][2] == 'SecondProject'
	assert phases_with_durations3 == []

	with pytest.raises(IndexError):
		phases_with_durations2[1][0]


def test_phase_time_entries_by_project(test_conn, analytics_table_initialize):
	"""Test that all a projects time_entries are returned ordered by start time"""
	cur = test_conn.cursor()

	project1_id = analytics_table_initialize['project1_id']
	project2_id = analytics_table_initialize['project2_id']

	time_entry2_datetime = int(datetime.strptime("02-15-2024 09:00:00",
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry1_datetime = int(datetime.strptime("01-15-2025 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry3_datetime = int(datetime.strptime("03-15-2025 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry4_datetime = int(datetime.strptime("04-15-2025 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())
	time_entry5_datetime = int(datetime.strptime("05-15-2024 09:00:00", 
		"%m-%d-%Y %I:%M:%S").timestamp())

	phases_by_time1 = phase_time_entries_by_project(project1_id, cur)
	phases_by_time2 = phase_time_entries_by_project(project2_id, cur)

	assert phases_by_time1[0][0] == 1
	assert phases_by_time1[0][1] == 120
	assert phases_by_time1[0][2] == time_entry2_datetime
	assert phases_by_time1[1][0] == 1
	assert phases_by_time1[1][1] == 60
	assert phases_by_time1[1][2] == time_entry1_datetime
	assert phases_by_time1[2][0] == 2
	assert phases_by_time1[2][1] == 90
	assert phases_by_time1[2][2] == time_entry3_datetime
	assert phases_by_time2[0][0] == 3
	assert phases_by_time2[0][1] == 45
	assert phases_by_time2[0][2] == time_entry5_datetime
	assert phases_by_time2[1][0] == 1
	assert phases_by_time2[1][1] == 60
	assert phases_by_time2[1][2] == time_entry4_datetime


def test_phase_duration_all_projects_no_time(test_conn,
	analytics_table_initialize):
	"""Test that all phase durations in time_entries table are returned rounded"""
	cur = test_conn.cursor()

	test_data = phase_duration_all_projects(cur)

	assert test_data[0][0] == 1
	assert test_data[0][1] == 6.0
	assert test_data[1][0] == 2
	assert test_data[1][1] == 1.5
	assert test_data[2][0] == 3
	assert test_data[2][1] == 0.75

def test_phase_duration_all_projects_with_time(test_conn,
	analytics_table_initialize):
	"""Test that all phase durations in time_entries table are returned rounded"""
	cur = test_conn.cursor()
	range_start = analytics_table_initialize['range_start']
	range_end = analytics_table_initialize['range_end']

	test_data = phase_duration_all_projects(cur, range_start, range_end)

	assert test_data[0][0] == 1
	assert test_data[0][1] == 2.0
	assert test_data[1][0] == 2
	assert test_data[1][1] == 1.5

	with pytest.raises(IndexError):
		test_data[2][0]


def test_total_number_of_projects_by_phase_no_time(test_conn,
	analytics_table_initialize):
	"""Test that the number of project_ids per phase is returned correctly"""
	cur = test_conn.cursor()

	test_data = total_number_of_projects_by_phase(cur)

	assert test_data[0][0] == 1
	assert test_data[0][1] == 3
	assert test_data[1][0] == 2
	assert test_data[1][1] == 1
	assert test_data[2][0] == 3
	assert test_data[2][1] == 1

def test_total_number_of_projects_by_phase_with_time(test_conn,
	analytics_table_initialize):
	"""Test that the number of project_ids per phase is returned correctly"""
	cur = test_conn.cursor()
	range_start = analytics_table_initialize['range_start']
	range_end = analytics_table_initialize['range_end']

	test_data = total_number_of_projects_by_phase(cur, range_start, range_end)

	assert test_data[0][0] == 1
	assert test_data[0][1] == 2
	assert test_data[1][0] == 2
	assert test_data[1][1] == 1

	with pytest.raises(IndexError):
		test_data[2][0]


def test_project_start_date(test_conn, analytics_table_initialize):
	"""Test that a project_id's start_date is correctly returned"""
	cur = test_conn.cursor()

	project1_id = analytics_table_initialize['project1_id']
	project2_id = analytics_table_initialize['project2_id']

	date1 = datetime.strptime("01-01-2025", "%m-%d-%Y")
	int_date1 = int(date1.timestamp())
	date2 = datetime.strptime("02-01-2025", "%m-%d-%Y")
	int_date2 = int(date2.timestamp())

	proj1_date = project_start_date(project1_id, cur)
	proj2_date = project_start_date(project2_id, cur)

	assert proj1_date[0] == int_date1
	assert proj2_date[0] == int_date2


def test_earliest_start_date(test_conn, analytics_table_initialize):
	"""Test that the earliest project start_date is returned"""
	cur = test_conn.cursor()

	date3 = datetime.strptime('01-01-2023', '%m-%d-%Y')
	int_date3 = int(date3.timestamp())

	earliest_date = earliest_start_date(cur)

	assert earliest_date[0] == int_date3


def test_project_ids_over_time_period(test_conn, analytics_table_initialize):
	"""Test that only projecct_ids and project_names within time period are returned"""
	cur = test_conn.cursor()
	range_start = analytics_table_initialize['range_start']
	range_end = analytics_table_initialize['range_end']

	proj_ids_names = project_ids_over_time_period(range_start, range_end, cur)

	assert proj_ids_names[0][0] == 1
	assert proj_ids_names[0][1] == 'NewProject'
	assert proj_ids_names[1][0] == 2
	assert proj_ids_names[1][1] == 'SecondProject'

	with pytest.raises(IndexError):
		proj_ids_names[2][0]
