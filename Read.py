# Connect to the database
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Retrieve all records from the Registration table
def retrieve_records():
    cursor.execute("SELECT * FROM Registration")
    rows = cursor.fetchall()
    return rows

# Example usage:
records = retrieve_records()
for record in records:
    print(record)

# Close the connection
conn.close()
