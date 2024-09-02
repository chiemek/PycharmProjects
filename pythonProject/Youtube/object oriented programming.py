# class computer:
#     def config(self):
#         print("i7, 16gb, 512")
#
# computer().config()
#
# # __init__  it calls itself
# class computer:
#     def __init__(self):
#         print("hello")
#     def config(self):
#         print("i7, 16gb, 512")
#
# computer().config()


# class computer:
#     def __init__(self,cpu, ram):    #here we used __init__ to initialize the variable used by config method
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("the config is ", self.cpu, self.ram)
#
# comp1 = computer('i5', '16')
# comp2 = computer("razen 3", '8')
#
# comp1.config()
# comp2.config()

# types of variables
# instant variable
# class car:
#     def __init__(self):
#         self.mil = 10
#         self.company = "Benz"
# c1 = car()
# c2 = car()
# c1.mil = 700
#
# print(c1.mil, c2.company)

# class variable
# class car:
#     wheels = 4
#     def __init__(self):
#         self.mil = 10
#         self.company = "Benz"
# c1 = car()
# c2 = car()
# c1.mil = 700
#
# print(c1.mil, c2.company,c1.wheels)


#  types of method in OOP  static method, class method, instance method
# class student:
#     school = "NIIT"
#
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#
#     @classmethod
#     def info(cls):
#         return cls.school
#
#     @staticmethod
#     def asa():
#         print("Asa di ok")
#
#
# c1 = student(30,40,10)
# c2 = student(60,30,50)
#
# print(student.info())
# student.asa()

# inner class or nested
# class student:
#     def __init__(self, name, rollno):
#         self.name = name
#         self.rollno = rollno
#
# s1 = student("emeka",1)
# print(s1.name, s1.rollno)

# operator overloading

# class student:
#     def __init__(self,m1,m2):
#         self.m1 = m1
#         self.m2 = m2
#
#     def __add__(self, other):   # here we use this function so as to allow allow the function perform a task
#         m1 = self.m1 + other.m1
#         m2 = self.m2 + other.m2
#         s3 =  student(m1,m2)
#         return s3
#
#     def __gt__(self, other):        #here we used if statement but we firstly have to create a function/ method for it
#         s1 = self.m1 + self.m2
#         s2 = other.m1 + other.m2
#         if s1 > s2:
#             return True
#         else:
#             return False
#
#
#
# s1 = student(40, 10)
# s2 = student(20,15)
# s3 = s1 + s2
# print(s3.m1)
#
# if s1 > s2:
#     print('s1 wins')
# else:
#     print("s1 loss")
#
# print(s2)


#  method overloading
class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2

    def sum(self, a = None, b = None, c = None):
        s = 0
        if a != None and b != None and c !=None:
            s = a+b+c
            return s
        elif a != None and b != None:
            s = a+b
            return s
        else:
            s = a
            return s

s1 = student(30,20)

print(s1.sum(10,20,30))


#  method overriding
class A:
    def show():
        print("in A show")

class B(A):
    def show():
        print("in B show")

a1 = B
a1.show()
