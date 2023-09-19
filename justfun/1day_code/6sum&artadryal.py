ls = [1, 3, 12, 4, 2, 0]
gumar = ls[0]
arta = ls[0]
for i in range(1, len(ls)):
    gumar += ls[i]
    arta *= ls[i]
print('Sum = ', gumar)
print('artadryala klni', arta)    
