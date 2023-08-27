# Ask user for their name, and store it as a variable
#name = input("What's yout name? ")

## Ask user for theri name, and store value, remove whitespace and capitalize each word within the captured string.
name = input("What's your name? ").strip().title()

# Remocing whitespace from str (from whenever a user accidentaly types spaces when inputing data to the variable)
#name = name.strip()

# Capitalize user's name
# this will onlt capitalize the first character on the string
#name = name.capitalize()

# Capitalize first characater on each word on a string
#name = name.title()

# Combining solutions, remove whitespace and capitalizing each word
#name = name.strip().title()

# Split user's name into first name and last name
first, last = name.split(" ")

## Say hello to user while returning the value stored in the name variable

# Concatenating a string with an argument
# in theory, this returns the value of one single argument, as the data was concatened to become a single output
print("Hello, " + name)

# Printing two arguments
print("Hello,", name)

# change the printing behaviour to structure the code in a different layout
print("Hello, ", end = "") # changed the behaviour of the end parameter to not create a new line, hence concatinating both prints when run
print(name)

# another way of solving the same problem
print(f"Hello, {name}") # added curly braces around the argument i want to pass down while adding an "f" before the quotes to indicate that this string has a special format.

# Say hello to user while only using the first name
print(f"Hello, {first}")