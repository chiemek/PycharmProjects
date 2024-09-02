# def is_even(n):
#     return n % 2 == 0
# num = [10,20,23,27,90,30,5,34,24,56,786,6]
# even = list(filter(is_even,num))
# print(even)

#  here we can use lambda
num = [10,20,23,27,90,30,5,34,24,56,786,6]
even = list(filter(lambda n : n%2 == 0,num))
# print(even)

# map.  this is used to change a result of a value
double = list(map( lambda f : f * 2, even))
print(double)

#  reduce() this is used to add values together
from functools import reduce
num = [10,20,23,27,90,30,5,34,24,56,786,6]
even = list(filter(lambda n : n%2 == 0,num))
double = list(map( lambda f : f * 2, even))

sum = reduce( lambda a,b : a + b, double)
print(sum)