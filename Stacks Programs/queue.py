import time 
class queue:
    mark = []
    def insert(cls, rear):
        cls.mark.append(n := int(input("Enter a Mark? ")))
        rear += 1

    def display(cls):
        if len(cls.mark) == 0:
            print("Queue is Undefined")
        
        else:
            print("Displaying Queue in FIFO Order...")
            time.sleep(2)
            for val in range(len(cls.mark)):
                print(cls.mark[val])

    def delete(cls, front):
        if len(cls.mark) == 0:
            print("Queue is Underflow")
        
        else:
            print("Displaying elements in FIFO Order...")
            front += 1
            return (item := cls.mark.pop(0))



    if __name__ == "__main__":
        mark = []
        front = rear = 0
        while True:
            print("""1. INSERT\t2. DISPLAY\t3. DELETE\t0. EXIT""")
            userInput = int(input("Enter Your Choice? "))
            if userInput == 0:
                exit()
            elif userInput == 1:
                insert(mark, rear)
            elif userInput == 2:
                display(mark)
            elif userInput == 3:
                print( x := delete(mark, front))

Queue = queue







