st = "helo"
vzgo = 0
for i in st:
    pos = ord(i) 
    if vzgo & (1 << pos) > 0:
        print("false")
        break
    vzgo = vzgo | (1 << pos)
  