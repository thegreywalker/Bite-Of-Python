# Below will be the ANSI color codes and it is used in coloring the Report Card.
"""
Make Sure you put a space after "," while entering multiple values at once, e.g -> (Himangshu, Apurba, Raima) 
"""



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


def Grader(score : int) -> str:
    if score >= 91:
        return "A+"
    if score >= 81 and score <= 90:
        return "A"
    if score >= 71 and score <= 80:
        return "B+"
    if score >= 61 and score <= 70:
        return "B"
    if score >= 51 and score <= 60:
        return "C"
    if score >= 41 and score <= 50:
        return "D"
    if score >= 31 and score <= 40:
        return "E"
    if score <= 30:
        return "Fail"


def banner_text(text : str , screen_width : int = 80, *args : str, orient : str = "center", border : str = " " ) -> None:
    if len(text) > (screen_width - 4):
        raise ValueError (f"String {text} is larger than specified width {screen_width}")
    if text == "=":
        color_effects = "".join(args)
        print(f"{color_effects}""=" * screen_width, f"{RESET}")
    else:
        if orient == "left":
            left_text = text.ljust(screen_width-4," ")
            color_effects = "".join(args)
            print(f"={color_effects} {left_text} {RESET}=")
            
        if orient == "right":
            right_text = text.rjust(screen_width-4," ")
            color_effects = "".join(args)
            print(f"={color_effects} {right_text} {RESET}=")
            
        if orient == "center":
            centered_text = text.center(screen_width-4, " ")
            color_effects = "".join(args)
            print(f"={color_effects} {centered_text} {RESET}=")


def main():
    marks_container = input("Enter the Marks of 6 Subjects: ")
    name = input("Enter Your NAME, SEC, Roll No: ")
    data = name.split(", ")
    list_container = marks_container.split(", ")

    sum = 0
    for val in list_container:
        num = int(val)
        sum = sum + num

    percent = (sum/600)*100
    x = Grader(percent)
    banner_text("=",60, RED, BOLD)
    banner_text(" ",60)
    banner_text("Satish Chandra Memorial School",60, CYAN, BOLD, border = RED)
    banner_text("REPORT CARD", 60, RED, BOLD, border = RED)
    banner_text(" ", 60)
    banner_text("=", 60, RED, BOLD)
    banner_text(f"NAME : {data[0]}                        CLASS : XI", 60, orient ="left")
    banner_text(f"ROLL NO : {data[1]}                                SEC   : {data[2]}", 60, orient = "left")
    banner_text(" ",60)
    banner_text("------------------------------------",60, MAGENTA, BOLD)
    banner_text(" ", 60)
    banner_text("SUBJECTWISE MARKS", 60, CYAN)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(f"English:         {list_container[0]}", 60, orient = "left")
    banner_text(f"Bengali:         {list_container[1]}", 60, orient = "left")
    banner_text(f"Physics:         {list_container[2]}", 60, orient = "left")
    banner_text(f"Chemistry:       {list_container[3]}", 60, orient = "left")
    banner_text(f"Biology:         {list_container[4]}", 60, orient = "left")
    banner_text(f"Computer:        {list_container[5]}", 60, orient = "left")
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text(f"The Total Marks is {sum}.", 60, BLUE, BOLD, orient = "left")
    if x == "Fail":
        banner_text(f"We are Sorry!, the Student has Failed.", 60, BLUE, BOLD, orient = "left")
    else:
        banner_text(f"The Grade Obtained is {x}", 60, BLUE, BOLD, orient = "left")
    banner_text(" ", 60)
    banner_text(" ", 60)
    banner_text("=", 60, RED, BOLD)
    
    
    
    
if __name__ == "__main__":
    main()
