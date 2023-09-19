ls = [13.2, 3.5, 12, 4, 3.6, 33]
small_num = ls[0]
i = 1
while ( i < len(ls)):
    if(small_num > ls[i]):
        small_num = ls[i]
    i += 1
print(small_num)    
