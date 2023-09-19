ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
zuyg = []
kent = []
for i in range(0, len(ls)):
    if(ls[i] % 2 == 0):
        zuyg.append(ls[i])
    else:
        kent.append(ls[i])
print(zuyg)
print(kent)

