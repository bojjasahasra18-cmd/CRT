'''
# square star pattern
n = 4
for i in range(n):
    for j in range(n):
        print('*', end = '')
    print()


# right angled triangle star pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end = '')
    print()

# inverted right triangle star pattern
n = int(input())
for i in range(n):
    for j in range(n - i):
        print('*', end = '')
    print()

n = int(input())
for i in range(n, 0, -1):
    for j in range(i):
        print('*', end = '')
    print()



# number triangle
n = int(input())

for i in range(n):
    for j in range(i+1):
        print(j+1, end = '')
    print()

# repeated number pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print(i+1, end = '')
    print()

n = int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+i) , end = '')
    print()


# floyd triangle
n = int(input())
'''

#hollow square
n = int(input())
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print('*', end = '')
