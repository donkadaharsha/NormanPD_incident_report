import pytest
import os.path
from project0 import main

@pytest.fixture
def url():
    return "https://www.normanok.gov/sites/default/files/documents/2023-01/2023-01-02_daily_incident_summary.pdf"

def test_fetchincidents(url):
    filename = "incident_report.pdf"
    main.fetchincidents(url)
    assert os.path.exists(filename)

