"""
Command line beer tracker

## Key Project requirements
"""
import BeerList

escape = "E"  # escape character for user input
user_input = ""  # initialize placeholder for user input
beer_list = BeerList.BeerList()  # initialize a beer list

print(
    '''
      o©ºº©oo©oº°©           
     /      º°©   \          
     |___________ |____      
     |     B U     |___ )     
     |    CS521   |  | |     
     |   B E E R  |  | |         
     |   TRACKER  |  | |     
     |            |____)     
     |____________|          
    (______________)         
    LUTHER RICHARDSON'''
)

while user_input != escape:

    user_input = input("\nEnter a selection..."
                       "\n1 to input a new beer"
                       "\n2 to input data from a file"
                       "\n3 to see top beers of a specific style"
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
        input_ok = False
        while input_ok is False:
            try:
                file_path = input("Enter a filename (defaults path to current "
                                  "directory)")
                open(file_path)
                old_length = len(beer_list.beer_list)
                beer_list.import_data("test_data")
                new_beers = len(beer_list.beer_list) - old_length
                print("Added {:d} new beers in the tracker!".format(
                    new_beers))
                input_ok = True
            except FileNotFoundError:
                print("File not found...try again!")

    # top beers in a selected style
    elif user_input == '3':
        beer_style = input("Input a beer style: ")
        beer_list.top_beers(beer_style, "style")

    # top beer by a name you input
    elif user_input == '4':
        beer_name = input("Search for a beer by name:")
        beer_list.top_beers(beer_name, "name")

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
