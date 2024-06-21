#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import db

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[1], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cu.close()
    db.close()
