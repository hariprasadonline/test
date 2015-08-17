'''
Created on Aug 11, 2015

@author: hmadas
'''

import MySQLdb





# Open database connection
db = MySQLdb.connect("localhost","root","admin","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print ("Database version : %s " % data)

# disconnect from server
db.close()