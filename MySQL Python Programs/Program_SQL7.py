"""
Write a Program to Update any column of a Particular Student in the table used in the files before 
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password", database="mydb")
myCursor = db.cursor()

myCursor.execute("UPDATE table1 SET sec='A' WHERE name='Apurba Ghosh'")
db.commit()
myCursor.execute("SELECT * FROM table1")
for x in myCursor:
    print(x)


















