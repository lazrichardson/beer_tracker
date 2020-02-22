"""
Command line beer tracker

## Key Project requirements
TODO: Provide unit tests that prove that your class methods work;
TODO: Evaluate results using assert statements.
TODO: at least 1 private and 1 public method that take arguments, return values and are used by your program
"""
import Beer
import BeerList

escape = "E"
user_input = ""
beer_list = BeerList.BeerList()  # initialize a beer list

while user_input != escape:

    user_input = input("\nEnter a selection..."
                       "\n1 to input a new beer"
                       "\n2 to input data from a file"
                       "\n3 to see top beers by a specific style"
                       "\n4 to search for a beer by name"
                       "\n5 to see the top beers overall"
                       "\n6 to export data to file"
                       "\nE to exit\n...\n")
    # manually add a beer
    if user_input == '1':
        beer_list.add_beer()
        print("New beer added...")

    # input from a file
    elif user_input == '2':
        # TODO: add input of file name
        beer_list.import_data("test_data")

    # top beers in a selected style
    elif user_input == '3':
        beer_style = input("Input a beer style: ")
        beer_list.top_beers(beer_style,"style")

    # top beer by a name you input
    elif user_input == '4':
        beer_name = input("Search for a beer by name:")
        beer_list.top_beers(beer_name,"name")

    # top rated beers overall
    elif user_input == '5':
        beer_list.top_beers_by_rating()

    # export data to file
    elif user_input == '6':
        beer_list.export_data()

    # escape
    elif user_input == "E":
        print("Goodbye!...")
        break

    # error msg
    else:
        print("That's not a valid input...try again!")

