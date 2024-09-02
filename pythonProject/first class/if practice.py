
height = int(input("enter your height: "))

bill = 0


if height >= 120 :
  print("you can ride")
  age = int(input("enter your age:"))
  if age < 12:
    bill == 5
    print("please pay $5")
  elif age <=18:
    bill == 7
    print("please pay $7")
  else:
    bill == 12
    print("please pay $12")

  photo = input("do you want a photo: type Y or N ")
  if photo == 'Y':
    bill = bill + 3

  print(f"your bill is {bill}")
else:
  print("you cant ride sorry:")
