# friuts = "banana"
# index = 0
# while index < len(friuts):
#     letter = friuts[index]
#     print(letter)
#     index += 1
#
#
# file = input("enter file name: ")
#
# try:
#     filename = open(file)
# except:
#     print("the file ",file , " does not exist" )
#     quit()
#
# linenumber = 0
# for line in file:
#     if line("def:"):
#         linenumber += 1
# print(linenumber)

friends = ["emeka", "emma", "ebuka", "nelson"]
# print(range(len(friends)))
#
# for friend in friends:
#     print("happy new year", friend)
#
# for freind in range(len(friends)):
#     i = friends[3]
#     print("happy new year", i)


# x = list()
# x.append("emeka")
# print(x)
# print(x)
# x.append("paul")

# total = 0
# count = 0
# while True:
#     number = input("enter your number: ")
#
#     if number== "done":
#         break
#     real = float(number)
#     total += real
#     count +=1
# average = total / count
# print("average ", average)

# newlist = list()
# while True:
#     list = input("enter your number: ")
#
#     if list == 'done':
#         break
#
#     lists = float(list)
#     newlist.append(lists)
# average = sum(newlist) / len(newlist)
# print("the avearge = ", average)

# name = "mekus1085@gmail.com"
# start = name.split("@")
# print(start)
# gmail = start[1]
# com = gmail.split(".")
# last = com[1]
# print(last)
#
# count = dict()
# names = ['emeka', 'paul' , 'philip' , 'emeka', 'paul' , 'ebuka' ]
# # for name in names :
# #     if name in count:
# #         count[name] += 1
# #     else:
# #         count[name] = 1
# # print(count)
# for name in names:
#     count[name] = count.get(name, 0) +1
# print(count)

# print(ord('\n'))  # here we are checking the unicode of a space
#
# print('emeka\'s "book"') #here we use \ to skip the ' in front of emeka
# # print('emeka ' * 10)
# #
# x = 9
#
# print(x + 10)
#
# name = [10, 20, 30, 40, 50]
#
# num = [25, 14, 36, 95, 12, 14, 26]
# del num[3:]
# print(num)

help()