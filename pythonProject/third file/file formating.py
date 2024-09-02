# x - creating of file
# r - reading content of a file
# w - writing to a file             this is just like creating new file
# a - appending to a file           updating a file

# here we are creating a new file
# f = open("class4.py","x")
# f.close()

# how to read file
# p = open("class4.py", "r")   ## here we read the file in class4.py
# reader = p.read()
# print(reader)

# writting to a file
# f = open("class4.py","w")
# f.write("am trying to replace you now")             # here we are writing to the file in class 4.py, and every other thing in the file will be replaced with the new text
# f.close()

#appending to a file
# f = open("class4.py","a")
# f.write(", but you seems i replaceable")
# f.close()

# # how to make a file open in another line
#
# print("HEllo\n world")
#
# how to check if file start with a letter
# p = open("class4.py", "r")
# reader = p.read()
# print(reader)
# if reader.startswith("am"):         #here we use startwith to check if specified text starts the file
#     print("starts with am")
# else:
#     print("doesnt start with am")


f = open("class4.py","r")

for line in f:
    line = line.rstrip()    # we use rstrip to
    if line.find("@gmail") == -1:    # here if the condition is false it will print and go back to search again
        continue   # this continue means that if the number did not have gmail it should not print
    print(line)    # if the line have gmail it should print