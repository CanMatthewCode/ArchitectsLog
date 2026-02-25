# PDF generation function for the Architect's Log

import os
import sqlite3
from datetime import datetime
from fpdf import FPDF
from platformdirs import PlatformDirs
from PySide6.QtWidgets import QFileDialog

from architectsLog_db import load_architect, load_project
from architectsLog_constants import PHASES


def generate_invoice_pdf(invoice_id: int, cur: sqlite3.Cursor) -> None:
	"""Function to retrieve information from architects, projects, and invoices table
	and save an invoice to PDF in user selected location"""
	arch_sql = "SELECT DISTINCT architect_id FROM time_entries WHERE invoice_id = ?"
	cur.execute(arch_sql, (invoice_id,))
	arch_row = cur.fetchone()
	architect_id = arch_row[0]
	architect = load_architect(architect_id, cur)

	proj_sql = "SELECT DISTINCT project_id FROM invoices WHERE invoice_id = ?"
	cur.execute(proj_sql, (invoice_id,))
	proj_row = cur.fetchone()
	project_id = proj_row[0]
	project = load_project(project_id, cur)

	phase_sql = "SELECT DISTINCT phase_id FROM time_entries WHERE invoice_id = ?"
	cur.execute(phase_sql, (invoice_id,))
	phase_row = cur.fetchone()
	phase_id = phase_row[0]
	phase_name = PHASES[phase_id]

	invoice_sql = "SELECT invoice_number FROM invoices WHERE invoice_id = ?"
	cur.execute(invoice_sql, (invoice_id,))
	invoice_row = cur.fetchone()
	invoice_name = invoice_row[0]

	time_entries_sql = "SELECT start_time, duration_minutes, notes \
		FROM time_entries WHERE invoice_id = ?"
	cur.execute(time_entries_sql, (invoice_id,))
	times_rows = cur.fetchall()

	time_entries_strings = []
	for row in times_rows:
		date_time = datetime.fromtimestamp(row[0])
		start_str = date_time.strftime("%m/%d/%Y  %I:%M %p")
		hour = row[1] // 60
		minute = row[1] % 60
		duration_str = (f"{hour:02d}:{minute:02d}")
		note = row[2]
		time_entries_strings.append([start_str, duration_str, note])

	time_sum_sql = "SELECT SUM(duration_minutes) FROM time_entries WHERE invoice_id = ?"
	cur.execute(time_sum_sql, (invoice_id,))
	sum_time_row = cur.fetchone()
	total_mins = sum_time_row[0]
	hour = total_mins // 60
	minute = total_mins % 60
	total_duration_str = f"{hour:02d}:{minute:02d}"

	pdf = FPDF(format="Letter")
	pdf.set_margins(left=25, top=20, right=25)
	pdf.add_page()
	pdf.set_font("helvetica", style="BU", size=28)
	pdf.cell(0, 14, project.project_name, align="C", new_x="LMARGIN", new_y="NEXT")
	pdf.set_font("helvetica", size=12)
	pdf.ln(10)

	pdf.cell(0, 5, architect.name, align="C", new_x="LMARGIN", new_y="NEXT")
	pdf.cell(0, 5, architect.company_name, align="C", new_x="LMARGIN", new_y="NEXT")
	pdf.cell(0, 5, architect.phone_number, align="C", new_x="LMARGIN", new_y="NEXT")
	pdf.cell(0, 5, architect.email, align="C", new_x="LMARGIN", new_y="NEXT")
	license_str = f"Lic Num: {architect.license_number}"
	pdf.cell(0, 5, license_str, align="C", new_x="LMARGIN", new_y="NEXT")
	pdf.ln(10)

	pdf.cell(0, 5, project.client_name, align="L", new_x="LMARGIN", new_y="NEXT")
	client_address = project.client_address.split(",", 1)
	pdf.cell(0, 5, f"{client_address[0]},", new_x="LMARGIN", new_y="NEXT")
	pdf.cell(0, 5, client_address[1].strip(), new_x="LMARGIN", new_y="NEXT")

	pdf.set_font("helvetica", style="B", size=12)
	label_width = pdf.get_string_width("Invoice Number: ")
	pdf.cell(label_width, 5, "Invoice Number: ", new_x="RIGHT", new_y="TOP")
	pdf.set_font("helvetica", size=12)
	pdf.cell(0, 5, invoice_name, new_x="LMARGIN", new_y="NEXT")
	pdf.set_font("helvetica", style="B", size=12)
	label_width = pdf.get_string_width("Invoice Phase: ")
	pdf.cell(label_width, 5, "Invoice Phase: ", new_x="RIGHT", new_y="TOP")
	pdf.set_font("helvetica", size=12)
	pdf.cell(0, 5, phase_name, new_x="LMARGIN", new_y="NEXT")
	pdf.ln(10)

	pdf.set_font("helvetica", style="B", size=12)
	pdf.cell(40, 5, "Start Time", new_x="RIGHT", new_y="TOP")
	pdf.cell(30, 5, "Duration", new_x="RIGHT", new_y="TOP")
	pdf.cell(0, 5, "Notes", new_x="LMARGIN", new_y="NEXT")
	pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
	pdf.set_font("helvetica", size=9)
	for line in time_entries_strings:
		pdf.cell(40, 5, line[0], new_x="RIGHT", new_y="TOP")
		pdf.cell(30, 5, f"     {line[1]}", new_x="RIGHT", new_y="TOP")
		pdf.cell(0, 5, line[2], new_x="LMARGIN", new_y="NEXT")

	pdf.set_font("helvetica", style="B", size=12)
	time_label = "TOTAL TIME:  "
	time_label_width = pdf.get_string_width(time_label)
	pdf.set_font("helvetica", size=12)
	time_value_width = pdf.get_string_width(total_duration_str)
	pdf.set_y(pdf.h - pdf.b_margin - 5)
	pdf.set_x(pdf.w - pdf.r_margin - time_label_width - time_value_width)


	pdf.set_font("helvetica", style="B", size=12)
	pdf.cell(time_label_width, 5, time_label, new_x="RIGHT", new_y="TOP")
	pdf.set_font("helvetica", size=12)
	pdf.cell(time_value_width, 5, total_duration_str, new_x="LMARGIN", new_y="NEXT")

	dirs = PlatformDirs("architectsLog")
	default_path = os.path.join(dirs.user_documents_path, f"{invoice_name}_invoice.pdf")

	file_path, _ = QFileDialog.getSaveFileName(
		None, "Save Invoice as PDF", default_path, "PDF Files (*.pdf)")
	if file_path:
		pdf.output(file_path)
