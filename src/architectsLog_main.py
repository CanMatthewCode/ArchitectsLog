# main entry pathway into the architects log

import sys
import os
import shutil
import json
from platformdirs import PlatformDirs

import architectsLog_db
from architectsLog_PySide import MainWindow, initialize_database, deleteEmptyInvoices

from PySide6.QtWidgets import QApplication


def program_loadup() -> str:
	dirs = PlatformDirs("ArchitectsLog", ensure_exists=True)
	settings_path = dirs.user_config_path / "settings.json"
	data_dir = dirs.user_data_path
	DB_FILE = ""
	if not settings_path.exists():
		log_name = "demo_architectsLog.db"
		basedir = os.path.dirname(os.path.abspath(__file__))
		DB_FILE = os.path.join(basedir, log_name)
		shutil.copy2(DB_FILE, data_dir)
		settings_dict = {"db_name" : "demo_ArchitectsLog.db"}
		with open(settings_path, "w") as file:
			json.dump(settings_dict, file)
		DB_FILE = os.path.join(data_dir, log_name)
	else:
		with open(settings_path) as file:
			settings = json.load(file)
		log_name = settings['db_name']
		DB_FILE = os.path.join(data_dir, log_name)
	return DB_FILE


if __name__ == "__main__":
	architectsLog_db.DB_FILE = program_loadup()
	architectsLog_db.sqltable_initialize()
	app = QApplication()
	initialize_database(architectsLog_db.DB_FILE)
	deleteEmptyInvoices()
	window = MainWindow()
	sys.exit(app.exec())