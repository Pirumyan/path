ls = [1,3,12,13,2]
big_num = ls[0]
i_s = 0
for i in range(1,len(ls)):
    if(ls[i] > big_num):
        i_s = i
print(i_s)
