import mysql.connector, csv

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "mydb",
    auth_plugin = "mysql_native_password"
)

myCursor = db.cursor()

query = "SELECT name, class, sec, id, percentages, roll_num FROM table1"

myCursor.execute(query)
result = myCursor.fetchall()

with open("CSV File Operations With Python\PythonCSVDataExtracted.csv", "w") as file:
    for row in result:
        csv.writer(file).writerow(row)
        
myCursor.close()






