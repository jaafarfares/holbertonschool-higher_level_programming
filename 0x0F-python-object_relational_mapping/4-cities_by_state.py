#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_4_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ now lets connect to the database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    """ i didnt declare the *host and the *port arguments
    cuz they will be ther bye default """
cursor = db.cursor()
cursor.execute(
    "SELECT cities.id, cities.name, states.name FROM cities" +
    " INNER JOIN states ON cities.state_id = states.id ORDER BY cities.id ")
""" we only select cities id first and then cities name and states names"""
result = cursor.fetchall()
for i in result:
    """ lets loop through the states"""
    print(i)
cursor.close()
""" we have to close the cursor"""
db.close()
""" and finally close the database"""
