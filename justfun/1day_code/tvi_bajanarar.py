x = int(input('input your number: '))
if(x == 0):
    print(x)
else:   
    for i in range(1, x + 1):
        if(x % i == 0):
            print(i)

