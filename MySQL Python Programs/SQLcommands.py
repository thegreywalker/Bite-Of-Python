import mysql.connector
from datetime import datetime



db = mysql.connector.connect(host="localhost", user="root", passwd="root", auth_plugin="mysql_native_password",
                             database="myorg")

myCursor = db.cursor()
# myCursor.execute("CREATE TABLE Student (name VARCHAR(60), class smallint UNSIGNED, Section char, Roll_Num smallint PRIMARY KEY, Percentages smallint)")
# myCursor.execute("INSERT INTO Student (name, class, Section, Roll_Num, Percentages) VALUES (%s,%s,%s,%s,%s)", ("Himangshu", 11,"C",8,72))
# db.commit()
# myCursor.execute("CREATE TABLE Test (name varchar(60) NOT NULL, created datetime NOT NULL, gender ENUM('M', 'F', 'O'), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# myCursor.execute ("INSERT INTO Test (name, created, gender ) VALUES (%s,%s,%s)", ('Raima', datetime.now(), "F"))
# db.commit()

# myCursor.execute("DESCRIBE Test")
# for x in myCursor:
#     print(x)

# 
# myCursor.execute("ALTER TABLE Test ADD COLUMN foods VARCHAR(60) NOT NULL")


# myCursor.execute("ALTER TABLE Test CHANGE name First_Name VARCHAR (70)")
# myCursor.execute("DESCRIBE Test")
# myCursor.execute("SELECT * FROM Test ORDER BY id ASC")
# for x in myCursor:
#     print(x)


import mysql.connector

db = mysql.connector.connect(host="localhost", user="root", passwd="root", auth_plugin="mysql_native_password",
                             database="myorg")

users = [("Apurba Ghosh", "1345"),
         ("Himangshu De", "password#$34"),
         ("Raima Ray", "iloveapurba")
         ]

user_scores = [(45, 500),
               (30, 200),
               (40, 124)
               ]

myCursor = db.cursor()

Q1 = "CREATE TABLE Users(id int PRIMARY KEY AUTO_INCREMENT, name VARCHAR(60), passwd VARCHAR(70))"
Q2 = "CREATE TABLE Scores (user_id int PRIMARY KEY, FOREIGN KEY(user_id) REFERENCES Users(id), game1 int DEFAULT 0, game2 int DEFAULT 0)"

# myCursor.execute("SHOW TABLES")


# for x in myCursor:
#     print(x)

Q3 = "INSERT INTO Users (name, passwd) VALUES (%s,%s)"
Q4 = "INSERT INTO Scores (user_id, game1, game2) VALUES (%s,%s,%s)"

# for x, user in enumerate(users):
#     myCursor.execute(Q3, user)
#     last_id = myCursor.lastrowid
#     myCursor.execute(Q4, (last_id,) + user_scores[x])
# db.commit()
    

# myCursor.execute("SELECT * FROM Users")
# for x in myCursor:
#     print(x)
# myCursor.execute("SELECT * FROM Scores")
# for x in myCursor:
#     print(x)

# myCursor.execute("SHOW TABLES")
# for x in myCursor:
#     print(x)

# myCursor.execute("DESCRIBE Users")
# for x in myCursor:
#     print(x)
    
# myCursor.execute("DESCRIBE Scores")
# for x in myCursor:
#     print(x)



