import sqlite3

# Connect to the SQLite database (creates a new database if not exists)
conn = sqlite3.connect('registration.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Define the CREATE TABLE SQL command
create_table_sql = '''
    CREATE TABLE IF NOT EXISTS Registration (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Name TEXT NOT NULL,
        Email TEXT NOT NULL,
        DateOfBirth DATE
    )
'''


cursor.execute(create_table_sql)


def create_record(name, email, dob):
    insert_sql = "INSERT INTO Registration (Name, Email, DateOfBirth) VALUES (?, ?, ?)"
    cursor.execute(insert_sql, (name, email, dob))
    conn.commit()

# Example usage:
create_record('pratiksha kavthale', 'pratiksha123@gmail.com', '2002-04-25')

# Close the connection
conn.close()
