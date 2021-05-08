limit = float(input("Enter the Limit? "))
maxPrice = 0
# Read the next price
while (nextPrice := float(input("Enter a Price or 0 to stop? "))) != 0:
    print(f"The Next Price is {nextPrice}")
    if maxPrice > 0:
        print(f"The largest Price is {maxPrice}.")
    else:
        print(f"The largest price is less than the limit.")











