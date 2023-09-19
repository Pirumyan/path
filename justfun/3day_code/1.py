ls = [123, 213, 123, 222, 5432, 234, 111]
count = 0

for i in range(len(ls)):
    if(ls[i] % 2 != 0):
        count += 1

print(count)