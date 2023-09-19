a = 3723
b = 3
while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1
print(a)
