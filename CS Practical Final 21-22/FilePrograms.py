# Q12 Solution
with open("text.txt") as optFile:
    lines = optFile.read().split()
    for items in lines:
        print(items+"#", end="")


# Q13 Solution
with open("text.txt") as tarFile:
    lines = tarFile.read()
    vowel = consonants = uppercase = lowercase = 0
    for items in lines:
        if items in "aeiouAEIOU":
            vowel += 1
        if items.isupper():
            uppercase += 1
        if items.islower():
            lowercase += 1
        if items not in "AaEeIiOoUu":
            consonants += 1
    print(f"Total Vowels are: {vowel}\nTotal Consonants are: {consonants}\nTotal Uppercase Characters are: {uppercase}\nTotal Lowercase characters are: {lowercase}")



# Q14 Solution
import os
file1 = open("text.txt", "r")
file2 = open("sample.txt", "w")
file3 = open("text1.txt","w")
lines = file1.readlines()
for items in lines:
    if 'a' in items:
        file2.write(items)
    if 'a' not in items:
        file3.write(items)

file1.close()
file2.close()
file3.close()
os.remove("./text.txt")
os.rename("./text1.txt", "text.txt")


# Q15 Solution
import pickle


def inputRecord():
    with open("student.bin", "ab") as binFile:
        records = []
        while True:
            nameInput = input("Enter student's name: ")
            rollInput = int(input("Enter roll number: "))
            userInput = input("Do you want to input another record?(y/N) ")
            records.append([nameInput, rollInput])
            if userInput == "y".casefold():
                continue
            else:
                break
        pickle.dump(records, binFile)


def searchRecord():
    with open("student.bin", "rb") as binFile:
        mainFile = pickle.load(binFile)
        rollInput = int(input("Enter roll number to search: "))
        for items in mainFile:
            if rollInput == items[1]:
                print("The name of the student is:", items[0])
                break
            else:
                pass
        else:
            print("No records found! :(")


inputRecord()
searchRecord()


# Q16 Solution
import pickle
import os


def marksInRecord():
    records = []
    with open("marks.bin", "wb") as binFile:
        while True:
            rollInput = int(input("Enter roll number: "))
            nameInput = input("Enter name: ")
            markInput = float(input("Enter mark: "))
            userChoice = input("Add other Record?(y/N): ")
            records.append([rollInput, nameInput, markInput])
            if userChoice == "y".casefold():
                continue
            else:
                break
        pickle.dump(records, binFile)


def searchMarkInRecord():
    binFile1 = open("marks.bin", "rb")
    mainFile = pickle.load(binFile1)
    records = mainFile
    rollNumberInput = int(input("Enter roll number: "))
    markUpdate = float(input("Enter marks to be updated: "))
    for items in records:
        if rollNumberInput == items[0]:
            items[2] = markUpdate
            break
        else:
            pass
    else:
        print("No Records Found! :(")
    anotherBinFile = open("marks1.bin", "wb")
    pickle.dump(records, anotherBinFile)
    binFile1.close()
    anotherBinFile.close()
    os.remove("./marks.bin")
    os.rename("./marks1.bin", "marks.bin")


marksInRecord()
searchMarkInRecord()

# Q17 Solution
import random

while True:
    userEnter = input("Press Enter for  random number or E to exit: ")
    if userEnter == "e".casefold(): break
    randomNumber = random.randint(1,6)
    print(randomNumber)



#Q18 Solution
import csv
def csvUserIn():
    records = []
    while True:
        userID = input("Enter user ID: ")
        password = input("Enter password: ")
        userChoice = input("Add another Record?(y/N) ")
        records.append([userID, password])
        if userChoice == "y".casefold():
            continue
        else: break
    with open("credentials.csv", "a") as csvFile:
        writerCsv = csv.writer(csvFile)
        writerCsv.writerow(["UserID", "Password"])
        writerCsv.writerows(records)
    
def csvSearchIn():
    with open("credentials.csv", "r") as csvFile:
        mainReader = csv.reader(csvFile)
        header = next(mainReader)
        rows = []
        for row in mainReader:
            if row != []:
                rows.append(row)
    
    while True:
        userIDInput = input("Enter userID to search: ")
        for items in rows:
            if userIDInput == items[0]:
                print(f"The password for '{userIDInput}' is '{items[1]}'")
                break
            else: pass
        else:
            print("No records found! :(")
        userChoice = input("Search another?(y/N)")
        if userChoice == "y".casefold(): continue
        else: break

# csvUserIn()
csvSearchIn()
        

# 19. Write a python program to read a text file STORY.TXT and print only palindrome words from the file.

def palindromePrinter():
    f = open("story.txt", "r")
    f = f.read().split()
    for i in f:
        if i == i[::-1]:
            print(i)

palindromePrinter()



# Q20 Solution
with open("text.txt") as txtFile:
    linesList = txtFile.readlines()
    for i in linesList[::-1]:
        print(i.strip("\n"))



