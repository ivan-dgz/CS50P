### This is an alternative to hello.py for unit testing practice

def main():
    name = input("What is your name? ")
    print(hello(name)) # passed the print side effect to the main function for the side effect to be printed on screen


def hello(to="world"):
    return f"Hello, {to}" # replaced print (which generates a side effect) with return (return can be tested with pytest, side effects cannot)


if __name__ == "__main__":
    main()