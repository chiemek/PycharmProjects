# # def greet():
# #     print("hello")
# #     greet()
# #
# # greet()
#
# #  how to get the limit of recursion
# import sys
# print(sys.getrecursionlimit())
# def greet():
#     print("hello")
#     greet()
#
# # how to increase the limit
# sys.setrecursionlimit(10000)
# print(sys.getrecursionlimit())
#
#
# def greet():
#     print("hello")
#     greet()

#  finding factorial using recursive function
# def fact(n):
#     if n == 0:
#         return 1     # factorial of 0 is 1
#     return n * fact(n -1) # here we multiply n which is five by n -1 which is 4. it will keep reducing until it reaches zero
# print(fact(5))

# annonymous function
f = lambda a : a *a
print(f(5))

# addition of two numbers
f = lambda a,b : a + b
print(f(5,10))
