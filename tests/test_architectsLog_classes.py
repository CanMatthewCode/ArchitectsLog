from architectsLog_classes import Architect

#	~CLASS CREATION AND INITIALIZATION TESTS~~~

#test if the Architect class instance is initialized correctly
def test_architect_initialization():
	"""Test if the Architect class instance is created and __init__() initializes correctly"""
	testArchitect = Architect("Name", "LicenseNumber01", "123-456-7890", "email@domain.com", "MyCompany")

	assert testArchitect.name ==  "Name"
	assert testArchitect.license_number == "LicenseNumber01"
	assert testArchitect.phone_number == "123-456-7890"
	assert testArchitect.email =="email@domain.com"
	assert testArchitect.company_name == "MyCompany"