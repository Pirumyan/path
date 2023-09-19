def prtfect(x):
    baj = 1
    sum = 0
    while baj < x / 2 + 1:
        if( x % baj == 0):
            sum += baj
            baj += 1
        else:
            baj += 1
    if (sum == x):
        return True
    else:
        return False
number = 1
while (number < 8129):
    if(prtfect(number)):
        print(number)
    number += 1                   