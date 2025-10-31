#Constants for the Architect's Log

#All possible phases eachg project will go through
PHASES = {
	1: "Schematic Design", 
	2: "Design Development", 
	3: "Construction Documents", 
	4: "Bidding Negotiation", 
	5: "Construction Administration",
	6: "Interior Design",
	7: "Add Service",
	8: "Business Development",
	9: "Administration"
	}

#Possible architect statuses
ARCHITECT_STATUSES = ('active', 'inactive')


#tuples of all updatable columns per table
UPDATABLE_ARCHITECTS_COLUMNS = (
	"name", 
	"license_number",
	"phone_number",
	"email",
	"company_name",
	"status"
	)

UPDATABLE_PROJECTS_COLUMNS = (
	"project_name",
	"client_name",
	"client_address",
	"start_date",
	"current_phase_id",
	"status"
	)

UPDATABLE_INVOICES_COLUMNS = (
	"created_date",
	"invoice_number",
	"status"
	)

UPDATABLE_TIME_ENTRIES_COLUMNS = (
	"project_id",
	"architect_id",
	"phase_id",
	"start_time",
	"end_time",
	"duration_minutes",
	"notes",
	"invoice_id"
	)