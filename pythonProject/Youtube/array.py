' use strict '
import array as a


val = a.array('i', [1, 2, 3, 4, 5])
print(val.buffer_info())

# how to copy array to a new array
newArr = a.array(val.typecode,( a for a in val)) # in the for loop we created a variable a, then iterate through val, and assign each value to it
print(newArr)
# to get the square root of the values we simply
newArr = a.array(val.typecode,( a*a for a in val))
print(newArr)

# to get the values printed one one in diferent line
# for i in val:
#     print(i)

# note we can still use while loop here. but the line of code will be longer
e = 1
while e <= len(val):
    print(val[e-1])
    e += 1

