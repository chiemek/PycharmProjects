# Name = "emeka"
# for letter in Name: # here we are printing the letter one one in the
#     print(letter)

# Name = "missionary"
# for letter in Name:
#     print(letter)

# Names = ["Ola","Lala","Emmanuel","Emeka"]
# Names[1] = "Tunde"
# for name in Names:
#     print(name)

#list opereators  + *
# Names = ["Ola","Lala","Emmanuel","Emeka"]
# names2 = ['zino','machalla','prince','zino']  # here you use + to print 2 variables together
# print(Names  + names2)

# to print the names  on one
# Names = ["Ola","Lala","Emmanuel","Emeka"]
# names2 = ['zino','machalla','prince','zino']  # here you use + to print 2 variables together
# total = names2 + Names
# for name in total:
#     print(name)


# here we want to print and skip some name
Names = ["Ola","Lala","Emmanuel","Emeka"]
names2 = ['zino','machalla','prince','zino']  # here you use + to print 2 variables together
total = names2 + Names

counter = 0
for name in total:
    counter = counter + 1
    if counter == 6:
        continue
    print(name)
