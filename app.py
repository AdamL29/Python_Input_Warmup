def prompt():
    print("Welcome to the application\
        \nPlease select from the following:\
        \n1. Enter a new thought\
        \n2. Display all thoughts\
        \n3. Exit")
    # Below is used to show text in your application.
    # print("Welcome to the application")
    # print("Please select from the following:")
    # print("1. Enter a new thought")
    # print("2. Display all thoughts")
    # print("3. Exit")
    selection = input("Please enter your selection: ")
    # if selection == "test":
        # raise ZeroDivisionError (This is a manually raise exception!)
    return selection

def get_thought():
    thought = input("Please enter your thought ")
    thoughts.append(thought)

def print_thoughts():
    for thought in thoughts:
        print(thought)

def journal():
    print("Welcome to the application!")
    while True:
        try:
            selection = int(prompt())
        except ValueError:
            print("Please enter numbers only")
            continue
        # Continue jumps to the next iteration of the loop.
        if selection == 1:
            get_thought()
        elif selection == 2:
            print_thoughts()
        elif selection == 3:
            print("Goodbye")
            break
        # Break ends the loop.
        else:
            print("Your input is invalid! Please select from the displayed options.")

thoughts = []
journal()