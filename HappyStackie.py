import os
import platform
from typing import Any


class Stacker():
    def __init__(self, stack:list):
        self.Stack = stack

    def isEmpty(self)-> bool:
        '''
        Checks whether the given stack is empty or not.
        '''
        if len(self.Stack) == 0:
            return True
        return False

    def Push(self, element:Any)-> Any:
        self.Stack.append(element)
        return element
    
    def Pop(self)-> Any:
        if self.isEmpty():
            return None
        return self.Stack.pop()
    
    def Peek(self)-> Any:
        return self.Stack[-1]
    
    def Display(self) -> None:

        if self.isEmpty(): print('>> Stack is Underflow :: No Data to Display! <<')
        else:
            for items in self.Stack[::-1]:
                if items == self.Stack[-1]:
                    var = "|" + f"{items}".center(20) + " |"
                    print(var+"<-- Top")
                    print(f"{len(var)*'-'}".center(20))
                else: 
                    nVar = "|"+ f"{items}".center(20) +  " |"
                    print(nVar)
                    print(f"{len(nVar)*'-'}".center(20))

        
        return None


# Driver Code
if __name__ == '__main__':
    stack_list = []
    StackClass = Stacker(stack_list)
    flag = False
    while flag != True:
        print("""
        1. (P)ush Data to Stack.
        2. P(o)p Data from Stack
        3. P(e)ek into Stack
        4. (D)isplay the Stack
        0. Exit the Process
        """)

        user = input('Enter your choice: ')
        if user[0] == '1' or user[0].lower() == 'p':
            itemToPush = input("Enter item to push into stack: ")
            StackClass.Push(itemToPush)

        elif user[0] == '2' or user[0].lower() == "o":
            result = StackClass.Pop()
            if result is not None: print(f"Removed {result} from the stack.")
            else: print('Stack UnderFlow! :(')

        elif user[0] == '3' or user[0].lower() == 'e':
            print(f'The top most item in stack is: {StackClass.Peek()}')

        elif user[0] == '4' or user[0].lower() == 'd':
            print()
            print()
            StackClass.Display()

        elif user[0] == '0': 
            flag = True
            match platform.system():
                case 'Windows': os.system('cls')
                case 'Linux': os.system('clear')
                case 'Darwin': os.system('clear')

        else:
            print('Please enter a valid input!')