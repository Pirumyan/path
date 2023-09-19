# put your python code here
num = float(input().split())
lst = [ a for a in range(1, len(num), 2)]
print(*lst)


a = input().split()
b = [float(x) for i, x in enumerate(a) if i % 2 == 0 and float(x) % 2 == 0]
print(b)
