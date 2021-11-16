# 1. Write a program to take input name of student,roll & marks of 3 subjects of 4 students and store these details along with total of 3 subjects in a binary file names.txt. the program should also search a student from the file by the roll number and print the details if found otherwise it will print " Student not found" msg.


import pickle

with open('names.dat', 'rb') as f:
    data = pickle.load(f)
    print(data)


    
data = []

for j in range(0,2):
    name = input("Enter Your Name? ")
    roll = int(input("Enter Your Roll Number? "))
    marks = input("Enter Marks of 3 Subjects? ")
    data.append([name, roll] + marks.split(", "))



with open('names.dat', 'rb') as f:
    data = pickle.load(f)
    print(data)

def search(Args):
    flag = 0
    with open('names.dat', 'rb') as f:
        data = pickle.load(f)
        for record in data:
            if record[1] == Args:
                print(f"The Details of the Student is {record}")
                flag = 0
                break
            
            else:
                flag = 1
    if flag == 0:
        pass
    else:
        print("Student not Found")
        
search(roll := int(input("Enter the Roll Number to search? ")))



# 2. Write a python program to interchange the highest number and the lowest number from a list of 10 numbers using function.


def InterChange():
    ls = [1 , 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # ls = [5, 4, 8, 9, 1, 2, 7, 6, 2, 1.5]
    smallestNumber = largestNumber = ls[0]
    for val in ls:
        if val > largestNumber:
            largestNumber = val

        else:
            pass

        if val < smallestNumber:
            smallestNumber = val
        
        else:
            pass
    data = [ls.index(largestNumber), ls.index(smallestNumber)]
    ls[data[0]] = smallestNumber
    ls[data[1]] = largestNumber
    
    return ls

print(InterChange())




# 3. Write a program to store the details of books in a csv file. The user should give input book id,book name,author name,publisher & price as input to store. The program should search a book by the book id and print the details if found and print necessary result if not found.


import csv


for val in range(0, 2):
    with open('books.csv', 'w') as f:
        book_id = int(input("Enter the Book Id? "))
        book_name = input("Enter the Name of the Book? ")
        author_name = input("Enter the Name of the Author? ")
        publisher_name = input("Enter the name of the Publisher? ")
        price = int(input("Enter the Price of the Book? "))
        
        writerObj = csv.writer(f)
        writerObj.writerow([book_id, book_name, author_name, publisher_name, price])

with open('books.csv', 'r') as f:
    print()
    flag = 0
    Args = int(input("Enter the Book ID to Search? "))
    data = csv.reader(f)
    for record in data:
        if record == []:
            continue
        if record[0] == str(Args):
            print(record)
            flag = 0
            break

        else:
            flag = 1

    if flag == 0:
        pass
    
    else:
        print("Result Not Found...")




# 4. Using python function write a program that accept a string as input from the user and print the new string after replacing all the vowels with '*'.



def Replace(String):
    MyString = ''
    for char in String:
        if char.casefold() in  "aeiou":
            MyString += "*"
        else:
            MyString += char

    return MyString

print(Replace("Apurba"))




# 5. Write a program to create a text file programming.txt with 3 lines about python programming. The program should replace all the 'is' with 'was' in the file.


with open('programming.txt', 'w') as f:
    f.write("Python is a high level programming language.\n")
    f.write("Python is a easy to learn language.\n")
    f.write("Python is a powerful language.\n")


with open('programming.txt', 'r') as f:
    data = f.readlines()
    for line in data:
        print(line.replace("is", "was"))


# 6. Write a program to take a function which accepts 10 numbers from the user as input and interchnge the 1st two elements with the last two elements. The program should print the new list.


def InterChangeNumbers(*args):
    ls = list(args)
    val, val2 = ls[0], ls[1]
    ls[0], ls[1] = ls[-2], ls[-1]
    ls[-2], ls[-1] = val, val2
    return ls


print(InterChangeNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))













