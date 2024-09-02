s = 'Hello World'
print(s[::-1])
p = 1.234

# strings are immutable
# print formatting
print("place this here : %s" %s)   # this is not for float
print("float should be %1.3f" %p)  # this is for float, the 3behind the dot shows how many decimal places we want
print("first %s, second %s, third %s"  %("emeka", 1995, 102))