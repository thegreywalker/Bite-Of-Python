"""
Write a Program to show all the records present in the table you are using 
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password",database="mydb")
myCursor = db.cursor()

myCursor.execute("SELECT * FROM table1")
for x in myCursor:
    print(x)






















