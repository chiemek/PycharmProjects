# # note if error is not handled your application or program will crash or stop working whenever it encouters one error
# # so we use try and except. inside except we put exception
#
# a = 6
# b = 0
# try:                                 # if this error was not handled bye will not print
#     print(a/b)
# except Exception:
#     print("you cant divide the value by zero")
#
# print('bye')
#
#
# # using except alias in your code
# a = 6
# b = 0
# try:                                 # if this error was not handled bye will not print
#     print(a/b)
# except Exception as e:               # you can still print the execption or error message by using the execption
#     print("hey your error is ",e)
#
# print('bye')
#
# # finally block
# a = 6
# b = 0
# try:
#     print("resource open")                      # if this error was not handled bye will not print
#     print(a/b)
# except Exception as e:               # you can still print the execption or error message by using the execption
#     print("hey your error is ",e)
# finally:
#     print("Resource closed")
#
# print('bye')

# using more than one execpt, to use more than one except you have to specify the kind of error you want to handle
a = 6
b = 0


try:
    f = int(input("enter a number "))
    print(f)
    print(a/b)
except ZeroDivisionError as z:
    print("hey your error is ",z)
except ValueError as v:
    print("hey your error is ",v)
finally:
    print("i must execute sha")
