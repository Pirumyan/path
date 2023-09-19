ls = [[j + i for j in range(3)] for i in range(1,10,3)]
ls1 = [[ls[i][j]for i in range(len(ls))]for j in range(len(ls))] 
print(*ls1)