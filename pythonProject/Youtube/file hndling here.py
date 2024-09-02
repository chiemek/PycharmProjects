

# it is a way we access a file from another file.
# f = open("calc.py", "r")
# f = f.read()
# print(f)

# to read the lines
# f = open("calc.py", "r")
# f = f.readline()        # this will read line one by one for you
# print(f)

# Write on a file
# p = open("abc", "w")
# p = p.write("what is the name, ops i just created a new text file")
#
# # appened on a file we use a
a = open("abc", "w")
a = a.write("emeka")

#  how to copy a file to another file
f = open("threads.py", "r")
a = open("abc",'a')
for data in f:
   a.write(data)