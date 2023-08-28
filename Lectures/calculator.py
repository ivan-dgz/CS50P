### Implementing calculator with the standard practice of defining main
def main():
    x = int(input("What is x? ")) # created a variable to ask the user for an "x" value
    print("x squared is", square(x)) # this will print the string "x squared is" followed by the number entered by the user, that also passed through the function called square


def square(n): # defined a function that requires an argument called "n"
    return n * n # this will return to the function the product of "n" times "n"
# alternatively, you can also use
# return pow(n, 2)
# or
# return ** 2


main()


### All notes below, were the original text before previous text was added.

#x = input("What's x? ")
#y = input("What's y? ")

#z = int(x) + int(y)

#print(z)

# Nesting functions to solve the same problem.
# consider that the user can only enter base 10 values, meaning no decimal points.
#x = int(input("What's x? "))
#y = int(input("What's y? "))

# float, it is a number that has decimal values
#x = float(input("What is x? "))
#y = float(input("What is y? "))

# perform some divisions
#z = x / y

# perform a division and also round the number up to 2 decimal places
#z = round(x / y, 2)

# same problems as before, but now we use an f string as a solution
#print(f"{z:.2f}")

# using round
# when using the function as is, it will round up to the nearest integer (meaning, no decimal value)
#z = round(x + y)

#print(z)

# add format to larger values where it can express the use of separators, for example 1,033 instead of 1033
#print(f"{z:,}")