
"""
Write following functions:
1.Left Shift (L)
2.Right Shift(L)
3.Even ODD Swap(L)
4.Reverse(L)
5.Half Swap(L)
6.Left Right Shift(L)
7.LargestAndSmallest(L)
8.LargeAndSmall(L, L)
9.ZeroinPrime(L)
"""


def LeftShift(ls: list, n: int = 1) -> str:
    return "The Modified Left Shift List is: {}".format(ls[-n::] + ls[0:-n])


def RightShift(ls: list, n: int = 1) -> str:
    return "The Modified Right Shift List is: {}".format(ls[n::] + ls[0:n])


def EvenOddSwap(ls: list) -> str:
    for i in range(0, len(ls), 2):
        ls[i], ls[i + 1] = ls[i + 1], ls[i]
    return "The Modified Even Odd Swap List is: {}".format(ls)


def Reverse(ls: list) -> str:
    val = 1
    for i in range(0, (len(ls) // 2)):
        b = ls[i]
        ls[i] = ls[-val]
        ls[-val] = b
        val += 1
    return "The Modified Reverse List is: {}".format(ls)


def HalfSwap(ls: list) -> str:
    return "The Modified Half Swapped List is: {}".format(ls[len(ls) // 2::] + ls[0:len(ls) // 2])


def LeftRightShift(ls: list, orientation='l') -> str:
    if orientation == mylist:
        b = LeftShift(ls)
        return "The Modified Left Shift List is: {}".format(b)
    else:
        b = RightShift(ls)
        return "The Modified Right Shift List is: {}".format(b)


def LargestAndSmallest(ls: list) -> str:
    large = small = ls[0]
    for val in ls:
        if val > large:
            large = val
        else:
            large = large
        if val < small:
            small = val
        else:
            small = small
    return "The Largest & Smallest element in the List are {}, {} respectively." \
        .format(large, small)


def LargeAndSmall(ls: list, lst: list = None) -> tuple:
    if lst is None:
        lst = [24, 75, 96, 87]
    Arr1 = ls
    Arr2 = lst
    a,b = LargestAndSmallest(Arr1), LargestAndSmallest(Arr2)
    return a,b


def ZeroinPrime(ls: list) -> str:
    for index, val in enumerate(ls):
        for value in range(2, val):
            if ls[index]%value == 0:
                break
        else:
            ls[index] = 0
    return "The Modified List where Prime Elements are Zero is {}"\
        .format(ls)


def menu():
    print("""
1. Left Shift the List                          (Specifying Number of Elements not necessary)
2. Right Shift the List
3. Even Odd Swap the List                       (Specifying Number of Elements not necessary)
4. Reverse  the List
5. Half Swap the List
6. Left Right Shift                             (Choice of l/r not necessary)
7. Largest & Smallest element in List           
8. Largest & Smallest element in "Two" List     (Giving an Extra List not necessary)
9. Replace Prime Element by Zero                
10. 0 to Exit
""")


# main Segment
mylist = eval(input("Enter a List? "))
while len(mylist) % 2 != 0:
    mylist = eval(input("Enter a List? "))
temp = mylist.copy()
print()
menu()
while (n := int(input("Enter Choice? "))) != 0:
    if n == 1:
        try:
            number = int(input("""Enter Number of Elements to LeftShift?
             (Not necessary) --> """))
            a = LeftShift(temp, number)
            print(a)
        except ValueError:
            a = LeftShift(temp)
            print(a)
    elif n == 2:
        try:
            number = int(input("""Enter Number of Elements to RightShift? 
            (Not necessary) --> """))
            a = RightShift(temp, number)
            print(a)
        except ValueError:
            a = RightShift(temp)
            print(a)
    elif n == 3:
        a = EvenOddSwap(temp)
        print(a)
    elif n == 4:
        a = Reverse(temp)
        print(a)
    elif n == 5:
        a = HalfSwap(temp)
        print(a)
    elif n == 6:
        try:
            shift = input("""Enter the Choice Left(l)/Right(r)? 
            (Not necessary) -->  """)
            a = LeftRightShift(temp, shift)
            print(a)
        except ValueError:
            a = LeftRightShift(temp)
            print(a)
    elif n == 7:
        a = LargestAndSmallest(temp)
        print(a)
    elif n == 8:
        try:
            b = eval(input("Enter a List? (Not necessary) -->  "))
            a = LargeAndSmall(temp, b)
            print(a[0])
            print(a[1])
        except SyntaxError:
            a = LargeAndSmall(temp)
            print(f"Arr1 --> {a[0]}")
            print(f"Arr2 --> {a[1]}")
    elif n == 9:
        a = ZeroinPrime(temp)
        print(a)
    temp = mylist.copy()
    print()
    menu()
print("Thanks for Visiting.")



