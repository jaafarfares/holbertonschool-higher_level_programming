#!/usr/bin/python3
""" Write a script that lists all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ now lets connect to the database"""
    db = MySQLdb.connect(
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    """ i didnt assgin the *host value and the *port value in the arguments
    cuz they will be ther bye default """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    result = cursor.fetchall()
    for i in result:
        if i[1][0] == "N":
            """ lets loop through the states and print the once
            that starts with *N """
            print(i)
    cursor.close()
    """ we have to close the cursor"""
    db.close()
    """ and finally close the database"""
