def sayHello():
   print('hello world')

sayHello()

def sayHello(name):
    return name                   # return is holding values until you say print
def sayAge(age):
    return age

userName=input("name")
userAge=int(input("age"))

addAge=sayAge(userAge)
addName=sayHello(userName)      # here we are assigning the values of sayhello function to,  and put in the values inside
print(addName,addAge)
