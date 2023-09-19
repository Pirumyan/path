ls = [12, 3, 4, 5, 6, 7, 1]
big = ls[0]
small = ls[0]
for i in range(1,len(ls)):
    if(ls[i] > big):
        big = ls[i]
    if(small > ls[i]):
        small = ls[i]
print(big + small)        
