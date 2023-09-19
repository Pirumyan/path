x = int(input())
y = int(input())
z = int(input())
if((x ** 2) < (y ** 2 + z ** 2)):
    if((y ** 2) < (x ** 2 + z ** 2)):
        if((z ** 2) < (x ** 2 + y ** 2)):
            print("Yes")
        else:
            print("No")
    else:
        print("no")
else:
    print("no")                 
