# dictionary is created with {} while list is create with[]
students = {
    "name": "Emeka",            # here the name is the key value, we will use the name to call
    "age": 30,
    "class": "python"

}
# print(students)    here we can call the dictionary direct
print(students["name"])  # here we are calling Emeka with the key value name

# how to iterate through our dictionary. you will get only the key
for key in students:
    print(key,students[key])  #here we use student [key] to print out the values of the key. which are the names.

#.keys will print out all the keys in our dictionary
print(students.keys())

# .values prints the values in our dictionary
print(students.values())

# how to print out specific value in your dictionary
print(students["age"])  # here we specify using the key value per

#in operator uses bullean values
print("name" in students)
        #or
my_value = students.values()
print(30 in my_value)

# how to add value to your dictionary
students["passion"] = 'CODING'
print(students)

# to print the length of you dictionary
print(len(students))