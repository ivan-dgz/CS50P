name = input("What's your name? ")

#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")

### Solving the same problem with the match function

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

# Match function did not work for me, need to debug and understand