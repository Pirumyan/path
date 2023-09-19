st = "hello"
ayo = set ()
vzgo = True
for i in st:
    if i in ayo:
        vzgo = False
        break
    else:
        ayo.add(i)
print(vzgo)
    