#x = input("What's x? ")
#y = input("What's y? ")

#z = int(x) + int(y)

#print(z)

# Nesting functions to solve the same problem.
# consider that the user can only enter base 10 values, meaning no decimal points.
#x = int(input("What's x? "))
#y = int(input("What's y? "))

# float, it is a number that has decimal values
x = float(input("What is x? "))
y = float(input("What is y? "))

# perform some divisions
z = x / y

# perform a division and also round the number up to 2 decimal places
#z = round(x / y, 2)

# same problems as before, but now we use an f string as a solution
print(f"{z:.2f}")

# using round
# when using the function as is, it will round up to the nearest integer (meaning, no decimal value)
#z = round(x + y)

#print(z)

# add format to larger values where it can express the use of separators, for example 1,033 instead of 1033
#print(f"{z:,}")