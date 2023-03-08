import argparse
import requests
from PyPDF2 import PdfReader
import codecs
import io 
import sqlite3
import urllib.request
import string
import re
def main(url):
    # Download data
    incident_data = fetchincidents(url)

    # Extract data
    incidents=extractincidents()
	
    # Create new database
    db,conn = createdb()
	
    # Insert data
    populatedb(db, conn, incidents)
	
    # Print incident counts
    status(db,conn)

#Function to store the URL pdf file in filename 'incident_report.pdf'
def fetchincidents(url):

    filename = 'incident_report.pdf'
    urllib.request.urlretrieve(url, filename)

#Function to extract the text contents from pdf using PDFreader and return text
def extractincidents():
    filename = 'incident_report.pdf'
    with open(filename, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
            text=re.sub(' \n',' ',text)
    return text

#Function to create the DB and create a new table with pdf columnn names as the table contents        
def createdb():
    conn = sqlite3.connect('incident_report.db')
    c = conn.cursor()
    c.execute('''DROP TABLE IF EXISTS incident_report''')
    c.execute('''CREATE TABLE IF NOT EXISTS incident_report
             (Date_Time text, Incident_Number text, Location text, Nature_Incident text, ORI text)''')
    return c,conn

#Function to populate database table with the text which returned from extractincidents function
def populatedb(c, conn, text):
    lines = text.split('\n')
    lines.remove('Date / Time Incident Number Location Nature Incident ORI')
    #separating the columns according to their index
    for line in lines:
        data = line.split()
        if len(data) >= 5:
            date_time = data[0] + ' ' + data[1]
            incident_number = data[2]
            i=-2
            #Address and Nature can be differentiated by the case of letters lower or upper to seperate accordigly line by line and insert it in db
            while(data[i][-1].islower()):
                i=i-1
            location=' '.join(data[3:i])
            nature_incident=' '.join(data[i+1:-1])
            ori = data[-1]
            incident = (date_time, incident_number, location, nature_incident, ori)
            c.execute("INSERT INTO incident_report VALUES (?,?,?,?,?)", incident)
    conn.commit()
   # rows=conn.execute('SELECT * FROM incident_report').fetchall()
   # for row in rows:
    #    print(row)

#Function to take count of each nature and list them in sorted order by count and then alphabetical order.
def status(db,conn):
    sorted_incident=db.execute("SELECT Nature_Incident, COUNT(*) FROM incident_report GROUP BY Nature_Incident ORDER BY COUNT(*) DESC, Nature_Incident")
    for i in sorted_incident:
        print(i[0], "|", i[1])

    conn.close()
    
if  __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--incidents", type=str, required=True, 
                help="Incident summary url.")
     
    args = parser.parse_args()
    if args.incidents:
        main(args.incidents)

