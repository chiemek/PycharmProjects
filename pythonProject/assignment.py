
total = 0
count = 0

while True:
    try:
        userInput = input("Enter a number: ")

        if userInput== "done" :
            average = total/count
            print(total,count,average)
            break
        else:
            total = total + int(userInput)
            count = count +1
    except:
        print("invalid Error")

while True:
    line = input('>type anything ')
    if line[0] == "e":
        continue
    if line == 'done':
        break
    print(line)
print("done")

list = (5, 4, 3, 2, 1)
for i in list:
    print(i)
print("Blastoff")

list = [20, 10, 20, 4, 3, 80]
t = 0
for number in list:
    if number > t:
        t = number
print(t)

list = [20, 10, 20, 4, 3, 80]
count = 0

for number in list:
    count += 1
print(count)

#

