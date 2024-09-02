# myTup = ("emeka", "peter", 50, "okey")
# print(myTup[2])
myList = [2,5,8,90,6]
summation = sum(myList)
print(f"the sum of myList = {summation}")

myDict = {
    "num1": 2,
    "num2" : 5,
    "num3" : 8,
    "num4" : 90,
    "num5" : 6,
}

print(myDict.values())


sumdicts = sum(myDict.values())
print(f"the sum of myList = {sumdicts}")

            #or
total =0
for key in myDict:
    total = total+myDict[key]

print(total)

