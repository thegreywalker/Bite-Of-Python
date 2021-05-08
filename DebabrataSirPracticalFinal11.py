"""
Q) 1.
 Write a menu driven program in python to take a string from user and display whether the string is palindrome or not. 
 User will also give choice whether to input a string again and to test it is palindrome or not. 
 Run the program and input at least two strings and check it is palindrome or not. Generate proper output. (4)
"""


# def SentencePalindrome(x):
#     char = ''
#     for val in x.casefold():
#         if val.isalnum() == True:
#             char += val 
#     if char == char[::-1]:
#         return True
#     else:
#         return False


# def NumberPalindrome(y):
#     if SentencePalindrome(y):
#         return True
#     else:
#         return False
#     pass


# def main():
#     info = input(""" You want to enter a Sentence(1)
#                         or
#                 You Want to enter a Number as a Palindrome(2),\tChoose: """)
#     if info == '1':
#         userSentenceString = input("Enter a String: ")
#         if SentencePalindrome(userSentenceString):
#             print(f"The String {userSentenceString} is a Paliondrome.")
#         else:
#             print(f"The String {userSentenceString} is not a Palindrome.")
            
#     else:
#         userNumberString = input("Enter a Number: ")
#         if NumberPalindrome(userNumberString):
#             print(f"The String {userNumberString} is a Palindrome.")
#         else:
#             print(f"The String {userNumberString} is not a Palindrome.")
#     print()        
#     reEnter = input("Do you want to enter the string again(y/n): ")
#     if reEnter == 'y':
#         print()
#         info = input(""" You want to enter a Sentence(1)
#                         or
#                 You Want to enter a Number as a Palindrome(2),\tChoose: """)
#         if info == '1':
#             userSentenceString = input("Enter a String: ")
#             if SentencePalindrome(userSentenceString):
#                 print(f"The String {userSentenceString} is a Paliondrome.")
#             else:
#                 print(f"The String {userSentenceString} is not a Palindrome.")
                
#         else:
#             userNumberString = input("Enter a Number: ")
#             if NumberPalindrome(userNumberString):
#                 print(f"The String {userNumberString} is a Palindrome.")
#             else:
#                 print(f"The String {userNumberString} is not a Palindrome.")
        
#     else:
#         print()
#         print("Thanks for Visiting.")


# if __name__ == '__main__':
#     main()


"""
Q.2. Write a menu driven program in python to take a number from user and test whether the given number is an Armstrong Number or not. 
Run the program and input at least two numbers (two times) to test palindrome or not. Generate proper output. (4) 
"""


# def NumberPalindrome(x):
#     data = str(x)
#     if data == data[::-1]:
#         return True
#     else:
#         return False


# def Armstrong(y):
#     data = str(y)
#     n = len(data)
#     temp = y
#     cur = 0
#     arm = 0
#     while temp != 0:
#         cur = temp%10
#         arm = arm*1 + pow(cur,n)
#         temp //= 10
#     if y == arm:
#         return True

#     else:
#         return False


# def main():
#     counter = 1
#     while counter <= 2:
#         print()
#         userNumber = int(input("Enter the Number: "))
#         print()
#         if Armstrong(userNumber):
#             print(f"The Number {userNumber} is an Armstrong number.")
#         else:
#             print(f"The Number {userNumber} is not an Armstrong number.")
            
        
#         if NumberPalindrome(userNumber):
#             print(f"The Number {userNumber} is a Plaindrome.")
#         else:
#             print(f"The Number {userNumber} is not a Plaindrome.")
        
#         counter += 1 
#     pass


# if __name__ == "__main__":
#     main()



""" 
Q.3.Write a program in python to take a list from user and display all its EVEN position and ODD position elements individually. (4)
"""


# def EvenPosition(x):
#     data = []
#     for j in range(0,len(x)):
#         if j%2 == 0:
#             data.append(x[j])   
    
#     print("The Even Position Elements are: ", end=" ")
#     print(*data, sep=", ")
#     pass


# def OddPosition(y):
#     data = []
#     for j in range(0,len(y)):
#         if j%2 != 0:
#             data.append(y[j])   
    
#     print("The Odd Position Elements are: ", end=" ")
#     print(*data, sep=", ")
#     pass


# def main():
#     userList = eval(input("Enter the list: "))
#     EvenPosition(userList)
#     OddPosition(userList)


# if __name__ == "__main__":
#     main()


"""
Q.4. Write a program in python to declare a dictionary and display all keys and values of the dictionary individually. (4) 
"""


# dict1 = dict(zip(('Name', 'Class', 'Section'), ('Debabrata Patikar', 'XII', 'B')))

# dictionary_keys = list(dict1.keys())
# dictionary_values = list(dict1.values())

# print("The Dictionary is ", dict1)
# print()
# print("The keys in the Dictionary are: ", end=" ")
# print(*dictionary_keys, sep=", ")
# print("The values in the Dictionary are: ", end=" ")
# print(*dictionary_values, sep=", ")


"""
Q.5. Write a program in python to take a string from user and test how many words are there in the string.
Display the user given string first and then display total number of words in the string. (4) 
"""


# userString = input("Please enter a String to display: ")
# print()
# print(f'The String you have entered is "{userString}"')

# words = 0
# for val in userString:
#     if val.isalpha():
#         words += 1

# print(f'The total number of words in the String "{userString}" is {words}')



"""
Q.6. Write a menu driven program in python to take 6 subjects (eng, beng, math, phy, chem, comp) mark from user and 
calculate total mark and average mark of a student and display result based on user choice whether user want to add more students’ 
marks and want to see total marks and average mark as well. User can stop the process by choice also. 
Run the program and input at least two students’ subject marks and display the result. Generate proper output. (4) 
"""


# def StudentCredentials():
#     names = []
#     subjects = []
#     name = input("Enter Your Name: ")
#     names.append(name)
#     SubjectMarks = input("Enter your Subject marks(6 Subjects): ")
#     subjects.append(tuple(map(str, SubjectMarks.split(", "))))
#     print()
#     print(f"Student Name: {names[0]}")
#     print()
#     print("\t\t------------Marks------------")
#     print()
#     print(f"English:   \t{subjects[0][0]}")
#     print(f"Bengali:   \t{subjects[0][1]}")
#     print(f"Maths:     \t{subjects[0][2]}")
#     print(f"Physics:   \t{subjects[0][3]}")
#     print(f"Chemistry: \t{subjects[0][4]}")
#     print(f"Computer:  \t{subjects[0][5]}")
#     print()
#     return subjects
    
    


# def MarksCalculations(y):
#     TotalMarks = 0
#     for j in range(0, len(y[0])):
#         TotalMarks = TotalMarks + int(y[0][j])
#     print(f"The total marks is {TotalMarks}")
#     print()
#     pass


# def main():
#     choice = 0
#     print("You can add as many Student Data as you want and can print them on the Screen. Remember to write n to quit the program.")
#     while choice != 'n':
#         subjects = StudentCredentials()
#         MarksCalculations(subjects)
#         choice = input("Do you want to add a new Student data(y/n): ")
#         if choice == 'n':
#             print()
#             print("Thank You for Visiting.")


# if __name__ == "__main__":
#     main()



"""
Q.7. Write a menu driven program in python to take two numbers from user and calculate addition, multiplication and subtraction of 
two given numbers and display result based on user choice whether user want to add again two numbers and want to see the result 
again or not. User can stop the process by choice also.
Run the program and input at least two times – two numbers and display result. Generate proper output. (4) 
"""


# def Addition(x):
#     a = int(x[0])
#     b = int(x[1])
#     print(f"The Addition of the two numbers is: {a+b}")
#     pass


# def Subtraction(y):
#     a = int(y[0])
#     b = int(y[1])
#     if a > b:
#         print(f"The Subtraction of the two numbers is: {a-b}")
#     if a < b:
#         print(f"The Subtraction of the two numbers is: {b-a}")
#     if a == b:
#         print(f"The Subtraction of the two numbers is: {a-b}")
#     print()
#     pass


# def Multiplication(z):
#     a = int(z[0])
#     b = int(z[1])
#     print(f"The Multiplication of the two numbers is: {a*b}")
#     pass


# def main():
#     choice = 0
#     while choice != 'n':
#         numbers = input("Enter two Numbers: ")
#         print()
#         data = numbers.split(", ")
#         Addition(data)
#         Multiplication(data)
#         Subtraction(data)
        
#         choice = input("Do you want to eanter Numbers again(y/n): ")
#         if choice == 'n':
#             print()
#             print("Thanks for visiting.")
#     pass


# if __name__ == "__main__":
#     main()



"""
Q.8.Write a program in python to take a list from user and modify the list by multiplying all its EVEN elements by 2
and ODD elements by 3. Display the original list first. Then display the modified list. (4) 
"""


# UserList = eval(input("Enter the List: "))
# print()
# print(f"The List before modification is {UserList}")
# i = 0
# for val in UserList:
#     if val%2 == 0:
#         UserList[i] = val*2
#     else:
#         UserList[i] = val*3
#     i += 1
# print(f"The List after modification is {UserList}")




"""
Q.9. Write a program in python to declare a dictionary and modify the dictionary by adding N number of elements
From user. Display the original dictionary first. Then display the modified dictionary. (4)
"""


# dict1 = {'Debabrata' : 'The Best Computer Teacher'}
# print(f"The Original Dictionary is {dict1}")
# print()
# choice = 0
# while choice != 'n':
#     keyValue = input('Enter the Key and Value of the dictionary: ')
#     data = keyValue.split(", ")
#     print()
#     print(f"The Original Dictionary before modifiocation is: {dict1}")
#     dict1[data[0]] = data[1]
#     print(f"The Original Dictionary after modifiocation is: {dict1}")
#     print()
#     choice = input("Do you want to add more dictionary elements(y/n): ")
#     if choice == 'n':
#         print()
#         print("Thanks for Visiting.")
    


"""
Q.10. Write a program in python to take a string from user and test whether the user given string is palindrome or not. (4) 
"""


# def Palindrome(x):
#     char = ''
#     for val in x.casefold():
#         if val.isalnum():
#             char += val
            
#     if char == char[::-1]:
#         return True
#     else:
#         return False


# def main():
#     UserString = input('Enter A STRING: ')
#     print()
#     if Palindrome(UserString):
#         print(f"The String {UserString} entered by you is a Palindrome.")
#     else:
#         print(f"The String {UserString} entered by you is not a Palindrome.")
#     pass

# if __name__ == "__main__":
#     main()





