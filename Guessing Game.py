import random 

guess = random.randint(0,20)
print(f"A range of the Random Number which the Computer has choosen in range of 0 -> 20 is {random.randint(guess,guess+5)}")
print()
user = int(input("Enter your Choice: "))
while True:
    if user != guess:
        if user < guess:
            print("Guess Higher!")
            user = int(input("Enter: "))
            continue
        else:
            print("Guess Lower!")
            user = int(input("Enter: "))
            continue
    else:
        print(f"Congrats! You've guessed the correct number {guess}. ")
        break      









