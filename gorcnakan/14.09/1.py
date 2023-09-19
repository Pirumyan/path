str1 = "listen"
str2 = "sileat"
ls1 = list(str1)
hash = 0
for i in range (len(str2)):
    if ls1[i] in str2:
        hash += 1
            
if hash == len(str2):
    print("exav")
else:
    print("chelav")