"""
Write a code to create a database in MySQL
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password")
myCursor = db.cursor()

# myCursor.execute("CREATE DATABASE mydb")
myCursor.execute("SHOW DATABASES")
for x in myCursor:
    print(x)



















