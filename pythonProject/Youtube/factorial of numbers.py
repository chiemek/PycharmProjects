def fact(n):
    f = 1
    for i in range(1 , n +1):  # here we used range to specify that we want the number to be from 1 to n +1. 
        f = f * 1
    return f

print(fact(5))