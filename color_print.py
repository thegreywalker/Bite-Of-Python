# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'
 
BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# print(RED,BOLD, "this will be in red")

# print(WHITE,BOLD, "this will be in white")

# print(CYAN, BOLD, "this will be in Cyan", RESET)

# print("Hello World")


def colour_print(text: str, *effects: str) -> None:
    """
    This function takes one postional and one `var-positional` argument and gives the desired color to each text passed in this function 
    and then resets the process.

    Args:
        `text (str)``: It is the positional argument of the text passed into the function by order.
        `*effects (str)``:It is the `Var-positional argumrnt` of the `color code` as well as the `Reset Code` passed into the function by order.

    Returns:
        `None`

    """
    
    effects_string = "".join(effects)
    output_string = f"{effects_string}{text}{RESET}"
    print(output_string)
    
    



colour_print("Hello, Red", RED, BOLD)
print("This should be the default color")
colour_print("Hello, Blue", BLUE)
colour_print("Hello, Blue", BLUE, BOLD)
colour_print("Hello, Yellow", YELLOW)
colour_print("Hello Bold", BOLD)
colour_print("Hello Bold", BOLD, GREEN, UNDERLINE)
colour_print("Hello, Underline", UNDERLINE)
colour_print("Hello, Reverse", REVERSE)
colour_print("Hello, Reverse", REVERSE, BLUE, UNDERLINE)
colour_print("Hello Balck", BLACK)
colour_print("Hello Magenta", BOLD, MAGENTA)






"""
Note: The ASCII sequence color code works fine with macOS/Linux but on Windows it may give some problems as it's not fully supported. But 
with the release of the Windows Terminal now it has began Supporting the ASCII color sequence Codes, but still m,ight face some issues.
In that Case try using the "Colorama" module in python, first install it using pip -> then import it in your python script
"""