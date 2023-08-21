#!/usr/bin/python3
"""
Write a script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connect to the database"""
    db_con = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                            passwd=argv[2], db=argv[3])
    cur = db_con.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
        JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    results = cur.fetchall()
    for result in results:
        print(result)
cur.close()
db_con.close()
