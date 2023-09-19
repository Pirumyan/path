st = "helo"
vzgo = 0
for i in range(len(st)):
    for g in range(len(st)):
        if i == g:
            continue
        if st[i] == st[g]:
            vzgo += 1
if vzgo > 1:
    print("chelav")
else:
    print("elav")           