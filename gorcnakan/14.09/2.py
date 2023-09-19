st = "vzgovbghdvaas"
ls = []
max = ""
tmp = ""
for i in range(len(st)):
    if st[i] not in tmp:
        tmp += st[i]
    else:
        if len(tmp) > len(max):
            max = tmp
        tmp = st[i]  
if len(tmp) > len(max):
    max = tmp
print(max)

    