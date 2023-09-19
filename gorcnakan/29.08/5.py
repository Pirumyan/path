x =int(input("Write your squar size:"))
arr = [[0 for i in range(x)]for j in range(x)]
sum = 0
for i in range(x):
    print("\n")
    for j in range(x):
        arr[i][j]= int(input("Write nuber:"))
        if(j == x - 1 -i):
            sum = sum + arr[i][j]
for i in range(x):
    print("\n")
    for j in range(x):
        print(arr[i][j], end=' ')
print("\n",sum)            
