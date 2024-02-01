# Connect to the database
conn = sqlite3.connect('registration.db')
cursor = conn.cursor()

# Update an existing record in the Registration table
def update_record(record_id, new_email):
    update_sql = "UPDATE Registration SET Email = ? WHERE ID = ?"
    cursor.execute(update_sql, (new_email, record_id))
    conn.commit()

# Example usage:
update_record(1, 'pratiksha12345@gmail.com')

# Close the connection
conn.close()
