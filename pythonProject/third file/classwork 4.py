#given a two list of numbers, write a program to crreate a new list such that
# the new list should contain odd numbers from the first list and even number from the second list..
# list1 = [10,20,25,30,35]
# list2 = [40,45,60,75,90]

list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]

newList =[]

for number in list1:
    if number % 2 == 1:
        newList.append(number)

for number in list2:
    if number % 2 == 0:
        newList.append(number)

print(newList)





