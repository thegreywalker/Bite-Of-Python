import mysql.connector, csv

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "mydb",
    )

myCursor = db.cursor()

"""
Creation of the Sample Table and passing it's fields as in Columns, and reading it to see if everything is correct 
"""

myCursor.execute("create table PythonCsvData (EmployeeID VARCHAR(20) PRIMARY KEY, Name VARCHAR(30), FloorNumber INT(5), ContactNumber VARCHAR(50), Address VARCHAR(200), Designation VARCHAR(60), Salary INT(20))")
myCursor.execute("describe pythoncsvdata")
myCursor.execute("select * from pythoncsvdata")
myCursor.execute("show tables")
for x in myCursor:
    print(x)
    


with open("CSV File Operations with Python\PythonCSVData.csv") as csv_file:
    csvfile = csv.reader(csv_file, delimiter = ",", )
    all_value = []
    for row in csvfile:
        value = (row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        all_value.append(value)

        

query = """INSERT INTO PythonCsvData(EmployeeID, Name, FloorNumber, ContactNumber, Address, Designation, Salary) VALUES (%s, %s, %s, %s, %s, %s, %s)"""
myCursor.executemany(query, all_value)
db.commit()














