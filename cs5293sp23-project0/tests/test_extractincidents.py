import pytest
from unittest.mock import MagicMock
from project0 import main
import PyPDF2
@pytest.fixture
def mock_PdfReader(monkeypatch):
    mock_PdfReader = MagicMock()
    monkeypatch.setattr("PyPDF2.PdfReader", mock_PdfReader)
    yield mock_PdfReader

def test_extractincidents(mock_PdfReader):
    # Define expected output
    expected_output = "Date / Time Incident Number Location Nature Incident ORI"
    
    # Set up mock PdfReader object to return a mock page object
    mock_page = MagicMock()
    mock_page.extract_text.return_value = expected_output
    mock_pdf = MagicMock()
    mock_pdf.pages = [mock_page]
    mock_PdfReader.return_value = mock_pdf
    
    # Call the function being tested
    result = main.extractincidents()
    
    # Assert that the expected output was returned
    assert result.startswith(expected_output)


