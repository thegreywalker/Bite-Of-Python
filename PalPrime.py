"""
Bugs are there for inputs like 121, 757 etc.error -> Number is not a palindrome but a prime numner.
121 - The number neither a Plaindrome nor a prime number.
"""


def palPrime(n):
    flag1 = True
    flag2 = True

    #Palindrome
    
    rev = 0
    cur = 0
    temp = n
    while temp != 0:
        cur = n%10
        temp //= 10
        rev = rev*10 + cur
    if rev == n:
        flag1 = True
    else:
        flag1 = False

    for val in range(2,n//2):
        if n%val == 0:
            flag2 = False
            break
        
    if flag1 == False and flag2 == False:
        print("The Number is neither a Palindrome nor a Prime Number")
    elif flag1 == True and flag2 == False:
        print("The Number is a Palindrome but not a Prime Number")
    elif flag1 == False and flag2 == True:
        print("The Number is not a Palindrome but a Prime Number")
    else:
        print("The Number is a Palindrome and a Prime Number")





#main segment
z = int(input("ENTER THE NUMBER? "))
x = palPrime(z)