#!/usr/bin/python

'''

'''

# Declaring a string variable and assigning value to it.
name = 'Test String'

# This will print the value of name
print('--------'*4)
print('Printing the string variable.')
print(name)

# Lets try to concat the name with Hello World.
print('--------'*4)
print('Concatination of string variable wiht Hello Wolrd.')
print(name + ' Hello World')

# Lets try to print first letter of our name variabe. Indexing starts with 0 so we will takes the o for our first letter
print('--------'*4)
print('Printing the first letter of string variable.')
print(name[0])

# Lets try to print last letter of our name variabe. We can take last letter using negative index.
print('--------'*4)
print('Printing the last letter of string variable.')
print(name[-1])


# Lets try to print using range.
print('--------'*4)
print('Printing letter which index is 2 upto index 10.')
print(name[2:10])
print('Printing letter which index is 5 upto unknown index which is last.')
print(name[5:])
print('Printing letter which last index is 7 from unknown index which is first.')
print(name[:7])
