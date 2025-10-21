# Classes and Methods for the Architect's Log


class Architect:
	def __init__(self, name, license_number, phone_number, email, company_name, is_active = 1, architect_id = None):
		self.architect_id = architect_id
		self.name = name
		self.license_number = license_number
		self.phone_number = phone_number
		self.email = email
		self.company_name = company_name
		self.is_active = is_active


class Project:
	def __init__(self, project_name, client_name, client_address, start_date, architect_id = None, current_phase_id = None, status = "active"):
		self.project_name = project_name
		self.client_name = client_name
		self.client_address = client_address
		self.start_date = start_date
		self.architect_id = architect_id
		self.current_phase_id = current_phase_id
		self.status = status

