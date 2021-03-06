import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "mydb"
)

myCursor = db.cursor()


"""
Creating the necessary table and checking if it exist 
"""

myCursor.execute("create table pythontextdata(SongName VARCHAR(60), ArtistName VARCHAR(60) PRIMARY KEY, ReleaseDate VARCHAR(40))")
myCursor.execute("show tables")
for x in myCursor:
    print(x)


"""
Reading and pasing the text data into SQL Database mydb, table -- pythontextdata 
"""


values = []
with open("PythonTextData.txt", "r") as text_file:
    for text in text_file:
        value1 = text.strip("\n")
        value1 = tuple(map(str, value1.split(', ')))
        values.append(value1)
query = "INSERT INTO pythontextdata(SongName, ArtistName, ReleaseDate) VALUES (%s,%s,%s)"
myCursor.executemany(query, values)
db.commit()
myCursor.execute("select * from pythontextdata")
for x in myCursor:
    print(x)
