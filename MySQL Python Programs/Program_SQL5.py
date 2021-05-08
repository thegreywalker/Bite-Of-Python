"""
Write a Program to generate a list of tables present in the database you are using currently 
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password",database="mydb")
myCursor = db.cursor()

myCursor.execute("SHOW TABLES")
for x in myCursor:
    print(x)






























