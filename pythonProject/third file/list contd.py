# list1 = [1, 2, 3]
# list2 = [5, 6, 7]
#
# list1.extend(list2) #we use extend to add the list2 to list 1
# print(list1)


#pop() this will return only the last element if you dont pass any index value to it
# list1 = [1, 2, 3]
# list2 = [5, 6, 7]
#
# print(list1.pop())  # here we did not assign argument to pop, so it will return the last number in line 1

# list1 = [1, 2, 3]
# list2 = [5, 6, 7]
#
# print(list1.pop(1)) #here it will return number 1 to you


# del is used for delete. any value inside the record will be deleted
list1 = [1, 2, 3]
list2 = [5, 6, 7]

del list2[1]    # here we delete index 1 which is 6 in line2

print(list2)


# remove is used to a value not index, but delete is deleting based on index
list1 = [1, 2, 3]
list2 = [5, 6, 7]

list2.remove(6)
print(list2)