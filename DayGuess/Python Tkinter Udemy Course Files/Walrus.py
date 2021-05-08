"""
Normal way of Assigning Variables
"""

var = 0 
while var < 9:
    print(f"Var --> {var}")
    
    var += 1




""" 
Using Walrus Operator
""" 

while (var := str(input("Enter the Choice: "))) != 'q':
    print(f"Var is {var}")



 