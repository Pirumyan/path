# put your python code here
a = list(map(int, input().split()))
b = list(map(int, input().split()))
result = list(zip(a,b))
for i in range(len(result)):
    print(sum(result[i]), end= " ")