#!/usr/bin/python3
"""
This script lists all states from the database `hbtn_0e_0_usa`.

This script connects to a MySQL database and retrieves a list of all states
from the 'states' table in the 'hbtn_0e_0_usa' database. It requires the
following command-line arguments: username, password, and database name.

Usage:
    ./script.py <username> <password> <database_name>
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    """
    Connect to the database and retrieve the states.

    This function connects to the MySQL database using the provided
    credentials and retrieves all the rows from the 'states' table. It then
    prints each row to the console.
    """
    db_connect = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    db_cursor = db_connect.cursor()

    db_cursor.execute("SELECT * FROM states")

    rows_selected = db_cursor.fetchall()

    for row in rows_selected:
        print(row)

