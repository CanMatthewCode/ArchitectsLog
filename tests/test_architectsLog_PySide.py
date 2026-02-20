#Testing for architectsLog_PySide.py

import pytest
from architectsLog_PySide import validateDuration

def test_validateDuration_valid_string():
	"""Test to check if string input is correctly validated as minutes"""
	value1 = validateDuration("1:00")
	value2 = validateDuration("73")
	value3 = validateDuration(":23")
	value4 = validateDuration("2:03")

	assert value1 == 60
	assert value2 == 75
	assert value3 == 30
	assert value4 == 135

def test_validateDuration_invalid_string():
	with pytest.raises(ValueError):
		validateDuration("2:30:32")

	with pytest.raises(ValueError):
		validateDuration("Test")