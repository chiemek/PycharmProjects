# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >=num3:
#         return num2
#     else:
#         return num3
# print(max_num(300,300,10))

is_male = True
is_tall = False

if is_male and is_tall:
    print("you are a tall male")
# elif is_male and not is_tall:
#     print("you are a short male")
elif not is_male and is_tall:
    print("you are not a male and not tall")
else:
    print("you are either male or not tall")