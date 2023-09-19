# erank = [[1],
#          [1, 1],
#          [1, 2, 1],
#          [1, 3, 3, 1],
#          [1, 4, 6, 4, 1,],
#          [1, 5, 10, 10, 5, 1]]
N = 7
P = []
for i in range (7):
    row = [1] * (i + 1)
    for j in range (i + 1):
        if j != 0 and  j != i:
            row[j] = P[i -1][j - 1] + P[i - 1][j]
    
    P.append(row)
    
for r in P:
    print(r)    
            