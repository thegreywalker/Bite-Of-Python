"""
Write a Program to insert 5 records in any one of the table created 
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password", database="mydb")
myCursor = db.cursor()

Q1 = ("INSERT INTO table1(name,class,sec) VALUES(%s,%s,%s)")
userData = [
    ("Apurba Ghosh",11,'C'),
    ("Himangshu De",11,'C'),
    ("Raima Ray",11,'B'),
    ("Priyanka Das",11,'D'),
    ("Rupankar Das",11,'C')
    
]
myCursor.execute("DESCRIBE table1")
for x in userData:
    myCursor.execute(Q1,x)
db.commit()    

myCursor.execute("SELECT * FROM table1 ORDER BY sec ASC")
myCursor.execute("SELECT * FROM table1 ORDER BY sec DESC")
for x in myCursor:
    print(x)




































