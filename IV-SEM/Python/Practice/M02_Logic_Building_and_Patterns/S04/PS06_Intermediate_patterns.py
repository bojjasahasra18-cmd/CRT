
'''
# Pyramid pattern
# approach1
n = int(input())
for i in range(n):
    for j in range( n-i-1):
        print(' ', end = '')
    for j in range(2*i+1):
        print('*', end = '')
    print()
# approach2

for i in range(n):
    print(' '*(n-i-1) + '*'*i*2 + ' '*(n-i-1))
'''
'''
# invertered pyramid
n = int(input())
for i in range(n):
    for j in range(i):
        print(' ', end = '')
    for j in range(2*(n-i)-1):
        print('*', end = '')
    print()
'''
'''
# diamond pattern
n = int(input())
for i in range(n):
    for j in range( n-i-1):
        print(' ', end = '')
    for j in range(2*i+1):
        print('*', end = '')
    print()
for i in range(n-i-1):
    for j in range(i):
        print(' ', end = '')
    for j in range(2*(n-i)-1):
        print('*', end = '')
    print()
'''
# palindrome pattern

'''
# comprehension
#normal way
# read the the list and multiply each number/value with 2

n = list(map(int, input().split()))
a = []
 for i in n:                      
    s = i*2
    a.append(s)
print(a)

#comprehension way
print([i*2 for i in n])

# store the even numbers in another list
# normal way
n = list(map(int, input().split()))
a = []
for i in n:
    if i%2 == 0:
        a.append(i)
print(a)

# comprehension way
b = (i for i in n if i%2 == 0)
print(b)
# take the input as list of strings and output he list as a string but values of lit are separated by space

n = list(input().split())
# approach1
for i in n:
    print(i, end = ' ')
print()
# apporoach2
res = ' '
for i in n:
    res += i 
print(res + ' ')

# approach3
a = ' '.join(n)
print(a)
'''






