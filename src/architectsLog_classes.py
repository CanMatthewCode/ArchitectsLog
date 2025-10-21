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

