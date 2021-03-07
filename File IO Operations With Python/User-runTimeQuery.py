import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    passwd = "root",
    user = 'root',
    database = "mydb"
)

myCursor = db.cursor()

n = int(input("Enter the Number of Queries you want to enter: "))
data = []
for x in range(0,n):
    val = input("Enter the data: ")
    tup = tuple(map(str, val.split(", ")))
    data.append(tup)

query = "INSERT INTO textdata (Name, Class, Section) VALUES(%s, %s, %s)" 
myCursor.executemany(query, data)
myCursor.execute("SELECT * FROM textdata")
for x in myCursor:
    print(x)
db.commit()












