def is_palindrome(string):
    return string[::-1].casefold() == string.casefold()
    


def sentence_palindrome(check):
    char = ""
    for val in check:
        if val.isalnum():
            char += val
    return is_palindrome(char) 


user = int(input("Enter a number (1 for Numeric Numbers/ 2 for Charecters or sentences): "))
if user == 1:
    num = input("Enter the Number: ")
    if is_palindrome(num):
        print(f"The Number '{num}' is a Palindrome.")
    else:
        print(f"The Number '{num}' is not a Palindrome.")
        
if user == 2:
    word = input("Enter the (Charecter/Sentence): ")
    if sentence_palindrome(word):
        print(f"The Word/Sentence '{word}' is a Palindrome.")
    else:
        print(f"The Word/Sentence '{word}' is not a Palindrome.")
























