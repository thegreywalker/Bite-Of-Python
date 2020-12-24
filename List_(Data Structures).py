""" 1) Write a Python Program to sum all the items of a List  """


# lst = []
# n = int(input("Enter the Number of items to enter: "))
# for i in range(0,n):
# 	ele = int(input("Enter the Item: "))
# 	lst.append(ele)
# print()
# print("THE CURRENT LIST IS ",lst)
# sum = 0
# i = 0
# for ch in lst:
# 	sum = sum + lst[i]
# 	i += 1
# print("The Sum of the items in the list is: ",sum)


""" 2) Write a Python Program to multiplies all the items in the list """


# lst = []
# n  = int(input("Enter the Number of elements: "))
# for i in range(0,n):
# 	ele = int(input("Enter the Item: "))
# 	lst.append(ele)
# print()
# print("THE CURRENT LIST IS ",lst)
# mult = 1
# i = 0
# for item in lst:
# 	mult  = mult*lst[i]
# 	i += 1
# print("The Multiplication of the items in the list is: ",mult)


""" 3) Write a Python Program to find the largest number in the list """


# lst = []
# n = int(input("Enter the Number of Elements: "))
# for i in range(0,n):
# 	ele = int(input("Enter the Number: "))
# 	lst.append(ele)
# print()
# print("THE CURRENT LIST IS ",lst)
# largest = lst[0]
# i = 1
# while (i <= n-1):
# 	if largest > lst[i]:
# 		largest = largest
# 	else:
# 		largest = lst[i]
# 	i += 1
# print("The Largest Number in the List is: ",largest)


""" 4) Write a Python Program to get the Smallest Number from the list  """


# lst = []
# n = int(input("Enter the Number if Elements: "))
# for i in range(0,n):
# 	ele = int(input("Enter the Element: "))
# 	lst.append(ele)
# print()
# print("THE CURRENT LIST IS ",lst)
# smallest = lst[0]
# i = 1
# while (i <= n-1):
# 	if smallest < lst[i]:
# 		smallest = smallest
# 	else:
# 		smallest = lst[i]
# 	i += 1
# print("The Smallest Number in the List is: ",smallest)


""" 5) Write a Python Program to Count the number of Strings where  
the String Length is 2 or more and the first and the last charecters are same from the given list of strings.
"""

# lst = ['rana','apurba','raima','rupankar','aniruddha']
# i = 0
# for ch in lst:
# 	if (len(lst[i])>= 2 and lst[i][0] == lst[i][-1]):
# 		print("String no. {} is: {}".format(i,lst[i]))
# 	i += 1


""" 6) Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
 Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
 Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
 
"""


# lst = [(1,4),(2,5),(3,1),(8,9),(2.5,4),(1,2)]
# lst.sort()
# print(lst)


""" 7) Write a Python Program to Remove all the duplicates from the list  """


""" 8) Write a Python program to check a list is empty or not. """


# lst = []
# if len(lst) == 0:
# 	print("This is an Empty List")
# else:
# 	print("This List has elements")


""" 9) Write a Python program to clone or copy a list """

# lst1 = [2,4,5,8,7]
# # List 2 is on a different memory location
# lst2 = lst1[:]
# print(lst2)


""" 10) Write a Python program to find the list of words that are longer than n from a given list of words. """


# lst = eval(input("Enter the List: "))
# n = len(lst[0])

# for i in range(1,len(lst)):
# 	if len(lst[i])>n:
# 		print(lst[i])


"""  Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. """

# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']


""" 
Write a Program to create a user generated list and find the occurance of the element given by the user.
"""


#l = []
#b = int(input("Enter the number of elements to enter: "))
# for val in range(b):
#ele = int(input ())
#	l.append(ele)

# n = int(input("Enter the item to search: "))
# print(l.count(n))


"""  Write a Program to sort a list in reverse order  """

# l = [23, 45,7,56,67,198]
# l. sort(reverse = True)
# print(l)


""" Write a Program to count the frequencies of all the elements of a list and
    Also print the following:
    i) List of Unique elements.
   ii) List of Duplicate elements.
"""


# l = [12, 5, 4, 5, 8, 9, 12, 4, 8, 52, 45, 8, 20, 52, 45, 89, 21, 16]
# Unique = []
# duplicate = []
# print(l)
# for i in range(len(l)):Cool
#     if l[i] in Unique:
#         continue
#     else:
#         count = l.count(l[i])
#         if count > 1:
#             duplicate.append(l[i])
#             duplicate.sort()
#         else:
#             pass
#         Unique.append(l[i])
#         Unique.sort()
#         print("{0:<2} has {1} occurances in the list"
#               .format(l[i], count))
# print(f"Unique Element list is {Unique}")
# print(f"Duplicate Element list is {duplicate}")


"""
@Author ---- Apurba [code 10];
"""
















"""
Write a Program to calculate the mean of a given list of numbers (list has to be an input by the user)
"""

# l = []
# n = int(input("Enter the number of elements you want to enter: "))
# for val in range(n):
#     ele = int(input("Enter the Element: "))
#     l.append(ele)

# sum = mean = 0
# i = 0
# for val in l:
#     sum = sum + l[i]
#     mean = sum / len(l)
#     i += 1
# print(f"The mean of {l} is {mean}")


# l = [12,45,62,96]
# l2 = [1,2,3]
# l.append(25)
# l.append(l2)
# print(l)
# print(l+l2)
# print(l.pop(2))
















"""
Program to find minium element from a list of element along with it's index in the list.
"""


# l = [45,85,36,21,57,95,24,37,52,89,27,15,51]
# smallest = l[0]
# i = 0
# for val in l:
#     if l[i] < smallest:
#         smallest = l[i]
#     else:
#         smallest = smallest
    
#     i += 1
# print(f"The Smallest Number in the list is {smallest} found at index \
# {l.index(smallest)}")
    



""" Alternative of the Above Solution """




# l = [45,85,36,21,57,95,24,37,52,89,27,15,51]
# smallest = l[0]
# for val in l:
#     if val < smallest:
#         smallest = val
#     else:
#         smallest = smallest
# print(f"The Smallest number in the list is {smallest} found at index \
# {l.index(smallest)}")
















"""
Program to find largest element from a list of element along with it's index in the list.
"""


# l = [45,85,36,21,57,95,24,37,52,89,27,15,51]
# largest = l[0]
# i = 0
# for val in l:
#     if l[i] > largest:
#         largest = l[i]
#     else:
#         largest = largest
#     i += 1
# print(f"The largest number in the list is {largest} is found at index \
# {l.index(largest)}")





""" Alternative of the Above Solution """





# l = [45,85,36,21,57,95,24,37,52,89,27,15,51]
# largest= l[0]
# for val in l:
#     if val > largest:
#         largest = val
#     else:
#         largest = largest
# print(f"The largest number in the list is {largest} is found at index \
# {l.index(largest)}")


















"""
Program to search for an element in a given list of numbers.
"""

# l = ["Apurba","Raima","25",25,54,89,296,26,25.4,58.7,"Himangshu"]
# search = eval(input("Enter the Element to search: "))
# index = 0
# for val in l:
#     if val == search:
#         if search == l[2]:
#             print(f"The String Element {search} is found at index {index}")
#             break
#         else:
#             print(f"Element {search} is found at index {index}")
#             break
#     else:
#         index += 1
#         continue
# else:
#     print(f"The Element {search} is not found in list")





""" Alternative of the Above Solution """



# l = ["Apurba","Raima","25",25,54,89,296,26,25.4,58.7,"Himangshu"]
# search = eval(input("Enter the Element to search: "))
# if search in l:
#     if search == l[2]:
#         print(f"The String Element {search} is found at index {l.index(search)}")
#     else:
#         print(f"The Element {search} is found in list at index {l.index(search)}")






"""
Two Unsolved Mystry probably could do when I learn Python in a better way
"""





# words = ["Apurba", "Raima", "Himangshu"]
# for index, word in enumerate(words):
#     print(index, word)


# subjects = ["math", "chemistry", "biology", "physics"]
# grades = [100, 83, 90, 92]

# grades_dict = list(zip(subjects, grades))
# print(grades_dict)
























"""
Write a Program to find the Secondlargest number in a list.
"""
# # l = [45,85,36,57,85,24,75,69,105,52,47,21,85]
# l = [45,85,36,21,57,95,24,37,52,89,27,15,51]
# largest = Secondlargest = l[0]
# for val in l:
# 	if val > largest or val > Secondlargest:
# 		if val < largest and val > Secondlargest:
# 			Secondlargest = val
# 			continue
# 		else:
# 			Secondlargest = largest
# 		largest = val
# 	else:
# 		Secondlargest = Secondlargest
# 		largest = largest
		
# print(f"The Largest Element in the list is {largest}")
# print(f"The Second Largest Element in the list is {Secondlargest}")
# l.sort()
# print(l)













"""
Write a Program that inputs a list of numbers and shifts all the Zeros to right and all non-zero numbers to the left of the list.
"""



# l = [12,0,50,0,89,60,0,25,63,0,85,96]    #for optional use to check the program faster by already defining a pre-defined list.


# Part where we gather the elements of the list

# l = []
# n = int(input("Enter the Number of item you want to nter in list: "))
# for i in range(n):
#     ele = eval(input())
#     l.append(ele)

# #  Part where we check each item if it's non-zer or not and then do as directed in the question


# temp = list(l)
# zero = []
# non_zero = []
# flag = True
# for val in l:
#     if val == 0:
#         flag = True
#     else:
#         flag = False

#     if flag == True:
#         zero.append(val)
#     else:
#         non_zero.append(val)

# l2 = []
# l2.extend(non_zero)
# l2.extend(zero)
# print(l2)










# l = [27,44,11,5,11,8,11,8]
# ul = dl = []

# for i in l:
#     if i not in dl:
#         if l.count(i) > 1:
#             dl.append(i)
#             ul.append(i)
#         else:
#             ul.append(i)
#     else:
#         continue
        
# print(f"Unique List is {ul}")
# print(f"Duplicate List is {dl}")









































"""
Write the most appropriate list methods to perform the following tasks.
a) Delete a given Element from the list.
b) Delete 3rd Element from the List.
c) Add an Element in the end of the List.
d) Add an Element at the beginning of the List.
e) Add Element of the list at the end of the list
"""


#  a)
# L = [12,52,65,85,32,94,47,15,48]

#  Say it;s said to delete 94 from the list
# L.remove(94)
# print(L)


#  b)

#  So the 3rd Element from the List is 65 at index 2
# L.pop(2)
# print(L)


#  c)

# So let's say that we want to add 105 in the end of the list
# L.append(105)
# print(L)


# d)

# Say we want to add 204 at the beginning of the list
# L.insert(0,204)
# print(L)


# e)

# Say we want to add the list [12,52,45] at the end of the list and we can 
# do that by two ways. Let's explore that

# 1st)

# L.extend([12,52,45])
# print(L)


# or
# l = [12,52,45]
# L.extend(l)












"""
Given a List of integers, L, Write Code to add the integers and display the sum.
"""
# L = [12,52,45,65,89,52]
# sum = 0
# for val in L:
#     sum = sum + val

# print(L)
# print(f"The Sum of all the ELements in the List is {sum}.")


# # Alternative Solution

# L = [12,52,45,65,89,52]
# sum = 0
# for i in range(len(L)):
#     sum = sum + L[i]
    
# print(L)
# print(f"The Sum of all the Elements of the List is {sum}.")













"""
Given a list of integers, L, write code to calculate and display the sum of all odd numbers in the list
"""

# L = [45,85,96,32,54,72,24]
# odd_sum = 0
# for val in L:
#     if not val%2 == 0:
#         odd_sum = odd_sum + val

# print(f"The Sum of all the Odd Numbers in the List is {odd_sum}")


# # Alternative Solution

# L = [45,85,96,32,54,72,24]
# odd_sum = 0
# for i in range(len(L)):
#     if L[i]%2 == 0:
#         continue
#     else:
#         odd_sum = odd_sum + L[i]

# print(f"The Sum of all the Odd Numbers in the List is {odd_sum}")


# # Alternative Solution

# L = [45,85,96,32,54,72,24]
# odd_sum = 0
# for i in range(len(L)):
#     if not L[i]%2 == 0:
#         odd_sum = odd_sum + L[i]

# print(f"The Sum of all the Odd Numbers in the List is {odd_sum}")

"""
Given two lists, Write a program that prints "Overlapped" if they have 
at least one member in common otherwise prints "Separated". 
You may use the "in" Operator, but for the sake of the program, 
Write it Using loops.
"""

# l = [12,52,85,47,96,35]
# l2 = [12,45,85,62,94,96]

# flag = 0
# for i in range(len(l)):
#     for j in range(len(l2)):
#         if l[i] == l2[j]:
#             flag = flag + 1
#         else:
#             pass

# if flag > 0:
#     print("Overlapped")
# else:
#     print("Skipped")













"""
Write a Program to revrese a list without creating a new list or using a different memory location, and without using Reverse Function.
"""

# l = [12,52,44,78,98,35,64,24,17,8,27]

# index = 0
# while index < len(l):
#     position = l[-1]
#     # l.remove(l[-1])
#     l.pop(-1)
#     l.insert(index,position)
#     index += 1
# print(f"The Reversed list is {l}")









"""
Q3) Write a Program to display the Maximum and the Minimum values from the specified range of indexes 
of the List including the Start Index and End Index.

L = [ 45, 85, 25, 35, 74, 58, 69, 32, 47, 37, 21, 54 ]
Output:
Enter the Start Index: 5
Enter the End Index: 10

The Largest Number in the Specified Index 5 - 10 is 69
The Smallest Number in the Specified Index 5 - 10 is 21
"""




# l = [15,85,57,65,24,17,35,65,24,75]
# index = 0
# a = int(input("Enter the Start Index: "))
# b = int(input("Enter the End Index: "))
# largest = smallest = l[a]
# for val in l:
#     if a == index or index > a:
#         if index > b:
#             break
#         else:
#             if val > largest:
#                 largest = val
                
#             else:
#                 largest = largest
            
#             if val < smallest:
#                 smallest = val
#                 index += 1
#             else:
#                 smallest = smallest
#                 index += 1
                
#     else:
#         index += 1
# print()
# print(f"The Largest Number in the Specified Index {a} - {b} is {largest}")
# print(f"The Smallest Number in the Specified Index {a} - {b} is {smallest}")




"""
Q) Write a Program to move all the duplicate values of the list to the end of the list.

L = [ 45, 52, 65, 89, 45, 25, 45, 52, 35, 65, 89, 54, 21, 57, 33, 61, 50 ]
Output: 

The List before modification is [ 45, 52, 65, 89, 45, 25, 45, 52, 35, 65, 89, 54, 21, 57, 33, 61, 50 ]
The List after modification is [ 25, 35, 54, 21, 57, 33, 61, 50, 45, 45, 45, 52, 52, 65, 65, 89, 89 ]


"""

# l = [ 45, 52, 65, 89, 45, 25, 45, 52, 35, 65, 89, 54, 21, 57, 33, 61, 50 ]
# l3 = []
# num_count = 0
# l2 = []
# for val in l:
#     num_count = l.count(val)
#     if val in l2:
#         continue
#     else:
#         if num_count > 1:
#             l2.append(val)
#             for val2 in range(num_count-1):
#                 l2.append(val)
#         else:
#             l3.append(val) 

# print(f"The List before modification is {l}")
# print(f"The List after modification is {l3+l2}")












"""
Q) Write a Program to read two lists Num and Denum which contains the Numerators and Denominators 
of some fractions at the respective indexes. Then Display the Smallest Fraction along with it's index.

num = [12,24,35,32,45,11,7]
denum = [2,5,3,8,9,7,5]

Output: 

Smallest Faction is 7/5 which is at index 6.
"""

# num = [12,24,35,32,45,11,7]
# denum = [2,5,3,8,9,7,5]

# print(num)
# print(denum)

# sf = num[1]/denum[1]
# for i in range(len(num)):
#     s1 = num[i]/denum[i]
#     if  s1 < sf:
#         sf = s1
#     else: 
#         sf = sf
# print(f"Smallest Fraction is {num[i]}/{denum[i]}({num[i]/denum[i]}) which is at index {i}")

"""
This Code is Contributed by Himangshu De (himangshu-de)
"""


# Or 

# num = [12,24,35,32,45,11,7]
# denum = [2,5,3,8,9,7,5]
# numerator = 0
# denominator = 0
# smallest_frac = num[0]/denum[0]
# for i in range(len(num)):
#     if num[i] / denum[i] < smallest_frac:
#         numerator = num[i]
#         denominator = denum[i]
#         smallest_frac = num[i]/denum[i]
       
        
#     else:
#         smallest_frac = smallest_frac
#         numerator = numerator
#         denominator = denominator
# print(f"Smallest Fraction in the list is {smallest_frac} \
# ({numerator}/{denominator}) at index {i}")


"""
This code is Contribited by Apurba Ghosh (@iamapurba2003)
"""






"""
Q) Write a Program to compare two equal sized lists and print the first index where they differ.
l = [12,54,24,75,35,21,65,57,21,34]
l2 = [12,54,24,75,35,21,75,21,35,87]

Output:
The two Lists differ at Index 6.
"""




# l = [12,54,24,75,35,21,65,57,21,34]
# l2 = [12,54,24,75,35,21,75,21,35,87]


# for i in range(len(l)):
#     if l[i] != l2[i]:
#         print(f"The two Lists differ at index {i}")
#         break
#     else:
#         continue












"""
Q) Write a Python program to find the list of words that are longer than n from a given list of words, where n is the 
length of the specified word by the user.

l = ["Apurba","Raima","Ruhi","Himangshu","Aniruddha","Rupankar","Arunadaya","Pritha","Pronob"]

Output:
Enter the Word: hellog

The List of words which are longer than the Specified word hellog are:-
1) Himangshu
2) Aniruddha
3) Rupankar
4) Arunadaya

"""



# l = ["Apurba","Raima","Ruhi","Himangshu","Aniruddha","Rupankar","Arunadaya","Pritha","Pronob"]

# user = input("Enter the Word: ")
# output_list = []
# for i in range(len(l)):
#     if len(user) >= len(l[i]):
#         continue
#     else:
#         output_list.append(l[i])

# print()

# index = 1
# for j in range(len(output_list)):
#     print(f"{index}.  {output_list[j]}")
#     index += 1















"""
Q) Write a Python program to select an item randomly from a list.

l = ["Python","Java","C++","C","Ruby","Django","Flask","ReactNative","Mern Stack","JavaScript","TypeScript"]

Output:
The Random Choice of the given list is C++.
"""



# import random
# l = ["Python","Java","C++","C","Ruby","Django","Flask","ReactNative","Mern Stack","JavaScript","TypeScript"]

# ran_choice = random.choice(l)
# print(f"The Random Choice of the given List is {ran_choice}")















































