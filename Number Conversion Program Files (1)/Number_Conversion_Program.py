user_base = int(input("Enter the base of the number: "))
to_be_converted = int(input("Enter the base to be Converted: "))

# Binary -> [    ] Conversion 

    # Binary -> Decimal Conversion
if user_base == 2:
    user_input = int(input("Enter the Number: "))
    if to_be_converted == 10:
        temp = user_input
        sum = 0
        j = 0
        while temp != 0:
            power  = pow(2,j)
            sum = sum +  temp%10 * power
            temp //= 10
            j += 1
        print()       
        print(f"The Binary -> Decimal Conversion result is {sum}")    



    # Binary -> Octal Conversion
    
    if to_be_converted == 8:
        dict = {000 : "0", 1 : "1", 10 : "2", 11 : "3", 100 : "4", 101 : "5", 110 : "6", 111 : "7" }
        temp = user_input
        sum = '0'
        while temp != 0:
            rem = temp%1000
            if rem in dict:
                sum = sum + dict[rem]
                temp//=1000
            else:
                pass
        reverse = sum[::-1]
        print(f"The Binary -> Octal COnversion is {reverse.rstrip('0')}")

    # Binary -> Hexadecimal Conversion
    
    if to_be_converted == 16:
        dict = {000 : "0", 1: "1", 10 : "2", 11 : "3", 100 : "4", 101 : "5", 110 : "6", 111 : "7", 1000 : "8", 1001: "9", 1010: "A", 1011 : "B", 1100 : "C", 1101 : "D", 1110 : "E", 1111 : "F"}
        temp = user_input
        sum = '0'
        while temp != 0:
            rem = temp%10000
            if rem in dict:
                sum = sum + dict[rem]
                temp //= 10000
            else:
                pass
        reverse = sum[::-1]
        print(f"The Binary -> Hexadecimal Conversion is {reverse.rstrip('0')}")



# Decimal -> [    ] Conversion

    # Decimal -> Binary Conversion
if user_base == 10:
    user_input = int(input("Enter the Number: "))
    if to_be_converted == 2:
        rem = 0
        cur = 0
        next = user_input
        list_of_numbers = []
        while next != 0:
            rem = next%2
            list_of_numbers.append(rem)
            cur = next//2
            next = cur 
        list_of_numbers.reverse()
        numbers = 0
        for val in range(len(list_of_numbers)):
            numbers = numbers*10 + list_of_numbers[val]
            
        print(f"The Decimal -> Binary Conversion is {numbers}")

    # Decimal -> Octal Conversion
    
    if to_be_converted == 8:
        rem = 0
        cur = 0
        next = 0
        next = user_input
        list_of_numbers = []
        while next != 0:
            rem = next%8
            list_of_numbers.append(rem)
            cur = next//8
            next = cur
        list_of_numbers.reverse()
        numbers = 0
        for val in range(len(list_of_numbers)):
            numbers = numbers*10 + list_of_numbers[val]
        print(f"The Decimal -> Octal Conversion is {numbers}")
        
    # Decimal -> Hexadecimal Conversion
    
    if to_be_converted == 16:
        dict = {10: "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F"}
        cur = 0
        rem = 0
        next = user_input
        list_of_numbers = []
        while next != 0:
            rem = next%16
            if rem > 9:
                if rem in dict:
                    rem = dict[rem]
                    list_of_numbers.append(rem)
                else:
                    pass
            else:
                list_of_numbers.append(rem)
            cur = next//16
            next = cur 
        list_of_numbers.reverse()
        numbers = '0'
        for val in range(len(list_of_numbers)):
            string  = str(list_of_numbers[val])
            numbers = numbers + string
        print(f"The Decimal -> Hexadecimal Conversion is {numbers.lstrip('0')}")
          
          

#  Octal -> [    ] Conversion

    # Octal -> Decimal Conversion
if user_base == 8:
    user_input = int(input("Enter the Number: "))
    
    """
    Part to Check if the entered number is an Octal Number or not.
    """
    check = user_input
    flag = False
    while check != 0:
        rem = check%10
        if rem <= 7:
            check //= 10
        else:
            flag = True
            break
    
    if flag == False:
        if to_be_converted == 10:
            temp1 = user_input
            sum = 0
            rem1 = 0
            j = 0
            while temp1 != 0:
                rem1 = temp1%10
                power = pow(8,j)
                sum1 =  sum1 + rem1*power
                temp1 //= 10
                j += 1
            print()
            print(f"The Octal -> Decimal Conversion is {sum1}")
            
        #  Octal -> Binary Conversion
            
        if to_be_converted == 2:
            dict = {0 : "000", 1 : "001", 2 : "010", 3 : "011", 4 : "100", 5 : "101", 6 : "110", 7 : "111"}
            temp2 = user_input
            rem2 = 0
            list_of_numbers = []
            while temp2 != 0:
                rem2 = temp2%10
                if rem2 in dict:
                    list_of_numbers.append(dict[rem2])
                temp2 //= 10
            numbers = '0'
            list_of_numbers.reverse()
            for val in range(len(list_of_numbers)):
                numbers = numbers + list_of_numbers[val]
            print()
            print(f"The Octal -> Binary Conversion is {numbers.lstrip('0')}")
    else:
        print()
        print("This is not an Octal Number. Retry Again")
       
    
    
# Hexadecimal -> [    ] Conversion

    # Hexadecimal -> Decimal Conversion
if user_base == 16:
    user_input = input("Enter the Number: ")
    if to_be_converted == 10:
        temp3 = list(user_input)
        dict = {'A' : "10", 'B' : "11", 'C' : "12", 'D' : "13", 'E' : "14", 'F' : "15"}
        for val in range(len(temp3)):
            if temp3[val] in dict:
                temp3[val] = dict[temp3[val]]
            else:
                continue
        print(temp3)
        
        sum4 = 0
        j = 0
        while temp3 != []:
            num = int(temp3[-1])
            temp3.pop(-1)
            power = pow(16,j)
            sum4 = sum4 + num*power
            j += 1

        print(f"The Hexadecimal -> Decimal Conversion is {sum4}")

    # Hexadecimal -> Binary Conversion
    
    if to_be_converted == 2:
        dict = {"0" : "0000", "1" : "0001", "2" : "0010", "3" : "0011", "4" : "0100", "5" : "0101", "6" : "0110", "7" : "0111", "8" : "1000", "9" : "1001", "A" : "1010", "B" : "1011", "C" : "1100", "D" : "1101", "E" : "1110", "F" : "1111"}
        elements = []
        temp = list(user_input)
        index = 0
        while temp != []:
            if temp[index] in dict:
                elements.append(dict[temp[index]])
                temp.pop(index)
        numbers = ''
        for val in elements:
            numbers = numbers + val
        print(f"The Hexadecimal -> Binary conversion is {numbers}")
                


"""
This Code is Contributed by Apurba Ghosh (@iamapurba2003)
"""








