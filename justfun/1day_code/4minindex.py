ls = [13.2,3.5,12,4,3.6]
small_num = ls[0]
i_s = 0
for i in range(1,len(ls) - 1):
    if(small_num > ls[i]):
        i_s = i

print(i_s)        
