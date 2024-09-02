def identity(Name, Age):
    return 'Hello', Name, ' You Are ', Age, ' Years Old'


Name = input("Name: ")
age = int(input("Age :"))


print(identity(Name,age))
