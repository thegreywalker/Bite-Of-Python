import os

import webbrowser

print('Hello! I can open or search for you just type path variable or web address...')

while True:
    i = input("")
    if i == "":
        break
    else:
        try:
            os.startfile(i)
        except FileNotFoundError:
            print("Can't Find the file according to the given path")
            



