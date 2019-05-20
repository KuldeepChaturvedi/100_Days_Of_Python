#!/usr/bin/python

# List is mutable
# List allow to change values stored in it
# List declared in squre brackets

num = [25,45,85,95,65,82,62,35,55]

'''
Index :-             0   1   2   3   4   5   6   7   8
                    [25, 45, 85, 95, 65, 82, 62, 35, 55]
Negtive Index :-     -9  -8  -7  -6  -5  -4  -3  -2  -1
'''

# This will print the list num
print('--------'*4)
print('Printing the all values in list.')
print(num)

# Print the list element at index 5
print('--------'*4)
print('Printing the list element at index 5.')
print(num[5])

# Print the list element from index 4 to last
print('--------'*4)
print('Printing the list element from index 4 to last')
print(num[4:])

# Print the list element at last index
print('--------'*4)
print('Printing the list element at last index')
print(num[-1])

# Append function to append new value in list
print('--------'*4)
print('Append 99 in list')
num.append(99)
print(num)


# Insert function to insert new value at specific index
print('--------'*4)
print('Insert 33 at index 4')
num.insert(4,33)
print(num)

# Remove function to remove value from list
print('--------'*4)
print('Removeing 85 from list')
num.remove(85)
print(num)


# Pop function to pop value using index
print('--------'*4)
print('Pop value at index 3')
print(num.pop(3))


# Pop function to pop value using index
print('--------'*4)
print('Pop value at last index')
print(num.pop())

# Del function to delete value after index 5
print('--------'*4)
print('Delete value after index 5')
del num[5:]
print(num)

# Extend function to extend value in list
print('--------'*4)
print('Extending [62,35,55] in list')
num.extend([62,35,55])
print(num)


# Minimun function to get minimun value from list
print('--------'*4)
print('Getting minimum value from list')
print(min(num))

# Maximum function to get maximum value from list
print('--------'*4)
print('Getting maximum value from list')
print(max(num))

# Sum function to get sum of all list items
print('--------'*4)
print('Getting sum of list')
print(sum(num))

# Sorting function to get sort list
print('--------'*4)
print('Sotring the list')
num.sort()
print(num)
