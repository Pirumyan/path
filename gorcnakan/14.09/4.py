ls = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
gum = 0
for i in range(len(ls)):
    for g in range(len(ls)):
        if g + 1 == len(ls[i]) - i:
            gum += ls[i][g]
print(gum)
          