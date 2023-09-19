a = int(input())
b = int(input())
c = int(input())
d = b ** 2 - 4 * a * c 

if( d > 0):
    print("x_1 = ", (-b + d ** 0.5 ) / 2 * a)
    print("x_2 = ", (-b - d ** 0.5) / 2 * a)
elif(d == 0):
    print(-b / 2 * a)
else:
    print("X_1 = ", -b / (2 * a) - (abs(d) ** 0.5 / (2 * a)) * 1j)
    print("X_2 = ", -b / (2 * a) + (abs(d) ** 0.5 / (2 * a)) * 1j)
    print("Datark pazmutyun")    
