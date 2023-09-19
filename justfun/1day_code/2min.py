ls = [13.2,3.5,12,4,3.6,3.2]
small_num = ls[0]
for i in range(1,len(ls)):
    if(small_num > ls[i]):
        small_num = ls[i]
print(small_num)        
