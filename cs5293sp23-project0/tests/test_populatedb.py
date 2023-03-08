import pytest
import sqlite3
from project0 import main

def test_populatedb():
    # Set up a temporary in-memory database for testing
    conn = sqlite3.connect(':memory:')
    c = conn.cursor()
    c.execute('''CREATE TABLE incident_report
                 (date_time TEXT, incident_number TEXT, location TEXT, nature_incident TEXT, ori TEXT)''')
    
    # Define test data
    text = "Date / Time Incident Number Location Nature Incident ORI\n" \
           "2/1/2023 0:01 2023-00002060 3300 HEALTHPLEX PKWY Transfer/Interfacility EMSSTAT\n" \
           "2/1/2023 0:17 2023-00002068 3300 HEALTHPLEX PKWY Transfer/Interfacility EMSSTAT\n"
           
    # Call the function being tested
    main.populatedb(c, conn, text)
    
    # Assert that the database was populated correctly
    expected_output = [('2/1/2023 0:01', '2023-00002060', '3300 HEALTHPLEX', 'Transfer/Interfacility', 'EMSSTAT'),
                       ('2/1/2023 0:17', '2023-00002068', '3300 HEALTHPLEX', 'Transfer/Interfacility', 'EMSSTAT')]
    assert c.execute('SELECT * FROM incident_report').fetchall() == expected_output

