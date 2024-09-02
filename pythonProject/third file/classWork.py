#given two numbers return thier product only if the product is equal to or lower than 1000 else return the sum
num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
product = num1 * num2
sum = num1 + num2

if product <= 1000:
    print(product)
else:
    print(sum)


