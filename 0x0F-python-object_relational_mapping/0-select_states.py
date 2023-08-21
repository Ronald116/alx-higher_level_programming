#!/bin/bash/python3
"""
Write a script that lists all states from the database hbtn_0e_0_usa
Args:
        1. mysql username
        2. mysql password
        3. database name
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by states.id
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    """Connect to database"""
    
    db_conn = MySQLdb.connect(host='localhost', user=argv[1],
                            port=3306, passwd=argv[2], db=argv[3])
    
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM states')
    states_selected = cur.fetchall()
    for state in states_selected:
        print(state)
cur.close()
db_conn.close()


