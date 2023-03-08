import sqlite3
import pytest
from project0 import main
@pytest.fixture
def db():
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE incident_report
             (Date_Time text, Incident_Number text, Location text, Nature_Incident text, ORI text)''')
    yield conn
    conn.close()

def test_createdb(db):
    c = db.cursor()
    c.execute('SELECT name FROM sqlite_master WHERE type="table" AND name="incident_report"')
    assert c.fetchone()[0] == 'incident_report'

