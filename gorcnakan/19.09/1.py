ls = [15, 4,3, 2, 1, 16]
max = ls[0]
i = 1
while i < len(ls):
    if max <= ls[i]:
        max = ls[i]
    i += 1
print(max ,ls.index(max))        
X = enumerate(ls)
print(list(X))