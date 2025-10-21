from architectsLog_classes import Architect, Project

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
	assert testArchitect.is_active == 1
	assert testArchitect.architect_id == None

#test if the Project class instance is initialized correctly
def test_project_initialization():
	"""Test if the Project class instance is created and __init__() initializes correctly"""
	testProject = Project("NewProject", "NewClient", "123ClientStreet", "01-01-2025")

	assert testProject.project_name == "NewProject"
	assert testProject.client_name == "NewClient"
	assert testProject.client_address == "123ClientStreet"
	assert testProject.start_date == "01-01-2025"
	assert testProject.architect_id == None
	assert testProject.current_phase_id == None
	assert testProject.status == "active"