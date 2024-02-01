import sqlite3
from sqlite3 import Error
from datetime import datetime

# Function to create a database connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
    return conn

# Function to create a new registration
def create_registration(conn, registration):
    sql = ''' INSERT INTO Registration(Name, Email, DateOfBirth,department)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, registration)
    conn.commit()
    return cur.lastrowid

# Function to retrieve registrations
def retrieve_registrations(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM Registration")
    rows = cur.fetchall()
    for row in rows:
        print(row)

# Function to update registration details
def update_registration(conn, registration):
    sql = ''' UPDATE Registration
              SET Name = ? ,
                  Email = ? ,
                  DateOfBirth = ?
		  Department=?
              WHERE ID = ?'''
    cur = conn.cursor()
    cur.execute(sql, registration)
    conn.commit()

# Function to delete a registration
def delete_registration(conn, id):
    sql = 'DELETE FROM Registration WHERE ID=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def main():
    database = r"registration.db"
    conn = create_connection(database)
    
    with conn:
        # Create a new registration
        registration_1 = ('Pratiksha kavthale', 'pratikshaqkavthale123@gmail.com', '2002-04-25','ENTC')
        registration_id_1 = create_registration(conn, registration_1)
        print("New registration ID:", registration_id_1)

        # Retrieve registrations
        print("Registrations:")
        retrieve_registrations(conn)

        # Update a registration
        update_registration(conn, ('Aiswarya Basude', 'Aiswarya123@gmail.com', '2005-04-17','ENTC', registration_id_1))
        print("Updated registration:")
        retrieve_registrations(conn)

        # Delete a registration
        delete_registration(conn, registration_id_1)
        print("Registration deleted:")
        retrieve_registrations(conn)

if __name__ == '__main__':
    main()
