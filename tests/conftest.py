import sys
from pathlib import Path
import pytest
import os

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from architectsLog_db import get_connection

TEST_DB = 'test_architectsLog.db'

#create a database auto cleanup before and after each test
@pytest.fixture(autouse=True)
def cleanup_test_db():
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

#create a connection for the databases then closes them before each test
@pytest.fixture
def test_conn():
    """Fixture that provides a test connection and cleans up after"""
    conn = get_connection(TEST_DB)
    yield conn
    conn.close()