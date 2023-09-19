ls = [1, 2, 4, 12, 13, 4]
big_num = ls[0]
i = 1
i_s = 0
while(i < len(ls) - 1):
    if(ls[i] > big_num):
        i_s = i
    i += 1
print(i_s)

