## CS5293sp23 – Project0

## Name: Harsha Vardhan

## PROJECT DESCRIPTION:
The Norman Police Department offers several reports that showcase both its departmental activities and crime data. In this project, we will input any incident pdf url from the website 'https://www.normanok.gov/public-safety/police-department/crime-prevention-data/department-activity-reports' and extract the pdf file data to a list. Then we will create sqllite3 database and insert the list data into the database table. After creation and insertion of data, we will write a query to output Nature of the incidents, sorted by their count and in alphabetical order. All the code and test functions are written using Python and python libraries. 

## How to install
Installation of pipenv : sudo -H pip install -U pipenv 
Installation of Python Packaging : sudo pip3 install --user --editable
Installation of requests: sudo pipenv install requests
Installation of urllib: sudo pipenv install urllib
Installation of PyPDF2: sudo pipenv install PyPDF2
Installation of pytest: sudo pipenv install pytest

## How to run
Run the program:
pipenv run python project0/main.py --incidents <url>

Run the pytests: 
pipenv run python -m pytest

https://user-images.githubusercontent.com/114453047/223617011-9b61472e-a217-498c-8dbd-acc222a862fb.mp4


## FUNCTIONS

fetchincidents(url)
This function takes the URL as input and stores the pdf file which is in URL in a filename 'inicident_report.pdf'.


extractincidents()
This function extracts the text contents from pdf using PDFReader library and returns the text.


createdb()
In this we create sqllitet3 database- 'incident_report.db' and a new table 'incident_report'  is created with PDF column names as the table contents which are : Data/Time, Incident Number, Location, Incident Nature and ORI.


populatedb(db,conn,text)
In this function, we populate the database with the text which is returned from extractincidents function and takes input db, db connection and incidents text. 
This function reads text data line by line using line split  and then seperates each column in the pdf. Splitting column is done according to the index number. While Date/Time and incident number have fixed index numbers, I used lower case and upper case letters of the Location and Nature to differentiate between them as size of location and nature is not fixed.   
Simaltaneously after each row's columns split, row data is inserted in the database table - incident_report with help of sql queries.


status(db,conn)

In this function, the database and db connection is taken as input. SQL query is written to meet the final requirement of the project, which is to count the incident nature and print them in sorted manner by count and alphabetically, seperated with '|'.
This will return the final output which is each nature | count, sorted in order of count(descending) and alphabetically ascending.

# Pytest Functions

test_fetchincidents(url)
In this method, we use assert os.path.exists(). This method in Python is used to check whether the specified path exists or not. So using this we check if pdf is extracted from the url and stored in our os. 

test_extractincidents()
In this test method, @pytest.fixture decorator is used to create a fixture called mock_PdfReader. It is used to create a mock PdfReader object. The monkeypatch argument is used to change the behavior of the PdfReader module during the test. It first defines an expected output which is a string "Date / Time Incident Number Location Nature Incident ORI" and then matches with the extracted text if it starts with the expected output.

test_createdb()
This pytest runs a pytest fixture and created an SQLLite Database in-memory. It ensures that incident_report table is created correctly.

test_populatedb()
This pytest stores the first two rows of the pdf content as the expected output and matches it with database table content. If the data in db table matches with expected output, it will run successfully.


test_status()
This pytest checks that the SQL query returns results and that the counts are sorted in descending order.

## Database Development
I created two functions - createdb() and populatedb().  
In createdb(), a  sqllite3 database is created, named it - 'incident_report.db'. c=conn.cursor() creates a cursor object c that allows you to interact with a database using a Connection object conn. Then, created a table using sql query with with PDF column names as the table contents which are : Data/Time, Incident Number, Location, Incident Nature and ORI.
In populatedb(), I inserted the rows of the pdf text contents using INSERT query in the table incident_report. After the insertion, I close the db connection using conn.close()to free up the memory used for the connection.

## Bugs

- There are few fields containing multiple lines such as location. My code is not able to detect the multiple lines row correctly. Though it is detecing for few rows, it is not detecting multiple lines of some fields.
- In the installation of any library, I have to use sudo(root) for installation or else it is not installing successfully. 

## Assumptions

- Date is not sperated by a space, Time is not seperated by any space, same with Incident number and  ORI. So their indexes are  :  0, 1, 2 and -1 respectively.
- Location of an incident and nature have one or multiple spaces. So to detect their indexes, we assume location  does not end with a lower case. 
