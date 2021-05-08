
"""
Walrus Operator in Python
"""

# Usual way to writing code

# choice = 0
# while choice != 9:
#     print(f"Choice --> {choice}")
    
#     choice += 1


# Using Walrus Operator
choice = -1
while (choice := choice + 1) != 9:
    print(f"Choice --> {choice}")


# or

while (choice := input("Enter Your Choice: ")).casefold() != 'quit':
    print(f"Your Choice is {choice}")
    print()

l = [1, 2, 3, 4, 5, 6]
total = sum(l)
total2 = 0
doubleTotal = total + sum(v for v in l)
print(f"Total is: {total}")
print(f"Double of Total is: {doubleTotal}")

























