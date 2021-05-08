"""
for x in range(1,4):
    for y in range(1,x+1):
        print("*",end=" ")
    print()

for x in range(1,4):
    for y in range(4,x,-1):
        print(" ",end=" ")
    for x in range(0,x):
        print("*", end=" ")
    print()

for x in range(1,4):
    for y in range(4,x,-1):
        print("*", end=" ")
    print()

for x in range(3,0,-1):
    for y in range(x,4):
        print(" ",end=" ")
    for z in range(0,x):
        print("*",end=" ")
    print()

for x in range(1,4):
    for y in range(1,x+1):
        print(x,end=" ")
    print()

for x in range(1,4):
    for y in range(3,x,-1):
        print("  ",end=" ")
    for z in range(0,x):
        print(x,end=" ")
    print()

for x in range(3,0,-1):
    for y in range(1,x+1):
        print(x,end= " ")
    print()

i = 0
for x in range(3,0,-1):
    for z in range(1,i+1):
        print("  ",end=" ")
    for y in range(1,x+1):
        print(x,end= " ")
    i += 1
    print()
      
for x in range(1,4):
    for y in range(3,x,-1):
        print("  ",end=" ")
    for z in range(1,x+1):
        print(z,end=" ")
    print()

for x in range(4,1,-1):
    for y in range(1,x):
        print(y,end=" ")
    print()

for x in range(3,0,-1):
    for y in range(x,3):
        print("  ",end=" ")
    for z in range(1,x+1):
        print(z,end=" ")
    print()

for x in range(3,0,-1):
    for y in range(x,3):
        print(" ",end=" ")
    for z in range(1,x+1):
        print("*",end=" ")
    print()

size = 3
for x in range(size,-(size),-1):
    for y in range(1,abs(x)+1):
        print(" ",end=" ")
    for z in range(size, abs(x), -1):
        print("* ",end=" ")
    print()

n = 5
cen = n//2+1
for x in range(1,n+1):
    for y in range(1,n+1):
        if (x == cen or y == cen):
            print("* ",end=" ")
        else:
            print("  " ,end=" ")
    print()

for x in range(65,68):
    for y in range(65,x+1):
        print(chr(y),end= " ")
    print()        

for x in range(1,4):
    for y in range(3,x,-1):
        print("  ",end= " ")
    for z in range(1,x+1):
        print(chr(z+64),end=" ")
    print()

for x in range(3,0,-1):
    for y in range(0,x):
        print(chr(y+65),end= " ")
    print()

for x in range(3,0,-1):
    for y in range(x,3):
        print("  " ,end= "  ")
    for z in range(0,x):
        print(chr(z+65),end= "  ")
    print()

for x in range(1,4):
    for y in range(1,x+1):
        print(y,end=" ")
    print()

for x in range(1,4):
    for y in range(3,x,-1):
        print(" " ,end= " ")
    for z in range(0,x):
        print("* ", end= " ")
    print()
"""























































