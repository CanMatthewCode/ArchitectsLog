# main entry pathway into the architects log

import sys

import architectsLog_db
from architectsLog_PySide import MainWindow, initialize_database, deleteEmptyInvoices
from architectsLog_utils import program_loadup

from PySide6.QtWidgets import QApplication


if __name__ == "__main__":
	app = QApplication(sys.argv)
	architectsLog_db.DB_FILE = program_loadup()
	architectsLog_db.sqltable_initialize()
	initialize_database(architectsLog_db.DB_FILE)
	deleteEmptyInvoices()
	window = MainWindow()
	sys.exit(app.exec())
