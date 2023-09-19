x = int(input("enter number: "))
y = 0
z = 1
tmp = 0
print(y, end = " ")
print(z, end = " ")
if(x == 0):
    print(y)
elif(x == 1):
    print(z)
else:        
    for i in range(2, x + 1):
        tmp = z
        z += y
        y = tmp
        print(z, end = " ") 

