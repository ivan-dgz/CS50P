# Create a function that says hello
# to create a function, we need to define it.
#def hello(to = "world"): # also defined a parameter "to", the fucntion will need this to work
#    print("hello,", to) # this passes the argument captured in "to" and will be part of the printed string

#hello()
#name = input("What's your name? ") # a variable "name" will be asked to the user
#hello(name) # this indicates that the argument "name" will be pased to the parameter "to" and executing the function on the captured argument.

# A way to organize a file is to send the functions we created to the bottom of the text.
# this is done so we can focus on the body of the code
# however, the interpreter reads the code from top to bottom, so it would need to "exist" on the top of the file.
# Hence why the following convention is used at the top of the file
def main():
    name = input("What's your name? ")
    hello(name)
# main defines the function that we are creating "hello", as well as the variable for the parameter that the function hello needs "to"
# this will be at the top of the file
# note that the variables that are defined within a function can only be used within that same function.


# in this space you can code


# all the way at the bottom of the file we can define the function hello
def hello(to = "world"):
    print("Hello,", to)

# below the definition of the hello function we need to make the call to execute main, otherwise hello function will not run.
main()