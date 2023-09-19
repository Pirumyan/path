x = input()
mec = []
poqr = []
for i in range(len(x)):
    if ord(x[i]) >= 97 and ord(x[i]) <= 122:
        poqr.append(x[i])
    elif ord(x[i]) >= 65 and ord(x[i]) <= 90:
        mec.append(x[i])
print(f"mecery {len(mec)}")
print(f"poqrery{len(poqr)}")        