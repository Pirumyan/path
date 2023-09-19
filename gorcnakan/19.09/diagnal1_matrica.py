N = int(input())
lst =  [[1 if i == j else 0 for j in range(N)]for i in range(N)]
for i in lst:
    print(*i)