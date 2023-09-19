ls = [1, 3, 4, 6, 6]
ls2 = [1, 3, 5, 7, 3]
res = []
for i in range(len(ls)):
    for g in range(len(ls2)):
        if(ls[i] == ls2[g]):
            res.append(ls[i])
            break
print(res)
      