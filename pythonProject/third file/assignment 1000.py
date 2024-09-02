# write a program to check if a given number is a palindrome number.

# number = int(input("enter number: "))
# numstr = str(number)
# reverse = numstr[:: -1]
#
# if numstr == reverse:
#     print(f"{numstr} is a parlindrome number")
# else:
#     print(f"{numstr} is not a parlindrome number")


# Write a menu based program to insert , remove, sort, extend, reverse and traverse a list of
# items.
# Hint: Define functions to perform different operation of list, such as insertlist() and
# removelist etc.

mylist = [10, 'emeka', 30, 'paul', 50 ]
secondlist = [60, 70, 80, 90]

#sort()
secondlist.sort(reverse=True)
print(secondlist)

#extend
mylist.extend(secondlist)
print(mylist)

#reverse
secondlist.reverse()
print(secondlist)

#tranverse
secondlist.tra