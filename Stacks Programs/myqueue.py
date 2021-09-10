from queue import Queue
queue = Queue()
front = rear = 0
while True:
    print("""1. INSERT\t2. DISPLAY\t3. DELETE\t0. EXIT""")
    userInput = int(input("Enter Your Choice? "))
    if userInput == 0:
        exit()
    elif userInput == 1:
        queue.insert(rear)
    elif userInput == 2:
        queue.display()
    elif userInput == 3:
        print( x := queue.delete(front))