#name = input("name: ")
#age= int(input("age: "))

#if age < 18:
    #print("hello",name," you are a minor")
#elif age > 18:
    #print("hello", name," , you are a major")

# you must close your condition with :

# here we collected number and check if the number is greater than 50 or less than 50 or equal to 50
#number =int(input("enter number:"))
#if number >50:
   # print(number,"greater than 50")
#elif number < 50:
    #print(number,"less than 50")
#else:
    #print(number,"equal to 50")

#number =int(input("enter number:"))
#if number%2==0:
    #print(number,"is an even number")
    #if number%3==0:
       # print(number,"Idan Number")
    #else:
       # print(number,"not an Idan number")
#else:
    #print(number,"odd number")


#Times = int(input("put Times"))

#if Times >=0 and Times <=12:
    #print("Good Morning")
#elif Times >=12 and Times <=16:
    #print("Good Afternoon")
#elif Times >=12 and Times <=20:
    #print("Good Evening")
#elif Times >= 20 and Times <=24:
   # print("Good Night")
#else:
    #print("wrong Input")

#def greetings():                    #def is used to create function
    #return "Hello World"    #print will display the values but return will only work if you call the function with print statement

#print(greetings())

#def addTwoNumbers():
    #num1=2
    #num2=4
    #return num1 + num2         here we are assigning values to it

#print(addTwoNumbers())

def addTwoNumbers(num1 ,num2):
    return num1+num2

userInput1 = int(input("num1:"))
useerInput2 = int(input("num2:"))

print(addTwoNumbers(userInput1,useerInput2))







