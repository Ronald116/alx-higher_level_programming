#!/usr/bin/python3
"""
A script that lists all states with a name starting with 'N'
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Connect to database"""
    db_con = MySQLdb.connect(host='localhost', user=argv[1],
                            port=3306, passwd=argv[2], db=argv[3])
    
    cur = db_con.cursor()
    cur.execute("SELECT * FROM states WHERE name like 'N%' \
                ORDER BY states.id ASC")
    desired_states = cur.fetchall()
    for desired_state in desired_states:
        print(desired_state)
cur.close()
db_con.close()
