"""
Way 1: By Using the .join function where wach element in the list of Fibonacci Numbers is <'class' str>
"""

def fibonacci_numbers(x: int) -> list:
    """ It generates the Fibonacci Series Upto the given argument x,

    Args:
        x (`int`): It is the Positional argument by passed by order and holds the limit upto which the fibonacci series has to be print in the `int` form.

    Returns:
        `series`: It holds the `Fibonacci Series` which the function returns.
    """
    
    series = [0, 1]
    index = 1
    for val in range(x-2):
        sum = series[index-1] + series[index]
        series.append(sum)
        index += 1
    return series
    

def seive_of_list(arg: list,n: int) -> None:
    """It generates the list passed from the function `fibonacci_numbers` and the user input `n` and convert each element of the list to `str` class and then prints each element with the help of `.join()` method.

    Args:
        arg (`list`): It is the positional argument of `value` passed by order contains the `Fibonacci Series` passed from the function `fibonacci_numbers`.
        n (`int`): It is the positional argument of `n` passed by order and contains the `user_input`
    """
    
    for index,val in enumerate(arg):
        arg[index] = str(val)
    print(f"The fibonacci sequence upto {n} is: ",end = " ")
    print(", ".join(arg))


user = int(input("Enter the Nth Term of the Sequence: "))
value = fibonacci_numbers(user)
seive_of_list(value,user)




"""
Way 2: By Unpacking the list and seperating the elements using sep where all elements in the list of Fibonacci Numbers is of <'class' int>
"""
def fibonacci(x: int) -> list:
    """ It generates the Fibonacci Series Upto the given argument x,

    Args:
        x (`int`): It is the Positional argument by passed by order and holds the limit upto which the fibonacci series has to be print in the `int` form.

    Returns:
        `series`: It holds the `Fibonacci Series` which the function returns.
    """
    
    series = [0, 1]
    index = 1
    for val in range(x-2):
        sum = series[index-1] + series[index]
        series.append(sum)
        index += 1
    return series
    

user = int(input("Enter the Nth Term of the Sequence: "))
value = fibonacci(user)
print(f"The fibonacci sequence upto {user} is: ",end=" ")
print(*value, sep=", ")


















