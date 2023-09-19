ls = [1, 2, 3, 45, 5, 23]
print(ls)
for i in range(len(ls)):
    ls[i] /= len(ls)
    ls[i] = round (ls[i],2)
print('nor list', ls)    
