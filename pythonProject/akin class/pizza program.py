welcome = '''
welcome to meks pizza
here are the lists of the pizza we have and the prices
'''
print(welcome)
orders = 'chicken_pizza= 500\n''peperoni_pizza= 300\n''meat_pizza = 250\n'

chicken_pizza = 500
peperoni_pizza = 300
meat_pizza = 250

print(orders)

total = 0
while True:
    userInput = input("select the category of pizza you need: ")

    userInputs = userInput.lower()

    if userInputs == 'done':
        break

    if userInputs == "chicken_pizza":
        print("price is 500 each")

        quantity = int(input("how many did you want: "))
        subtotal = quantity * chicken_pizza
        total = total + subtotal
        print(f"\tyour subtotal = #{subtotal}")

    if userInputs == "peperoni_pizza":
        print(' price is 300 each')

        quantity = int(input("how many did you want: "))
        subtotal = quantity * peperoni_pizza
        total = total + subtotal
        print(f"\tyour subtotal = #{subtotal}")

    if userInputs == "meat_pizza":
        print('price= 250')

        quantity = int(input("how many did you want: "))
        subtotal = quantity * meat_pizza
        total = total + subtotal
        print(f"\tyour subtotal = #{subtotal}", )

    if userInputs not in orders:
        print("sorry we dont sell that kind of pizza check next time")

print(f'\tyour subtotal = #{total}')
print("check out")