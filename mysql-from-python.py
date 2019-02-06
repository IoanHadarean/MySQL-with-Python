import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host = 'localhost',
                            user = username,
                            password = '',
                            db='Chinook')
                            
try:
    #Run a query
    with connection.cursor() as cursor:
        rows = [("Bob", 22, "1997-02-06 23:04:56"),
              ("Jim", 56, "1963-05-09 13:12:45"),
              ("Fred", 100, "1919-09-12 01:01:01")]
        cursor.executemany("INSERT INTO Friends VALUES (%s, %s, %s);", rows)
        connection.commit();
finally:
    # Close the connection, regardless of whether the 
    # above was successful
    connection.close()
    