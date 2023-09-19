ls = ['asdasd', 'asdasdqwdq', 'asdasd', 'asdasdasd']
big = len(ls[0])
ind = 0
for i in range(1,len(ls)):
    if(big < len(ls[i])):
        big = len(ls[i])
        ind = i
print(ls[ind],"inxey = ", ind)