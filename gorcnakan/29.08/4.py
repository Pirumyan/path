x = int(input())
num = x
y = 0
vzgo = 0
cikl = 0
while cikl!=1:
    while x > 0:
        y = x % 10
        vzgo = vzgo * 10 + y
        x = x // 10
    if(vzgo==num):
            print(vzgo)
            cikl = 1
    else:
            x = num
            x = x + vzgo
            vzgo = 0
            num = x
