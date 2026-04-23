# Match cases

numbers = int(input("Enter a number\n"))
match numbers:
    case 1:
        print("You have enter 1")
    case 2:
        print("You have enter 2")
    case 3:
        print("You have enter 3")
    case 4:
        print("You have enter 4")
    case 5:
        print("You have enter 5")
    case 6:
        print("You have enter 6")
    case _:
        print("No idea")