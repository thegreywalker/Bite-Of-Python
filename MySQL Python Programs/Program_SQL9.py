"""
Write a Program to add 5 more users in the table where it contains the data of
name, class, sec, percentages, roll_num. 
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password", database="mydb")
myCursor = db.cursor()

userData = [
    ("Shovan Das",12,'F','71.5%',8),
    ("Shreyashi Halder",12,'A','85%',2),
    ("Debabrata Patikar",12,'B','98.5%',1),
    ("Sangram Sarkar",10,'A','74.5%',7),
    ("Subhajit De",9,'E','95%',10)
]

Q1 = "INSERT INTO table1 (name,class,sec,percentages,roll_num) VALUES(%s,%s,%s,%s,%s)"
for x in userData:
    myCursor.execute(Q1,x)
db.commit()

myCursor.execute("SELECT * FROM table1")
for x in myCursor:
    print(x)























