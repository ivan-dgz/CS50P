### Is this number even or odd
#x = int(input("What is x? "))

#if x % 2 == 0:
#    print("Even")
#else:
#    print("Odd")

### Define our parity function

def main():
    x = int(input("What is x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(n):
    if n % 2 == 0:
        return bool

# another way of solving the same problem    
#def is_even(n):
#    return n % 2 == 0

main()