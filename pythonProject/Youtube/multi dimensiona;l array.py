from numpy import  *

# this is how we create a numpy with array()
# arr = array( [1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(arr)

# how to create a numpy with linspace()

# arr = linspace(0,15,30)
# print(arr)

# arange() this also takes 3 parameter but not the same with linspace(), the last value will determine how you want the value to skip
arr = arange(0,30,3)
print(arr)

#  multi-dimensional array

arr2 = array([
    [1, 2, 3, 4, 5, 6],
    [5, 6, 7, 8, 7, 8 ]
    ]
)
# print(arr2)
# print(arr2.ndim) # ndim is used to know howmany dimension the array is
# print(arr2.shape) # shape will give you the number of rows and column
# arr1 = arr2.flatten() # this will convert multi-dimensional array to single array
# print(arr1)
# arr3 = arr1.reshape(4,3)
# print(arr3)

#  matrix in array
m = matrix(arr2)
print(m)
# more advantages of matrix
m = matrix('1,2,3; 4,6,7; 8,9,9')  # note here we just created multi dimensional array using matrix
print(m)

