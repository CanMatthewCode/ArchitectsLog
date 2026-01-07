# Classes and Methods for the Architect's Log

from __future__ import annotations


class Architect:
	def __init__(self, name: str, license_number: str, phone_number: str, email: str,
		company_name: str, status: str = "Active", architect_id: int = None) -> None:
		self.architect_id = architect_id
		self.name = name
		self.license_number = license_number
		self.phone_number = phone_number
		self.email = email
		self.company_name = company_name
		self.status = status


class Project:
	def __init__(self, project_name: str, client_name: str, client_address: str, start_date: str,
		current_phase_id: int = 1, status: str = "Active", project_id: int = None) -> None:
		self.project_name = project_name
		self.client_name = client_name
		self.client_address = client_address
		self.start_date = start_date
		self.current_phase_id = current_phase_id
		self.status = status
		self.project_id = project_id


class Invoice:
	def __init__(self, invoice_number: int, created_date: int, project: Project = None,
		status: str = "Draft", invoice_id: int = None) -> None:
		self.invoice_number = invoice_number
		self.created_date = created_date
		self.project = project
		self.status = status
		self.invoice_id = invoice_id


class TimeEntry:
	def __init__(self, start_time: int, duration_minutes: int, 
		project_id: int = None, architect_id: int = None, phase_id: int = 1, 
		notes: str = None, invoice_id: int = None, time_entry_id: int = None,) -> None:
		self.start_time = start_time
		self.duration_minutes = duration_minutes
		self.project_id = project_id
		self.architect_id = architect_id
		self.phase_id = phase_id
		self.notes = notes
		self.invoice_id = invoice_id
		self.time_entry_id = time_entry_id
		