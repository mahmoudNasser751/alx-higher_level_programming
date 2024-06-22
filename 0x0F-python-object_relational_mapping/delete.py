#!/usr/bin/python3

import MySQLdb as db
from sys import argv

if __name__ == '__main__':

    # Establish database connection
    db_connect = db.connect(host="localhost", port=3306,
                            user=argv[1], passwd=argv[2], db=argv[3])
    
    db_cursor = db_connect.cursor()

    # Prepare SQL statement with parameterized query
    delete_query = "DELETE FROM states WHERE id = %s"
    state_id = argv[4]

    # Execute the delete query with the state_id parameter
    db_cursor.execute(delete_query, (state_id,))

    # Commit the transaction (assuming autocommit is not enabled)
    db_connect.commit()

    # Print feedback or confirmation
    print(f"Deleted state with id: {state_id}")

    # Close cursor and connection
    db_cursor.close()
    db_connect.close()

