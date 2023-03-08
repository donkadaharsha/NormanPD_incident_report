import sqlite3

def test_sorted_incidents():
    conn = sqlite3.connect('incident_report.db')
    cursor = conn.cursor()
    cursor.execute("SELECT Nature_Incident, COUNT(*) FROM incident_report GROUP BY Nature_Incident ORDER BY COUNT(*) DESC, Nature_Incident")
    result = cursor.fetchall()
    assert len(result) > 0, "No results found in the database."
    prev_count = result[0][1] + 1 # to ensure that first count is greater than prev_count
    for row in result:
        count = row[1]
        assert count <= prev_count, f"Counts not sorted in descending order: {prev_count} should be greater than {count}."
        prev_count = count
    conn.close()

