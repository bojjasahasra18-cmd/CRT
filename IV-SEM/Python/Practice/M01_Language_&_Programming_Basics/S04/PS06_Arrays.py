'''
Arrays:
1. list - built-in dsa
 - use [] to create alist
 -list is mutable
 -list is hetereogeneous
 - list is indexed
 -list is ordered
 -list allows duplicate values
2. array using array module
3.array using numpy module

'''
'''
li =[8,8,80,9,'iyf', 9.0000]
print(li, type(li), len(li))
# updation
# li  = False
# print(li)

# adding element
li.append(100)
print(li)
li.insert(-300, 09765.0986)
print(li)

li.extend([93,3345,66666,5,442356,])
print(li)

# remove
li.pop()
print(li)
li.pop(4)
print(li)

li.remove(8)
print(li)


li.clear()
print(li)

# copy
li1 = [1,2,3,4,5]
li2 = li1
li3 = li1.copy()
print(li1, li2, li3)

li1.append(100)
print(li1, li2, li3)

'''
'''
import array
from array import array
arr = array('i', [1, 2, 3, 4])
print(type(arr))
'''
