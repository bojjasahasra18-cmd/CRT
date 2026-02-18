'''
# Pascal triangle
n = int(input())
for i in range(n):
    c = 1
    for j in range(i+1):
        
        print(c, end = "")
        c = c * (i-j) // (j+1)
    print()
'''
# butterfly pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print('*', end = '')
    for j in range(2*(n-i-1)):
        print(" ", end = '')
    for j in range(i+1):
        print('*', end = '')

    print()
   