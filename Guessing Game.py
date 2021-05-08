import random 

guess = random.randint(0,20)
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









