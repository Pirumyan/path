ls = [15, 4,3, 2, 1, 16]
ls1 = [ 11 , 23 , 5 , 8, 5]
result = 0
min = len(ls)
if ls > ls1:
    min = len(ls1)
for i in range(min):
    print(ls[i] * ls1[i], end= " ")