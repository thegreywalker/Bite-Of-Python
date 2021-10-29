# 1. Write a python code that prints the longest word in a list of words

def longestWord(ls : list) -> str:
    lengthOflargestWord = len(ls[0])
    wordIndex = 0
    for index, val in enumerate(ls):
        if len(val) >= lengthOflargestWord:
           wordIndex = index
           lengthOflargestWord = len(val)
        else:
            lengthOflargestWord = lengthOflargestWord
            wordIndex = wordIndex
    return ls[wordIndex]


# 2. Write a python program to create a tuple storing first 9 Fibonacci series.
def FiboinTuple() -> tuple:
    ls = [0, 1]
    for val in range(1, 8):
        ls.append(ls[-1] + ls[-2])
    return tuple(ls)


# 3.Write a program that returns a list contains only common elements from two given lists of 10 elements and 7 elements respectively.

def commonElements(ls: list, ls2: list) -> list:
    Commonlist = []
    for val in ls:
        for element in ls2:
            if val == element:
                Commonlist.append(val)
            else:
                pass
        
        else:
            continue
    return Commonlist

#or


def common_elements(list1, list2):
    return [x for x in list1 if x in list2]


common_elements([1, 2, 3, 4], [2, 3, 4, 5])

# 4. Create a dictionary whose keys are month names and whose values are the number of days in the corresponding months.
# i) Ask the user to enter a month name and use the dictionary to tell how many days are there in the month.
# ii) Print out of all the months with 31 days.


class Dictionary():
    def __init__(self) -> None:
        self.dictionary = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'Octobar': 31,
        'Novembar': 30,
        'Decembar': 31
    }

    def getDays(self, month) -> str:
        return "The Number of Days in {0} is {1}".format(
            month, self.dictionary[month]
        )
    
    def getMonths(self) -> list:
        listOfMonths = []
        for val in self.dictionary.keys():
            if self.dictionary[val] == 31:
                listOfMonths.append( "{0}".format(val))
        return listOfMonths


# 5. Write a program that prints the following series:
# i) -X + X2 – X3 + X4 + …..Xn

x= float (input ("Enter number of terms: ")  
y=int(input ("Enter the constant value: ")) 
a=0
for i in range (1, x+1):
      If i%2= = 0:
          a +=(y **i) 
      else:
          a-=(y**i) 
print (The result of the series is:" ,a)



# ii) 1+(1+2)+(1+2+3)+(1+2+3+4)+...+(1+2+3...+n)


def series_sum(n):
    return sum(1 + x for x in range(n))


print(series_sum(5))


# 6. Write a program that accept any number and prints number of digits.
def getDigits(number : int) -> int:
    nm = number
    count = 0
    for val in range(len(str(number))):
        number //= 10
        count += 1
    return "The Number {0} has {1} digits in it.".format(nm, count)


# 7.Write a function to insert a string into the middle of another string.
def insert_string(str1, str2):
    return str1[:2] + str2 + str1[2:]


print(insert_string("abc", "xyz"))


# 8. Write a python program to read a name and display it in abbreviated form.
# Name: Raju Verma
# Output: RV

def abbvName():
    name = input("Enter your name: ")
    name = name.split()
    print("Abbreviated form of your name is: ", name[0][0]+name[-1][0])

abbvName()


# 9. Write a function to calculate GCD of two given numbers.


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


# 10. Write a function that prints the maximum and minimum values in a dictionary. The dictionary is given as an argument to the function.
def minMax(dic):
    print("Maximum value: ", max(dic.values()))
    print("Minimum value: ", min(dic.values()))

minMax({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})   

#   11. Write a program that prompts a number from the user and adds it in a list. If the number is more than 100 then add 'EXCESS' in the list.
def addNum():
    numList = []
    while True:
        num=int(input("Enter a number: "))
        if num<100:
            numList.append(num)
            print(numList)
        else:
            numList.append("EXCESS")
            break
    print(numList)

addNum()

    
