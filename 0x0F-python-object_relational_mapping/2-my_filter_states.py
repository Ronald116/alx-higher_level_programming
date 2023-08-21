#!/usr/bin/python3
"""
A script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connec to the database"""
    db_con = MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
            port=3306, db=argv[3])
    
    cur = db_con.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' \
        ORDER BY states.id ASC".format(argv[4]))
    desired_names = cur.fetchall()
    
    for desired_name in desired_names:
        print(desired_name)
cur.close()
db_con.close()
