# def add(x,y):
#     c = x + y
#     return c
# print(add(5,9))
#
# #  to return 2values
# def add_sub(x,y):
#     c = x + y
#     a = x -y
#     return c,a
#
# result1, result2 = add_sub(5, 9)
# print(result1, result2)

#  functions arguments
# position. this is called position argument
# def person(name, age):
#     print(name)
#     print(age)
#
# person("emeka", 37)

# keyword arguement
# person(age=37, name="emeka")

# default arguement. here if i dont give age an arguemnt it will take the default arguement, but if i give it an
# arugement it will override the defaul arguement def person(name, age = 18): print(name) print(age) person("emeka")

# variable length here we use * to show that our function can accept multiple values.
# def multiAdd(x, *y): # here y takes the value as tuple
#    c = x
#    for i in y:          # here we iterate within the y values adding the values to c
#         = c + i
#
#    print(c)             # here we printed c. note the indentation is in the same line with the for loop
# multiAdd(5, 6 ,12, 30)
#
# # keyworded arguement contd
# def person(name, **data):  # note we used double * or ** to tell the function to accept keyworded arguement
#     print(name)
#     print(data)
# person("emeka", age = 30, city = "awka", phoneNumber = 9073097705)

# to use for loop to fetch the key and the values
# def person(name, **data):  # note we used double * or ** to tell the function to accept keyworded arguement
#     print(name)
#     for key, value in data.items():
#         print(key, value)
#
#
# person("emeka", age=30, city="awka", phoneNumber=9073097705)

#  local and global variable
#  for the global variable
# name = "emeka"
# def per():
#     global name
#     name = "emma"
#     print(name)
# per()
# print(name)

#  we use globals() in order to have both global and local variable in a function
# name = 'emeka'
# def per():
#
#     name = "emma"
#     print(name)
#     globals()['name']= "paul" # note here we used globals()[] to change the global variable
#
#
# per()
# print(name)

#  lists in function
#  here we want to calculate the number of even and odd number in a list using a function
def number(lis):
    even = 0
    odd = 0
    for i in lis:
        if i % 2 == 0:
            even +=1
        else:
            odd +=1
    return even, odd
lis =[10,20,13,15,19,30,40]
print(number(lis))


