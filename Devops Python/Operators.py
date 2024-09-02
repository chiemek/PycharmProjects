'''# Arithmetic Operators
x = 2
y = 7

Total = x + y
print(Total)

Total = x - y
print(Total)

Total = x * y
print(Total)

Total = y / x
print(Total)

Total = y ** x
print(Total)

Total = y % x
print(Total)
'''

# Comparison Operator
a = 30
b = 60

out = a < b
print(out)

out = a > b
print(out)

out = a == b
print(out)

out = a != b
print(out)

out = a >= b
print(out)

out = a <= b
print(out)


# Assignment Operators
c = 0
d = 1

c += d
print(c)

c -= d
print(c)

# Logical Operator
# and
# or
# not

a = 40
b = 60
x = 2
y = 3
out = (a < b) or (x > y)
print(out)

out = (a < b) and (x > y)
print(out)

out = (a < b) and not(x > y)
print(out)

# membership operators
first_tuple = ("Devops", 47,  1.5)
ans = "Devops" in first_tuple
print(ans)

first_tuple = ("Devops", 47,  1.5)
ans = "Devops" not in first_tuple
print(ans)

# identity operator
# is
# is not

a = 12
b = 10
result = a is b
print(result)

result = a is not b
print(result)
