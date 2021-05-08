"""
Write a Program to Create five tables in the Database created in previous file 
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password", database="mydb")
myCursor = db.cursor()

Q1 = "CREATE TABLE table1(name VARCHAR(50), class int(5), sec VARCHAR(5))"
Q2 = "CREATE TABLE table2(name VARCHAR(50), class int(5), sec VARCHAR(5))"
Q3 = "CREATE TABLE table3(name VARCHAR(50), class int(5), sec VARCHAR(5))"
Q4 = "CREATE TABLE table4(name VARCHAR(50), class int(5), sec VARCHAR(5))"
Q5 = "CREATE TABLE table5(name VARCHAR(50), class int(5), sec VARCHAR(5))"
myCursor.execute(Q1)
myCursor.execute(Q2)
myCursor.execute(Q3)
myCursor.execute(Q4)
myCursor.execute(Q5)
db.commit()

myCursor.execute("SHOW TABLES")
for x in myCursor:
    print(x)
























