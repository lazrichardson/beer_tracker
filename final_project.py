"""
Command line beer tracker

## Key Project requirements
TODO: Try blocks
TODO: Provide unit tests that prove that your class methods work;
TODO: Evaluate results using assert statements.
TODO: at least 1 private and 1 public method that take arguments, return values and are used by your program
"""
import Beer
escape = "E"
user_input = ""

while user_input != escape:
    user_input = input("\nEnter a selection..."
                       "\n1 to input a new beer"
                       "\n2 to input data from a file"
                       "\n3 to see top beers by a specific style"
                       "\n4 to search for a beer by name"
                       "\n5 to see the top beers overall"
                       "\nE to exit\n...\n")
    # manually add a beer
    if user_input == '1':
        beer_list.append(Beer.Beer())
        print("New beer added...")

    # input from a file
    elif user_input == '2':


    # top beers in a selected style
    elif user_input == '3':
        user_input = input("Input a beer style: ")
        Beer.top_beers(beer_list, user_input, None)

    # top beer by a name you input
    elif user_input == '4':
        beer_search = input("Search for a beer by name:")
        Beer.top_beers(beer_list, None, beer_search)

    # top rated beers overall
    elif user_input == '5':
        print(beer_list)

    # escape
    elif user_input == "E":
        print("Goodbye!...")
        break

print(beer_list)
