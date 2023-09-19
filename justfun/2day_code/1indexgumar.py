ls = [12, 3, 4, 5, 6, 3, 12, 123]
ls2 = [5, 6, 3, 9, 12, 4, 2]
lsgumar = []
erkarutyun = 0
if(len(ls) >= len(ls2)):
    erkarutyun = len(ls2)
else:
    erkarutyun = len(ls)
erk = min(len(ls), len(ls2))    
for i in range(erkarutyun):
    lsgumar.append(ls[i]+ls2[i])
print(lsgumar)    