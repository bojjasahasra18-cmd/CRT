
i = int(input())
s = 0
while i > 0:
    a = i % 10
    s += a
    i //= 10
c = 0
while s >0:
    b = s % 10
    c += b
    s //= 10
print(c)


