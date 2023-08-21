#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """connec to database"""
    db_con = MySQLdb.connect(host='localhost', user=argv[1],
                             passwd=argv[2], db=argv[3], port=3306)
    
    cur = db_con.cursor()
    cur.execute("""SELECT cities.id, cities.name FROM cities JOIN states ON 
                cities.state_id = states.id WHERE states.name LIKE 
                BINARY %(name)s ORDER BY cities.id ASC""",{'name': argv[4]})
    results = cur.fetchall()
    
    if results != None:
        print(", ".join([result[1] for result in results]))

cur.close()
db_con.close()
