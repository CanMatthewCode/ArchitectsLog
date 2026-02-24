# program load, new database, load database functionality

import os
import sys
import shutil
import json
from platformdirs import PlatformDirs
from datetime import datetime
from PySide6.QtWidgets import QFileDialog

import architectsLog_db

def program_loadup() -> str:
	dirs = PlatformDirs("ArchitectsLog", ensure_exists=True)
	settings_path = dirs.user_config_path / "settings.json"
	data_dir = dirs.user_data_path
	DB_FILE = ""
	if not settings_path.exists():
		log_name = "demo_ArchitectsLog.db"
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

def new_database() -> None:
	dirs = PlatformDirs("ArchitectsLog", ensure_exists=True)
	settings_path = dirs.user_config_path / "settings.json"
	data_dir = dirs.user_data_path
	if os.path.basename(architectsLog_db.DB_FILE) == 'architectsLog.db':
		YYYYMMDD = datetime.now().strftime('%Y%m%d')
		os.rename(architectsLog_db.DB_FILE, os.path.join(
			data_dir, "architectsLog_old_" + YYYYMMDD + ".db"))
		architectsLog_db.DB_FILE = os.path.join(data_dir, "architectsLog.db")
		architectsLog_db.sqltable_initialize()
	else:
		os.remove(architectsLog_db.DB_FILE)
		settings_dict = {"db_name" : "architectsLog.db"}
		with open(settings_path, "w") as file:
			json.dump(settings_dict, file)
		architectsLog_db.DB_FILE = os.path.join(data_dir, "architectsLog.db")
		architectsLog_db.sqltable_initialize()
	os.execv(sys.executable, [sys.executable] + sys.argv)

def load_database() -> None:
	dirs = PlatformDirs("ArchitectsLog", ensure_exists=True)
	data_dir = dirs.user_data_path
	returned_database, _ = QFileDialog.getOpenFileName(None, "Select a Database", 
		str(data_dir), "Database Files (*.db)")
	if returned_database:
		if os.path.basename(returned_database) in ("architectsLog.db", 
			"demo_ArchitectsLog.db"):
			return
		else:
			YYYYMMDD = datetime.now().strftime('%Y%m%d')
			os.rename(architectsLog_db.DB_FILE, os.path.join(
				data_dir, "architectsLog_old_" + YYYYMMDD + ".db"))
			os.rename(returned_database, os.path.join(data_dir, "architectsLog.db"))
			os.execv(sys.executable, [sys.executable] + sys.argv)
