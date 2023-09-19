qanak =int(input(' write your size ls'))
ls = []
zut = 0
i = 0
while i != qanak:
    zut = input('input your list number')
    i += 1
    if(zut.isdigit()):
        ls.append(zut)
    else:
        print('bro input number')
        i -= 1
print(ls)         
