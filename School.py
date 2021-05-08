
# n = int(input("Enter the Number: "))
# cur = 0
# temp = n
# rev = 0
# count = 0
# while temp != 0:
# 	cur = temp%10
# 	count += 1
# 	temp //= 10
# 	rev = rev*10 + cur

# print("The count is: ",count)
# print("The Reverse is: ",rev)





# string = str(input("Enter a String: "))
# rev = string[::-1]
# i = 0
# for chr in  rev:
#     count = rev[i]
#     i += 1
#     print(count,end = " ")

#  Program to check if a number is an Armstrong Number or not, provided it can be of any digits.

# n = int(input('Enter a Number: '))
# # Section of the Program to find the length of the numeric value entered
# temp2 = n 
# cur2 = 0
# count = 0
# while temp2 != 0:
#     cur = temp2%10
#     count += 1
#     temp2 //= 10

# #  Section to check if if the number entered is an Armstrong Number or not.
# p = count
# arm  = 0
# cur = 0
# temp = n
# while temp != 0:
#     cur = temp%10 
#     arm  = arm + pow(cur,p)
#     temp //= 10
    
# if arm == n:
#     print('This is an Armstrong Number')

# else:
#     print('This is not an Armstrong Number')









# n = int(input("Enter a Number: "))
# rev  = 0 
# while n != 0:
#     rev  = rev*10
#     rev  = rev + n%10
#     n = n//10
# print("The Reversed Number is: ",rev)




























# print("""
# 1
#   2
#     3
# """)

# text = "Test.\nNext line."    ----   Test 
#                                     Next Line
# print(text);

# print('One','Two'*2);

# print("One" + "Two" * 2);

# print(len('0123456789'));

# s = '0123456789'

# print(s[3],",",s[0:3],"-",s[2:5]);

# print(s[:3],"-",s[3:],",",s[3:100]);

# print(s[20:],s[2:1],s[1:1]);

# s = '987654321'

# print(s[-1],s[-3]);

# print(s[-3:],s[:-3]);

# print(s[-100:-3],s[-100:3]);













# 1) Write a Python Program to sum all the items of a List




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






# n  = int(input("Enter the table: "))
# b = int(input("Enter the range: "))
# for i in range(1,b+1):
#     print(n,'x',i,'=',n*i)










# l  = ['Apurba','and','Raima','loves','each','other.']
# i = 0
# for x in l:
#     if i == 1:
#         pass
#     else:
#         print(x,end=" ")
#     i += 1


# print(6/2/2)
# print((2**2)**3)


# ()
# **
# / // * %
# + -






#  Write a Program to Check if the entered number is a Palindrome or not.


# n = int(input("Enter the Numnber: "))
# rev = 0
# temp = n
# cur = 0
# while temp != 0:
#     cur = temp%10
#     temp //= 10
#     rev = rev*10 + cur 
# if n == rev:
#     print("The Entered Number is a Palindrome Number")
# else:
#     print("The Entered Number is not a Palindrome Number")


# for val in range(1, 13):
#     print("No. { } squared is { } and cubed is { }".format(val, val**2, val**3))







# tup = eval(input("Enter: "))
# n = len(tup)
# for val in range(0,n,1):
#     if tup[val] % 2 == 0:
#         print(tup[val], end=" ")
#     else:
#         pass


# t = (10,20,30,40,50,60,70,80,90)
# for i in range(len(t)):
#     print(t[i],end = ",")

# print("\n")
# print("Raima")


# t = (3,4,"Apurba")
# print(t[0::])


# Seraching and Printing the Index of the Element

# tup = (12,25,85,65,20)
# print()
# x  = int(input("Enter the Element to be Searched: "))
# flag  = 0
# for val in range(len(tup)):
#     if tup[val] == x:
#         flag = val
#         print("The Element is found and is in position: ",flag)
#         break
#     if x not in tup:
#         print("The Element is not found")
#         break
#     else:
#         continue
        


# Creation of an Array

# import array as arr 

# a = arr.array('i',[1,2,3])
# print("The Array before insertion is: ", end = " ")
# for i in range(3):
#     print([a[i]],end = " ")

# # Inserting using insert()

# a.insert(3,24)
# print()
# print("The Array after insertion is: ", end = " ")
# for i in a:
#     print([i], end = " ")






# Python program for linked list implementation of stack

# Class to represent a node


# class StackNode:

# 	# Constructor to initialize a node
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None


# class Stack:

# 	# Constructor to initialize the root of linked list
# 	def __init__(self):
# 		self.root = None

# 	def isEmpty(self):
# 		return True if self.root is None else False

# 	def push(self, data):
# 		newNode = StackNode(data)
# 		newNode.next = self.root
# 		self.root = newNode
# 		print ("% d pushed to stack") % (data)

# 	def pop(self):
# 		if (self.isEmpty()):
# 			return float("-inf")
# 		temp = self.root
# 		self.root = self.root.next
# 		popped = temp.data
# 		return popped

# 	def peek(self):
# 		if self.isEmpty():
# 			return float("-inf")
# 		return self.root.data


# # Driver code
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)

# print ("% d popped from stack") % (stack.pop())
# print ("Top element is % d ") % (stack.peek())

# This code is contributed by Apurba Ghosh(iamapurba2003)










"""
Q) Display the elements of a user defined String whose ASCII Value is even
"""

# string = input("Enter a String: ")

# for val in range(len(string)):
#     if (ord(string[val])%2) == 0:
#         print(string[val])
#     else:
#         continue





"""
Q) Take a String from User. Display only even position elements
"""

# string = input("Enter a String: ")
# j = 0
# for val in range(1,len(string)+1):
#     if val%2 == 0:
#         print(string[j])
#         j += 1
#     else:
#         j += 1


# or



# str2 = (input("Enter String: "))
# n = len(str2)

# for i in range(0, n):
#     if i%2 == 0:
#         print(str2[i+1], end = " ")
#     else:
#         continue



































# Binary -> Decimal


# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))


# if user_base == 2:
#     user_input = input("Enter the Number: ")
#     if to_be_converted == 10:
#         list1 = list(user_input)
        
#         # For recognizing the Dot
#         left = []
#         right = []
#         flag = False
#         for val in range(len(list1)):
#             if list1[val] == "." or flag == True:
#                 if list1[val] != ".":
#                     num = int(list1[val])
#                     right.append(num)
#                 else:
#                     flag = True
#                     continue
#             else:
#                 num = int(list1[val])
#                 left.append(num)
        
#         # For Shifting the left elements in list into a variable
        
#         leftmost = 0
#         for val in left:
#             leftmost = leftmost*10 + val
        
#         # For Shifting the right elements in list into a variable
        
#         rightmost = 0
#         for val in right:
#             rightmost = rightmost*10 + val
        
#         # Calculation of the left part
        
#         temp = leftmost
#         sum = 0
#         j = 0
#         while temp != 0:
#             power  = pow(2,j)
#             sum = sum +  temp%10 * power
#             temp //= 10
#             j += 1
            
#         # Calculation of the right part
        
#         sum2 = 0
#         j = -1
#         while right != []:
#             power = pow(2,j)
#             sum2 = sum2 + right[0] * power
#             right.pop(0)
#             j += -1
#         print()       
#         print(f"The Binary -> Decimal Conversion result is {sum+sum2}")    






















#  Binary -> Octal


# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))

# if user_base == 2:
#     user_input = input("Enter the Number: ")

    # if to_be_converted == 8:
        
        # """ For Recognising the Dot """
        # list1 = list(user_input)
        # left = []
        # right = []
        # flag = False
        # for val in range(len(list1)):
        #     if list1[val] == "." or flag == True:
        #         if list1[val] != ".":
        #             num = int(list1[val])
        #             right.append(num)
        #         else:
        #             flag = True
        #             continue
        #     else:
        #         num = int(list1[val])
        #         left.append(num)
                
        # """ For Shifting the left elements in list into a variable """
        
        # leftmost = 0
        # for val in left:
        #     leftmost = leftmost*10 + val
            
               
        # """ For Shifting the right elements in list into a variable """
        
        # rightmost = 0
        # for val in right:
        #     rightmost = rightmost*10 + val

    #     dict = {000 : "0", 1 : "1", 10 : "2", 11 : "3", 100 : "4", 101 : "5", 110 : "6", 111 : "7" }
        
    #     """ Calculation of the left part """
        
    #     temp = leftmost
    #     sum = ''
    #     while temp != 0:
    #         rem = temp%1000
    #         if rem in dict:
    #             sum = sum + dict[rem]
    #             temp//=1000
    #         else:
    #             pass
    #     reverse = sum[::-1]
        
    #     """ Calculation of the right part """
    
        # num = len(right)
        # if num %3 == 0:
        #     temp2 = rightmost
        #     sum = ''
        #     while temp2 != 0:
        #         rem = temp2%1000
        #         if rem in dict:
        #             sum = sum + dict[rem]
        #             temp2//=1000
        #         else:
        #             pass
        #     reverse2 = sum[::-1]
        
        
        # else:
            # numbers = str(rightmost)
            # while num%3 != 0:
            #     numbers = numbers + '0' 
            #     num += 1
            # numbers2 = int(numbers)
            # temp3 = numbers2
        #     sum = ''
        #     while temp3 != 0:
        #         rem = temp3%1000
        #         if rem in dict:
        #             sum = sum + dict[rem]
        #             temp3//=1000
        #         else:
        #             pass
        #     reverse2 = sum[::-1]
    #         print()
    #         print(f"The Binary -> Octal COnversion is {reverse}.{reverse2}")
        
            
        
        
        

# Binary -> Hexadecimal

# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))

# if user_base == 2:
#     user_input = input("Enter the Number: ")
    # if to_be_converted == 16:
        
    #     """ For Recognising the Dot """
    #     list1 = list(user_input)
    #     left = []
    #     right = []
    #     flag = False
    #     for val in range(len(list1)):
    #         if list1[val] == "." or flag == True:
    #             if list1[val] != ".":
    #                 num = int(list1[val])
    #                 right.append(num)
    #             else:
    #                 flag = True
    #                 continue
    #         else:
    #             num = int(list1[val])
    #             left.append(num)
                
    #     """ For Shifting the left elements in list into a variable """
        
    #     leftmost = 0
    #     for val in left:
    #         leftmost = leftmost*10 + val
            
               
    #     """ For Shifting the right elements in list into a variable """
        
    #     rightmost = 0
    #     for val in right:
    #         rightmost = rightmost*10 + val 
        
        
    #     dict = {000 : "0", 1: "1", 10 : "2", 11 : "3", 100 : "4", 101 : "5", 110 : "6", 111 : "7", 1000 : "8", 1001: "9", 1010: "A", 1011 : "B", 1100 : "C", 1101 : "D", 1110 : "E", 1111 : "F"}

        
    #     """ Calculation of the left part """
        
    #     temp = leftmost
    #     sum = ''
    #     while temp != 0:
    #         rem = temp%10000
    #         if rem in dict:
    #             sum = sum + dict[rem]
    #             temp //= 10000
    #         else:
    #             pass
    #     reverse = sum[::-1]
        
      
    #     """ Calculation of the right part"""
        
    #     num = len(right)
    #     if num%4 == 0:
    #         temp2 = leftmost
    #         sum = ''
    #         while temp2 != 0:
    #             rem = temp2%10000
    #             if rem in dict:
    #                 sum = sum + dict[rem]
    #                 temp2 //= 10000
    #             else:
    #                 pass
    #         reverse2 = sum[::-1]
           
        
        
    #     else:
    #         numbers = str(rightmost)
    #         while num%4 != 0:
    #             numbers = numbers + '0' 
    #             num += 1
    #         numbers2 = int(numbers)
    #         temp3 = numbers2
    #         sum = ''
    #         while temp3 != 0:
    #             rem = temp3%10000
    #             if rem in dict:
    #                 sum = sum + dict[rem]
    #                 temp3 //= 10000
    #             else:
    #                 pass
    #         reverse2 = sum[::-1]
            
    #     print(f"The Binary -> Hexadecimal Conversion is {reverse}.{reverse2.rstrip('0')}")






























# Decimal -> Binary 


# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))


# if user_base == 10:
#     user_input = input("Enter the Number: ")
    # if to_be_converted == 2:
        # """ For Recognising the Dot """
        # list1 = list(user_input)
        # left = []
        # right = []
        # flag = False
        # for val in range(len(list1)):
        #     if list1[val] == "." or flag == True:
        #         if list1[val] != ".":
        #             right.append(list1[val])
        #         else:
        #             flag = True
        #             continue
        #     else:
        #         num = int(list1[val])
        #         left.append(num)
                
        # """ For Shifting the left elements in list into a variable """
        
        # leftmost = 0
        # for val in left:
        #     leftmost = leftmost*10 + val
            
               
        # """ For Shifting the right elements in list into a variable """
        
        # rightmost = ''
        # for val in right:
        #     rightmost = rightmost + val 
        
        
    #     """ Calculation of the left part """
        
                
    #     rem = 0
    #     cur = 0
    #     next = leftmost
    #     list_of_numbers = []
    #     while next != 0:
    #         rem = next%2
    #         list_of_numbers.append(rem)
    #         cur = next//2
    #         next = cur 
    #     list_of_numbers.reverse()
    #     numbers = 0
    #     for val in range(len(list_of_numbers)):
    #         numbers = numbers*10 + list_of_numbers[val]
        
    #     print(f"The Leftmost part is {numbers}")
        
        
        
    #     """ Calculation of the right part """
        
        # zeros = '1' + len(rightmost)*'0'
        # length = int(zeros)
        # next = int(rightmost)/length 
        # list_of_numbers = []
        # length = 0
        # while length <= 20:
        #     if next * 2< 1:
        #         list_of_numbers.append(0)
        #         next = next * 2
        #     else:
        #         next = next * 2
        #         num = int(next)
        #         list_of_numbers.append(1)
        #         next = next - num
        #         pass
        #     length += 1
        # numbers2 = ''
        # for val in range(len(list_of_numbers)):
        #     number = str(list_of_numbers[val])
        #     numbers2 = numbers2 + number
    #     print(list_of_numbers)
    #     print(f"The Decimal -> Binary Conversion is {numbers}.{numbers2.rstrip('0')}")
            
        








# Decimal -> Octal

# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))


# if user_base == 10:
#     user_input = input("Enter the Number: ")
#     if to_be_converted == 8:
        
        # """ For Recognising the Dot """
        # list1 = list(user_input)
        # left = []
        # right = []
        # flag = False
        # for val in range(len(list1)):
        #     if list1[val] == "." or flag == True:
        #         if list1[val] != ".":
        #             right.append(list1[val])
        #         else:
        #             flag = True
        #             continue
        #     else:
        #         num = int(list1[val])
        #         left.append(num)
                
        # """ For Shifting the left elements in list into a variable """
        
        # leftmost = 0
        # for val in left:
        #     leftmost = leftmost*10 + val
       
            
               
        # """ For Shifting the right elements in list into a variable """
        
        # rightmost = ''
        # for val in right:
        #     rightmost = rightmost + val 
        
        
        
#         """ Calculating the left part """
        
        
#         rem = 0
#         cur = 0
#         next = leftmost
#         list_of_numbers = []
#         while next != 0:
#             rem = next%8
#             list_of_numbers.append(rem)
#             cur = next//8
#             next = cur
#         list_of_numbers.reverse()
#         numbers = 0
#         for val in range(len(list_of_numbers)):
#             numbers = numbers*10 + list_of_numbers[val]
        
        
        
        
        
#         """ Calculating the right part"""
        
        
        # zeros = '1' + len(rightmost)*'0'
        # length = int(zeros)
        # next = int(rightmost)/length 
        # list_of_numbers = []
        # length = 0
        # while length <= 20:
        #     if next * 8< 1:
        #         list_of_numbers.append(0)
        #         next = next * 8
        #     else:
        #         next = next * 8
        #         num2 = int(next)
        #         num = int(next)
        #         list_of_numbers.append(num2)
        #         next = next - num
        #         pass
        #     length += 1
        # numbers2 = ''
        # for val in range(len(list_of_numbers)):
        #     number = str(list_of_numbers[val])
        #     numbers2 = numbers2 + number
#         print(f"The Decimal -> Octal Conversion is {numbers}.{numbers2.rstrip('0')}")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
# Decimal -> Hexadecimal   

# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))


# if user_base == 10:
#     user_input = input("Enter the Number: ")
    # if to_be_converted == 16:
            
    #     """ For Recognising the Dot """
    #     list1 = list(user_input)
    #     left = []
    #     right = []
    #     flag = False
    #     for val in range(len(list1)):
    #         if list1[val] == "." or flag == True:
    #             if list1[val] != ".":
    #                 right.append(list1[val])
    #             else:
    #                 flag = True
    #                 continue
    #         else:
    #             num = int(list1[val])
    #             left.append(num)
                
    #     """ For Shifting the left elements in list into a variable """
        
    #     leftmost = 0
    #     for val in left:
    #         leftmost = leftmost*10 + val
        
       
            
               
    #     """ For Shifting the right elements in list into a variable """
        
    #     rightmost = ''
    #     for val in right:
    #         rightmost = rightmost + val 
        
            
        
    #     dict = {10: "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
    #     """ Calculation of the left part """
    #     cur = 0
    #     rem = 0
    #     next = leftmost
    #     list_of_numbers = []
    #     while next != 0:
    #         rem = next%16
    #         if rem > 9:
    #             if rem in dict:
    #                 rem = dict[rem]
    #                 list_of_numbers.append(rem)
    #             else:
    #                 pass
    #         else:
    #             list_of_numbers.append(rem)
    #         cur = next//16
    #         next = cur 
    #     list_of_numbers.reverse()
    #     numbers = ''
    #     for val in range(len(list_of_numbers)):
    #         string  = str(list_of_numbers[val])
    #         numbers = numbers + string
        
        
            
            
        
    #     """ Calculation of the right part """
        
        
    #     zeros = '1' + len(rightmost)*'0'
    #     length = int(zeros)
    #     next = int(rightmost)/length 
    #     list_of_numbers = []
    #     length = 0
    #     while length <= 20:
    #         if next * 16< 1:
    #             list_of_numbers.append(0)
    #             next = (next * 16)
    #         else:
    #             next = (next * 16)
    #             num2 = int(next)
    #             if num2 > 9:
    #                 if num2 in dict:
    #                     alter = dict[num2]
    #                     list_of_numbers.append(alter)
    #                 else:
    #                     pass
    #             else:
    #                 list_of_numbers.append(num2)
    #             num = int(next)
    #             next = next - num
    #             pass
    #         length += 1
    #     numbers2 = ''
    #     for val in range(len(list_of_numbers)):
    #         number = str(list_of_numbers[val])
    #         numbers2 = numbers2 + number
            
    #     print(f"The Decimal -> Hexadecimal Conversion is {numbers}.{numbers2.rstrip('0')}")
            
            
            
            
            
            
            
            
            
            
            
# Octal -> Decimal

# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))


# if user_base == 8:
#     user_input = input("Enter the Number: ")
    
#     """ For Recognising the Dot """
#     list1 = list(user_input)
#     left = []
#     right = []
#     flag = False
#     for val in range(len(list1)):
#         if list1[val] == "." or flag == True:
#             if list1[val] != ".":
#                 num = int(list1[val])
#                 right.append(num)
#             else:
#                 flag = True
#                 continue
#         else:
#             num = int(list1[val])
#             left.append(num)
                    
#     """ For Shifting the left elements in list into a variable """
            
#     leftmost = 0
#     for val in left:
#         leftmost = leftmost*10 + val
 
            
        
                
                
#     """ For Shifting the right elements in list into a variable """
            
#     rightmost = 0
#     for val in right:
#         rightmost = rightmost*10 + val 
 
    
    
    
#     """
#     Part to Check if the left part of '.' entered is an Octal Number or not.
#     """
#     check = leftmost
#     flag = False
#     while check != 0:
#         rem = check%10
#         if rem <= 7:
#             check //= 10
#         else:
#             flag = True
#             break
    

    
#     """
#     Part to Check if the left part of '.' entered is an Octal Number or not.
#     """
#     check = rightmost
#     flag2 = False
#     while check != 0:
#         rem = check%10
#         if rem <= 7:
#             check //= 10
#         else:
#             flag2 = True
#             break
    
#     if flag == False and flag2 == False:
#         if to_be_converted == 10:
            
#             """ Calcilation of the left part """
            
#             temp1 = leftmost
#             sum1 = 0
#             rem1 = 0
#             j = 0
#             while temp1 != 0:
#                 rem1 = temp1%10
#                 power = pow(8,j)
#                 sum1 =  sum1 + rem1*power
#                 temp1 //= 10
#                 j += 1
            
            
            
        
#             """ Calculation of the right part """
#             string = str(rightmost)
#             temp2 = list(string)
#             sum2 = 0
#             rem2 = 0
#             j = -1
#             while temp2 != []:
#                 power = pow(8,j)
#                 number = int(temp2[0])
#                 sum2 =  sum2 + number*power
#                 temp2.pop(0)
#                 j -= 1
#             print(f"The Octal -> Decimal Conversion is {sum1+sum2}")
            
            
            
#         # Octal -> Binary Conversion
            
#         if to_be_converted == 2:
#             dict = {0 : "000", 1 : "001", 2 : "010", 3 : "011", 4 : "100", 5 : "101", 6 : "110", 7 : "111"}

#             """ Calculation of the left part """

#             temp2 = leftmost
#             rem2 = 0
#             list_of_numbers = []
#             while temp2 != 0:
#                 rem2 = temp2%10
#                 if rem2 in dict:
#                     list_of_numbers.append(dict[rem2])
#                 temp2 //= 10
#             numbers = ''
#             list_of_numbers.reverse()
#             for val in range(len(list_of_numbers)):
#                 numbers = numbers + list_of_numbers[val]
            
            
            
            
            
#             """ Calculation of the right part """
#             string = str(rightmost)
#             temp3 = list(string)
#             list_of_numbers = []
#             cur = 0
#             while temp3 != []:
#                 cur = int(temp3[0])
#                 if cur in dict:
#                     list_of_numbers.append(dict[cur])
#                 temp3.pop(0)
#             numbers2 = ''
#             for val in list_of_numbers:
#                 numbers2 = numbers2 + val
#             print(f"The Octal -> Binary Conversion is {numbers.lstrip('0')}.{numbers2}")
                
#     else:
#         if flag == True and flag2 == True:
#             print("The entered number is not an Octal Number on both Sides of decimal. Retry Again!")
#         elif flag == True:
#             print()
#             print("The left part of Decimal is not an Octal Number. Retry Again!")
#         elif flag2 == True:
#             print()
#             print("The right part of Decimal is not an Octal Number. Retry Again!")
       
    
            
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
           
    
            
# Hexadecimal -> Decimal Conversion

# user_base = int(input("Enter the base of the number: "))
# to_be_converted = int(input("Enter the base to be Converted: "))

# if user_base == 16:
#     user_input = input("Enter the Number: ")
#     if to_be_converted == 10:
#         temp3 = list(user_input)
#         dict = {'A' : "10", 'B' : "11", 'C' : "12", 'D' : "13", 'E' : "14", 'F' : "15"}
#         for val in range(len(temp3)):
#             if temp3[val] in dict:
#                 temp3[val] = dict[temp3[val]]
#             else:
#                 continue
#         number  = '0'
#         for val in range(len(temp3)):
#             number = number + temp3[val]
#         number.lstrip('0')
#         numbers = int(number)
#         temp4 = numbers
#         rem4 = 0
#         sum4 = 0
#         j = 0
#         dict2 = {'10' : "A", '11' : "B", '12' : "C", '13' : "D", '14' : "E", '15' : "F"}
#         while temp4 != 0:
#             num = temp4%100
#             if str(num) in dict2:
#                 rem4 = temp4%100
#                 temp4 //= 100
#             else:
#                 rem4 = temp4%10
#                 temp4 //= 10
#             power = pow(16,j)
#             sum4 = sum4 + rem4*power
#             j += 1

#         print(f"The Hexadecimal -> Decimal Conversion is {sum4}")
        
        


        












# name = "Tim", 10, "School"
# print(name)

# for t in enumerate("abcdefgh"):
#     index, charecter = t
#     print(index,charecter)


# album = [
#     ("Welcome", "Himangshu", 2004),
#     ("Hello", "Rupankar", 2005),
#     ("Hii!", "Apurba", 2003),
#     ("Whats Up!", "Raima", 2004)
# ]
# for (greeting,name,year) in album :
#     print("Greeting: {0}, Name: {1}, Year: {2}".format(greeting,name,year))











# def multiply(x, y):
#     result = x * y
#     return result

# answer = multiply(10.5, 4)
# print(answer)

# answer = multiply(7, 6)
# print(answer)

# print()
# for val in range(1,5):
#     answer = multiply(2, val)
#     print(answer)




""" To Check if a given Number or Sentence is a Palindrome or not """


# def is_palindrome(string):
#     return string[::-1].casefold() == string.casefold()


# def sentence_palindrome(sentence):
#     charecter = ""
#     for char in sentence:
#         if sentence.isalnum():
#             char += sentence
#     return is_palindrome(charecter)


# user_input = int(input("Enter Your Choice(1 for Word, 2 for sentence): "))

# if user_input == 1:
#     word = input("Enter the Number to check: ")
#     if is_palindrome(word):
#         print(f"{word} is a Palindrome.")
#     else:
#         print(f"{word} is not a Palindrome.")

# if user_input == 2:
#     word = input("Enter the Sentence to check: ")
#     if sentence_palindrome(word):
#         print(f"{word} is a Palindrome.")
#     else:
#         print(f"{word} is not a Palindrome.")
    




""" Write a Program to make a function sum_eo with two parameters n,t where n is the number input and t is either e or o, if t is e 
return all the even number upto n, else if t is o then return all the odd numbers upto n and t is anything other than e or o 
then return -1"""



# def sum_eo(n,t):
#     """Adds the Even or Odd Numbers passed as argument to this function.

#     Args:
#         n (`int`): It is the Positional Parameter for the argument passed by order and holds the integer Value that the User gives. 
#         t (`str`): It is the Positional Parameter for the argument passed by order and holds the string literal to mention whether the type of number entered is `even` or `odd`.

#     Returns:
#         `int`: It returns an integer value based on it's even or odd and -1 if the Positional argument `t` is anything other than `o` or `e`
#     """
    
#     if t == "e":
#         even = 0
#         for val in range(n-1,-1,-1):
#             if val%2 == 0:
#                 even = even*1 + val
#         print(f"The Sum of all the even Numbers upto {n} is {even}")

#     elif t == "o":
#         odd = 0
#         for val in range(n-1,-1,-1):
#             if val%2 != 0:
#                 odd = odd*1 + val
#         print(f"The Sum of all the Odd numbers upto {n} is {odd}")
#     else:
#         print("Please provide a Correct Input.")
#         return -1
        

# user_1 = int(input("Enter the Number: "))
# user_2 = input("Enter the Choice(e/o): ")

# sum_eo(user_1,user_2)








    


# """ Write a Program to print all the Fibonacci Numbers Uto n where n is an user input """

# def fibonacci_numbers(x):
    # """ It generates the Fibonacci Series Upto the given argument x,

    # Args:
    #     x (`int`): It is the Positional argument by passed by order and holds the limit upto which the fibonacci series has to be print in the `int` form.

    # Returns:
    #     `series`: It holds the `Fibonacci Series` which the function returns.
    # """
#     series = [0,1]
#     index = 1
#     for val in range(0,x-2):
#         value = series[index-1] + series[index]
#         series.append(value)
#         index += 1
#     return series


# # def seive_of_list(set,x):
    # """It generates the list passed from the function `fibonacci_numbers` and the user input `n` and convert each element of the list to `str` class and then prints each element with the help of `.join()` method.

    # Args:
    #     set (`list`): It is the positional argument of `value` passed by order contains the `Fibonacci Series` passed from the function `fibonacci_numbers`.
    #     x (`int`): It is the positional argument of `n` passed by order and contains the `user_input`
    # """
# #     for index,val in enumerate(set):
# #         set[index] = str(val)
# #     print(f"The Fibonacci Series upto {x} is ",", ".join(set))

# n = int(input("Enter the term upto for printing the Fibonacci Numbers: "))
# value = fibonacci_numbers(n)
# print(f"The Fibonacci numbers upto {n} is", end=" ")
# print(*value,sep=", ")
# # seive_of_list(value,n)















# import colorama

# # Some ANSI escape sequences for colours and effects
# from tkinter.constants import BOTTOM
# from typing import Any, List


# BLACK = '\u001b[30m'
# RED = '\u001b[31m'
# GREEN = '\u001b[32m'
# YELLOW = '\u001b[33m'
# BLUE = '\u001b[34m'
# MAGENTA = '\u001b[35m'
# CYAN = '\u001b[36m'
# WHITE = '\u001b[37m'
# RESET = '\u001b[0m'
 
# BOLD = '\u001b[1m'
# UNDERLINE = '\u001b[4m'
# REVERSE = '\u001b[7m'

# # print(RED,BOLD, "this will be in red")

# # print(WHITE,BOLD, "this will be in white")

# # print(CYAN, BOLD, "this will be in Cyan", RESET)

# # print("Hello World")


# def colour_print(text: str, *effects: str) -> None:
    
#     effects_string = "".join(effects)
#     output_string = f"{effects_string}{text}{RESET}"
#     print(output_string)



# colour_print("Hello, Red", RED, BOLD)
# print("This should be the default color")
# colour_print("Hello, Blue", BLUE)
# colour_print("Hello, Blue", BLUE, BOLD)
# colour_print("Hello, Yellow", YELLOW)
# colour_print("Hello Bold", BOLD)
# colour_print("Hello Bold", BOLD, GREEN, UNDERLINE)
# colour_print("Hello, Underline", UNDERLINE)
# colour_print("Hello, Reverse", REVERSE)
# colour_print("Hello, Reverse", REVERSE, BLUE, UNDERLINE)
# colour_print("Hello Balck", BLACK)
# colour_print("Hello Magenta", BOLD, MAGENTA)






# l = (21, 52, 63, 85, 96, 105, 113, 153)
# print(l)
# print(*l, sep=", ")




# def test(p1,p2,*args,apu,**kwargs):
#     print(f"Keyword or Positional:...{p1},{p2}")
#     print(f"Var-positional (*args):..{args}")
#     print(f"Keyword:.................{apu}")
#     print(f"Var-Keyword:.............{kwargs}")



# test(1, 2, 4, 5, 6, 7, 8, 9, 10, apu = 11, key1 = 12, key2 = 13)































# dict = {"apple": "A crunchy fruit",
#         "grape": "A small green sweet fruit",
#         "orange": "A bulged sour fruit",
#         "apple": "A good fruit"}

# # dict["apple"] = "A good fruit"
# description = dict.get("apple")
# print(description)






# jabber = open('test.txt','r')
# for line in jabber:
#     print(line)
    
# jabber.close()


# with open('test.txt','r') as jabber:
#     for line in jabber:
#         print(line)

# with open('test.txt','r') as jabber:
#     readline = jabber.readline()
#     while readline:
#         print(readline, end =" ")
#         readline = jabber.readline()




# data = dict(zip(('name','class'), ('Apurba',11)))
# print(data)







# Employee = {'name':'John', 'Salary':12500, 'age': 23, 'dept':'Production'}
# print("All Elements of the Dictionary -Employee")
# print(Employee)
# print()
# print("Keys of Dictionary - Employee: ", end = " ")
# for k in Employee.keys():
#     print(k,end=", ")

# print()
# print("Thank You")

# Employee = {'name':'John', 'Salary':'12500', 'age': '23', 'dept':'Production'}
# value = Employee.values()
# print("All Elements of the Dictionary - Employee")
# print(Employee)
# print()
# print("Values of Dictionary - Employee: ",end=" ")
# print(", ".join(value))

# print()
# print("Thank You")










# dic = {"apurba":"A good boy", "raima":"A good Girl", "himangshu":"A good Friend"}

# ordered_keys = list(dic.keys())
# print(ordered_keys)
# ordered_keys.sort()
        # or

# ordered_keys = sorted(list(dic.keys()))
# for f in ordered_keys:
#     print(f,"-",dic[f])

        # or

# for f in sorted(dic.keys()):
#     print(f,"-",dic[f])


# f = dic.keys()
# print(f)

# user = input("Enter the Key to Search the Dictionary: ")
# print(dic.get(user.casefold(),"We dont have "+user))



# import pymongo

# myclient = pymongo.MongoClient("mongodb://localhost:15124")

# mydb = myclient["mydatabase"]

# mycol = mydb["Customers"]
# print(mydb.list_collection_names())


# nd3 = dict.fromkeys([10,20],"Apurba")
# print(nd3)



# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# car.update({"model":"Bronco"})

# print(car)





























# dic = {1 : "Robotics and Control System", 2 : "Microprocessors and Electronics", 3 : "Neural Networks", 4 : "Microcontrollers"}


# print(min(dic))


# week = {"MONDAY" : 1, "TUESDAY" : 2, "WEDNWSDAY" : 3, "THURSDAY" : 4, "FRIDAY": 5}



""" 
Write a Program in Python to create a dictionary Vowel from the User and then search data continuously in the dictionary
whose key will be given by the User again.
"""


# def showdict(k : tuple, z : tuple) -> dict:
#     Employee = dict(zip(k,z))
#     print(f"{YELLOW} The Keys present in the Dictionary are {GREEN} \"{Employee.keys()}\" {RESET}")
#     return Employee


# def search(l : dict):
#     print()
#     print("""Please enter the Keys one at a time to search the Vowels and 
#           enter 'exit' to Quit. """)
#     print()
#     search = input("Enter the Key for the Corresponding Vowel to be Searched: ")
#     while True:
#         if search == 'exit':
#             print()
#             print(f"{BLUE} Thank You {RESET}")
#             break
#         for val in range(1):
#             if int(search) in l.keys():
#                 print(f"{MAGENTA} \"The Vowel is {l[int(search)]}\" {RESET}")
#                 print()
#             else:
#                 print()
#                 print(f"{RED} Please Enter a Valid key {RESET}")
#                 print()
#         search = input("Enter the Key for the Corresponding Vowel to be Searched: ")      
            
        


# t1 = eval(input("Enter the Keys: "))
# t2 = eval(input("Enter the Values: "))

# data = showdict(t1,t2)
# search(data)


# from ArcticCloud import BaseConverter as bk 
# from ArcticCloud import MarkSheet as mk

# v1 = bk.Decimal_to_Binary("55894.554675")
# # print(v1)

# mk.PrintMarksheet("Satish Chandra Memorial School",[100,100,100,100,100,99],["Apurba Ghosh","C",5,"XII"])


# old = {'age' : 25}
# new = old.copy()
# new['age'] = 30
# print(new)
# print(old)

# a = {(1,2) : 101, (2,3) : 202, {1:1,2:2} : 303}
# print(a(1,2))












# from ArcticCloud import BaseConverter as bk 

# v1 = bk.Decimal_to_Hexadecimal("5896.2564")
# print(v1)














# data_dic = {'a': " ", 'b': " ", 'c': " ", 'd': " ", 'e': " ", 'f': " ", 'g': " ", 'h': " ", 'i': " "}
# Choice_dict = {'Player 1' : " ", 'Player 2' : " "}
# raw = Choice_dict.items()
# win_tuple = tuple(raw)   
# GREEN = '\u001b[32m'
# YELLOW = '\u001b[33m'
# RESET = '\u001b[0m'
# RED = '\u001b[31m'
# CYAN = '\u001b[36m'
# MAGENTA = '\u001b[35m'
# BOLD = '\u001b[1m'

# def board(container : str = "", screenwidth : int = 59, sign1 = " ", sign2 = " ", sign3 = " "):
#     counter = 0
#     while counter <= 21:
#         if counter == 0 or counter == 14 or counter == 7 or counter == 21:
#             container = "-" * screenwidth
#             print(container)
#             counter += 1
#             continue
        
#         if counter == 3:
#             container = f"|          {data_dic['a']}       |          {data_dic['b']}        |          {data_dic['c']}       |" f"{sign1}"
#             print(container)
#             counter += 1 
#             continue
        
#         if counter == 10 :
#             container = f"|          {data_dic['d']}       |          {data_dic['e']}        |          {data_dic['f']}       |" f"{sign2}"
#             print(container)
#             counter += 1
#             continue
            
#         if counter == 17:
#             container = f"|          {data_dic['g']}       |          {data_dic['h']}        |          {data_dic['i']}       |" f"{sign3}"
#             print(container)
#             counter += 1
#             continue
            
#         else:
#             container = "|                  |                   |                  |"
#             print(container)
#             counter += 1
               
        
# def check(a : str ,b : str ,c : str ,d : str ,e : str ,f : str ,g : str ,h : str ,i : str ):
    
#     # Part 1:
#     if data_dic.get(a) == data_dic.get(b) == data_dic.get(c) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     if data_dic.get(a) == data_dic.get(b) == data_dic.get(c) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     if data_dic.get(d) == data_dic.get(e) == data_dic.get(f) == "X":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return d

#     if data_dic.get(d) == data_dic.get(e) == data_dic.get(f) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return d

#     if data_dic.get(g) == data_dic.get(h) == data_dic.get(i) == "X":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return g
        
#     if data_dic.get(g) == data_dic.get(h) == data_dic.get(i) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return g
    
    
#     # Part 2:
#     if data_dic.get(a) == data_dic.get(d) == data_dic.get(g) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a
    
#     if data_dic.get(a) == data_dic.get(d) == data_dic.get(g) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a
    
#     if data_dic.get(b) == data_dic.get(e) == data_dic.get(h) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return b
    
#     if data_dic.get(b) == data_dic.get(e) == data_dic.get(h) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return b
    
#     if data_dic.get(c) == data_dic.get(f) == data_dic.get(i) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    
#     if data_dic.get(c) == data_dic.get(f) == data_dic.get(i) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    

    
#     # Part 3:
#     if (data_dic.get(a) == data_dic.get(e) == data_dic.get(i)) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     elif (data_dic.get(a) == data_dic.get(e) == data_dic.get(i)) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     elif data_dic.get(c) == data_dic.get(e) == data_dic.get(g) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c

#     elif data_dic.get(c) == data_dic.get(e) == data_dic.get(g) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    
#     else:
#         return " "
    
    
      


# def overwrite(user : tuple):
#     if data_dic[user[1]] != " ":
#         print("Sorry the Column is already filled, Please Choose any other Column...")
#         return True
#     else:
#         return False

 
# def game():
#     board()
#     winner = ""
#     counter = 1
#     continuous_check = " "
#     f = ""
#     while counter <= 9:
#         if counter%2 != 0:
#             user1 = eval(input("Player 1, Enter the Cloumn: "))
#             if user1[0] == 'exit':
#                 print("Thanks For Playing")
#                 f = 'a'
#                 break
#             if Choice_dict['Player 1'] == " ":
#                 pass
#             else:
#                 if Choice_dict['Player 1'] == user1[0]:
#                     pass
#                 else:
#                     print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
#                     user1 = eval(input("Player 1, Enter the Cloumn: "))
#                     if user1[0] == 'exit':
#                         print("Thanks For Playing")
#                         f = 'a'
#                         break
#                     else:
#                         pass
#             info = overwrite(user1)
#             if info == True:
#                 user1 = eval(input("Player 1, Enter the Cloumn: "))
#                 info2 = overwrite(user1)
#                 if info2 == True:
#                     user1 = eval(input("Player 1, Enter the Cloumn: "))
#                 else:
#                     pass
#             else:
#                 pass
            
#             if user1[1] == 'a':
#                 data_dic['a'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'b':
#                 data_dic['b'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'c':
#                 data_dic['c'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'd':
#                 data_dic['d'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'e':
#                 data_dic['e'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'f':
#                 data_dic['f'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'g':
#                 data_dic['g'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'h':
#                 data_dic['h'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'i':
#                 data_dic['i'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             Choice_dict['Player 1'] = user1[0]
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                    ,data_dic['g'],data_dic['h'],data_dic['i'])
#             if winner != " ":
#                 continuous_check = (True,winner)
#                 break
#         else:
#             user2 = eval(input("Player 2, Enter the Column: "))
#             if user2[0] == 'exit':
#                 print("Thanks For Playing")
#                 f = 'b'
#                 break
#             if Choice_dict['Player 2'] == " ":
#                 pass
#             else:
#                 if Choice_dict['Player 2'] == user2[0]:
#                     pass
#                 else:
#                     print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
#                     user2 = eval(input("Player 2, Enter the Cloumn: "))
#                     if user2[0] == 'exit':
#                         print("Thanks For Playing")
#                         f = 'b'
#                         break
#                     else:
#                         pass
#             info = overwrite(user2)
#             if info == True:
#                 user2 = eval(input("Player 2, Enter the Cloumn: "))
#                 info2 = overwrite(user2)
#                 if info2 == True:
#                     user2 = eval(input("Player 2, Enter the Cloumn: "))
#                 else:
#                     pass
#             else:
#                 pass
            
#             if user2[1] == 'a':
#                 data_dic['a'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'b':
#                 data_dic['b'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'c':
#                 data_dic['c'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'd':
#                 data_dic['d'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'e':
#                 data_dic['e'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'f':
#                 data_dic['f'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'g':
#                 data_dic['g'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'h':
#                 data_dic['h'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'i':
#                 data_dic['i'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
                
#             Choice_dict['Player 2'] = user2[0]
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                    ,data_dic['g'],data_dic['h'],data_dic['i'])
#             if winner != " ":
#                 continuous_check = (True,winner)
#                 break


#         counter += 1
    
    
#     if f == 'a' or f == 'b':
#         pass
#     else:
#         if continuous_check[0] == True:
#             print(f"{MAGENTA}Congratulations! Winner of the Game is {continuous_check[1]}")
#         else:
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                 ,data_dic['g'],data_dic['h'],data_dic['i'])
#             print(f"{BOLD}{winner}")
        
# if __name__ == '__main__':
#     game()
    
    
# """ 
# My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
# in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
# Also the Colors of each Variable and the Arrows pointing to the current input column is given, the Warning situation such as If entered a column 
# already filled then it will give warning and choice to re-enter twice and if Choosed a variable which is not the same as choosed in the beginning
# it will give a Warning and choice to re-enter once etc.
# """
  


# data_dic = {'a': " ", 'b': " ", 'c': " ", 'd': " ", 'e': " ", 'f': " ", 'g': " ", 'h': " ", 'i': " "}
# Choice_dict = {'Player 1' : " ", 'Player 2' : " "}
# raw = Choice_dict.items()
# win_tuple = tuple(raw)   
# GREEN = '\u001b[32m'
# YELLOW = '\u001b[33m'
# RESET = '\u001b[0m'
# RED = '\u001b[31m'
# CYAN = '\u001b[36m'
# MAGENTA = '\u001b[35m'
# BOLD = '\u001b[1m'

# def board(container : str = "", screenwidth : int = 59, sign1 = " ", sign2 = " ", sign3 = " "):
#     counter = 0
#     while counter <= 21:
#         if counter == 0 or counter == 14 or counter == 7 or counter == 21:
#             container = "-" * screenwidth
#             print(container)
#             counter += 1
#             continue
        
#         if counter == 3:
#             container = f"|          {data_dic['a']}       |          {data_dic['b']}        |          {data_dic['c']}       |" f"{sign1}"
#             print(container)
#             counter += 1 
#             continue
        
#         if counter == 10 :
#             container = f"|          {data_dic['d']}       |          {data_dic['e']}        |          {data_dic['f']}       |" f"{sign2}"
#             print(container)
#             counter += 1
#             continue
            
#         if counter == 17:
#             container = f"|          {data_dic['g']}       |          {data_dic['h']}        |          {data_dic['i']}       |" f"{sign3}"
#             print(container)
#             counter += 1
#             continue
            
#         else:
#             container = "|                  |                   |                  |"
#             print(container)
#             counter += 1
               
        
# def check(a : str ,b : str ,c : str ,d : str ,e : str ,f : str ,g : str ,h : str ,i : str ):
    
#     # Part 1:
#     if data_dic.get(a) == data_dic.get(b) == data_dic.get(c) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     if data_dic.get(a) == data_dic.get(b) == data_dic.get(c) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     if data_dic.get(d) == data_dic.get(e) == data_dic.get(f) == "X":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return d

#     if data_dic.get(d) == data_dic.get(e) == data_dic.get(f) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return d

#     if data_dic.get(g) == data_dic.get(h) == data_dic.get(i) == "X":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return g
        
#     if data_dic.get(g) == data_dic.get(h) == data_dic.get(i) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return g
    
    
#     # Part 2:
#     if data_dic.get(a) == data_dic.get(d) == data_dic.get(g) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a
    
#     if data_dic.get(a) == data_dic.get(d) == data_dic.get(g) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a
    
#     if data_dic.get(b) == data_dic.get(e) == data_dic.get(h) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return b
    
#     if data_dic.get(b) == data_dic.get(e) == data_dic.get(h) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return b
    
#     if data_dic.get(c) == data_dic.get(f) == data_dic.get(i) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    
#     if data_dic.get(c) == data_dic.get(f) == data_dic.get(i) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    

    
#     # Part 3:
#     if (data_dic.get(a) == data_dic.get(e) == data_dic.get(i)) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     elif (data_dic.get(a) == data_dic.get(e) == data_dic.get(i)) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     elif data_dic.get(c) == data_dic.get(e) == data_dic.get(g) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c

#     elif data_dic.get(c) == data_dic.get(e) == data_dic.get(g) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    
#     else:
#         return " "
    
    
      


# def overwrite(user : tuple):
#     if data_dic[user[1]] != " ":
#         print("Sorry the Column is already filled, Please Choose any other Column...")
#         return True
#     else:
#         return False

 
# def game():
#     board()
#     winner = ""
#     counter = 1
#     continuous_check = " "
#     f = ""
#     while counter <= 9:
#         if counter%2 != 0:
#             user1 = eval(input("Player 1, Enter the Cloumn: "))
#             if user1[0] == 'exit':
#                 print("Thanks For Playing")
#                 f = 'a'
#                 break
#             if Choice_dict['Player 1'] == " ":
#                 pass
#             else:
#                 if Choice_dict['Player 1'] == user1[0]:
#                     pass
#                 else:
#                     print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
#                     user1 = eval(input("Player 1, Enter the Cloumn: "))
#                     if user1[0] == 'exit':
#                         print("Thanks For Playing")
#                         f = 'a'
#                         break
#                     else:
#                         pass
#             info = overwrite(user1)
#             if info == True:
#                 user1 = eval(input("Player 1, Enter the Cloumn: "))
#                 info2 = overwrite(user1)
#                 if info2 == True:
#                     user1 = eval(input("Player 1, Enter the Cloumn: "))
#                 else:
#                     pass
#             else:
#                 pass
            
#             if user1[1] == 'a':
#                 data_dic['a'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'b':
#                 data_dic['b'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'c':
#                 data_dic['c'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'd':
#                 data_dic['d'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'e':
#                 data_dic['e'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'f':
#                 data_dic['f'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'g':
#                 data_dic['g'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'h':
#                 data_dic['h'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'i':
#                 data_dic['i'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             Choice_dict['Player 1'] = user1[0]
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                    ,data_dic['g'],data_dic['h'],data_dic['i'])
#             if winner != " ":
#                 continuous_check = (True,winner)
#                 break
#         else:
#             user2 = eval(input("Player 2, Enter the Column: "))
#             if user2[0] == 'exit':
#                 print("Thanks For Playing")
#                 f = 'b'
#                 break
#             if Choice_dict['Player 2'] == " ":
#                 pass
#             else:
#                 if Choice_dict['Player 2'] == user2[0]:
#                     pass
#                 else:
#                     print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
#                     user2 = eval(input("Player 2, Enter the Cloumn: "))
#                     if user2[0] == 'exit':
#                         print("Thanks For Playing")
#                         f = 'b'
#                         break
#                     else:
#                         pass
#             info = overwrite(user2)
#             if info == True:
#                 user2 = eval(input("Player 2, Enter the Cloumn: "))
#                 info2 = overwrite(user2)
#                 if info2 == True:
#                     user2 = eval(input("Player 2, Enter the Cloumn: "))
#                 else:
#                     pass
#             else:
#                 pass
            
#             if user2[1] == 'a':
#                 data_dic['a'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'b':
#                 data_dic['b'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'c':
#                 data_dic['c'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'd':
#                 data_dic['d'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'e':
#                 data_dic['e'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'f':
#                 data_dic['f'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'g':
#                 data_dic['g'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'h':
#                 data_dic['h'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'i':
#                 data_dic['i'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
                
#             Choice_dict['Player 2'] = user2[0]
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                    ,data_dic['g'],data_dic['h'],data_dic['i'])
#             if winner != " ":
#                 continuous_check = (True,winner)
#                 break


#         counter += 1
    
    
#     if f == 'a' or f == 'b':
#         pass
#     else:
#         if continuous_check[0] == True:
#             print(f"{MAGENTA}Congratulations! Winner of the Game is {continuous_check[1]}")
#         else:
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                 ,data_dic['g'],data_dic['h'],data_dic['i'])
#             print(f"{BOLD}{winner}")
        
# if __name__ == '__main__':
#     game()
    
    
""" 
My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
Also the Colors of each Variable and the Arrows pointing to the current input column is given, the Warning situation such as If entered a column 
already filled then it will give warning and choice to re-enter twice and if Choosed a variable which is not the same as choosed in the beginning
it will give a Warning and choice to re-enter once etc.
"""
  





# data_dic = {'a': " ", 'b': " ", 'c': " ", 'd': " ", 'e': " ", 'f': " ", 'g': " ", 'h': " ", 'i': " "}
# Choice_dict = {'Player 1' : " ", 'Player 2' : " "}
# raw = Choice_dict.items()
# win_tuple = tuple(raw)
# GREEN = '\u001b[32m'
# YELLOW = '\u001b[33m'
# RESET = '\u001b[0m'
# RED = '\u001b[31m'
# CYAN = '\u001b[36m'
# MAGENTA = '\u001b[35m'
# BOLD = '\u001b[1m'

# def board(container : str = "", screenwidth : int = 59, sign1 = " ", sign2 = " ", sign3 = " "):
#     counter = 0
#     while counter <= 21:
#         if counter == 0 or counter == 14 or counter == 7 or counter == 21:
#             container = "-" * screenwidth
#             print(container)
#             counter += 1
#             continue
        
#         if counter == 3:
#             container = f"|          {data_dic['a']}       |          {data_dic['b']}        |          {data_dic['c']}       |" f"{sign1}"
#             print(container)
#             counter += 1 
#             continue
        
#         if counter == 10 :
#             container = f"|          {data_dic['d']}       |          {data_dic['e']}        |          {data_dic['f']}       |" f"{sign2}"
#             print(container)
#             counter += 1
#             continue
            
#         if counter == 17:
#             container = f"|          {data_dic['g']}       |          {data_dic['h']}        |          {data_dic['i']}       |" f"{sign3}"
#             print(container)
#             counter += 1
#             continue
            
#         else:
#             container = "|                  |                   |                  |"
#             print(container)
#             counter += 1
               
        
# def check(a : str ,b : str ,c : str ,d : str ,e : str ,f : str ,g : str ,h : str ,i : str ):
    
#     # Part 1:
#     if data_dic.get(a) == data_dic.get(b) == data_dic.get(c) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     if data_dic.get(a) == data_dic.get(b) == data_dic.get(c) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     if data_dic.get(d) == data_dic.get(e) == data_dic.get(f) == "X":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return d

#     if data_dic.get(d) == data_dic.get(e) == data_dic.get(f) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return d

#     if data_dic.get(g) == data_dic.get(h) == data_dic.get(i) == "X":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return g
        
#     if data_dic.get(g) == data_dic.get(h) == data_dic.get(i) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return g
    
    
#     # Part 2:
#     if data_dic.get(a) == data_dic.get(d) == data_dic.get(g) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a
    
#     if data_dic.get(a) == data_dic.get(d) == data_dic.get(g) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a
    
#     if data_dic.get(b) == data_dic.get(e) == data_dic.get(h) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return b
    
#     if data_dic.get(b) == data_dic.get(e) == data_dic.get(h) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return b
    
#     if data_dic.get(c) == data_dic.get(f) == data_dic.get(i) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    
#     if data_dic.get(c) == data_dic.get(f) == data_dic.get(i) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    

    
#     # Part 3:
#     if (data_dic.get(a) == data_dic.get(e) == data_dic.get(i)) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     elif (data_dic.get(a) == data_dic.get(e) == data_dic.get(i)) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return a

#     elif data_dic.get(c) == data_dic.get(e) == data_dic.get(g) == "X":
#         if win_tuple[0][1] == "X":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "X":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c

#     elif data_dic.get(c) == data_dic.get(e) == data_dic.get(g) == "O":
#         if win_tuple[0][1] == "O":
#             print(f"{MAGENTA} Congratulations! The winner is Player1{RESET}")
#         if win_tuple[1][1] == "O":
#             print(f"{MAGENTA}Congratulations! The winner is Player2{RESET}")
#         return c
    
#     else:
#         return " "
    
    
      


# def overwrite(user : tuple):
#     if data_dic[user[1]] != " ":
#         print("Sorry the Column is already filled, Please Choose any other Column...")
#         return True
#     else:
#         return False

 
# def game():
#     board()
#     winner = ""
#     counter = 1
#     continuous_check = " "
#     f = ""
#     while counter <= 9:
#         if counter%2 != 0:
#             user1 = eval(input("Player 1, Enter the Cloumn: "))
#             if user1[0] == 'exit':
#                 print("Thanks For Playing")
#                 f = 'a'
#                 break
#             if Choice_dict['Player 1'] == " ":
#                 pass
#             else:
#                 if Choice_dict['Player 1'] == user1[0]:
#                     pass
#                 else:
#                     print(f"Sorry You can't take {user1[0]}, You have to choose {Choice_dict['Player 1']}")
#                     user1 = eval(input("Player 1, Enter the Cloumn: "))
#                     if user1[0] == 'exit':
#                         print("Thanks For Playing")
#                         f = 'a'
#                         break
#                     else:
#                         pass
#             info = overwrite(user1)
#             if info == True:
#                 user1 = eval(input("Player 1, Enter the Cloumn: "))
#                 info2 = overwrite(user1)
#                 if info2 == True:
#                     user1 = eval(input("Player 1, Enter the Cloumn: "))
#                 else:
#                     pass
#             else:
#                 pass
            
#             if user1[1] == 'a':
#                 data_dic['a'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'b':
#                 data_dic['b'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'c':
#                 data_dic['c'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign1=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'd':
#                 data_dic['d'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'e':
#                 data_dic['e'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'f':
#                 data_dic['f'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign2=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'g':
#                 data_dic['g'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'h':
#                 data_dic['h'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             if user1[1] == 'i':
#                 data_dic['i'] = f"{RED}{user1[0]}{RESET}"
#                 board(sign3=f"{GREEN} <--- {RESET}")
#             Choice_dict['Player 1'] = user1[0]
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                    ,data_dic['g'],data_dic['h'],data_dic['i'])
#             if winner != " ":
#                 continuous_check = (True,winner)
#                 break
#         else:
#             user2 = eval(input("Player 2, Enter the Column: "))
#             if user2[0] == 'exit':
#                 print("Thanks For Playing")
#                 f = 'b'
#                 break
#             if Choice_dict['Player 2'] == " ":
#                 pass
#             else:
#                 if Choice_dict['Player 2'] == user2[0]:
#                     pass
#                 else:
#                     print(f"Sorry You can't take {user2[0]}, You have to choose {Choice_dict['Player 2']}")
#                     user2 = eval(input("Player 2, Enter the Cloumn: "))
#                     if user2[0] == 'exit':
#                         print("Thanks For Playing")
#                         f = 'b'
#                         break
#                     else:
#                         pass
#             info = overwrite(user2)
#             if info == True:
#                 user2 = eval(input("Player 2, Enter the Cloumn: "))
#                 info2 = overwrite(user2)
#                 if info2 == True:
#                     user2 = eval(input("Player 2, Enter the Cloumn: "))
#                 else:
#                     pass
#             else:
#                 pass
            
#             if user2[1] == 'a':
#                 data_dic['a'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'b':
#                 data_dic['b'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'c':
#                 data_dic['c'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign1=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'd':
#                 data_dic['d'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'e':
#                 data_dic['e'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'f':
#                 data_dic['f'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign2=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'g':
#                 data_dic['g'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'h':
#                 data_dic['h'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
#             if user2[1] == 'i':
#                 data_dic['i'] = f"{CYAN}{user2[0]}{RESET}"
#                 board(sign3=f"{YELLOW} <--- {RESET}")
                
#             Choice_dict['Player 2'] = user2[0]
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                    ,data_dic['g'],data_dic['h'],data_dic['i'])
#             if winner != " ":
#                 continuous_check = (True,winner)
#                 break


#         counter += 1
    
    
#     if f == 'a' or f == 'b':
#         pass
#     else:
#         if continuous_check[0] == True:
#             print(f"{MAGENTA}Congratulations! Winner of the Game is {continuous_check[1]}")
#         else:
#             winner = check(data_dic['a'],data_dic['b'],data_dic['c'],data_dic['d'],data_dic['e'],data_dic['f']
#                 ,data_dic['g'],data_dic['h'],data_dic['i'])
#             print(f"{BOLD}{winner}")


# raw = Choice_dict.items()
# win_tuple = tuple(raw)

# if __name__ == '__main__':
#     game()
   
    
""" 
My Approach is that I will create  a dictionary and each time a column is filed I will pass the column name and the value given to that column
in the dictionary and while giving input I will check if that column is already filled and also the checking will be done using the dictionary.
Also the Colors of each Variable and the Arrows pointing to the current input column is given, the Warning situation such as If entered a column 
already filled then it will give warning and choice to re-enter twice and if Choosed a variable which is not the same as choosed in the beginning
it will give a Warning and choice to re-enter once etc.
"""
  

















# We will prepare board for the chess game
# Asking user for color choice
#Swap players
#Cutting or eleminating the opponent's card

# BLACK = '\u001b[30m'
# RED = '\u001b[31m'
# GREEN = '\u001b[32m'
# YELLOW = '\u001b[33m'
# BLUE = '\u001b[34m'
# MAGENTA = '\u001b[35m'
# CYAN = '\u001b[36m'
# WHITE = '\u001b[37m'
# RESET = '\u001b[0m'

# BOLD = '\u001b[1m'
# UNDERLINE = '\u001b[4m'
# REVERSE = '\u001b[7m'

# chess_pos = ['Bishop', 'Knight', 'Rook', 'King', 'Queen', 'Pawns', '     ']

# def chessboard():
#     i = 0
#     while i<33:
#         if i == 0:
#             print('-'*66, i)
        
#         elif i == 2:
#             print(f"|  {chess_pos[2]}  | {chess_pos[1]}| {chess_pos[0]}| {chess_pos[4]} | {chess_pos[3]}  | {chess_pos[0]}| {chess_pos[1]}| {chess_pos[2]}  |", i)
        
#         elif i == 4:
#             print('-'*66,i)

#         elif i == 6:
#             print(f"| {chess_pos[5]}  | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} |", i)
        
#         elif i == 8:
#             print('-'*66,i)
        
#         elif i == 10:
#             print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

#         elif i == 12:
#             print('-'*66,i)
        
#         elif i == 14:
#             print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

#         elif i == 16:
#             print('-'*66,i)
        
#         elif i == 18:
#             print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

#         elif i == 20:
#             print('-'*66,i)
        
#         elif i == 22:
#             print(f"| {chess_pos[6]}  | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} | {chess_pos[6]} |", i)

#         elif i == 24:
#             print('-'*66,i)
        
#         elif i == 26:
#             print(f"| {chess_pos[5]}  | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} | {chess_pos[5]} |", i)
                
#         elif i == 28:
#             print('-'*66,i)
        
#         elif i == 30:
#             print(f"|  {chess_pos[2]}  | {chess_pos[1]}| {chess_pos[0]}| {chess_pos[4]} | {chess_pos[3]}  | {chess_pos[0]}| {chess_pos[1]}| {chess_pos[2]}  |", i)
        
#         elif i == 32:
#             print('-'*66,i)

#         else:
#             print("| \t | \t | \t | \t | \t | \t | \t | \t |", i)
        
#         i+=1


# if __name__ == "__main__":
#     chessboard()



# # Left Side triangle
# n = int(input("Enter the Number of Rows: "))
# for i in range(0,n):
#     for j in range(0,i+1):
#         print('*',end=" ")
#     print()

# # Right diagonal Triangle
# n = int(input("Enter the Number of Rows: "))
# spaces = n-1
# k = n 
# for i in range(0,n):
#     print(" "*(spaces+n),end=" ")
#     for j in range(k,n+1):
#         print('*',end=" ")
#     spaces-=2
#     k -= 1
#     print()
    
# # Equilateral Triangle
# n = int(input("Enter the Number of rows: "))
# spaces=n
# for i in range(0,n):
#     for j in range(spaces-1,0,-1):
#         print(" ",end="")
#     for m in range(i+1):
#         print("*",end=" ")
#     print()
#     spaces-=1






# RED = '\u001b[31m'
# GREEN = '\u001b[32m'

# userString = input("Enter the String: ")
# lowercase = ""
# uppercase = ""
# for val in userString:
#     if val == val.upper():
#         uppercase = val
#         print(f"The letter {uppercase} is Capital letter.")
#         print()
#     if val == val.lower():
#         lowercase = val
#         print(f"The letter {lowercase} is Small letter.")
#         print()


# userList = eval(input("Enter the List: "))
# length = len(userList)-1
# print(f"The List before Starting the Program is {userList}")
# print()
# for i in range(len(userList)):
#     print(f"{RED}The Element Deleted is --> {userList[length]}{RESET}")
#     userList.pop(length)
#     length = length-1
#     print(f"{GREEN}Present List is {userList}{RESET}")
#     print()
    
# print("Now the entered List is Empty, Congratulations!..")




# import datetime as dt
# import tkinter as tk
# from tkinter import ttk

# dateTime = dt.datetime.now()

# master = tk.Tk()
# master.title("Apurba's Greeting Software")

# userName = tk.StringVar()

# master.geometry("550x300")



# label = ttk.Label(master, text=f"Hello!", foreground= "Blue")
# label.pack(side= 'top', ipadx=5, ipady=5)

# if dateTime.strftime("%H") >= "0" and dateTime.strftime("%H") <"12":
#     label = ttk.Label(master, text= "Good Morning!", foreground="Blue")
#     label.pack(side="top")

# if dateTime.strftime("%H%M") =="1200":
#     label = ttk.Label(master, text="Good Noon!", foreground="Blue")
#     label.pack(side="top")

# if dateTime.strftime("%H") >="12" and dateTime.strftime("%H%M") <"1630":
#     label= ttk.Label(master, text="Good Afternoon!", foreground="Blue")
#     label.pack(side="top")

# if dateTime.strftime("%H%M")>="1630" and dateTime.strftime("%H%M")<"1959":
#     label = ttk.Label(master, text="Good Evening!", foreground="Blue")
#     label.pack(side="top")

# else:
#     label = ttk.Label(master, text="Good Night! Sweet Dreams", foreground="Blue")
#     label.pack(side="top")

# label = ttk.Label(master, text=f"{dateTime.strftime('%A  %d - %b - %Y')}\n{dateTime.strftime('%I:%M:%S %p')}", foreground= "Blue")
# label.pack(side= 'left', ipadx=5, ipady=5)



# button = ttk.Button(master, text="Close This Dialogue", command=master.destroy).place(x=213, y= 250 )

# master.mainloop()














# from tkinter import *
# from tkinter.ttk import *

# def listAppend():
#     list1=[]
#     user1 = userInput.get()
#     pwd = password.get()
#     list1.extend([user1,pwd])
#     newLabel = Label(root, text="Sign up Successful!")
#     newLabel.grid()
#     print(list1)
#     newButton1 = Button(root,text="Quit",command=root.destroy)
#     newButton1.grid()
    
#     return True
    



# root = Tk()

# root.geometry("500x500")
# root.title("SignUp Page")

# userInput= StringVar()
# password = StringVar()

# nameLabel = Label(root, text='User Name: ')
# nameLabel.grid(row=0, column=0)

# nameEntry = Entry(root, width=20, textvariable=userInput)
# nameEntry.grid(row=0, column=1)
# nameEntry.focus()

# passLabel = Label(root,text="Password: ")
# passLabel.grid(row=1, column=0)

# passEntry =  Entry(root, width=20,textvariable=password)
# passEntry.grid(row=1, column=1)
# passEntry.focus()

# button1 = Button(root, text="Sign Up", command=listAppend)
# button1.grid(row=2, column=1)

# button2 = Button(root, text="Cancel", command=root.destroy)
# button2.grid(row=4,column=1)


# root.mainloop()




#!========================================================== !Modules! =============================================================!

# import random
# from tkinter import *
# from tkinter.ttk import *
# import mysql.connector as mc

# db = mc.connect(host='localhost', user='root', passwd='root', database= 'testimonials')
# myCursor = db.cursor()
# myCursor.execute('create table logins (username varchar(255), password varchar(255))')

# myCursor.execute('DESCRIBE logins')
# for x in myCursor:
#     print(x)
# root = Tk()

# root.geometry("500x400")
# root.title("SignUp Page")

# userInput= StringVar()
# password = StringVar()

# sql = f"SELECT username FROM logins"
# myCursor.execute(sql)
# fetch=myCursor.fetchall()
# store = []
# for i in range(0,len(fetch)):
#     store.append(fetch[i][0])
    



# def mainFuntion():
#     listEmpty=[]
#     list1= ['red', 'orange', 'violet', 'blue', 'green', 'black']
#     user1 = userInput.get()
#     pwd = password.get()
          
    
#     if user1 == '' and pwd == '':
        
#         newLabel1= Label(root, text='Please fill above fields', foreground=list1[random.randint(0,5)])
#         newLabel1.grid(column=1)
#         root.update()
    
     
#     if user1 in store:
#         newLabel1= Label(root, text='X', foreground=list1[0])
#         newLabel1.grid(row=0, column=2)
#         root.update()

#     if user1 not in store:
#         newLabel1= Label(root, text='O', foreground=list1[4])
#         newLabel1.grid(row=0, column=2)
#         root.update()

        
    
#     if ' ' in user1:
        
#         newlabel4=Label(root, text='X', foreground=list1[random.randint(0,5)])
#         newlabel4.grid(row=0, column=2)
#         root.update()

#     if len(pwd)<8:
        
#         newlabel3 = Label(root, text='Password < 8 characters!', foreground=list1[random.randint(0,5)])
#         newlabel3.grid(row=1,column=2)
#         root.update()

#     if len(pwd)>=8:
#         if len(pwd)>8:
#             newlabel3 = Label(root, text='Password > 8 characters!', foreground=list1[4])
#             newlabel3.grid(row=1,column=2)
#             root.update()
        
#         if len(pwd)==8:
#             newlabel3 = Label(root, text='Password = 8 characters!', foreground=list1[4])
#             newlabel3.grid(row=1,column=2)
#             root.update()


#     if (user1 not in store) and (' ' not in user1) and (len(pwd)>=8):
#         listEmpty.extend([user1,pwd])

#         sql = "insert into logins (username, password) values (%s, %s)"
#         val1 = tuple([user1, pwd])
#         myCursor.execute(sql, val1)
#         db.commit()

#         newLabel = Label(root, text="Sign up Successful!")
#         newLabel.grid(row=4, column=1)
#         root.update()
        
#         def NameSearch():
#             sql = "select username from logins"
#             myCursor.execute(sql)
#             fetcher1 = myCursor.fetchall()
            
#             sql = "select password from logins"
#             myCursor.execute(sql)
#             fetcher2 = myCursor.fetchall()

#             db.commit()
#             UserLabel = Label(root, text=f'username: \'{listEmpty[0]}\'  password: \'{listEmpty[1]}\'')
#             UserLabel.grid(column=1)
#             return True
        
#         newButton2= Button(root, text="Show", command=NameSearch)
#         newButton2.grid(row=5, column=1)
#         # print(listEmpty)
#         newButton1 = Button(root,text="Quit",command=root.destroy)
#         newButton1.grid(row=6, column=1)
        
#         return True
    

# nameLabel = Label(root, text='User Name: ')
# nameLabel.grid(row=0, column=0)

# nameEntry = Entry(root, width=20, textvariable=userInput)
# nameEntry.grid(row=0, column=1)
# nameEntry.focus()

# passLabel = Label(root,text="Password: ")
# passLabel.grid(row=1, column=0)

# passEntry =  Entry(root, width=20,textvariable=password)
# passEntry.grid(row=1, column=1)
# passEntry.focus()

# newlabel2= Label(root, text='Password should have atleast 8 characters', foreground='red')
# newlabel2.grid(row=2, column=1)


# button1 = Button(root, text="Sign Up", command=mainFuntion)
# button1.grid(row=3, column=1)

# button2 = Button(root, text="Cancel", command=root.destroy)
# button2.grid(row=4,column=1)


# root.mainloop()
