"""
Write a Program to add three column of your choice in an existing table and Update the Values of the the columns
"""

import mysql.connector
db = mysql.connector.connect(host="localhost", user="root",passwd="root",auth_plugin="mysql_native_password", database="mydb")
myCursor = db.cursor()

myCursor.execute("ALTER TABLE table1 ADD COLUMN id int PRIMARY KEY AUTO_INCREMENT, ADD COLUMN percentages VARCHAR(6), ADD COLUMN roll_num int(7)")
myCursor.execute("DESCRIBE table1")


Q1 = "UPDATE table1 SET percentages='90%' WHERE id = 1"
Q2 = "UPDATE table1 SET roll_num = 5 WHERE id = 1"
myCursor.execute(Q1)
myCursor.execute(Q2)

Q3 = "UPDATE table1 SET percentages='78%' WHERE id = 2"
Q4 = "UPDATE table1 SET roll_num = 6 WHERE id = 2"
myCursor.execute(Q3)
myCursor.execute(Q4)

Q5 = "UPDATE table1 SET percentages='62%' WHERE id = 3"
Q6 = "UPDATE table1 SET roll_num = 7 WHERE id = 3"
myCursor.execute(Q5)
myCursor.execute(Q6)

Q7 = "UPDATE table1 SET percentages='78%' WHERE id = 4"
Q8 = "UPDATE table1 SET roll_num = 2 WHERE id = 4"
myCursor.execute(Q7)
myCursor.execute(Q8)

Q9 = "UPDATE table1 SET percentages='72%' WHERE id = 5"
Q10 = "UPDATE table1 SET roll_num = 9 WHERE id = 5"
myCursor.execute(Q9)
myCursor.execute(Q10)
db.commit()
myCursor.execute("SELECT * FROM table1")
for x in myCursor:
    print(x)























