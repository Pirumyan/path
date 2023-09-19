ls = [12, 4, 123, 543,213, 234, 765, 88]
x = int(input())
count = 0
for i in ls:
    if(x == i):
        count += 1
if(count >= 1):
    print('yes')
else:
    print("no")            