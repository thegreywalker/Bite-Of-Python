from typing import Union

# ?  Implementation of Stack using a Module Based Approach

class Stacks():
    """
    Module Based Approach to Implement a Stack using Classes in Python
    `Methods` ~

    `push(data: int | str | bool | list) -> None`
    `pop() -> any`
    `top() -> any`
    `empty() -> bool | str`
    `size() -> int | float`
    """

    def __init__(self: any) -> None:
        self.array = ['Prepopulated Data']
        self.arrayNumbers = []

    def push(self, data: Union[int, str, bool, list]) -> None:
        self.array.insert(0, data)

    def pop(self, data) -> any:
        if  len(self.array) > 0:
            try:
                index = self.array.index(data)
            except ValueError:
                return "Element Not Present in Stack"
            self.array.pop(index)
            return self.array
        else:
            return "Stack is Empty"
    
    def pops(self):
        if len(self.arrayNumbers) > 0:
            self.arrayNumbers.pop()
            return self.arrayNumbers
        else:
            return "Stack Underflow"
            
    def add(self, data):
        if len(self.arrayNumbers) > 4:
            return "Stack Overflow"
        else:
            self.arrayNumbers.insert(0,data)
            return self.arrayNumbers
        
    def top(self) -> any:
        if len(self.array) > 0:
            return self.array
        else:
            return "Stack is Empty"
        
    def empty(self) -> Union[bool, str]:
        if len(self.array) > 0:
            return False
        else:
            return "Stack is Empty"
        
    def size(self) -> Union[int, float]:
        return len(self.array)


Stack = Stacks
