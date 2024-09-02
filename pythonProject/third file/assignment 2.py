#
# try:
#     while True:
#         filename = input("enter file name: ")
#         Q = open(filename, "r")
#         lineNumber = Q.readline()
#         line = len(lineNumber)
#
#
#         print(line)
#
#
# except FileNotFoundError:
#         if filename == "NA NA BOO BOO":
#             print("NA NA BOO BOO TO YOU - you have been a punk")
#

while True:
    try:
        filename = input("Enter filename: ")

        if filename == 'na na boo boo':
            print("NA  NA BOO  BOO TO YOU - you have been a punk'd")
            exit(0)

        file = open(filename,"r")

        linenumber =0

        for line in file:
            linenumber += 1

        print(linenumber)

    except FileNotFoundError:
        print("invalid input")