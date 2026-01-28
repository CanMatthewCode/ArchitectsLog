# main entry pathway into the architects log

import sys

from architectsLog_db import DB_FILE, sqltable_initialize
from architectsLog_PySide import MainWindow, initialize_database, deleteEmptyInvoices

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
	sqltable_initialize()
	app = QApplication()
	initialize_database(DB_FILE)
	deleteEmptyInvoices()
	window = MainWindow()
	sys.exit(app.exec())