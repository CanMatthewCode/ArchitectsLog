# main entry pathway into the architects log

import sys

from architectsLog_db import DB_FILE, sqltable_initialize
from architectsLog_PySide import MainWindow, initialize_database

from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
	sqltable_initialize()
	app = QApplication()
	initialize_database(DB_FILE)
	window = MainWindow()
	sys.exit(app.exec())