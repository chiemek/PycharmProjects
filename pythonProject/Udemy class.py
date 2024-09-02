# print(bin(500))
# print(0b111110100)
# print(oct(500))
# print(0o764)
# print(hex(500))
# print(0x1f4)
# print(~50)
# print(25 % 13)
# help("maths")

# a = 1
# while a <= 100:
#     if a % 3 !=0:
#        print(a)
#        a +=1
# j = 1
# for i in range(1, 501):
#     if j * j == i:
#         print(i)
#         j += 1
# printing patterns
# print("Emeka ",end="")
# print("Emeka ",end="")
# print("Emeka ",end="")
# print("Emeka")

# we use end="" to print on the same line
# we use print() to print an empty line

# for i in range(4):
#     for e in range(4):
#         print("Emeka ", end="")
#     print()

# for i in range(4):
#     for e in range(4 - i):
#         print("Emeka ", end="")
#     print()
#
# for i in range(4):
#     for e in range(i + 1):
#         print("Emeka ", end="")
#     print()

for i in range(4):
    num = 1
    for e in range(4 - i):

        print(num, end="")
        num += 1
    print()





