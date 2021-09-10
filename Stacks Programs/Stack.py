# I am going to create a Stack Class so that I can use built-in Stack features 

from typing import Union


class IndexNumber():
    pass

class Stack():
    pass

class StackElements():
    pass

class Stacks(IndexNumber):
    
    def __init__(self) -> None:
        self.array = []
        pass
    
    def push(self, data: Union[list, int]) -> None:
        self.array += self.array.append(data)
    
    def pops(self, data: IndexNumber) -> None:
        self.array.pop(data)
    
    def getStack(self) -> Stack:
        return self.array

    def traverse(self) -> StackElements:
        for val in self.array:
            return val
        
Stack = Stacks
        
