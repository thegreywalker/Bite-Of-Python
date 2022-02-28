import random

from Stack import Stack
from typing import Union

from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.columns import Columns



myStack = Stack()
console = Console()

"""
# ! Write a PUSH(NAMES) & POP() Methods to add Names and Remove Names 
# ! considering them to act as PUSH and POP operations in Stack.
"""

def push(data_pushed: Union[int, str, bool, any]) -> str:
    myStack.push(data_pushed)

    print()
    # * * Styling the Data
    Stack_Status = myStack.top()
    console.log(Stack_Status, log_locals=True)
    print()

def pop(data_pushed) -> str:
    Stack_Status = myStack.pop(data_pushed)
    console.log(Stack_Status, log_locals=True)
    



# print("""
#     1. Add Name
#     2. Delete Name
#     3. Exit
# """)
# payload = int(input("Enter You Choice? "))
# print()
# while payload:
    
#     if payload == 1:
#         payload_name = input("Enter You Name? ")
#         push(payload_name)
#         print()
#     if payload == 2:
#         payload_name = input("Enter the Name to be Deleted? ")
#         pop(payload_name)
#         print()
#     if payload == 3:
#         name = 'Thank you'
#         data = f"[b]{name}[/b]\n[yellow]{'Visit Again'}"
#         final = [Panel(data)]
#         console.print(Columns(final))
#         break
#     print("""
#     1. Add Name
#     2. Delete Name
#     3. Exit
# """)
#     payload = int(input("Enter You Choice? "))
#     print()
    

# ! Write AddScore (Game) and DelScore() methods in Python to add new Score in the list of Score in a game and remove a Score from the list of Score in a game considering them to act as PUSH and POP operations in Stack.

def AddScore(data_pushed: Union[int, str, bool, any]) -> str:
    myStack.push(data_pushed)

    print()
    # * * Styling the Data
    Stack_Status = myStack.top()
    console.log(Stack_Status, log_locals=True)
    print()

def DelScore(data_pushed) -> str:
    Stack_Status = myStack.pop(data_pushed)
    console.log(Stack_Status, log_locals=True)
    print()



# print("""
# 1. Add Score
# 2. Delete Score
# 3. Exit
# """)
# payload = int(input("Enter You Choice? "))
# print()
# while payload:
#     if payload == 1:
#         payload_score = input("Enter Your Game Score? ")
#         AddScore(payload_score)
#         print()

#     if payload == 2:
#         payload_score = input("Enter the Score to be Deleted? ")
#         DelScore(payload_score)
#         print()

#     if payload == 3:
#         name = 'Thank you'
#         data = f"[b]{name}[/b]\n[yellow]{'Visit Again'}"
#         final = [Panel(data)]
#         console.print(Columns(final))
#         break
#     print("""
#     1. Add Score
#     2. Delete Score
#     3. Exit
# """)
#     payload = int(input("Enter You Choice? "))
#     print()



# ! Write a menu Driven Program in Python to implement a Stack using list of integers.


elems = [1, 52, 35, 65, 8, 85, 65, 57, 54, 74, 85, 96, 85, 54, 96, 35, 14, 25, 35, 72.5, 89]

def add():
    Stack_Status = myStack.add(elems[0])
    elems.pop(0)
    console.log(Stack_Status, log_locals=True)

def remove():
    Stack_Status = myStack.pops()
    console.log(Stack_Status, log_locals=True)
    


# print("""
# 1. Add Element
# 2. Remove Element
# 3. Exit""")
# print()
# payload = int(input("Enter your Choice? "))
# while payload: 
#     if payload == 1:
#         add()
#         print()
#     if payload == 2:
#         remove()
#         print()
#     if payload == 3:
#         name = 'Thank you'
#         data = f"[b]{name}[/b]\n[yellow]{'Visit Again'}"
#         final = [Panel(data)]
#         console.print(Columns(final))
#         break
#     print("""
#     1. Add Element
#     2. Remove Element
#     3. Exit
#     """)
#     payload = int(input("Enter your Choice? "))
#     print()


# ! Write AddCustomer(Customer) and DeleteCustomer() methods in Python to add a new Customer and delete a Customer fro  list of Customer Names, considering them to act as PUSH and POP operations of Stack Data Structure.

def AddCustomer(data_pushed: Union[int, str, bool, any]) -> str:
    myStack.push(data_pushed)

    print()
    # * * Styling the Data
    Stack_Status = myStack.top()
    console.log(Stack_Status, log_locals=True)
    print()

def DeleteCustomer(data_pushed) -> str:
    Stack_Status = myStack.pop(data_pushed)
    console.log(Stack_Status, log_locals=True)
    


print("""
    1. Add Customer
    2. Delete Customer
    3. Exit
""")
payload = int(input("Enter You Choice? "))
print()
while payload:
    
    if payload == 1:
        payload_name = input("Enter You Customer Name? ")
        AddCustomer(payload_name)
        print()
    if payload == 2:
        payload_name = input("Enter the Customer Name to be Deleted? ")
        DeleteCustomer(payload_name)
        print()
    if payload == 3:
        name = 'Thank you'
        data = f"[b]{name}[/b]\n[yellow]{'Visit Again'}"
        final = [Panel(data)]
        console.print(Columns(final))
        break
    print("""
    1. Add Customer
    2. Delete Customer
    3. Exit
""")
    payload = int(input("Enter You Choice? "))
    print()
